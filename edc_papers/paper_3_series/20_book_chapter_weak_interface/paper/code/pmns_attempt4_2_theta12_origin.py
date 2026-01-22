#!/usr/bin/env python3
"""
PMNS Attempt 4.2: θ₁₂ Origin Micro-Attempt
==========================================

Goal: Test two geometric candidates for the solar angle θ₁₂ without PDG-smuggling.

Candidate mechanisms:
    T1: θ₁₂ = arctan(1/√2) ≈ 35.264°
        Rationale: Projection from Z₆ to brane in 5D geometry

    T2: θ₁₂ = 45° - arcsin(λ) ≈ 32.0°
        Rationale: Wolfenstein-scale deviation from maximal mixing

NO SMUGGLING constraint:
    - Do NOT use PDG θ₁₂ or PDG sin²θ₁₂ to calibrate θ₁₂
    - PDG is used ONLY for final evaluation AFTER prediction
    - θ₁₂ ≈ 33.7° (PDG-exact) is NOT a candidate

Baseline inputs:
    - λ ≈ 0.225 [BL] (Wolfenstein scale, from CKM Ch7)
    - θ₂₃ from Z₆ geometry [Dc] (Attempt 2)
    - ε = λ/√2 [BL→Dc] (Attempt 4.1)

Author: Claude Code (Attempt 4.2)
Date: 2026-01-22
"""

import numpy as np
from pathlib import Path

# ==============================================================================
# CONSTANTS FROM ESTABLISHED EDC/BOOK QUANTITIES
# ==============================================================================

# λ from Wolfenstein parametrization [BL]
# Provenance: sections/07_ckm_cp.tex, Eq.~(\ref{eq:ch7_wolfenstein})
LAMBDA_WOLFENSTEIN = 0.225  # [BL]

# θ₂₃ from geometry [Dc] — derived in Attempt 2
# Provenance: sections/ch6_pmns_attempt2.tex
SIN2_THETA23_GEOM = 0.564  # [Dc]
THETA23_GEOM = np.arcsin(np.sqrt(SIN2_THETA23_GEOM))

# ε from Attempt 4.1 [BL→Dc]
# Provenance: sections/ch6_pmns_attempt4_1_derive_epsilon.tex
EPSILON_C1 = LAMBDA_WOLFENSTEIN / np.sqrt(2)  # [BL→Dc]

# PDG 2024 targets [BL] — for comparison AFTER prediction
SIN2_THETA12_PDG = 0.307
SIN2_THETA23_PDG = 0.546
SIN2_THETA13_PDG = 0.022

# Theta12 from PDG (for error calculation only, NOT as candidate)
THETA12_PDG = np.arcsin(np.sqrt(SIN2_THETA12_PDG))


# ==============================================================================
# θ₁₂ CANDIDATE MECHANISMS
# ==============================================================================

def compute_theta12_T1() -> tuple:
    """Candidate T1: θ₁₂ = arctan(1/√2) ≈ 35.264°

    Geometric rationale: In Z₆-symmetric 5D geometry, the projection factor
    from bulk to brane involves arctan(1/√2), which naturally appears in
    the overlap integral between flavor eigenstates.

    This is the same √2 factor that appears in ε = λ/√2 (Attempt 4.1),
    suggesting a unified geometric origin.

    Returns: (θ₁₂_value, sin²θ₁₂, epistemic_tag, rationale)
    """
    theta12 = np.arctan(1 / np.sqrt(2))
    sin2_theta12 = np.sin(theta12)**2

    tag = '[Dc]'  # Pure geometry, no external input
    rationale = "θ₁₂ = arctan(1/√2) from Z₆ projection geometry"

    return theta12, sin2_theta12, tag, rationale


def compute_theta12_T2() -> tuple:
    """Candidate T2: θ₁₂ = 45° - arcsin(λ)

    Geometric rationale: Maximal mixing (45°) reduced by Cabibbo-scale
    deviation, suggesting CKM-PMNS connection via common geometric origin.

    Returns: (θ₁₂_value, sin²θ₁₂, epistemic_tag, rationale)
    """
    theta12 = np.radians(45) - np.arcsin(LAMBDA_WOLFENSTEIN)
    sin2_theta12 = np.sin(theta12)**2

    tag = '[BL→Dc]'  # Uses λ [BL], transformation is geometric
    rationale = f"θ₁₂ = 45° - arcsin(λ) with λ = {LAMBDA_WOLFENSTEIN}"

    return theta12, sin2_theta12, tag, rationale


