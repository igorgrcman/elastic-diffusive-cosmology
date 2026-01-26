#!/usr/bin/env python3
"""
OPEN-22-4b: Physical μ-Sweep for Domain Wall Potential

================================================================================
ARTIFACT CLASSIFICATION: CONDITIONAL [Dc]
================================================================================

Sprint Goal: Produce robust μ-sweep in the PHYSICAL regime μ ∈ [13, 17]
with the derived domain-wall potential V_L = M² - M'.

This upgrades OPEN-22-4 by:
1. Using corrected μ-window [13, 17] from OPR-21R (shape-dependent)
2. Sweeping over κ (Robin BC parameter) and ρ (Δ/ℓ ratio)
3. Running convergence checks at multiple grid resolutions
4. Generating stable tables for x₁, |f₁(0)|², G_eff, N_bound

EPISTEMIC STATUS:
    V(ξ) structure: [Dc] derived from 5D Dirac equation (OPR-21)
    μ₃ window:      [Dc] shape-dependent, [13, 17] for domain wall
    Parameters:     [P] postulated (σ, Δ, ℓ, y, g₅)

NO-SMUGGLING CERTIFICATION:
    NOT used: M_W, M_Z, G_F, v=246GeV, sin²θ_W, α(M_Z), PMNS/CKM, τ_n, CODATA

================================================================================

Outputs:
    code/output/open22_4b_mu_sweep.json
    code/output/open22_4b_mu_sweep_table.md
    code/output/open22_4b_convergence_check.json

Author: EDC Book 2 OPEN-22-4b Sprint
Date: 2026-01-25
"""

import json
import numpy as np
from pathlib import Path
from typing import Dict, Any, List, Tuple
from datetime import datetime
import warnings

# =============================================================================
# CONSTANTS
# =============================================================================

# Sprint identification
SPRINT_ID = "OPEN-22-4b"
DATE = datetime.now().strftime("%Y-%m-%d")

# Physical μ-window for domain wall (from OPR-21R)
MU_WINDOW_PHYSICAL = (13, 17)  # [Dc] shape-dependent

# Unit conversion: 1 fm = 5.0677 GeV^-1
FM_TO_GEV_INV = 5.0677


# =============================================================================
# DERIVED: V_eff from 5D Dirac Equation [Dc]
# =============================================================================

def V_eff_domain_wall(
    xi: np.ndarray,
    ell: float,
    M0: float,
    Delta: float,
    kappa: float = 0.0,
    chirality: str = 'L'
) -> np.ndarray:
    """
    Effective potential from domain wall mass profile.

    DERIVATION STATUS: [Dc] Conditional
        Structure derived from 5D Dirac equation (OPR-21 L2)
        This is the CANONICAL PHYSICAL POTENTIAL for Book 2.

    M(xi) = M0 tanh((xi - ell/2)/Delta)

    For flat space (A = 0):
        V_L(xi) = M(xi)² - M'(xi)
        V_R(xi) = M(xi)² + M'(xi)

    Parameters:
        xi: position array
        ell: domain size
        M0: bulk mass amplitude
        Delta: domain wall width
        kappa: NOT used in potential, only in BCs (kept for interface consistency)
        chirality: 'L' (left-handed, physical) or 'R' (right-handed)

    Returns:
        V(xi) array
    """
    zeta = (xi - ell / 2) / Delta
    zeta_clipped = np.clip(zeta, -20, 20)  # Prevent overflow

    sech2 = 1.0 / np.cosh(zeta_clipped)**2
    tanh_val = np.tanh(zeta_clipped)

    V_mass_sq = M0**2 * tanh_val**2
    M_prime = (M0 / Delta) * sech2

    if chirality == 'L':
        return V_mass_sq - M_prime
    else:
        return V_mass_sq + M_prime


# =============================================================================
# DERIVED: M0 from sigma via OPR-01 [Dc]
# =============================================================================

