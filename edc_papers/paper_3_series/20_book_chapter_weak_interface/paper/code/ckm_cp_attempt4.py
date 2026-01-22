#!/usr/bin/env python3
"""
CKM CP Phase: Attempt 4 - Z6 Refinement for delta
=================================================

Goal: Refine δ prediction from 120° (Z₃ minimal) to ~65° (PDG)
Constraint: Preserve J ~ 2.9×10⁻⁵ (already within 6% of PDG)

Test mechanisms:
M1: Z₆ = Z₂×Z₃ "half-phase" selection
M2: Non-uniform discrete charges for u/d sectors
M3: Z₂-controlled sign flips in overlaps
M4: Minimal holonomy/torsion

Author: EDC Research / Claude Code
Date: 2026-01-22
Epistemic tags: [Dc] = derived, [Cal] = calibrated, [I] = identified, [P] = postulated
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, Optional, Dict, List

# ==============================================================================
# PDG BASELINE VALUES [BL]
# ==============================================================================

# Wolfenstein parameters (PDG 2024)
LAMBDA = 0.22500
A_WOLF = 0.826
RHO_BAR = 0.159
ETA_BAR = 0.348

# Derived quantities
RHO_ETA_MAG = np.sqrt(RHO_BAR**2 + ETA_BAR**2)  # ~ 0.383
DELTA_PDG = np.arctan2(ETA_BAR, RHO_BAR)         # ~ 1.14 rad (65.4 deg)
J_PDG = 3.08e-5

# CKM magnitudes [BL]
V_US_PDG = 0.22500
V_CB_PDG = 0.04182
V_UB_PDG = 0.00369
V_CS_PDG = 0.973

# From Attempt 3: Z₃ baseline
OMEGA_3 = np.exp(2j * np.pi / 3)   # Primitive cube root: exp(2πi/3)
OMEGA_6 = np.exp(2j * np.pi / 6)   # Primitive sixth root: exp(πi/3)

# Attempt 3 result (baseline)
J_ATTEMPT3 = 2.93e-5
DELTA_ATTEMPT3 = 2*np.pi/3  # 120°

# ==============================================================================
# DATA STRUCTURES
# ==============================================================================

@dataclass
class CPRefinementResult:
    """Result from a δ refinement mechanism test."""
    mechanism: str
    tag: str
    delta_pred_deg: float
    J_pred: float
    delta_error_deg: float      # |delta_pred - delta_PDG|
    J_error_pct: float          # |J_pred - J_PDG|/J_PDG * 100
    preserves_J: bool           # |J_error| < 20%
    improves_delta: bool        # |delta_pred - 65°| < |120° - 65°|
    verdict: str
    reason: str
    charge_assignment: Optional[str] = None
    free_params: int = 0

# ==============================================================================
# MECHANISM M1: Z₆ = Z₂×Z₃ "Half-Phase" Selection
# ==============================================================================

def mechanism_m1_z6_half_phase() -> CPRefinementResult:
    """
    M1: Z₆ = Z₂×Z₃ with Z₂ selection halving the effective phase.

    Idea: Z₆ phases are ω₆ = exp(iπ/3) = exp(i·60°)
    If generations use Z₆ charges (0,1,2) instead of Z₃,
    the phase differences are 60° instead of 120°.

    But Z₆ = Z₂ × Z₃ means we have both:
    - Z₃ factor: charges mod 3
    - Z₂ factor: charges mod 2

    The "half-phase" selection: use Z₆ phases ω₆^k for charge k ∈ {0,1,2,3,4,5}
    If we assign charges (0, 2, 4) to generations (effectively Z₃ embedded in Z₆),
    the phases are ω₆^0 = 1, ω₆^2 = ω₃, ω₆^4 = ω₃² — same as Z₃.

    Alternative: assign charges (0, 1, 2) in Z₆ to get smaller phase steps.
    """
    mechanism = "M1: Z₆ half-phase selection"

    # Z₆ assignment: generations have charges (0, 1, 2)
    # This gives phase steps of 2π/6 = 60° instead of 2π/3 = 120°
    #
    # For Jarlskog: V_ij ~ |V_ij| × ω₆^(q_ui - q_dj)
    # J = Im(V_us V_cb V_ub* V_cs*)
    #
    # With (0,1,2) assignments for both sectors:
    # q_us = q_u1 - q_d2 = 0 - 1 = -1   → ω₆^(-1)
    # q_cb = q_u2 - q_d3 = 1 - 2 = -1   → ω₆^(-1)
    # q_ub* = -(q_u1 - q_d3) = -(0 - 2) = +2 → ω₆^(+2)
    # q_cs* = -(q_u2 - q_d2) = -(1 - 1) = 0  → ω₆^(0) = 1
    #
    # Total phase: ω₆^(-1-1+2+0) = ω₆^0 = 1
    # This gives J = 0! The phase cancels completely.

    # Alternative assignment: up = (0,1,2), down = (0,2,1)
    # This is the same as swapping 2nd and 3rd down generations
    # q_us = 0 - 2 = -2  → ω₆^(-2)
    # q_cb = 1 - 1 = 0   → ω₆^(0) = 1
    # q_ub* = -(0 - 1) = +1 → ω₆^(+1)
    # q_cs* = -(1 - 2) = +1 → ω₆^(+1)
    # Total: ω₆^(-2+0+1+1) = ω₆^0 = 1
    # Still zero!

    # Try: up = (0,1,2), down = (1,2,0)
    # q_us = 0 - 2 = -2  → ω₆^(-2)
    # q_cb = 1 - 0 = +1  → ω₆^(+1)
    # q_ub* = -(0 - 0) = 0 → ω₆^(0) = 1
    # q_cs* = -(1 - 2) = +1 → ω₆^(+1)
    # Total: ω₆^(-2+1+0+1) = ω₆^0 = 1
    # Still zero!

    # The problem: Z₆ with standard generation charges always gives
    # total phase = 0 mod 6 for the Jarlskog combination.
    # This is because J is rephasing-invariant and the Z₆ phases
    # form a representation of the Abelian symmetry.

    # BUT: What if we use DIFFERENT Z₆ charges for u and d sectors?
    # This is M2 (non-uniform charges), so Z₆ alone doesn't help.

    # Alternative interpretation: Z₂ factor SELECTS which Z₃ phase applies
    # If Z₂ = +1: use ω₃ phase
    # If Z₂ = -1: use ω₃* = ω₃² phase
    # This can effectively halve phases via interference

    # Simplest Z₆ half-phase model that works:
    # Postulate: effective phase in J is ω₆ instead of ω₃
    # Then δ = arg(ω₆) = π/3 = 60°

    delta_pred = np.pi/3  # 60°
    phase_factor = np.sin(delta_pred)  # sin(60°) = √3/2 ≈ 0.866
    J_pred = V_US_PDG * V_CB_PDG * V_UB_PDG * V_CS_PDG * phase_factor

    delta_pdg_deg = np.degrees(DELTA_PDG)  # ~65°
    delta_pred_deg = np.degrees(delta_pred)  # 60°
    delta_error = abs(delta_pred_deg - delta_pdg_deg)  # ~5°
    J_error_pct = abs(J_pred - J_PDG) / J_PDG * 100

    return CPRefinementResult(
        mechanism=mechanism,
        tag="M1",
        delta_pred_deg=delta_pred_deg,
        J_pred=J_pred,
        delta_error_deg=delta_error,
        J_error_pct=J_error_pct,
        preserves_J=(J_error_pct < 20),
        improves_delta=(delta_error < 55),  # 120° - 65° = 55°
        verdict="YELLOW",
        reason=f"Z₆ → δ = 60° (vs PDG 65°), J preserved; requires charge selection rule",
        charge_assignment="Postulated: effective phase = ω₆ not ω₃",
        free_params=0
    )

# ==============================================================================
# MECHANISM M2: Non-Uniform Discrete Charges
# ==============================================================================

def mechanism_m2_nonuniform_charges() -> List[CPRefinementResult]:
    """
    M2: Different Z₃ charge assignments for up vs down sectors.

    If up = (0, 1, 2) but down = (a, b, c) with (a,b,c) ≠ (0,1,2),
    the total phase in J changes.

    Test all permutations of down charges.
    """
    results = []

    # Up sector: fixed at (0, 1, 2)
    up_charges = [0, 1, 2]

    # Test all 6 permutations of down charges
    from itertools import permutations

    for perm in permutations([0, 1, 2]):
        down_charges = list(perm)

        # Calculate total Z₃ phase for Jarlskog
        # J = Im(V_us V_cb V_ub* V_cs*)
        # V_us: u(1) → d(2), charge diff = up[0] - down[1]
        # V_cb: c(2) → b(3), charge diff = up[1] - down[2]
        # V_ub*: conj of u(1) → b(3), charge diff = -(up[0] - down[2])
        # V_cs*: conj of c(2) → s(2), charge diff = -(up[1] - down[1])

        q_us = up_charges[0] - down_charges[1]
        q_cb = up_charges[1] - down_charges[2]
        q_ub_conj = -(up_charges[0] - down_charges[2])
        q_cs_conj = -(up_charges[1] - down_charges[1])

        total_q = (q_us + q_cb + q_ub_conj + q_cs_conj) % 3

        # Phase = arg(ω₃^total_q)
        phase = 2 * np.pi * total_q / 3
        delta_pred = phase if phase <= np.pi else phase - 2*np.pi
        if delta_pred < 0:
            delta_pred = abs(delta_pred)  # Take absolute value for comparison

        # Jarlskog
        phase_factor = np.sin(phase)
        J_pred = abs(V_US_PDG * V_CB_PDG * V_UB_PDG * V_CS_PDG * phase_factor)

        delta_pred_deg = np.degrees(delta_pred)
        delta_pdg_deg = np.degrees(DELTA_PDG)
        delta_error = abs(delta_pred_deg - delta_pdg_deg)
        J_error_pct = abs(J_pred - J_PDG) / J_PDG * 100 if J_pred > 0 else 100

        # Determine verdict
        if J_pred == 0:
            verdict = "RED"
            reason = "J = 0 (phases cancel)"
        elif delta_error < 10 and J_error_pct < 20:
            verdict = "GREEN"
            reason = f"δ within 10°, J within 20%"
        elif delta_error < 30 and J_error_pct < 30:
            verdict = "YELLOW"
            reason = f"Partial improvement"
        else:
            verdict = "RED"
            reason = f"No improvement over Z₃ baseline"

        charge_str = f"up=(0,1,2), down={tuple(down_charges)}, total_q={total_q}"

        results.append(CPRefinementResult(
            mechanism=f"M2: non-uniform charges",
            tag="M2",
            delta_pred_deg=delta_pred_deg,
            J_pred=J_pred,
            delta_error_deg=delta_error,
            J_error_pct=J_error_pct,
            preserves_J=(J_error_pct < 20 or J_pred == 0),
            improves_delta=(delta_error < 55),
            verdict=verdict,
            reason=reason,
            charge_assignment=charge_str,
            free_params=0
        ))

    return results

# ==============================================================================
# MECHANISM M3: Z₂-Controlled Sign Flips
# ==============================================================================

def mechanism_m3_z2_sign_flips() -> List[CPRefinementResult]:
    """
    M3: Z₂ factor introduces sign flips that modify effective phase.

    Z₆ = Z₂ × Z₃: The Z₂ factor can be interpreted as:
    - Parity/reflection in extra dimension
    - Sign of overlap amplitude

    If certain CKM elements have their phases flipped by Z₂,
    the total phase in J can change.
    """
    results = []

    # Baseline Z₃ phases: ω = exp(2πi/3)
    # V_us ~ |V_us| × ω^0 = |V_us| × 1
    # V_cb ~ |V_cb| × ω^(-1)
    # V_ub ~ |V_ub| × ω^(-2)
    # V_cs ~ |V_cs| × ω^(-1)

    # Z₂ sign flip options: each element can have sign = +1 or -1
    # 2^4 = 16 combinations, but overall sign doesn't matter for J
    # Effective: 8 distinct combinations

    # Key insight: a sign flip on V_ij means ω → -ω = ω × exp(iπ)
    # This adds π to the phase

    # Test representative combinations
    test_cases = [
        # (name, signs for [V_us, V_cb, V_ub*, V_cs*])
        ("No flips (baseline)", [1, 1, 1, 1]),
        ("Flip V_ub", [1, 1, -1, 1]),
        ("Flip V_cb", [1, -1, 1, 1]),
        ("Flip V_us", [-1, 1, 1, 1]),
        ("Flip V_cs", [1, 1, 1, -1]),
        ("Flip V_ub and V_cb", [1, -1, -1, 1]),
        ("Flip V_us and V_cs", [-1, 1, 1, -1]),
        ("Flip all four", [-1, -1, -1, -1]),
    ]

    # Baseline phases (Z₃)
    # V_us V_cb V_ub* V_cs* ~ ω^(0-1+2+1) = ω^2 ... wait, let me recalculate
    # For uniform (0,1,2) charges:
    # V_us: u(0) → s(1): charge diff = 0-1 = -1, so V_us ~ ω^(-1)
    # V_cb: c(1) → b(2): charge diff = 1-2 = -1, so V_cb ~ ω^(-1)
    # V_ub*: (u(0) → b(2))* = charge diff = -(0-2) = +2, so V_ub* ~ ω^(+2)
    # V_cs*: (c(1) → s(1))* = charge diff = -(1-1) = 0, so V_cs* ~ ω^(0) = 1
    #
    # Total: ω^(-1-1+2+0) = ω^0 = 1
    #
    # Hmm, this gives J = 0! But Attempt 3 got J ≠ 0...
    # Let me check the Attempt 3 calculation again...

    # Ah, in Attempt 3 the calculation was:
    # V_us V_cb V_ub* V_cs* ~ |...| × ω^{0-2+2+1} = |...| × ω
    # This uses different indexing. Let me be consistent.

    # Using matrix indexing V[i,j] where i = up flavor, j = down flavor:
    # V_us = V[u,s] = V[1,2], generations are (u,c,t)=(1,2,3), (d,s,b)=(1,2,3)
    # If generations carry Z₃ charges (0,1,2) for both sectors:
    # V[i,j] ~ ω^(q_i - q_j)
    #
    # V_us = V[1,2]: q=0-1=-1 → ω^(-1)
    # V_cb = V[2,3]: q=1-2=-1 → ω^(-1)
    # V_ub = V[1,3]: q=0-2=-2 → ω^(-2)
    # V_cs = V[2,2]: q=1-1=0 → ω^(0)=1
    #
    # Jarlskog: Im(V_us × V_cb × V_ub* × V_cs*)
    # = Im(ω^(-1) × ω^(-1) × ω^(+2) × ω^(0)) × |magnitudes|
    # = Im(ω^(-1-1+2+0)) × |...|
    # = Im(ω^0) × |...|
    # = Im(1) × |...|
    # = 0
    #
    # This contradicts Attempt 3! Let me re-read Attempt 3...

    # From ckm_cp_attempt3.py lines 418-424:
    # V_us = V_US_PDG * OMEGA**0           # 0.225 * 1
    # V_cb = V_CB_PDG * OMEGA**(-2)        # 0.042 * omega^{-2}
    # V_ub = V_UB_PDG * OMEGA**(-2)        # 0.0037 * omega^{-2}
    # V_cs = 0.973 * OMEGA**(-1)           # cos(theta_C) * omega^{-1}
    #
    # These are specific ASSUMED phases, not derived from charge differences!
    # The comment at line 426:
    # "Phase structure: V_us V_cb V_ub* V_cs* = |...| * omega^{0-2+2+1} = |...| * omega^1"
    #
    # So the phases are:
    # V_us ~ ω^0
    # V_cb ~ ω^(-2)
    # V_ub* ~ ω^(+2)
    # V_cs* ~ ω^(+1)
    # Total: 0-2+2+1 = 1 → ω^1
    #
    # This is NOT the same as uniform Z₃ charges! The Attempt 3 phases are:
    # V_us: q=0
    # V_cb: q=-2
    # V_ub: q=-2
    # V_cs: q=-1
    #
    # Let me decode what charge assignment gives these:
    # V[i,j] ~ ω^(q_up[i] - q_down[j])
    # V_us = V[1,2]: q_up[1] - q_down[2] = 0 → q_up[1] = q_down[2]
    # V_cb = V[2,3]: q_up[2] - q_down[3] = -2
    # V_ub = V[1,3]: q_up[1] - q_down[3] = -2
    # V_cs = V[2,2]: q_up[2] - q_down[2] = -1
    #
    # From V_us=0: q_up[1] = q_down[2]
    # From V_ub - V_cb: (q_up[1] - q_down[3]) - (q_up[2] - q_down[3]) = -2 - (-2) = 0
    #                   → q_up[1] = q_up[2]
    # From V_cs=-1: q_up[2] - q_down[2] = -1 → q_up[2] = q_down[2] - 1
    # But q_up[1] = q_down[2] and q_up[1] = q_up[2]
    # So: q_down[2] = q_down[2] - 1 → contradiction!
    #
    # Conclusion: The Attempt 3 phase assignment is INCONSISTENT with
    # any Z₃ charge assignment! It was an ad-hoc ansatz.
    #
    # This means we need to find a CONSISTENT charge assignment that gives δ ~ 65°.

    # For Z₂ sign flips analysis, let's use the Attempt 3 ansatz as baseline
    # (even though it's not derived from charges)

    baseline_phase = 2*np.pi/3  # 120° from ω^1

    for name, signs in test_cases:
        # Each sign flip adds π to the total phase
        n_flips = sum(1 for s in signs if s == -1)
        # But sign flips in pairs cancel: (-1)×(-1) = +1
        # The Jarlskog product is: V_us × V_cb × V_ub* × V_cs*
        # Sign contribution: signs[0] × signs[1] × signs[2] × signs[3]
        total_sign = np.prod(signs)

        if total_sign == 1:
            # No net phase change
            phase = baseline_phase
        else:  # total_sign == -1
            # Phase shift by π
            phase = baseline_phase + np.pi
            if phase > np.pi:
                phase = phase - 2*np.pi  # Bring to [-π, π]

        delta_pred = abs(phase)
        delta_pred_deg = np.degrees(delta_pred)

        phase_factor = np.sin(delta_pred)
        J_pred = abs(V_US_PDG * V_CB_PDG * V_UB_PDG * V_CS_PDG * phase_factor)

        delta_pdg_deg = np.degrees(DELTA_PDG)
        delta_error = abs(delta_pred_deg - delta_pdg_deg)
        J_error_pct = abs(J_pred - J_PDG) / J_PDG * 100

        if delta_pred_deg < 10 or delta_pred_deg > 170:
            verdict = "RED"
            reason = f"δ ~ {delta_pred_deg:.0f}°: J ~ 0"
        elif delta_error < 10:
            verdict = "GREEN"
            reason = f"δ within 10° of PDG"
        elif delta_error < 30:
            verdict = "YELLOW"
            reason = f"Partial improvement"
        else:
            verdict = "RED"
            reason = f"No improvement"

        results.append(CPRefinementResult(
            mechanism=f"M3: Z₂ sign flip ({name})",
            tag="M3",
            delta_pred_deg=delta_pred_deg,
            J_pred=J_pred,
            delta_error_deg=delta_error,
            J_error_pct=J_error_pct,
            preserves_J=(J_error_pct < 30),
            improves_delta=(delta_error < 55),
            verdict=verdict,
            reason=reason,
            charge_assignment=f"signs={signs}, total_sign={total_sign}",
            free_params=0
        ))

    return results

# ==============================================================================
# MECHANISM M4: Minimal Holonomy/Torsion
# ==============================================================================

def mechanism_m4_holonomy() -> CPRefinementResult:
    """
    M4: Non-trivial holonomy/torsion in internal space.

    If the Z₃ cycle has non-trivial connection (curvature/torsion),
    parallel transport gives a geometric phase different from 2π/3.

    This is a continuous deformation of the Z₃ mechanism.
    """
    mechanism = "M4: Minimal holonomy deformation"

    # For Z₃ holonomy, the natural phase is 2π/3 = 120°
    # A deformation could give any phase in principle
    #
    # Question: Is there a MINIMAL deformation that gives 65°?
    #
    # Consider: The Z₃ symmetry is exact, but the holonomy
    # depends on the metric/connection in the internal space.
    # A "minimal" deformation would be e.g. 2π/3 × (1 - ε) for small ε.
    #
    # For δ = 65° = 1.134 rad:
    # 2π/3 × (1 - ε) = 1.134
    # 2.094 × (1 - ε) = 1.134
    # 1 - ε = 0.542
    # ε = 0.458
    #
    # This is a ~46% deformation — NOT minimal!
    #
    # Alternative: The "minimal" angle in Z₆ that's closest to 65° is:
    # Z₆ phases: 0°, 60°, 120°, 180°, 240°, 300°
    # Closest to 65°: 60°
    #
    # So M4 with truly minimal deformation gives 60°, same as M1.

    # BUT: What if we consider Z₁₂ = Z₂ × Z₆?
    # Z₁₂ phases: 0°, 30°, 60°, 90°, 120°, ...
    # Closest to 65°: 60° or 90°
    # Neither is within 5°.

    # What about Z₁₈ = Z₂ × Z₉?
    # Z₁₈ phases: 0°, 20°, 40°, 60°, 80°, 100°, 120°, ...
    # Closest to 65°: 60° or 80°
    # 60° is 5° off, 80° is 15° off.

    # What about Z₃₆?
    # Z₃₆ phases: 0°, 10°, 20°, 30°, 40°, 50°, 60°, 70°, 80°, ...
    # Closest to 65°: 60° (5° off) or 70° (5° off)
    #
    # For 65° exactly, we'd need Z_n with 65 | n or close divisibility.
    # gcd(65, 360) = 5, so Z₇₂ has 65° ± 0° ... no wait.
    # 360/65 ≈ 5.54, so no integer Zn has exactly 65°.

    # Conclusion: Minimal holonomy from Zn structure gives at best 60° (Z₆)
    # or requires fine-tuned continuous deformation.

    # Report the Z₆ result as "minimal holonomy"
    delta_pred = np.pi/3  # 60° from Z₆
    phase_factor = np.sin(delta_pred)
    J_pred = V_US_PDG * V_CB_PDG * V_UB_PDG * V_CS_PDG * phase_factor

    delta_pred_deg = np.degrees(delta_pred)
    delta_pdg_deg = np.degrees(DELTA_PDG)
    delta_error = abs(delta_pred_deg - delta_pdg_deg)
    J_error_pct = abs(J_pred - J_PDG) / J_PDG * 100

    return CPRefinementResult(
        mechanism=mechanism,
        tag="M4",
        delta_pred_deg=delta_pred_deg,
        J_pred=J_pred,
        delta_error_deg=delta_error,
        J_error_pct=J_error_pct,
        preserves_J=(J_error_pct < 20),
        improves_delta=(delta_error < 55),
        verdict="YELLOW",
        reason=f"Minimal holonomy → Z₆ → δ = 60°; same as M1",
        charge_assignment="Z₆ minimal holonomy: phase = 2π/6",
        free_params=0
    )

# ==============================================================================
# EXECUTIVE SEARCH: Find Best Charge Assignment
# ==============================================================================

def executive_search() -> Tuple[CPRefinementResult, str]:
    """
    Exhaustive search over Z₃ charge assignments to find one giving δ ~ 65°.

    Returns best result and analysis.
    """
    # We want: Im(V_us V_cb V_ub* V_cs*) to have phase ~ 65° (1.134 rad)
    #
    # Let up charges = (q1, q2, q3) and down charges = (r1, r2, r3)
    # where qi, ri ∈ {0, 1, 2}
    #
    # V_us ~ ω^(q1 - r2)
    # V_cb ~ ω^(q2 - r3)
    # V_ub* ~ ω^(-(q1 - r3)) = ω^(r3 - q1)
    # V_cs* ~ ω^(-(q2 - r2)) = ω^(r2 - q2)
    #
    # Total phase exponent (mod 3):
    # (q1 - r2) + (q2 - r3) + (r3 - q1) + (r2 - q2)
    # = q1 - r2 + q2 - r3 + r3 - q1 + r2 - q2
    # = 0
    #
    # So for ANY Z₃ charge assignment, the total phase is 0 mod 3!
    # This means J = 0 or the phase is 0°, 120°, or 240°.
    #
    # The total exponent is identically 0, so phase = 0° → J = 0!
    #
    # This is a FUNDAMENTAL constraint: uniform Z₃ charges on CKM
    # CANNOT give non-trivial CP violation!

    # Wait, but Attempt 3 claimed J ≠ 0 from Z₃ phases...
    # Let me re-examine.
    #
    # Actually, the issue is that I'm computing the phase DIFFERENCE
    # in the Jarlskog product, which sums to 0.
    #
    # But J = Im(...) requires the argument of the complex number.
    # If V_us, V_cb, V_ub, V_cs each have phases φ_us, φ_cb, φ_ub, φ_cs,
    # then:
    # arg(V_us × V_cb × V_ub* × V_cs*) = φ_us + φ_cb - φ_ub - φ_cs
    #
    # For Z₃ phases: φ_ij = 2π(q_i - r_j)/3
    # Sum = (2π/3) × [(q1-r2) + (q2-r3) - (q1-r3) - (q2-r2)]
    #     = (2π/3) × [q1 - r2 + q2 - r3 - q1 + r3 - q2 + r2]
    #     = (2π/3) × 0
    #     = 0
    #
    # CONFIRMED: Z₃ charges give phase = 0 → J = 0!
    #
    # So the Attempt 3 "result" was based on an INCONSISTENT phase assignment.
    # The phases ω^0, ω^(-2), ω^(-2), ω^(-1) used in Attempt 3 do NOT
    # come from any Z₃ charge assignment!

    analysis = """
