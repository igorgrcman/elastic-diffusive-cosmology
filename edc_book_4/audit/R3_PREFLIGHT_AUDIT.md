# R3 Preflight Audit

**Date:** 2026-03-13
**Branch:** `research/topological-pinning-v7_8-integration`
**Status:** AUDIT ONLY — no R3 implementation

---

## 1. Executive Verdict

R3 cannot be executed as a full implementation pass (Mode A). The repo
contains a well-structured reduction corridor (Put C) but all computational
steps remain open — the corridor is scaffolding, not derivation. The
secondary minimum has no Hessian computation, only a plausibility argument
from observational absence of partner states. The barrier height depends on
an unresolved unit identification (E_arm ≡ Δm_np) that cannot close within
Phase 1. The effective mass M(q) has no donor computation anywhere in the
repo. **Recommended execution mode: B (partial closure only)** — implement
the geometric V(q) shape along the chosen path and the barrier existence
claim, but do not overclaim closure of the secondary minimum, barrier height
in physical units, or M(q) numerical coefficient.

---

## 2. Scope of Audit

### Files Inspected

| File | Purpose |
|------|---------|
| `edc_book_4/PHASE1_PLAN_REVISED.md` | Canonical plan (source of truth) |
| `edc_book_4/chapters/ch03_neutron_metastable.tex` | Target chapter: V(q), barrier height |
| `edc_book_4/chapters/ch06_instanton.tex` | Target chapter: S_E, M(q), instanton |
| `edc_book_2/src/derivations/S5D_TO_SEFF_Q_REDUCTION.md` | Put C corridor |
| `edc_book_2/src/derivations/Z3_SYMMETRY_ANALYSIS_NEUTRON.md` | Z₃ stability argument |
| `edc_book_2/src/derivations/V_B_FROM_Z3_BARRIER_CONJECTURE.md` | Barrier height conjecture |
| `edc_book_4/code/kramers_double_well_v2.py` | Kramers escape code |
| `edc_book_4/code/book4_kramers_validation.py` | Kramers validation |
| `edc_book_4/main.tex` | Appendix wiring |
| `edc_book_4/preamble.tex` | Macros and environments |

---

## 3. Donor Inventory

| Asset | Location | Relevance to R3 | Epistemic Quality | Reusable? |
|-------|----------|-----------------|-------------------|-----------|
| Put C corridor (5D→1D) | `edc_book_2/src/derivations/S5D_TO_SEFF_Q_REDUCTION.md` | Central — defines reduction pathway | Framework [Dc], all integrals OPEN | Partial — scaffolding reusable, no computed content to import |
| Z₃ symmetry analysis | `edc_book_2/src/derivations/Z3_SYMMETRY_ANALYSIS_NEUTRON.md` | Secondary minimum stability | Plausibility [P]+[BL]+[M], no Hessian | Partial — Landau expansion framework reusable, stability claim not closable |
| V_B conjecture | `edc_book_2/src/derivations/V_B_FROM_Z3_BARRIER_CONJECTURE.md` | Barrier height identification | Conditional [Dc], key link OPEN | Partial — Z₃ factor-of-3 argument reusable, unit ID not closable |
| q definition (Put C) | Put C §2 | Collective coordinate | [Def] — geometric definition clear | Yes — q = ξ_node(t) − ξ₀ |
| 5D action decomposition | Put C §1-3 | Action structure | [Def]+[I] | Yes — S_bulk + S_brane + S_GHY + S_junc |
| Kramers code | `edc_book_4/code/kramers_double_well_v2.py` | Numerical V(q) verification | [Dc] framework, phenomenological V(q) | Partial — framework yes, V(q) form must be replaced |
| Ch.3 V(q) description | `ch03_neutron_metastable.tex` §3 | Current V(q) status | [P] — postulated, no functional form | No — must be upgraded by R3, not imported from |
| Ch.6 instanton formalism | `ch06_instanton.tex` §2-3 | S_eff[q] structure | [Der] for WKB form, [P] for V(q) and M(q) inputs | Yes — WKB integral structure is sound |
| Δm_np value | V_B conjecture doc | Baseline datum | [BL] = 1.2933 MeV | Yes — comparison target only |
| Steiner optimality | Ch.1 ([Der]) | q=0 is global minimum | [Der] | Yes — anchor for V(q=0) |

