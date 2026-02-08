# HYPOTHESES UPDATE (V7)

**Created**: 2026-01-31
**Purpose**: Update hypothesis status based on BL testing
**Result**: H-N48-01 largely falsified; revised hypotheses proposed

---

## Hypothesis Registry

### H-N48-01: d(n) Branching Rule [P → Partially Falsified]

**Original Statement**:
> At branch points, the channel that reduces d(n) is preferred.

**Test Result**: 1/3 success (33%)

**Status Change**: [P] → [Partially Falsified]

**Evidence**:
- ²¹¹Bi: ✓ Confirms (α = 99.7% as predicted)
- ²¹²Bi: ✗ Contradicts (β⁻ = 64% despite d(n) favoring α)
- ²²⁷Ac: ✗ Strongly contradicts (β⁻ = 98.6% despite d(n) and Q favoring α)

**Verdict**: d(n) alone is NOT a reliable branching predictor.

---

### H-N48-01b: Q-Threshold Gated d(n) Rule [P → Falsified]

**Original Statement**:
> Channel selection by d(n) applies ONLY if Q > Q_threshold.

**Test Result**: 1/3 success (33%)

**Status Change**: [P] → [Falsified]

**Evidence**:
- The Q-threshold concept cannot explain why ²²⁷Ac strongly favors β⁻ (Q_β = 45 keV) over α (Q_α = 5042 keV)
- Q-threshold would predict α dominance, not β⁻

**Verdict**: Q-threshold gating does not rescue H-N48-01.

---

### H-N48-01c: Conditional d(n) Rule [P — NEW]

**Statement**:
> d(n) influences branching only when both channels have comparable Q-values AND no special spin-parity selection rules apply.

**Formulation**:
```
Condition 1: |Q_α - Q_β| / max(Q_α, Q_β) < 0.5
Condition 2: ΔJ ≤ 2, parity change allowed for both channels
If Conditions 1 AND 2: Apply d(n) preference
Else: Nuclear structure dominates
```

**Status**: [P] — Untested; requires additional branchpoints

**Rationale**: ²²⁷Ac case shows that when β⁻ is an "allowed" Gamow-Teller transition with favorable spin-parity, it can dominate despite extremely low Q and unfavorable d(n).

---

### H-N48-02: Monotonic d(n) Decrease [I — Supported]

**Statement**:
> Along any decay chain, d(n) decreases monotonically toward the stable endpoint.

**Test Result**: 3/3 chains confirm

**Evidence**:
- U-238: d(n) decreases from 1.81 (²³⁸U) to 0.03 (²⁰⁶Pb) ✓
- Th-232: d(n) decreases from 1.48 (²³²Th) to 0.14 (²⁰⁸Pb) ✓
- U-235: d(n) decreases from 1.65 (²³⁵U) to 0.09 (²⁰⁷Pb) ✓

**Status**: [P] → [I] (Inferred from data)

**Note**: This says nothing about branching, only about chain trajectory.

---

### H-N48-03: Stable Endpoints at Allowed n [I — Supported]

**Statement**:
> Stable isotopes terminate at or very near allowed coordination n ∈ S.

**Test Result**: 3/3 endpoints confirm

**Evidence**:
- ²⁰⁶Pb: n(206) = 36.03, d = 0.03 ≈ 0 ✓
- ²⁰⁸Pb: n(208) = 36.14, d = 0.14 ≈ 0 ✓
- ²⁰⁷Pb: n(207) = 36.09, d = 0.09 ≈ 0 ✓

**Status**: [I] — All endpoints within d < 0.15 of n=36

**Caveat**: This is a consistency check of the n(A) formula calibration, not an independent prediction.

---

### H-N48-04: n=48 Target Relevance [P — Untested]

**Statement**:
> For A > 350, nuclei approach n=48 as their target rather than n=36.

**Status**: [P] — No chain data available for A > 250

**Required Data**: Decay chains of superheavy elements (Z > 110)

---

### H-N48-05: Island Ladder (36 → 48 → 54) [P — Untested]

**Statement**:
> There exists a sequence of coordination targets at n = 36, 48, 54, ... that heavy nuclei can approach.

**Status**: [P] — Theoretical prediction from S_extended

**Crossover Points** (Model M-A):
- 36 ↔ 48: A ≈ 285
- 48 ↔ 54: A ≈ 530

---

## Summary Table

| Hypothesis | Original | After V7 BL Test | Score |
|------------|----------|------------------|-------|
| H-N48-01 | [P] | Partially Falsified | 1/3 |
| H-N48-01b | [P] | Falsified | 1/3 |
| H-N48-01c | - | [P] NEW | Untested |
| H-N48-02 | [P] | [I] Supported | 3/3 |
| H-N48-03 | [P] | [I] Supported | 3/3 |
| H-N48-04 | [P] | [P] Untested | - |
| H-N48-05 | [P] | [P] Untested | - |

---

## Key Learnings

1. **d(n) is not a branching predictor**: The coordination distance does not reliably determine which decay channel dominates.

2. **Nuclear structure trumps geometry**: Spin-parity selection rules, matrix elements, and Coulomb barriers are more important than topological coordination.

3. **d(n) describes chain trajectory**: The monotonic decrease in d(n) along chains IS observed, suggesting d(n) may influence overall chain direction without controlling individual branching.

4. **Q-value is not sufficient either**: High Q_α does not guarantee α-dominance (see ²²⁷Ac).

5. **Combined factors needed**: Any successful branching model must include Q-values, spin-parity, AND possibly d(n) as a minor modifier.

---

## Falsification Tests Completed

| Test ID | Description | Result |
|---------|-------------|--------|
| TEST-N48-08 | d(n) branching correlation | ✗ Failed (1/3) |
| TEST-BL-01 | Q-threshold rescue | ✗ Failed |
| TEST-BL-02 | Chain monotonicity | ✓ Passed (3/3) |
| TEST-BL-03 | Endpoint allowed | ✓ Passed (3/3) |

---

## Recommended Next Steps

1. **Abandon H-N48-01 for branching**: The hypothesis is not predictive.

2. **Retain d(n) for chain analysis**: The monotonicity and endpoint convergence are real patterns.

3. **Develop H-N48-01c if needed**: But only with spin-parity data for branchpoints.

4. **Focus on half-life correlations**: Test whether d(n) correlates with t₁/₂ deviations from G-N law (this doesn't require branching prediction).
