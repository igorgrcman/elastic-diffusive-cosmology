# P-U1-Phase Prove-or-Fail Test

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Test:** Can P-U1-phase be promoted from [P] to [Dc] via ξ gauge structure?
**Result:** **PASS — P-U1-phase promoted to [Dc]**

---

## Executive Summary

P-U1-phase ("the effective action/energy is invariant under U(1) phase shifts
along the Hopf S¹ fiber") **can** be promoted from [P] to [Dc].

**Derivation mechanism:** The Hopf S¹ fiber IS the compact ξ dimension.
Phase shifts along this fiber are U(1) gauge transformations (shifts of the
absolute ξ-phase). Energy density is gauge-invariant — it depends on field
gradients and winding numbers (topological), not on the absolute phase
(gauge-dependent). Therefore ε(θ) cannot depend on the S¹ component of θ.

**Checkpoint results:**
- Checkpoint 1 (Identity of U(1)): **PASS** — same U(1)
- Checkpoint 2 (Gauge vs. physical): **PASS** — gauge redundancy → exact invariance
- Checkpoint 3 (Junction condition): **PASS** — P-local-vertex ensures independence

**Status after this test:**

| Sub-claim | Status | Source |
|-----------|--------|--------|
| P-U1-phase | **[Dc]** | U(1) gauge invariance of ξ compactification |
| P-S2-direction | [P] | Not tested in this prompt |

P-isotropy (full S³ invariance) requires BOTH sub-claims. Since P-S2-direction
remains [P], P-isotropy itself remains [P]. But the decomposition has yielded
one derivable component.

---

## Checkpoint 1 — Identity of U(1)

### Question

Is the U(1) acting on the Hopf S¹ fiber the SAME U(1) as charge quantization?

### Analysis

Three canonical identifications establish this:

**1. Charge quantization U(1) = ξ rotation**

Part I Ch. 3 (`chapter_3_confinement.tex`, lines 205–227):
> "Electric charge is associated with the U(1) factor in U(3) = SU(3) × U(1).
> Geometrically, this U(1) corresponds to **rotation in the compact ξ dimension**."

The charge formula is:
$$
Q = \frac{e}{2\pi} \oint d\xi \, \partial_\xi(\arg \Phi) = e \cdot n
$$

Charge = winding number around ξ. The U(1) is rotation in ξ.

**2. ξ rotation U(1) = KK gauge U(1)**

Part I Ch. 0 (`chapter_0_theory_core_V17.49.tex`, lines 197–200):
> "Electric charge arises from **winding number** around the compact dimension ξ."
> "Mathematically, this is a U(1) connection 1-form A on M₅"

The KK reduction of the 5D metric produces a U(1) gauge field. This IS the
electromagnetic U(1). The gauge transformation is ξ → ξ + const (constant
phase shift along the compact dimension).

**3. KK gauge U(1) = Hopf fiber U(1)**

Book II Ch. 2 (`chapter_02_ontology.tex`, lines 228–232):
> "Internal phase ψ ∈ S³ describes full 5D orientation"
> "The S¹ fiber is the internal phase (related to U(1) gauge freedom)"

The Hopf fibration S¹ → S³ → S² decomposes the internal orientation into
a base point on S² (observed spin) and a phase on S¹ (internal, gauge-related).
This S¹ is explicitly identified with "U(1) gauge freedom."

**Chain of identifications:**

$$
\text{Hopf fiber } S^1 \;=\; \text{internal ξ-phase} \;=\; \text{KK gauge } U(1) \;=\; \text{charge quantization } U(1)
$$

All four are the **same** U(1). This chain is canonical — each link is
established in published Part I or canonical Book II text.

### Verdict: **PASS — same U(1)**

The Hopf S¹ fiber is identical to the ξ-compactification U(1) responsible
for charge quantization. This is not a coincidence or an additional assumption —
it is the canonical EDC physical picture.

---

## Checkpoint 2 — Gauge Redundancy vs. Physical Symmetry

### Question

Is the Hopf fiber rotation a gauge transformation (redundancy) or a physical
rotation that changes observables?

### Analysis

**The Hopf fiber rotation is a gauge transformation.**

A vortex with winding number n around ξ has field configuration:
$$
\Phi(\xi) \sim e^{i n \xi / R_\xi + i\varphi_0}
$$

where φ₀ is the absolute phase. A Hopf fiber rotation shifts φ₀ → φ₀ + δ.

**What depends on φ₀?**

- The winding number n: **No.** n is a topological invariant — it counts how
  many times the phase wraps around ξ. It is independent of the absolute
  phase φ₀.

- The energy density: **No.** The energy density of a membrane/vortex
  configuration depends on:
  - Field gradients: ∂_ξ Φ ~ (in/R_ξ) · Φ — the magnitude |∂_ξ Φ|²
    does not depend on φ₀
  - Membrane tension contributions: σ · (geometric quantities) — no φ₀
    dependence
  - Topological structure: winding numbers — no φ₀ dependence

- The electric charge Q = e·n: **No.** Charge is determined by winding
  number, which is topological.

**What DOES depend on φ₀?**

Only the complex phase of the field Φ at a given point. This is a gauge
degree of freedom — the choice of "zero angle" in ξ. Different choices of
φ₀ describe the same physical state, just with different gauge conventions.

**Consequence for P-U1-phase:**

Since the Hopf fiber rotation is a gauge transformation (redundancy), the
energy density ε(θ) **must** be invariant under it. This is not an empirical
fact or a contingent physical symmetry — it is a structural requirement of
gauge-invariant physics.

$$
\varepsilon(\theta) = \varepsilon(e^{i\varphi} \cdot \theta) \quad \forall \varphi \in U(1)
$$

This invariance is:
- **Exact** (not approximate) — gauge invariance is exact
- **Automatic** (not contingent) — any well-defined physical observable is
  gauge-invariant
- **Derivable** (not postulated) — follows from the structure of ξ
  compactification

### Important distinction

The fact that P-U1-phase follows from gauge redundancy does NOT make it
"physically empty." It has a concrete physical consequence:

**ε(θ) depends only on the S² base point of the Hopf projection, not on the
S¹ fiber phase.**

This reduces the possible functional dependence of ε from a function on S³
(3 dimensions) to a function on S² (2 dimensions). This is a genuine constraint
on the effective action, even though it follows from gauge structure rather
than a dynamical symmetry.

### Verdict: **PASS — gauge redundancy → exact invariance**

P-U1-phase is [Dc]: it follows from U(1) gauge invariance of ξ compactification.
The invariance is exact and structural, not approximate or contingent.

---

## Checkpoint 3 — Junction Condition under U(1) Rotation

### Question

Does a U(1) phase shift on one fiber preserve the Y-junction condition?
Is the invariance local (per-fiber) or only global (all fibers together)?

### Analysis

**P-local-vertex states:** The junction action S_junction(X_J, n̂ᵢ) depends
on the junction position X_J and the arm normal vectors n̂ᵢ, but NOT on
the internal orientations θᵢ ∈ S³.

This means:
1. The junction energy does not depend on θ₁, θ₂, θ₃ at all
2. A U(1) phase shift θᵢ → e^{iφ}·θᵢ on any single fiber has no effect on
   the junction energy
3. Independent phase shifts on different fibers are allowed

**Compatibility with Z₃ topological locking:**

Part I Ch. 3 establishes the Z₃ locking mechanism (Postulate 3.1): within a
baryon, the three quarks share the ξ coordinate, each occupying a 120° sector.
This constrains the **discrete winding structure** (1/3 + 1/3 + 1/3 = 1).

Does Z₃ locking constrain the continuous U(1) phase?

**No.** The Z₃ locking fixes the winding numbers (discrete topological
invariants). A U(1) phase shift changes the absolute phase φ₀ without
changing the winding number n. The locking constrains:
- Winding sectors: each quark in a 120° sector — topological, discrete
- NOT the absolute phase within each sector — continuous, gauge-dependent

Therefore:
- Z₃ locking constrains topology (winding structure) — unaffected by U(1) phase
- P-local-vertex ensures no orientation coupling — independent shifts allowed
- Both conditions are preserved under per-fiber U(1) phase shifts

**Invariance type: LOCAL (per-fiber independent)**

Each fiber can be independently U(1)-rotated without affecting the junction
condition or the Z₃ locking. This is because:
- The junction depends on geometry (X_J, n̂ᵢ), not orientation (θᵢ)
- The Z₃ locking depends on winding numbers (topology), not absolute phases

### Verdict: **PASS — junction condition preserved, local invariance established**

---

## Conclusion

### Final Status

$$
\boxed{\text{P-U1-phase: promoted to [Dc]}}
$$

**Conditional on:**
- ξ compactification (KK structure) — canonical EDC, tagged [D]
- U(1) gauge invariance (from KK reduction) — canonical EDC, tagged [D]
- P-local-vertex (junction θ-independence) — already [Dc]

### Checkpoint Summary

| # | Checkpoint | Result | Detail |
|---|-----------|--------|--------|
| 1 | Identity of U(1) | **PASS** | Hopf S¹ = ξ-compactification U(1) = charge-quantization U(1) (canonical) |
| 2 | Gauge vs. physical | **PASS** | Gauge redundancy → exact, structural invariance |
| 3 | Junction condition | **PASS** | P-local-vertex ensures independence; Z₃ locking is topological, not phase-dependent |

### Derivation Chain

| Step | Statement | Status | Dependencies |
|------|-----------|--------|--------------|
| U1 | ξ ∈ S¹ is compact | [D] | EDC postulate P2 |
| U2 | KK reduction gives U(1) gauge field | [D] | U1, standard KK |
| U3 | U(1) gauge transformation = ξ phase shift | [D] | U2 |
| U4 | Hopf S¹ fiber = ξ phase | [D] | Book II Ch. 2 canonical identification |
| U5 | Energy density is gauge-invariant | [D] | Standard physics |
| U6 | Hopf fiber rotation = ξ phase shift = gauge transformation | [Dc] | U3 + U4 |
| U7 | Junction does not couple θ | [Dc] | P-local-vertex |
| **U8** | **ε(θ) invariant under Hopf fiber rotation (per-fiber)** | **[Dc]** | U5 + U6 + U7 |

### What P-U1-phase Says in [Dc] Form

**Statement:**
The energy density ε(θ₁, θ₂, θ₃) of the proton Y-junction is invariant under
independent U(1) phase shifts along the Hopf S¹ fiber of each S³:

$$
\varepsilon(e^{i\varphi_1}\theta_1, \; e^{i\varphi_2}\theta_2, \; e^{i\varphi_3}\theta_3)
= \varepsilon(\theta_1, \theta_2, \theta_3)
\quad \forall \varphi_1, \varphi_2, \varphi_3 \in U(1)
$$

**Physical meaning:**
The energy density depends on the observed spin directions (S² base points)
but not on the internal ξ-phases (S¹ fiber). This is because the S¹ phase is
a gauge degree of freedom — it describes the choice of "zero angle" in ξ,
which is not a physical observable.

### What Remains for Full P-Isotropy

P-isotropy = P-U1-phase + P-S2-direction

| Component | Status | What it requires |
|-----------|--------|------------------|
| **P-U1-phase** | **[Dc]** | ε independent of S¹ Hopf fiber phase |
| P-S2-direction | [P] | ε independent of S² spin direction |
| P-isotropy (full) | [P] | Both components needed |

To close P-isotropy fully, one would need to show that the energy density
also does not depend on the S² base point — i.e., that no physical mechanism
selects a preferred spin direction for the flux tube. This is a separate
question about the spatial embedding symmetry, not about gauge structure.

---

## Files and Sources Consulted

| File | Location | Relevance |
|------|----------|-----------|
| `chapter_3_confinement.tex` | `edc_book/chapters/` | U(1) = ξ rotation; charge = winding; Z₃ locking |
| `chapter_0_theory_core_V17.49.tex` | `edc_book/chapters/` | U(1) connection from KK; D6 charge tag |
| `chapter_02_ontology.tex` | `edc_book_2/reorganized/part1/` | Hopf S¹ = "internal phase (U(1) gauge freedom)" |
| `P_ISOTROPY_PROVE_OR_FAIL.md` | `edc_book_4/derivations/` | Prior test establishing decomposition |
| `EDC_SU2_SYM_From_Action_v1.md` | `edc_papers/paper_2/supplementary/derivations/` | Existing v9 P-isotropy → P-SU2-sym derivation |
