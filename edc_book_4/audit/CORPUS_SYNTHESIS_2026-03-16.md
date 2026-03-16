# Complete Corpus Synthesis — EDC Research Program

**Date:** 2026-03-16
**Scope:** Full audit of both repositories, all 116 branches, ~2500+ files
**Repos:**
- `elastic-diffusive-cosmology` (90 branches, ~727 files on main)
- `EDC_Research` (26 branches, ~1717 files on main)
**Method:** Systematic git-tree traversal, diff analysis, and content extraction

---

## 1. Corpus Overview

### 1.1 Repository Architecture

| Component | Location | Content | Size |
|-----------|----------|---------|------|
| Book I (Core Theory) | `edc_book/` | 13 chapters + 5 appendices | ~200 pages |
| Book II (Weak Sector) | `edc_book_2/` | 18+ chapters + OPR register + audit infrastructure | ~440 pages |
| Book IV (Strong/Nuclear) | `edc_book_4/` | 13 chapters + appendices + derivations + audits | ~230 pages |
| Paper 2 (α derivation) | `edc_papers/paper_2/` | Published paper + supplementary derivations | ~30 pages |
| Paper 3 (Neutron) | `EDC_Research/releases/paper_3_private/` | Neutron lifetime from 5D + Path B | ~50+ pages |
| Block-003 (Gravity) | `edc_papers/paper_gravity_block003/` | 67 derivation versions + cosmology lane | ~2000 pages |
| Python Code | `code/`, `EDC_Research/P7_derivation/` | ~50 scripts, validation, simulations | ~15000 lines |

### 1.2 Date Range

| Phase | Dates | Focus |
|-------|-------|-------|
| Foundation | Pre-2026 | Core theory, 5D action, Book I |
| Paper 2 | ~2025 | α derivation, m_p/m_e = 6π⁵ |
| Paper 3 / Path B | 2026-01-12 to 2026-01-17 | Neutron lifetime, electron soliton |
| Book II development | 2026-01-18 to 2026-01-31 | Weak sector, Z₆, OPR system |
| Book II OPR closure | 2026-01-22 to 2026-01-27 | GF attempts, BVP, notation |
| Audit/Backfill | 2026-01-30 to 2026-01-31 | Gap register (90 entries), donor hunts |
| Book IV (Nuclear) | 2026-03-13 to 2026-03-14 | Topological pinning, 13 chapters |
| Cosmology Lane | 2026-03-15 | σ̃ audit, warped geometry, epistemic correction |
| Proton elastic energy | 2026-03-16 | Prove-or-fail from 5D action |

### 1.3 Research Phases Identified

1. **Genesis** — 5D membrane action, scanning velocity → c, brane topology → charge quantization
2. **Constants** — α⁻¹ = 6π⁵/(4π+5/6), m_p/m_e = 6π⁵ (Paper 2)
3. **Neutron** — Path A (pipeline) vs Path B (instanton) for τ_n (Paper 3)
4. **Weak Sector** — Z₆ → sin²θ_W = 1/4, V−A from chirality, GF attempts (Book II)
5. **Nuclear Topology** — Pinning constant K, coordination lattice M₆, Geiger-Nuttall (Book IV)
6. **Gravity** — G_N from ρ_Plenum, 67 derivation versions, cosmology lane (Block-003)
7. **Meta-Audit** — σ̃ consistency, epistemic corrections, OPR system (current)

---

## 2. Research Methodology

### 2.1 Workflow Pattern

The EDC research follows a distinctive methodology documented in `DIRECTIVES.md` and `EDC_GLOBAL_GUARDS.md`:

1. **Prove-or-Fail format**: Each derivation attempt must explicitly PASS or FAIL. Failures are documented as valuable negative results (e.g., Helfrich NO-GO, taskD bounce NO-GO, warped geometry NEGATIVE).

2. **Branch-per-topic**: Every research task gets its own git branch. Branches are NEVER deleted (forensic archive policy). 116 branches preserve the complete intellectual history.

3. **Epistemic tagging**: Every claim is tagged [Der], [Dc], [I], [Cal], [P], [BL], [M], or [OPEN]. This system was formalized as "Framework v2.0" and enforced throughout.

4. **Anti-circularity enforcement**: Before any derivation, a dependency graph must be drawn. If X→Y→X (circular), work stops. This was explicitly invoked in the warped geometry derivation and the G formula audit.

5. **Ontological purity guards** (`EDC_GLOBAL_GUARDS.md`): Standard Model constructs (gauge groups, SM Lagrangian, QCD, Higgs mechanism) are BANNED as inputs. Only pure mathematics, 5D geometry, and empirical data are allowed.

6. **Stoplight system**: GREEN (derived, <5% error), YELLOW (mechanism identified, OOM agreement), RED (open/failed). Extended to GREEN-A/YELLOW-B/RED-C for GF derivation levels.

7. **OPR Register**: Open Problems Register tracks 30+ items (OPR-01 through OPR-32) with status, dependencies, and blocking relationships.

### 2.2 Documentation Standards

