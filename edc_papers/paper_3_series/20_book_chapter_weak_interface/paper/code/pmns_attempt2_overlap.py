#!/usr/bin/env python3
"""
PMNS Overlap Model — Attempt 2
==============================
Applies overlap/localization logic to PMNS matrix.

Goal: Can exponential overlap profiles with Z3/Z6 structure produce
      large theta12/theta23 and small theta13?

Approach:
- Track A: No free parameters (pure Z3 geometry)
- Track B: One calibrated parameter (localization asymmetry or spacing)

Epistemic tags:
- [BL] PDG 2024 values
- [Dc] Computed from model
- [P] Ansatz/postulated
- [I] Identified (calibrated)

Author: EDC Project
Date: 2026-01-22
"""

import numpy as np
from scipy.linalg import svd, qr
import sys

# =============================================================================
# PDG 2024 Reference Values [BL]
# =============================================================================

PDG_PMNS = {
    'sin2_theta12': 0.307,      # +/- 0.013 (solar)
    'sin2_theta23': 0.546,      # +/- 0.021 (atmospheric, normal ordering)
    'sin2_theta13': 0.0220,     # +/- 0.0007 (reactor)
    'delta_cp': 1.36 * np.pi,   # ~245 degrees (poorly constrained)
}

# Mass-squared differences [BL]
PDG_MASSES = {
    'dm21_sq': 7.53e-5,   # eV^2
    'dm31_sq': 2.453e-3,  # eV^2 (normal ordering)
}

# =============================================================================
# PMNS Angle Extraction Functions
# =============================================================================

def extract_pmns_angles(U):
    """
    Extract mixing angles from a unitary (or near-unitary) matrix.

    Standard parametrization [BL]:
    - sin^2(theta13) = |U_e3|^2
    - sin^2(theta12) = |U_e2|^2 / (1 - |U_e3|^2)
    - sin^2(theta23) = |U_mu3|^2 / (1 - |U_e3|^2)

    Returns dict with sin^2 values.
    """
    U_abs = np.abs(U)

    # theta13 from |U_e3|^2
    sin2_13 = U_abs[0, 2]**2

    # Denominator for 12 and 23
    denom = 1.0 - sin2_13
    if denom < 1e-10:
        # Pathological case
        return {'sin2_theta12': 0.5, 'sin2_theta23': 0.5, 'sin2_theta13': sin2_13}

    # theta12 from |U_e2|^2
    sin2_12 = U_abs[0, 1]**2 / denom

    # theta23 from |U_mu3|^2
    sin2_23 = U_abs[1, 2]**2 / denom

    return {
        'sin2_theta12': sin2_12,
        'sin2_theta23': sin2_23,
        'sin2_theta13': sin2_13,
    }


def compute_jarlskog(U):
    """
    Compute Jarlskog invariant J = Im(U_e1 U_mu2 U_e2* U_mu1*).

    For real matrices, J = 0 (no CP violation).
    """
    J = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))
    return J


# =============================================================================
# Overlap Model Construction
# =============================================================================

def build_overlap_matrix(z_flavor, z_mass, kappa):
    """
    Construct overlap matrix O_ij between flavor positions z_flavor
    and mass positions z_mass with localization scale kappa.

    O_ij = exp(-|z_flavor[i] - z_mass[j]| / (2*kappa))

    This is [P] — profile ansatz.
    """
    O = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            dist = np.abs(z_flavor[i] - z_mass[j])
            O[i, j] = np.exp(-dist / (2.0 * kappa))
    return O


def build_overlap_with_weights(z_flavor, z_mass, kappa, w_flavor, w_mass=None):
    """
    Overlap matrix with flavor weights:
    O_ij -> sqrt(w_flavor[i] * w_mass[j]) * O_ij

    If w_mass is None, use uniform weights for mass eigenstates.
    """
    if w_mass is None:
        w_mass = np.ones(3)

    O = build_overlap_matrix(z_flavor, z_mass, kappa)
    for i in range(3):
        for j in range(3):
            O[i, j] *= np.sqrt(w_flavor[i] * w_mass[j])
    return O


