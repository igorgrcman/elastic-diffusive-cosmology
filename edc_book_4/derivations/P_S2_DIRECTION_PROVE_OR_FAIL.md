# P-S2-Direction Prove-or-Fail Test

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Test:** Can P-S2-direction be promoted from [P] to [Dc] via bulk Plenum rotational isotropy?
**Result:** **FAIL — P-S2-direction remains [P]**

---

## Executive Summary

P-S2-direction ("the effective energy density ε does not depend on which direction
n̂ ∈ S² the flux tube points") **cannot** be promoted from [P] to [Dc] using bulk
Plenum rotational isotropy as the derivation base.

**Failure mode:** The candidate derivation base — "bulk Plenum rotational isotropy" —
is not an independent canonical postulate in EDC. It IS P-isotropy itself. Using
P-isotropy to derive a component of P-isotropy is circular. No independent source
of SO(3) symmetry exists in the EDC postulate set (P1–P6) that could serve as an
alternative derivation base.

**Checkpoint results:**
- Checkpoint 1 (Physical content of S²): **PASS** — S² direction is a genuine
  physical observable (observed spin direction), not a gauge artifact
- Checkpoint 2 (Canonical bulk isotropy): **FAIL** — no independent bulk isotropy
  postulate exists; P-isotropy IS the bulk isotropy assertion
- Checkpoint 3 (Symmetry-breaking mechanisms): **MIXED** — Z₆ lattice breaks
  membrane isotropy; other mechanisms compatible but Z₆ finding is structurally
  relevant

**Consequence:** P-S2-direction remains [P]. P-isotropy (full) remains [P].
The 6π⁵ derivation chain retains 4 core postulates.

---

## Checkpoint 1 — Physical Content of S² Direction

### Question

Is the S² direction in P-S2-direction a genuine physical observable (spin
direction, angular momentum direction) or a gauge/coordinate artifact?

### Analysis

**The S² direction is a genuine physical observable.**

Five independent canonical sources establish this:

**1. Book II Ch. 2 — Ontology**

`edc_book_2/reorganized/part1/chapter_02_ontology.tex` (lines 215–236):

> "Observed behavior: We see S² angular momentum (spin, 3D rotation)"
> "Observed direction t̂ ∈ S² is what we measure"
> "The S¹ fiber is the internal phase (related to U(1) gauge freedom)"

The S² base point under Hopf projection is explicitly identified as "what we
measure" — the observed direction. The S¹ fiber is the hidden/gauge part.

**2. Book II Ch. 3 — Frozen Regime**

`edc_book_2/reorganized/part1/chapter_03_frozen.tex` (lines 150–166):

Under "What Gets Frozen" (stable observables):
> "Spin structure: S³ → S² projection (half-integer vs integer)"

Under "What Remains Dynamic":
> "Phase oscillations: Internal U(1) phase can evolve"

The S³ → S² projection is classified as frozen structure (observable), while
the S¹ phase is dynamic/internal. This confirms S² carries physical content.

**3. Companion Paper F — Two Viewpoints**

`edc_papers/paper_3_series/07_companion_F_proton_junction/paper/main.tex`
(lines 556–564):

> "Brane/3D observed: Only Hopf base variables t̂ᵢ ∈ S² are directly
> observable as spatial directions. The S¹ fiber phases are frozen by the
> boundary condition during projection."

Explicit statement: S² variables are "directly observable as spatial directions."

**4. Same paper — Projection Chain**

(line 642):
> "The 3D observer sees only the base directions t̂ᵢ ∈ S²; fiber phases
> are frozen under criterion ℏω ≫ E_env."

**5. Same paper — Physical Interpretation of Fiber**

(lines 715–723):
> "The key point: from the 4D brane, we see only the S² projection (tangent
> direction), but the full 5D description requires S³."

### Verdict: **PASS — S² direction is a genuine physical observable**

The S² direction represents the observed spin direction / spatial orientation
of the flux tube as seen from the 3D brane. It is NOT a gauge artifact — the
gauge part (S¹ fiber = ξ phase) was already closed by P-U1-phase (commit
58640bf). The S² isotropy claim is therefore a genuine physical symmetry
assertion: no physical mechanism selects a preferred spin direction.

