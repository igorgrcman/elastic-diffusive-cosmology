#!/usr/bin/env python3
"""
PMNS Attempt 3: Z6 Discrete-Phase Sweep (Z2 x Z3 Refinement)
=============================================================

Date: 2026-01-22
Goal: Preserve theta23 from Attempt 2 A3, fix theta12 and theta13 using
      ONLY discrete Z6 phases (no continuous parameters).

Strategy:
- Start from A3 overlap magnitudes (which gave theta23 GREEN)
- Apply discrete phases from Z6 = Z2 x Z3:
  - Z3 phases: {1, omega, omega^2}, omega = exp(2*pi*i/3)
  - Z2 signs: {+1, -1}
- Combined: 6 possible phases per entry = 6^9 = 10,077,696 combinations
- Reduce by rephasing invariance: physical phases are entry-wise, not row/column

Key insight: Row/column phase multiplications are gauge freedoms (can be absorbed
by field redefinitions). Only ENTRY-WISE phases that CANNOT be factored as
phase_row[i] * phase_col[j] are physical.

Author: Claude Code (for Igor's EDC project)
"""

import numpy as np
from numpy.linalg import svd
from itertools import product
import sys

# ==============================================================================
# CONSTANTS
# ==============================================================================

# PDG 2024 values [BL]
PDG_SIN2_THETA12 = 0.307
PDG_SIN2_THETA23 = 0.546
PDG_SIN2_THETA13 = 0.022
PDG_J = 3.08e-5  # Jarlskog invariant magnitude

# Z3 phases
OMEGA = np.exp(2j * np.pi / 3)
Z3_PHASES = np.array([1.0, OMEGA, OMEGA**2])  # {1, omega, omega^2}

# Z2 signs
Z2_SIGNS = np.array([1.0, -1.0])

# Combined Z6 phases (6 options)
Z6_PHASES = np.array([s * z for s in Z2_SIGNS for z in Z3_PHASES])

# Phase labels for reporting
Z6_LABELS = ['+1', '+omega', '+omega^2', '-1', '-omega', '-omega^2']

# ==============================================================================
# A3 BASELINE (from Attempt 2)
# ==============================================================================

def build_a3_magnitudes():
    """
    Build the A3 overlap matrix magnitudes from Attempt 2.

    z_flavor = [0, 2pi/3, 4pi/3]  (Z3 positions)
    z_mass = [0, pi/3, 2pi/3]      (Z6 subset positions)
    kappa = 1.0

    O_ij = exp(-|z_flavor[i] - z_mass[j]| / (2*kappa))
    """
    z_flavor = np.array([0.0, 2*np.pi/3, 4*np.pi/3])
    z_mass = np.array([0.0, np.pi/3, 2*np.pi/3])
    kappa = 1.0

    O_mag = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            dist = abs(z_flavor[i] - z_mass[j])
            O_mag[i, j] = np.exp(-dist / (2 * kappa))

    return O_mag

# ==============================================================================
# UNITARIZATION AND ANGLE EXTRACTION
# ==============================================================================

def unitarize_svd(O):
    """Unitarize via SVD: O = U S V^T -> return U V^T"""
    U, S, Vt = svd(O)
    return U @ Vt

def extract_pmns_angles(U):
    """
    Extract PMNS mixing angles from unitary matrix U (PDG convention).

    sin^2(theta13) = |U_e3|^2
    sin^2(theta12) = |U_e2|^2 / (1 - |U_e3|^2)
    sin^2(theta23) = |U_mu3|^2 / (1 - |U_e3|^2)
    """
    U_abs = np.abs(U)

    sin2_13 = U_abs[0, 2]**2
    denom = 1.0 - sin2_13

    if denom < 1e-10:
        return {'sin2_theta12': np.nan, 'sin2_theta23': np.nan, 'sin2_theta13': sin2_13}

    sin2_12 = U_abs[0, 1]**2 / denom
    sin2_23 = U_abs[1, 2]**2 / denom

    return {
        'sin2_theta12': sin2_12,
        'sin2_theta23': sin2_23,
        'sin2_theta13': sin2_13
    }

def compute_jarlskog(U):
    """
    Compute Jarlskog invariant J = Im(U_e1 * U_mu2 * U_e2* * U_mu1*)
    """
    J = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))
    return J

