# SUMMARY AND NEXT ACTIONS (V7.1)

**Created**: 2026-01-31
**Purpose**: Consolidate V7.1 findings and prioritize next steps

---

## What Passed

1. **α17 Dataset Construction**: Successfully built 17-nuclide dataset with full BL provenance from NNDC/NuDat. Coverage constraints largely met (minor gaps in high-Qα bin).

2. **Baseline G-N Fit**: Classic Geiger-Nuttall law achieves R² = 0.987. This is the expected excellent fit for the well-established empirical relationship.

3. **d(n) Mapping**: Computed n(A) and d(n) for all 17 nuclides using model M-A (c = 6.1). Range spans d = 0.2 to 2.1, providing reasonable dynamic range.

4. **Selection Rule Analysis (2/3)**: Spin-parity selection rules explain ²¹²Bi and ²¹¹Bi branchpoint outcomes. This improves on d(n) alone (1/3).

---

## What Failed

1. **d(n) Branching Prediction**: H-N48-01 remains falsified (1/3). Adding selection rules (H-N48-01c) helps but does not fully resolve all cases.

2. **²²⁷Ac Anomaly**: Neither d(n), Q-values, nor simple selection rules explain why β⁻ dominates despite favored α-decay. This remains an open nuclear structure puzzle.

3. **High-Qα Coverage**: Unable to populate the Qα > 8 MeV bin adequately (only 1/5 required). This is a BL limitation, not a methodological failure.

---

## What Is Ambiguous

1. **Residual ~ d(n) Correlation**:
   - Pearson r = -0.47 (p = 0.056) — borderline significant
   - Direction is consistent with "frustrated nuclei decay faster"
   - Cannot claim definitive d(n) effect with current sample size

2. **G-N + d(n) Augmented Model**:
   - g = -0.72 ± 0.40 (p = 0.093) — not significant at α = 0.05
   - ΔAIC = -1.5 — weak evidence favoring augmented model
   - Verdict: **Suggestive but inconclusive**

3. **Crystal-Nucleus Analogy**:
   - Provides vocabulary and geometric intuition
   - Falsifiable predictions proposed but not yet tested
   - Status: Conceptual tool, not predictive model

---

## Does Residual ~ d(n) Have Any Signal?

**Answer**: Maybe.

The weak negative correlation (r = -0.47) suggests that nuclei with larger d(n) (more topologically frustrated) tend to decay faster than G-N predicts. However:

- Effect size is small (~4% additional variance explained)
- Statistical significance is marginal (p = 0.056)
- Sample size (N = 17) limits power to detect real effects

**Conservative Interpretation**: There may be a small d(n) effect on half-lives, but it is dwarfed by the dominant Z/√Qα (Coulomb barrier) term. With current data, we cannot distinguish a real effect from statistical noise.

---

## Does H-N48-01c Look Promising?

**Answer**: Partially.

The spin-parity conditional rule improves branching prediction from 1/3 to 2/3:

| Hypothesis | Score |
|------------|-------|
| H-N48-01 (d(n) only) | 1/3 |
| H-N48-01b (+Q threshold) | 1/3 |
| H-N48-01c (+selection rules) | 2/3 |

However:
- ²²⁷Ac remains unexplained (α should win by all criteria but doesn't)
- The "rule" is becoming ad hoc — adding exceptions to save the hypothesis
- No independent predictive power demonstrated

**Verdict**: H-N48-01c is worth documenting but should not be promoted as a validated model.

---

## What Data Expansion Would Most Increase Statistical Power?

### Option A: Expand to α30 Dataset
- Add 13 more α-emitters with good BL data
- Target: Fill the Qα 6.5-8.0 MeV bin
- Expected benefit: Pearson test power would increase from ~60% to ~85%

### Option B: Include Hindered α-Decays
- Add nuclides with ΔJ > 2 for α-decay (where hindrance factors are known)
- Would allow testing whether d(n) correlates with hindrance-corrected rates
- Requires hindrance factor compilation

### Option C: Superheavy Element Data
- Add any SHE with measured t₁/₂ and Qα
- Would extend d(n) range beyond 2.0
- Limited by experimental availability

**Recommendation**: Option A (α30) provides best cost-benefit. Focus on well-measured Po/At/Bi region nuclides with Qα in the 6.5-8 MeV gap.

---

## Specific Next Actions

### Priority 1: Close ²²⁷Ac Anomaly
- Consult nuclear structure literature for ²²⁷Ac ground state configuration
- Check if there are known matrix element enhancements for the β-transition
- Status: [Open] → [Documented] or [Explained]

### Priority 2: Expand Dataset
- Identify 10-15 additional α-emitters with:
  - Qα in 6.5-8.0 MeV range
  - Well-measured t₁/₂ (< 10% uncertainty)
  - Available in NUBASE2020/AME2020
- Target nuclides: ²¹⁵Po, ²¹⁹Rn, ²²³Ra, ²¹⁵At, ²¹⁹At, etc.

### Priority 3: Test Crystal-Nucleus Predictions
- Query NUBASE2020 for isomer counts in A = 260-270, 290-300, 320-330 ranges
- Compute isomer density per mass unit
- Test prediction that A ≈ 294 shows enhancement

### Priority 4: Archive and Merge
- Commit V7.1 files to repository
- Update hypothesis ledger in V7 with V7.1 findings
- Prepare draft section for Book 2 integration

---

## Hypothesis Status After V7.1

| Hypothesis | V7 Status | V7.1 Status | Change |
|------------|-----------|-------------|--------|
| H-N48-01 | Partially Falsified | Partially Falsified | — |
| H-N48-01b | Falsified | Falsified | — |
| H-N48-01c | [P] NEW | [P] Partial (2/3) | Tested |
| H-N48-02 (chain trajectory) | [I] Confirmed | [I] Confirmed | — |
| H-N48-03 (endpoints) | [I] Confirmed | [I] Confirmed | — |
| G-N + d(n) | BLOCKED | INCONCLUSIVE | Tested |

---

## Key Takeaways

1. **d(n) is NOT a strong predictor**: Neither for branching (1/3) nor for half-life deviations (p > 0.05).

2. **Nuclear structure dominates**: Spin-parity selection rules and matrix elements are more important than topological coordination.

3. **The analogy has limits**: The crystal-nucleus mapping provides conceptual tools but not quantitative predictions.

4. **More data could resolve ambiguity**: The suggestive but insignificant correlation needs larger N to confirm or reject.

---

## Final Verdict

**V7.1 Outcome**: The G-N + d(n) test is no longer BLOCKED but is now **INCONCLUSIVE**.

- There is a weak signal in the expected direction
- Statistical power is insufficient to confirm or reject
- Expanding to α30 would likely resolve the ambiguity

**Recommendation for Book 2**: Present d(n) as a descriptive quantity (chain trajectories) rather than a predictive one (branching or half-lives). Acknowledge the V7/V7.1 falsification results explicitly.

