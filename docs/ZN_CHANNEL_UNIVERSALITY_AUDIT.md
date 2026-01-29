# Z_N Correction Channel — Universality Audit

**Date:** 2026-01-29
**Status:** Audit Complete
**Purpose:** Determine if k(N) = 1 + 1/N applies universally across EDC sectors
**Anchor:** `docs/ZN_CORRECTION_CHANNEL.md`

---

## A. Executive Summary (6 Bullets)

1. **k(6) = 7/6 has PARTIAL support** — applies to 2 of 4 audited channels
2. **Strong APPLY channels:** N_cell renormalization (12→10), Pion splitting (r_π/4α ≈ 7/6)
3. **Control channel confirms exclusion:** sin²θ_W = 1/4 uses cardinality ratio, not averaging (DOES-NOT-APPLY)
4. **Inconclusive channel:** Δm_np ε-dressing has speculative k connection ([P] status)
5. **Universality verdict: PARTIAL** — k applies to averaging processes, NOT to all Z₆-derived quantities
6. **Recommended discriminator:** Test Δm_np ε = 14α/15 hypothesis (cheap numerical check)

---

## B. Definition Recap

### B.1 Mathematical Framework [Der]

**Source:** `edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex`

For test function f(θ) = c + a cos(Nθ) with Z_N symmetry:
```
Discrete average:  <f>_disc = c + a     (samples at corners where cos(Nθ) = 1)
Continuum average: <f>_cont = c         (cos term integrates to 0)
Ratio: R = 1 + a/c
```

### B.2 Physical Normalization [Dc]

**Equal Corner Share Hypothesis:**
```
a/c = 1/N   (corner excess = 1/N of mean)
```

This is NOT derived from the 5D action — it's a hypothesis about how Z_N anisotropy manifests.

### B.3 Combined Result [Der]+[Dc]

```
k(N) = 1 + 1/N
```

For Z₆: k(6) = 7/6 = 1.1667

### B.4 Current Canonical Usage

| Usage | Document | Equation |
|-------|----------|----------|
| N_cell 12→10 | `docs/BREADTH_SYNTHESIS_2026-01-29.md` Section D.3 | N_cell_eff = 12 / k(6) = 10.29 |
| Pion observation | `docs/PION_SPLITTING_EPSILON_CHECK.md` Section D.3 | r_π / (4α) = 1.166 ≈ 7/6 |

---

## C. Channel-by-Channel Audit

### Table Summary

| Channel | Observable | Where Would k Enter? | Evidence in Repo | Verdict | Notes |
|---------|------------|---------------------|------------------|---------|-------|
| N_cell renormalization | 12 → 10 | N_cell_eff = N_cell_bare / k(6) | BREADTH_SYNTHESIS D.3, ncell_renorm_box.tex | **APPLY** | Explains τ_n uses 10 not 12 |
| Pion splitting | r_π / (4α) = 1.166 | Δm_π = k × 4α × m_π0 | PION_SPLITTING_EPSILON_CHECK.md D.3 | **APPLY** | Original observation (0.07% match) |
| Δm_np reconciliation | ε = 0.679% | ε_eff = ε_bare × k(6)? | ZN_CORRECTION_CHANNEL.md C.2 | **UNCLEAR** | Speculative: ε_bare = 4α/5 → ε = 14α/15 |
| sin²θ_W = 1/4 | Weinberg angle | NOWHERE | FLAVOR_SKELETON_v0.1.md B | **DOES-NOT-APPLY** | Cardinality ratio, not averaging |

---

## D. Channel Details

### D.1 N_cell Renormalization (12 → 10)

**Verdict: APPLY**

**Document anchors:**
- Algebraic bridge: `docs/OP-SIGMA-2_NCELL12_RESOLUTION.md`
- k(6) derivation: `docs/Z6_CORRECTION_FACTOR_7over6.md`
- Synthesis: `docs/BREADTH_SYNTHESIS_2026-01-29.md` Section D.3
- LaTeX box: `edc_papers/_shared/boxes/ncell_renorm_box.tex`

**Minimal equation where k enters:**
```
N_cell_bare = 12        (from E_σ / σr_e² algebraic bridge)
k(6) = 7/6              (discrete averaging correction)
N_cell_eff = 12 / k(6) = 12 × (6/7) = 10.29 ≈ 10
```

**Why k applies:**
- N_cell relates geometric (bare) counting to dynamical (effective) counting
- The discrete-to-continuum correction naturally arises when counting cells on a Z₆ ring
- τ_n calculation "sees" the effective count (10), not the bare count (12)

**Status:** YELLOW — math is [Der], physical interpretation is [Dc]

---

### D.2 Pion Splitting ε-Check

**Verdict: APPLY**

**Document anchors:**
- Main analysis: `docs/PION_SPLITTING_EPSILON_CHECK.md`
- k hypothesis: `docs/Z6_CORRECTION_FACTOR_7over6.md` Section A-B

**Minimal equation where k enters:**
```
r_π = Δm_π / m_π0 = 3.403%
4α = 2.919%
r_π / (4α) = 1.166 ≈ 7/6 = k(6)

→ Δm_π ≈ (7/6) × 4α × m_π0   [I]
```

**Why k applies:**
- This is the ORIGINAL OBSERVATION that motivated k = 7/6
- Suggests pion EM splitting carries same discrete correction as other Z₆ quantities
- Numerical match: 1.166 vs 7/6 = 1.1667 → 0.07% error