### Why P-U1-phase Did Not Already Close This

P-U1-phase established that ε does not depend on the S¹ fiber phase. This
reduces ε from a function on S³ (3 parameters) to a function on S² (2
parameters): ε = ε(n̂). But ε(n̂) could still be non-constant on S² — for
example, ε could depend on the polar angle of n̂ relative to some reference
direction. P-S2-direction claims ε(n̂) = const, which is a separate physical
assertion about the absence of any preferred S² direction.

---

## Checkpoint 2 — Bulk Plenum Isotropy in EDC

### Question

Does EDC already have a canonical postulate or established result that asserts
the Plenum bulk is rotationally isotropic — independently of P-isotropy?

### Analysis

**No. Bulk Plenum rotational isotropy is NOT independently postulated in EDC.**

**1. The formal postulate set (P1–P6) does not include bulk isotropy.**

`edc_book/chapters/chapter_0_theory_core_V17.49.tex` (lines 1430–1450)
lists the foundational postulates:

| ID | Statement |
|----|-----------|
| P1 | The universe is a 5D Lorentzian manifold M₅ with signature (−,+,+,+,+) |
| P2 | One spatial dimension ξ is compact with topology S¹ and radius R_ξ |
| P3 | Observable 3D space is a membrane Σ moving through the Bulk at velocity v_scan |
| P4 | The identification v_scan = c (speed of light) |
| P5 | The Bulk contains a Plenum with energy density ρ_Plenum |
| P6 | The membrane has surface tension σ |

None of P1–P6 assert rotational isotropy of the Plenum. P1 gives Lorentz
signature (which includes Lorentz invariance of the metric), but this is a
statement about the manifold structure, not about the Plenum medium's
physical properties.

**2. P-isotropy IS the bulk isotropy assertion.**

`edc_papers/paper_2/paper/derivations/EDC_SU2_SYM_From_Action_v1.tex`
(lines 41–47):

> Postulate P-isotropy [P]:
> "The Plenum (5D bulk medium) has no preferred internal direction."

P-isotropy was introduced in Paper 2 as a NEW postulate, separate from P1–P6.
It is explicitly tagged [P] — a primitive assumption. It is the ONLY statement
in EDC that asserts the Plenum has no preferred internal direction.

**3. P-isotropy is not used elsewhere independently.**

The INFLOW/OUTFLOW framework (`edc_papers/paper_3_series/01_paper3_njsr_journal/
paper/main.tex`, lines 490–506) rests on assumptions A1–A6 (positive bulk
pressure, energy conservation, codimension-1 membrane, localized defects,
INFLOW/OUTFLOW classification). None of these reference P-isotropy or bulk
rotational symmetry.

No other EDC derivation chain uses bulk isotropy as an input independently
of P-isotropy.

**4. The circularity is explicit.**

P-S2-direction IS a component of P-isotropy (as established in the
P-isotropy decomposition, commit 7ad6101):

> P-isotropy = P-U1-phase + P-S2-direction

"Bulk Plenum rotational isotropy" is the physical content of P-isotropy.
Using it to derive P-S2-direction is equivalent to using P-isotropy to
derive a sub-component of itself. This is circular.

**5. Could Lorentz invariance (P1) serve as an alternative?**

P1 asserts M₅ is a Lorentzian manifold with signature (−,+,+,+,+). This
gives local Lorentz invariance of the metric. However:

- Lorentz invariance of the manifold ≠ isotropy of the Plenum. A Lorentz-
  invariant spacetime can contain matter with preferred directions (e.g.,
  a magnetic field in Minkowski space).
- The Plenum is a physical medium filling the bulk — its properties are
  additional physical inputs beyond the manifold structure.
- The Z₆ crystallographic structure (see Checkpoint 3) shows that EDC
  explicitly allows preferred directions in the matter content even on a
  Lorentz-invariant manifold.

P1 cannot serve as an independent derivation base for P-S2-direction.

### Verdict: **FAIL — no independent bulk isotropy postulate exists**

