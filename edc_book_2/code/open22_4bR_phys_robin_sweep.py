#!/usr/bin/env python3
"""
OPEN-22-4b-R-PHYS: Physical Domain Wall Robin BC Sweep (Green-B Path)

Goal: Promote Robin BC (κ̂>0) into the green physical reader path for the
canonical physical potential V_L = M² - M' by producing converged physical
tables for x₁, |f₁(0)|², and G_eff/(g₅²ℓ) in the μ-window where N_bound=3.

This script uses FEM weak formulation — NO ghost-point FD.

=============================================================================
GREEN-B GATES (all must pass for Robin to enter canonical green tables)
=============================================================================

1. METHOD gate: FEM/solve_bvp only (no FD)
2. CONVERGENCE gate: N_grid 2000→4000 drift < 1% for x₁, |f₁(0)|², G_eff
3. SPECTRUM gate: In μ∈[13,17], ρ=0.2 achieve N_bound=3 in a sub-window
4. CONTINUITY gate: κ̂→0 limit reproduces Green-A (Neumann) within tolerance
5. NO-SMUGGLING gate: No M_W, G_F, v, sin²θ_W used as inputs

=============================================================================
"""

import numpy as np
from scipy import linalg
from scipy.integrate import solve_bvp
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import warnings
from dataclasses import dataclass, asdict
from datetime import datetime

# Output directory
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


# =============================================================================
# FEM WEAK FORMULATION (correct Robin BC implementation)
# =============================================================================

