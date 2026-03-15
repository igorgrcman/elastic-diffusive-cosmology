# P-Isotropy Decomposition — Synthesis

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Program:** P-isotropy decomposition (3 prove-or-fail tests)
**Commits:** `7ad6101`, `58640bf`, `0e4d204`

---

## 1. Executive Summary

The P-isotropy decomposition program decomposed the monolithic postulate
"the Plenum has no preferred internal direction" into two independent
sub-claims, tested each, and found that one (P-U1-phase) was always
gauge-automatic while the other (P-S2-direction) is a genuine irreducible
physical assumption. The 6π⁵ postulate count remains 4 [P], but the
program precisely identified what P-isotropy actually claims: no preferred
observed spin direction for flux tube embeddings.

---

## 2. The Old Postulate

**P-isotropy [P]:** "The Plenum (5D bulk medium) has no preferred internal
direction."

This postulate was introduced in Paper 2 as the root assumption from which
SU(2)³ internal symmetry of the effective action is derived (P-isotropy →
P-SU2-sym [Dc]). It is one of 4 core postulates in the 6π⁵ = m_p/m_e
derivation chain, alongside P-σ, P-local-vertex, and P-common-origin.

**Why it was examined:** The epistemic position program aims to minimize the
number of primitive postulates and to identify which assumptions are genuinely
independent versus derivable from existing structure. P-isotropy was the
natural candidate because it operates on the internal S³ ≅ SU(2) orientation
space, which has rich geometric structure (Hopf fibration, ξ compactification,
gauge redundancy) that might partially or fully determine the claimed
invariance.

**What was problematic:** As a primitive, P-isotropy asserts invariance under
the full SU(2) group acting on S³. But the canonical EDC structure already
includes the Hopf fibration S¹ → S³ → S², which decomposes S³ into an S¹
fiber (identified with the compact ξ dimension) and an S² base (identified
with observed spin direction). These two components have fundamentally
different physical character — one is gauge-related, the other is observable —
yet the old postulate treated them as a single undifferentiated claim.

---

## 3. The Decomposition

The Hopf fibration S¹ → S³ → S² provides a canonical decomposition of the
internal orientation space into two independent components:

**P-U1-phase:** ε(θ) does not depend on the S¹ Hopf fiber phase.

Physical meaning: The energy density at the Y-junction is invariant under
rotations of the internal ξ-phase. Since the S¹ fiber IS the compact ξ
dimension, and shifts in ξ-phase are U(1) gauge transformations, this is
a statement about gauge redundancy. The absolute phase of the field
configuration in ξ is not a physical observable — only winding numbers
(topological invariants) carry physical content.

**P-S2-direction:** ε(n̂) does not depend on the S² spin direction n̂.

Physical meaning: The energy density at the Y-junction is invariant under
rotations of the observed spin direction. Since S² is what the 3D observer
measures ("observed direction t̂ ∈ S² is what we measure" — Book II Ch. 2),
this is a statement about physical rotational symmetry. No mechanism in
the Plenum selects a preferred spin direction for flux tube embeddings.

The decomposition is exhaustive: P-isotropy holds if and only if both
P-U1-phase and P-S2-direction hold. (Technically: SU(2) invariance on S³
decomposes into U(1) fiber invariance plus SO(3) base invariance under
the Hopf projection.)

---

## 4. Test Results Table

| Component | Test | Result | Failure mode / Source |
|-----------|------|--------|----------------------|
| P-isotropy (full S³) | Action symmetry + P-local-vertex → SU(2) invariance? | **FAIL** | Hopf S¹ fiber = compact ξ provides preferred U(1) ⊂ SU(2); P-local-vertex excludes inter-fiber holonomy but not within-fiber preferred direction. Commit `7ad6101`. |
| P-U1-phase (S¹ fiber) | ξ compactification + gauge principle → U(1) invariance? | **PASS → [Dc]** | Hopf S¹ = ξ-compactification U(1) = charge-quantization U(1) (canonical chain). Fiber rotation = gauge transformation → exact invariance. Z₃ locking compatible (constrains topology, not phase). Commit `58640bf`. |
| P-S2-direction (S² base) | Bulk Plenum rotational isotropy → S² invariance? | **FAIL** | Circularity: "bulk Plenum rotational isotropy" is not an independent postulate — it IS P-isotropy. P1–P6 contain no SO(3) bulk symmetry assertion. Commit `0e4d204`. |

---

## 5. Irreducible Postulate Content

**P-U1-phase was always gauge-automatic.** It follows from the structure of
ξ compactification: the S¹ fiber phase is a gauge degree of freedom, and
gauge-invariant quantities cannot depend on it. This was never genuine
postulate content — it is a structural consequence of the KK framework
that EDC already adopts. Its inclusion in the monolithic P-isotropy was
redundant.

**P-S2-direction is the irreducible physical claim.** It asserts that no
physical mechanism selects a preferred observed spin direction for flux
tube embeddings. This is a genuine symmetry assertion about the Plenum
medium's physical properties — not a gauge redundancy, not a geometric
identity, and not derivable from the existing postulate set P1–P6.

**The old P-isotropy was essentially claiming:** "no preferred spin direction
for flux tube embedding." The S³ formulation obscured this by bundling a
gauge-automatic component (S¹ phase) with a genuine physical assumption
(S² direction) into a single undifferentiated postulate.

