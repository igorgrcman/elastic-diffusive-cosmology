# Canonical Post-N1/N7/N2 Minimal-Class Closure Memo

**Date:** 2026-03-13
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Forensic closure memo — no new derivations
**Governing action class:** S_EH + S_NG (Einstein–Hilbert bulk + Nambu–Goto branes)

---

## 1. Executive Verdict

The minimal action class S_EH + S_NG has been **exhaustively tested for
node-well generation** across all three candidate lanes (N1, N7, N2).
All three returned bounded insufficiency or no-go results. No mechanism
within S_EH + S_NG — thin-junction matching, thick-junction core
physics, or bulk gravitational backreaction — generates an attractive
V_node(q) capable of producing a double-well V(q). The double-well
postulate [P] cannot be promoted to [Dc] within the minimal model class.

This is a **significant negative result**: the neutron-line instanton
program requires physics beyond Nambu–Goto + Einstein–Hilbert to source
the metastable secondary minimum. The result does not falsify EDC — it
constrains the model class in which V(q) must be sought.

---

## 2. Scope Boundary

### What this memo covers
- The three Phase 2 investigations (N1, N7, N2) that tested
  whether S_EH + S_NG generates V_node(q)
- The accumulated dead-end record from Phase 1 (Helfrich, ξ-BC,
  Put C Variants 1–2)
- The consolidated status of V(q) decomposition within the minimal class
- Ranking of remaining non-minimal escape routes

### What this memo does not cover
- New derivations or proposed solutions
- Non-minimal action terms (higher-curvature, Gauss–Bonnet, form fields)
- Derivation of L₀/δ, A, ω₀, or any other neutron-line parameter
- Revision of chapters or epistemic tags (that is a WP-D task)

---

## 3. The Three Minimal-Class Investigations

### 3.1 N1 — Israel Thin-Junction (WP2)

**Appendix:** `app_P2_WP2_Israel_nodewell.tex`
**Check code:** `p2_wp2_israel_nodewell_check.py` (6/6 pass)

**What was tested:** Whether Israel matching conditions at a
thin Y-junction vertex generate q-dependent attractive energy.

**Result: Bounded no-go [Dc].**
1. Deficit angle at the junction node is **identically zero** for all q
   (coplanar arms always partition 2π — geometric identity).
2. Arm-interior Israel energy is **proportional to V_geom(q)** =
   τ L_tot(q); tension renormalization only. Single-well.
3. No other Israel-sector mechanism produces a q-dependent attractive term.

**Scope:** Valid for **all** thin Y-junctions in **any** warped 5D
background with S_EH + S_NG. Geometric, not parameter-dependent.

**What it eliminated:** Thin-junction matching as a source of V_node.

**What it left open:** Thick-junction internal-core physics (finite-width
vertex structure invisible to the distributional matching).

### 3.2 N7 — Thick-Junction / Internal-Core (WP2)

**Appendix:** `app_P2_N7_core_nodewell.tex`
**Check code:** `p2_n7_core_nodewell_check.py` (7/7 pass)

**What was tested:** Whether a regularized junction core at scale δ,
treated via separable density ansatz ρ_core(r_⊥, q) = σ g_⊥(r_⊥/r₀) f(q/δ),
generates an attractive V_core(q).

**Result: Bounded insufficiency [Dc] within the natural model class.**
1. **Energy scale [Dc]:** Core energy E₀ = σ L₀² ~ O(10 MeV) is
   sufficient in magnitude to compete with V_geom.
2. **Monotone profile no-go [Dc]:** If the core profile f is peaked
   at q = 0 and monotonically non-increasing for q > 0 (the physically
   motivated class), then V(q) = V_geom(q) + V_core(q) is single-well.
   No secondary minimum can exist.
3. **Sign result [Dc+I]:** Both binding energy (maximal overlap) and
   strain energy (symmetric stress) favor the Steiner configuration as
   the core energy minimum. The core contribution reinforces V_geom.

**Scope:** Valid for all monotone, separable core profiles within the
S_EH + S_NG action class.

**What it eliminated:** Monotone thick-junction core as a source of
V_node.

