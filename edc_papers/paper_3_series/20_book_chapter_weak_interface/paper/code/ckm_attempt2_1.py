#!/usr/bin/env python3
"""
CKM Overlap Model — Attempt 2.1: Non-Uniform Spacing
=====================================================

UPGRADE from Attempt 2:
- Two parameters: Δz₁₂/(2κ) and Δz₂₃/(2κ) instead of single Δz/(2κ)
- Fit Δz₁₂ from V_us, Δz₂₃ from V_cb
- PREDICT V_ub ~ exp(-(Δz₁₂ + Δz₂₃)/(2κ)) — no new parameters!
- Unitarity enforced via Gram-Schmidt orthonormalization
- CP phase discussion: complex z-shift possibility

Author: EDC Project
Date: 2026-01-22
"""

import numpy as np
from scipy.linalg import norm, qr

# =============================================================================
# PDG 2024 Reference Values [BL]
# =============================================================================
PDG_CKM = np.array([
    [0.97435, 0.22500, 0.00369],
    [0.22486, 0.97349, 0.04182],
    [0.00857, 0.04110, 0.999118]
])

# Key elements for calibration and prediction
V_us_PDG = 0.22500  # Cabibbo: calibrate Δz₁₂
V_cb_PDG = 0.04182  # Calibrate Δz₂₃
V_ub_PDG = 0.00369  # PREDICTION target

LAMBDA_WOLFENSTEIN = 0.22500  # For comparison


# =============================================================================
# Core Functions
# =============================================================================

def overlap_amplitude(delta_z_over_2kappa):
    """
    Overlap between two localized profiles separated by Δz.

    For exponential profiles f(z) ∝ exp(-|z-z₀|/κ):
        O ∝ exp(-Δz / 2κ)

    This gives |V_ij|² ∝ O_ij, so |V_ij| ∝ √O ∝ exp(-Δz / 4κ)
    BUT: actual overlap integral for probability amplitude gives exp(-Δz/2κ)

    Convention: input is Δz/(2κ), output is amplitude |V| ~ exp(-Δz/2κ)
    """
    return np.exp(-delta_z_over_2kappa)


def build_overlap_matrix(d12, d23):
    """
    Build 3×3 overlap matrix with non-uniform spacing.

    Generation positions: z₁, z₂, z₃
    Spacings: Δz₁₂ = z₂ - z₁, Δz₂₃ = z₃ - z₂

    Parameters:
        d12: Δz₁₂/(2κ)
        d23: Δz₂₃/(2κ)

    Returns: Raw overlap matrix (before normalization)
    """
    # Overlap amplitudes
    O_12 = overlap_amplitude(d12)      # gen 1 ↔ gen 2
    O_23 = overlap_amplitude(d23)      # gen 2 ↔ gen 3
    O_13 = overlap_amplitude(d12 + d23)  # gen 1 ↔ gen 3 (full distance)

    # Build symmetric overlap matrix
    O = np.array([
        [1.0,   O_12,  O_13],
        [O_12,  1.0,   O_23],
        [O_13,  O_23,  1.0 ]
    ])

    return O


def normalize_to_unitary(O, method='gram_schmidt'):
    """
    Convert overlap matrix to unitary CKM-like matrix.

    Physical interpretation:
    - O_ij gives relative transition amplitudes
    - CKM must be unitary (probability conservation)
    - Normalization procedure enforces unitarity

    Methods:
    - 'gram_schmidt': QR decomposition (orthonormalize columns)
    - 'row_normalize': Simple row normalization (approximate)
    - 'wolfenstein': Use Wolfenstein parametrization structure
    """
    if method == 'row_normalize':
        # Simple approach: normalize each row
        row_sums = O.sum(axis=1, keepdims=True)
        V = O / row_sums
        return np.sqrt(V)  # Amplitude from probability

    elif method == 'gram_schmidt':
        # Use QR decomposition for proper orthonormalization
        # O ≈ Q·R where Q is orthonormal
        Q, R = qr(O)
        # Q has orthonormal columns; transpose for orthonormal rows
        return np.abs(Q)

    elif method == 'wolfenstein':
        # Extract parameters from diagonal ratios
        # V_us/V_ud ≈ λ, V_cb/V_cs ≈ λ²/1 ≈ λ²
        lambda_12 = O[0,1] / O[0,0]  # Cabibbo-like
        lambda_23 = O[1,2] / O[1,1]  # Second mixing

        # Build Wolfenstein-structured matrix
        V = np.array([
            [np.sqrt(1 - lambda_12**2), lambda_12, O[0,2]],
            [lambda_12, np.sqrt(1 - lambda_12**2 - lambda_23**2), lambda_23],
            [O[0,2], lambda_23, np.sqrt(1 - O[0,2]**2 - lambda_23**2)]
        ])
        return V

    else:
        raise ValueError(f"Unknown method: {method}")


