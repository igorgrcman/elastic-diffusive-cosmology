# Phase 1 Revised Implementation Plan: R4, R3, R1

## Revision History

| Version | Date | Notes |
|---------|------|-------|
| v1.0 | 2026-03 | Original plan (claude/analyze-codebase branch) |
| v2.0 | 2026-03-12 | First revision — fixed circularity, Fourier error, epistemic inflation |
| v3.0 | 2026-03-12 | Hard revision — epistemically strict stress-test framing |
| **v3.1** | **2026-03-13** | **Mini hardening pass — 7 targeted fixes (V₀ status, M(q) scope, R₅ provenance, ledger language, R3 title, contact saturation, numerical check split)** |

## v2.0 → v3.0 Change Summary

| Area | v2.0 Issue | v3.0 Fix |
|------|-----------|----------|
| Overall framing | Still reads as "closure plan" | Reframed as stress-test with four possible exit states |
| R4 title | "Topological Proof" | "Local Pinning-Model Optimality Derivation" |
| R4 Lemma 2 | Monotonicity stated without scope limits | Scoped to pairwise-additive local model; failure modes listed |
| R4 Lemma 3 | Uniqueness stated broadly | Scoped to restricted geometric contact model |
| R3 goal | "Derive V(q)" without qualification | "Derive V(q) along an explicitly chosen collective deformation path" |
| R3 q-coordinate | Treated as natural | Explicitly labeled as chosen, not uniquely derived |
| R3 subtargets | Single [Dc] target | Split into three graded subtargets |
| R3 Z₃ minimum | Implied closure via Landau language | Conditional unless Hessian is computed from reduced action |
| R3 M(q) | Presented as derived | Labeled as scaling estimate within chosen reduction |
| R1 goal | Suggests derivation of universal ratio | Derives dependence within explicit localization model |
| R1 localization potential | Labeled [Dc] | Labeled as effective ansatz anchored in EDC picture |
| R1 R₅ derivation | 6δ mode-count as main bridge | Demoted to candidate assumption [P]; sensitivity scan required |
| R1 success criterion | Reproduce π² | Replace naked postulate with derived dependence/range |
| R3→R1 dependency | Not addressed | Explicit: R1 cannot exceed R3 epistemic status for imported M |
| Integration ledger | Single target column | Two columns: best-case and conservative-likely |
| Commit messages | Encode successful promotion | Neutral implementation language |
| Guards | "All derivations from S_EDC" | Distinguishes direct, effective-reduction, and auxiliary-ansatz |
| Missing sections | — | Added 5 new sections (see A2, A3, D1, D2, D3) |

---

## Overview

Phase 1 is a **disciplined stress-test** of three foundational bottlenecks
in the neutron/topological-pinning derivation chain:

- **R4**: N_bonds = 3 optimality for A=2 cluster (local pinning model)
- **R3**: V(q) effective potential along a chosen collective deformation path
- **R1**: L₀/δ ratio within an explicit compact-localization model

Execution order: **R4 → R3 → R1** (simplest first, each builds context).

**Phase 1 is not a guaranteed closure sequence.** It is a structured attempt
to reduce three [P]-tagged bottlenecks, with three possible outcomes for
each item:

1. **Genuine promotion**: assumption replaced by derivation within stated model
2. **Partial closure / dependency exposure**: derivation chain improved but
   one or more critical bridges remain explicitly open
3. **Non-confirmation**: the previously preferred number (e.g., π²) does not
   emerge from the derivation; the derived value replaces the postulate
   regardless of whether it matches

Negative results count as progress if they replace a postulate with a
derived non-matching value. A derived L₀/δ = 9.5 is strictly better
than a postulated L₀/δ = π², even if less aesthetically satisfying.

---

## What Counts as Success?

Phase 1 is successful if it achieves at least one of the following:

1. Upgrades one bottleneck from [P] to a rigorously bounded [Dc] or [P*]
   within its stated effective model.
2. Replaces a preferred constant by a derived function or constrained range,
   even if the preferred value is not recovered.
3. Exposes the precise assumption preventing closure — converting an
   unnamed gap into a named, testable condition.
4. Quantitatively tests whether the neutron lifetime line survives,
   weakens, or fails under stricter derivation discipline.

---

## What Phase 1 Does Not Claim

Phase 1 does **not** claim:

- Full direct closure of neutron lifetime from first principles.
- Unique derivation of all effective coordinates and reduction paths.
- Elimination of all model choices, ansatz dependencies, or auxiliary assumptions.
- Final closure of the Put C corridor unless every sub-step (C1–C4) is
  explicitly completed and tagged.
- That any promotion target will necessarily be achieved.

---

## Methodology Principle

> **Analitičke derivacije su primarne.** Svaki korak derivacije mora biti
> zapisan u LaTeX-u, čitljiv za čovjeka, sa svim međukoracima. Numerički
> izračuni dolaze SAMO na kraju kao nezavisna potvrda analitičkog rezultata.
> Nikada obrnuto.

> **Epistemička iskrenost je obavezna.** Ako korak zahtijeva pretpostavku,
> tagira se [P] bez obzira koliko je "očita". Promocija [P]→[Dc] ili [Der]
> zahtijeva eksplicitan, provjerljiv lanac bez praznina. Ako lanac ima
> prazninu, rezultat je [P*] (partially derived), ne [Dc].

> **Ansatz-zavisnost mora biti imenovana.** Ako derivacija koristi
> kolektivnu koordinatu, lokalizacijski potencijal, ili efektivnu redukciju
> koja nije jedinstven izbor, to mora biti eksplicitno navedeno, a rezultat
> tagan "within [named model/ansatz]".

All work uses EDC-native vocabulary. No Standard Model constructs.

---

## Epistemic Output Classes

All results in Phase 1 are tagged using these labels:

