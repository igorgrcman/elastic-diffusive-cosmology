#!/usr/bin/env python3
"""
OPR-04 Δ (Wall Thickness) — Consistency Check

This script verifies the BPS relation σΔ = 4v²/3 and computes Δ from
various input scenarios.

NO SM OBSERVABLES ARE USED AS INPUTS (except M_Z for R_ξ anchor).

Usage:
    python opr04_delta_consistency_check.py

Author: EDC Book 2 Sprint (2026-01-25)
Status: CONDITIONAL [Dc]
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, Optional

# ==============================================================================
# CONSTANTS
# ==============================================================================

# Conversion factors
HBAR_C_MEV_FM = 197.327  # ℏc in MeV·fm
FM_TO_GEV_INV = 5.068    # 1 fm = 5.068 GeV⁻¹

# Baseline values [BL]
M_Z_GEV = 91.1876  # Z boson mass [GeV]
ALPHA_EM = 1/137.036  # Fine structure constant at Thomson limit
M_E_MEV = 0.51100  # Electron mass [MeV]

# Derived scales
R_XI_FM = HBAR_C_MEV_FM / (M_Z_GEV * 1000)  # R_ξ = ℏc/M_Z ≈ 2.17×10⁻³ fm
R_E_FM = ALPHA_EM * HBAR_C_MEV_FM / M_E_MEV  # r_e = αℏc/m_e ≈ 2.82×10⁻³ fm

# ==============================================================================
# SIGMA VALUES
# ==============================================================================

@dataclass
class SigmaHypothesis:
    """Different hypotheses for membrane tension σ."""
    name: str
    sigma_mev_fm2: float  # [MeV/fm²]
    status: str  # [P], [Dc], [BL]
    source: str

# Two competing σ values from turning point document
SIGMA_HYPOTHESIS_A = SigmaHypothesis(
    name="E_σ = m_e c²/α",
    sigma_mev_fm2=8.82,  # σ = m_e³c⁴/(α³ℏ²)
    status="[Dc]",
    source="Turning point: E_σ hypothesis"
)

SIGMA_HYPOTHESIS_B = SigmaHypothesis(
    name="Framework v2.0",
    sigma_mev_fm2=5.856,  # σr_e² = (36/π)m_e → σ = 5.856/r_e²
    status="[Dc]",
    source="Framework v2.0: σr_e² = 5.856 MeV"
)

# ==============================================================================
# BPS RELATIONS
# ==============================================================================

def compute_sigma_delta(v_mev: float) -> float:
    """
    Compute σΔ from vacuum expectation value v.

    BPS relation: σΔ = 4v²/3  [M]

    Returns σΔ in [MeV · fm].
    """
    return (4/3) * v_mev**2


def compute_delta_from_sigma_v(sigma_mev_fm2: float, v_mev: float) -> float:
    """
    Compute Δ from σ and v using BPS relation.

    Δ = 4v²/(3σ)  [Dc]

    Returns Δ in [fm].
    """
    sigma_delta = compute_sigma_delta(v_mev)
    return sigma_delta / sigma_mev_fm2


def compute_v_from_sigma_delta(sigma_mev_fm2: float, delta_fm: float) -> float:
    """
    Compute v from σ and Δ using BPS relation.

    v² = (3/4)σΔ → v = √(3σΔ/4)  [Dc]

    Returns v in [MeV].
    """
    return np.sqrt(0.75 * sigma_mev_fm2 * delta_fm)


def compute_lambda_from_v_delta(v_mev: float, delta_fm: float) -> float:
    """
    Compute λ from v and Δ.

    From Δ = √(2/λ)/v → λ = 2/(v²Δ²)  [M]

    Returns dimensionless λ.
    """
    # Convert to consistent units: v in MeV, Δ in fm
    # Need v·Δ in dimensionless units: (MeV)·(fm) / (ℏc in MeV·fm) = dimensionless
    v_delta_dimless = v_mev * delta_fm / HBAR_C_MEV_FM
    return 2 / (v_delta_dimless**2)


# ==============================================================================
# OPR-01/OPR-21 BRIDGE
# ==============================================================================

def compute_M0_from_sigma_delta_y(sigma_mev_fm2: float, delta_fm: float, y: float) -> float:
    """
    Compute M₀ from OPR-01 relation.

    M₀² = (3y²/4)σΔ → M₀ = (√3/2)y√(σΔ)  [Dc]

    Returns M₀ in [MeV].
    """
    sigma_delta = sigma_mev_fm2 * delta_fm  # [MeV · fm]
    # σΔ has units [MeV·fm²/fm] = [MeV·fm]
    # Need to convert to energy: multiply by appropriate factor
    # Actually: M₀² = (3y²/4)σΔ where σΔ should be in [energy²]
    # Let's use natural units: σ in GeV³, Δ in GeV⁻¹
    sigma_gev3 = sigma_mev_fm2 * 1e-3 * (FM_TO_GEV_INV)**2  # MeV/fm² → GeV³
    delta_gev_inv = delta_fm * FM_TO_GEV_INV  # fm → GeV⁻¹
    sigma_delta_gev2 = sigma_gev3 * delta_gev_inv  # GeV²

    M0_gev = (np.sqrt(3)/2) * y * np.sqrt(sigma_delta_gev2)
    return M0_gev * 1000  # Convert to MeV


def compute_mu(M0_mev: float, ell_fm: float) -> float:
    """
    Compute dimensionless μ = M₀ℓ.

    Returns dimensionless μ.
    """
    M0_gev = M0_mev / 1000
    ell_gev_inv = ell_fm * FM_TO_GEV_INV
    return M0_gev * ell_gev_inv


# ==============================================================================
# SCENARIO ANALYSIS
# ==============================================================================

def analyze_scenario(name: str, sigma: SigmaHypothesis, delta_fm: float,
                     y: float = 1.0, n: float = 4.0):
    """Analyze a (σ, Δ) scenario and report results."""

    print(f"\n{'='*70}")
    print(f"SCENARIO: {name}")
    print(f"{'='*70}")

    print(f"\nINPUTS:")
    print(f"  σ = {sigma.sigma_mev_fm2:.3f} MeV/fm² ({sigma.name}) {sigma.status}")
    print(f"  Δ = {delta_fm:.4e} fm")
    print(f"  y = {y:.2f} (Yukawa coupling) [P]")
    print(f"  n = {n:.1f} (ℓ/Δ ratio) [P]")

    # Compute derived quantities
    v = compute_v_from_sigma_delta(sigma.sigma_mev_fm2, delta_fm)
    lambda_val = compute_lambda_from_v_delta(v, delta_fm)
    M0 = compute_M0_from_sigma_delta_y(sigma.sigma_mev_fm2, delta_fm, y)
    ell_fm = n * delta_fm
    mu = compute_mu(M0, ell_fm)
    sigma_delta3 = sigma.sigma_mev_fm2 * (delta_fm ** 3)

    print(f"\nDERIVED QUANTITIES [Dc]:")
    print(f"  v = √(3σΔ/4) = {v:.4f} MeV (vacuum expectation value)")
    print(f"  λ = 2/(vΔ)² = {lambda_val:.4e} (self-coupling, dimensionless)")
    print(f"  M₀ = (√3/2)y√(σΔ) = {M0:.4f} MeV")
    print(f"  ℓ = nΔ = {ell_fm:.4e} fm (ASSUMES n = {n})")
    print(f"  σΔ³ = {sigma_delta3:.4e} MeV·fm")

    # Detailed μ breakdown
    M0_gev = M0 / 1000
    ell_gev_inv = ell_fm * FM_TO_GEV_INV
    print(f"\n  μ BREAKDOWN (dimensionless = GeV × GeV⁻¹):")
    print(f"    M₀ = {M0:.4f} MeV = {M0_gev:.6f} GeV")
    print(f"    ℓ = {ell_fm:.4e} fm = {ell_gev_inv:.4e} GeV⁻¹")
    print(f"    μ = M₀ × ℓ = {M0_gev:.6f} × {ell_gev_inv:.4e} = {mu:.6f}")

    # Check OPR-21 window
    print(f"\nOPR-21 THREE-GENERATION CHECK:")
    if 25 <= mu < 35:
        print(f"  ✓ μ = {mu:.2f} ∈ [25, 35) → N_bound = 3")
    elif mu < 25:
        print(f"  ✗ μ = {mu:.6f} < 25 → N_bound < 3 (too few generations)")
        print(f"  INTERPRETATION: This is a CONDITIONAL tension.")
        print(f"    - Assumes ℓ = n×Δ with n = {n}")
        print(f"    - If n ≫ {n}, μ could reach [25,35]")
        required_n = 30 / mu * n  # n needed to get μ = 30
        print(f"    - To get μ = 30, would need n ≈ {required_n:.0f}")
    else:
        print(f"  ✗ μ = {mu:.2f} ≥ 35 → N_bound > 3 (too many generations)")

    # BPS consistency
    sigma_delta_computed = sigma.sigma_mev_fm2 * delta_fm
    sigma_delta_from_v = compute_sigma_delta(v)
    print(f"\nBPS CONSISTENCY CHECK:")
    print(f"  σΔ (direct) = {sigma_delta_computed:.6f} MeV·fm")
    print(f"  4v²/3 = {sigma_delta_from_v:.6f} MeV·fm")
    print(f"  Difference = {abs(sigma_delta_computed - sigma_delta_from_v):.2e}")

    return {
        'v': v,
        'lambda': lambda_val,
        'M0': M0,
        'mu': mu,
        'sigma_delta3': sigma_delta3
    }


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    """Run OPR-04 consistency analysis."""

    print("="*70)
    print("OPR-04 Δ (Wall Thickness) — Consistency Check")
    print("Status: CONDITIONAL [Dc]")
    print("="*70)

    print("\nKEY RELATIONS:")
    print("  [M] Δ = 2/(v√λ) — kink width from scalar potential")
    print("  [M] σΔ = 4v²/3 — BPS constraint")
    print("  [Dc] M₀² = (3y²/4)σΔ — OPR-01 result")
    print("  [Dc] μ = M₀ℓ — OPR-21 parameter")

    print("\nREFERENCE SCALES:")
    print(f"  R_ξ = ℏc/M_Z = {R_XI_FM:.4e} fm [BL]")
    print(f"  r_e = αℏc/m_e = {R_E_FM:.4e} fm [BL]")

    # Scenario 1: Δ = R_ξ (OPR-04 identification)
    analyze_scenario(
        "Δ = R_ξ (diffusion scale) with σ = 8.82 MeV/fm²",
        SIGMA_HYPOTHESIS_A,
        R_XI_FM
    )

    # Scenario 2: Δ = R_ξ with Framework σ
    analyze_scenario(
        "Δ = R_ξ (diffusion scale) with σ = 5.86 MeV/fm²",
        SIGMA_HYPOTHESIS_B,
        R_XI_FM
    )

    # Scenario 3: Δ = 3.121×10⁻³ fm (CH4 value)
    analyze_scenario(
        "Δ = 3.121×10⁻³ fm (CH4 calibrated) with σ = 5.86 MeV/fm²",
        SIGMA_HYPOTHESIS_B,
        3.121e-3
    )

    # Scenario 4: Find Δ for μ = 30 (middle of 3-generation window)
    print("\n" + "="*70)
    print("INVERSE PROBLEM: What Δ gives μ = 30?")
    print("="*70)

    target_mu = 30.0
    y, n = 1.0, 4.0
    sigma = SIGMA_HYPOTHESIS_A

    # From μ² = (3y²n²/4) σΔ³ → Δ³ = 4μ²/(3y²n²σ)
    sigma_gev3 = sigma.sigma_mev_fm2 * 1e-3 * (FM_TO_GEV_INV)**2
    delta3_gev_inv3 = (4 * target_mu**2) / (3 * y**2 * n**2 * sigma_gev3)
    delta_gev_inv = delta3_gev_inv3 ** (1/3)
    delta_fm = delta_gev_inv / FM_TO_GEV_INV

    print(f"\nFor μ = {target_mu}, y = {y}, n = {n}, σ = {sigma.sigma_mev_fm2} MeV/fm²:")
    print(f"  Required Δ = {delta_fm:.4e} fm")
    print(f"  Compare: R_ξ = {R_XI_FM:.4e} fm")
    print(f"  Ratio Δ/R_ξ = {delta_fm/R_XI_FM:.2f}")

    # Verify
    results = analyze_scenario(
        f"VERIFY: Δ chosen to give μ = {target_mu}",
        sigma,
        delta_fm
    )

    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print("\nThe wall thickness Δ is determined by:")
    print("  1. The kink profile: Δ = 2/(v√λ) [M]")
    print("  2. The BPS relation: σΔ = 4v²/3 [M]")
    print("  3. Once σ is fixed [Dc], Δ and v are related by a single constraint")
    print("\nRemaining free parameters after OPR-04:")
    print("  - v (or equivalently M₀ = yv) [P]")
    print("  - y (Yukawa coupling) [P]")
    print("  - n (domain ratio ℓ/Δ) [P]")
    print("\nClosure paths:")
    print("  Path A: Set Δ = R_ξ (OPR-04 identification) [P]")
    print("  Path B: Use μ ∈ [25,35] to constrain Δ (phenomenological) [Dc]")
    print("\n" + "-"*70)
    print("IMPORTANT: CONDITIONAL TENSION")
    print("-"*70)
    print("If Δ = R_ξ ~ 10⁻³ fm AND ℓ = nΔ with small n, then μ << 25.")
    print("This tension is CONDITIONAL on:")
    print("  (1) Δ = δ (kink width = boundary-layer scale)")
    print("  (2) δ = R_ξ (boundary-layer = diffusion scale)")
    print("  (3) ℓ = nΔ with modest n ~ O(1)")
    print("\nResolution paths (all remain viable):")
    print("  - δ ≠ Δ: boundary-layer scale may differ from kink width")
    print("  - n ≫ 4: domain size may be much larger than kink width")
    print("  - Derive ℓ independently from 5D action")
    print("-"*70)
    print("\nNO SM OBSERVABLES USED except M_Z anchor for R_ξ [BL]")
    print("="*70)


if __name__ == "__main__":
    main()
