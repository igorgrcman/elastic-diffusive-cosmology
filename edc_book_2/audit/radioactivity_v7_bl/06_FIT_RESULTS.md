# FIT RESULTS (V7)

**Created**: 2026-01-31
**Purpose**: Test whether d(n) improves Geiger-Nuttall half-life predictions
**Status**: LIMITED — Insufficient BL data for full regression

---

## Fit Framework

### Baseline: Classic Geiger-Nuttall [BL]
```
log₁₀(t₁/₂) = a × (Z / √Q_α) + b
```

Where:
- t₁/₂ in seconds
- Z = atomic number
- Q_α in MeV

### Augmented: G-N + Frustration [P]
```
log₁₀(t₁/₂) = a × (Z / √Q_α) + b + c × d(n)
```

Where d(n) = coordination distance from n(A) model.

---

## Available BL Data for α-Emitters

| Nuclide | Z | Q_α (MeV) | t₁/₂ | log₁₀(t₁/₂/s) | d(n) [P] |
|---------|---|-----------|------|---------------|----------|
| ²³⁸U | 92 | 4.270 | 4.468×10⁹ y | 17.15 | 1.81 |
| ²³²Th | 90 | 4.082 | 1.40×10¹⁰ y | 17.65 | 1.48 |
| ²³⁵U | 92 | 4.678 | 7.04×10⁸ y | 16.35 | 1.65 |
| ²¹²Bi(α) | 83 | 6.207 | 60.55 min (×0.36) | 3.12* | 0.39 |
| ²¹¹Bi(α) | 83 | 6.750 | 2.14 min (×0.997) | 2.11 | 0.32 |
| ²¹²Po | 84 | 8.954 | 294.3 ns | -6.53 | 0.39 |

*Note: For branch points, effective t₁/₂(α) = t₁/₂(total) / BR(α)

---

## Baseline Fit: G-N Only

With only 6 data points, formal regression is unreliable. Qualitative observations:

### Z/√Q vs log₁₀(t₁/₂) Pattern

| Nuclide | Z/√Q | log₁₀(t₁/₂/s) |
|---------|------|---------------|
| ²¹²Po | 28.1 | -6.53 |
| ²¹¹Bi | 32.0 | 2.11 |
| ²¹²Bi | 33.3 | 3.12 |
| ²³⁵U | 42.5 | 16.35 |
| ²³⁸U | 44.5 | 17.15 |
| ²³²Th | 44.5 | 17.65 |

**Observation**: Clear positive correlation between Z/√Q and log₁₀(t₁/₂).
This is the expected Geiger-Nuttall relationship.

---

## Augmented Fit: G-N + d(n)

### Question: Does d(n) explain residuals from G-N?

**Method**: Calculate G-N prediction, compare to observed, check if d(n) correlates with residual.

**Problem**: We have only 3 heavy actinides with similar d(n) ≈ 1.5-1.8, so no dynamic range.

### Qualitative Assessment

| Nuclide | d(n) | G-N Residual | Pattern? |
|---------|------|--------------|----------|
| ²³⁸U | 1.81 | — | Reference |
| ²³²Th | 1.48 | +0.50 | Lower d, longer t₁/₂ |
| ²³⁵U | 1.65 | -0.80 | Middle d, shorter t₁/₂ |

**Observation**: No clear correlation. Th-232 has LOWER d(n) but LONGER t₁/₂.

This is OPPOSITE to H-N48-01 expectation (lower d should mean less frustration, hence shorter t₁/₂).

---

## Status: BLOCKED — Insufficient Data

### Why Full Fit Cannot Be Done

1. **Too few data points**: Only 6 α-emitters with complete BL data
2. **No dynamic range in d(n)**: Heavy actinides all have d ≈ 1.5-2.0
3. **Branch point complications**: For ²¹²Bi and ²¹¹Bi, effective α half-life requires BR correction

### Required for Proper Fit

To test d(n) correlation with half-life deviations:
- Need 15-20 α-emitters across d(n) range [0.2, 2.0]
- Need Q_α with < 1% uncertainty
- Need t₁/₂ with < 10% uncertainty
- Need to control for Z (or use Z-corrected residuals)

---

## Fit Results Summary

| Model | Data Points | R² | Status |
|-------|-------------|-----|--------|
| Baseline G-N | 6 | ~0.95 (est.) | Works as expected |
| Augmented +d(n) | 6 | Not computed | Insufficient data |

---

## Conclusion

**The augmented G-N + d(n) model cannot be tested with current BL data.**

The V7 BL collection focused on branchpoints, not on building a half-life correlation dataset.

### Recommendation

Create a dedicated α-emitter half-life dataset (15+ nuclides) with:
- Wide range in A (and hence d(n))
- Precise Q_α from AME2020
- Precise t₁/₂ from NUBASE2020
- Exclude branchpoint complications

This would allow proper testing of whether d(n) improves G-N predictions.
