# Book IV — Neutron-Line Final Forensic Status After Phase 1

**Date:** 2026-03-13
**Branch:** `research/topological-pinning-v7_8-integration`
**Auditor:** Forensic post-Phase-1 review
**Type:** Cold audit — no new derivations, no Phase 2 implementation

---

## 1. Executive Verdict

The Book IV neutron line is **partially closed**. Phase 1 converted three
previously open routes (R4, R3, R1) into scoped partial closures, each
delivering a conditional result within a declared effective model. The
headline number τ_n ≈ 880 s is now **assembled** from a five-link chain
(σ → K_pin → V_B → S_E/ℏ → τ_n) in which two links remain postulated [P]
(L₀/δ = π², V(q) double-well structure) and one is calibrated [Cal]
(prefactor A ≈ 0.9). One topological link (κ = 2π) is genuinely derived
[Dc]. The integration pass removed overclaiming language but did not — and
could not — elevate any [P] or [Cal] tag. The neutron line is epistemically
honest and architecturally coherent, but the <1% agreement with observation
is contingent, not independently confirmed. The strongest single blocker
for further closure is the absence of a physical V(ξ) from the 5D action.

---

## 2. Scope of Audit

### 2.1 Files Inspected

| File | Role |
|------|------|
| `main.tex` | Master document, preface, book structure |
| `chapters/ch03_neutron_metastable.tex` | Double-well, barrier height, V_B conjecture |
| `chapters/ch06_instanton.tex` | Euclidean action, decay rate formula |
| `chapters/ch08_L0_delta_ratio.tex` | L₀/δ hypothesis, heuristic approaches |
| `chapters/ch09_tau_n_prediction.tex` | τ_n assembly, anti-tuning firewall, sensitivity |
| `appendices/app_Nbonds_local_optimality.tex` | R4: N_bonds = 3 local optimality |
| `appendices/app_Vq_chosen_path.tex` | R3: V_geom along chosen path |
| `appendices/app_L0delta_model_bvp.tex` | R1: model-dependent BVP route |
| `code/r1_L0delta_verify.py` | R1: numerical verification code |
| `PHASE1_PLAN_REVISED.md` | Phase 1 plan (v3.1) |
| `audit/PHASE1_INTEGRATION_STATUS.md` | Phase 1 integration pass summary |
| `audit/R1_GLOBAL_DISCOVERY.md` | Global forensic inventory of R1 content |
| `audit/R1_PREFLIGHT_AUDIT.md` | R1 preflight assessment |

### 2.2 Scope Limitation

This is a forensic audit of accepted Phase 1 materials. No new
derivations, chapter rewrites, or Phase 2 implementation are performed.
Tiny wording corrections are permitted only if they materially affect
status accuracy; none were needed.

---

## 3. Phase 1 Outcome Summary

| Route | Intended Goal | Actual Achieved Outcome | Final Status |
|-------|--------------|------------------------|--------------|
| **R4** | Derive N_bonds = 3 from EDC principles | Local optimality within pairwise-additive pinning model. Three lemmas proved (upper bound, saturation, uniqueness). Five postulated assumptions declared. | **[Dc] within model** — retained with scope qualifier |
| **R3** | Derive V(q) from 5D action | Geometric sector V_geom(q) computed along two chosen paths. Single-well with Steiner minimum. No secondary minimum from geometry alone. Full double-well requires non-geometric terms (V_node, V_bulk). | **Partial** — V_geom = [Dc]; full V(q) = [P]; secondary minimum = [P] |
| **R1** | Derive L₀/δ from BVP / localization | Model-dependent square-well eigenvalue route yields L₀/δ = F(η) as continuous family. π² reproduced at η ≈ 0.052 but not uniquely selected. Semiclassical A formula recovered [Der within 1D model]. δ-scale ambiguity documented. | **Partial** — F(η) = [Dc\|model]; η = [P]; π² = [P]; δ identification = [P] |
| **Integration** | Remove overclaiming; harmonize epistemic tags | Preface softened ("assembles" not "derives"). Ch.03/06/09 overclaiming passages corrected. "Derivation chain complete" → "partially closed". | **Done** — no residual overclaiming detected |