| Tag | Meaning | Requirement |
|-----|---------|-------------|
| **[Der]** | Fully derived from stated inputs with no unresolved internal gap | Every step closed; inputs themselves [Der] or [I] |
| **[Dc]** | Derived within an explicitly declared effective model or reduction | Model/reduction named; steps closed within that model |
| **[P\*]** | Partially derived; chain improved but one critical bridge remains open | The open bridge must be named and testable |
| **[P]** | Postulated; physically motivated but not derived | May be plausible; no derivation chain exists |
| **[Check]** | Internal consistency check or numerical confirmation | Not an independent derivation; confirms or falsifies an analytic result |
| **[Cal]** | Calibrated to empirical data | Fit, not derivation |
| **[BL]** | Baseline empirical measurement | Observer-frame data |

**Rule**: A result's tag cannot exceed the weakest unresolved tag in its
dependency chain. If R1 imports M from R3 at [Dc], R1's final status
cannot exceed [Dc] for any quantity depending on M.

---

## Dependency Map

```
R4 (N_bonds = 3)
├── Depends on: local pairwise-additive pinning Hamiltonian [P/Dc from Ch.5]
├── Depends on: Y-junction arm count = 3 [Der from Ch.1]
├── Depends on: contact saturation (one bond per arm) [P — locality assumption]
└── Independent of R3 and R1

R3 (V(q) effective potential)
├── Depends on: chosen collective coordinate q [ansatz — not uniquely derived]
├── Depends on: S_EDC action structure [I]
├── Depends on: Steiner optimality for q=0 minimum [Der from Ch.1]
├── Depends on: Z₃ subgroup stability argument [P/Dc — Landau, not Hessian-derived]
├── Depends on: Put C corridor steps C2-C4 [OPEN — must be completed]
└── Produces: V(q) shape, M(q) estimate — consumed by R1

R1 (L₀/δ ratio)
├── Depends on: compact-localization effective model [ansatz]
├── Depends on: localization potential form (square well) [ansatz]
├── Depends on: compact-dimension topology and R₅ [P — mode-count assumption]
├── Depends on: M(q) from R3 [inherited status — cannot exceed R3 tag]
└── Produces: L₀/δ value or range — consumed by Integration

Integration (τ_n recalculation)
├── Depends on: all R4/R3/R1 outputs
├── Cannot back-promote unresolved inputs
└── τ_n inherits the weakest major unresolved dependency from R3/R1
```

**Cross-dependency warning**: R1 uses M from R3. If R3's effective mass
is revised or re-tagged, R1 results must be re-evaluated. The integration
step must not mask this coupling.

---

## Existing Infrastructure (DO NOT DUPLICATE)

| Asset | Location | Status | Use in Phase 1 |
|-------|----------|--------|-----------------|
| Put C corridor (5D→1D pathway) | `edc_book_2/src/derivations/S5D_TO_SEFF_Q_REDUCTION.md` | [P]+[Dc] framework, steps C1–C4 OPEN | R3: complete steps C2–C4 |
| V_B = 2Δm_np conjecture | `edc_book_2/src/derivations/V_B_FROM_Z3_BARRIER_CONJECTURE.md` | [Dc] conditional | R3: formalize or bound |
| Z₃ symmetry analysis | `edc_book_2/src/derivations/Z3_SYMMETRY_ANALYSIS_NEUTRON.md` | [P]+[OPEN] | R3: use Landau expansion |
| L₀/δ exploration (6 approaches) | `edc_book_2/src/derivations/DERIVE_L0_DELTA_PI_SQUARED.md` | [P] all routes | R1: build on, don't repeat |
| L₀/δ v2 (6 more approaches) | `edc_book_2/src/derivations/DERIVE_L0_DELTA_PI_SQUARED_V2.md` | [P] all routes | R1: identify strongest |
| Kramers double-well code | `edc_book_4/code/kramers_double_well_v2.py` | [Dc] 1000-traj ensemble | R3: reuse for V(q) verification |
| Topological pinning model | `edc_book_2/src/derivations/BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex` | [Dc/I] partial | R4: K_pin formula |
| M₆ exploration | `edc_book_2/src/derivations/M6_TOPOLOGICAL_MODEL_EXPLORATION.md` | [P] exploratory | R4: bond counting context |

**Rule**: Reference existing work. Extend it. Don't rewrite from scratch.

---

## Step 1: R4 — N_bonds = 3 Local Pinning-Model Optimality Derivation

**Goal**: Target promotion of N_bonds = 3 from [P] to [Dc] **within the
local pairwise-additive pinning model**. This is not a general topological
proof; it is an optimality result within a specific effective energy model.

**Why [Dc] not [Der]**: The proof operates within the pinning Hamiltonian
H_pin from Ch.5, which itself contains [P] assumptions about pairwise
additivity and locality. A full [Der] would require deriving H_pin from
S_EDC, which is R3-level work (Put C corridor). Therefore the strongest
achievable tag is [Dc] (derived within the declared pinning model).

### 1a. Analytic derivation (LaTeX)

Create `edc_book_4/appendices/app_Nbonds_local_optimality.tex`

**Theorem (N_bonds Local Optimality)**: Within the pairwise-additive
pinning model, for two Y-junctions sharing a contact face in the M₆
lattice, the energy-minimizing configuration has exactly N_bonds = 3
contact pairs.

**Proof structure:**

**Lemma 1 — Upper bound** [Der + model constraint]:
- Each Y-junction has exactly 3 arms (Z₃ Steiner geometry, Ch.1 [Der]).
- Each arm participates in at most one bond. This is a geometric
  constraint within the contact model: two worldsheet segments with
  the same orientation sharing the same contact face are treated as
  a single bond, not multiple independent bonds. This follows from
  the model's definition of "bond" as a pairwise arm-to-arm contact,
  but has not been independently derived as a physical saturation
  theorem from the full 5D action.
- Therefore N_bonds ≤ 3 within this contact model. ∎