**Status:** [I] — pattern identification, not derivation

---

### D.3 Δm_np Reconciliation (Bare vs Renormalized)

**Verdict: UNCLEAR**

**Document anchors:**
- ε calculation: `docs/DELTA_MNP_RECONCILIATION.md`
- k connection hypothesis: `docs/ZN_CORRECTION_CHANNEL.md` Section C.2

**Equation where k MIGHT enter:**
```
Known: (8/π)(1 - ε) = 5/2 + 4α   where ε = 0.679%

Hypothesis: ε_eff = ε_bare × k(6)
If true: ε_bare = ε × (6/7) = 0.679% × 0.857 = 0.582%

Test: 0.582% ≈ 4α/5 = 0.584%   (0.3% match)

Candidate form: ε_bare = 4α/5, ε_dressed = (4α/5) × (7/6) = 14α/15 ≈ 0.68%
```

**Why UNCLEAR:**
- The k connection is SPECULATIVE [P], not established
- The ε = 0.679% is well-defined as a bridge number
- Whether it decomposes as (4α/5) × (7/6) is unverified
- Alternative: ε is purely an EM correction unrelated to discrete averaging

**Recommended test:**
Check if ε = 14α/15 = 0.682% matches better than ε = 0.679%.
Difference: 14α/15 - 0.679% = +0.003% → indistinguishable at current precision.

**Status:** [P] — proposed connection, needs independent evidence

---

### D.4 sin²θ_W = 1/4 (Control Channel)

**Verdict: DOES-NOT-APPLY**

**Document anchors:**
- Derivation: `docs/FLAVOR_SKELETON_v0.1.md` Section B, C.2
- Framework: Paper 3, `sections/05_three_generations.tex`

**Formula (NO k factor):**
```
sin²θ_W = |Z₂| / |Z₆| = 2/6 = 1/4   [Der]
```

**Why k does NOT apply:**

1. **Different mechanism:** sin²θ_W is a RATIO OF CARDINALITIES, not an averaging process
2. **No discrete vs continuum tension:** Both numerator and denominator are discrete counts
3. **No integral involved:** The formula is pure group theory (counting elements)
4. **k requires an averaging process:** k = 1 + 1/N arises from ⟨f⟩_disc / ⟨f⟩_cont where f has Z_N Fourier mode
5. **sin²θ_W has no Fourier mode to sample:** It's a static ratio, not a dynamical average

**This channel confirms k is NOT universal to all Z₆ quantities.**

**Status:** [Der] — fully derived, k is excluded by mechanism

---

## E. Conclusion

### E.1 Universality Assessment: PARTIAL (YELLOW)

**k(N) = 1 + 1/N is NOT universal across all Z₆-derived quantities.**

It applies ONLY to quantities arising from discrete-to-continuum averaging:
- ✅ N_cell renormalization (geometric → dynamical count)
- ✅ Pion splitting (EM correction with discrete sampling)
- ❓ Δm_np ε-dressing (speculative)

It does NOT apply to quantities from cardinality ratios:
- ❌ sin²θ_W = |Z₂|/|Z₆| (static group theory, no averaging)
- ❌ N_g = |Z₃| = 3 (direct count)

### E.2 Applicability Criterion

**k(N) applies when:**
```
Observable = ⟨O⟩_discrete / ⟨O⟩_continuum
where O has a cos(Nθ) Fourier component
```

**k(N) does NOT apply when:**
```
Observable = |G₁| / |G₂|
(cardinality ratio, no averaging)
```

### E.3 Constraint: Do Not Apply k Blindly

**CRITICAL:** k(6) = 7/6 should NOT be applied to:
- Cardinality ratios (sin²θ_W, N_g, Koide Q = 2/3)
- Phase factors (CP phase δ = 60°)
- Quantities without explicit discrete-vs-continuum structure

**k is a correction for averaging processes, not a universal Z₆ factor.**

### E.4 Next Cheap Test (Discriminator)

**Test: Δm_np ε = 14α/15 hypothesis**

**Method:**
1. Compute 14α/15 = 14 × 0.007297 / 15 = 0.006810 = 0.6810%
2. Compare to observed ε = 0.6790%
3. Difference: 0.002% (indistinguishable)

**Alternative test:** Find another channel where k would predict a specific numerical factor and check against data.

**Candidate:** If CKM Cabibbo suppression involves Z₆ averaging, predict λ_Cabibbo ≈ f × k(N) for some base factor f.

---

## F. Reference Anchors

| Document | Content |
|----------|---------|
| `docs/ZN_CORRECTION_CHANNEL.md` | k(N) = 1 + 1/N general formula |
| `docs/Z6_CORRECTION_FACTOR_7over6.md` | k(6) = 7/6 hypothesis + derivation |
| `edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex` | Mathematical derivation |
| `docs/PION_SPLITTING_EPSILON_CHECK.md` | Pion observation r_π/(4α) ≈ 7/6 |
| `docs/BREADTH_SYNTHESIS_2026-01-29.md` | N_cell renormalization |
| `docs/DELTA_MNP_RECONCILIATION.md` | ε = 0.679% bridge |
| `docs/FLAVOR_SKELETON_v0.1.md` | sin²θ_W = 1/4 (control) |

---

*This document audits universality of k(N) = 1 + 1/N across EDC sectors. Result: PARTIAL — k applies to averaging processes, not to cardinality ratios.*
