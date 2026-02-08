# n(A) AND d(n) TABLES (V7)

**Created**: 2026-01-31
**Purpose**: Coordination mapping and distance to allowed set
**Status**: Model variants M-A, M-B, M-C per V7.1

---

## Model Definitions

### Allowed Set S_extended [Der]
```
S = {2^a × 3^b : a,b ≥ 0}
S_extended = {1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, ...}
```

### Model Variants [P]

| Model | Formula | c value | Rationale |
|-------|---------|---------|-----------|
| M-A | n(A) = 6.1 × A^(1/3) | 6.1 | V6 default; n(208)≈36 |
| M-B | n(A) = 7.2 × A^(1/3) | 7.2 | Alternative; higher coordination |
| M-C | n(A) = c_fit × A^(1/3) | 6.08 | Calibrated: n(208) = 36.00 exactly |

**M-C Calibration**: c_fit = 36 / 208^(1/3) = 36 / 5.925 = 6.076 ≈ 6.08 [Cal]

---

## Distance Function [Der]

```
d(n) = min_{m ∈ S} |n - m|
```

For nuclear range, primary targets are m ∈ {36, 48, 54}.

---

## U-238 Chain: n(A) and d(n)

### Model M-A (c = 6.1) [P]

| Nuclide | A | A^(1/3) | n(A) | Nearest m | d(n) | Zone |
|---------|---|---------|------|-----------|------|------|
| ²³⁸U | 238 | 6.198 | 37.81 | 36 | 1.81 | Forbidden |
| ²³⁴Th | 234 | 6.163 | 37.59 | 36 | 1.59 | Forbidden |
| ²³⁴Pa | 234 | 6.163 | 37.59 | 36 | 1.59 | Forbidden |
| ²³⁴U | 234 | 6.163 | 37.59 | 36 | 1.59 | Forbidden |
| ²³⁰Th | 230 | 6.127 | 37.37 | 36 | 1.37 | Forbidden |
| ²²⁶Ra | 226 | 6.091 | 37.16 | 36 | 1.16 | Forbidden |
| ²²²Rn | 222 | 6.055 | 36.94 | 36 | 0.94 | Near-allowed |
| ²¹⁸Po | 218 | 6.019 | 36.72 | 36 | 0.72 | Near-allowed |
| ²¹⁴Pb | 214 | 5.983 | 36.50 | 36 | 0.50 | Near-allowed |
| ²¹⁴Bi | 214 | 5.983 | 36.50 | 36 | 0.50 | Near-allowed |
| ²¹⁴Po | 214 | 5.983 | 36.50 | 36 | 0.50 | Near-allowed |
| ²¹⁰Pb | 210 | 5.944 | 36.26 | 36 | 0.26 | Near-allowed |
| ²¹⁰Bi | 210 | 5.944 | 36.26 | 36 | 0.26 | Near-allowed |
| ²¹⁰Po | 210 | 5.944 | 36.26 | 36 | 0.26 | Near-allowed |
| ²⁰⁶Pb | 206 | 5.906 | 36.03 | 36 | 0.03 | **ALLOWED** |

---

## Th-232 Chain: n(A) and d(n)

### Model M-A (c = 6.1) [P]

| Nuclide | A | A^(1/3) | n(A) | Nearest m | d(n) | Zone |
|---------|---|---------|------|-----------|------|------|
| ²³²Th | 232 | 6.145 | 37.48 | 36 | 1.48 | Forbidden |
| ²²⁸Ra | 228 | 6.109 | 37.26 | 36 | 1.26 | Forbidden |
| ²²⁸Ac | 228 | 6.109 | 37.26 | 36 | 1.26 | Forbidden |
| ²²⁸Th | 228 | 6.109 | 37.26 | 36 | 1.26 | Forbidden |
| ²²⁴Ra | 224 | 6.073 | 37.05 | 36 | 1.05 | Forbidden |
| ²²⁰Rn | 220 | 6.037 | 36.83 | 36 | 0.83 | Near-allowed |
| ²¹⁶Po | 216 | 6.001 | 36.61 | 36 | 0.61 | Near-allowed |
| ²¹²Pb | 212 | 5.965 | 36.39 | 36 | 0.39 | Near-allowed |
| **²¹²Bi** | 212 | 5.965 | **36.39** | 36 | **0.39** | Near-allowed |
| ²¹²Po | 212 | 5.965 | 36.39 | 36 | 0.39 | Near-allowed |
| ²⁰⁸Tl | 208 | 5.925 | 36.14 | 36 | 0.14 | Near-allowed |
| ²⁰⁸Pb | 208 | 5.925 | 36.14 | 36 | 0.14 | **ALLOWED** |

---

## U-235 Chain: n(A) and d(n)

### Model M-A (c = 6.1) [P]