**Lemma 2 — Energetic preference for saturation** [Dc within pinning model]:
- Define contact energy for n bonded pairs (0 ≤ n ≤ 3):
  ```
  E(n) = n × K_pin + (3 - n) × E_free
  ```
  where K_pin < 0 (binding, from Ch.5 [Dc]) and E_free = 0 (free arm,
  reference level).

- **Stated assumptions** (all required for monotonicity):
  1. Pairwise additivity: total energy is sum of pair contributions [P]
  2. Locality: no long-range inter-arm coupling beyond nearest contact [P]
  3. No frustration penalty: adding bonds does not create geometric
     strain that offsets binding energy [P]
  4. No multi-arm nonlocal coupling: three-body or higher terms absent [P]

- Under these four assumptions, E(n) = n × K_pin is monotonically
  decreasing (since K_pin < 0), minimized at n = 3.

- **Warning**: If any of assumptions 1–4 fail, monotonicity in n can
  fail. For example, if frustration penalties grow faster than |K_pin|
  with increasing n, the minimum could shift to n < 3. This would
  require a different physical mechanism and is not excluded by the
  current argument.

- **Tag**: [Dc] within the local pairwise-additive pinning model. ∎

**Lemma 3 — Uniqueness up to Z₃** [Der within restricted contact geometry]:
- Three arms of J₁ at angles {0°, 120°, 240°}.
- Three arms of J₂ at complementary angles {180°, 300°, 60°}.
- The pairing that minimizes angular mismatch is the identity pairing
  (arm_i ↔ arm_i') with zero mismatch.
- Any permutation σ ∈ S₃ \ {id} creates nonzero mismatch for at least
  one pair, increasing brane area (Steiner optimality, Ch.1 [Der]).
- The minimum is unique within each Z₃ orbit. ∎
- **Scope**: This is uniqueness within the restricted geometric contact
  model (fixed Y-junction orientations, fixed arm directions). It is
  not uniqueness in the full configuration space of all admissible
  5D brane deformations.

**Corollary**: B_d = 3 × K_pin [Dc within pinning model].
- With K_pin = 0.74 MeV [Dc]: B_d = 2.22 MeV.
- Measured: B_d^exp = 2.224 MeV [BL]. Agreement: <1%.

**Honest residual [P]**: The four assumptions of Lemma 2. Upgrading any
of them requires explicit computation from the 5D action (Put C corridor).

### 1b. Numerical verification [Check]

Create `edc_book_4/code/r4_nbonds_verify.py`:
- Discretize relative orientation of two Y-junctions on SO(3)
- Compute total contact energy E(θ₁, θ₂, θ₃) using K_pin from Ch.5
- Confirm global minimum at N_bonds = 3 with Z₃-symmetric pairing
- Compare to analytic prediction
- Output: PASS/FAIL with numerical values
- **Tag**: [Check] — this confirms the analytic result within the same
  model, not an independent derivation

**Reuse**: Import K_pin value from existing `book4_kramers_validation.py`
infrastructure.

### 1c. Chapter updates

- `ch10_deuterium.tex`: Update N_bonds discussion to reflect local
  optimality derivation. Promote N_bonds from [P] to [Dc] with
  explicit scope note: "within the local pairwise-additive pinning model."
  Do not state [Dc] unqualified.
- Update epistemic table in ch10 with model-scope qualifier.

**Deliverables**: 1 appendix derivation (~120 lines), 1 verification
script (~120 lines), 1 chapter edit.

---

## Step 2: R3 — Effective V(q) Along a Chosen Collective Path

**Goal**: Derive the effective potential V(q) **along an explicitly chosen
collective deformation path** from the Z₆ (anchor) to Z₃ (metastable)
junction configuration. This is not a derivation of the unique full
effective potential of the entire 5D system. It is a reduction along a
specific interpolation path in configuration space.

**The coordinate q is a chosen collective interpolation parameter.**
It is not yet a uniquely derived normal mode of the full 5D dynamics.
All V(q) results produced in this step are therefore conditional on
this deformation-path choice. An alternative collective coordinate
choice could yield a quantitatively different effective potential.
This conditionality must be preserved in all tags.

**Subtargets** (graded by epistemic level):

| Subtarget | Description | Target tag | Conditions |
|-----------|-------------|------------|------------|
| R3a | Geometric contribution to V(q): brane energy along chosen path | [Dc] | Steiner optimality [Der] + explicit pullback computation |
| R3b | Existence and location of secondary minimum at Z₃ | [Dc]+[P] or [P*] | Requires stability (positive Hessian) from reduced action; Landau argument alone is [P] |
| R3c | Barrier height identification V_B = 2Δm_np | Conditional only | Depends on unresolved unit identification E_arm ≡ Δm_np [OPEN] |

### 2a. Complete Put C corridor steps C2–C4

**Build on** `S5D_TO_SEFF_Q_REDUCTION.md` — do NOT rewrite the framework.

Create `edc_book_4/appendices/app_Vq_collective_coordinate.tex`

**Section 1: Recap of Put C framework** [reference only]
- Cite the reduction pathway S_total → S_eff[q] from existing document
- State which steps are already established (C1: ansatz) and which
  this derivation attempts to complete (C2–C4)
- Explicitly note: completing C2–C4 would close the corridor within
  the chosen collective-coordinate framework. If C4 (fast-mode
  integration) proves intractable, document partial result.

**Section 2: Collective coordinate definition and brane embedding** [ansatz + Dc]
- Define the collective coordinate q ∈ [0,1]:
  ```
  α_i(q) = α_i^(Z₆) + q × [α_i^(Z₃) - α_i^(Z₆)]
  ```
  where α^(Z₆) = {0°, 60°, 120°} and α^(Z₃) = {0°, 120°, 240°}

- **Mandatory statement**: q is a chosen linear interpolation between
  two known configurations. It is not derived as the unique lowest-energy
  deformation mode. The choice is physically motivated (connects the
  two configurations of interest) but not unique. A geodesic interpolation
  in configuration space, or a non-linear reparametrization, could yield
  a different V(q) profile.

- Arm lengths ℓ_i(q) from Steiner minimization at fixed angles [Der for
  Steiner problem; application to fixed-angle case is [Dc]]
- Compute induced metric h_μν by pullback: h_μν = G_AB ∂_μX^A ∂_νX^B
- **Every tensor component written explicitly**

**Section 3: Brane energy E_brane(q) — geometric contribution** [Dc]
- Static limit (Nambu-Goto):
  ```
  E_brane(q) = σ × Σ_i ℓ_i(q)
  ```
- Key property: E_brane(0) is global minimum (Steiner theorem, Ch.1 [Der])
- Expand around q=0:
  ```
  E_brane(q) = E_brane(0) + ½ σ L₀ c₂ q² + O(q³)
  ```
  with c₂ > 0 (positive Hessian from Steiner minimum)
- **Tag**: [Dc] — this is a direct geometric computation within the
  Nambu-Goto framework along the chosen path

**Section 4: Z₃ secondary minimum — conditional stability** [P* or Dc conditional]
- The Z₃ configuration (q = q_n) is not on the quadratic expansion
  around q=0. It is a separate critical point.
- **Symmetry argument**: At q_n, the junction has Z₃ symmetry (arms at
  120° spacing). Small perturbations breaking Z₃ are expected to
  increase energy by the Landau argument (existing `Z3_SYMMETRY_ANALYSIS`):
  ```
  E(q, Δ) = E₀(q) + a(q)Δ² + b(q)Δ⁴
  ```
  where Δ measures deviation from Z₃ symmetry.

- **The secondary minimum is not fully closed from this plan.** The claim
  that q_n is a local minimum requires a(q_n) > 0, which means the
  Z₃-symmetric configuration is stable against symmetry-breaking
  perturbations.

- Current support for a(q_n) > 0:
  - Observational: absence of low-lying doublet partners [BL]+[M]
  - Symmetry: Z₃ is a subgroup of Z₆, so breaking Z₃ breaks more
    symmetry and is generically costly
  - Neither constitutes a derivation from the reduced action

- **To close this**: Compute the Hessian of V(q,Δ) at q_n from the
  explicit brane energy and verify a(q_n) > 0. If this computation
  succeeds, the secondary minimum is [Dc]. If it requires additional
  assumptions, it remains [P*].

- **Tag**: [P*] unless Hessian computation closes within this step

**Section 5: Barrier shape — geometric interpolation** [Dc for shape; open for height]
- The barrier sits at the maximum of E_brane(q) between q=0 and q=q_n
- At the barrier, the junction has neither Z₆ nor Z₃ symmetry
- Barrier shape:
  ```
  V_B = E_brane(q_B) - E_brane(q_n) = σ × [L_total(q_B) - L_total(q_n)]
  ```
- Compute L_total(q_B) explicitly from arm-length formula along chosen path

- **Two distinct questions — do not conflate:**
  1. Does V(q) along the chosen path have a barrier between q=0 and q_n?
     → This is a geometric question, likely [Dc]
  2. What is the numerical height of that barrier in physical units?
     → This requires identifying brane-energy differences with
     observer-frame mass differences, which involves the unresolved
     unit identification below

**Section 6: Barrier height and Δm_np — conditional identification** [OPEN]
- From the Z₃ barrier conjecture:
  - Z₃ symmetry → equal energy partition: E_B = 3 × E_arm [Der from Z₃]
  - **Unit identification**: E_arm ≡ Δm_np [OPEN — not derived]
  - Result: V_B = E_B - E_n = 3×Δm_np - 1×Δm_np = 2×Δm_np
    [conditional on unit identification]

- **Honest statement**: V_B = 2×Δm_np holds IF each arm carries exactly
  one mass-difference quantum AND that quantum equals the observer-frame
  neutron-proton mass difference. Both identifications require either:
  (a) completion of the full Put C computation linking 5D brane energy
      to observer-frame mass, or
  (b) an independent geometric argument for the energy quantum.
  Neither is provided by this step.

- **Barrier geometry may close before barrier quantization closes.**
  The shape of V(q) can be [Dc] while the absolute height in MeV
  remains [OPEN] or [Cal].

- **Tag**: [OPEN conditional]. Barrier shape: [Dc]. Barrier height
  in physical units: [OPEN] pending unit identification.

**Section 7: Effective mass M(q) — scaling estimate** [ansatz-dependent]
- Kinetic term from junction node motion:
  ```
  T = ½ M(q) q̇²
  M(q) = σ × Σ_i ∫₀^{ℓ_i} ds (∂X^A/∂q)²
  ```
- In the constant-mass approximation (valid near minima):
  ```
  M ≈ 3σδ²/c²
  ```
  (each arm contributes σδ²/c² — arm cross-section times tension)

- **This is a scaling estimate valid only within the chosen collective-
  coordinate path and the chosen normalization of q.** It is not a
  coordinate-independent or uniquely derived mass law. Specifically:
  - The functional form M ∝ σδ²/c² follows from dimensional analysis
    within the Nambu-Goto framework.
  - The numerical coefficient (the factor 3) depends on the geometric
    details of the embedding, the normalization convention for q, and
    the arm-length parametrization. A different collective coordinate
    or a non-linear reparametrization of q would yield a different
    numerical M.
  - The constant-mass approximation itself is valid only near the
    potential minima; away from minima, M(q) may vary significantly.

- **Tag**: [Dc(path-dependent)] for the functional form M ∝ σδ²/c²
  within the chosen path and q normalization. The numerical coefficient
  is [P] (model- and coordinate-dependent).

**Summary**: S_eff[q] = ∫ dt [½M q̇² - V(q)] with:
- Global minimum at q=0 (anchor/Z₆) — [Dc]
- Local minimum at q=q_n (metastable/Z₃) — [P*] unless Hessian closes
- Barrier at q=q_B — shape [Dc], height in MeV [OPEN]
- Coefficients in terms of {σ, δ, L₀} — [Dc] for structure, [P] for
  numerical prefactors
- All results conditional on chosen collective coordinate path

### 2b. Numerical verification [Check]

Create `edc_book_4/code/r3_vq_verify.py`:
- Implement V(q) from analytic formula of §2a
- **Barrier verification** (separate from minimum verification):
  - Compute V(q) along the chosen path for q ∈ [0,1]
  - Verify that a local maximum exists between q=0 and q=q_n
  - Report barrier location q_B and height in σ-units
  - Compare barrier height to Δm_np = 1.293 MeV [BL] (comparison,
    not calibration)
- **Metastable minimum verification** (distinct test):
  - Verify that q_n is a genuine local minimum, not merely an
    inflection point or shoulder
  - Test: V''(q_n) > 0 along the chosen path
  - Test: Hessian in transverse directions (if computed in §2a Section 4)
  - A barrier without a true second minimum is NOT a double-well —
    report this distinction explicitly
- Cross-check with existing Kramers code (`kramers_double_well_v2.py`)
- Plot V(q) and compare shape to Phase-1 ansatz
- Output: V(q) at key points, barrier PASS/FAIL, minimum PASS/FAIL
  (separate gates)
- **Tag**: [Check] — confirms or falsifies the analytic construction

### 2c. Chapter updates

- `ch03_neutron_metastable.tex`: Update V(q) discussion to reflect
  collective-coordinate derivation. Promote only the geometric/effective-path
  part if earned:
  - Brane energy along path: [P] → [Dc] if computation closes
  - Secondary minimum existence: [P] → [P*] unless Hessian computed
  - Barrier height in MeV: remains [OPEN conditional]
  Do not blindly flip V(q) [P] → [Dc].
- `ch06_instanton.tex`: Reference derived V(q) shape. Update M(q)
  discussion to note scaling-estimate status. Preserve [P] or [P*]
  tags where assumptions remain.

**Deliverables**: 1 appendix derivation (~250 lines), 1 verification
script (~180 lines), 2 chapter edits (graded tag updates, not blanket
promotion).

---

## Step 3: R1 — L₀/δ Within Explicit Compact-Localization Model

**Goal**: Derive the dependence of L₀/δ **within an explicit
compact-localization effective model**, and test whether the preferred
value π² emerges. This is not a derivation of a universal ratio from
first principles. It is the construction of an effective eigenvalue
problem whose solution constrains L₀/δ under stated assumptions.

**Success criterion**: Replace the naked postulate L₀/δ = π² [P] with
a derived dependence and constrained value or range within the stated
model. The primary success is converting an unnamed gap into a named,
model-bounded result — whether or not π² is recovered.

### 3a. The derivation (single route, stated model)

Create `edc_book_4/appendices/app_L0delta_localization_model.tex`

**Section 1: Problem statement**
- A junction defect in the compact fifth dimension ξ ∈ [0, 2πR₅]
- The defect creates a localization potential V_loc(ξ)
- Question: What is the characteristic extent L₀ of the defect?
- **We must derive or constrain both L₀ AND R₅ in terms of δ.**
- The result will be L₀/δ = F(R₅/δ, V₀δ²M/ℏ², ...), a function of
  model parameters — not necessarily a single number.

**Section 2: The localization potential — effective ansatz** [ansatz anchored in EDC]
- The junction brane has thickness δ (UV cutoff from Book I [I])
- The junction creates a potential well in the transverse direction:
  ```
  V_loc(ξ) = -V₀  for |ξ - ξ₀| < δ/2
  V_loc(ξ) = 0    otherwise
  ```
- Well depth scale: V₀ ~ σ/δ. This is an EDC-anchored scaling estimate
  within the localization ansatz: brane tension σ concentrated over
  thickness δ gives a natural depth scale. It is not a uniquely derived
  action-level result. The proportionality constant (order unity) is
  not determined by this argument.
  **Tag**: [ansatz(model-scaling)] — not [Dc]

- **This is an effective localization ansatz**, not a unique derivation
  from the full 5D action. It is anchored in the EDC picture (the
  junction creates a potential well whose depth scales with brane tension
  and whose width is set by brane thickness), but the square-well form
  is a simplification. The actual potential from a Y-junction defect in
  curved 5D space could differ in profile shape and depth.

- **Tag**: [ansatz] — physically motivated effective model, not [Dc]

**Section 3: Eigenvalue equation** [Der within stated model]
- Sturm-Liouville problem on S¹:
  ```
  -ψ''(ξ) + V_loc(ξ) ψ(ξ) = E_n ψ(ξ)
  ```
  with periodic boundary conditions ψ(0) = ψ(2πR₅)

- Inside well: ψ(ξ) = A cos(k_w ξ)
- Outside well: ψ(ξ) = B exp(-κ₀|ξ|)

- Matching at ξ = ±δ/2:
  ```
  k_w tan(k_w δ/2) = κ₀
  ```

- The localization length is: L₀ = 1/κ₀

- **Tag**: [Der] within the stated localization model. The eigenvalue
  problem and matching conditions are exact for the stated V_loc.

**Section 4: Compactification radius R₅ — candidate assumptions** [P]

- **This is the critical model-dependent step.** R₅ is not independently
  measured or derived from S_EDC in the current theory. It must be
  constrained by an auxiliary condition.

- **Candidate assumption A** (from existing v1/v2 exploration):
  Fundamental mode wavelength set by Y-junction arm count:
  λ_fundamental = 2 × (3δ) = 6δ → 2πR₅ = 6δ → R₅ = 3δ/π
  - **Provenance**: This is a legacy assumption inherited from the
    v1/v2 L₀/δ exploration documents (`DERIVE_L0_DELTA_PI_SQUARED.md`,
    `DERIVE_L0_DELTA_PI_SQUARED_V2.md`). It was the preferred
    candidate in prior work but was never independently derived.
  - **Tag**: [P] — the factor 3 comes from Y-junction arm count but the
    identification of λ_fundamental with 3 arm-widths is heuristic
  - If this holds: L₀/δ will be determined by the transcendental equation

- **Candidate assumption B**: R₅ = πδ (standing-wave resonance from Ch.8)
  - **Provenance**: This is also a legacy assumption from Ch.8's
    standing-wave argument (Approach 1 in the existing chapter text).
    It predates the v1/v2 exploration and was one of the original
    motivations for L₀/δ ≈ π².
  - **Tag**: [P] — same level of justification as A

- **Candidate assumption C**: R₅ as free parameter, scan over range
  - This yields L₀/δ = F(R₅/δ) — a function, not a number
  - Useful for sensitivity analysis

- **Required approach**: Compute L₀/δ for ALL candidate R₅ values.
  Report:
  1. L₀/δ as a function of R₅/δ
  2. Which R₅/δ value(s), if any, give L₀/δ = π²
  3. Whether the R₅ that yields π² has independent justification
  4. The range of L₀/δ over physically plausible R₅

- **The primary derived result of R1 is the function L₀/δ = F(R₅/δ, ...),
  not a unique number.** If one specific R₅ assumption reproduces π²,
  that is noted but the result remains tagged with the assumption.

**Section 5: Computing L₀/δ — transcendental equation** [Dc within model + [P] for R₅]
- With V₀ ~ σ/δ (scaling estimate, see Section 2) and chosen R₅, solve:
  ```
  k_w tan(k_w δ/2) = κ₀
  k_w² + κ₀² = 2M V₀/ℏ²
  κ₀ = 1/L₀
  ```
  subject to periodic boundary conditions on S¹ of radius R₅.

- **Imported input**: M ≈ 3σδ²/c² from R3 Step 2.
  - This is a conditional input inherited from the R3 collective-coordinate
    reduction.
  - R1's final epistemic status for any quantity depending on M cannot
    exceed R3's tag for M ([Dc] for functional form, [P] for numerical
    coefficient).
  - If R3 does not close, or if M is revised, R1 results must be
    re-evaluated.