**What it left open:** Non-monotone core profiles (e.g., Z₃→Z₂ internal
symmetry transition at critical displacement). This escape route is
physically unmotivated within the current framework and requires
solving internal core dynamics beyond the separable ansatz.

### 3.3 N2 — Bulk Gravitational Backreaction (WP2)

**Appendix:** `app_P2_N2_bulk_backreaction.tex`
**Check code:** `p2_n2_bulk_backreaction_check.py` (7/7 pass)

**What was tested:** Whether bulk metric perturbation sourced by
junction displacement generates q-dependent attraction. Decomposed
into cross-term, LO self-energy, and NLO shape correction.

**Result: Bounded insufficiency [Dc] — structural κ₅²-suppression.**
1. **Cross-term [Dc]:** Interaction of source perturbation with
   background gravitational field is **proportional to V_geom(q)**.
   Tension renormalization only. Structurally identical to N1 result.
2. **LO self-energy [Dc]:** Gravitational self-energy of displaced brane
   is proportional to L_tot(q). Another tension renormalization. No new
   structure.
3. **NLO shape correction [Dc]:** Shape-dependent backreaction is
   competitive with V_geom **only if M₅ ≲ 100 MeV** (for R₅ = πδ).
   For M₅ ≳ 1 GeV, suppression is below 1%. For M₅ ~ M_Pl, suppression
   is ~10⁻⁴⁷.

**Scope:** Valid for linearized 5D gravity with junction-sourced
perturbations. M₅ is undetermined [P] — no branch constrains it.
The threshold M₅ ≲ 100 MeV is far below the electroweak scale.

**What it eliminated:** Bulk backreaction as a viable V_node source
for any physically reasonable M₅.

**What it left open:** The extreme low-M₅ regime (M₅ ≲ 100 MeV),
which has no independent physical motivation within EDC.

---

## 4. Consolidated Minimal-Class Ledger

| # | Candidate | Action Class | Result | Tag | Appendix | Escape Route |
|---|-----------|-------------|--------|-----|----------|-------------|
| **N1** | Israel thin-junction | S_EH + S_NG | Bounded no-go: Δθ ≡ 0, V_Israel ∝ V_geom | [Dc] | app_P2_WP2_Israel | Thick-junction (→ N7) |
| **N7** | Thick-junction core (monotone) | S_EH + S_NG | Bounded insufficiency: monotone profiles → single-well | [Dc] | app_P2_N7_core | Non-monotone profiles [OPEN] |
| **N2** | Bulk backreaction | S_EH + S_NG | Bounded insufficiency: κ₅²-suppressed, threshold M₅ ≲ 100 MeV | [Dc] | app_P2_N2_bulk | Low-M₅ regime [OPEN] |
| **Put C V1** | Flat bulk Nambu–Goto | S_EH + S_NG | V(q) monotonically increasing; no metastability | [Dc] | putC exec report | — |
| **Put C V2** | Warped/RS metric | S_EH + S_NG | 125 parameter combinations; no metastability | [Dc] | putC exec report | — |
| **Helfrich** | Bending rigidity | S_NG + κ_b | 260/260 NO-GO; V_bend ~ +κq²/a² reinforces stretching | [Dc] | helfrich branch | — (falsified) |
| **ξ-BC** | Compact-direction BC | S_EH + S_NG | V'_lin(d) > 0 for all BC types (Neumann, Robin, Dirichlet) | [Der] | frozen-brane branch | — (falsified) |

**Consolidated verdict:** Every mechanism testable within the minimal
S_EH + S_NG action class has been tested. All produce single-well V(q)
or are quantitatively negligible. The double-well requires non-minimal
physics.

---

## 5. What the Minimal Class Has Established

Despite the negative result for double-well generation, the minimal-class
investigations have produced genuine positive knowledge:

1. **V_geom(q) = τ L_tot(q) is the dominant q-dependent energy** [Dc].
   All three investigations found their respective terms proportional to
   or dominated by V_geom. The geometric sector is robust.

