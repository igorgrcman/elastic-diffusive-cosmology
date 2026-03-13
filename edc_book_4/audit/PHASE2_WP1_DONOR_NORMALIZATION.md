# Phase 2 WP1: Donor Normalization and Put C Corridor Input Cleanup

**Date:** 2026-03-13
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Normalization task — no derivation, no implementation
**Governing document:** `edc_book_4/PHASE2_PLAN_V1.md`

---

## 1. Executive Verdict

The donor base for Phase 2 WP2 is now inventoried, classified, and
normalized. **Fourteen donor assets** were inspected across six branches.
Seven are cleared for WP2 use (three central, four supporting). Five are
archived as dead-end/no-go references. Two are classified as forbidden
positive donors (circular or phenomenological content that must not be
imported as [Dc]).

The Put C substeps C1–C4 have been normalized to stable definitions.
C1 is complete [Def]. C2 is the core open step — explicit integration
of S_total components. C3 and C4 are downstream of C2.

The node-well problem has exactly one admissible physical hypothesis
(Israel junction energy) and one speculative backup (bulk backreaction).
All other historical candidates are either falsified (Helfrich, ξ-BC) or
circular (phenomenological Gaussian well, C = 100).

**The donor base is clean enough for WP2 to begin**, provided the
explicit allowed/forbidden import lists in §10–§11 are respected.

---

## 2. Scope of WP1

### Files/Branches Inspected

| # | Source | Files | Purpose |
|---|--------|-------|---------|
| 1 | Current branch | `PHASE2_PLAN_V1.md`, `BOOK4_NEUTRONLINE_FINAL_STATUS.md`, `PHASE1_INTEGRATION_STATUS.md`, `app_Vq_chosen_path.tex`, `ch03`, `ch06` | Canonical Phase 1/2 status |
| 2 | `putC-computation-v1` | `S5D_TO_SEFF_Q_REDUCTION.md`, `PUTC_EXECUTION_REPORT.md`, `putC_compute_MV.py`, `putC_results.json` | Put C corridor + 3 model variants |
| 3 | `taskB-derive-Mq-v1` | `DERIVE_MQ_FROM_ACTION.md` | M(q) derivation framework |
| 4 | `junction-core-derive-C-v1` | `DERIVE_C_FROM_GEOMETRY.md` | C = (L₀/δ)² structure |
| 5 | `helfrich-well-from-action-v1` | `HELFRICH_EXECUTION_REPORT.md` | Helfrich NO-GO (260/260) |
| 6 | `frozen-brane-bc-v1` | `01_MODEL_AND_DEFINITION.md` through `07_VERDICT.txt` | ξ-BC NO-GO |

### Scope Limitation

This document normalizes and classifies donor material. It does not
derive new results, write appendix content, or implement any Phase 2
computation.

---

## 3. Minimal Canonical Donor Set

These are the **central donor assets** WP2 is authorized to build upon.

| # | Asset | Location | Purpose | Quality | Reusable |
|---|-------|----------|---------|---------|----------|
| **D1** | Put C formal corridor (C1–C4) | `putC-computation-v1` : `S5D_TO_SEFF_Q_REDUCTION.md` | Canonical 5D→1D reduction skeleton; defines S_total decomposition, ansatz class, integration procedure | [Dc] structural; explicit integrals [OPEN] | **YES — central** |
| **D2** | Put C execution report | `putC-computation-v1` : `PUTC_EXECUTION_REPORT.md` | Documents 3 model variants; establishes that minimal models fail; identifies node-well gap | [Dc/P/Cal] | **YES — central** |
| **D3** | V_geom(q) chosen-path appendix | Current branch : `app_Vq_chosen_path.tex` | Geometric sector [Dc]; single-well with Steiner minimum; curvature V''(0) = 3τ/(2R) | [Dc] (Phase 1 R3) | **YES — central** |

### What makes these central

- **D1** provides the formal structure WP2 must follow: the action
  decomposition S_total = S_bulk + S_brane + S_GHY + S_junction, the
  substep definitions C1–C4, and the target effective action form.
- **D2** provides the negative baseline: Variants 1–2 show what doesn't
  work; Variant 3 identifies the phenomenological node well as the gap.
- **D3** provides the validated geometric baseline V_geom [Dc] that
  any new non-geometric terms must combine with.