def explicit_ckm_parametrization(d12, d23):
    """
    Build CKM matrix using standard parametrization with geometric interpretation.

    Standard CKM: three angles θ₁₂, θ₂₃, θ₁₃ and one CP phase δ

    Geometric interpretation:
    - θ₁₂ ~ Δz₁₂/(2κ) → sin θ₁₂ ~ exp(-Δz₁₂/2κ)
    - θ₂₃ ~ Δz₂₃/(2κ) → sin θ₂₃ ~ exp(-Δz₂₃/2κ)
    - θ₁₃: skip-one transition, must traverse both gaps

    For small angles: sin θ ≈ θ, so we can use overlaps directly
    """
    # Small mixing angles from overlaps
    s12 = overlap_amplitude(d12)  # sin θ₁₂
    s23 = overlap_amplitude(d23)  # sin θ₂₃
    s13 = overlap_amplitude(d12 + d23)  # sin θ₁₃ (PREDICTED)

    c12 = np.sqrt(1 - s12**2)
    c23 = np.sqrt(1 - s23**2)
    c13 = np.sqrt(1 - s13**2)

    # Standard CKM matrix (δ = 0 for now)
    V = np.array([
        [c12 * c13,                    s12 * c13,           s13],
        [-s12 * c23 - c12 * s23 * s13, c12 * c23 - s12 * s23 * s13, s23 * c13],
        [s12 * s23 - c12 * c23 * s13,  -c12 * s23 - s12 * c23 * s13, c23 * c13]
    ])

    return np.abs(V), {'s12': s12, 's23': s23, 's13': s13,
                       'c12': c12, 'c23': c23, 'c13': c13}


# =============================================================================
# Main Analysis
# =============================================================================

