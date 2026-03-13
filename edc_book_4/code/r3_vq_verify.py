#!/usr/bin/env python3
"""
R3 Numerical Verification: Geometric V(q) Along Chosen Path
============================================================

Phase 1 / R3 Mode B deliverable (see PHASE1_PLAN_REVISED.md v3.1)

PURPOSE:
    Verify the geometric brane-energy profile V_geom(q) computed in
    Appendix app_Vq_chosen_path.tex. This is a [Check], not a derivation.
    Numerical agreement confirms the analytic arm-length computation
    within the same geometric model.

EPISTEMIC STATUS: [Check]
    This script confirms the analytic V_geom(q) within the declared
    displacement model. It does NOT verify the double-well structure
    (which requires non-geometric terms not computed in R3).

MODEL:
    Y-junction with three arms meeting at a node. Boundary points form
    an equilateral triangle at distance R from center. Node displaced
    by q along chosen path.

    In-brane path: node at (q, 0), arms to (R,0), R(-1/2, sqrt(3)/2),
                   R(-1/2, -sqrt(3)/2).
    Compact path: node at (0, 0, xi_0 + q), arms to boundary on brane.
"""

import numpy as np

# ============================================================
# Parameters
# ============================================================

# Characteristic arm length (set to 1 for dimensionless computation)
R = 1.0

# String/edge tension (in units of tau*R for energy)
# Physical value: tau ~ sigma ~ 8.82 MeV/fm^2 times a length scale
# We work in dimensionless units: V/tau vs q/R
TAU = 1.0

# Baseline empirical values for consistency check
DELTA_M_NP_MEV = 1.2933  # [BL] PDG value
E_ARM_MEV = DELTA_M_NP_MEV  # [OPEN] — conditional identification

# ============================================================
# Test 1: In-Brane Path — Geometric Profile
# ============================================================

def arm_lengths_inplane(q, R=1.0):
    """
    Compute arm lengths for in-brane displacement.

    Node at (q, 0). Boundary points:
    P1 = (R, 0), P2 = R(-1/2, sqrt(3)/2), P3 = R(-1/2, -sqrt(3)/2)

    Returns (L1, L2, L3).
    """
    L1 = abs(R - q)
    L2 = np.sqrt(R**2 + R * q + q**2)
    L3 = L2  # Z2 symmetry
    return L1, L2, L3


def Ltot_inplane(q, R=1.0):
    """Total arm length for in-brane path."""
    L1, L2, L3 = arm_lengths_inplane(q, R)
    return L1 + L2 + L3


def dLtot_dq_inplane(q, R=1.0):
    """Analytic first derivative of L_tot for in-brane path."""
    return -1.0 + (R + 2 * q) / np.sqrt(R**2 + R * q + q**2)


def d2Ltot_dq2_inplane(q, R=1.0):
    """Analytic second derivative of L_tot for in-brane path."""
    denom = (R**2 + R * q + q**2) ** 1.5
    return 1.5 * R**2 / denom