- **Chapter Spine boxes**: Every Book IV chapter has explicit Inputs/Outputs/Dependencies/Forward-links
- **Contamination checks**: Every chapter header declares "Contamination check: PASSED (no SM terms)"
- **Session logs**: `edc_book_2/docs/SESSION_LOG.md` tracks every research session
- **Claim Ledgers**: Machine-parseable databases of all claims with stoplight status
- **Reproducibility packs**: Python scripts + data + requirements.txt for independent verification

### 2.3 Key Methodological Innovations

- **Donor hunt**: Systematic search across all branches for "donor" derivations that could fill gaps in the canonical text
- **Quarantine system**: Content without proper epistemic tags is quarantined until reviewed
- **Provenance seals**: SHA-256 hashes on critical JSON files with one-way data flow contracts
- **No-smuggling checklists**: Explicit verification that no forbidden SM inputs leaked in

---

## 3. Complete Physics Knowledge Map

### 3.1 Fundamental Constants

#### α⁻¹ — Fine Structure Constant

| Attribute | Value |
|-----------|-------|
| **Best result** | α⁻¹ = 6π⁵/(4π + 5/6) ≈ 137.028 |
| **Deviation** | 6.7 ppm from CODATA |
| **Tag** | [Der] |
| **Location** | Book I Ch.6, Paper 2, Book II Ch.2 |
| **Derivation chain** | Brane topology → genus-1 knot → surface tension ratio |
| **19 ppm correction path** | OPR-01 (BVP mode profile) — identified but not computed |
| **Superseded** | Earlier numerical fits in code/ archive scripts |

#### m_p/m_e — Proton-to-Electron Mass Ratio

| Attribute | Value |
|-----------|-------|
| **Best result** | m_p/m_e = 6π⁵ ≈ 1836.12 |
| **Deviation** | 1.8 ppm from CODATA |
| **Tag** | [Der] |
| **Location** | Book I Ch.6, Paper 2 §2.8, Book II Ch.2 |
| **Derivation chain** | Y-junction energy (proton) / genus-1 knot energy (electron) |
| **Key identity** | Vol(B³) × Area(S³) × 3 tubes = (4π/3)(2π²)(3) = 8π³; full: 6π⁵ |
| **Postulates required** | 4: P-σ, P-local-vertex, P-common-origin, P-isotropy |
| **P-isotropy status** | Decomposed into P-U1-phase [Dc] + P-S2-direction [P] (research/topological-pinning branch) |

#### c — Speed of Light

| Attribute | Value |
|-----------|-------|
| **Best result** | c = v_scan (scanning velocity of vibrating brane) |
| **Tag** | [Der] (structural) |
| **Location** | Book I Ch.2 |

#### ℏ — Reduced Planck Constant

| Attribute | Value |
|-----------|-------|
| **Best result** | ℏ = σ_eff · r_e³ / c |
| **Tag** | [Der] (structural) |
| **Location** | Book I Ch.6 |

---

### 3.2 Electroweak Parameters

#### sin²θ_W — Weinberg Angle

| Attribute | Value |
|-----------|-------|
| **Best result** | sin²θ_W = \|Z₂\|/\|Z₆\| = 1/4 (bare), → 0.2314 after RG running |
| **Deviation** | 0.08% from PDG (at M_Z) |
| **Tag** | [Der] (bare), [Dc] (running uses SM beta functions [BL]) |
| **Location** | Book II Ch.3/4, eq:ch3_sin2_bare |
| **Key insight** | Z₆ hexagonal symmetry → Z₂ × Z₃ → coupling ratio = subgroup counting |

#### g² — Weak Coupling Constant

| Attribute | Value |
|-----------|-------|
| **Best result** | g² = 4πα/sin²θ_W = 0.4246 |
| **Deviation** | 1.1% from PDG |
| **Tag** | [Dc] |
| **Location** | Book II Ch.4 |

#### M_W — W Boson Mass

| Attribute | Value |
|-----------|-------|
| **Best result** | M_W = 80.2 GeV |
| **Deviation** | 0.2% from PDG |
| **Tag** | [Dc] |
| **Location** | Book II Ch.4 |

#### M_Z — Z Boson Mass

| Attribute | Value |
|-----------|-------|
| **Best result** | m_Z = (19/2)·m_e/α² ≈ 91.19 GeV |
| **Deviation** | 0.03% |
| **Tag** | [Dc] (Z-scale identification) |
| **Location** | Book I, Block-003 |

#### G_F — Fermi Constant

| Attribute | Value |
|-----------|-------|
| **Best result** | G_F = g²/(4√2 M_W²) — numerical closure |
| **Deviation** | 0.0% (but circular — uses v which depends on G_F) |
| **Tag** | GREEN-A [Dc] (consistency), not GREEN-C [Der] |
| **Location** | Book II Ch.9/11/13 |
| **Circularity** | Acknowledged in DEC-002 — v = (√2 G_F)^{-1/2} is input |
| **First-principles path** | RED-C: requires solving OPR-19 (g₅), OPR-20 (mediator mass), OPR-21 (BVP), OPR-22 (G_eff) |
| **Attempts** | 11+ attempts across part2-gf-* branches (A through H2-plus) |
| **Factor-8 problem** | Persistent factor of 8 discrepancy in mediator mass derivation |
| **Mode overlap** | G_eff = g₅²·ℓ·|f₁(0)|²/(2x₁²) [Dc] — explains "why weak is weak" |

#### V−A Structure

