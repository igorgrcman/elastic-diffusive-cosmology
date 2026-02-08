# RADIOACTIVITY V7.4: α102 DATASET — EVIDENCE-GRADE ANALYSIS

**Version**: 7.4
**Created**: 2026-01-31
**Parent**: V7.3 (audit/radioactivity_v7_3_alpha45/)
**Purpose**: Expand dataset to α100+ for definitive statistical power on d(n) effect

---

## Executive Summary

V7.4 expands the α-decay dataset from 45 to **102 nuclides**, specifically targeting:
- **H1+H2 nuclides**: 20 total (8 H1 + 12 H2) — exceeds target of 12
- **Odd-odd nuclides**: 12 (was 0 in V7.3) — new category for hindrance diversity
- **High-Qα (≥6 MeV)**: 59 nuclides — exceeds target of 18
- **Elements covered**: 18 (Z = 83 to 100) — includes new Bi, Pa, Bk, Es, Fm

**Main Finding**: After hindrance control, d(n) shows coefficient:
```
g = -0.31 ± 0.11
t = -2.82
p = 0.006
95% CI: [-0.53, -0.09]
```

**The 95% CI excludes zero. This is statistically significant at p < 0.01.**

**Verdict**: **SUGGESTIVE → EVIDENCE** (upgrade from V7.3)
- Effect direction confirmed (negative: frustrated nuclei decay faster)
- Statistical power now adequate (82% at α=0.05)
- Result robust across even-even subset, outlier exclusion, and bootstrap

---

## Acceptance Criteria Evaluation

| Criterion | Target | Achieved | Status |
|-----------|--------|----------|--------|
| AC1: Dataset rows 95-110 | 95-110 | **102** | ✓ PASS |
| AC2: 100% BL for Qα and t₁/₂ | 100% | **100%** | ✓ PASS |
| AC3: High-Qα ≥18 | 18 | **59** | ✓ PASS |
| AC4: H1+H2 ≥12 OR proven impossible | 12 | **20** | ✓ PASS |
| AC5: Models 0-3 run, CI and p-values | Yes | **Yes** | ✓ PASS |
| AC6: Verdict stated with thresholds | EVIDENCE/SUGGESTIVE/NULL | **EVIDENCE** | ✓ PASS |
| AC7: No guardrail violations | None | **None** | ✓ PASS |

**All 7 acceptance criteria met.**

---

## Verdict Thresholds (from V7.4 prompt)

| Verdict | Threshold | Status |
|---------|-----------|--------|
| EVIDENCE | p ≤ 0.01, stable sign, robust | **✓ MET** |
| SUGGESTIVE | p ≤ 0.10, stable sign | (exceeded) |
| NULL | p > 0.10 or sign unstable | — |

**Achieved**: p = 0.006 < 0.01, sign stable across all robustness checks → **EVIDENCE**

---

## File Index

| File | Description |
|------|-------------|
| 00_README.md | This summary |
| 01_SESSION_LOG.md | Work chronology with BL fetch details |
| 02_SOURCES_AND_VERSIONS.md | BL whitelist with access dates |
| 03_ALPHA100_RAW_BL.md | Verbatim BL data for all 57 additions |
| 04_ALPHA100_DATASET.csv | Machine-readable 102-nuclide dataset |
| 04_ALPHA100_DATASET.md | Human-readable + coverage summary |
| 05_HINDRANCE_AUDIT_V7_4.md | H0/H1/H2 classification (82/8/12) |
| 06_GN_FIT_V7_4.md | Models 0-3 with full statistics |
| 07_RESIDUALS_DN_CORRELATION_V7_4.md | Correlation analysis (r=-0.27, p=0.006) |
| 08_POWER_AND_SENSITIVITY_V7_4.md | Power analysis and robustness |
| 09_BRANCHPOINTS_SCORECARD_V7_4.md | Extended branchpoint analysis (7/8 match) |
| 10_DATASET_COVERAGE_SCORECARD.md | Bucket counts and coverage |
| 11_DATA_GAPS_V7_4.md | Remaining missing BL items |
| 12_BOOK2_PARAGRAPH_UPDATE_V7_4.md | Evidence-grade Book 2 paragraph |
| code/build_dataset.py | Dataset construction script |
| code/fit_models.py | G-N regression models |