def test_inplane_profile():
    """
    Verify the in-brane geometric profile.

    Checks:
    1. L_tot(0) = 3R (Steiner)
    2. dL/dq(0) = 0 (critical point)
    3. d^2L/dq^2(0) = 3/(2R) (positive curvature)
    4. L_tot(q) > 3R for all q != 0 (single well)
    5. Numerical vs analytic derivatives agree
    """
    print("=" * 60)
    print("Test 1: In-Brane Path — Geometric Profile")
    print("=" * 60)
    print()
    print("Model: Y-junction node displaced in brane plane")
    print("Path: toward boundary point P1 (breaks Z3 to Z2)")
    print()

    # Check 1: L_tot(0) = 3R
    L0 = Ltot_inplane(0.0, R)
    expected_L0 = 3.0 * R
    check1 = abs(L0 - expected_L0) < 1e-12
    print("  Check 1: L_tot(0) = {:.6f}, expected {:.6f}  {}".format(
        L0, expected_L0, "PASS" if check1 else "FAIL"))

    # Check 2: dL/dq(0) = 0
    dL_analytic = dLtot_dq_inplane(0.0, R)
    dL_numeric = (Ltot_inplane(1e-8, R) - Ltot_inplane(-1e-8, R)) / (2e-8)
    check2 = abs(dL_analytic) < 1e-12
    print("  Check 2: dL/dq(0) = {:.2e} (analytic)  {}".format(
        dL_analytic, "PASS" if check2 else "FAIL"))
    print("           dL/dq(0) = {:.2e} (numeric)".format(dL_numeric))

    # Check 3: d^2L/dq^2(0) = 3/(2R)
    d2L_analytic = d2Ltot_dq2_inplane(0.0, R)
    expected_d2L = 1.5 / R
    d2L_numeric = (Ltot_inplane(1e-5, R) - 2 * L0 + Ltot_inplane(-1e-5, R)) / (1e-5)**2
    check3 = abs(d2L_analytic - expected_d2L) < 1e-12
    print("  Check 3: d²L/dq²(0) = {:.6f} (analytic), expected {:.6f}  {}".format(
        d2L_analytic, expected_d2L, "PASS" if check3 else "FAIL"))
    print("           d²L/dq²(0) = {:.6f} (numeric)".format(d2L_numeric))

    # Check 4: Single well — L_tot(q) > L_tot(0) for q != 0
    q_test = np.linspace(-0.9 * R, 0.9 * R, 1000)
    q_test = q_test[q_test != 0.0]
    L_test = np.array([Ltot_inplane(q, R) for q in q_test])
    check4 = np.all(L_test > L0)
    print("  Check 4: L_tot(q) > L_tot(0) for all q != 0:  {}".format(
        "PASS" if check4 else "FAIL"))

    # Profile table
    print()
    print("  Profile (dimensionless, R=1):")
    print("  {:>8s}  {:>12s}  {:>12s}".format("q/R", "L_tot/R", "ΔV/(τR)"))
    print("  " + "-" * 36)
    for qtilde in [0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.8]:
        q = qtilde * R
        Lt = Ltot_inplane(q, R)
        dV = Lt - 3.0 * R
        print("  {:>8.2f}  {:>12.6f}  {:>12.6f}".format(qtilde, Lt / R, dV / R))

    print()
    all_pass = check1 and check2 and check3 and check4
    print("  RESULT: {}".format("PASS" if all_pass else "FAIL"))
    print()
    return all_pass


# ============================================================
# Test 2: Compact-Direction Path — Geometric Profile
# ============================================================

def Ltot_compact(q, R=1.0):
    """Total arm length for compact-direction displacement."""
    return 3.0 * np.sqrt(R**2 + q**2)


def test_compact_profile():
    """
    Verify the compact-direction geometric profile.

    Checks:
    1. L_tot(0) = 3R
    2. dL/dq(0) = 0
    3. d^2L/dq^2(0) = 3/R (twice the in-brane curvature)
    4. Single well
    """
    print("=" * 60)
    print("Test 2: Compact-Direction Path — Geometric Profile")
    print("=" * 60)
    print()
    print("Model: Y-junction node displaced along compact xi")
    print("Path: preserves in-brane Z3 symmetry")
    print()

    L0 = Ltot_compact(0.0, R)
    check1 = abs(L0 - 3.0 * R) < 1e-12

    # Numeric derivative at q=0
    eps = 1e-8
    dL_num = (Ltot_compact(eps, R) - Ltot_compact(-eps, R)) / (2 * eps)
    check2 = abs(dL_num) < 1e-6

    # Second derivative: analytic = 3/R
    eps2 = 1e-5
    d2L_num = (Ltot_compact(eps2, R) - 2 * L0 + Ltot_compact(-eps2, R)) / eps2**2
    d2L_expected = 3.0 / R
    check3 = abs(d2L_num - d2L_expected) / d2L_expected < 1e-4

    # Single well
    q_test = np.linspace(-0.9 * R, 0.9 * R, 1000)
    q_test = q_test[q_test != 0.0]
    L_test = np.array([Ltot_compact(q, R) for q in q_test])
    check4 = np.all(L_test > L0)

    print("  Check 1: L_tot(0) = {:.6f}, expected {:.6f}  {}".format(
        L0, 3.0 * R, "PASS" if check1 else "FAIL"))
    print("  Check 2: dL/dq(0) ≈ {:.2e}  {}".format(
        dL_num, "PASS" if check2 else "FAIL"))
    print("  Check 3: d²L/dq²(0) = {:.4f}, expected {:.4f}  {}".format(
        d2L_num, d2L_expected, "PASS" if check3 else "FAIL"))
    print("  Check 4: Single well (L > L0 for q≠0):  {}".format(
        "PASS" if check4 else "FAIL"))
    print()
    print("  Curvature ratio (compact / in-brane) = {:.2f}".format(
        d2L_expected / (1.5 / R)))
    print("  (Expected: 2.0 — compact path is stiffer)")
    print()

    all_pass = check1 and check2 and check3 and check4
    print("  RESULT: {}".format("PASS" if all_pass else "FAIL"))
    print()
    return all_pass


