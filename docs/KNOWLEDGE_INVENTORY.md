# EDC KNOWLEDGE INVENTORY

**Created:** 2026-01-28
**Purpose:** Comprehensive catalog of all EDC knowledge, systematized for permanent use
**Scope:** elastic-diffusive-cosmology_repo + EDC_Research_PRIVATE

---

## SECTION 1: CANONICAL DERIVATIONS (GREEN - DERIVED)

These are the strongest, independently derived EDC predictions.

### 1.1 Electroweak Sector

| Result | Formula | Value | PDG | Error | Source |
|--------|---------|-------|-----|-------|--------|
| **Weinberg angle** | sin²(θ_W) = \|Z_2\|/\|Z_6\| = 1/4 | 0.2500 (bare) | 0.2314 (M_Z) | 0.08% after RG | `edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/meta_part2_md/CLAIM_LEDGER.md` CL-3.1 |
| **Three generations** | N_g = \|Z_6/Z_2\| = \|Z_3\| = 3 | 3 | 3 | exact | CLAIM_LEDGER.md CL-5.1 |
| **V-A structure** | Chirality projection at ε-boundary | (1-γ_5) | — | — | CLAIM_LEDGER.md CL-9.1, CL-9.2 |

### 1.2 Mass Ratios

| Result | Formula | Value | Exp | Error | Source |
|--------|---------|-------|-----|-------|--------|
| **m_p/m_e** | Vol(Q)/Vol(B³) = (2π²)³/(4π/3) = 6π⁵ | 1836.118 | 1836.153 | 0.0018% | `edc_book/chapters/chapter_3_confinement.tex`, `edc_papers/paper_2/paper/derivations/EDC_Q_Factorization_From_Action_v1.tex` |
| **α⁻¹** | (4π + 5/6)/6π⁵ | 137.027 | 137.036 | 0.0067% | `edc_papers/paper_2/README.md` |
| **Δm_np** | 8m_e/π | 1.301 MeV | 1.293 MeV | 0.6% | `edc_book_2/src/derivations/EDC_5D_Complete_Mathematical_Framework.md` |

### 1.3 Electroweak Masses (from chapter_9)

| Result | Formula | Value | Exp | Error | Label |
|--------|---------|-------|-----|-------|-------|
| **m_Z** | (19/2) × m_e/α² | 91.19 GeV | 91.19 GeV | 0.03% | `sec:wz_masses` |
| **m_W** | m_Z × √(3/4 + 4α) | 80.38 GeV | 80.38 GeV | 0.11% | `sec:wz_masses` |
| **m_π** | 2 × m_e/α | 139.5 MeV | 139.0 MeV | 0.34% | `sec:pion` |

---

## SECTION 2: DERIVED CONDITIONAL [Dc]

These require specific assumptions to hold.

### 2.1 Membrane Tension

| Result | Formula | Condition | Source |
|--------|---------|-----------|--------|
| **σ** | 2π × R_ξ² × ρ_P | δ ~ R_ξ (membrane thickness) | `edc_papers/paper_2/paper/derivations/EDC_Sigma_From_Pressure_v1.tex` |
| **σ numeric** | m_e³c⁴/(α³ħ²) = 8.82 MeV/fm² | From known m_e, α | `EDC_Research_PRIVATE/kb/turning_points/TP-2026-01-20` |

### 2.2 Fine Structure Constant

| Result | Formula | Condition | Source |
|--------|---------|-----------|--------|
| **α** | r_e/(R_ξ + r_e) | Energy matching principle | `edc_papers/paper_2/paper/derivations/EDC_Alpha_Geometric_Ratio_v1.tex` |
| **R_ξ/r_e** | 136.036 ≈ 1/α - 1 | Pressure balance | RESEARCH_ITERATION_1_Alpha_Derivation.md |

### 2.3 Frozen Criterion

| Result | Routes | Status | Source |
|--------|--------|--------|--------|
| τ_relax >> τ_obs | A: Large-σ instanton barrier; B: Topological superselection | [Dc] (two routes) | `EDC_FROZEN_Criterion_From_Action_v1.tex` |

### 2.4 PMNS Mixing Angles

| Angle | Formula | Value | PDG | Error | Status |
|-------|---------|-------|-----|-------|--------|
| **θ_23** | Z_6 submixing | sin²=0.564 | 0.546 | 3% | [Dc] GREEN |
| **θ_12** | arctan(1/√2) | sin²=0.333 | 0.307 | 8.6% | [Dc] YELLOW |
| **θ_13** | ε = λ/√2 | sin²=0.025 | 0.022 | 15% | [Dc] YELLOW |

