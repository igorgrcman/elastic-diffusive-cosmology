# N2 WP1: Donor Normalization for Bulk Gravitational Backreaction Route

**Date:** 2026-03-13
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Normalization and model-scope setup — no derivation, no implementation
**Governing documents:**
- `PHASE2_PLAN_V1.md` (v1.1)
- `PHASE2_NEXTSTEP_PLAN_V1.md`
- `audit/PHASE2_WP1_DONOR_NORMALIZATION.md` (original Put C corridor)
- `audit/N7_WP1_DONOR_NORMALIZATION.md` (N7 thick-junction lane)
- `appendices/app_P2_WP2_Israel_nodewell.tex` (N1 bounded no-go)
- `appendices/app_P2_N7_core_nodewell.tex` (N7 bounded insufficiency)

---

## 1. Executive Verdict

The donor base for the N2 bulk gravitational backreaction lane has been
inspected, classified, and normalized. **V_bulk(q) has never been
computed anywhere in the repo** — not on any of the 90+ branches, not
in any appendix, not in any code file. No analytical or numerical
computation of the linearized 5D Einstein equations with a Y-junction
source exists.

The N2 lane has:
- One formal corridor definition (Put C C1–C4) that defines the action
  decomposition but performs no explicit bulk integral
- One negative prior (Variant 2: 125 warped metric combinations,
  zero metastability) that tested background warping but NOT
  junction-sourced perturbations
- One constraining result (WP2 Israel no-go: deficit angle ≡ 0,
  arm-interior energy ∝ V_geom)
- One further constraining result (N7 bounded insufficiency: monotone
  core profiles cannot produce metastability)
- Multiple derived 5D reduction results (OPR-19, 21, 22; M(q)
  framework; T* derivation) that demonstrate 5D variational methods
  but do not address V_bulk(q)
- No derived V_bulk(q) of any kind

**The donor base is thin but clean.** N2 WP2 would be building from
near-scratch: formal action structure + methodology templates from
other 5D sectors + constraining dead ends. This is simultaneously
the lane's weakness (no positive infrastructure to extend) and its
strength (no historical baggage or phenomenological forms to smuggle).

**N2 WP2 may begin**, provided the model-class boundary (§7), scale
normalization (§8), and anti-smuggling rules (§9) are respected.

---

## 2. Scope of N2 WP1

### Files/Branches Inspected

| # | Source | Key Files | Purpose |
|---|--------|-----------|---------|
| 1 | `putC-computation-v1` | `S5D_TO_SEFF_Q_REDUCTION.md`, `PUTC_EXECUTION_REPORT.md`, `putC_compute_MV.py`, `putC_results.json` | Put C corridor definition; Variants 1–3 |
| 2 | `taskB-derive-Mq-v1` | `DERIVE_MQ_FROM_ACTION.md` | M(q) derivation framework |
| 3 | `junction-core-derive-C-v1` | `DERIVE_C_FROM_GEOMETRY.md`, `JUNCTION_CORE_EXECUTION_REPORT.md` | Core ansatz (N7 donor; provides structural contrasts for N2) |
| 4 | `delta-audit-anchor-v1` | `DELTA_ANCHOR_MAP.md` | Scale hierarchy |
| 5 | `frozen-brane-bc-v1` | `01_MODEL_AND_DEFINITION.md` through `07_VERDICT.txt` | ξ-BC NO-GO |
| 6 | `helfrich-well-from-action-v1` | `HELFRICH_EXECUTION_REPORT.md` | Helfrich NO-GO |
| 7 | Current branch | `PHASE2_PLAN_V1.md`, `PHASE2_NEXTSTEP_PLAN_V1.md`, `PHASE2_WP1_DONOR_NORMALIZATION.md`, `N7_WP1_DONOR_NORMALIZATION.md`, `app_P2_WP2_Israel_nodewell.tex`, `app_P2_N7_core_nodewell.tex`, `app_Vq_chosen_path.tex`, `ch03_neutron_metastable.tex` | Phase 2 status, accepted results |
| 8 | Current branch (BLOCK-003) | `edc_papers/paper_gravity_block003/main.tex`, `cosmology_sigma_tilde_lane/TSTAR_DERIVATION_5D.md` | G_N program, T* derivation |
| 9 | Current branch (OPR chain) | `OPR19_G5_DERIVATION_REPORT.md`, `OPR21_VEFF_DERIVATION_REPORT.md`, `OPR21_BC_ISRAEL_REPORT.md`, `OPR22_GEFF_DERIVATION_REPORT.md` | 5D reduction methodology |
| 10 | Current branch (Paper 3) | `edc_papers/paper_3_series/04_companion_C_5d_reduction/`, `code/common/full5d_reduction.py` | 5D pipeline roadmap, code skeleton |
| 11 | Current branch (mining) | `edc_book_2/audit/jsonl_mining/special/f_bulk_full.md` | Numerological G formula |

### Full Branch Scan

A search across all 90+ branches for "bulk backreaction," "V_bulk,"
"linearized gravity," "metric perturbation," "kappa_5," "M_5,"
"Randall-Sundrum," "5D Einstein" confirmed that **no branch contains
an analytical computation of V_bulk(q)** — the bulk gravitational
energy change as a function of junction displacement q.

