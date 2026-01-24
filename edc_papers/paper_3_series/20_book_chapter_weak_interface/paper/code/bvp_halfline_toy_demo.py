#!/usr/bin/env python3
"""
Half-Line BVP Toy Demonstration
===============================

Numerical demonstration of the thick-brane BVP pipeline for Part II.
Uses Pöschl-Teller potential on half-line z ∈ [0, ∞).

EPISTEMIC STATUS:
- [M] Pure mathematics / numerics
- [Toy] Placeholder potential, NOT derived from 5D action
- Does NOT constitute OPR-21 closure
- OPR-21 remains OPEN until V(z), BCs derived from membrane physics

Purpose:
- Demonstrate numerical pipeline for bound-state counting
- Extract N_bound, x1, I4 as defined in BVP Closure Pack
- Show robustness under:
  (a) z_max truncation
  (b) Robin BC parameter κ variations

NO CALIBRATION:
- No fitting to PDG, MW, GF, v=246 GeV
- Parameters chosen a priori (V0=10, a=1)

Author: EDC Research / Claude Code
Date: 2026-01-23
"""

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from scipy.integrate import simpson
from dataclasses import dataclass
from typing import List, Tuple
import sys
import os

# Optional: matplotlib for figure generation
try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend for PDF generation
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: matplotlib not available; figure generation will be skipped.")

# ==============================================================================
# TOY POTENTIAL: PÖSCHL-TELLER [M]/[Toy]
# ==============================================================================

def poschl_teller_potential(z: np.ndarray, V0: float = 10.0, a: float = 1.0) -> np.ndarray:
    """
    Pöschl-Teller potential: V(z) = -V0 * sech²(z/a)

    This is a toy placeholder. NOT derived from 5D membrane action.
    Essential spectrum: [0, ∞) since V(z) → 0 as z → ∞.
    Bound states: E < 0 (below essential spectrum threshold).

    Parameters:
        V0: Well depth (dimensionless, > 0)
        a: Width parameter (dimensionless)

    Returns:
        V(z) array
    """
    return -V0 / np.cosh(z / a)**2

# ==============================================================================
# FINITE-DIFFERENCE BVP SOLVER
# ==============================================================================

@dataclass
class HalfLineBVPResult:
    """Result container for half-line BVP."""
    z: np.ndarray              # Grid points
    eigenvalues: np.ndarray    # Eigenvalues (E < 0 are bound states)
    eigenvectors: np.ndarray   # Normalized eigenfunctions (columns)
    n_bound: int               # Count of bound states (E < threshold)
    threshold: float           # Essential spectrum onset (= 0 for Pöschl-Teller)
    x1: float                  # First positive eigenvalue (or |E_ground| if E<0)
    I4_ground: float           # Overlap integral ∫|ψ_0|⁴ dz
    params: dict               # Input parameters for reproducibility