| Attribute | Value |
|-----------|-------|
| **Best result** | V−A emerges from boundary chirality projection |
| **Tag** | [Der] |
| **Location** | Book II Ch.10, eq:ch9_va_projection |
| **Mechanism** | 5D Dirac field + domain wall mass profile → chiral localization |
| **Right-handed currents** | Forbidden by ε-boundary Neumann BC [Der] |

---

### 3.3 Neutron Lifetime

#### τ_n — Book II Pipeline (Path A)

| Attribute | Value |
|-----------|-------|
| **Best result** | τ_n ≈ 830 s |
| **Deviation** | 6% from experiment (879 s) |
| **Tag** | [Dc] |
| **Location** | Book II Ch.4, §4.4 (WKB tunneling) |
| **Mechanism** | Absorption → dissipation → release pipeline |

#### τ_n — Book IV Instanton (Path B)

| Attribute | Value |
|-----------|-------|
| **Best result** | τ_n = A·(ℏ/ω₀)·exp(2π³) ≈ 880 s |
| **Deviation** | < 1% from experiment |
| **Tag** | [Dc]+[P]+[Cal] |
| **Location** | Book IV Ch.6-9 |
| **Derivation chain** | S_EDC → S_eff[q] → V(q) double-well → κ=2π [Dc] × L₀/δ=π² [P] → S_E/ℏ=2π³ → exp(62) |
| **Key postulate** | L₀/δ = π² [P] — physically motivated but not rigorously derived |
| **Prefactor** | A ≈ 0.9 [Cal] — calibrated, not derived |
| **Barrier height** | V_B = 2Δm_np [P] — conjecture from Z₃ barrier geometry |

#### τ_n — NO-GO Results

| Attempt | Branch | Result |
|---------|--------|--------|
| 1D WKB bounce | taskD-bounce-scaling-audit-v1 | B/ℏ = 0.009, need 60.7 → deficit 6800× |
| Helfrich bending | helfrich-well-from-action-v1 | 260 configs, 0 metastable → NO-GO |
| Route D 2D bounce | taskD-bounce-scaling-audit-v1 | NO-GO for (q,Δ) parameter space |

---

### 3.4 Nuclear Physics (Book IV — Topological Pinning)

#### Proton Stability

| Attribute | Value |
|-----------|-------|
| **Best result** | Anchor junction is topological ground state of Z₆ Steiner minimum |
| **Tag** | [Der] (stability), [Dc] (τ_p > 10³⁴ yr) |
| **Location** | Book IV Ch.1, Book II Ch.2 |
| **Mechanism** | π₁ homotopy obstruction prevents decay to trivial sector |

#### Z₆ Symmetry and Subgroup Chain

| Attribute | Value |
|-----------|-------|
| **Best result** | G_jun ≅ Z₆ from hexagonal crystallization |
| **Tag** | [Dc] (crystallization), [Der] (subgroup chain Z₆ ⊃ Z₃ ⊃ Z₂) |
| **Location** | Book IV Ch.2, Book II Ch.3 |
| **Outputs** | Z₃ → 3 generations [Dc]; Z₂ → chirality [Der]; allowed set S = {2ᵃ×3ᵇ} [Der] |

#### Pinning Constant K

| Attribute | Value |
|-----------|-------|
| **Best result** | K = f × σ × A_contact, where A_contact = πδL₀ |
| **Tag** | [Dc]+[I] |
| **Location** | Book IV Ch.4 |
| **Inputs** | σ = 8.82 MeV/fm² [Dc], L₀ = 1 fm [P], δ = 0.105 fm [P] |
| **Geometric factor** | f = √(δ/L₀) [I] |
| **Value** | K ≈ 0.93 MeV → K ≈ 0.74 MeV (variant) |

#### Deuterium Binding (A=2)

| Attribute | Value |
|-----------|-------|
| **Best result** | B_d = 3K ≈ 2.22 MeV |
| **Deviation** | <1% from experiment (2.224 MeV) |
| **Tag** | [Dc] (bond count N=3 within pinning model) |
| **Location** | Book IV Ch.10 |

#### Helium-4 Binding (A=4)

| Attribute | Value |
|-----------|-------|
| **Best result** | B₄ ≈ 28.3 MeV (4-term budget: localization + pinning + surface + closure) |
| **Deviation** | ~0.01 MeV from experiment (28.296 MeV) |
| **Tag** | [Dc]+[P] |
| **Location** | Book IV Ch.11 |
| **Key mechanism** | Closed-4 topology enables collective localization sharing (~70% of binding) |

#### M₆ Coordination Lattice

| Attribute | Value |
|-----------|-------|
| **Best result** | n=6 from Steiner graph duality; allowed set S = {2ᵃ×3ᵇ} |
| **Tag** | [Der] |
| **Location** | Book IV Ch.5 |
| **Prediction** | Forbidden zone [37, 47] — no stable configurations |
| **Verified** | Matches all known stable nuclear configurations |

#### Coordination Frustration and α-Decay Systematics

| Attribute | Value |
|-----------|-------|
| **Best result** | V7.8 M2 frustration-corrected Geiger-Nuttall model |
| **Tag** | [Dc]+[Cal] |
| **Location** | Book IV Ch.13, superheavy_predictions.csv |
| **Improvement** | 7× error reduction vs. baseline GN law |
| **Superheavy predictions** | 3 undiscovered isotopes predicted (Z=119,120) |

