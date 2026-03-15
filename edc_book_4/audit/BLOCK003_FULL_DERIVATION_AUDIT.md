# Systematic Content Audit: Block-003/004 Derivations v1–v67

**Date:** 2026-03-15
**Branch:** `archive/nuclear-topology-discovery`
**Scope:** All 67 derivation versions in `edc_papers/paper_gravity_block003/`
**Method:** Every version read (README, REPORT, ACCEPTANCE, main.tex); no title-only summaries.

---

## Individual Version Summaries

---

### v1 — 5D → 4D Newton Constant (Derivation Attempt v1)
**Problem:** Derive the effective 4D Newton constant G_N from the 5D bulk action.
**Approach:** Linearize 5D Einstein equations; apply Israel junction conditions; solve for static weak-field potential; extract G_N via canonical KK matching. Compact extra dimension and RS warped geometry paths explored.
**Outcome:** PARTIAL
**Key result:** G_N = κ₅²/(6πL) for compact extra dimension; G_N ~ κ₅⁴σ for RS-type. Non-compact gives wrong 1/r² potential.
**Inputs:** 5D EH action [BL], flat background with Λ₅ = 0 [P], Z₂ orbifold [P], brane tension σ [BL], compact L [P].
**Circularity:** CLEAN
**Tag:** Dc / OPEN
**σ/Rξ relevance:** No — σ and R_ξ appear as parameters but EDC values not used.
**Notes:** Sets scaffold for all subsequent versions. EDC scaling exponents 12/13 do not emerge.

---

### v2 — Can R_ξ Serve as the Compactification Scale L?
**Problem:** Whether EDC weak-scale length R_ξ = ℏc/M_Z can serve as compactification scale L.
**Approach:** Substitute L = R_ξ into v1 result; also test L = δ (membrane thickness).
**Outcome:** PARTIAL (INCONCLUSIVE)
**Key result:** G_N = κ₅²/(6πR_ξ) — dimensionally consistent but κ₅² unspecified.
**Inputs:** v1 result [Dc], R_ξ = ℏc/M_Z [I], L = R_ξ [P].
**Circularity:** CLEAN
**Tag:** P / OPEN
**σ/Rξ relevance:** Yes — R_ξ is central proposed input; supplies compactification scale but doesn't fix κ₅².
**Notes:** Missing element sharpened: need κ₅² = f(σ, R_ξ, …).

---

### v3 — Can κ₅² Be Fixed by σ?
**Problem:** Whether 5D gravitational coupling κ₅² can be determined from brane tension σ alone.
**Approach:** Dimensional analysis → κ₅² = C·σ^(-3/4) is unique form. Normalization freedom analyzed.
**Outcome:** PARTIAL (INCONCLUSIVE)
**Key result:** κ₅² = C·σ^(-3/4). Combined: G_N = C·σ^(-3/4)/(6πR_ξ). C cannot be fixed by σ alone.
**Inputs:** σ [BL], dimensional analysis, v1/v2 results.
**Circularity:** CLEAN
**Tag:** Dc / OPEN
**σ/Rξ relevance:** Yes — σ^(-3/4) scaling is main result; bridge equation established.
**Notes:** Proposition 1: rescaling g_AB → λ²g_AB absorbs C. Missing element: fix C.

---

### v4 — Fix Constant C in κ₅² = C·σ^(-3/4)
**Problem:** Whether C can be fixed using EDC-internal principles.
**Approach:** Three attempts (pressure-balance, induced gravity, junction curvature). Formal No-Go Lemma proved.
**Outcome:** NEGATIVE
**Key result:** No-Go Lemma: {σ, ρ_P, R_ξ} with pressure-balance provide only 2 independent scales; fixing C requires 3.
**Inputs:** σ, ρ_P, R_ξ with pressure-balance constraint. G_N^obs excluded.
**Circularity:** CLEAN
**Tag:** Der (No-Go proved formally)
**σ/Rξ relevance:** Yes — σ and R_ξ shown insufficient; proof depends on counting independent scales.
**Notes:** Pivotal version. Need one additional normalization principle beyond {σ, ρ_P, R_ξ}.

---

### v5 — Normalization Principle Choices to Fix C
**Problem:** Document available normalization principles to fix C.
**Approach:** Two paths: NP1 (EDC-internal postulate C = 8π) and NP2 (calibration to G_N^obs).
**Outcome:** PARTIAL (OPTIONS DOCUMENTED)
**Key result:** NP1: C = 8π → G_N predictable [P]. NP2: C from G_N^obs [Cal].
**Inputs:** v4 No-Go, σ, L = R_ξ [P], G_N^obs [Cal for NP2].
**Circularity:** WARNING — NP2 uses G_N^obs (labeled [Cal]).
**Tag:** P / Cal
**σ/Rξ relevance:** Yes — both paths depend on σ.
**Notes:** Decision map, not derivation. NP1 falsifiable; NP2 not.

---

### v6 — Collective Bulk Dimple and Auto-Trapping Threshold
**Problem:** Formalize collective brane deformation by N nucleons; define auto-trapping threshold N*.
**Approach:** Define dimple Ξ_N(r), depth h_N, test-particle energy, N* by ΔE(N*) = 0.
**Outcome:** PARTIAL (OPEN — definitions only)
**Key result:** Operational definition of N* via ΔE(N*) = 0. No quantitative N* prediction.
**Inputs:** 5D EH + brane action [BL], Israel conditions [BL], κ₅² with C unfixed [OPEN].
**Circularity:** CLEAN
**Tag:** OPEN
**σ/Rξ relevance:** Yes — σ enters via κ₅²; both remain symbolic.
**Notes:** Concept-definition document, not result.

---

### v7 — Normalization Candidate Catalog
**Problem:** Survey normalization candidates to fix C; identify best next attempt.
**Approach:** 5 candidates evaluated for circularity risk and viability.
**Outcome:** PARTIAL (CATALOG)
**Key result:** NC-1 (zero-mode KK normalization) identified as best: lowest circularity risk.
**Inputs:** v1–v6 results; No-Go from v4.
**Circularity:** CLEAN
**Tag:** I (assessment)
**σ/Rξ relevance:** Yes — NC-1 needs L (candidate: R_ξ); NC-4 references Z₆.
**Notes:** Motivates v8 (NC-1) and v9 (NC-2).

---

### v8 — NC-1 Attempt: Graviton Zero-Mode Normalization
**Problem:** Fix C using canonical KK graviton zero-mode normalization.
**Approach:** 5D EH → KK zero mode → match to 4D canonical form → extract G_N.
**Outcome:** PARTIAL (INCONCLUSIVE)
**Key result:** G_N = κ₅²/(8πL). C can be absorbed by convention (C = 8π). Missing element shifts to: specify σ numerically.
**Inputs:** 5D EH [BL], KK reduction [BL/Dc], κ₅² = C·σ^(-3/4) [Dc], L = R_ξ [P].
**Circularity:** CLEAN
**Tag:** Dc / OPEN
**σ/Rξ relevance:** Yes — σ appears in final formula; R_ξ used as L.
**Notes:** Problem reframed from "find C" to "derive σ."

---

### v9 — NC-2 Attempt: DGP / Induced Gravity
**Problem:** Test DGP induced gravity as alternative path.
**Approach:** DGP action with brane-localized EH term; compute M₄² from loops; set Λ_UV = σ^(1/4).
**Outcome:** PARTIAL (INCONCLUSIVE)
**Key result:** G_N = 2π/(N·σ^(1/2)). Degeneracy C·σ^(-3/4) replaced by N·σ^(1/2) — unknown relocated from C to N.
**Inputs:** DGP action [BL], Λ_UV = σ^(1/4) [P], N unknown.
**Circularity:** CLEAN
**Tag:** Dc / OPEN
**σ/Rξ relevance:** Yes — σ enters directly.
**Notes:** NC-1 and NC-2 produce isomorphic degeneracies, confirming v4 No-Go.

---

### v10 — Tautology Audit + Order-of-Magnitude Check
**Problem:** Audit whether any G_N "derivation" is tautological; check if EDC is in the right ballpark.
**Approach:** Part A: circularity audit. Part B: set σ ansatz, compute G_N numerically.
**Outcome:** PARTIAL (DIAGNOSTIC)
**Key result:** Part A: MEDIUM tautology risk; problem is underdetermination not tautology. Part B: G_N^obs reproduced by σ^(1/4) ≈ 2 × 10¹³ GeV (GUT scale) — plausible.
**Inputs:** All v1–v9; G_N^obs [Cal for Part B]; R_ξ = (91 GeV)^(-1).
**Circularity:** WARNING (Part B uses G_N^obs as calibration, labeled [Cal]).
**Tag:** Cal / I
**σ/Rξ relevance:** Yes — required σ ~ 10⁵³ GeV⁴; R_ξ = (M_Z)^(-1) used explicitly.
**Notes:** Path forward unambiguous: derive σ from field equations. GUT-scale result is sanity check.

