# R1 Global Discovery: All Branches and Local Files

**Date:** 2026-03-13
**Branch:** research/topological-pinning-v7_8-integration
**Purpose:** Forensic inventory of all R1-related content across the entire repo
**Scope:** Discovery only — no implementation

---

## 1. Executive Verdict

**The repo contains substantial hidden R1-related work across ~25 branches, most of it
not visible from the current branch or captured in the R1 preflight audit.**

Key findings:
1. **C = (L₀/δ)² = 100 "derivation"** exists on `junction-core-derive-C-v1` and
   `delta-audit-anchor-v1` — but is **circular** (uses L₀ = 1.0 fm [I] and δ = 0.1 fm [I]
   as inputs; confirms dimensional analysis, not independent derivation)
2. **L₀/δ tension resolution** exists on `book-routeC-narrative-cleanup-v1` (commit e7f298f) —
   claims static (π²) vs dynamic (9.33) difference is "quantum corrections" [Dc];
   actually depends on r_p [BL] input
3. **Prefactor A derived** from semiclassical formula: A = π(ω₀/ω_B)/√(L₀/δ) [Der within 1D model]
   — genuine result, upgrades A from [Cal] to [Der]
4. **OPR-21 BVP infrastructure** is complete and executable across multiple branches —
   Sturm-Liouville solver, Robin BC, eigenvalue extraction all validated
5. **δ scale ambiguity** is severe: four distinct "δ-like" scales (R_ξ ~ 0.002 fm,
   Δ ~ 0.003 fm, ℓ ~ 0.013 fm, δ ~ 0.1 fm) with ~50× spread, never reconciled
6. **Helfrich bending route** is falsified (260/260 NO-GO) — dead end preserved
7. **Six OPR-20 factor-8 attempts (A–F)** all failed to achieve closure — documented
8. **No branch anywhere derives R₅ from first principles** — confirms preflight conclusion

**Bottom line: Nothing found that materially changes the R1 Mode B recommendation.
The prefactor A derivation is the only genuinely new [Der] result not in the audit.
The δ-scale ambiguity is a previously undocumented risk factor.**

---

## 2. Branches Inspected

| # | Branch | Exists | R1 Content |
|---|--------|--------|------------|
| 1 | `research/topological-pinning-v7_8-integration` (current) | ✓ | Primary: ch08, ch09, audit |
| 2 | `main` | ✓ | Baseline; no edc_book_4 |
| 3 | `book2-opr21-bvp-foundation-v1` | ✓ | BVP lemma chain + demo |
| 4 | `part2-opr21-bvp-numerical-demo` | ✓ | Pöschl-Teller toy solver |
| 5 | `part2-opr21-bvp-closure-pack` | ✓ | Pointer-only variant of #3 |
| 6 | `part2-bvp-workpackage-opr02-21` | ✓ | BVP specification doc |
| 7 | `part2-gf-opr20-attemptF-mediator-bvp-junction` | ✓ | Robin BC + α scan |
| 8 | `part2-gf-g5-kk-tightening` | ✓ | g₅→g₄ KK normalization |
| 9 | `book2-opr04-delta-derivation-v1` | ✓ | Scale taxonomy (Δ, δ, ℓ, R_ξ) |
| 10 | `book2-opr04-delta-equals-Rxi-v1` | ✓ | δ ≡ R_ξ closure attempt |
| 11 | `book2-opr19-g5-derivation-v1` | ✓ | g₅ from 5D action |
| 12 | `book2-opr22-geff-derivation-v1` | ✓ | G_eff(g₅, ℓ) derivation |
| 13 | `part2-gf-opr22-full-closure-plan` | ✓ | G_F closure spine |
| 14 | `part2-closurepass-opr-falsified-attempt3` | ✓ | Z₃ CP falsified |
| 15 | `delta-audit-anchor-v1` | ✓ | δ forensic audit + C derivation |
| 16 | `helfrich-well-from-action-v1` | ✓ | Helfrich NO-GO (260/260) |
| 17 | `junction-core-derive-C-v1` | ✓ | C = (L₀/δ)² derivation |
| 18 | `junction-core-well-v1` | ✓ | V_B computation with C=100 |
| 19 | `frozen-brane-bc-v1` | ✓ | ξ-BC structure (no minimum) |
| 20 | `putC-computation-v1` | ✓ | 3 model variants for V(q) |
| 21 | `book2-opr20-mediator-mass-v1` | ✓ | m_φ = x₁/ℓ eigenvalue |
| 22 | `book-routeC-narrative-cleanup-v1` | ✓ | Tension resolution + A [Der] |
| 23 | `part2-gf-opr20-attemptD-...-robin-overcount` | ✓ | Robin BC + overcounting |
| 24 | `part2-gf-opr20-attemptE-prefactor8-derivation` | ✓ | Factor-8 first-principles |
| 25 | `part2-gf-opr20-factor8-attempt3` | ✓ | Factor-8 forensic sweep |
| 26 | `part2-gf-opr20-factor8-geometric-attemptC` | ✓ | Geometric factor-8 |
| 27 | `part2-gf-opr20-factor8-forensic` | ✓ | BC eigenvalue sweep |
| 28 | `part2-gf-opr20-suppression-attempt2` | ✓ | f_geom = R_ξ/r_e |
| 29 | `part2-gf-opr19-coefficient-provenance` | ✓ | g₅ coefficient audit |
| 30 | `book2-open22-4-physical-veff-v1` | ✓ | V_eff from 5D action |
| 31 | `book2-open22-4b-fd-robin-fix-v1` | ✓ | Robin BC FEM fix |
| 32 | `book2-open22-4b-physical-mu-sweep-v1` | ✓ | μ-parameter sweep |
| 33 | `book2-open22-4b1-slice-family-v1` | ✓ | Robin BC canonical family |
| 34 | `book2-opr01-sigma-anchor-v1` | ✓ | σ anchoring + OPR-21 bridge |
| 35 | `book2-opr02-robin-alpha-from-action-v1` | ✓ | Robin α partial derivation |
| 36 | `reorganization-epistemic-framework` | ✓ | OPR register + standards |
| 37 | `audit/donor-hunt-pass3-v1` | ✓ | Cross-repo donor locator |
| 38 | `audit/gap-register-full-v1` | ✓ | 90-gap prioritized catalog |
| 39 | `audit/prelet-scan-v1` | ✓ | Page-by-page gap scan |
| 40 | `book2-neutron-dual-route-v1` | ✓ | Minimal R1 content |