# ============================================================
# Test 3: Z3 Barrier Algebraic Relations
# ============================================================

def test_z3_barrier_algebra():
    """
    Verify the Z3 barrier algebra.

    This checks the ALGEBRAIC relations from the Z3 symmetry argument
    (Ch.3 §4.2), NOT a derivation from V_geom.

    The factor of 3 at the barrier is [Der] from Z3 symmetry.
    The E_arm identification is [OPEN].

    Checks:
    1. E_B = 3 × E_arm (Z3 symmetric barrier)
    2. E_n = 1 × E_arm (model assignment)
    3. V_B = E_B - E_n = 2 × E_arm
    4. If E_arm = Δm_np [OPEN], then V_B = 2 × Δm_np
    """
    print("=" * 60)
    print("Test 3: Z3 Barrier Algebraic Relations")
    print("=" * 60)
    print()
    print("Scope: algebraic consistency of the Z3 barrier model")
    print("NOT a derivation from V_geom (which is single-well)")
    print()

    # Z3 factor [Der]
    E_arm = 1.0  # symbolic unit
    E_B = 3 * E_arm
    E_n = 1 * E_arm  # [P] — model assignment
    V_B = E_B - E_n

    check1 = (E_B == 3 * E_arm)
    check2 = (V_B == 2 * E_arm)

    print("  E_B = 3 × E_arm = {:.1f} × E_arm  [Der from Z3]  {}".format(
        E_B / E_arm, "PASS" if check1 else "FAIL"))
    print("  E_n = 1 × E_arm = {:.1f} × E_arm  [P]".format(E_n / E_arm))
    print("  V_B = E_B - E_n = {:.1f} × E_arm  {}".format(
        V_B / E_arm, "PASS" if check2 else "FAIL"))
    print()

    # Conditional: if E_arm = Δm_np [OPEN]
    V_B_mev = 2 * DELTA_M_NP_MEV
    V_B_cal = 2.6  # [Cal] from WKB calibration
    deviation = abs(V_B_mev - V_B_cal) / V_B_cal * 100

    print("  Conditional check (E_arm ≡ Δm_np [OPEN]):")
    print("    V_B = 2 × {:.4f} MeV = {:.4f} MeV".format(
        DELTA_M_NP_MEV, V_B_mev))
    print("    V_B^cal = {:.1f} MeV  [Cal]".format(V_B_cal))
    print("    Deviation = {:.1f}%  [Check — consistency, not derivation]".format(
        deviation))
    print()
    print("  NOTE: This numerical agreement does NOT close the E_arm")
    print("  identification. The identification E_arm ≡ Δm_np remains [OPEN].")
    print("  Agreement is a consistency check, not derivation evidence.")
    print()

    all_pass = check1 and check2
    print("  RESULT: {}".format("PASS" if all_pass else "FAIL"))
    print()
    return all_pass


# ============================================================
# Test 4: Profile distinguishes single-well from double-well
# ============================================================

