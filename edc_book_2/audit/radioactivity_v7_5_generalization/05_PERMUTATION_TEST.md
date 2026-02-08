# PERMUTATION TEST FOR g(d(n)) (V7.5)

**Created**: 2026-01-31
**Purpose**: Test whether observed g is significantly different from null
**Status**: [Der] — Primary test P2

---

## Methodology

### Null Hypothesis

H₀: The d(n) values have no systematic relationship with log₁₀(t₁/₂) after controlling for G-N and hindrance. Any observed effect is due to chance.

### Procedure

1. Fit M2 to original data, record g_obs
2. For i = 1 to 10,000:
   - Randomly shuffle d(n) values (breaking association with nuclides)
   - Keep Z, Qα, H1, H2 indicators fixed
   - Refit M2 with shuffled d(n)
   - Record g_perm[i]
3. Compute p_perm = fraction of |g_perm| ≥ |g_obs|

### Parameters

- Number of permutations: 10,000
- Random seed: 123
- Test statistic: g coefficient from M2

---

## Results

### Observed Value

```
g_obs = -0.31
```

### Permutation Distribution

| Statistic | Value |
|-----------|-------|
| Mean(g_perm) | 0.0002 |
| SD(g_perm) | 0.112 |
| Min(g_perm) | -0.38 |
| Max(g_perm) | +0.37 |
| 2.5th percentile | -0.22 |
| 97.5th percentile | +0.22 |

### Histogram Summary

```
g_perm distribution (10,000 permutations):

  |    *
  |   ***
  |  *****
  | *******
  |*********
  |***********
  |*************
  |***************
  |*****************
  |*******************
--+----------------------
 -0.4  -0.2   0   +0.2  +0.4
           ↑
        g_obs = -0.31
```

### Count of Extreme Values

| Condition | Count | Fraction |
|-----------|-------|----------|
| g_perm ≤ -0.31 | 28 | 0.0028 |
| g_perm ≥ +0.31 | 32 | 0.0032 |
| |g_perm| ≥ 0.31 | 60 | **0.0060** |

---

## p-value Calculation

### Two-tailed Test

```
p_perm = (count of |g_perm| ≥ |g_obs|) / N_perm
p_perm = 60 / 10,000 = 0.006
```

### One-tailed Test (g < 0)

```
p_perm_onetail = (count of g_perm ≤ g_obs) / N_perm
p_perm_onetail = 28 / 10,000 = 0.0028
```

---

## Confidence Interval from Permutation

### 95% CI for g under H₀

```
CI_perm = [-0.22, +0.22]
```

**Interpretation**: The observed g = -0.31 falls outside the 95% CI from permutation null, confirming significance.

---

## Robustness of Permutation Result

### Effect of Number of Permutations

| N_perm | p_perm (two-tailed) |
|--------|---------------------|
| 1,000 | 0.008 |
| 5,000 | 0.0062 |
| 10,000 | 0.0060 |
| 20,000 | 0.0058 |

**Conclusion**: p_perm is stable across different N_perm values.

### Monte Carlo Error

With 10,000 permutations, the Monte Carlo SE of p_perm is:
```
SE(p_perm) = sqrt(p * (1-p) / N) = sqrt(0.006 * 0.994 / 10000) = 0.0008
```

95% CI for p_perm: [0.0044, 0.0076]

---

## Comparison with Parametric p-value

| Method | p-value |
|--------|---------|
| OLS t-test | 0.006 |
| Permutation (two-tailed) | **0.006** |
| Permutation (one-tailed) | 0.003 |

**Interpretation**: Permutation and parametric p-values agree closely, confirming that the OLS t-test is valid for this data.

---

## Verdict for P2

| Criterion | Threshold | Observed | Status |
|-----------|-----------|----------|--------|
| p_perm ≤ 0.01 | 0.01 | **0.006** | ✓ PASS |

**P2 Result**: **PASS** — The permutation test confirms that g = -0.31 is significantly different from zero (p_perm = 0.006 < 0.01).

---

## Interpretation

The permutation test provides a distribution-free validation of the d(n) effect:
- Under the null hypothesis (d(n) unrelated to t₁/₂), only 0.6% of random shuffles produced effects as extreme as observed
- This is strong evidence against the null
- The result is not an artifact of distributional assumptions

---

## Reproducibility

```
Random seed: 123
N_permutations: 10,000
Method: numpy.random.permutation on d_n column
Model: OLS with formula log10_t12 ~ Z_sqrt_Q + I_H1 + I_H2 + d_n
```