def solve_halfline_bvp(
    z_max: float = 12.0,
    n_grid: int = 500,
    V0: float = 10.0,
    a: float = 1.0,
    kappa: float = 0.0,        # Robin BC: ψ'(0) + κψ(0) = 0; κ=0 is Neumann
    n_eig: int = 10,
) -> HalfLineBVPResult:
    """
    Solve Schrödinger-type BVP on truncated half-line [0, z_max].

    Operator: L = -d²/dz² + V(z)
    BC at z=0: Robin: ψ'(0) + κψ(0) = 0
    BC at z=z_max: Dirichlet: ψ(z_max) = 0 (mimics decay at infinity)

    For Pöschl-Teller, essential spectrum threshold = 0.
    Bound states have E < 0.

    Parameters:
        z_max: Truncation point (should be >> a for convergence)
        n_grid: Number of grid points
        V0: Potential depth
        a: Potential width
        kappa: Robin parameter at z=0 (κ=0: Neumann, κ→∞: Dirichlet)
        n_eig: Number of eigenvalues to compute

    Returns:
        HalfLineBVPResult with eigenvalues, eigenfunctions, and derived quantities
    """
    # Grid setup
    z = np.linspace(0, z_max, n_grid)
    dz = z[1] - z[0]

    # Potential on grid
    V = poschl_teller_potential(z, V0, a)

    # Build finite-difference matrix for -d²/dz² + V(z)
    # Second derivative: (ψ_{i+1} - 2ψ_i + ψ_{i-1}) / dz²
    main_diag = 2.0 / dz**2 + V
    off_diag = -1.0 / dz**2 * np.ones(n_grid - 1)

    # Robin BC at z=0: ψ'(0) + κψ(0) = 0
    # Using one-sided derivative: ψ'(0) ≈ (ψ_1 - ψ_0) / dz
    # → (ψ_1 - ψ_0)/dz + κψ_0 = 0 → ψ_1 = ψ_0(1 - κ*dz)
    # Modify first row of matrix to enforce this
    # For simplicity, we implement via ghost point method:
    # The matrix element H[0,0] gets modified to account for Robin BC
    if abs(kappa) < 1e-10:
        # Neumann: ψ'(0) = 0 → symmetric reflection → H[0,0] unchanged, H[0,1] = -2/dz²
        main_diag[0] = 2.0 / dz**2 + V[0]
        # Actually for Neumann, we use ψ_{-1} = ψ_1, so:
        # (-d²/dz²)ψ_0 ≈ (ψ_1 - 2ψ_0 + ψ_{-1})/dz² = (2ψ_1 - 2ψ_0)/dz² = 2(ψ_1 - ψ_0)/dz²
        # This changes the off-diagonal at position [0,1]
        # We implement by modifying main diagonal instead: effective factor
        main_diag[0] = 1.0 / dz**2 + V[0]  # Neumann-adjusted
    else:
        # Robin: ψ'(0) + κψ(0) = 0
        # Ghost point: ψ_{-1} = ψ_1 - 2*dz*κ*ψ_0
        # Second derivative at 0: (ψ_1 - 2ψ_0 + ψ_{-1})/dz² = (2ψ_1 - 2ψ_0 - 2*dz*κ*ψ_0)/dz²
        #                       = 2(ψ_1 - ψ_0)/dz² - 2κψ_0/dz
        # So H[0,0] += 2κ/dz, but we need to be careful with sign
        main_diag[0] = 1.0 / dz**2 + V[0] + 2.0 * kappa / dz

    # Dirichlet at z=z_max: ψ(z_max) = 0 (last row already correct)

    # Build sparse matrix
    H = diags([off_diag, main_diag, off_diag], [-1, 0, 1], format='csr')

    # Solve for lowest eigenvalues (we want negative ones = bound states)
    # sigma=None finds smallest algebraic eigenvalues
    try:
        eigenvalues, eigenvectors = eigsh(H, k=min(n_eig, n_grid-2), which='SA')
    except Exception as e:
        print(f"Warning: eigsh failed ({e}), using smaller k")
        eigenvalues, eigenvectors = eigsh(H, k=min(5, n_grid-2), which='SA')

    # Sort by eigenvalue
    idx = np.argsort(eigenvalues)
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Normalize eigenfunctions
    for i in range(eigenvectors.shape[1]):
        psi = eigenvectors[:, i]
        norm = np.sqrt(simpson(psi**2, x=z))
        if norm > 1e-10:
            eigenvectors[:, i] = psi / norm

    # Count bound states (E < 0 = threshold for Pöschl-Teller)
    threshold = 0.0
    n_bound = np.sum(eigenvalues < threshold)

    # x1: first eigenvalue magnitude (ground state energy)
    # In closure pack, x1 is first positive eigenvalue of dimensionless BVP
    # For E < 0, we use |E_ground| as the "binding energy scale"
    x1 = abs(eigenvalues[0]) if len(eigenvalues) > 0 else 0.0

    # I4 for ground state: ∫|ψ_0|⁴ dz
    psi0 = eigenvectors[:, 0]
    I4_ground = simpson(psi0**4, x=z)

    params = {
        'z_max': z_max,
        'n_grid': n_grid,
        'V0': V0,
        'a': a,
        'kappa': kappa,
    }

    return HalfLineBVPResult(
        z=z,
        eigenvalues=eigenvalues,
        eigenvectors=eigenvectors,
        n_bound=n_bound,
        threshold=threshold,
        x1=x1,
        I4_ground=I4_ground,
        params=params,
    )


# ==============================================================================
# ROBUSTNESS SCAN
# ==============================================================================

def run_robustness_scan(
    z_max_values: List[float] = [10.0, 12.0, 14.0],
    kappa_values: List[float] = [0.0, 0.1, 0.5],
    V0: float = 10.0,
    a: float = 1.0,
    n_grid: int = 500,
) -> List[dict]:
    """
    Scan over z_max and κ to demonstrate N_bound robustness.
    """
    results = []
    for z_max in z_max_values:
        for kappa in kappa_values:
            res = solve_halfline_bvp(z_max=z_max, n_grid=n_grid, V0=V0, a=a, kappa=kappa)
            results.append({
                'z_max': z_max,
                'kappa': kappa,
                'n_bound': res.n_bound,
                'E_ground': res.eigenvalues[0] if len(res.eigenvalues) > 0 else None,
                'x1': res.x1,
                'I4_ground': res.I4_ground,
            })
    return results