---

### 3.5 Gravity

#### Newton's G

| Attribute | Value |
|-----------|-------|
| **Best result** | G = c⁴R_ξ¹²/(128π²σr_e¹³) |
| **Tag** | [Dc] (structural — verified non-circular) |
| **Location** | Book I Ch.7, Block-003 |
| **Key feature** | (R_ξ/r_e)¹² = 10⁻³⁸ explains gauge-gravity hierarchy |
| **Audit** | 128π² found numerically → interpretation (4π)²×8 is post hoc |

#### Schwarzschild and Mercury Precession

| Attribute | Value |
|-----------|-------|
| **Tag** | [Dc] |
| **Location** | Book I Ch.8 (River model) |
| **Python scripts** | edc_mercury_precession_simulator*.py (multiple versions) |

---

### 3.6 Cosmology Lane (σ̃ and Related)

#### σ̃ — Dimensionless Brane Tension

| Attribute | Value |
|-----------|-------|
| **Current status** | σ̃ = 1 from RS geometry + Λ₄ [Dc] |
| **Previous claims** | σ̃ = 100 (RETRACTED — was DERIVED, now CALIBRATED) |
| **Audit** | FOUR incompatible definitions found across v29-v67 (SIGMA_TILDE_DEFINITION_AUDIT.md) |
| **Key correction** | sigma_tilde_value.json: DERIVED → CALIBRATED (commit 8d2bdfa) |
| **NO-GO** | Warped geometry C derivation: C depends on free k=√(-κ₅²Λ₅/6), not determinable |
| **Session 2026-03-16** | σ̃ = 100 fully resolved as artefact; σ̃ = 1 is correct structural value |

#### T_* — Characteristic Tension Scale

| Attribute | Value |
|-----------|-------|
| **Definition** | T_* = C·M₅³ |
| **Tag** | [Dc] (structural form only; C undetermined → [P]+[NEGATIVE]) |
| **Location** | cosmology_sigma_tilde_lane/TSTAR_DERIVATION_5D.md |

#### g₅^(C) — 5D Gauge Coupling (Color)

| Attribute | Value |
|-----------|-------|
| **Status** | Free parameter [P] — irreducible |
| **Root cause** | Gauge kinetic and gravitational sectors are independent |
| **OPR-32** | Opened to track this |
| **Route A** | g₅² = 4π/M₅ → INVALIDATED |
| **Route C** | g₅² = 4π/Λ₅ → INVALIDATED |
| **Resolution** | Accept as one measurement input (α_s(M_Z) = 0.118) |

---

### 3.7 Three Generations

| Attribute | Value |
|-----------|-------|
| **Best result** | N_g = |Z₆/Z₂| = |Z₃| = 3 |
| **Tag** | [Der] (counting), [Dc] (if BVP gives 3 bound states — shape-dependent) |
| **Location** | Book II Ch.6, Book IV Ch.2 |
| **BVP route** | Thick-brane BVP (OPR-21) — if N_bound = 3, provides geometric explanation |
| **μ-window** | Physical domain-wall potential: μ₃ ∈ [13, 17]; toy PT: [15, 18] |

---

### 3.8 Mixing Matrices

#### CKM Matrix

| Attribute | Value |
|-----------|-------|
| **Z₃ DFT baseline** | \|V_ij\|² = 1/3 → FALSIFIED (×144 off from PDG) |
| **Overlap model** | O_ij ∝ exp(−\|Δz\|/2κ) → Wolfenstein λ, λ², λ³ scaling [Dc/P] |
| **Parameter** | Δz/(2κ) = −ln λ ≈ 1.49 [Cal] |
| **CP phase** | Multiple attempts (Z₆ refinement, Jarlskog, phase cancellation theorem) — RED/OPEN |
| **Location** | Book II Ch.8 |

#### PMNS Matrix

| Attribute | Value |
|-----------|-------|
| **Status** | YELLOW — mechanism identified, not closed |
| **Attempts** | 4+ series: symmetry baseline, overlap model, Z₆ discrete-phase, rank-2 baseline |
| **θ₁₂** | arctan(1/√2) = 35.26° [Dc] candidate (attempt 4.2) |
| **θ₂₃** | Success case documented (backfill/pmns-theta23-v1) |
| **θ₁₃** | Reactor perturbation ε [P] |
| **Location** | Book II Ch.7 |

---

### 3.9 Lepton Masses

| Attribute | Value |
|-----------|-------|
| **Electron** | Brane defect (genus-1 knot), golden ratio tail exponent φ = (1+√5)/2 [Dc] |
| **Muon** | Brane-dominant mode relaxation — mass formula candidate [P] |
| **Tau** | Higher-mode excitation — Koide constraint attempted [P] |
| **Location** | Book II Ch.5, Paper 3 (electron soliton work on neutron-pathB-v4/v5 branches) |

#### Golden Ratio Exponent (Electron Soliton)

| Attribute | Value |
|-----------|-------|
| **Result** | f(r) ~ C/r^φ where φ = (1+√5)/2 ≈ 1.618 |
| **Tag** | [Dc] — rigorous proof (universal for any Q=±1 brane soliton) |
| **Location** | EDC_Research/neutron-pathB-v5-electron-soliton-closure |
| **Significance** | Golden ratio emerges from nonlinear brane soliton equation, not imposed |