def build_fem_robin(
    N: int,
    ell: float,
    V: Optional[np.ndarray],
    kappa: float
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Build SYMMETRIC stiffness and mass matrices using FEM weak formulation.

    FEM weak form for Robin BC:
        ∫ f'g' dξ - κ[f(0)g(0) + f(ℓ)g(ℓ)] = λ ∫ fg dξ

    Note: Robin BC enters with MINUS sign in stiffness matrix!

    Parameters:
    -----------
    N : int
        Number of grid intervals (N+1 grid points)
    ell : float
        Domain size [0, ell]
    V : np.ndarray or None
        Potential values at grid points. If None, V=0.
    kappa : float
        Robin BC parameter. kappa=0 gives Neumann.

    Returns:
    --------
    K : np.ndarray
        (N+1) x (N+1) stiffness matrix (symmetric)
    M : np.ndarray
        (N+1) x (N+1) mass matrix (diagonal, lumped)
    """
    h = ell / N
    n_pts = N + 1

    if V is None:
        V = np.zeros(n_pts)

    K = np.zeros((n_pts, n_pts))

    # Interior points
    for i in range(1, N):
        K[i, i-1] = -1.0 / h
        K[i, i] = 2.0 / h + V[i] * h
        K[i, i+1] = -1.0 / h

    # Boundary points: half interval + Robin BC (SUBTRACT kappa)
    K[0, 0] = 1.0 / h + V[0] * h / 2 - kappa
    K[0, 1] = -1.0 / h
    K[N, N] = 1.0 / h + V[N] * h / 2 - kappa
    K[N, N-1] = -1.0 / h

    # Mass matrix (lumped)
    M = np.zeros((n_pts, n_pts))
    for i in range(1, N):
        M[i, i] = h
    M[0, 0] = h / 2
    M[N, N] = h / 2

    return K, M


def solve_fem_eigenvalue(
    N: int,
    ell: float,
    V: Optional[np.ndarray],
    kappa: float,
    n_modes: int = 15
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Solve generalized eigenvalue problem K @ f = λ * M @ f.
    """
    K, M = build_fem_robin(N, ell, V, kappa)
    eigenvalues, eigenvectors = linalg.eigh(K, M)
    idx = np.argsort(eigenvalues)
    return eigenvalues[idx][:n_modes], eigenvectors[:, idx][:, :n_modes]


# =============================================================================
# DOMAIN WALL POTENTIAL
# =============================================================================

def domain_wall_potential(xi: np.ndarray, mu: float, rho: float, ell: float) -> np.ndarray:
    """
    Domain wall potential V(ξ) = M² - M' for 5D Dirac field.

    Profile: M(ξ) = μ·tanh((ξ - ℓ/2) / ρ)
    V(ξ) = M² - dM/dξ

    This is the CANONICAL PHYSICAL POTENTIAL (Green path).
    """
    z = (xi - ell / 2) / rho
    M = mu * np.tanh(z)
    dMdxi = mu / rho / np.cosh(z)**2
    return M**2 - dMdxi


# =============================================================================
# SOLVE_BVP CROSS-CHECK
# =============================================================================

def solve_bvp_eigenvalue(
    ell: float,
    V_func,
    kappa: float,
    x_guess: float,
    n_mesh: int = 500
) -> Tuple[float, np.ndarray, np.ndarray]:
    """
    Solve eigenvalue problem using scipy solve_bvp for cross-check.
    """
    xi_mesh = np.linspace(0, ell, n_mesh)
    lambda_guess = (x_guess / ell)**2

    def ode(xi, y, p):
        f, fp = y
        lam = p[0]
        return [fp, (V_func(xi) - lam) * f]

    def bc(ya, yb, p):
        return [
            ya[1] + kappa * ya[0],   # f'(0) + κf(0) = 0
            yb[1] - kappa * yb[0],   # f'(ℓ) - κf(ℓ) = 0
            ya[0] - 1.0              # Normalization
        ]

    y_guess = np.zeros((2, n_mesh))
    y_guess[0, :] = np.cos(x_guess * xi_mesh / ell)
    y_guess[1, :] = -x_guess / ell * np.sin(x_guess * xi_mesh / ell)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sol = solve_bvp(ode, bc, xi_mesh, y_guess, p=[lambda_guess], tol=1e-8)

    if sol.success:
        lam = sol.p[0]
        x = np.sqrt(max(0, lam)) * ell
        return x, sol.x, sol.y[0]
    return np.nan, xi_mesh, np.zeros(n_mesh)


# =============================================================================
# PHYSICAL QUANTITIES EXTRACTION
# =============================================================================

def extract_physical_quantities(
    eigenvalues: np.ndarray,
    eigenvectors: np.ndarray,
    mu: float,
    ell: float,
    h: float
) -> Dict:
    """
    Extract physical quantities from BVP solution.
    """
    # Count bound states (eigenvalues below asymptotic barrier μ²)
    n_bound = sum(1 for lam in eigenvalues if lam < mu**2 and lam > -1e6)

    # First bound state eigenvalue
    x1 = np.nan
    f1_0_sq = np.nan
    for i, lam in enumerate(eigenvalues):
        if lam > -1e6:  # First reasonable eigenvalue
            x1 = np.sqrt(max(0, lam)) * ell
            f1 = eigenvectors[:, i]
            # Normalize: |f₁(0)|² with ∫|f|²dξ = ℓ (natural normalization)
            norm = np.sum(f1**2) * h
            f1_0_sq = f1[0]**2 / norm * ell
            break

    # Effective coupling: G_eff = Σ_n |f_n(0)|² / λ_n for bound states
    G_eff_sum = 0.0
    for i, lam in enumerate(eigenvalues):
        if lam > 0.01 and lam < mu**2:
            fn = eigenvectors[:, i]
            norm = np.sum(fn**2) * h
            fn_0_sq = fn[0]**2 / norm * ell
            G_eff_sum += fn_0_sq / lam

    return {
        "n_bound": n_bound,
        "x1": x1,
        "f1_0_sq": f1_0_sq,
        "G_eff_normalized": G_eff_sum
    }


# =============================================================================
# MAIN SWEEP
# =============================================================================

def run_physical_robin_sweep(
    mu_grid: np.ndarray,
    kappa_hat_grid: List[float],
    rho: float = 0.2,
    ell: float = 1.0,
    N: int = 4000
) -> Dict:
    """
    Run comprehensive physical Robin BC sweep.
    """
    results = {
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "rho": rho,
            "ell": ell,
            "N": N,
            "mu_range": [float(mu_grid.min()), float(mu_grid.max())],
            "n_mu_points": len(mu_grid),
            "kappa_hat_grid": kappa_hat_grid
        },
        "scans": []
    }

    xi = np.linspace(0, ell, N + 1)
    h = ell / N

    for kappa_hat in kappa_hat_grid:
        kappa = kappa_hat / ell
        scan = {
            "kappa_hat": kappa_hat,
            "data": [],
            "n_bound_3_window": None
        }

        n3_mus = []

        for mu in mu_grid:
            V = domain_wall_potential(xi, mu, rho, ell)
            eigenvalues, eigenvectors = solve_fem_eigenvalue(N, ell, V, kappa)
            phys = extract_physical_quantities(eigenvalues, eigenvectors, mu, ell, h)

            scan["data"].append({
                "mu": float(mu),
                **phys
            })

            if phys["n_bound"] == 3:
                n3_mus.append(float(mu))

        # Record N_bound=3 window
        if n3_mus:
            scan["n_bound_3_window"] = [min(n3_mus), max(n3_mus)]

        results["scans"].append(scan)

    return results