The candidate derivation base ("bulk Plenum rotational isotropy") is not
independently established in EDC. It IS P-isotropy. Using P-isotropy to
derive P-S2-direction (a component of P-isotropy) is circular. No alternative
source of SO(3) symmetry exists in the postulate set P1–P6.

**This checkpoint is fatal. The derivation cannot proceed.**

---

## Checkpoint 3 — EDC Mechanisms That Could Break S² Isotropy

### Question

Even if the bulk Plenum were isotropic, could any EDC-specific mechanism
reintroduce a preferred S² direction for a flux tube?

### Analysis

Although Checkpoint 2 is already fatal, this checkpoint is completed for
completeness and to document what would need to be addressed if an
independent bulk isotropy source were found in the future.

**1. Z₆ Lattice Structure — BREAKS membrane isotropy**

`edc_book_2/reorganized/part1/chapter_04_z6_program.tex` (line 46):

> "The 5D membrane is not isotropic — it has a preferred lattice structure."

The Z₆ = Z₃ × Z₂ crystallographic symmetry is explicit:
- Z₃: 3-fold rotational symmetry (120° rotations) — selects preferred
  angular sectors for particle generations
- Z₂: 2-fold symmetry (reflection or phase flip)

**Does Z₆ break S² isotropy for individual flux tubes?**

The Z₆ structure constrains where on the membrane defects can form and
how junction arms are arranged (120° arm configurations). This is a
constraint on the 3D spatial embedding of the Y-junction, not directly
on the internal S² orientation of individual flux tube cores.

However, the relationship between the 3D spatial arm direction and the
internal S² spin direction is not trivially independent. If the Hopf
projection maps the internal S³ orientation to an observable 3D direction
(as established in Checkpoint 1), and the Z₆ lattice constrains the 3D
directions of junction arms, then Z₆ could indirectly constrain the
accessible S² directions.

**Assessment:** Z₆ breaks membrane isotropy. Whether it breaks S²
isotropy for individual flux tube internal orientations is not explicitly
resolved in the codebase, but the existence of preferred spatial
directions on the membrane is structurally concerning.

**Status: POTENTIALLY BREAKING — not definitively resolved**

**2. KK Modes Along ξ — UNEXPLORED**

`edc_book/chapters/chapter_0_theory_core_V17.49.tex` (line 500):

> "We truncate the KK tower to the zero mode n=0, valid when the
> characteristic 4D energy scale satisfies E ≪ ℏc/R_ξ"

The zero-mode truncation is standard for low-energy physics. Higher KK
modes (n > 0) could in principle couple to flux tubes with specific
winding configurations, potentially selecting preferred S² orientations.
However:

- No explicit calculation of KK-mode-induced S² anisotropy exists
- The zero-mode truncation is standard and well-motivated at low energies
- Higher KK modes are suppressed by ℏc/R_ξ

**Assessment:** KK modes are unlikely to break S² isotropy at low
energies, but this has not been formally proven.

**Status: COMPATIBLE (at zero-mode level) — not rigorously excluded**

**3. Junction Geometry (P-local-vertex) — COMPATIBLE**

`edc_book_4/chapters/ch02_junction_symmetries.tex` (lines 55–67, 163–171):

The Y-junction has Z₃ symmetry: three arms at 120° with equal lengths.
P-local-vertex states the junction action depends on X_J and n̂ᵢ
(junction position and arm normal vectors) but NOT on θᵢ (internal
orientations).

The 120° arm constraint is a geometric constraint on the spatial
embedding. It constrains the relative angles between arms but does NOT
select a preferred absolute orientation — the entire Y-junction can be
rotated in 3D space. Similarly, P-local-vertex explicitly decouples the
junction energy from internal orientations θᵢ.

**Assessment:** Junction geometry constrains relative arm angles but
not absolute S² orientation. P-local-vertex ensures no θ-dependence.

**Status: COMPATIBLE — does not break S² isotropy**

**4. Membrane Boundary Conditions — COMPATIBLE (at basic level)**

`edc_book/chapters/chapter_0_theory_core_V17.49.tex` (lines 173–177):