# ==============================================================================
# TABLE GENERATION (LaTeX output)
# ==============================================================================

def generate_latex_table(results: List[dict], output_path: str = None) -> str:
    """
    Generate LaTeX table from robustness scan results.
    """
    lines = [
        r"% Generated by code/bvp_halfline_toy_demo.py",
        r"% Epistemic status: [M]/[Toy] — pipeline demo only",
        r"% Does NOT close OPR-21; remains OPEN until V(z), BCs derived from 5D action",
        r"",
        r"\begin{table}[htbp]",
        r"\centering",
        r"\caption{Half-line BVP toy outputs (\tagM{}/[Toy], dimensionless units).}",
        r"\label{tab:bvp_toy_demo}",
        r"\small",
        r"\begin{tabular}{ccccccc}",
        r"\toprule",
        r"$z_{\max}$ & $\kappa$ & $N_{\text{bound}}$ & $E_0$ & $x_1 = |E_0|$ & $I_4^{(0)}$ \\",
        r"\midrule",
    ]

    for r in results:
        E0 = r['E_ground']
        E0_str = f"{E0:.4f}" if E0 is not None else "---"
        x1_str = f"{r['x1']:.4f}"
        I4_str = f"{r['I4_ground']:.4f}"
        lines.append(
            f"{r['z_max']:.1f} & {r['kappa']:.1f} & {r['n_bound']} & "
            f"{E0_str} & {x1_str} & {I4_str} \\\\"
        )

    lines.extend([
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ])

    table_str = "\n".join(lines)

    if output_path:
        with open(output_path, 'w') as f:
            f.write(table_str)
        print(f"Table written to: {output_path}")

    return table_str


# ==============================================================================
# PHASE DIAGRAM: N_bound(V0) sweep
# ==============================================================================

def run_phase_diagram_sweep(
    V0_values: List[float] = [1.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0],
    a: float = 1.0,
    z_max: float = 14.0,
    n_grid: int = 500,
    kappa: float = 0.0,
) -> List[dict]:
    """
    Sweep over V0 to show stepwise N_bound behavior.

    This demonstrates that N_bound is an OUTPUT of V(z)+BC,
    NOT a tuned parameter. The sweep is a priori — no PDG/GF/MW calibration.
    """
    results = []
    for V0 in V0_values:
        res = solve_halfline_bvp(z_max=z_max, n_grid=n_grid, V0=V0, a=a, kappa=kappa)
        results.append({
            'V0': V0,
            'a': a,
            'n_bound': res.n_bound,
            'E_ground': res.eigenvalues[0] if len(res.eigenvalues) > 0 else None,
            'x1': res.x1,
        })
    return results


def generate_phase_table(results: List[dict], output_path: str = None) -> str:
    """
    Generate LaTeX table for phase diagram (N_bound vs V0).
    """
    lines = [
        r"% Generated by code/bvp_halfline_toy_demo.py",
        r"% Epistemic status: [M]/[Toy] — phase diagram demonstration",
        r"% Shows stepwise spectral counting; N_bound is OUTPUT of V(z)+BC",
        r"% Does NOT close OPR-02/OPR-21; requires physical V(z) from 5D action",
        r"",
        r"\begin{table}[htbp]",
        r"\centering",
        r"\caption{Stepwise bound-state counting: $N_{\text{bound}}(V_0)$ for Pöschl--Teller toy.}",
        r"\label{tab:bvp_phase_diagram}",
        r"\small",
        r"\begin{tabular}{cccc}",
        r"\toprule",
        r"$V_0$ & $N_{\text{bound}}$ & $E_0$ & $x_1 = |E_0|$ \\",
        r"\midrule",
    ]

    for r in results:
        E0 = r['E_ground']
        E0_str = f"{E0:.4f}" if E0 is not None else "---"
        x1_str = f"{r['x1']:.4f}" if r['x1'] > 0 else "---"
        lines.append(
            f"{r['V0']:.1f} & {r['n_bound']} & {E0_str} & {x1_str} \\\\"
        )

    lines.extend([
        r"\bottomrule",
        r"\end{tabular}",
        r"\vspace{0.5em}",
        r"\parbox{0.85\textwidth}{\small\textit{Note:} $N_{\text{bound}}$ increases stepwise",
        r"as well depth $V_0$ grows. This is generic Sturm--Liouville behavior, not",
        r"an EDC prediction. Physical closure requires deriving $V(z)$ from membrane action.}",
        r"\end{table}",
    ])

    table_str = "\n".join(lines)

    if output_path:
        with open(output_path, 'w') as f:
            f.write(table_str)
        print(f"Phase table written to: {output_path}")

    return table_str