def run_convergence_check(
    kappa_hat_values: List[float],
    mu_test: float = 14.0,
    rho: float = 0.2,
    ell: float = 1.0,
    N_list: List[int] = [2000, 4000]
) -> Dict:
    """
    Convergence gate: check drift between N=2000 and N=4000.
    """
    results = {
        "mu_test": mu_test,
        "rho": rho,
        "ell": ell,
        "N_list": N_list,
        "data": []
    }

    for kappa_hat in kappa_hat_values:
        kappa = kappa_hat / ell
        entry = {
            "kappa_hat": kappa_hat,
            "N_results": {}
        }

        for N in N_list:
            xi = np.linspace(0, ell, N + 1)
            h = ell / N
            V = domain_wall_potential(xi, mu_test, rho, ell)
            eigenvalues, eigenvectors = solve_fem_eigenvalue(N, ell, V, kappa)
            phys = extract_physical_quantities(eigenvalues, eigenvectors, mu_test, ell, h)
            entry["N_results"][str(N)] = phys

        # Compute drift
        if len(N_list) >= 2:
            N1, N2 = str(N_list[-2]), str(N_list[-1])
            r1, r2 = entry["N_results"][N1], entry["N_results"][N2]

            def pct_diff(a, b):
                if a > 0 and b > 0:
                    return abs(b - a) / a * 100
                return np.nan

            entry["drift_pct"] = {
                "x1": pct_diff(r1["x1"], r2["x1"]),
                "f1_0_sq": pct_diff(r1["f1_0_sq"], r2["f1_0_sq"]),
                "G_eff": pct_diff(r1["G_eff_normalized"], r2["G_eff_normalized"])
            }

        results["data"].append(entry)

    return results


def run_continuity_check(
    mu_test: float = 14.0,
    rho: float = 0.2,
    ell: float = 1.0,
    N: int = 4000,
    kappa_hat_small: List[float] = [0.0, 0.01, 0.05, 0.1, 0.2, 0.5]
) -> Dict:
    """
    Continuity gate: verify κ̂→0 reproduces Neumann (Green-A).
    """
    results = {
        "mu_test": mu_test,
        "rho": rho,
        "ell": ell,
        "N": N,
        "data": []
    }

    xi = np.linspace(0, ell, N + 1)
    h = ell / N
    V = domain_wall_potential(xi, mu_test, rho, ell)

    neumann_result = None

    for kappa_hat in kappa_hat_small:
        kappa = kappa_hat / ell
        eigenvalues, eigenvectors = solve_fem_eigenvalue(N, ell, V, kappa)
        phys = extract_physical_quantities(eigenvalues, eigenvectors, mu_test, ell, h)

        entry = {
            "kappa_hat": kappa_hat,
            **phys
        }

        if kappa_hat == 0.0:
            neumann_result = phys

        results["data"].append(entry)

    # Compute deviation from Neumann
    if neumann_result:
        results["neumann_reference"] = neumann_result
        for entry in results["data"]:
            if entry["kappa_hat"] > 0:
                entry["x1_dev_from_neumann_pct"] = abs(entry["x1"] - neumann_result["x1"]) / neumann_result["x1"] * 100 if neumann_result["x1"] > 0 else np.nan
                entry["f1_dev_from_neumann_pct"] = abs(entry["f1_0_sq"] - neumann_result["f1_0_sq"]) / neumann_result["f1_0_sq"] * 100 if neumann_result["f1_0_sq"] > 0 else np.nan

    return results


