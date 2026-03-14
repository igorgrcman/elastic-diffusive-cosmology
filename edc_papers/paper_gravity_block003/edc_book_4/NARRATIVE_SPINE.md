# NARRATIVE SPINE: Book Organization

**Date:** 2026-02-09
**Purpose:** Map source material to book chapters; distinguish Book III vs Book IV

---

## CRITICAL CLARIFICATION: TWO SEPARATE BOOKS

### Book III: Gravity + GUT + Proton Decay
**Source:** `paper_gravity_block003/derivation_v1-v67/`
**Content:**
- 5D→4D gravity reduction (v1-v20)
- KK spectrum, conventions (v21-v30)
- GUT track selection, PS canonicalization (v31-v54)
- Strong sector α₃, proton decay τ_p(σ̃) (v55-v67)

### Book IV: Nuclear Structure + Topological Pinning
**Source:** `edc_book_2/src/derivations/`
**Content:**
- Topological pinning model (σ → K)
- M6 coordination lattice
- Neutron lifetime (τ_n = 880 s)
- Nuclear binding (d, He-4)
- Alpha decay (coordination frustration)
- Superheavy predictions

---

## BOOK IV NARRATIVE SPINE (Nuclear/Topological Pinning)

### Source Files in `edc_book_2/src/derivations/`

| File | Type | Topic |
|------|------|-------|
| M6_MODEL_SUMMARY.md | Summary | Topological pinning overview |
| M6_PINNING_CONSTANT_DERIVATION.md | Derivation | K = f × σ × A_contact |
| M6_K_RIGOROUS_DERIVATION.md | Derivation | K from contact geometry |
| M6_GEOMETRY_DERIVATION.md | Derivation | M6 lattice structure |
| M6_TOPOLOGICAL_MODEL_EXPLORATION.md | Exploration | Model development |
| M6_HELIUM4_ANALYSIS.md | Analysis | He-4 binding energy |
| M6_Li6_Be8_ANALYSIS.md | Analysis | Light nuclei |
| M6_SENSITIVITY_REPORT.md | Verification | Sensitivity analysis |
| M6_EXTENDED_ANALYSIS_REPORT.md | Verification | Extended checks |
| INSTANTON_DERIVATION_CHAIN.md | Derivation | τ_n instanton formula |
| DERIVE_KAPPA_FROM_5D_HOMOTOPY.md | Derivation | κ = 2π from π₁(S¹) |
| DERIVE_L0_DELTA_PI_SQUARED.md | Derivation | L₀/δ ≈ π² hypothesis |
| DERIVE_L0_DELTA_PI_SQUARED_V2.md | Derivation | Alternate derivation |
| DERIVE_L0_RP_MAP.md | Derivation | L₀ ↔ r_p mapping |
| DERIVE_L0_RP_FROM_5D_ELECTROSTATICS.md | Derivation | Electrostatic approach |
| DERIVE_PREFACTOR_A.md | Derivation | Instanton prefactor |
| DERIVE_OMEGA0_FROM_5D.md | Derivation | ω₀ from 5D |
| DERIVE_M_EQUALS_MP.md | Derivation | M = M_P identification |
| DERIVE_FOUR_THIRDS_FACTOR.md | Derivation | 4/3 factor origin |
| NEUTRON_LIFETIME_NARRATIVE_SYNTHESIS.md | Narrative | Complete τ_n story |
| SESSION_LOG_NEUTRON_LIFETIME.md | Log | Research session |
| Z3_SYMMETRY_ANALYSIS_NEUTRON.md | Analysis | Z₃ symmetry of neutron |
| V_B_FROM_Z3_BARRIER_CONJECTURE.md | Conjecture | V_B = 2×Δm_np |
| S5D_TO_SEFF_Q_REDUCTION.md | Derivation | 5D→1D reduction |
| ROUTE_F_STATUS_BOX.md | Status | Kramers escape status |
| EPISTEMIC_CORRECTION_L0_MAP.md | Correction | L₀ map correction |

### Python Scripts in `edc_book_2/src/derivations/code/`

