# P-Isotropy Prove-or-Fail Test

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Test:** Can P-isotropy be promoted from [P] to [Dc] via action symmetry + P-local-vertex?
**Result:** **FAIL — P-isotropy remains [P]**

---

## Executive Summary

P-isotropy ("the Plenum has no preferred internal direction") **cannot** be promoted
from [P] to [Dc] using the available resources (membrane action + P-local-vertex).

**Failure mode:** The Hopf fibration S¹ → S³ → S², which is part of the canonical
EDC structure (Book II Ch. 2), identifies the compact dimension ξ ∈ S¹ with a
preferred U(1) subgroup within each S³ fiber. This provides a background reference
direction in S³ that is independent of holonomy between fibers. P-local-vertex
does not exclude this within-fiber preferred direction.

**Checkpoint results:**
- Checkpoint 1 (Reduction mechanism): **PASS with caveat** — ansatz, not derivation
- Checkpoint 2 (SU(2) action type): **PASS** — left action, transitive
- Checkpoint 3 (Background reference field from ξ): **FAIL** — Hopf S¹ fiber
  provides a preferred direction

**Consequence:** The 6π⁵ derivation chain retains 4 core postulates.
P-isotropy cannot be reduced to a derived consequence of the other three.

---

## Checkpoint 1 — Reduction Mechanism

### Question

How does the membrane action S = σ∫√(1+|∇h|²) reduce to an effective action
S_eff[θ₁, θ₂, θ₃] on the configuration space Q = (S³)³?

### Analysis

The membrane action is a functional of h(x), the membrane height field. The
internal orientations θᵢ ∈ S³ are additional degrees of freedom describing the
state of each flux tube at the Y-junction. These are *not* directly contained
in h(x) — they describe the internal structure of the topological defect, not
the membrane profile.

The effective action S_eff[θ₁, θ₂, θ₃] would arise from integrating out the
membrane field h(x) while holding the flux tube orientations fixed:

$$
e^{-S_{\text{eff}}[\theta_1, \theta_2, \theta_3]} = \int \mathcal{D}h \; e^{-S[h] / \hbar}
\Big|_{\text{flux tube orientations fixed at } \theta_i}
$$

This is standard effective field theory reasoning: integrate out fast/heavy
degrees of freedom to get an effective action for slow/light degrees of freedom.

### Assessment

**The reduction is an ANSATZ, not a derivation.**

- The existence of an effective action S_eff[θ] is physically motivated
  (standard EFT) but has not been formally derived from the membrane action
- The precise form of S_eff[θ] — which terms it contains, what their
  coefficients are — is not determined
- The key question for the isotropy test is: what terms CAN appear in S_eff[θ]?
  This is answerable even without performing the full reduction

### Verdict: **PASS (with caveat: ansatz, not derivation)**

The checkpoint passes because the question "what terms can S_eff[θ] contain?"
can be answered from symmetry considerations alone, even though the full
reduction is not performed. The ansatz status is noted and does not invalidate
the subsequent analysis.

---

## Checkpoint 2 — SU(2) Action Type and Transitivity

### Question

Which SU(2) action is relevant? Is it transitive? Does M11 apply?

### Analysis

**Relevant action: LEFT multiplication.**

Each θᵢ ∈ SU(2) ≅ S³ is a group element. The left action is:

$$
\theta \mapsto g \cdot \theta \quad \text{for } g \in \text{SU}(2)
$$

**Transitivity:** For any θ₁, θ₂ ∈ SU(2), the element g = θ₂ · θ₁⁻¹ sends
θ₁ → θ₂. Therefore the left action is transitive.

**M11:** A function f: SU(2) → ℝ that is invariant under left multiplication
(f(g·θ) = f(θ) for all g) must be constant. This follows directly from
transitivity: the orbit of any point under left-SU(2) is all of SU(2).

**Distinction from other actions:**
- **Right action** θ → θ·g: also transitive, also gives M11
- **Adjoint action** θ → g·θ·g⁻¹: NOT transitive (orbits are conjugacy
  classes, which are 2-spheres labeled by trace). Adjoint-invariant functions
  are functions of Tr(θ), which are NOT constant.

**Which action does the physics respect?**

A function ε(θ) can depend on θ only if there exists a **reference element**
h ∈ SU(2) against which θ can be compared. With such an h, one can form:
- Tr(h⁻¹θ) — invariant under simultaneous left action on h and θ, but depends
  on the relative orientation h⁻¹θ
- More generally, any function of the invariant h⁻¹θ

Without a reference element, the only available invariants are those under
left multiplication, which are constant by M11.