---

## Key Results

### Model Comparison

| Model | Parameters | R² | AIC | d(n) coeff | p-value |
|-------|------------|-----|-----|------------|---------|
| M0: G-N baseline | 2 | 0.9847 | 278.4 | — | — |
| M1: +Hindrance | 4 | 0.9912 | 256.8 | — | — |
| M2: +Hindrance+d(n) | 5 | 0.9933 | 248.6 | **-0.31** | **0.006** |
| M3: +d(n) only | 3 | 0.9867 | 273.2 | -0.27 | 0.027 |

### Robustness Checks

| Check | n | g | p | Sign stable? |
|-------|---|---|---|--------------|
| Full dataset | 102 | -0.31 | 0.006 | ✓ |
| Even-even only | 42 | -0.34 | 0.028 | ✓ |
| Excluding 3 outliers | 99 | -0.29 | 0.010 | ✓ |
| H0 only | 82 | -0.32 | 0.008 | ✓ |
| Bootstrap mean | — | -0.31 | — | ✓ |

### d(n) Effect Summary

| Statistic | Value |
|-----------|-------|
| Coefficient g | -0.31 |
| Standard Error | 0.11 |
| 95% CI | [-0.53, -0.09] |
| p-value | 0.006 |
| Effect size r | -0.27 |
| Power (α=0.05) | 82% |

**Interpretation**: Each unit increase in d(n) corresponds to ~0.31 log-units decrease in t₁/₂, or approximately a factor of 2× faster decay.

---

## Dataset Expansion Summary

| Metric | V7.3 | V7.4 | Change |
|--------|------|------|--------|
| Total nuclides | 45 | 102 | +57 |
| Elements | 13 | 18 | +5 |
| H0 | 39 | 82 | +43 |
| H1 | 4 | 8 | +4 |
| H2 | 2 | 12 | +10 |
| Odd-odd | 0 | 12 | +12 |
| High-Qα | 19 | 59 | +40 |
| Long-lived | 18 | 56 | +38 |

### New Elements Added

| Element | Z | Nuclides Added |
|---------|---|----------------|
| Bi | 83 | 2 (Bi-211, Bi-212) |
| Pa | 91 | 2 (Pa-227, Pa-231) |
| Bk | 97 | 3 (Bk-245, Bk-246, Bk-247) |
| Es | 99 | 6 (Es-250 to Es-255) |
| Fm | 100 | 6 (Fm-252 to Fm-257) |

---

## Comparison with V7.3

| Metric | V7.3 | V7.4 | Improvement |
|--------|------|------|-------------|
| Sample size | 45 | 102 | 2.3× |
| p-value | 0.071 | 0.006 | 12× more significant |
| 95% CI | [-1.08, +0.04] | [-0.53, -0.09] | Excludes zero |
| Power | 52% | 82% | +30% |
| Verdict | SUGGESTIVE | EVIDENCE | **Upgraded** |

---

## Guardrail Compliance

| Guardrail | Status |
|-----------|--------|
| G0: No hallucinated data | ✓ All BL-cited |
| G1: Whitelist only | ✓ S1-S5 only |
| G2: No Book 2 edits | ✓ Output to audit/ only |
| G3: Full provenance | ✓ All rows have BL_source |
| G4: Reproducible pipeline | ✓ code/ directory |
| G5: No re-mining jsonl | ✓ Used existing donors |
| G6: Epistemic tags | ✓ [BL], [Der], [P] used |
| G7: No supernova/fission | ✓ α-decay only |

---

## Conclusion

The V7.4 analysis provides **statistical evidence** (p = 0.006) for the EDC prediction that coordination frustration accelerates α-decay. The effect is:
- **Significant**: p < 0.01, 95% CI excludes zero
- **Correctly signed**: Negative (as predicted)
- **Robust**: Stable across subsets and bootstrap
- **Moderate in size**: r = -0.27, factor of ~2× per unit d(n)

Nuclear structure (spin-parity) remains the primary driver, but M-topology coordination provides a secondary, measurable modulation of decay rates within allowed channels.

**For Book 2**: The text can now state that the d(n) effect is "confirmed" with appropriate caveats about effect size and the primacy of structure effects.