---

## 4. What Is Now Closed

The following results are retained as genuinely closed within their declared scope:

| Claim | Tag | Scope | Evidence |
|-------|-----|-------|----------|
| **κ = 2π** | [Dc] | From π₁(S¹) = ℤ; topological, not model-dependent | Ch.07 homotopy derivation |
| **V_geom(q) = τ × L_tot(q)** | [Dc] | Geometric brane-energy along chosen displacement paths (in-brane and compact-direction) | App. B, Theorem (Steiner minimum) |
| **V_geom is a single well** | [Dc] | No secondary minimum from Nambu-Goto arm-length alone; Steiner point is unique minimum | App. B §4–5 |
| **V_geom''(0) = 3τ/(2R) > 0** | [Dc] | Curvature at Steiner minimum; restoring force confirmed | App. B, Theorem |
| **E_B = 3 × E_arm** (factor-of-3 at barrier) | [Der] | From Z₃ symmetry + energy additivity at barrier saddle | Ch.03, Step 1 |
| **N_bonds = 3** (local optimality) | [Dc] | Within pairwise-additive pinning model with 5 declared [P] assumptions | App. A, Theorem + 3 lemmas |
| **B_d = 3 K_pin** (corollary) | [Dc] | Direct consequence of N_bonds = 3 within same model | App. A, Corollary |
| **L₀/δ = F(η) functional relation** | [Dc\|model] | Square-well eigenvalue model; transcendental equation solved; monotonically decreasing | App. C, §4–5 |
| **A_sc = π(ω₀/ω_B)/√(L₀/δ)** | [Der] | Within 1D semiclassical effective model | App. C §7; donor: commit e7f298f |
| **Γ = A(ω₀/2π) exp(−S_E/ℏ)** | [Der] | Standard instanton tunneling formula | Ch.06, Eq. (6.12) |
| **Conditional barrier existence** | [Dc] | If double-well exists, continuity guarantees barrier; V_geom provides lower bound on cost | App. B §5 |

**Note:** "Closed" here means the result follows logically from stated premises within its declared scope. It does not mean "derived from S_EDC without model assumptions."

---

## 5. What Is Only Partially Closed

| Claim | Tag | What is achieved | What remains conditional |
|-------|-----|-----------------|------------------------|
| **V(q) double-well structure** | [P] | Geometric sector [Dc] confirms single-well restoring force. Observational absence of doublet partners [BL]+[M] supports Z₃-symmetric metastable. | Non-geometric terms (V_node, V_bulk) not derived. Put C steps C2–C4 open. Double-well is postulated, not computed. |
| **V_B = 2 Δm_np** | [P] | Factor-of-2 follows from Z₃ [Der] + single-mode assignment [P]. Calibration V_B^cal ≈ 2.6 MeV matches 2 × 1.293 MeV to <1%. | E_arm ≡ Δm_np identification is projection-level [OPEN]. Numerical agreement is [Check], not derivation evidence. |
| **L₀/δ = π²** | [P] | Reproduced at η ≈ 0.052 in eigenvalue model. Three heuristic motivations (standing wave, two-fold winding, Steiner). | One candidate among continuous family F(η). η not derived from 5D. Closest τ_n match at L₀/δ ≈ 9.33, not π². δ identification ambiguous by factor ~50. |
| **τ_n ≈ 880 s** | [Dc]+[P]+[Cal] | Assembly chain from instanton formula + κ + L₀/δ + A. Exponent dominance confirmed (~27 orders of magnitude from exp(62)). Sensitivity analysis complete. | Depends on L₀/δ = π² [P] and A ≈ 0.9 [Cal]. With A_sc ≈ 0.84 [Der] and π², get τ_n ≈ 24,000 s — factor ~27 off. <1% agreement requires calibrated A. |
| **S_E/ℏ = κ × (L₀/δ)** | [P] | Parametric form [Dc]; value 2π³ ≈ 62 conditional on L₀/δ = π² [P]. | The factorization S_E/ℏ = κ(L₀/δ) is postulated [P] from the EDC instanton ansatz. Not yet verified as the correct dimensional reduction of S_5D. |
| **ω₀ = √(σ/m_p) ≈ 19 MeV** | [P] | Dimensional estimate from brane parameters. | Numerical coefficient undetermined. Not derived from V''(q_n) of the actual potential. |
| **M(q) effective mass** | [P] | Scaling M ~ τR/c². Constant-mass approximation. | Numerical coefficient unknown. q-dependence assumed trivial. No computation from 5D action exists. |