---

### 3.10 Scale Taxonomy

| Symbol | Name | Value | Status |
|--------|------|-------|--------|
| σ | Membrane tension | 8.82 MeV/fm² | [Dc] (OPR-01 conditional) |
| R_ξ | Diffusion/correlation length | ~2×10⁻³ fm | [P]+[BL] (= ℏc/M_Z) |
| Δ | Kink width | 3.121×10⁻³ fm | [P] (OPR-04) |
| δ | Boundary-layer thickness | ~0.1 fm (junction) or ~10⁻³ fm (transport) | MULTIPLE SCALES — see §3.10.1 |
| ℓ | Domain support | 2πR_ξ ≈ 0.013 fm | [Dc] |
| L₀ | Junction separation | ~1 fm | [P] |
| r_e | Topological defect radius | 2.82 fm | [BL] |

#### 3.10.1 The δ Ambiguity (Critical Finding)

The δ anchor audit (delta-audit-anchor-v1 branch) identified **four distinct thickness-like scales** that are sometimes conflated:

| Symbol | Value | Context | Status |
|--------|-------|---------|--------|
| R_ξ | ~2×10⁻³ fm | Membrane correlation length | [P]+[BL] |
| Δ | 3.121×10⁻³ fm | Electron mass formula | [P] |
| ℓ | 2πR_ξ ≈ 0.013 fm | Orbifold circumference | [Dc] |
| δ | 0.1 fm | Junction core / Put C | [I] — NOT in book |

Three assumption labels track these identifications:
- (A1): Δ = δ — kink width = boundary-layer
- (A2): δ = R_ξ — boundary-layer = diffusion scale
- (A3): ℓ = nΔ with n=O(1) — domain proportional to kink width

**No derivation may silently assume any of (A1)-(A3).**

---

### 3.11 P-Isotropy Decomposition

The monolithic postulate "Plenum has no preferred internal direction" was decomposed into two independent sub-claims (research/topological-pinning branch):

| Sub-claim | Status | Mechanism |
|-----------|--------|-----------|
| P-U1-phase | **[Dc]** (PROMOTED) | Hopf S¹ = ξ compactification = gauge transformation → exact invariance |
| P-S2-direction | **[P]** (remains) | No independent SO(3) source; P-isotropy IS the assertion |

**Net effect:** 6π⁵ derivation retains 4 core postulates (not reducible to 3).

---

## 4. Superseded Results Register

| Result | Old Status | New Status | Reason | Branch |
|--------|-----------|------------|--------|--------|
| σ̃ = 100 as DERIVED | [D] | [Cal] (RETRACTED) | Warped geometry NO-GO; C not a pure number | archive/nuclear-topology-discovery |
| σ̃ = σ/T_* = 100 | [D] | [Cal] | No derivation chain exists; calibrated from α₃=1/σ̃ | archive/nuclear-topology-discovery |
| PHYSICAL_DERIVATION claim | PASS | RETRACTED | TSTAR_DERIVATION_5D gives structural form only | archive/nuclear-topology-discovery |
| Route A: g₅²=4π/M₅ | [Dc] | INVALIDATED | Fails by 7-10 orders of magnitude | claude/analyze-codebase-KKY9n |
| Route C: g₅²=4π/Λ₅ | [Dc] | INVALIDATED | Same failure | claude/analyze-codebase-KKY9n |
| α₃ = 1/σ̃ (as derivation) | [Dc] | ARTEFACT | α₃=1/σ̃ is from failed Route A; does not hold physically | claude/analyze-codebase-KKY9n |
| β = σ̃⁴ (v56) | [Dc] | FALSE | Numerically wrong by ~210 orders of magnitude | archive/nuclear-topology-discovery |
| Z₃ DFT baseline for CKM | [Dc] | FALSIFIED | \|V_ij\|²=1/3, ×144 off from PDG | part2-closurepass-opr-falsified-attempt3 |
| τ_n from 1D WKB bounce | [Dc] | NO-GO | B/ℏ deficit 6800× | taskD-bounce-scaling-audit-v1 |
| Helfrich bending → metastability | [P] | NO-GO | 260 configurations, 0 metastable | helfrich-well-from-action-v1 |
| P-isotropy as single postulate | [P] | Decomposed | P-U1-phase→[Dc], P-S2-direction→[P] | research/topological-pinning-v7_8-integration |
| μ-window "universal" [25,35) | [Dc] | DEPRECATED | Shape-dependent; physical DW: [13,17] | book2-opr21r-mu-window-recalibration-v1 |
| Notation: z vs ξ (5D depth) | Mixed | Resolved | Mapping established; z kept + explicit mapping | part2-notation-mapping-keep-z |

---

## 5. Falsified Results Register

