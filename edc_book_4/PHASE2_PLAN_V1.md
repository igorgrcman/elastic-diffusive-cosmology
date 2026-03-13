# Phase 2 Execution Plan: Full V(q) from 5D Action (Put C Corridor)

## 1. Title

Canonical Phase 2 Execution Plan for Book IV / Neutron Line:
**Derive V(q) from the 5D Action via the Put C Reduction Corridor**

---

## 2. Revision History

| Version | Date | Notes |
|---------|------|-------|
| **v1.0** | **2026-03-13** | Initial plan. Derived from the recommended entry point in `BOOK4_NEUTRONLINE_FINAL_STATUS_AFTER_PHASE1.md` §12. |
| **v1.1** | **2026-03-13** | Post-WP2 update. WP1 completed (donor normalization). WP2 executed: Israel junction energy (N1) tested → bounded no-go within minimal thin-junction S_EH + S_NG model. N1 reclassified as preserved dead-end. Surviving active lanes: N2 (bulk backreaction), thick-junction/internal-core. See `PHASE2_NEXTSTEP_PLAN_V1.md` for next-step lane selection. |

---

## 3. Origin of Phase 2

The final neutron-line forensic audit after Phase 1
(`BOOK4_NEUTRONLINE_FINAL_STATUS_AFTER_PHASE1.md`, §11–12) ranked five
candidate Phase 2 targets. **Rank 1 — Full V(q) from 5D Action (Put C
Corridor)** — was selected as the recommended entry point.

The rationale: V(q) is the architectural foundation of the instanton
program. It is the single derivation with the highest downstream
multiplier — one result would simultaneously address the double-well
structure [P], barrier height V_B [P], effective mass M(q) [P],
oscillation frequency ω₀ [P], and the E_arm ≡ Δm_np identification
[OPEN]. Every other open item in the neutron-line ledger (L₀/δ, A, ω₀)
requires V(q) as a prerequisite or co-input.

---

## 3A. Phase 2 Current Status (v1.1 Update)

**As of 2026-03-13, after WP2 execution:**

| Work Package | Status | Outcome |
|-------------|--------|---------|
| **WP-A (WP1)** | **Complete** | Donor normalization delivered (`PHASE2_WP1_DONOR_NORMALIZATION.md`). 14 donor assets inspected across 6 branches. 7 cleared, 5 archived as dead-end, 2 forbidden. Donor base clean. |
| **WP-B (WP2)** | **Partial — N1 tested** | Israel junction energy (N1) tested as primary node-well candidate. Result: **bounded no-go** within minimal thin-junction S_EH + S_NG model. Deficit angle identically zero (coplanar geometry). Arm-interior Israel energy ∝ V_geom (tension renormalization only). No attractive term generated. See `appendices/app_P2_WP2_Israel_nodewell.tex` and `code/p2_wp2_israel_nodewell_check.py` (6/6 tests pass). |
| **WP-C** | **Not reached** | Depends on WP-B producing a computable V(q). N1 yielded no new V(q) terms. |
| **WP-D** | **Partial** | Conservative ch03 update noting N1 no-go. Full WP-D integration deferred to after next lane execution. |

### Candidate Lane Status After WP2

| # | Candidate | Status Before WP2 | Status After WP2 | Active? |
|---|-----------|-------------------|-------------------|---------|
| **N1** | Israel junction energy (thin) | [OPEN] — primary candidate | **Bounded no-go** [Dc] within minimal model | **NO — preserved dead-end** |
| **N2** | Bulk gravitational backreaction | [OPEN] — speculative backup | [OPEN] — now primary surviving candidate | **YES** |
| **N3** | Warp-factor gradient coupling | Partially tested — no metastability | Unchanged; subsumable under N2 | **Conditional** |
| **N4** | Topological compact-direction | Partially falsified (ξ-BC) | Unchanged | **Limited** |
| **N5** | Helfrich bending | FALSIFIED (260/260) | Unchanged | **NO** |
| **N6** | Phenomenological Gaussian | [P/Cal] — no physical origin | Unchanged | **NO** |
| **N7** | Thick-junction / internal-core | Not previously listed as separate candidate | Identified by WP2 as escape route from thin-junction no-go | **YES — new active candidate** |

### Dead-End Preservation: N1

