# V7.5 GENERALIZATION TESTS — EXECUTIVE SUMMARY

**Created**: 2026-01-31
**Purpose**: Test robustness and generalization of V7.4 α-decay findings
**Dataset**: V7.4 102-nuclide α-emitter dataset (reused, no new data)
**Verdict**: **EVIDENCE** (all primary tests pass)

---

## Key Results

| Test | Type | Threshold | Observed | Status |
|------|------|-----------|----------|--------|
| P1: Cross-Validation | Primary | ΔRMSE > 0.02 | **0.043** | ✓ PASS |
| P2: Permutation Test | Primary | p_perm ≤ 0.01 | **0.006** | ✓ PASS |
| P3: Calibration Sensitivity | Primary | Stable sign/magnitude | **All stable** | ✓ PASS |
| S1: VIF Check | Secondary | VIF < 10 | max 2.87 | ✓ PASS |
| S2: Robust Regression | Secondary | g stable | within 10% | ✓ PASS |
| S3: Within-Element | Secondary | g survives FE | g = -0.28, p = 0.032 | ✓ PASS |

---

## Effect Summary

| Metric | V7.4 Value | V7.5 Validation |
|--------|------------|-----------------|
| g (d(n) coefficient) | -0.31 ± 0.11 | Confirmed |
| p-value (OLS) | 0.006 | p_perm = 0.006 |
| ΔR² | 0.84% | CV ΔRMSE = 0.043 |
| 95% CI | [-0.53, -0.09] | Robust: [-0.55, -0.07] |

---

## Generalization Evidence

### Cross-Validation (P1)

- **10-fold stratified CV** on 102 nuclides
- **All 10 folds** favor M2 over M1
- **Out-of-sample improvement**: ΔRMSE = 0.043 (2× threshold)
- **Conclusion**: d(n) improves prediction, not just in-sample fit

### Permutation Test (P2)

- **10,000 permutations** of d(n)
- **Only 60/10,000** (0.6%) as extreme as observed
- **Distribution-free p-value**: 0.006
- **Conclusion**: Effect is not chance correlation

### Calibration Sensitivity (P3)

- Tested 3 alternative n(A) calibrations:
  - Alt-A (Pb-208 anchor): g = -0.30
  - Alt-B (SSE-minimized): g = -0.34
  - Alt-C (piecewise): g = -0.29
- **All same sign**, all within 10% of baseline
- **Conclusion**: Result not dependent on calibration choice

---

## Robustness Checks

### Outlier Sensitivity (S2)

| Method | g | p |
|--------|---|---|
| Standard OLS | -0.31 | 0.006 |
| Robust SE (HC3) | -0.31 | 0.011 |
| Huber M-estimator | -0.29 | 0.005 |
| Bisquare | -0.28 | 0.012 |

**Conclusion**: g is not driven by outliers

### Within-Element Analysis (S3)

- **Fixed effects model**: g = -0.28, p = 0.032
- **All 9 elements** (with n≥4) show negative g
- **Conclusion**: Effect operates within elements (among isotopes), not just between elements

---

## Acceptance Criteria Evaluation

### AC-V7.5 Criteria

| ID | Criterion | Status |
|----|-----------|--------|
| AC-1 | CV improvement exceeds threshold | ✓ 0.043 > 0.02 |
| AC-2 | Permutation p ≤ 0.01 | ✓ 0.006 ≤ 0.01 |
| AC-3 | g stable across n(A) alternatives | ✓ All within 10% |
| AC-4 | No new data sourcing (reuse V7.4) | ✓ Compliant |
| AC-5 | Pre-registered analysis | ✓ 02_DECISIONS.md |

**All AC-V7.5 criteria met.**

---

## Verdict Logic

From pre-registration (02_DECISIONS.md):

| Outcome | Verdict |
|---------|---------|
| P1 ✓, P2 ✓, P3 ✓ | **EVIDENCE** |

**V7.5 VERDICT: EVIDENCE** — V7.4 findings robustly generalize.

---

## Interpretation

The V7.5 analysis confirms that the V7.4 finding (g = -0.31, p = 0.006) is:

1. **Generalizable**: Predicts out-of-sample with consistent improvement
2. **Robust**: Insensitive to outliers, calibration choices, and estimation method
3. **Within-element**: Not confounded by between-element variation
4. **Significant**: Confirmed by both parametric and non-parametric tests

The M-topology coordination distance d(n) is a genuine predictor of α-decay half-lives beyond the Geiger-Nuttall law and hindrance classification.

---

## Files in This Folder

| File | Description |
|------|-------------|
| 00_README.md | This summary |
| 01_SESSION_LOG.md | Chronological work log |
| 02_DECISIONS.md | Pre-registration of tests |
| 03_MODEL_SPEC_CHECKS.md | VIF and diagnostics |
| 04_CV_PREDICTIVE_GAIN.md | 10-fold CV results (P1) |
| 05_PERMUTATION_TEST.md | Permutation test (P2) |
| 06_ROBUST_REGRESSION.md | Huber/HC3 analysis (S2) |
| 07_ALTERNATIVE_nA_SENSITIVITY.md | Calibration sensitivity (P3) |
| 08_HIERARCHICAL_OR_GROUPED_CHECK.md | Within-element analysis (S3) |
| 09_UPDATED_BOOK2_PARAGRAPH_CANDIDATES.md | Draft text for Book 2 |

---

## Epistemic Status

All analyses in this folder carry tag **[Der]** — derived from V7.4 BL-sourced data using standard statistical methods. No theoretical claims beyond statistical association.

---

## Reproducibility

- CV seed: 42
- Permutation seed: 123
- Dataset: `../radioactivity_v7_4_alpha100/04_ALPHA100_DATASET.csv`
- Methods: sklearn StratifiedKFold, numpy.random.permutation, statsmodels OLS/RLM

