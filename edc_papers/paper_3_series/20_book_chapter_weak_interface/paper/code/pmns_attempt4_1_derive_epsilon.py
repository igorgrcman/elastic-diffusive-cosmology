#!/usr/bin/env python3
"""
PMNS Attempt 4.1: Derive epsilon from existing EDC quantities
==============================================================

Goal: Derive the reactor perturbation ε from CKM-scale λ (and κ ratio)
      without smuggling PDG θ13.

Candidate mechanisms:
    C1: ε = λ / √2
    C2: ε = λ × (κ_quark / κ_lepton)

NO SMUGGLING constraint:
    - Do NOT use PDG θ13 or PDG ε to calibrate ε
    - Do NOT minimize error vs PDG to pick ε
    - Compare predicted θ13 to PDG AFTER prediction

λ provenance:
    File: sections/07_ckm_cp.tex:313-318
    Label: eq:ch7_wolfenstein
    Value: λ ≈ 0.225 [BL] (Wolfenstein parametrization from PDG)

κ_q/κ_ℓ provenance:
    File: sections/07_ckm_cp.tex:714
    Label: eq:ch7_kappa_ratio
    Value: κ_q/κ_ℓ ≈ 0.4 [I] (identified from CKM/PMNS comparison, not derived)

Author: Claude Code (Attempt 4.1)
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

# κ_q/κ_ℓ ratio [I] — identified, not derived
# Provenance: sections/07_ckm_cp.tex, Eq.~(\ref{eq:ch7_kappa_ratio})
KAPPA_RATIO = 0.4  # [I]

# θ23 from geometry [Dc] — derived in Attempt 2
# Provenance: sections/ch6_pmns_attempt2.tex
SIN2_THETA23_GEOM = 0.564  # [Dc]
THETA23_GEOM = np.arcsin(np.sqrt(SIN2_THETA23_GEOM))

# PDG 2024 targets [BL] — for comparison AFTER prediction
SIN2_THETA12_PDG = 0.307
SIN2_THETA23_PDG = 0.546
SIN2_THETA13_PDG = 0.022

# Discrete θ12 candidates (NO 33.7° — that is PDG-smuggling)
THETA12_DISCRETE = {
    '30°': np.radians(30),
    '35°': np.radians(35),
    '45°': np.radians(45),
    '54.74° (arctan√2)': np.arctan(np.sqrt(2)),
}

# Identified θ12 [I] — matches PDG exactly (not derived)
THETA12_IDENTIFIED = np.radians(33.7)  # [I]

# Stoplight thresholds (from Attempt 4)
SIGMA_12 = 0.03
SIGMA_23 = 0.03
SIGMA_13 = 0.01


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
    # Standard parametrization
    sin2_13 = np.abs(U[0, 2])**2
    sin_13 = np.sqrt(sin2_13)
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


def get_status(value: float, target: float, sigma: float) -> str:
    """Return stoplight status (GREEN/YELLOW/RED)."""
    rel_error = abs(value - target) / target if target > 0 else abs(value)

    if rel_error < sigma / target:  # Within ~10%
        return 'GREEN'
    elif rel_error < 3 * sigma / target:  # Within ~30%
        return 'YELLOW'
    else:
        return 'RED'


def score_result(angles: dict) -> float:
    """Compute chi-square-like score."""
    chi2 = 0
    chi2 += ((angles['sin2_12'] - SIN2_THETA12_PDG) / SIGMA_12)**2
    chi2 += ((angles['sin2_23'] - SIN2_THETA23_PDG) / SIGMA_23)**2
    chi2 += ((angles['sin2_13'] - SIN2_THETA13_PDG) / SIGMA_13)**2
    return chi2


# ==============================================================================
# CANDIDATE ε MECHANISMS
# ==============================================================================

def compute_epsilon_C1() -> tuple:
    """Candidate C1: ε = λ / √2

    Rationale: Reactor angle is suppressed relative to Cabibbo by geometric
    factor √2, which appears naturally in projection from Z6 to brane.

    Returns: (ε_value, epistemic_tag, rationale)
    """
    epsilon = LAMBDA_WOLFENSTEIN / np.sqrt(2)
    tag = '[BL→Dc]' if True else '[Dc]'  # λ is [BL], transformation is geometric
    rationale = "ε = λ/√2 from geometric suppression"

    return epsilon, tag, rationale


def compute_epsilon_C2() -> tuple:
    """Candidate C2: ε = λ × (κ_q / κ_ℓ)

    Rationale: Reactor angle inherits quark-lepton localization asymmetry.

    Returns: (ε_value, epistemic_tag, rationale)
    """
    epsilon = LAMBDA_WOLFENSTEIN * KAPPA_RATIO
    tag = '[I]'  # κ ratio is [I], not derived
    rationale = f"ε = λ × (κ_q/κ_ℓ) with κ ratio ≈ {KAPPA_RATIO}"

    return epsilon, tag, rationale


# ==============================================================================
# MAIN ANALYSIS
# ==============================================================================

def analyze_candidate(name: str, epsilon: float, tag: str, rationale: str):
    """Analyze a single ε candidate."""
    print(f"\n{'='*70}")
    print(f"CANDIDATE {name}: ε = {epsilon:.4f} rad ({np.degrees(epsilon):.2f}°)")
    print(f"{'='*70}")
    print(f"Epistemic tag: {tag}")
    print(f"Rationale: {rationale}")
    print()

    results = []

    # Mode A: Discrete θ12 candidates (NO PDG-smuggling)
    print("-" * 70)
    print("MODE A: Discrete θ12 candidates (no PDG-smuggling)")
    print("-" * 70)
    print(f"{'θ12 candidate':<20} {'sin²θ12':>10} {'sin²θ23':>10} {'sin²θ13':>10} {'Score':>8} {'Status':>8}")
    print(f"{'(PDG targets)':<20} {SIN2_THETA12_PDG:>10.3f} {SIN2_THETA23_PDG:>10.3f} {SIN2_THETA13_PDG:>10.3f}")
    print("-" * 70)

    for label, theta12 in THETA12_DISCRETE.items():
        U = construct_pmns(theta12, THETA23_GEOM, epsilon)
        angles = extract_angles(U)
        score = score_result(angles)

        s12 = get_status(angles['sin2_12'], SIN2_THETA12_PDG, SIGMA_12)
        s23 = get_status(angles['sin2_23'], SIN2_THETA23_PDG, SIGMA_23)
        s13 = get_status(angles['sin2_13'], SIN2_THETA13_PDG, SIGMA_13)

        if s12 == 'GREEN' and s23 == 'GREEN' and s13 == 'GREEN':
            overall = 'GREEN'
        elif s12 == 'RED' or s23 == 'RED' or s13 == 'RED':
            overall = 'YELLOW' if (s12 == 'GREEN' or s23 == 'GREEN' or s13 == 'GREEN') else 'RED'
        else:
            overall = 'YELLOW'

        print(f"{label:<20} {angles['sin2_12']:>10.4f} {angles['sin2_23']:>10.4f} {angles['sin2_13']:>10.4f} {score:>8.2f} {overall:>8}")

        results.append({
            'candidate': name,
            'mode': 'A',
            'theta12_label': label,
            'theta12': theta12,
            'epsilon': epsilon,
            'angles': angles,
            'score': score,
            'overall': overall,
            'tag': tag
        })

    # Mode B: Identified θ12 = 33.7° [I]
    print()
    print("-" * 70)
    print("MODE B: Identified θ12 = 33.7° [I] (matches PDG solar)")
    print("-" * 70)

    U = construct_pmns(THETA12_IDENTIFIED, THETA23_GEOM, epsilon)
    angles = extract_angles(U)
    score = score_result(angles)

    s12 = get_status(angles['sin2_12'], SIN2_THETA12_PDG, SIGMA_12)
    s23 = get_status(angles['sin2_23'], SIN2_THETA23_PDG, SIGMA_23)
    s13 = get_status(angles['sin2_13'], SIN2_THETA13_PDG, SIGMA_13)

    if s12 == 'GREEN' and s23 == 'GREEN' and s13 == 'GREEN':
        overall = 'GREEN'
    elif s12 == 'RED' or s23 == 'RED' or s13 == 'RED':
        overall = 'YELLOW' if (s12 == 'GREEN' or s23 == 'GREEN' or s13 == 'GREEN') else 'RED'
    else:
        overall = 'YELLOW'

    print(f"{'θ12 = 33.7° [I]':<20} {angles['sin2_12']:>10.4f} {angles['sin2_23']:>10.4f} {angles['sin2_13']:>10.4f} {score:>8.2f} {overall:>8}")

    results.append({
        'candidate': name,
        'mode': 'B',
        'theta12_label': '33.7° [I]',
        'theta12': THETA12_IDENTIFIED,
        'epsilon': epsilon,
        'angles': angles,
        'score': score,
        'overall': overall,
        'tag': tag
    })

    # θ13 prediction analysis
    print()
    print("-" * 70)
    print("θ13 PREDICTION (key test)")
    print("-" * 70)

    # For small ε, sin²θ13 ≈ ε²
    sin2_13_pred = epsilon**2
    sin2_13_actual = angles['sin2_13']  # From Mode B

    print(f"  Predicted sin²θ13 (≈ε²): {sin2_13_pred:.4f}")
    print(f"  PDG sin²θ13:             {SIN2_THETA13_PDG:.4f}")
    print(f"  Ratio (pred/PDG):        {sin2_13_pred/SIN2_THETA13_PDG:.2f}")

    if abs(sin2_13_pred - SIN2_THETA13_PDG) / SIN2_THETA13_PDG < 0.3:
        print(f"  Status: CLOSE (within 30%)")
    else:
        print(f"  Status: OFF (>30% error)")

    return results


def main():
    """Main routine."""
    print("=" * 70)
    print("PMNS ATTEMPT 4.1: DERIVE EPSILON FROM EDC QUANTITIES")
    print("=" * 70)
    print()
    print("NO SMUGGLING CONSTRAINT:")
    print("  - ε is predicted from λ (and κ ratio), NOT fit to θ13")
    print("  - We compare to PDG AFTER prediction")
    print()
    print("PROVENANCE:")
    print("  - λ = 0.225 [BL]: sections/07_ckm_cp.tex, Eq.(eq:ch7_wolfenstein)")
    print("  - κ_q/κ_ℓ ≈ 0.4 [I]: sections/07_ckm_cp.tex, Eq.(eq:ch7_kappa_ratio)")
    print("  - θ23 ≈ 48.7° [Dc]: sections/ch6_pmns_attempt2.tex (sin²θ23 = 0.564)")
    print()

    all_results = []

    # Candidate C1: ε = λ / √2
    eps_C1, tag_C1, rationale_C1 = compute_epsilon_C1()
    results_C1 = analyze_candidate('C1', eps_C1, tag_C1, rationale_C1)
    all_results.extend(results_C1)

    # Candidate C2: ε = λ × κ_ratio
    eps_C2, tag_C2, rationale_C2 = compute_epsilon_C2()
    results_C2 = analyze_candidate('C2', eps_C2, tag_C2, rationale_C2)
    all_results.extend(results_C2)

    # Summary comparison
    print()
    print("=" * 70)
    print("SUMMARY: ε CANDIDATE COMPARISON")
    print("=" * 70)
    print()
    print(f"PDG θ13: sin²θ13 = {SIN2_THETA13_PDG} → ε_PDG ≈ {np.sqrt(SIN2_THETA13_PDG):.4f} rad")
    print()
    print(f"{'Candidate':<12} {'ε (rad)':<10} {'ε (deg)':<10} {'sin²θ13':<10} {'Tag':<12} {'Source'}")
    print("-" * 70)
    print(f"{'C1: λ/√2':<12} {eps_C1:<10.4f} {np.degrees(eps_C1):<10.2f} {eps_C1**2:<10.4f} {tag_C1:<12} Wolfenstein + √2")
    print(f"{'C2: λ×κ':<12} {eps_C2:<10.4f} {np.degrees(eps_C2):<10.2f} {eps_C2**2:<10.4f} {tag_C2:<12} Wolfenstein + κ ratio")
    print(f"{'PDG target':<12} {np.sqrt(SIN2_THETA13_PDG):<10.4f} {np.degrees(np.sqrt(SIN2_THETA13_PDG)):<10.2f} {SIN2_THETA13_PDG:<10.4f} {'[BL]':<12} PDG 2024")
    print()

    # What κ ratio would be needed for C2 to hit PDG exactly?
    eps_target = np.sqrt(SIN2_THETA13_PDG)
    kappa_needed = eps_target / LAMBDA_WOLFENSTEIN
    print(f"For C2 to hit PDG exactly: κ_q/κ_ℓ = {kappa_needed:.3f} (vs current {KAPPA_RATIO})")
    print()

    # Verdict
    print("=" * 70)
    print("VERDICT")
    print("=" * 70)
    print()

    # C1 analysis
    c1_error = abs(eps_C1**2 - SIN2_THETA13_PDG) / SIN2_THETA13_PDG
    if c1_error < 0.15:
        c1_verdict = "GREEN"
        c1_reason = f"ε = λ/√2 gives sin²θ13 within 15% of PDG"
    elif c1_error < 0.50:
        c1_verdict = "YELLOW"
        c1_reason = f"ε = λ/√2 gives sin²θ13 within 50% of PDG"
    else:
        c1_verdict = "RED"
        c1_reason = f"ε = λ/√2 gives sin²θ13 >50% off from PDG"

    print(f"C1 (ε = λ/√2): {c1_verdict}")
    print(f"   {c1_reason}")
    print(f"   Predicted sin²θ13 = {eps_C1**2:.4f} vs PDG {SIN2_THETA13_PDG}")
    print(f"   Error: {c1_error*100:.1f}%")
    print(f"   Epistemic: {tag_C1} — λ is [BL], √2 is geometric factor")
    print()

    # C2 analysis
    c2_error = abs(eps_C2**2 - SIN2_THETA13_PDG) / SIN2_THETA13_PDG
    if c2_error < 0.15:
        c2_verdict = "GREEN"
        c2_reason = f"ε = λ×κ gives sin²θ13 within 15% of PDG"
    elif c2_error < 0.50:
        c2_verdict = "YELLOW"
        c2_reason = f"ε = λ×κ gives sin²θ13 within 50% of PDG"
    else:
        c2_verdict = "RED"
        c2_reason = f"ε = λ×κ gives sin²θ13 >50% off from PDG"

    print(f"C2 (ε = λ×κ): {c2_verdict}")
    print(f"   {c2_reason}")
    print(f"   Predicted sin²θ13 = {eps_C2**2:.4f} vs PDG {SIN2_THETA13_PDG}")
    print(f"   Error: {c2_error*100:.1f}%")
    print(f"   Epistemic: {tag_C2} — κ ratio is [I], not derived")
    print(f"   Dependency: OPR-10 (κ_q/κ_ℓ derivation) remains OPEN")
    print()

    # Overall assessment
    print("-" * 70)
    print("OVERALL ASSESSMENT")
    print("-" * 70)
    print()
    print("Best candidate: C1 (ε = λ/√2)")
    print(f"  - Predicts sin²θ13 = {eps_C1**2:.4f} ({c1_error*100:.1f}% from PDG)")
    print(f"  - No new [I] dependency (uses only λ [BL] + geometric √2)")
    print()
    print("C2 (ε = λ×κ) is viable but:")
    print(f"  - Depends on κ_q/κ_ℓ ≈ {KAPPA_RATIO} which is [I] (OPR-10)")
    print(f"  - Would need κ ratio ≈ {kappa_needed:.3f} for exact match")
    print()

    # OPR-05 status recommendation
    print("-" * 70)
    print("OPR-05 STATUS UPDATE")
    print("-" * 70)
    print()
    print("θ23: GREEN [Dc] — derived from Z6 geometry (unchanged)")
    print(f"θ13: YELLOW [BL→Dc] — ε = λ/√2 predicts sin²θ13 ≈ {eps_C1**2:.4f} ({c1_error*100:.1f}% off)")
    print("     Not [Cal] because ε is predicted, not fit")
    print("     Not fully [Dc] because λ is [BL] input")
    print("θ12: YELLOW [I] — requires θ12⁰ ≈ 33.7° (identified from PDG, not derived)")
    print()
    print("OVERALL: YELLOW [Dc/I] with ε mechanism partially closed")

    # Save output
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / 'pmns_attempt4_1_results.txt'

    with open(output_file, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("PMNS ATTEMPT 4.1: DERIVE EPSILON FROM EDC QUANTITIES\n")
        f.write("=" * 70 + "\n\n")

        f.write("CANDIDATE COMPARISON\n")
        f.write("-" * 70 + "\n")
        f.write(f"{'Candidate':<12} {'ε (rad)':<10} {'sin²θ13':<10} {'Error':<10} {'Verdict':<10} {'Tag'}\n")
        f.write("-" * 70 + "\n")
        f.write(f"{'C1: λ/√2':<12} {eps_C1:<10.4f} {eps_C1**2:<10.4f} {c1_error*100:<10.1f}% {c1_verdict:<10} {tag_C1}\n")
        f.write(f"{'C2: λ×κ':<12} {eps_C2:<10.4f} {eps_C2**2:<10.4f} {c2_error*100:<10.1f}% {c2_verdict:<10} {tag_C2}\n")
        f.write(f"{'PDG':<12} {np.sqrt(SIN2_THETA13_PDG):<10.4f} {SIN2_THETA13_PDG:<10.4f} {'—':<10} {'—':<10} [BL]\n")
        f.write("\n")

        f.write("FULL PMNS ANALYSIS (Mode B: θ12 = 33.7° [I])\n")
        f.write("-" * 70 + "\n")
        f.write(f"{'Candidate':<12} {'sin²θ12':<10} {'sin²θ23':<10} {'sin²θ13':<10} {'Score':<10} {'Status'}\n")
        f.write("-" * 70 + "\n")

        for r in all_results:
            if r['mode'] == 'B':
                f.write(f"{r['candidate']:<12} {r['angles']['sin2_12']:<10.4f} ")
                f.write(f"{r['angles']['sin2_23']:<10.4f} {r['angles']['sin2_13']:<10.4f} ")
                f.write(f"{r['score']:<10.2f} {r['overall']}\n")

        f.write("\n")
        f.write("VERDICT\n")
        f.write("-" * 70 + "\n")
        f.write(f"C1 (ε = λ/√2): {c1_verdict} — sin²θ13 = {eps_C1**2:.4f} ({c1_error*100:.1f}% off)\n")
        f.write(f"C2 (ε = λ×κ):  {c2_verdict} — sin²θ13 = {eps_C2**2:.4f} ({c2_error*100:.1f}% off)\n")
        f.write("\n")
        f.write("BEST: C1 (ε = λ/√2) closes θ13 scale without new [I] dependency\n")

    print()
    print(f"Results saved to: {output_file}")


if __name__ == '__main__':
    main()