The N1 no-go is preserved for the following reasons:
1. **Prevents accidental revival.** Future work must not re-attempt thin-junction Israel conditions as a metastability source without new physics (e.g., higher-curvature terms, additional branes).
2. **Constrains the model class.** The no-go applies to ALL thin Y-junctions in ANY warped 5D background with S_EH + S_NG — it is geometric (coplanar arm angular sum = 2π), not parameter-dependent.
3. **Narrows the search.** Any viable node-well mechanism must involve physics not present in the thin-junction treatment: either internal core structure (thick-junction) or bulk field response (backreaction).
4. **Reference:** `appendices/app_P2_WP2_Israel_nodewell.tex`, §6 (Outcome Classification).

---

## 4. Phase 2 Objective

**Derive the effective potential V(q) along the collective coordinate q
from the 5D EDC action (S_bulk + S_brane + S_GHY + S_junction), and
determine whether the full V(q) has double-well structure.**

Concretely:
- Compute non-geometric terms (V_node, V_bulk) that supplement the
  known geometric sector V_geom(q) [Dc]
- Determine whether these terms create a secondary minimum at q_n > 0
- If yes: extract V_B, M(q), and ω₀ from the derived potential
- If no: document the no-go result and its implications

This is a **bounded attempt** at the Put C reduction corridor
(steps C2–C4), not a guarantee of double-well closure.

---

## 5. What Phase 2 Is Not

Phase 2 does **not** claim or attempt:

- Full closure of the neutron lifetime from first principles
- Derivation of L₀/δ (Rank 2 target; separate from Put C)
- Derivation of the prefactor A from the full 5D fluctuation determinant
  (Rank 4 target; downstream of V(q))
- Independent derivation of R₅ (Rank 3 target; orthogonal)
- Promotion of τ_n beyond [Dc]+[P]+[Cal] in a single phase
- A guaranteed positive outcome — no-go is explicitly allowed
- Rewriting Book IV chapters beyond minimal integration of new results
- Revival of any falsified lane from Phase 1 discovery

---

## 6. Epistemic Goal

The **strongest honest target** for the Phase 2 core output is:

| Outcome | V(q) Tag | Conditions |
|---------|----------|------------|
| **Best case** | [Dc] within declared 5D model | All Put C steps C2–C4 completed; secondary minimum confirmed; V_B computed |
| **Likely case** | [Dc\|model] partial | Some non-geometric terms derived; secondary minimum conditional on residual [P] assumptions |
| **Mixed case** | [P*] upgraded | Functional form narrowed; specific assumptions identified but not eliminated |
| **Negative case** | [OPEN] with documented no-go | Minimal 5D models insufficient; secondary minimum not found; result is a bounded non-confirmation |

Phase 2 does **not** assume success. A no-go result that documents why
V(q) does not have double-well structure in minimal 5D models is a valid
and valuable outcome.

---

## 7. Why This Target Comes First

From the final forensic audit §11:

1. **Highest multiplier.** V(q) from 5D simultaneously addresses ledger
   rows 3 (double-well), 4 (secondary minimum), 5 (V_B), 6 (M(q)), and
   13 (ω₀) — five of the fifteen open items.

2. **Architectural prerequisite.** The Rank 2 target (V(ξ) for L₀/δ)
   involves the same 5D variational machinery. Rank 4 (prefactor A)
   requires the bounce solution, which requires V(q). Rank 5 (M(q))
   is a byproduct of Put C. Doing Put C first builds infrastructure
   that all downstream targets reuse.

3. **Existing infrastructure.** The Put C corridor is defined
   (S5D_TO_SEFF_Q_REDUCTION.md), three model variants are already
   tested (PUTC_EXECUTION_REPORT.md), and executable code exists
   (putC_compute_MV.py). Phase 2 extends existing work rather than
   starting from zero.

4. **Decisive outcome.** If Put C yields a double-well: multiple [P]
   tags upgrade. If it yields no double-well: the instanton program
   either requires new physics or is falsified at the foundation level.
   Either outcome is high-information.

Other targets lack this combination. Rank 3 (R₅) could yield a quick
win but does not address the double-well. Rank 2 (V(ξ)) is narrower
and leaves the double-well open.

---

## 8. Existing Donor Infrastructure

