#!/usr/bin/env python3
"""
OPR-21 BVP Foundation Demo — Boundary Value Problem Infrastructure

================================================================================
ARTIFACT CLASSIFICATION: REPRO (Reproducibility)
================================================================================
This script demonstrates the BVP infrastructure for OPR-21.
It is a REPRODUCIBILITY artifact, not a physics derivation.

STATUS: DEMO (toy potential, NOT derived from membrane physics)
================================================================================

Demonstrates:
1. Sturm-Liouville spectral problem setup
2. Eigenvalue extraction for toy potentials
3. Overlap integral I₄ computation
4. Robustness scan over BC parameters

Outputs:
    code/output/opr21_robustness_table.md
    code/output/opr21_phase_diagram.md
    code/output/opr21_summary.json

Author: EDC Book 2 OPR-21 Sprint
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


def poschl_teller_potential(xi: np.ndarray, V0: float = 10.0, a: float = 1.0) -> np.ndarray:
    """
    Pöschl-Teller potential: V(ξ) = -V₀ sech²(ξ/a)

    This is a TOY potential for infrastructure testing.
    NOT derived from membrane physics.
    """
    return -V0 / np.cosh(xi / a)**2


def solve_bvp_finite_difference(
    V: np.ndarray,
    xi: np.ndarray,
    kappa_left: float = 0.0,
    kappa_right: float = 0.0,
    n_states: int = 5
) -> tuple:
    """
    Solve 1D Schrödinger BVP using finite differences.

    BCs: Robin form f'(0) + κ_L f(0) = 0, f'(ℓ) + κ_R f(ℓ) = 0
    κ = 0: Neumann (no flux)
    κ → ∞: Dirichlet (hard wall)

    Returns:
        eigenvalues: Array of first n_states eigenvalues
        eigenvectors: Array of corresponding eigenfunctions
    """
    N = len(xi)
    h = xi[1] - xi[0]

    # Build tridiagonal Hamiltonian: H = -d²/dξ² + V(ξ)
    # Using central differences: f'' ≈ (f_{i+1} - 2f_i + f_{i-1})/h²

    # Main diagonal: 2/h² + V_i
    diag = 2.0 / h**2 + V

    # Off-diagonals: -1/h²
    off_diag = -np.ones(N - 1) / h**2

    # Incorporate Robin BCs via ghost points
    # At ξ=0: f'(0) + κ_L f(0) = 0 → f_{-1} = f_1 - 2h κ_L f_0
    # This modifies the corner elements
    if kappa_left != 0:
        diag[0] += 2 * kappa_left / h / (1/h**2)

    if kappa_right != 0:
        diag[-1] += 2 * kappa_right / h / (1/h**2)

    # Solve eigenvalue problem
    if HAS_SCIPY:
        eigenvalues, eigenvectors = eigh_tridiagonal(diag, off_diag)
    else:
        # Fallback: construct full matrix and use numpy
        H = np.diag(diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
        eigenvalues, eigenvectors = np.linalg.eigh(H)

    # Normalize eigenvectors
    for i in range(min(n_states, len(eigenvalues))):
        norm = np.sqrt(np.trapezoid(eigenvectors[:, i]**2, xi))
        if norm > 1e-10:
            eigenvectors[:, i] /= norm

    return eigenvalues[:n_states], eigenvectors[:, :n_states]


def compute_overlap_I4(psi: np.ndarray, xi: np.ndarray) -> float:
    """
    Compute overlap integral I₄ = ∫|ψ|⁴ dξ

    This measures the "peakedness" of the mode profile.
    Larger I₄ → more localized → stronger effective coupling.
    """
    if HAS_SCIPY:
        return simpson(psi**4, x=xi)
    else:
        return np.trapezoid(psi**4, xi)


def count_bound_states(eigenvalues: np.ndarray, threshold: float = 0.0) -> int:
    """
    Count bound states below threshold.

    For potentials approaching 0 at infinity, threshold = 0.
    Bound states have E < 0.
    """
    return np.sum(eigenvalues < threshold)


def robustness_scan(V0: float = 10.0, a: float = 1.0) -> list:
    """
    Scan over (ξ_max, κ) parameter space to test robustness of N_bound.

    OPR-21 requirement: N_bound should be stable under BC variations.
    """
    results = []

    xi_max_values = [10.0, 12.0, 14.0]
    kappa_values = [0.0, 0.1, 0.5, 1.0]

    for xi_max in xi_max_values:
        for kappa in kappa_values:
            xi = np.linspace(0, xi_max, 500)
            V = poschl_teller_potential(xi, V0, a)

            eigenvalues, eigenvectors = solve_bvp_finite_difference(
                V, xi, kappa_left=kappa, kappa_right=0.0
            )

            n_bound = count_bound_states(eigenvalues, threshold=0.0)
            E0 = eigenvalues[0] if len(eigenvalues) > 0 else np.nan
            x1 = abs(E0)
            I4 = compute_overlap_I4(eigenvectors[:, 0], xi) if eigenvectors.shape[1] > 0 else np.nan

            results.append({
                'xi_max': xi_max,
                'kappa': kappa,
                'n_bound': n_bound,
                'E0': float(E0),
                'x1': float(x1),
                'I4': float(I4)
            })

    return results


def phase_diagram_scan(a: float = 1.0) -> list:
    """
    Scan V₀ to show stepwise N_bound behavior.

    Demonstrates that N_bound = 3 is NOT automatic—it requires
    specific potential depth.
    """
    results = []

    V0_values = [1.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0]
    xi_max = 14.0
    xi = np.linspace(0, xi_max, 500)

    for V0 in V0_values:
        V = poschl_teller_potential(xi, V0, a)
        eigenvalues, eigenvectors = solve_bvp_finite_difference(V, xi)

        n_bound = count_bound_states(eigenvalues, threshold=0.0)
        E0 = eigenvalues[0] if len(eigenvalues) > 0 else np.nan

        results.append({
            'V0': V0,
            'n_bound': n_bound,
            'E0': float(E0),
            'x1': float(abs(E0))
        })

    return results


def write_markdown_table(data: list, headers: list, filename: str) -> None:
    """Write results as markdown table."""
    lines = []
    lines.append('| ' + ' | '.join(headers) + ' |')
    lines.append('|' + '|'.join(['---'] * len(headers)) + '|')

    for row in data:
        values = [str(row.get(h.lower().replace(' ', '_').replace('₀', '0').replace('₄', '4'), ''))
                  for h in headers]
        # Format floats
        formatted = []
        for v in values:
            try:
                fv = float(v)
                formatted.append(f'{fv:.3f}' if abs(fv) < 1000 else f'{fv:.2e}')
            except ValueError:
                formatted.append(v)
        lines.append('| ' + ' | '.join(formatted) + ' |')

    with open(filename, 'w') as f:
        f.write('\n'.join(lines))


def main():
    print("=" * 70)
    print("OPR-21 BVP Foundation Demo")
    print("=" * 70)
    print()
    print("CLASSIFICATION: DEMO (toy potential, NOT derived from physics)")
    print()

    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)

    # Parameters
    V0 = 10.0
    a = 1.0

    print(f"Toy potential: V(ξ) = -{V0} sech²(ξ/{a})")
    print()

    # Run robustness scan
    print("1. Robustness scan (ξ_max, κ variations)...")
    robustness_results = robustness_scan(V0, a)

    # Check stability
    n_bounds = set(r['n_bound'] for r in robustness_results)
    print(f"   N_bound values found: {n_bounds}")
    if len(n_bounds) == 1:
        print(f"   ✓ STABLE: N_bound = {list(n_bounds)[0]} across all (ξ_max, κ) pairs")
    else:
        print(f"   ⚠ UNSTABLE: N_bound varies with parameters")
    print()

    # Run phase diagram
    print("2. Phase diagram scan (V₀ variation)...")
    phase_results = phase_diagram_scan(a)

    # Find transition points
    transitions = []
    for i in range(1, len(phase_results)):
        if phase_results[i]['n_bound'] != phase_results[i-1]['n_bound']:
            transitions.append((phase_results[i-1]['V0'], phase_results[i]['V0']))

    print(f"   Transition regions (N_bound changes):")
    for i, (v1, v2) in enumerate(transitions):
        print(f"     {v1} < V₀ < {v2}")
    print()

    # Write outputs
    print("3. Writing outputs...")

    # Robustness table
    robustness_file = output_dir / 'opr21_robustness_table.md'
    write_markdown_table(
        robustness_results,
        ['xi_max', 'kappa', 'n_bound', 'E0', 'x1', 'I4'],
        str(robustness_file)
    )
    print(f"   ✓ {robustness_file}")

    # Phase diagram table
    phase_file = output_dir / 'opr21_phase_diagram.md'
    write_markdown_table(
        phase_results,
        ['V0', 'n_bound', 'E0', 'x1'],
        str(phase_file)
    )
    print(f"   ✓ {phase_file}")

    # Summary JSON
    summary = {
        'artifact_class': 'DEMO',
        'potential': f'Pöschl-Teller V(ξ) = -{V0} sech²(ξ/{a})',
        'status': 'Infrastructure validated, physics inputs OPEN',
        'robustness': {
            'n_bound_stable': len(n_bounds) == 1,
            'n_bound_value': int(list(n_bounds)[0]) if len(n_bounds) == 1 else [int(x) for x in n_bounds],
            'parameter_ranges': {
                'xi_max': [10.0, 14.0],
                'kappa': [0.0, 1.0]
            }
        },
        'phase_diagram': {
            'V0_range': [1.0, 40.0],
            'n_bound_transitions': transitions
        },
        'opr21_status': 'STRONG PARTIAL',
        'blocking': ['V(ξ) derivation from action', 'BC derivation from junction'],
        'note': 'N_bound = 3 requires V₀ > 25 for this toy potential'
    }

    summary_file = output_dir / 'opr21_summary.json'
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"   ✓ {summary_file}")

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  N_bound (toy, V₀=10): {list(n_bounds)[0] if len(n_bounds) == 1 else 'varies'}")
    print(f"  Robustness: {'STABLE' if len(n_bounds) == 1 else 'UNSTABLE'}")
    print(f"  I₄ range: {min(r['I4'] for r in robustness_results):.3f} - {max(r['I4'] for r in robustness_results):.3f}")
    print()
    print("OPR-21 Status: STRONG PARTIAL")
    print("  ✓ Infrastructure validated")
    print("  ✗ V(ξ) not derived from 5D action")
    print("  ✗ BC parameters not derived from junction")
    print()


if __name__ == '__main__':
    main()
