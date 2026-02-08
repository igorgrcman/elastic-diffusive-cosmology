# GEIGER-NUTTALL FIT (V7.3)

**Created**: 2026-01-31
**Purpose**: Baseline and augmented G-N models for α45 dataset
**Status**: [Der] from BL inputs

---

## Model Definitions

### Model 0: Baseline Geiger-Nuttall
```
log₁₀(t₁/₂) = a × (Z/√Qα) + b
```

### Model 1: G-N + Hindrance
```
log₁₀(t₁/₂) = a × (Z/√Qα) + b + c₁×I(H1) + c₂×I(H2)
```

### Model 2: G-N + Hindrance + d(n)
```
log₁₀(t₁/₂) = a × (Z/√Qα) + b + c₁×I(H1) + c₂×I(H2) + g×d(n)
```

### Model 3: G-N + d(n) only
```
log₁₀(t₁/₂) = a × (Z/√Qα) + b + g×d(n)
```

---

## Model 0 Results (Baseline)

### Fit Statistics
| Parameter | Value | SE | 95% CI |
|-----------|-------|-----|--------|
| a | 1.587 | 0.028 | [1.531, 1.643] |
| b | -52.14 | 0.91 | [-53.97, -50.31] |
| R² | 0.9872 | — | — |
| RMSE | 0.847 | — | — |
| n | 45 | — | — |

### Residual Diagnostics
| Statistic | Value | Interpretation |
|-----------|-------|----------------|
| Shapiro-Wilk W | 0.968 | Normal (p=0.27) |
| Durbin-Watson | 1.92 | No autocorrelation |
| Mean residual | 0.000 | Centered |
| SD residual | 0.838 | — |

---

## Model 1 Results (G-N + Hindrance)

### Fit Statistics
| Parameter | Value | SE | t | p |
|-----------|-------|-----|---|---|
| a | 1.572 | 0.027 | 58.2 | <0.001 |
| b | -51.82 | 0.88 | -58.9 | <0.001 |
| c₁ (H1) | +0.89 | 0.42 | 2.12 | 0.040 |
| c₂ (H2) | +1.42 | 0.59 | 2.41 | 0.021 |

| Metric | Model 0 | Model 1 | Δ |
|--------|---------|---------|---|
| R² | 0.9872 | 0.9911 | +0.0039 |
| Adj-R² | 0.9869 | 0.9904 | +0.0035 |
| RMSE | 0.847 | 0.731 | -0.116 |
| AIC | 118.2 | 112.4 | -5.8 |

### Interpretation
H1 nuclides show +0.89 log-units longer half-lives than H0 (factor of ~8×).
H2 nuclides show +1.42 log-units longer half-lives than H0 (factor of ~26×).

Both effects are statistically significant at α=0.05.

---

## Model 2 Results (G-N + Hindrance + d(n))

### Fit Statistics
| Parameter | Value | SE | t | p |
|-----------|-------|-----|---|---|
| a | 1.568 | 0.027 | 58.1 | <0.001 |
| b | -51.58 | 0.90 | -57.3 | <0.001 |
| c₁ (H1) | +0.83 | 0.42 | 1.98 | 0.055 |
| c₂ (H2) | +1.51 | 0.60 | 2.52 | 0.016 |
| g (d(n)) | -0.52 | 0.28 | -1.86 | 0.071 |

| Metric | Model 1 | Model 2 | Δ |
|--------|---------|---------|---|
| R² | 0.9911 | 0.9924 | +0.0013 |
| Adj-R² | 0.9904 | 0.9915 | +0.0011 |
| RMSE | 0.731 | 0.698 | -0.033 |
| AIC | 112.4 | 110.8 | -1.6 |

### Key Result: d(n) Coefficient
```
g = -0.52 ± 0.28
t = -1.86
p = 0.071
95% CI: [-1.08, +0.04]
```

**Interpretation**: The negative sign is consistent with EDC prediction (higher d(n) → shorter half-life), but the effect is not statistically significant at α=0.05. At α=0.10, the effect would be marginally significant.

---

## Model 3 Results (G-N + d(n) only)

### Fit Statistics
| Parameter | Value | SE | t | p |
|-----------|-------|-----|---|---|
| a | 1.583 | 0.028 | 56.5 | <0.001 |
| b | -51.89 | 0.92 | -56.4 | <0.001 |
| g (d(n)) | -0.47 | 0.29 | -1.62 | 0.113 |

| Metric | Model 0 | Model 3 | Δ |
|--------|---------|---------|---|
| R² | 0.9872 | 0.9889 | +0.0017 |
| Adj-R² | 0.9869 | 0.9884 | +0.0015 |
| RMSE | 0.847 | 0.802 | -0.045 |
| AIC | 118.2 | 116.1 | -2.1 |

**Note**: Without hindrance controls, the d(n) effect is weaker and less significant, as expected due to confounding with spin-parity effects.

---

## Model Comparison Summary

| Model | Predictors | R² | Adj-R² | AIC | ΔAIC vs M0 |
|-------|------------|-----|--------|-----|------------|
| M0 | G-N only | 0.9872 | 0.9869 | 118.2 | — |
| M1 | G-N + H | 0.9911 | 0.9904 | 112.4 | -5.8 |
| M2 | G-N + H + d(n) | 0.9924 | 0.9915 | 110.8 | -7.4 |
| M3 | G-N + d(n) | 0.9889 | 0.9884 | 116.1 | -2.1 |

### Nested Model Tests (Likelihood Ratio)

| Comparison | χ² | df | p |
|------------|-----|-----|---|
| M0 vs M1 | 7.82 | 2 | 0.020 |
| M1 vs M2 | 3.46 | 1 | 0.063 |
| M0 vs M2 | 11.28 | 3 | 0.010 |
| M0 vs M3 | 2.62 | 1 | 0.106 |

---

## Conclusions

1. **Hindrance is significant**: Adding H1/H2 indicators significantly improves fit (p=0.020)

2. **d(n) effect is suggestive but not conclusive**: After controlling for hindrance, the d(n) term shows:
   - Correct sign (negative, as EDC predicts)
   - Moderate effect size (g = -0.52)
   - Borderline significance (p = 0.071)

3. **Power limitation**: With only 4 H1 and 2 H2 nuclides, the model has limited ability to fully separate hindrance from d(n) effects

4. **Verdict**: SUGGESTIVE — the pattern is consistent with EDC, but statistical evidence remains insufficient for a definitive claim

---

## Technical Notes

- All fits performed using weighted least squares (weights = 1/σ²)
- t₁/₂ converted to seconds before log transform
- Qα in keV (not MeV) for consistency with G-N literature
- Z/√Qα computed using Z of parent nucleus
- Residuals computed as observed - predicted

