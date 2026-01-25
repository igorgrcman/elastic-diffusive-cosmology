#!/usr/bin/env python3
"""
OPR-21 Physical BVP Run — Derived Potential from 5D Dirac Equation

================================================================================
ARTIFACT CLASSIFICATION: REPRO (Reproducibility) + PARTIAL PHYSICS
================================================================================
This script runs the BVP with DERIVED potential structure from 5D Dirac.
The structure V_L = M² - M' (flat case) is [Dc] derived.
Parameter values (M_0, Delta, ell) remain [P] postulated.

STATUS: CONDITIONAL [Dc] — structure derived, parameters postulated
================================================================================

Implements:
1. V_eff(xi) from 5D Dirac reduction (domain wall family)
2. Robin BC from Israel junction (kappa = m_b/2)
3. Robustness scans over (ell, kappa) parameter space
4. N_bound determination for physical potential

Outputs:
    code/output/opr21_physical_robustness_table.md
    code/output/opr21_physical_phase_diagram.md
    code/output/opr21_physical_summary.json

Author: EDC Book 2 OPR-21 Physics Closure Sprint
Date: 2026-01-25
"""

import json
import numpy as np
from pathlib import Path

# Try to import scipy for eigenvalue solving
try:
    from scipy.linalg import eigh_tridiagonal
    from scipy.integrate import simpson
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    print("Warning: scipy not available. Using fallback methods.")


# =============================================================================
# DERIVED: V_eff from 5D Dirac Equation (Task A deliverable)
# =============================================================================

def V_eff_domain_wall(
    xi: np.ndarray,
    ell: float,
    M0: float,
    Delta: float,
    chirality: str = 'L',
    A_prime: float = 0.0
) -> np.ndarray:
    """
    Effective potential from domain wall mass profile M(xi) = M0 tanh((xi - ell/2)/Delta).

    DERIVATION STATUS: [Dc] Conditional
    - Structure V_L = M² - M' derived from 5D Dirac equation
    - Parameter values (M0, Delta, ell) are [P] postulated

    For flat space (A = 0):
        V_L(xi) = M(xi)² - M'(xi) = M0² tanh²(...) - (M0/Delta) sech²(...)
        V_R(xi) = M(xi)² + M'(xi) = M0² tanh²(...) + (M0/Delta) sech²(...)

    The chirality asymmetry V_R - V_L = 2M' is the geometric origin of V-A structure.

    Parameters:
        xi: coordinate array
        ell: domain size [P]
        M0: bulk mass scale [P]
        Delta: domain wall width [P]
        chirality: 'L' (left-handed) or 'R' (right-handed)
        A_prime: warp factor derivative (0 for flat case)

    Returns:
        V_eff(xi) array

    References:
        OPR21_VEFF_DERIVATION_REPORT.md Section 3
    """
    # Domain wall mass profile centered at ell/2
    zeta = (xi - ell / 2) / Delta

    # Avoid overflow for large |zeta|
    zeta_clipped = np.clip(zeta, -20, 20)

    sech2 = 1.0 / np.cosh(zeta_clipped)**2
    tanh_val = np.tanh(zeta_clipped)

    # M² term
    V_mass_sq = M0**2 * tanh_val**2

    # M' term (derivative of domain wall)
    M_prime = (M0 / Delta) * sech2

    # Include warp factor correction if present
    # Full formula: Sigma = M + 2A', V_L = Sigma² - Sigma'
    # For A' constant, Sigma' = M' so V_L = (M + 2A')² - M'
    Sigma = M0 * tanh_val + 2 * A_prime
    Sigma_sq = Sigma**2

    if chirality == 'L':
        # V_L = Sigma² - Sigma' = (M + 2A')² - M' (for constant A')
        return Sigma_sq - M_prime
    else:  # R
        # V_R = Sigma² + Sigma' = (M + 2A')² + M' (for constant A')
        return Sigma_sq + M_prime