- The ground-state solution gives L₀ as a function of δ, V₀, R₅, M.
- L₀/δ depends on the dimensionless well-strength parameter:
  ```
  η = V₀ δ² M / ℏ² ~ (σ/δ)(δ²)(3σδ²/c²)/ℏ² ~ σ²δ³/(ℏ²c²)  [order-of-magnitude]
  ```
  and on R₅/δ.

- **Tag**: [Dc] within the localization model, conditional on R₅ choice [P]
  and M import [Dc/P from R3].

**Section 6: Consistency check** [Check]
- Variational bound: minimize E(L₀) = E_kinetic + E_tension
  ```
  E(L₀) = 3π²ℏ²/(2M L₀²) + 2πσδ L₀
  ```
- This gives an independent estimate of L₀ that should agree with
  the eigenvalue result within the approximations used.
- **Tag**: [Check] — this uses the same physics and model. Disagreement
  indicates an error in the calculation, not a new physical result.
  Agreement does not elevate the epistemic status.

**Section 7: Sensitivity analysis and τ_n impact** [Check]
- For each R₅ candidate and the resulting L₀/δ:
  ```
  S_E/ℏ = κ × (L₀/δ) = 2π × (L₀/δ)
  τ_n = A × (ℏ/ω₀) × exp(S_E/ℏ)
  ```