# ==============================================================================
# REPHASING INVARIANCE CHECK
# ==============================================================================

def is_rephasing_removable(phase_matrix):
    """
    Check if a 3x3 phase matrix can be factored as:
        phase_matrix[i,j] = alpha[i] * beta[j]
    where alpha, beta are row/column phases.

    If true, phases are gauge artifacts and can be absorbed.

    Method: Check if all 2x2 minors have trivial phase.
    For a factorizable matrix: phase[i,j]*phase[k,l] = phase[i,l]*phase[k,j]
    => phase[i,j]*phase[k,l]*conj(phase[i,l])*conj(phase[k,j]) = 1
    """
    tol = 1e-10

    # Check all 2x2 minors
    for i in range(3):
        for j in range(3):
            for k in range(i+1, 3):
                for l in range(j+1, 3):
                    # Rephasing condition: P[i,j]*P[k,l] = P[i,l]*P[k,j]
                    lhs = phase_matrix[i, j] * phase_matrix[k, l]
                    rhs = phase_matrix[i, l] * phase_matrix[k, j]
                    if np.abs(lhs - rhs) > tol:
                        return False  # Not removable - physical phases present
    return True  # Removable - gauge artifact

def count_physical_phases(phase_matrix):
    """
    Count the number of independent physical phases.

    For 3x3 unitary: 9 entries - 3 row phases - 3 col phases + 1 overall = 4 physical
    But for discrete phases, we count how many 2x2 minors are non-trivial.
    """
    non_trivial = 0
    tol = 1e-10

    for i in range(3):
        for j in range(3):
            for k in range(i+1, 3):
                for l in range(j+1, 3):
                    lhs = phase_matrix[i, j] * phase_matrix[k, l]
                    rhs = phase_matrix[i, l] * phase_matrix[k, j]
                    if np.abs(lhs - rhs) > tol:
                        non_trivial += 1

    return non_trivial

# ==============================================================================
# SCORING
# ==============================================================================

def compute_score(angles):
    """
    Compute deviation score (lower is better).
    Score = sum of (|predicted - PDG| / PDG) for each angle.
    """
    if np.isnan(angles['sin2_theta12']):
        return float('inf')

    score = 0.0
    score += abs(angles['sin2_theta12'] - PDG_SIN2_THETA12) / PDG_SIN2_THETA12
    score += abs(angles['sin2_theta23'] - PDG_SIN2_THETA23) / PDG_SIN2_THETA23
    score += abs(angles['sin2_theta13'] - PDG_SIN2_THETA13) / PDG_SIN2_THETA13

    return score

def stoplight(predicted, pdg, tolerance=0.1):
    """Return stoplight color based on relative error."""
    if pdg == 0:
        return 'RED'
    rel_err = abs(predicted - pdg) / pdg
    if rel_err < tolerance:
        return 'GREEN'
    elif rel_err < 0.5:
        return 'YELLOW'
    else:
        return 'RED'

# ==============================================================================
# PHASE SWEEP - TRACK A (DISCRETE ONLY)
# ==============================================================================