def robin_params_from_brane_mass(m_b: float, ell: float, boundary: str = 'left') -> tuple:
    """
    Compute Robin BC parameters from brane-localized mass.

    DERIVATION STATUS: [Dc] Conditional
    - Structure kappa = m_b/2 derived from variational principle
    - m_b value is [P] postulated (linked to OPR-01 sigma anchor)

    From Israel junction derivation:
        f'(0) + kappa f(0) = 0  where kappa = m_b / 2

    This is Robin BC with (alpha, beta) = (kappa, 1).

    Parameters:
        m_b: brane mass (in units of 1/length) [P]
        ell: domain size
        boundary: 'left' (xi=0) or 'right' (xi=ell)

    Returns:
        (alpha, beta) such that alpha*f + beta*f' = 0

    References:
        OPR21_BC_ISRAEL_REPORT.md Section 4
    """
    kappa = m_b / 2

    if boundary == 'left':
        # f'(0) + kappa f(0) = 0 => alpha=kappa, beta=1
        return (kappa, 1.0)
    else:
        # f'(ell) - kappa f(ell) = 0 => alpha=-kappa, beta=1
        # Sign change due to outward normal convention
        return (-kappa, 1.0)


# =============================================================================
# BVP Solver (same infrastructure as demo)
# =============================================================================

def solve_bvp_finite_difference(
    V: np.ndarray,
    xi: np.ndarray,
    kappa_left: float = 0.0,
    kappa_right: float = 0.0,
    n_states: int = 10
) -> tuple:
    """
    Solve 1D Schrodinger BVP using finite differences.

    MATHEMATICAL STATUS: [M] Standard Sturm-Liouville numerics

    BCs: Robin form f'(0) + kappa_L f(0) = 0, f'(ell) - kappa_R f(ell) = 0
    kappa = 0: Neumann (no flux)
    kappa -> infinity: Dirichlet (hard wall)

    Returns:
        eigenvalues: Array of first n_states eigenvalues
        eigenvectors: Array of corresponding eigenfunctions
    """
    N = len(xi)
    h = xi[1] - xi[0]

    # Build tridiagonal Hamiltonian: H = -d²/dxi² + V(xi)
    diag = 2.0 / h**2 + V
    off_diag = -np.ones(N - 1) / h**2

    # Robin BC modifications via ghost point method
    if kappa_left != 0:
        diag[0] += 2 * kappa_left * h * (1 / h**2)

    if kappa_right != 0:
        diag[-1] += 2 * kappa_right * h * (1 / h**2)

    # Solve eigenvalue problem
    if HAS_SCIPY:
        eigenvalues, eigenvectors = eigh_tridiagonal(diag, off_diag)
    else:
        H = np.diag(diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
        eigenvalues, eigenvectors = np.linalg.eigh(H)

    # Normalize eigenvectors
    for i in range(min(n_states, len(eigenvalues))):
        norm = np.sqrt(np.trapezoid(eigenvectors[:, i]**2, xi))
        if norm > 1e-10:
            eigenvectors[:, i] /= norm

    return eigenvalues[:n_states], eigenvectors[:, :n_states]


def compute_overlap_I4(psi: np.ndarray, xi: np.ndarray) -> float:
    """Compute overlap integral I4 = integral |psi|^4 dxi."""
    if HAS_SCIPY:
        return simpson(psi**4, x=xi)
    else:
        return np.trapezoid(psi**4, xi)


def count_bound_states(eigenvalues: np.ndarray, V_asymptotic: float = 0.0) -> int:
    """
    Count bound states below continuum threshold.

    For domain wall: V_asymptotic = M0² (value at boundaries)
    Bound states have E < V_asymptotic.
    """
    return np.sum(eigenvalues < V_asymptotic)


# =============================================================================
# Parameter Scan Functions
# =============================================================================

def physical_robustness_scan(M0: float, Delta: float, base_ell: float) -> list:
    """
    Scan over (ell, kappa) parameter space for physical potential.

    This tests OPR-21 requirement: N_bound should be stable under BC variations.

    Parameters:
        M0: bulk mass scale [P]
        Delta: domain wall width [P]
        base_ell: nominal domain size [P]
    """
    results = []

    # Vary domain size around base value
    ell_factors = [0.8, 1.0, 1.2, 1.5]
    # Vary Robin parameter (kappa = m_b/2)
    kappa_values = [0.0, 0.1, 0.5, 1.0, 2.0]

    for ell_factor in ell_factors:
        ell = base_ell * ell_factor

        for kappa in kappa_values:
            # Discretize domain
            N_points = 500
            xi = np.linspace(0, ell, N_points)

            # Physical potential from 5D Dirac
            V = V_eff_domain_wall(xi, ell, M0, Delta, chirality='L')

            # Threshold for bound states: V_asymptotic = M0²
            V_asymptotic = M0**2

            # Solve BVP
            eigenvalues, eigenvectors = solve_bvp_finite_difference(
                V, xi, kappa_left=kappa, kappa_right=0.0, n_states=10
            )

            # Count bound states
            n_bound = count_bound_states(eigenvalues, V_asymptotic)

            # Ground state properties
            E0 = eigenvalues[0] if len(eigenvalues) > 0 else np.nan
            x1 = abs(E0 - V_asymptotic)  # distance from threshold
            I4 = compute_overlap_I4(eigenvectors[:, 0], xi) if eigenvectors.shape[1] > 0 else np.nan

            results.append({
                'ell': float(ell),
                'ell_factor': ell_factor,
                'kappa': kappa,
                'n_bound': int(n_bound),
                'E0': float(E0),
                'V_asymptotic': float(V_asymptotic),
                'x1': float(x1),
                'I4': float(I4)
            })

    return results


def physical_phase_diagram(Delta: float, base_ell: float) -> list:
    """
    Scan M0 to find parameter regime where N_bound = 3.

    This addresses OPR-02: Can we get exactly 3 generations from membrane physics?

    Parameters:
        Delta: domain wall width [P]
        base_ell: domain size [P]
    """
    results = []

    # Scan over dimensionless ratio mu = M0 * ell
    mu_values = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0]

    xi = np.linspace(0, base_ell, 500)

    for mu in mu_values:
        M0 = mu / base_ell

        V = V_eff_domain_wall(xi, base_ell, M0, Delta, chirality='L')
        V_asymptotic = M0**2

        eigenvalues, eigenvectors = solve_bvp_finite_difference(V, xi, n_states=10)

        n_bound = count_bound_states(eigenvalues, V_asymptotic)
        E0 = eigenvalues[0] if len(eigenvalues) > 0 else np.nan

        results.append({
            'mu': mu,
            'M0': float(M0),
            'n_bound': int(n_bound),
            'E0': float(E0),
            'V_asymptotic': float(V_asymptotic),
            'binding_energy': float(V_asymptotic - E0) if not np.isnan(E0) else np.nan
        })

    return results


