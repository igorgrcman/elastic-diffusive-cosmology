#!/usr/bin/env python3
"""
R4 Numerical Verification: N_bonds = 3 Local Optimality
=========================================================

Phase 1 / R4 deliverable (see PHASE1_PLAN_REVISED.md v3.1)

PURPOSE:
    Verify the analytic R4 result (N_bonds = 3 minimizes contact energy)
    within the SAME declared pairwise-additive pinning model.

EPISTEMIC STATUS: [Check]
    This script confirms or falsifies the analytic result within the model.
    It is NOT an independent derivation. Numerical agreement does not
    elevate the epistemic status of the underlying model assumptions.

MODEL:
    E(n) = n * K_pin,  K_pin < 0  (binding)
    for n = 0, 1, 2, 3 bonded arm pairs

    Pairing mismatch: angular deviation from complementary alignment
    of two Y-junctions in face-to-face contact.
"""

import numpy as np
from itertools import permutations

# ============================================================
# Parameters
# ============================================================

# Pinning constant from Ch.4 (sigma -> K derivation) [Dc]
# Value: K_pin ~ 0.74 MeV per bond
K_PIN_MEV = -0.74  # negative = binding

# Baseline empirical deuteron binding energy [BL]
BD_EXP_MEV = 2.224

# Y-junction arm angles (Z3 Steiner geometry, Ch.1 [Der])
# Arms at 120-degree separation
ARM_ANGLES_DEG = np.array([0.0, 120.0, 240.0])

# ============================================================
# Test 1: Energy monotonicity within pinning model
# ============================================================

def test_energy_monotonicity():
    """
    Verify that E(n) = n * K_pin is monotonically decreasing for n = 0..3.

    This tests the analytic result of Lemma 2, within the same model.
    The four model assumptions (pairwise additivity, locality, no
    frustration, no multi-arm coupling) are built into this energy
    function by construction.
    """
    print("=" * 60)
    print("Test 1: Energy monotonicity (Lemma 2)")
    print("=" * 60)
    print()
    print("Model: E(n) = n * K_pin, with K_pin = {:.3f} MeV".format(K_PIN_MEV))
    print("Assumptions: pairwise additivity, locality,")
    print("             no frustration, no multi-arm coupling")
    print()

    energies = {}
    for n in range(4):
        e = n * K_PIN_MEV
        energies[n] = e
        print("  n = {}:  E = {:.3f} MeV".format(n, e))

    print()

    # Check monotonicity
    is_monotonic = all(energies[n] > energies[n + 1] for n in range(3))
    n_min = min(energies, key=energies.get)

    print("  Monotonically decreasing: {}".format(is_monotonic))
    print("  Minimum at n = {}".format(n_min))
    print()

    # Binding energy (positive convention)
    b_d = -energies[3]
    deviation = abs(b_d - BD_EXP_MEV) / BD_EXP_MEV * 100

    print("  B_d = 3 * |K_pin| = {:.3f} MeV".format(b_d))
    print("  B_d^exp           = {:.3f} MeV  [BL]".format(BD_EXP_MEV))
    print("  Deviation         = {:.1f}%".format(deviation))
    print()

    pass_mono = is_monotonic and (n_min == 3)
    print("  RESULT: {}".format("PASS" if pass_mono else "FAIL"))
    print()
    return pass_mono, b_d, deviation


# ============================================================
# Test 2: Pairing mismatch within restricted contact geometry
# ============================================================

def angular_mismatch(perm):
    """
    Compute total angular mismatch for a given arm pairing permutation.

    Setup: J1 and J2 face each other in contact.
    - J1 arms point outward at angles: {0, 120, 240} degrees
    - J2 arms, as seen from J1's frame, point at: {180, 300, 60} degrees
      (i.e., J2 arm k points at (ARM_ANGLES[k] + 180) mod 360)

    A bond pairs arm i of J1 with arm perm[i] of J2.
    Perfect contact: paired arms are collinear (J1 arm direction equals
    J2 arm direction as seen from J1). Mismatch = angular deviation.
    """
    j1_angles = ARM_ANGLES_DEG  # [0, 120, 240]
    # J2 arm directions as seen from J1 (face-to-face, 180-degree flip)
    j2_facing = (ARM_ANGLES_DEG + 180.0) % 360.0  # [180, 300, 60]

    total_mismatch = 0.0
    for i, j in enumerate(perm):
        # Angular separation between J1 arm i and J2 arm j (as seen by J1)
        diff = abs(j1_angles[i] - j2_facing[j])
        if diff > 180.0:
            diff = 360.0 - diff
        # Ideal contact: arms are anti-parallel (180 degrees apart).
        # Mismatch = deviation from this ideal.
        mismatch = abs(diff - 180.0)
        total_mismatch += mismatch

    return total_mismatch