| # | Donor Asset | Location (Branch / File) | Relevance | Quality | Reusable? |
|---|-------------|--------------------------|-----------|---------|-----------|
| D1 | Put C formal corridor (C1–C4 definitions) | `putC-computation-v1` / `S5D_TO_SEFF_Q_REDUCTION.md` | Canonical skeleton for 5D→1D reduction | [Dc] structural | ★★★★★ — directly reusable |
| D2 | Put C execution report (3 model variants) | `putC-computation-v1` / `PUTC_EXECUTION_REPORT.md` | Documents what failed; identifies gaps | [Dc/P/Cal] | ★★★★★ — critical baseline |
| D3 | Put C computation code | `putC-computation-v1` / `putC_compute_MV.py` | Tested V(q) scanner for 3 variants | [Cal] | ★★★★★ — extend, don't rewrite |
| D4 | Put C numerical results | `putC-computation-v1` / `putC_results.json` | 53+ records per variant | [Cal] | ★★★★ — comparison baseline |
| D5 | V_geom(q) chosen-path appendix | Current branch / `app_Vq_chosen_path.tex` | Geometric sector [Dc]; single-well confirmed | [Dc] | ★★★★★ — Phase 1 deliverable |
| D6 | M(q) derivation framework | `taskB-derive-Mq-v1` / `DERIVE_MQ_FROM_ACTION.md` | Methodology for canonical M(q) extraction | [Dc] structural | ★★★★ — framework reusable |
| D7 | Γ₀ prefactor derivation | `taskC-derive-Gamma0-v1` / `DERIVE_GAMMA0_FROM_ACTION.md` | Downstream: decay prefactor from V''(q_n) | [Dc] structural | ★★★ — after V(q) derived |
| D8 | Physical V_eff from 5D Dirac | `book2-open22-4-physical-veff-v1` / `OPEN22_4_PHYSICAL_VEFF_REPORT.md` | Different sector (Dirac), but shows 5D→V_eff derivation pattern | [Dc] | ★★★ — methodological |
| D9 | Junction-core geometry (C ∝ (L₀/δ)²) | `junction-core-derive-C-v1` | Structural scaling [Dc]; value circular | [Dc] structure / [I] value | ★★★ — supports M(q) |
| D10 | ξ-BC falsification suite | `frozen-brane-bc-v1` (7 files) | BC alone cannot create barrier; eliminates a mechanism | [Der] NO-GO | ★★ — cautionary |
| D11 | Helfrich NO-GO | `helfrich-well-from-action-v1` | Bending rigidity cannot source metastability | [Dc] NO-GO | ★★ — cautionary |
| D12 | Minimal 5D models insufficient | D2 above | Variants 1–2 produce no metastability | [Dc] | ★★★★★ — defines the gap |
| D13 | OPR-21 BVP infrastructure | `book2-opr21-bvp-foundation-v1` | Sturm-Liouville solver, Robin BC, eigenvalue extraction | [Dc]+[M] | ★★★ — if BVP needed |
| D14 | **WP2 Israel no-go (v1.1)** | Current branch / `app_P2_WP2_Israel_nodewell.tex` + `p2_wp2_israel_nodewell_check.py` | N1 bounded no-go: thin-junction Israel conditions yield Δθ ≡ 0 and V_Israel ∝ V_geom. Constrains next-lane search. | [Dc] NO-GO | ★★★★★ — mandatory constraint |

### Critical Prior Finding from D2/D12

The Put C execution report established that:
- **Variant 1** (flat bulk, Nambu-Goto): V(q) is monotonically increasing.
  No metastability. [Dc]
- **Variant 2** (warped/RS-like metric): Parameter scan found no
  metastability even with warping and brane tension. [Dc]
- **Variant 3** (warped + phenomenological node well): Metastability
  found with fitted parameters. V_B = 2.82 MeV achievable but requires
  phenomenological node well term [P/Cal]. V_B = 2 Δm_np does NOT
  emerge naturally.

**Implication for Phase 2:** The gap is the **physical origin of the node
well term**. The geometric sector V_geom is necessary but insufficient.
Phase 2 must identify what 5D physics (beyond Nambu-Goto + bulk gravity
in simple backgrounds) generates an attractive potential at q_n > 0.

---

## 9. Core Open Problem to Be Addressed

**Problem:** What non-geometric contribution to V(q) — arising from the
5D action with junction boundary conditions — creates a secondary minimum
at q_n > 0?

**Why it blocked Phase 1:**
- R3 (Phase 1) computed V_geom(q) [Dc] and confirmed it is a single well.
  This was the maximal result achievable without the non-geometric terms.
- The full double-well structure was declared [P] because V_node and V_bulk
  are not derived.
- Prior Put C attempts (Variants 1–2 on `putC-computation-v1`) showed that
  minimal models without additional structure produce no metastability.

