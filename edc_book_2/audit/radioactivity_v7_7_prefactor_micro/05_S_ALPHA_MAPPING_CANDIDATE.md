# S_α MAPPING CANDIDATES (V7.7)

**Created**: 2026-01-31
**Purpose**: Propose functional forms for S_α(d)
**Status**: [P] — All forms are proposed hypotheses

---

## Current Empirical Constraint

From V7.4 M2 regression [Der]:
```
log₁₀(t₁/₂) = ... + g×d(n)
g = -0.31 ± 0.11
```

If d(n) acts entirely through S_α:
```
log₁₀(λ) = ... + log₁₀(S_α(d))
log₁₀(S_α(d)) ≈ constant + 0.31 × d(n)
```

---

## Candidate 1: Linear in Log-Space [P]

### Form

```
log₁₀(S_α) = k₀ + k₁ × d(n)
S_α(d) = S₀ × 10^(k₁ × d)
```

### Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| k₁ | 0.31 | From g (V7.4) |
| S₀ | ~10⁻³ | Typical actinide S_α [BL:SOURCE_TBD] |

### Implied S_α Values

| d(n) | S_α | Factor vs d=0 |
|------|-----|---------------|
| 0 | 10⁻³ | 1 |
| 1 | 2×10⁻³ | 2 |
| 2 | 4×10⁻³ | 4 |
| 3 | 8×10⁻³ | 8 |

### Pros/Cons

| Pro | Con |
|-----|-----|
| Simple, one parameter | Unbounded for large d |
| Matches regression directly | No saturation physics |
| Easy to interpret | May overpredict for d > 5 |

### Upgrade Requirements

- Independent S_α measurements for 10+ nuclides
- Test linearity of log₁₀(S_α) vs d(n)

---

## Candidate 2: Saturating Form [P]

### Form

```
S_α(d) = S_min + (S_max - S_min) × (1 - e^(-d/d₀))
```

### Motivation

Physical expectation: S_α cannot exceed 1 (probability bound).

### Parameters

| Parameter | Proposed Value | Physical Meaning |
|-----------|----------------|------------------|
| S_min | 10⁻⁴ | Baseline at d=0 |
| S_max | 0.3 | Saturation limit |
| d₀ | 2.0 | Scale of saturation |

### Implied S_α Values

| d(n) | S_α | Factor vs d=0 |
|------|-----|---------------|
| 0 | 10⁻⁴ | 1 |
| 1 | 0.12 | 1200 |
| 2 | 0.22 | 2200 |
| 3 | 0.27 | 2700 |
| ∞ | 0.30 | 3000 |

### Pros/Cons

| Pro | Con |
|-----|-----|
| Bounded | 3 parameters vs 1 |
| Physics: probability ≤ 1 | Saturation not observed in data range |
| Predicts plateau at high d | Harder to fit with current data |

### Upgrade Requirements

- Data with d(n) > 5 (superheavy elements)
- Model comparison: linear vs saturating AIC

---

## Candidate 3: Piecewise by Hindrance [P]

### Form

```
log₁₀(S_α) = k₀ + k_H × d(n)

where k_H depends on hindrance class:
  k_H0 = 0.34  (from T1: g in H0)
  k_H1 = 0.26  (g + interaction)
  k_H2 = 0.22  (g + interaction)
```

### Motivation

T1 shows d(n) effect varies by hindrance class. This could reflect:
- Different S_α sensitivity to frustration
- Masking by selection rules

### Implied S_α Enhancement

| Class | k | Factor per unit d |
|-------|---|-------------------|
| H0 | 0.34 | 2.2× |
| H1 | 0.26 | 1.8× |
| H2 | 0.22 | 1.7× |

### Pros/Cons

| Pro | Con |
|-----|-----|
| Matches observed interaction | More complex (3 params) |
| Class-specific physics | May be overfitting |
| Testable by class | Interaction not significant (p > 0.5) |

### Upgrade Requirements

- Larger dataset with more H1/H2
- Significant interaction term (p < 0.05)

---

## Candidate 4: Threshold Form [P]

### Form

```
S_α(d) = S₀           if d < d_crit
S_α(d) = S₀ × f(d)    if d ≥ d_crit
```

### Motivation

Maybe frustration effect only kicks in above some threshold.

### Proposed Parameters

| Parameter | Value | Meaning |
|-----------|-------|---------|
| d_crit | 1.0 | Threshold |
| S₀ | 10⁻³ | Baseline |
| f(d) | 10^(0.5×(d-1)) | Enhancement |

### Pros/Cons

| Pro | Con |
|-----|-----|
| Physical: threshold effects common | Discontinuity |
| Explains why small d shows less effect | 3 parameters |
| Testable | Current data doesn't clearly show threshold |

### Upgrade Requirements

- Residual analysis: is there break at d ≈ 1?
- Compare threshold vs linear AIC

---

## Comparison Matrix

| Candidate | Parameters | Matches Data? | Bounded? | Testable? |
|-----------|------------|---------------|----------|-----------|
| 1: Linear | 1 | Yes | No | Easy |
| 2: Saturating | 3 | Partial | Yes | Needs d>5 |
| 3: Piecewise | 3 | Yes | No | Needs more H1/H2 |
| 4: Threshold | 3 | Uncertain | No | Needs residual check |

---

## Recommended Path

**Current best**: Candidate 1 (Linear)
- Matches regression
- Simplest (Occam)
- Sufficient for d ∈ [0, 3]

**Future upgrade**: If superheavy data shows saturation, switch to Candidate 2.

---

## Falsification Tests

| Form | Test | Threshold |
|------|------|-----------|
| Linear | Residuals vs d² | r < 0.1 (no curvature) |
| Saturating | Fit with d > 5 | AIC improves |
| Piecewise | Interaction significant | p < 0.05 |
| Threshold | Break in residuals | Clear discontinuity at d_crit |