---

## 6. What Remains Open

Ranked by impact on neutron-line closure (highest impact first):

### Rank 1: Physical V(ξ) from 5D Action

The localization potential V(ξ) — the potential that confines the junction
wavefunction in the compact fifth dimension — is not derived from the 5D
action (bulk + brane + GHY + Israel). The R1 appendix uses a square-well
ansatz [P]. All subsequent eigenvalue results (L₀/δ = F(η), η values)
inherit this model dependence. Deriving V(ξ) would simultaneously:
- determine η from first principles → select unique L₀/δ
- resolve the δ-scale ambiguity
- ground the entire instanton exponent

**Impact:** Blocks promotion of L₀/δ from [P] to [Der]. Blocks exponent closure.

### Rank 2: Full V(q) Including Non-Geometric Terms

The effective potential V(q) along the tunneling path has only its
geometric sector V_geom(q) computed [Dc]. The non-geometric terms (junction
node energy V_node, bulk gravitational V_bulk) that would create a
secondary minimum and complete the double-well are not derived. This is the
Put C corridor (steps C2–C4).

**Impact:** Blocks confirmation of double-well existence. Blocks V_B derivation.
Blocks M(q) derivation. Blocks ω₀ derivation.

### Rank 3: Well Strength η from First Principles

The dimensionless parameter η = MV₀δ²/(2ℏ²) contains two undetermined
quantities: well depth V₀ [P] and effective mass M [P]. The entire
L₀/δ = F(η) curve is computed [Dc|model], but without η the curve does
not select a unique point.

**Impact:** Directly blocks unique L₀/δ determination within the eigenvalue model.

### Rank 4: E_arm ≡ Δm_np Identification

The factor-of-3 at the barrier is [Der] from Z₃ symmetry, but the
identification E_arm = Δm_np (mapping the per-arm deformation cost to the
observer-frame mass difference) is a projection-level assumption [OPEN].
Without it, V_B = 2 Δm_np remains [P].

**Impact:** Blocks barrier-height closure.

### Rank 5: Prefactor A from Full 5D Determinant

The semiclassical formula A_sc = π(ω₀/ω_B)/√(L₀/δ) is [Der within 1D
model]. But it gives A ≈ 0.84, which with π² produces τ_n ≈ 24,000 s.
The <1% agreement requires A ≈ 0.9 [Cal]. A full fluctuation determinant
from the 5D path integral would determine A without calibration.

**Impact:** Blocks removal of [Cal] dependence. Partially entangled with L₀/δ (co-tuning risk).

### Rank 6: Compactification Radius R₅

No branch in the entire 40-branch repo derives R₅ independently. All
heuristic routes (standing wave, two-fold winding) assume R₅ = πδ [P].
The eigenvalue model bypasses R₅ via η, but physically R₅ determines
the compact geometry.

**Impact:** Not directly blocking if η can be derived independently, but
needed for full geometric consistency.

### Rank 7: ω₀ from Junction Dynamics

Currently a dimensional estimate [P]. Requires V''(q_n) from the full
potential and M(q) from 5D kinetic term reduction.

**Impact:** Moderate. Enters prefactor (linear, not exponential).

---

## 7. Neutron-Line Epistemic Ledger