2. **The Steiner configuration is the unique energy minimum** [Dc].
   Confirmed independently by V_geom analysis (Phase 1 R3), N1 (Israel),
   N7 (core binding + strain), and N2 (cross-term + LO self-energy).

3. **Tension renormalization is the universal low-order effect** [Dc].
   N1 (arm-interior Israel), N2 (cross-term), and N2 (LO self-energy) all
   reduce to multiplicative corrections to V_geom. The minimal action
   renormalizes the brane tension but does not change the potential shape.

4. **Energy scale for core physics is correct** [Dc].
   N7 established that E₀ = σ L₀² ~ O(10 MeV) can compete with V_geom.
   The problem is not magnitude — it is the sign/shape of the profile.

5. **κ₅²-suppression provides a clean parametric bound** [Dc].
   N2 established that bulk backreaction is quantitatively irrelevant for
   M₅ ≳ 1 GeV. This constrains any future attempt to invoke bulk gravity.

---

## 6. Why the Double-Well Requires Non-Minimal Physics

The logical chain is:

1. V_geom(q) is single-well with minimum at q = 0 (Steiner). [Dc]
2. N1: thin-junction Israel adds no new q-dependent terms. [Dc]
3. N7: thick-junction core (monotone) reinforces the Steiner minimum. [Dc]
4. N2: bulk backreaction is κ₅²-suppressed. [Dc]
5. Helfrich: bending rigidity reinforces stretching. [Dc]
6. ξ-BC: compact-direction BC alone → V' > 0. [Der]
7. Put C V1+V2: minimal flat/warped models → no metastability. [Dc]

**Conclusion:** Within S_EH + S_NG, every accessible mechanism either
reinforces the single-well or is negligible. A secondary minimum at
q_n > 0 requires at least one term not present in the minimal action.

This is not a proof of impossibility (the minimal class may have
unexplored corners), but it exhausts all physically motivated mechanisms
that have been identified across 40+ branches and three dedicated Phase 2
investigations.

---

## 7. Remaining Non-Minimal Escape Routes (Ranked)

These are the identified routes that lie **outside** the minimal S_EH + S_NG
class. Each would require extending the action with additional terms.

| Priority | Route | Required Extension | Physical Motivation | Technical Difficulty | Donor Readiness | Key Risk |
|----------|-------|-------------------|--------------------|--------------------|----------------|----------|
| **1** | Non-monotone core profiles (Z₃→Z₂ transition) | Internal core dynamics beyond separable ansatz | Symmetry transition releasing stress energy at critical q | High — requires solving 5D junction-core equations of motion | Low — no existing computation | Profile might not arise from S_5D |
| **2** | Higher-order brane terms (Gauss–Bonnet, DBI) | S_NG → S_DBI or + S_GB curvature corrections | UV completion of Nambu–Goto; natural in string/M-theory brane actions | Moderate — well-studied in brane literature | Low — no EDC-specific donor | Coefficients are new [I] parameters |
| **3** | Topological contributions (Chern–Simons, winding) | + S_CS or topological sector in S_5D | Topological energy quantization; AR-02/AR-03 in archive | High — poorly constrained within EDC | Marginal — AR-02/AR-03 preserved, not developed | Could be ad hoc if not derived from compactification |
| **4** | Form-field coupling (bulk gauge field on brane) | + S_gauge in S_bulk | Brane charged under bulk form field; common in string compactifications | Moderate — standard formalism | None within EDC | Introduces new sector with unconstrained parameters |
| **5** | Low-M₅ regime (M₅ ≲ 100 MeV) | None (stays within S_EH + S_NG, but requires extreme parameter) | N2 threshold — backreaction becomes competitive | Low — computation already done (N2) | High — N2 appendix | M₅ ~ 100 MeV is far below electroweak; physically questionable |

---

## 8. Assessment of Each Escape Route

### 8.1 Priority 1: Non-Monotone Core Profiles

**What it is:** The N7 no-go applies to monotone profiles f(q/δ) peaked
at q = 0. If the core energy has a qualitative change at some critical
displacement — e.g., a Z₃ → Z₂ symmetry transition inside the core
that releases stress energy — the profile could be non-monotone, and
the no-go would not apply.