---

## 4. Put C Corridor Status

Explicit breakdown of steps as they exist in `S5D_TO_SEFF_Q_REDUCTION.md`:

| Step | Description | State | Content Type |
|------|-------------|-------|-------------|
| **C1** | Choose collective coordinate ansatz | **Donor-ready** | q(t) defined geometrically as junction node displacement. Metric ansatz and brane embedding specified. [Def]+[I] |
| **C2** | Insert ansatz into 5D action components | **Placeholder** | Schematic form of L(q, q̇, φ_α) shown. ALL explicit integrals listed as OPEN: S_bulk evaluation, h_μν(q) computation, K(q) computation, S_junc for Y-junction. No computed expression for any component. |
| **C3** | Integrate out fast modes (Born-Oppenheimer) | **Placeholder** | Adiabatic reduction procedure described. Timescale separation assumed but not verified. Standard framework, but no actual mode integration performed. |
| **C4** | Extract canonical form S_eff[q] = ½M(q)q̇² − V(q) | **Placeholder** | Formal definitions given: M(q) := ∂²L_eff/∂q̇², V(q) := −L_eff(q,0). Both are OPEN — no functional form computed. 14 explicit OPEN items listed in §6. |

**Verdict:** Put C is a **well-structured empty corridor**. The mathematical
pathway is honest and clear, but no computational step has been executed.
R3 cannot claim "completion of C2-C4" unless those integrals are actually
computed. The strongest honest outcome for Put C within Phase 1:

- **Geometric V(q) shape from Nambu-Goto brane energy**: achievable [Dc]
  without completing full Put C. This bypasses C2-C4 by computing E_brane(q)
  directly from arm-length geometry, rather than going through the full
  5D action reduction.
- **Full C2-C4 completion**: NOT achievable in Phase 1. The integrals
  (S_bulk with Λ₅, extrinsic curvature K(q), fast-mode integration) are
  substantial calculations that have not been attempted.
- **Honest tag for Put C after Phase 1**: partial [Dc] + [OPEN]. The
  geometric contribution is derivable; the full action-level reduction
  remains open.

---

## 5. q-Coordinate Assessment

### What q Is Currently

- **In Put C:** q(t) = ξ_node(t) − ξ₀ (junction node displacement along
  compact 5D coordinate). [Def] — geometric definition.
- **In Ch.3:** q ∈ [0,1] scalar parametrizing deformation path between
  anchor and metastable configurations. Tagged [Dc] but with caveat that
  "precise definition requires dimensional reduction from full 5D action."
- **In Ch.6:** Inherited from Ch.3 as given. Used in S_eff[q] without
  further justification.
- **In V_B conjecture doc:** Not explicitly discussed.

### Assessment

The coordinate q is used consistently across donor files and chapters.
Its geometric motivation is clear (junction displacement). However:
- It is a **chosen parametrization**, not a uniquely derived normal mode.
- The linear interpolation between Z₆ and Z₃ configurations is one
  possible path; other parametrizations could yield different V(q).
- No donor file computes whether q is the lowest-energy deformation
  mode or merely a convenient coordinate.

### Strongest Honest Future Wording

**"Chosen collective interpolation parameter"** — as specified in the
canonical plan. The wording "motivated collective coordinate" would also
be acceptable. The wording "reduction ansatz" is slightly too strong
(implies a systematic reduction procedure was performed, which Put C
has not completed).

---

## 6. Secondary Minimum Assessment

### What Exists

1. **Landau expansion framework** (Z3_SYMMETRY_ANALYSIS): Generic form
   E(q,Δ) = E₀(q) + a(q)Δ² + b(q)Δ⁴. Stability requires a(q_n) > 0.
   Coefficients a(q), b(q) are NOT computed.

2. **Observational constraint** [BL]+[M]: Absence of low-lying doublet
   partners in baryon spectrum constrains a(q_n) > 0 or pushes splitting
   above observable energy. The Z3_SYMMETRY_ANALYSIS doc is explicit:
   "This is a [BL]+[M] constraint, NOT a strict mathematical proof."

3. **Steiner theorem at anchor** [Der]: a(0) > 0 is proven (the anchor
   is a genuine minimum). This does NOT extend to a(q_n) > 0.

