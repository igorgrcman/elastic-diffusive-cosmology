# N7 WP1: Donor Normalization for Thick-Junction / Internal-Core Route

**Date:** 2026-03-13
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Normalization task — no derivation, no implementation
**Governing documents:**
- `PHASE2_PLAN_V1.md` (v1.1)
- `PHASE2_NEXTSTEP_PLAN_V1.md`
- `audit/PHASE2_WP1_DONOR_NORMALIZATION.md` (WP1 original — for Put C corridor)

---

## 1. Executive Verdict

The donor base for the N7 thick-junction/internal-core lane has been
inspected, classified, and normalized. **Eleven donor assets** were
reviewed across four branches. Five are cleared for N7 use (two central,
three supporting). Four are archived as dead-end / no-go references.
Two are classified as **forbidden positive donors** (circular or
phenomenological content that must not be imported as [Dc]).

The N7 lane has one structurally reusable framework (separable core
ansatz from `junction-core-derive-C-v1`) and one validated geometric
baseline (V_geom [Dc] from Phase 1 R3). Everything else is either
constraint material or forbidden imports.

**The donor base is clean enough for N7 WP2 to begin**, provided the
explicit allowed/forbidden import lists in §10–§11 are respected.

---

## 2. Scope of This Normalization

### Branches/Files Inspected

| # | Source | Key Files | Purpose |
|---|--------|-----------|---------|
| 1 | `junction-core-derive-C-v1` | `DERIVE_C_FROM_GEOMETRY.md`, `JUNCTION_CORE_EXECUTION_REPORT.md`, `derive_C_integrals.py`, `junction_core_well.py` | Core donor: separable ansatz, C structure, numerical scan |
| 2 | `delta-audit-anchor-v1` | `DELTA_ANCHOR_MAP.md` | Scale hierarchy, δ anchoring |
| 3 | `putC-computation-v1` | `S5D_TO_SEFF_Q_REDUCTION.md`, `PUTC_EXECUTION_REPORT.md`, `putC_compute_MV.py` | Put C corridor, Variant 3 comparison baseline |
| 4 | Current branch | `PHASE2_PLAN_V1.md`, `PHASE2_NEXTSTEP_PLAN_V1.md`, `PHASE2_WP1_DONOR_NORMALIZATION.md`, `app_P2_WP2_Israel_nodewell.tex`, `app_Vq_chosen_path.tex`, `ch03_neutron_metastable.tex` | Phase 2 status, WP2 no-go constraint, V_geom baseline |

### What This Document Does

- Identifies which donor material from the junction-core branches is
  reusable (structure vs value)
- Separates viable structural content from circular/phenomenological
  material
- Normalizes the allowed model scope for N7
- Defines canonical symbols and scales for the thick-junction lane
- Prepares a clean donor bundle with explicit allowed/forbidden lists

### What This Document Does Not Do

- No derivation. No new equations. No implementation.
- Does not determine the core profile f(q/δ) — that is WP2 work.
- Does not resolve the δ-scale ambiguity — that is out of scope (Rank 2).
- Does not upgrade any epistemic tag.

---

## 3. Central Donor Assets

These are the **primary donors** the N7 lane is authorized to build upon.

| # | Asset | Location | Content | Quality | Reusable? |
|---|-------|----------|---------|---------|-----------|
| **D-N7-1** | Separable core ansatz framework | `junction-core-derive-C-v1` : `DERIVE_C_FROM_GEOMETRY.md` §3 | ρ_core(r⊥, q) = σ × g⊥(r⊥/r₀) × f(q/δ); 3D→1D reduction via transverse integration; structural relation C = I⊥ × (r₀/δ)² | [Dc] structural | **YES — central.** The separable ansatz and the 3D→1D reduction procedure are reusable. The transverse integration yielding A_eff = r₀² × I⊥ is clean [Dc]. |
| **D-N7-2** | V_geom(q) geometric baseline | Current branch : `app_Vq_chosen_path.tex` | V_geom(q) = τ × L_tot(q) [Dc]; Steiner minimum at q = 0; curvature V''(0) = 3τ/(2R); single-well | [Dc] (Phase 1 R3) | **YES — central.** Any thick-junction V_core must combine with this baseline. |