---

## SECTION 3: IDENTIFIED [I] (Pattern Matching)

Not uniquely derived; require interpretation.

| Result | Mapping | Error | Source |
|--------|---------|-------|--------|
| **CKM Wolfenstein** | O_ij ~ exp(-\|Δz\|/2κ) | λ calibrated to Cabibbo | CLAIM_LEDGER.md CL-7.2 |
| **Koide Q = 2/3** | \|Z_2\|/\|Z_3\| = 2/3 | 6 ppm | LEPTON_MASS_ATTEMPT_1.md |
| **m_μ/m_e** | (\|Z_3\|/\|Z_2\|) × (1/α) = 205.5 | 0.6% from 206.768 | LEPTON_MASS_ATTEMPT_1.md |

---

## SECTION 4: POSTULATES (7 Foundational)

From `EDC_Research_PRIVATE/kb/assumptions/POSTULATES_MASTER.md`:

| KB-ID | Postulate | Statement |
|-------|-----------|-----------|
| KB-POST-001 | 5D Bulk Manifold | M⁵ = ℝ¹'³ × S¹ |
| KB-POST-002 | Plenum Existence | ρ_P > 0 fills bulk |
| KB-POST-003 | Membrane Existence | Σ⁴ at ξ = 0 |
| KB-POST-004 | Particles as Defects | Topological defects in membrane |
| KB-POST-005 | Positive Pressure | P_bulk > 0 |
| KB-POST-006 | δ-Localization | Φ(x^μ, ξ) = φ(x^μ) δ(ξ) |
| KB-POST-007 | P-Sum | E_p = ∫_Q ε(q) dμ(q), NOT minimum |

---

## SECTION 5: NO-GO RESULTS (What Doesn't Work)

Critical negative results to avoid repeating.

| Attempt | Result | Why Failed | Source |
|---------|--------|------------|--------|
| Pure Z_3 DFT for CKM | \|V_ij\|² = 1/3 | Factor 144 off PDG | CLAIM_LEDGER.md CL-7.1 [FALSIFIED] |
| Z_6 discrete phases for PMNS | Either gauge artifacts or worse fit | Cannot produce asymmetric pattern | OPEN_PROBLEMS_REGISTER.md |
| Wave dispersion for σ | Introduces unknown g | Not clean derivation | RESEARCH_ITERATION_1_Sigma.md |
| Topological route for σ | K = 0 for flat embedding | Requires curved bulk | RESEARCH_ITERATION_1_Sigma.md |
| A_5 as weak mediator | Profile vanishes at boundary | Coupling suppressed | OPR shortlist |
| BC eigenvalue for factor-8 | Max factor-4 with standard BCs | Robin BCs need tuning | OPR |
| Route E/F for energy cascade | Circular dependencies | NO-GO historical | TP-2026-01-28 |

---

## SECTION 6: OPEN PROBLEMS (Priority Ordered)

### Priority 1 (Blocks major claims)

| KB-ID | Problem | Blocking | Status |
|-------|---------|----------|--------|
| OPR-02 | KK tower truncation | N_gen = 3 | RED |
| OPR-21 | Mode profiles f_L(z) from thick-brane BVP | G_F derivation | RED |
| OPR-22 | First-principles G_F | Complete weak sector | RED-C |
| KB-OPEN-033 | Derive V_B from 5D action | τ_n becomes [Der] | PARTIAL |

### Priority 2 (Important)

| KB-ID | Problem | Blocking | Status |
|-------|---------|----------|--------|
| OPR-17 | SU(2)_L gauge embedding | W/Z origin | RED |
| OPR-19 | 5D gauge coupling g_5 | G_F numeric | RED |
| OPR-20 | Mediator mass m_φ | Weak scale | RED |
| KB-OPEN-009 | δS sign derivation | Matter-antimatter → [Der] | PARTIAL |

### Priority 3 (Would be nice)

| KB-ID | Problem | Blocking | Status |
|-------|---------|----------|--------|
| OPR-04 | Absolute neutrino masses | Complete spectrum | YELLOW |
| KB-OPEN-014 | Origin of P_bulk > 0 | Reduce postulate count | OPEN |
| KB-OPEN-015 | Quantitative η prediction | Baryon asymmetry | OPEN |

---

## SECTION 7: KEY DISCOVERIES (2026-01-28)

From session mining (`dmining/projects/`):