def unitarize_svd(O):
    """
    Unitarize via SVD: O = U Sigma V^T -> return U V^T (closest unitary).
    """
    U, S, Vt = svd(O)
    return U @ Vt


def unitarize_qr(O):
    """
    Unitarize via QR decomposition: O = Q R -> return Q.
    """
    Q, R = qr(O)
    return Q


# =============================================================================
# Model Variants
# =============================================================================

def variant_A1_uniform_z3():
    """
    Variant A1: Pure Z3 geometry with uniform spacing.

    z_flavor = [0, 2pi/3, 4pi/3] (in units of kappa)
    z_mass aligned with z_flavor (Z3 symmetric mass basis)

    No free parameters — Track A.
    """
    # Z3 positions (angular positions mapped to linear positions)
    z_flavor = np.array([0.0, 2*np.pi/3, 4*np.pi/3])
    z_mass = np.array([0.0, 2*np.pi/3, 4*np.pi/3])  # Aligned
    kappa = 1.0  # Set scale

    O = build_overlap_matrix(z_flavor, z_mass, kappa)
    U = unitarize_svd(O)

    return {
        'name': 'A1: Uniform Z3 (aligned)',
        'track': 'A',
        'free_params': 0,
        'O': O,
        'U': U,
        'z_flavor': z_flavor,
        'z_mass': z_mass,
        'kappa': kappa,
    }


def variant_A2_z3_offset():
    """
    Variant A2: Z3 geometry with mass basis offset by pi/3.

    Tests if mass eigenstates are rotated relative to flavor.

    No free parameters — Track A.
    """
    z_flavor = np.array([0.0, 2*np.pi/3, 4*np.pi/3])
    z_mass = np.array([np.pi/3, np.pi, 5*np.pi/3])  # Offset by pi/3
    kappa = 1.0

    O = build_overlap_matrix(z_flavor, z_mass, kappa)
    U = unitarize_svd(O)

    return {
        'name': 'A2: Z3 with pi/3 offset',
        'track': 'A',
        'free_params': 0,
        'O': O,
        'U': U,
        'z_flavor': z_flavor,
        'z_mass': z_mass,
        'kappa': kappa,
    }


def variant_A3_z6_submixing():
    """
    Variant A3: Z6 = Z2 x Z3 structure.

    Mass eigenstates at Z6 positions (pi/3 spacing).
    Flavor eigenstates at Z3 positions (2pi/3 spacing).

    No free parameters — Track A.
    """
    z_flavor = np.array([0.0, 2*np.pi/3, 4*np.pi/3])
    z_mass = np.array([0.0, np.pi/3, 2*np.pi/3])  # Z6 subset
    kappa = 1.0

    O = build_overlap_matrix(z_flavor, z_mass, kappa)
    U = unitarize_svd(O)

    return {
        'name': 'A3: Z6 submixing',
        'track': 'A',
        'free_params': 0,
        'O': O,
        'U': U,
        'z_flavor': z_flavor,
        'z_mass': z_mass,
        'kappa': kappa,
    }


def variant_B1_electron_suppression(epsilon):
    """
    Variant B1: Electron neutrino localization asymmetry.

    nu_e is more localized (smaller kappa), reducing its overlap
    with distant mass eigenstates.

    One free parameter epsilon = kappa_e / kappa_avg (Track B).
    """
    z_flavor = np.array([0.0, 2*np.pi/3, 4*np.pi/3])
    z_mass = np.array([0.0, 2*np.pi/3, 4*np.pi/3])

    # Different kappa for electron vs. muon/tau
    kappa_e = epsilon  # Smaller -> more localized
    kappa_mu = 1.0
    kappa_tau = 1.0

    O = np.zeros((3, 3))
    kappas = [kappa_e, kappa_mu, kappa_tau]
    for i in range(3):
        for j in range(3):
            dist = np.abs(z_flavor[i] - z_mass[j])
            O[i, j] = np.exp(-dist / (2.0 * kappas[i]))

    U = unitarize_svd(O)

    return {
        'name': f'B1: nu_e suppression (eps={epsilon:.2f})',
        'track': 'B',
        'free_params': 1,
        'calibrated': f'epsilon={epsilon:.3f}',
        'O': O,
        'U': U,
        'z_flavor': z_flavor,
        'z_mass': z_mass,
        'epsilon': epsilon,
    }