---

### v11 — Derive σ from EDC Field Equations
**Problem:** Whether σ can be derived from EDC-internal field equations without G_N^obs or M_Pl.
**Approach:** Four attempts: Israel junction, Schwinger limit, variational, topological quantization.
**Outcome:** NEGATIVE
**Key result:** No EDC-internal constraint closes σ. Only calibration identities available (σ = ℏc/R_ξ³ or σ = m_ec²/(αr_e²)). ℏ (exact since SI 2019) is metrologically optimal anchor.
**Inputs:** No forbidden inputs used; finding is that σ requires m_e, ℏ, r_e, or α as external anchor.
**Circularity:** CLEAN
**Tag:** NEGATIVE
**σ/Rξ relevance:** Yes — σ is direct subject; conclusion: σ is [BL] calibrated, not [D] derived.
**Notes:** DEPENDENCY_TEST.md: EDC derives ratios (α, m_p/m_e) from geometry but cannot fix absolute scale without one measurement.

---

### v12 — Part I Gravity & Mercury Precession Audit
**Problem:** Forensic audit of how gravity was introduced in EDC Book Part I.
**Approach:** Source-level audit of chapter_7_gravity.tex and chapter_8_river_model.tex.
**Outcome:** NEGATIVE (NO BRIDGE)
**Key result:** Part I's G formula G = ℓ_P²c⁴/(σr_e³) is [I] — uses observed ℓ_P. Mercury precession is consistency check, not prediction. 6 open gaps identified.
**Inputs:** Observed G_N^obs, ℓ_P^obs.
**Circularity:** FAIL — Part I uses G_N^obs and ℓ_P^obs; no 5D→4D reduction attempted.
**Tag:** I (G formula), P (flow ansatz), D+BL (Mercury)
**σ/Rξ relevance:** Yes — G formula contains σ; κ₅² and R_ξ gaps identified.
**Notes:** Bridge map documents 6 open gaps in Part I.

---

### v13 — Weak-Field 5D→4D Matching: The Normalization Extractor
**Problem:** Establish formal mechanism for 4D Newton constant emergence from 5D theory.
**Approach:** KK decomposition of linearized 5D gravity; Sturm-Liouville equation; zero-mode; normalization integral.
**Outcome:** PARTIAL (BRIDGE SLOT FOUND)
**Key result:** M_Pl² = M₅³ × I where I = ∫dξ e^{4A(ξ)}|ψ₀(ξ)|². Flat: I = L. RS-II: I = 1/k.
**Inputs:** 5D EH + GHY boundary term [I from literature]; no G_N used in structural derivation.
**Circularity:** CLEAN
**Tag:** D (normalization extractor), I (5D action from literature), P (warp profile)
**σ/Rξ relevance:** Yes — R_ξ is natural candidate for extra-dimension scale.
**Notes:** Citations: RS (1999), GHY (1977), York (1972).

---

### v14 — EDC Candidates for Warp Profile and Zero-Mode
**Problem:** Whether EDC can determine warp factor A(ξ) and zero-mode profile.
**Approach:** Model A (compact flat, L = R_ξ) and Model B (warped RS-type).
**Outcome:** PARTIAL
**Key result:** Model A: I = R_ξ → G_N = 1/(8πM₅³R_ξ). Model B: I = 1/k. M₅ remains undetermined.
**Inputs:** R_ξ from EDC [Dc]; one external calibration required.
**Circularity:** WARNING for Model B; LOW for Model A.
**Tag:** Dc (Model A preferred)
**σ/Rξ relevance:** Yes — R_ξ identified as compactification length in preferred Model A.
**Notes:** Model A preferred: R_ξ independent of G_N.

---

### v15 — Calibrated Closure with ℓ_P and Error Budget
**Problem:** Execute one-scale calibration closure of BLOCK-003.
**Approach:** Insert M_Pl^obs [BL]; solve M_Pl² = M₅³R_ξ for M₅; error budget.
**Outcome:** PASS (CLOSED — calibrated)
**Key result:** M₅ = M_Pl^{2/3}R_ξ^{-1/3}. R_ξ = (M_Z)^(-1) → M₅ ~ 10¹³ GeV (GUT scale).
**Inputs:** M_Pl^obs [BL], R_ξ [P/Dc].
**Circularity:** CLEAN
**Tag:** D (M₅ formula), BL (M_Pl^obs)
**σ/Rξ relevance:** Yes — R_ξ directly enters; uncertainty dominates error budget.
**Notes:** Open: derive R_ξ from EDC internal dynamics.

---

### v16 — R_ξ Determination: Internal vs Minimal-Baseline
**Problem:** Determine R_ξ internally (Track A) or identify minimal external input (Track B).
**Approach:** Track A: systematic search for R_ξ derivation. Track B: R_ξ = ℏc/M_Z.
**Outcome:** NEGATIVE (Track A) / PASS (Track B)
**Key result:** Track A NO-GO: all five candidates fail. Track B: R_ξ = 2.165 × 10⁻¹⁸ m → M₅ = 2.4 × 10¹³ GeV.
**Inputs:** ℏ (exact), c (exact), M_Z = 91.19 GeV [BL], M_Pl^obs [BL].
**Circularity:** CLEAN for Track B — M_Z independent of G_N.
**Tag:** BL (R_ξ via M_Z), D (M₅ derived)
**σ/Rξ relevance:** Yes — R_ξ = 2.165 × 10⁻¹⁸ m. Track A NO-GO is the fundamental remaining gap.
**Notes:** Full elimination of last [BL] requires deriving M_Z from membrane dynamics.

---

### v17 — EW-Scale Calibration Robustness for R_ξ and M₅
**Problem:** Does choice of EW constant for R_ξ materially change M₅?
**Approach:** Proxy family {M_Z, M_W, v_EW} propagated through full chain.
**Outcome:** PASS (ROBUST)
**Key result:** All three yield GUT-scale M₅. Spread Δlog₁₀(M₅) = 0.162. M_Z justified on metrological grounds.
**Inputs:** M_Z, M_W, v_EW [all BL], M_Pl^obs [BL].
**Circularity:** CLEAN
**Tag:** D (robustness), BL (inputs)
**σ/Rξ relevance:** Yes — R_ξ sensitivity tested; <15% variation.
**Notes:** Closure is proxy-independent at GUT scale.

---

### v18 — Gravity Sector Closure Summary + Reader Contract
**Problem:** Consolidate v13–v17 into reader-grade summary with epistemic labeling.
**Approach:** Synthesis document. Five-step canonical chain. Numerical closure table.
**Outcome:** PASS (CONSOLIDATION)
**Key result:** Chain: M_Pl² = M₅³I [D] → I = R_ξ [Dc] → R_ξ = ℏc/M_Z [I+BL] → M₅ = 2.41 × 10¹³ GeV. δM₅/M₅ = 1.1 × 10⁻⁵.
**Inputs:** M_Pl^obs [BL], M_Z [BL], R_ξ [I].
**Circularity:** CLEAN
**Tag:** I (R_ξ is epistemic weak link)
**σ/Rξ relevance:** Yes — R_ξ tagged [I]+[BL], primary unresolved item.
**Notes:** No new results; consolidation of v13–v17.

---

### v19 — Derivation-First: From 5D Action to 4D Newton Law
**Problem:** Produce self-contained derivation with 35+ displayed equations.
**Approach:** Full sequence: 5D action → Israel → linearized gravity → KK → mode equation → zero-mode → normalization integral → Newton constant → closure.
**Outcome:** PASS (DERIVATION — calibrated closure)
**Key result:** G_N = 1/(8πM₅³R_ξ) with M₅ = 2.41 × 10¹³ GeV. 35+ equations. Non-compact case excluded.
**Inputs:** M_Pl^obs [BL], M_Z [BL], R_ξ = ℏc/M_Z [I+BL].
**Circularity:** CLEAN
**Tag:** D (primary derivation document for gravity sector)
**σ/Rξ relevance:** Yes — R_ξ is compactification scale; [I+BL] status preserved.
**Notes:** Most detailed derivation document in v13–v20 range. 7 pages, 35+ equations.

