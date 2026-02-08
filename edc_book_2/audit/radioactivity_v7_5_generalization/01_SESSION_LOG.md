# V7.5 SESSION LOG

**Session**: V7.5 Generalization Tests
**Date**: 2026-01-31
**Status**: COMPLETE

---

## Objective

Test generalization and robustness of V7.4 α-decay findings using pre-registered primary and secondary analyses.

---

## Chronological Log

### Phase 1: Pre-Registration

**Task**: Define primary vs secondary tests before analysis
**Output**: `02_DECISIONS.md`
**Result**:
- Primary tests: P1 (CV), P2 (permutation), P3 (calibration sensitivity)
- Secondary tests: S1 (VIF), S2 (robust regression), S3 (hierarchical)
- Verdict thresholds specified

### Phase 2: Model Specification Checks

**Task**: Verify M2 is well-specified (multicollinearity, diagnostics)
**Output**: `03_MODEL_SPEC_CHECKS.md`
**Result**:
- All VIF < 10 (max = 2.87 for d(n))
- Residuals normal (Shapiro-Wilk p = 0.28)
- Homoscedastic (Breusch-Pagan p = 0.31)
- No influential outliers (max Cook's D = 0.082)
- RESET test passes (p = 0.16)

### Phase 3: Cross-Validation (P1)

**Task**: Test out-of-sample predictive improvement of M2 over M1
**Output**: `04_CV_PREDICTIVE_GAIN.md`
**Result**:
- 10-fold stratified CV
- ΔRMSE = +0.043 (M1 - M2)
- All 10 folds favor M2
- Paired t-test: p < 0.001
- **P1: PASS**

### Phase 4: Permutation Test (P2)

**Task**: Distribution-free significance test for g
**Output**: `05_PERMUTATION_TEST.md`
**Result**:
- 10,000 permutations
- p_perm = 0.006 (two-tailed)
- g_obs = -0.31 outside 95% null CI [-0.22, +0.22]
- **P2: PASS**

### Phase 5: Robust Regression (S2)

**Task**: Test sensitivity of g to outliers
**Output**: `06_ROBUST_REGRESSION.md`
**Result**:
- OLS: g = -0.31, p = 0.006
- HC3: g = -0.31, p = 0.011
- Huber: g = -0.29, p = 0.005
- Bisquare: g = -0.28, p = 0.012
- All p < 0.05; coefficient stable within 10%
- **S2: PASS**

### Phase 6: Alternative n(A) Calibrations (P3)

**Task**: Test stability across different n(A) mappings
**Output**: `07_ALTERNATIVE_nA_SENSITIVITY.md`
**Result**:
- Alt-A (Pb-208 anchor): g = -0.30, p = 0.008
- Alt-B (SSE-minimized): g = -0.34, p = 0.006
- Alt-C (piecewise): g = -0.29, p = 0.010
- All same sign, all within 10% of baseline
- **P3: PASS**

### Phase 7: Hierarchical Analysis (S3)

**Task**: Decompose within-element vs between-element effects
**Output**: `08_HIERARCHICAL_OR_GROUPED_CHECK.md`
**Result**:
- Fixed effects: g = -0.28, p = 0.032
- Mixed effects: g = -0.29, p = 0.016
- All 9 elements (n≥4) show negative g
- Within-element effect is primary driver
- **S3: PASS**

### Phase 8: Book 2 Candidates

**Task**: Draft paragraph variants for potential Book 2 inclusion
**Output**: `09_UPDATED_BOOK2_PARAGRAPH_CANDIDATES.md`
**Result**:
- 3 variants (technical, narrative, minimal)
- Recommended: Variant B (122 words)
- Proper caveats included

### Phase 9: Summary and Verdict

**Task**: Evaluate acceptance criteria, determine verdict
**Output**: `00_README.md`
**Result**: See README

---

## Files Created

| File | Description | Status |
|------|-------------|--------|
| 00_README.md | Executive summary | Complete |
| 01_SESSION_LOG.md | This file | Complete |
| 02_DECISIONS.md | Pre-registration | Complete |
| 03_MODEL_SPEC_CHECKS.md | VIF and diagnostics | Complete |
| 04_CV_PREDICTIVE_GAIN.md | 10-fold CV (P1) | Complete |
| 05_PERMUTATION_TEST.md | Permutation test (P2) | Complete |
| 06_ROBUST_REGRESSION.md | Robust methods (S2) | Complete |
| 07_ALTERNATIVE_nA_SENSITIVITY.md | Calibration sensitivity (P3) | Complete |
| 08_HIERARCHICAL_OR_GROUPED_CHECK.md | Within-element analysis (S3) | Complete |
| 09_UPDATED_BOOK2_PARAGRAPH_CANDIDATES.md | Book 2 text candidates | Complete |

---

## Key Findings

1. **P1 (CV)**: M2 generalizes with ΔRMSE = 0.043 > 0.02 threshold
2. **P2 (Permutation)**: p_perm = 0.006 < 0.01 threshold
3. **P3 (Calibration)**: g stable across all alternative n(A) choices
4. **S2 (Robust)**: g insensitive to outliers
5. **S3 (Hierarchical)**: Effect is within-element, not between-element confounding

---

## Verdict

Based on primary tests:
- P1: ✓ PASS
- P2: ✓ PASS
- P3: ✓ PASS

**V7.5 VERDICT: EVIDENCE** — V7.4 findings generalize.

---

## Guardrail Compliance

| Guardrail | Status |
|-----------|--------|
| G0: No hallucinated data | ✓ Reused V7.4 dataset |
| G1: Whitelist sources only | ✓ No new data sourcing |
| G2: No Book 2 edits | ✓ Candidates only |
| G3: Full provenance | ✓ All methods documented |
| G4: Reproducible | ✓ Seeds specified |
| G5: No re-mining | ✓ Analysis only |
| G6: Epistemic tags | ✓ [Der] throughout |
| G7: No supernova/fission | ✓ α-decay only |

---

## Session Duration

- Start: 2026-01-31
- End: 2026-01-31
- Files: 10

