# DECAY CHAIN Th-232 V5 (Thorium Series)

**Created**: 2026-01-31
**Purpose**: EDC-annotated decay chain to Pb-208
**Data Status**: All nuclear data [BL:SOURCE_TBD]

---

## Chain Overview

```
²³²Th → ²²⁸Ra → ²²⁸Ac → ²²⁸Th → ²²⁴Ra → ²²⁰Rn →
²¹⁶Po → ²¹²Pb → ²¹²Bi → ²¹²Po/²⁰⁸Tl → ²⁰⁸Pb
```

---

## EDC Step Annotations

### DC-TH232-001: ²³²Th → ²²⁸Ra (α)
- **n(232)**: 6.1 × 232^(1/3) ≈ 37.5 [P]
- **d(n)**: d(36)=1.5, d(48)=10.5 → toward 36
- **Mechanism**: M1 (domain mixing)
- **Prediction**: α-decay favored [P]
- **Branching**: α only
- **Notes**: Primordial nuclide, t₁/₂ ~ 14 Gyr

### DC-TH232-002: ²²⁸Ra → ²²⁸Ac (β⁻)
- **n(228)**: 6.1 × 228^(1/3) ≈ 37.3 [P]
- **d(n)**: d(36)=1.3 → toward 36
- **Mechanism**: M2 (defect-mediated)
- **Prediction**: β⁻ [P]
- **Branching**: β⁻ only
- **Notes**: t₁/₂ ~ 5.75 yr

### DC-TH232-003: ²²⁸Ac → ²²⁸Th (β⁻)
- **n(228)**: 37.3 [P]
- **d(n)**: toward 36
- **Mechanism**: M2
- **Prediction**: β⁻ [P]
- **Branching**: β⁻ only
- **Notes**: t₁/₂ ~ 6.15 hr

### DC-TH232-004: ²²⁸Th → ²²⁴Ra (α)
- **n(228)**: 37.3 [P]
- **d(n)**: toward 36
- **Mechanism**: M3 (α-clusterization)
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: t₁/₂ ~ 1.91 yr

### DC-TH232-005: ²²⁴Ra → ²²⁰Rn (α)
- **n(224)**: 6.1 × 224^(1/3) ≈ 37.1 [P]
- **d(n)**: d(36)=1.1 → toward 36
- **Mechanism**: M3
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: t₁/₂ ~ 3.63 days

### DC-TH232-006: ²²⁰Rn → ²¹⁶Po (α)
- **n(220)**: 6.1 × 220^(1/3) ≈ 36.8 [P]
- **d(n)**: d(36)=0.8 → near 36
- **Mechanism**: M3
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: t₁/₂ ~ 55.6 s, thoron gas

### DC-TH232-007: ²¹⁶Po → ²¹²Pb (α)
- **n(216)**: 6.1 × 216^(1/3) ≈ 36.6 [P]
- **d(n)**: d(36)=0.6 → near 36
- **Mechanism**: M3
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: t₁/₂ ~ 0.15 s

### DC-TH232-008: ²¹²Pb → ²¹²Bi (β⁻)
- **n(212)**: 6.1 × 212^(1/3) ≈ 36.4 [P]
- **d(n)**: d(36)=0.4 → at 36
- **Mechanism**: M2
- **Prediction**: β⁻ [P]
- **Branching**: β⁻ only
- **Notes**: t₁/₂ ~ 10.6 hr

### DC-TH232-009: ²¹²Bi (BRANCH POINT)
- **n(212)**: 36.4 [P]
- **d(n)**: at 36
- **Mechanism**: M2/M3 competition
- **Prediction**: Mixed β⁻/α [P]
- **Branching**: β⁻ ~64%, α ~36%
- **Notes**: **KEY BRANCHING TEST** (H1)

#### Branch A: ²¹²Bi → ²¹²Po (β⁻)
- **Mechanism**: M2
- **Notes**: Leads to fast α

#### Branch B: ²¹²Bi → ²⁰⁸Tl (α)
- **Mechanism**: M3
- **Notes**: Leads to β⁻

### DC-TH232-010A: ²¹²Po → ²⁰⁸Pb (α)
- **n(212)**: 36.4 [P]
- **Mechanism**: M3
- **Branching**: α only
- **Notes**: t₁/₂ ~ 0.3 μs (very fast)

### DC-TH232-010B: ²⁰⁸Tl → ²⁰⁸Pb (β⁻)
- **n(208)**: 6.1 × 208^(1/3) ≈ 36.1 [P]
- **Mechanism**: M2
- **Branching**: β⁻ only
- **Notes**: t₁/₂ ~ 3.05 min

### DC-TH232-011: ²⁰⁸Pb (STABLE)
- **n(208)**: 6.1 × 208^(1/3) ≈ 36.1 [P]
- **d(n)**: d(36)=0.1 → ESSENTIALLY ALLOWED
- **Mechanism**: None (doubly magic)
- **Notes**: End of chain, Z=82, N=126

---

## Chain Statistics

| Metric | Value |
|--------|-------|
| Total steps | 10-11 (branch-dependent) |
| α-decays | 6-7 |
| β⁻-decays | 4 |
| Branch points | 1 (²¹²Bi) |
| n(start) | ~37.5 (forbidden) |
| n(end) | ~36.1 (allowed) |

---

## Branching Test H1

The ²¹²Bi branch point provides a key test:

**EDC Prediction** [P]:
- β⁻ channel: Maintains n, reduces Z-asymmetry
- α channel: Reduces n by ~4, forms cluster

**Observed**: β⁻ 64%, α 36%

**Interpretation**:
- M2 (defect-mediated β⁻) slightly favored
- M3 (α-cluster) significant minority
- Competition reflects comparable ε_f for both paths

---

## EDC Interpretation

The Th-232 chain demonstrates:
1. **Initial state**: n ≈ 37.5, in forbidden zone
2. **Final state**: n ≈ 36.1, at doubly-magic Pb-208
3. **Trend**: d(n) decreases toward 36
4. **Branching**: ²¹²Bi tests M2/M3 competition
5. **Magic number alignment**: N=126, Z=82 at endpoint
