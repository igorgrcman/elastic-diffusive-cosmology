# Phase 2 Next-Step Plan: Lane Selection After WP2 Bounded No-Go

---

## 1. Title

Next-Step Execution Plan for Phase 2 / Book IV Neutron Line:
**Select and structure the next derivation lane after the N1 (Israel
junction energy) bounded no-go in WP2.**

---

## 2. Origin

This plan follows the accepted bounded no-go of N1 in WP2.

**Governing documents:**
- `PHASE2_PLAN_V1.md` (v1.1) — canonical Phase 2 execution plan, updated
  after WP2
- `appendices/app_P2_WP2_Israel_nodewell.tex` — WP2 derivation and
  no-go result
- `code/p2_wp2_israel_nodewell_check.py` — WP2 numerical verification
  (6/6 pass)
- `audit/PHASE2_WP1_DONOR_NORMALIZATION.md` — donor normalization,
  candidate landscape

**What WP2 established:**
- Thin-junction Israel conditions produce zero deficit angle for all q
  (coplanar arms partition 2π — geometric identity)
- Arm-interior Israel energy is proportional to V_geom(q) = τ L_tot(q),
  renormalizing tension only; single-well
- No Israel-sector mechanism generates an attractive V_node(q)
- Scope: valid for all thin Y-junctions in any warped 5D background
  with S_EH + S_NG

---

## 3. Current Decision Problem

**The decision:** Choose the next execution lane between:

- **Lane A — N2: Bulk gravitational backreaction.** Junction displacement
  sources a bulk metric perturbation; the energy stored in this
  perturbation depends on q.
- **Lane B — N7: Thick-junction / internal-core structure.** Replace
  the thin-junction (distributional) treatment with a regularized core
  at scale δ; the internal core energy depends on q through the
  changing stress configuration at the vertex.

One lane must be selected for the next implementation cycle. The other
becomes the backup.

---

## 4. Why Replanning Is Required

WP2 eliminated the primary candidate mechanism (N1: Israel junction
energy in the thin-junction approximation) from the active candidate
list. The WP1 donor normalization had identified N1 as the sole
untested, unfalsified candidate with clear physical basis and
tractability. With N1 now a preserved dead-end, the candidate landscape
has narrowed:

**Before WP2:**
| Active | Dead/Falsified |
|--------|----------------|
| N1 (primary), N2 (backup) | N3 (partial), N4 (partial), N5 (Helfrich), N6 (phenomenological) |

**After WP2:**
| Active | Dead/Falsified |
|--------|----------------|
| N2 (surviving), N7 (new — thick-junction) | N1 (bounded no-go), N3, N4, N5, N6 |

Target selection must be updated before the next implementation cycle.

---

## 5. Lane A — N2: Bulk Gravitational Backreaction

### Technical Description

When the Y-junction node displaces by q, the stress-energy distribution
on the brane changes. The bulk metric responds through the 5D Einstein
equations. The change in total gravitational energy of the
bulk+brane+junction system as a function of q defines V_bulk(q).

Formally:
```
V_bulk(q) = E_grav[g(q)] - E_grav[g(0)]
```
where g(q) is the 5D metric sourced by the junction at displacement q,
and E_grav is the gravitational energy functional.

### What It Would Need to Derive or Bound

1. **Linearized 5D Einstein equations** with the displaced junction as
   source: δR_AB - ½ g_AB δR = κ₅² δT_AB, where δT_AB encodes the
   change in brane stress-energy from q ≠ 0.
2. **Green's function** for the linearized operator in the relevant
   background (flat, RS, or warped).
3. **Integration** of the linearized perturbation energy over the bulk
   to obtain V_bulk(q).
4. **Sign determination**: is V_bulk attractive (negative) or repulsive
   (positive) at q > 0?

### Existing Donor Material

| Asset | Location | Relevance | Status |
|-------|----------|-----------|--------|
| Put C Variant 2 results | D2: `PUTC_EXECUTION_REPORT.md` | Warped metric scan (125 combinations); no metastability found | [Dc] — partial negative |
| S_bulk action definition | D1: `S5D_TO_SEFF_Q_REDUCTION.md` | Formal bulk action structure | [Def] |
| OPR-21 Robin BC / Israel report | `OPR21_BC_ISRAEL_REPORT.md` | Robin BC from Israel conditions; self-adjointness check | [Dc] — methodology |
| putC_compute_MV.py | D3 | Extendable numerical V(q) scanner | [Cal] — code |