---

### v20 — Factor & Normalization Audit
**Problem:** Forensic tracking of all numerical pre-factors in 5D→4D bridge.
**Approach:** Factor-by-factor audit; two Planck conventions compared; orbifold factors.
**Outcome:** PASS (AUDIT)
**Key result:** Reduced: M̄_Pl → M₅ = 8.1 × 10¹² GeV. Original: M_Pl → M₅ = 2.4 × 10¹³ GeV. Conversion: (8π)^{1/3} ≈ 2.94.
**Inputs:** M_Z [BL], both Planck conventions.
**Circularity:** CLEAN
**Tag:** Cal (convention audit)
**σ/Rξ relevance:** Yes — R_ξ identification confirmed convention-independent.
**Notes:** Resolves M₅ value confusion (8.1 × 10¹² vs 2.4 × 10¹³: same physics, different conventions).

---

### v21 — KK Mass Gap to R_ξ Identification
**Problem:** Determine compactification scale R_ξ from KK mode spectrum.
**Approach:** Derive KK spectrum m_n = nπ/R_ξ under three BC types; invert with m_gap = M_Z identification.
**Outcome:** PASS
**Key result:** R_ξ = πℏc/M_Z = 6.80 × 10⁻¹⁸ m; M₅ = 4.3 × 10¹² GeV. Factor-of-π shift relative to v15–v20.
**Inputs:** 5D flat metric, v20 conventions, M_Z = 91.19 GeV [BL].
**Circularity:** CLEAN
**Tag:** D (spectral relation), I+BL (numerical R_ξ)
**σ/Rξ relevance:** Yes — R_ξ is central; primary KK-physics derivation route.
**Notes:** Introduces π-factor discrepancy resolved in v22.

---

### v22 — KK Conventions Unification
**Problem:** Resolve π-factor inconsistency between v15–v20 and v21.
**Approach:** Derive KK spectra for three geometries; show equivalence L = πR; declare canonical convention.
**Outcome:** PASS
**Key result:** R_ξ ≡ L (interval length) adopted canonically. R_ξ = πℏc/M_Z = 6.80 × 10⁻¹⁸ m.
**Inputs:** Three geometric setups, prior v20 conventions.
**Circularity:** CLEAN
**Tag:** D (definitional)
**σ/Rξ relevance:** Yes — fixes canonical R_ξ definition.
**Notes:** 10 pages, 63 equations. Convention bookkeeping.

---

### v23 — BLOCK-003 Canonical Closure Packet
**Problem:** Single reviewer-grade document closing 5D→4D Newton constant chain.
**Approach:** Full unbroken derivation sequence with all conventions from v20/v22.
**Outcome:** PASS
**Key result:** R_ξ = 6.80 × 10⁻¹⁸ m; M₅(red) = 5.6 × 10¹² GeV; M₅(orig) = 1.6 × 10¹³ GeV. δM₅/M₅ ≈ 1.1 × 10⁻⁵.
**Inputs:** M_Z [BL], M̄_Pl [BL], v22 canonical convention.
**Circularity:** CLEAN
**Tag:** D (M₅ closure), BL (R_ξ), I+BL (m_gap = M_Z step)
**σ/Rξ relevance:** Yes — R_ξ is pivot of entire chain.
**Notes:** 15 pages, 97 equations. Most comprehensive single document in series.

---

### v24 — Reproducibility & Unit/Convention Audit
**Problem:** Independently verify all v23 numerical values.
**Approach:** Python recompute.py script; cross-check π-map and Planck conversions.
**Outcome:** PASS
**Key result:** All 7 audit checks passed; no numerical discrepancies. π-map verified to < 10⁻¹⁰ relative error.
**Inputs:** Same as v23; script uses no additional inputs.
**Circularity:** CLEAN
**Tag:** Verification (inherits v23 tags)
**σ/Rξ relevance:** Yes — verifies R_ξ to high precision.
**Notes:** Includes recompute.py.

---

### v25 — Alternative Gap Identifications & Proxy Robustness
**Problem:** Why M_Z and not M_W or v_EW as gap proxy?
**Approach:** Proxy family propagated through chain; Δlog₁₀(M₅) computed.
**Outcome:** PASS
**Key result:** Total spread Δlog₁₀(M₅) = 0.162 (< 0.2 decades). Factor spread 1.45. M_Z justified: best precision, gauge-invariant pole mass.
**Inputs:** M_Z, M_W, v_EW [all BL], M̄_Pl [BL].
**Circularity:** CLEAN
**Tag:** I+BL (proxy identifications), D (propagation)
**σ/Rξ relevance:** Yes — R_ξ sensitivity to proxy confirmed within same order of magnitude.
**Notes:** 17 pages, 79 equations.

---

### v26 — Gap Derivability Program
**Problem:** What must EDC provide to derive KK mass gap from first principles?
**Approach:** Brane-localized mass term → Robin BC → transcendental spectral equation.
**Outcome:** PARTIAL
**Key result:** tan(m_nL) = −m_b/m_n [D]; gap bounds π/(2L) < m_gap < π/L [D]. Gap value still [I+BL] because L and m_b both OPEN.
**Inputs:** Bulk 5D action + brane mass term; v22 conventions.
**Circularity:** CLEAN
**Tag:** D (spectral mechanism), OPEN (L and m_b)
**σ/Rξ relevance:** Yes — identifies L and m_b as two open slots for R_ξ derivation.
**Notes:** Program note, not result. 16 pages, 82 equations.

---

### v27 — Brane Mass from Brane Tension (m_b from σ Pinning)
**Problem:** Connect Robin BC parameter m_b to brane tension σ and M₅.
**Approach:** m_b = λσ/M₅³ from dimensional analysis + action. Topological pinning λ = πn proposed.
**Outcome:** PARTIAL
**Key result:** m_b = λσ/M₅³ [Dc]; b = λσL²/M̄_Pl² [Dc]; λ = πn [P].
**Inputs:** v26 framework, brane tension σ, bridge relation.
**Circularity:** CLEAN
**Tag:** D/Dc (scaling), P (topological pinning)
**σ/Rξ relevance:** Yes — σ directly used; b = λσL²/M̄_Pl² makes σ and L the key structural inputs.
**Notes:** 19 pages, 85 equations.

---

### v28 — λ-Pinning from Self-Adjointness + Topological Quantization
**Problem:** Can self-adjointness quantize λ? What topological mechanisms give discrete λ?
**Approach:** SA extension theory; three topological mechanisms (Chern-Simons, axionic, orbifold).
**Outcome:** PARTIAL
**Key result:** SA does NOT quantize b (proven). Topological: λ = c_λ·n, n ∈ Z⁺. Freedom reduced from continuous to discrete.
**Inputs:** Sturm-Liouville theory, Chern-Simons, v26–v27 framework.
**Circularity:** CLEAN
**Tag:** D (SA theory), Dc (CS quantization), P (axionic/orbifold), OPEN (c_λ)
**σ/Rξ relevance:** Yes — σ enters through β = σL²/M̄_Pl².
**Notes:** 19 pages, 100 equations. Key negative: SA alone does NOT quantize b.

---

### v29 — The β Control Parameter
**Problem:** Formally derive and evaluate β = σL²/M̄_Pl².
**Approach:** Two routes: Route A (direct, L open), Route B (with L = πℏc/M_Z identification).
**Outcome:** PASS
**Key result:** β = 4.89 × 10⁻³⁶ (reduced Planck). For all k values, b = λβ ≪ 1 → Neumann regime.
**Inputs:** ℏ, c (exact), M̄_Pl [BL], σ from anchor σL³ = ℏc, M_Z for Route B.
**Circularity:** WARNING (Route B chain flagged but resolved)
**Tag:** BL (Route A), I+BL (Route B), D (algebra)
**σ/Rξ relevance:** Yes — β = σL²/M̄_Pl² is explicitly the σ-R_ξ control parameter.
**Notes:** 18 pages, 91 equations. β ~ 5 × 10⁻³⁶ reflects M_Z/M̄_Pl hierarchy squared.

---

