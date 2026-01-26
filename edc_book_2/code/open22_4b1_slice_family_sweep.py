#!/usr/bin/env python3
"""
OPEN-22-4b.1 PATCH: Slice-Family μ-Sweep

================================================================================
ARTIFACT CLASSIFICATION: CONDITIONAL [Dc]
================================================================================

Upgrades OPEN-22-4b from "single-slice band" to "slice-family band" by:
1. Sweeping κ ∈ {0, 0.5, 1, 2} (Robin BC parameter)
2. Sweeping ρ ∈ {0.05, 0.1, 0.2} (Δ/ℓ ratio)
3. Primary μ ∈ [13, 17] + margin μ ∈ [12, 18]
4. Producing (κ, ρ)-indexed band ranges for x₁, |f₁(0)|², G_eff/(g₅²ℓ)
5. Convergence worst-case across all slices
6. Meta file with hashes and solver settings

NON-UNIVERSALITY STATEMENT:
    All band ranges are CONDITIONAL on (V_L family, κ, ρ).
    No universal claims. Different potential shapes give different windows.

NO-SMUGGLING CERTIFICATION:
    NOT used: M_W, M_Z, G_F, v=246GeV, sin²θ_W, α(M_Z), PMNS/CKM, τ_n, CODATA

================================================================================
"""

import json
import hashlib
import subprocess
import sys
import numpy as np
from pathlib import Path
from typing import Dict, Any, List, Tuple
from datetime import datetime

# =============================================================================
# CONSTANTS
# =============================================================================

SPRINT_ID = "OPEN-22-4b.1"
DATE = datetime.now().strftime("%Y-%m-%d")

# Physical μ-window (from OPR-21R)
MU_WINDOW_PHYSICAL = (13, 17)
MU_MARGIN = (12, 18)

# Sweep parameters
KAPPA_VALUES = [0.0, 0.5, 1.0, 2.0]
RHO_VALUES = [0.05, 0.10, 0.20]
MU_PRIMARY = np.arange(13.0, 17.5, 0.5).tolist()  # [13, 13.5, ..., 17]
MU_MARGIN_COARSE = [12.0, 12.5, 17.5, 18.0]  # Margin extension
MU_ALL = sorted(set(MU_PRIMARY + MU_MARGIN_COARSE))

# Solver settings
N_GRID_DEFAULT = 2000
N_GRID_CONVERGENCE = [1000, 2000, 4000]
YUKAWA_Y = 1.0


# =============================================================================
# DERIVED: V_eff from 5D Dirac Equation [Dc]
# =============================================================================

def V_eff_domain_wall(
    xi: np.ndarray,
    ell: float,
    M0: float,
    Delta: float,
    chirality: str = 'L'
) -> np.ndarray:
    """
    Effective potential from domain wall mass profile.
    V_L = M² - M' [Dc] from OPR-21 L2
    """
    zeta = (xi - ell / 2) / Delta
    zeta_clipped = np.clip(zeta, -20, 20)

    sech2 = 1.0 / np.cosh(zeta_clipped)**2
    tanh_val = np.tanh(zeta_clipped)

    V_mass_sq = M0**2 * tanh_val**2
    M_prime = (M0 / Delta) * sech2

    if chirality == 'L':
        return V_mass_sq - M_prime
    else:
        return V_mass_sq + M_prime


def sigma_from_M0_Delta(M0: float, Delta: float, y: float = 1.0) -> float:
    """σ = 4 M0² / (3 y² Δ) — inverse of OPR-01"""
    return 4.0 * M0**2 / (3.0 * y**2 * Delta)


# =============================================================================
# BVP Solver with Robin BC
# =============================================================================