| Approach | Branch | What Failed | Why | Value |
|----------|--------|-------------|-----|-------|
| Helfrich well for metastability | helfrich-well-from-action-v1 | V_bend always positive → no well | No mechanism for negative linear/constant term | Eliminates κ~σδ² route |
| 1D WKB bounce for τ_n | taskD-bounce-scaling-audit-v1 | B/ℏ = 0.009 vs needed 60.7 | Junction-core V(q) too shallow | Need geometric enhancement ~10⁴ |
| Route D: 2D (q,Δ) bounce | taskD-bounce-scaling-audit-v1 | NO-GO | Parameter space exhausted | Multi-channel tunneling unlikely |
| Z₃ DFT for CKM | part2-closurepass-opr-falsified-attempt3 | \|V_ij\|²=1/3 (×144 off) | Z₃ democracy ≠ Wolfenstein hierarchy | Overlap model needed |
| Warped geometry C derivation | archive/nuclear-topology-discovery | C = σκ₅²/(6k) depends on free k | Gauge hierarchy problem | σ̃=100 not derivable |
| 5D geometry P7 (proton model) | EDC_Research P7_derivation | FAILURE CERTIFICATE issued | Volume calculation discrepancy | S³ from spin not physical space |
| σ̃ = 100 from 5D brane world | archive/nuclear-topology-discovery | Three ansätze all FAIL | σ̃~10⁻¹⁸ for C=O(1) | σ̃=100 requires C~10⁻²⁰ |
| v56 β = σ̃⁴ | archive/nuclear-topology-discovery | ~210 orders of magnitude wrong | Dimensional mismatch | DEF-B and DEF-C incompatible |
| Route A/C for g₅ | claude/analyze-codebase-KKY9n | 7-10 OOM wrong | Not physical | g₅ is free parameter |

---

## 6. Research Frontier (State of the Art at Most Recent Commits)

### 6.1 Active Research Directions (March 2026)

| Direction | Latest Branch | Status | Next Step |
|-----------|---------------|--------|-----------|
| Proton elastic energy from 5D | claude/analyze-codebase-KKY9n | In progress | Prove-or-fail from S_EDC |
| σ̃ canonical closure | claude/analyze-codebase-KKY9n | CLOSED | σ̃=1, OPR-31 MOOT, OPR-32 OPENED |
| Part I corrections (F1-F3) | research/topological-pinning-v7_8-integration | Applied | Verify propagation |
| Nuclear topology Book IV | archive/nuclear-topology-discovery | 13 chapters written | Build/publish |

### 6.2 Critical Open Problems

| OPR | Problem | Status | Blocks |
|-----|---------|--------|--------|
| OPR-21 | BVP master closure (V_eff shape) | Shape-dependent | Everything in weak sector |
| OPR-01 | σ from first principles | [Dc] conditional | Sub-ppm α, τ_n robustness |
| L₀/δ=π² | Geometric ratio derivation | [P] | τ_n from [Dc+P+Cal] to [Der] |
| OPR-19 | g₅ from 5D action | Framework only | G_F first-principles |
| OPR-20 | Mediator mass (factor-8 problem) | 11 attempts, persistent | G_F |
| OPR-32 | g₅^(C) is free parameter | OPENED | 1 measurement input needed |

### 6.3 Ledger Summary (Across All Books)

| Tag | Count | Examples |
|-----|-------|---------|
| [Der] | ~12 | α, m_p/m_e, sin²θ_W, V−A, Z₆→S, forbidden zone |
| [Dc] | ~184 | τ_n, G, M_Z, M_W, g², B_d, B_4, ... |
| [P] | ~30 | L₀/δ=π², V_B=2Δm_np, δ identifications, ... |
| [Cal] | ~10 | σ̃=100 (retracted from [D]), prefactor A, frustration coefficient |
| [OPEN] | ~32 | OPR-01 through OPR-32 |
| [FALSIFIED] | ~9 | See §5 |

---

## 7. Overlooked Knowledge

### 7.1 Results in Non-Canonical Branches Deserving Attention

1. **Golden ratio tail exponent** (EDC_Research neutron-pathB-v5): φ=(1+√5)/2 emerges universally from brane soliton equation for Q=±1. This rigorous [Dc] result is on a Paper 3 branch and has NOT been incorporated into Book II or IV. **INTEGRATION IN PROGRESS** — see `GOLDEN_RATIO_INTEGRATION.md`. Present in Paper 3 journal and Companion B publications but absent from monograph series. Source: `boxes_pathB_research_v5/lemma_tail_exponent_robustness.tex` (94-line self-contained proof), `box_pathB_electron_soliton_full_EOM.tex` (full nonlinear EOM), `solve_electron_soliton_bvp_v5.py` (numerical verification).

2. **C = (L₀/δ)² = 100 from junction-core geometry** (junction-core-derive-C-v1): **ASSESSED** — see `JUNCTION_CORE_C100_ASSESSMENT.md`. The geometric insight C ∝ (L₀/δ)² is genuine [Dc], but C = 100 exactly is [I] (depends on L₀=1.0 fm and δ=0.1 fm, both pattern-matched). The derivation document was tuned to reproduce the best-fit answer. **COMPLETELY UNRELATED** to σ̃ = 100 (different physics sectors, zero cross-references). Key finding: if L₀/δ = π² then C = π⁴ ≈ 97 — a pure constant within 3% of 100. Not in canonical text.

3. **Derive Γ₀ from local mode spectrum** (taskC-derive-Gamma0-v1): The prefactor Γ₀ in the tunneling rate was derived [Dc] from local mode spectrum. On a task branch, not in Book IV.

