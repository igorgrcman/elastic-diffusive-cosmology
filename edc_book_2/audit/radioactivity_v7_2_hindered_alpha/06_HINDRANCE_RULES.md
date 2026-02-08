# HINDRANCE CLASSIFICATION RULES (V7.2)

**Created**: 2026-01-31
**Purpose**: Define spin-parity hindrance classes for α-decay
**Status**: [Der] from nuclear physics selection rules

---

## Physical Background

### α-Decay Selection Rules [Der]

For α-decay from parent (Jπ_p) to daughter (Jπ_d):

1. **Angular momentum**: The α-particle carries orbital angular momentum L
   - Conservation: |J_p - J_d| ≤ L ≤ J_p + J_d
   - Minimum L determines barrier: higher L → stronger centrifugal barrier

2. **Parity**: π_p = π_d × (-1)^L
   - No parity change: L must be even (0, 2, 4, ...)
   - Parity change: L must be odd (1, 3, 5, ...)

3. **Hindrance factor**: H ∝ exp(+barrier height)
   - L = 0 is "favored" (no centrifugal barrier)
   - Higher L → exponentially slower decay

---

## Hindrance Classification Scheme

### Class H0: Favored [Der]

**Definition**: ΔJ ≤ 2 AND no parity change

**Physical meaning**:
- L = 0 or L = 2 possible
- Minimal centrifugal barrier
- "Normal" α-decay rate

**Examples**:
| Transition | Jπ(P) → Jπ(D) | ΔJ | ΔΠ | L_min |
|------------|---------------|----|----|-------|
| ²¹⁰Po → ²⁰⁶Pb | 0⁺ → 0⁺ | 0 | N | 0 |
| ²⁴⁴Cm → ²⁴⁰Pu | 0⁺ → 0⁺ | 0 | N | 0 |
| ²⁰⁹Po → ²⁰⁵Pb | 1/2⁻ → 5/2⁻ | 2 | N | 2 |

**Count in α32**: 29 nuclides

---

### Class H1: First-Forbidden Equivalent [Der]

**Definition**: ΔJ ≤ 2 AND parity change

**Physical meaning**:
- L must be odd (1, 3, ...)
- Even with L = 1, there's additional centrifugal + parity barrier
- Decay rate reduced by factor ~10-100 compared to H0

**Examples**:
| Transition | Jπ(P) → Jπ(D) | ΔJ | ΔΠ | L_min |
|------------|---------------|----|----|-------|
| ²³⁵U → ²³¹Th | 7/2⁻ → 5/2⁺ | 1 | Y | 1 |
| ²⁴¹Am → ²³⁷Np | 5/2⁻ → 5/2⁺ | 0 | Y | 1 |
| ²⁴³Am → ²³⁹Np | 5/2⁻ → 5/2⁺ | 0 | Y | 1 |

**Count in α32**: 3 nuclides

---

### Class H2: Highly Hindered [Der]

**Definition**: ΔJ > 2 OR (ΔJ = 2 AND L > 2 required)

**Physical meaning**:
- High-L barrier (L ≥ 3 or 4)
- Decay rate reduced by factor ~100-10000 compared to H0
- Rare among ground-state-to-ground-state transitions

**Examples (not in α32 but known)**:
| Transition | Jπ(P) → Jπ(D) | ΔJ | L_min | Comment |
|------------|---------------|-----|-------|---------|
| ²¹²Bi → ²⁰⁸Tl | 1⁻ → 5⁺ | 4 | 4 | V7 branchpoint |
| ²¹¹Bi → ²⁰⁷Tl | 9/2⁻ → 1/2⁺ | 4 | 4 | V7 branchpoint |

**Count in α32**: 0 nuclides (selection bias: hindered α-decays rare)

---

## Classification Decision Tree

```
START with (Jπ_parent, Jπ_daughter)

1. Compute ΔJ = |J_p - J_d|

2. Compute parity change:
   ΔΠ = (π_p ≠ π_d) ? "Y" : "N"

3. Classify:
   IF ΔJ > 2:
       → H2 (Highly Hindered)
   ELSE IF ΔΠ = "Y":
       → H1 (First-Forbidden Equivalent)
   ELSE:
       → H0 (Favored)
```

---

## Expected Effect on G-N Residuals

### Model Prediction [P]

If hindrance classification is meaningful:
- H0 nuclides: residuals near zero (baseline)
- H1 nuclides: positive residuals (slower than G-N predicts)
- H2 nuclides: large positive residuals (much slower)

### Regression Implementation

Use dummy variables with H0 as reference:
```
residual = β₁ × I(H1) + β₂ × I(H2) + ε
```

Where I(Hx) = 1 if nuclide is class Hx, 0 otherwise.

**Expected signs**:
- β₁ > 0 (H1 decays slower)
- β₂ >> β₁ > 0 (H2 decays much slower)

---

## Limitations of This Classification

1. **Ground-state bias**: Assumes decay to daughter ground state; excited states may have different Jπ

2. **Discrete classes**: Real hindrance is continuous; classes are approximations

3. **Missing structure effects**: Does not account for α-clustering, nuclear deformation, shell effects

4. **No quantitative hindrance factors**: Would require spectroscopic data for each transition

---

## Connection to d(n)

After controlling for hindrance class:
- If d(n) still shows significant effect → topological frustration is real
- If d(n) effect vanishes → apparent d(n) effect was confounded with structure

This is the key test of V7.2.