def solve_bvp_robin(
    V: np.ndarray,
    xi: np.ndarray,
    kappa_left: float = 0.0,
    kappa_right: float = 0.0,
    n_states: int = 10
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Solve 1D Sturm-Liouville BVP: -f'' + V(xi)f = λf
    with Robin BC: f'(0) + κ_L f(0) = 0, f'(ℓ) - κ_R f(ℓ) = 0
    """
    N = len(xi)
    h = xi[1] - xi[0]

    diag = 2.0 / h**2 + V
    off_diag = -np.ones(N - 1) / h**2

    H = np.diag(diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)

    if kappa_left == 0:
        H[0, 0] = 1.0 / h**2 + V[0]
    else:
        H[0, 0] += kappa_left / h

    if kappa_right == 0:
        H[-1, -1] = 1.0 / h**2 + V[-1]
    else:
        H[-1, -1] += kappa_right / h

    eigenvalues, eigenvectors = np.linalg.eigh(H)

    for i in range(min(n_states, len(eigenvalues))):
        norm_sq = np.trapezoid(eigenvectors[:, i]**2, xi)
        if norm_sq > 1e-10:
            eigenvectors[:, i] /= np.sqrt(norm_sq)

    return eigenvalues[:n_states], eigenvectors[:, :n_states]


# =============================================================================
# Single Point Computation
# =============================================================================

def run_single_point(
    mu: float,
    kappa: float,
    rho: float,
    N_grid: int = N_GRID_DEFAULT,
    y: float = YUKAWA_Y
) -> Dict[str, Any]:
    """Run BVP for single (μ, κ, ρ) point."""
    ell = 1.0
    Delta = rho * ell
    M0 = mu / ell
    sigma = sigma_from_M0_Delta(M0, Delta, y)
    sigma_Delta3 = sigma * Delta**3

    xi = np.linspace(0, ell, N_grid)
    V = V_eff_domain_wall(xi, ell, M0, Delta, chirality='L')
    V_asymptotic = M0**2

    eigenvalues, eigenvectors = solve_bvp_robin(
        V, xi, kappa_left=kappa, kappa_right=kappa, n_states=10
    )

    n_bound = int(np.sum(eigenvalues < V_asymptotic))

    # First massive mode
    first_massive_idx = 1 if kappa == 0 else 0

    if first_massive_idx < len(eigenvalues):
        lambda_1 = eigenvalues[first_massive_idx]
        f_unit = eigenvectors[:, first_massive_idx]
        f1_tilde_at_0 = f_unit[0]
        f1_at_0_sq = f1_tilde_at_0**2 * ell
        x1 = np.sqrt(abs(lambda_1)) * ell if lambda_1 > 0 else 0.0
        Geff_norm = f1_at_0_sq / (2.0 * x1**2) if x1 > 0 else np.nan
    else:
        x1 = np.nan
        f1_at_0_sq = np.nan
        Geff_norm = np.nan

    return {
        'mu': float(mu),
        'kappa': float(kappa),
        'rho': float(rho),
        'N_grid': N_grid,
        'n_bound': n_bound,
        'x1': float(x1),
        'f1_at_0_squared': float(f1_at_0_sq),
        'Geff_over_g5sq_ell': float(Geff_norm),
        'sigma_Delta3': float(sigma_Delta3),
        'in_primary_window': MU_WINDOW_PHYSICAL[0] <= mu <= MU_WINDOW_PHYSICAL[1],
    }


# =============================================================================
# Slice-Family Sweep
# =============================================================================

def run_slice_family_sweep(verbose: bool = True) -> Dict[str, Any]:
    """Run full (κ, ρ, μ) sweep and organize by slices."""
    results = {}

    total = len(KAPPA_VALUES) * len(RHO_VALUES) * len(MU_ALL)
    count = 0

    for kappa in KAPPA_VALUES:
        kappa_key = f"kappa_{kappa:.1f}"
        results[kappa_key] = {}

        for rho in RHO_VALUES:
            rho_key = f"rho_{rho:.2f}"
            results[kappa_key][rho_key] = {
                'kappa': kappa,
                'rho': rho,
                'mu_grid': [],
                'points': [],
            }

            for mu in MU_ALL:
                count += 1
                if verbose and count % 20 == 0:
                    print(f"   Progress: {count}/{total}...")

                result = run_single_point(mu, kappa, rho)
                results[kappa_key][rho_key]['mu_grid'].append(mu)
                results[kappa_key][rho_key]['points'].append(result)

    return results


def extract_slice_bands(slice_data: Dict) -> Dict[str, Any]:
    """Extract band ranges from a (κ, ρ) slice over μ∈[13,17]."""
    primary_points = [p for p in slice_data['points'] if p['in_primary_window']]

    if not primary_points:
        return {'n3_achieved': False}

    n3_points = [p for p in primary_points if p['n_bound'] == 3]

    if not n3_points:
        return {
            'n3_achieved': False,
            'n_bound_values': list(set(p['n_bound'] for p in primary_points)),
        }

    x1_vals = [p['x1'] for p in n3_points if not np.isnan(p['x1'])]
    f1_vals = [p['f1_at_0_squared'] for p in n3_points if not np.isnan(p['f1_at_0_squared'])]
    Geff_vals = [p['Geff_over_g5sq_ell'] for p in n3_points if not np.isnan(p['Geff_over_g5sq_ell'])]
    mu_n3 = [p['mu'] for p in n3_points]

    return {
        'n3_achieved': True,
        'n3_count': len(n3_points),
        'mu_n3_range': [min(mu_n3), max(mu_n3)] if mu_n3 else None,
        'x1_range': [min(x1_vals), max(x1_vals)] if x1_vals else None,
        'f1_sq_range': [min(f1_vals), max(f1_vals)] if f1_vals else None,
        'Geff_range': [min(Geff_vals), max(Geff_vals)] if Geff_vals else None,
    }


# =============================================================================
# Convergence Check
# =============================================================================

def run_convergence_worstcase(verbose: bool = True) -> Dict[str, Any]:
    """Run convergence check across slices, report worst-case drift."""
    test_points = [
        {'mu': 15.0, 'kappa': 0.0, 'rho': 0.2},   # Neumann, middle
        {'mu': 14.0, 'kappa': 0.5, 'rho': 0.2},   # Robin, middle
        {'mu': 13.0, 'kappa': 0.0, 'rho': 0.1},   # Neumann, different ρ
        {'mu': 16.0, 'kappa': 1.0, 'rho': 0.2},   # Robin κ=1
    ]

    convergence_results = []
    worst_case = {'rel_x1': 0, 'rel_f1_sq': 0, 'rel_Geff': 0}

    for tp in test_points:
        if verbose:
            print(f"   Testing convergence: μ={tp['mu']}, κ={tp['kappa']}, ρ={tp['rho']}")

        results_by_grid = []
        for N_grid in N_GRID_CONVERGENCE:
            r = run_single_point(tp['mu'], tp['kappa'], tp['rho'], N_grid)
            results_by_grid.append({
                'N_grid': N_grid,
                'x1': r['x1'],
                'f1_sq': r['f1_at_0_squared'],
                'Geff': r['Geff_over_g5sq_ell'],
            })

        # Compute relative change from second-to-last to last
        prev, curr = results_by_grid[-2], results_by_grid[-1]

        if prev['x1'] > 0 and curr['x1'] > 0:
            rel_x1 = abs(curr['x1'] - prev['x1']) / prev['x1']
            rel_f1 = abs(curr['f1_sq'] - prev['f1_sq']) / max(prev['f1_sq'], 1e-10)
            rel_Geff = abs(curr['Geff'] - prev['Geff']) / max(prev['Geff'], 1e-10)
        else:
            rel_x1 = rel_f1 = rel_Geff = np.nan

        convergence_results.append({
            'test_point': tp,
            'results': results_by_grid,
            'rel_change': {
                'from_N': prev['N_grid'],
                'to_N': curr['N_grid'],
                'rel_x1': float(rel_x1),
                'rel_f1_sq': float(rel_f1),
                'rel_Geff': float(rel_Geff),
            }
        })

        # Track worst case
        if not np.isnan(rel_x1):
            worst_case['rel_x1'] = max(worst_case['rel_x1'], rel_x1)
            worst_case['rel_f1_sq'] = max(worst_case['rel_f1_sq'], rel_f1)
            worst_case['rel_Geff'] = max(worst_case['rel_Geff'], rel_Geff)

    converged = all(v < 0.01 for v in worst_case.values())

    return {
        'grid_sizes': N_GRID_CONVERGENCE,
        'test_points': convergence_results,
        'worst_case': worst_case,
        'converged': converged,
        'threshold': 0.01,
    }


# =============================================================================
# Output Writers
# =============================================================================

def compute_file_hash(filepath: Path) -> str:
    """Compute SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()


def get_git_hash() -> str:
    """Get current git commit hash."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', 'HEAD'],
            capture_output=True, text=True, cwd=Path(__file__).parent.parent
        )
        return result.stdout.strip()[:12] if result.returncode == 0 else 'unknown'
    except:
        return 'unknown'


def write_slices_table(sweep_results: Dict, filepath: Path) -> None:
    """Write slice-family results as book-ready markdown table."""
    lines = [
        f"# OPEN-22-4b.1: Slice-Family μ-Sweep Results",
        "",
        f"**Status**: CONDITIONAL [Dc]",
        f"**Date**: {DATE}",
        f"**Potential**: V_L = M² - M' (domain wall) [Dc]",
        "",
        "## NON-UNIVERSALITY STATEMENT",
        "",
        "**All band ranges are CONDITIONAL on (V_L family, κ, ρ).**",
        "Different potential shapes, boundary conditions, or wall-to-domain ratios",
        "give different numerical bands. No universal claims are made.",
        "",
        "## Slice-Family Summary (μ ∈ [13, 17])",
        "",
    ]

    for rho in RHO_VALUES:
        rho_key = f"rho_{rho:.2f}"
        lines.append(f"### ρ = {rho:.2f} (Δ/ℓ)")
        lines.append("")
        lines.append("| κ | N=3 μ-range | x₁ range | |f₁(0)|² range | G_eff/(g₅²ℓ) range |")
        lines.append("|---|-------------|----------|---------------|-------------------|")

        for kappa in KAPPA_VALUES:
            kappa_key = f"kappa_{kappa:.1f}"
            slice_data = sweep_results[kappa_key][rho_key]
            bands = extract_slice_bands(slice_data)

            kappa_label = f"{kappa:.1f}" + (" (Neumann)" if kappa == 0 else "")

            if bands['n3_achieved']:
                mu_range = f"[{bands['mu_n3_range'][0]:.1f}, {bands['mu_n3_range'][1]:.1f}]"
                x1_range = f"[{bands['x1_range'][0]:.2f}, {bands['x1_range'][1]:.2f}]" if bands['x1_range'] else "—"
                f1_range = f"[{bands['f1_sq_range'][0]:.3f}, {bands['f1_sq_range'][1]:.3f}]" if bands['f1_sq_range'] else "—"
                Geff_range = f"[{bands['Geff_range'][0]:.2e}, {bands['Geff_range'][1]:.2e}]" if bands['Geff_range'] else "—"
            else:
                mu_range = "N=3 not achieved"
                x1_range = "—"
                f1_range = "—"
                Geff_range = "—"

            lines.append(f"| {kappa_label} | {mu_range} | {x1_range} | {f1_range} | {Geff_range} |")

        lines.append("")

    lines.extend([
        "## Key Formulas",
        "",
        "- **V(ξ)**: V_L = M² - M' [Dc] from 5D Dirac (OPR-21)",
        "- **μ**: μ = M₀ℓ (dimensionless) — **NOT M₀Δ**",
        "- **κ**: Robin BC parameter (κ=0 is Neumann)",
        "- **ρ**: ρ = Δ/ℓ (wall-to-domain ratio)",
        "- **G_eff**: G_eff = g₅²ℓ|f₁(0)|²/(2x₁²)",
        "",
        "## No-Smuggling Certification",
        "",
        "NOT used as inputs: M_W, M_Z, G_F, v=246GeV, sin²θ_W, α(M_Z), PMNS/CKM, τ_n",
        "",
        f"*Generated by open22_4b1_slice_family_sweep.py on {DATE}*"
    ])

    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))


def write_meta(output_dir: Path, sweep_file: Path, table_file: Path, conv_file: Path) -> Path:
    """Write meta.json with settings and hashes."""
    meta = {
        'sprint': SPRINT_ID,
        'date': DATE,
        'git_commit': get_git_hash(),
        'python_version': sys.version,

        'solver_settings': {
            'N_grid_default': N_GRID_DEFAULT,
            'N_grid_convergence': N_GRID_CONVERGENCE,
            'eigensolver': 'numpy.linalg.eigh',
            'boundary_condition_form': "f'(0) + κf(0) = 0 (Robin)",
            'normalization': 'unit (∫|f̃|²dξ = 1)',
            'potential_family': 'V_L = M² - M\' (domain wall) [Dc]',
        },

        'sweep_parameters': {
            'kappa_values': KAPPA_VALUES,
            'rho_values': RHO_VALUES,
            'mu_primary': MU_PRIMARY,
            'mu_margin': MU_MARGIN_COARSE,
            'mu_all': MU_ALL,
            'yukawa_y': YUKAWA_Y,
        },

        'file_hashes': {
            'sweep_json': compute_file_hash(sweep_file) if sweep_file.exists() else None,
            'table_md': compute_file_hash(table_file) if table_file.exists() else None,
            'convergence_json': compute_file_hash(conv_file) if conv_file.exists() else None,
        },

        'non_universality_statement': (
            "All band ranges are CONDITIONAL on (V_L family, κ, ρ). "
            "Different potential shapes give different windows. "
            "No universal claims."
        ),

        'no_smuggling': {
            'NOT_used': ['M_W', 'M_Z', 'G_F', 'v=246GeV', 'sin²θ_W', 'α(M_Z)', 'PMNS/CKM', 'τ_n', 'CODATA'],
            'status': 'PASS',
        },
    }

    meta_file = output_dir / 'open22_4b1_meta.json'
    with open(meta_file, 'w') as f:
        json.dump(meta, f, indent=2)

    return meta_file


# =============================================================================
# Main
# =============================================================================

def main():
    print("=" * 70)
    print("OPEN-22-4b.1 PATCH: Slice-Family μ-Sweep")
    print("=" * 70)
    print()
    print("CLASSIFICATION: CONDITIONAL [Dc]")
    print("  Potential: V_L = M² - M' (domain wall) [Dc]")
    print("  NON-UNIVERSALITY: All bands conditional on (V_L, κ, ρ)")
    print()

    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)

    print("SWEEP PARAMETERS:")
    print(f"  κ values: {KAPPA_VALUES}")
    print(f"  ρ values: {RHO_VALUES}")
    print(f"  μ primary: {MU_PRIMARY}")
    print(f"  μ margin: {MU_MARGIN_COARSE}")
    print(f"  Total slices: {len(KAPPA_VALUES) * len(RHO_VALUES)}")
    print(f"  Total points: {len(KAPPA_VALUES) * len(RHO_VALUES) * len(MU_ALL)}")
    print()

    # =========================================================================
    # RUN 1: Slice-family sweep
    # =========================================================================
    print("1. Running slice-family sweep...")
    sweep_results = run_slice_family_sweep(verbose=True)
    print("   Done.")
    print()

    # Extract summary
    print("2. Extracting slice bands...")
    slice_summary = {}
    for kappa in KAPPA_VALUES:
        kappa_key = f"kappa_{kappa:.1f}"
        slice_summary[kappa_key] = {}
        for rho in RHO_VALUES:
            rho_key = f"rho_{rho:.2f}"
            bands = extract_slice_bands(sweep_results[kappa_key][rho_key])
            slice_summary[kappa_key][rho_key] = bands

            if bands['n3_achieved']:
                print(f"   κ={kappa:.1f}, ρ={rho:.2f}: N=3 in μ∈{bands['mu_n3_range']}, "
                      f"x₁∈{bands['x1_range']}")
            else:
                print(f"   κ={kappa:.1f}, ρ={rho:.2f}: N=3 NOT achieved")
    print()

    # =========================================================================
    # RUN 2: Convergence check
    # =========================================================================
    print("3. Running convergence check (worst-case across slices)...")
    convergence = run_convergence_worstcase(verbose=True)
    print(f"   Worst-case drift: x₁={convergence['worst_case']['rel_x1']*100:.3f}%, "
          f"|f₁|²={convergence['worst_case']['rel_f1_sq']*100:.3f}%, "
          f"G_eff={convergence['worst_case']['rel_Geff']*100:.3f}%")
    print(f"   Converged: {'✓ PASS' if convergence['converged'] else '⚠ FAIL'}")
    print()

    # =========================================================================
    # WRITE OUTPUTS
    # =========================================================================
    print("4. Writing outputs...")

    # Full JSON
    sweep_file = output_dir / 'open22_4b1_slices.json'
    full_output = {
        'artifact_class': 'CONDITIONAL [Dc]',
        'sprint': SPRINT_ID,
        'date': DATE,
        'potential': 'V_L = M² - M\' (domain wall)',
        'non_universality': 'All bands conditional on (V_L, κ, ρ)',
        'sweep_params': {
            'kappa': KAPPA_VALUES,
            'rho': RHO_VALUES,
            'mu_all': MU_ALL,
        },
        'slices': sweep_results,
        'slice_summary': slice_summary,
        'convergence': convergence,
    }
    with open(sweep_file, 'w') as f:
        json.dump(full_output, f, indent=2)
    print(f"   ✓ {sweep_file}")

    # Table
    table_file = output_dir / 'open22_4b1_slices_table.md'
    write_slices_table(sweep_results, table_file)
    print(f"   ✓ {table_file}")

    # Convergence JSON
    conv_file = output_dir / 'open22_4b1_convergence_worstcase.json'
    with open(conv_file, 'w') as f:
        json.dump(convergence, f, indent=2)
    print(f"   ✓ {conv_file}")

    # Meta
    meta_file = write_meta(output_dir, sweep_file, table_file, conv_file)
    print(f"   ✓ {meta_file}")
    print()

    # =========================================================================
    # FINAL SUMMARY
    # =========================================================================
    print("=" * 70)
    print("SUMMARY: OPEN-22-4b.1 COMPLETE")
    print("=" * 70)
    print()
    print("SLICE-FAMILY BANDS (μ ∈ [13, 17]):")
    print()

    # Print concise table
    print(f"{'ρ':>6} | {'κ':>10} | {'N=3 μ-range':>15} | {'x₁ range':>18} | {'|f₁(0)|² range':>18}")
    print("-" * 80)

    for rho in RHO_VALUES:
        rho_key = f"rho_{rho:.2f}"
        for kappa in KAPPA_VALUES:
            kappa_key = f"kappa_{kappa:.1f}"
            bands = slice_summary[kappa_key][rho_key]

            kappa_label = f"{kappa:.1f}" + (" (N)" if kappa == 0 else "")

            if bands['n3_achieved']:
                mu_str = f"[{bands['mu_n3_range'][0]:.1f}, {bands['mu_n3_range'][1]:.1f}]"
                x1_str = f"[{bands['x1_range'][0]:.2f}, {bands['x1_range'][1]:.2f}]" if bands['x1_range'] else "—"
                f1_str = f"[{bands['f1_sq_range'][0]:.3f}, {bands['f1_sq_range'][1]:.3f}]" if bands['f1_sq_range'] else "—"
            else:
                mu_str = "not achieved"
                x1_str = "—"
                f1_str = "—"

            print(f"{rho:>6.2f} | {kappa_label:>10} | {mu_str:>15} | {x1_str:>18} | {f1_str:>18}")

    print()
    print(f"CONVERGENCE: {'✓ PASS' if convergence['converged'] else '⚠ FAIL'} "
          f"(worst-case drift < {convergence['threshold']*100:.0f}%)")
    print()
    print("NON-UNIVERSALITY: All bands conditional on (V_L family, κ, ρ).")
    print("NO-SMUGGLING: ✓ PASS")
    print()


if __name__ == '__main__':
    main()