def track_a_discrete_sweep(O_mag, max_report=20):
    """
    Track A: Sweep all discrete Z6 phase combinations.

    Total: 6^9 = 10,077,696 combinations.
    Filter: Only keep combinations with non-removable phases (physical).
    """
    print("=" * 70)
    print("TRACK A: DISCRETE Z6 PHASE SWEEP")
    print("=" * 70)
    print(f"Z6 phases: {Z6_LABELS}")
    print(f"Total combinations: 6^9 = {6**9:,}")
    print()

    results = []
    total_checked = 0
    removable_count = 0

    # Generate all 6^9 phase combinations
    # phase_indices[k] gives index into Z6_PHASES for matrix entry k (row-major)
    for phase_indices in product(range(6), repeat=9):
        total_checked += 1

        if total_checked % 500000 == 0:
            print(f"  Progress: {total_checked:,} / {6**9:,} ({100*total_checked/6**9:.1f}%)")

        # Build phase matrix
        phase_matrix = np.array([Z6_PHASES[i] for i in phase_indices]).reshape(3, 3)

        # Check if phases are removable by rephasing
        if is_rephasing_removable(phase_matrix):
            removable_count += 1
            continue  # Skip gauge-equivalent configurations

        # Build complex overlap matrix with phases
        O_complex = O_mag * phase_matrix

        # Unitarize
        U = unitarize_svd(O_complex)

        # Extract angles
        angles = extract_pmns_angles(U)

        # Compute score
        score = compute_score(angles)

        if score < float('inf'):
            # Compute Jarlskog
            J = compute_jarlskog(U)

            # Create phase label
            phase_label = ''.join([Z6_LABELS[i][0] if Z6_LABELS[i][0] != '+' else Z6_LABELS[i]
                                   for i in phase_indices])

            results.append({
                'phase_indices': phase_indices,
                'phase_label': phase_label,
                'angles': angles,
                'J': J,
                'score': score,
                'n_physical': count_physical_phases(phase_matrix)
            })

    print(f"\nTotal checked: {total_checked:,}")
    print(f"Removable (gauge artifacts): {removable_count:,}")
    print(f"Physical configurations: {len(results):,}")
    print()

    # Sort by score
    results.sort(key=lambda x: x['score'])

    # Report top results
    print(f"TOP {min(max_report, len(results))} RESULTS:")
    print("-" * 70)
    print(f"{'Rank':<5} {'Score':<8} {'sin2_12':<8} {'sin2_23':<8} {'sin2_13':<8} {'J':<12} {'Phys':<5}")
    print(f"{'':5} {'':8} {'(0.307)':<8} {'(0.546)':<8} {'(0.022)':<8} {'(3e-5)':<12} {'':5}")
    print("-" * 70)

    for i, r in enumerate(results[:max_report]):
        a = r['angles']
        print(f"{i+1:<5} {r['score']:<8.3f} {a['sin2_theta12']:<8.3f} {a['sin2_theta23']:<8.3f} "
              f"{a['sin2_theta13']:<8.4f} {r['J']:<12.2e} {r['n_physical']:<5}")

    return results

# ==============================================================================
# STRUCTURED PHASE PATTERNS - TRACK A VARIANTS
# ==============================================================================