4. **Symmetry argument**: Z₃ is a subgroup of Z₆, so breaking Z₃ breaks
   more symmetry and is "generically costly." This is a plausibility
   argument, not a derivation.

### What Does Not Exist

- **No Hessian computation** at q_n. Explicitly marked [OPEN] in the
  Z3_SYMMETRY_ANALYSIS doc (line 233: "needs calculation").
- **No numerical coefficients** for a(q), b(q).
- **No 5D energy functional evaluation** at the Z₃ configuration.
- **No demonstration that q_n is a local minimum** rather than an
  inflection point or shoulder.

### Strongest Honest Current Tag

**[P]** — postulated, with [BL]+[M] observational support.

The secondary minimum is motivated by symmetry and observational absence,
but not derived. It cannot be promoted beyond [P] without a Hessian
computation or equivalent stability demonstration. The canonical plan's
target of [P*] (partially derived) would require at least computing
V''(q_n) > 0 along the chosen path.

---

## 7. Barrier Height Assessment

Three distinct questions, as required by the canonical plan:

### 7a. Barrier Shape (Does a Maximum Exist Between q=0 and q_n?)

**Donor status:** The geometric V(q) from Nambu-Goto brane energy
(E_brane(q) = σ × Σ ℓ_i(q)) is computable. The anchor at q=0 is a
Steiner minimum [Der]. If the Z₃ configuration at q_n has higher brane
energy (which it does — non-Steiner configurations have longer total arm
length), then continuity guarantees a maximum between q=0 and q_n.

**Achievable tag:** [Dc] — derivable from explicit geometric computation
along the chosen path.

**Caveat:** This assumes V(q) along the chosen linear interpolation path.
A different path could have a different barrier profile.

### 7b. Barrier Height in Geometric/Tension Units

**Donor status:** No computation exists. The V_B conjecture doc gives
V_B ≈ 2.6 MeV from WKB calibration [Cal], not from geometric computation.

**What R3 can do:** Compute V_B = σ × [L_total(q_B) − L_total(q_n)] in
σ-units from the arm-length formula. This is a straightforward geometric
calculation. The result would be V_B in units of (σ × fm), not in MeV,
unless σ is converted using its known value.

**Achievable tag:** [Dc] for the geometric barrier height in σ-units.
Converting to MeV uses σ = 8.82 MeV/fm² [Dc from Book I], so the
converted height would also be [Dc].

**Risk:** The geometric barrier height may or may not equal 2Δm_np.
If it doesn't, that is a genuine finding, not a failure.

### 7c. Barrier Height Identification V_B = 2Δm_np

**Donor status:** The V_B conjecture doc establishes:
- Z₃ symmetry → E_B = 3 × E_arm [Der from symmetry]
- Unit identification E_arm ≡ Δm_np [OPEN — explicitly marked]
- Result: V_B = 2 × Δm_np [Dc conditional on unit ID]

The critical missing piece is: **why does E_arm equal Δm_np?** The
conjecture doc says (line 94): "OPEN: 'One unit per leg = Δm_np' requires
5D action verification." This link requires either:
- Full Put C completion (5D brane energy → observer-frame mass mapping), or
- An independent geometric argument for the energy quantum.

Neither exists in the repo.

**Achievable tag within Phase 1:** [OPEN conditional]. The shape and
geometric height are derivable; the identification with Δm_np is not.

---

## 8. Effective Mass Assessment

### What Exists for M(q)

- **Put C doc:** Formal definition M(q) := ∂²L_eff/∂q̇². [Def] — no
  functional form computed. Listed as OPEN in §6.
- **Ch.6:** M(q) = M (constant approximation). Tagged [P]. Sources listed
  as junction inertia + brane kinetic energy + bulk contributions. No
  numerical value specified beyond "order the junction mass scale."
- **Kramers code:** Uses unit mass (dimensionless). No physical mass.
- **Canonical plan:** Proposes M ≈ 3σδ²/c² as scaling estimate.

### What Is Missing

- **No computation of M(q) from the 5D action** anywhere in the repo.
- **No numerical evaluation** of the proposed scaling M ≈ 3σδ²/c².
- **No verification that constant-M approximation is valid** (M(q) could
  vary significantly between q=0 and q_B).