- Use sensitivity table from ch09 to assess impact on τ_n
- Report:
  - Does the derived ratio (under each R₅ assumption) give τ_n
    consistent with 878.4 ± 0.5 s?
  - Which R₅ assumption, if any, is selected by τ_n agreement?
  - Is this selection independent or circular (fitting R₅ to match τ_n)?

- **Warning on circularity**: If the only R₅ that gives the right τ_n
  has no independent justification, then the "derivation" is effectively
  a fit with one free parameter (R₅), and the result is [Cal] for the
  ratio, not [Dc]. This must be stated honestly.

### 3b. Numerical verification [Check]

Create `edc_book_4/code/r1_L0delta_verify.py`:
- Implement Sturm-Liouville solver (scipy shooting method or
  `eigh_tridiagonal`)
- Set up V_loc(ξ) with parameters from §3a
- Compute ground-state eigenvalue and localization length
- Scan R₅/δ ∈ [0.5, 5.0] and plot L₀/δ vs R₅/δ
- Mark π² on the plot; identify which R₅/δ (if any) recovers it
- Verify against analytic transcendental-equation solution
- Output: L₀/δ function, comparison to π², parameter sensitivity
- **Tag**: [Check]

### 3c. Chapter updates

- `ch08_L0_delta_ratio.tex`: Update to reflect localization-model
  derivation. Do not blindly flip [P] → [Dc]. Instead:
  1. Report the model-derived dependence L₀/δ = F(R₅/δ, η)
  2. State which R₅ assumption(s) were tested
  3. Report the actual derived value/range under each assumption
  4. Tag the result as:
     - [Dc(model)] if the derivation closes within the localization
       model but R₅ choice remains [P]
     - [P*] if the derivation exposed a critical gap or yielded
       an ambiguous range
     - [Dc] only if R₅ itself is independently derived (unlikely
       in Phase 1)