---

## 4. Supporting Donors

These provide useful methodology or structure but are not core to the
Put C derivation itself.

| # | Asset | Location | Purpose | Quality | Notes |
|---|-------|----------|---------|---------|-------|
| **S1** | M(q) derivation framework | `taskB-derive-Mq-v1` : `DERIVE_MQ_FROM_ACTION.md` | Canonical M(q) extraction methodology; resolves M(0) = 0 issue | [Dc] | Downstream of V(q); use if WP2 reaches step B7 |
| **S2** | Put C computation code | `putC-computation-v1` : `putC_compute_MV.py` | Tested numerical V(q) scanner; extend for new variants | [Cal] | Code infrastructure only; results are variant-dependent |
| **S3** | Junction-core C structure | `junction-core-derive-C-v1` : `DERIVE_C_FROM_GEOMETRY.md` | C ∝ (L₀/δ)² scaling [Dc]; supports M_core(q) | [Dc] structure / [I] value | Use structure only; value C = 100 is circular (see §5) |
| **S4** | ξ-BC mode analysis | `frozen-brane-bc-v1` : files 01–06 | Mode spectrum under various BC; GHY boundary term context | [Der] for modes; [Der] NO-GO for attraction | Methodology reference; BC don't create wells |

---

## 5. Forbidden / Dead-End / No-Go Donors

These must **not** be imported as positive evidence. They are preserved
as dead-end references that constrain what WP2 can attempt.

| # | Asset | Location | Why Not Reusable as Positive Donor | Preserved Lesson |
|---|-------|----------|------------------------------------|------------------|
| **F1** | Helfrich bending route | `helfrich-well-from-action-v1` : `HELFRICH_EXECUTION_REPORT.md` | 260/260 configurations tested, zero metastable wells. V_bend ~ +κq²/a² (positive quadratic) reinforces Nambu-Goto. With c₀ = 0, no attraction possible. **FALSIFIED.** | Bending rigidity κ ~ σδ² cannot source metastability. Do not revisit Helfrich as a node-well mechanism. |
| **F2** | ξ-BC as metastability source | `frozen-brane-bc-v1` : `07_VERDICT.txt` | V'_lin(d) > 0 for ALL BC types (Neumann, Robin, Dirichlet). BC affect mode spectrum but NOT sign structure. Minimum mechanism is topological (radial-frozen core), not BC. **FALSIFIED.** | Boundary conditions in the compact direction do not create attraction. The secondary minimum, if it exists, must come from junction-node or bulk-field physics, not ξ-BC alone. |
| **F3** | C = (L₀/δ)² = 100 as independent constraint | `junction-core-derive-C-v1` : `DERIVE_C_FROM_GEOMETRY.md` §6.4 | C = 100 uses L₀ = 1.0 fm [I] and δ = 0.1 fm [I] as inputs. The π factor from profile integral I_⊥ is dropped by ad hoc normalization. If kept, C = 314. **CIRCULAR.** | The *structure* C ∝ (L₀/δ)² is [Dc] — legitimate dimensional scaling. The *value* 100 is not independent. WP2 may use the scaling relation but must not cite C = 100 as derived evidence for L₀/δ = 10. |
| **F4** | Phenomenological node well (Put C Variant 3) | `putC-computation-v1` : `PUTC_EXECUTION_REPORT.md` §Variant 3 | V_node = −V₀ exp(−(q−q*)²/2w²) is a fitted Gaussian with no physical derivation. Parameters (V₀, q*, w) are tuned to produce V_B ≈ 2.8 MeV. **[P/Cal], not [Dc].** | Demonstrates that IF an attractive node term exists with certain properties, metastability is possible. Does not establish that such a term arises from S_5D. WP2 must derive the physical origin, not recycle the fitted profile. |
| **F5** | Flux quantization routes for L₀/δ | Pre-Phase 1 (v1 heuristic routes 3a–3c) | Three flux quantization attempts; none produced L₀/δ. **DEAD END.** | Flux quantization does not yield the geometric ratio. Not relevant to Put C V(q) derivation, but included to prevent accidental revival. |

---

## 6. Put C Vocabulary and Substep Normalization

### Canonical Definitions for Phase 2

