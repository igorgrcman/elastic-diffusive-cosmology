# BRANCHING RULES HYPOTHESES V4

**Created**: 2026-01-31
**Purpose**: Framework for predicting decay mode selection
**Status**: All [P] unless sourced

---

## Overview

Branching occurs when multiple decay modes are energetically accessible.
EDC interpretation: Mode selection reflects topological stress relief efficiency.

---

## Observed Branching Points

| Nuclide | Chain | β⁻ % | α % | d(n) |
|---------|-------|------|-----|------|
| ²¹²Bi | Th-232 | 64 | 36 | 0.4 |
| ²¹¹Bi | U-235 | 0.3 | 99.7 | 0.3 |
| ²²⁷Ac | U-235 | 98.6 | 1.4 | 1.2 |
| ²¹⁴Bi | U-238 | ~100 | <0.1 | 0.5 |

---

## Hypothesis H1: d(n) Direction Rule [P]

**Statement**:
```
If n > n_allowed_above - d_threshold:
    β⁻ preferred (push n up toward allowed)
If n < n_allowed_below + d_threshold:
    β⁺/EC preferred (push n down)
If n far from both:
    α preferred (large Δn jump)
```

**d_threshold** ≈ 2 (qualitative)

**Consistency Check**:

| Nuclide | n(A) | Nearest | Direction | Predicted | Observed |
|---------|------|---------|-----------|-----------|----------|
| ²¹²Bi | 36.4 | 36 (below) | ↓ | β⁻ or α | 64:36 ✓ |
| ²¹¹Bi | 36.3 | 36 (below) | ↓ | α | 99.7% α ✓ |
| ²²⁷Ac | 37.2 | 36 (below) | ↓ | β⁻ | 98.6% β⁻ ✓ |

**Issue**: ²²⁷Ac and ²¹¹Bi both have n < 36, but opposite branching!

---

## Hypothesis H2: Proximity to Endpoint [P]

**Statement**:
```
Near chain endpoint (small A):
    α preferred (direct path to stable Pb)
Far from endpoint (large A):
    β preferred (N/Z adjustment before α-chain)
```

**Rationale**:
- ²¹¹Bi (A=211) is close to ²⁰⁷Pb → α direct
- ²²⁷Ac (A=227) is far from ²⁰⁷Pb → β adjusts first

**Consistency**:

| Nuclide | A | A - A_endpoint | Dominant |
|---------|---|----------------|----------|
| ²²⁷Ac | 227 | 20 | β⁻ ✓ |
| ²¹²Bi | 212 | 4 | 64% β⁻ |
| ²¹¹Bi | 211 | 4 | α ✓ |

**Partial success**: Explains ²²⁷Ac vs ²¹¹Bi but not ²¹²Bi

---

## Hypothesis H3: Q-Value Competition [P]

**Statement**:
```
Mode with higher Q-value is favored
(modulo barrier penetration for α)
```

**Rationale**:
- If Q_α >> Q_β: α wins
- If Q_β >> Q_α: β wins
- If Q_α ≈ Q_β: competitive

**Data needed**: Q_α, Q_β for branching nuclei [BL:SOURCE_TBD]

---

## Hypothesis H4: N/Z Optimization [P]

**Statement**:
```
If (N-Z)/A far from optimal ratio:
    β preferred (adjusts N/Z)
If (N-Z)/A near optimal:
    α preferred (N/Z fine, reduce A)
```

**Optimal N/Z** ≈ (A - 2Z)/(2Z) for heavy nuclei

**Consistency**: Requires N/Z calculation [Open]

---

## Hypothesis H5: Mechanism Competition [P]

**Statement**:
```
M1 (domain mixing) → β preferred
M3 (α-cluster) → α preferred
M6 (core-mantle) → α preferred

Branching = mechanism competition
```

**Application**:

| Nuclide | Dominant Mechanism | Predicted | Observed |
|---------|-------------------|-----------|----------|
| ²²⁷Ac | M1 (d=1.2 small) | β | 98.6% β ✓ |
| ²¹¹Bi | M3 (α ready) | α | 99.7% α ✓ |
| ²¹²Bi | M1/M3 competitive | 50:50 | 64:36 ✓ |

**Best fit so far**

---

## Combined Branching Model [P]

**Proposed formula** (qualitative):
```
P(α) / P(β) = f(d(n)) × g(Q_α/Q_β) × h(A - A_end) × m(mechanism)
```

Where:
- f(d): larger d → more α
- g(Q): larger Q_α → more α
- h(ΔA): smaller ΔA → more α (near endpoint)
- m: M3 active → more α; M1 active → more β

---

## Falsification Tests

### Test B1: d(n) Correlation

**Method**: Plot branching ratio vs d(n) for all known branching nuclei
**Prediction**: Positive correlation (larger d → more α)
**Falsification**: No correlation or negative

### Test B2: Q-Value Correlation

**Method**: Get Q_α, Q_β for branching nuclei
**Prediction**: Higher Q → higher probability
**Falsification**: No Q correlation

### Test B3: Position in Chain

**Method**: Compare branching at different chain positions
**Prediction**: More α near endpoint
**Falsification**: More β near endpoint

### Test B4: Mechanism Signature

**Method**: Look for domain/cluster signatures in branching nuclei
**Prediction**: Cluster pre-formation → α; Domain structure → β
**Falsification**: No structural correlation

---

## Data Gaps

| Nuclide | Missing | Priority |
|---------|---------|----------|
| ²¹²Bi | Q_α, Q_β | HIGH |
| ²¹¹Bi | Q_α, Q_β | HIGH |
| ²²⁷Ac | Q_α, Q_β | HIGH |
| All | n(A) verification | HIGH |

---

## Summary: Best Current Hypothesis

**H5 (Mechanism Competition)** provides best fit:
- M1-dominant → β
- M3-dominant → α
- Competitive → branching ratio reflects mechanism balance

Combined with **H2 (Proximity to Endpoint)**:
- Near endpoint: M3 (α-cluster) more ready → α
- Far from endpoint: M1 (domain) handles stress → β

**Status**: [P] — qualitative framework, needs Q-value data for quantitative test