- `ch09_tau_n_prediction.tex`: Update epistemic composition of τ_n.
  τ_n cannot be promoted beyond the weakest tag in its dependency chain.

**Deliverables**: 1 appendix derivation (~300 lines), 1 verification
script (~200 lines), 2 chapter edits (graded, not blanket promotion).

---

## Step 4: Integration and Cross-Checks

### 4a. Full τ_n recalculation

Create `edc_book_4/code/phase1_tau_n_integration.py`:
- Assemble τ_n from all Phase 1 results:
  - κ = 2π [Dc] (Ch.7, locked)
  - L₀/δ = [result from R1] (model-derived value or range)
  - V(q) shape [Dc along chosen path] (from R3) → ω₀ and A
  - N_bonds = 3 [Dc within pinning model] (from R4)
- Compute τ_n and compare to 878.4 ± 0.5 s [BL]
- Uncertainty budget: which input dominates residual uncertainty?

**Critical rule**: τ_n inherits the weakest unresolved major dependency
from R3/R1. Integration cannot back-promote unresolved inputs. If L₀/δ
is [Dc(model)] with R₅ [P], τ_n remains partially [P]-dependent.

### 4b. Negative-result handling

If any of the following occur, the integration step must still:
- Recompute τ_n with the actual derived values
- Show quantitative deviation from 878.4 s
- Document whether the neutron line survives, weakens, or fails

