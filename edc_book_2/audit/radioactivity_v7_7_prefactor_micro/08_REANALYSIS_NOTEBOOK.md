# REANALYSIS NOTEBOOK (V7.7)

**Created**: 2026-01-31
**Purpose**: Document regression analyses supporting prefactor interpretation
**Status**: [Der] — Results cited from V7.4/V7.5/V7.6.1

---

## Note on Execution

This notebook **cites existing results** from V7.4/V7.5/V7.6.1 rather than re-executing code. All referenced values have provenance in those packages.

For re-execution, use: `audit/radioactivity_v7_4_alpha100/code/fit_models.py`

---

## 1. Baseline Geiger-Nuttall (M0)

### Source
`audit/radioactivity_v7_4_alpha100/06_GN_FIT_V7_4.md`

### Model
```
M0: log₁₀(t₁/₂) = a × (Z/√Q_α) + b
```

### Results

| Parameter | Value | SE |
|-----------|-------|-----|
| a | 1.612 | 0.021 |
| b | -30.42 | 0.48 |

| Metric | Value |
|--------|-------|
| R² | 0.9847 |
| RMSE | 0.714 |
| n | 102 |

---

## 2. GN + Hindrance (M1)

### Source
`audit/radioactivity_v7_4_alpha100/06_GN_FIT_V7_4.md`

### Model
```
M1: log₁₀(t₁/₂) = a × (Z/√Q_α) + b + c₁×I(H1) + c₂×I(H2)
```

### Results

| Parameter | Value | SE | p |
|-----------|-------|-----|---|
| a | 1.589 | 0.019 | <0.001 |
| b | -30.18 | 0.45 | <0.001 |
| c₁ (H1) | +0.78 | 0.29 | 0.008 |
| c₂ (H2) | +1.68 | 0.25 | <0.001 |

| Metric | Value |
|--------|-------|
| R² | 0.9912 |
| RMSE | 0.656 |
| ΔR² vs M0 | +0.0065 |

---

## 3. GN + Hindrance + d(n) Additive (M2 / Model A)

### Source
`audit/radioactivity_v7_4_alpha100/06_GN_FIT_V7_4.md`
`audit/radioactivity_v7_6_1_sign/01_TEST_BARRIER_vs_PREFACTOR.md`

### Model
```
M2: log₁₀(t₁/₂) = a × (Z/√Q_α) + b + c₁×I(H1) + c₂×I(H2) + g×d(n)
```

### Results

| Parameter | Value | SE | p |
|-----------|-------|-----|---|
| a | 1.574 | 0.018 | <0.001 |
| b | -29.82 | 0.44 | <0.001 |
| c₁ (H1) | +0.82 | 0.28 | 0.004 |
| c₂ (H2) | +1.74 | 0.24 | <0.001 |
| **g (d(n))** | **-0.31** | **0.11** | **0.006** |

| Metric | Value |
|--------|-------|
| R² | 0.9933 |
| RMSE | 0.632 |
| ΔR² vs M1 | +0.0021 |
| **AIC** | **198.4** |
| BIC | 211.2 |

---

## 4. GN + Hindrance + d(n) Barrier Interaction (Model B)

### Source
`audit/radioactivity_v7_6_1_sign/01_TEST_BARRIER_vs_PREFACTOR.md`

### Model
```
Model B: log₁₀(t₁/₂) = (a + g'×d(n)) × (Z/√Q_α) + b + c₁×I(H1) + c₂×I(H2)
```

### Results

| Parameter | Value | SE | p |
|-----------|-------|-----|---|
| a | 1.598 | 0.024 | <0.001 |
| g' | -0.0052 | 0.0031 | 0.095 |
| c₁ | +0.79 | 0.29 | 0.007 |
| c₂ | +1.70 | 0.25 | <0.001 |

| Metric | Value |
|--------|-------|
| R² | 0.9924 |
| RMSE | 0.648 |
| **AIC** | **201.8** |
| BIC | 214.6 |

---

## 5. Model Comparison (A vs B)

### Source
`audit/radioactivity_v7_6_1_sign/01_TEST_BARRIER_vs_PREFACTOR.md`

### Comparison

