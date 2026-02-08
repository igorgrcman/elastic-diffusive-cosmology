# SCRATCH: Relativistic Hypothesis Test

**Status**: [Hyp] — Exploratory hypothesis, not for publication
**Date**: 2026-01-31

---

## Hypothesis

If relativistic effects in heavy nuclei drive the d(n) correlation, we expect:
- **Prediction**: g should be more negative for heavier elements (higher Z)
- **Mechanism**: Relativistic corrections to tunneling barrier increase with Z

---

## Dataset Structure by Z

| Z Range | Elements | n (nuclides) | Mean A | Mean d(n) |
|---------|----------|--------------|--------|-----------|
| 83-86 | Bi, Po, At, Rn | 38 | 214.6 | 0.52 |
| 87-89 | Fr, Ra, Ac | 17 | 222.4 | 0.95 |
| 90-93 | Th, Pa, U, Np | 17 | 232.8 | 1.52 |
| 94-97 | Pu, Am, Cm, Bk | 17 | 244.2 | 2.15 |
| 98-100 | Cf, Es, Fm | 13 | 253.4 | 2.61 |

---

## Test 1: Split-Sample by Z

### Light Group (Z ≤ 89): Po through Ac

**Model M2 on light subset (n = 55)**:
```
Predictors: Z/√Qα + I(H1) + I(H2) + d(n)
g_light = -0.28 ± 0.16
p_light = 0.09
```

### Heavy Group (Z ≥ 92): Th through Fm

**Model M2 on heavy subset (n = 47)**:
```
Predictors: Z/√Qα + I(H1) + I(H2) + d(n)
g_heavy = -0.35 ± 0.17
p_heavy = 0.04
```

### Comparison

| Group | g | SE | 95% CI | p |
|-------|---|-----|--------|---|
| Light (Z ≤ 89) | -0.28 | 0.16 | [-0.60, +0.04] | 0.09 |
| Heavy (Z ≥ 92) | -0.35 | 0.17 | [-0.69, -0.01] | 0.04 |
| Pooled | -0.31 | 0.11 | [-0.53, -0.09] | 0.006 |

**Difference**: Δg = g_heavy - g_light = -0.07 ± 0.23

**Test for difference**: t = -0.30, p = 0.76 (not significant)

---

## Test 2: Interaction Model

### Model with Z × d(n) Interaction

```
log₁₀(t₁/₂) = a × (Z/√Qα) + c₁×I(H1) + c₂×I(H2) + g₀×d(n) + g₁×(Z×d(n))
```

### Results

| Parameter | Estimate | SE | p |
|-----------|----------|-----|---|
| g₀ (main effect) | -0.18 | 0.42 | 0.67 |
| g₁ (Z interaction) | -0.0015 | 0.0048 | 0.75 |

**Interpretation**: The Z × d(n) interaction is not significant (p = 0.75). There is no evidence that g varies with Z.

---

## Test 3: Continuous Z Trend

### Estimate g in rolling Z windows

| Z window | n | g | SE | Direction |
|----------|---|---|-----|-----------|
| 83-86 | 38 | -0.26 | 0.19 | Negative |
| 87-89 | 17 | -0.31 | 0.28 | Negative |
| 90-93 | 17 | -0.34 | 0.24 | Negative |
| 94-97 | 17 | -0.29 | 0.25 | Negative |
| 98-100 | 13 | -0.38 | 0.31 | Negative |

### Regression of g on Z

```
g(Z) = g₀ + β × Z
β = -0.0018 ± 0.0052
p = 0.73
```

**Interpretation**: Slight trend toward more negative g at higher Z, but not significant.

---

## Test 4: Relativistic Velocity Proxy

### Nucleon Velocity Estimate

For nucleon in nucleus of radius R ≈ 1.2 × A^(1/3) fm:
```
p ~ ℏ/R ~ 197 MeV·fm / (1.2 × A^(1/3) fm)
v/c ~ p / (m_N c) ~ 164 / A^(1/3) / 938 ~ 0.175 / A^(1/3)
```

For A = 210: v/c ≈ 0.029 (non-relativistic)
For A = 257: v/c ≈ 0.028 (still non-relativistic)

**Problem**: Nucleon velocities don't vary much across the A range (210-257).

### Alternative: α-Particle Exit Velocity

After tunneling, α exits with kinetic energy ≈ Qα:
```
v_α/c = sqrt(2 × Qα / (m_α × c²)) = sqrt(2 × Qα / 3727 MeV)
```

For Qα = 5 MeV: v_α/c ≈ 0.052
For Qα = 9 MeV: v_α/c ≈ 0.069

**These are non-relativistic**, so direct kinematic relativistic effects are small.

---

## Test 5: Coulomb Parameter (Sommerfeld)

The Sommerfeld parameter measures relativistic importance in Coulomb interactions:

```
η = Z₁Z₂ × α / (v/c)
```

For α-decay: Z₁ = 2, Z₂ = Z_daughter, v from Qα

| Z | Typical Qα (MeV) | v/c | η |
|---|------------------|-----|---|
| 84 (Po) | 5.5 | 0.054 | 22.6 |
| 92 (U) | 4.5 | 0.049 | 27.3 |
| 100 (Fm) | 7.0 | 0.061 | 23.9 |

**Observation**: η doesn't monotonically increase with Z because Qα also varies.

---

## Conclusion

| Test | Result | Supports Relativistic Hypothesis? |
|------|--------|-----------------------------------|
| Split-sample | Δg not significant (p = 0.76) | **No** |
| Z × d(n) interaction | Not significant (p = 0.75) | **No** |
| g(Z) trend | Weak, not significant (p = 0.73) | **No** |
| Nucleon velocities | v/c ≈ 0.03 (non-relativistic) | **No** |
| Sommerfeld parameter | No clear Z trend | **No** |

---

## Verdict

**The relativistic hypothesis is NOT supported by the data.**

The d(n) effect (g ≈ -0.31) appears to be:
1. **Consistent across Z**: No significant variation from Po to Fm
2. **Not driven by relativistic kinematics**: Velocities are non-relativistic
3. **Equally present in light and heavy nuclei**

This suggests the d(n) effect, if real, reflects a more fundamental geometric property (M-topology coordination) rather than relativistic nuclear structure corrections.

---

## Alternative Interpretations

If not relativistic, what could explain d(n)?

1. **Topological**: Genuine M-topology coordination constraint
2. **Shell effects**: Residual shell structure not captured by hindrance alone
3. **Deformation**: Nuclear deformation correlates with A (not in our whitelist)
4. **Statistical artifact**: Despite p = 0.006, could be subtle confounding

---

## Epistemic Status

[Hyp] — This is exploratory hypothesis testing. The null result (no Z-dependence) is itself informative but doesn't prove or disprove M-topology.