| Nuclide | A | A^(1/3) | n(A) | Nearest m | d(n) | Zone |
|---------|---|---------|------|-----------|------|------|
| ²³⁵U | 235 | 6.172 | 37.65 | 36 | 1.65 | Forbidden |
| ²³¹Th | 231 | 6.136 | 37.43 | 36 | 1.43 | Forbidden |
| ²³¹Pa | 231 | 6.136 | 37.43 | 36 | 1.43 | Forbidden |
| **²²⁷Ac** | 227 | 6.100 | **37.21** | 36 | **1.21** | Forbidden |
| ²²⁷Th | 227 | 6.100 | 37.21 | 36 | 1.21 | Forbidden |
| ²²³Fr | 223 | 6.064 | 36.99 | 36 | 0.99 | Near-allowed |
| ²²³Ra | 223 | 6.064 | 36.99 | 36 | 0.99 | Near-allowed |
| ²¹⁹Rn | 219 | 6.028 | 36.77 | 36 | 0.77 | Near-allowed |
| ²¹⁵Po | 215 | 5.992 | 36.55 | 36 | 0.55 | Near-allowed |
| ²¹¹Pb | 211 | 5.954 | 36.32 | 36 | 0.32 | Near-allowed |
| **²¹¹Bi** | 211 | 5.954 | **36.32** | 36 | **0.32** | Near-allowed |
| ²¹¹Po | 211 | 5.954 | 36.32 | 36 | 0.32 | Near-allowed |
| ²⁰⁷Tl | 207 | 5.916 | 36.09convergence | 36 | 0.09 | Near-allowed |
| ²⁰⁷Pb | 207 | 5.916 | 36.09 | 36 | 0.09 | **ALLOWED** |

---

## Branchpoint Analysis

### ²¹²Bi (Th-232)
| Channel | Daughter | A_d | n(A_d) | d(n_d) | Δd = d_d - d_p |
|---------|----------|-----|--------|--------|----------------|
| Parent | ²¹²Bi | 212 | 36.39 | 0.39 | - |
| α | ²⁰⁸Tl | 208 | 36.14 | 0.14 | **-0.25** |
| β⁻ | ²¹²Po | 212 | 36.39 | 0.39 | 0.00 |

**H-N48-01 Prediction**: α preferred (Δd < 0)
**BL Observed**: β⁻ = 64.06%, α = 35.94%
**Match**: ✗ FAILS (β⁻ dominant despite larger d)

### ²²⁷Ac (U-235)
| Channel | Daughter | A_d | n(A_d) | d(n_d) | Δd = d_d - d_p |
|---------|----------|-----|--------|--------|----------------|
| Parent | ²²⁷Ac | 227 | 37.21 | 1.21 | - |
| α | ²²³Fr | 223 | 36.99 | 0.99 | **-0.22** |
| β⁻ | ²²⁷Th | 227 | 37.21 | 1.21 | 0.00 |

**H-N48-01 Prediction**: α preferred (Δd < 0)
**BL Observed**: β⁻ = 98.62%, α = 1.38%
**Match**: ✗ FAILS STRONGLY (β⁻ dominant despite larger d)

### ²¹¹Bi (U-235)
| Channel | Daughter | A_d | n(A_d) | d(n_d) | Δd = d_d - d_p |
|---------|----------|-----|--------|--------|----------------|
| Parent | ²¹¹Bi | 211 | 36.32 | 0.32 | - |
| α | ²⁰⁷Tl | 207 | 36.09 | 0.09 | **-0.23** |
| β⁻ | ²¹¹Po | 211 | 36.32 | 0.32 | 0.00 |

**H-N48-01 Prediction**: α preferred (Δd < 0)
**BL Observed**: α = 99.724%, β⁻ = 0.276%
**Match**: ✓ SUCCESS (α dominant as predicted)

---

## Island Ladder: Target Transitions

Using Model M-A (c = 6.1):

| A Range | n(A) Range | Nearest Target | Zone |
|---------|------------|----------------|------|
| 180-220 | 34.4-36.8 | n=36 | Approaching target |
| 220-260 | 36.8-38.9 | n=36 | Forbidden (low) |
| 260-300 | 38.9-40.8 | n=36 or 48 | Deep forbidden |
| 300-380 | 40.8-44.2 | n=48 | Forbidden (high) |
| 380-500 | 44.2-48.4 | n=48 | Approaching target |
| 500-600 | 48.4-51.4 | n=48 or 54 | Transition zone |
| >600 | >51.4 | n=54 | New target |

**Crossover Points**:
- 36 ↔ 48: A ≈ 285 (n = 42, equidistant)
- 48 ↔ 54: A ≈ 530 (n = 51, equidistant)

---

## ASCII Plot: d(n) Along U-238 Chain

```
d(n)
2.0 |●
    |  ●
1.5 |    ●  ●  ●
    |          ●
1.0 |            ●
    |              ●
0.5 |                ● ●  ●  ●
    |                          ● ●  ●
0.0 |________________________________●____
    U Th Pa  U Th Ra Rn Po Pb Bi Po Pb Bi Po Pb
   238    234   230   222   214      210     206
                        Chain Step →
```

**Trend**: Monotonic decrease in d(n) toward stable Pb-206.