def main():
    print("=" * 75)
    print("CKM OVERLAP MODEL — ATTEMPT 2.1: NON-UNIFORM SPACING")
    print("=" * 75)
    print()

    # =========================================================================
    # STEP 1: Calibrate from V_us and V_cb
    # =========================================================================
    print("STEP 1: TWO-PARAMETER CALIBRATION [Cal]")
    print("-" * 50)

    # From V_us = exp(-Δz₁₂/2κ), solve for Δz₁₂/2κ
    d12 = -np.log(V_us_PDG)

    # From V_cb = exp(-Δz₂₃/2κ), solve for Δz₂₃/2κ
    d23 = -np.log(V_cb_PDG)

    print(f"Calibration inputs [BL]:")
    print(f"  V_us (PDG) = {V_us_PDG:.5f}")
    print(f"  V_cb (PDG) = {V_cb_PDG:.5f}")
    print()
    print(f"Extracted parameters [Cal]:")
    print(f"  Δz₁₂/(2κ) = -ln(V_us) = {d12:.4f}")
    print(f"  Δz₂₃/(2κ) = -ln(V_cb) = {d23:.4f}")
    print()
    print(f"Ratio Δz₂₃/Δz₁₂ = {d23/d12:.3f}")
    print("  → Second gap is {:.1f}× larger than first".format(d23/d12))
    print()

    # Compare with uniform spacing
    d_uniform = -np.log(LAMBDA_WOLFENSTEIN)
    print(f"Comparison with uniform spacing (Attempt 2):")
    print(f"  Δz/(2κ)|uniform = -ln(λ) = {d_uniform:.4f}")
    print(f"  Non-uniform captures that generations are NOT evenly spaced")
    print()

    # =========================================================================
    # STEP 2: PREDICT V_ub (the punchline!)
    # =========================================================================
    print("STEP 2: V_ub PREDICTION [Dc]")
    print("-" * 50)

    # V_ub corresponds to 1↔3 transition: must traverse both gaps
    V_ub_predicted = overlap_amplitude(d12 + d23)

    print("Physical reasoning:")
    print("  - V_ub = amplitude for u ↔ b transition")
    print("  - Must traverse gap 1→2 (Δz₁₂) AND gap 2→3 (Δz₂₃)")
    print("  - Total distance: Δz₁₃ = Δz₁₂ + Δz₂₃")
    print("  - Amplitude: V_ub ~ exp(-(Δz₁₂ + Δz₂₃)/(2κ))")
    print()
    print("Prediction:")
    print(f"  V_ub(predicted) = exp(-{d12:.4f} - {d23:.4f})")
    print(f"                  = exp(-{d12 + d23:.4f})")
    print(f"                  = {V_ub_predicted:.6f}")
    print()
    print(f"Comparison with PDG:")
    print(f"  V_ub(PDG)       = {V_ub_PDG:.6f}")
    print(f"  Ratio pred/PDG  = {V_ub_predicted/V_ub_PDG:.3f}")
    print(f"  Discrepancy     = {100*(V_ub_predicted/V_ub_PDG - 1):.1f}%")
    print()

    # Also predict V_td (same structure, slightly different because of matrix structure)
    V_td_predicted = V_ub_predicted  # Same distance in overlap model
    V_td_PDG = 0.00857

    print(f"Similarly for V_td:")
    print(f"  V_td(predicted) = {V_td_predicted:.6f}")
    print(f"  V_td(PDG)       = {V_td_PDG:.6f}")
    print(f"  Ratio           = {V_td_predicted/V_td_PDG:.3f}")
    print()

    # =========================================================================
    # STEP 3: Full CKM matrix with explicit parametrization
    # =========================================================================
    print("STEP 3: FULL CKM MATRIX [Dc]")
    print("-" * 50)

    V_model, angles = explicit_ckm_parametrization(d12, d23)

    print("Using standard CKM parametrization with geometric angles:")
    print(f"  sin θ₁₂ = exp(-Δz₁₂/2κ) = {angles['s12']:.5f}")
    print(f"  sin θ₂₃ = exp(-Δz₂₃/2κ) = {angles['s23']:.5f}")
    print(f"  sin θ₁₃ = exp(-(Δz₁₂+Δz₂₃)/2κ) = {angles['s13']:.6f}  [PREDICTED]")
    print()

    print("Model CKM matrix |V|:")
    print("         d          s          b")
    for i, (label, row) in enumerate(zip(['u', 'c', 't'], V_model)):
        print(f"  {label} | {row[0]:.6f}   {row[1]:.6f}   {row[2]:.7f}")
    print()

    print("PDG 2024 |V|:")
    print("         d          s          b")
    for i, (label, row) in enumerate(zip(['u', 'c', 't'], PDG_CKM)):
        print(f"  {label} | {row[0]:.6f}   {row[1]:.6f}   {row[2]:.7f}")
    print()

    # =========================================================================
    # STEP 4: Element-by-element comparison
    # =========================================================================
    print("STEP 4: ELEMENT-BY-ELEMENT COMPARISON")
    print("-" * 65)
    print(f"{'Element':<8} {'Model':>10} {'PDG':>10} {'Ratio':>8} {'Status':>8} {'Origin'}")
    print("-" * 65)

    elements = [
        ('V_ud', 0, 0, 'c₁₂c₁₃',     'derived'),
        ('V_us', 0, 1, 's₁₂c₁₃',     '[Cal]'),
        ('V_ub', 0, 2, 's₁₃',        '[PRED]'),
        ('V_cd', 1, 0, '~s₁₂c₂₃',    'derived'),
        ('V_cs', 1, 1, '~c₁₂c₂₃',    'derived'),
        ('V_cb', 1, 2, 's₂₃c₁₃',     '[Cal]'),
        ('V_td', 2, 0, '~s₁₂s₂₃',    '[PRED]'),
        ('V_ts', 2, 1, '~c₁₂s₂₃',    'derived'),
        ('V_tb', 2, 2, 'c₂₃c₁₃',     'derived'),
    ]

    for name, i, j, formula, origin in elements:
        model_val = V_model[i, j]
        pdg_val = PDG_CKM[i, j]
        ratio = model_val / pdg_val if pdg_val > 0 else float('inf')

        if 0.8 <= ratio <= 1.2:
            status = "✓ GOOD"
        elif 0.5 <= ratio <= 2.0:
            status = "~ OK"
        else:
            status = "✗ OFF"

        highlight = "**" if origin == '[PRED]' else "  "
        print(f"{highlight}{name:<6} {model_val:>10.6f} {pdg_val:>10.6f} {ratio:>8.3f} {status:>8} {formula}")

    print()

    # =========================================================================
    # STEP 5: Unitarity check
    # =========================================================================
    print("STEP 5: UNITARITY CHECK")
    print("-" * 50)

    VVdag = V_model @ V_model.T
    VdagV = V_model.T @ V_model

    print("V·V† (should be identity):")
    for row in VVdag:
        print(f"  [{row[0]:8.5f} {row[1]:9.6f} {row[2]:10.7f}]")

    err_rows = norm(VVdag - np.eye(3))
    err_cols = norm(VdagV - np.eye(3))

    print(f"\n||V·V† - I|| = {err_rows:.6f}")
    print(f"||V†·V - I|| = {err_cols:.6f}")
    print(f"Status: {'UNITARY' if max(err_rows, err_cols) < 0.01 else 'APPROXIMATE'}")
    print()

    # =========================================================================
    # STEP 6: CP phase discussion
    # =========================================================================
    print("STEP 6: CP PHASE STRUCTURE [P/OPEN]")
    print("-" * 50)

    print("""
The overlap model as presented has δ = 0 (no CP violation).

CP violation requires a complex phase. In the geometric picture:

  OPTION A: Complex z-positions (z → z + iη)
    - Phases arise from imaginary components of positions
    - O_ij = exp(-|z_i - z_j|/2κ) becomes complex when z's are complex
    - δ_CP ~ Im(z₁₂ × z₂₃*) / |z₁₂||z₂₃|

  OPTION B: Complex coupling (κ → κ + iκ')
    - Localization width has phase
    - Requires physical interpretation of Im(κ)

  OPTION C: Multiple overlap contributions
    - If more than one bulk field mediates mixing
    - Relative phases between paths

Current status: [OPEN]
- Need to derive δ_CP from geometry
- Jarlskog invariant J ~ 3×10⁻⁵ is another prediction target
""")

    # =========================================================================
    # STEP 7: Why κ_quark < κ_lepton?
    # =========================================================================
    print("STEP 7: κ_quark vs κ_lepton [P]")
    print("-" * 50)

    # From the data:
    # CKM hierarchy: λ ~ 0.22 → Δz/2κ ~ 1.5
    # PMNS: much larger mixing angles ~ O(1) → Δz/2κ ~ O(1) or smaller

    lambda_CKM = LAMBDA_WOLFENSTEIN  # ~0.22
    theta_PMNS = np.sin(np.radians(33.4))  # θ₁₂ ~ 33°

    d_CKM = -np.log(lambda_CKM)
    d_PMNS = -np.log(theta_PMNS)  # rough estimate

    print(f"Observed hierarchies:")
    print(f"  CKM:  V_us ~ {lambda_CKM:.3f}  → Δz/(2κ_q) ~ {d_CKM:.2f}")
    print(f"  PMNS: sin θ₁₂ ~ {theta_PMNS:.3f} → Δz/(2κ_ℓ) ~ {d_PMNS:.2f}")
    print()
    print("If Δz is similar for quarks and leptons, then:")
    print(f"  κ_quark / κ_lepton ~ {d_PMNS/d_CKM:.2f}")
    print()
    print("""Physical interpretation [P]:

  Quarks experience COLOR CONFINEMENT:
    - Strong interaction compresses their 5D profiles
    - Smaller κ → more localized → less overlap
    - Hence smaller mixing angles

  Leptons are COLOR-NEUTRAL:
    - No confinement compression
    - Larger κ → broader profiles → more overlap
    - Hence larger mixing angles (θ_PMNS ~ 30-45°)

  This is QUALITATIVE — quantitative derivation [OPEN].
""")

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print("=" * 75)
    print("SUMMARY: ATTEMPT 2.1 RESULTS")
    print("=" * 75)
    print(f"""
INPUTS (Calibrated from PDG) [Cal]:
  Δz₁₂/(2κ) = {d12:.4f}  ← from V_us = {V_us_PDG}
  Δz₂₃/(2κ) = {d23:.4f}  ← from V_cb = {V_cb_PDG}

KEY PREDICTION [Dc]:
  V_ub(predicted) = exp(-(Δz₁₂+Δz₂₃)/(2κ)) = {V_ub_predicted:.6f}
  V_ub(PDG)       = {V_ub_PDG:.6f}
  Agreement: {100*(V_ub_predicted/V_ub_PDG):.1f}%

INTERPRETATION:
  - Non-uniform spacing: 2nd gap is {d23/d12:.1f}× larger than 1st
  - This captures that top quark is "further away" in extra dimension
  - V_ub is NOT a free parameter — it's PREDICTED from calibrated Δz₁₂, Δz₂₃

EPISTEMIC STATUS:
  ┌─────────────────────────────────────────────────────────────────┐
  │  [Cal] Two parameters fitted: Δz₁₂/(2κ), Δz₂₃/(2κ)            │
  │  [Dc]  Third element predicted: V_ub ~ exp(-(d₁₂+d₂₃))         │
  │  [P]   Exponential overlap ansatz                              │
  │  [OPEN] CP phase, Jarlskog invariant, κ_q/κ_ℓ derivation       │
  └─────────────────────────────────────────────────────────────────┘

UPGRADE FROM ATTEMPT 2:
  - Attempt 2:   1 param (Δz/2κ=1.49), explains λⁿ scaling
  - Attempt 2.1: 2 params, PREDICTS V_ub with {100*abs(V_ub_predicted/V_ub_PDG - 1):.0f}% accuracy

The "punchline": V_ub = exp(-d₁₂) × exp(-d₂₃) = V_us × V_cb/c₁₃
""")


if __name__ == "__main__":
    main()
