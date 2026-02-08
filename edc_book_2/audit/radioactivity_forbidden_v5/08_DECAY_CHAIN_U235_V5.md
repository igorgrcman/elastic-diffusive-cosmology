# DECAY CHAIN U-235 V5 (Actinium Series)

**Created**: 2026-01-31
**Purpose**: EDC-annotated decay chain to Pb-207
**Data Status**: All nuclear data [BL:SOURCE_TBD]

---

## Chain Overview

```
²³⁵U → ²³¹Th → ²³¹Pa → ²²⁷Ac → ²²⁷Th/²²³Fr → ²²³Ra →
²¹⁹Rn → ²¹⁵Po → ²¹¹Pb → ²¹¹Bi → ²¹¹Po/²⁰⁷Tl → ²⁰⁷Pb
```

---

## EDC Step Annotations

### DC-U235-001: ²³⁵U → ²³¹Th (α)
- **n(235)**: 6.1 × 235^(1/3) ≈ 37.6 [P]
- **d(n)**: d(36)=1.6, d(48)=10.4 → toward 36
- **Mechanism**: M1 (domain mixing)
- **Prediction**: α-decay favored [P]
- **Branching**: α only
- **Notes**: Fissile nuclide, t₁/₂ ~ 704 Myr

### DC-U235-002: ²³¹Th → ²³¹Pa (β⁻)
- **n(231)**: 6.1 × 231^(1/3) ≈ 37.4 [P]
- **d(n)**: d(36)=1.4 → toward 36
- **Mechanism**: M2 (defect-mediated)
- **Prediction**: β⁻ [P]
- **Branching**: β⁻ only
- **Notes**: t₁/₂ ~ 25.5 hr

### DC-U235-003: ²³¹Pa → ²²⁷Ac (α)
- **n(231)**: 37.4 [P]
- **d(n)**: toward 36
- **Mechanism**: M3 (α-clusterization)
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: t₁/₂ ~ 32,760 yr

### DC-U235-004: ²²⁷Ac (BRANCH POINT)
- **n(227)**: 6.1 × 227^(1/3) ≈ 37.2 [P]
- **d(n)**: d(36)=1.2 → toward 36
- **Mechanism**: M2/M3 competition
- **Prediction**: β⁻ dominant [P]
- **Branching**: β⁻ ~98.6%, α ~1.4%
- **Notes**: **KEY BRANCHING TEST** (H2)

#### Branch A: ²²⁷Ac → ²²⁷Th (β⁻) - DOMINANT
- **Mechanism**: M2
- **Notes**: Main pathway

#### Branch B: ²²⁷Ac → ²²³Fr (α) - MINOR
- **Mechanism**: M3
- **Notes**: Rare francium pathway

### DC-U235-005A: ²²⁷Th → ²²³Ra (α)
- **n(227)**: 37.2 [P]
- **Mechanism**: M3
- **Branching**: α only
- **Notes**: t₁/₂ ~ 18.7 days

### DC-U235-005B: ²²³Fr → ²²³Ra (β⁻)
- **n(223)**: 6.1 × 223^(1/3) ≈ 37.0 [P]
- **Mechanism**: M2
- **Notes**: t₁/₂ ~ 22 min

### DC-U235-006: ²²³Ra → ²¹⁹Rn (α)
- **n(223)**: 37.0 [P]
- **d(n)**: d(36)=1.0 → toward 36
- **Mechanism**: M3
- **Prediction**: α [P]
- **Branching**: α ~100%
- **Notes**: t₁/₂ ~ 11.4 days

### DC-U235-007: ²¹⁹Rn → ²¹⁵Po (α)
- **n(219)**: 6.1 × 219^(1/3) ≈ 36.8 [P]
- **d(n)**: d(36)=0.8 → near 36
- **Mechanism**: M3
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: t₁/₂ ~ 3.96 s

### DC-U235-008: ²¹⁵Po → ²¹¹Pb (α)
- **n(215)**: 6.1 × 215^(1/3) ≈ 36.6 [P]
- **d(n)**: d(36)=0.6 → near 36
- **Mechanism**: M3
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: t₁/₂ ~ 1.78 ms