4. **M(q) from 5D action** (taskB-derive-Mq-v1): Effective mass M(q) derived from 5D action dimensional reduction. Status [Dc] with robustness analysis.

5. **δ anchor map** (delta-audit-anchor-v1): Critical finding of 4 distinct δ scales — may not be fully propagated to Book IV which uses δ=0.105 fm.

6. **OPR-21R shape dependence** (book2-opr21r-*): The discovery that μ₃ window is shape-dependent (not universal [25,35)) is critical but on side branches.

7. **α from 5D derivations** (EDC_Research/restructure/paper3-companion-doi-split): "Untracked critical derivation sources" were preserved — α 5D derivations and KK reduction that may contain unpublished results.

8. **Superheavy predictions** (Book IV): 3 undiscovered isotopes (Z=119,120) with specific α-decay predictions. Could be submitted as a standalone prediction paper.

### 7.2 Potential Contradictions

1. **δ values**: Book IV uses δ=0.105 fm (Ch.4) and δ=0.1 fm (junction-core), while Book II OPR system uses δ~2.5×10⁻³ fm (OPR-04). These differ by ~40×. The δ anchor map (§3.10.1) documents this but resolution is incomplete.

2. **σ values**: Book II notation appendix: σ = 5.86 MeV/fm². Book IV Ch.4: σ = 8.82 MeV/fm². Both are [Dc] conditional. The different values may reflect different anchoring assumptions (OPR-01).

3. **σ̃ session log entry** (2026-03-16): States σ̃=1 from RS geometry. But earlier today's correction (archive/nuclear-topology-discovery) retained σ̃=100±10 as [Cal]. The session log entry appears to be from a LATER session that supersedes the earlier correction.

### 7.3 Additional Findings from Deep Branch Analysis (Enrichment Pass)

*Added 2026-03-16 from comprehensive agent analysis of all 116 branches.*

#### 7.3.1 EDC_Research Repo — Key Results Not in Synthesis v1

| Finding | Branch | Tag | Notes |
|---------|--------|-----|-------|
| Z₃ quantization downgrade [Der]→[P] | neutron-pathB-foundation-closure-v1 | [P] | π₃(S¹×S²)=ℤ, not ℤ₃. Factor of 3 requires postulating CS level k=3. Documented in CLAIM_REGISTRY.md |
| WKB No-Go Lemma (KB-LEMMA-001) | main | [Dc] | Multiplicative bridge Γ=A_weak×exp(−B/ℏ) gives τ≥τ_SM>τ_exp. Resolution: additive two-channel Γ_tot=Γ_SM+Γ_EDC |
| Power-law exponent p=5/16 | main (kb/neutron/) | [I] | A_EDC=A₀^{11/16}×Γ_SM^{5/16}. Three candidate mechanisms: Clifford 5/16=D_bulk/dim(Cl₄), boundary GHY, spectral D_eff=16/5. None constitutes derivation |
| R_det=0.63±0.10 | neutron-pathB-foundation-closure-v1 | [Cal] | Gel'fand-Yaglom determinant ratio for WKB prefactor |
| Spin/helicity mapping h₃=h₅×χ | paper3-pathB-edition-v1 | [P] | Reproduces V−A without postulating SU(2)_L. Mapping rule itself is [P] |
| Non-monotonic mechanism r₀>r₂>r₁ | neutron-pathB-next3-exploration | [P] | Z₃ vacuum construction candidates A (piecewise) and B (determinant-sector [OPEN]) |
| Electron mass scale tension ~10⁴ | neutron-pathB-v5-electron-soliton-closure | [OPEN] | Nuclear tension option: σ~100 MeV/fm³, r_c~0.4 fm. Compton option: r_c~386 fm, σ~10⁻⁸ MeV/fm³ |
| Framework Reference Paper (29 pages) | research/neutron-proton-mass-difference-5D | Mixed | 45 claims: 10 [Der], 12 [Dc], 1 [Cal], 7 [I], 8 [P], 7 [OPEN]. Contains m_p/m_e, α, Δm_np, SU(3) |
| Symmetry Ops Companion (28 claims) | main | Mixed | 8 [P], 6 [Dc], 2 [Der], 3 [I], 1 [Cal], 8 [OPEN]. Z₆ factorization, quark windings, ξ-wave |

#### 7.3.2 Repo 1 — Key Findings from Branch Exhaustion

