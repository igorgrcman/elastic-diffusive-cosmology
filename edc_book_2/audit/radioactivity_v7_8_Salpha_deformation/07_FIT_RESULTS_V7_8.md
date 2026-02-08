# V7.8 FIT RESULTS

**Created**: 2026-01-31
**Purpose**: Complete regression tables for M0-M7
**Source**: `code/fit_models_v7_8.py` run on 2026-01-31

---

## Summary Table

| Model | R² | R²_adj | RMSE | AIC | BIC | k |
|-------|-----|--------|------|-----|-----|---|
| M0 | 0.9522 | 0.9517 | 1.267 | 354.9 | 360.3 | 2 |
| M1 | 0.9547 | 0.9534 | 1.233 | 353.3 | 363.9 | 4 |
| **M2** | **0.9805** | **0.9797** | **0.810** | **266.2** | 279.5 | 5 |
| M3 | 0.9785 | 0.9776 | 0.850 | 276.4 | 289.7 | 5 |
| M4 | 0.9624 | 0.9609 | 1.123 | 335.4 | 348.7 | 5 |
| M5 | 0.9805 | 0.9795 | 0.809 | 268.0 | 284.0 | 6 |
| M6 | 0.9812 | 0.9802 | 0.795 | 264.2 | 280.2 | 6 |
| **M7** | **0.9812** | **0.9801** | **0.794** | **266.0** | 284.6 | 7 |

---

## M0: GN Only

```
log₁₀(t₁/₂) = a × (Z/√Q) + b
```

| Predictor | Coef | SE | t | p | 95% CI |
|-----------|------|-----|---|---|--------|
| intercept | -44.49 | 1.10 | -40.5 | <0.001 | [-46.67, -42.31] |
| Z/√Q | 1.368 | 0.030 | 45.5 | <0.001 | [1.31, 1.43] |

R² = 0.9522, RMSE = 1.267, AIC = 354.9

---

## M1: GN + Hindrance

```
log₁₀(t₁/₂) = a × (Z/√Q) + b + c₁×I(H1) + c₂×I(H2)
```

| Predictor | Coef | SE | t | p | 95% CI |
|-----------|------|-----|---|---|--------|
| intercept | -44.50 | 1.10 | -40.5 | <0.001 | [-46.68, -42.32] |
| Z/√Q | 1.364 | 0.030 | 45.4 | <0.001 | [1.30, 1.42] |
| I(H1) | 0.684 | 0.472 | 1.4 | 0.147 | [-0.25, 1.62] |
| I(H2) | 0.774 | 0.388 | 2.0 | 0.046 | [0.01, 1.54] |

R² = 0.9547, RMSE = 1.233, AIC = 353.3

---

## M2: M1 + d(n) [REFERENCE MODEL]

```
log₁₀(t₁/₂) = a × (Z/√Q) + b + c₁×I(H1) + c₂×I(H2) + g×d(n)
```

| Predictor | Coef | SE | t | p | 95% CI |
|-----------|------|-----|---|---|--------|
| intercept | -50.77 | 0.91 | -56.1 | <0.001 | [-52.57, -48.97] |
| Z/√Q | 1.593 | 0.028 | 56.8 | <0.001 | [1.54, 1.65] |
| I(H1) | 1.121 | 0.314 | 3.6 | <0.001 | [0.50, 1.74] |
| I(H2) | 1.538 | 0.265 | 5.8 | <0.001 | [1.01, 2.06] |
| **d(n)** | **-1.643** | **0.142** | **-11.5** | **<0.001** | **[-1.93, -1.36]** |

R² = 0.9805, RMSE = 0.810, AIC = 266.2

---

## M3: M1 + proxy_deform

```
log₁₀(t₁/₂) = a × (Z/√Q) + b + c₁×I(H1) + c₂×I(H2) + δ×proxy_deform
```