### What This Document Does

- Defines the N2 lane precisely and distinguishes it from N1, N7, and
  phenomenological routes
- Inventories all bulk/gravity-related donor material
- Separates formal definitions from computed results from circular content
- Normalizes scales and symbols for the bulk backreaction lane
- Defines the admissible model class for N2 WP2
- Establishes anti-smuggling rules specific to the bulk sector

### What This Document Does Not Do

- No derivation. No new equations. No implementation.
- Does not solve linearized Einstein equations — that is N2 WP2 work.
- Does not determine V_bulk(q) sign, magnitude, or shape.
- Does not resolve M_5 or the background metric choice.

---

## 3. Definition of the N2 Lane

### 3.1 Precise Lane Definition

**N2 tests whether the 5D bulk gravitational response to junction
displacement generates a q-dependent energy contribution V_bulk(q)
that could create a secondary minimum in V(q).**

When the Y-junction node displaces from Steiner equilibrium (q = 0) to
q > 0, the stress-energy distribution on the brane changes. The bulk
metric must adjust to satisfy the 5D Einstein equations with the
modified source. The change in total gravitational energy of the
bulk+brane+junction system as a function of q defines V_bulk(q):

```
V_bulk(q) = E_grav[g(q)] - E_grav[g(0)]
```

where g(q) is the 5D metric sourced by the junction at displacement q,
and E_grav is the gravitational energy functional (bulk + GHY + Israel
contributions evaluated on the perturbed metric).

### 3.2 How N2 Differs from Other Lanes

| Aspect | N1 (Israel thin-junction) | N7 (Thick-junction core) | N2 (Bulk backreaction) | Phenomenological |
|--------|--------------------------|-------------------------|----------------------|-----------------|
| **What varies with q** | Junction matching conditions at zero-width vertex | Internal stress configuration in core of width δ | Bulk metric field sourced by displaced junction | Nothing physical; V_node is postulated |
| **Where energy lives** | On the junction worldline (distributional) | Inside the regularized core (r⊥ < r₀) | In the 5D bulk spacetime (away from brane) | In a fitted function |
| **Physical mechanism** | Deficit-angle curvature at codim-2 defect | Elastic strain/binding in finite-size vertex | Gravitational field response to source displacement | None (phenomenological) |
| **What equations govern it** | Israel matching [K_ab] − h_ab[K] = −κ₅² S_ab | Core elasticity / regularized junction dynamics | Linearized 5D Einstein: δR_AB − ½g_AB δR = κ₅² δT_AB | None (parameter fit) |
| **Scale set by** | Brane tension σ; deficit angle Δθ | Core energy E₀ = σL₀²; profile f(q/δ) | κ₅² = 8πG₅ = 8π/M₅³; bulk curvature scales | Fitted V₀, q*, w |
| **Current status** | **Bounded no-go** [Dc] | **Bounded insufficiency** [Dc] | **[OPEN] — never computed** | [P/Cal] — not derivation |
| **Key risk** | (Dead) | CR2: relabeling Gaussian | κ₅²-suppression → too small | CR2: relabeling |

### 3.3 Why N2 Is Distinct

N2 is the only surviving candidate that:

1. **Involves the bulk metric field itself.** N1 and N7 concern physics
   at the junction (matching conditions or core structure). N2 concerns
   physics in the 5D bulk spacetime.

2. **Is governed by the Einstein equations.** N1 uses Israel conditions
   (which are derived from the Einstein equations at a boundary), but
   the N1 no-go showed these conditions produce Δθ ≡ 0 and tension
   renormalization only. N2 uses the full linearized field equations
   in the bulk, which could generate energy contributions not visible
   in the boundary matching.

3. **Has never been tested with junction-sourced perturbations.** The
   Put C Variant 2 scan tested background warping (different fixed
   metrics) but did NOT solve for the metric response to a displaced
   junction. These are different computations.

---

## 4. Minimal Canonical Donor Set

These are the **central donor assets** the N2 lane is authorized to
build upon.

| # | Asset | Location | Content | Quality | Reusable? |
|---|-------|----------|---------|---------|-----------|
| **D-N2-1** | Put C corridor (C1–C4) | `putC-computation-v1` : `S5D_TO_SEFF_Q_REDUCTION.md` | Formal action decomposition S_total = S_bulk + S_brane + S_GHY + S_junction. Defines integration procedure, target S_eff[q] = ∫ dt [½M(q)q̇² − V(q)]. Steps C2–C4 [OPEN]. | [Def] structural | **YES — central.** Provides the formal skeleton. N2 executes the bulk sector of C2. |
| **D-N2-2** | V_geom(q) geometric baseline | Current branch : `app_Vq_chosen_path.tex` | V_geom(q) = τ L_tot(q) [Dc]. Steiner minimum at q = 0. Curvature V''(0) = 3τ/(2R). Single-well. V(q) = V_geom + V_node + V_bulk + ... where V_bulk is [OPEN]. | [Dc] (Phase 1 R3) | **YES — central.** Any bulk contribution must combine with this baseline. |
| **D-N2-3** | Put C Variant 1–2 negative results | `putC-computation-v1` : `PUTC_EXECUTION_REPORT.md` | Variant 1 (flat bulk): V(q) monotonically increasing, no metastability. Variant 2 (warped/RS-like): 125 parameter combinations, no metastability. | [Dc] (Variant 1); [Dc/P] (Variant 2) | **YES — central.** Establishes negative baseline. N2 must explain why junction-sourced perturbations produce a different result than background warping. |