### Main Strengths

1. **Arises from explicit S_total terms.** Bulk backreaction is a
   physical effect present in any gravitational theory with localized
   sources; it does not require additional physics beyond S_EH.
2. **Could produce attraction.** In gravitational physics, localized
   massive objects attract; a junction pulling bulk gravitational energy
   toward a displaced position could in principle lower total energy at
   certain q values.
3. **Standard formalism.** Linearized gravity in 5D with brane sources
   is a well-studied problem (Randall-Sundrum literature, brane-world
   perturbation theory).

### Main Blockers

1. **Variant 2 negative result.** The Put C execution report scanned 125
   warped metric parameter combinations and found zero metastability.
   While this used specific metric ansätze (not junction-sourced
   perturbations), it provides a negative prior.
2. **Technical complexity.** Solving linearized 5D Einstein equations
   with a Y-junction source (three intersecting worldsheets) is
   substantially harder than the thin-junction Israel matching tested in
   WP2. The source term δT_AB is distributional on three surfaces.
3. **Background dependence.** Results depend on the choice of background
   metric [I/P]. Different backgrounds (flat, RS, AdS-Schwarzschild)
   could give qualitatively different V_bulk(q).
4. **No existing analytical computation.** No branch in the 40-branch
   repo contains a linearized bulk perturbation calculation for the
   Y-junction.

### Main Circularity / Smuggling Risks

- **CR3 applies directly:** Background metric chosen to produce
  double-well. If V_bulk(q) depends sensitively on background, the
  result is [Dc|model, metric-dependent].
- **CR6 applies:** Undetermined coefficients from mode integration could
  absorb the gap.
- **New risk:** If V_bulk(q) is small (gravitational backreaction is
  typically suppressed by κ₅² ∝ 1/M₅³), it may be unable to compete
  with V_geom ~ τR ~ O(10 MeV). The mechanism might be real but
  quantitatively irrelevant.

---

## 6. Lane B — N7: Thick-Junction / Internal-Core Structure

### Technical Description

Replace the thin-junction (distributional, zero-width) treatment used in
WP2 with a regularized junction core at the physical scale
δ ≈ 0.105 fm [I]. The core occupies a finite region around the junction
vertex, with internal structure determined by the brane tension, warp
factor, and stress distribution at the point where three worldsheets
converge.

The core energy as a function of node displacement:
```
V_core(q) = -E₀ × f(q/δ)
```
where E₀ = C × σ × δ² is the core ground-state energy scale (structural
relation [Dc]: C ∝ (L₀/δ)²), and f(q/δ) is the q-dependent profile
to be derived or constrained.

The WP2 no-go identified thick-junction core as the primary escape route:
the thin-junction approximation removes all core physics by replacing the
vertex with a distributional matching condition. Any q-dependent energy
associated with the internal structure of the junction vertex is
invisible in the thin-junction limit.

### What It Would Need to Derive or Bound

1. **Core regularization model:** Specify the internal structure of the
   junction vertex at scale δ. Options:
   - (a) Smoothed junction: replace distributional matching with a smooth
     transition region of width δ, with internal metric determined by the
     5D equations of motion.
   - (b) Separable core ansatz: adopt the framework from
     `DERIVE_C_FROM_GEOMETRY.md` (S3) with ρ_core(r_⊥, q) = σ × g_⊥(r_⊥/r₀) × f(q/δ).
   - (c) Effective core energy: model the core as a finite-size defect
     with energy depending on the local stress tensor, which changes with q.
2. **q-dependence of core energy:** Compute how displacing the node by q
   changes the stress configuration within the core. Does the core energy
   decrease (attractive) or increase (repulsive) with displacement?
3. **Magnitude estimate:** Is |V_core(q_n)| large enough to compete with
   V_geom(q_n) = τ × ΔL_tot(q_n)?
4. **Profile shape:** Does V_core(q) have the right functional form
   (localized attractive region at q > 0) to create a secondary minimum
   when combined with V_geom?