### What Makes These Central

- **D-N7-1** provides the only existing framework for computing junction-core
  energy as a function of q. The separable ansatz ρ_core = σ × g⊥ × f is a
  structural [Dc] result: it follows from dimensional analysis of a
  localized core with two length scales (r₀ transverse, δ longitudinal).
  The 3D→1D integration is standard.

- **D-N7-2** provides the validated single-well baseline that any new
  attractive term must overcome. V_geom is Phase 1 [Dc] and not contested.

---

## 4. Supporting Donor Assets

| # | Asset | Location | Content | Quality | Notes |
|---|-------|----------|---------|---------|-------|
| **S-N7-1** | Junction-core numerical scan results | `junction-core-derive-C-v1` : `JUNCTION_CORE_EXECUTION_REPORT.md` | 2340 configurations; 635 metastable; A1/A2/A3 mechanism comparison; V_B scaling with C | [Cal] scan | Comparison/calibration reference only. The scan results cannot be imported as [Dc] because profiles were postulated [P], not derived. |
| **S-N7-2** | Junction-core computation code | `junction-core-derive-C-v1` : `junction_core_well.py`, `derive_C_integrals.py` | V_total(q) = V_NG(q) + V_core(q) scanner; profile integral verification | [Cal] code | Infrastructure. Extend for new N7 variants. |
| **S-N7-3** | WP2 Israel no-go constraint | Current branch : `app_P2_WP2_Israel_nodewell.tex` | Thin-junction Israel conditions produce zero deficit angle; arm-interior energy ∝ V_geom; no attraction from thin-junction sector | [Dc] NO-GO | **Constraint donor.** Establishes that V_core cannot come from thin-junction matching. Any N7 result must reduce to this no-go in the δ → 0 limit. |

---

## 5. Dead-End / No-Go / Forbidden Donors

These must **not** be imported as positive evidence for the N7 lane.

| # | Asset | Location | Why Not Reusable as Positive Donor | Preserved Lesson |
|---|-------|----------|------------------------------------|------------------|
| **F-N7-1** | C = 100 numerical value | `DERIVE_C_FROM_GEOMETRY.md` §6.4 | C = (L₀/δ)² = (1.0/0.1)² = 100 uses L₀ = 1.0 fm [I] and δ = 0.1 fm [I]. The π factor from I⊥ was dropped by normalization choice (§6.4: "If f already includes normalization, C = (r₀/δ)²"). The value is [I]-dependent, not independently derived. **CIRCULAR.** | The *structure* C = I⊥ × (r₀/δ)² is [Dc]. The *value* 100 is not independent. N7 may use the scaling relation but must not cite C = 100 as derived evidence. |
| **F-N7-2** | Phenomenological node well (Variant 3) | `PUTC_EXECUTION_REPORT.md` §Variant 3 | V_node = −V₀ exp(−(q−q*)²/2w²) with V₀ = 10 MeV, q* = 2 fm, w = 0.4 fm [P/Cal]. Parameters fitted to produce V_B ≈ 2.8 MeV. No physical derivation. **[P/Cal], not [Dc].** | Demonstrates that IF an attractive node term exists with O(10 MeV) depth and width O(δ), metastability is achievable. Comparison target only. The functional form (Gaussian) is an output to be checked against, not an input. |
| **F-N7-3** | Helfrich bending route | `helfrich-well-from-action-v1` : `HELFRICH_EXECUTION_REPORT.md` | 260/260 NO-GO. V_bend ~ +κq²/a² (positive). **FALSIFIED.** | Bending rigidity cannot source metastability. Do not reintroduce under a different name. |
| **F-N7-4** | N1 Israel thin-junction energy | `app_P2_WP2_Israel_nodewell.tex` | Bounded no-go [Dc]. Deficit angle ≡ 0 for all q. Arm-interior Israel energy ∝ V_geom. **BOUNDED NO-GO.** | Thin-junction matching does not generate attraction. The N7 thick-junction route is specifically designed to test what the thin-junction approximation discards. |

---

## 6. Donor Provenance Decomposition: What Is Reusable vs What Is Circular

The `junction-core-derive-C-v1` branch contains a mixture of structural
[Dc] results and circular/phenomenological content. This section separates
them line by line.

