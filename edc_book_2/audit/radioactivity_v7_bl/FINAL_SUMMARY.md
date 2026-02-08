# FINAL SUMMARY (V7)

**Created**: 2026-01-31
**Purpose**: Conclusions from BL-grounded testing of M-topology radioactivity hypotheses
**Status**: COMPLETE

---

## What Was Confirmed

### 1. Chain Trajectory Follows d(n) Gradient [I]

All three canonical decay chains show monotonic decrease in coordination distance:

| Chain | d(start) → d(end) | Confirmed |
|-------|-------------------|-----------|
| U-238 | 1.81 → 0.03 | ✓ |
| Th-232 | 1.48 → 0.14 | ✓ |
| U-235 | 1.65 → 0.09 | ✓ |

**Confidence**: High (3/3 chains, no exceptions)

### 2. Stable Endpoints at Allowed Coordination [I]

All three stable Pb isotopes terminate at d(n) ≈ 0:

| Isotope | d(n) |
|---------|------|
| ²⁰⁶Pb | 0.03 |
| ²⁰⁷Pb | 0.09 |
| ²⁰⁸Pb | 0.14 |

**Confidence**: High (inherent to calibration, but consistent)

### 3. Forbidden Zone [37-47] Is Real [Der]

The interval [37, 47] contains no allowed coordination values. Heavy nuclei (A ≈ 220-350) occupy this zone and must decay to exit it.

**Confidence**: Mathematical certainty (follows from S = {2^a × 3^b})

---

## What Failed

### 1. H-N48-01: d(n) Branching Prediction [P → Partially Falsified]

**Hypothesis**: Preferred decay channel minimizes d(n) of daughter.

**Score**: 1/3 = 33% on mandatory branchpoints

| Branchpoint | Prediction | Observation | Result |
|-------------|------------|-------------|--------|
| ²¹²Bi | α | β⁻ (64%) | ✗ FAIL |
| ²²⁷Ac | α | β⁻ (99%) | ✗ FAIL |
| ²¹¹Bi | α | α (99.7%) | ✓ SUCCESS |

**Verdict**: d(n) does NOT reliably predict branching.

### 2. H-N48-01b: Q-Threshold Gating [P → Falsified]

**Hypothesis**: d(n) applies only when Q > Q_threshold.

**Result**: Cannot explain ²²⁷Ac (Q_α = 5042 keV >> Q_β = 45 keV, yet β⁻ = 98.6%)

**Verdict**: Q-threshold does not rescue H-N48-01.

### 3. G-N + d(n) Half-Life Correlation [P → Blocked]

**Attempt**: Test if d(n) explains residuals from Geiger-Nuttall law.

**Result**: Insufficient data (only 6 α-emitters with complete BL data, narrow d(n) range).

**Verdict**: Cannot test with current dataset.

---

## What Remains Open

### Top 5 Open Questions (OQ-V7)

| ID | Question | Data Needed | Priority |
|----|----------|-------------|----------|
| OQ-V7-01 | Does spin-parity condition enable d(n) branching? | Jπ for all branchpoints | High |
| OQ-V7-02 | Does d(n) correlate with G-N residuals? | 15+ α-emitters | High |
| OQ-V7-03 | Is n=48 the target for A > 350? | SHE decay chains | Medium |
| OQ-V7-04 | Do isomers have different effective n? | Isomer branching data | Low |
| OQ-V7-05 | Does nuclear deformation affect d(n)? | Deformation correlations | Low |

### Proposed Revision: H-N48-01c [P]

A conditional hypothesis that may rescue d(n) relevance:

```
Condition 1: |Q_α - Q_β| / max(Q_α, Q_β) < 0.5
Condition 2: ΔJ ≤ 2, parity change allowed for both channels
If Conditions 1 AND 2: Apply d(n) preference
Else: Nuclear structure dominates
```

**Status**: Untested — requires spin-parity data

---

## Key Insights

### 1. d(n) Describes Trajectory, Not Mechanism

The coordination distance describes *where* decay chains go (toward d=0) but not *how* individual steps are chosen. This is analogous to:

- Thermodynamics vs. kinetics
- Free energy landscape vs. reaction pathway
- Potential gradient vs. transition state

### 2. Nuclear Structure Trumps Topology

At branchpoints, factors like spin-parity selection rules and matrix elements dominate. The ²²⁷Ac case is decisive:

- Q_α exceeds Q_β by 100×
- d(n) favors α
- Yet β⁻ = 98.6%

**Explanation**: The Gamow-Teller β transition ²²⁷Ac → ²²⁷Th is "allowed" (ΔJ=1, parity change), overwhelming all other factors.

### 3. The Crystal Analogy Has Limits

While the crystal-nucleus analogy provides vocabulary (coordination, frustration, domains), it does not yield quantitative predictions. The analogy is conceptual, not predictive.

---

## What Single Next Step Would Most Increase Confidence?

### Recommendation: Build G-N Correlation Dataset

**Action**: Compile 15-20 α-emitters with:
- Wide range in A (hence wide range in d(n))
- Precise Q_α from AME2020
- Precise t₁/₂ from NUBASE2020
- Exclude branchpoint complications

**Rationale**: This allows testing whether d(n) appears in half-life deviations from the Geiger-Nuttall law, which is a *quantitative* test independent of branching.

**Expected Outcome**:
- If d(n) correlates with G-N residuals → some predictive value remains
- If no correlation → d(n) is purely descriptive (chain trajectory only)

### Alternative: Spin-Parity Verification

**Action**: Verify Jπ assignments for ²¹²Bi and ²¹¹Bi branchpoints.

**Rationale**: This would test H-N48-01c and determine if spin-parity conditioning rescues d(n) branching relevance.

---

## Status of All Hypotheses After V7

| Hypothesis | Before V7 | After V7 | Score |
|------------|-----------|----------|-------|
| H-N48-01 | [P] | Partially Falsified | 1/3 |
| H-N48-01b | [P] | Falsified | 0/3 |
| H-N48-01c | — | [P] NEW | Untested |
| H-N48-02 | [P] | [I] Confirmed | 3/3 |
| H-N48-03 | [P] | [I] Confirmed | 3/3 |
| H-N48-04 | [P] | [P] Untested | — |
| H-N48-05 | [P] | [P] Untested | — |

---

## Falsification Tests Completed

| Test ID | Description | Result |
|---------|-------------|--------|
| TEST-N48-08 | d(n) predicts branching | ✗ Failed (1/3) |
| TEST-BL-01 | Q-threshold rescues d(n) | ✗ Failed |
| TEST-BL-02 | Chain d(n) monotonicity | ✓ Passed (3/3) |
| TEST-BL-03 | Endpoint at allowed n | ✓ Passed (3/3) |
| TEST-BL-04 | d(n) + G-N correlation | ⊘ Blocked (data) |

---

## Final Verdict

The V7 BL audit achieved its primary goal: **convert philosophy to testable claims and test them**.

**Main Results**:
1. d(n) chain trajectory: **CONFIRMED**
2. d(n) branching prediction: **PARTIALLY FALSIFIED**
3. Crystal analogy: **CONCEPTUAL ONLY** (not predictive)

**Implication for EDC Theory**: The M-topology coordination law applies to nuclear structure in a *qualitative* sense (chains flow toward allowed n) but does not control *quantitative* decay properties (branching ratios, half-lives).

**Implication for Book 2**: Present d(n) as a trajectory descriptor, not a branching predictor. Acknowledge the V7 falsification result explicitly.

---

## End of V7 Audit

All deliverables complete. Audit closed 2026-01-31.