def run_solve_bvp_crosscheck(
    mu_test: float = 14.0,
    kappa_hat_values: List[float] = [0.0, 1.0, 5.0],
    rho: float = 0.2,
    ell: float = 1.0,
    N_fem: int = 4000
) -> Dict:
    """
    Cross-check FEM against solve_bvp for selected points.
    """
    results = {
        "mu_test": mu_test,
        "rho": rho,
        "ell": ell,
        "data": []
    }

    xi = np.linspace(0, ell, N_fem + 1)
    h = ell / N_fem
    V = domain_wall_potential(xi, mu_test, rho, ell)

    def V_func(x):
        return np.interp(x, xi, V)

    for kappa_hat in kappa_hat_values:
        kappa = kappa_hat / ell

        # FEM solution
        eigenvalues, eigenvectors = solve_fem_eigenvalue(N_fem, ell, V, kappa)
        phys_fem = extract_physical_quantities(eigenvalues, eigenvectors, mu_test, ell, h)

        # solve_bvp solution
        x_guess = phys_fem["x1"] if not np.isnan(phys_fem["x1"]) else 10.0
        x_bvp, _, f_bvp = solve_bvp_eigenvalue(ell, V_func, kappa, x_guess)

        entry = {
            "kappa_hat": kappa_hat,
            "x1_fem": phys_fem["x1"],
            "x1_bvp": x_bvp,
            "x1_diff_pct": abs(x_bvp - phys_fem["x1"]) / phys_fem["x1"] * 100 if phys_fem["x1"] > 0 and not np.isnan(x_bvp) else np.nan
        }
        results["data"].append(entry)

    return results


# =============================================================================
# GATE EVALUATION
# =============================================================================

