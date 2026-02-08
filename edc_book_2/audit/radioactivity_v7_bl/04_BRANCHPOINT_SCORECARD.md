# BRANCHPOINT SCORECARD (V7)

**Created**: 2026-01-31
**Purpose**: Test H-N48-01 and H-N48-01b with BL data
**Status**: 3 mandatory branchpoints evaluated

---

## Hypothesis Definitions

### H-N48-01 (Baseline) [P]
> At branch points, the channel that reduces d(n) is preferred.

**Rule**: Prefer channel with Δd < 0 (daughter closer to allowed n).

### H-N48-01b (Q-Threshold Gated) [P]
> Channel selection by d(n) applies ONLY if Q > Q_threshold.

**Rule**: If Q_channel < Q_threshold, channel is suppressed regardless of Δd.

---

## Scorecard: Mandatory Branchpoints

### BP-1: ²¹²Bi (Th-232 Series)

| Field | α Channel | β⁻ Channel |
|-------|-----------|------------|
| Daughter | ²⁰⁸Tl (A=208) | ²¹²Po (A=212) |
| n(A_d) | 36.14 [P] | 36.39 [P] |
| d(n_d) | 0.14 | 0.39 |
| **Δd** | **-0.25** | 0.00 |
| Q (keV) | 6207.26 [BL] | 2251.5 [BL] |
| BR(%) | 35.94 [BL] | **64.06** [BL] |

**H-N48-01 Prediction**: α preferred (Δd = -0.25 < 0)
**H-N48-01 Result**: ✗ **FAILS** — β⁻ dominant (64.06%)

**H-N48-01b Analysis**:
- Q_α = 6207 keV >> Q_β = 2252 keV
- α channel is energetically favorable, yet β⁻ dominates
- Q-threshold cannot rescue this case

**Explanation Tag**: [Open] — Neither d(n) nor Q explains β⁻ dominance

---

### BP-2: ²²⁷Ac (U-235 Series)

| Field | α Channel | β⁻ Channel |
|-------|-----------|------------|
| Daughter | ²²³Fr (A=223) | ²²⁷Th (A=227) |
| n(A_d) | 36.99 [P] | 37.21 [P] |
| d(n_d) | 0.99 | 1.21 |
| **Δd** | **-0.22** | 0.00 |
| Q (keV) | 5042.19 [BL] | 44.8 [BL] |
| BR(%) | 1.38 [BL] | **98.62** [BL] |

**H-N48-01 Prediction**: α preferred (Δd = -0.22 < 0)
**H-N48-01 Result**: ✗ **FAILS STRONGLY** — β⁻ = 98.62%

**H-N48-01b Analysis**:
- Q_α = 5042 keV >> Q_β = 44.8 keV (!)
- Extremely low Q_β, yet β⁻ dominates overwhelmingly
- This is OPPOSITE of Q-threshold expectation

**Explanation Tag**: [Open] — Strong counterexample; spin-parity selection likely

**Note**: ²²⁷Ac (3/2⁻) → ²²⁷Th (1/2⁺) is a ΔJ=1, parity change — "allowed" β transition
         ²²⁷Ac (3/2⁻) → ²²³Fr (3/2⁻) is ΔJ=0, no parity change — but α has Coulomb barrier

---

### BP-3: ²¹¹Bi (U-235 Series)

| Field | α Channel | β⁻ Channel |
|-------|-----------|------------|
| Daughter | ²⁰⁷Tl (A=207) | ²¹¹Po (A=211) |
| n(A_d) | 36.09 [P] | 36.32 [P] |
| d(n_d) | 0.09 | 0.32 |
| **Δd** | **-0.23** | 0.00 |
| Q (keV) | 6750.3 [BL] | 574 [BL] |
| BR(%) | **99.724** [BL] | 0.276 [BL] |

**H-N48-01 Prediction**: α preferred (Δd = -0.23 < 0)
**H-N48-01 Result**: ✓ **SUCCESS** — α = 99.724%

**H-N48-01b Analysis**:
- Q_α = 6750 keV >> Q_β = 574 keV
- Both d(n) and Q favor α
- Consistent with both hypotheses

**Explanation Tag**: [I] — d(n) and Q aligned; success expected

---

## Summary Scorecard

| Branchpoint | H-N48-01 | H-N48-01b | Q Favors | d(n) Favors | Dominant |
|-------------|----------|-----------|----------|-------------|----------|
| ²¹²Bi | ✗ FAIL | ✗ FAIL | α | α | **β⁻** |
| ²²⁷Ac | ✗ FAIL | ✗ FAIL | α | α | **β⁻** |
| ²¹¹Bi | ✓ SUCCESS | ✓ SUCCESS | α | α | **α** |

### Overall Score

| Hypothesis | Successes | Failures | Score |
|------------|-----------|----------|-------|
| H-N48-01 | 1 | 2 | **1/3 = 33%** |
| H-N48-01b | 1 | 2 | **1/3 = 33%** |

---

## Critical Analysis

### Why H-N48-01 Fails on ²¹²Bi and ²²⁷Ac

1. **²¹²Bi**: Both d(n) and Q favor α, yet β⁻ dominates
   - Possible factor: Phase space (more final states for β⁻)
   - Possible factor: Matrix elements (nuclear structure)

2. **²²⁷Ac**: Extreme case — Q_α >> Q_β by 100×, yet β⁻ = 98.6%
   - Key insight: Q_β = 44.8 keV is VERY low
   - Low Q_β means slow β⁻, but still dominates
   - **Spin-parity selection rules** likely explanation:
     - ²²⁷Ac (3/2⁻) → ²²⁷Th (1/2⁺): Allowed Gamow-Teller β transition
     - α-decay must tunnel through Coulomb barrier

### Why H-N48-01 Works on ²¹¹Bi

- Both d(n) and Q strongly favor α
- Parent is far from magic numbers; no special selection rules
- Standard α-dominance case

---

## Revised Hypothesis: H-N48-01c [P]

**Proposed**: d(n) influences branching only when:
1. Both channels have comparable Q-values, AND
2. No special spin-parity selection rules apply

**Formulation**:
```
If |Q_α - Q_β| / max(Q_α, Q_β) < 0.5 AND no forbidden transitions:
    Apply d(n) preference
Else:
    Nuclear structure dominates
```

**Status**: [P] — needs testing on more branchpoints

---

## Falsification Status

| Test | Result | Implication |
|------|--------|-------------|
| d(n) alone predicts branching | ✗ FAILED | d(n) insufficient |
| Q-threshold rescues d(n) | ✗ FAILED | Q doesn't explain |
| d(n) + Q together | Partial | Works when aligned |

**Conclusion**: The coordination distance d(n) is NOT a reliable predictor of branching ratios. Nuclear structure effects (spin-parity, matrix elements) dominate in 2/3 of test cases.