### 7.1 M6/Mn Topological Model

**Discovery:** Nuclei follow M_n/M_6 coordination patterns from flux-tube constraints.

- **Constraint:** n = 2^a × 3^b (Y-junction trivalent + quantum doubling)
- **Result:** n = 43 is FORBIDDEN geometrically
- **Verification:** All known magic numbers satisfy constraint
- **Source:** `edc_book_2/src/derivations/m_coordination_full_test.py`

### 7.2 Frustration-Corrected Geiger-Nuttall

**Discovery:** Include geometric frustration in G-N law.

- **Formula:** log₁₀(τ) = A(Z-2)/√Q + B + C × frustration_factor
- **Improvement:** R² = 0.9941 vs 0.6921 (45% better)
- **Source:** `edc_book_2/src/derivations/frustration_geiger_nuttall.py`

### 7.3 Neutron Lifetime from Pure 5D

**Discovery:** τ_n emerges from (σ, L₀, δ) without fitting.

- **Uncalibrated:** τ_n ~ 10³ s
- **Calibrated:** τ_n = 880 s [Cal] with A = 0.8-1.0
- **Source:** `edc_book_2/BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex`

---

## SECTION 8: 3D TRAPS (CRITICAL ANTI-PATTERNS)

From `ANTI_PATTERNS_3D_TRAPS.md`:

| KB-ID | Trap | Wrong | Correct |
|-------|------|-------|---------|
| KB-TRAP-001 | Wrong Volume | 4π/3 (3D) | 2π² (4D) for S³ |
| KB-TRAP-002 | Wrong Surface | 4πr² | 2π²r³ for S³ boundary |
| KB-TRAP-004 | S³ = S² | Confusing hypersphere | S³ ⊂ ℝ⁴, S² ⊂ ℝ³ |
| KB-TRAP-010 | "Obviously 4π" | Assuming 3D solid angle | Must derive from 5D |
| KB-TRAP-014 | Spherical symmetry | Assuming without proof | Verify R >> τ/σ |
| KB-TRAP-015 | Vol ratio = mass ratio | Direct scaling | May have geometric factors |

**GOLDEN RULE:** NEVER trust 3D intuition in 5D calculations.

---

## SECTION 9: FILE LOCATIONS

### Source of Truth

| Content | Location |
|---------|----------|
| Book 1 chapters | `edc_book/chapters/*.tex` |
| Book 2 | `edc_book_2/` |
| Paper 2 derivations | `edc_papers/paper_2/paper/derivations/*.tex` |
| Paper 3 series | `edc_papers/paper_3_series/` |
| Research Private KB | `EDC_Research_PRIVATE/kb/` |
| Turning Points | `EDC_Research_PRIVATE/kb/turning_points/` |

### Key Files

| File | Purpose |
|------|---------|
| `docs/CANON_BUNDLE.md` | All P0 content concatenated |
| `docs/CONCEPT_INDEX.md` | Lookup table for definitions |
| `docs/WORKSPACE_MAP.md` | Navigation guide |
| `edc_book/standards/EDC_RIGOR_STANDARD.md` | Epistemic labeling rules |
| `edc_papers/_shared/style/STYLE_GUIDE.md` | LaTeX style with epistemic tags |

---

## SECTION 10: STATISTICS

### Epistemic Status Counts

| Status | Count | Description |
|--------|-------|-------------|
| [Der] | 9 | Derived from postulates |
| [Dc] | 12+ | Derived conditional |
| [I] | 5+ | Identified/mapped |
| [P] | 7 | Postulates |
| [Cal] | 3+ | Calibrated |
| [BL] | 5+ | Baseline references |
| [M] | 7 | Pure mathematics |
| RED/OPEN | 19+ | Unresolved |
| FALSIFIED | 7+ | Documented failures |

### Document Counts

| Type | Count |
|------|-------|
| .tex derivation files | 80+ |
| .md documentation | 100+ |
| KB entries | 120+ |
| Companions (Paper 3) | 9 |

---

## SECTION 11: VERIFICATION CHECKLIST

Before claiming anything:

1. [ ] Check CONCEPT_INDEX.md for existing definition
2. [ ] Check ANTI_PATTERNS_3D_TRAPS.md for known errors
3. [ ] Verify epistemic tag is correct
4. [ ] Check for circularity in derivation chain
5. [ ] Cross-reference with existing sources
6. [ ] Update KNOWLEDGE_INVENTORY if new discovery

---

*This inventory is the permanent record of EDC project knowledge as of 2026-01-28.*