Specific scenarios:
- **R1 yields L₀/δ ≠ π²**: Compute τ_n with actual value. Report
  deviation. Assess whether prefactor A can absorb it naturally.
- **R3 fails to stabilize secondary minimum**: Document that the
  double-well structure is not confirmed. τ_n derivation chain breaks
  at V(q). Report this as a critical finding, not a failure to hide.
- **R3 barrier height ≠ 2Δm_np**: Report actual barrier in σ-units.
  Compute τ_n with actual barrier. Assess survival of neutron line.

### 4c. Epistemic ledger (conservative, two-column)

| Quantity | Before Phase 1 | Best-case promotion | Conservative likely status |
|----------|----------------|---------------------|---------------------------|
| N_bonds = 3 | [P] | [Dc] (within pinning model) | [Dc] (within pinning model) — low risk |
| V(q) geometric shape | [P] | [Dc] (along chosen path) | [Dc] (along chosen path) — moderate risk |
| V(q) secondary minimum | [P] | [Dc] (if Hessian closes) | [P*] — Hessian may not be computed |
| V_B = 2Δm_np | [P] | [Dc conditional] on unit ID | [OPEN conditional] — unit ID unlikely to close |
| M(q) coefficient | [P] | [Dc] (scaling form) | [Dc] scaling, [P] numerical coefficient |
| L₀/δ value | [P] = π² | [Dc(model)] if R₅ derived | [Dc(model)] with R₅ [P], or [P*] |
| S_E/ℏ = 2π³ | [Dc]×[P] | [Dc]×[Dc(model)] | [Dc]×[P*] or [Dc]×[Dc(model)+P(R₅)] |
| τ_n ≈ 880 s | [Dc]+[P]+[Cal] | Reduced postulate load; status depends on R3/R1 outcome | Mixed [Dc]/[P*]/[Cal] — inherits weakest link |

### 4d. Commit structure

Neutral implementation language — no promotion claims in commit titles:

1. `R4: derive local optimality conditions for N_bonds=3 in pinning model`
2. `R3: build collective-coordinate V(q) reduction along Z6-Z3 path`
3. `R1: derive L0/delta dependence in compact-localization model`
4. `Phase 1 integration: recompute tau_n and update epistemic ledger`

---

## File Plan

### New files (7):

| File | Purpose | Lines (est.) |
|------|---------|-------------|
| `edc_book_4/appendices/app_Nbonds_local_optimality.tex` | N_bonds optimality within local pinning model | ~120 |
| `edc_book_4/appendices/app_Vq_collective_coordinate.tex` | V(q) effective potential along chosen collective path | ~250 |
| `edc_book_4/appendices/app_L0delta_localization_model.tex` | L₀/δ dependence within compact-localization model | ~300 |
| `edc_book_4/code/r4_nbonds_verify.py` | N_bonds numerical confirmation [Check] | ~120 |
| `edc_book_4/code/r3_vq_verify.py` | V(q) numerical confirmation [Check] | ~180 |
| `edc_book_4/code/r1_L0delta_verify.py` | L₀/δ numerical confirmation + sensitivity scan [Check] | ~200 |
| `edc_book_4/code/phase1_tau_n_integration.py` | Full τ_n integration + negative-result handling | ~180 |

### Modified files (5):

| File | Changes |
|------|---------|
| `ch10_deuterium.tex` | N_bonds scoped [Dc] within pinning model |
| `ch03_neutron_metastable.tex` | V(q) graded update: geometric [Dc], minimum [P*], height [OPEN] |
| `ch06_instanton.tex` | V(q) + M(q) references with scaling-estimate caveat |
| `ch08_L0_delta_ratio.tex` | L₀/δ model-derived dependence; actual value/range; graded tag |
| `ch09_tau_n_prediction.tex` | τ_n epistemic composition — inherits weakest link |

### NOT modified during Phase 1:

| File | Why not |
|------|---------|
| `EDC_UNIFIED_SYNTHESIS.md` | Update AFTER Phase 1 completed and verified, not during |
| `EDC_RESEARCH_ROADMAP.md` | Same — premature to mark status changes during active work |

---