### v30 — Derive or Constrain L from β + λ (No Gap Identification)
**Problem:** Derive L using only β and topological λ, prohibiting gap identification.
**Approach:** Route C (variational: brane tension + Casimir + boundary). Route D (spectral self-consistency).
**Outcome:** PARTIAL (weak closure only)
**Key result:** L = ℏc/(β·M̄_Pl²) [D+BL]; discrete k-branch structure [D+P]; point selection OPEN.
**Inputs:** ℏ, c (exact), M̄_Pl [BL], topological k [P]. NO forbidden inputs.
**Circularity:** CLEAN
**Tag:** D+BL (L formula), P (k-branch), OPEN (point selection)
**σ/Rξ relevance:** Yes — most identification-free attempt to derive L/R_ξ. Internal EDC narrows L to discrete family but cannot select k-branch.
**Notes:** 19 pages, 91 equations. Farthest the series progresses toward internal R_ξ derivation.

---

### v31 — Gauge Sector Normalization, BC Registry, and Scale Regime Map
**Problem:** How does 5D gauge action reduce to 4D effective gauge kinetic term?
**Approach:** KK decomposition of gauge fields; unified BC registry; CS quantization.
**Outcome:** PASS
**Key result:** g₄⁻² = g₅⁻²·I_gauge. For flat: I_gauge = 1. CS level k ∈ Z.
**Inputs:** ℏ, c, π only. No forbidden SM inputs. g₅ tagged [OPEN].
**Circularity:** CLEAN
**Tag:** D (gauge bridge, BC classes, CS quantization)
**σ/Rξ relevance:** No — structural scaffold only.
**Notes:** Program note; strong closure not claimed.

---

### v32 — Unified Gauge BC Breaking + Scale Map
**Problem:** Can SU(5), SO(10), PS, E₆ each produce SM via BC projections?
**Approach:** Explicit orbifold parity matrices; Generator Survival Matrices; algebraic closure proofs.
**Outcome:** PASS
**Key result:** All four tracks yield exactly 12 surviving generators: SU(3)_c × SU(2)_L × U(1)_Y. c_Y = 5/3 [Dc].
**Inputs:** Group-theoretic counts only. No forbidden SM inputs.
**Circularity:** CLEAN
**Tag:** D (BC classes, algebra closure), Dc (c_Y), P (parent group choice)
**σ/Rξ relevance:** No — purely group-theoretic.
**Notes:** Structural closure; point selection remains OPEN.

---

### v33 — Matter + RG Dual-Track Program
**Problem:** How does chirality emerge from 5D BCs? How do couplings run with KK thresholds?
**Approach:** Track M: chiral BC theorem, Yukawa overlap, Hosotani skeleton. Track R: piecewise running with SM beta coefficients.
**Outcome:** PASS
**Key result:** Chiral zero-mode condition [D]; y₄ = y₅·I_overlap [D]; piecewise α_i⁻¹(μ) with μ_KK = π/L [D].
**Inputs:** π, SM beta coefficients b₁ = 41/10, b₂ = −19/6, b₃ = −7 [Dc], N_g = 3, N_H = 1 [Dc].
**Circularity:** WARNING — b_i encode SM content without deriving generation count.
**Tag:** D (fermion BCs, RG), Dc (betas), P (Hosotani), OPEN (anomaly cancellation)
**σ/Rξ relevance:** No — Track R framework will accommodate σ-dependent KK spectra later.
**Notes:** Dual-Track Program Note.

---

### v34 — Fermi Constant from KK Tower Exchange
**Problem:** Derive G_F from 5D→4D KK tower exchange.
**Approach:** KK decompose gauge + fermion fields; compute 4-fermion operator; prove factor of 8; tower convergence via ζ(2).
**Outcome:** PARTIAL
**Key result:** G_F/√2 = Σ(g₄^(n))²/(8m_n²). EDC form: G_F/√2 = g₅²ℏc/(8x₁(b)²βM̄_Pl²)·|I₁|².
**Inputs:** π, ζ(2) [I]. g₅, β, k all open.
**Circularity:** CLEAN — G_F derived, not input.
**Tag:** D (formula structure), OPEN (g₅, β, k)
**σ/Rξ relevance:** Yes — parametric form contains β = σL²/M̄_Pl². First direct link between gravity sector (σ) and SM observable (G_F).
**Notes:** Flat fermion profile gives vanishing coupling to excited modes; need exponential localization.

---

### v35 — GUT BC Survivor Map
**Problem:** Systematic mapping from BC choices to residual 4D gauge group.
**Approach:** Survivor Rule from mode equation; Projector Algebra theorem; all four GUT tracks.
**Outcome:** PASS
**Key result:** Zero-mode exists iff (N,N) or (+,+). All four tracks yield 12 survivors. BC→Breaking Dictionary complete.
**Inputs:** Group-theoretic counts only.
**Circularity:** CLEAN
**Tag:** D (Survivor Rule, Projector Algebra)
**σ/Rξ relevance:** No — purely algebraic.
**Notes:** Minimal, clean. Entire result is algebraic — no numerics needed.

---

### v36 — G_F Numerical Closure Step: g₅ Fixing
**Problem:** Determine g₅ from first principles to close G_F formula.
**Approach:** Three tracks: A (stiffness: g₅² = c_A/M₅), B (topological: g₅² = 2πc_B L/λ), C (self-consistency: g₅² = 4πc_C/Λ₅).
**Outcome:** PARTIAL
**Key result:** Track B: g₄² = 2πc_B/λ (L-independent, quantized). Undetermined coefficients c_A, c_B, c_C remain OPEN.
**Inputs:** π, 2π, 4π. c_A, c_B, c_C undetermined. No forbidden inputs.
**Circularity:** CLEAN
**Tag:** D (dimensional structure), Dc (track formulas), OPEN (coefficients)
**σ/Rξ relevance:** Yes — Track A connects g₅² to σ via M₅.
**Notes:** Three structurally distinct tracks; selection requires additional principle.

---

### v37 — BC Selection Principle Sketch
**Problem:** Can a hierarchical principle narrow infinite BC space to unique selection?
**Approach:** Four-stage pipeline: variational → self-adjointness → topological pinning → vacuum energy minimization.
**Outcome:** PASS
**Key result:** BC selection pipeline: B → B_var → B_SA → B_topo → BC*. Regulator-invariance of ΔE_vac^finite proved.
**Inputs:** π, integers only. Vacuum minimum [OPEN].
**Circularity:** CLEAN
**Tag:** D (pipeline structure, SA verification), Dc/P (topological selector), P (vacuum minimization)
**σ/Rξ relevance:** Yes — prediction hooks link BC selection to G_F and v_EW, both σ-dependent.
**Notes:** Key conceptual paper in v31–v40. Converts BC selection from catalog to principled derivation.

---

### v38 — Hosotani Closure Roadmap
**Problem:** Complete roadmap for deriving EW symmetry breaking from Hosotani mechanism.
**Approach:** Six-stage roadmap: 5D gauge → Wilson line → V_eff(θ) → vacuum → v_EW → m_H.
**Outcome:** PARTIAL
**Key result:** v_EW = (θ*/g₄)√(σ/(βM̄_Pl²)) — cleanest σ-to-observable formula in the series.
**Inputs:** π, integers. g₄ from v36, L from v30 [both OPEN].
**Circularity:** CLEAN — v_EW appears as output, not input.
**Tag:** D (Wilson line, EW scale formula), P (matter content), OPEN (θ*, g₄, L)
**σ/Rξ relevance:** Yes — strong. v_EW = (θ*/g₄)√(σ/(βM̄_Pl²)) directly connects σ to EW scale.
**Notes:** Breaking condition: |V₁| < 4|V₂| with gauge/fermion competition.

---

### v39 — BC Selector Applied to GUT Survivor Map
**Problem:** Integrate BC selection pipeline (v37) with GUT survivor maps (v35) and G_F formula (v34).
**Approach:** Unified operational interface: BC candidates → ΔE_vac scoring → survivor algebra → G_F hook.
**Outcome:** PASS
**Key result:** Unified interface established. Free knobs: β and λ (σ-dependent).
**Inputs:** v34/v35/v36/v37 results. No forbidden inputs.
**Circularity:** CLEAN
**Tag:** D (interface), Dc (free knobs)
**σ/Rξ relevance:** Yes — free knobs catalog lists β = σL²/M̄_Pl².
**Notes:** Integration/stitching layer. Numerical ΔE_vac delegated to v40.

---

### v40 — Numerical ΔE_vac^finite Track Ranking
**Problem:** Compute vacuum energy for all four GUT tracks; produce definitive ranking.
**Approach:** Zeta-function and heat-kernel regularization; Casimir coefficients; finite part proven regulator-independent.
**Outcome:** PARTIAL
**Key result:** ΔE_vac: SU(5) = PS = E₆ = 0 < SO(10) = 3π/(4L). SO(10) disfavored. Three-way tie unresolved.
**Inputs:** BC patterns from v35/v39, Casimir coefficients [BL]. Minimal matter content [P].
**Circularity:** CLEAN
**Tag:** D (ΔE_vac, regulator invariance), BL (Casimir), P (matter), OPEN (tiebreaker)
**σ/Rξ relevance:** Indirect — ΔE_vac ~ π/L depends on L and thus on σ.
**Notes:** SO(10) definitively disfavored. Tiebreaker requires matter sector (v41).