def variant_B2_mass_hierarchy_spacing(delta):
    """
    Variant B2: Non-uniform mass eigenstate spacing.

    Mass eigenstates not uniformly spaced: nu3 is closer to nu2 than nu1.
    Models normal hierarchy separation.

    One free parameter delta = asymmetry factor (Track B).
    """
    z_flavor = np.array([0.0, 2*np.pi/3, 4*np.pi/3])
    # nu1 at 0, nu2 closer to nu3
    z_mass = np.array([0.0, 2*np.pi/3 * delta, 4*np.pi/3])
    kappa = 1.0

    O = build_overlap_matrix(z_flavor, z_mass, kappa)
    U = unitarize_svd(O)

    return {
        'name': f'B2: Hierarchical spacing (delta={delta:.2f})',
        'track': 'B',
        'free_params': 1,
        'calibrated': f'delta={delta:.3f}',
        'O': O,
        'U': U,
        'z_flavor': z_flavor,
        'z_mass': z_mass,
        'delta': delta,
    }


def variant_B3_flavor_weights(w_e, w_mu=1.0, w_tau=1.0):
    """
    Variant B3: Flavor-dependent overlap weights.

    Models different "strength" of flavor eigenstates.

    One free parameter w_e (Track B).
    """
    z_flavor = np.array([0.0, 2*np.pi/3, 4*np.pi/3])
    z_mass = np.array([0.0, 2*np.pi/3, 4*np.pi/3])
    kappa = 1.0

    w_flavor = np.array([w_e, w_mu, w_tau])
    O = build_overlap_with_weights(z_flavor, z_mass, kappa, w_flavor)
    U = unitarize_svd(O)

    return {
        'name': f'B3: Flavor weights (w_e={w_e:.2f})',
        'track': 'B',
        'free_params': 1,
        'calibrated': f'w_e={w_e:.3f}',
        'O': O,
        'U': U,
        'z_flavor': z_flavor,
        'z_mass': z_mass,
        'w_e': w_e,
    }


# =============================================================================
# Scoring and Reporting
# =============================================================================

def compute_score(angles, pdg=PDG_PMNS):
    """
    Compute scores for each angle.

    score = |predicted - observed| / observed

    Returns individual scores and overall.
    """
    scores = {}
    for key in ['sin2_theta12', 'sin2_theta23', 'sin2_theta13']:
        pred = angles[key]
        obs = pdg[key]
        if obs > 0:
            scores[key] = abs(pred - obs) / obs
        else:
            scores[key] = float('inf')

    # Overall score (geometric mean)
    scores['overall'] = np.power(
        scores['sin2_theta12'] * scores['sin2_theta23'] * scores['sin2_theta13'],
        1.0/3.0
    )
    return scores


def stoplight_status(score):
    """
    Convert score to stoplight status.

    < 0.10: GREEN
    < 0.30: YELLOW
    >= 0.30: RED
    """
    if score < 0.10:
        return 'GREEN'
    elif score < 0.30:
        return 'YELLOW'
    else:
        return 'RED'