The Put C corridor reduces the full 5D action to an effective 1D action.
The following substep definitions are drawn from D1 (`S5D_TO_SEFF_Q_REDUCTION.md`)
and normalized for Phase 2 use.

#### Total Action

```
S_total = S_bulk + S_brane + S_GHY + S_junction
```

| Component | Expression | Status |
|-----------|-----------|--------|
| S_bulk | ∫d⁵x √(−g₅) [R₅/(2κ₅²) + L_matter] | [Def] — Einstein-Hilbert + matter in 5D |
| S_brane | −σ ∫d⁴x √(−g₄^ind) | [Dc] — Nambu-Goto brane action with tension σ |
| S_GHY | (1/κ₅²) ∫d⁴x √(−h) K | [Def] — Gibbons-Hawking-York boundary term |
| S_junction | Junction matching conditions at Y-vertex | [Def] — Israel conditions at codim-2 defect |

#### Substeps

| Step | Name | Definition | Current Status | WP2 Target |
|------|------|-----------|----------------|------------|
| **C1** | Choose Ansatz Class | Parametrize configuration by slow coordinate q(t) (junction displacement from Steiner) and fast modes {ϕ_α}. q is a chosen collective coordinate [Dc], not uniquely derived. | **[Def]+[I] — Complete** | Reuse as-is |
| **C2** | Insert Ansatz into S_total | Substitute the q-dependent junction configuration into all four action components. Perform explicit integrals over extra-dimensional coordinates. | **[OPEN] — Core gap** | Perform explicit integrals; identify which terms generate V_node(q) |
| **C3** | Integrate Out Fast Modes | Born-Oppenheimer / adiabatic approximation: minimize over fast modes at fixed q. Requires timescale separation [P]. | **[OPEN] — Depends on C2** | Identify fast modes; verify separation |
| **C4** | Extract Canonical Form | Read off M(q) = ∂²L_eff/∂q̇² and V(q) = −L_eff(q, q̇=0). Identify all coefficients. | **[OPEN] — Depends on C2–C3** | Extract M(q), V(q) with traced coefficients |

#### Target Effective Action

```
S_eff[q] = ∫ dt [ ½ M(q) q̇² − V(q) ]
```

with V(q) decomposed as:

```
V(q) = V_geom(q) + V_node(q) + V_bulk(q) + ...
         [Dc]        [OPEN]      [OPEN]
```

### Key Terminology Normalization

| Term | Canonical Meaning (Phase 2) | Legacy Ambiguities |
|------|----------------------------|--------------------|
| **V_geom(q)** | Nambu-Goto arm-length contribution τ × L_tot(q). Phase 1 R3 [Dc]. Single-well. | Sometimes conflated with "full V(q)" in pre-Phase-1 text |
| **V_node(q)** | Energy contribution from the Y-junction vertex structure as q varies. Physical origin: to be determined in WP2. | Previously only a phenomenological Gaussian [P/Cal] in Variant 3 |
| **V_bulk(q)** | Energy contribution from bulk gravitational backreaction when junction displaces. | Not previously computed in any variant |
| **Node well** | Informal term for the attractive (negative) part of V_node(q) that could create a secondary minimum. | Must not be assumed to exist — WP2 tests whether it emerges from S_5D |
| **Double-well** | V(q) has two local minima (q = 0 anchor, q = q_n metastable) with barrier at q_B. | Currently [P]. WP2 tests whether this structure emerges |
| **Israel conditions** | Junction matching conditions for metric and extrinsic curvature across the Y-junction worldsheet. Codimension-2 generalization. | Not yet explicitly written for Y-junction in any donor file |
| **Put C** | The full 5D → 1D reduction corridor (C1–C4). | Sometimes used loosely for "any V(q) calculation"; in Phase 2, restricted to the formal corridor |

---

## 7. Node-Well Candidate Landscape

All known candidate mechanisms for generating a non-geometric attractive
term in V(q) are listed below.