---

### v41 — Matter-Augmented ΔE_vac^finite Ranking
**Problem:** Break three-way tie from v40 using fermion contributions.
**Approach:** Chiral BC fermion contributions added to gauge-sector result.
**Outcome:** PASS
**Key result:** Full ranking: E₆ < PS < SU(5) < SO(10). E₆ wins due to 36 exotic fermions with mixed BCs.
**Inputs:** v40 gauge result [D], v33 chiral BC [D], v37 subtraction protocol [D].
**Circularity:** CLEAN
**Tag:** D
**σ/Rξ relevance:** No — BC counting only.
**Notes:** 23/23 checks. E₆ wins vacuum energy; viability conditional on anomaly and mass gating.

---

### v42 — E₆ Anomaly Audit + Exotics Mass Gating
**Problem:** E₆ won v41 but needs anomaly check and exotic decoupling verification.
**Approach:** Three-stage pipeline: BC selection → anomaly gate → mass gating.
**Outcome:** PARTIAL
**Key result:** E₆ passes anomaly but CONDITIONAL on mass gating. PS CONDITIONAL on hypercharge embedding. SU(5) and SO(10) ADMISSIBLE.
**Inputs:** v41 counts, v37 protocol. No forbidden inputs.
**Circularity:** CLEAN
**Tag:** D/Dc
**σ/Rξ relevance:** Yes — β = σL²/M̄_Pl² enters gating conditions.
**Notes:** PS hypercharge 42 vs 45 Weyl discrepancy left open → v43.

---

### v43 — PS Chirality Closure + Anomaly Gate
**Problem:** Resolve PS 42 vs 45 Weyl discrepancy; prove PS anomaly-free.
**Approach:** PS→SM field decomposition; all six anomaly coefficients computed explicitly.
**Outcome:** PASS
**Key result:** 42→45 resolved: 3 ν_R have mixed BC → no zero-mode. All anomaly sums = 0. PS: CONDITIONAL → PASS.
**Inputs:** PS group, BC assignments from v35.
**Circularity:** CLEAN
**Tag:** D
**σ/Rξ relevance:** No — purely group-theoretic.
**Notes:** Document underwent P44 cleanup pass.

---

### v44 — Anomaly One-Shot SoT Lock
**Problem:** Prevent table drift between LaTeX and Python verification.
**Approach:** Single Source of Truth (SoT) architecture; hash-locked auto-generated tables; rational arithmetic.
**Outcome:** PASS
**Key result:** All anomalies = 0 via exact rational arithmetic. Hash: ea07022b108f0721.
**Inputs:** SM field representations, exact rational hypercharges.
**Circularity:** CLEAN
**Tag:** D (methodology)
**σ/Rξ relevance:** No — pure SM anomaly engineering.
**Notes:** Key contribution is hash-lock protocol preventing LaTeX/Python drift.

---

### v45 — SoT-Lock Track Compiler
**Problem:** Unified track compiler for all four GUT tracks.
**Approach:** Extended SoT to all tracks; computed ΔE_vac scores; admissibility classified.
**Outcome:** PASS
**Key result:** ΔE_vac scores: PS = 25 (rank 1), SU(5) = 32, SO(10) = 49, E₆ = 82. SO(10) and PS = PASS; SU(5) and E₆ = CONDITIONAL.
**Inputs:** v35–v44 results. No forbidden inputs.
**Circularity:** CLEAN
**Tag:** D/Dc
**σ/Rξ relevance:** No — scoring based on BC counting.
**Notes:** 56/56 checks. Scoring formula differs from v41 physical vacuum energy.

---

### v46 — No-Escape Track Selector
**Problem:** Deterministic selection among GUT tracks.
**Approach:** Lexicographic pipeline: hard gates → admissibility → min ΔE_vac → min mechanism burden → max prediction hooks.
**Outcome:** PASS
**Key result:** Selected: **Pati-Salam**. Decision at Stage 2: S_vac(PS) = 25 < S_vac(SO10) = 49.
**Inputs:** v45 SoT_TRACKS (hash-verified).
**Circularity:** CLEAN
**Tag:** D (algorithmic selection)
**σ/Rξ relevance:** No — selection purely from BC counting.
**Notes:** SU(5) and E₆ excluded at Stage 1 by AC-P47-17 rule. Pati-Salam canonical.

---

### v47 — PS Coupling Matching + Weinberg Hook + G_F Readiness
**Problem:** PS→SM coupling matching, structural sin²θ_W hook, G_F readiness map.
**Approach:** Zero-handwave normalization; 1/g_Y² derived from trace audit; two-route verification.
**Outcome:** PASS
**Key result:** 1/g_Y² = 3/(5g_R²) + 4/(5g_{B-L}²) [D]. G_F readiness: 3 blocking items (g₅, L, KK convergence).
**Inputs:** v45/v46 hashes, PS group, trace conventions. No forbidden inputs.
**Circularity:** CLEAN
**Tag:** D (coupling matching), I/D (Weinberg hook)
**σ/Rξ relevance:** Yes — σ is root input in G_F readiness map via L = M̄_Pl√(β/σ).
**Notes:** 38/38 checks. c_R = 3/5, c_{B-L} = 4/5 derived.

---

### v48 — PS G_F Numerical Closure
**Problem:** Close three G_F blocking items from v47.
**Approach:** g₅ via three routes; L = M̄_Pl√(β/σ); KK sum via ζ(2); BKT sensitivity.
**Outcome:** PASS
**Key result:** G_F = (√2/48)g₅²L. All three blockers CLOSED. BKT: < 2% for r_B/L < 0.01.
**Inputs:** σ [P], β [D], M̄_Pl, g₅ via Route A or C [Dc+P]. No forbidden inputs.
**Circularity:** CLEAN
**Tag:** Dc/P — G_F derived given postulated g₅ route.
**σ/Rξ relevance:** Yes — σ is direct root input: L = M̄_Pl√(β/σ).
**Notes:** 49/49 checks. Route B (GUT) flagged CONDITIONAL.

---

### v49 — PS Weinberg Angle Numerical Closure
**Problem:** Close sin²θ_W at KK scale without measured EW inputs.
**Approach:** Four hard rules (Ω1–Ω4); v47 matching coefficients; scheme-invariant thresholds.
**Outcome:** PASS
**Key result:** sin²θ_W(μ*) = 5/12 ≈ 0.4167 at unified KK scale [D]. Parameter-free structural prediction.
**Inputs:** σ, β, M̄_Pl, v47/v48 chain. No M_Z, α_EM.
**Circularity:** CLEAN
**Tag:** D — structural consequence of PS embedding
**σ/Rξ relevance:** Yes — σ enters via L → μ_KK = π/L.
**Notes:** 55/55 checks, 362 equations. sin²θ_W = 5/12 is at KK scale; RG running to IR in v50.

---

### v50 — PS → IR Matching & Physical-Scale Map
**Problem:** Propagate KK-scale predictions to symbolic IR scale via RG.
**Approach:** Matching stack: PS matching → RG running → threshold corrections. Scheme invariance via I = 1/g_Y² − 1/g₂².
**Outcome:** PASS
**Key result:** sin²θ_W(μ_IR) = 5/12 + (b₁−b₂)/(8π²)·(5/12)(7/12)·ln(μ_IR/μ_KK). Scaffold formula.
**Inputs:** σ [P], β [D], M̄_Pl, b₁, b₂ [D/Dc], μ_IR (symbolic). No forbidden inputs.
**Circularity:** CLEAN
**Tag:** D/Dc (RG scaffold)
**σ/Rξ relevance:** Yes — σ is root input throughout; without σ, no numeric prediction possible.
**Notes:** 37/37 checks. End of Block-003 structural derivation for PS path.

---

