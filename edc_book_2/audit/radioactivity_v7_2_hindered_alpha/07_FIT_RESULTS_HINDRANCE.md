# FIT RESULTS WITH HINDRANCE CONTROL (V7.2)

**Created**: 2026-01-31
**Purpose**: Test d(n) effect after controlling for nuclear structure
**Dataset**: α32 (32 nuclides)

---

## Model 0: Baseline Geiger-Nuttall [Der]

### Formulation
```
log₁₀(t₁/₂) = a × (Z / √Qα) + b
```

### Input Data (abbreviated)

| Nuclide | Z | Qα (MeV) | Z/√Qα | t₁/₂ (s) | log₁₀(t₁/₂) | H | d(n) |
|---------|---|----------|-------|----------|-------------|---|------|
| ²¹²Po | 84 | 8.954 | 28.07 | 2.94×10⁻⁷ | -6.53 | H0 | 0.39 |
| ²¹⁴Po | 84 | 7.834 | 30.01 | 1.64×10⁻⁴ | -3.79 | H0 | 0.50 |
| ²³²Th | 90 | 4.082 | 44.55 | 4.42×10¹⁷ | 17.65 | H0 | 1.48 |
| ²³⁵U | 92 | 4.678 | 42.54 | 2.22×10¹⁶ | 16.35 | H1 | 1.65 |
| ²⁴¹Am | 95 | 5.638 | 40.02 | 1.37×10¹⁰ | 10.14 | H1 | 1.96 |
| ²⁵²Cf | 98 | 6.217 | 39.30 | 8.35×10⁷ | 7.92 | H0 | 2.56 |

### Results

| Parameter | Value | Std Error | 95% CI |
|-----------|-------|-----------|--------|
| a (slope) | **1.487** | 0.031 | [1.42, 1.55] |
| b (intercept) | **-48.32** | 1.15 | [-50.6, -46.0] |

### Fit Statistics

| Metric | Value |
|--------|-------|
| R² | **0.985** |
| Adjusted R² | 0.984 |
| RMSE | 1.21 |
| n | 32 |
| df | 30 |

**Interpretation**: Excellent baseline fit. G-N explains 98.5% of variance.

---

## Model 0 Residuals

| # | Nuclide | Observed | Predicted | Residual | H | d(n) |
|---|---------|----------|-----------|----------|---|------|
| 1 | ²⁰⁹Po | 9.59 | 7.66 | +1.93 | H0 | 0.20 |
| 2 | ²¹⁰Po | 7.08 | 5.40 | +1.68 | H0 | 0.26 |
| 3 | ²¹²Po | -6.53 | -6.55 | +0.02 | H0 | 0.39 |
| 4 | ²¹⁴Po | -3.79 | -3.67 | -0.12 | H0 | 0.50 |
| 5 | ²¹⁵Po | -2.75 | -2.54 | -0.21 | H0 | 0.56 |
| 6 | ²¹⁶Po | -0.84 | -0.72 | -0.12 | H0 | 0.61 |
| 7 | ²¹¹At | 4.41* | 3.18 | +1.23 | H0 | 0.32 |
| 8 | ²¹⁷At | -1.49 | -0.97 | -0.52 | H0 | 0.67 |
| 9 | ²¹⁹Rn | 0.60 | 0.97 | -0.37 | H0 | 0.77 |
| 10 | ²²⁰Rn | 1.75 | 2.27 | -0.52 | H0 | 0.83 |
| 20 | ²³⁵U | 16.35 | 14.92 | **+1.43** | **H1** | 1.65 |
| 27 | ²⁴¹Am | 10.14 | 11.18 | **-1.04** | **H1** | 1.96 |
| 28 | ²⁴³Am | 11.37 | 11.96 | **-0.59** | **H1** | 2.07 |
| 32 | ²⁵²Cf | 7.92 | 10.14 | -2.22 | H0 | 2.56 |

*At-211 uses t₁/₂(α) = 17.26 h

**Observation**: H1 nuclides (²³⁵U, ²⁴¹Am, ²⁴³Am) show mixed residuals, not systematically positive.

---

## Model 1: G-N Residual ~ Hindrance Class

### Formulation
```
residual₀ = β₁ × I(H1) + ε
```

Where I(H1) = 1 for H1 class, 0 for H0 (reference).

Note: No H2 nuclides in dataset.

### Results

| Parameter | Value | Std Error | t-stat | p-value |
|-----------|-------|-----------|--------|---------|
| Intercept (H0 mean) | -0.17 | 0.19 | -0.89 | 0.38 |
| β₁ (H1 effect) | **-0.07** | 0.65 | -0.11 | **0.91** |

### Fit Statistics

| Metric | Value |
|--------|-------|
| R² | 0.0004 |
| F-statistic | 0.01 |
| p(F) | 0.91 |

**Interpretation**: Hindrance class H1 shows **no significant effect** on G-N residuals. This is surprising — H1 decays should be slower.

### Why H1 Effect Is Not Detected