| Predictor | Coef | SE | t | p | 95% CI |
|-----------|------|-----|---|---|--------|
| intercept | -49.99 | 0.92 | -54.3 | <0.001 | [-51.82, -48.17] |
| Z/√Q | 1.542 | 0.027 | 57.6 | <0.001 | [1.49, 1.59] |
| I(H1) | 1.061 | 0.329 | 3.2 | 0.001 | [0.41, 1.71] |
| I(H2) | 1.714 | 0.283 | 6.1 | <0.001 | [1.15, 2.27] |
| proxy_deform | -6.967 | 0.659 | -10.6 | <0.001 | [-8.28, -5.66] |

R² = 0.9785, RMSE = 0.850, AIC = 276.4

**Note**: proxy_deform is significant alone, but M2 (with d(n)) has better AIC.

---

## M4: M1 + proxy_Salpha

```
log₁₀(t₁/₂) = a × (Z/√Q) + b + c₁×I(H1) + c₂×I(H2) + σ×proxy_Salpha
```

| Predictor | Coef | SE | t | p | 95% CI |
|-----------|------|-----|---|---|--------|
| intercept | -92.30 | 10.53 | -8.8 | <0.001 | [-113.2, -71.4] |
| Z/√Q | 1.409 | 0.029 | 48.2 | <0.001 | [1.35, 1.47] |
| I(H1) | 0.749 | 0.432 | 1.7 | 0.083 | [-0.11, 1.61] |
| I(H2) | 1.042 | 0.360 | 2.9 | 0.004 | [0.33, 1.76] |
| proxy_Salpha | -21.91 | 4.81 | -4.6 | <0.001 | [-31.4, -12.4] |

R² = 0.9624, RMSE = 1.123, AIC = 335.4

**Note**: proxy_Salpha alone has much worse fit than d(n) (AIC = 335 vs 266).

---

## M5: M1 + d(n) + proxy_deform [KEY TEST]

```
log₁₀(t₁/₂) = a × (Z/√Q) + b + c₁×I(H1) + c₂×I(H2) + g×d(n) + δ×proxy_deform
```

| Predictor | Coef | SE | t | p | 95% CI |
|-----------|------|-----|---|---|--------|
| intercept | -50.74 | 0.91 | -55.7 | <0.001 | [-52.55, -48.93] |
| Z/√Q | 1.589 | 0.030 | 53.8 | <0.001 | [1.53, 1.65] |
| I(H1) | 1.118 | 0.315 | 3.5 | <0.001 | [0.49, 1.74] |
| I(H2) | 1.568 | 0.275 | 5.7 | <0.001 | [1.02, 2.11] |
| **d(n)** | **-1.460** | **0.455** | **-3.2** | **0.001** | **[-2.36, -0.56]** |
| proxy_deform | -0.850 | 2.009 | -0.4 | 0.672 | [-4.84, 3.14] |

R² = 0.9805, RMSE = 0.809, AIC = 268.0

**KEY FINDING**: d(n) remains significant (p = 0.001), proxy_deform becomes non-significant (p = 0.67).

---

## M6: M1 + d(n) + proxy_Salpha

```
log₁₀(t₁/₂) = a × (Z/√Q) + b + c₁×I(H1) + c₂×I(H2) + g×d(n) + σ×proxy_Salpha
```

| Predictor | Coef | SE | t | p | 95% CI |
|-----------|------|-----|---|---|--------|
| intercept | -66.20 | 7.93 | -8.3 | <0.001 | [-81.9, -50.5] |
| Z/√Q | 1.591 | 0.028 | 57.5 | <0.001 | [1.54, 1.65] |
| I(H1) | 1.111 | 0.310 | 3.6 | <0.001 | [0.50, 1.72] |
| I(H2) | 1.572 | 0.262 | 6.0 | <0.001 | [1.05, 2.09] |
| **d(n)** | **-1.525** | **0.153** | **-10.0** | **<0.001** | **[-1.83, -1.22]** |
| proxy_Salpha | -7.282 | 3.720 | -2.0 | 0.050 | [-14.7, 0.1] |

R² = 0.9812, RMSE = 0.795, AIC = 264.2