### Existing Donor Material

| Asset | Location | Relevance | Status |
|-------|----------|-----------|--------|
| Junction-core C structure | S3: `junction-core-derive-C-v1` / `DERIVE_C_FROM_GEOMETRY.md` | C ∝ (L₀/δ)² derived from separable core ansatz; 3D→1D reduction framework | [Dc] structure / [I] value |
| Separable core density ansatz | S3 §3 | ρ_core = σ × g_⊥(r_⊥/r₀) × f(q/δ) framework | [Dc] structural — directly reusable |
| V_core(q) = -E₀ × f(q/δ) form | S3 §1 | Target functional form for core well | [Dc] structural — reusable |
| Put C Variant 3 (phenomenological well) | D2 §Variant 3 | Demonstrates that an attractive term with E₀ ~ 10 MeV and width ~ δ creates metastability. Comparison target only. | [P/Cal] — forbidden as [Dc] |
| E₀ scaling: σ × δ² ~ 0.097 MeV (C=1) | Dimensional | Bare core energy scale without geometric amplification | [Dc] — sets baseline |
| E₀ scaling: σ × L₀ × δ ~ 0.93 MeV (with L₀) | Dimensional | Cross-scale core energy with junction extent | [Dc] — alternate scaling |

### Main Strengths

1. **Directly addresses the WP2 escape route.** The WP2 no-go is
   specifically about thin junctions. Thick-junction physics is the
   natural next step: it tests whether the missing V_node lives in the
   internal structure that the thin-junction approximation discards.
2. **Existing framework.** The `junction-core-derive-C-v1` branch
   provides a separable core ansatz, 3D→1D reduction methodology, and
   the structural relation C ∝ (L₀/δ)². This is directly extendable.
3. **Physical motivation.** Three worldsheets converging at a point
   create a stress concentration. At finite resolution δ, this stress
   is spread over a core region. The energy stored in this region
   plausibly depends on the node position q: displacing the node
   redistributes stress among the three arms within the core.
4. **Falsifiable.** If the core energy is repulsive or q-independent
   for all physically reasonable core profiles, the thick-junction
   lane yields a no-go — directly constraining the theory.
5. **Scalable energy.** The geometric amplification C ∝ (L₀/δ)² can
   produce E₀ ~ O(10 MeV) from a bare scale σδ² ~ 0.1 MeV. This is
   the right order of magnitude to compete with V_geom.

### Main Blockers

1. **Core structure must be specified [P].** The internal profile
   g_⊥(r_⊥/r₀) and the q-dependence f(q/δ) are not derived from
   S_5D — they require a regularization model. Different models give
   different V_core(q). The result is inherently [Dc|model].
2. **Circularity with C = 100.** The numerical value C = 100 from S3
   uses L₀ = 1.0 fm [I] and δ = 0.1 fm [I]. The scaling structure
   is [Dc] but the value is circular (WP1, F3). Must use only the
   structural relation, not the numerical value.
3. **Risk of reproducing Variant 3.** If the core profile f(q/δ) is
   chosen (rather than derived), the result could amount to relabeling
   the phenomenological Gaussian well as a "core model" — which is
   exactly the smuggling risk CR2 from the Phase 2 plan.

### Main Circularity / Smuggling Risks

- **CR2 is the primary risk:** Relabeling the phenomenological node
  well. The core profile f(q/δ) must be derived or constrained from
  physical principles (stress balance, elasticity, variational
  minimization), not fitted to reproduce V_B ≈ 2.6 MeV.
- **CR4 applies:** The numerical value C = 100 must not be imported
  as independent evidence.
- **New risk (CR9):** Core profile chosen to match τ_n. If the only
  constraint on f(q/δ) is that V_core creates V_B ≈ 2Δm_np, the
  result is [Cal], not [Dc].
- **Mitigation:** The q-dependence of V_core must follow from the
  stress redistribution physics at the vertex, not from the desired
  barrier height. The anti-smuggling rule: compute V_core(q) first,
  then check whether V_B matches 2Δm_np.

---

## 7. Head-to-Head Comparison