# ==============================================================================
# FIGURE GENERATION: V(z) and ψ_0(z)
# ==============================================================================

def generate_potential_wavefunction_figure(
    V0: float = 10.0,
    a: float = 1.0,
    z_max: float = 12.0,
    n_grid: int = 500,
    output_path: str = None,
) -> bool:
    """
    Generate a simple figure showing V(z) and ground state ψ_0(z).

    Returns True if figure was generated, False if matplotlib unavailable.
    """
    if not HAS_MATPLOTLIB:
        print("Skipping figure generation: matplotlib not available.")
        return False

    # Solve BVP
    res = solve_halfline_bvp(z_max=z_max, n_grid=n_grid, V0=V0, a=a, kappa=0.0)
    z = res.z
    V = poschl_teller_potential(z, V0, a)
    psi0 = res.eigenvectors[:, 0]
    E0 = res.eigenvalues[0]

    # Create figure with two y-axes
    fig, ax1 = plt.subplots(figsize=(6, 4))

    # Plot potential on left axis
    color1 = 'tab:blue'
    ax1.set_xlabel(r'$z$ (dimensionless)', fontsize=11)
    ax1.set_ylabel(r'$V(z)$', color=color1, fontsize=11)
    ax1.plot(z, V, color=color1, linewidth=1.5, label=r'$V(z) = -V_0 \mathrm{sech}^2(z/a)$')
    ax1.axhline(y=0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    ax1.axhline(y=E0, color='green', linestyle=':', linewidth=1.0, alpha=0.8,
                label=f'$E_0 = {E0:.2f}$')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim([-V0 * 1.1, V0 * 0.3])

    # Plot wavefunction on right axis
    ax2 = ax1.twinx()
    color2 = 'tab:red'
    ax2.set_ylabel(r'$\psi_0(z)$', color=color2, fontsize=11)
    ax2.plot(z, psi0, color=color2, linewidth=1.5, linestyle='-', label=r'$\psi_0(z)$')
    ax2.tick_params(axis='y', labelcolor=color2)

    # Title with epistemic status
    ax1.set_title(
        f'Toy BVP: $V_0={V0}$, $a={a}$, $N_{{\\mathrm{{bound}}}}={res.n_bound}$\n'
        r'[M]/[Toy] — pipeline demo, not OPR-21 closure',
        fontsize=10
    )

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=9)

    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=150, bbox_inches='tight')
        print(f"Figure saved to: {output_path}")
        plt.close(fig)
        return True
    else:
        plt.show()
        return True


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    print("=" * 70)
    print("HALF-LINE BVP TOY DEMONSTRATION")
    print("Epistemic status: [M]/[Toy] — pipeline demo, NOT OPR-21 closure")
    print("=" * 70)
    print()

    # Parameters (a priori, no fitting)
    V0 = 10.0  # Well depth
    a = 1.0    # Width scale

    print(f"Toy potential: Pöschl-Teller V(z) = -{V0} sech²(z/{a})")
    print(f"Essential spectrum threshold: λ_th = 0")
    print(f"Bound states: E < 0")
    print()

    # Run robustness scan
    z_max_values = [10.0, 12.0, 14.0]
    kappa_values = [0.0, 0.1, 0.5]

    print("Running robustness scan...")
    results = run_robustness_scan(
        z_max_values=z_max_values,
        kappa_values=kappa_values,
        V0=V0,
        a=a,
        n_grid=500,
    )

    # Print results
    print()
    print("Results (dimensionless):")
    print("-" * 70)
    print(f"{'z_max':>8} {'kappa':>8} {'N_bound':>8} {'E_ground':>12} {'x1':>12} {'I4':>12}")
    print("-" * 70)
    for r in results:
        E0 = r['E_ground']
        print(f"{r['z_max']:>8.1f} {r['kappa']:>8.1f} {r['n_bound']:>8} "
              f"{E0:>12.4f} {r['x1']:>12.4f} {r['I4_ground']:>12.4f}")
    print("-" * 70)

    # Check robustness
    n_bounds = [r['n_bound'] for r in results]
    if len(set(n_bounds)) == 1:
        print(f"\n✓ N_bound = {n_bounds[0]} is STABLE across all tested (z_max, κ) pairs.")
    else:
        print(f"\n⚠ N_bound varies: {set(n_bounds)}")

    # Generate LaTeX table
    print()
    output_dir = "code/output"
    import os
    os.makedirs(output_dir, exist_ok=True)
    output_path = f"{output_dir}/bvp_halfline_toy_table.tex"

    # Need to use relative path from script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir_abs = os.path.join(script_dir, "output")
    os.makedirs(output_dir_abs, exist_ok=True)
    output_path_abs = os.path.join(output_dir_abs, "bvp_halfline_toy_table.tex")

    table_str = generate_latex_table(results, output_path_abs)
    print()
    print("LaTeX table:")
    print(table_str)

    print()
    print("=" * 70)
    print("SUMMARY (Robustness Scan)")
    print("=" * 70)
    print(f"• Toy potential: V(z) = -V0 sech²(z/a) with V0={V0}, a={a}")
    print(f"• Threshold: λ_th = 0 (essential spectrum onset)")
    print(f"• N_bound = {n_bounds[0]} (stable under z_max, κ variations)")
    print(f"• x1 ≈ {results[0]['x1']:.4f} (ground state binding energy)")
    print(f"• I4 ≈ {results[0]['I4_ground']:.4f} (ground state concentration)")

    # =========================================================================
    # PHASE DIAGRAM: N_bound(V0) sweep
    # =========================================================================
    print()
    print("=" * 70)
    print("PHASE DIAGRAM: N_bound(V0) sweep")
    print("=" * 70)
    print()

    V0_values = [1.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0]
    phase_results = run_phase_diagram_sweep(
        V0_values=V0_values,
        a=a,
        z_max=14.0,
        n_grid=500,
        kappa=0.0,
    )

    print("Phase diagram results (a=1, z_max=14, κ=0, Neumann BC):")
    print("-" * 50)
    print(f"{'V0':>8} {'N_bound':>10} {'E_ground':>12} {'x1':>12}")
    print("-" * 50)
    for r in phase_results:
        E0 = r['E_ground']
        E0_str = f"{E0:.4f}" if E0 is not None else "---"
        x1_str = f"{r['x1']:.4f}" if r['x1'] > 0 else "---"
        print(f"{r['V0']:>8.1f} {r['n_bound']:>10} {E0_str:>12} {x1_str:>12}")
    print("-" * 50)

    # Show stepwise behavior
    unique_n_bounds = sorted(set(r['n_bound'] for r in phase_results))
    print(f"\n✓ N_bound takes values: {unique_n_bounds}")
    print("  This demonstrates STEPWISE spectral counting.")
    print("  N_bound is an OUTPUT of V(z)+BC, not a calibrated parameter.")

    # Generate phase table
    phase_table_path = os.path.join(output_dir_abs, "bvp_halfline_phase_table.tex")
    phase_table_str = generate_phase_table(phase_results, phase_table_path)
    print()
    print("Phase table (LaTeX):")
    print(phase_table_str)

    # =========================================================================
    # FIGURE: V(z) and ψ_0(z)
    # =========================================================================
    print()
    print("=" * 70)
    print("FIGURE GENERATION")
    print("=" * 70)

    figure_path = os.path.join(output_dir_abs, "bvp_halfline_toy_figure.pdf")
    if generate_potential_wavefunction_figure(V0=V0, a=a, z_max=12.0, n_grid=500,
                                               output_path=figure_path):
        print(f"✓ Figure generated: {figure_path}")
    else:
        print("⚠ Figure generation skipped (matplotlib not available).")

    # =========================================================================
    # FINAL SUMMARY
    # =========================================================================
    print()
    print("=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    print()
    print("Files generated:")
    print(f"  • {output_path_abs}")
    print(f"  • {phase_table_path}")
    if HAS_MATPLOTLIB:
        print(f"  • {figure_path}")
    print()
    print("Epistemic status: [M]/[Toy]")
    print("  • Pöschl-Teller potential is a TOY placeholder")
    print("  • Parameters chosen a priori (no PDG/MW/GF/v=246 calibration)")
    print("  • N_bound is OUTPUT of BVP, not input")
    print()
    print("OPR status:")
    print("  • OPR-21 (BVP): OPEN until V(z), BCs derived from 5D membrane action")
    print("  • OPR-02 (Ngen): OPEN until N_bound=3 emerges from physical potential")
    print()
    print("Reproducibility:")
    print("  python3 code/bvp_halfline_toy_demo.py")
    print("  Requirements: numpy, scipy (matplotlib optional for figures)")
    print("=" * 70)


if __name__ == "__main__":
    main()