**Why Priority 1:** It is the most direct escape from the strongest
no-go (N7). It stays closest to the existing framework. The energy
scale is already correct (E₀ ~ 10 MeV). Only the profile shape needs
to change.

**Blockers:** No physical mechanism for a non-monotone profile has
been identified. The N7 appendix notes that "a non-monotone profile
would require a mechanism that makes the core energy decrease with
increasing asymmetry, which has no obvious elastic-medium analogue."
This is physically unmotivated unless a specific internal dynamics
model is provided.

**Required work:** Solve the internal core equations of motion for the
regularized junction vertex. Determine whether stress redistribution
at the vertex can produce non-monotone V_core(q). This goes beyond
the separable ansatz and requires a genuine 5D computation.

### 8.2 Priority 2: Higher-Order Brane Terms

**What it is:** Replace the Nambu–Goto action (lowest-order in
derivatives) with DBI or add Gauss–Bonnet curvature corrections.
These contribute q-dependent energy terms not present in S_NG.

**Why Priority 2:** These are the standard UV corrections to brane
actions in string/M-theory. They are physically well-motivated as
the next terms in a derivative expansion. They could modify V(q)
at the scale δ where higher-derivative terms become important.

**Blockers:** The coefficients (DBI parameter, Gauss–Bonnet coupling)
are new input parameters [I]. Without an independent constraint on
these coefficients, any double-well produced is [Dc|model, parameter-
dependent]. The Helfrich bending no-go (which is structurally related
to quadratic curvature corrections) provides a cautionary precedent.

**Required work:** Compute V_DBI(q) or V_GB(q) for the displaced
Y-junction. Check sign and magnitude. Compare to V_geom.

### 8.3 Priority 3: Topological Contributions

**What it is:** Energy terms from topological invariants (Chern–Simons
forms, winding numbers) that are q-dependent. Archive items AR-02
(F = ∫ω₃ (mod 3)) and AR-03 (Λ pinning / self-adjointness +
topological quantization) are preserved references in this direction.

**Why Priority 3:** Topological contributions are already part of the
EDC framework (κ = 2π is a topological derivation). A q-dependent
topological term could provide a sharp, discrete contribution
(quantized) rather than a smooth correction — potentially avoiding the
continuous tuning issues that plague other routes.

**Blockers:** No concrete computation exists. The archive items
(AR-02, AR-03) are conceptual only. Connection to V(q) is unclear.

### 8.4 Priority 4: Form-Field Coupling

**What it is:** A bulk gauge field or form field to which the brane is
charged. The brane–field coupling provides an additional contribution
to V(q) when the junction displaces.

**Why Priority 4:** Standard in string compactifications but introduces
an entirely new sector with unconstrained parameters. Furthest from the
existing EDC framework.

### 8.5 Priority 5: Low-M₅ Regime

**What it is:** The N2 analysis already showed that bulk backreaction
becomes competitive for M₅ ≲ 100 MeV. This is not a new mechanism —
it is the N2 mechanism in an extreme parameter regime.

**Why Priority 5 (lowest):** M₅ ~ 100 MeV is far below the electroweak
scale. No physical motivation exists within EDC for such a low 5D Planck
mass. Invoking it would be parameter tuning [Cal], not a derivation.

---

## 9. Recommended Next Active Entry Point

**Recommendation: Priority 1 — Non-monotone core profiles.**

**Rationale:**

1. **Most direct.** It addresses the specific escape route identified by
   the strongest investigation (N7). The energy scale is already correct.
   Only the profile shape needs to change.

2. **Minimal action extension.** Unlike Priorities 2–4, it does not
   require adding new terms to the action. It requires solving the
   existing action's equations of motion at the junction core — which
   should have been done anyway.

3. **Decisive.** If the internal core dynamics produce a non-monotone
   profile → the double-well may exist within S_EH + S_NG after all
   (the N7 monotone no-go is circumvented, not violated). If they
   confirm monotone behavior → the minimal class is genuinely exhausted,
   and the search must move to Priorities 2–3.

