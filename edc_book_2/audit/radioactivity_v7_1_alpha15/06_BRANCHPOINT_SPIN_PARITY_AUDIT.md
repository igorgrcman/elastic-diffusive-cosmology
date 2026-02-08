# BRANCHPOINT SPIN-PARITY AUDIT (V7.1)

**Created**: 2026-01-31
**Purpose**: Test if spin-parity selection rules explain V7 branching failures
**Goal**: Refine H-N48-01 → H-N48-01c (conditional d(n) rule)

---

## V7 Branchpoint Results (Recap)

| Branchpoint | H-N48-01 | d(n) favors | Q favors | Observed | Score |
|-------------|----------|-------------|----------|----------|-------|
| ²¹²Bi | ✗ FAIL | α | α | β⁻ (64%) | 0 |
| ²²⁷Ac | ✗ FAIL | α | α | β⁻ (99%) | 0 |
| ²¹¹Bi | ✓ SUCCESS | α | α | α (99.7%) | 1 |

**Question**: Can spin-parity selection rules explain why ²¹²Bi and ²²⁷Ac favor β⁻ despite d(n) and Q pointing to α?

---

## Spin-Parity Data [BL]

### BP-1: ²¹²Bi

| State | Nuclide | Jπ | Source |
|-------|---------|-----|--------|
| Parent | ²¹²Bi | 1⁻ | [BL:S1] ENSDF A=212 |
| α-daughter | ²⁰⁸Tl | 5⁺ | [BL:S1] ENSDF A=208 |
| β-daughter | ²¹²Po | 0⁺ | [BL:S1] ENSDF A=212 |

**α-decay analysis**:
- ²¹²Bi (1⁻) → ²⁰⁸Tl (5⁺)
- ΔJ = |1 - 5| = 4
- Parity change: (-) → (+) = YES
- **Classification**: ΔJ = 4, ΔΠ = yes → **Highly hindered α** (L = 4 or 5 required)

**β-decay analysis**:
- ²¹²Bi (1⁻) → ²¹²Po (0⁺)
- ΔJ = |1 - 0| = 1
- Parity change: (-) → (+) = YES
- **Classification**: ΔJ = 1, ΔΠ = yes → **First-forbidden unique β⁻**

**Assessment**: The α-decay requires high orbital angular momentum (L ≥ 4) to carry away the spin change, which introduces a strong centrifugal barrier. The β-decay is first-forbidden but still more accessible than a highly hindered α.

**Verdict**: Selection rules FAVOR β⁻ ✓

---

### BP-2: ²²⁷Ac

| State | Nuclide | Jπ | Source |
|-------|---------|-----|--------|
| Parent | ²²⁷Ac | 3/2⁻ | [BL:S1] ENSDF A=227 |
| α-daughter | ²²³Fr | 3/2⁻ | [BL:S1] ENSDF A=223 |
| β-daughter | ²²⁷Th | 1/2⁺ | [BL:S1] ENSDF A=227 |

**α-decay analysis**:
- ²²⁷Ac (3/2⁻) → ²²³Fr (3/2⁻)
- ΔJ = 0
- Parity change: NO
- **Classification**: ΔJ = 0, ΔΠ = no → **Favored α** (L = 0 allowed)

**β-decay analysis**:
- ²²⁷Ac (3/2⁻) → ²²⁷Th (1/2⁺)
- ΔJ = |3/2 - 1/2| = 1
- Parity change: (-) → (+) = YES
- **Classification**: ΔJ = 1, ΔΠ = yes → **Allowed Gamow-Teller** (if treated as ΔJ=1, yes-parity change is first-forbidden, but...)

**Critical Insight**: Wait — for β-decay:
- ΔJ = 1 with parity change is actually **first-forbidden** (not allowed)
- But the Q_β = 45 keV is extremely low
- Yet β⁻ = 98.6%

**Re-analysis**: The ²²⁷Ac → ²²⁷Th transition:
- Parent: 3/2⁻
- Daughter: 1/2⁺
- This is ΔI = 1, Δπ = yes
- **Classification**: First-forbidden (ΔJ = 0,1,2 with parity change)

But wait — why does first-forbidden β dominate over favored α with Q_α >> Q_β?

**Nuclear Structure Effect**: The α-decay, though "allowed" by spin-parity, must tunnel through the Coulomb barrier. The extremely low Q_β (45 keV) means slow β-decay, but the matrix element must be unusually large.

**Alternative Explanation**: The ²²⁷Ac ground state may have significant admixture with states that enhance the β-decay matrix element. This is a nuclear structure effect beyond simple selection rules.

**Verdict**: Selection rules do NOT fully explain ²²⁷Ac ✗

---

### BP-3: ²¹¹Bi

