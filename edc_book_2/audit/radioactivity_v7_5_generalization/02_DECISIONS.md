# PRE-REGISTRATION OF TESTS (V7.5)

**Created**: 2026-01-31
**Purpose**: Pre-register primary vs secondary analyses for V7.5 generalization tests
**Status**: [Der]

---

## Pre-Registration Statement

This document specifies, before analysis, which tests are **primary** (decision-making) versus **secondary** (exploratory). This prevents p-hacking and ensures the verdict is based on pre-specified criteria.

---

## Primary Tests (Decision-Making)

These tests determine the final V7.5 verdict.

### P1: Cross-Validation Predictive Gain

**Question**: Does M2 (with d(n)) predict out-of-sample better than M1 (without d(n))?

**Method**: 10-fold CV, stratified by hindrance class
**Metric**: ΔRMSE = RMSE(M1) - RMSE(M2)
**Decision rule**:
- ΔRMSE > 0.02 in favor of M2 → Supports generalization
- ΔRMSE ≤ 0.02 or negative → Fails to generalize

### P2: Permutation Test for g(d(n))

**Question**: Is the observed g under M2 significantly different from null?

**Method**: 10,000 permutations of d(n), holding other predictors fixed
**Metric**: p_perm = fraction of |g_perm| ≥ |g_obs|
**Decision rule**:
- p_perm ≤ 0.01 → Supports significance
- p_perm > 0.01 → Fails permutation check

### P3: n(A) Calibration Stability

**Question**: Is g stable across alternative n(A) calibrations?

**Method**: Test 3 alternative calibrations (Alt-A, Alt-B, Alt-C)
**Decision rule**:
- All 3 have same sign AND at least 2/3 have |g| within 50% of baseline → Stable
- Otherwise → Unstable

---

## Secondary Tests (Exploratory)

These tests provide additional insight but do not determine the verdict.

### S1: VIF / Multicollinearity Check

**Question**: Are predictors highly collinear?

**Method**: Compute VIF for each predictor in M2
**Threshold**: VIF > 10 suggests concern
**Status**: Exploratory (does not change verdict)

### S2: Robust Regression

**Question**: Is g sensitive to outliers?

**Method**: Huber regression or OLS with HC3 robust SE
**Comparison**: g and 95% CI under robust vs standard OLS
**Status**: Exploratory

### S3: Within-Element vs Between-Element

**Question**: Is g driven by within-element or between-element variation?

**Method**: Compare g in model with element fixed effects vs without
**Status**: Exploratory (addresses mechanism, not significance)

---

## Verdict Criteria

Based on **primary tests only**:

| Outcome | Verdict |
|---------|---------|
| P1 ✓, P2 ✓, P3 ✓ | **EVIDENCE** (confirmed generalization) |
| P1 ✓, P2 ✓, P3 ~ | **EVIDENCE** (minor calibration sensitivity) |
| 2/3 primary pass | **SUGGESTIVE** |
| ≤1/3 primary pass | **INCONCLUSIVE** (fails to generalize) |

---

## Random Seeds

For reproducibility:
- CV folds: seed = 42
- Permutation test: seed = 123
- Bootstrap (if used): seed = 456

---

## Analysis Order

1. Run P1 (CV) first
2. Run P2 (permutation) second
3. Run P3 (calibration sensitivity) third
4. Then run secondary tests S1-S3
5. Compute verdict from P1-P3 only

---

## Signature

Pre-registered before analysis: 2026-01-31
Analysis commenced: 2026-01-31