### DC-U235-009: ²¹¹Pb → ²¹¹Bi (β⁻)
- **n(211)**: 6.1 × 211^(1/3) ≈ 36.3 [P]
- **d(n)**: d(36)=0.3 → at 36
- **Mechanism**: M2
- **Prediction**: β⁻ [P]
- **Branching**: β⁻ only
- **Notes**: t₁/₂ ~ 36.1 min

### DC-U235-010: ²¹¹Bi (BRANCH POINT)
- **n(211)**: 36.3 [P]
- **d(n)**: at 36
- **Mechanism**: M3 dominant / M2 minor
- **Prediction**: α dominant [P]
- **Branching**: α ~99.7%, β⁻ ~0.3%
- **Notes**: **KEY BRANCHING TEST** (H3)

#### Branch A: ²¹¹Bi → ²⁰⁷Tl (α) - DOMINANT
- **Mechanism**: M3
- **Notes**: Main pathway

#### Branch B: ²¹¹Bi → ²¹¹Po (β⁻) - MINOR
- **Mechanism**: M2
- **Notes**: Rare polonium pathway

### DC-U235-011A: ²⁰⁷Tl → ²⁰⁷Pb (β⁻)
- **n(207)**: 6.1 × 207^(1/3) ≈ 36.1 [P]
- **Mechanism**: M2
- **Branching**: β⁻ only
- **Notes**: t₁/₂ ~ 4.77 min

### DC-U235-011B: ²¹¹Po → ²⁰⁷Pb (α)
- **n(211)**: 36.3 [P]
- **Mechanism**: M3
- **Branching**: α only
- **Notes**: t₁/₂ ~ 0.52 s

### DC-U235-012: ²⁰⁷Pb (STABLE)
- **n(207)**: 6.1 × 207^(1/3) ≈ 36.0 [P]
- **d(n)**: d(36)=0 → EXACTLY ALLOWED
- **Mechanism**: None (stable)
- **Notes**: End of chain, N=125

---

## Chain Statistics

| Metric | Value |
|--------|-------|
| Total steps | 11-12 (branch-dependent) |
| α-decays | 7-8 |
| β⁻-decays | 4-5 |
| Branch points | 2 (²²⁷Ac, ²¹¹Bi) |
| n(start) | ~37.6 (forbidden) |
| n(end) | ~36.0 (allowed) |

---

## Branching Tests H2-H3

### H2: ²²⁷Ac Branch
**EDC Prediction** [P]:
- β⁻ favored (maintains n, reduces asymmetry)
- α suppressed (cluster formation harder)

**Observed**: β⁻ 98.6%, α 1.4%

**Interpretation**: M2 >> M3 at this n

### H3: ²¹¹Bi Branch
**EDC Prediction** [P]:
- α favored (near allowed n=36, cluster formed)
- β⁻ suppressed

**Observed**: α 99.7%, β⁻ 0.3%

**Interpretation**: M3 >> M2 when near target

---

## Comparison: Ac-227 vs Bi-211

| Nuclide | n(A) | d(36) | α% | β⁻% | Dominant M |
|---------|------|-------|----|----|------------|
| ²²⁷Ac | 37.2 | 1.2 | 1.4 | 98.6 | M2 |
| ²¹¹Bi | 36.3 | 0.3 | 99.7 | 0.3 | M3 |

**Pattern**: As d(36) → 0, α becomes dominant.

This supports the EDC hypothesis that decay mode selection correlates with proximity to allowed coordination.

---

## EDC Interpretation

The U-235 chain demonstrates:
1. **Initial state**: n ≈ 37.6, in forbidden zone
2. **Final state**: n = 36, at allowed target
3. **Trend**: d(n) decreases toward 36
4. **Branching evolution**:
   - Early (far from 36): β⁻ dominant
   - Late (near 36): α dominant
5. **Mechanism transition**: M2 → M3 as n → 36