def test_pairing_uniqueness():
    """
    Verify that the identity pairing minimizes angular mismatch
    among all 3! = 6 permutations. (Lemma 3)

    This operates within the restricted geometric contact model:
    fixed arm directions, angular mismatch energy only.

    The identity pairing means arm_0 of J1 pairs with arm_0 of J2, etc.
    In face-to-face contact, J1 arm 0 (at 0 deg) faces J2 arm 0
    (at 180 deg from J1's perspective) — they are collinear and
    anti-parallel, which is the ideal contact geometry.
    """
    print("=" * 60)
    print("Test 2: Pairing uniqueness (Lemma 3)")
    print("=" * 60)
    print()
    print("Model: restricted geometric contact (fixed arm directions)")
    print("Scope: uniqueness within this model only, not full 5D space")
    print()
    print("  J1 arm angles: {}".format(list(ARM_ANGLES_DEG)))
    print("  J2 arm angles (from J1 frame): {}".format(
        list((ARM_ANGLES_DEG + 180.0) % 360.0)))
    print()

    perms = list(permutations(range(3)))
    results = []

    print("  {:>12s}  {:>15s}".format("Permutation", "Mismatch (deg)"))
    print("  " + "-" * 30)

    for perm in perms:
        mismatch = angular_mismatch(perm)
        results.append((perm, mismatch))
        marker = " <-- minimum" if perm == (0, 1, 2) else ""
        print("  {:>12s}  {:>15.1f}{}".format(
            str(perm), mismatch, marker))

    print()

    # Find minimum
    min_result = min(results, key=lambda x: x[1])
    min_perm, min_mismatch = min_result

    # Check: minimum should be at identity pairing with zero mismatch
    identity_mismatch = [r[1] for r in results if r[0] == (0, 1, 2)][0]
    non_identity_mismatches = [r[1] for r in results if r[0] != (0, 1, 2)]

    id_is_zero = (identity_mismatch == 0.0)
    all_others_positive = all(m > 0.0 for m in non_identity_mismatches)
    id_is_unique_min = id_is_zero and all_others_positive

    print("  Identity pairing mismatch = 0:  {}".format(id_is_zero))
    print("  All other pairings mismatch > 0: {}".format(all_others_positive))
    print("  Identity is unique minimum:     {}".format(id_is_unique_min))
    print()
    print("  Note: The Z3 symmetry of the junction means that")
    print("  simultaneously relabeling arms of both J1 and J2 by")
    print("  the same cyclic shift maps the identity pairing to")
    print("  itself. The identity pairing is Z3-invariant.")
    print()
    print("  RESULT: {}".format("PASS" if id_is_unique_min else "FAIL"))
    print()
    return id_is_unique_min


# ============================================================
# Summary
# ============================================================

def main():
    print()
    print("R4 Numerical Verification: N_bonds = 3 Local Optimality")
    print("Epistemic status: [Check] — not an independent derivation")
    print()

    pass_mono, b_d, deviation = test_energy_monotonicity()
    pass_pairing = test_pairing_uniqueness()

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print()
    print("  Test 1 (Lemma 2 — energy monotonicity):  {}".format(
        "PASS" if pass_mono else "FAIL"))
    print("  Test 2 (Lemma 3 — pairing uniqueness):   {}".format(
        "PASS" if pass_pairing else "FAIL"))
    print()
    print("  B_d = 3|K_pin| = {:.3f} MeV".format(b_d))
    print("  B_d^exp        = {:.3f} MeV  [BL]".format(BD_EXP_MEV))
    print("  Deviation      = {:.1f}%".format(deviation))
    print()

    all_pass = pass_mono and pass_pairing
    print("  OVERALL: {}".format("PASS" if all_pass else "FAIL"))
    print()

    if all_pass:
        print("  Analytic result N_bonds = 3 confirmed within the")
        print("  pairwise-additive pinning model. This is a [Check],")
        print("  not evidence for promotion of underlying assumptions.")
    else:
        print("  WARNING: Analytic result NOT confirmed. Review model")
        print("  implementation for errors.")
    print()

    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
