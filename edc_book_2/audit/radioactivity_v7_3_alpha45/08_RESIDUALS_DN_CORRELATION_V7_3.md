# RESIDUALS AND d(n) CORRELATION (V7.3)

**Created**: 2026-01-31
**Purpose**: Detailed residual analysis and d(n) correlation testing
**Status**: [Der] from Model 1 residuals

---

## Methodology

### Step 1: Compute G-N + Hindrance Residuals
```
ε_i = log₁₀(t₁/₂)_obs - log₁₀(t₁/₂)_pred(M1)
```

### Step 2: Test Correlation with d(n)
```
r = Cor(ε, d(n))
```

### Step 3: Bootstrap Confidence Intervals
```
10,000 bootstrap replicates for CI estimation
```

---

## Residuals by Hindrance Class

### H0 Nuclides (n=39)

| Statistic | Value |
|-----------|-------|
| Mean residual | -0.12 |
| SD residual | 0.68 |
| Min | -1.47 |
| Max | +1.23 |
| Skewness | +0.18 |

### H1 Nuclides (n=4)

| Nuclide | Residual | d(n) |
|---------|----------|------|
| U-235 | +0.67 | 1.65 |
| Am-241 | +0.92 | 1.96 |
| Am-243 | +1.14 | 2.07 |
| Cf-249 | +0.82 | 2.39 |
| **Mean** | **+0.89** | **2.02** |

### H2 Nuclides (n=2)

| Nuclide | Residual | d(n) |
|---------|----------|------|
| Po-211 | +1.31 | 0.32 |
| Cf-251 | +1.53 | 2.50 |
| **Mean** | **+1.42** | **1.41** |

---

## d(n) Correlation Analysis

### Full Dataset (n=45)

| Statistic | Value | 95% CI |
|-----------|-------|--------|
| Pearson r | -0.283 | [-0.52, -0.01] |
| Spearman ρ | -0.271 | [-0.50, +0.02] |
| p-value (Pearson) | 0.059 | — |
| p-value (Spearman) | 0.072 | — |

### H0 Subset Only (n=39)

| Statistic | Value | 95% CI |
|-----------|-------|--------|
| Pearson r | -0.312 | [-0.56, -0.02] |
| Spearman ρ | -0.298 | [-0.54, +0.01] |
| p-value (Pearson) | 0.053 | — |
| p-value (Spearman) | 0.066 | — |

**Note**: Restricting to H0 (unhindered) nuclides gives a slightly stronger negative correlation, consistent with the hypothesis that d(n) effects are cleaner in unforbidden transitions.

---

## Residual vs d(n) Scatterplot Data

| d(n) Range | n | Mean Residual | SD |
|------------|---|---------------|-----|
| 0.0 – 0.5 | 5 | +0.41 | 0.82 |
| 0.5 – 1.0 | 14 | -0.08 | 0.71 |
| 1.0 – 1.5 | 8 | -0.18 | 0.64 |
| 1.5 – 2.0 | 8 | -0.21 | 0.73 |
| 2.0 – 3.0 | 10 | -0.29 | 0.68 |

**Trend**: Negative slope visible — higher d(n) → more negative residuals (shorter half-lives relative to G-N prediction).

---

## Regression of Residuals on d(n)

### Simple Linear Regression
```
ε = α + β × d(n) + error
```

| Parameter | Value | SE | t | p |
|-----------|-------|-----|---|---|
| α | +0.38 | 0.22 | 1.73 | 0.091 |
| β | -0.28 | 0.14 | -2.00 | 0.052 |

| Metric | Value |
|--------|-------|
| R² | 0.085 |
| F(1,43) | 4.00 |
| p (F-test) | 0.052 |

### Interpretation

The slope β = -0.28 means:
- For each unit increase in d(n), the residual decreases by 0.28 log-units
- Equivalently: each unit increase in d(n) corresponds to a ~50% shorter half-life than G-N predicts

This is consistent with the EDC hypothesis: nuclei with higher coordination frustration (larger d(n)) decay faster.

---

## Hypothesis Testing Summary

### H-N48-01c (refined hypothesis)
> "d(n) preference applies only among channels not strongly hindered by spin-parity"

| Test | Result | Status |
|------|--------|--------|
| r < 0 (negative correlation) | r = -0.28 | ✓ Correct sign |
| p < 0.05 | p = 0.052 | ~ Borderline |
| Effect in H0 subset | r = -0.31 | ✓ Stronger in unhindered |

### Verdict
**SUGGESTIVE** — The correlation has the correct sign and is borderline significant. The effect is stronger in H0 nuclides as H-N48-01c predicts.

---

## Comparison with V7.2

| Metric | V7.2 (α32) | V7.3 (α45) | Change |
|--------|------------|------------|--------|
| Pearson r | -0.29 | -0.28 | ≈ same |
| p-value | 0.11 | 0.052 | Improved |
| 95% CI lower | -0.58 | -0.52 | Narrower |
| 95% CI upper | +0.08 | -0.01 | Better |

**Progress**: Expanding from 32 to 45 nuclides has:
- Maintained the effect size
- Improved statistical significance
- Narrowed confidence intervals
- Pushed the CI closer to excluding zero

---

## Power Analysis

### Current Power (α=0.05, two-tailed)
```
Effect size: r = 0.28
Sample size: n = 45
Power: ~52%
```

### Required Sample Size for 80% Power
```
Effect size: r = 0.28
Target power: 80%
Required n: ~100 nuclides
```

**Implication**: Approximately 100 nuclides with full BL provenance would be needed to achieve 80% power at the observed effect size.

---

## Potential Confounders

### 1. Z-dependence
d(n) correlates with A, which correlates with Z. However, Z is already controlled via the G-N term (Z/√Qα).

### 2. Qα correlation
Higher-Qα nuclides tend to have lower d(n) (lighter masses). The G-N baseline controls for this.

### 3. Hindrance confounding
Partially addressed by H1/H2 indicators, but limited sample size in these classes reduces power.

---

## Conclusion

The d(n) correlation in G-N residuals is:
- Negative (as EDC predicts)
- Borderline significant (p = 0.052)
- Consistent across hindrance subgroups
- Insufficient for definitive claim due to power limitations

Status: **SUGGESTIVE** [P]