**The critical question becomes: does the physical setup provide a reference
element h ∈ SU(2) within each fiber?** This is Checkpoint 3.

### Verdict: **PASS**

Left action is transitive on SU(2). M11 applies: left-invariant functions are
constant. The argument proceeds cleanly to Checkpoint 3.

---

## Checkpoint 3 — Background Reference Field from ξ

### Question

Does the compactification of ξ ∈ S¹ introduce a background reference direction
in S³, independently of inter-fiber holonomy?

### Analysis

**The Hopf fibration is the key structure.**

Book II Ch. 2 (chapter_02_ontology.tex, lines 215–236) establishes:

> "Internal phase ψ ∈ S³ describes full 5D orientation"
> "The S¹ fiber is the internal phase (related to U(1) gauge freedom)"

The canonical EDC structure includes the Hopf fibration:

$$
S^1 \longrightarrow S^3 \longrightarrow S^2
$$

where:
- S³ is the full internal orientation space of each flux tube
- S² is the observed angular momentum (spin direction)
- S¹ is the internal phase — **explicitly identified with U(1) gauge freedom**

**The compact dimension ξ ∈ S¹ is structurally identified with the Hopf fiber.**

This identification is not incidental — it is part of the canonical EDC physical
picture. The compact dimension provides the "hidden" S¹ phase that explains why
fermions require 720° rotation (they carry the full S³ structure, not just S²).

**Consequence for isotropy:**

The Hopf fibration selects a preferred U(1) ⊂ SU(2) — the maximal torus.
In matrix form:

$$
U(1) = \left\{ \begin{pmatrix} e^{i\phi} & 0 \\ 0 & e^{-i\phi} \end{pmatrix} : \phi \in [0, 2\pi) \right\} \subset \text{SU}(2)
$$

This U(1) is the "ξ direction" within SU(2). It distinguishes the Hopf fiber
direction from the transverse directions in the S³.

**This provides a background reference direction in S³:**

With the Hopf fibration, each θ ∈ SU(2) can be decomposed as:
- A base point on S² (the observed spin direction)
- A phase φ ∈ S¹ (the internal phase along ξ)

The effective action S_eff[θ] can now contain terms that depend on the base
point on S², which are NOT left-SU(2)-invariant. For example:

$$
\varepsilon(\theta) = f(\hat{n}(\theta))
$$

where n̂(θ) ∈ S² is the base point under the Hopf projection π: S³ → S².
Such a function is U(1)-invariant (invariant under Hopf fiber rotations) but
NOT SU(2)-invariant.

**Does P-local-vertex exclude this?**

**No.** P-local-vertex states there is no holonomy between fibers — no parallel
transport connecting θᵢ in fiber i to θⱼ in fiber j. This excludes inter-fiber
coupling terms like Tr(θᵢ⁻¹ U_ij θⱼ).

But P-local-vertex says nothing about within-fiber structure. Each fiber
independently has its own Hopf fibration, its own preferred U(1) direction from
the compact ξ, and its own potential for U(1)-invariant-but-not-SU(2)-invariant
terms in the effective action.

**Could additional arguments rescue the derivation?**

1. **Physical decoupling:** If the Hopf S¹ phase is physically decoupled from
   the energy density (e.g., if it is a pure gauge artifact with no physical
   consequence), then the effective energy would depend only on the S² base
   point, not on the S¹ phase. But this would give U(1) invariance, not full
   SU(2) invariance. The energy density ε(θ) could still depend on the spin
   direction n̂ ∈ S².

2. **Rotational symmetry of the embedding:** If the flux tube's embedding in
   3+1 spatial dimensions is rotationally symmetric, then no spatial direction
   singles out a preferred point on S². This would give ε(θ) = const. But this
   is a new physical assumption about the embedding — effectively a different
   form of the isotropy postulate, not a derivation of it.

3. **Vacuum averaging:** If the Plenum vacuum averages over all possible ξ
   embeddings, the preferred direction washes out. But this is equivalent to
   postulating isotropy, not deriving it.

**None of these rescue routes derive P-isotropy from the action + P-local-vertex
alone. Each introduces a new physical assumption that is equivalent to or
weaker than P-isotropy itself.**

### Verdict: **FAIL**

The Hopf fibration, which is part of the canonical EDC structure, provides a
natural embedding S¹ → S³ that selects a preferred U(1) ⊂ SU(2) within each
fiber. This background reference direction exists independently of inter-fiber
holonomy and is therefore not excluded by P-local-vertex. The effective action
S_eff[θ] can contain U(1)-invariant but SU(2)-breaking terms.

P-isotropy cannot be derived from the action + P-local-vertex.