# ==============================================================================
# PMNS CONSTRUCTION (from Attempt 4)
# ==============================================================================

def rotation_matrix(plane: str, theta: float) -> np.ndarray:
    """Return 3x3 rotation matrix in specified plane."""
    c, s = np.cos(theta), np.sin(theta)

    if plane == '12':
        return np.array([
            [c, s, 0],
            [-s, c, 0],
            [0, 0, 1]
        ])
    elif plane == '13':
        return np.array([
            [c, 0, s],
            [0, 1, 0],
            [-s, 0, c]
        ])
    elif plane == '23':
        return np.array([
            [1, 0, 0],
            [0, c, s],
            [0, -s, c]
        ])
    else:
        raise ValueError(f"Unknown plane: {plane}")


def construct_pmns(theta12: float, theta23: float, epsilon: float) -> np.ndarray:
    """Construct PMNS matrix using rank-2 + reactor perturbation.

    U = R23(θ23) · R13(ε) · R12(θ12)
    """
    R12 = rotation_matrix('12', theta12)
    R13 = rotation_matrix('13', epsilon)
    R23 = rotation_matrix('23', theta23)

    return R23 @ R13 @ R12


def extract_angles(U: np.ndarray) -> dict:
    """Extract mixing angles from PMNS matrix."""
    sin2_13 = np.abs(U[0, 2])**2
    cos_13 = np.sqrt(1 - sin2_13)

    if cos_13 > 1e-10:
        sin2_12 = np.abs(U[0, 1])**2 / (1 - sin2_13)
        sin2_23 = np.abs(U[1, 2])**2 / (1 - sin2_13)
    else:
        sin2_12 = 0.5
        sin2_23 = 0.5

    return {
        'sin2_12': sin2_12,
        'sin2_23': sin2_23,
        'sin2_13': sin2_13
    }


# ==============================================================================
# ANALYSIS
# ==============================================================================