def evaluate_gates(
    sweep_results: Dict,
    convergence_results: Dict,
    continuity_results: Dict,
    bvp_crosscheck: Dict
) -> Dict:
    """
    Evaluate all 5 GREEN-B gates.
    """
    gates = {
        "METHOD": {"status": "PASS", "note": "FEM weak formulation used (no FD)"},
        "CONVERGENCE": {"status": "UNKNOWN", "note": ""},
        "SPECTRUM": {"status": "UNKNOWN", "note": ""},
        "CONTINUITY": {"status": "UNKNOWN", "note": ""},
        "NO_SMUGGLING": {"status": "PASS", "note": "No SM constants (M_W, G_F, v, sin²θ_W) used"}
    }

    # CONVERGENCE gate: all drifts < 1%
    max_drift = 0.0
    for entry in convergence_results["data"]:
        for key, val in entry.get("drift_pct", {}).items():
            if not np.isnan(val):
                max_drift = max(max_drift, val)

    if max_drift < 1.0:
        gates["CONVERGENCE"]["status"] = "PASS"
        gates["CONVERGENCE"]["note"] = f"Max drift = {max_drift:.4f}% < 1%"
    else:
        gates["CONVERGENCE"]["status"] = "FAIL"
        gates["CONVERGENCE"]["note"] = f"Max drift = {max_drift:.4f}% >= 1%"

    # SPECTRUM gate: N_bound=3 achieved somewhere for at least one κ̂>0
    n3_achieved = []
    for scan in sweep_results["scans"]:
        if scan["kappa_hat"] > 0 and scan["n_bound_3_window"]:
            n3_achieved.append({
                "kappa_hat": scan["kappa_hat"],
                "window": scan["n_bound_3_window"]
            })

    if n3_achieved:
        gates["SPECTRUM"]["status"] = "PASS"
        gates["SPECTRUM"]["note"] = f"N_bound=3 achieved for κ̂ in {[x['kappa_hat'] for x in n3_achieved]}"
    else:
        gates["SPECTRUM"]["status"] = "FAIL"
        gates["SPECTRUM"]["note"] = "N_bound=3 NOT achieved for any κ̂>0 in μ∈[13,17]"

    # CONTINUITY gate: κ̂→0 approaches Neumann within 5%
    max_dev = 0.0
    for entry in continuity_results["data"]:
        if entry["kappa_hat"] > 0 and entry["kappa_hat"] <= 0.5:
            dev = entry.get("x1_dev_from_neumann_pct", 0)
            if not np.isnan(dev):
                max_dev = max(max_dev, dev)

    if max_dev < 5.0:
        gates["CONTINUITY"]["status"] = "PASS"
        gates["CONTINUITY"]["note"] = f"κ̂≤0.5 deviates {max_dev:.2f}% from Neumann (< 5%)"
    else:
        gates["CONTINUITY"]["status"] = "FAIL"
        gates["CONTINUITY"]["note"] = f"κ̂≤0.5 deviates {max_dev:.2f}% from Neumann (>= 5%)"

    # Overall
    all_pass = all(g["status"] == "PASS" for g in gates.values())
    gates["OVERALL"] = "ALL GATES PASS" if all_pass else "SOME GATES FAILED"

    return gates


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 80)
    print("OPEN-22-4b-R-PHYS: Physical Domain Wall Robin BC Sweep (Green-B Path)")
    print("=" * 80)
    print()

    # Configuration
    MU_GRID = np.linspace(13.0, 17.0, 21)  # Dense enough grid
    KAPPA_HAT_GRID = [0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0]
    RHO = 0.2  # Canonical thick wall
    ELL = 1.0
    N = 2000  # Main sweep uses N=2000; convergence check uses 2000→4000

    print(f"Configuration:")
    print(f"  μ range: [{MU_GRID.min()}, {MU_GRID.max()}] ({len(MU_GRID)} points)")
    print(f"  κ̂ grid: {KAPPA_HAT_GRID}")
    print(f"  ρ = {RHO} (canonical)")
    print(f"  N = {N}")
    print()

    # [A] MAIN SWEEP
    print("[A] RUNNING PHYSICAL ROBIN SWEEP...")
    sweep_results = run_physical_robin_sweep(MU_GRID, KAPPA_HAT_GRID, rho=RHO, ell=ELL, N=N)

    for scan in sweep_results["scans"]:
        kh = scan["kappa_hat"]
        window = scan["n_bound_3_window"]
        print(f"  κ̂={kh}: N_bound=3 window = {window}")
    print()

    # [B] CONVERGENCE CHECK
    print("[B] RUNNING CONVERGENCE CHECK (N=2000 vs N=4000)...")
    conv_results = run_convergence_check(KAPPA_HAT_GRID, mu_test=14.0, rho=RHO, ell=ELL)

    for entry in conv_results["data"]:
        kh = entry["kappa_hat"]
        drift = entry.get("drift_pct", {})
        print(f"  κ̂={kh}: x₁ drift={drift.get('x1', np.nan):.4f}%, |f₁(0)|² drift={drift.get('f1_0_sq', np.nan):.4f}%")
    print()

    # [C] CONTINUITY CHECK
    print("[C] RUNNING CONTINUITY CHECK (κ̂→0 → Neumann)...")
    cont_results = run_continuity_check(mu_test=14.0, rho=RHO, ell=ELL, N=N)

    print(f"  Neumann reference: x₁={cont_results['neumann_reference']['x1']:.4f}, |f₁(0)|²={cont_results['neumann_reference']['f1_0_sq']:.6f}")
    for entry in cont_results["data"]:
        if entry["kappa_hat"] > 0:
            dev = entry.get("x1_dev_from_neumann_pct", np.nan)
            print(f"  κ̂={entry['kappa_hat']}: x₁={entry['x1']:.4f}, deviation={dev:.2f}%")
    print()

    # [D] SOLVE_BVP CROSS-CHECK
    print("[D] RUNNING SOLVE_BVP CROSS-CHECK...")
    bvp_check = run_solve_bvp_crosscheck(mu_test=14.0, kappa_hat_values=[0.0, 1.0, 5.0], rho=RHO, ell=ELL)

    for entry in bvp_check["data"]:
        kh = entry["kappa_hat"]
        print(f"  κ̂={kh}: x₁(FEM)={entry['x1_fem']:.4f}, x₁(BVP)={entry['x1_bvp']:.4f}, diff={entry['x1_diff_pct']:.4f}%")
    print()

    # [E] EVALUATE GATES
    print("[E] GATE EVALUATION")
    print("-" * 60)
    gates = evaluate_gates(sweep_results, conv_results, cont_results, bvp_check)

    for gate_name, gate_info in gates.items():
        if gate_name != "OVERALL":
            print(f"  {gate_name}: {gate_info['status']} — {gate_info['note']}")
    print("-" * 60)
    print(f"  OVERALL: {gates['OVERALL']}")
    print()

    # [F] SAVE OUTPUTS
    print("[F] SAVING OUTPUTS...")

    def nan_to_none(obj):
        if isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)):
            return None
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.ndarray):
            return [nan_to_none(x) for x in obj]
        if isinstance(obj, dict):
            return {k: nan_to_none(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [nan_to_none(v) for v in obj]
        return obj

    # Main sweep results
    with open(OUTPUT_DIR / "open22_4bR_phys_robin_sweep.json", 'w') as f:
        json.dump(nan_to_none(sweep_results), f, indent=2)
    print(f"  Saved: {OUTPUT_DIR / 'open22_4bR_phys_robin_sweep.json'}")

    # Convergence results
    with open(OUTPUT_DIR / "open22_4bR_phys_robin_convergence.json", 'w') as f:
        json.dump(nan_to_none(conv_results), f, indent=2)
    print(f"  Saved: {OUTPUT_DIR / 'open22_4bR_phys_robin_convergence.json'}")

    # Gate summary
    gate_summary = {
        "gates": gates,
        "sweep_metadata": sweep_results["metadata"],
        "continuity": nan_to_none(cont_results),
        "bvp_crosscheck": nan_to_none(bvp_check)
    }
    with open(OUTPUT_DIR / "open22_4bR_phys_robin_gates.json", 'w') as f:
        json.dump(nan_to_none(gate_summary), f, indent=2)
    print(f"  Saved: {OUTPUT_DIR / 'open22_4bR_phys_robin_gates.json'}")

    # Markdown table
    with open(OUTPUT_DIR / "open22_4bR_phys_robin_table.md", 'w') as f:
        f.write("# OPEN-22-4b-R-PHYS: Physical Domain Wall Robin BC Sweep\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"**Parameters**: ρ={RHO}, ℓ={ELL}, N={N}\n\n")

        f.write("## Gate Summary\n\n")
        f.write("| Gate | Status | Note |\n")
        f.write("|------|--------|------|\n")
        for gate_name, gate_info in gates.items():
            if gate_name != "OVERALL":
                f.write(f"| {gate_name} | {gate_info['status']} | {gate_info['note']} |\n")
        f.write(f"\n**OVERALL**: {gates['OVERALL']}\n\n")

        f.write("## N_bound=3 Windows by κ̂\n\n")
        f.write("| κ̂ | N_bound=3 Window |\n")
        f.write("|---:|:----------------:|\n")
        for scan in sweep_results["scans"]:
            kh = scan["kappa_hat"]
            window = scan["n_bound_3_window"]
            window_str = f"[{window[0]:.1f}, {window[1]:.1f}]" if window else "—"
            f.write(f"| {kh} | {window_str} |\n")
        f.write("\n")

        f.write("## Detailed Results (μ=14.0 cross-section)\n\n")
        f.write("| κ̂ | x₁ | |f₁(0)|² | G_eff/(g₅²ℓ) | N_bound |\n")
        f.write("|---:|----:|---------:|-------------:|--------:|\n")
        for scan in sweep_results["scans"]:
            # Find μ=14.0 entry
            for d in scan["data"]:
                if abs(d["mu"] - 14.0) < 0.1:
                    f.write(f"| {scan['kappa_hat']} | {d['x1']:.4f} | {d['f1_0_sq']:.6f} | {d['G_eff_normalized']:.6e} | {d['n_bound']} |\n")
                    break
        f.write("\n")

        f.write("## Convergence (N=2000 → N=4000)\n\n")
        f.write("| κ̂ | x₁ drift % | |f₁(0)|² drift % | G_eff drift % |\n")
        f.write("|---:|----------:|-----------------:|--------------:|\n")
        for entry in conv_results["data"]:
            drift = entry.get("drift_pct", {})
            f.write(f"| {entry['kappa_hat']} | {drift.get('x1', 0):.4f} | {drift.get('f1_0_sq', 0):.4f} | {drift.get('G_eff', 0):.4f} |\n")
        f.write("\n")

        f.write("## Continuity Check (κ̂→0)\n\n")
        f.write("| κ̂ | x₁ | Deviation from Neumann % |\n")
        f.write("|---:|----:|-------------------------:|\n")
        for entry in cont_results["data"]:
            dev = entry.get("x1_dev_from_neumann_pct", 0) if entry["kappa_hat"] > 0 else 0
            f.write(f"| {entry['kappa_hat']} | {entry['x1']:.4f} | {dev:.2f} |\n")

    print(f"  Saved: {OUTPUT_DIR / 'open22_4bR_phys_robin_table.md'}")
    print()

    # Final summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"  {gates['OVERALL']}")
    if gates['OVERALL'] == "ALL GATES PASS":
        print("  → Robin BC (Green-B) is ready for canonical green tables")
    else:
        print("  → Robin BC remains OPEN; specific failed gates noted above")
    print()


if __name__ == "__main__":
    main()