| Criterion | Lane A (N2 Bulk Backreaction) | Lane B (N7 Thick-Junction Core) |
|-----------|------------------------------|--------------------------------|
| **Physical plausibility** | Moderate. Gravitational backreaction is real but typically small (κ₅²-suppressed). | Moderate-high. Stress concentration at junction vertex is physical; finite-size effects are real at scale δ. |
| **Donor readiness** | Low. No existing analytical computation. Variant 2 provides negative results only. Methodology must be built from scratch. | Moderate. `junction-core-derive-C-v1` provides separable ansatz framework, structural scaling, and code. Directly extendable. |
| **Implementation complexity** | High. Requires solving linearized 5D Einstein equations with Y-junction source (3 intersecting distributional worldsheets). Green's function needed. | Moderate. Requires specifying and computing with a regularized core profile. Separable ansatz already exists. Numerical implementation straightforward. |
| **Falsifiability** | High. If linearized bulk perturbation energy is repulsive or negligible → clear no-go. | High. If core energy is repulsive or q-independent for all reasonable profiles → clear no-go. |
| **Calibration risk** | Low-moderate. V_bulk(q) shape determined by linearized equations, not freely adjustable. Background metric is the main free choice [I/P]. | Moderate-high. Core profile g_⊥ and f are model inputs [P]. Risk of adjusting them to produce desired outcome. |
| **Smuggling risk** | Low. No existing phenomenological form to relabel. Result is genuinely new. | Moderate. Risk of relabeling Variant 3 Gaussian well as "core model" (CR2). Requires strict anti-smuggling discipline. |
| **Likelihood of reproducing another phenomenological well** | Low — but also low likelihood of producing any well at all (Variant 2 negative prior). | Moderate — the core framework already has V_core(q) = -E₀ × f(q/δ) with adjustable profile. Honest derivation vs fitted profile is the key distinction. |
| **Expected epistemic leverage if successful** | High. A V_bulk from linearized gravity with no free parameters (beyond background metric) would be a clean [Dc|model] result. | Moderate-high. A V_core from a specified regularization model is [Dc|model] but inherits the core-specification model dependence. |
| **Negative-prior weight** | Variant 2 (125 combinations, no metastability) provides moderate negative evidence. | No prior test of thick-junction core energy. Fresh territory. |
| **Time to first result** | Longer. Formalism must be built. | Shorter. Framework exists; extension is targeted. |

---

## 8. Decision

**Selected next lane: Lane B — N7: Thick-junction / internal-core
structure.**

**Rationale:**

1. **Direct response to WP2.** The WP2 no-go is specifically about
   thin junctions. The thick-junction lane tests whether the physics
   discarded by the thin-junction approximation contains the missing
   V_node. This is the most logically coherent next step.

2. **Donor readiness.** The `junction-core-derive-C-v1` branch provides
   a working framework (separable core ansatz, 3D→1D reduction, structural
   scaling C ∝ (L₀/δ)²) that can be extended to compute V_core(q).
   Lane A has no comparable infrastructure.

3. **Negative prior for N2.** Variant 2 tested 125 warped metric
   parameter combinations and found no metastability. While this is not
   a full linearized perturbation calculation, it provides moderate
   negative evidence for bulk backreaction as the sole source of
   attraction. Lane B has no such negative prior.

4. **Shorter path to decisive result.** The thick-junction framework
   exists; extending it to compute V_core(q) is a bounded task. Lane A
   requires building linearized 5D perturbation theory from scratch.

5. **Correct energy scale.** The geometric amplification C ∝ (L₀/δ)²
   can produce core energies E₀ ~ O(10 MeV) from bare σδ² ~ 0.1 MeV.
   Bulk backreaction energies are generically κ₅²-suppressed and may
   be too small to compete with V_geom.

**Lane A (N2) becomes the backup.** If Lane B yields a no-go (core
energy is repulsive or q-independent), Lane A should be attempted before
declaring the double-well postulate falsified within the S_EH + S_NG
model class.

---

## 9. Chosen Next Lane Objective

**Objective:** Derive or bound V_core(q) — the junction-core energy as
a function of node displacement q — from a physically specified
regularization of the Y-junction vertex at scale δ.

Concretely:
1. Specify a regularized core model (smoothed junction or separable
   density ansatz) with declared [P] assumptions
