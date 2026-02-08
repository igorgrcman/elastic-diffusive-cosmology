# POWER AND SENSITIVITY ANALYSIS (V7.4)

**Created**: 2026-01-31
**Purpose**: Statistical power and sensitivity analysis for α102 dataset
**Status**: [Der]

---

## Power Analysis

### Current Power (α=0.05, two-tailed)
```
Effect size: r = 0.27
Sample size: n = 102
Achieved power: 82%
```

### Current Power (α=0.01, two-tailed)
```
Effect size: r = 0.27
Sample size: n = 102
Achieved power: 64%
```

**Interpretation**: With n=102, we have good power (82%) to detect the observed effect at α=0.05, and moderate power (64%) at α=0.01. The significant result at p=0.006 is consistent with this power.

---

## Comparison with V7.3

| Metric | V7.3 (n=45) | V7.4 (n=102) |
|--------|-------------|--------------|
| Sample size | 45 | 102 |
| Power at α=0.05 | ~52% | ~82% |
| Power at α=0.01 | ~28% | ~64% |
| Observed p-value | 0.071 | 0.006 |
| Verdict | SUGGESTIVE | EVIDENCE |

**Conclusion**: The expansion from n=45 to n=102 more than doubled the sample size and increased power from ~52% to ~82%, enabling detection of the effect.

---

## Minimum Detectable Effect Size

### At n=102, α=0.05, power=80%:
```
Minimum detectable |r| = 0.27
```

### At n=102, α=0.01, power=80%:
```
Minimum detectable |r| = 0.32
```

**Interpretation**: With 102 nuclides, we can reliably detect correlations of |r| ≥ 0.27 at α=0.05. The observed r = -0.27 is right at this threshold, consistent with borderline but adequate power.

---

## Sample Size for Future Studies

### To detect r = 0.27 at α=0.01 with 90% power:
```
Required n ≈ 140
```

### To detect r = 0.20 at α=0.01 with 80% power:
```
Required n ≈ 200
```

**Recommendation**: If a smaller true effect is suspected (r ~ 0.20), approximately 200 nuclides would be needed.

---

## Sensitivity Analysis: Effect of Sample Size

| n | Power (α=0.05) | Power (α=0.01) | Verdict threshold |
|---|----------------|----------------|-------------------|
| 45 | 52% | 28% | SUGGESTIVE |
| 60 | 64% | 40% | SUGGESTIVE |
| 80 | 75% | 54% | SUGGESTIVE/EVIDENCE |
| 100 | 82% | 64% | EVIDENCE |
| 120 | 87% | 72% | EVIDENCE |
| 150 | 92% | 81% | EVIDENCE |

---

## Sensitivity Analysis: Effect Size Stability

### By Data Subset

| Subset | n | r | p | Stable? |
|--------|---|---|---|---------|
| Full dataset | 102 | -0.27 | 0.006 | — |
| Even-even only | 42 | -0.32 | 0.039 | ✓ |
| Odd-A only | 48 | -0.24 | 0.098 | ✓ |
| H0 only | 82 | -0.29 | 0.007 | ✓ |
| Excluding outliers | 99 | -0.26 | 0.010 | ✓ |
| Z ≤ 90 only | 52 | -0.28 | 0.044 | ✓ |
| Z > 90 only | 50 | -0.25 | 0.082 | ✓ |

**Conclusion**: The effect size is remarkably stable across subsets, ranging from -0.24 to -0.32. This consistency supports the robustness of the finding.

---

## Influence Diagnostics

### Cook's Distance

| Nuclide | Cook's D | Influential? |
|---------|----------|--------------|
| Es-252 | 0.082 | No (D < 1) |
| At-213 | 0.068 | No |
| Rn-214 | 0.054 | No |
| Cf-251 | 0.048 | No |

**Maximum Cook's D**: 0.082 (Es-252)
**Threshold**: D > 1 would indicate influence
**Conclusion**: No individual nuclide has undue influence on the regression.

### Leverage

| Nuclide | Leverage | Notes |
|---------|----------|-------|
| Fm-257 | 0.078 | Highest d(n) |
| Po-206 | 0.072 | Lowest d(n) |
| At-213 | 0.065 | Highest Qα |

**Mean leverage**: 1/n = 0.0098
**Threshold**: > 2/n = 0.0196 is high leverage
**Conclusion**: Some nuclides have higher leverage due to extreme d(n) or Qα, but none are unduly influential.

---

## Leave-One-Out Analysis

### Effect of Removing Each Nuclide

| Removed | New r | Change from -0.271 |
|---------|-------|-------------------|
| Es-252 | -0.264 | +0.007 |
| Cf-251 | -0.268 | +0.003 |
| At-213 | -0.275 | -0.004 |
| Po-206 | -0.269 | +0.002 |
| Fm-257 | -0.272 | -0.001 |

**Conclusion**: No single nuclide changes r by more than ±0.01. The effect is not driven by any individual data point.

---

## Multiple Testing Considerations

### Tests Performed

| Test | Purpose | p-value |
|------|---------|---------|
| M1 vs M2 (LRT) | d(n) significance | 0.005 |
| Pearson correlation | Residuals vs d(n) | 0.006 |
| Spearman correlation | Robustness check | 0.009 |
| Even-even subset | Robustness check | 0.039 |
| H0-only subset | Robustness check | 0.007 |

### Bonferroni Correction

With 5 correlated tests at α = 0.05:
- Adjusted α = 0.01
- Primary test (M1 vs M2): p = 0.005 < 0.01 ✓

**Conclusion**: The primary finding survives Bonferroni correction.

---

## False Discovery Rate

### Benjamini-Hochberg Procedure

| Rank | p-value | Threshold | Significant? |
|------|---------|-----------|--------------|
| 1 | 0.005 | 0.010 | ✓ |
| 2 | 0.006 | 0.020 | ✓ |
| 3 | 0.007 | 0.030 | ✓ |
| 4 | 0.009 | 0.040 | ✓ |
| 5 | 0.039 | 0.050 | ✓ |

**Conclusion**: All 5 tests remain significant under FDR control at q = 0.05.

---

## Minimum Effect for Verdict Thresholds

### At n=102, what effect size gives p=0.01?
```
|r| ≥ 0.25 → p ≤ 0.01
```

### At n=102, what effect size gives p=0.05?
```
|r| ≥ 0.19 → p ≤ 0.05
```

**Observed r = -0.27 exceeds both thresholds.**

---

## Summary

| Metric | Value | Status |
|--------|-------|--------|
| Sample size | 102 | Adequate |
| Power at α=0.05 | 82% | Good |
| Power at α=0.01 | 64% | Moderate |
| Effect stability | ±0.04 | Robust |
| Influential points | 0 | None |
| Multiple testing | Survives correction | ✓ |

**Conclusion**: The statistical analysis is adequately powered, robust to outliers, and survives multiple testing correction. The EVIDENCE verdict is well-supported.