def track_a_structured_patterns(O_mag):
    """
    Track A variants: Try physically motivated phase patterns.
    """
    print("\n" + "=" * 70)
    print("TRACK A VARIANTS: STRUCTURED PHASE PATTERNS")
    print("=" * 70)

    variants = []

    # Variant A3-0: Baseline (no phases) - for reference
    phase_0 = np.ones((3, 3))
    variants.append(('A3-0: No phases (baseline)', phase_0))

    # Variant A3-1: Z3 row phases (flavor rotation)
    # Row i gets phase omega^i
    phase_z3_row = np.array([[1, 1, 1],
                             [OMEGA, OMEGA, OMEGA],
                             [OMEGA**2, OMEGA**2, OMEGA**2]])
    variants.append(('A3-1: Z3 row phases', phase_z3_row))

    # Variant A3-2: Z3 column phases (mass rotation)
    phase_z3_col = np.array([[1, OMEGA, OMEGA**2],
                             [1, OMEGA, OMEGA**2],
                             [1, OMEGA, OMEGA**2]])
    variants.append(('A3-2: Z3 column phases', phase_z3_col))

    # Variant A3-3: DFT-like phases (i*j mod 3)
    phase_dft = np.array([[Z3_PHASES[(i*j) % 3] for j in range(3)] for i in range(3)])
    variants.append(('A3-3: DFT phases (i*j mod 3)', phase_dft))

    # Variant A3-4: Anti-DFT phases (-i*j mod 3)
    phase_anti_dft = np.array([[Z3_PHASES[(-i*j) % 3] for j in range(3)] for i in range(3)])
    variants.append(('A3-4: Anti-DFT phases', phase_anti_dft))

    # Variant A3-5: Z2 checkerboard (alternating signs)
    phase_checker = np.array([[(-1)**((i+j) % 2) for j in range(3)] for i in range(3)], dtype=complex)
    variants.append(('A3-5: Z2 checkerboard', phase_checker))

    # Variant A3-6: Sign on (0,2) entry (target U_e3 for theta13)
    phase_sign_e3 = np.ones((3, 3), dtype=complex)
    phase_sign_e3[0, 2] = -1
    variants.append(('A3-6: Sign flip on U_e3', phase_sign_e3))

    # Variant A3-7: omega on (0,2) entry
    phase_omega_e3 = np.ones((3, 3), dtype=complex)
    phase_omega_e3[0, 2] = OMEGA
    variants.append(('A3-7: omega on U_e3', phase_omega_e3))

    # Variant A3-8: omega^2 on (0,2) entry
    phase_omega2_e3 = np.ones((3, 3), dtype=complex)
    phase_omega2_e3[0, 2] = OMEGA**2
    variants.append(('A3-8: omega^2 on U_e3', phase_omega2_e3))

    # Variant A3-9: Tribimaximal-inspired pattern
    # Try to enhance (0,1) and (1,2) while suppressing (0,2)
    phase_tbm = np.array([[1, 1, -1],
                          [1, OMEGA, 1],
                          [1, OMEGA**2, 1]], dtype=complex)
    variants.append(('A3-9: TBM-inspired pattern', phase_tbm))

    # Variant A3-10: Phase pattern that cancels in U_e3
    # If O[0,:] has phases that interfere destructively in column 3
    phase_cancel = np.array([[1, 1, OMEGA],
                             [1, 1, OMEGA**2],
                             [1, 1, 1]], dtype=complex)
    variants.append(('A3-10: Cancel in col 3', phase_cancel))

    # Variant A3-11: Z6 diagonal pattern
    z6_6 = np.exp(2j * np.pi / 6)  # primitive 6th root
    phase_z6_diag = np.array([[1, z6_6, z6_6**2],
                              [z6_6**3, z6_6**4, z6_6**5],
                              [1, z6_6**2, z6_6**4]], dtype=complex)
    variants.append(('A3-11: Z6 diagonal', phase_z6_diag))

    print(f"\n{'Variant':<35} {'Removable?':<12} {'Score':<8} {'sin2_12':<8} {'sin2_23':<8} {'sin2_13':<8} {'J':<12}")
    print(f"{'':35} {'':12} {'':8} {'(0.307)':<8} {'(0.546)':<8} {'(0.022)':<8} {'(3e-5)':<12}")
    print("-" * 100)

    results = []
    for name, phase_matrix in variants:
        removable = is_rephasing_removable(phase_matrix)

        O_complex = O_mag * phase_matrix
        U = unitarize_svd(O_complex)
        angles = extract_pmns_angles(U)
        score = compute_score(angles)
        J = compute_jarlskog(U)

        rem_str = "YES (gauge)" if removable else "NO (physical)"

        print(f"{name:<35} {rem_str:<12} {score:<8.3f} {angles['sin2_theta12']:<8.3f} "
              f"{angles['sin2_theta23']:<8.3f} {angles['sin2_theta13']:<8.4f} {J:<12.2e}")

        results.append({
            'name': name,
            'removable': removable,
            'angles': angles,
            'score': score,
            'J': J
        })

    return results

# ==============================================================================
# TRACK B: ONE CALIBRATED PARAMETER
# ==============================================================================

