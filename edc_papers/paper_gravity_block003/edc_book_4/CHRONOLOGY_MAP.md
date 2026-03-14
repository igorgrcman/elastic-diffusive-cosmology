# CHRONOLOGY MAP: paper_gravity_block003 (v1-v67)

**Date:** 2026-02-09
**Purpose:** Editorial map of derivation evolution for Book III/IV organization
**Policy:** NO 3D/SM language in canonical text; external model references marked as "Quarantine"

---

## IMPORTANT CLARIFICATION

**This folder (`paper_gravity_block003/`) contains BLOCK-003 and BLOCK-004 material:**
- BLOCK-003 (v1-v54): 5D→4D gravity reduction, GUT track selection, electroweak predictions
- BLOCK-004 (v55-v67): Strong sector, proton decay, σ̃ import

**This is Book III material (Gravity + GUT + Proton Decay), NOT Book IV.**

**Book IV (Nuclear Structure / Topological Pinning) source material is in:**
- `edc_book_2/src/derivations/` (topological pinning, neutron lifetime, α-decay)

---

## CHRONOLOGY TABLE

### BLOCK-003 Part 1: Gravity Foundation (v1-v20)

| v# | Title | Scope | New vs prev | Canonical output | Epistemic impact | Contam |
|:--:|-------|-------|-------------|------------------|------------------|--------|
| 1 | Linearized 5D Einstein + brane-world gravity | Derives G_N = κ₅²/(6πL) from EH action + Israel junction | **First attempt** — baseline brane-world reduction | G_N = κ₅²/(6πL); 1/r recovery | [BL] inputs; [Dc] derivation; [OPEN] G_N | OK |
| 2 | Can R_ξ serve as compactification scale? | Tests L = R_ξ ansatz | Attempts closure: G_N = κ₅²/(6πR_ξ) | G_N = κ₅²/(6πR_ξ) formula | Missing: κ₅² from EDC | OK |
| 3 | κ₅² from brane tension σ | Dimensional analysis | Shows κ₅² = C·σ^(-3/4) unique form, C unfixed | Scaling law κ₅² = C·σ^(-3/4) | [OPEN] σ alone insufficient | OK |
| 4 | No-Go Lemma: fix C from EDC | Tests three closure attempts | 2 EDC scales cannot fix 3-parameter C | No-Go theorem | Narrowed missing element | OK |
| 5 | Normalization principle choices | Catalogs NP1, NP2 paths | [P] vs [Cal] approaches | NP1: C = 8π [P]; NP2: C from G_N^obs [Cal] | Both options documented | OK |
| 6 | Collective dimple + auto-trapping | N* threshold concept | Defines Ξ_N(r), h_N, R_N, ΔE(N), N* | N* = threshold | [OPEN] Definitions only | OK |
| 7 | Normalization candidate catalog | Reviews NC-1 through NC-5 | Evaluates circularity risk | Recommends NC-1 (zero-mode) | NC-1 identified as viable | OK |
| 8 | NC-1 attempt: graviton zero-mode | KK reduction to fix C | Derives G_N formula | G_N = C·σ^(-3/4)/(8πR_ξ) | [P] L = R_ξ; σ unspecified | OK |
| 9 | NC-2 attempt: DGP induced gravity | DGP action test | Relocates unknown to species count N | Induced gravity formula | Degeneracy shifted | OK |
| 10 | Tautology audit + order-of-magnitude | Circularity check; σ₀ test | Confirms MEDIUM risk; σ ≈ 10⁵³ GeV⁴ plausible | Tautology audit | [OPEN] σ derivation missing | OK |
| 11 | Derive σ from EDC field equations | Exhaustive audit + 4 closure attempts | **NO-GO:** σ calibrated, not EDC-internal | NO-GO verdict | [OPEN] σ lacks principle | OK |
| 12 | Part I gravity audit (Mercury) | Back-reference audit | Part I uses G with observed ℓ_P | G = ℓ_P² c⁴/(σ r_e³) is [I]+[P] | Part I import is [I] | OK |
| 13 | Weakfield 5D→4D matching | Normalization extractor | M_Pl² = M₅³ I formula | **Bridge slot:** M_Pl² = M₅³ ∫dξ... | Key insight: formula works | OK |
| 14 | EDC warp candidates (Model A & B) | Two geometries: flat vs warped | Model A: I = R_ξ; Model B: I = 1/k | Model A preferred | Partial bridge | OK |
| 15 | Calibrated closure + error budget | Closes via one-scale [BL] calibration | M₅ = M_Pl^(2/3) R_ξ^(-1/3) | **BLOCK-003 CLOSED (calibrated)** | Standard paradigm | OK |
| 16 | R_ξ determination | Track A NO-GO; Track B CLOSED | R_ξ = ℏc/M_Z = 2.165×10⁻¹⁸ m | M₅ = 2.4×10¹³ GeV (GUT scale) | [BL] identification | OK |
| 17 | EW-scale robustness | Stress-tests with M_Z, M_W, v_EW | All yield M₅ in same decade | **ROBUST:** M_Z canonical | Calibration family stable | OK |
| 18 | Gravity closure summary | Consolidation v13-v17 | Explicit epistemic ledger | **CONSOLIDATED:** M₅ = 2.41×10¹³ GeV | Epistemic transparency | OK |
| 19 | Derivation-first: 5D→4D Newton | Full 35+ equation derivation | Shows all steps | **35+ equations:** full chain | Detailed [D] chain | OK |
| 20 | Factor & normalization audit | Forensic: reduced vs original Planck | Convention difference clarified | M₅^(red) vs M₅^(orig) | Convention resolved | OK |