| # | Claim | Current Tag | Scope | Key Dependency | Primary Blocker |
|---|-------|-------------|-------|----------------|-----------------|
| 1 | N_bonds = 3 | [Dc] | Local pairwise-additive model | 5 [P] assumptions (additivity, locality, no frustration, no multi-arm coupling, contact saturation) | H_pin from S_EDC |
| 2 | V_geom(q) single-well | [Dc] | Chosen displacement paths | Path choice [Dc]; Steiner optimality [Der] | None within scope |
| 3 | Full V(q) double-well | [P] | Postulated structure | V_node + V_bulk not derived | Put C (C2–C4) |
| 4 | Secondary minimum at q_n | [P] | Observational support [BL]+[M] | No Hessian computation | Put C |
| 5 | V_B = 2 Δm_np | [P] | Z₃ factor [Der] × unit identification [OPEN] | E_arm ≡ Δm_np | V(q) from 5D |
| 6 | M(q) effective mass | [P] | Scaling estimate only | τR/c² dimensional; coefficient unknown; q-indep. assumed | 5D kinetic reduction |
| 7 | κ = 2π | [Dc] | From π₁(S¹) = ℤ | Topological invariant | None |
| 8 | L₀/δ = F(η) | [Dc\|model] | Square-well eigenvalue model | η [P]; V(ξ) ansatz [P] | Physical V(ξ) |
| 9 | L₀/δ = π² | [P] | Candidate in continuous family | η ≈ 0.052; not naturally selected | η from 5D; V(ξ) from 5D |
| 10 | R₅ | [P] | Never derived on any branch | All routes assume R₅ = πδ [P] | Independent 5D constraint |
| 11 | δ identification | [P] | δ ≈ 0.105 fm [I] vs R_ξ ≈ 0.002 fm | ×50 ambiguity unresolved | Scale reconciliation |
| 12 | A ≈ 0.9 | [Cal] | Calibrated prefactor | A_sc ≈ 0.84 [Der in 1D] gives τ_n ≈ 24k s with π² | Full fluctuation det. |
| 13 | ω₀ ≈ 19 MeV | [P] | Dimensional estimate | V''(q_n) + M(q) needed | V(q) + M(q) |
| 14 | S_E/ℏ = 2π³ ≈ 62 | [Dc]×[P] | Product of [Dc] κ and [P] L₀/δ | Inherits [P] from L₀/δ | L₀/δ closure |
| 15 | τ_n ≈ 880 s | [Dc]+[P]+[Cal] | Assembled from #7, #9, #12, #13 | Contingent on [P] and [Cal] | L₀/δ + A closure |

---

## 8. Circularity and Calibration Risks

This section is mandatory. The following circularity and calibration
vulnerabilities survive Phase 1.

### 8.1 Post-Hoc R₅ Choice

All three heuristic routes to L₀/δ = π² assume R₅ = πδ, which is chosen
specifically because it yields the desired π² value. No independent
constraint on R₅ exists anywhere in the repo (confirmed across 40
branches). If R₅ were derived to be, say, 2δ or 5δ, the standing-wave
argument gives L₀/δ = 2π or 5π — neither of which is π². The R₅ = πδ
assumption is unfalsifiable within the current framework because R₅ is
never independently determined.

**Severity:** High. The exponent depends on R₅ via L₀/δ.

### 8.2 Prefactor Rescue via A

With the semiclassical A_sc ≈ 0.84 and L₀/δ = π², the predicted
τ_n ≈ 24,000 s — a factor ~27 too long. The <1% agreement requires
A ≈ 0.03 (if using π²) or choosing L₀/δ ≈ 9.33 with A ≈ 0.9. In
practice, A is calibrated to absorb the discrepancy between the
exponent and observation. This creates a co-tuning risk: A and L₀/δ are
not independently constrained, so any exponent can be "corrected" by
adjusting A.

**Severity:** High. Until both A and L₀/δ are independently derived,
<1% agreement is not an independent prediction.

**Clarification:** The anti-tuning firewall in Ch.09 correctly states
that the exponent dominates in log-space. This is true — but the
factor-27 discrepancy between A_sc × exp(S_E) and observation is
precisely what the calibration absorbs.

### 8.3 C = (L₀/δ)² = 100 Circularity

