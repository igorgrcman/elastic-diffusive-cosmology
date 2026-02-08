# d(n) MAPPING CHECK (V7.1)

**Created**: 2026-01-31
**Purpose**: Compute n(A) and d(n) for α17 dataset
**Model**: n(A) = c × A^(1/3) with c = 6.1 [P]

---

## Allowed Set S_extended [Der]

```
S_extended = {2^a × 3^b : a,b ≥ 0}
           = {1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, ...}
```

For the nuclear mass range (A = 209-244), relevant targets are:
- **n = 36**: Primary target for A ~ 180-260
- **n = 48**: Secondary target for A ~ 350-500
- **n = 54**: Tertiary target for A > 500

---

## n(A) Computation

### Formula [P]
```
n(A) = 6.1 × A^(1/3)
```

### Calibration Check
- n(208) = 6.1 × 208^(1/3) = 6.1 × 5.925 = 36.14 ✓ (near n* = 36)

---

## d(n) Results for α17

| # | Nuclide | A | A^(1/3) | n(A) [P] | n* (target) | d(n) | Zone |
|---|---------|---|---------|----------|-------------|------|------|
| 1 | ²⁰⁹Po | 209 | 5.935 | 36.20 | 36 | **0.20** | Near-allowed |
| 2 | ²¹⁰Po | 210 | 5.944 | 36.26 | 36 | **0.26** | Near-allowed |
| 3 | ²¹²Po | 212 | 5.965 | 36.39 | 36 | **0.39** | Near-allowed |
| 4 | ²¹⁴Po | 214 | 5.983 | 36.50 | 36 | **0.50** | Near-allowed |
| 5 | ²¹⁶Po | 216 | 6.001 | 36.61 | 36 | **0.61** | Near-allowed |
| 6 | ²²⁰Rn | 220 | 6.037 | 36.83 | 36 | **0.83** | Near-allowed |
| 7 | ²²²Rn | 222 | 6.055 | 36.94 | 36 | **0.94** | Near-allowed |
| 8 | ²²⁶Ra | 226 | 6.091 | 37.16 | 36 | **1.16** | Forbidden |
| 9 | ²²⁸Th | 228 | 6.109 | 37.26 | 36 | **1.26** | Forbidden |
| 10 | ²³²Th | 232 | 6.145 | 37.48 | 36 | **1.48** | Forbidden |
| 11 | ²³⁴U | 234 | 6.163 | 37.59 | 36 | **1.59** | Forbidden |
| 12 | ²³⁵U | 235 | 6.172 | 37.65 | 36 | **1.65** | Forbidden |
| 13 | ²³⁸U | 238 | 6.198 | 37.81 | 36 | **1.81** | Forbidden |
| 14 | ²³⁸Pu | 238 | 6.198 | 37.81 | 36 | **1.81** | Forbidden |
| 15 | ²⁴⁰Pu | 240 | 6.214 | 37.91 | 36 | **1.91** | Forbidden |
| 16 | ²⁴⁴Cm | 244 | 6.249 | 38.12 | 36 | **2.12** | Forbidden |
| 17 | ²⁴¹Am | 241 | 6.223 | 37.96 | 36 | **1.96** | Forbidden |

---

## d(n) Range Analysis

| Statistic | Value |
|-----------|-------|
| Minimum d(n) | 0.20 (²⁰⁹Po) |
| Maximum d(n) | 2.12 (²⁴⁴Cm) |
| Range | 1.92 |
| Mean d(n) | 1.17 |
| Std dev | 0.62 |

**Coverage Assessment**: The α17 dataset spans d(n) from 0.2 to 2.1, providing reasonable dynamic range for correlation testing.

---

## Target Transition Analysis

All 17 nuclides have n* = 36 as nearest target. None are close to n = 48.

| A | n(A) | Distance to 36 | Distance to 48 | Nearest |
|---|------|----------------|----------------|---------|
| 209-238 | 36.2-37.8 | 0.2-1.8 | 10.2-11.8 | 36 |
| 240-244 | 37.9-38.1 | 1.9-2.1 | 9.9-10.1 | 36 |

**Crossover Point**: n(A) = 42 (equidistant from 36 and 48) occurs at:
```
42 = 6.1 × A^(1/3)
A^(1/3) = 6.89
A = 326
```

No nuclide in α17 is above A = 244, so all target n = 36.

---

## Zone Classification

| Zone | d(n) Range | Nuclides | Count |
|------|------------|----------|-------|
| Near-allowed | 0 - 1.0 | ²⁰⁹Po, ²¹⁰Po, ²¹²Po, ²¹⁴Po, ²¹⁶Po, ²²⁰Rn, ²²²Rn | 7 |
| Forbidden | 1.0 - 5.0 | ²²⁶Ra, ²²⁸Th, ²³²Th, ²³⁴U, ²³⁵U, ²³⁸U, ²³⁸Pu, ²⁴⁰Pu, ²⁴⁴Cm, ²⁴¹Am | 10 |

---

## Model Sensitivity Check

### Alternative c values

| Model | c | n(244) | d(244) |
|-------|---|--------|--------|
| M-A (default) | 6.1 | 38.12 | 2.12 |
| M-B (high) | 7.2 | 45.00 | 3.00 (from 48) |
| M-C (calibrated) | 6.08 | 38.00 | 2.00 |

For M-B, heavy actinides would be closer to n = 48. However, M-A remains the primary model per V7 specification.

---

## d(n) for Daughter Nuclei

For G-N analysis, we need d(n) of the parent. For completeness, here are daughter d(n) values:

| Parent | A | Daughter | A_d | n(A_d) | d(n_d) | Δd |
|--------|---|----------|-----|--------|--------|-----|
| ²⁰⁹Po | 209 | ²⁰⁵Pb | 205 | 35.97 | 0.03 | -0.17 |
| ²¹⁰Po | 210 | ²⁰⁶Pb | 206 | 36.03 | 0.03 | -0.23 |
| ²¹²Po | 212 | ²⁰⁸Pb | 208 | 36.14 | 0.14 | -0.25 |
| ²⁴⁴Cm | 244 | ²⁴⁰Pu | 240 | 37.91 | 1.91 | -0.21 |

**Observation**: All α-decays reduce d(n) — consistent with H-N48-02 (chain trajectory).