### 6.1 Reusable Structural Content [Dc]

| Item | Source Section | What It Says | Why Reusable |
|------|--------------|--------------|--------------|
| Separable density ansatz | §3.2 | ρ_core(r⊥, q) = σ × g⊥(r⊥/r₀) × f(q/δ) | Dimensional decomposition of a localized source with two scales. Model-independent structure. |
| Transverse integration | §3.3 | A_eff = r₀² × I⊥ where I⊥ = ∫ d²ξ g⊥(\|ξ\|) | Standard 2D integral. Result I⊥ = π for Gaussian, squared-Lorentzian, uniform disk [Dc]. |
| C scaling structure | §3.4 | C = I⊥ × (r₀/δ)² | Follows algebraically from separable ansatz + transverse integration. Pure dimensional bookkeeping. |
| E₀ = σ × r₀² × I⊥ | §3.4 | Core energy scale = tension × effective transverse area | Dimensional closure [Dc]. Independent of δ. |
| E₀ = σ × L₀² reformulation | Delta anchor §4, §5 Option B | Energy scale depends on L₀ only, not δ | Removes explicit δ from magnitude. Strengthens [Dc] status. |
| V_core(q) = −E₀ × f(q/δ) form | §1 | Localized attractive potential at junction vertex | Structural form [Dc]. The profile f is [OPEN] — to be derived or constrained in N7 WP2. |
| Two-scale pancake picture | §10 | Core is wide (L₀) in brane plane, thin (δ) in bulk | Physical interpretation [Dc]. Consistent with junction as finite-size defect. |

### 6.2 Circular / Phenomenological Content (Forbidden)

| Item | Source Section | What It Says | Why Forbidden |
|------|--------------|--------------|---------------|
| C = 100 | §6.4 | C = (L₀/δ)² = (1.0/0.1)² = 100 | Uses L₀ [I] and δ [I]. I⊥ factor dropped by normalization choice. Value is [I]-dependent. |
| "Exact match" with best-fit | §7 | C_derived = 100 matches C_scan = 100 | Tautological: both use the same L₀, δ inputs. Not independent confirmation. |
| V_B = 2.87 MeV from C = 100 scan | Exec Report §4.2 | Best-match V_B | [Cal] result from parameter scan with C = 100 [I]. Not a derivation. |
| Epistemic upgrade C: [P/Cal] → [Dc] | §9 | "C is derived from geometry with no free parameters" | Overstated. C is [Dc] *conditional on* L₀ [I] and δ [I]. The claim "no free parameters" ignores the I⊥ normalization choice and the [I] inputs. Correct tag: [Dc\|I]. |
| f(q/δ) = exp(−(q/δ)²) (Gaussian) | Exec Report §2.2 (A1/A2) | Postulated profile | [P]. Not derived from stress balance or variational principle. Cannot be imported as [Dc]. |
| f(q/δ) = 1/(1 + (q/δ)²) (Lorentzian) | Exec Report §2.2 (A3) | Postulated profile | [P]. Same status as Gaussian. |

### 6.3 Summary: The Clean Donor Core

After stripping circular content, the reusable donor core is:

```
STRUCTURE (reusable):
  ρ_core(r⊥, q) = σ × g⊥(r⊥/r₀) × f(q/δ)          [Dc] ansatz
  A_eff = r₀² × I⊥                                    [Dc] integral
  C = I⊥ × (r₀/δ)²                                    [Dc] scaling
  E₀ = σ × L₀²  (equivalently σ × r₀² × I⊥)         [Dc] magnitude
  V_core(q) = −E₀ × f(q/δ)                            [Dc] form

OPEN (to be determined in N7 WP2):
  f(q/δ)   — the q-dependent profile                  [OPEN]
  g⊥(r⊥/r₀) — the transverse profile                 [OPEN] (I⊥ ~ π for reasonable choices)
  Sign of V_core(q) — attraction vs repulsion          [OPEN]

FORBIDDEN (do not import):
  C = 100                                              [I]-dependent
  f = Gaussian, Lorentzian                             [P] postulated
  V_B = 2.87 MeV                                      [Cal] scanned
```

---

## 7. Scale and Symbol Normalization for N7

### 7.1 Canonical Parameters

