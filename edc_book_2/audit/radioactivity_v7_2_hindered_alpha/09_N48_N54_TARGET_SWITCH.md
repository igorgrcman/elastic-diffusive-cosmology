# N=48 / N=54 TARGET SWITCHING ANALYSIS (V7.2)

**Created**: 2026-01-31
**Purpose**: Analyze target transitions in the allowed coordination set
**Status**: [P] — Geometric analysis, no BL data in transition region

---

## Target Transition Framework

### Allowed Set S_extended [Der]

```
S_extended = {2^a × 3^b : a,b ≥ 0}
```

Relevant targets for heavy nuclei:
- n = 36 = 2² × 3² (primary target for A ~ 180-260)
- n = 48 = 2⁴ × 3¹ (secondary target for A ~ 350-500)
- n = 54 = 2¹ × 3³ (tertiary target for A > 550)

### Target Distance Function

For a given n(A), the target is the nearest member of S:
```
target(n) = argmin_{m ∈ S} |n - m|
```

---

## Crossover Points [Der]

### 36 ↔ 48 Transition

**Equidistant point**: n = (36 + 48) / 2 = 42

**Corresponding A**:
```
n(A) = 6.1 × A^(1/3) = 42
A^(1/3) = 42 / 6.1 = 6.885
A = 6.885³ = **326**
```

**Interpretation**: For A > 326, nuclei are closer to n = 48 than to n = 36.

### 48 ↔ 54 Transition

**Equidistant point**: n = (48 + 54) / 2 = 51

**Corresponding A**:
```
n(A) = 6.1 × A^(1/3) = 51
A^(1/3) = 51 / 6.1 = 8.361
A = 8.361³ = **585**
```

**Interpretation**: For A > 585, nuclei are closer to n = 54 than to n = 48.

---

## α32 Dataset Position

### All nuclides in α32

| Nuclide | A | n(A) | d(36) | d(48) | Target |
|---------|---|------|-------|-------|--------|
| ²⁰⁹Po | 209 | 36.20 | 0.20 | 11.80 | **36** |
| ²¹⁰Po | 210 | 36.26 | 0.26 | 11.74 | **36** |
| ... | ... | ... | ... | ... | **36** |
| ²⁵²Cf | 252 | 38.56 | 2.56 | 9.44 | **36** |

**Maximum A in dataset**: 252 (Cf-252)
**Maximum n(A) in dataset**: 38.56

**Conclusion**: All 32 nuclides in α32 have n* = 36 as their target. None approach the 36↔48 crossover at A = 326.

---

## Superheavy Element Region [P]

### Predicted Target Assignments

| A Range | n(A) Range | Primary Target | Zone |
|---------|------------|----------------|------|
| 250-280 | 38.5-40.0 | 36 | Forbidden (far from 36) |
| 280-326 | 40.0-42.0 | 36 (barely) | Deep forbidden |
| **326** | 42.0 | **Crossover** | Equidistant 36/48 |
| 326-400 | 42.0-45.0 | 48 | Approaching 48 |
| 400-500 | 45.0-48.5 | 48 | Near 48 target |
| 500-585 | 48.5-51.0 | 48 (barely) | Between 48 and 54 |
| **585** | 51.0 | **Crossover** | Equidistant 48/54 |
| >585 | >51.0 | 54 | Approaching 54 |

### Known Superheavy Elements

| Element | Z | A (longest-lived) | n(A) | Target |
|---------|---|-------------------|------|--------|
| Og (Oganesson) | 118 | 294 | 40.6 | 36 (marginally) |
| Fl (Flerovium) | 114 | 289 | 40.3 | 36 |
| Lv (Livermorium) | 116 | 293 | 40.5 | 36 |
| Ts (Tennessine) | 117 | 294 | 40.6 | 36 |

**Observation**: Even the heaviest known elements (A ≈ 294) are still below the 36↔48 crossover.

---

## "Island of Stability" Predictions [P]

### Traditional Shell Model Prediction

Nuclear shell model predicts enhanced stability near:
- Z = 114, N = 184 → A = 298
- Z = 120, N = 184 → A = 304
- Z = 126, N = 184 → A = 310

### M-Topology Prediction

If the coordination law is relevant:
- A ≈ 326: Crossover point (maximum frustration)
- A ≈ 350-400: Approaching n = 48 (reduced frustration)
- A ≈ 488: n(A) = 48.0 exactly (minimum frustration at secondary target)

**Comparison**:
| Model | Predicted Stability Peak |
|-------|-------------------------|
| Shell model | A ≈ 298-310 |
| M-topology | A ≈ 488 |

These predictions are **incompatible**. The M-topology peak is ~150 mass units higher than shell model predictions.

---

## Experimental Implications

### What Would Confirm M-Topology?

1. **Enhanced stability at A ≈ 488**: If a nucleus with A ≈ 488 (e.g., Z = 190, N = 298?) shows anomalously long t₁/₂

2. **Smooth G-N deviations**: If nuclei near A = 326 show systematically shorter t₁/₂ (maximum frustration) and nuclei near A = 488 show longer t₁/₂ (minimum frustration at n = 48)

3. **Fission barrier trends**: If fission barriers decrease near A = 326 and increase near A = 488

### What Would Falsify M-Topology?

1. **Stability peak at A ≈ 298-310**: If the shell model island is correct, M-topology's n = 48 target is irrelevant

2. **No correlation with n(A)**: If SHE half-lives follow pure shell effects with no d(n) signature

---

## Coulomb/Fission Caveat

### Important Limitation [Open]

For A > 300, spontaneous fission becomes increasingly probable:
```
t₁/₂(SF) ∝ exp(-barrier)
barrier ∝ Z²/A (Coulomb repulsion vs. surface tension)
```

As Z increases:
- Coulomb repulsion grows as Z²
- Fission barrier decreases
- SF may dominate over α-decay before n = 48 target is reached

**Implication**: The n = 48 target may be physically inaccessible if SF prevents nuclei from surviving long enough to α-decay.

---

## Summary

### Current Status

| Finding | Status |
|---------|--------|
| All α32 nuclides target n = 36 | ✓ Confirmed |
| Crossover at A = 326 | [Der] (geometric) |
| SHE targeting n = 48 | [P] (no BL data) |
| n = 48 "island" at A ≈ 488 | [P] (speculative) |
| n = 54 relevant for A > 585 | [P] (beyond any synthesis) |

### Key Uncertainty

The M-topology prediction for SHE stability (A ≈ 488) conflicts with shell model predictions (A ≈ 298-310). Future experimental data on superheavy element half-lives could discriminate between these models.

However, SF competition may render the n = 48 target experimentally inaccessible.