def analyze_candidate(name: str, theta12: float, sin2_theta12: float,
                      tag: str, rationale: str) -> dict:
    """Analyze a single θ₁₂ candidate."""

    print(f"\n{'='*70}")
    print(f"CANDIDATE {name}: θ₁₂ = {np.degrees(theta12):.3f}°")
    print(f"{'='*70}")
    print(f"  sin²θ₁₂ = {sin2_theta12:.4f}")
    print(f"  Epistemic tag: {tag}")
    print(f"  Rationale: {rationale}")
    print()

    # Comparison to PDG
    error_sin2 = abs(sin2_theta12 - SIN2_THETA12_PDG) / SIN2_THETA12_PDG * 100
    error_angle = abs(np.degrees(theta12) - np.degrees(THETA12_PDG))

    print(f"  PDG comparison:")
    print(f"    PDG sin²θ₁₂ = {SIN2_THETA12_PDG}")
    print(f"    PDG θ₁₂ = {np.degrees(THETA12_PDG):.2f}°")
    print(f"    Error (sin²): {error_sin2:.1f}%")
    print(f"    Error (angle): {error_angle:.2f}°")
    print()

    # Stoplight verdict for θ₁₂ alone
    if error_sin2 < 10:
        verdict_12 = 'GREEN'
    elif error_sin2 < 25:
        verdict_12 = 'YELLOW'
    else:
        verdict_12 = 'RED'

    print(f"  θ₁₂ verdict: {verdict_12} ({error_sin2:.1f}% error)")

    # Full PMNS test with this θ₁₂
    print()
    print(f"  Full PMNS with θ₂₃ [Dc] and ε = λ/√2 [BL→Dc]:")

    U = construct_pmns(theta12, THETA23_GEOM, EPSILON_C1)
    angles = extract_angles(U)

    err_12 = abs(angles['sin2_12'] - SIN2_THETA12_PDG) / SIN2_THETA12_PDG * 100
    err_23 = abs(angles['sin2_23'] - SIN2_THETA23_PDG) / SIN2_THETA23_PDG * 100
    err_13 = abs(angles['sin2_13'] - SIN2_THETA13_PDG) / SIN2_THETA13_PDG * 100

    print(f"    sin²θ₁₂ = {angles['sin2_12']:.4f} (PDG: {SIN2_THETA12_PDG}, err: {err_12:.1f}%)")
    print(f"    sin²θ₂₃ = {angles['sin2_23']:.4f} (PDG: {SIN2_THETA23_PDG}, err: {err_23:.1f}%)")
    print(f"    sin²θ₁₃ = {angles['sin2_13']:.4f} (PDG: {SIN2_THETA13_PDG}, err: {err_13:.1f}%)")

    # Overall status
    v12 = 'GREEN' if err_12 < 10 else ('YELLOW' if err_12 < 25 else 'RED')
    v23 = 'GREEN' if err_23 < 10 else ('YELLOW' if err_23 < 25 else 'RED')
    v13 = 'GREEN' if err_13 < 25 else ('YELLOW' if err_13 < 50 else 'RED')

    print()
    print(f"    Status: θ₁₂={v12}, θ₂₃={v23}, θ₁₃={v13}")

    # Combined assessment
    if v12 == 'GREEN' and v23 == 'GREEN' and v13 in ['GREEN', 'YELLOW']:
        overall = 'GREEN'
    elif v12 == 'RED' or v23 == 'RED' or v13 == 'RED':
        overall = 'YELLOW' if any(v == 'GREEN' for v in [v12, v23, v13]) else 'RED'
    else:
        overall = 'YELLOW'

    print(f"    Overall: {overall}")

    return {
        'name': name,
        'theta12': theta12,
        'sin2_theta12': sin2_theta12,
        'tag': tag,
        'rationale': rationale,
        'error_sin2': error_sin2,
        'error_angle': error_angle,
        'verdict_12': verdict_12,
        'full_pmns': angles,
        'full_pmns_errors': {'err_12': err_12, 'err_23': err_23, 'err_13': err_13},
        'overall': overall
    }