### v51 — Log Hygiene Lock + Unit-Change Invariance
**Problem:** Ensure all log expressions dimensionless; physical predictions unit-invariant.
**Approach:** Single-reference-scale protocol μ* := π/L; automated scan of 103 log expressions; S-scaling tests.
**Outcome:** PASS
**Key result:** All 103 log arguments dimensionless; S-invariance confirmed across 21 orders of magnitude.
**Inputs:** μ* := π/L, c_R = 3/5, c_{B-L} = 4/5, β, σ [P], SM betas.
**Circularity:** CLEAN
**Tag:** Der/Dc (engineering protocol)
**σ/Rξ relevance:** Yes — σ enters dimensional scaling test via σ ∝ S⁴.
**Notes:** 52/52 checks. Protection layer for all downstream derivations.

---

### v52 — PS Prediction Pack
**Problem:** Consolidate PS track results v47–v51 into auditable prediction pack.
**Approach:** Collect structural predictions; two-route scheme-invariance verification; no-escape ledger.
**Outcome:** PASS
**Key result:** sin²θ_W(μ*) = 5/12 [PREDICTION]; G_F = (√2ζ(2)/48)(g₅²/μ*²L) [PREDICTION]; c_R + c_{B-L} = 7/5 [PREDICTION]; T1 = T2 verified.
**Inputs:** c_R, c_{B-L}, betas [D]; σ [P]; β, λ [D/P]. No M_Z, M_W, v_EW, α_EM, G_N.
**Circularity:** CLEAN
**Tag:** Der
**σ/Rξ relevance:** Yes — all predictions conditional on σ via L.
**Notes:** 61/61 checks. "Prediction framework, not a fit."

---

### v53 — PS Observable Interface Without Contamination
**Problem:** Enable future experimental comparison without contaminating derivation chain.
**Approach:** Two-layer architecture: Layer A (canonical, hash-locked) + Layer B (quarantined placeholders). 8 Observable Interface APIs.
**Outcome:** PASS
**Key result:** 8-API interface; firewall: Layer B cannot modify Layer A. α₃ structure left [OPEN].
**Inputs:** All Layer A from v47–v52; Layer B: symbolic placeholders only.
**Circularity:** CLEAN
**Tag:** Der/I (interface)
**σ/Rξ relevance:** Yes — σ identification [OPEN].
**Notes:** 54/54 checks. "NOT a claim of matching experiment."

---

### v54 — BLOCK-003 Canonical Single Document
**Problem:** Consolidate complete BLOCK-003 chain (v45–v53) into single canonical reference.
**Approach:** Deterministic narrative from track selection through PS canonicalization to EW predictions.
**Outcome:** PASS — BLOCK-003 CLOSED
**Key result:** PS uniquely selected (score = 5); sin²θ_W = 5/12; G_F structural formula; 235 logs scanned — 0 violations; T1 = T2; regulator invariance.
**Inputs:** c_R, c_{B-L} [D]; betas [D]; ζ(2) [U]; μ* = π/L. No M_Z, M_W, v_EW, α_EM, G_N, ℓ_P.
**Circularity:** CLEAN
**Tag:** Der — canonical reference
**σ/Rξ relevance:** Yes — α₃, proton decay, neutrino masses deferred; σ still open.
**Notes:** 83/83 checks. 33 pages. BLOCK-004 flagged as next.

---

### v55 — BLOCK-004 PS → QCD (α₃) Structural Closure
**Problem:** Derive canonical path from PS SU(4)_C to QCD SU(3)_c; establish α₃(μ*).
**Approach:** Embed SU(3)_c ⊂ SU(4)_C; verify trace normalization c_C = 1 (two-route); define α₃(μ*) with 1-loop RG connector.
**Outcome:** PASS
**Key result:** c_C = 1 [D]; α₃(μ*) := g₃²(μ*)/(4π) [D]; RG connector derived. Structural only.
**Inputs:** c_C = 1 [D], c_R, c_{B-L} [D], b₃ = −7 [Dc], μ* = π/L. No α_s(M_Z), M_Z, Λ_MS.
**Circularity:** CLEAN
**Tag:** Der
**σ/Rξ relevance:** Yes — α₃(μ*) conditional on μ* = π/L which depends on σ.
**Notes:** 73/73 checks. Opens BLOCK-004.

---

### v56 — BLOCK-004 α₃(μ*) Numerical Closure
**Problem:** Upgrade α₃ to bounded prediction by fixing g₅^PS.
**Approach:** PS unification hook [P]; Route A (tension/Planck) and Route C (cutoff); Route B (GUT) excluded.
**Outcome:** PASS
**Key result:** **α₃(μ*) = 1/σ̃** [PREDICTION]. σ̃ := M̄_Pl⁴/σ.
**Inputs:** c_C = 1 [D], μ* [canonical], c_A = 4π [Dc+P], β [D]. No α_s(M_Z), G_N.
**Circularity:** CLEAN
**Tag:** P/Der — α₃ = 1/σ̃ depends on postulate for unification hook.
**σ/Rξ relevance:** Yes — **central result**: α₃ = 1/σ̃ where σ̃ = M̄_Pl⁴/σ.
**Notes:** 99/99 checks. Analogous to v48 G_F closure.

---

### v57 — Layer B Adapter (α₃ vs M_Z Comparison)
**Problem:** Enable comparison of α₃ prediction with experimental α_s(M_Z) without contamination.
**Approach:** Layer B B-API1–B-API4; σ̃ swept (not fitted); two-route RG verification.
**Outcome:** PASS
**Key result:** Framework established; firewall intact; no-fit policy enforced.
**Inputs:** Layer A: α₃ = 1/σ̃ (read-only). Layer B [Q]: M_Z, α_s(M_Z), m_t, m_b, etc.
**Circularity:** CLEAN
**Tag:** I (interface)
**σ/Rξ relevance:** Yes — σ̃ is sweep parameter.
**Notes:** 51/51 checks.

---

### v58 — Layer B Λ_QCD Extraction (Two-Route)
**Problem:** Λ_QCD extraction from Layer B with two-route consistency.
**Approach:** Λ₁ (1-loop analytic) vs Λ₂ (numeric/2-loop); threshold policy invariance.
**Outcome:** PASS
**Key result:** |Λ₁ − Λ₂|/Λ₁ < 0.15; threshold invariance < 5%; No Backflow v2 verified.
**Inputs:** Layer A: α₃ = 1/σ̃ (read-only). Layer B [Q]: 10 PDG quantities.
**Circularity:** CLEAN
**Tag:** I/Cal (Layer B only)
**σ/Rξ relevance:** Yes — σ̃ determines α₃ input.
**Notes:** 57/57 checks.

---

### v59 — Formal Λ_QCD Two-Route Extraction (No Handwave)
**Problem:** Replace informal approximations in v58 with fully explicit formulas.
**Approach:** Explicit boxed formulas; Newton solver formally specified; No Backflow v3.
**Outcome:** PASS
**Key result:** Routes Λ₁, Λ₂ explicit with reproducible formulas; Newton solver specified.
**Inputs:** Layer A (read-only), Layer B [Q]: PDG 2024 values.
**Circularity:** CLEAN
**Tag:** I/Cal (formalization of v58)
**σ/Rξ relevance:** Yes — σ̃ sweep drives Λ_QCD extraction.
**Notes:** 75/75 checks. Upgrade from v58 is purely formal.

---

### v60 — BLOCK-004 Canonical Single Document
**Problem:** Consolidate BLOCK-004 (v55–v59) into single canonical reference.
**Approach:** Layer A prediction + Layer B adapter + all invariances + hard policies + status matrix.
**Outcome:** PASS — BLOCK-004 CLOSED (conditional)
**Key result:** Layer A: α₃(μ*) = 1/σ̃ × (1 ± ε) [VERIFIED]. Layer B: RG + Λ extraction [VERIFIED]. No Backflow v3. CLOSED conditional on σ̃.
**Inputs:** Layer A: σ̃, ε ≲ 0.1; Layer B [Q]: PDG 2024.
**Circularity:** CLEAN
**Tag:** Der/I — canonical consolidation
**σ/Rξ relevance:** Yes — **conditional closure depends on σ̃**.
**Notes:** 98/98 checks. 36 pages, 556 labels. Boundary between BLOCK-003 and BLOCK-004.

---

### v61 — BLOCK-004: Proton Decay Program Note (PS)
**Problem:** Structural framework for proton decay within Pati-Salam.
**Approach:** Operator catalog, leptoquark sector, symbolic τ_p formula. Layer A + Layer B architecture.
**Outcome:** PARTIAL (PROGRAM NOTE)
**Key result:** τ_p = 32πM_X⁴/(g_PS⁴|C_CG|²|α_H|²)·m_p³/(m_p² − m_π²)² — symbolic, M_X not supplied.
**Inputs:** PS group [P], generator conventions [Dc], α_H symbolic [P], M_X [P].
**Circularity:** CLEAN
**Tag:** P/OPEN
**σ/Rξ relevance:** No — σ̃ appears only as future input slot.
**Notes:** All 12 reviewer traps passed. OPEN: M_X, α_H, flavor structure.