def M0_from_sigma_Delta(sigma: float, Delta: float, y: float = 1.0) -> float:
    """
    Compute M0 from membrane tension and domain wall width.

    DERIVATION STATUS: [Dc] from OPR-01 Lemma 4

    M0² = (3/4) y² σ Δ
    M0 = (√3/2) y √(σΔ) ≈ 0.866 y √(σΔ)
    """
    M0_squared = (3.0 / 4.0) * y**2 * sigma * Delta
    return np.sqrt(M0_squared)


def sigma_from_M0_Delta(M0: float, Delta: float, y: float = 1.0) -> float:
    """
    Inverse of M0 formula: compute σ from M0.

    σ = 4 M0² / (3 y² Δ)
    """
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

    BCs: Robin form
        f'(0) + κ_L f(0) = 0
        f'(ℓ) - κ_R f(ℓ) = 0

    Special cases:
        κ = 0: Neumann (∂f = 0, no flux)
        κ → ∞: Dirichlet (f = 0, hard wall)

    Uses "half-cell" approach for Neumann BC (validated in OPEN-22-1).

    Returns:
        eigenvalues: Array of first n_states eigenvalues
        eigenvectors: Unit-normalized eigenfunctions (∫|f̃|²dξ = 1)
    """
    N = len(xi)
    h = xi[1] - xi[0]

    # Build Hamiltonian: H = -d²/dξ² + V(ξ)
    diag = 2.0 / h**2 + V
    off_diag = -np.ones(N - 1) / h**2

    H = np.diag(diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)

    # Boundary conditions
    if kappa_left == 0:
        # Neumann: half-cell approach
        H[0, 0] = 1.0 / h**2 + V[0]
    else:
        # Robin: add κ/h to corner
        H[0, 0] += kappa_left / h

    if kappa_right == 0:
        H[-1, -1] = 1.0 / h**2 + V[-1]
    else:
        H[-1, -1] += kappa_right / h

    # Solve eigenvalue problem
    eigenvalues, eigenvectors = np.linalg.eigh(H)

    # Unit normalize: ∫|f̃|²dξ = 1
    for i in range(min(n_states, len(eigenvalues))):
        norm_sq = np.trapezoid(eigenvectors[:, i]**2, xi)
        if norm_sq > 1e-10:
            eigenvectors[:, i] /= np.sqrt(norm_sq)

    return eigenvalues[:n_states], eigenvectors[:, :n_states]


# =============================================================================
# Mode Analysis
# =============================================================================

def analyze_modes(
    eigenvalues: np.ndarray,
    eigenvectors: np.ndarray,
    xi: np.ndarray,
    ell: float,
    M0: float,
    kappa_left: float = 0.0
) -> Dict[str, Any]:
    """
    Analyze BVP modes: count bound states, extract x₁, |f₁(0)|².

    Returns comprehensive mode analysis dict.
    """
    V_asymptotic = M0**2  # Threshold for bound states
    n_bound = int(np.sum(eigenvalues < V_asymptotic))

    # Identify first massive mode index
    # For Neumann (κ=0): mode 0 is zero mode, mode 1 is first massive
    # For Robin (κ>0): mode 0 is already massive
    if kappa_left == 0:
        first_massive_idx = 1
    else:
        first_massive_idx = 0

    result = {
        'n_bound': n_bound,
        'V_asymptotic': float(V_asymptotic),
        'first_massive_idx': first_massive_idx,
        'all_eigenvalues': [float(e) for e in eigenvalues[:min(8, len(eigenvalues))]],
    }

    # Extract first massive mode data
    if first_massive_idx < len(eigenvalues):
        lambda_1 = eigenvalues[first_massive_idx]
        f_unit = eigenvectors[:, first_massive_idx]

        # Brane amplitude at ξ = 0
        f1_tilde_at_0 = f_unit[0]
        f1_tilde_at_0_sq = f1_tilde_at_0**2

        # Convert to natural normalization: f = f̃√ℓ
        f1_at_0 = f1_tilde_at_0 * np.sqrt(ell)
        f1_at_0_sq = f1_tilde_at_0_sq * ell

        # Dimensionless eigenvalue x₁ = √λ₁ × ℓ
        if lambda_1 > 0:
            x1 = np.sqrt(lambda_1) * ell
        else:
            x1 = 0.0  # Negative eigenvalue (shouldn't happen for bound)

        result.update({
            'lambda_1': float(lambda_1),
            'x1': float(x1),
            'm1': float(x1 / ell) if ell > 0 else np.nan,
            'f1_at_0_unit': float(f1_tilde_at_0),
            'f1_at_0_squared_unit': float(f1_tilde_at_0_sq),
            'f1_at_0_natural': float(f1_at_0),
            'f1_at_0_squared_natural': float(f1_at_0_sq),
        })
    else:
        result.update({
            'lambda_1': np.nan,
            'x1': np.nan,
            'm1': np.nan,
            'f1_at_0_unit': np.nan,
            'f1_at_0_squared_unit': np.nan,
            'f1_at_0_natural': np.nan,
            'f1_at_0_squared_natural': np.nan,
        })

    return result


def compute_Geff_normalized(f1_sq: float, x1: float) -> float:
    """
    Compute G_eff / (g₅²ℓ) — the dimensionless factor.

    G_eff = g₅²ℓ |f₁(0)|² / (2 x₁²)
    G_eff / (g₅²ℓ) = |f₁(0)|² / (2 x₁²)

    Parameters:
        f1_sq: |f₁(0)|² in natural normalization
        x1: dimensionless eigenvalue

    Returns:
        G_eff / (g₅²ℓ) [dimensionless]
    """
    if x1 > 0:
        return f1_sq / (2.0 * x1**2)
    else:
        return np.nan


# =============================================================================
# Main Sweep Functions
# =============================================================================

def run_single_point(
    mu: float,
    kappa: float,
    rho: float,
    N_grid: int = 2000,
    y: float = 1.0
) -> Dict[str, Any]:
    """
    Run BVP for single (μ, κ, ρ) point.

    Parameters:
        mu: dimensionless parameter μ = M₀ℓ
        kappa: Robin BC parameter (0 = Neumann)
        rho: ratio ρ = Δ/ℓ
        N_grid: number of grid points
        y: Yukawa coupling [P]

    Returns:
        Dict with all computed quantities
    """
    # Derive geometry from (μ, ρ)
    # Set ℓ = 1 as reference scale, then Δ = ρ×ℓ = ρ
    ell = 1.0
    Delta = rho * ell

    # From μ = M₀ℓ with ℓ = 1: M₀ = μ
    M0 = mu / ell

    # Compute corresponding σ from OPR-01 inverse
    sigma = sigma_from_M0_Delta(M0, Delta, y)
    sigma_Delta_cubed = sigma * Delta**3

    # Build grid
    xi = np.linspace(0, ell, N_grid)

    # Domain wall potential [Dc]
    V = V_eff_domain_wall(xi, ell, M0, Delta, chirality='L')

    # Solve BVP with Robin BC (same κ on both boundaries)
    eigenvalues, eigenvectors = solve_bvp_robin(
        V, xi, kappa_left=kappa, kappa_right=kappa, n_states=10
    )

    # Analyze modes
    mode_data = analyze_modes(eigenvalues, eigenvectors, xi, ell, M0, kappa)

    # Compute G_eff normalized
    x1 = mode_data.get('x1', np.nan)
    f1_sq = mode_data.get('f1_at_0_squared_natural', np.nan)
    Geff_norm = compute_Geff_normalized(f1_sq, x1)

    return {
        # Input parameters
        'mu': float(mu),
        'kappa': float(kappa),
        'rho': float(rho),
        'N_grid': N_grid,
        'y': float(y),

        # Derived geometry
        'ell': float(ell),
        'Delta': float(Delta),
        'M0': float(M0),
        'sigma': float(sigma),
        'sigma_Delta_cubed': float(sigma_Delta_cubed),

        # Mode results
        'n_bound': mode_data['n_bound'],
        'x1': float(x1),
        'f1_at_0_squared': float(f1_sq),
        'Geff_over_g5sq_ell': float(Geff_norm),

        # Regime classification
        'regime': 'N=3 TARGET' if mode_data['n_bound'] == 3 else f"N={mode_data['n_bound']}",
        'in_physical_window': MU_WINDOW_PHYSICAL[0] <= mu <= MU_WINDOW_PHYSICAL[1],

        # Full mode data for diagnostics
        'mode_data': mode_data,
    }


def run_mu_sweep(
    mu_values: List[float],
    kappa_values: List[float],
    rho_values: List[float],
    N_grid: int = 2000,
    y: float = 1.0,
    verbose: bool = True
) -> List[Dict[str, Any]]:
    """
    Full sweep over (μ, κ, ρ) parameter space.

    Returns list of results for all combinations.
    """
    results = []
    total = len(mu_values) * len(kappa_values) * len(rho_values)
    count = 0

    for mu in mu_values:
        for kappa in kappa_values:
            for rho in rho_values:
                count += 1
                if verbose and count % 20 == 0:
                    print(f"   Progress: {count}/{total}...")

                try:
                    result = run_single_point(mu, kappa, rho, N_grid, y)
                    result['status'] = 'OK'
                except Exception as e:
                    result = {
                        'mu': mu, 'kappa': kappa, 'rho': rho,
                        'status': 'ERROR', 'error': str(e)
                    }

                results.append(result)

    return results


def run_convergence_check(
    mu_test: float,
    kappa_test: float,
    rho_test: float,
    grid_sizes: List[int],
    y: float = 1.0
) -> Dict[str, Any]:
    """
    Check convergence by running same point at different grid resolutions.

    Returns convergence analysis including relative changes.
    """
    results = []
    for N_grid in grid_sizes:
        r = run_single_point(mu_test, kappa_test, rho_test, N_grid, y)
        results.append({
            'N_grid': N_grid,
            'x1': r['x1'],
            'f1_at_0_squared': r['f1_at_0_squared'],
            'Geff_over_g5sq_ell': r['Geff_over_g5sq_ell'],
            'n_bound': r['n_bound'],
        })

    # Compute relative changes between consecutive grid sizes
    rel_changes = []
    for i in range(1, len(results)):
        prev, curr = results[i-1], results[i]
        if prev['x1'] > 0 and curr['x1'] > 0:
            rel_x1 = abs(curr['x1'] - prev['x1']) / prev['x1']
            rel_f1 = abs(curr['f1_at_0_squared'] - prev['f1_at_0_squared']) / max(prev['f1_at_0_squared'], 1e-10)
            rel_Geff = abs(curr['Geff_over_g5sq_ell'] - prev['Geff_over_g5sq_ell']) / max(prev['Geff_over_g5sq_ell'], 1e-10)
        else:
            rel_x1 = rel_f1 = rel_Geff = np.nan

        rel_changes.append({
            'from_N': prev['N_grid'],
            'to_N': curr['N_grid'],
            'rel_change_x1': float(rel_x1),
            'rel_change_f1_sq': float(rel_f1),
            'rel_change_Geff': float(rel_Geff),
        })

    # Final convergence assessment
    final_rel = rel_changes[-1] if rel_changes else {}
    converged = all(
        not np.isnan(final_rel.get(k, np.nan)) and final_rel.get(k, 1.0) < 0.01
        for k in ['rel_change_x1', 'rel_change_f1_sq', 'rel_change_Geff']
    )

    return {
        'test_point': {'mu': mu_test, 'kappa': kappa_test, 'rho': rho_test},
        'grid_sizes': grid_sizes,
        'results': results,
        'relative_changes': rel_changes,
        'converged': converged,
        'convergence_threshold': 0.01,  # 1%
    }


# =============================================================================
# Output Writers
# =============================================================================

def write_sweep_table(results: List[Dict], filepath: Path) -> None:
    """Write sweep results as markdown table."""
    lines = [
        f"# OPEN-22-4b: Physical μ-Sweep Results",
        "",
        f"**Status**: CONDITIONAL [Dc]",
        f"**Date**: {DATE}",
        f"**μ-window (physical)**: [{MU_WINDOW_PHYSICAL[0]}, {MU_WINDOW_PHYSICAL[1]}]",
        "",
        "## Canonical Physical Path",
        "",
        "- **Potential**: V_L = M² - M' (domain wall) [Dc]",
        "- **Source**: OPR-21 L2 (5D Dirac reduction)",
        "- **μ-window**: [13, 17] (shape-dependent, NOT universal)",
        "",
        "## Sweep Results",
        "",
        "| μ | κ | ρ | N_bound | x₁ | |f₁(0)|² | G_eff/(g₅²ℓ) | σΔ³ | Regime |",
        "|---|---|---|---------|-----|---------|--------------|-----|--------|"
    ]

    for r in results:
        if r.get('status') == 'ERROR':
            continue
        mu = r.get('mu', np.nan)
        kappa = r.get('kappa', np.nan)
        rho = r.get('rho', np.nan)
        n_bound = r.get('n_bound', '?')
        x1 = r.get('x1', np.nan)
        f1_sq = r.get('f1_at_0_squared', np.nan)
        Geff = r.get('Geff_over_g5sq_ell', np.nan)
        sigma_Delta3 = r.get('sigma_Delta_cubed', np.nan)
        regime = r.get('regime', '')

        # Highlight N=3 rows
        marker = "**" if n_bound == 3 else ""

        lines.append(
            f"| {marker}{mu:.1f}{marker} | {kappa:.1f} | {rho:.2f} | {marker}{n_bound}{marker} | "
            f"{x1:.4f} | {f1_sq:.4f} | {Geff:.6f} | {sigma_Delta3:.2f} | {regime} |"
        )

    lines.extend([
        "",
        "## Key Formulas",
        "",
        "- **V(ξ)**: V_L = M² - M' [Dc] from 5D Dirac (OPR-21)",
        "- **M₀**: M₀² = (3/4)y²σΔ [Dc] from OPR-01",
        "- **μ**: μ = M₀ℓ (dimensionless) — **NOT M₀Δ**",
        "- **ρ**: ρ = Δ/ℓ (ratio)",
        "- **x₁**: First massive mode eigenvalue (dimensionless)",
        "- **|f₁(0)|²**: Brane amplitude (natural normalization)",
        "- **G_eff**: G_eff = g₅²ℓ|f₁(0)|²/(2x₁²)",
        "",
        "## No-Smuggling Certification",
        "",
        "NOT used as inputs: M_W, M_Z, G_F, v=246GeV, sin²θ_W, α(M_Z), PMNS/CKM, τ_n",
        "",
        f"*Generated by open22_4b_mu_sweep_physical.py on {DATE}*"
    ])

    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))


def extract_N3_summary(results: List[Dict]) -> Dict[str, Any]:
    """Extract summary statistics for N_bound = 3 regime."""
    n3_results = [r for r in results if r.get('n_bound') == 3 and r.get('status') != 'ERROR']

    if not n3_results:
        return {'achieved': False, 'count': 0}

    mu_vals = [r['mu'] for r in n3_results]
    x1_vals = [r['x1'] for r in n3_results]
    f1_sq_vals = [r['f1_at_0_squared'] for r in n3_results]
    Geff_vals = [r['Geff_over_g5sq_ell'] for r in n3_results]

    return {
        'achieved': True,
        'count': len(n3_results),
        'mu_range': [min(mu_vals), max(mu_vals)],
        'x1_range': [min(x1_vals), max(x1_vals)],
        'f1_sq_range': [min(f1_sq_vals), max(f1_sq_vals)],
        'Geff_range': [min(Geff_vals), max(Geff_vals)],
        'x1_mean': float(np.mean(x1_vals)),
        'f1_sq_mean': float(np.mean(f1_sq_vals)),
        'Geff_mean': float(np.mean(Geff_vals)),
    }


# =============================================================================
# Main
# =============================================================================

def main():
    print("=" * 70)
    print("OPEN-22-4b: Physical μ-Sweep for Domain Wall Potential")
    print("=" * 70)
    print()
    print("CLASSIFICATION: CONDITIONAL [Dc]")
    print("  Potential:  V_L = M² - M' (domain wall) [Dc]")
    print("  μ-window:   [13, 17] (shape-dependent, from OPR-21R)")
    print("  Parameters: σ, Δ, ℓ, y, g₅ remain [P] postulated")
    print()

    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)

    # =========================================================================
    # SWEEP PARAMETERS (from user specification)
    # =========================================================================
    # μ ∈ [13, 17] — physical domain wall window
    mu_values = [13.0, 14.0, 15.0, 16.0, 17.0]

    # κ ∈ {0, 0.5, 1, 2} — Robin BC parameter
    kappa_values = [0.0, 0.5, 1.0, 2.0]

    # ρ = Δ/ℓ ∈ {0.05, 0.1, 0.2}
    rho_values = [0.05, 0.1, 0.2]

    # Grid resolution (baseline)
    N_grid_baseline = 2000

    print("SWEEP PARAMETERS:")
    print(f"  μ values:  {mu_values}")
    print(f"  κ values:  {kappa_values}")
    print(f"  ρ values:  {rho_values}")
    print(f"  N_grid:    {N_grid_baseline}")
    print(f"  Total configurations: {len(mu_values) * len(kappa_values) * len(rho_values)}")
    print()

    # =========================================================================
    # RUN 1: Main μ-sweep
    # =========================================================================
    print("1. Running μ-sweep...")
    sweep_results = run_mu_sweep(
        mu_values, kappa_values, rho_values,
        N_grid=N_grid_baseline, verbose=True
    )
    print(f"   Completed: {len(sweep_results)} configurations")

    # N=3 summary
    n3_summary = extract_N3_summary(sweep_results)
    if n3_summary['achieved']:
        print(f"   ✓ N_bound = 3 achieved in {n3_summary['count']} configurations")
        print(f"     μ range: [{n3_summary['mu_range'][0]:.1f}, {n3_summary['mu_range'][1]:.1f}]")
        print(f"     x₁ range: [{n3_summary['x1_range'][0]:.4f}, {n3_summary['x1_range'][1]:.4f}]")
        print(f"     |f₁(0)|² range: [{n3_summary['f1_sq_range'][0]:.4f}, {n3_summary['f1_sq_range'][1]:.4f}]")
    else:
        print("   ⚠ N_bound = 3 NOT achieved in scanned range")
    print()

    # =========================================================================
    # RUN 2: Convergence check
    # =========================================================================
    print("2. Running convergence check...")
    # Test point: middle of μ-window, Neumann BC, middle ρ
    mu_test = 15.0
    kappa_test = 0.0
    rho_test = 0.1
    grid_sizes = [500, 1000, 2000, 4000]

    convergence = run_convergence_check(mu_test, kappa_test, rho_test, grid_sizes)

    if convergence['converged']:
        print(f"   ✓ CONVERGED at N_grid = {grid_sizes[-1]}")
    else:
        print(f"   ⚠ Convergence check: threshold 1% not met")

    for rc in convergence['relative_changes']:
        print(f"     {rc['from_N']} → {rc['to_N']}: "
              f"Δx₁={rc['rel_change_x1']*100:.3f}%, "
              f"Δ|f₁|²={rc['rel_change_f1_sq']*100:.3f}%, "
              f"ΔG_eff={rc['rel_change_Geff']*100:.3f}%")
    print()

    # =========================================================================
    # WRITE OUTPUTS
    # =========================================================================
    print("3. Writing outputs...")

    # Markdown table
    table_file = output_dir / 'open22_4b_mu_sweep_table.md'
    write_sweep_table(sweep_results, table_file)
    print(f"   ✓ {table_file}")

    # Convergence JSON
    conv_file = output_dir / 'open22_4b_convergence_check.json'
    with open(conv_file, 'w') as f:
        json.dump(convergence, f, indent=2)
    print(f"   ✓ {conv_file}")

    # Full summary JSON
    summary = {
        'artifact_class': 'CONDITIONAL [Dc]',
        'sprint': SPRINT_ID,
        'date': DATE,
        'description': 'Physical μ-sweep for domain wall potential V_L = M² - M\'',

        'canonical_physical_path': {
            'potential': 'V_L = M² - M\' (domain wall)',
            'source': 'OPR-21 L2 (5D Dirac reduction)',
            'status': '[Dc] DERIVED',
            'mu_window': list(MU_WINDOW_PHYSICAL),
            'note': 'Shape-dependent window, NOT universal [25,35)'
        },

        'sweep_parameters': {
            'mu_values': mu_values,
            'kappa_values': kappa_values,
            'rho_values': rho_values,
            'N_grid': N_grid_baseline,
            'y': 1.0,
            'total_configurations': len(sweep_results)
        },

        'N_bound_3_summary': n3_summary,

        'convergence_check': {
            'test_point': convergence['test_point'],
            'grid_sizes': grid_sizes,
            'converged': convergence['converged'],
            'threshold': convergence['convergence_threshold'],
        },

        'key_results': {
            'description': 'Representative values in N=3 regime',
            'x1_mean': n3_summary.get('x1_mean'),
            'f1_sq_mean': n3_summary.get('f1_sq_mean'),
            'Geff_mean': n3_summary.get('Geff_mean'),
            'formula': 'G_eff = (g₅²ℓ) × (G_eff/(g₅²ℓ))',
        },

        'no_smuggling_certification': {
            'NOT_used': [
                'M_W', 'M_Z', 'G_F', 'v=246GeV', 'sin²θ_W',
                'α(M_Z)', 'PMNS/CKM', 'τ_n', 'CODATA'
            ],
            'status': 'PASS'
        },

        'derivation_chain': {
            'V_eff': '[Dc] from OPR-21 L2',
            'M0': '[Dc] from OPR-01 Lemma 4',
            'mu_window': '[Dc] from OPR-21R (shape-dependent)',
            'f1_extraction': '[Dc] from OPEN-22-1',
            'G_eff': '[Dc] from OPR-22 L9',
        },

        'full_sweep_results': sweep_results,

        'files_generated': [
            str(table_file),
            str(conv_file),
            str(output_dir / 'open22_4b_mu_sweep.json'),
        ]
    }

    summary_file = output_dir / 'open22_4b_mu_sweep.json'
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"   ✓ {summary_file}")

    # =========================================================================
    # FINAL SUMMARY
    # =========================================================================
    print()
    print("=" * 70)
    print("SUMMARY: OPEN-22-4b COMPLETE")
    print("=" * 70)
    print()
    print("  Canonical Physical Path:")
    print("    Potential: V_L = M² - M' (domain wall) [Dc]")
    print(f"    μ-window:  [{MU_WINDOW_PHYSICAL[0]}, {MU_WINDOW_PHYSICAL[1]}] (shape-dependent)")
    print()
    if n3_summary['achieved']:
        print("  N_bound = 3 regime (PHYSICAL):")
        print(f"    x₁ ∈ [{n3_summary['x1_range'][0]:.4f}, {n3_summary['x1_range'][1]:.4f}]")
        print(f"    |f₁(0)|² ∈ [{n3_summary['f1_sq_range'][0]:.4f}, {n3_summary['f1_sq_range'][1]:.4f}]")
        print(f"    G_eff/(g₅²ℓ) ∈ [{n3_summary['Geff_range'][0]:.6f}, {n3_summary['Geff_range'][1]:.6f}]")
    print()
    print("  Convergence: " + ("✓ PASS" if convergence['converged'] else "⚠ CHECK"))
    print()
    print("  Remaining for full closure:")
    print("    - Derive σ, Δ, ℓ, g₅ from independent physics")
    print("    - Map G_eff → G_F via normalization choice")
    print()


if __name__ == '__main__':
    main()