| State | Nuclide | Jπ | Source |
|-------|---------|-----|--------|
| Parent | ²¹¹Bi | 9/2⁻ | [BL:S1] ENSDF A=211 |
| α-daughter | ²⁰⁷Tl | 1/2⁺ | [BL:S1] ENSDF A=207 |
| β-daughter | ²¹¹Po | 9/2⁺ | [BL:S1] ENSDF A=211 |

**α-decay analysis**:
- ²¹¹Bi (9/2⁻) → ²⁰⁷Tl (1/2⁺)
- ΔJ = |9/2 - 1/2| = 4
- Parity change: (-) → (+) = YES
- **Classification**: ΔJ = 4, ΔΠ = yes → **Hindered α** (L = 4 or 5)

**β-decay analysis**:
- ²¹¹Bi (9/2⁻) → ²¹¹Po (9/2⁺)
- ΔJ = 0
- Parity change: (-) → (+) = YES
- **Classification**: ΔJ = 0, ΔΠ = yes → **First-forbidden non-unique β⁻**

**Assessment**: Both decays are hindered:
- α: ΔJ = 4 requires high L
- β: First-forbidden

But Q_α = 6750 keV >> Q_β = 574 keV, so α wins despite hindrance.

**Verdict**: High Q_α overcomes hindrance; consistent with observation ✓

---

## Summary of Selection Rule Analysis

| Branchpoint | α Classification | β Classification | Expected Dominant | Observed | Match |
|-------------|------------------|------------------|-------------------|----------|-------|
| ²¹²Bi | Highly hindered (ΔJ=4) | First-forbidden | β⁻ | β⁻ | ✓ |
| ²²⁷Ac | Favored (ΔJ=0) | First-forbidden | α | β⁻ | ✗ |
| ²¹¹Bi | Hindered (ΔJ=4) | First-forbidden | Q-dependent | α | ✓ |

**Score**: 2/3 explained by selection rules (improvement over 1/3 for d(n) alone)

---

## The ²²⁷Ac Anomaly [Open]

The ²²⁷Ac case remains unexplained by simple selection rules:
- α-decay is spin-parity favored (ΔJ = 0, no parity change)
- β-decay is first-forbidden
- Q_α = 5042 keV >> Q_β = 45 keV
- Yet β⁻ = 98.6%

**Possible Explanations**:
1. **Nuclear matrix element**: The ²²⁷Ac → ²²⁷Th matrix element is anomalously large
2. **Collective enhancement**: Deformation or pairing effects enhance β-decay
3. **α-clustering suppression**: Poor α-cluster formation in ²²⁷Ac ground state
4. **Fine structure**: The α-decay may be to excited states with reduced Q

**Status**: [Open] — requires detailed nuclear structure calculation

---

## Proposed Hypothesis: H-N48-01c [P]

### Statement
> The d(n) preference applies only among decay channels that are NOT strongly hindered by spin-parity selection rules.

### Formal Rule
```
For branchpoint with channels {α, β⁻}:

1. Classify each channel:
   - "Favored": ΔJ ≤ 2, no parity change
   - "Allowed": ΔJ ≤ 2, with parity change (first-forbidden for β)
   - "Hindered": ΔJ > 2 or high-L requirement for α

2. Apply d(n) preference:
   IF both channels are "Favored" or "Allowed":
       Prefer channel with smaller d(n)_daughter
   ELSE:
       Channel classification dominates; d(n) is secondary
```

### Corollary
When nuclear structure strongly favors one channel, neither d(n) nor Q-value alone can override the selection rules.

---

## Falsification Tests for H-N48-01c

### Test 1: Find branchpoint where both channels are "Favored"
**Prediction**: d(n) should correctly predict the dominant channel
**Required data**: Branchpoint with ΔJ ≤ 2 and no parity change for both α and β⁻
**Status**: No such case identified in the three mandatory branchpoints

### Test 2: Find branchpoint where d(n) and selection rules conflict
**Prediction**: Selection rules should dominate
**Example**: ²¹²Bi (α is hindered, β is allowed → β dominates despite d(n))
**Status**: ✓ Confirmed

### Test 3: Quantitative hindrance factors
**Prediction**: If hindrance factor H can be computed, then:
```
Observed BR ∝ (phase space) × (barrier penetration) / H
```
**Required data**: Hindrance factors from α-spectroscopy
**Status**: Not computed in V7.1

---

## Conclusions

1. **Selection rules explain ²¹²Bi**: The ΔJ = 4 requirement for α makes β more accessible despite lower Q.

2. **Selection rules do NOT explain ²²⁷Ac**: The α-decay is spin-parity favored, yet β dominates. This is a nuclear structure anomaly.

3. **H-N48-01c is partially supported**: Selection rules improve branching prediction from 1/3 to 2/3, but the ²²⁷Ac case remains unexplained.

4. **d(n) remains secondary**: Even with selection-rule gating, d(n) does not provide additional predictive power beyond the already-considered factors.