**What is needed:**
1. Identify the physical mechanism within S_5D that generates V_node(q)
2. Compute V_node(q) + V_bulk(q) along the collective path
3. Combine with V_geom(q) [Dc] to form full V(q)
4. Determine whether double-well structure exists

**Candidate mechanisms** (updated after WP2):
- ~~Israel junction energy at the Y-junction vertex~~ — **bounded no-go** (WP2, v1.1). Thin-junction Israel conditions produce zero deficit angle and only tension renormalization. Not viable in minimal model.
- Bulk gravitational backreaction (N2) — junction displacement sources bulk metric perturbation; energy change depends on q. Partially tested in Variant 2 with negative results, but not with junction-sourced perturbations. **Active.**
- Thick-junction / internal-core structure (N7) — regularized core at scale δ with non-trivial internal metric and stress. Core energy depends on q through changing stress configuration at vertex. **Active — new candidate identified by WP2.**
- ~~Topological energy of compact-direction deformation~~ — partially falsified (ξ-BC, V' > 0). Not viable as sole source.
- ~~Warp-factor gradient coupling~~ — subsumable under N2; no independent mechanism identified.

---

## 10. Execution Architecture

Phase 2 is organized into four bounded work packages:

```
WP-A: Donor Normalization & Gap Analysis
WP-B: Core Derivation — Non-Geometric V(q) Terms
WP-C: Numerical Verification & Landscape Scan
WP-D: Chapter Integration & Epistemic Update
```

Dependencies:
```
WP-A ──→ WP-B ──→ WP-C ──→ WP-D
              └──→ WP-D (partial, even if WP-B yields no-go)
```

WP-A is a prerequisite. WP-B is the core derivation. WP-C is
verification (proceeds only if WP-B produces a computable result).
WP-D integrates results into Book IV regardless of outcome.

---

## 11. Step-by-Step Plan

### WP-A: Donor Normalization & Gap Analysis

**Goal:** Consolidate all donor material into a single consistent
notation and identify the precise gap between existing infrastructure
and the Phase 2 target.

**Steps:**

| Step | Action | Output | Tag |
|------|--------|--------|-----|
| A1 | Read and normalize `S5D_TO_SEFF_Q_REDUCTION.md` into Book IV notation | Corridor definition document with consistent symbols | [Def] |
| A2 | Read and summarize `PUTC_EXECUTION_REPORT.md` findings | One-page digest of what Variants 1–3 showed and where they failed | [Dc] |
| A3 | Catalog which terms in S_total = S_bulk + S_brane + S_GHY + S_junction are already computed vs open | Gap table: {term, status, what's needed} | [Def] |
| A4 | Identify candidate mechanisms for V_node from the 5D action structure | Ranked list of physical terms to investigate | [Def] |

**Strongest honest target:** [Def] — definitions and gap identification.
No derivation in WP-A.

**Key assumptions:** Donor material is accurate and internally consistent.

**Failure mode:** If the formal corridor (S5D_TO_SEFF_Q_REDUCTION.md) contains
structural errors or inconsistencies with Book IV, WP-A surfaces them as
blockers before derivation begins.

**Checkpoint A:** After A3–A4, assess whether any identified mechanism is
tractable. If all candidate mechanisms require physics not present in
S_EDC, flag as potential no-go and consult before proceeding to WP-B.

---

### WP-B: Core Derivation — Non-Geometric V(q) Terms

**Goal:** Derive V_node(q) and/or V_bulk(q) from the 5D action and
determine whether the full V(q) = V_geom + V_node + V_bulk has
double-well structure.

**Steps:**

| Step | Action | Output | Target Tag |
|------|--------|--------|------------|
| B1 | ~~Write the explicit Israel junction conditions for a Y-junction displaced by q from Steiner point~~ | ~~Junction matching conditions in terms of q~~ | **DONE — WP2 bounded no-go** |
| B2 | ~~Compute the Israel junction energy contribution V_Israel(q) from the matching conditions~~ | V_Israel ∝ V_geom (tension renormalization only); no attractive term | **DONE — no-go [Dc]** |
| B3 | Compute the next-lane contribution to V(q) — either V_bulk(q) from linearized gravity (N2) or V_core(q) from thick-junction (N7). See `PHASE2_NEXTSTEP_PLAN_V1.md` for lane selection. | V_node(q) or scaling estimate with identified coefficients | [Dc] or [P] |
| B4 | Combine V_geom [Dc] + V_Israel + V_bulk into full candidate V(q) | Candidate effective potential V(q; parameters) | [Dc\|model] |
| B5 | Analyze V(q) for critical points: minima at q = 0 and q_n, maximum at q_B | Classification: single-well, double-well, or no bound state | [Dc] |
| B6 | If double-well found: extract V_B, q_n, q_B, V''(q_n), V''(q_B) | Barrier parameters | [Dc\|model] |
| B7 | If double-well found: extract M(q) from the kinetic sector of the reduction | Effective mass function | [Dc\|model] |

**Strongest honest target:** [Dc] within the declared 5D reduction model.
Promotion to [Der] would require proving uniqueness of the reduction path
and showing no relevant terms are omitted, which is beyond Phase 2 scope.

**Key assumptions:**
- The adiabatic reduction (timescale separation, mode decoupling) holds [P]
- The Y-junction is treated as a codimension-2 defect in the 5D bulk [Def]
- The collective coordinate q parametrizes a specific chosen displacement
  (same as R3); path non-uniqueness is inherited [Dc]
- Background metric is taken as given (e.g., flat, RS-warped, or
  AdS-Schwarzschild slice) — choice declared as [I] or [P]

**Failure modes:**
- **B1 blocked:** Israel conditions for codimension-2 Y-junction may not
  have a standard form. If junction geometry is too complex for analytical
  matching, this is a structural blocker. → Pivot to effective junction
  energy model with explicitly declared ansatz.
- **B2–B3 yield only repulsive terms:** If V_Israel and V_bulk both add
  to V_geom (all repulsive), no secondary minimum exists. → Document as
  no-go within minimal model; identify what additional physics would be
  needed.
- **B4 double-well requires fine-tuning:** If a secondary minimum exists
  only for a narrow parameter window, document the tuning and flag it as
  [Cal]-dependent.
- **B5 single-well confirmed:** The full V(q) from 5D is single-well.
  → This is a significant negative result. The double-well postulate [P]
  is falsified within the minimal 5D model. The instanton program then
  requires either (a) additional physics beyond the minimal 5D action or
  (b) revision of the metastability mechanism.

**Checkpoint B1:** After step B2, assess whether V_Israel is analytically
tractable. If not, decide whether to proceed with numerical methods or
declare the step blocked.

**Checkpoint B2:** After step B5, assess the landscape:
- Double-well found → proceed to B6–B7 and WP-C.
- Single-well found → proceed directly to WP-D (no-go documentation).
- Ambiguous (depends on undetermined parameters) → document parameter
  dependence and proceed to WP-C with parameter scan.

---

### WP-C: Numerical Verification & Landscape Scan

**Goal:** Verify analytical results numerically and scan the parameter
space for robustness.

**Steps:**

| Step | Action | Output | Target Tag |
|------|--------|--------|------------|
| C1 | Extend `putC_compute_MV.py` with new model variants from WP-B | Updated code with Variant 4+ implementing Israel/bulk terms | [Check] |
| C2 | Reproduce WP-B analytical V(q) numerically at reference parameters | Match to <1% between analytical and numerical V(q) profiles | [Check] |
| C3 | Scan parameter space: identify which parameter regions give double-well vs single-well | Phase diagram: (parameter₁, parameter₂) → {single-well, double-well, no bound state} | [Check] |
| C4 | If double-well: compute V_B numerically and compare to 2 Δm_np | V_B table across parameter space; identify where V_B ≈ 2.59 MeV | [Check] |
| C5 | Sensitivity analysis: how much do V_B, q_n, q_B vary with model parameters | Sensitivity table analogous to Ch.09 τ_n sensitivity | [Check] |

**Strongest honest target:** [Check] — verification, not derivation.

**Key assumptions:** Code correctly implements the analytical expressions.
Standard numerical methods (root-finding, optimization) are adequate.

**Failure mode:** If parameter space has no double-well region, confirm
WP-B no-go numerically. If double-well exists only in a measure-zero
region, document as fine-tuned.

**Checkpoint C:** After C3, assess whether the double-well region is
natural (broad parameter range) or fine-tuned (narrow). Report to WP-D.

---

### WP-D: Chapter Integration & Epistemic Update

**Goal:** Integrate Phase 2 results into Book IV, regardless of whether
the outcome is positive, negative, or mixed.

**Steps:**

| Step | Action | Output |
|------|--------|--------|
| D1 | Create new appendix documenting the Put C derivation and results | `appendices/app_putC_Vq_from_5D.tex` |
| D2 | Update Ch.03 (double-well section) with Phase 2 status | Epistemic tags updated; forward ref to new appendix |
| D3 | Update Ch.06 (instanton) with any new V(q) information | M(q), ω₀ updates if derived |
| D4 | Update Ch.09 (τ_n assembly) if V_B or ω₀ are now derived | Reduced [P]/[Cal] dependence or documented no-go |
| D5 | Update `PHASE1_INTEGRATION_STATUS.md` or create Phase 2 status document | Epistemic ledger with Phase 2 outcomes |
| D6 | Build check — verify PDF compiles | Clean build |

**Strongest honest target:** Book IV chapters reflect actual Phase 2
outcome with no overclaiming.

---

## 12. Possible Outcomes

### Outcome A: Strong Partial Closure

V(q) derived from 5D action with double-well structure confirmed.
V_B computed. M(q) extracted. Residual dependence on background metric
choice [I] and adiabatic approximation [P].

- V(q): [P] → [Dc\|model]
- V_B: [P] → [Dc\|model]
- M(q): [P] → [Dc\|model]
- τ_n: [Dc]+[P]+[Cal] → [Dc]+[Dc\|model]+[Cal] (A still calibrated)
- **Net:** Significant upgrade. Double-well confirmed within a 5D model.

### Outcome B: Mixed / Conditional Closure

Double-well exists only for specific parameter values or background
metric choices. V_B depends on undetermined coefficients. The result is
conditional: "If the 5D parameters satisfy [conditions], then
double-well with V_B ≈ 2 Δm_np."

- V(q): [P] → [Dc\|model, conditional]
- V_B: [P] → [Dc\|model, conditional]
- **Net:** Informative but not decisive. The postulate [P] is replaced by
  a condition, which is progress, but the condition itself may be [P].

### Outcome C: Non-Confirmation

Double-well exists but V_B ≠ 2 Δm_np. The derived barrier height is,
e.g., 4 MeV or 1 MeV, incompatible with the conjectured value. The
instanton exponent changes, and τ_n shifts by orders of magnitude.

- V(q): [P] → [Dc\|model] (structure derived, but not matching conjecture)
- V_B = 2 Δm_np: **falsified** within the model
- **Net:** High-information negative result. The V_B conjecture is replaced
  by a derived value, which propagates through Ch.09.

### Outcome D: No-Go / Negative Result

The full V(q) from minimal 5D models (flat, warped, Israel, linearized
gravity) is single-well. No secondary minimum. The double-well postulate
[P] is falsified within the examined model class.

- V(q): [P] remains [P]; no promotion possible within minimal models
- **Net:** The metastability mechanism requires physics beyond the
  minimal 5D action (e.g., non-perturbative effects, additional fields,
  or topology change). This constrains the theory and directs future work.
  The no-go is documented and preserved.

**v1.1 note:** WP2 has partially realized Outcome D for the Israel
junction sector specifically. Within the thin-junction S_EH + S_NG model
class, Israel conditions do not produce attraction. This is a bounded
no-go for one mechanism, not a total no-go for the double-well. Two
active lanes remain (N2, N7). Full Outcome D applies only if all
remaining lanes also yield no-go.

---

## 13. Circularity / Smuggling Risks

### Risk 1: Importing V_B = 2 Δm_np as a Target

**Risk:** Tuning model parameters to reproduce V_B = 2 Δm_np rather
than deriving V_B from the action.
**Anti-smuggling rule:** V_B must be computed BEFORE comparing to
2 Δm_np. The comparison is a consistency check [Check], not a derivation
input. If V_B is matched by parameter adjustment, the result is [Cal],
not [Dc].

### Risk 2: Phenomenological Node Well Relabeled as [Dc]

**Risk:** The Put C Variant 3 (warped + node well) used a phenomenological
V_node = −V₀ × exp(−(q−q*)²/2w²). If Phase 2 merely refines the
functional form of the node well without deriving its physical origin,
the result remains [P/Cal].
**Anti-smuggling rule:** V_node must emerge from explicit terms in S_5D
(Israel conditions, bulk backreaction, etc.). A fitted Gaussian or
similar ansatz is [P], regardless of how well it matches.

### Risk 3: Background Metric Chosen to Produce Double-Well

**Risk:** Scanning over background metrics (flat, RS, AdS-Schwarzschild,
etc.) until one produces a double-well, then declaring that metric
"physical."
**Anti-smuggling rule:** The background metric must be declared [I] or
[P] at the start, not selected post-hoc. If multiple metrics are
scanned, all results must be reported, not just the one that works.

### Risk 4: Adiabatic Approximation Absorbing the Gap

**Risk:** The adiabatic reduction (5D → 1D) involves integrating out
fast modes. If the "fast mode" integration is done approximately or with
undetermined coefficients, these coefficients can absorb the missing
physics and fake a double-well.
**Anti-smuggling rule:** Every coefficient in V(q) must be traceable to
an explicit integral over the extra dimensions. Undetermined coefficients
must be declared [P] and cannot be fit to produce a desired potential shape.

### Risk 5: Circular Use of τ_n to Constrain V(q)

**Risk:** Using the measured τ_n ≈ 878 s [BL] to back-compute what V_B
must be, then declaring V(q) "derived."
**Anti-smuggling rule:** τ_n [BL] appears ONLY in the final comparison
(Ch.09 consistency check). It must never enter the V(q) derivation chain.

---

## 14. Guard Compliance

### G1: Ontological Purity

All V(q) derivation uses EDC-native vocabulary (junction, loop, mode,
cluster, brane, bulk). No Standard Model language (quark, gluon, QCD).
Comparisons to conventional physics quarantined in Appendix X.

### G2: Empirical Protocol

Empirical data (Δm_np, τ_n, r_p) appear only as [BL] baselines for
comparison. They do not enter the derivation chain.

### G3: Anti-Calibration

Parameters fit to data are tagged [Cal]. Parameters derived from the
action are tagged [Dc] or [Der] with explicit scope. Co-tuning of
multiple [Cal] parameters is forbidden.

### G4: Anti-Back-Promotion

If a Phase 2 result is [Dc\|model], it does not retroactively upgrade
Phase 1 results that are [P]. The [P] tags in Ch.03 and Ch.08 persist
unless independently resolved.

### G5: Donor Provenance

Every imported result must cite its source branch and file. No anonymous
donor content. Dead ends (Helfrich, ξ-BC, minimal models) must not be
silently revived; if revisited, the reason must be documented.

### G6: Path Non-Uniqueness

The collective coordinate q is a chosen path [Dc], not a uniquely derived
normal mode. Phase 2 inherits this limitation from R3. If Phase 2 uses
the same path, this is stated. If a new path is chosen, both paths are
documented and compared.

---

## 15. Checkpoints

| ID | After | Decision Gate | Proceed If | Stop/Narrow If |
|----|-------|--------------|------------|----------------|
| **CP-A** | WP-A (gap analysis) | Are any candidate mechanisms for V_node tractable? | At least one mechanism can be computed from S_5D terms | All mechanisms require physics not in S_EDC → potential no-go; consult before WP-B |
| **CP-B1** | Step B2 | ~~Is V_Israel analytically tractable for the Y-junction?~~ | **RESOLVED (WP2):** V_Israel is tractable — result is bounded no-go. No attractive term. | Proceed to next lane (N2 or N7). See `PHASE2_NEXTSTEP_PLAN_V1.md`. |
| **CP-B2** | Step B5 | Does full V(q) have double-well structure? | Yes → proceed to B6–B7, WP-C | No → document no-go; proceed directly to WP-D |
| **CP-C** | Step C3 | Is the double-well region natural or fine-tuned? | Broad parameter region → strong result | Measure-zero or narrow region → document as fine-tuned; downgrade tag |
| **CP-D** | WP-D complete | Do chapter updates match actual epistemic outcome? | Tags are honest; no overclaiming | Any mismatch between result and chapter language → fix before commit |

---

## 16. Deliverable Plan

Files likely to be created or modified (not created now):

### New Files

| File | Purpose |
|------|---------|
| `appendices/app_putC_Vq_from_5D.tex` | Phase 2 core appendix: Put C derivation, V(q) from 5D action |
| `code/putC_phase2_verify.py` | Numerical verification of V(q) from WP-B; extends putC_compute_MV.py |
| `audit/PHASE2_EXECUTION_STATUS.md` | Phase 2 outcome documentation; epistemic ledger update |

### Modified Files

| File | Likely Changes |
|------|---------------|
| `main.tex` | Add `\input{appendices/app_putC_Vq_from_5D}` |
| `chapters/ch03_neutron_metastable.tex` | Update double-well section with Phase 2 outcome; forward ref to new appendix |
| `chapters/ch06_instanton.tex` | Update V(q) status; M(q) if derived |
| `chapters/ch09_tau_n_prediction.tex` | Update ω₀, V_B if derived; adjust τ_n assembly tags |
| `appendices/app_Vq_chosen_path.tex` | Add cross-reference to Phase 2 appendix; note V_geom baseline role |
| `audit/PHASE1_INTEGRATION_STATUS.md` | Add Phase 2 outcome row |

---

## 17. Integration Impact

| Chapter/Appendix | Impact Level | Nature of Change |
|-----------------|-------------|------------------|
| Ch.03 (metastable junction) | **High** | Double-well status upgrade or no-go; V_B update |
| Ch.06 (instanton) | **Medium** | V(q) status in effective action; M(q) if derived |
| Ch.09 (τ_n prediction) | **Medium** | ω₀ and V_B tags; anti-tuning firewall update |
| App. B (V_geom chosen path) | **Low** | Cross-reference only |
| App. C (L₀/δ BVP) | **None** | Independent of Put C |
| App. A (N_bonds) | **None** | Independent of Put C |
| main.tex preface | **Low** | Status language update if warranted |
| Ch.07 (κ homotopy) | **None** | κ = 2π is independent |
| Ch.08 (L₀/δ) | **None** | Phase 2 does not address L₀/δ |

---

## 18. Success Criteria

Phase 2 is successful if it achieves at least one of the following:

1. **Derives V_node(q) or V_bulk(q) from explicit 5D action terms** with
   identified coefficients and traceable integrals. Tag: at least [Dc\|model].
   The derived terms, combined with V_geom [Dc], yield a computable V(q).

2. **Determines whether double-well structure exists** within the minimal
   5D model class. A confirmed yes or confirmed no are both successes.

3. **If double-well confirmed:** extracts V_B and at least one of {M(q), ω₀}
   as derived quantities, replacing [P] tags with [Dc\|model].

4. **If no double-well:** documents the no-go with sufficient precision
   to identify what additional physics would be required. Converts an
   unnamed [P] gap into a named, bounded constraint.

Phase 2 is **not** successful if:
- It merely repeats Phase 1 Put C Variant 3 with a relabeled node well
- It produces results that depend on fitted parameters without identifying
  their physical origin
- It overclaims [Dc] for results that are actually [P] or [Cal]
- It fails to document its outcome clearly enough for the next phase

---

## 19. Failure Criteria / Abort Signals

| Signal | Response |
|--------|----------|
| **CP-A: No tractable mechanism identified** | Pause WP-B. Document the gap. Consider pivoting to Rank 2 (V(ξ) from 5D) as fallback. |
| **CP-B1: Israel conditions intractable** | Pivot to effective junction energy model with explicit [P] ansatz. Document the structural limitation. Phase 2 continues with reduced scope. |
| **CP-B2: Single-well confirmed across all model variants** | Proceed to WP-D with no-go documentation. This is a valid and valuable Phase 2 outcome. Do not force a double-well by adding phenomenological terms. |
| **CP-C: Double-well requires fine-tuning (< 5% of parameter space)** | Document as fine-tuned. Tag result [Dc\|model, fine-tuned]. Do not present as natural. |
| **Persistent model dependence: V(q) shape changes qualitatively with metric choice** | Document the metric dependence. Tag as [Dc\|model, metric-dependent]. This is a partial result, not a failure, but limits downstream claims. |
| **Discovery of structural inconsistency in the Put C corridor** | Stop. Investigate. Do not paper over. Report to next audit. |

---

## 20. Bottom Line

Phase 2 targets the single highest-leverage open problem in the Book IV
neutron line: **deriving V(q) from the 5D action to determine whether
double-well structure exists.** This is the architectural foundation that
all other open items depend on. The plan is structured around the Put C
reduction corridor (C2–C4), with existing donor infrastructure from three
branches and validated code.

The plan is bounded: four work packages, five checkpoints, explicit
failure modes at each stage. A no-go result is an allowed and
informative outcome — if the minimal 5D action does not produce a
double-well, that constrains the theory and redirects future work.

Phase 2 is worth attempting because it is the only route that can
simultaneously address five open items in the neutron-line ledger, and
because the existing infrastructure (corridor definition, three tested
model variants, executable code) means the marginal cost of the attempt
is bounded while the information value — positive or negative — is high.