CRITICAL FINDING: Uniform Z₃ Charge Assignment Gives J = 0

Mathematical proof:
- Let up charges = (q₁, q₂, q₃), down charges = (r₁, r₂, r₃)
- CKM phases: φ_ij = (2π/3)(q_i - r_j)
- Jarlskog phase = φ_us + φ_cb - φ_ub - φ_cs
                 = (2π/3)[(q₁-r₂) + (q₂-r₃) - (q₁-r₃) - (q₂-r₂)]
                 = (2π/3) × 0
                 = 0

Conclusion: ANY Z₃ charge assignment gives J = 0!

The Attempt 3 result (J ~ 2.9×10⁻⁵) was based on an ad-hoc phase
ansatz that is NOT consistent with any Z₃ charge structure.

To get J ≠ 0 from discrete symmetry, we need:
1. DIFFERENT symmetry structure (not pure Z₃), or
2. Non-Abelian discrete symmetry, or
3. Additional interference mechanism

This is a significant correction to the Part II narrative.
"""

    # Return a "null result" indicating the search failed
    return CPRefinementResult(
        mechanism="Executive search: all Z₃ assignments",
        tag="SEARCH",
        delta_pred_deg=0.0,
        J_pred=0.0,
        delta_error_deg=65.4,
        J_error_pct=100.0,
        preserves_J=False,
        improves_delta=False,
        verdict="RED",
        reason="ALL Z₃ charge assignments give J = 0 (phase cancellation)",
        charge_assignment="Any (q₁,q₂,q₃), (r₁,r₂,r₃) ∈ Z₃³",
        free_params=0
    ), analysis

# ==============================================================================
# ALTERNATIVE: Non-Abelian A₄ or S₃ Structure
# ==============================================================================

def mechanism_alt_a4() -> CPRefinementResult:
    """
    Alternative: A₄ (alternating group on 4 elements) instead of Z₃.

    A₄ is a non-Abelian discrete group with order 12.
    It has 3D irreps that could explain three generations
    AND provide complex phases not present in Abelian groups.

    This is a standard mechanism in flavor physics literature.
    """
    mechanism = "ALT: A₄ non-Abelian structure"

    # A₄ has generators S, T with:
    # S² = T³ = (ST)³ = 1
    #
    # The 3D irrep gives complex phases from the T generator:
    # T = diag(1, ω, ω²) in the diagonal basis
    #
    # But the S generator mixes generations, so the CKM phases
    # are not simply ω^n anymore.
    #
    # In the tribimaximal mixing ansatz (from A₄):
    # The Dirac CP phase can be maximal (δ = π/2) or other values
    # depending on vacuum alignment.
    #
    # This is beyond what we can compute without detailed model.

    # Report as plausible alternative
    return CPRefinementResult(
        mechanism=mechanism,
        tag="ALT",
        delta_pred_deg=float('nan'),  # Not computed
        J_pred=float('nan'),
        delta_error_deg=float('nan'),
        J_error_pct=float('nan'),
        preserves_J=True,  # In principle
        improves_delta=True,  # In principle
        verdict="YELLOW",
        reason="A₄ can give δ ~ 65° in principle; requires full model specification",
        charge_assignment="Non-Abelian: 3D irrep of A₄",
        free_params=0
    )

# ==============================================================================
# ALTERNATIVE: Two-Channel Interference (from Track B of Attempt 3)
# ==============================================================================

def mechanism_alt_interference() -> CPRefinementResult:
    """
    Alternative: Genuine two-channel interference.

    From Attempt 3 Track B, Option 2: if V_ub receives contributions
    from two paths with equal amplitude and calibrated relative phase,
    the effective phase is φ/2 where φ ~ 134°, giving δ ~ 67°.

    This requires postulating a second path, which is not present
    in the simple overlap model.
    """
    mechanism = "ALT: Two-channel interference"

    # From Attempt 3: calibrate φ to match |ρ̄ - iη̄|
    # Equal paths: V_ub ~ exp(-d_total) × [1/2 + 1/2 × exp(iφ)]
    #            = exp(-d_total) × cos(φ/2) × exp(iφ/2)
    #
    # |V_ub| = exp(-d_total) × cos(φ/2)
    # exp(-d_total) ~ 0.0094 (from overlap model)
    # |V_ub|_PDG = 0.0037
    # cos(φ/2) = 0.0037/0.0094 ~ 0.394
    # φ/2 ~ 66.8° → φ ~ 133.6°
    #
    # Predicted δ = φ/2 ~ 67°
    # PDG δ ~ 65°
    # Agreement: within 3°!

    phi_over_2 = np.arccos(RHO_ETA_MAG)  # cos⁻¹(0.383) ~ 1.177 rad ~ 67.4°
    phi = 2 * phi_over_2

    delta_pred = phi_over_2
    delta_pred_deg = np.degrees(delta_pred)

    # J prediction
    d_total = -np.log(V_US_PDG) + (-np.log(V_CB_PDG))  # ~1.49 + 3.17 = 4.66
    vub_eff = np.exp(-d_total) * np.cos(phi_over_2)
    J_pred = V_US_PDG * V_CB_PDG * vub_eff * V_CS_PDG * np.sin(delta_pred)

    delta_pdg_deg = np.degrees(DELTA_PDG)
    delta_error = abs(delta_pred_deg - delta_pdg_deg)
    J_error_pct = abs(J_pred - J_PDG) / J_PDG * 100

    return CPRefinementResult(
        mechanism=mechanism,
        tag="ALT",
        delta_pred_deg=delta_pred_deg,
        J_pred=J_pred,
        delta_error_deg=delta_error,
        J_error_pct=J_error_pct,
        preserves_J=(J_error_pct < 30),
        improves_delta=(delta_error < 10),
        verdict="YELLOW",
        reason=f"δ = {delta_pred_deg:.1f}° (PDG: 65°); requires second path postulate",
        charge_assignment="Two equal paths with relative phase",
        free_params=1  # The path amplitude ratio or phase
    )

# ==============================================================================
# MAIN ANALYSIS
# ==============================================================================

def print_results_table(results: List[CPRefinementResult], title: str):
    """Print a formatted results table."""
    print(f"\n{'='*100}")
    print(f"{title}")
    print(f"{'='*100}")
    print(f"{'Mechanism':<40} {'δ_pred':<10} {'δ_err':<10} {'J_pred':<12} {'J_err%':<10} {'Verdict':<8}")
    print("-"*100)

    for r in results:
        delta_str = f"{r.delta_pred_deg:.1f}°" if not np.isnan(r.delta_pred_deg) else "N/A"
        delta_err_str = f"{r.delta_error_deg:.1f}°" if not np.isnan(r.delta_error_deg) else "N/A"
        J_str = f"{r.J_pred:.2e}" if not np.isnan(r.J_pred) and r.J_pred > 0 else "0"
        J_err_str = f"{r.J_error_pct:.1f}%" if not np.isnan(r.J_error_pct) else "N/A"
        print(f"{r.mechanism:<40} {delta_str:<10} {delta_err_str:<10} {J_str:<12} {J_err_str:<10} {r.verdict:<8}")

    print("-"*100)

def main():
    """Main entry point."""

    print("="*100)
    print("CKM CP PHASE: ATTEMPT 4 — Z₆ REFINEMENT FOR δ")
    print("="*100)
    print(f"\nGoal: Refine δ from 120° (Z₃) to ~65° (PDG)")
    print(f"Constraint: Preserve J ~ 3×10⁻⁵")
    print(f"\nPDG Reference:")
    print(f"  δ_PDG = {np.degrees(DELTA_PDG):.1f}°")
    print(f"  J_PDG = {J_PDG:.2e}")
    print(f"\nAttempt 3 Baseline:")
    print(f"  δ_A3 = {np.degrees(DELTA_ATTEMPT3):.1f}°")
    print(f"  J_A3 = {J_ATTEMPT3:.2e}")

    # Run all mechanisms
    all_results = []

    # M1: Z₆ half-phase
    print("\n" + "-"*50)
    print("Testing M1: Z₆ half-phase selection...")
    m1_result = mechanism_m1_z6_half_phase()
    all_results.append(m1_result)

    # M2: Non-uniform charges
    print("Testing M2: Non-uniform charge assignments...")
    m2_results = mechanism_m2_nonuniform_charges()
    all_results.extend(m2_results)

    # M3: Z₂ sign flips
    print("Testing M3: Z₂ sign flips...")
    m3_results = mechanism_m3_z2_sign_flips()
    all_results.extend(m3_results)

    # M4: Minimal holonomy
    print("Testing M4: Minimal holonomy...")
    m4_result = mechanism_m4_holonomy()
    all_results.append(m4_result)

    # Executive search
    print("Running executive search over all Z₃ assignments...")
    search_result, search_analysis = executive_search()

    # Alternative mechanisms
    print("Testing alternative mechanisms...")
    alt_a4 = mechanism_alt_a4()
    alt_interf = mechanism_alt_interference()

    # Print results
    print_results_table(all_results, "PRIMARY MECHANISMS (M1-M4)")
    print_results_table([alt_a4, alt_interf], "ALTERNATIVE MECHANISMS")

    # Executive search analysis
    print("\n" + "="*100)
    print("EXECUTIVE SEARCH ANALYSIS")
    print("="*100)
    print(search_analysis)

    # Summary
    print("\n" + "="*100)
    print("ATTEMPT 4 SUMMARY")
    print("="*100)

    print("""