**KEY FINDING**: d(n) remains highly significant (p < 0.001), proxy_Salpha is marginally significant (p = 0.05).

---

## M7: Full Model [DEFINITIVE TEST]

```
log₁₀(t₁/₂) = a × (Z/√Q) + b + c₁×I(H1) + c₂×I(H2) + g×d(n) + δ×proxy_deform + σ×proxy_Salpha
```

| Predictor | Coef | SE | t | p | 95% CI |
|-----------|------|-----|---|---|--------|
| intercept | -67.76 | 8.78 | -7.7 | <0.001 | [-85.2, -50.4] |
| Z/√Q | 1.595 | 0.029 | 54.4 | <0.001 | [1.54, 1.65] |
| I(H1) | 1.113 | 0.311 | 3.6 | <0.001 | [0.50, 1.73] |
| I(H2) | 1.544 | 0.271 | 5.7 | <0.001 | [1.01, 2.08] |
| **d(n)** | **-1.711** | **0.467** | **-3.7** | **<0.001** | **[-2.64, -0.78]** |
| proxy_deform | 0.920 | 2.180 | 0.4 | 0.673 | [-3.40, 5.24] |
| proxy_Salpha | -8.005 | 4.109 | -1.9 | 0.051 | [-16.2, 0.2] |

R² = 0.9812, RMSE = 0.794, AIC = 266.0

---

## Primary Test Results

| Test | Criterion | Result | Status |
|------|-----------|--------|--------|
| P1 | g < 0 and p < 0.01 in M2 | g = -1.64, p < 0.001 | ✓ PASS |
| P2 | g < 0 and p < 0.05 in M5 | g = -1.46, p = 0.001 | ✓ PASS |
| P3 | g < 0 and p < 0.05 in M6 | g = -1.53, p < 0.001 | ✓ PASS |
| P4 | |Δg|/|g_M2| < 20% in M7 | Δg = -0.07, 4.2% | ✓ STABLE |

---

## Mediation Analysis

### d(n) Coefficient Across Models

| Model | g(d(n)) | SE | p | Δg vs M2 | % change |
|-------|---------|-----|---|----------|----------|
| M2 (baseline) | -1.643 | 0.142 | <0.001 | — | — |
| M5 (+deform) | -1.460 | 0.455 | 0.001 | +0.183 | +11.1% |
| M6 (+Salpha) | -1.525 | 0.153 | <0.001 | +0.118 | +7.2% |
| M7 (full) | -1.711 | 0.467 | <0.001 | -0.068 | -4.2% |

**Conclusion**: g is ROBUST to proxy inclusion.

### Proxy Significance

| Proxy | Alone (M3/M4) | With d(n) (M5/M6) | Interpretation |
|-------|---------------|-------------------|----------------|
| proxy_deform | p < 0.001 | p = 0.67 | Absorbed by d(n) |
| proxy_Salpha | p < 0.001 | p = 0.05 | Marginally independent |

---

## Model Comparison (AIC)

| Comparison | ΔAIC | Interpretation |
|------------|------|----------------|
| M2 vs M0 | -88.7 | d(n)+hindrance huge improvement |
| M2 vs M1 | -87.1 | d(n) huge improvement |
| M2 vs M3 | -10.2 | d(n) better than proxy_deform |
| M2 vs M5 | -1.8 | Adding proxy_deform doesn't help |
| M2 vs M6 | +2.0 | Adding proxy_Salpha slightly helps |
| M6 vs M7 | -1.8 | Adding proxy_deform to M6 doesn't help |

---

## Verdict

**V7.8 verdict: ROBUST**

- g remains negative: -1.711 (M7) vs -1.643 (M2)
- g remains significant: p < 0.001
- g is stable: 4.2% change when both proxies included
- proxy_deform is absorbed by d(n) (becomes non-significant)
- proxy_Salpha adds marginally (p = 0.05) but doesn't eliminate g

**d(n) captures variance beyond standard deformation and S_α proxies.**