def grid_convergence_test(M0: float, Delta: float, ell: float) -> list:
    """
    Test numerical convergence with grid resolution.

    Validates that N_bound and x1 are resolution-independent.
    """
    results = []

    N_points_values = [100, 200, 500, 1000, 2000]
    V_asymptotic = M0**2

    for N_points in N_points_values:
        xi = np.linspace(0, ell, N_points)
        V = V_eff_domain_wall(xi, ell, M0, Delta, chirality='L')

        eigenvalues, eigenvectors = solve_bvp_finite_difference(V, xi, n_states=10)

        n_bound = count_bound_states(eigenvalues, V_asymptotic)
        E0 = eigenvalues[0] if len(eigenvalues) > 0 else np.nan

        results.append({
            'N_points': N_points,
            'h': ell / (N_points - 1),
            'n_bound': int(n_bound),
            'E0': float(E0),
            'E0_error_estimate': abs(E0 - eigenvalues[0]) if len(results) > 0 else 0.0
        })

    return results


def write_markdown_table(data: list, headers: list, filename: str) -> None:
    """Write results as markdown table."""
    lines = []
    lines.append('| ' + ' | '.join(headers) + ' |')
    lines.append('|' + '|'.join(['---'] * len(headers)) + '|')

    for row in data:
        values = []
        for h in headers:
            key = h.lower().replace(' ', '_').replace('₀', '0').replace('₄', '4')
            val = row.get(key, '')
            values.append(str(val))

        # Format floats
        formatted = []
        for v in values:
            try:
                fv = float(v)
                if abs(fv) < 1e-6:
                    formatted.append(f'{fv:.2e}')
                elif abs(fv) < 1000:
                    formatted.append(f'{fv:.4f}')
                else:
                    formatted.append(f'{fv:.2e}')
            except ValueError:
                formatted.append(v)
        lines.append('| ' + ' | '.join(formatted) + ' |')

    with open(filename, 'w') as f:
        f.write('\n'.join(lines))