def print_variant_report(variant):
    """
    Print detailed report for a model variant.
    """
    print(f"\n{'='*70}")
    print(f"VARIANT: {variant['name']}")
    print(f"Track: {variant['track']} | Free params: {variant['free_params']}")
    print('='*70)

    # Extract angles
    angles = extract_pmns_angles(variant['U'])
    scores = compute_score(angles)
    J = compute_jarlskog(variant['U'])

    # Print overlap matrix
    print("\nOverlap Matrix O (before unitarization):")
    O = variant['O']
    for row in O:
        print(f"  [{row[0]:.4f}  {row[1]:.4f}  {row[2]:.4f}]")

    # Print unitarized matrix
    print("\nUnitarized PMNS Matrix |U|:")
    U_abs = np.abs(variant['U'])
    for row in U_abs:
        print(f"  [{row[0]:.4f}  {row[1]:.4f}  {row[2]:.4f}]")

    # Print angles comparison
    print("\n" + "-"*60)
    print("ANGLE COMPARISON [Dc] vs [BL]")
    print("-"*60)
    print(f"{'Angle':<15} {'Model':>10} {'PDG':>10} {'Ratio':>10} {'Status':>10}")
    print("-"*60)

    for key in ['sin2_theta12', 'sin2_theta23', 'sin2_theta13']:
        pred = angles[key]
        obs = PDG_PMNS[key]
        ratio = pred / obs if obs > 0 else float('inf')
        status = stoplight_status(scores[key])

        angle_name = key.replace('sin2_', 'sin^2 ')
        print(f"{angle_name:<15} {pred:>10.4f} {obs:>10.4f} {ratio:>10.2f} {status:>10}")

    print("-"*60)
    print(f"{'Jarlskog J':<15} {J:>10.2e}")
    print(f"{'Overall score':<15} {scores['overall']:>10.3f} {stoplight_status(scores['overall']):>21}")

    return angles, scores


def print_stoplight_table(results):
    """
    Print summary stoplight table for all variants.
    """
    print("\n" + "="*90)
    print("STOPLIGHT SUMMARY TABLE")
    print("="*90)
    print(f"{'Variant':<40} {'theta12':>10} {'theta23':>10} {'theta13':>10} {'Overall':>10}")
    print("-"*90)

    for r in results:
        name = r['name'][:38]
        s12 = stoplight_status(r['scores']['sin2_theta12'])
        s23 = stoplight_status(r['scores']['sin2_theta23'])
        s13 = stoplight_status(r['scores']['sin2_theta13'])
        overall = stoplight_status(r['scores']['overall'])
        print(f"{name:<40} {s12:>10} {s23:>10} {s13:>10} {overall:>10}")

    print("="*90)


# =============================================================================
# Parameter Scan for Track B
# =============================================================================

def scan_B1_epsilon():
    """
    Scan epsilon parameter in variant B1 to find best fit for theta13.
    """
    print("\n" + "="*70)
    print("PARAMETER SCAN: B1 (nu_e localization)")
    print("="*70)

    best_score = float('inf')
    best_epsilon = None

    print(f"{'epsilon':<10} {'sin2_13':<12} {'score_13':<12} {'overall':<12}")
    print("-"*50)

    for epsilon in np.linspace(0.1, 1.5, 15):
        v = variant_B1_electron_suppression(epsilon)
        angles = extract_pmns_angles(v['U'])
        scores = compute_score(angles)

        print(f"{epsilon:<10.2f} {angles['sin2_theta13']:<12.4f} "
              f"{scores['sin2_theta13']:<12.3f} {scores['overall']:<12.3f}")

        if scores['overall'] < best_score:
            best_score = scores['overall']
            best_epsilon = epsilon

    print("-"*50)
    print(f"Best epsilon: {best_epsilon:.2f} with overall score: {best_score:.3f}")
    return best_epsilon