### BLOCK-003 Part 2: KK Spectrum & Conventions (v21-v30)

| v# | Title | Scope | New vs prev | Canonical output | Epistemic impact | Contam |
|:--:|-------|-------|-------------|------------------|------------------|--------|
| 21 | KK Mass Gap to R_xi | KK spectrum; m_gap = M_Z identification | KK mode equation; m_gap = π/R_xi | R_xi = 6.80×10⁻¹⁸ m [I]+[BL] | Upgrade R_xi to [I]+[BL] | OK |
| 22 | KK Conventions Unification | Resolve π-factor discrepancy | Three KK cases; canonical R_ξ = L | R_ξ ≡ L (interval length) | Single convention | OK |
| 23 | Canonical Closure Packet | Full derivation chain | Both Planck conventions; error budget | M_5 values; δM_5/M_5 = 1.1×10⁻⁵ | Full epistemic ledger | OK |
| 24 | Reproducibility Audit | Python recompute.py verification | All v23 values reproduced | π-map and Planck-map verified | ALL CHECKS PASSED | OK |
| 25 | Alternative Gap Identifications | All EW proxies tested | Three-proxy analysis; robustness metrics | M_5 spread factor ~1.45; GUT scale robust | Robustness proven | OK |
| 26 | Gap Derivability Program | What EDC must provide | Robin BC from variational principle | tan(m_n L) = -m_b/m_n [D] | GDC-1/2/3 program | OK |
| 27 | Brane Mass from Tension | m_b = λσ/M_5³ derivation | Connect m_b to σ; topological pinning | m_b = λσ/M_5³ [Dc]; λ = πn [P] | Upgrade to [Dc] | OK |
| 28 | λ-Pinning from SA Theory | SA extension + topological quantization | SA does NOT quantize b; topology does | λ = c_λ n with discrete c_λ | SA [D]; topology [Dc/P] | OK |
| 29 | β Control Parameter | Dimensionless β = σL²/M̄_Pl² | Two independent routes | β = 4.89×10⁻³⁶; δβ/β = 3.2×10⁻⁵ | Trap-to-equation mapping | OK |
| 30 | L from β + λ (No Gap ID) | Can L be derived without m_gap = M_Z? | Discrete k-branches | Weak closure; strong [OPEN] | No forbidden inputs | OK |

### BLOCK-003 Part 3: Gauge Sector & GUT Tracks (v31-v40)