Also checked: 4 git stash entries (no R1-relevant content).

Missing branches (requested but don't exist locally):
- `book2-opr21-closure-writeup-v1`
- `book2-opr21-physics-closure-v1`
- `book2-opr21r-mu-window-recalibration-v1`
- `book2-opr21r-propagation-sweep-v1`
- `claude/analyze-codebase-KKY9n`

---

## 3. Search Strategy

**Terms searched** (grep, git log --grep, manual file inspection):
`L_0`, `L0`, `L₀`, `R_5`, `R5`, `compactification`, `Sturm-Liouville`,
`eigenvalue`, `localization`, `bound state`, `thick brane`, `square well`,
`BVP`, `boundary value`, `transcendental`, `kappa`, `tau_n`, `S_E`,
`instanton`, `mode matching`, `standing wave`, `delta`, `Helfrich`,
`junction core`, `C = `, `prefactor`

**Method:** Four parallel search agents covering:
- Agent 1: BVP/eigenvalue branches (#3–7)
- Agent 2: KK/compactification/delta branches (#8–21)
- Agent 3: Current branch + main + edc_papers/ + edc_book_2/
- Agent 4: Remaining 20 branches (#22–40)

Plus manual deep-reads of key files from `junction-core-derive-C-v1`,
`delta-audit-anchor-v1`, and `book-routeC-narrative-cleanup-v1`.

---

## 4. Discovery Hits Table

### 4.1 High-Relevance Findings

| Branch | File | Topic | Relevance | Quality | Reusable? |
|--------|------|-------|-----------|---------|-----------|
| `junction-core-derive-C-v1` | `DERIVE_C_FROM_GEOMETRY.md` | C = (L₀/δ)² = 100 | **Direct R1** | [Dc]* see §5.1 | Partial — circular |
| `delta-audit-anchor-v1` | `DELTA_ANCHOR_MAP.md` | Four δ-scales forensic audit | **Direct R1** | [I] audit | YES — critical |
| `book-routeC-narrative-cleanup-v1` | `docs/L0_DELTA_TENSION_RESOLUTION.md` | π² vs 9.33 resolution | **Direct R1** | [Dc]* see §5.2 | Partial |
| `book-routeC-narrative-cleanup-v1` | `docs/PREFACTOR_A_DERIVATION_NOTE.md` | A = π(ω₀/ω_B)/√(L₀/δ) | **Direct R1** | [Der] genuine | YES |
| `book2-opr21-bvp-foundation-v1` | `OPR-21.md` + demo code | BVP lemma chain L1–L5 | **Infrastructure** | [Dc]+[M] | YES |
| `part2-opr21-bvp-numerical-demo` | `bvp_halfline_toy_demo.py` | Finite-diff eigenvalue solver | **Infrastructure** | [M] validated | YES |
| `book2-opr04-delta-derivation-v1` | `ch16_opr04_delta_derivation.tex` | Scale taxonomy (Δ, δ, ℓ, R_ξ) | **Foundation** | [M]+[Dc] | YES |
| `book2-opr04-delta-equals-Rxi-v1` | `OPR04_CLOSURE_REPORT.md` | δ ≡ R_ξ closure: ALL routes blocked | **Negative** | [P] blocked | YES — dead end |
| `helfrich-well-from-action-v1` | `HELFRICH_EXECUTION_REPORT.md` | Bending rigidity NO-GO (260/260) | **Falsified** | [Dc] NO-GO | YES — dead end |
| `frozen-brane-bc-v1` | 7 markdown files | ξ-BC alone: no minimum | **Falsified** | [Dc] | YES — dead end |
| `putC-computation-v1` | `putC_compute_MV.py` + results | 3 model variants, minimal fails | **Negative** | [Cal] | YES — baseline |

### 4.2 Supporting/Infrastructure Findings

| Branch | File | Topic | Quality | Reusable? |
|--------|------|-------|---------|-----------|
| `part2-gf-g5-kk-tightening` | `ch11_g5_canonical_and_kk.tex` | g₅→g₄ KK normalization | [Dc]+[P] | YES |
| `book2-opr19-g5-derivation-v1` | `ch17_opr19_g5_from_action.tex` | g₅ from 5D gauge action | [Dc]+[P] | YES |
| `book2-opr22-geff-derivation-v1` | `ch19_opr22_geff_from_exchange.tex` | G_eff formula | [Dc]+[P] | YES |
| `book2-opr20-mediator-mass-v1` | `ch18_opr20_mediator_mass.tex` | m_φ = x₁/ℓ eigenvalue | [Dc]+[P] | YES |
| `part2-gf-opr22-full-closure-plan` | `ch11_gf_full_closure_plan.tex` | G_F closure spine | [Dc] | YES |
| `book2-opr01-sigma-anchor-v1` | `ch14_opr21_closure_derivation.tex` | σ anchor + BVP chain | [Dc]+[P] | YES |
| `book2-open22-4-physical-veff-v1` | `ch19_opr22_geff_from_exchange.tex` | V_eff from 5D action | [Dc]+[P] | YES |
| `book2-open22-4b-fd-robin-fix-v1` | FEM correction | Robin BC discretization fix | [Dc] | YES |
| `book2-open22-4b-physical-mu-sweep-v1` | μ-sweep results | Localization parameter landscape | [Dc] numerical | YES |

### 4.3 Factor-8 Attempts (All Failed/Partial)

| Branch | Attempt | Result | Status |
|--------|---------|--------|--------|
| `part2-gf-opr20-suppression-attempt2` | A2: f_geom = R_ξ/r_e | Max ×4 | PARTIAL |
| `part2-gf-opr20-factor8-geometric-attemptC` | C: geometric | Max ×4 | PARTIAL |
| `part2-gf-opr20-attemptD-...-robin-overcount` | D: Z₂+Israel | Overcounting found | AUDITED |
| `part2-gf-opr20-attemptE-prefactor8-derivation` | E: circumference | Residual ×0.9 | PARTIAL |
| `part2-gf-opr20-factor8-attempt3` | Forensic sweep | No closure | PARTIAL |
| `part2-gf-opr20-attemptF-mediator-bvp-junction` | F: BKT+Robin α scan | α not derived | PARTIAL |

---

## 5. Strongest Newly Found Donor Content

### 5.1 C = (L₀/δ)² = 100 — Circular, Not Independent

**Location:** `junction-core-derive-C-v1` → `DERIVE_C_FROM_GEOMETRY.md` (473 lines)

**What it claims:** C is derived [Dc] from 3D→1D reduction of junction-core density:
```
ρ_core(x,y,q) = σ × g_⊥(r_⊥/r₀) × f(q/δ)   [separable ansatz]
V_core(q) = −σ × r₀² × I_⊥ × f(q/δ)
E₀ = C × σ × δ²  with  C = I_⊥ × (r₀/δ)²
```

For standard profiles: I_⊥ = π. With identification r₀ = L₀:
```
C = π × (L₀/δ)²
```

But the derivation then drops the π factor (§6.4: "if f already includes normalization")
to get C = (L₀/δ)² = (1.0/0.1)² = 100.

**Assessment:** This is dimensional analysis confirming itself. Both L₀ = 1.0 fm
and δ = 0.1 fm are [I] inputs. The derivation shows *why* C has the form (L₀/δ)²
— which is useful structure — but does not derive the *value* 100 independently.
The I_⊥ = π factor is dropped by ad hoc normalization choice. If kept, C = 314,
contradicting the scan. **Not an independent derivation of L₀/δ = 10.**

**Reusable:** The *structure* C ∝ (L₀/δ)² is legitimate [Dc]. The *value* 100
requires the same [I] inputs as everything else.

### 5.2 L₀/δ Tension Resolution — Depends on r_p [BL]

**Location:** `book-routeC-narrative-cleanup-v1` (commit e7f298f) →
`docs/L0_DELTA_TENSION_RESOLUTION.md`

**What it claims:** The tension between π² ≈ 9.87 (static/resonance) and
9.33 (dynamic/tunneling) is resolved by recognizing they apply to different
physical contexts. The 5.5% difference = "quantum corrections."

**Assessment:** The "dynamic" value 9.33 comes from L₀ = r_p + δ = 0.875 + 0.105,
which uses the measured proton charge radius r_p = 0.875 fm [BL]. This is not a
derivation — it's a brane-to-observer map using an empirical input. The
"resolution" frames calibration as context-dependence. The epistemic status
is [Dc] conditional on the brane→observer map [P] and r_p [BL].

**Reusable:** YES as comparison framework. The two-context framing is physically
reasonable but should not be presented as closing the L₀/δ tension.

### 5.3 Prefactor A from Semiclassics — Genuine [Der]

**Location:** `book-routeC-narrative-cleanup-v1` (commit e7f298f) →
`docs/PREFACTOR_A_DERIVATION_NOTE.md` +
`edc_papers/_shared/derivations/prefactor_A_from_fluctuations.tex`

**What it derives:**
```
A = π × (ω₀/ω_B) / √(L₀/δ)
```

From standard semiclassical tunneling theory (WKB/instanton):
```
τ = (2π/ω_B) × √(πℏ/2S_E) × exp(S_E/ℏ)
```

Comparing to τ = A × (ℏ/ω₀) × exp(S_E/ℏ) and using S_E/ℏ = 2π(L₀/δ):
```
A = π × (ω₀/ω_B) / √(S_E/2πℏ) = π × (ω₀/ω_B) / √(L₀/δ)
```

With ω₀/ω_B ≈ 0.82 and L₀/δ = 9.33: A ≈ 0.84.

**Assessment:** This is a **genuine derivation** within the 1D effective model [Der].
It upgrades A from [Cal] to [Der] (conditional on the 1D model [P]). The formula
connects A to physically meaningful quantities (well/barrier curvature ratio and
geometric scale ratio). The ω₀/ω_B ratio is model-dependent but constrained.

**Reusable:** YES — this is the strongest new finding. Should be incorporated into
the R1 implementation as it provides a non-circular relation between A and L₀/δ.

### 5.4 δ-Scale Ambiguity — Critical Risk Factor

**Location:** `delta-audit-anchor-v1` → `DELTA_ANCHOR_MAP.md` (372 lines)

**Discovery:** The repo uses **four distinct thickness-like scales**:

| Symbol | Value | Context | Status |
|--------|-------|---------|--------|
| R_ξ | ~0.002 fm | Membrane correlation length | [P]+[BL] (via M_Z) |
| Δ | ~0.003 fm | Electron mass formula | [P] (OPR-04) |
| ℓ | ~0.013 fm | Orbifold circumference (2πR_ξ) | [Dc] |
| δ | ~0.1 fm | Junction core / Put C | [I] (not in book!) |

**Critical finding:** δ = 0.1 fm is ~50× larger than R_ξ. This is noted in the
audit as "introduced in code without book-level anchoring." The factor-50 gap
between the EW-scale thickness (R_ξ) and the nuclear-scale thickness (δ) is
never explained or reconciled.

**Assessment:** This is a **previously undocumented risk factor** for R1. If R1
uses δ = 0.1 fm, it must justify why this scale (not R_ξ or Δ) is the correct
brane thickness for the localization problem. The L₀/δ ratio is meaningless
if δ itself is ambiguous by a factor of 50.

**Reusable:** YES — the scale taxonomy from `book2-opr04-delta-derivation-v1` is
foundational and should be explicitly referenced.

---

## 6. Dead Ends / Falsified Lanes Worth Preserving

### 6.1 Helfrich Bending Route — FALSIFIED

**Branch:** `helfrich-well-from-action-v1` + `junction-core-derive-C-v1`
**Result:** 260/260 configurations tested, 0 metastable wells found.
**Reason:** V_bend ~ +κq²/a² (positive quadratic) reinforces Nambu-Goto stretching.
Cannot create well with c₀ = 0.
**Preserve as:** Dead end. Do not revisit κ ~ σδ² as metastability source.

### 6.2 ξ-Boundary Conditions Alone — FALSIFIED

**Branch:** `frozen-brane-bc-v1`
**Result:** V'_lin(d) > 0 for ALL BC types (Neumann, Robin, Dirichlet).
**Reason:** ξ-direction boundary conditions produce no attraction; minimum comes
from radial-frozen core (topology), not ξ-BC.
**Preserve as:** Dead end. Do not expect ξ-BC to generate metastable well.

### 6.3 δ ≡ R_ξ Closure — ALL ROUTES BLOCKED

**Branch:** `book2-opr04-delta-equals-Rxi-v1`
**Result:** Three routes attempted, all OPEN:
- Route A (Diffusion → BL theorem): BLOCKED
- Route B (Junction → Robin → δ): PARTIAL
- Route C (S¹ geometry): PARTIAL
**Preserve as:** Ongoing gap. δ identification remains [P].

### 6.4 Flux Quantization for L₀/δ — DEAD END

**Location:** `DERIVE_L0_DELTA_PI_SQUARED.md` (v1, Routes 3a–3c)
**Result:** Three flux quantization attempts, none produced L₀/δ.
**Preserve as:** Dead end. Do not revisit flux quantization as L₀/δ source.

### 6.5 OPR-20 Factor-8 (Six Attempts) — NO CLOSURE

**Branches:** Six separate `part2-gf-opr20-*` branches
**Result:** None achieved full factor-8 suppression from first principles.
Attempt D found overcounting. Attempt F found "broad region" (47.6% of
parameter space) but α not derived.
**Preserve as:** Ongoing gap. Not directly R1 but illustrates the difficulty
of parameter derivation in this framework.

### 6.6 Minimal 5D Models for V(q) — INSUFFICIENT

**Branch:** `putC-computation-v1`
**Result:** Variant 1 (flat bulk): no metastability. Variant 2 (warped/RS): no
metastability. Variant 3 (warped + node well): metastable with [P/Cal] node well.
**Preserve as:** V_B = 2×Δm_np does NOT emerge from minimal 5D models.
Phenomenological node well [P] required.

---

## 7. Comparison Against Current R1 Preflight Audit

### 7.1 What the Preflight Audit Captured Correctly

- R₅ never independently derived ✓ (confirmed across all 40 branches)
- All L₀/δ routes are [P] heuristic ✓
- π² vs 3π tension ✓
- Sturm-Liouville structure well-posed ✓
- Mode B (partial closure) recommendation ✓
- M(q) circularity ✓
- τ_n exponential sensitivity ✓

### 7.2 What the Preflight Audit Missed

| Item | Location | Impact |
|------|----------|--------|
| **Prefactor A [Der] formula** | commit e7f298f | A = π(ω₀/ω_B)/√(L₀/δ) upgrades A from [Cal] to [Der]; creates non-circular A↔(L₀/δ) relation |
| **δ-scale ambiguity** (4 distinct δ values, factor-50 spread) | `delta-audit-anchor-v1` | R1 result meaningless if δ itself is undefined by ×50 |
| **C = (L₀/δ)² structure** (valid) but value circular | `junction-core-derive-C-v1` | Confirms dimensional structure but no independent constraint |
| **Helfrich NO-GO** (falsified route) | `helfrich-well-from-action-v1` | Not critical for R1 but relevant context |
| **ξ-BC no-minimum result** | `frozen-brane-bc-v1` | Constraints on localization mechanism |
| **Minimal 5D models insufficient** for V_B | `putC-computation-v1` | Node well [P] required — R1 inherits this |
| **OPR-21 BVP complete infrastructure** (solver, Robin, I₄) | `book2-opr21-bvp-foundation-v1` | Deployable immediately; preflight only mentions "Sturm-Liouville lane" generically |
| **Robin BC FEM fix** (discretization bug corrected) | `book2-open22-4b-fd-robin-fix-v1` | Must use FEM weak formulation, not naive FD |
| **μ-parameter landscape** | `book2-open22-4b-physical-mu-sweep-v1` | Localization parameter space already scanned |
| **L₀/δ "tension resolution"** | commit e7f298f | Exists but depends on r_p [BL]; not true resolution |

### 7.3 Does Anything Change the Recommended Mode?

**No.** The newly found content reinforces Mode B:

1. The prefactor A [Der] formula is **compatible** with Mode B — it provides
   A as a function of L₀/δ, which fits naturally into the functional-relation
   framework L₀/δ = F(R₅/δ, η).

2. The δ-scale ambiguity **strengthens** the case for Mode B — if δ itself is
   uncertain by ×50, claiming L₀/δ = π² is even less justified.

3. The falsified routes (Helfrich, ξ-BC, minimal models) **narrow** the viable
   space without changing the mode.

4. The OPR-21 infrastructure **enables** Mode B implementation more concretely
   than the preflight audit suggested.

---

## 8. Recommendation

### 8.1 Proceed with R1 Mode B — UNCHANGED

The existing recommendation stands. No branch contains a hidden R1 closure
that would upgrade to Mode A (full derivation).

### 8.2 Revisions to Implementation Scope

**ADD to the R1 implementation prompt:**

1. **Import prefactor A formula** from commit e7f298f:
   A = π(ω₀/ω_B)/√(L₀/δ) [Der within 1D model]. This creates a non-circular
   constraint: given L₀/δ, A is predicted, and τ_n = f(L₀/δ) has no free
   prefactor. The R1 appendix should include this.

2. **Acknowledge δ-scale ambiguity** explicitly. The R1 appendix should state
   which δ is used and why, referencing the four-scale taxonomy from
   `delta-audit-anchor-v1`. At minimum: "We use δ ~ 0.1 fm [I] (junction-core
   scale), noting that the EW-scale R_ξ ~ 0.002 fm [P+BL] is 50× smaller.
   The identification δ_nucl ≠ R_ξ is an unresolved assumption."

3. **Use OPR-21 BVP infrastructure** as foundation rather than writing a new
   solver from scratch. The existing code (`opr21_bvp_demo.py`) handles Robin BC,
   eigenvalue extraction, and I₄ computation. Adapt, don't rewrite.

4. **Note falsified routes** in the epistemic table: Helfrich NO-GO, ξ-BC
   no-minimum, flux quantization dead end. These constrain what R1 can invoke.

5. **Do NOT import** the C = (L₀/δ)² = 100 "derivation" as [Dc] — it is circular.
   Reference the *structure* C ∝ (L₀/δ)² as [Dc] but the *value* as [I].

6. **Do NOT import** the tension "resolution" as [Dc] — it depends on r_p [BL].
   Reference the two-context framing as [Dc]+[BL] comparison, not closure.

### 8.3 No Revision to Mode B Exit States

The four exit states from the Phase 1 plan remain:
1. Confirmation — L₀/δ = π² independently derived [Dc]
2. Partial closure — L₀/δ = F(R₅/δ) computed, R₅ choice documented [Dc]+[P]
3. Non-confirmation — cannot achieve π² without extra physics [OPEN]
4. Critical failure — framework inconsistency [Red flag]

Exit state 2 remains the most likely outcome.

---

## 9. Bottom Line

**Nothing found across 40 branches materially changes the R1 preflight
conclusion.** R₅ is never derived. L₀/δ = π² is never derived independently.
All routes remain [P] heuristic.

The strongest new finding is the **prefactor A [Der] formula**, which should
be incorporated. The most important risk factor is the **δ-scale ambiguity**
(factor-50 spread), which should be explicitly acknowledged.

The OPR-21 BVP infrastructure is more mature than the preflight audit suggested
and should be reused rather than rebuilt.

**Recommendation: Proceed with R1 Mode B as planned, with the four scope
additions listed in §8.2.**