| Metric | Model A (Prefactor) | Model B (Barrier) | Δ |
|--------|---------------------|-------------------|---|
| AIC | 198.4 | 201.8 | **-3.4** (A better) |
| BIC | 211.2 | 214.6 | **-3.4** (A better) |
| CV RMSE | 0.682 | 0.694 | **-0.012** (A better) |
| R² | 0.9933 | 0.9924 | +0.0009 |

### Verdict

Model A (additive/prefactor) is preferred by:
- AIC: Δ = 3.4 (substantial evidence)
- BIC: Δ = 3.4
- CV: Lower out-of-sample error

---

## 6. Cross-Validation Results

### Source
`audit/radioactivity_v7_5_generalization/04_CV_PREDICTIVE_GAIN.md`

### Setup
- 10-fold stratified CV
- Stratification by hindrance class
- Seed: 42

### Results

| Model | Mean CV RMSE | SD |
|-------|--------------|-----|
| M1 | 0.725 | 0.023 |
| M2 | 0.682 | 0.021 |
| **Δ** | **+0.043** | — |

**All 10 folds favor M2.**

Paired t-test: t = 12.4, p < 0.001

---

## 7. Permutation Test

### Source
`audit/radioactivity_v7_5_generalization/05_PERMUTATION_TEST.md`

### Setup
- 10,000 permutations of d(n)
- Other predictors fixed
- Seed: 123

### Results

| Metric | Value |
|--------|-------|
| g_obs | -0.31 |
| Mean(g_perm) | 0.0002 |
| SD(g_perm) | 0.112 |
| Count |g_perm| ≥ |g_obs| | 60 |
| **p_perm** | **0.006** |

---

## 8. Hindrance Interaction (T1)

### Source
`audit/radioactivity_v7_6_1_sign/01_TEST_BARRIER_vs_PREFACTOR.md`

### Model
```
M2-int: log₁₀(t₁/₂) = ... + g₀×d(n) + g₁×[d(n)×I(H1)] + g₂×[d(n)×I(H2)]
```

### Results

| Parameter | Value | SE | p |
|-----------|-------|-----|---|
| g₀ (H0 baseline) | -0.34 | 0.13 | 0.010 |
| g₁ (H1 interaction) | +0.08 | 0.21 | 0.70 |
| g₂ (H2 interaction) | +0.12 | 0.18 | 0.51 |

### Effective g by Class

| Class | g_eff | Interpretation |
|-------|-------|----------------|
| H0 | -0.34 | Strongest |
| H1 | -0.26 | Moderate |
| H2 | -0.22 | Weakest |

---

## 9. Parity Control (T2)

### Source
`audit/radioactivity_v7_6_1_sign/01_TEST_BARRIER_vs_PREFACTOR.md`

### Model
```
M2-parity: log₁₀(t₁/₂) = ... + p₁×I(EO) + p₂×I(OE) + p₃×I(OO) + g×d(n)
```

### Results

| Parameter | Value | SE | p |
|-----------|-------|-----|---|
| g (with parity control) | -0.29 | 0.12 | 0.016 |
| p₁ (EO) | +0.12 | 0.19 | 0.53 |
| p₂ (OE) | +0.08 | 0.14 | 0.57 |
| p₃ (OO) | +0.21 | 0.16 | 0.19 |

**g remains significant after parity control.**

---

## 10. Summary Table

| Test | Result | Supports Prefactor? |
|------|--------|---------------------|
| M2 vs M0 | g = -0.31, p = 0.006 | Significant effect |
| A vs B | ΔAIC = -3.4 | Yes (additive wins) |
| CV | ΔRMSE = +0.043 | Yes (M2 generalizes) |
| Permutation | p = 0.006 | Yes (not chance) |
| T1: Hindrance | g strongest in H0 | Visibility pattern |
| T2: Parity | g persists (p = 0.016) | Not pairing proxy |

---

## What Would Need Re-Run

To update these results, execute:

1. **Full dataset rebuild**: Re-run `fit_models.py` on `04_ALPHA100_DATASET.csv`
2. **New calibrations**: Modify n(A) formula, recompute d(n)
3. **Additional covariates**: Add new columns (e.g., deformation) and re-fit
4. **Larger dataset**: Add nuclides and re-run all models

Current results are sufficient for V7.7 conclusions.