Found on `junction-core-derive-C-v1`: C is derived [Dc] structurally as
C ∝ (L₀/δ)², which is legitimate dimensional analysis. But the *value*
C = 100 uses L₀ = 1.0 fm [I] and δ = 0.1 fm [I] as inputs — confirming
dimensional analysis, not deriving L₀/δ. The π factor from the profile
integral I_⊥ is dropped by ad hoc normalization. If retained, C = 314.
This route cannot independently constrain L₀/δ.

**Severity:** Low (already documented and not imported as evidence).
Risk is only if future work silently cites C = 100 as independent support.

### 8.4 Tension "Resolution" Depends on r_p [BL]

The claimed resolution between "static" π² and "dynamic" 9.33 uses the
measured proton charge radius r_p = 0.875 fm [BL] as input:
L₀ = r_p + δ = 0.875 + 0.105 = 0.980 fm → L₀/δ = 9.33. This is a
brane-to-observer map using empirical data, not a derived result. The
"quantum corrections" framing disguises calibration as physics.

**Severity:** Medium. The two-context comparison is legitimate as a
consistency check [Check], but must not be cited as resolving the
L₀/δ question.

### 8.5 τ_n as Pseudo-Anchor

The entire derivation chain targets τ_n ≈ 878 s [BL] as the observable
to match. While τ_n is correctly labeled [BL] (measurement input, not
derivation target), the chain is implicitly calibrated backward from this
value: A is adjusted to match τ_n given the chosen exponent. A truly
independent prediction would compute τ_n from parameters that are
themselves independently constrained — which is not the case for L₀/δ
or A.

**Severity:** Medium-high. Not a logical circularity (the framework
legitimately predicts a functional form for τ_n), but the numerical
agreement is calibration-assisted, not calibration-free.

---

## 9. Dead Ends / No-Go Results Preserved

These are documented failures that must be preserved to prevent
re-derivation of falsified routes. Each is archived in the repo.

### 9.1 Helfrich Bending Route — FALSIFIED

**Branch:** `helfrich-well-from-action-v1`
**Result:** 260/260 configurations tested, zero metastable wells found.
V_bend ~ +κq²/a² (positive quadratic) reinforces Nambu-Goto stretching;
cannot create a well with vanishing spontaneous curvature c₀ = 0.
**Why useful:** Eliminates bending rigidity as a source of metastability.
Constrains the search for the secondary-minimum mechanism to non-geometric
(V_node, V_bulk) terms.

### 9.2 ξ-Boundary Conditions Alone — FALSIFIED

**Branch:** `frozen-brane-bc-v1`
**Result:** V'_lin(d) > 0 for ALL boundary condition types (Neumann,
Robin, Dirichlet). Seven markdown files documenting the result.
**Why useful:** Eliminates compact-direction boundary conditions as a
standalone source of the localizing potential. The minimum must come from
radial-frozen core topology, not ξ-direction BC alone.

### 9.3 δ ≡ R_ξ Closure — ALL ROUTES BLOCKED

**Branch:** `book2-opr04-delta-equals-Rxi-v1`
**Result:** Three routes attempted (Diffusion→BL theorem, Junction→Robin→δ,
S¹ geometry); all OPEN or BLOCKED.
**Why useful:** Documents the δ-scale ambiguity as a genuine unresolved gap,
not a trivial identification. The factor-50 spread between R_ξ ≈ 0.002 fm
and δ ≈ 0.105 fm is real and unexplained.

### 9.4 Flux Quantization for L₀/δ — DEAD END

**Location:** DERIVE_L0_DELTA_PI_SQUARED.md (v1, Routes 3a–3c)
**Result:** Three flux quantization attempts; none produced L₀/δ.
**Why useful:** Eliminates flux quantization as a viable route to the
geometric ratio. Narrows the derivation options.

### 9.5 OPR-20 Factor-8 (Six Attempts) — NO CLOSURE

**Branches:** Six `part2-gf-opr20-*` branches (attempts A–F)
**Result:** None achieved full factor-8 suppression from first principles.
Attempt D found overcounting. Attempt F found "broad region" (47.6% of
parameter space) but Robin α not derived.
**Why useful:** Not directly R1, but illustrates the difficulty of
parameter derivation in the 5D framework. Provides calibrated baselines.