2. Compute V_core(q) from the core model
3. Combine V_geom(q) [Dc] + V_core(q) to form candidate V(q)
4. Determine whether the combined V(q) has double-well structure
5. If yes: extract V_B, q_n, and compare to 2Δm_np as [Check]
6. If no: document no-go with scope

**Target epistemic tag:** [Dc|model] at best. The model dependence
enters through the core regularization, which is [P].

---

## 10. What the Chosen Next Lane Is Not

- Not a derivation of V_core from pure S_5D without model input.
  Some core-structure specification [P] is unavoidable.
- Not a full Put C completion (C2-C4). Only the core contribution to
  C2 is addressed.
- Not a derivation of M(q), ω₀, or A. These are downstream.
- Not an attempt to derive L₀/δ. That is a separate target (Rank 2).
- Not a recycling of the Variant 3 phenomenological Gaussian under a
  new name. The core profile must follow from the regularization model,
  not from the desired V_B.
- Not a proof that the double-well exists. A no-go is an allowed
  outcome.

---

## 11. Minimal Donor Bundle for the Chosen Lane

| Asset | Purpose | Status | Reusable? |
|-------|---------|--------|-----------|
| V_geom(q) = τ L_tot(q) | Geometric baseline [Dc] | Phase 1 R3 | YES — central |
| Junction-core C ∝ (L₀/δ)² structure | Separable core ansatz framework | [Dc] structural | YES — extend |
| Separable density ρ_core = σ g_⊥ f(q/δ) | 3D→1D reduction template | [Dc] structural | YES — extend |
| σ = 8.82 MeV/fm² | Brane tension | [Dc] | YES |
| δ ≈ 0.105 fm | Junction-core scale | [I] | YES |
| L₀ ≈ 1.0 fm | Junction extent (5D localization) | [I] | YES — scaling only |
| WP2 no-go (D14) | Constrains: thin-junction Israel produces no attraction | [Dc] NO-GO | YES — constraint |
| Put C Variant 3 | Comparison target: V_B ≈ 2.8 MeV with fitted parameters | [P/Cal] — forbidden as [Dc] | Comparison only |
| putC_compute_MV.py | Extendable V(q) numerical scanner | [Cal] code | YES — extend |

**Forbidden imports** (inherited from WP1 §11 + WP2):
- V_B = 2Δm_np as constraint
- Phenomenological Gaussian well as [Dc]
- C = 100 as independent evidence
- τ_n as derivation input
- N1 (Israel thin-junction) as a positive mechanism

---

## 12. Primary Risks

Ranked by impact:

1. **CR2 — Relabeling the phenomenological well.** The core profile
   f(q/δ) could be chosen to reproduce the Variant 3 Gaussian, making
   the result [P/Cal] dressed as [Dc|model]. **Mitigation:** The profile
   must follow from the regularization physics (stress balance,
   variational principle), not from V_B matching.

2. **Model dependence of core regularization.** Different core models
   (smoothed metric, profile function, elastic membrane) could give
   qualitatively different V_core(q). The result is inherently
   model-dependent. **Mitigation:** Test at least two distinct core
   models. Report all results, not just the one that works.

3. **Circularity with L₀/δ.** The geometric amplification C ∝ (L₀/δ)²
   uses L₀ [I]. If V_B ≈ 2Δm_np is achieved only because C × σδ² ~
   O(1 MeV) with C = (L₀/δ)² ~ 100, and L₀ is chosen to produce this,
   the result is [Cal]. **Mitigation:** Report V_core as a function of
   (L₀/δ). If V_B depends sensitively on L₀/δ, flag as [I]-dependent.

4. **Core energy too small.** If the core energy scale is set by σδ²
   without geometric amplification, E₀ ~ 0.1 MeV — too small by a
   factor ~30 to compete with V_geom. The mechanism would be real but
   quantitatively irrelevant. **Mitigation:** This is an informative
   no-go, not a failure of the analysis.

5. **Core energy repulsive.** If the stress redistribution at the vertex
   increases energy when the node displaces (core energy is repulsive),
   V_core reinforces V_geom rather than opposing it. **Mitigation:**
   Document as no-go within the model.

---

## 13. Checkpoint Design