### What Makes These Central

- **D-N2-1** defines the action that N2 must integrate. V_bulk arises
  from the S_bulk component evaluated on the junction-displaced
  configuration.
- **D-N2-2** provides the validated geometric baseline. V_bulk must
  combine with V_geom to form V(q).
- **D-N2-3** provides the negative baseline. Variants 1–2 show that
  naive warped metrics do not produce metastability. N2 must go beyond
  this — either by solving the actual Einstein equations with a junction
  source, or by showing that the Variant 2 scan missed a physical
  effect.

---

## 5. Supporting Donors

| # | Asset | Location | Content | Quality | Notes |
|---|-------|----------|---------|---------|-------|
| **S-N2-1** | M(q) derivation framework | `taskB-derive-Mq-v1` : `DERIVE_MQ_FROM_ACTION.md` | M(q) = M_NG(q) + M_core(q) from 5D kinetic term. Methodology for extracting the effective mass function from the 5D reduction. | [Dc] structural | Downstream of V(q); use if N2 WP2 reaches kinetic sector. Shows how 5D → 1D reduction works for the kinetic term — methodological template for the potential term. |
| **S-N2-2** | Put C computation code | `putC-computation-v1` : `putC_compute_MV.py` | Tested V(q) scanner for 3 model variants. | [Cal] code | Infrastructure. May be extendable if N2 produces a computable V_bulk(q). |
| **S-N2-3** | OPR-21 V_eff(ξ) for fermion localization | `edc_book_2/audit/evidence/OPR21_VEFF_DERIVATION_REPORT.md` | Derives V_L(ξ) = [M(ξ) + 2A'(ξ)]² − [M(ξ) + 2A'(ξ)]' from 5D Dirac action in warped background. SUSY QM form. | [Dc] conditional on A(ξ) [P] | **Methodological template.** Shows how a 5D action produces an effective potential in a reduced coordinate via explicit integration. Different sector (fermion), but the reduction methodology (variational principle → eigenvalue problem → effective potential) is transferable. |
| **S-N2-4** | OPR-19 warp cancellation | `edc_book_2/audit/evidence/OPR19_G5_DERIVATION_REPORT.md` | In gauge kinetic reduction, warp factors e^{4A} and e^{−4A} cancel exactly. | [Dc] conditional | **Caution donor.** The gauge sector has simpler warp dependence than the gravitational sector. This does NOT imply warp cancellation in V_bulk. But it provides context for how warp factors enter and cancel (or don't) in different sectors. |
| **S-N2-5** | Robin BC from Israel junction | `edc_book_2/audit/evidence/OPR21_BC_ISRAEL_REPORT.md` | Robin BC f'(0) + (m_b/2)f(0) = 0 derived from 5D Dirac variational principle with brane mass. Israel conditions stated: [K_ab] − g_ab[K] = −(1/M₅³) S_ab. | [Dc] conditional | **BC reference.** The linearized bulk perturbation equation in N2 will require boundary conditions at the brane. The Robin BC structure from Israel matching provides a template. |
| **S-N2-6** | T* derivation from 5D action | `edc_papers/paper_gravity_block003/cosmology_sigma_tilde_lane/TSTAR_DERIVATION_5D.md` | T* = C × M₅³ from Israel junction conditions. Defines κ₅² = 8π/M₅³, AdS length ℓ² = −6/Λ₅. | [Dc] structural | **Scale reference.** Provides the structural relation between brane tension σ, bulk cosmological constant Λ₅, and 5D Planck mass M₅. These enter V_bulk through the gravitational coupling. |
| **S-N2-7** | G_eff from 5D mediator exchange | `edc_book_2/audit/evidence/OPR22_GEFF_DERIVATION_REPORT.md` | G_eff = g₅² ℓ / (2x₁²) |f₁(0)|² from KK reduction + mediator exchange. | [Dc] conditional | **Normalization reference.** Provides the derived structure for how 5D gravitational physics projects to 4D. The KK mode structure (eigenvalues x_n, profiles f_n) may enter V_bulk through the Green's function expansion. |
| **S-N2-8** | 5D reduction code skeleton | `edc_papers/paper_3_series/code/common/full5d_reduction.py` | Python module defining BulkMetricParams, warp factor family, GateResult tri-state. Flag USE_FULL5D_REDUCTION = False. | [OPEN] code | Skeleton infrastructure. Defines data structures for bulk metric parameters. Not yet functional. |
| **S-N2-9** | Companion Note C: 5D reduction pipeline | `edc_papers/paper_3_series/04_companion_C_5d_reduction/paper/main.tex` | Paper-grade pipeline for 5D → 1D reduction. Covers bulk geometry ansatz, brane embedding, induced geometry, extrinsic curvature, Israel conditions, extraction of M(q) and V(q). | Mixed [Der]/[Dc]/[P]/[OPEN] | **Pipeline roadmap.** Provides the formal chain of steps for the reduction. Actual integrals remain OPEN. |

---

## 6. Forbidden / Circular / Dead-End Donors

These must **not** be imported as positive evidence for the N2 lane.

| # | Asset | Location | Why Not Reusable as Positive Donor | Preserved Lesson |
|---|-------|----------|------------------------------------|------------------|
| **F-N2-1** | N1 Israel thin-junction energy | `app_P2_WP2_Israel_nodewell.tex` | **Bounded no-go** [Dc]. Deficit angle ≡ 0 (coplanar geometry). Arm-interior Israel energy ∝ V_geom (tension renormalization only). **BOUNDED NO-GO.** | Thin-junction matching cannot generate attraction. The bulk backreaction route is specifically about physics NOT captured by the thin-junction Israel conditions. N2 must demonstrate that its mechanism produces q-dependent energy beyond what Israel matching delivers. |
| **F-N2-2** | N7 thick-junction core (monotone profiles) | `app_P2_N7_core_nodewell.tex` | **Bounded insufficiency** [Dc]. Monotone profiles peaked at q = 0 produce V_core'(q) ≥ 0 for q > 0 → no secondary minimum. Core reinforces geometric restoring force. | The thick-junction core mechanism is distinct from bulk backreaction. N2 must not conflate "bulk gravitational response to junction displacement" with "internal core energy of the junction vertex." These are different physics. |
| **F-N2-3** | Phenomenological node well (Variant 3) | `PUTC_EXECUTION_REPORT.md` §Variant 3 | V_node = −V₀ exp(−(q−q*)²/2w²) with fitted parameters V₀ = 10 MeV, q* = 2 fm, w = 0.4 fm. **[P/Cal], not [Dc].** | Demonstrates that IF an attractive term exists with O(10 MeV) depth centered at q* > 0, metastability is achievable. Comparison target only. N2 must derive V_bulk from Einstein equations, not recycle this fitted form. |
| **F-N2-4** | Helfrich bending route | `helfrich-well-from-action-v1` : `HELFRICH_EXECUTION_REPORT.md` | 260/260 NO-GO. V_bend ~ +κq²/a² (positive). **FALSIFIED.** | Bending rigidity cannot source metastability. Do not reintroduce as a "curvature contribution" to V_bulk. |
| **F-N2-5** | ξ-BC as metastability source | `frozen-brane-bc-v1` : `07_VERDICT.txt` | V'_lin(d) > 0 for ALL BC types. BC affect mode spectrum but not sign structure. **FALSIFIED.** | Boundary conditions alone cannot create attraction. N2 boundary conditions (at brane, at AdS boundary) constrain the bulk perturbation but do not generate the attractive potential. |
| **F-N2-6** | C = (L₀/δ)² = 100 | `DERIVE_C_FROM_GEOMETRY.md` §6.4 | [I]-dependent value. **CIRCULAR.** | This is an N7 quantity, not an N2 quantity. V_bulk does not involve the junction-core geometric amplification factor C. Must not import C = 100 into the N2 lane under any guise. |
| **F-N2-7** | F_bulk numerological formula | `edc_book_2/audit/jsonl_mining/special/f_bulk_full.md` | F_bulk = c⁴ R_ξ¹² / (32π r_e¹³) is a numerological identification [I] with fitted powers (12, 13). Not derived from 5D action. | This "F_bulk" is NOT V_bulk(q). It is a separate formula relating bulk physics to Newton's constant. Must not be conflated with the V_bulk(q) that N2 seeks to derive. The name collision is dangerous. |
| **F-N2-8** | Variant 2 as positive evidence | `PUTC_EXECUTION_REPORT.md` §Variant 2 | 125 warped metric combinations, zero metastability. But this tested fixed warped backgrounds, NOT the metric response to a displaced junction. | **The negative result is valid but its scope must be respected.** It shows that changing the background metric (different A(ξ)) does not produce metastability in V_geom(q; A). It does NOT show that the metric perturbation δg_AB sourced by junction displacement fails to produce attraction. These are different questions. N2 addresses the latter. |

---

## 7. Model-Class Boundary for N2

### 7.1 What N2 Is (Admissible Model Scope)

The N2 lane tests whether **the bulk gravitational field energy,
computed from the linearized 5D Einstein equations with the displaced
Y-junction as source**, produces a q-dependent contribution to V(q)
that can create a secondary minimum.

**Admissible model class:**

1. **Start from the 5D Einstein-Hilbert action** (from D-N2-1):
   ```
   S_bulk = (1/2κ₅²) ∫ d⁵x √(−g₅) (R₅ − 2Λ₅)
   ```
   This is the bulk component of S_total.

2. **Declare a background metric** [I] or [P]:
   ```
   ds² = e^{2A(ξ)} η_μν dx^μ dx^ν + dξ²
   ```
   The warp factor A(ξ) and cosmological constant Λ₅ define the
   background. At minimum, flat (A = 0, Λ₅ = 0) and RS-like
   (A = −k|ξ|, Λ₅ < 0) should be tested.

3. **Linearize around the background** with the junction displacement
   as source:
   ```
   g_AB = ḡ_AB + h_AB(q)
   ```
   where h_AB(q) is the metric perturbation sourced by the junction at
   displacement q. The source term δT_AB encodes the change in brane
   stress-energy from q ≠ 0.

4. **Solve the linearized equations** (or bound the solution):
   ```
   δG_AB = κ₅² δT_AB
   ```
   with appropriate boundary conditions at the brane (Israel-derived)
   and at the bulk boundary (e.g., AdS asymptotics, Z₂ orbifold).

5. **Extract V_bulk(q)** from the total gravitational energy:
   ```
   V_bulk(q) = -(1/2κ₅²) ∫ d⁴x dξ √(−ḡ) h^AB G_AB^(1)[h] + ...
   ```
   or equivalently from the on-shell action evaluated at the perturbed
   solution.

6. **Combine with V_geom:**
   ```
   V(q) = V_geom(q) [Dc] + V_bulk(q) [Dc|model]
   ```
   and determine whether double-well structure exists.

### 7.2 What N2 Is Not (Forbidden Moves)

| Forbidden Move | Why | Anti-Smuggling Rule |
|----------------|-----|---------------------|
| Postulating V_bulk(q) = −V₀ × g(q) with fitted g | CR2: relabeling phenomenological well | V_bulk must emerge from solving (or bounding) linearized Einstein equations, not from postulating a functional form. |
| Choosing A(ξ) to produce double-well | CR3: background metric chosen post-hoc | A(ξ) must be declared [I] or [P] before computing V_bulk. If multiple backgrounds are tested, all results must be reported. |
| Tuning κ₅² or M₅ to make V_bulk match V_B ≈ 2.6 MeV | CR1: calibration dressed as derivation | V_bulk is computed at declared M₅ [P]. If V_bulk ≈ 2Δm_np only for a specific M₅, report M₅ dependence explicitly and tag as [Dc|model, M₅-dependent]. |
| Importing the thick-junction core profile as a "bulk" effect | Lane conflation | V_bulk is the bulk gravitational field energy, not the junction-core internal energy. The core is N7; the bulk is N2. These are physically distinct contributions. |
| Using τ_n to constrain V_bulk | CR5: output used as input | τ_n [BL] appears only in the final Ch.09 comparison. |
| Importing Variant 2 negative results as "bulk backreaction tested" | Scope conflation (F-N2-8) | Variant 2 tested different background metrics, not junction-sourced perturbations. These are different computations. N2 is about the perturbative response. |
| Absorbing undetermined coefficients from mode integration into V_bulk shape | CR6: adiabatic coefficients absorbing the gap | Every coefficient in V_bulk must trace to an explicit integral or Green's function evaluation. Undetermined coefficients must be declared [P]. |

### 7.3 What Would Count as Smuggling

**The smuggling test for N2:** Before N2 WP2 can claim a result, the
following must pass:

> **Delete all knowledge of τ_n, V_B ≈ 2.6 MeV, the Variant 3
> Gaussian form, and the desired double-well shape from the derivation.
> Does the linearized Einstein equation still have the same solution?
> Does V_bulk(q) still have the same sign and shape?**

If yes: the result is honest [Dc|model].
If no: the result is [Cal] dressed as [Dc].

---

## 8. Scale and Symbol Normalization

### 8.1 Essential N2 Symbols

| Symbol | Canonical Meaning (N2 Lane) | Value / Status | Tag | Ambiguities / Notes |
|--------|-----------------------------|----------------|-----|---------------------|
| **κ₅²** | 5D gravitational coupling: κ₅² = 8πG₅ = 8π/M₅³ | Dimensional | [Def] | **Must not be confused with κ = 2π** (instanton topological winding, Ch.07). Different quantities. In N2 context, κ₅² is always the gravitational coupling. |
| **M₅** | 5D Planck mass | Not derived | [P] | Never independently derived on any branch. Enters V_bulk through κ₅² = 8π/M₅³. The value of M₅ controls whether V_bulk is large enough to compete with V_geom. |
| **G₅** | 5D Newton's constant: G₅ = 1/M₅³ | Not derived | [P] | Equivalent to M₅ through dimensional analysis. |
| **Λ₅** | 5D (bulk) cosmological constant | Not derived | [P] or [I] | Enters the background metric through ℓ² = −6/Λ₅ (AdS length). If Λ₅ = 0, the bulk is flat. If Λ₅ < 0, the bulk is AdS. Must be declared before computation. |
| **ℓ** | AdS curvature length: ℓ = √(−6/Λ₅) | From Λ₅ | [P] or [I] | Exists only if Λ₅ < 0 (AdS bulk). Sets the scale of warp decay. In RS models, ℓ = 1/k where k is the RS curvature parameter. |
| **k** | RS curvature parameter: A(ξ) = −k|ξ| | From Λ₅ | [P] or [I] | k = 1/ℓ in standard RS. Controls warp factor decay. In Variant 2, k was scanned over but no metastability found. |
| **A(ξ)** | Warp factor in bulk metric | Function [P] or [I] | [P] or [I] | The central model input for N2. Different A(ξ) choices (flat, RS, general AdS) give qualitatively different V_bulk(q). Must be declared before computation. |
| **h_AB(q)** | Metric perturbation sourced by junction at displacement q | To be solved | [OPEN] | This is the N2 unknown. Solving for h_AB is the core of N2 WP2. |
| **δT_AB(q)** | Change in brane stress-energy from q ≠ 0 | Computable from brane embedding | [Dc] once computed | The source term for the linearized Einstein equations. Depends on the junction configuration (arm lengths, angles) at displacement q. Not yet computed. |
| **σ** | Brane tension | 8.82 MeV/fm² | [Dc] | Enters δT_AB through the Nambu-Goto stress-energy. Same as in N1 and N7. |
| **q** | Collective coordinate: junction node displacement from Steiner | [0, R) | [Dc] (chosen path) | Same as in all previous lanes. Inherited from R3. |
| **R** | Y-junction arm length | O(1) fm | [Dc] geometric | Same as previous. |
| **δ** | Junction-core scale (Compton anchor) | ℏ/(2m_p c) ≈ 0.105 fm | [I] | In N2, δ appears only if the junction source is regularized (smoothed rather than distributional). If the junction is treated as thin (distributional source), δ does not enter the bulk perturbation equation directly. |

### 8.2 Curvature / Warp / Backreaction Scale Ambiguity

The N2 lane introduces several length/energy scales from the bulk
gravitational sector that are NOT present in N1 or N7. These must be
explicitly tracked.

| Scale | Definition | Relation to Other Scales | Status |
|-------|-----------|--------------------------|--------|
| **1/M₅** | 5D Planck length | Gravitational coupling scale | [P] — never derived |
| **ℓ = √(−6/Λ₅)** | AdS curvature length | Warp decay scale; RS: ℓ = 1/k | [P] or [I] — from background metric choice |
| **r_c = πℓ** | Compactification radius (RS2 convention) | Size of extra dimension | [P] — related to R₅ |
| **R₅** | Compactification radius (EDC convention) | R₅ = πδ [P] in heuristic routes | [P] — never derived |
| **κ₅²σ** | Dimensionless bulk response parameter | Controls how much the bulk deforms per unit brane tension | [Def] — determines V_bulk magnitude |

**The central ambiguity:** V_bulk(q) scales as κ₅² × (energy density)
× (volume). The energy density comes from the brane stress-energy
(∝ σ). The volume depends on the background geometry (∝ ℓ, R₅). The
magnitude of V_bulk relative to V_geom depends on the combination
κ₅² σ ℓ, which is undetermined.

**N2 rule:** The values M₅, Λ₅ (or equivalently ℓ, k) must be
declared as [P] or [I] at the start of N2 WP2. V_bulk must be
reported as a function of these parameters, not evaluated at a single
"best" value.

### 8.3 The κ₅²-Suppression Concern

A central concern for N2 (noted in `PHASE2_NEXTSTEP_PLAN_V1.md` §5)
is that bulk backreaction energies are generically κ₅²-suppressed:

```
V_bulk(q) ~ κ₅² × (source strength)² × (Green's function) ~ σ²/M₅³ × geometric factors
```

With σ ≈ 8.82 MeV/fm² and M₅ unknown, the magnitude of V_bulk cannot
be estimated without specifying M₅.

**Dimensional estimate (if V_bulk ~ σ²R³/M₅³):**
- If M₅ ~ 10 GeV: V_bulk ~ O(10 MeV) — potentially relevant
- If M₅ ~ 100 GeV: V_bulk ~ O(10⁻⁴ MeV) — negligible
- If M₅ ~ M_Pl,4D: V_bulk ~ O(10⁻³⁷ MeV) — irrelevant

**N2 rule:** If V_bulk is κ₅²-suppressed and quantitatively irrelevant
for any reasonable M₅, this is a valid no-go result: the mechanism
exists but is too weak. This must be documented honestly, not hidden.

### 8.4 The δ-Scale in N2

In N2, δ plays a different role than in N7:

| Lane | Role of δ |
|------|----------|
| **N7** | Core decay scale: V_core(q) = −E₀ f(q/δ). The profile width is set by δ. |
| **N2** | **Source regularization** (optional): if the junction source δT_AB is distributional (thin brane), δ does not appear in the bulk equation. If the source is smoothed at scale δ, it provides a UV cutoff for the Green's function. |

**N2 rule:** If the junction source is treated as distributional (thin
brane), state this as a model assumption. If regularized at scale δ,
state the regularization prescription. In either case, δ enters at
most as a cutoff, not as a dominant scale for V_bulk shape.

---

## 9. Circularity / Smuggling Risk Register (N2-Specific)

All risks from the original WP1 §9 and N7 WP1 §9 are inherited where
applicable. N2 adds specific risks from the bulk gravitational sector.

| # | Risk | Mechanism | Anti-Smuggling Rule |
|---|------|-----------|---------------------|
| **CR1** | V_B = 2Δm_np imported as constraint | Tuning M₅ or A(ξ) to reproduce V_B ≈ 2.59 MeV | V_bulk is computed before comparing to 2Δm_np. Comparison is [Check], not derivation. If V_bulk ≈ 2Δm_np only for specific M₅, tag as [Cal]. |
| **CR2** | Relabeling phenomenological well | Postulating V_bulk(q) = −V₀ exp(−(q−q*)²/2w²) without deriving it from Einstein equations | V_bulk must emerge from solving (or rigorously bounding) linearized 5D Einstein equations. The functional form is an output, not an input. |
| **CR3** | Background metric chosen to produce double-well | Scanning A(ξ) until one gives metastability, then declaring it "the EDC background" | A(ξ) declared [I] or [P] at start. All tested backgrounds reported. If only one background works, this is [Dc|model, metric-dependent], not [Dc]. |
| **CR5** | τ_n used to constrain V_bulk | Back-computing required V_bulk from measured τ_n | τ_n [BL] never enters V_bulk derivation. Final comparison in Ch.09 only. |
| **CR6** | Adiabatic coefficients absorbing the gap | Undetermined coefficients from mode integration or Green's function truncation fitted to produce desired V_bulk shape | Every coefficient must trace to an explicit integral or mode sum. Truncation errors bounded explicitly. |
| **CR12** (new) | κ₅²-suppression ignored or circumvented | Claiming V_bulk is large without justifying why the generic κ₅² suppression is overcome | V_bulk magnitude must be computed or bounded with explicit M₅ dependence. If V_bulk ∝ κ₅² and is small, report as quantitative no-go. Do not introduce non-gravitational forces to boost V_bulk. |
| **CR13** (new) | Variant 2 negative results reinterpreted as positive | Claiming that Variant 2 "shows warping helps" when it actually found zero metastability | Variant 2 is a NEGATIVE result [Dc/P]. Any N2 claim must explain specifically what the linearized perturbation computation adds beyond Variant 2's background metric scan. |
| **CR14** (new) | Bulk and core conflated | Importing N7 thick-junction core energy under the label "bulk contribution" | V_bulk is the bulk gravitational field energy (away from the brane). V_core is the internal junction energy (at the brane). These are distinct physical contributions. If N2 WP2 includes both, they must be separated and separately tagged. |
| **CR15** (new) | Green's function IR divergence absorbed into V_bulk | If the linearized Green's function has an IR divergence (e.g., in flat 5D without compact direction), the regularization could introduce arbitrary parameters | If the Green's function requires IR regularization (compactification, AdS boundary), the regularization must be declared [P] or [I] and its impact on V_bulk quantified. |
| **CR16** (new) | M₅ chosen to make mechanism work | Selecting M₅ specifically so that κ₅²-suppression doesn't kill V_bulk | M₅ must be declared as [P] before computing V_bulk. If V_bulk is relevant only for M₅ in a narrow range, document the range and tag as [Dc|model, M₅-dependent]. |

---

## 10. Allowed Inputs for N2 WP2

### Central Inputs

| Input | Source | Tag | What N2 WP2 May Use |
|-------|--------|-----|---------------------|
| Put C corridor structure (C1–C4) | D-N2-1 | [Def] structural | Action decomposition, integration procedure, target S_eff[q] form |
| S_bulk = (1/2κ₅²) ∫ d⁵x √(−g₅)(R₅ − 2Λ₅) | D-N2-1 | [Def] | Bulk Einstein-Hilbert action to be integrated |
| V_geom(q) = τ L_tot(q) | D-N2-2 | [Dc] | Geometric baseline; Steiner minimum; curvature 3τ/(2R) |
| Variant 1–2 negative results | D-N2-3 | [Dc]/[Dc/P] | Negative baseline: background warping alone does not produce metastability |
| σ = 8.82 MeV/fm² | Book I | [Dc] | Brane tension (enters δT_AB) |
| Δm_np ≈ 1.293 MeV | PDG | [BL] | **Comparison target only; NOT derivation input** |
| WP2 Israel no-go | F-N2-1 | [Dc] NO-GO | Constraint: thin-junction matching produces no attraction |
| N7 bounded insufficiency | F-N2-2 | [Dc] NO-GO | Constraint: monotone thick-junction profiles cannot produce secondary minimum |

### Supporting Inputs (Use If Needed)

| Input | Source | Tag | What N2 WP2 May Use |
|-------|--------|-----|---------------------|
| M(q) framework | S-N2-1 | [Dc] structural | Methodology for extracting kinetic term; if N2 reaches kinetic sector |
| putC_compute_MV.py | S-N2-2 | [Cal] code | V(q) scanner infrastructure; extend with new V_bulk model |
| V_eff(ξ) derivation methodology | S-N2-3 | [Dc] conditional | Template for 5D → effective-potential reduction |
| Robin BC structure | S-N2-5 | [Dc] conditional | Boundary conditions for linearized bulk perturbation at brane |
| T* = C × M₅³ | S-N2-6 | [Dc] structural | Scale relations between σ, Λ₅, M₅ |
| G_eff KK structure | S-N2-7 | [Dc] conditional | Green's function / KK mode expansion template |
| full5d_reduction.py | S-N2-8 | [OPEN] code | Bulk metric parameter data structures |

### Assumptions N2 WP2 Must State Upfront

1. **Background metric A(ξ)** — declared as [I] or [P] before any computation.
   At minimum specify: flat (A = 0) and RS-like (A = −k|ξ|).
2. **5D Planck mass M₅** — declared as [P]. Report V_bulk as function of M₅.
3. **Cosmological constant Λ₅** — declared as [P] or [I]. Related to A(ξ).
4. **Compact-direction topology** — Z₂ orbifold, circle, or infinite.
   Affects Green's function boundary conditions.
5. **Junction source treatment** — distributional (thin brane) or
   regularized (smoothed at scale δ). Declared as model assumption.
6. **Linearization validity** — the perturbation h_AB(q) must be small
   compared to ḡ_AB. If q/R is not small, linearization breaks down.
   The range of q for which the linearized solution is valid must be stated.
7. **Adiabatic approximation** — fast bulk modes relax at fixed q [P].
   Same as in all previous lanes.
8. **Collective coordinate q** — chosen in-brane displacement path
   (inherited from R3) [Dc].

### Assumptions N2 WP2 Must NOT Treat as Settled

1. **V_bulk(q) sign** — NOT assumed attractive. Could be repulsive (→ no-go) or zero.
2. **V_bulk(q) magnitude** — NOT assumed sufficient to compete with V_geom.
   κ₅²-suppression may render V_bulk quantitatively irrelevant.
3. **Double-well structure** — [P]. N2 tests whether it emerges.
4. **V_B = 2Δm_np** — [P]. V_B is computed output, not input.
5. **M₅ value** — [P]. Not determined by any existing derivation.
6. **Whether N2 produces metastability** — not assumed. No-go is allowed.

---

## 11. Forbidden Imports for N2 WP2

| Forbidden Import | Why |
|-----------------|-----|
| V_B = 2Δm_np as constraint on V_bulk | [P] conjecture. V_B is computed, not assumed (CR1). |
| Phenomenological node well shape | [P/Cal]. V_bulk must be derived from Einstein equations (CR2). |
| Background metric chosen to produce double-well | [P/I] must be declared before computation (CR3). |
| τ_n ≈ 878 s as constraint | [BL]. Comparison only; never enters V_bulk derivation (CR5). |
| Helfrich bending as bulk contribution | FALSIFIED (F-N2-4). Not a bulk gravitational effect. |
| ξ-BC as attraction source | FALSIFIED (F-N2-5). |
| C = 100 or E₀ = σL₀² | N7 quantities, not N2. V_bulk does not involve junction-core geometric amplification. |
| N1 Israel energy as positive mechanism | Bounded no-go (F-N2-1). |
| N7 thick-junction core as "bulk" contribution | Lane conflation (CR14). Core energy is distinct from bulk field energy. |
| Variant 2 as positive evidence for warping | NEGATIVE result (F-N2-8). Must not be reinterpreted. |
| F_bulk numerological formula | Different quantity (F-N2-7). Name collision risk. |
| Double-well structure as assumed | [P]. N2 tests whether it emerges. |
| ω₀ = 19 MeV | [P] dimensional estimate. Not a derivation input. |
| M₅ value chosen to match τ_n | [P]. Must be declared before computation (CR16). |

---

## 12. Bottom Line

The N2 bulk gravitational backreaction lane has the thinnest donor base
of all lanes tested so far:

**No existing computation.** V_bulk(q) has never been computed on any
branch. N2 WP2 must build the calculation from the formal action
definition (D-N2-1) and linearized Einstein equation structure, using
methodological templates from the OPR-19/21/22 chain and the M(q)
derivation framework as guides.

**One negative prior.** Variant 2 (125 warped combinations, zero
metastability) tested background warping but not junction-sourced
perturbations. The negative prior applies to the background-warping
sub-question, not to the linearized perturbation question that N2
addresses.

**Two constraining dead ends.** N1 (Israel thin-junction) and N7
(monotone thick-junction) are both bounded failures. They constrain
what N2 can claim: N2 must demonstrate that the bulk gravitational
response produces energy contributions NOT captured by either the
thin-junction matching or the thick-junction core.

**One critical uncertainty.** The κ₅²-suppression concern: bulk
backreaction energies scale as κ₅² ∝ 1/M₅³. If M₅ is large, V_bulk
is negligible. Whether V_bulk is quantitatively relevant depends
entirely on M₅, which is undetermined. A no-go of the form "V_bulk
is real but κ₅²-suppressed" is a valid and informative outcome.

**Primary risk:** CR12 (κ₅²-suppression swept under the rug) and CR3
(background metric chosen post-hoc).

**The donor base is clean.** Because no prior computation exists, there
is no historical phenomenological form to smuggle. N2 WP2 starts from
the Einstein equations, not from a legacy ansatz. This is both a
disadvantage (no infrastructure to extend) and a safeguard (nothing
to recycle illegitimately).

**N2 WP2 may begin.**