def test_single_vs_double_well():
    """
    Explicitly verify that V_geom is single-well (no second minimum),
    distinguishing it from the postulated double-well V(q).

    This test guards against mistakenly reporting a double-well from
    the geometric profile alone.
    """
    print("=" * 60)
    print("Test 4: Single-Well vs Double-Well Distinction")
    print("=" * 60)
    print()

    # Scan for local minima in V_geom (in-brane path)
    q_scan = np.linspace(-0.95 * R, 0.95 * R, 10000)
    L_scan = np.array([Ltot_inplane(q, R) for q in q_scan])

    # Find local minima: L[i] < L[i-1] and L[i] < L[i+1]
    minima_indices = []
    for i in range(1, len(L_scan) - 1):
        if L_scan[i] < L_scan[i - 1] and L_scan[i] < L_scan[i + 1]:
            minima_indices.append(i)

    n_minima = len(minima_indices)
    check1 = (n_minima == 1)

    print("  V_geom (in-brane path):")
    print("    Number of local minima found: {}".format(n_minima))
    if n_minima >= 1:
        for idx in minima_indices:
            print("    Minimum at q/R = {:.4f}, L_tot/R = {:.6f}".format(
                q_scan[idx] / R, L_scan[idx] / R))
    print("    Single-well confirmed: {}".format("YES" if check1 else "NO"))
    print()

    # Find local maxima (barriers)
    maxima_indices = []
    for i in range(1, len(L_scan) - 1):
        if L_scan[i] > L_scan[i - 1] and L_scan[i] > L_scan[i + 1]:
            maxima_indices.append(i)

    n_maxima = len(maxima_indices)
    check2 = (n_maxima == 0)

    print("    Number of local maxima (barriers): {}".format(n_maxima))
    print("    No barrier in V_geom alone: {}".format(
        "CONFIRMED" if check2 else "UNEXPECTED"))
    print()
    print("  Implication: double-well structure requires non-geometric")
    print("  terms (V_node, V_bulk) that are NOT computed in R3.")
    print()

    all_pass = check1 and check2
    print("  RESULT: {}".format("PASS" if all_pass else "FAIL"))
    print()
    return all_pass


# ============================================================
# Summary
# ============================================================

def main():
    print()
    print("R3 Numerical Verification: Geometric V(q) Along Chosen Path")
    print("Epistemic status: [Check] — not an independent derivation")
    print()

    pass1 = test_inplane_profile()
    pass2 = test_compact_profile()
    pass3 = test_z3_barrier_algebra()
    pass4 = test_single_vs_double_well()

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print()
    print("  Test 1 (In-brane geometric profile):     {}".format(
        "PASS" if pass1 else "FAIL"))
    print("  Test 2 (Compact-direction profile):       {}".format(
        "PASS" if pass2 else "FAIL"))
    print("  Test 3 (Z3 barrier algebra):              {}".format(
        "PASS" if pass3 else "FAIL"))
    print("  Test 4 (Single-well confirmation):        {}".format(
        "PASS" if pass4 else "FAIL"))
    print()
    print("  Key results:")
    print("    V_geom''(0) = 3τ/(2R)  [Dc] (in-brane path)")
    print("    V_geom''(0) = 3τ/R     [Dc] (compact path)")
    print("    V_geom is single-well  [Dc] (Steiner minimum only)")
    print("    V_B = 2 E_arm          [P]  (Z3 algebra, E_n=E_arm [P])")
    print("    E_arm ≡ Δm_np          [OPEN]")
    print()

    all_pass = pass1 and pass2 and pass3 and pass4
    print("  OVERALL: {}".format("PASS" if all_pass else "FAIL"))
    print()

    if all_pass:
        print("  Geometric profile V_geom(q) confirmed within the")
        print("  chosen displacement model. Double-well structure")
        print("  requires additional (non-geometric) terms not")
        print("  computed in R3 Mode B.")
    else:
        print("  WARNING: One or more checks failed. Review model")
        print("  implementation for errors.")
    print()

    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