KEY FINDINGS:

1. Z₃ PHASE CANCELLATION (CRITICAL):
   - For ANY Z₃ charge assignment, the Jarlskog phase sum = 0
   - This means pure Z₃ structure gives J = 0 (no CP violation)
   - The Attempt 3 result was based on inconsistent phase assignment

2. M1/M4 (Z₆ half-phase / minimal holonomy):
   - Best discrete structure gives δ = 60° (Z₆ minimal)
   - Within 5° of PDG value
   - BUT: requires selection rule that's not derived from first principles

3. M2 (Non-uniform charges):
   - All permutations tested
   - Result: J = 0 or phases 0°/120°/240° only
   - No improvement possible within Z₃

4. M3 (Z₂ sign flips):
   - Sign flips add π to phase
   - Results: 120° or 60° (=|120° - 180°|)
   - 60° case is equivalent to M1

5. ALTERNATIVE: Two-channel interference
   - Gives δ ~ 67° with one calibrated parameter
   - Requires postulating second path (not derived)
   - Best match to PDG but not fully predictive

CONCLUSION:

The simple discrete Z₃ or Z₆ structure CANNOT reproduce the PDG CP phase
from first principles with J ≠ 0. The Attempt 3 "success" was based on
an ad-hoc phase assignment that is not self-consistent.

To get physical CP violation (J ≠ 0) from discrete symmetry, we need:
- Non-Abelian discrete group (A₄, S₃, ...), or
- Additional interference mechanism, or
- Continuous parameters (holonomy angle)

RECOMMENDATION:

Option A: Accept Z₆ → δ = 60° as "close enough" (5° off)
Option B: Develop non-Abelian A₄ model (significant work)
Option C: Use two-channel interference (requires postulate)
Option D: Flag CP phase as (open) requiring further work

The safest epistemic position is Option D: acknowledge that the simple
discrete symmetry ansatz does not fully explain δ, while noting that
the *magnitude* of J is correctly predicted by the hierarchy structure.
""")

    # Return best results
    return {
        'primary': all_results,
        'alternatives': [alt_a4, alt_interf],
        'search': search_result,
        'search_analysis': search_analysis
    }

if __name__ == "__main__":
    results = main()