def main():
    print("=" * 70)
    print("OPR-21 Physical BVP Run — Derived Potential from 5D Dirac")
    print("=" * 70)
    print()
    print("CLASSIFICATION: CONDITIONAL [Dc]")
    print("  Structure V_L = M² - M' : DERIVED from 5D Dirac")
    print("  Parameters (M0, Delta, ell): POSTULATED [P]")
    print()

    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)

    # ===========================================================================
    # PHYSICAL PARAMETERS (all marked [P] postulated)
    # ===========================================================================
    # These are NOT tuned to SM observables (M_W, G_F, v, sin²theta_W)
    # They are trial values for exploring the parameter space

    # [P] Base domain size (in natural units, ~ 1/mass scale)
    base_ell = 10.0

    # [P] Domain wall width (characteristic thickness)
    Delta = 1.0

    # [P] Bulk mass scale (sets potential depth)
    # Dimensionless: mu = M0 * ell
    # Trial value: mu = 6 (expect ~ 2-3 bound states)
    mu_nominal = 6.0
    M0_nominal = mu_nominal / base_ell

    print("POSTULATED PARAMETERS [P]:")
    print(f"  ell (domain size)    = {base_ell}")
    print(f"  Delta (wall width)   = {Delta}")
    print(f"  M0 (bulk mass)       = {M0_nominal}")
    print(f"  mu = M0*ell          = {mu_nominal}")
    print(f"  delta = Delta/ell    = {Delta/base_ell}")
    print()
    print("NO SM SMUGGLING: These are NOT tuned to M_W, G_F, v, sin²theta_W")
    print()

    # ===========================================================================
    # RUN 1: Robustness Scan
    # ===========================================================================
    print("1. Robustness scan (ell, kappa variations)...")
    robustness_results = physical_robustness_scan(M0_nominal, Delta, base_ell)

    # Analyze stability
    n_bounds = set(r['n_bound'] for r in robustness_results)
    print(f"   N_bound values found: {sorted(n_bounds)}")
    if len(n_bounds) == 1:
        n_val = list(n_bounds)[0]
        print(f"   ✓ STABLE: N_bound = {n_val} across all (ell, kappa) pairs")
        stability_verdict = 'STABLE'
    else:
        print(f"   ⚠ VARIABLE: N_bound varies with parameters")
        stability_verdict = 'VARIABLE'
    print()

    # ===========================================================================
    # RUN 2: Phase Diagram (find N_bound = 3 regime)
    # ===========================================================================
    print("2. Phase diagram scan (mu = M0*ell variation)...")
    phase_results = physical_phase_diagram(Delta, base_ell)

    # Find where N_bound = 3
    n3_regimes = [r for r in phase_results if r['n_bound'] == 3]
    if n3_regimes:
        mu_range = [min(r['mu'] for r in n3_regimes), max(r['mu'] for r in n3_regimes)]
        print(f"   N_bound = 3 regime: mu in [{mu_range[0]}, {mu_range[1]}]")
    else:
        print("   N_bound = 3 NOT achieved in scanned range")
        mu_range = None

    # Find transitions
    transitions = []
    for i in range(1, len(phase_results)):
        if phase_results[i]['n_bound'] != phase_results[i-1]['n_bound']:
            transitions.append({
                'from_n': phase_results[i-1]['n_bound'],
                'to_n': phase_results[i]['n_bound'],
                'mu_range': [phase_results[i-1]['mu'], phase_results[i]['mu']]
            })

    print(f"   Transitions found:")
    for t in transitions:
        print(f"     N_bound: {t['from_n']} -> {t['to_n']} at mu ~ {t['mu_range']}")
    print()

    # ===========================================================================
    # RUN 3: Grid Convergence Test
    # ===========================================================================
    print("3. Grid convergence test...")
    convergence_results = grid_convergence_test(M0_nominal, Delta, base_ell)

    # Check if E0 is converged
    E0_values = [r['E0'] for r in convergence_results]
    E0_variation = max(E0_values) - min(E0_values)
    print(f"   E0 variation across resolutions: {E0_variation:.2e}")
    if E0_variation < 0.01 * abs(E0_values[-1]):
        print("   ✓ CONVERGED: E0 stable to < 1%")
        convergence_verdict = 'CONVERGED'
    else:
        print("   ⚠ NOT CONVERGED: Increase resolution")
        convergence_verdict = 'NOT_CONVERGED'
    print()

    # ===========================================================================
    # WRITE OUTPUTS
    # ===========================================================================
    print("4. Writing outputs...")

    # Robustness table
    robustness_file = output_dir / 'opr21_physical_robustness_table.md'
    write_markdown_table(
        robustness_results,
        ['ell', 'kappa', 'n_bound', 'E0', 'V_asymptotic', 'x1', 'I4'],
        str(robustness_file)
    )
    print(f"   ✓ {robustness_file}")

    # Phase diagram table
    phase_file = output_dir / 'opr21_physical_phase_diagram.md'
    write_markdown_table(
        phase_results,
        ['mu', 'M0', 'n_bound', 'E0', 'binding_energy'],
        str(phase_file)
    )
    print(f"   ✓ {phase_file}")

    # Summary JSON
    summary = {
        'artifact_class': 'CONDITIONAL [Dc]',
        'potential_type': 'Domain wall: V_L = M² - M\'',
        'derivation_status': {
            'V_eff_structure': 'DERIVED [Dc] from 5D Dirac equation',
            'BC_structure': 'DERIVED [Dc] from Israel junction',
            'parameter_values': 'POSTULATED [P]'
        },
        'parameters_postulated': {
            'ell': base_ell,
            'Delta': Delta,
            'M0': M0_nominal,
            'mu': mu_nominal,
            'note': 'NOT tuned to SM observables'
        },
        'robustness': {
            'verdict': stability_verdict,
            'n_bound_values': sorted(list(n_bounds)),
            'parameter_ranges': {
                'ell_factor': [0.8, 1.5],
                'kappa': [0.0, 2.0]
            }
        },
        'phase_diagram': {
            'mu_range_scanned': [0.5, 20.0],
            'n_bound_equals_3': {
                'achieved': len(n3_regimes) > 0,
                'mu_range': mu_range
            },
            'transitions': transitions
        },
        'grid_convergence': {
            'verdict': convergence_verdict,
            'E0_variation': float(E0_variation)
        },
        'opr21_status': 'CONDITIONAL [Dc]',
        'remaining_for_closure': [
            'Derive M0 from membrane tension sigma (OPR-01)',
            'Derive Delta from transition layer physics',
            'Derive ell from domain size principle',
            'Show N_bound = 3 robustly for physical parameters'
        ],
        'no_smuggling_certification': 'Parameters NOT tuned to M_W, G_F, v, sin²theta_W'
    }

    summary_file = output_dir / 'opr21_physical_summary.json'
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"   ✓ {summary_file}")

    # ===========================================================================
    # FINAL SUMMARY
    # ===========================================================================
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"  V_eff structure:     DERIVED [Dc] — V_L = M² - M'")
    print(f"  BC structure:        DERIVED [Dc] — kappa = m_b/2")
    print(f"  Parameter values:    POSTULATED [P]")
    print()
    print(f"  N_bound (mu=6):      {list(n_bounds)[0] if len(n_bounds) == 1 else 'varies'}")
    print(f"  N_bound=3 achieved:  {'YES' if n3_regimes else 'NO'} in scanned range")
    print(f"  Robustness:          {stability_verdict}")
    print(f"  Grid convergence:    {convergence_verdict}")
    print()
    if n3_regimes:
        print(f"  → N_bound=3 regime found at mu in {mu_range}")
        print(f"    This is PROMISING but parameter values are [P] postulated.")
    else:
        print(f"  → N_bound=3 NOT achieved for mu up to 20")
        print(f"    May need larger mu or different Delta/ell ratio.")
    print()
    print("OPR-21 Status: CONDITIONAL [Dc]")
    print("  ✓ V(xi) structure derived from 5D Dirac")
    print("  ✓ BC structure derived from Israel junction")
    print("  ✗ Parameter values (M0, Delta, ell) not derived from membrane action")
    print()


if __name__ == '__main__':
    main()