| Symbol | Canonical Meaning (N7 Lane) | Value | Tag | Source |
|--------|-----------------------------|-------|-----|--------|
| **σ** | Brane tension | 8.82 MeV/fm² | [Dc] | Book I, E_σ = m_e c²/α |
| **δ** | Junction-core scale (Compton anchor) | ℏ/(2m_p c) ≈ 0.105 fm | [I] | Delta anchor audit |
| **L₀** | Transverse junction extent | ≈ 1.0 fm | [I] | Nucleon scale identification |
| **r₀** | Transverse core radius | = L₀ [I] | [I] | Identified with junction footprint |
| **τ** | Effective 1D string tension | = σ in reduced context | [Dc] | Phase 1 |
| **R** | Y-junction arm length | O(1) fm | [Dc] | Geometric |
| **q** | Node displacement from Steiner center | [0, R) | [Dc] | Chosen path (R3) |

### 7.2 Derived Scales (N7-Specific)

| Symbol | Definition | Approximate Value | Tag | Notes |
|--------|-----------|-------------------|-----|-------|
| **E₀** | σ × L₀² (core energy scale) | 8.82 MeV | [Dc] | Independent of δ in this formulation |
| **C** | I⊥ × (L₀/δ)² (geometric amplification) | ≈ π × (L₀/δ)² | [Dc] structure / [I] value | Scaling is [Dc]; numerical value depends on L₀/δ [I] |
| **L₀/δ** | Aspect ratio of junction core | ≈ 9.5 (with δ = 0.105 fm) | [I] | Key ratio. If L₀ = 1.0 fm, δ = 0.105 fm: L₀/δ = 9.52. |
| **σδ²** | Bare core energy (no amplification) | ≈ 0.097 MeV | [Dc] | Too small by factor ~30 without geometric amplification |

### 7.3 The δ-Scale Hierarchy (Inherited from Delta Audit)

Four δ-like scales exist in EDC. N7 uses only one.

| Scale | Value | N7 Usage |
|-------|-------|----------|
| R_ξ ≈ 0.002 fm | Electroweak correlation length | **Not used.** Wrong sector. |
| Δ ≈ 0.003 fm | Electron mass formula | **Not used.** Different physics. |
| ℓ/(2π) ≈ 0.002 fm | Orbifold radius | **Not used.** Compactification scale. |
| **δ ≈ 0.105 fm** | **Junction core (Compton anchor)** | **Used.** δ = ℏ/(2m_p c) [I]. |

**N7 rule:** δ refers exclusively to the Compton-anchored scale.
The factor-50 ambiguity with R_ξ is acknowledged but not resolved
(out of scope). If N7 results depend sensitively on δ, this must
be reported as [I]-dependent.

### 7.4 The E₀ Reformulation (from Delta Audit)

The delta audit identified that E₀ = C × σ × δ² = σ × L₀² when
C = (L₀/δ)². This means:

```
E₀ = σ × L₀²    [Dc]
```

The energy scale depends on L₀ (transverse junction extent), not on δ.
The role of δ is confined to the *shape* of f(q/δ) — the decay profile
of V_core with distance from the vertex.

**Implication for N7:** The energy scale E₀ ≈ 8.82 MeV is set by σ
and L₀, both of which are used elsewhere in EDC. No new scale is
introduced for the magnitude. Only the profile shape requires δ.

---

## 8. Model-Class Boundary: What N7 Is and Is Not

### 8.1 What N7 Is (Allowed Model Scope)

The N7 thick-junction lane tests whether **regularizing the Y-junction
vertex at finite scale δ** produces a q-dependent core energy that,
combined with V_geom, creates a double-well potential.

**Allowed model class:**

1. Start from the separable core ansatz [Dc]:
   ρ_core(r⊥, q) = σ × g⊥(r⊥/r₀) × f(q/δ)

2. The transverse profile g⊥ and the q-profile f must be **derived or
   constrained** from one of:
   - (a) Stress balance at the regularized junction vertex
   - (b) Variational minimization of the regularized core action
   - (c) Matching to the thin-junction limit (WP2 no-go) as δ → 0
   - (d) Physical boundary conditions at the core boundary (r⊥ ~ r₀, q ~ δ)

