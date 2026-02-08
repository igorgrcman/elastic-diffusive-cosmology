# RADIOACTIVITY V7.2: HINDERED α + STRUCTURE FIRST

**Version**: 7.2
**Created**: 2026-01-31
**Parent**: V7.1 (audit/radioactivity_v7_1_alpha15/)
**Purpose**: Test d(n) signal after controlling for hindrance and nuclear structure

---

## Executive Summary

V7.2 implements a "structure first" approach: before testing d(n), we first control for nuclear structure effects (spin-parity hindrance). This addresses the V7.1 finding that d(n) showed only a borderline-significant signal (p = 0.056).

**Dataset**: α32 (32 nuclides with full BL data)

**Analysis Pipeline**:
- Model 0: Baseline G-N (Z/√Qα only)
- Model 1: G-N residual ~ HindranceClass
- Model 2: G-N residual ~ HindranceClass + d(n)
- Model 3: G-N residual ~ HindranceClass + d(n) + d(n)²

**Main Finding**:
After controlling for hindrance class, the d(n) coefficient in Model 2 is:
- **g = -0.58 ± 0.35** (p = 0.11)
- **Status: INCONCLUSIVE** — effect direction consistent but not significant

The hindrance class alone (Model 1) explains more variance than d(n) alone, confirming that **nuclear structure dominates over topological coordination**.

---

## Book 2 Ready Paragraph (≤250 words)

The M-topology coordination law predicts that nuclei with effective coordination n far from the allowed set S = {2^a × 3^b} should experience "topological frustration." We tested whether this frustration manifests in α-decay half-lives by fitting Geiger-Nuttall residuals against the coordination distance d(n).

Using a 32-nuclide dataset spanning Z = 84–98 and A = 209–252, we first established that the classic Geiger-Nuttall law explains 98.5% of half-life variance (R² = 0.985). We then classified decays by spin-parity hindrance: H0 (ΔJ ≤ 2, no parity change), H1 (ΔJ ≤ 2 with parity change), and H2 (ΔJ > 2 or multiply hindered).

In hierarchical regression, hindrance class reduces residual variance significantly (p < 0.05). Adding d(n) provides a small additional improvement (ΔR² ≈ 0.01) in the expected direction — nuclei with larger d(n) decay faster than G-N predicts — but the effect is not statistically significant (p = 0.11).

We conclude that **topological frustration may contribute to α-decay rates, but the effect is weak compared to nuclear structure factors** (Coulomb barrier, centrifugal potential, spin-parity selection). The coordination law successfully describes chain trajectories (monotonic d(n) decrease) but does not provide quantitative predictions for individual decay rates.

This result is consistent with the M-topology framework's role as a geometric constraint rather than a dynamical law: it specifies where nuclei can stably exist, not how fast they decay.

---

## File Index

| File | Description |
|------|-------------|
| 00_README.md | This summary |
| 01_SESSION_LOG.md | Work chronology |
| 02_DECISIONS.md | Methodological choices |
| 03_SOURCES_AND_VERSIONS.md | BL whitelist |
| 04_ALPHA30_RAW_BL.md | Verbatim BL tables |
| 05_ALPHA30_DATASET.csv | Machine-readable dataset |
| 05_ALPHA30_DATASET.md | Human-readable + coverage |
| 06_HINDRANCE_RULES.md | Classification definitions |
| 07_FIT_RESULTS_HINDRANCE.md | Models 0–3 + comparison |
| 08_BRANCHPOINTS_SCORECARD_V7_2.md | Extended branchpoint analysis |
| 09_N48_N54_TARGET_SWITCH.md | Target transition analysis |
| 10_DATA_GAPS_V7_2.md | Missing data inventory |

---

## Acceptance Criteria Status

| Criterion | Status |
|-----------|--------|
| AC1: ≥25 nuclides with full BL | ✓ 32 nuclides |
| AC2: Model 1–3 with verdict | ✓ INCONCLUSIVE |
| AC3: No hallucinated numbers | ✓ All BL-sourced |
| AC4: Book 2 paragraph | ✓ Above |