| # | Candidate Mechanism | Source | Physical Basis | Status | Admissible for WP2? |
|---|--------------------|---------|----|--------|---------------------|
| **N1** | Israel junction energy (V_Israel) | D1 corridor definition; not yet computed | Junction node displacement changes the matching conditions across the Y-junction worldsheet. Gravitational energy stored in the junction vertex depends on q. | **[OPEN] — never computed for Y-junction** | **YES — primary candidate** |
| **N2** | Bulk gravitational backreaction (V_bulk) | D1 corridor; Variant 2 tested warped metric | Linearized gravity in 5D: bulk field configuration responds to junction displacement. Energy cost/gain from metric perturbation. | **[OPEN] — Variant 2 scan found no metastability in minimal warped models** | **YES — speculative backup** |
| **N3** | Warp-factor gradient coupling | Variant 2 (RS-like) | In a warped background, the warp factor A(ξ) creates a position-dependent tension. Moving the junction in q samples different warp factors. | **Partially tested [Dc] — no metastability found** | **Conditional — only if combined with N1 or new physics** |
| **N4** | Topological energy of compact-direction deformation | `frozen-brane-bc-v1` investigated | Deforming the junction in the compact ξ-direction changes the topological structure. | **Partially FALSIFIED — ξ-BC alone give V' > 0** | **Limited — cannot be sole source; might contribute if combined with N1** |
| **N5** | Helfrich bending rigidity | `helfrich-well-from-action-v1` | Bending energy κ(2H − c₀)² of the displaced junction dimple. | **FALSIFIED — 260/260 NO-GO** | **NO — dead end** |
| **N6** | Phenomenological Gaussian well | Variant 3 | V_node = −V₀ exp(−(q−q*)²/2w²). Fitted parameters. | **[P/Cal] — no physical origin** | **NO — forbidden as [Dc] donor; allowed only as comparison baseline** |

### Strongest Currently Admissible Hypothesis

**N1 (Israel junction energy)** is the primary admissible candidate. It is
the only mechanism that:
- arises from explicit terms in S_total (the junction matching conditions)
- has not been tested and falsified
- has a clear physical picture (junction displacement changes gravitational
  matching at the vertex)
- is tractable in principle (Israel conditions are standard GR formalism,
  though codimension-2 requires care)

**N2 (bulk backreaction)** is the backup. Variant 2 tested warped metrics
without finding metastability, but that scan used specific metric forms.
Bulk backreaction in a different background or with junction-sourced
perturbations could differ.

### What WP2 Must Explicitly Forbid Importing

- N5 (Helfrich) as a positive mechanism — FALSIFIED
- N6 (phenomenological Gaussian) as a [Dc] result — it is [P/Cal]
- Any "node well" term whose physical origin is not traced to an explicit
  integral in S_total
- The *value* C = 100 as independent evidence (see F3)

---

## 8. Scale and Symbol Normalization

### Canonical Scale Definitions for Phase 2

| Symbol | Canonical Meaning (Phase 2) | Value | Tag | Ambiguous Legacy Meanings |
|--------|-----------------------------|-------|-----|--------------------------|
| **σ** | Brane tension | 8.82 MeV/fm² | [Dc] (Book I) | None — consistently used |
| **δ** | Brane thickness / junction-core scale. Compton regularization: δ = ℏ/(2m_p c) | ≈ 0.105 fm | [I] | **AMBIGUOUS:** 4 distinct δ-like scales exist (see below). In Phase 2, δ refers exclusively to this Compton scale. |
| **L₀** | Characteristic junction extent in 5th dimension. Decay scale of junction wavefunction. | ≈ 1.0 fm | [I] | Sometimes conflated with arm length R or charge radius r_p. L₀ is the 5D localization length, not the 3D size. |
| **R** | Characteristic Y-junction arm length (distance from Steiner center to boundary point) | O(1) fm | [Dc] (geometric) | Sometimes confused with R₅. R is the in-brane arm length; R₅ is the compactification radius. |
| **R₅** | Compactification radius of the 5th dimension | Not derived | [P] | WP2 does not use R₅ directly (Put C corridor operates in the full 5D; compactification enters through background metric). |
| **q** | Collective coordinate: Y-junction node displacement from Steiner equilibrium | [0, R) | [Dc] (chosen path) | Must specify which displacement path (in-brane vs compact-direction). Phase 2 inherits the R3 in-brane path as primary model. |
| **κ₅²** | 5D gravitational coupling: κ₅² = 8πG₅ | Dimensional | [Def] | Must not be confused with κ = 2π (instanton topological winding, Ch.07). Different symbols in different chapters. |
| **τ** | String/edge tension (Nambu-Goto) | = σ in 2D brane context | [Dc] | Sometimes τ = brane tension in reduced dimensions; context-dependent. Phase 2 uses τ for the effective 1D string tension of Y-junction arms. |
| **V_B** | Barrier height measured from metastable minimum: V_B = V(q_B) − V(q_n) | ≈ 2.59 MeV [P] | [P] conjecture | Must not be imported as [Dc]. Phase 2 target is to compute V_B, not assume it. |
| **M(q)** | Effective mass of the collective coordinate q | Scaling: τR/c² | [P] | D-S1 (`DERIVE_MQ_FROM_ACTION.md`) provides a framework. Phase 2 may use the scaling as [P] baseline. |
| **E₀** | Junction-core ground-state energy: E₀ = C × σ × δ² | Scaling [Dc]; value depends on C | [Dc] structure / [I] value | The structural relation E₀ ∝ σδ² is [Dc]. The coefficient C depends on L₀/δ [I]. |

