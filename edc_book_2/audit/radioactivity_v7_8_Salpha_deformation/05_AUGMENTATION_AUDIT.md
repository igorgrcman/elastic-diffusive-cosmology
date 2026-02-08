# V7.8 AUGMENTATION AUDIT

**Created**: 2026-01-31
**Purpose**: Coverage scorecard and bias analysis for proxy variables

---

## Coverage Summary

| Proxy | Available | Missing | Coverage |
|-------|-----------|---------|----------|
| proxy_deform | 106 | 0 | **100%** |
| proxy_Salpha | 106 | 0 | **100%** |

**No missing data** — both proxies are derived from Z, A and require no external lookup.

---

## Proxy Statistics

### proxy_deform (Shell Distance Product)

```
Formula: |N - 126| × |Z - 82| / 1000
```

| Statistic | Value |
|-----------|-------|
| Min | 0.000 (Po-210, N=126) |
| Max | 0.558 (Fm-257) |
| Mean | 0.158 |
| Median | 0.111 |
| SD | 0.140 |

### Distribution by Element

| Element | Z | Mean proxy_deform | Range |
|---------|---|-------------------|-------|
| Bi | 83 | 0.003 | 0.002-0.003 |
| Po | 84 | 0.007 | 0.000-0.016 |
| At | 85 | 0.010 | 0.003-0.018 |
| Rn | 86 | 0.016 | 0.006-0.032 |
| Fr | 87 | 0.033 | 0.015-0.047 |
| Ra | 88 | 0.051 | 0.030-0.072 |
| Ac | 89 | 0.077 | 0.056-0.091 |
| Th | 90 | 0.107 | 0.080-0.144 |
| Pa | 91 | 0.132 | 0.108-0.148 |
| U | 92 | 0.170 | 0.130-0.220 |
| Np | 93 | 0.209 | 0.187-0.231 |
| Pu | 94 | 0.254 | 0.216-0.312 |
| Am | 95 | 0.307 | 0.286-0.328 |
| Cm | 96 | 0.378 | 0.338-0.462 |
| Bk | 97 | 0.435 | 0.405-0.465 |
| Cf | 98 | 0.493 | 0.456-0.528 |
| Es | 99 | 0.527 | 0.493-0.561 |
| Fm | 100 | 0.540 | 0.504-0.558 |

### proxy_Salpha (Royer Preformation)

```
Formula: log₁₀(P_α) = -2.52 + 0.0121×Z - 0.0087×N + 0.0023×A
```

| Statistic | Value |
|-----------|-------|
| Min | -2.168 |
| Max | -2.053 |
| Mean | -2.105 |
| Median | -2.108 |
| SD | 0.027 |

**Note**: Very narrow range (0.115 log units) due to Royer formula's linear structure.

---

## Correlation Analysis

### Correlations with Key Variables

| Variable | vs d(n) | vs proxy_deform | vs proxy_Salpha |
|----------|---------|-----------------|-----------------|
| d(n) | 1.000 | 0.971 | -0.568 |
| proxy_deform | 0.971 | 1.000 | -0.505 |
| proxy_Salpha | -0.568 | -0.505 | 1.000 |
| Z | 0.949 | 0.984 | -0.325 |
| A | 0.987 | 0.997 | -0.463 |
| Qalpha_keV | -0.352 | -0.334 | -0.247 |
| log10_t12 | 0.392 | 0.329 | -0.128 |

### Key Observation

**d(n) and proxy_deform are highly correlated (r = 0.971)**

This is expected because both scale with A:
- d(n) = distance from n(A) = 6.1 × A^(1/3) to nearest allowed
- proxy_deform = |N-126| × |Z-82| / 1000 ≈ function of A and Z

Despite high correlation, **M5 results show d(n) captures additional variance beyond proxy_deform**:
- proxy_deform becomes non-significant (p = 0.67) when d(n) is included
- d(n) remains highly significant (p = 0.001)

---

## Bias Analysis: Missingness

Since coverage is 100% for both proxies, there is **no missing data bias**.

However, the derived nature of proxies introduces potential **proxy bias**:

### Potential Biases

| Bias Type | Description | Mitigation |
|-----------|-------------|------------|
| Formula bias | Royer S_α is linear approximation | Validated against experimental data |
| Shell distance proxy | proxy_deform assumes deformation ∝ shell distance | True for actinides; may fail elsewhere |
| No odd-even variation | Proxies don't distinguish ee/eo/oe/oo | Hindrance classes partially capture this |

---

## Comparison with External Data (If Available)

### Expected vs Actual proxy_deform

If β₂ from FRDM were available, we would expect:

| Nuclide | proxy_deform | Expected β₂ | Correlation |
|---------|--------------|-------------|-------------|
| Po-210 | 0.000 | ~0.00 | ✓ |
| U-238 | 0.200 | ~0.22 | ✓ |
| Cm-248 | 0.364 | ~0.28 | ✓ |

Expected r(proxy_deform, β₂) > 0.85 [I]

---

## Summary

| Metric | Value |
|--------|-------|
| Total nuclides | 106 |
| Nuclides with proxy_deform | 106 (100%) |
| Nuclides with proxy_Salpha | 106 (100%) |
| Missing values | 0 |
| Correlation d(n) vs proxy_deform | 0.971 |
| Correlation d(n) vs proxy_Salpha | -0.568 |

**Conclusion**: Full coverage achieved with derived proxies. High d(n)-proxy_deform correlation necessitates careful interpretation, but regression results show d(n) contains independent information.

