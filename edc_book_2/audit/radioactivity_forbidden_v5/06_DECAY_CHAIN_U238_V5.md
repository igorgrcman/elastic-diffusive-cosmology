# DECAY CHAIN U-238 V5 (Radium Series)

**Created**: 2026-01-31
**Purpose**: EDC-annotated decay chain to Pb-206
**Data Status**: All nuclear data [BL:SOURCE_TBD]

---

## Chain Overview

```
²³⁸U → ²³⁴Th → ²³⁴Pa → ²³⁴U → ²³⁰Th → ²²⁶Ra → ²²²Rn →
²¹⁸Po → ²¹⁴Pb → ²¹⁴Bi → ²¹⁴Po → ²¹⁰Pb → ²¹⁰Bi → ²¹⁰Po → ²⁰⁶Pb
```

---

## EDC Step Annotations

### DC-U238-001: ²³⁸U → ²³⁴Th (α)
- **n(238)**: 6.1 × 238^(1/3) ≈ 37.9 [P]
- **d(n)**: d(36)=1.9, d(48)=10.1 → toward 36
- **Mechanism**: M1 (domain mixing)
- **Prediction**: α-decay favored [P]
- **Branching**: α only (no β⁻ channel)
- **Notes**: Near FT-38 (n=38), high frustration

### DC-U238-002: ²³⁴Th → ²³⁴Pa (β⁻)
- **n(234)**: 6.1 × 234^(1/3) ≈ 37.6 [P]
- **d(n)**: d(36)=1.6, d(48)=10.4 → toward 36
- **Mechanism**: M2 (defect-mediated)
- **Prediction**: β⁻ (no α accessible) [P]
- **Branching**: β⁻ only
- **Notes**: Isomeric states exist

### DC-U238-003: ²³⁴Pa → ²³⁴U (β⁻)
- **n(234)**: 37.6 [P]
- **d(n)**: toward 36
- **Mechanism**: M2
- **Prediction**: β⁻ [P]
- **Branching**: β⁻ only
- **Notes**: Short-lived (6.7 hr)

### DC-U238-004: ²³⁴U → ²³⁰Th (α)
- **n(234)**: 37.6 [P]
- **d(n)**: toward 36
- **Mechanism**: M1/M3
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: Preformed α-cluster

### DC-U238-005: ²³⁰Th → ²²⁶Ra (α)
- **n(230)**: 6.1 × 230^(1/3) ≈ 37.4 [P]
- **d(n)**: d(36)=1.4, d(48)=10.6 → toward 36
- **Mechanism**: M3 (α-clusterization)
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: Approaching n=36 target

### DC-U238-006: ²²⁶Ra → ²²²Rn (α)
- **n(226)**: 6.1 × 226^(1/3) ≈ 37.2 [P]
- **d(n)**: d(36)=1.2, d(48)=10.8 → toward 36
- **Mechanism**: M3
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: Radon gas product

### DC-U238-007: ²²²Rn → ²¹⁸Po (α)
- **n(222)**: 6.1 × 222^(1/3) ≈ 36.9 [P]
- **d(n)**: d(36)=0.9, d(48)=11.1 → at 36
- **Mechanism**: M3
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: Near allowed n=36

### DC-U238-008: ²¹⁸Po → ²¹⁴Pb (α)
- **n(218)**: 6.1 × 218^(1/3) ≈ 36.7 [P]
- **d(n)**: d(36)=0.7 → at 36 target
- **Mechanism**: M3
- **Prediction**: α [P]
- **Branching**: α ~99.98%, β ~0.02%
- **Notes**: Essentially pure α

### DC-U238-009: ²¹⁴Pb → ²¹⁴Bi (β⁻)
- **n(214)**: 6.1 × 214^(1/3) ≈ 36.5 [P]
- **d(n)**: d(36)=0.5 → at 36
- **Mechanism**: M2
- **Prediction**: β⁻ [P]
- **Branching**: β⁻ only
- **Notes**: At allowed configuration

### DC-U238-010: ²¹⁴Bi → ²¹⁴Po (β⁻)
- **n(214)**: 36.5 [P]
- **d(n)**: at 36
- **Mechanism**: M2
- **Prediction**: β⁻ dominant [P]
- **Branching**: β⁻ ~99.98%, α ~0.02%
- **Notes**: Near-pure β⁻

### DC-U238-011: ²¹⁴Po → ²¹⁰Pb (α)
- **n(214)**: 36.5 [P]
- **d(n)**: at 36
- **Mechanism**: M3
- **Prediction**: α (fast) [P]
- **Branching**: α only
- **Notes**: Microsecond half-life

### DC-U238-012: ²¹⁰Pb → ²¹⁰Bi (β⁻)
- **n(210)**: 6.1 × 210^(1/3) ≈ 36.2 [P]
- **d(n)**: d(36)=0.2 → at 36
- **Mechanism**: M2
- **Prediction**: β⁻ [P]
- **Branching**: β⁻ only
- **Notes**: Long-lived (22 yr)

### DC-U238-013: ²¹⁰Bi → ²¹⁰Po (β⁻)
- **n(210)**: 36.2 [P]
- **d(n)**: at 36
- **Mechanism**: M2
- **Prediction**: β⁻ [P]
- **Branching**: β⁻ ~99.99%, α ~0.01%
- **Notes**: Near-pure β⁻

### DC-U238-014: ²¹⁰Po → ²⁰⁶Pb (α)
- **n(210)**: 36.2 [P]
- **d(n)**: at 36
- **Mechanism**: M3
- **Prediction**: α [P]
- **Branching**: α only
- **Notes**: Final α to stable Pb

### DC-U238-015: ²⁰⁶Pb (STABLE)
- **n(206)**: 6.1 × 206^(1/3) ≈ 36.0 [P]
- **d(n)**: d(36)=0 → EXACTLY ALLOWED
- **Mechanism**: None (stable)
- **Notes**: End of chain at n=36 target

---

## Chain Statistics

| Metric | Value |
|--------|-------|
| Total steps | 14 |
| α-decays | 8 |
| β⁻-decays | 6 |
| Branch points | 3 (minor) |
| n(start) | ~38 (forbidden) |
| n(end) | 36 (allowed) |

---

## EDC Interpretation

The U-238 chain demonstrates:
1. **Initial state**: n ≈ 38, in forbidden zone FT-38
2. **Final state**: n = 36, at allowed target
3. **Trend**: d(n) decreases monotonically toward 36
4. **Mode selection**:
   - α when Q_α > 0 and preformed cluster
   - β⁻ when no α channel energetically available
5. **Stability criterion**: Chain terminates at first allowed n