- **No donor file addresses the q-dependence of M**.

### Strongest Honest Claim

- **Functional scaling M ∝ σδ²/c²**: [P] — dimensional analysis within
  the Nambu-Goto framework. The σδ² combination has dimensions of
  (energy/length) × (length²) = energy×length, which with c² gives mass.
  But the proportionality constant is undetermined.
- **Numerical coefficient (factor 3)**: [P] — depends on arm count,
  embedding geometry, and q normalization. Not computed.
- **q-independence**: [P] — assumed, not verified.

**Bottom line:** M(q) is the weakest link in R3. There is essentially
no donor content to build on. The appendix can state the scaling argument
but must be honest that the coefficient is undetermined and q-dependence
is unknown.

---

## 9. Chapter Impact Assessment

### Ch.03 (Metastable Junction)

| Section | Current State | If R3 Delivers Partial Results |
|---------|--------------|-------------------------------|
| §2.3: q definition | [Dc] with caveat | Can strengthen if geometric path is made explicit |
| §3: V(q) double-well | [P], no functional form | Can promote geometric shape to [Dc]; functional form remains [P*] |
| §3.3: Open box (V(q) from 5D) | [OPEN] | Can partially close: barrier existence [Dc], full V(q) remains [OPEN] |
| §4.2: Step 1 (Z₃ → factor 3) | [Der] | No change — this is sound |
| §4.2: Step 2 (E_arm ≡ Δm_np) | [OPEN] | Cannot close in Phase 1 |
| §4.3: Open box (unit quantization) | [OPEN] | Cannot close |
| §4.4: Physical picture table | Fixed energy levels | Must add caveat that levels use [OPEN] unit ID |

**Promotable:** Geometric barrier existence. V(q) shape along chosen path.
**Must remain conservative:** Secondary minimum ([P] or [P*] at best).
Barrier height in MeV ([OPEN conditional]). E_arm identification ([OPEN]).

### Ch.06 (Instanton)

| Section | Current State | If R3 Delivers Partial Results |
|---------|--------------|-------------------------------|
| §1.1: V(q) recap | [P] from Ch.3 | Can note geometric shape is now [Dc]; height remains [P] |
| §2.2: M(q) definition | [P] constant | Can add scaling estimate but remains [P] |
| §2.3: WKB integral | [Der] for form, [P] inputs | No change — integral form is sound; inputs remain [P] |
| §3.2: Bounce solution | Depends on V(q), M(q) | Cannot close without explicit V(q) functional form |
| §4.2-4.3: Prefactor, ω_z | [Cal] and [P] | Cannot close — requires M(q) and V''(q_n) |
| Parametric form S_E/ℏ = κ(L₀/δ) | [P] | Cannot validate from R3 alone |

**Risk:** If R3 shows V(q) shape differs significantly from the assumed
quartic double-well, the bounce solution in Ch.6 needs qualitative
revision. If V(q) shape is broadly consistent, Ch.6 can proceed with
updated references but no structural change.

---

## 10. Recommended R3 Execution Mode

### Mode B: Partial Closure Only

**Justification:**

1. **Full R3 (Mode A) is not realistic** because:
   - Put C steps C2-C4 are entirely open (no integrals computed)
   - M(q) has zero donor content
   - Secondary minimum has no Hessian
   - E_arm ≡ Δm_np is structurally unclosable in Phase 1

2. **Splitting R3 (Mode C) is unnecessary** because the partial closure
   is coherent as a single pass — the deliverables that CAN be done form
   a natural unit.

3. **Delaying R3 (Mode D) is wrong** because the geometric V(q) shape IS
   computable now without any external dependency, and it provides real
   value.

### What Mode B Delivers

| Subtarget | Achievable? | Target Tag |
|-----------|-------------|------------|
| R3a: Geometric V(q) along chosen path | **YES** | [Dc] |
| R3a': Barrier existence along path | **YES** | [Dc] |
| R3a'': Barrier height in σ-units | **YES** | [Dc] |
| R3b: Secondary minimum stability | **PARTIAL** — V''(q_n) along path only | [P*] at best, likely [P] |
| R3c: V_B = 2Δm_np identification | **NO** | [OPEN conditional] |
| M(q) scaling form | **PARTIAL** — dimensional argument only | [P] |
| M(q) numerical coefficient | **NO** | [P] |
| Put C C2-C4 completion | **NO** | Remains OPEN |