---

## 6. What Changed

The decomposition program achieved the following:

1. **One component identified as derivable [Dc]:** P-U1-phase follows from
   ξ gauge structure. It was never independent postulate content.

2. **Irreducible content precisely identified:** P-S2-direction is the sole
   genuine physical claim within P-isotropy. The full S³ invariance assertion
   contained gauge redundancy that masked the postulate's true content.

3. **Postulate count: 4 [P] → 4 [P] (unchanged).** No postulate was
   eliminated. P-isotropy remains [P] because its irreducible component
   (P-S2-direction) cannot be derived.

4. **Monolithic postulate replaced by precise claim.** Instead of "the Plenum
   has no preferred internal direction" (which conflates gauge and physical
   content), the operative claim is now identified as "no preferred observed
   spin direction for flux tube embeddings" (purely physical, precisely
   bounded).

---

## 7. What Did Not Change

1. **The 6π⁵ derivation chain still requires 4 [P].** No postulate was
   promoted or eliminated. The derivation m_p/m_e = 6π⁵ remains conditional
   on P-σ, P-local-vertex, P-common-origin, and P-isotropy (now understood
   as P-S2-direction + gauge-automatic P-U1-phase).

2. **P-isotropy is not promoted.** It remains [P]. The fact that half its
   content is gauge-automatic does not promote the other half.

3. **The physical claim that matters is P-S2-direction.** Future work on
   reducing the postulate count must target P-S2-direction specifically —
   the S¹ fiber part is already closed.

4. **All existing derivations conditional on P-isotropy remain valid.**
   P-isotropy still holds as a postulate; the decomposition did not weaken
   or invalidate it.

---

## 8. Z₆ Lattice Tension — Open Problem

Book II Ch. 4 (`chapter_04_z6_program.tex`, line 46) establishes:

> "The 5D membrane is not isotropic — it has a preferred lattice structure."

The Z₆ = Z₃ × Z₂ crystallographic symmetry imposes discrete preferred
directions on the membrane. P-S2-direction claims no preferred S² direction
for flux tube internal orientations. These statements are potentially in
tension:

- **Z₆** constrains spatial positions and generation structure on the membrane
- **P-S2-direction** concerns internal S² orientations of individual flux tubes

These operate at different levels (spatial embedding vs. internal orientation
space) and are logically independent as currently formulated. However, the
Hopf projection maps internal S³ orientation to observed 3D spatial direction,
which means the relationship between membrane spatial anisotropy and internal
orientation isotropy is not trivially guaranteed.

**Resolution was not attempted in this program.** The decomposition program
tested derivability of P-isotropy's components, not their consistency with
Z₆. This tension is flagged as an OPR candidate for future work: explicitly
verify that Z₆ spatial anisotropy is compatible with P-S2-direction internal
orientation isotropy, or identify conditions under which they conflict.

---

## 9. What This Changes / What It Does Not Change

**For future derivation work:** Any attempt to reduce the 6π⁵ postulate count
by deriving P-isotropy should now target P-S2-direction specifically. The S¹
component is closed and need not be re-examined. The precise failure mode
(circularity — no independent SO(3) source in P1–P6) tells future work exactly
what is needed: either an independent grounding for bulk rotational symmetry,
a dynamical isotropy argument from the action, or a statistical averaging
mechanism over S² directions.

**For current canonical results:** Nothing changes. All results conditional on
P-isotropy remain valid. The 6π⁵ derivation is unaffected. The epistemic tags
in the claims registry are unaffected.

**Whether 6π⁵ is affected:** No. The derivation chain is:
P-isotropy [P] → P-SU2-sym [Dc] → volume ratio (2π²)³/(4π/3) → 6π⁵ [Dc].
P-isotropy remains [P] and the chain is intact.

**Whether P-isotropy's role in the derivation chain changes:** Its formal role
is unchanged (root postulate for P-SU2-sym). Its understood content is
sharpened: what the chain actually requires is P-S2-direction (S² invariance),
not the full S³ invariance. The gauge-automatic U(1) component was logically
redundant as an input to the chain.

---

## 10. Derivation Chain Status

Final 6π⁵ postulate status after the decomposition program:

| Postulate | Status | Notes |
|-----------|--------|-------|
| P-σ (large membrane tension) | [P] | Unchanged |
| P-local-vertex (no holonomy at junction) | [P] | Unchanged; used in P-U1-phase derivation |
| P-common-origin (τ = σa, L = a) | [P] | Unchanged |
| P-isotropy (no preferred internal direction) | [P] | Decomposed; irreducible content = P-S2-direction |
| — P-U1-phase (S¹ fiber phase invariance) | [Dc] | Gauge-automatic from ξ compactification |
| — P-S2-direction (S² spin direction invariance) | [P] | Irreducible; no independent derivation base |

**Core postulate count: 4 [P]** (unchanged from pre-decomposition).

---

## 11. Bottom Line

The P-isotropy decomposition program is a precision upgrade to the postulate
structure, not a failure and not a promotion. It revealed that half of
P-isotropy's content (U(1) phase invariance) was always gauge-automatic and
never needed to be postulated, while the other half (S² direction invariance)
is a genuine, irreducible physical assumption about the absence of preferred
spin directions. The 6π⁵ derivation chain is unaffected, but the physical
content of its assumptions is now more precisely characterized.
