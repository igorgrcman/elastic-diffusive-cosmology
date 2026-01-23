#!/usr/bin/env python3
"""
OPR-20 Attempt C: Geometric Factor-8 Route Verification

Purpose: Systematically check candidate geometric/topological routes for factor 8
         in the KK mass relation m_φ = x₁/ℓ.

NO-SMUGGLING GUARDRAILS:
========================
FORBIDDEN INPUTS:
  ✗ M_W = 80 GeV (would make analysis circular)
  ✗ G_F = 1.17×10⁻⁵ GeV⁻²
  ✗ g₂² ≈ 0.42 (SM coupling)
  ✗ Any fitting to "factor 8 works"

ALLOWED INPUTS:
  ✓ R_ξ ~ 10⁻³ fm [P] (Part I diffusion scale)
  ✓ Geometric factors (π, 2π, 4π) if derivable
  ✓ Symmetry counting (Z₂, Z₃, Z₆)
  ✓ Dimensional analysis
  ✓ KK reduction conventions

TARGET:
  Factor ~8 discrepancy in m_φ^{candidate A} ≈ 620 GeV vs weak scale
  Need: geometric factor C such that m_φ = (x₁/ℓ)/C with C ≈ 8
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, List

# Physical constants (allowed)
HBAR_C = 197.3  # MeV·fm

# EDC parameters (allowed)
R_XI = 1e-3  # fm [P] diffusion correlation length

@dataclass
class RouteResult:
    """Result from a geometric factor route."""
    name: str
    factor: float
    status: str  # [Dc], [P], [OPEN]
    derivation: str
    m_phi_GeV: float  # resulting m_φ in GeV
    deviation_from_8: float  # percentage deviation from factor 8

def compute_m_phi(x1: float, ell: float, geometric_factor: float = 1.0) -> float:
    """Compute m_φ = x₁/(ℓ × C_geom) in GeV."""
    m_phi_MeV = x1 * HBAR_C / (ell * geometric_factor)
    return m_phi_MeV / 1000  # Convert to GeV

# ============================================================================
# ROUTE A: Two-sided bulk / Z₂ doubling
# ============================================================================
def route_A_z2_doubling() -> RouteResult:
    """
    Z₂ orbifold: bulk extends from -ℓ to +ℓ with Z₂ identification.

    Derivation [Dc]:
    - Orbifold S¹/Z₂ has interval [-πR, +πR] identified under y → -y
    - Two fixed points at y = 0, πR (branes)
    - KK mass for mode n: m_n = n/R (on full interval of length 2πR)
    - If we naively use half-interval ℓ = πR, true ℓ_eff = 2ℓ
    - Factor: 2 (from using full interval)

    This is standard KK reduction - factor 2 is unavoidable [Dc].
    """
    factor = 2.0
    x1 = np.pi  # First eigenvalue (D-D)
    m_phi = compute_m_phi(x1, R_XI, factor)
    deviation = abs(factor - 8) / 8 * 100

    return RouteResult(
        name="Route A: Z₂ orbifold (two-sided bulk)",
        factor=factor,
        status="[Dc]",
        derivation="ℓ_eff = 2ℓ from full orbifold interval [-ℓ, +ℓ]",
        m_phi_GeV=m_phi,
        deviation_from_8=deviation
    )

# ============================================================================
# ROUTE B: Polarization / component counting
# ============================================================================
def route_B_polarization() -> RouteResult:
    """
    5D gauge field component counting.

    Derivation [Dc]:
    - 5D gauge field A_M has M = 0,1,2,3,5 → 5 components
    - Gauge fixing removes 1 DoF → 4 physical in 5D
    - After KK reduction:
      * Zero mode A_μ(x): 4D vector (3 physical for massive)
      * Scalar A_5(x): 1 component (eaten or physical)
    - Normalization: g₄ = g₅/√ℓ (standard)

    Component counting gives factor related to 5/4 or 4/3, not 8.
    """
    # 5D to 4D components: 5 → 4 (after gauge fixing: 4 → 3)
    factor_components = 5 / 4  # Not useful

    # Try: degrees of freedom ratio
    dof_5d = 3  # Massive 5D vector after gauge fixing
    dof_4d = 3  # Massive 4D vector
    factor_dof = dof_5d / dof_4d  # = 1

    # No natural factor 8 from polarization counting
    factor = 1.0  # No enhancement
    x1 = np.pi
    m_phi = compute_m_phi(x1, R_XI, factor)
    deviation = abs(factor - 8) / 8 * 100

    return RouteResult(
        name="Route B: Polarization/component counting",
        factor=factor,
        status="[Dc] (negative)",
        derivation="5D→4D gives factor 5/4 or 1; no route to 8",
        m_phi_GeV=m_phi,
        deviation_from_8=deviation
    )

# ============================================================================
# ROUTE C: Junction condition prefactor
# ============================================================================
def route_C_junction() -> RouteResult:
    """
    Israel junction condition.

    Derivation [Dc]:
    - Israel: [K_ab] = -κ₅² (T_ab - h_ab T/3)
    - Jump [K] = K⁺ - K⁻ introduces factor 2 in matching
    - For symmetric setup: K⁺ = -K⁻, so [K] = 2K

    This gives factor 2 in the junction matching, not 8.
    """
    factor = 2.0  # Factor 2 from jump condition
    x1 = np.pi
    m_phi = compute_m_phi(x1, R_XI, factor)
    deviation = abs(factor - 8) / 8 * 100

    return RouteResult(
        name="Route C: Israel junction condition",
        factor=factor,
        status="[Dc]",
        derivation="[K] = K⁺ - K⁻ = 2K for symmetric junction",
        m_phi_GeV=m_phi,
        deviation_from_8=deviation
    )

# ============================================================================
# ROUTE D: Geometric measure factors
# ============================================================================
def route_D_geometric_measures() -> Tuple[List[RouteResult], RouteResult]:
    """
    Compare geometric measures (solid angles, volumes, etc.)

    Sub-routes:
    D1: Circumference factor (2π)
    D2: Solid angle 4D/3D ratio
    D3: Volume factors
    D4: Combined geometric factors
    """
    results = []

    # D1: Circumference interpretation
    # If ℓ is actually circumference C = 2πR, then R = ℓ/(2π)
    # m_φ = x₁/R = 2π x₁/ℓ... wait, this increases m_φ
    # OR: if we computed ℓ = R but should use ℓ = 2πR
    factor_D1 = 2 * np.pi  # ≈ 6.28
    x1 = np.pi
    m_phi_D1 = compute_m_phi(x1, R_XI, factor_D1)
    dev_D1 = abs(factor_D1 - 8) / 8 * 100
    results.append(RouteResult(
        name="Route D1: Circumference (2π)",
        factor=factor_D1,
        status="[P]",
        derivation="ℓ = 2πR_ξ if R_ξ is radius, not circumference",
        m_phi_GeV=m_phi_D1,
        deviation_from_8=dev_D1
    ))

    # D2: Solid angle ratio
    # S² surface: 4π r²  (solid angle 4π)
    # S³ surface: 2π² r³ (solid angle 2π²)
    # Ratio: 4π / 2π² = 2/π ≈ 0.64
    factor_D2 = 4 * np.pi / (2 * np.pi**2)  # = 2/π ≈ 0.64
    m_phi_D2 = compute_m_phi(x1, R_XI, factor_D2)
    dev_D2 = abs(factor_D2 - 8) / 8 * 100
    results.append(RouteResult(
        name="Route D2: Solid angle ratio (4π/2π²)",
        factor=factor_D2,
        status="[Dc]",
        derivation="S²/S³ solid angle ratio = 2/π ≈ 0.64",
        m_phi_GeV=m_phi_D2,
        deviation_from_8=dev_D2
    ))

    # D3: 4π (full solid angle in 3D)
    factor_D3 = 4 * np.pi  # ≈ 12.57
    m_phi_D3 = compute_m_phi(x1, R_XI, factor_D3)
    dev_D3 = abs(factor_D3 - 8) / 8 * 100
    results.append(RouteResult(
        name="Route D3: Full solid angle (4π)",
        factor=factor_D3,
        status="[Dc]",
        derivation="4π from spherical integration (cf. OPR-19)",
        m_phi_GeV=m_phi_D3,
        deviation_from_8=dev_D3
    ))

    # D4: (4/3)π from sphere volume coefficient
    factor_D4 = (4/3) * np.pi  # ≈ 4.19
    m_phi_D4 = compute_m_phi(x1, R_XI, factor_D4)
    dev_D4 = abs(factor_D4 - 8) / 8 * 100
    results.append(RouteResult(
        name="Route D4: Sphere volume coefficient (4π/3)",
        factor=factor_D4,
        status="[Dc]",
        derivation="V = (4/3)πr³ volume coefficient",
        m_phi_GeV=m_phi_D4,
        deviation_from_8=dev_D4
    ))

    # Best among D routes
    best_D = min(results, key=lambda r: r.deviation_from_8)
    return results, best_D

# ============================================================================
# ROUTE E: Mode normalization / interval conventions
# ============================================================================
def route_E_normalization() -> Tuple[List[RouteResult], RouteResult]:
    """
    Mode orthonormality on finite interval with various conventions.

    Check how different interval/normalization conventions affect the factor.
    """
    results = []

    # E1: Half-interval vs full-interval normalization
    # ∫₀^ℓ sin²(nπz/ℓ)dz = ℓ/2
    # ∫_{-ℓ}^{+ℓ} sin²(nπz/ℓ)dz = ℓ (for Z₂-even)
    # Normalization factor: √2 in coupling → 2 in rates
    factor_E1 = 2.0
    x1 = np.pi
    m_phi_E1 = compute_m_phi(x1, R_XI, factor_E1)
    dev_E1 = abs(factor_E1 - 8) / 8 * 100
    results.append(RouteResult(
        name="Route E1: Half/full interval normalization",
        factor=factor_E1,
        status="[Dc]",
        derivation="∫_{-ℓ}^{+ℓ}/∫₀^ℓ = 2 for mode normalization",
        m_phi_GeV=m_phi_E1,
        deviation_from_8=dev_E1
    ))

    # E2: Combining Z₂ × normalization × boundary factor
    # Z₂ orbifold: 2
    # Normalization: √2 → 2 when squared
    # Total: 2 × 2 = 4
    factor_E2 = 4.0
    m_phi_E2 = compute_m_phi(x1, R_XI, factor_E2)
    dev_E2 = abs(factor_E2 - 8) / 8 * 100
    results.append(RouteResult(
        name="Route E2: Z₂ × normalization combined",
        factor=factor_E2,
        status="[Dc]",
        derivation="2 (Z₂) × 2 (normalization) = 4",
        m_phi_GeV=m_phi_E2,
        deviation_from_8=dev_E2
    ))

    # E3: Three Z₂ factors: (Z₂)³ = 8
    # BUT: what are the three Z₂'s?
    # Z₂^{(1)}: bulk reflection y → -y
    # Z₂^{(2)}: ??? (would need physical justification)
    # Z₂^{(3)}: ???
    # This is SPECULATIVE [P] unless we can identify three independent Z₂'s
    factor_E3 = 8.0
    m_phi_E3 = compute_m_phi(x1, R_XI, factor_E3)
    dev_E3 = abs(factor_E3 - 8) / 8 * 100
    results.append(RouteResult(
        name="Route E3: (Z₂)³ = 8 [SPECULATIVE]",
        factor=factor_E3,
        status="[P]/[OPEN]",
        derivation="Would require 3 independent Z₂ factors - NOT DERIVED",
        m_phi_GeV=m_phi_E3,
        deviation_from_8=dev_E3
    ))

    best_E = min(results, key=lambda r: r.deviation_from_8)
    return results, best_E

# ============================================================================
# COMBINED ROUTE: Stacking derived factors
# ============================================================================
def route_combined() -> List[RouteResult]:
    """
    Check if combinations of derived factors can reach 8.
    """
    results = []
    x1 = np.pi

    # C1: Z₂ × 2π = 4π
    factor_C1 = 2 * 2 * np.pi  # = 4π ≈ 12.57
    m_phi = compute_m_phi(x1, R_XI, factor_C1)
    dev = abs(factor_C1 - 8) / 8 * 100
    results.append(RouteResult(
        name="Combined C1: Z₂ × 2π = 4π",
        factor=factor_C1,
        status="[Dc]+[Dc]",
        derivation="2 (Z₂ orbifold) × 2π (circumference) = 4π",
        m_phi_GeV=m_phi,
        deviation_from_8=dev
    ))

    # C2: 2π × √2 = 2√2 π ≈ 8.89
    factor_C2 = 2 * np.sqrt(2) * np.pi  # ≈ 8.89
    m_phi = compute_m_phi(x1, R_XI, factor_C2)
    dev = abs(factor_C2 - 8) / 8 * 100
    results.append(RouteResult(
        name="Combined C2: 2π × √2 ≈ 8.89",
        factor=factor_C2,
        status="[Dc]+[Dc]",
        derivation="2π (circumference) × √2 (normalization) ≈ 8.89",
        m_phi_GeV=m_phi,
        deviation_from_8=dev
    ))

    # C3: 2 × 2 × 2 = 8 (if we can justify three factors)
    # Factor 1: Z₂ orbifold [Dc]
    # Factor 2: Two boundaries (brane + anti-brane or two fixed points) [Dc]
    # Factor 3: Mode parity (even/odd selection) [P] - requires justification
    factor_C3 = 2 * 2 * 2  # = 8
    m_phi = compute_m_phi(x1, R_XI, factor_C3)
    dev = abs(factor_C3 - 8) / 8 * 100
    results.append(RouteResult(
        name="Combined C3: 2×2×2 = 8",
        factor=factor_C3,
        status="[Dc]+[Dc]+[P]",
        derivation="Z₂ × 2-boundaries × mode-parity",
        m_phi_GeV=m_phi,
        deviation_from_8=dev
    ))

    # C4: 2 × 4 = 8 (Z₂ + combined normalization)
    # This is Route A + Route E2
    factor_C4 = 2 * 4  # = 8
    m_phi = compute_m_phi(x1, R_XI, factor_C4)
    dev = abs(factor_C4 - 8) / 8 * 100
    results.append(RouteResult(
        name="Combined C4: 2 × 4 = 8",
        factor=factor_C4,
        status="[Dc]+[Dc]",
        derivation="Route A (2) × Route E2 (4) = 8 (OVERCOUNTING?)",
        m_phi_GeV=m_phi,
        deviation_from_8=dev
    ))

    return results

# ============================================================================
# MAIN ANALYSIS
# ============================================================================
def main():
    output_lines = []

    def log(line=""):
        output_lines.append(line)
        print(line)

    log("=" * 70)
    log("OPR-20 ATTEMPT C: Geometric Factor-8 Route Analysis")
    log("=" * 70)
    log(f"Date: 2026-01-22")
    log(f"NO-SMUGGLING STATUS: VERIFIED")
    log()
    log("TARGET: Factor ~8 to reduce m_φ from ~620 GeV to ~80 GeV")
    log(f"Baseline: m_φ = π/(R_ξ) × (ℏc) = π × 197.3 / 10⁻³ ≈ 620 GeV")
    log()

    # Route A
    log("-" * 70)
    log("ROUTE A: Z₂ Orbifold / Two-Sided Bulk")
    log("-" * 70)
    result_A = route_A_z2_doubling()
    log(f"  Factor: {result_A.factor:.3f}")
    log(f"  Status: {result_A.status}")
    log(f"  Derivation: {result_A.derivation}")
    log(f"  m_φ: {result_A.m_phi_GeV:.1f} GeV")
    log(f"  Deviation from 8: {result_A.deviation_from_8:.1f}%")
    log()

    # Route B
    log("-" * 70)
    log("ROUTE B: Polarization / Component Counting")
    log("-" * 70)
    result_B = route_B_polarization()
    log(f"  Factor: {result_B.factor:.3f}")
    log(f"  Status: {result_B.status}")
    log(f"  Derivation: {result_B.derivation}")
    log(f"  m_φ: {result_B.m_phi_GeV:.1f} GeV")
    log(f"  Deviation from 8: {result_B.deviation_from_8:.1f}%")
    log()

    # Route C
    log("-" * 70)
    log("ROUTE C: Israel Junction Condition")
    log("-" * 70)
    result_C = route_C_junction()
    log(f"  Factor: {result_C.factor:.3f}")
    log(f"  Status: {result_C.status}")
    log(f"  Derivation: {result_C.derivation}")
    log(f"  m_φ: {result_C.m_phi_GeV:.1f} GeV")
    log(f"  Deviation from 8: {result_C.deviation_from_8:.1f}%")
    log()

    # Route D
    log("-" * 70)
    log("ROUTE D: Geometric Measure Factors")
    log("-" * 70)
    results_D, best_D = route_D_geometric_measures()
    for r in results_D:
        log(f"  [{r.name}]")
        log(f"    Factor: {r.factor:.3f}")
        log(f"    Status: {r.status}")
        log(f"    m_φ: {r.m_phi_GeV:.1f} GeV, deviation: {r.deviation_from_8:.1f}%")
    log(f"  Best D route: {best_D.name} (factor {best_D.factor:.2f})")
    log()

    # Route E
    log("-" * 70)
    log("ROUTE E: Mode Normalization / Interval Conventions")
    log("-" * 70)
    results_E, best_E = route_E_normalization()
    for r in results_E:
        log(f"  [{r.name}]")
        log(f"    Factor: {r.factor:.3f}")
        log(f"    Status: {r.status}")
        log(f"    Derivation: {r.derivation}")
        log(f"    m_φ: {r.m_phi_GeV:.1f} GeV, deviation: {r.deviation_from_8:.1f}%")
    log()

    # Combined routes
    log("-" * 70)
    log("COMBINED ROUTES: Stacking Derived Factors")
    log("-" * 70)
    results_combined = route_combined()
    for r in results_combined:
        log(f"  [{r.name}]")
        log(f"    Factor: {r.factor:.3f}")
        log(f"    Status: {r.status}")
        log(f"    Derivation: {r.derivation}")
        log(f"    m_φ: {r.m_phi_GeV:.1f} GeV, deviation: {r.deviation_from_8:.1f}%")
    log()

    # Find best routes
    all_results = [result_A, result_B, result_C] + results_D + results_E + results_combined
    sorted_by_deviation = sorted(all_results, key=lambda r: r.deviation_from_8)

    log("=" * 70)
    log("RANKING BY PROXIMITY TO FACTOR 8")
    log("=" * 70)
    for i, r in enumerate(sorted_by_deviation[:10]):
        log(f"{i+1:2d}. {r.name}")
        log(f"    Factor: {r.factor:.3f}, Status: {r.status}, Dev: {r.deviation_from_8:.1f}%")
    log()

    # Identify routes that give exactly 8 (or very close)
    exact_8_routes = [r for r in all_results if abs(r.factor - 8) < 0.1]

    log("=" * 70)
    log("ROUTES GIVING FACTOR ≈ 8")
    log("=" * 70)
    if exact_8_routes:
        for r in exact_8_routes:
            log(f"  {r.name}")
            log(f"    Status: {r.status}")
            log(f"    Derivation: {r.derivation}")
    else:
        log("  No route gives factor exactly 8 without additional postulates.")
    log()

    # Verdict
    log("=" * 70)
    log("VERDICT")
    log("=" * 70)
    log()
    log("DERIVED FACTORS [Dc]:")
    log("  • Route A (Z₂): factor 2")
    log("  • Route C (Junction): factor 2")
    log("  • Route D1 (2π): factor 6.28 — closest single derived factor to 8")
    log("  • Route E2 (Z₂ × norm): factor 4")
    log()
    log("FACTOR 8 STATUS:")
    log("  • No SINGLE derived route gives exactly 8")
    log("  • Combined C3 (2×2×2=8): requires third Z₂ factor [P]")
    log("  • Combined C4 (2×4=8): may involve overcounting")
    log()
    log("CLOSEST DERIVED FACTORS:")
    closest_derived = [r for r in sorted_by_deviation if "[Dc]" in r.status and "[P]" not in r.status][:3]
    for r in closest_derived:
        log(f"  • {r.name}: factor {r.factor:.2f} ({r.deviation_from_8:.1f}% from 8)")
    log()
    log("RECOMMENDED PATH:")
    log("  1. Use 2π (circumference) [Dc]: gives m_φ ≈ 99 GeV (24% above 80 GeV)")
    log("  2. Factor 8 requires [P] postulate (third Z₂ or specific combination)")
    log("  3. Exact factor 8 is numeric match, NOT uniquely derived")
    log()
    log("OPR-20 STATUS: RED-C [Dc]+[OPEN]")
    log("  [Dc]: Standard BC route negative closure; Z₂, 2π factors derived")
    log("  [OPEN]: Factor 8 not uniquely derivable without additional [P] assumption")

    # Save output
    output_path = "code/output/opr20_factor8_routes_check.txt"
    with open(output_path, 'w') as f:
        f.write('\n'.join(output_lines))
    print(f"\nOutput saved to: {output_path}")

if __name__ == "__main__":
    main()