4. **Builds on existing infrastructure.** The N7 separable ansatz
   framework, E₀ scaling, and V_geom baseline are all reusable. The
   computation extends N7 rather than starting from zero.

**Concrete entry point:** Solve the regularized junction-core equations
of motion (stress–energy balance at the Y-junction vertex with finite
width δ) and determine whether the equilibrium core energy profile
V_core(q) is monotone or non-monotone. This requires going beyond the
separable ansatz to a genuine 5D variational calculation at the vertex.

**Fallback:** If non-monotone profiles are ruled out or confirmed to be
insufficient, proceed to Priority 2 (higher-order brane terms).

---

## 10. Anti-Regression Rules

These rules prevent the re-testing or revival of closed lanes.

| Rule | Statement | Violation Trigger |
|------|-----------|-------------------|
| **ARR-1** | N1 (Israel thin-junction) is a preserved dead-end. Do not re-attempt thin-junction matching as a V_node source without new physics (e.g., higher-curvature terms, additional branes). | Any proposal to "try Israel conditions again" within S_EH + S_NG. |
| **ARR-2** | N7 (monotone thick-junction) is closed. Do not re-test monotone, separable core profiles. The no-go is proven: monotone f(q/δ) → single-well V(q). | Any proposal to "try a different monotone core profile." |
| **ARR-3** | N2 (bulk backreaction) is structurally κ₅²-suppressed. Do not invoke bulk gravity as a V_node source without specifying M₅ < 100 MeV and justifying that value. | Any proposal to use backreaction at unspecified M₅. |
| **ARR-4** | Helfrich bending is falsified (260/260). Do not re-test bending rigidity with c₀ = 0. | Any proposal involving κ_b q²/a² term. |
| **ARR-5** | ξ-BC alone cannot create a barrier. Do not invoke compact-direction boundary conditions as a standalone V_node mechanism. | Any proposal for "BC-driven well." |
| **ARR-6** | Put C Variants 1–2 produced no metastability. Do not re-scan flat/RS backgrounds within S_EH + S_NG without new terms. | Any proposal to "try more warped metrics" within the same action. |
| **ARR-7** | C = 100 is circular. Do not cite C = (L₀/δ)² = 100 as independent evidence for L₀/δ. The structural scaling C ∝ (L₀/δ)² is [Dc]; the numerical value uses [I] inputs. | Any proposal using C = 100 to constrain L₀/δ. |
| **ARR-8** | The phenomenological Gaussian well (Put C Variant 3, N6) is forbidden as [Dc]. Do not relabel a fitted profile as a derived core model. | Any core profile whose parameters are chosen to reproduce V_B ≈ 2Δm_np. |

---

## 11. What Remains True Despite the Negative Result

The minimal-class closure does not invalidate the following:

1. **κ = 2π is genuinely derived [Dc]** from π₁(S¹) = ℤ. Topological.
   Independent of V(q).

2. **V_geom(q) = τ L_tot(q) is genuinely derived [Dc].** The geometric
   sector stands regardless of whether V_node exists.

3. **The instanton formula Γ = A(ω₀/2π)exp(−S_E/ℏ) is correct [Der].**
   The formula is valid given a double-well potential. The question is
   whether the double-well exists, not whether the formula is right.

4. **N_bonds = 3 local optimality is derived [Dc] within its model.**
   Independent of V(q).

5. **L₀/δ = F(η) functional relation is derived [Dc|model].** Independent
   of V(q) (it concerns V(ξ), the compact-direction potential, not V(q)).

6. **The τ_n ≈ 880 s assembly is architecturally coherent.** The chain
   σ → K_pin → V_B → S_E/ℏ → τ_n is logically valid. Its weakest link
   is V_B [P], which depends on the double-well that the minimal class
   cannot source.

---

## 12. Impact on the Neutron-Line Epistemic Ledger

The minimal-class closure affects the following ledger rows
(from `BOOK4_NEUTRONLINE_FINAL_STATUS_AFTER_PHASE1.md` §7):