### 9.6 Minimal 5D Models for V(q) — INSUFFICIENT

**Branch:** `putC-computation-v1`
**Result:** Variant 1 (flat bulk): no metastability. Variant 2 (warped/RS):
no metastability. Variant 3 (warped + phenomenological node well):
metastable, but only with [P/Cal] node well.
**Why useful:** Demonstrates that V_B = 2 Δm_np does NOT emerge from
minimal 5D models. The secondary minimum requires physics beyond
Nambu-Goto + bulk gravity in simple warped backgrounds.

---

## 10. Net Effect of Phase 1

### Did Phase 1 strengthen the neutron line?

**Yes, structurally.** The three appendices (N_bonds, V_geom, L₀/δ BVP)
replaced hand-waving with scoped mathematical results. Each declares its
model assumptions and scope limits explicitly. The epistemic tagging is
now internally consistent across chapters and appendices.

### Did Phase 1 weaken the neutron line?

**Yes, rhetorically.** The pre-Phase-1 text presented τ_n ≈ 880 s as
a near-derivation. Phase 1 revealed and documented that:
- L₀/δ = π² is one candidate in a continuous family, not naturally selected
- A_sc with π² gives τ_n ≈ 24,000 s, not 880 s
- <1% agreement requires calibrated A
- δ itself is ambiguous by factor ~50

These were always true, but Phase 1 made them explicit.

### Did Phase 1 clarify the neutron line?

**Yes, substantially.** The epistemic map is now precise. Every link in the
chain has a declared tag, scope, and blocker. The dead ends are
documented. The circularity risks are flagged. A reader can now assess
exactly what is derived, what is postulated, and what is calibrated.

### Did Phase 1 partially falsify prior stronger rhetoric?

**Yes.** The following claims from pre-Phase-1 text were corrections:
- "This book derives... τ_n = 880 s" → "assembles" (not derives)
- "Derivation chain complete" → "partially closed"
- "emerges from topology and geometry, not from fitted parameters" →
  replaced with honest epistemic accounting
- "The metastable sector is now complete" → "partially closed"

These were not falsifications of the physics, but corrections to
overclaiming rhetoric that conflated assembly with derivation.

### Summary assessment

Phase 1 **clarified and structurally strengthened** the neutron line while
**honestly reducing** the apparent strength of the τ_n prediction. The
net effect is positive: the framework is now more trustworthy precisely
because it no longer overclaims. The τ_n result is properly framed as a
partially closed assembly, not a first-principles derivation.

---

## 11. Phase 2 Candidate Targets (Ranked)

### Rank 1: Full V(q) from 5D Action (Put C Corridor)

**Why it matters:** The double-well structure is the architectural
foundation of the entire instanton program. Currently [P]. Deriving V(q)
from S_5D (bulk + brane + GHY + Israel) would simultaneously:
- Confirm or deny the secondary minimum
- Determine V_B from first principles
- Provide M(q) as a byproduct
- Enable ω₀ = √(V''(q_n)/M) computation
- Ground the E_arm ≡ Δm_np identification

**What it would unlock:** Promotion of V(q) from [P] to [Dc] or [Der].
Resolution of 4+ open items in the ledger (rows 3, 4, 5, 6, 13).

**Why it comes first:** It has the highest multiplier — one derivation
resolves the most downstream dependencies. Every other open item
(L₀/δ, A, ω₀) requires V(q) as prerequisite or co-input.

**Difficulty:** High. Put C steps C2–C4 involve non-trivial 5D
variational calculus with junction boundary conditions. Prior attempts
(putC-computation-v1) showed minimal models are insufficient.

### Rank 2: Physical V(ξ) Localization Potential from 5D

**Why it matters:** The R1 appendix uses a square-well ansatz [P].
Deriving V(ξ) from the 5D action would determine η from first
principles, uniquely selecting L₀/δ on the F(η) curve. This would:
- Close the L₀/δ question
- Resolve the δ-scale ambiguity (physical V(ξ) would reveal which
  thickness scale is relevant)