| ID | After | Decision Gate | Proceed If | Stop/Narrow If |
|----|-------|---------------|------------|----------------|
| **CP-N7-1** | Core model specification | Is the regularized core model well-defined with clear [P] assumptions? | Core model produces a computable V_core(q) with finite number of parameters | Core model requires unbounded parameter choices or reduces to thin-junction limit |
| **CP-N7-2** | V_core(q) computation | Does V_core(q) have an attractive (negative) region at q > 0? | Yes: V_core(q*) < 0 for some q* > 0. Proceed to combination with V_geom. | No: V_core ≥ 0 for all q, or V_core ≡ 0. → No-go for thick-junction lane within this model. |
| **CP-N7-3** | Full V(q) = V_geom + V_core analysis | Does combined V(q) have double-well structure? | Yes: secondary minimum at q_n > 0 with barrier. Extract V_B. Proceed to numerical verification. | No: V_core is attractive but insufficient to overcome V_geom. → Partial no-go (mechanism real but too weak). |
| **CP-N7-4** | Numerical verification | Does V_B compare to 2Δm_np within reasonable L₀/δ range? | V_B within factor 2–3 of 2.59 MeV for L₀/δ in [5, 15]. → Informative partial result. | V_B off by > order of magnitude, or requires extreme parameter choices. → Document as conditional/fine-tuned. |

---

## 14. Likely Deliverables for the Next Implementation Cycle

### New Files (predicted)

| File | Purpose |
|------|---------|
| `appendices/app_P2_WP3_thick_junction_core.tex` | Derivation appendix: core model, V_core(q), combination with V_geom, outcome classification |
| `code/p2_wp3_thick_junction_check.py` | Numerical verification: V_core computation, V(q) profile, critical point analysis |

### Modified Files (predicted)

| File | Likely Changes |
|------|---------------|
| `main.tex` | Add `\input{appendices/app_P2_WP3_thick_junction_core}` |
| `chapters/ch03_neutron_metastable.tex` | Update V_node status with thick-junction result |
| `PHASE2_PLAN_V1.md` | Update revision history, WP-B status |
| `PHASE2_NEXTSTEP_PLAN_V1.md` | Update with execution outcome |

---

## 15. No-Go / Abort Signals

| Signal | Response |
|--------|----------|
| **CP-N7-1: Core model reduces to thin junction** | If regularization at scale δ → 0 recovers the WP2 thin-junction result (no new physics), the thick-junction lane adds nothing. Abort and pivot to Lane A (N2). |
| **CP-N7-2: V_core is repulsive or zero** | Document as no-go for thick-junction core. Candidate N7 joins N1 as preserved dead-end. Pivot to Lane A (N2). |
| **CP-N7-3: V_core attractive but too weak** | Document as partial result: mechanism is real, scale is insufficient. The double-well requires either larger core energy (which needs independent justification) or additional physics. |
| **CP-N7-2 + Lane A no-go: Both N2 and N7 fail** | The double-well postulate [P] is falsified within the S_EH + S_NG model class. The instanton program requires physics beyond the minimal 5D action. This is a significant negative result. Document in WP-D and proceed to full Phase 2 integration as Outcome D. |
| **Profile f(q/δ) reproduces Variant 3 Gaussian exactly** | Smuggling alert. If the derived core profile happens to be Gaussian, verify it follows from the regularization physics, not from parameter fitting. If the match is coincidental and traceable, accept. If it is engineered, reject and flag as CR2 violation. |

---

## 16. Bottom Line

WP2 eliminated the primary node-well candidate (N1: thin-junction
Israel energy) with a bounded no-go. Two active lanes remain:
N2 (bulk backreaction) and N7 (thick-junction/internal-core).

**The next execution lane is N7 (thick-junction core).** It directly
addresses the physics the thin-junction approximation discards, has
existing donor infrastructure (separable core ansatz, structural scaling),
no negative prior, and the correct energy-scale mechanism (geometric
amplification C ∝ (L₀/δ)²). N2 becomes the backup if N7 yields a
no-go.

The thick-junction lane is bounded: four checkpoints, explicit abort
signals, and anti-smuggling discipline (CR2 is the primary risk). A
no-go result is an allowed and informative outcome. If both N7 and N2
fail, the double-well postulate is falsified within the minimal 5D
model class — a significant negative result that constrains the theory.