| v# | Title | Scope | New vs prev | Canonical output | Epistemic impact | Contam |
|:--:|-------|-------|-------------|------------------|------------------|--------|
| 31 | Gauge Sector Normalization | 5D→4D gauge; BC Registry | Gauge bridge g₄⁻² = g_5⁻² I | Unified BC registry | Program note | **Quarantine** |
| 32 | Unified Gauge BC Breaking | 5D parent → SM via BCs | Four tracks (SU(5)/SO(10)/PS/E₆) | 12 SM survivors; c_Y = 5/3 | Structural closure | **Quarantine** |
| 33 | Matter + RG Dual-Track | Fermion BCs; RG framework | Chiral zero-modes; β functions | G_F, RG beta functions | Dual-track structure | **Quarantine** |
| 34 | G_F from KK Tower | Fermi constant via KK exchange | G_F = Σ(g₄⁽ⁿ⁾)²/(8m_n²) | G_F formula [D]; tower convergent | Structural closure | **Quarantine** |
| 35 | GUT BC Survivor Map | BCs select 4D gauge group | Survivor Rule [D]; BC→Breaking dict | 12 SM survivors all tracks | BC→survivor [D] | **Quarantine** |
| 36 | G_F Numerical: g_5 Fixing | Three tracks for g_5 | g_5² = c/M_5 [Dc] variants | Three g_5 tracks [Dc] | Bridge to G_F | **Quarantine** |
| 37 | BC Selection Principle | Hierarchical pipeline | Four-stage selection | BC pipeline B → BC* | Selection framework | **Quarantine** |
| 38 | Hosotani Closure Roadmap | EW breaking + Higgs mass | Wilson line; V_eff; v_EW | v_EW ∝ 1/g_4 L; m_H formula | Roadmap [D] | **Quarantine** |
| 39 | BC Selector Applied | Connect v35 + v37 + v36 | Four GUT tracks scored | BC candidates ranked | Integration | **Quarantine** |
| 40 | ΔE_vac Track Ranking | Vacuum energy ranking | Gauge-only: PS=E₆=SU(5)=0 < SO(10) | Ranking robust [D] | Four-track comparison | **Quarantine** |

### BLOCK-003 Part 4: Track Selection & Closure (v41-v54)

| v# | Title | Scope | New vs prev | Canonical output | Epistemic impact | Contam |
|:--:|-------|-------|-------------|------------------|------------------|--------|
| 41 | Matter-Augmented Ranking | Add fermion contributions | E₆ < PS < SU(5) < SO(10) | Ranking with fermions | Tie broken [D] | OK |
| 42 | E₆ Anomaly Audit | Exotics gating | E₆ PASS anomaly, CONDITIONAL | Track admissibility matrix | E₆ conditional [P] | OK |
| 43 | PS Chirality Closure | PS→SM decomposition | PS CONDITIONAL→PASS | Y = T₃R + (B-L)/2 verified | PS anomalies [D] | OK |
| 44 | Anomaly One-Shot SoT Lock | Hash-locked SoT | All 6 anomalies = 0 | Tables hash-locked | SoT protocol [D] | OK |
| 45 | SoT-Lock Track Compiler | Unified track processing | PS & SO(10) PASS | Track compiler [D] | OK |
| 46 | No-Escape Track Selector | Deterministic selection | **PS uniquely selected** (S_vac=25) | No-escape decision [D] | OK |
| 47 | PS Coupling Matching | PS→SM couplings | 1/g_Y² = 3/5g_R² + 4/5g_{B-L}² | Trace normalization [D] | OK |
| 48 | PS G_F Numerical Closure | Close blocking items | G_F = (√2/48)g_5²L | g_5 routes [Dc]; KK [D] | OK |
| 49 | PS Weinberg Angle Closure | sin²θ_W(μ*) | **sin²θ_W(μ*) = 5/12** | Ω gates [D]; Weinberg [D] | OK |
| 50 | PS → IR Matching | Scale map μ_KK → μ_IR | Scheme-invariant map | Matching scaffold [D] | OK |
| 51 | Log Hygiene Lock | Single μ*=π/L; dimensionless | All 103 logs verified | Log hygiene [D] | OK |
| 52 | PS Prediction Pack | Consolidate v47-v51 | sin²θ_W=5/12, G_F, g_L=g_R | Traceability [D] | OK |
| 53 | Observable Interface | Layer A/B architecture | No-contamination protocol | Hash firewall [D] | OK |
| 54 | BLOCK-003 Canonical | Single document | **BLOCK-003 CLOSED** | 83/83 checks; hash verified | OK |

### BLOCK-004: Strong Sector & Proton Decay (v55-v67)