### The δ-Scale Ambiguity

Four distinct thickness-like scales exist in the repo (from D-S3,
`delta-audit-anchor-v1`):

| Scale | Value | Context | Phase 2 Usage |
|-------|-------|---------|---------------|
| R_ξ | ≈ 0.002 fm | Membrane correlation length (EW sector) | **Not used.** Wrong physical scale for junction-core problem. |
| Δ | ≈ 0.003 fm | Loop-state mass formula parameter | **Not used.** Different sector. |
| ℓ/(2π) | ≈ 0.002 fm | Orbifold radius | **Not used.** Compactification scale, not junction scale. |
| **δ** | **≈ 0.105 fm** | **Junction-core / brane thickness** | **Used.** This is the Compton regularization δ = ℏ/(2m_p c). |

**WP2 rule:** Phase 2 uses δ ≈ 0.105 fm [I] exclusively. The factor-50
ambiguity with R_ξ is acknowledged as a systematic uncertainty but is
**not resolved by Phase 2** (out of scope). If WP2 results depend
sensitively on the choice of δ, this must be reported as a residual risk.

---

## 9. Circularity / Smuggling Risk Register

| # | Risk | Mechanism | Anti-Smuggling Rule |
|---|------|-----------|---------------------|
| **CR1** | Importing V_B = 2Δm_np as derivation target | Tuning new V(q) model parameters to reproduce V_B ≈ 2.59 MeV, then calling the result [Dc]. | V_B must be computed BEFORE comparing to 2Δm_np. If matched by parameter adjustment → [Cal]. |
| **CR2** | Relabeling phenomenological node well | Taking the Variant 3 fitted Gaussian V_node and adding a post-hoc "derivation" that arrives at the same profile. | V_node must emerge from explicit S_total integrals. The functional form is an output, not an input. If the derived form happens to be Gaussian, that's fine — but the derivation must precede the form. |
| **CR3** | Background metric chosen to produce double-well | Scanning over metrics until one gives metastability, then declaring it "the EDC metric." | Background metric must be declared [I] or [P] at the start of WP2. If multiple metrics are tested, all results reported. |
| **CR4** | C = 100 imported as independent evidence | Using E₀ = 100 σδ² to set the energy scale of the node well, when C = 100 derives from L₀ = 1.0 fm [I] and δ = 0.1 fm [I]. | The *scaling* C ∝ (L₀/δ)² is [Dc] and may be used. The *value* 100 is [I]-dependent and must not be cited as independent confirmation. |
| **CR5** | τ_n used to constrain V(q) | Back-computing "what V_B must be" from measured τ_n, then declaring V(q) "derived." | τ_n [BL] appears ONLY in the final Ch.09 comparison. It must not enter the V(q) derivation. |
| **CR6** | Adiabatic coefficients absorbing the gap | Integrating out fast modes with undetermined numerical coefficients that are later fit to produce the desired V(q) shape. | Every coefficient in V(q) must trace to an explicit integral. Undetermined coefficients declared [P]. |
| **CR7** | Revival of Helfrich or ξ-BC mechanisms | Introducing bending terms or boundary-condition-based attraction under a new name. | WP2 must explicitly check new V_node terms against the Helfrich and ξ-BC no-go criteria. If a new term reduces to κq²/a² or V'(d) > 0 under the same limits, it inherits the no-go. |
| **CR8** | Conflating V_geom curvature with node energy | Attributing the Steiner curvature V''(0) = 3τ/(2R) to the node-well mechanism, when it is purely geometric. | V_geom [Dc] is a fixed, known baseline. Any new attractive term must be shown to be *additional* to V_geom, not a repackaging of it. |