3. The combined potential is:
   V(q) = V_geom(q) [Dc] + V_core(q) [Dc|model]

4. The outcome is one of:
   - Double-well → extract V_B, compare to 2Δm_np as [Check]
   - Single-well → no-go for N7 within the specified model
   - Attractive but too weak → partial result (mechanism real, scale insufficient)

### 8.2 What N7 Is Not (Forbidden Moves)

| Forbidden Move | Why | Anti-Smuggling Rule |
|----------------|-----|---------------------|
| Choosing f(q/δ) = Gaussian to match Variant 3 | CR2: relabeling phenomenological well | f must follow from stress/variational physics, not from desired V_B |
| Importing C = 100 as independent evidence | CR4: circular [I]-dependent value | Use scaling C ∝ (L₀/δ)² only; report results as function of L₀/δ |
| Using τ_n to constrain f | CR5/CR9: output used as input | τ_n appears only in final Ch.09 comparison, never in V_core derivation |
| Scanning profiles until V_B ≈ 2.6 MeV | CR1: calibration dressed as derivation | Compute V_core first, then check V_B. If match requires tuning → [Cal] |
| Reintroducing Helfrich bending | CR7: reviving falsified mechanism | Any new curvature term must be checked against Helfrich no-go |
| Claiming V_core is "derived" when f is postulated | Tag inflation | If f is [P], then V_core is [Dc\|P] at best, not [Dc] |

### 8.3 The Anti-Smuggling Test

Before N7 WP2 can claim a result, the following test must pass:

> **Delete all knowledge of τ_n, V_B ≈ 2.6 MeV, and the Variant 3
> Gaussian from the derivation. Does the derivation still stand?
> Does it still produce the same V_core(q)?**

If yes: the result is honest [Dc|model].
If no: the result is [Cal] dressed as [Dc].

---

## 9. Circularity / Smuggling Risk Register (N7-Specific)

All risks from WP1 §9 are inherited. N7 adds:

| # | Risk | Mechanism | Anti-Smuggling Rule |
|---|------|-----------|---------------------|
| **CR2** (primary) | Relabeling phenomenological well | Core profile f(q/δ) chosen to reproduce Variant 3 Gaussian, making the result [P/Cal] dressed as [Dc\|model]. | f must follow from regularization physics. Compute V_core, then compare to Variant 3. If match is coincidental and traceable → accept. If engineered → reject. |
| **CR4** | C = 100 imported as evidence | Using E₀ = 100 σδ² to set energy scale, when 100 = (L₀/δ)² uses two [I] inputs. | Report V_core as function of L₀/δ. The scaling C ∝ (L₀/δ)² is [Dc]; the value is [I]-dependent. |
| **CR9** (new) | Profile chosen to match τ_n | The only constraint on f is that V_core creates V_B ≈ 2Δm_np. | f must be derived before V_B is computed. The derivation of f must not reference τ_n, V_B, or Δm_np. |
| **CR10** (new) | Transverse profile g⊥ tuned to adjust E₀ | If g⊥ is chosen to make I⊥ larger/smaller to tune E₀, the result is [Cal]. | For well-behaved profiles, I⊥ ≈ π (Gaussian, squared-Lorentzian, disk all give π). If a non-standard g⊥ is used, justify from physics, not from E₀ matching. |
| **CR11** (new) | Separability assumed to avoid hard integral | If ρ_core does not actually separate, the ansatz is [P], not [Dc]. | State separability as a model assumption [P]. If possible, bound the error from non-separable corrections. |

---

## 10. N7 WP2 Allowed Inputs

### Central Inputs

| Input | Source | Tag | What N7 WP2 May Use |
|-------|--------|-----|---------------------|
| Separable core ansatz structure | D-N7-1 | [Dc] structural | Ansatz form, 3D→1D reduction, C scaling |
| V_geom(q) = τ L_tot(q) | D-N7-2 | [Dc] | Geometric baseline; Steiner minimum; curvature 3τ/(2R) |
| σ = 8.82 MeV/fm² | Book I | [Dc] | Brane tension |
| δ = ℏ/(2m_p c) ≈ 0.105 fm | Delta audit | [I] | Core decay scale |
| L₀ ≈ 1.0 fm | Phase 1 | [I] | Transverse junction extent |
| E₀ = σ × L₀² ≈ 8.82 MeV | D-N7-1 + Delta audit | [Dc] | Core energy scale (independent of δ) |
| WP2 Israel no-go | S-N7-3 | [Dc] NO-GO | Constraint: thin-junction limit produces no attraction |
| Δm_np ≈ 1.293 MeV | PDG | [BL] | Comparison target only; NOT derivation input |

