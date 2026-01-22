#!/usr/bin/env python3
"""
OPR-20 Attempt E: Prefactor-8 First-Principles Derivation Verification

Purpose:
- Compute the factor implied by each interpretation of R_ξ
- Calculate resulting m_φ given x₁ and ℓ
- Identify the residual needed to hit 80 GeV (comparison only, NOT input)

NO-SMUGGLING GUARDRAILS:
================================================================================
FORBIDDEN INPUTS (will trigger warnings if used to SET parameters):
  - M_W = 80 GeV
  - G_F = 1.17 × 10⁻⁵ GeV⁻²
  - g₂ (SM weak coupling)
  - v = 246 GeV (Higgs VEV)
  - Any PDG weak-scale numbers

ALLOWED INPUTS:
  - R_ξ ~ 10⁻³ fm (Part I diffusion scale) [P]
  - Geometric constants (π, √2) with derived origin
  - KK eigenvalue x₁ from boundary conditions [Dc]

COMPARISON ONLY (tagged [BL]):
  - M_W = 80 GeV for sanity check at the end
================================================================================

Usage:
    python check_opr20_prefactor8_attemptE.py
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple
import sys

# ==============================================================================
# NO-SMUGGLING BANNER
# ==============================================================================

def print_no_smuggling_banner():
    """Print the no-smuggling guardrails at startup."""
    print("=" * 78)
    print("OPR-20 ATTEMPT E: PREFACTOR-8 VERIFICATION")
    print("=" * 78)
    print()
    print("NO-SMUGGLING GUARDRAILS ACTIVE")
    print("-" * 40)
    print("FORBIDDEN as inputs to define ℓ, x₁, or R_ξ:")
    print("  ✗ M_W = 80 GeV")
    print("  ✗ G_F = 1.17 × 10⁻⁵ GeV⁻²")
    print("  ✗ g₂ (SM weak coupling)")
    print("  ✗ v = 246 GeV")
    print()
    print("ALLOWED:")
    print("  ✓ R_ξ ~ 10⁻³ fm from Part I [P]")
    print("  ✓ Geometric constants (π, √2) with derivation")
    print("  ✓ x₁ from KK eigenvalue equation [Dc]")
    print()
    print("COMPARISON ONLY [BL]:")
    print("  → M_W = 80 GeV for sanity check")
    print("=" * 78)
    print()


# ==============================================================================
# CONSTANTS (EDC-native, no SM smuggling)
# ==============================================================================

HBAR_C_MEV_FM = 197.327    # MeV·fm (fundamental constant, not SM)
R_XI_FM = 1e-3             # Diffusion scale from Part I [P]

# Comparison only [BL] - NOT used as input
M_W_GEV_BL = 80.4          # [BL] For comparison only

# KK eigenvalue for Neumann-Neumann on orbifold
X1_NEUMANN = np.pi / 2     # [Dc] From BC eigenvalue equation


# ==============================================================================
# R_ξ INTERPRETATION ANALYSIS
# ==============================================================================

@dataclass
class RxiInterpretation:
    """An interpretation of how R_ξ relates to the KK length ℓ."""
    name: str
    factor: float
    derivation: str
    tag: str
    status: str


def get_interpretations() -> List[RxiInterpretation]:
    """Return all R_ξ interpretations with their derivations."""
    return [
        RxiInterpretation(
            name="A1: R_ξ = ℓ (radius as length)",
            factor=1.0,
            derivation="Direct identification: R_ξ is the KK length itself",
            tag="[P]",
            status="Non-standard; requires redefining R_ξ as circumference"
        ),
        RxiInterpretation(
            name="A2: ℓ = 2πR_ξ (circumference)",
            factor=2 * np.pi,
            derivation="R_ξ is radius; KK uses circumference L = 2πR",
            tag="[Dc]",
            status="DERIVED: Standard circle geometry"
        ),
        RxiInterpretation(
            name="A3: ℓ = πR_ξ (half-orbifold)",
            factor=np.pi,
            derivation="Fundamental domain of S¹/Z₂ is half-circle",
            tag="[Dc] (neg)",
            status="NEGATIVE CLOSURE: x₁ already accounts for orbifold"
        ),
        RxiInterpretation(
            name="A4: ℓ = 4πR_ξ (solid angle)",
            factor=4 * np.pi,
            derivation="3D isotropic solid angle",
            tag="[Dc] (neg)",
            status="NEGATIVE CLOSURE: Wrong dimension (3D not 1D)"
        ),
    ]


def compute_m_phi(x1: float, factor: float, r_xi_fm: float) -> float:
    """
    Compute m_φ from first principles.

    m_φ = x₁ / ℓ = x₁ / (factor × R_ξ)

    Returns mass in GeV.
    """
    ell_fm = factor * r_xi_fm
    m_phi_mev = x1 * HBAR_C_MEV_FM / ell_fm
    return m_phi_mev / 1000  # Convert to GeV


# ==============================================================================
# COMBINED FACTOR ANALYSIS
# ==============================================================================

@dataclass
class CombinedFactor:
    """A composite geometric factor with independence check."""
    name: str
    value: float
    components: str
    tag: str
    independence: str


def get_combined_factors() -> List[CombinedFactor]:
    """Return valid combined factors with independence verification."""
    return [
        CombinedFactor(
            name="2π (circumference only)",
            value=2 * np.pi,
            components="Circumference interpretation",
            tag="[Dc]",
            independence="Single factor, no combination"
        ),
        CombinedFactor(
            name="√2 (normalization only)",
            value=np.sqrt(2),
            components="Mode orthonormality on orbifold",
            tag="[Dc]",
            independence="Single factor, no combination"
        ),
        CombinedFactor(
            name="2π√2 (circumference + normalization)",
            value=2 * np.pi * np.sqrt(2),
            components="2π × √2",
            tag="[Dc]",
            independence="PASS: Independent physics (geometry vs normalization)"
        ),
        CombinedFactor(
            name="8 (target)",
            value=8.0,
            components="Unknown combination",
            tag="[OPEN]",
            independence="No valid decomposition found"
        ),
    ]


# ==============================================================================
# RESIDUAL ANALYSIS
# ==============================================================================

def compute_residual_to_target(m_phi: float, target: float = M_W_GEV_BL) -> Tuple[float, float]:
    """
    Compute the residual factor needed to hit target mass.

    Returns: (residual_factor, percentage_deviation)

    NOTE: Target is [BL] comparison only, NOT an input for derivation.
    """
    residual = target / m_phi
    deviation_pct = (m_phi - target) / target * 100
    return residual, deviation_pct


def analyze_missing_factor():
    """Analyze what factor would be needed to convert 2π√2 to 8."""
    f_current = 2 * np.pi * np.sqrt(2)
    f_target = 8.0

    missing = f_target / f_current

    print("MISSING FACTOR ANALYSIS")
    print("-" * 50)
    print(f"Current best factor: 2π√2 = {f_current:.6f}")
    print(f"Target factor: 8")
    print(f"Missing factor: 8 / (2π√2) = {missing:.6f}")
    print()
    print("Algebraic form:")
    print(f"  8 / (2π√2) = 4 / (π√2) = 2√2 / π")
    print(f"  Numeric: {4/(np.pi*np.sqrt(2)):.6f}")
    print()

    # Check against simple fractions
    candidates = [
        ("9/10", 0.9),
        ("π/√(12)", np.pi / np.sqrt(12)),
        ("√(2)/√(π)", np.sqrt(2) / np.sqrt(np.pi)),
        ("1 - 0.1", 0.9),
        ("e^(-0.1)", np.exp(-0.1)),
    ]

    print("Simple candidate comparison:")
    for name, val in candidates:
        diff = abs(val - missing) / missing * 100
        print(f"  {name:<15} = {val:.6f}  (diff: {diff:.2f}%)")

    print()


# ==============================================================================
# MAIN ANALYSIS
# ==============================================================================

def main():
    print_no_smuggling_banner()

    # Part 1: R_ξ Interpretation Analysis
    print("PART 1: R_ξ INTERPRETATION ANALYSIS")
    print("-" * 78)
    print()
    print(f"Input: R_ξ = {R_XI_FM} fm [P] (from Part I diffusion)")
    print(f"       x₁ = π/2 = {X1_NEUMANN:.6f} [Dc] (Neumann-Neumann)")
    print()

    interpretations = get_interpretations()

    print(f"{'Interpretation':<35} {'Factor':>8} {'ℓ (fm)':>12} {'m_φ (GeV)':>10} {'Tag':<10}")
    print("-" * 78)

    for interp in interpretations:
        ell = interp.factor * R_XI_FM
        m_phi = compute_m_phi(X1_NEUMANN, interp.factor, R_XI_FM)
        print(f"{interp.name:<35} {interp.factor:8.4f} {ell:12.6f} {m_phi:10.2f} {interp.tag:<10}")

    print()
    print("Derivation details:")
    for interp in interpretations:
        print(f"  {interp.name}:")
        print(f"    Derivation: {interp.derivation}")
        print(f"    Status: {interp.status}")
        print()

    # Part 2: Combined Factor Analysis
    print("PART 2: COMBINED FACTOR ANALYSIS (with independence check)")
    print("-" * 78)
    print()

    combined = get_combined_factors()

    print(f"{'Combined Factor':<30} {'Value':>8} {'m_φ (GeV)':>10} {'Tag':<12} {'Independence':<20}")
    print("-" * 90)

    for cf in combined:
        m_phi = compute_m_phi(X1_NEUMANN, cf.value, R_XI_FM)
        residual, dev = compute_residual_to_target(m_phi)
        print(f"{cf.name:<30} {cf.value:8.4f} {m_phi:10.2f} {cf.tag:<12} {cf.independence[:20]}")

    print()

    # Part 3: Residual Analysis
    print("PART 3: RESIDUAL ANALYSIS (comparison to M_W [BL] only)")
    print("-" * 78)
    print()
    print("NOTE: M_W = 80 GeV is [BL] comparison ONLY, not an input for derivation.")
    print()

    # Best derived candidate
    best_factor = 2 * np.pi * np.sqrt(2)
    m_phi_best = compute_m_phi(X1_NEUMANN, best_factor, R_XI_FM)
    residual, dev = compute_residual_to_target(m_phi_best)

    print(f"Best derived factor: 2π√2 = {best_factor:.4f} [Dc]")
    print(f"Resulting m_φ: {m_phi_best:.2f} GeV")
    print(f"Comparison to M_W = {M_W_GEV_BL} GeV [BL]:")
    print(f"  Deviation: {dev:+.1f}%")
    print(f"  Factor needed to hit M_W: {residual:.4f}")
    print()

    # Part 4: Missing Factor Analysis
    print("PART 4: MISSING FACTOR (to convert 2π√2 → 8)")
    print("-" * 78)
    print()
    analyze_missing_factor()

    # Part 5: Track B Candidate Evaluation
    print("PART 5: TRACK B CANDIDATES FOR 0.9003 FACTOR")
    print("-" * 78)
    print()

    missing = 8 / (2 * np.pi * np.sqrt(2))

    candidates_B = [
        ("B1: Orbifold domain (0.5)", 0.5, "[Dc] (neg)", "Already in x₁"),
        ("B2: Thick-brane overlap", "variable", "[P]/[OPEN]", "Requires BVP"),
        ("B3: BKT (1+κ)⁻¹, κ=0.11", 1/(1+0.11), "[P]", "Parameter not derived"),
        ("B4: Brane curvature", "variable", "[P]/[OPEN]", "No evidence"),
        ("B5: Numeric (4/π√2)", missing, "[OPEN]", "Definition, not derivation"),
    ]

    print(f"{'Candidate':<30} {'Value':>10} {'Match?':>8} {'Status':<15} {'Note':<20}")
    print("-" * 90)

    for name, val, tag, note in candidates_B:
        if isinstance(val, float):
            match = "Yes" if abs(val - missing) / missing < 0.02 else "No"
            print(f"{name:<30} {val:10.4f} {match:>8} {tag:<15} {note:<20}")
        else:
            print(f"{name:<30} {val:>10} {'Maybe':>8} {tag:<15} {note:<20}")

    print()

    # Final Verdict
    print("=" * 78)
    print("ATTEMPT E VERDICT")
    print("=" * 78)
    print()
    print("TRACK A (2π derivation):")
    print("  ✓ R_ξ is the radius of the compact dimension")
    print("  ✓ KK quantization uses circumference ℓ = 2πR_ξ")
    print("  ✓ Factor 2π is now [Dc], upgraded from [P]")
    print("  ✓ Alternative factors (1, π, 4π) negatively closed [Dc]")
    print()
    print("TRACK B (0.9003 residual):")
    print("  ✗ No unique derivation of the missing factor")
    print("  ✗ Candidates exist but all require new parameters [P]")
    print("  ✗ Residual remains [OPEN]")
    print()
    print("COMBINED RESULT:")
    print(f"  Best factor: 2π√2 = {best_factor:.4f} [Dc]")
    print(f"  Result: m_φ = {m_phi_best:.2f} GeV")
    print(f"  Residual vs M_W: {dev:+.1f}% [BL comparison]")
    print()
    print("STATUS: OPR-20 partial upgrade")
    print("  - 2π factor: [P] → [Dc]")
    print("  - 2π√2 combined: [Dc] (all components derived)")
    print("  - Exact factor 8: remains [OPEN]")
    print("  - Overall: RED-C [Dc]+[OPEN]")
    print("=" * 78)


if __name__ == "__main__":
    main()