- Fix the instanton exponent S_E/ℏ

**What it would unlock:** Promotion of L₀/δ from [P] to [Der].
Exponent closure. Massive reduction in calibration dependence.

**Why it comes second:** Closely related to Rank 1 (both require 5D
variational analysis), but more narrowly scoped. Could be pursued in
parallel if resources allow. Rank 2 because V(ξ) without V(q) leaves
the double-well question open.

### Rank 3: Independent R₅ Constraint

**Why it matters:** R₅ is never derived anywhere in the 40-branch repo.
All heuristic L₀/δ routes assume R₅ = πδ. An independent constraint
on R₅ from compactification physics (flux quantization, anomaly
cancellation, or moduli stabilization) would either confirm or exclude
the π² hypothesis.

**What it would unlock:** If R₅ = πδ is confirmed: promotes the standing
wave argument from [P] to [Dc]. If R₅ ≠ πδ: falsifies the π²
hypothesis cleanly.

**Why it comes third:** Important for falsifiability but does not by
itself close the double-well or V(ξ) questions. Could yield a quick win
if a constraint is found.

### Rank 4: Prefactor A from Full Fluctuation Determinant

**Why it matters:** Currently [Cal]. The semiclassical formula
A_sc ≈ 0.84 [Der within 1D model] is a partial result. A full
5D fluctuation determinant calculation would determine A without
calibration, removing the [Cal] tag.

**What it would unlock:** Removal of [Cal] from τ_n. Combined with
L₀/δ closure (Rank 2), would promote τ_n to [Der].

**Why it comes fourth:** Requires the bounce solution, which requires
V(q), which is Rank 1. Cannot be completed before Ranks 1–2 unless
using the 1D model (already done — gives A_sc ≈ 0.84, insufficient
for <1% match).

### Rank 5: M(q) Inertia Tensor from 5D Kinetic Reduction

**Why it matters:** Currently [P] (scaling only). M(q) enters the
instanton calculation through the effective action and the prefactor.
q-dependence of M modifies the bounce solution.

**What it would unlock:** Better prefactor estimate. More accurate
instanton exponent (M enters through the WKB integral).

**Why it comes fifth:** Partially a byproduct of Rank 1 (V(q) from 5D
also involves the kinetic reduction). Lower independent leverage.

---

## 12. Recommended Phase 2 Entry Point

**Recommendation: Full V(q) from 5D Action (Put C Corridor)**

This is the highest-leverage target. It addresses the largest number of
open items simultaneously, provides the architectural foundation for all
downstream derivations (A, ω₀, L₀/δ via V(ξ)), and represents the single
most impactful step toward promoting τ_n from [Dc]+[P]+[Cal] to
something stronger.

The entry point should be Put C step C2: derive the non-geometric
contributions (V_node, V_bulk) to V(q) from the 5D action with junction
boundary conditions. The existing V_geom [Dc] provides a validated
geometric baseline against which new terms can be checked.

**Fallback if Put C is blocked:** Pivot to Rank 2 (V(ξ) from 5D) as a
narrower target that still delivers exponent closure even if the full
double-well remains [P].

---

## 13. Bottom Line

The Book IV neutron line after Phase 1 is **epistemically honest and
architecturally coherent, but not closed.** The headline result
τ_n ≈ 880 s is an assembly from a five-link chain in which one link is
topologically derived [Dc] (κ = 2π), two links are postulated [P]
(L₀/δ = π², V(q) double-well), and one is calibrated [Cal] (A ≈ 0.9).
The <1% agreement with observation is contingent on [P] and [Cal]
choices that are not independently determined by the theory.

Phase 1 accomplished what it set out to do: convert vague heuristic
arguments into scoped mathematical results, document circularity and
calibration risks, preserve dead ends, and remove overclaiming language.
The framework is now in a state where further closure attempts can be
evaluated against a precise epistemic baseline.

The strongest single next step is to derive V(q) from the 5D action
(Put C corridor), which would resolve the largest number of open items
and provide the foundation for all remaining closures.