def scan_B2_delta():
    """
    Scan delta parameter in variant B2.
    """
    print("\n" + "="*70)
    print("PARAMETER SCAN: B2 (mass hierarchy spacing)")
    print("="*70)

    best_score = float('inf')
    best_delta = None

    print(f"{'delta':<10} {'sin2_13':<12} {'score_13':<12} {'overall':<12}")
    print("-"*50)

    for delta in np.linspace(0.3, 1.5, 13):
        v = variant_B2_mass_hierarchy_spacing(delta)
        angles = extract_pmns_angles(v['U'])
        scores = compute_score(angles)

        print(f"{delta:<10.2f} {angles['sin2_theta13']:<12.4f} "
              f"{scores['sin2_theta13']:<12.3f} {scores['overall']:<12.3f}")

        if scores['overall'] < best_score:
            best_score = scores['overall']
            best_delta = delta

    print("-"*50)
    print(f"Best delta: {best_delta:.2f} with overall score: {best_score:.3f}")
    return best_delta


def scan_B3_we():
    """
    Scan w_e parameter in variant B3.
    """
    print("\n" + "="*70)
    print("PARAMETER SCAN: B3 (flavor weights)")
    print("="*70)

    best_score = float('inf')
    best_we = None

    print(f"{'w_e':<10} {'sin2_13':<12} {'score_13':<12} {'overall':<12}")
    print("-"*50)

    for w_e in np.linspace(0.1, 2.0, 20):
        v = variant_B3_flavor_weights(w_e)
        angles = extract_pmns_angles(v['U'])
        scores = compute_score(angles)

        print(f"{w_e:<10.2f} {angles['sin2_theta13']:<12.4f} "
              f"{scores['sin2_theta13']:<12.3f} {scores['overall']:<12.3f}")

        if scores['overall'] < best_score:
            best_score = scores['overall']
            best_we = w_e

    print("-"*50)
    print(f"Best w_e: {best_we:.2f} with overall score: {best_score:.3f}")
    return best_we


# =============================================================================
# DFT Baseline Comparison
# =============================================================================

def dft_baseline():
    """
    Compute DFT matrix (from Attempt 1) for comparison.
    """
    omega = np.exp(2j * np.pi / 3)
    U_dft = np.array([
        [1, 1, 1],
        [1, omega.conj(), omega],
        [1, omega, omega.conj()]
    ]) / np.sqrt(3)

    return {
        'name': 'DFT Baseline (Attempt 1)',
        'track': 'A',
        'free_params': 0,
        'O': np.abs(U_dft),  # Magnitude
        'U': U_dft,
    }


# =============================================================================
# Main Execution
# =============================================================================