---

### v62 — BLOCK-004: PS Breaking Scale M_X (Two-Route)
**Problem:** Derive M_X from EDC-internal quantities.
**Approach:** Route A (geometric/topological, C_X = √(4/15)); Route B (EFT matching via α₃ = 1/σ̃). Consistency verified.
**Outcome:** PARTIAL (CONDITIONAL CLOSURE — awaits σ̃)
**Key result:** **M_X = C_X·(π/L)·σ̃^(1/2)** = 0.516·μ*·σ̃^(1/2).
**Inputs:** μ* = π/L [D], α₃ = 1/σ̃ [D], σ̃ [P]. No observed M_X used.
**Circularity:** CLEAN
**Tag:** Der/Dc — formula derived; σ̃ open.
**σ/Rξ relevance:** Yes — σ̃ is central; M_X first becomes function of σ̃ alone.
**Notes:** Allowed range σ̃ ∈ (0.1, 4) for hierarchy consistency.

---

### v63 — BLOCK-004: Proton Decay τ_p Structural Interface
**Problem:** Express τ_p as function of single parameter σ̃.
**Approach:** Import M_X(σ̃) from v62 into v61 formula; substitute g_X ∝ σ̃^(-1/2) from v55.
**Outcome:** PASS (STRUCTURAL INTERFACE)
**Key result:** **τ_p(σ̃) ∝ σ̃⁴**. Extra σ̃² arises because g_X⁴ ∝ σ̃^(-2).
**Inputs:** v62 M_X [D], v55 g_X [D], μ* [D], C_X [D], σ̃ [P], H_p^(sym) [P].
**Circularity:** CLEAN
**Tag:** Der — fully derived modulo σ̃ and H_p.
**σ/Rξ relevance:** Yes — τ_p ∝ σ̃⁴ is central result.
**Notes:** 52/52 checks.

---

### v64 — BLOCK-004: Proton Decay Coupling Lane g_X(M_X)
**Problem:** Close g_X dependency by deriving leptoquark coupling from α₃ chain.
**Approach:** Route T1 (QCD RG) and Route T2 (PS Direct RG); consistency verified.
**Outcome:** PASS
**Key result:** g_X(M_X) = √(4π/σ̃)·(1 ± ε_g). Confirms τ_p = (1/225π²)·μ*⁴σ̃⁴/H_p.
**Inputs:** v55 α₃ [D], v62 M_X [D], b₃ = −7 [D], b_4C template.
**Circularity:** CLEAN
**Tag:** Der/Dc
**σ/Rξ relevance:** Yes — g_X ∝ σ̃^(-1/2).
**Notes:** 104/104 checks.

---

### v65 — BLOCK-004: Proton Decay Canonical Single Document
**Problem:** Consolidate v61–v64 into single firewall-locked canonical reference.
**Approach:** Five canonical boxed results; hash chain v55→v65; five APIs.
**Outcome:** PASS — BLOCK-004 CANONICAL CLOSURE (conditional on σ̃)
**Key result:** BOX-1: color matching; BOX-2: α₃ = 1/σ̃; BOX-3: M_X = C_Xμ*σ̃^(1/2); BOX-4: g_X; BOX-5: τ_p ∝ σ̃⁴.
**Inputs:** Entire v61–v64 chain; σ̃ [P]; H_p [P].
**Circularity:** CLEAN
**Tag:** Der — all locked; numerical conditional on σ̃.
**σ/Rξ relevance:** Yes — σ̃ is single free parameter.
**Notes:** 132 checks, 46 pages, 509 labels. Canonical anchor.

---

### v66 — BLOCK-004: Layer B τ_p(σ̃) Bounds Comparison
**Problem:** Quarantined comparison of τ_p with experimental bounds.
**Approach:** Four B-APIs; σ̃ swept (not fitted); Super-K bound imported; no backflow theorem.
**Outcome:** PASS (Layer B adapter)
**Key result:** σ̃_min from experimental bound; sensitivity ∂ln(τ_p)/∂ln(σ̃) = 4.
**Inputs:** v65 τ_p (read-only); Super-K τ > 2.4 × 10³⁴ yr [Q]; lattice α_H [Q].
**Circularity:** CLEAN — Layer A untouched.
**Tag:** Cal/I (Layer B)
**σ/Rξ relevance:** Yes — first document placing bound on σ̃ from experiment.
**Notes:** 104/104 checks. quarantine/ directory isolates external inputs.

---

### v67 — BLOCK-004: σ̃ Import Contract + Closure Map
**Problem:** Define interface for cosmology lane to deliver σ̃ to BLOCK-004; provide closure map.
**Approach:** Three A-APIs; JSON schema; activation gate state machine; REAL MODE achieved with σ̃ = 100.0 ± 10.0.
**Outcome:** PASS (CONDITIONAL → REAL CLOSURE after σ̃ import)
**Key result:** Complete chain: **α₃ ∝ σ̃⁻¹, M_X ∝ σ̃^(1/2), g_X ∝ σ̃^(-1/2), τ_p ∝ σ̃⁴**. REAL mode with σ̃ = 100.0 ± 10.0 from cosmology lane.
**Inputs:** σ̃ = 100.0 ± 10.0 from EDC-COSMO-TSTAR-5D-ROUTEAB [D after import]; all v55/v62/v64/v65 structural constants.
**Circularity:** CLEAN — σ̃ from cosmology, not reverse-engineered from τ_p.
**Tag:** Der/I — REAL mode verified with SHA256 seal.
**σ/Rξ relevance:** Yes — **termination point of σ̃ chain**; σ̃ = 100.0 closes proton decay program.
**Notes:** 123+ checks. BOOK2_VARIANT_MAP.md: dimensional σ = 8.82 MeV/fm² existed earlier; dimensionless σ̃ derived from cosmology lane later.

---

## Summary Tables

### Table 1: Outcome Distribution

| Outcome | Count | Versions |
|---------|-------|----------|
| **PASS** | 42 | v15–v25, v29, v31–v33, v35, v37, v39, v41, v43–v50, v51–v60, v63–v67 |
| **PARTIAL** | 21 | v1–v3, v5–v9, v13–v14, v26–v28, v30, v34, v36, v38, v40, v42, v61–v62 |
| **NEGATIVE** | 4 | v4 (No-Go Lemma), v11 (σ underivable), v12 (Part I circularity), v16-Track-A (R_ξ underivable) |

**Total: 67 versions.** (v10 classified PARTIAL/diagnostic; v16 has both NEGATIVE Track A and PASS Track B.)

---

### Table 2: Closed Results (Something Was Derived or Constrained)

| Version | What was derived | Tag |
|---------|-----------------|-----|
| v4 | No-Go Lemma: {σ, ρ_P, R_ξ} insufficient to fix C | Der |
| v13 | Normalization extractor: M_Pl² = M₅³·I | D |
| v15 | Calibrated closure: M₅ = M_Pl^{2/3}R_ξ^{-1/3} | D+BL |
| v16-B | R_ξ = ℏc/M_Z = 2.165 × 10⁻¹⁸ m; M₅ = 2.4 × 10¹³ GeV | BL+D |
| v19 | Full 5D→4D derivation with 35+ equations | D |
| v21 | KK spectrum m_n = nπ/R_ξ; R_ξ = πℏc/M_Z | D+I+BL |
| v23 | Canonical closure packet: M₅ = 5.6 × 10¹² GeV (reduced) | D |
| v29 | β = σL²/M̄_Pl² = 4.89 × 10⁻³⁶ | D+BL |
| v32 | All four GUT tracks yield 12 SM generators | D |
| v34 | G_F = Σ(g₄^(n))²/(8m_n²) from KK tower | D |
| v35 | Survivor Rule: zero-mode iff (N,N) BC | D |
| v37 | BC selection pipeline: var → SA → topo → vac | D |
| v40 | SO(10) disfavored by ΔE_vac | D |
| v41 | Full ranking: E₆ < PS < SU(5) < SO(10) | D |
| v43 | PS anomaly-free (all 6 coefficients = 0) | D |
| v46 | **Pati-Salam selected** as canonical track | D |
| v47 | 1/g_Y² = 3/(5g_R²) + 4/(5g_{B-L}²); c_R = 3/5, c_{B-L} = 4/5 | D |
| v48 | G_F = (√2/48)g₅²L structurally closed | Dc/P |
| v49 | **sin²θ_W(μ*) = 5/12** parameter-free prediction | D |
| v54 | BLOCK-003 CLOSED | Der |
| v55 | SU(3)_c ⊂ SU(4)_C with c_C = 1 | D |
| v56 | **α₃(μ*) = 1/σ̃** prediction | P/Der |
| v60 | BLOCK-004 CLOSED (conditional on σ̃) | Der/I |
| v62 | M_X = C_X·μ*·σ̃^(1/2) | Der/Dc |
| v63 | **τ_p ∝ σ̃⁴** | Der |
| v64 | g_X = √(4π/σ̃)·(1 ± ε_g) | Der/Dc |
| v65 | BLOCK-004 canonical: 5 boxed results | Der |
| v67 | σ̃ = 100.0 → REAL CLOSURE | Der/I |