### What Mode B Does NOT Deliver

- Full effective potential from 5D action
- Hessian-verified secondary minimum
- Barrier height in observer-frame units (MeV) from geometry alone
  (needs σ conversion, which is [Dc] from Book I but not from R3)
- Effective mass from first principles
- Put C completion

---

## 11. Proposed Next Prompt Scope

The R3 implementation prompt should be scoped to **Mode B deliverables only**:

### In Scope

1. **Appendix** (`app_Vq_collective_coordinate.tex`):
   - Define q as chosen interpolation parameter between Z₆ and Z₃
   - Compute E_brane(q) = σ × Σ ℓ_i(q) from explicit arm-length formula
   - Show E_brane(0) is global minimum (Steiner, [Der])
   - Show barrier exists between q=0 and q_n (continuity + geometric argument)
   - Compute barrier height in σ-units from arm-length differences
   - State V''(q_n) status: computable along path but not Hessian in transverse directions
   - State M(q) scaling argument with honest [P] tag
   - State E_arm ≡ Δm_np as [OPEN]
   - Section on what Put C would additionally provide (and doesn't yet)

2. **Verification script** (`r3_vq_verify.py`):
   - Implement E_brane(q) from arm-length geometry
   - Verify barrier existence (separate gate from minimum existence)
   - Verify V''(q_n) > 0 along chosen path (separate gate)
   - Report barrier height in σ-units
   - Compare to 2Δm_np as consistency check [Check], not derivation
   - Plot V(q) profile

3. **Chapter updates** (ch03, ch06):
   - Graded: geometric shape [Dc], minimum [P] or [P*], height [OPEN]
   - Do not flip any tag beyond what the appendix actually earns

### Out of Scope

- Put C integral computations (C2-C4)
- Hessian in transverse directions
- M(q) derivation beyond scaling argument
- E_arm ≡ Δm_np resolution
- Bounce solution in Ch.6
- Prefactor A or ω_z derivation

### Key Constraint

The implementation prompt must explicitly forbid claiming Put C completion.
The geometric V(q) bypasses Put C by computing E_brane directly — this is
a different (simpler) calculation, not Put C step C2.

---

## 12. Red Flags

- **Inflation risk 1:** Calling the geometric E_brane(q) computation "Put C
  completion." It is not. Put C requires the full 5D action reduction
  including S_bulk, K(q), and fast-mode integration. E_brane is only the
  Nambu-Goto surface contribution.

- **Inflation risk 2:** Treating V''(q_n) > 0 along the chosen path as
  proof of a genuine metastable minimum. It only proves a minimum along
  one direction in configuration space. Transverse directions are unchecked.

- **Inflation risk 3:** Using numerical agreement between geometric V_B
  and 2Δm_np as evidence for the E_arm ≡ Δm_np identification. Agreement
  is [Check], not derivation.

- **Inflation risk 4:** Presenting M ≈ 3σδ²/c² as if it were derived from
  the 5D action. It is dimensional analysis with a guessed coefficient.

- **Inflation risk 5:** Importing σ = 8.82 MeV/fm² to convert geometric
  barrier height to MeV, then claiming the result is "derived" when σ
  itself was calibrated in Book I via a chain that may involve [Cal] steps.

- **Circularity risk:** If the only reason the geometric V_B matches
  2Δm_np is because the arm-length parametrization was implicitly
  calibrated to produce that match, the "derivation" is circular. The
  verification script must check whether the match is a consequence of
  geometry or of parameter choice.

---

## 13. Bottom Line

R3 has enough donor material for a **genuine partial closure**: the
geometric V(q) shape along the chosen collective path, barrier existence,
and barrier height in σ-units are all honestly derivable. Everything
beyond that — secondary minimum stability, barrier height in physical
units, M(q), Put C completion — either lacks donor content or depends on
structurally unresolved links. Execute R3 as Mode B with explicit scope
limits and no overclaiming. The partial result is real and valuable; it
replaces a naked postulate [P] with a computed geometric profile [Dc]
and exposes the exact remaining gaps for Phase 2.

---

**Audit completed:** 2026-03-13