def track_b_calibrated(O_mag, target='theta13'):
    """
    Track B: Allow ONE continuous parameter for calibration.

    Strategy: Scale the (0,2) entry to match theta13, check if theta12/theta23 remain OK.
    """
    print("\n" + "=" * 70)
    print("TRACK B: ONE CALIBRATED PARAMETER")
    print("=" * 70)

    print(f"\nTarget: Calibrate {target}")
    print()

    # Try scaling the (0,2) magnitude
    print("Strategy B1: Scale O[0,2] magnitude")
    print("-" * 70)

    best_score = float('inf')
    best_result = None

    for scale in np.linspace(0.01, 3.0, 300):
        O_scaled = O_mag.copy()
        O_scaled[0, 2] *= scale

        U = unitarize_svd(O_scaled)
        angles = extract_pmns_angles(U)
        score = compute_score(angles)

        if score < best_score:
            best_score = score
            best_result = {
                'scale': scale,
                'angles': angles,
                'score': score,
                'J': compute_jarlskog(U)
            }

    print(f"Best scale factor: {best_result['scale']:.3f}")
    print(f"Score: {best_result['score']:.3f}")
    a = best_result['angles']
    print(f"sin2_theta12: {a['sin2_theta12']:.3f} (PDG: 0.307) [{stoplight(a['sin2_theta12'], 0.307)}]")
    print(f"sin2_theta23: {a['sin2_theta23']:.3f} (PDG: 0.546) [{stoplight(a['sin2_theta23'], 0.546)}]")
    print(f"sin2_theta13: {a['sin2_theta13']:.4f} (PDG: 0.022) [{stoplight(a['sin2_theta13'], 0.022)}]")
    print(f"J: {best_result['J']:.2e} (PDG: 3e-5)")

    # Strategy B2: Scale the overall kappa
    print("\nStrategy B2: Vary kappa (localization scale)")
    print("-" * 70)

    z_flavor = np.array([0.0, 2*np.pi/3, 4*np.pi/3])
    z_mass = np.array([0.0, np.pi/3, 2*np.pi/3])

    best_kappa_score = float('inf')
    best_kappa_result = None

    for kappa in np.linspace(0.1, 5.0, 500):
        O = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                dist = abs(z_flavor[i] - z_mass[j])
                O[i, j] = np.exp(-dist / (2 * kappa))

        U = unitarize_svd(O)
        angles = extract_pmns_angles(U)
        score = compute_score(angles)

        if score < best_kappa_score:
            best_kappa_score = score
            best_kappa_result = {
                'kappa': kappa,
                'angles': angles,
                'score': score,
                'J': compute_jarlskog(U)
            }

    print(f"Best kappa: {best_kappa_result['kappa']:.3f}")
    print(f"Score: {best_kappa_result['score']:.3f}")
    a = best_kappa_result['angles']
    print(f"sin2_theta12: {a['sin2_theta12']:.3f} (PDG: 0.307) [{stoplight(a['sin2_theta12'], 0.307)}]")
    print(f"sin2_theta23: {a['sin2_theta23']:.3f} (PDG: 0.546) [{stoplight(a['sin2_theta23'], 0.546)}]")
    print(f"sin2_theta13: {a['sin2_theta13']:.4f} (PDG: 0.022) [{stoplight(a['sin2_theta13'], 0.022)}]")
    print(f"J: {best_kappa_result['J']:.2e} (PDG: 3e-5)")

    return {'B1': best_result, 'B2': best_kappa_result}

# ==============================================================================
# FINAL SUMMARY
# ==============================================================================