---

### Table 3: Negative Results Worth Preserving

| Version | Failure mode | Why it matters |
|---------|-------------|---------------|
| v4 | No-Go Lemma: {σ, ρ_P, R_ξ} with pressure-balance provide only 2 independent scales; fixing C requires 3. | Proves structural impossibility; all subsequent work respects this constraint. |
| v11 | σ cannot be derived from EDC field equations alone. Four routes (Israel, Schwinger, variational, topological) all fail. Only calibration identities available. | Establishes σ as [BL] baseline, not derivable. EDC derives ratios but cannot fix absolute scale without one measurement. |
| v12 | Part I's G formula is circular: uses ℓ_P^obs. Mercury precession is consistency check, not prediction. Six open gaps in Part I gravity. | Documents exactly what Part I does and does not achieve. Prevents overclaiming. |
| v16-A | All five candidates for internal R_ξ derivation fail. R_ξ cannot be derived from {σ, M̄_Pl, β, λ} without one EW observable. | The fundamental remaining gap in full BLOCK-003 closure. |
| v28 | Self-adjointness does NOT quantize b (Robin parameter). SA provides a 1-parameter family, not discrete selection. | Topological quantization (CS, axionic, orbifold) needed instead of SA alone. |

---

### Table 4: σ and R_ξ Constraint Map

| Version | Target | What was attempted | What was achieved | Constraint |
|---------|--------|-------------------|------------------|-----------|
| v2 | R_ξ | L = R_ξ = ℏc/M_Z | Dimensionally consistent; κ₅² unfixed | R_ξ supplies L but doesn't close G_N |
| v3 | σ | κ₅² = C·σ^(-3/4) | Unique dimensional form | σ provides length scale but C unfixed |
| v4 | σ, R_ξ | Fix C from {σ, ρ_P, R_ξ} | **NO-GO**: only 2 independent scales | Cannot close from these 3 alone |
| v8 | σ | C absorbed by convention → derive σ | Problem reframed | Need σ from field equations |
| v10 | σ | σ required for G_N^obs | σ^(1/4) ≈ 2 × 10¹³ GeV (GUT scale) | Order-of-magnitude [Cal] |
| v11 | σ | Derive σ from EDC field equations | **NEGATIVE**: four routes fail | σ is [BL], not [D] |
| v14 | R_ξ | Model A: I = R_ξ | R_ξ identified as compactification length | R_ξ independent of G_N |
| v16 | R_ξ | Internal derivation (5 candidates) | **Track A NO-GO**; Track B: R_ξ = ℏc/M_Z | R_ξ requires one EW observable |
| v21 | R_ξ | KK spectrum → m_gap = M_Z | R_ξ = πℏc/M_Z [D+I+BL] | Spectral derivation but identification still [I] |
| v27 | σ | m_b = λσ/M₅³ from action | σ enters brane mass via dimensional scaling | σ connected to Robin BC parameter |
| v29 | σ, R_ξ | β = σL²/M̄_Pl² | β = 4.89 × 10⁻³⁶ (with L identified) | Neumann regime for all k |
| v30 | R_ξ | Derive L from β + λ (no gap ID) | L narrowed to discrete k-branches | Point selection still OPEN |
| v34 | σ | G_F parametric form | G_F contains β = σL²/M̄_Pl² | First σ-to-SM-observable link |
| v38 | σ | v_EW from Hosotani | v_EW = (θ*/g₄)√(σ/(βM̄_Pl²)) | Cleanest σ-to-EW formula |
| v48 | σ | G_F closure | G_F = (√2/48)g₅²L with L = M̄_Pl√(β/σ) | σ is root input to G_F |
| v56 | σ | α₃ numerical closure | **α₃ = 1/σ̃** where σ̃ = M̄_Pl⁴/σ | Central prediction; σ̃ is σ in Planck units |
| v62 | σ | M_X from σ̃ | M_X = C_X·μ*·σ̃^(1/2) | M_X depends on σ̃ alone |
| v63 | σ | τ_p from σ̃ | **τ_p ∝ σ̃⁴** | σ̃ controls proton lifetime |
| v67 | σ | σ̃ import from cosmology | **σ̃ = 100.0 ± 10.0** (REAL CLOSURE) | From EDC-COSMO-TSTAR-5D-ROUTEAB |

---

### Table 5: Critical Path to Parameter Closure

Based on the full v1–v67 audit, the following minimal open steps remain:

#### σ (Brane Tension)

| Step | Status | What's needed |
|------|--------|--------------|
| Dimensional σ = 8.82 MeV/fm² | [Cal] from nuclear binding (Book II) | Already available — calibrated, not derived |
| Dimensionless σ̃ = M̄_Pl⁴/σ | [D] from cosmology lane (v67 import) | **ACHIEVED**: σ̃ = 100.0 ± 10.0 via T* derivation |
| σ from EDC field equations alone | [NEGATIVE] (v11) | **NO-GO**: EDC derives ratios, not absolute scales. One measurement required. |

**Current status:** σ is conditionally closed via the cosmology lane (σ̃ = 100 from T* derivation). Full ab initio derivation proved impossible (v11). The metrologically optimal calibration anchor is ℏ (exact since SI 2019).

#### R_ξ (Compactification Scale)

| Step | Status | What's needed |
|------|--------|--------------|
| R_ξ = ℏc/M_Z (or πℏc/M_Z canonical) | [I+BL] | Available via gap identification — one EW measurement |
| Internal derivation from EDC | [NEGATIVE] (v16 Track A, v30 weak closure) | **NO-GO**: all five internal routes fail. v30 narrows to discrete k-branches but cannot select. |
| Derive M_Z from membrane dynamics | [OPEN] | Would eliminate last [BL]; requires new physics (Hosotani θ* from v38) |

**Current status:** R_ξ closed as [I+BL] via M_Z identification. Internal derivation remains NO-GO. The gap is structural: L can be narrowed to discrete family but not uniquely selected without one EW observable.

#### Remaining open items for full ab initio closure

1. **Derive σ from first principles** — proved impossible within current EDC axioms (v11). Would require extending the postulate set.
2. **Derive R_ξ from first principles** — proved impossible without one EW observable (v16-A, v30). Would require computing Hosotani potential V_eff(θ) and solving for θ* (v38 roadmap).
3. **Derive hadronic matrix element α_H** — needed for numerical τ_p. Currently [P] (lattice values available in Layer B).
4. **Derive geometric factor f = √(δ/L₀)** — needed for nuclear pinning model promotion from [I] to [Dc].
5. **Derive coordination prefactor p = 6.1** — needed for nuclear GN law promotion from [Cal] to [D].

#### What IS closed

- **BLOCK-003** (EW sector): sin²θ_W = 5/12, G_F formula, Pati-Salam selected — all structural, conditional on σ.
- **BLOCK-004** (strong sector): α₃ = 1/σ̃, M_X, g_X, τ_p ∝ σ̃⁴ — all derived, conditional on σ̃.
- **REAL CLOSURE**: σ̃ = 100.0 ± 10.0 imported from cosmology lane → all BLOCK-004 outputs close numerically.
- **Gravity sector**: G_N = 1/(8πM₅³R_ξ), M₅ derived — calibrated closure with one EW observable (M_Z).

**Bottom line:** The EDC derivation program v1–v67 achieves structural closure of the electroweak sector, strong sector, and proton decay predictions from a single dimensionless parameter σ̃. Two fundamental NO-GO results (v4/v11 for σ, v16-A for R_ξ) establish that one external measurement is irreducibly required. The cosmology lane provides σ̃ = 100, achieving REAL CLOSURE for BLOCK-004.