## Risk Table

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| L₀/δ ≠ π² under any R₅ assumption | Medium | HIGH (exponential in τ_n) | Report actual value/range. A derived 9.5 is better than postulated π². Compute τ_n impact. |
| R₅ has no independent derivation | High | Medium | Present L₀/δ as function of R₅/δ. Flag if τ_n-matching R₅ is the only justification (circularity). |
| V(q) secondary minimum not stabilized | Medium | HIGH (breaks double-well) | Document as critical finding. Assess whether alternative reduction path could stabilize it. |
| V_B ≠ 2Δm_np from geometry | Medium | Medium | Report actual V_B in σ-units. Unit identification E_arm=Δm_np flagged [OPEN] from start. |
| Collective coordinate q is not unique | Certain | Medium | Stated as inherent limitation. All V(q) results tagged "along chosen path". |
| M(q) numerical coefficient is model-dependent | High | Low-Medium | Report functional form [Dc] separately from coefficient [P]. |
| Put C step C4 (fast-mode integration) intractable | Medium-High | Medium | Document partial result (C2–C3 completed). Tag accordingly. |
| R3→R1 dependency: M revision invalidates R1 | Low-Medium | Medium | Track dependency explicitly. Re-run R1 if M changes. |
| Numerical confirmation mistaken for independent derivation | Low (if discipline maintained) | HIGH (epistemic) | All numerical work tagged [Check]. Never cite numerical agreement as promotion evidence. |

---

## Checkpoints (STOP-and-ASSESS)

### Checkpoint A (after R4):

- Is the local optimality derivation clean within the pinning model?
- Are the four assumptions of Lemma 2 clearly stated?
- Does numerical [Check] confirm the analytic result?
- → If clean: proceed to R3
- → If not: identify blocker before R3

### Checkpoint B (after R3):

- Did we derive a barrier **along the chosen path**, or merely fit one?
- Is the secondary minimum genuinely stabilized by Hessian computation,
  or only plausibly supported by symmetry/observation?
- Which parts earned [Dc], which remain [P*], which are [OPEN]?
- Specifically:
  - Geometric V(q) shape: [Dc]?
  - Secondary minimum existence: [Dc] or [P*]?
  - Barrier height in MeV: [OPEN conditional]?
  - M(q) scaling form: [Dc]? Numerical coefficient: [P]?
- Was Put C step C4 completed, partially completed, or blocked?
- → Record all tags before proceeding to R1

### Checkpoint C (after R1):

- Did we derive a **unique ratio**, a **constrained range**, or only a
  **model-dependent value**?
- Which assumption dominates the result? (Likely: R₅ choice)
- Is the R₅ that gives π² independently justified, or selected by
  τ_n matching (circular)?
- What is L₀/δ under each candidate R₅?
- Does τ_n survive only conditionally (under specific R₅)?
- Does M imported from R3 need revision?
- → Record L₀/δ result and its exact epistemic status before Integration

---

## Guard Compliance

All results in Phase 1 are anchored in the S_EDC picture, but different
levels of directness apply:

| Level | Description | Examples in Phase 1 |
|-------|-------------|---------------------|
| **Direct from S_EDC** | Derived from stated action terms without auxiliary model | Steiner optimality (Ch.1), κ=2π (Ch.7), Z₃ subgroup |
| **Effective reduction anchored in S_EDC** | Derived within an explicitly declared reduction (collective coordinate, localization model) whose inputs come from S_EDC | V(q) along chosen path, L₀/δ within localization model |
| **Explicit auxiliary ansatz** | A model choice not derivable from S_EDC alone but physically motivated | Square-well V_loc, R₅ mode-count assumption, constant-M approximation |

Every effective reduction, collective-coordinate choice, localization
ansatz, and stability assumption must be explicitly tagged and never
misrepresented as direct action-level closure.

Specific guards:
- **G1 (Ontological purity)**: Zero SM input. EDC-native vocabulary throughout.
- **G2 (Empirical protocol)**: Δm_np, B_d, τ_n appear only as verification targets.
- **G3 (Epistemic honesty)**: Every step tagged with exact class. No promotion
  without closed chain at the claimed level. Ansatz-dependent results tagged
  with ansatz name.
- **G4 (Vocabulary)**: EDC-native throughout.
- **G5 (Derivation chain)**: Every step traceable to S_EDC or to a named
  effective reduction/ansatz. No unnamed gaps.
- **G6 (Reproducibility)**: Verification scripts for all numerical claims,
  tagged [Check].
- **G7 (No contamination)**: Derive in EDC → compare to measurement. Never reverse.
- **G8 (No back-promotion)**: Integration cannot elevate input tags.
  Numerical agreement is [Check], not evidence for promotion.

---

## Phase 1 Exit States

Phase 1 may terminate in one of four states. All are legitimate outcomes.

### Exit A: Strong Partial Closure

- R4 closes at [Dc] within pinning model
- R3 produces [Dc] geometric V(q) with [P*] secondary minimum
- R1 produces [Dc(model)] L₀/δ with constrained range including or near π²
- τ_n retains derived support with reduced [P]-dependence
- **Outcome**: Significant progress. Neutron line strengthened.

### Exit B: Mixed Closure with Exposed Open Bridge

- R4 closes at [Dc]
- R3 partially closes (barrier shape [Dc], minimum [P*], height [OPEN])
- R1 produces function L₀/δ = F(R₅/δ) but R₅ remains [P]
- τ_n depends on one or two named [P] assumptions
- **Outcome**: Genuine progress. Open bridges are now named and testable.
  Phase 2 has clear targets.

### Exit C: Non-Confirmation of Preferred Constants

- R1 derives L₀/δ ≠ π² under all plausible R₅ assumptions
- Or R3 barrier height ≠ 2Δm_np from geometry
- τ_n deviates from 878.4 s under derived inputs
- **Outcome**: The derived values replace postulated ones. The theory
  is more honest. If deviation is large, the neutron line weakens but
  the model's predictive boundaries are clarified.

### Exit D: Critical Failure of Neutron Line

- R3 fails to produce a secondary minimum (no double-well)
- Or derived L₀/δ is far from any value giving reasonable τ_n
- The instanton tunneling mechanism does not survive stricter derivation
- **Outcome**: A negative result. The metastable-junction model for
  neutron decay requires fundamental revision or abandonment. This is
  still publishable and scientifically valuable.

**All four exits advance the research program.** The plan must not
psychologically force only success-like outcomes.

---

**Last updated:** 2026-03-13 (v3.1 — mini hardening pass)