> "X^A(t,x) = (w(t), x, y, z, ξ₀) with w(t) = v_scan · t"

The membrane is frozen at ξ = ξ₀. This fixes the ξ position but does
not select a preferred 3D direction within the membrane. The membrane
worldvolume is 3+1 dimensional with no built-in anisotropy from ξ₀.

**Assessment:** The ξ₀ boundary condition constrains the fifth
coordinate but does not break 3D rotational symmetry.

**Status: COMPATIBLE — does not break S² isotropy**

### Summary Table

| Mechanism | Breaks S² isotropy? | Detail |
|-----------|-------------------|--------|
| Z₆ lattice | **Potentially** | Breaks membrane isotropy explicitly; indirect effect on S² not resolved |
| KK modes | Unlikely | Zero-mode truncation preserves isotropy; higher modes suppressed |
| Junction geometry | **No** | Constrains relative angles, not absolute S² orientation |
| Membrane boundary | **No** | ξ₀ fixation does not select 3D direction |

### Verdict: **MIXED — no clean S² breaking, but Z₆ is structurally concerning**

No mechanism cleanly breaks S² isotropy for individual flux tube internal
orientations. However, the Z₆ lattice explicitly breaks membrane isotropy,
and the connection between membrane spatial directions and S² internal
directions is not fully resolved.

**Note:** This checkpoint is moot given the Checkpoint 2 failure, but the
Z₆ finding would need to be addressed in any future attempt to derive
P-S2-direction.

---

## Conclusion

### Final Status

$$
\boxed{\text{P-S2-direction: remains [P] — cannot be promoted to [Dc]}}
$$

### Failure Mode

**The candidate derivation base is circular.**

"Bulk Plenum rotational isotropy" is not an independent canonical postulate
in EDC. It IS P-isotropy — the very postulate whose sub-component
(P-S2-direction) we are trying to derive. The formal postulate set P1–P6
does not contain SO(3) bulk symmetry. Lorentz invariance (P1) governs the
manifold structure, not the Plenum medium's physical properties.

This is not a technical obstruction that could be overcome with a more
clever argument. It is a structural fact about the EDC postulate set:
bulk Plenum isotropy is not independently grounded.

### Checkpoint Summary

| # | Checkpoint | Result | Detail |
|---|-----------|--------|--------|
| 1 | Physical content of S² | **PASS** | S² is observed spin direction (genuine observable, not gauge) |
| 2 | Canonical bulk isotropy | **FAIL** | No independent bulk isotropy postulate; P-isotropy IS the assertion |
| 3 | Symmetry-breaking mechanisms | **MIXED** | Z₆ breaks membrane isotropy; other mechanisms compatible |

### What Would Be Needed to Close P-S2-direction

To promote P-S2-direction to [Dc], one would need one of:

1. **An independent SO(3) symmetry source:** A postulate or derivation that
   establishes 3D rotational symmetry of the Plenum without referencing
   P-isotropy. This could potentially be grounded in the Lorentz structure
   of M₅ (P1) if one could show that the Plenum medium inherits the
   manifold's symmetries — but this is a non-trivial physical claim, not
   an automatic consequence.

2. **A dynamical isotropy argument:** Show that the membrane action +
   equations of motion force the Plenum into an isotropic configuration
   dynamically, regardless of initial conditions. This would be a
   derivation of isotropy from the action, not from a postulate.

3. **A statistical/ergodic argument:** Show that the relevant energy
   scale averages over all S² directions, making ε(n̂) effectively
   constant even if individual configurations are anisotropic. This
   would require a well-defined measure on S² and a physical mechanism
   for averaging.

None of these routes is currently available in EDC.

### What This Result Means for P-Isotropy (Full)

$$
\boxed{\text{P-isotropy: remains [P] — decomposition partially closed}}
$$

| Component | Status | Derivation |
|-----------|--------|------------|
| **P-U1-phase** | **[Dc]** | ξ gauge redundancy (commit 58640bf) |
| **P-S2-direction** | **[P]** | No independent derivation base (this test) |
| **P-isotropy (full)** | **[P]** | Requires both components; S² component blocks |