def print_summary(structured_results, track_b_results):
    """Print final summary with stoplight table."""
    print("\n" + "=" * 70)
    print("FINAL SUMMARY: STOPLIGHT TABLE")
    print("=" * 70)

    # Find best structured variant
    physical_variants = [r for r in structured_results if not r['removable']]
    if physical_variants:
        best_structured = min(physical_variants, key=lambda x: x['score'])
    else:
        best_structured = min(structured_results, key=lambda x: x['score'])

    print("\n" + "-" * 70)
    print("TRACK A BEST (DISCRETE PHASES ONLY):")
    print("-" * 70)
    print(f"Variant: {best_structured['name']}")
    print(f"Removable by rephasing: {'YES (gauge artifact)' if best_structured['removable'] else 'NO (physical)'}")
    print()

    a = best_structured['angles']
    print(f"| Angle    | Model  | PDG    | Status  |")
    print(f"|----------|--------|--------|---------|")
    print(f"| sin2_12  | {a['sin2_theta12']:.3f}  | 0.307  | {stoplight(a['sin2_theta12'], 0.307):<7} |")
    print(f"| sin2_23  | {a['sin2_theta23']:.3f}  | 0.546  | {stoplight(a['sin2_theta23'], 0.546):<7} |")
    print(f"| sin2_13  | {a['sin2_theta13']:.4f} | 0.022  | {stoplight(a['sin2_theta13'], 0.022):<7} |")
    print(f"| J        | {best_structured['J']:.2e} | 3e-5   | {stoplight(abs(best_structured['J']), 3e-5):<7} |")
    print()
    print(f"Overall Score: {best_structured['score']:.3f}")

    print("\n" + "-" * 70)
    print("TRACK B (ONE CALIBRATED PARAMETER):")
    print("-" * 70)

    b1 = track_b_results['B1']
    print(f"\nB1: Scale O[0,2] by {b1['scale']:.3f}")
    a = b1['angles']
    print(f"| Angle    | Model  | PDG    | Status  |")
    print(f"|----------|--------|--------|---------|")
    print(f"| sin2_12  | {a['sin2_theta12']:.3f}  | 0.307  | {stoplight(a['sin2_theta12'], 0.307):<7} |")
    print(f"| sin2_23  | {a['sin2_theta23']:.3f}  | 0.546  | {stoplight(a['sin2_theta23'], 0.546):<7} |")
    print(f"| sin2_13  | {a['sin2_theta13']:.4f} | 0.022  | {stoplight(a['sin2_theta13'], 0.022):<7} |")
    print(f"Overall Score: {b1['score']:.3f}")

    b2 = track_b_results['B2']
    print(f"\nB2: kappa = {b2['kappa']:.3f}")
    a = b2['angles']
    print(f"| Angle    | Model  | PDG    | Status  |")
    print(f"|----------|--------|--------|---------|")
    print(f"| sin2_12  | {a['sin2_theta12']:.3f}  | 0.307  | {stoplight(a['sin2_theta12'], 0.307):<7} |")
    print(f"| sin2_23  | {a['sin2_theta23']:.3f}  | 0.546  | {stoplight(a['sin2_theta23'], 0.546):<7} |")
    print(f"| sin2_13  | {a['sin2_theta13']:.4f} | 0.022  | {stoplight(a['sin2_theta13'], 0.022):<7} |")
    print(f"Overall Score: {b2['score']:.3f}")

    print("\n" + "=" * 70)
    print("VERDICT:")
    print("=" * 70)

    # Determine verdict
    best_track_a_score = best_structured['score']
    best_track_b_score = min(b1['score'], b2['score'])

    if best_track_a_score < 0.3:
        print("Track A SUCCESS: Discrete Z6 phases alone achieve good agreement.")
        verdict = "GREEN"
    elif best_track_a_score < 0.5:
        print("Track A PARTIAL: Some improvement, but gaps remain.")
        verdict = "YELLOW"
    else:
        if best_track_b_score < 0.3:
            print("Track A FAILED. Track B required for acceptable fit.")
            verdict = "YELLOW (calibrated)"
        else:
            print("Both tracks FAILED: Additional physics needed.")
            verdict = "RED"

    print(f"\nOverall verdict: {verdict}")

    return verdict

# ==============================================================================
# MAIN
# ==============================================================================

def main():
    print("=" * 70)
    print("PMNS ATTEMPT 3: Z6 DISCRETE-PHASE SWEEP")
    print("=" * 70)
    print()
    print("Goal: Preserve theta23 from Attempt 2 A3, fix theta12 and theta13")
    print("Method: Apply discrete Z6 = Z2 x Z3 phases to A3 overlap magnitudes")
    print()
    print("PDG 2024 targets [BL]:")
    print(f"  sin2_theta12 = {PDG_SIN2_THETA12}")
    print(f"  sin2_theta23 = {PDG_SIN2_THETA23}")
    print(f"  sin2_theta13 = {PDG_SIN2_THETA13}")
    print(f"  J = {PDG_J:.2e}")
    print()

    # Build A3 baseline magnitudes
    O_mag = build_a3_magnitudes()
    print("A3 overlap magnitudes:")
    print(O_mag)
    print()

    # Baseline check
    U_baseline = unitarize_svd(O_mag)
    angles_baseline = extract_pmns_angles(U_baseline)
    print("Baseline (no phases):")
    print(f"  sin2_theta12 = {angles_baseline['sin2_theta12']:.3f} (PDG: 0.307)")
    print(f"  sin2_theta23 = {angles_baseline['sin2_theta23']:.3f} (PDG: 0.546)")
    print(f"  sin2_theta13 = {angles_baseline['sin2_theta13']:.4f} (PDG: 0.022)")
    print(f"  Score = {compute_score(angles_baseline):.3f}")
    print()

    # Track A: Structured patterns (fast)
    structured_results = track_a_structured_patterns(O_mag)

    # Track A: Full sweep (slow but thorough) - commented out by default
    # Uncomment to run full 6^9 sweep:
    # full_sweep_results = track_a_discrete_sweep(O_mag)

    # Track B: Calibrated parameter
    track_b_results = track_b_calibrated(O_mag)

    # Final summary
    verdict = print_summary(structured_results, track_b_results)

    return verdict

if __name__ == '__main__':
    main()