| Finding | Branch | Tag | Notes |
|---------|--------|-----|-------|
| μ-window correction [25,35)→[13,17] | book2-opr21r-* | [Dc] | The oft-cited [25,35) was Pöschl-Teller artifact. Physical domain wall: μ₃∈[13,17]. Changes σΔ³ from [52,102] to [14,24] |
| Minimal-class exhaustion (consolidated) | multiple task branches | [Dc] | ALL S_EH+S_NG mechanisms tested: Israel thin-junction, thick-junction core (monotone), bulk backreaction (κ₅²-suppressed), flat Put C, warped Put C (125 combos), Helfrich (260/260), ξ-BC. ZERO produce double well |
| Book II claim statistics | book2-chapter-audit-v1 | — | 201 total: 12 [Der] COMPLETE, 47 [Dc] PARTIAL, 134 MISSING→OPR assigned |
| junction-core-well-v1 (+72k lines) | junction-core-well-v1 | [Dc] | Most computation-intensive branch. All parameter scans return single-well V(q). LOCAL ONLY — no remote backup |
| 61 local-only branches | multiple | — | Risk: all research on these exists only on one machine. Highest-volume: junction-core-well-v1 (+72k lines) |
| A_sc=π(ω₀/ω_B)/√(L₀/δ) semiclassical prefactor | book-routeC-narrative-cleanup-v1 | [Der within 1D model] | Upgrades A from [Cal] to [Der within model]. A_sc≈0.84 → τ≈24,000s (not 880s). Factor 27 gap |
| OPR-28 G-exponent problem | archive/nuclear-topology-discovery | [I] | Standard KK: G∝R_ξ^{−1}. Part I formula: G∝R_ξ^{+12}. Exponent 12 is [I], not [Der] |
| Neutron-proton mass difference | research/neutron-proton-mass-difference-5D | [Der given Cal] | Δm_np=(8/π)m_e≈1.302 MeV vs 1.293 MeV (0.6%). Requires V₃=−(4/π)m_e [Cal] |

#### 7.3.3 Book IV Deep Dive — Chapter Completion Map

All 17 chapters FILLED. Six parts: A (Topological Foundations, Ch.1-3), B (Pinning Mechanism, Ch.4-5), C (Metastable Lifetime, Ch.6-9), D (Cluster Binding, Ch.10-12), E (Closed-4 Release, Ch.13-15), F (Synthesis, Ch.16-17).

**Metastable lifetime chain closure status:**
- κ=2π: Genuinely closed [Dc]
- V_geom(q) single-well: Genuinely closed [Dc]
- N_bonds=3: Closed within model [Dc within model]
- V(q) double-well: **[P]** — non-geometric terms not derived
- V_B=2Δm_np: **[P]** — E_arm≡Δm_np unverified
- L₀/δ=π²: **[P]** — one candidate in continuous family F(η)
- τ_n≈880s: **[Dc]+[P]+[Cal]** — <1% agreement contingent on both [P] choices

**Five ranked open problems (highest impact first):**
1. Derive V(ξ) from 5D action → uniquely select L₀/δ
2. Derive full V(q) including non-geometric terms
3. Derive well-strength η from first principles
4. Verify E_arm≡Δm_np identification
5. Compute prefactor A from full 5D fluctuation determinant

#### 7.3.4 Paper 3 Architecture (EDC_Research)

Paper 3 has two editions:
- **main.tex** (124 pages): Original pipeline approach
- **main_pathB.tex** (136 pages): Path B brane-soliton perspective

Path B tracks:
- **Track A (Ring Geometry):** WKB prefactor A₀ via Gel'fand-Yaglom
- **Track B (5D Reduction):** Bulk-to-brane output mapping
- **Track C (Electron Soliton):** Q=−1 soliton EOM, energy functional, BVP solutions → **golden ratio φ**
- **Track D (R_det):** Determinant ratio bounds (0.63±0.10 [Cal])

Six restructuring branches exist for journal submission: splitting into separately DOI-able companion papers.

---

## 8. Recommended Actions

### 8.1 Immediate (Within Current Research Cycle)

1. **Reconcile σ̃ across branches**: **COMPLETED** (Step 3 of 9). See `SIGMA_TILDE_SYNC_REPORT.md`. Four incompatible definitions found (DEF-A through DEF-E). Canonical: σ̃ = σ_cov/T_* = 1 at RS fine-tuning (v68). `claude/analyze-codebase-KKY9n` synchronized. `research/topological-pinning` flagged as stale (σ̃ = 100). Archive branches frozen per policy.

2. **Propagate golden ratio result**: The electron soliton f(r)~C/r^φ proof should be incorporated into canonical Book IV or a standalone publication.

3. **Publish superheavy predictions**: The Z=119,120 α-decay predictions are falsifiable and could establish priority.

### 8.2 Near-Term (Next Research Phase)

4. **Close L₀/δ=π²**: This is the single most impactful open problem. If derived, τ_n becomes a genuine prediction.

5. **Resolve δ ambiguity**: The 4 distinct δ scales need a definitive mapping or proof that they are distinct physical quantities.

6. **BVP master closure (OPR-21)**: This is the "master key" that unlocks G_F first-principles, generation counting, and mass spectrum.

### 8.3 Strategic

7. **Write "5 Pillars" summary paper**: α, m_p/m_e, τ_n, sin²θ_W, and coordination structure — each with explicit derivation chain and deviation from experiment. Targets journal publication.

8. **Coordinate notation across all books**: The z/ξ/ζ notation issue and δ/Δ/R_ξ ambiguity need a single canonical reference.

9. **Build automated epistemic tag checker**: Several branches contain tools for this (book2-opr07-repropack-v1, book2-global-symbol-table-v1). Could be made into CI.

---

*Synthesis produced by systematic traversal of 116 branches across 2 repositories. All git branch data verified against `git for-each-ref`, `git diff --name-only`, and `git show` on 2026-03-16. Enrichment pass (§7.3) added from comprehensive agent analysis of all branches including deep dives into EDC_Research (26 branches, Paper 3 + companions), repo1 research/archive/task branches (83+ branches), and Book IV chapters (17 chapters + 8 appendices + 8 derivations).*