1. **Small sample**: Only 3 H1 nuclides (²³⁵U, ²⁴¹Am, ²⁴³Am)
2. **Mixed signals**: ²³⁵U has positive residual (+1.43), Am isotopes have negative
3. **Confounding**: These are all odd-A actinides with similar structure

---

## Model 2: G-N Residual ~ Hindrance + d(n)

### Formulation
```
residual₀ = β₁ × I(H1) + g × d(n) + ε
```

### Results

| Parameter | Value | Std Error | t-stat | p-value |
|-----------|-------|-----------|--------|---------|
| Intercept | 0.72 | 0.42 | 1.71 | 0.098 |
| β₁ (H1 effect) | 0.52 | 0.68 | 0.76 | 0.45 |
| g (d(n) coeff) | **-0.58** | 0.35 | -1.66 | **0.108** |

### Fit Statistics

| Metric | Value |
|--------|-------|
| R² | 0.087 |
| Adjusted R² | 0.024 |
| RMSE | 1.07 |
| F-statistic | 1.38 |
| p(F) | 0.27 |

### Model Comparison

| Metric | Model 0 (G-N) | Model 1 (+H) | Model 2 (+H+d(n)) |
|--------|---------------|--------------|-------------------|
| Residual R² | — | 0.0004 | 0.087 |
| AIC | 106.2 | 108.1 | 106.8 |
| ΔAIC vs Model 0 | — | +1.9 | +0.6 |

**Interpretation**:
- d(n) coefficient g = -0.58 is in the expected direction (more frustration → faster decay)
- But p = 0.108 > 0.05, so **not statistically significant**
- Adding d(n) improves fit slightly but not enough to justify the extra parameter

---

## Model 3: G-N Residual ~ Hindrance + d(n) + d(n)²

### Formulation (pre-registered in DECISIONS.md)
```
residual₀ = β₁ × I(H1) + g₁ × d(n) + g₂ × d(n)² + ε
```

### Results

| Parameter | Value | Std Error | t-stat | p-value |
|-----------|-------|-----------|--------|---------|
| Intercept | 0.25 | 0.82 | 0.30 | 0.77 |
| β₁ (H1 effect) | 0.47 | 0.70 | 0.67 | 0.51 |
| g₁ (d(n) linear) | 0.25 | 1.18 | 0.21 | 0.83 |
| g₂ (d(n)²) | **-0.32** | 0.42 | -0.76 | **0.45** |

### Fit Statistics

| Metric | Value |
|--------|-------|
| R² | 0.105 |
| Adjusted R² | 0.009 |
| F-statistic | 1.10 |
| p(F) | 0.37 |

**Interpretation**:
- Quadratic term is not significant (p = 0.45)
- No evidence for non-linear d(n) effect
- **Model 3 does not improve on Model 2**

---

## Summary Comparison

| Model | Parameters | R² (residual) | AIC | Verdict |
|-------|------------|---------------|-----|---------|
| 0: G-N baseline | 2 | — | 106.2 | Excellent fit |
| 1: +Hindrance | 3 | 0.0004 | 108.1 | No improvement |
| 2: +H+d(n) | 4 | 0.087 | 106.8 | Slight improvement, not sig. |
| 3: +H+d(n)+d(n)² | 5 | 0.105 | 108.3 | Overfitting |

---

## Key Finding

### d(n) Effect After Hindrance Control

| Statistic | Value | Interpretation |
|-----------|-------|----------------|
| g (d(n) coeff) | -0.58 | Negative (expected direction) |
| SE(g) | 0.35 | Large uncertainty |
| 95% CI | [-1.30, 0.14] | Includes zero |
| p-value | 0.108 | Not significant at α = 0.05 |
| t-statistic | -1.66 | Suggestive but inconclusive |

### Verdict: **INCONCLUSIVE**

The d(n) effect:
- Is in the expected direction (negative: frustrated nuclei decay faster)
- Is small compared to G-N baseline (explains ~9% of residual variance)
- Is not statistically significant (p > 0.05)
- Would require ~60+ nuclides to detect at 80% power (estimated)

---

## Robustness Check: Leave-One-Out

| Nuclide Removed | g (d(n)) | p-value | Change |
|-----------------|----------|---------|--------|
| None (full) | -0.58 | 0.108 | — |
| ²⁵²Cf | -0.46 | 0.17 | Less negative |
| ²⁰⁹Po | -0.52 | 0.14 | Slightly less negative |
| ²³²Th | -0.61 | 0.09 | More negative |

**Interpretation**: Result is moderately robust; no single nuclide dominates the signal.

---

## Conclusion

**H-V7.2-01 (Hindrance-corrected d(n) effect)**: INCONCLUSIVE
- Effect direction is consistent with theory
- Statistical significance not achieved
- Sample size is limiting factor

**H-V7.2-02 (Hindrance dominates over d(n))**: NOT SUPPORTED
- Hindrance class shows no significant effect in this dataset
- This may be due to lack of H2 nuclides and small H1 sample

**H-V7.2-03 (Non-linear d(n) effect)**: REJECTED
- Quadratic term not significant (p = 0.45)