def main():
    """Main routine."""
    print("=" * 70)
    print("PMNS ATTEMPT 4.2: θ₁₂ ORIGIN MICRO-ATTEMPT")
    print("=" * 70)
    print()
    print("NO SMUGGLING CONSTRAINT:")
    print("  - θ₁₂ is predicted from geometry, NOT fit to PDG")
    print("  - PDG comparison is done AFTER prediction")
    print("  - PDG-exact θ₁₂ = 33.7° is NOT considered as candidate")
    print()
    print("BASELINE INPUTS:")
    print(f"  - λ = {LAMBDA_WOLFENSTEIN} [BL] (Wolfenstein scale)")
    print(f"  - θ₂₃: sin²θ₂₃ = {SIN2_THETA23_GEOM} [Dc] (Z₆ geometry)")
    print(f"  - ε = λ/√2 = {EPSILON_C1:.4f} rad [BL→Dc] (Attempt 4.1)")
    print()
    print("PDG TARGETS [BL]:")
    print(f"  - sin²θ₁₂ = {SIN2_THETA12_PDG} (θ₁₂ ≈ {np.degrees(THETA12_PDG):.2f}°)")
    print(f"  - sin²θ₂₃ = {SIN2_THETA23_PDG}")
    print(f"  - sin²θ₁₃ = {SIN2_THETA13_PDG}")

    results = []

    # Candidate T1: arctan(1/√2)
    theta12_T1, sin2_T1, tag_T1, rationale_T1 = compute_theta12_T1()
    result_T1 = analyze_candidate('T1', theta12_T1, sin2_T1, tag_T1, rationale_T1)
    results.append(result_T1)

    # Candidate T2: 45° - arcsin(λ)
    theta12_T2, sin2_T2, tag_T2, rationale_T2 = compute_theta12_T2()
    result_T2 = analyze_candidate('T2', theta12_T2, sin2_T2, tag_T2, rationale_T2)
    results.append(result_T2)

    # Summary comparison
    print()
    print("=" * 70)
    print("SUMMARY: θ₁₂ CANDIDATE COMPARISON")
    print("=" * 70)
    print()
    print(f"{'Candidate':<25} {'θ₁₂ (deg)':<12} {'sin²θ₁₂':<12} {'Error':<10} {'Tag':<15} {'Verdict'}")
    print("-" * 90)

    for r in results:
        print(f"{r['name'] + ': ' + r['rationale'][:18]:<25} "
              f"{np.degrees(r['theta12']):<12.3f} "
              f"{r['sin2_theta12']:<12.4f} "
              f"{r['error_sin2']:<10.1f}% "
              f"{r['tag']:<15} "
              f"{r['verdict_12']}")

    print(f"{'PDG target':<25} {np.degrees(THETA12_PDG):<12.2f} {SIN2_THETA12_PDG:<12.4f} {'—':<10} {'[BL]':<15} {'—'}")
    print()

    # Best candidate determination
    best = min(results, key=lambda x: x['error_sin2'])
    print(f"BEST CANDIDATE: {best['name']} ({best['rationale']})")
    print(f"  θ₁₂ = {np.degrees(best['theta12']):.3f}° → sin²θ₁₂ = {best['sin2_theta12']:.4f}")
    print(f"  Error: {best['error_sin2']:.1f}%")
    print(f"  Epistemic tag: {best['tag']}")
    print()

    # Comparison to discrete 35° (Attempt 4.1 candidate)
    theta12_35 = np.radians(35)
    sin2_35 = np.sin(theta12_35)**2
    error_35 = abs(sin2_35 - SIN2_THETA12_PDG) / SIN2_THETA12_PDG * 100

    print("-" * 70)
    print("COMPARISON TO DISCRETE 35° (Attempt 4.1)")
    print("-" * 70)
    print(f"  35° discrete: sin²θ₁₂ = {sin2_35:.4f}, error = {error_35:.1f}%")
    print(f"  T1 (arctan(1/√2) = 35.264°): sin²θ₁₂ = {sin2_T1:.4f}, error = {result_T1['error_sin2']:.1f}%")
    print()

    # The key insight: arctan(1/√2) ≈ 35.264° is very close to discrete 35°
    if abs(np.degrees(theta12_T1) - 35) < 1:
        print("  KEY INSIGHT: T1 provides geometric origin for 35° discrete candidate!")
        print(f"  arctan(1/√2) = {np.degrees(theta12_T1):.3f}° ≈ 35°")
        print("  This connects to the √2 factor already used in ε = λ/√2 (Attempt 4.1)")
    print()

    # Verdict
    print("=" * 70)
    print("VERDICT")
    print("=" * 70)
    print()

    # T1 assessment
    if result_T1['error_sin2'] < 10:
        t1_status = 'GREEN [Dc]'
        t1_assessment = 'derived from pure geometry'
    elif result_T1['error_sin2'] < 25:
        t1_status = 'YELLOW [Dc]'
        t1_assessment = 'derived but ~15% off'
    else:
        t1_status = 'RED'
        t1_assessment = 'fails to match PDG'

    print(f"T1 (θ₁₂ = arctan(1/√2)): {t1_status}")
    print(f"   {t1_assessment}")
    print(f"   Predicted sin²θ₁₂ = {sin2_T1:.4f} vs PDG {SIN2_THETA12_PDG}")
    print(f"   Error: {result_T1['error_sin2']:.1f}%")
    print(f"   Provides geometric origin for 35° discrete candidate")
    print()

    # T2 assessment
    if result_T2['error_sin2'] < 10:
        t2_status = 'GREEN [BL→Dc]'
        t2_assessment = 'close to PDG'
    elif result_T2['error_sin2'] < 25:
        t2_status = 'YELLOW [BL→Dc]'
        t2_assessment = 'reasonable but undershoots'
    else:
        t2_status = 'RED [BL→Dc]'
        t2_assessment = 'fails to match PDG'

    print(f"T2 (θ₁₂ = 45° - arcsin(λ)): {t2_status}")
    print(f"   {t2_assessment}")
    print(f"   Predicted sin²θ₁₂ = {sin2_T2:.4f} vs PDG {SIN2_THETA12_PDG}")
    print(f"   Error: {result_T2['error_sin2']:.1f}%")
    print()

    # OPR-05c recommendation
    print("-" * 70)
    print("OPR-05c STATUS UPDATE RECOMMENDATION")
    print("-" * 70)
    print()

    # Determine best path
    if result_T1['error_sin2'] < 15 or result_T2['error_sin2'] < 15:
        if result_T1['error_sin2'] < result_T2['error_sin2']:
            recommended = 'T1'
            print(f"RECOMMENDED: T1 (arctan(1/√2)) — pure geometry, {result_T1['error_sin2']:.1f}% error")
            print()
            print("OPR-05c: YELLOW [I] → YELLOW [Dc] upgrade path identified")
            print("  - T1 provides geometric origin for θ₁₂ ≈ 35.264°")
            print("  - Same √2 factor as ε = λ/√2 suggests unified geometric origin")
            print(f"  - Still ~{result_T1['error_sin2']:.0f}% off; not GREEN, but mechanism is [Dc]")
        else:
            recommended = 'T2'
            print(f"RECOMMENDED: T2 (45° - arcsin(λ)) — {result_T2['error_sin2']:.1f}% error")
            print()
            print("OPR-05c: YELLOW [I] → YELLOW [BL→Dc]")
            print("  - T2 connects θ₁₂ to CKM-scale λ")
            print(f"  - Error {result_T2['error_sin2']:.1f}%; uses baseline λ")
    else:
        recommended = 'neither'
        print("Neither candidate achieves < 15% error")
        print("OPR-05c: Remains YELLOW [I]")

    print()

    # Final summary
    print("-" * 70)
    print("FINAL SUMMARY")
    print("-" * 70)
    print()
    print("θ₁₂ candidates tested without PDG-smuggling:")
    print(f"  T1: arctan(1/√2) = {np.degrees(theta12_T1):.3f}° → sin²θ₁₂ = {sin2_T1:.4f} ({result_T1['error_sin2']:.1f}% off)")
    print(f"  T2: 45° - arcsin(λ) = {np.degrees(theta12_T2):.2f}° → sin²θ₁₂ = {sin2_T2:.4f} ({result_T2['error_sin2']:.1f}% off)")
    print()
    print(f"Best candidate: {recommended.upper()}")
    if recommended == 'T1':
        print("  Geometric origin for 35° discrete candidate established")
        print("  Unified √2 factor with ε = λ/√2 from Attempt 4.1")

    # Save output
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / 'pmns_attempt4_2_results.txt'

    with open(output_file, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("PMNS ATTEMPT 4.2: θ₁₂ ORIGIN MICRO-ATTEMPT\n")
        f.write("=" * 70 + "\n\n")

        f.write("CANDIDATE COMPARISON\n")
        f.write("-" * 70 + "\n")
        f.write(f"{'Candidate':<25} {'θ₁₂ (deg)':<12} {'sin²θ₁₂':<12} {'Error':<10} {'Tag'}\n")
        f.write("-" * 70 + "\n")

        for r in results:
            f.write(f"{r['name']:<25} {np.degrees(r['theta12']):<12.3f} "
                    f"{r['sin2_theta12']:<12.4f} {r['error_sin2']:<10.1f}% {r['tag']}\n")

        f.write(f"{'PDG target':<25} {np.degrees(THETA12_PDG):<12.2f} "
                f"{SIN2_THETA12_PDG:<12.4f} {'—':<10} [BL]\n")
        f.write("\n")

        f.write("VERDICT\n")
        f.write("-" * 70 + "\n")
        f.write(f"T1 (arctan(1/√2)): {t1_status} — {t1_assessment}\n")
        f.write(f"T2 (45° - arcsin(λ)): {t2_status} — {t2_assessment}\n")
        f.write("\n")
        f.write(f"RECOMMENDED: {recommended.upper()}\n")
        if recommended == 'T1':
            f.write("  Geometric origin for 35° discrete candidate\n")
            f.write("  Unified √2 factor with ε = λ/√2\n")

    print()
    print(f"Results saved to: {output_file}")


if __name__ == '__main__':
    main()