| File | Purpose |
|------|---------|
| superheavy_predictions.py | α-decay predictions for Z ≥ 114 |
| kramers_double_well_v2.py | Langevin escape simulations |
| delta_m_np_options.py | Δm_np calculation options |
| prefactor_sensitivity_full.py | Prefactor sensitivity |
| prefactor_refit_cv.py | Cross-validation refit |
| superheavy_oos_test.py | Out-of-sample testing |

### LaTeX Files

| File | Purpose |
|------|---------|
| TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex | Standalone monograph |
| BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex | Book chapter section |
| compile_topological_pinning.tex | Compilation driver |
| topological_pinning_standalone_UPDATED_v3.tex | Updated standalone |
| compile_neutron_section.tex | Neutron section driver |

---

## BOOK IV CHAPTER → SOURCE MAPPING

### PART A: TOPOLOGICAL FOUNDATIONS

**Chapter 1: Proton as Topological Ground State**
- Source of truth: `04b_proton_anchor.tex` (in edc_book_2/src/sections/)
- Steiner geometry: `04c_routeB_z6_steiner.tex`
- Excluded duplicates: None
- Quarantine hooks: None
- Open items: Hessian proof needs formalization

**Chapter 2: Junction Symmetries (Z₆)**
- Source of truth: `04c_routeB_z6_steiner.tex`
- Z₆ crystallization: `M6_GEOMETRY_DERIVATION.md`
- Excluded duplicates: Fermion/generation content (goes to Book II)
- Quarantine hooks: Any SM gauge language
- Open items: Z₆ → Z₃ breaking mechanism

**Chapter 3: Neutron as Metastable State**
- Source of truth: `05b_neutron_dual_route.tex`, `Z3_SYMMETRY_ANALYSIS_NEUTRON.md`
- Double-well: `V_B_FROM_Z3_BARRIER_CONJECTURE.md`
- Excluded duplicates: SM weak decay language
- Quarantine hooks: Fermi theory language
- Open items: V(q) shape from 5D

### PART B: PINNING MECHANISM

**Chapter 4: From σ to K**
- Source of truth: `M6_PINNING_CONSTANT_DERIVATION.md`, `M6_K_RIGOROUS_DERIVATION.md`
- Contact geometry: derivation in M6_K_RIGOROUS_DERIVATION.md
- Excluded duplicates: M6_MODEL_SUMMARY.md (summary, not source)
- Quarantine hooks: None
- Open items: f factor derivation from 5D

**Chapter 5: M6 Coordination Lattice**
- Source of truth: `M6_GEOMETRY_DERIVATION.md`, `M6_TOPOLOGICAL_MODEL_EXPLORATION.md`
- Allowed n: superheavy_predictions.py (generate_allowed_n function)
- Excluded duplicates: None
- Quarantine hooks: "Magic numbers" as SM nuclear physics
- Open items: Forbidden zone derivation

### PART C: NEUTRON LIFETIME

**Chapter 6: Instanton Derivation**
- Source of truth: `INSTANTON_DERIVATION_CHAIN.md`
- S_E formula: derivation in source
- Excluded duplicates: Earlier versions in SESSION_LOG
- Quarantine hooks: None
- Open items: Prefactor A derivation

**Chapter 7: κ = 2π from Homotopy**
- Source of truth: `DERIVE_KAPPA_FROM_5D_HOMOTOPY.md`
- π₁(S¹) = ℤ: standard topology [M]
- Excluded duplicates: None
- Quarantine hooks: None
- Open items: S¹ topology assumption [P]

**Chapter 8: L₀/δ Scale Ratio**
- Source of truth: `DERIVE_L0_DELTA_PI_SQUARED.md`, `DERIVE_L0_DELTA_PI_SQUARED_V2.md`
- π² hypothesis: [P] status
- Excluded duplicates: V2 supersedes V1 where different
- Quarantine hooks: None
- Open items: Rigorous derivation from 5D

**Chapter 9: τ_n = 880 s Prediction**
- Source of truth: `NEUTRON_LIFETIME_NARRATIVE_SYNTHESIS.md`
- Numerical: values from narrative synthesis
- Kramers cross-check: kramers_double_well_v2.py
- Excluded duplicates: SESSION_LOG (development, not canonical)
- Quarantine hooks: None
- Open items: Uncertainty propagation

### PART D: NUCLEAR BINDING