P-isotropy cannot be fully promoted to [Dc]. Its irreducible content is
P-S2-direction: the assertion that no physical mechanism selects a preferred
observed spin direction for a flux tube.

The decomposition program has achieved a clean result:
- Half of P-isotropy (the U(1) phase component) IS derivable from gauge
  structure — it was never truly an independent physical assumption
- The remaining half (the S² direction component) IS a genuine physical
  symmetry assumption — it requires independent grounding that EDC
  currently does not provide

### Final Postulate Count for 6π⁵

The 6π⁵ derivation chain retains **4 core postulates**:

| # | Postulate | Status | This test |
|---|-----------|--------|-----------|
| 1 | P-σ (large membrane tension) | [P] | Unchanged |
| 2 | P-local-vertex (no holonomy at junction) | [P] | Unchanged |
| 3 | P-common-origin (τ = σa, L = a) | [P] | Unchanged |
| 4 | **P-isotropy (no preferred internal direction)** | **[P]** | Partially decomposed; S² component irreducible |

**Note on P-isotropy's internal structure:**

Although P-isotropy remains [P], the decomposition reveals that its
"effective postulate content" is smaller than it appears. The U(1) phase
component is derivable — it was always automatic from gauge structure.
The genuine physical assumption is only the S² direction component: that
the Plenum has no preferred spin direction. This is a sharper, more
physically transparent version of the original P-isotropy.

### Value of This Negative Result

1. **Identifies the irreducible content:** P-isotropy's genuine physical
   content is P-S2-direction (S² spin direction invariance), not the full
   S³ invariance. The U(1) part was always gauge-automatic.

2. **Identifies the missing element:** What EDC lacks is an independent
   grounding for SO(3) symmetry of the Plenum. This is a precise gap that
   future work could target.

3. **Clarifies the Z₆ tension:** The Z₆ lattice explicitly breaks membrane
   isotropy. Any future derivation of P-S2-direction must explain the
   relationship between membrane anisotropy (Z₆) and internal orientation
   isotropy (P-S2-direction). These are logically independent — Z₆
   constrains spatial positions while P-S2-direction concerns internal
   orientations — but the tension should be explicitly addressed.

4. **Completes the decomposition program:** The P-isotropy decomposition
   into P-U1-phase [Dc] + P-S2-direction [P] is now fully resolved.
   No further sub-decomposition is available.

---

## Files and Sources Consulted

| File | Location | Relevance |
|------|----------|-----------|
| `chapter_02_ontology.tex` | `edc_book_2/reorganized/part1/` | S² = "observed direction, what we measure" (lines 215–236) |
| `chapter_03_frozen.tex` | `edc_book_2/reorganized/part1/` | S² projection = frozen spin structure (lines 150–166) |
| `main.tex` (Companion F) | `edc_papers/paper_3_series/07_companion_F_proton_junction/paper/` | S² = "directly observable spatial directions" (lines 556–564, 642, 715–723) |
| `chapter_0_theory_core_V17.49.tex` | `edc_book/chapters/` | Postulates P1–P6 (lines 1430–1450); KK truncation (line 500) |
| `EDC_SU2_SYM_From_Action_v1.tex` | `edc_papers/paper_2/paper/derivations/` | P-isotropy definition [P] (lines 41–47) |
| `chapter_04_z6_program.tex` | `edc_book_2/reorganized/part1/` | "5D membrane is not isotropic" (line 46) |
| `ch02_junction_symmetries.tex` | `edc_book_4/chapters/` | Junction crystallization Z₆ (lines 55–67, 163–171) |
| `main.tex` (Paper 3) | `edc_papers/paper_3_series/01_paper3_njsr_journal/paper/` | INFLOW assumptions A1–A6 (lines 490–506) |
| `P_ISOTROPY_PROVE_OR_FAIL.md` | `edc_book_4/derivations/` | P-isotropy decomposition (commit 7ad6101) |
| `P_U1_PHASE_PROVE_OR_FAIL.md` | `edc_book_4/derivations/` | P-U1-phase [Dc] (commit 58640bf) |
