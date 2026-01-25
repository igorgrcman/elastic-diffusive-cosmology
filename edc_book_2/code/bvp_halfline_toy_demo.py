#!/usr/bin/env python3
"""
BVP Halfline Toy Demo — Generate Figure for CH14

================================================================================
ARTIFACT CLASSIFICATION: DEMO (Pedagogical)
================================================================================
This script is a DEMONSTRATION of BVP methodology, NOT a REPRODUCIBILITY
artifact for physics claims. The Poschl-Teller potential used here is a
textbook toy model chosen for analytic tractability.

DO NOT cite this figure as evidence for EDC physics claims.
The potential V(xi) = -V_0 sech^2(xi/a) is NOT derived from membrane physics.
================================================================================

Solves the 1D Schrodinger equation for the Poschl-Teller potential:
    V(xi) = -V_0 sech^2(xi/a)

with parameters V_0 = 10, a = 1 (in natural units hbar^2/2m = 1).

Outputs:
    code/output/bvp_halfline_toy_figure.pdf

Author: EDC Book 2 audit automation
Date: 2026-01-24
"""

import numpy as np
from pathlib import Path

# Try to import matplotlib; gracefully handle if not available
try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: matplotlib not available. Skipping figure generation.")

# Try to import scipy for eigenvalue solving
try:
    from scipy.linalg import eigh_tridiagonal
    from scipy.integrate import simpson
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    print("Warning: scipy not available. Using analytic solution only.")


def poschl_teller_potential(xi, V0=10.0, a=1.0):
    """Poschl-Teller potential: V(xi) = -V_0 sech^2(xi/a)"""
    return -V0 / np.cosh(xi / a)**2


def analytic_ground_state(xi, V0=10.0, a=1.0):
    """
    Analytic ground state for Poschl-Teller potential.

    For -V_0 sech^2(xi/a), the bound states are:
        psi_n(xi) ~ sech^(lambda-n)(xi/a)
    where lambda*(lambda+1) = V_0 (in units hbar^2/2m = 1).
    """
    # Solve lambda*(lambda+1) = V0
    lam = (-1 + np.sqrt(1 + 4*V0)) / 2

    # Ground state (n=0)
    psi = 1.0 / np.cosh(xi / a)**lam

    # Normalize
    norm = np.sqrt(simpson(psi**2, x=xi)) if HAS_SCIPY else np.sqrt(np.trapz(psi**2, xi))
    psi = psi / norm

    # Ground state energy
    E0 = -(lam)**2

    return psi, E0, lam


def main():
    # Parameters (from CH14)
    V0 = 10.0
    a = 1.0

    # Grid
    xi = np.linspace(-5, 10, 1000)

    # Potential
    V = poschl_teller_potential(xi, V0, a)

    # Ground state
    psi0, E0, lam = analytic_ground_state(xi, V0, a)

    print(f"Poschl-Teller BVP Demo")
    print(f"  V_0 = {V0}, a = {a}")
    print(f"  lambda = {lam:.4f}")
    print(f"  E_0 = {E0:.4f}")

    if not HAS_MATPLOTLIB:
        print("Skipping figure generation (matplotlib not available).")
        return

    # Create figure
    fig, ax = plt.subplots(figsize=(8, 5))

    # Plot potential
    ax.plot(xi, V, 'b-', linewidth=2, label=r'$V(\xi) = -V_0\,\mathrm{sech}^2(\xi/a)$')

    # Plot wavefunction (scaled for visibility)
    scale = abs(V.min()) * 0.6
    ax.plot(xi, psi0 * scale + E0, 'r-', linewidth=2,
            label=r'$\psi_0(\xi)$ (scaled)')
    ax.fill_between(xi, E0, psi0 * scale + E0, alpha=0.3, color='red')

    # Threshold and energy level
    ax.axhline(0, color='gray', linestyle='--', linewidth=1,
               label='Threshold ($E = 0$)')
    ax.axhline(E0, color='orange', linestyle=':', linewidth=1.5,
               label=f'$E_0 = {E0:.2f}$')

    # Labels
    ax.set_xlabel(r'$\xi$ (dimensionless)', fontsize=12)
    ax.set_ylabel(r'Energy / Amplitude', fontsize=12)
    ax.set_title(r'Toy BVP: P\"oschl-Teller Potential ($V_0=10$, $a=1$)', fontsize=13)
    ax.legend(loc='upper right', fontsize=10)
    ax.set_xlim(-5, 10)
    ax.set_ylim(V.min() * 1.2, 5)
    ax.grid(True, alpha=0.3)

    # Add annotation
    ax.annotate(r'$N_{\mathrm{bound}} = \lfloor \lambda \rfloor + 1 = 3$',
                xy=(5, -2), fontsize=11,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Save
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / 'bvp_halfline_toy_figure.pdf'

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Saved: {output_path}")

    plt.close()


if __name__ == '__main__':
    main()