---

## 10. WP2 Allowed Inputs

The following is the **canonical donor bundle** WP2 is authorized to use.

### Central Inputs

| Input | Source | Tag | What WP2 May Use |
|-------|--------|-----|------------------|
| Put C corridor structure (C1–C4) | D1 | [Dc] structural | Action decomposition, substep definitions, integration procedure |
| What minimal models show | D2 | [Dc/Cal] | Variants 1–2 no-go as baseline; Variant 3 as comparison target only |
| V_geom(q) = τ L_tot(q) | D3 | [Dc] | Geometric sector; Steiner minimum; curvature 3τ/(2R) |
| σ = 8.82 MeV/fm² | Book I | [Dc] | Brane tension |
| δ = ℏ/(2m_p c) ≈ 0.105 fm | Book I | [I] | Brane thickness scale |
| Δm_np ≈ 1.293 MeV | PDG | [BL] | Comparison target only; not derivation input |

### Supporting Inputs (Use If Needed)

| Input | Source | Tag | What WP2 May Use |
|-------|--------|-----|------------------|
| M(q) framework | S1 | [Dc] | Methodology for extracting M(q); use if WP2 reaches step B7 |
| putC_compute_MV.py | S2 | [Cal] | Code infrastructure; extend with new variants |
| C ∝ (L₀/δ)² scaling | S3 | [Dc] | Structural relation only; not the value C = 100 |
| ξ-BC mode spectrum | S4 | [Der] | Boundary condition methodology; GHY context |

### Assumptions WP2 Must State Upfront

1. **Background metric** — declared as [I] or [P] before any computation
2. **Adiabatic approximation** — timescale separation [P]; mode decoupling [P]
3. **Collective coordinate q** — chosen in-brane displacement path (inherited from R3) [Dc]
4. **Codimension-2 junction treatment** — specify whether Y-junction is treated as thin (distributional) or thick (regularized at scale δ)
5. **Which components of S_total are included** and which are neglected, with justification

---

## 11. WP2 Forbidden Imports

WP2 must **not** treat the following as settled or import them as [Dc]:

| Forbidden Import | Why |
|-----------------|-----|
| V_B = 2Δm_np | [P] conjecture. WP2 computes V_B; comparison is [Check] only. |
| Double-well structure of V(q) | [P]. WP2 tests whether it exists. Assuming it defeats the purpose. |
| Secondary minimum at q_n | [P]. Must be discovered, not assumed. |
| Phenomenological node well (Gaussian shape, fitted V₀/q*/w) | [P/Cal]. Physical origin must be derived, not recycled. |
| C = 100 as evidence for L₀/δ | [I]-dependent. Circular. |
| Helfrich bending as attraction source | FALSIFIED. |
| ξ-BC as attraction source | FALSIFIED. |
| τ_n ≈ 878 s as constraint on V(q) | [BL]. Comparison only; never enters derivation. |
| M(q) numerical value | [P] scaling only. If WP2 computes M(q), the computation is fresh. |
| ω₀ = 19 MeV | [P] dimensional estimate. Not to be imported as fixed. |

---

## 12. Bottom Line

The Put C donor base is now inventoried, classified, and normalized.
WP2 has three central donors (corridor skeleton, execution report with
negative results, geometric V(q) baseline), four supporting donors
(M(q) framework, computation code, C-scaling, ξ-BC methodology), and
five explicitly forbidden/dead-end references.

The node-well problem is precisely defined: **what physical term in
S_total generates an attractive contribution to V(q) at q_n > 0?** The
primary candidate is Israel junction energy (never computed for
Y-junctions). All other historical candidates are either falsified or
phenomenological.

The substep vocabulary (C1–C4) is stable. The symbol table is
normalized. The circularity risks are registered. The allowed and
forbidden import lists are explicit.

**WP2 may begin.** The donor base is clean. The problem is well-defined.
The guardrails are in place.