| Row | Claim | Tag Before | Impact of Minimal-Class Closure | Tag After |
|-----|-------|-----------|--------------------------------|-----------|
| 3 | Full V(q) double-well | [P] | Cannot be promoted within S_EH + S_NG. Requires non-minimal physics. | [P] — unchanged, but now with stronger negative evidence |
| 4 | Secondary minimum at q_n | [P] | Not confirmed by any minimal-class investigation. | [P] — unchanged |
| 5 | V_B = 2Δm_np | [P] | Cannot be derived from minimal action. | [P] — unchanged |
| 6 | M(q) effective mass | [P] | Not derived. | [P] — unchanged |
| 15 | τ_n ≈ 880 s | [Dc]+[P]+[Cal] | The [P] component (V(q) double-well) is now known to be non-derivable within the minimal class. | [Dc]+[P]+[Cal] — unchanged, but [P] is now known to require non-minimal physics |

**Net effect on ledger:** No tag changes. The closure constrains
**where** the [P] tags can be resolved (not within S_EH + S_NG) but
does not change their current status.

---

## 13. Relationship to Archive Items

Three marginal archive items (from `ARCHIVE_REDISCOVERY_TRACKER.md`)
are relevant to the non-minimal escape routes:

| Archive Item | Connection | Status Change |
|-------------|-----------|---------------|
| **AR-02** (Chern–Simons / F = ∫ω₃ (mod 3)) | Directly relevant to Priority 3 (topological contributions). | **No change.** Remains preserved reference. Would need explicit reclassification and audit before activation. |
| **AR-03** (Λ pinning / P36 self-adjointness + topological quantization) | Potentially relevant to Priority 3. | **No change.** Remains preserved reference. |
| **AR-01** (5D analytic failure certificate) | Not relevant to any current escape route. | **No change.** |

The archive rediscovery tracker's canonical rule applies: archive items
may only re-enter active research through an explicit dedicated audit
that classifies the item, checks it against current branch content, and
assigns an epistemic tag.

---

## 14. What This Memo Prevents

1. **Re-mining the minimal action class.** All physically motivated
   mechanisms within S_EH + S_NG have been tested. New attempts within
   this class must specify which mechanism they test and how it differs
   from N1/N7/N2/Helfrich/ξ-BC/Put C V1–V2.

2. **Circular re-derivation.** ARR-1 through ARR-8 prevent revival of
   closed lanes without new physics.

3. **Scope creep.** The recommended next entry point (Priority 1:
   non-monotone core profiles) is bounded and specific. It does not
   authorize a general exploration of non-minimal actions.

4. **Premature falsification claims.** The minimal-class closure is a
   constraint, not a falsification of EDC. The double-well could exist
   in a non-minimal extension. The correct framing is "the minimal class
   is insufficient" not "the double-well is falsified."

5. **Importing negative results as positive evidence.** The bounded
   insufficiency of N7 and N2 does not confirm that V_node is zero — it
   confirms that V_node is not sourced by the tested mechanisms. The
   distinction matters.

---

## 15. Bottom Line

Three Phase 2 investigations (N1, N7, N2) have exhausted the minimal
S_EH + S_NG action class as a source of the V_node(q) needed for the
double-well potential. Combined with Phase 1 dead ends (Helfrich, ξ-BC,
Put C V1–V2), seven independent tests confirm: **the minimal 5D action
does not generate metastability.**

The double-well postulate [P] remains architecturally sound but requires
non-minimal physics. Five escape routes are ranked (§7–8), with
**non-monotone core profiles** (solving the internal core dynamics
beyond the separable ansatz) recommended as the single next active entry
point. This route stays closest to the existing framework, builds on N7
infrastructure, and is decisive: it either circumvents the monotone
no-go or closes the last minimal-class corner.

If non-monotone profiles also fail, the search moves to genuinely
non-minimal action extensions (higher-order brane terms, topological
contributions). Eight anti-regression rules (ARR-1 through ARR-8)
prevent re-testing of closed lanes.

The neutron-line assembly τ_n ≈ 880 s remains intact as an [Dc]+[P]+[Cal]
result. The minimal-class closure does not weaken it — it clarifies that
the [P] component (double-well V(q)) cannot be resolved within
S_EH + S_NG and must be sought elsewhere.