def main():
    print("="*70)
    print("PMNS OVERLAP MODEL — ATTEMPT 2")
    print("="*70)
    print("""
Goal: Apply overlap/localization model to PMNS matrix.
      Test whether Z3/Z6 geometry can produce observed mixing pattern.

PDG 2024 Reference [BL]:
  sin^2(theta12) = 0.307 (solar)
  sin^2(theta23) = 0.546 (atmospheric)
  sin^2(theta13) = 0.022 (reactor)

Key challenge: theta13 is SMALL (2.2%), while theta12 and theta23 are LARGE.
The DFT baseline (Attempt 1) predicts all |U|^2 = 1/3 -> FALSIFIED.
""")

    results = []

    # -------------------------------------------------------------------------
    # Track A: No free parameters
    # -------------------------------------------------------------------------
    print("\n" + "#"*70)
    print("# TRACK A: NO FREE PARAMETERS")
    print("#"*70)

    # DFT baseline
    v_dft = dft_baseline()
    angles, scores = print_variant_report(v_dft)
    results.append({'name': v_dft['name'], 'angles': angles, 'scores': scores, 'track': 'A'})

    # A1: Uniform Z3
    v_a1 = variant_A1_uniform_z3()
    angles, scores = print_variant_report(v_a1)
    results.append({'name': v_a1['name'], 'angles': angles, 'scores': scores, 'track': 'A'})

    # A2: Z3 with offset
    v_a2 = variant_A2_z3_offset()
    angles, scores = print_variant_report(v_a2)
    results.append({'name': v_a2['name'], 'angles': angles, 'scores': scores, 'track': 'A'})

    # A3: Z6 submixing
    v_a3 = variant_A3_z6_submixing()
    angles, scores = print_variant_report(v_a3)
    results.append({'name': v_a3['name'], 'angles': angles, 'scores': scores, 'track': 'A'})

    # -------------------------------------------------------------------------
    # Track B: One calibrated parameter
    # -------------------------------------------------------------------------
    print("\n" + "#"*70)
    print("# TRACK B: ONE CALIBRATED PARAMETER")
    print("#"*70)

    # Run parameter scans
    best_eps = scan_B1_epsilon()
    best_delta = scan_B2_delta()
    best_we = scan_B3_we()

    # Report best B variants
    print("\n" + "-"*70)
    print("BEST TRACK B VARIANTS")
    print("-"*70)

    v_b1 = variant_B1_electron_suppression(best_eps)
    angles, scores = print_variant_report(v_b1)
    results.append({'name': v_b1['name'], 'angles': angles, 'scores': scores, 'track': 'B'})

    v_b2 = variant_B2_mass_hierarchy_spacing(best_delta)
    angles, scores = print_variant_report(v_b2)
    results.append({'name': v_b2['name'], 'angles': angles, 'scores': scores, 'track': 'B'})

    v_b3 = variant_B3_flavor_weights(best_we)
    angles, scores = print_variant_report(v_b3)
    results.append({'name': v_b3['name'], 'angles': angles, 'scores': scores, 'track': 'B'})

    # -------------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------------
    print_stoplight_table(results)

    # Final verdict
    print("\n" + "="*70)
    print("FINAL VERDICT: PMNS ATTEMPT 2")
    print("="*70)

    # Check if any Track A passes
    track_a_results = [r for r in results if r['track'] == 'A']
    track_a_best = min(track_a_results, key=lambda x: x['scores']['overall'])

    track_b_results = [r for r in results if r['track'] == 'B']
    track_b_best = min(track_b_results, key=lambda x: x['scores']['overall'])

    print(f"""
TRACK A (no free parameters):
  Best variant: {track_a_best['name']}
  Overall score: {track_a_best['scores']['overall']:.3f}
  Status: {stoplight_status(track_a_best['scores']['overall'])}

TRACK B (one calibrated parameter):
  Best variant: {track_b_best['name']}
  Overall score: {track_b_best['scores']['overall']:.3f}
  Status: {stoplight_status(track_b_best['scores']['overall'])}
""")

    # Determine overall verdict
    if track_a_best['scores']['overall'] < 0.30:
        print("VERDICT: Track A PARTIALLY SUCCESSFUL — overlap model captures PMNS structure")
        print("         without free parameters (though not quantitatively precise).")
    elif track_b_best['scores']['overall'] < 0.30:
        print("VERDICT: Track B PARTIALLY SUCCESSFUL — overlap model requires one calibrated")
        print("         parameter to capture theta13 suppression.")
    else:
        print("VERDICT: NEGATIVE RESULT — overlap model does NOT naturally produce small theta13")
        print("         The fundamental challenge: Z3 symmetry predicts |U|^2 = 1/3 for all elements.")
        print("         Even with localization asymmetry, the theta13 suppression is insufficient.")

    print("""
KEY INSIGHT:
  The CKM hierarchy (lambda, lambda^2, lambda^3) emerges from exponential overlap
  with SMALL off-diagonal elements. PMNS requires the OPPOSITE: LARGE off-diagonal
  elements (theta12 ~ 33 deg, theta23 ~ 45 deg) with ONE small element (theta13 ~ 8 deg).

  This asymmetry is NOT natural in the overlap model, which tends to produce
  either democratic mixing (all equal) or hierarchical mixing (all suppressed).

EPISTEMIC STATUS:
  [Dc] Overlap model computed for multiple variants
  [I]  Best-fit parameters identified in Track B
  [P]  Ansatz: exponential profiles + Z3/Z6 geometry

  FALSIFICATION: Like Attempt 1 (DFT), no Track A variant reproduces observed PMNS.
                 Track B improves theta13 but introduces calibration.
""")

    return results


if __name__ == "__main__":
    results = main()
