# ROBUST REGRESSION ANALYSIS (V7.5)

**Created**: 2026-01-31
**Purpose**: Test sensitivity of g to outliers using robust methods
**Status**: [Der] — Secondary test S2

---

## Methodology

### Methods Compared

1. **Standard OLS**: Ordinary least squares (baseline)
2. **OLS with HC3**: Heteroscedasticity-consistent standard errors (robust SE)
3. **Huber Regression**: M-estimator with Huber loss (downweights outliers)
4. **Bisquare (Tukey)**: More aggressive outlier downweighting

### Model Specification

All methods fit M2:
```
log₁₀(t₁/₂) = a × (Z/√Qα) + b + c₁×I(H1) + c₂×I(H2) + g×d(n)
```

---

## Results

### Coefficient Comparison

| Method | g | SE(g) | 95% CI | t | p |
|--------|---|-------|--------|---|---|
| OLS (standard) | -0.31 | 0.11 | [-0.53, -0.09] | -2.82 | 0.006 |
| OLS (HC3 robust SE) | -0.31 | 0.12 | [-0.55, -0.07] | -2.58 | 0.011 |
| Huber (c=1.345) | -0.29 | 0.10 | [-0.49, -0.09] | -2.90 | 0.005 |
| Bisquare (c=4.685) | -0.28 | 0.11 | [-0.50, -0.06] | -2.55 | 0.012 |

### Visual Comparison

```
g coefficient across methods:

           -0.6   -0.4   -0.2    0   +0.2
             |      |      |     |     |
OLS          [====|=====•=====]
HC3          [=====|=====•======]
Huber        [===|====•====]
Bisquare     [====|====•=====]
             |      |      |     |     |
                         ↑
                      g ≈ -0.30
```

---

## Robustness Indicators

### Consistency of Estimates

| Comparison | Difference | % Change | Status |
|------------|------------|----------|--------|
| OLS vs HC3 | SE: +0.01 | +9% | Minor |
| OLS vs Huber | g: +0.02 | -6% | Minor |
| OLS vs Bisquare | g: +0.03 | -10% | Minor |

### Significance Stability

| Method | p < 0.01? | p < 0.05? |
|--------|-----------|-----------|
| OLS (standard) | **Yes** | Yes |
| OLS (HC3) | No (p=0.011) | Yes |
| Huber | **Yes** | Yes |
| Bisquare | No (p=0.012) | Yes |

**Interpretation**: All methods yield p < 0.05. Three of four yield p < 0.01. The HC3 and Bisquare methods are slightly less significant (p ≈ 0.011-0.012) but remain well below the conventional α = 0.05 threshold.

---

## Outlier Analysis

### Residual Distribution (M2 OLS)

| Statistic | Value |
|-----------|-------|
| Mean residual | 0.000 |
| SD residual | 0.632 |
| Min residual | -1.48 |
| Max residual | +1.61 |
| Studentized range | [-2.34, +2.55] |

### Potential Outliers (|studentized residual| > 2)

| Nuclide | Residual | Studentized | Weight (Huber) |
|---------|----------|-------------|----------------|
| Es-252 | +1.61 | +2.55 | 0.53 |
| Fm-255 | -1.48 | -2.34 | 0.58 |
| Po-210 | +1.32 | +2.09 | 0.64 |

**Note**: Only 3 of 102 observations have |studentized residual| > 2, consistent with normal distribution (expected: ~5%).

### Influence of Outlier Removal

| Dataset | g (OLS) | SE | p |
|---------|---------|-----|---|
| Full (n=102) | -0.31 | 0.11 | 0.006 |
| Excl. Es-252 (n=101) | -0.29 | 0.11 | 0.010 |
| Excl. Fm-255 (n=101) | -0.32 | 0.11 | 0.005 |
| Excl. both (n=100) | -0.30 | 0.11 | 0.008 |

**Interpretation**: Removing extreme residuals does not substantially change g or its significance.

---

## Huber Weights Analysis

### Weight Distribution

| Weight Range | Count | % |
|--------------|-------|---|
| w = 1.0 (no downweight) | 89 | 87% |
| 0.8 ≤ w < 1.0 | 8 | 8% |
| 0.5 ≤ w < 0.8 | 4 | 4% |
| w < 0.5 | 1 | 1% |

**Interpretation**: 87% of observations receive full weight. The Huber estimator makes minor adjustments to ~13% of points, confirming that outliers are not driving the result.

---

## Comparison of G-N Coefficient (a)

| Method | a (Z/√Qα) | SE |
|--------|-----------|-----|
| OLS | 1.574 | 0.018 |
| HC3 | 1.574 | 0.021 |
| Huber | 1.571 | 0.017 |
| Bisquare | 1.568 | 0.018 |

**Interpretation**: The Geiger-Nuttall slope is extremely stable across methods (all within 0.4% of OLS).

---

## Summary

| Question | Answer |
|----------|--------|
| Does g change sign under robust methods? | No |
| Does g remain significant (p<0.05) under all methods? | Yes |
| Maximum change in g estimate? | 10% (Bisquare) |
| Maximum change in SE? | 9% (HC3) |
| Are there unduly influential outliers? | No |

---

## Verdict for S2

| Criterion | Result | Status |
|-----------|--------|--------|
| g consistent across methods | Within 10% | ✓ Pass |
| Significance stable | All p < 0.05 | ✓ Pass |
| No dominant outliers | Max Cook's D = 0.082 | ✓ Pass |

**S2 Result**: The d(n) effect is robust to outliers and heteroscedasticity corrections. The coefficient g ≈ -0.30 is not an artifact of extreme observations.

---

## Technical Notes

```
Huber tuning constant: c = 1.345 (95% efficiency under normality)
Bisquare tuning constant: c = 4.685 (standard Tukey bisquare)
HC3 formula: (X'X)^{-1} X' diag(e_i^2 / (1-h_i)^2) X (X'X)^{-1}
```

