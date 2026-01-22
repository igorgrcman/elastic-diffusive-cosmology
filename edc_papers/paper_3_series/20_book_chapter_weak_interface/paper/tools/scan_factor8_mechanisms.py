#!/usr/bin/env python3
"""
Factor-8 Mechanism Scanner (OPR-20 Attempt 3)
=============================================

Scans SM-free candidate mechanisms for the factor C ≈ 7.75 needed to
bring Candidate A's m_φ ~ 620 GeV down to M_W ~ 80 GeV.

CRITICAL: No SM weak-scale inputs used for calibration.
The target C = 7.75 is computed from the ratio 620/80, which comes from
comparing Candidate A prediction to the known M_W. This is a CONSISTENCY
CHECK, not calibration.

Author: EDC Research / Claude Code
Date: 2026-01-22
Reference: sections/ch11_g5_ell_suppression_attempt3_factor8.tex
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple
import os

# =============================================================================
# TARGET FACTOR (for comparison only, NOT used to derive candidates)
# =============================================================================

# Candidate A prediction
M_PHI_CANDIDATE_A = 620.0  # GeV (from R_xi/r_e ~ 10^-3, x1 = pi)

# Known M_W for comparison (this is a CONSISTENCY CHECK target)
M_W_TARGET = 80.4  # GeV

# Required multiplicative correction
C_REQUIRED = M_PHI_CANDIDATE_A / M_W_TARGET  # ≈ 7.71

# =============================================================================
# CANDIDATE MECHANISMS (all SM-free)
# =============================================================================

@dataclass
class Factor8Candidate:
    """A candidate mechanism for the factor-8 correction."""
    name: str
    category: str  # (a) eigenvalue, (b) junction, (c) geometry, (d) length
    formula_str: str
    value: float
    derived: bool
    tag: str
    notes: str


def compute_candidates() -> List[Factor8Candidate]:
    """Compute all factor-8 candidates from SM-free sources."""

    candidates = []

    # =========================================================================
    # (a) Eigenvalue / BC factors
    # =========================================================================

    # Dirichlet to Neumann ratio
    x1_dirichlet = np.pi
    x1_neumann_mixed = np.pi / 2  # Dirichlet-Neumann mixed
    candidates.append(Factor8Candidate(
        name="Dirichlet/Mixed-ND",
        category="(a) eigenvalue",
        formula_str="x1_D / x1_ND = π / (π/2)",
        value=x1_dirichlet / x1_neumann_mixed,
        derived=True,
        tag="[Dc]",
        notes="Standard Sturm-Liouville eigenvalues; factor 2 too small"
    ))

    # Periodic BC comparison
    # For periodic, first non-zero mode has x1 = 2π/L; ratio depends on L
    # If we compare to unit interval: x1_periodic ~ 2π
    candidates.append(Factor8Candidate(
        name="Dirichlet/Periodic ratio",
        category="(a) eigenvalue",
        formula_str="2π / π",
        value=2.0,
        derived=True,
        tag="[Dc]",
        notes="Periodic vs Dirichlet first eigenvalue ratio"
    ))

    # Robin BC with parameter α: can tune to any value
    # x1 satisfies: x1 cot(x1) = -α for Robin BC at one end
    # For α → 0: x1 → π/2; for α → ∞: x1 → π
    # To get C = 7.75, need x1 ≈ π/7.75 ≈ 0.405
    # This requires specific α ≈ -cot(0.405)/0.405 ≈ -5.5
    candidates.append(Factor8Candidate(
        name="Robin BC (tuned)",
        category="(a) eigenvalue",
        formula_str="π / x1(α) where α tuned",
        value=7.75,  # By construction
        derived=False,
        tag="[P]",
        notes="Exact fit but parameter α must be tuned; not derived"
    ))

    # =========================================================================
    # (b) Junction / normalization factors
    # =========================================================================

    # Israel junction: sqrt(1 + α) form
    # To get C = 8: need α = 63
    alpha_for_8_sqrt = 63.0
    candidates.append(Factor8Candidate(
        name="Israel sqrt(1+α), α=63",
        category="(b) junction",
        formula_str="sqrt(1 + 63)",
        value=np.sqrt(1 + alpha_for_8_sqrt),
        derived=False,
        tag="[P]",
        notes="Junction matching; α=63 not derived from EDC"
    ))

    # Israel junction: (1 + α) form (linear correction)
    # To get C = 8: need α = 7
    alpha_for_8_linear = 7.0
    candidates.append(Factor8Candidate(
        name="Israel (1+α), α=7",
        category="(b) junction",
        formula_str="1 + 7",
        value=1 + alpha_for_8_linear,
        derived=False,
        tag="[P]",
        notes="Linear junction correction; α=7 not derived"
    ))

    # Mode normalization with BKT: (1 + κ g5^2)
    # From Attempt 2: κ g5^2 ~ c_κ × 0.4 / 5.86 MeV
    # To get factor 8, need c_κ ~ 100 (in appropriate units)
    candidates.append(Factor8Candidate(
        name="BKT normalization",
        category="(b) junction",
        formula_str="1 + κ g5^2 (tuned)",
        value=8.0,  # By construction
        derived=False,
        tag="[P]",
        notes="Brane kinetic term; requires c_κ tuning"
    ))

    # =========================================================================
    # (c) Geometric factors from discrete symmetry
    # =========================================================================

    # 2π: circumference to radius
    candidates.append(Factor8Candidate(
        name="2π (circumference)",
        category="(c) geometry",
        formula_str="2π",
        value=2 * np.pi,
        derived=True,
        tag="[Dc]",
        notes="Fundamental geometric ratio; 19% below target"
    ))

    # √2 × 2π: if Z2 contributes a √2 enhancement
    candidates.append(Factor8Candidate(
        name="√2 × 2π",
        category="(c) geometry",
        formula_str="√2 × 2π",
        value=np.sqrt(2) * 2 * np.pi,
        derived=False,
        tag="[P]",
        notes="If Z2 parity contributes √2; 15% above target"
    ))

    # √3 × 2π: if Z3 contributes √3
    candidates.append(Factor8Candidate(
        name="√3 × 2π",
        category="(c) geometry",
        formula_str="√3 × 2π",
        value=np.sqrt(3) * 2 * np.pi,
        derived=False,
        tag="[P]",
        notes="If Z3 contributes √3; 40% above target"
    ))

    # 4π: solid angle / sphere area factor
    candidates.append(Factor8Candidate(
        name="4π (solid angle)",
        category="(c) geometry",
        formula_str="4π",
        value=4 * np.pi,
        derived=True,
        tag="[Dc]",
        notes="Sphere solid angle; 62% above target"
    ))

    # 4π/3: sphere volume factor
    candidates.append(Factor8Candidate(
        name="4π/3 (sphere volume)",
        category="(c) geometry",
        formula_str="4π/3",
        value=4 * np.pi / 3,
        derived=True,
        tag="[Dc]",
        notes="Sphere volume prefactor; 46% below target"
    ))

    # 8: octahedral / 2^3
    candidates.append(Factor8Candidate(
        name="8 (octahedral/2³)",
        category="(c) geometry",
        formula_str="8 = 2³",
        value=8.0,
        derived=False,
        tag="[P]",
        notes="Number of octants; best numeric match (3% off)"
    ))

    # 8/π: lattice geometry factor
    candidates.append(Factor8Candidate(
        name="8/π",
        category="(c) geometry",
        formula_str="8/π",
        value=8 / np.pi,
        derived=False,
        tag="[P]",
        notes="Lattice-related; 67% below target"
    ))

    # π²: could arise from double integration
    candidates.append(Factor8Candidate(
        name="π²",
        category="(c) geometry",
        formula_str="π²",
        value=np.pi ** 2,
        derived=False,
        tag="[P]",
        notes="Double integral factor; 27% above target"
    ))

    # π²/4: quarter of π²
    candidates.append(Factor8Candidate(
        name="π²/4",
        category="(c) geometry",
        formula_str="π²/4",
        value=np.pi ** 2 / 4,
        derived=False,
        tag="[P]",
        notes="Quarter integral; 68% below target"
    ))

    # 3 × 2π / π = 6: from Z6?
    candidates.append(Factor8Candidate(
        name="6 (Z6 order)",
        category="(c) geometry",
        formula_str="|Z6| = 6",
        value=6.0,
        derived=False,
        tag="[P]",
        notes="Z6 group order; 22% below target"
    ))

    # 12: Z6 × Z2 order
    candidates.append(Factor8Candidate(
        name="12 (Z6 × Z2)",
        category="(c) geometry",
        formula_str="|Z6 × Z2| = 12",
        value=12.0,
        derived=False,
        tag="[P]",
        notes="Z6 × Z2 group order; 55% above target"
    ))

    # =========================================================================
    # (d) Effective length redefinition
    # =========================================================================

    # R_xi → 8 R_xi postulate
    candidates.append(Factor8Candidate(
        name="R_ξ × 8 postulate",
        category="(d) length",
        formula_str="R_ξ → 8 R_ξ",
        value=8.0,
        derived=False,
        tag="[P]",
        notes="Ad hoc rescaling; moves problem, doesn't solve it"
    ))

    # Half-wavelength vs quarter-wavelength
    candidates.append(Factor8Candidate(
        name="λ/2 vs λ/4",
        category="(d) length",
        formula_str="2 (half vs quarter wave)",
        value=2.0,
        derived=True,
        tag="[Dc]",
        notes="Wavelength ratio; factor 2 too small"
    ))

    return candidates


def rank_candidates(candidates: List[Factor8Candidate]) -> List[Tuple[Factor8Candidate, float]]:
    """Rank candidates by proximity to the target factor."""
    ranked = []
    for c in candidates:
        error = (c.value - C_REQUIRED) / C_REQUIRED * 100  # percent error
        ranked.append((c, error))

    # Sort by absolute error
    ranked.sort(key=lambda x: abs(x[1]))
    return ranked


def generate_report(ranked: List[Tuple[Factor8Candidate, float]], output_path: str):
    """Generate human-readable report."""

    lines = []
    lines.append("=" * 80)
    lines.append("OPR-20 FACTOR-8 MECHANISM SCAN REPORT")
    lines.append("=" * 80)
    lines.append("")
    lines.append("NO-SMUGGLING VERIFICATION:")
    lines.append("  - All candidates computed from SM-free inputs")
    lines.append("  - Target C = 7.71 is for COMPARISON ONLY (from 620 GeV / 80.4 GeV)")
    lines.append("  - NO candidate formula uses M_W, G_F, v, or sin²θ_W as input")
    lines.append("")
    lines.append(f"Target correction factor: C_required = {C_REQUIRED:.2f}")
    lines.append(f"  (From Candidate A: m_φ = {M_PHI_CANDIDATE_A} GeV → M_W = {M_W_TARGET} GeV)")
    lines.append("")
    lines.append("-" * 80)
    lines.append(f"{'Rank':<5} {'Candidate':<25} {'C value':<10} {'Error':<10} {'Tag':<8} {'Category'}")
    lines.append("-" * 80)

    for i, (c, error) in enumerate(ranked, 1):
        error_str = f"{error:+.1f}%"
        lines.append(f"{i:<5} {c.name:<25} {c.value:<10.3f} {error_str:<10} {c.tag:<8} {c.category}")

    lines.append("-" * 80)
    lines.append("")
    lines.append("DETAILED CANDIDATE INFORMATION:")
    lines.append("-" * 80)

    for i, (c, error) in enumerate(ranked, 1):
        lines.append(f"\n[{i}] {c.name}")
        lines.append(f"    Category: {c.category}")
        lines.append(f"    Formula:  {c.formula_str}")
        lines.append(f"    Value:    {c.value:.4f}")
        lines.append(f"    Error:    {error:+.1f}%")
        lines.append(f"    Derived:  {'YES' if c.derived else 'NO'}")
        lines.append(f"    Tag:      {c.tag}")
        lines.append(f"    Notes:    {c.notes}")

    lines.append("")
    lines.append("=" * 80)
    lines.append("SUMMARY")
    lines.append("=" * 80)

    # Find best derived and best overall
    best_derived = None
    for c, error in ranked:
        if c.derived:
            best_derived = (c, error)
            break

    best_overall = ranked[0]

    lines.append("")
    lines.append(f"Best overall match:  {best_overall[0].name}")
    lines.append(f"  C = {best_overall[0].value:.3f}, Error = {best_overall[1]:+.1f}%, Tag = {best_overall[0].tag}")
    lines.append("")

    if best_derived:
        lines.append(f"Best DERIVED [Dc]:   {best_derived[0].name}")
        lines.append(f"  C = {best_derived[0].value:.3f}, Error = {best_derived[1]:+.1f}%")
    else:
        lines.append("Best DERIVED [Dc]:   NONE within reasonable range")

    lines.append("")
    lines.append("CONCLUSION:")
    lines.append("  - No [Dc] candidate matches within 10%")
    lines.append("  - Best derived factor is 2π ≈ 6.28 (19% below target)")
    lines.append("  - Factor C = 8 is best numeric match (3% off) but [P]")
    lines.append("  - OPR-20 remains RED-C [OPEN]; attack surface narrowed")
    lines.append("")
    lines.append("=" * 80)

    report = "\n".join(lines)

    # Write to file
    with open(output_path, 'w') as f:
        f.write(report)

    return report


def main():
    """Run the factor-8 mechanism scan."""

    print("Running OPR-20 Factor-8 Mechanism Scan...")
    print(f"Target correction factor: C = {C_REQUIRED:.2f}")
    print()

    # Compute candidates
    candidates = compute_candidates()
    print(f"Computed {len(candidates)} candidates")

    # Rank by proximity to target
    ranked = rank_candidates(candidates)

    # Determine output path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "code", "output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "opr20_factor8_scan.txt")

    # Generate report
    report = generate_report(ranked, output_path)

    print(report)
    print(f"\nReport written to: {output_path}")

    return True


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