### Supporting Inputs (Use If Needed)

| Input | Source | Tag | What N7 WP2 May Use |
|-------|--------|-----|---------------------|
| Junction-core scan results | S-N7-1 | [Cal] | Comparison/calibration baseline. Which C values produce metastability. |
| Junction-core code | S-N7-2 | [Cal] code | V(q) scanner infrastructure. Extend with new variants. |
| Put C corridor (C1–C4) | WP1 D1 | [Dc] structural | Action decomposition if needed for stress-balance derivation |
| putC_compute_MV.py | WP1 S2 | [Cal] code | Extend if V_core computation requires new numerical framework |

### Assumptions N7 WP2 Must State Upfront

1. **Separable core density** [P] — the ansatz ρ_core = σ × g⊥ × f
   separates transverse and longitudinal degrees of freedom.
2. **Core scale δ** [I] — the Compton-anchored δ = ℏ/(2m_p c) is the
   decay scale of f(q/δ).
3. **Transverse extent r₀ = L₀** [I] — the core transverse radius
   equals the junction extent L₀.
4. **Which regularization model** — smoothed junction, elastic
   membrane, variational minimum, or other. Declared as [P] or [Dc|model].
5. **What determines f(q/δ)** — stress balance, variational principle,
   matching conditions, or other physical constraint.

---

## 11. N7 WP2 Forbidden Imports

| Forbidden Import | Why |
|-----------------|-----|
| C = 100 as independent evidence | [I]-dependent. Circular (F-N7-1). |
| f(q/δ) = exp(−(q/δ)²) as [Dc] | [P] postulated profile (F-N7-2). Must be derived, not assumed. |
| f(q/δ) = 1/(1 + (q/δ)²) as [Dc] | [P] postulated profile. Same status as Gaussian. |
| V_B = 2Δm_np as constraint | [P] conjecture. V_B is computed output, not input (CR1). |
| V_B = 2.87 MeV from C = 100 scan | [Cal] result from forbidden C value. |
| τ_n ≈ 878 s as constraint on V_core | [BL] comparison only. Never enters V_core derivation (CR5/CR9). |
| Helfrich bending as attraction source | FALSIFIED (F-N7-3). |
| N1 Israel thin-junction energy | Bounded no-go (F-N7-4). |
| Phenomenological Gaussian well (Variant 3) as [Dc] | [P/Cal]. Comparison target only (F-N7-2). |
| Double-well structure as assumed | [P]. N7 WP2 tests whether it emerges. |
| ω₀ = 19 MeV | [P] dimensional estimate. Not a derivation input. |

---

## 12. Bottom Line

The N7 thick-junction donor base reduces to a clean core:

**One structural framework** (separable core ansatz from
`junction-core-derive-C-v1`): provides the 3D→1D reduction template,
the C scaling structure, and the V_core functional form. All reusable
as [Dc] structural content.

**One geometric baseline** (V_geom [Dc] from Phase 1 R3): the
single-well that any core attraction must overcome.

**One constraint** (WP2 Israel no-go [Dc]): the thin-junction limit
produces no attraction. N7 must recover this in the δ → 0 limit.

**One energy scale** (E₀ = σ × L₀² ≈ 8.82 MeV [Dc]): set by tension
and transverse extent. Independent of δ. The right order of magnitude
to compete with V_geom.

**One open question** (the profile f(q/δ) [OPEN]): this is the
entire content of N7 WP2. The q-dependence of the core energy must
be derived from regularization physics — stress balance, variational
minimization, or physical boundary conditions at the core boundary.
The profile is the deliverable.

**Primary risk:** CR2 (relabeling the phenomenological well). The
anti-smuggling test (§8.3) must be passed before any result is accepted.

**The donor base is clean. N7 WP2 may begin.**
