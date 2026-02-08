# BRANCHING RULE H-N48-01 (V6)

**Created**: 2026-01-31
**Purpose**: Formalize branching hypothesis with falsification tests
**Status**: [P] — requires empirical validation

---

## Primary Hypothesis

### H-N48-01: d(n) Minimization Rule [P]

**Statement** (AS-N48-009):
> When multiple decay channels exist, the preferred branch is the one that reduces d(n(A_daughter)) fastest.

**Formal Definition**:
Let P be parent nucleus with mass A_P.
Let C₁, C₂, ... be available decay channels with daughters D₁, D₂, ...

```
BR(Cᵢ) ∝ exp(-λ × d(n(A_Dᵢ)))
```

where λ is an ordering parameter [P].

**Simplified Binary Rule**:
For two channels C₁ and C₂:
```
C₁ preferred ⟺ d(n(A_D₁)) < d(n(A_D₂))
```

---

## Refined Hypothesis

### H-N48-01b: Q-Threshold Gated d(n) Rule [P]

**Statement**:
> Channel selection by d(n) applies ONLY if Q > ε_f; otherwise channel is suppressed.

**Formal Definition**:
```
If Q(Cᵢ) < ε_f(P): Channel Cᵢ is suppressed
Among open channels: Select by d(n) minimization
```

**Rationale**: Explains why some branch points favor energetically disfavored channel.

---

## Falsification Tests

### TEST-H-01: High-d Branch Point
- **Description**: Find nucleus where H-N48-01 makes unambiguous prediction
- **Criterion**: d(n) difference > 1 between channels
- **Candidate**: ²²⁷Ac (d_α = 1.0, d_β = 1.2, Δd = 0.2)
- **Prediction**: α > β by d(n) rule
- **Test**: If β >> α despite open α channel, H-N48-01 falsified
- **Data Status**: [BL:SOURCE_TBD]

### TEST-H-02: Low-d Branch Point
- **Description**: Near-target nucleus with both channels open
- **Criterion**: Both channels have small d(n) < 0.5
- **Candidate**: ²¹¹Bi (d_α = 0.1, d_β = 0.3)
- **Prediction**: α >> β
- **Test**: If α < 90%, question d(n) sensitivity
- **Data Status**: [BL:SOURCE_TBD]

### TEST-H-03: Equal-d Branch Point
- **Description**: Find case where d(C₁) ≈ d(C₂)
- **Criterion**: |d₁ - d₂| < 0.1
- **Candidate**: Need to identify from chain analysis
- **Prediction**: BR₁/BR₂ ≈ 1
- **Test**: If strong asymmetry despite equal d, other factors dominate
- **Data Status**: [BL:SOURCE_TBD]

---

## Validation Data Requirements

For complete testing, need:

| Data Type | Count | Source |
|-----------|-------|--------|
| Branch point branching ratios | ≥ 10 | NNDC [BL] |
| Q-values (α and β) | ≥ 20 | AME2020 [BL] |
| Identified d(n) for each | Computed | Toy model |

---

## Current Scorecard

| Test Case | d(n) Prediction | Observed | H-N48-01 | H-N48-01b |
|-----------|-----------------|----------|----------|-----------|
| ²¹¹Bi | α >> β | α ~99.7% | ✓ | ✓ |
| ²¹²Bi | α > β | β ~64% | ✗ | ? (Q?) |
| ²¹⁴Bi | α > β | β ~99.98% | ✗ | ? (Q?) |
| ²¹⁸Po | α | α ~99.98% | ✓ | ✓ |
| ²²⁷Ac | α > β | β ~98.6% | ✗ | ? (Q?) |

**H-N48-01 Raw Score**: 2/5
**H-N48-01b Potential Score**: 5/5 (pending Q-value verification)

---

## Connection to n=48 Approach

For superheavy elements (A > 350):
- n(A) > 43, closer to n=48 than n=36
- H-N48-01 predicts decay channels that approach n=48
- α-decay (ΔA = -4) becomes less favorable as n → 48

**Prediction for A > 400**:
- SF may become preferred over α if it better approaches n=48
- Or fission products may partition to two n=36 nuclei

---

## Upgrade Path

| Current | Target | Requirement |
|---------|--------|-------------|
| [P] | [I] | Validate on 10+ branch points with complete Q-data |
| [I] | [Dc] | Derive λ from barrier physics |
| [Dc] | [Der] | Full derivation from 5D action |

---

## Summary

H-N48-01 is a testable hypothesis that:
1. Provides qualitative predictions for branching
2. Has partial empirical support (2/5 direct)
3. May be improved by Q-threshold correction (H-N48-01b)
4. Extends to n=48 approach predictions for SHE