**Chapter 10: Deuterium**
- Source of truth: `M6_MODEL_SUMMARY.md` §Deuterium
- B.E. = 3K: simple formula
- Excluded duplicates: None
- Quarantine hooks: None
- Open items: Why 3 effective bonds?

**Chapter 11: Helium-4**
- Source of truth: `M6_HELIUM4_ANALYSIS.md`
- Four contributions: confinement + pinning + surface + flux
- Excluded duplicates: None
- Quarantine hooks: None
- Open items: Confinement model refinement

**Chapter 12: Light Nuclei**
- Source of truth: `M6_Li6_Be8_ANALYSIS.md`
- He-3, H-3, Li-6: in source
- Excluded duplicates: None
- Quarantine hooks: SM nuclear shell model language
- Open items: Systematic A ≤ 10 predictions

### PART E: ALPHA DECAY

**Chapter 13: Geiger-Nuttall Baseline**
- Source of truth: superheavy_predictions.py documentation
- GN formula: log(t) = a×Z/√Q + b (empirical)
- Excluded duplicates: None
- Quarantine hooks: SM nuclear force language
- Open items: None (purely empirical baseline)

**Chapter 14: Coordination Frustration**
- Source of truth: superheavy_predictions.py (calc_d_n function)
- d(n) formula: min_k |n(A) - 2^a×3^b|
- Excluded duplicates: None
- Quarantine hooks: Dataset fitting → Appendix Q
- Open items: g coefficient derivation from first principles

**Chapter 15: Superheavy Predictions**
- Source of truth: superheavy_predictions.py (full output)
- Tables: hardcode from script output
- Excluded duplicates: None
- Quarantine hooks: Experimental comparisons → Layer B
- Open items: Z = 119, 120 predictions (extrapolation)

### PART F: SYNTHESIS

**Chapter 16: Unified Picture**
- Source of truth: All prior chapters; derivation tree diagram
- Epistemic ledger: compile from all sources
- Excluded duplicates: All narrative summaries
- Quarantine hooks: SM unification language
- Open items: Open problems registry

**Chapter 17: Reproducibility**
- Source of truth: Python scripts + their outputs
- Instructions: step-by-step from scripts
- Excluded duplicates: None
- Quarantine hooks: None
- Open items: Hash manifest

---

## APPENDICES

**Appendix A: superheavy_predictions.py**
- Source: `edc_book_2/src/derivations/code/superheavy_predictions.py`
- Full listing + documentation

**Appendix B: kramers_double_well_v2.py**
- Source: `edc_book_2/src/derivations/code/kramers_double_well_v2.py`
- Full listing + documentation

**Appendix C: Numerical Tables**
- Hardcoded from Python script outputs
- All intermediate values

**Appendix D: Provenance Index**
- Full mapping: Chapter.Section → Source file

**Appendix Q: Quarantine**
- Dataset fitting procedures
- External comparisons (PDG, experimental)
- Any SM analogies

**Glossary**
- EDC terminology
- Symbol definitions

---

## DE-DUPLICATION NOTES

### Content appearing in multiple files:
1. **K formula** (K = f × σ × A): in M6_MODEL_SUMMARY, M6_PINNING_CONSTANT, M6_K_RIGOROUS
   - Canonical: M6_K_RIGOROUS_DERIVATION.md
   - Others: cite as "earlier/alternate"

2. **τ_n derivation chain**: in INSTANTON_DERIVATION_CHAIN, NEUTRON_LIFETIME_NARRATIVE
   - Canonical: NEUTRON_LIFETIME_NARRATIVE_SYNTHESIS.md (most complete)
   - Others: historical development

3. **L₀/δ hypothesis**: in V1 and V2
   - Canonical: V2 (more developed)
   - V1: earlier attempt

### Excluded content (not for Book IV):
- All BLOCK-003/004 content (paper_gravity_block003) → Book III
- Fermion generations, CKM/PMNS → Book II
- 5D→4D gravity reduction → Book III

---

## NEXT STEPS

1. **Create edc_book_4/ in repository root** (not in paper_gravity_block003)
2. **Read all source files** from edc_book_2/src/derivations/
3. **Build chapters** following this spine
4. **Hardcode tables** from Python script outputs
5. **Create Provenance Index** as Appendix D
6. **Quarantine** any SM/external content to Appendix Q
