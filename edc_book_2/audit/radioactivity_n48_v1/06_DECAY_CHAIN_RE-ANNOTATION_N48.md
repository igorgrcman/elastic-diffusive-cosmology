# DECAY CHAIN RE-ANNOTATION (N48 View, V6)

**Created**: 2026-01-31
**Purpose**: Annotate existing chains with n=48 perspective + branching rule
**Source**: V5 decay chain files, V4 chain structures
**Status**: No [BL] numerics; qualitative annotations only

---

## Branching Rule Hypothesis H-N48-01

**Statement** [P] (AS-N48-009):
> When multiple decay channels exist, the preferred branch is the one that reduces d(n(A_daughter)) fastest.

**Formulation**:
For parent P with channels C₁ (daughter D₁) and C₂ (daughter D₂):
```
Preferred = C₁  if  d(n(A_D₁)) < d(n(A_D₂))
Preferred = C₂  if  d(n(A_D₂)) < d(n(A_D₁))
Equal     if  d(n(A_D₁)) = d(n(A_D₂))
```

---

## Chain Annotations

### U-238 Chain (View from n=48 perspective)

#### Key Steps with Branching

**DC-U238-V6-A: ²¹⁸Po (A=218)**
- n(218) = 6.1 × 5.99 = 36.5 [P]
- d(n) = 0.5 (to n=36)
- Channels: α (→A=214), β (rare)
- H-N48-01 Test:
  - α → A=214: n(214) = 36.4, d = 0.4
  - Decision: α preferred (reduces d)
  - **Branching slot**: α ~99.98% [BL:SOURCE_TBD]

**DC-U238-V6-B: ²¹⁴Bi (A=214)**
- n(214) = 36.4 [P]
- d(n) = 0.4
- Channels: β⁻ (→A=214), α (→A=210)
- H-N48-01 Test:
  - β⁻ → ²¹⁴Po (A=214): n unchanged, d = 0.4
  - α → ²¹⁰Tl (A=210): n(210) = 36.3, d = 0.3
  - Decision: α should be preferred (smaller d)
  - **Observed**: β⁻ dominant [BL:SOURCE_TBD]
  - **Anomaly Flag**: H-N48-01 may fail here; Q_α threshold issue?

---

### Th-232 Chain (View from n=48 perspective)

#### Key Branch Point

**DC-TH232-V6-A: ²¹²Bi (A=212)**
- n(212) = 6.1 × 5.96 = 36.4 [P]
- d(n) = 0.4
- Channels: β⁻ (→²¹²Po), α (→²⁰⁸Tl)
- H-N48-01 Test:
  - β⁻ → ²¹²Po (A=212): n = 36.4, d = 0.4
  - α → ²⁰⁸Tl (A=208): n = 36.2, d = 0.2
  - Decision: α should be preferred (d = 0.2 < 0.4)
  - **Branching slot**: β⁻ ~64%, α ~36% [BL:SOURCE_TBD]
  - **Mixed Result**: α minority but significant; partial support for H-N48-01

---

### U-235 Chain (View from n=48 perspective)

#### Key Branch Points

**DC-U235-V6-A: ²²⁷Ac (A=227)**
- n(227) = 6.1 × 6.10 = 37.2 [P]
- d(n) = 1.2 (to n=36)
- Channels: β⁻ (→²²⁷Th), α (→²²³Fr)
- H-N48-01 Test:
  - β⁻ → A=227: n unchanged, d = 1.2
  - α → A=223: n(223) = 37.0, d = 1.0
  - Decision: α should be preferred (smaller d)
  - **Branching slot**: β⁻ ~98.6%, α ~1.4% [BL:SOURCE_TBD]
  - **Strong Anomaly**: H-N48-01 fails; Q_α likely below threshold

**DC-U235-V6-B: ²¹¹Bi (A=211)**
- n(211) = 6.1 × 5.95 = 36.3 [P]
- d(n) = 0.3
- Channels: α (→²⁰⁷Tl), β⁻ (→²¹¹Po)
- H-N48-01 Test:
  - α → A=207: n(207) = 36.1, d = 0.1
  - β⁻ → A=211: n = 36.3, d = 0.3
  - Decision: α should be strongly preferred
  - **Branching slot**: α ~99.7%, β⁻ ~0.3% [BL:SOURCE_TBD]
  - **Strong Support**: H-N48-01 succeeds here

---

## Falsification Test Cases for H-N48-01

### Test Case 1: ²¹¹Bi
- **Prediction**: α >> β⁻ (d_α = 0.1 vs d_β = 0.3)
- **Required Data**: Branching ratio [BL:SOURCE_TBD]
- **Expected**: If H-N48-01 holds, α/β > 10

### Test Case 2: ²¹²Bi
- **Prediction**: α > β⁻ (d_α = 0.2 vs d_β = 0.4)
- **Required Data**: Branching ratio [BL:SOURCE_TBD]
- **Expected**: If H-N48-01 holds, α/β > 1
- **Known Issue**: Observed β > α; needs energy threshold correction

### Test Case 3: ²²⁷Ac
- **Prediction**: α > β⁻ (d_α = 1.0 vs d_β = 1.2)
- **Required Data**: Branching ratio [BL:SOURCE_TBD]
- **Expected**: If H-N48-01 holds, α/β > 1
- **Known Issue**: Observed β >> α; strong counterexample

---

## Refined Hypothesis H-N48-01b

Given the anomalies above, consider a refined rule:

**H-N48-01b** [P]:
> Preferred decay minimizes d(n) **GIVEN** that Q > ε_f threshold.

**Formulation**:
```
If Q(C₁) < ε_f(P): Channel C₁ suppressed regardless of d(n)
If Q(C₁) ≥ ε_f(P) and Q(C₂) ≥ ε_f(P): Apply d(n) rule
```

This explains:
- ²¹¹Bi: Q_α sufficient, α dominates per d(n) rule ✓
- ²²⁷Ac: Q_α below threshold, β forced despite d(n) ✓
- ²¹²Bi: Q_α marginal, mixed result ✓

---

## n=48 Approach Signature

For nuclei approaching n=48 (A > 350), H-N48-01 predicts:
- Decay toward n=48 rather than n=36
- α-decay may become less favored (n already near target)
- SF may compete when n > 45

**No Chain Data Yet**: Require superheavy element decay data [BL:SOURCE_TBD]

---

## Summary: Branch Point Scorecard

| Nuclide | A | d(n) | H-N48-01 Prediction | Observed | Match? |
|---------|---|------|---------------------|----------|--------|
| ²¹¹Bi | 211 | 0.3 | α >> β | α ~99.7% | ✓ YES |
| ²¹²Bi | 212 | 0.4 | α > β | β ~64% | ✗ NO |
| ²¹⁴Bi | 214 | 0.4 | α > β | β ~99.98% | ✗ NO |
| ²¹⁸Po | 218 | 0.5 | α | α ~99.98% | ✓ YES |
| ²²⁷Ac | 227 | 1.2 | α > β | β ~98.6% | ✗ NO |

**Score**: 2/5 direct matches

**With Q-threshold correction (H-N48-01b)**: Potentially 5/5 if Q_α values confirm suppression.