| v# | Title | Scope | New vs prev | Canonical output | Epistemic impact | Contam |
|:--:|-------|-------|-------------|------------------|------------------|--------|
| 55 | PS → QCD (α₃) Structural | Color matching | **c_C = 1** (two-route) | α₃(μ*) definition | Color matching [D] | OK |
| 56 | α₃(μ*) Numerical | Bounded prediction | **α₃(μ*) = 1/σ̃ × (1±ε)** | PS unification [P] | OK |
| 57 | Layer B Adapter (α₃ vs PDG) | External data adapter | Parameter sweep; no fitting | B-API interface | **Quarantine** |
| 58 | Layer B Λ_QCD Extraction | Two-route Λ_QCD | Λ₁≈Λ₂ verified | Two-route extraction [Dc] | **Quarantine** |
| 59 | Formal Λ_QCD Two-Route | Explicit formulas | Newton solver specified | Formal specification [Dc] | **Quarantine** |
| 60 | BLOCK-004 Canonical | Strong sector canonical | α₃, Λ_QCD; 98/98 checks | Block 004 closure [D] | OK |
| 61 | Proton Decay Program | Operator catalog; lifetime | τ_p ∝ M_X⁴ structure | Operator catalog [D] | OK |
| 62 | PS Breaking Scale M_X | Two-route M_X(σ̃) | **M_X = 0.516·μ*·σ̃^(1/2)** | M_X closure [Dc] | OK |
| 63 | τ_p Structural Interface | v61 + v62 → τ_p(σ̃) | **τ_p ∝ σ̃⁴** | Proton lifetime [D] | OK |
| 64 | g_X(M_X) Coupling Lane | g_X from α₃ chain | **g_X = √(4π/σ̃)** | Coupling absorption [D] | OK |
| 65 | Proton Decay Canonical | Five-box formalism | BOX-1 through BOX-5 | Canonical closure [D] | OK |
| 66 | Layer B τ_p Bounds | Quarantined bounds comparison | B-API interface; no-fit | Layer B bounds [Dc] | **Quarantine** |
| 67 | σ̃ Import Contract | Cosmology → BLOCK-004 interface | **Closure map:** σ̃ → τ_p | Import contract [D] | OK |

---

## MILESTONES

### Milestone 1: v1 — First 5D→4D Derivation
- Establishes baseline brane-world reduction
- G_N = κ₅²/(6πL) formula

### Milestone 2: v11 — σ Derivation NO-GO
- Proves σ cannot be derived from EDC axioms alone
- Definitively identifies missing element

### Milestone 3: v15 — BLOCK-003 Calibrated Closure
- First complete closure with one-scale calibration
- M₅ = M_Pl^(2/3) R_ξ^(-1/3)

### Milestone 4: v23 — Canonical Closure Packet
- Reviewer-grade full derivation chain
- Error budget established

### Milestone 5: v27 — Topological Pinning Introduced
- m_b = λσ/M_5³ connects to brane tension
- λ = πn topological quantization [P]

### Milestone 6: v46 — PS Track Uniquely Selected
- Deterministic no-escape selection
- PS wins over E₆, SO(10), SU(5)

### Milestone 7: v49 — sin²θ_W = 5/12 Closure
- Structural Weinberg angle at KK scale
- All Ω gates satisfied

### Milestone 8: v54 — BLOCK-003 Canonical Closed
- 83/83 checks pass
- Hash chain verified

### Milestone 9: v60 — BLOCK-004 Canonical Closed
- Strong sector closure
- 98/98 checks pass

### Milestone 10: v65 — Proton Decay Five-Box Formalism
- Complete τ_p(σ̃) structure
- BOX-1 through BOX-5 canonical

### Milestone 11: v67 — σ̃ Import Contract
- Interface between cosmology and BLOCK-004
- REAL closure achieved (with σ̃ = 100 ± 10)

---

## CONTAMINATION SUMMARY

| Status | Count | Versions |
|--------|-------|----------|
| **OK** (Clean EDC) | 53 | v1-v30, v41-v56, v60-v65, v67 |
| **Quarantine** (External model language) | 14 | v31-v40, v57-v59, v66 |

**Quarantine content includes:**
- GUT group language (SU(5), SO(10), Pati-Salam, E₆)
- RG beta functions for SM
- External data comparisons (PDG α_s, Super-K τ_p bounds)

**All Quarantine material is in Layer B only, with no backflow to Layer A.**

---

## EDITORIAL WARNINGS

### Warning 1: Convention Ambiguity (v15-v23)
- "Reduced" vs "original" Planck mass conventions
- Resolved in v20, but earlier versions may cause confusion

### Warning 2: R_ξ vs L Notation (v21-v22)
- π-factor discrepancy between early and late versions
- Resolved in v22 with canonical R_ξ ≡ L choice

### Warning 3: λ Status Unclear (v27-v28)
- λ = πn is [P] in some places, [Dc/P] in others
- Needs consistent tagging

### Warning 4: Book III vs Book IV Confusion
- This folder is BLOCK-003/004 = Book III material
- Nuclear/Topological Pinning (Book IV) is in edc_book_2/src/derivations/
