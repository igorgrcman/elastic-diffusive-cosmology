# P-Isotropy Ledger Update

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Test performed:** Prove-or-fail for P-isotropy [P] → [Dc]
**Result:** FAIL — P-isotropy remains [P]

---

## 1. Test Summary

| Item | Detail |
|------|--------|
| **Postulate tested** | P-isotropy: "The Plenum has no preferred internal direction" |
| **Current status** | [P] (primitive postulate) |
| **Target status** | [Dc] (derived conditional on P-local-vertex) |
| **Derivation route** | Action symmetry + P-local-vertex (Ruta A) |
| **Outcome** | **FAIL** |

---

## 2. Checkpoint Results

| # | Checkpoint | Result | Detail |
|---|-----------|--------|--------|
| 1 | Reduction S[h] → S_eff[θ] | **PASS** (caveat) | Ansatz via EFT reasoning; form of permitted terms analyzable from symmetry |
| 2 | SU(2) left action transitivity | **PASS** | Left action transitive; M11 applies (left-invariant functions are constant) |
| 3 | Background reference from ξ | **FAIL** | Hopf S¹ fiber ≡ compact ξ provides preferred U(1) ⊂ SU(2) in each fiber |

---

## 3. Failure Mode

**The Hopf fibration S¹ → S³ → S² identifies the compact dimension ξ with
a preferred U(1) subgroup within each S³ fiber.**

Source: Book II Ch. 2 (`chapter_02_ontology.tex`, lines 215–236):
- "The S¹ fiber is the internal phase (related to U(1) gauge freedom)"
- This identification is load-bearing for fermion spin statistics

**Consequence:** The effective action S_eff[θ] can contain terms that are
U(1)-invariant but NOT SU(2)-invariant. P-local-vertex does not exclude this
because it only addresses inter-fiber holonomy, not within-fiber structure.

---

## 4. Current P-Isotropy Status

$$
\boxed{\text{P-isotropy: [P] — UNCHANGED}}
$$

The 6π⁵ derivation chain retains 4 core postulates:

| # | Postulate | Status | Change |
|---|-----------|--------|--------|
| 1 | P-σ | [P] | — |
| 2 | P-local-vertex | [P] | — |
| 3 | P-common-origin | [P] | — |
| 4 | P-isotropy | [P] | Tested, FAIL |

---

## 5. What Would Change This Status

P-isotropy could potentially be decomposed into two sub-claims:

| Sub-claim | Content | Potentially derivable? |
|-----------|---------|----------------------|
| U(1) phase invariance | ε(θ) does not depend on the Hopf S¹ phase | Possibly — if S¹ phase is pure gauge with no physical coupling to energy |
| S² direction invariance | ε(θ) does not depend on the spin direction n̂ ∈ S² | Possibly — if the spatial embedding of the flux tube is rotationally symmetric |

If both sub-claims can be independently established, P-isotropy becomes [Dc].
This is a potential future research direction but requires explicit derivation
of each sub-claim, not just plausibility.

---

## 6. Relation to Existing Derivation Program

The v9 derivation (`EDC_SU2_SYM_From_Action_v1.md`) derives P-SU2-sym FROM
P-isotropy. That derivation remains valid — but it is conditional on P-isotropy,
which this test shows cannot itself be derived from the action + P-local-vertex.

The v11 "ALL GAPS CLOSED" claim (already classified as Type 1 local closure in
`P_EPSILON_V11_AUDIT.md`) is unaffected — it never claimed P-isotropy was
derived, only that it was one of the 4 accepted core postulates.

---

## 7. Bottom Line

P-isotropy remains [P]. The prove-or-fail test identified a precise obstruction:
the Hopf fibration embeds the compact dimension ξ into each S³ fiber, providing
a background reference direction that the action symmetry + P-local-vertex
argument cannot eliminate. This is a clean negative result with a well-defined
failure mode. The 6π⁵ derivation chain retains 4 core postulates.
