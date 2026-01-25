#!/usr/bin/env python3
"""
OPR-01 σ→M₀ Anchor — Numeric Sanity Check

This script computes M₀ and μ from the domain-wall derivation and checks
whether the result falls in the OPR-21 three-generation window.

NO SM OBSERVABLES ARE USED AS INPUTS.

Usage:
    python opr01_sigma_anchor_check.py

Author: EDC Book 2 Sprint (2026-01-25)
Status: CONDITIONAL [Dc]
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple

# ==============================================================================
# DERIVED CONSTANTS (from kink theory, [M])
# ==============================================================================

KINK_COEFFICIENT = np.sqrt(3) / 2  # ≈ 0.866 from σΔ = 4v²/3 derivation

# ==============================================================================
# INPUT PARAMETERS (all [P] postulated)
# ==============================================================================

@dataclass
class OPR01Params:
    """Parameters for OPR-01 derivation — all [P] postulated."""
    sigma: float  # Membrane tension [natural units: GeV³]
    Delta: float  # Wall thickness [natural units: GeV⁻¹]
    y: float      # Yukawa coupling [dimensionless]
    n: float      # Domain-size ratio ℓ/Δ [dimensionless]

    def __post_init__(self):
        """Validate parameters."""
        assert self.sigma > 0, "σ must be positive"
        assert self.Delta > 0, "Δ must be positive"
        assert self.y > 0, "y must be positive"
        assert self.n > 0, "n must be positive"


# ==============================================================================
# DERIVED QUANTITIES [Dc]
# ==============================================================================

def compute_M0(params: OPR01Params) -> float:
    """
    Compute M₀ from σ and Δ using domain-wall derivation.

    M₀ = (√3/2) y √(σΔ)    [Dc]

    Returns M₀ in natural units [GeV].
    """
    return KINK_COEFFICIENT * params.y * np.sqrt(params.sigma * params.Delta)


def compute_mu(params: OPR01Params) -> float:
    """
    Compute μ = M₀ℓ using the derived M₀.

    μ = M₀ × ℓ = M₀ × nΔ = (√3/2) y n √(σΔ³)    [Dc]

    Returns dimensionless μ.
    """
    M0 = compute_M0(params)
    ell = params.n * params.Delta
    return M0 * ell


def compute_sigma_Delta_cubed(params: OPR01Params) -> float:
    """
    Compute the combination σΔ³ that appears in the μ formula.

    Returns σΔ³ in natural units [GeV⁰ = dimensionless].
    """
    return params.sigma * (params.Delta ** 3)


# ==============================================================================
# OPR-21 WINDOW CHECK
# ==============================================================================

OPR21_MU_MIN = 25.0
OPR21_MU_MAX = 35.0

def check_three_generations(mu: float) -> Tuple[bool, str]:
    """
    Check if μ falls in the OPR-21 three-generation window [25, 35).

    Returns (is_in_window, message).
    """
    if OPR21_MU_MIN <= mu < OPR21_MU_MAX:
        return True, f"μ = {mu:.2f} ∈ [{OPR21_MU_MIN}, {OPR21_MU_MAX}) → N_bound = 3 ✓"
    elif mu < OPR21_MU_MIN:
        return False, f"μ = {mu:.2f} < {OPR21_MU_MIN} → N_bound < 3 (too few generations)"
    else:
        return False, f"μ = {mu:.2f} ≥ {OPR21_MU_MAX} → N_bound > 3 (too many generations)"


# ==============================================================================
# CONSISTENCY CONSTRAINT
# ==============================================================================

def compute_required_sigmaD3(y: float, n: float, mu_target: float) -> float:
    """
    Compute required σΔ³ to achieve a target μ.

    From: μ = (√3/2) y n √(σΔ³)
    We get: σΔ³ = (2μ / (√3 y n))²
    """
    return (2 * mu_target / (np.sqrt(3) * y * n)) ** 2


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    """Run OPR-01 sanity check with example parameters."""

    print("=" * 70)
    print("OPR-01 σ→M₀ Anchor — Numeric Sanity Check")
    print("Status: CONDITIONAL [Dc]")
    print("=" * 70)
    print()

    # Example parameters [P]
    # Using dimensional analysis: if σ ~ 10⁻² GeV³ and Δ ~ 20 GeV⁻¹
    # then √(σΔ) ~ √(0.2) ~ 0.45 GeV and M₀ ~ 0.39 GeV

    params = OPR01Params(
        sigma=0.01,   # [GeV³] ~ 10 MeV/fm² order of magnitude
        Delta=20.0,   # [GeV⁻¹] ~ 4 fm thickness
        y=1.0,        # Yukawa ~ O(1)
        n=4.0         # Domain is 4 wall-widths
    )

    print("INPUT PARAMETERS [P]:")
    print(f"  σ (tension)     = {params.sigma:.4f} GeV³")
    print(f"  Δ (thickness)   = {params.Delta:.2f} GeV⁻¹")
    print(f"  y (Yukawa)      = {params.y:.2f}")
    print(f"  n (ℓ/Δ)         = {params.n:.2f}")
    print()

    # Compute derived quantities
    M0 = compute_M0(params)
    mu = compute_mu(params)
    sigmaD3 = compute_sigma_Delta_cubed(params)

    print("DERIVED QUANTITIES [Dc]:")
    print(f"  M₀ = (√3/2) y √(σΔ)  = {M0:.4f} GeV")
    print(f"  ℓ  = nΔ              = {params.n * params.Delta:.2f} GeV⁻¹")
    print(f"  μ  = M₀ ℓ            = {mu:.2f}")
    print(f"  σΔ³                  = {sigmaD3:.2f}")
    print()

    # Check OPR-21 window
    in_window, message = check_three_generations(mu)
    print("OPR-21 WINDOW CHECK:")
    print(f"  {message}")
    print()

    # Compute required σΔ³ for target μ values
    print("CONSISTENCY CONSTRAINTS (for y=1, n=4):")
    for mu_target in [25.0, 30.0, 35.0]:
        required = compute_required_sigmaD3(params.y, params.n, mu_target)
        print(f"  μ = {mu_target:.0f} requires σΔ³ = {required:.1f}")
    print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Kink coefficient C = √3/2 = {KINK_COEFFICIENT:.4f}")
    print(f"Formula: M₀ = C × y × √(σΔ) = {KINK_COEFFICIENT:.3f} × {params.y} × √({params.sigma}×{params.Delta})")
    print(f"         M₀ = {M0:.4f} GeV")
    print()
    print(f"Formula: μ = C × y × n × √(σΔ³)")
    print(f"         μ = {KINK_COEFFICIENT:.3f} × {params.y} × {params.n} × √({sigmaD3:.2f})")
    print(f"         μ = {mu:.2f}")
    print()
    if in_window:
        print("✓ Parameters are CONSISTENT with 3-generation phenomenology")
    else:
        print("✗ Parameters are NOT in 3-generation window — adjust σ, Δ, or n")
    print()
    print("NO SM OBSERVABLES USED — derivation is from kink theory [M] + ansätze [P]")
    print("=" * 70)


if __name__ == "__main__":
    main()