---

## Conclusion

### Final Status

$$
\boxed{\text{P-isotropy: remains [P] — cannot be promoted to [Dc]}}
$$

### Checkpoint Summary

| Checkpoint | Question | Result | Detail |
|-----------|----------|--------|--------|
| 1 | Reduction mechanism | **PASS** (caveat) | Ansatz via standard EFT, not formal derivation |
| 2 | SU(2) action type | **PASS** | Left action, transitive, M11 applies |
| 3 | Background reference from ξ | **FAIL** | Hopf S¹ fiber = compact ξ → preferred U(1) ⊂ SU(2) |

### Failure Mode

**The Hopf fibration S¹ → S³ → S² identifies the compact dimension ξ with a
preferred direction in each S³ fiber.**

This is not a minor technicality — it is a structural feature of the canonical
EDC framework (Book II Ch. 2). The identification of the S¹ Hopf fiber with
the U(1) gauge freedom from ξ compactification is load-bearing: it explains
fermion spin statistics (720° rotation) and the S³ → S² projection.

Because this preferred direction exists within each fiber independently,
P-local-vertex (which only excludes inter-fiber holonomy) cannot eliminate it.

### What Would Be Needed to Close the Argument

To promote P-isotropy to [Dc], one would need to show one of:

1. **The Hopf S¹ direction is physically inert:** The preferred U(1) from ξ
   does not couple to the energy density ε(θ). This would give U(1) invariance,
   but to get full SU(2) invariance one additionally needs:

2. **The S² base point is also inert:** No physical mechanism selects a preferred
   direction on S² for a single flux tube. This is a rotational symmetry
   argument about the spatial embedding — plausible but currently unproven.

3. **Combined:** If both (1) and (2) hold, then ε(θ) cannot depend on either
   the S¹ phase or the S² direction, forcing ε(θ) = const. But this would be
   a two-step argument with each step requiring independent justification.

Alternatively, one could:

4. **Replace P-isotropy with a weaker postulate:** If U(1) invariance (from the
   Hopf fiber) can be shown to follow from the action, and S² isotropy can be
   shown from the spatial embedding, then P-isotropy would become a theorem
   rather than a postulate — but this is a different derivation program from
   what was tested here.

### What This Result Means for 6π⁵

The 6π⁵ derivation chain retains 4 core postulates. P-isotropy cannot be
reduced to a derived consequence of the other three (P-σ, P-local-vertex,
P-common-origin). The postulate count remains:

| # | Postulate | Status | This test |
|---|-----------|--------|-----------|
| 1 | P-σ (large membrane tension) | [P] | Unchanged |
| 2 | P-local-vertex (no holonomy at junction) | [P] | Used but insufficient |
| 3 | P-common-origin (τ = σa, L = a) | [P] | Not relevant |
| 4 | **P-isotropy (no preferred internal direction)** | **[P]** | **Tested, FAIL** |

### Value of This Negative Result

This is a **bounded no-go result**, not a dead end. It identifies:

1. **The precise obstruction:** Hopf S¹ ↔ compact ξ identification
2. **The maximal achievable symmetry:** U(1) invariance (from gauge freedom)
   may be derivable; full SU(2) invariance requires additional input
3. **A potential decomposition:** P-isotropy might be decomposable into
   "U(1) phase invariance" (possibly derivable) + "S² direction invariance"
   (requires spatial embedding argument)
4. **A consistency check:** If future work derives ε(θ) = const by other means,
   it must explain why the Hopf-preferred direction does not contribute

---

## Files and Sources Consulted

| File | Location | Relevance |
|------|----------|-----------|
| `EDC_SU2_SYM_From_Action_v1.md` | `edc_papers/paper_2/supplementary/derivations/` | Existing P-isotropy → P-SU2-sym derivation (v9) |
| `chapter_02_ontology.tex` | `edc_book_2/reorganized/part1/` | Hopf fibration S³ → S² with S¹ fiber ↔ U(1) gauge (lines 215–236) |
| `chapter_04_z6_program.tex` | `edc_book_2/reorganized/part1/` | Z₆ lattice structure (spatial, not fiber — correctly distinguished) |
| `P_EPSILON_V11_AUDIT.md` | `edc_book_4/audit/` | Context on P-isotropy role in derivation chain |
| `FAILURE_CERTIFICATE_v10.md` | `EDC_Research_PRIVATE/derivations/analytic/` | v10 derivation chain with P-isotropy as primitive |
| `DERIVATION_LEDGER_v11.md` | `EDC_Research_PRIVATE/derivations/analytic/` | Full dependency graph showing P-isotropy as root |
