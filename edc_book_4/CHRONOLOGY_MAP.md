# CHRONOLOGY MAP: Book IV Source Files

**Date:** 2026-02-09
**Purpose:** Complete inventory of Book IV source material with provenance tracking
**Source Directory:** `edc_book_2/src/derivations/`

---

## BOOK IV SCOPE

**Title:** Nuclear Structure from Topological Pinning
**Content:** σ → K → τ_n derivation chain, M6 lattice, nuclear binding, α-decay predictions

**NOT in Book IV:**
- Gravity sector (→ Book III)
- GUT/proton decay (→ Book III)
- Fermion generations, CKM/PMNS (→ Book II)
- Any 3D/SM language (→ Quarantine)

---

## SOURCE FILE INVENTORY

### PART A: Derivation Documents (.md)

| # | File | Topic | Epistemic Status | Chapter Target |
|---|------|-------|------------------|----------------|
| 1 | DERIVE_KAPPA_FROM_5D_HOMOTOPY.md | κ = 2π from π₁(S¹) | [Der] | Ch. 7 |
| 2 | DERIVE_L0_DELTA_PI_SQUARED.md | L₀/δ ≈ π² hypothesis | [P] | Ch. 8 |
| 3 | DERIVE_L0_DELTA_PI_SQUARED_V2.md | L₀/δ v2 (supersedes v1) | [P] | Ch. 8 |
| 4 | DERIVE_L0_RP_MAP.md | L₀ ↔ r_p mapping | [Dc] | Ch. 8 |
| 5 | DERIVE_L0_RP_FROM_5D_ELECTROSTATICS.md | Electrostatic approach | [Dc] | Ch. 8 |
| 6 | DERIVE_OMEGA0_FROM_5D.md | ω₀ from 5D | [Dc] | Ch. 6 |
| 7 | DERIVE_PREFACTOR_A.md | Instanton prefactor A | [Dc] | Ch. 6 |
| 8 | DERIVE_M_EQUALS_MP.md | M = M_P identification | [Dc] | Ch. 6 |
| 9 | DERIVE_FOUR_THIRDS_FACTOR.md | 4/3 factor origin | [Dc] | Ch. 4 |
| 10 | INSTANTON_DERIVATION_CHAIN.md | τ_n instanton formula | [Der] | Ch. 6 |
| 11 | EPISTEMIC_CORRECTION_L0_MAP.md | L₀ map correction | [Dc] | Ch. 8 |
| 12 | M6_MODEL_SUMMARY.md | Topological pinning overview | [Summary] | Reference |
| 13 | M6_PINNING_CONSTANT_DERIVATION.md | K = f × σ × A_contact | [Der] | Ch. 4 |
| 14 | M6_K_RIGOROUS_DERIVATION.md | K from contact geometry | [Der] | Ch. 4 |
| 15 | M6_GEOMETRY_DERIVATION.md | M6 lattice structure | [Der] | Ch. 5 |
| 16 | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | Model development | [Dev] | Reference |
| 17 | M6_HELIUM4_ANALYSIS.md | He-4 binding energy | [Der] | Ch. 11 |
| 18 | M6_Li6_Be8_ANALYSIS.md | Light nuclei analysis | [Der] | Ch. 12 |
| 19 | M6_SENSITIVITY_REPORT.md | Sensitivity analysis | [Ver] | Appendix |
| 20 | M6_EXTENDED_ANALYSIS_REPORT.md | Extended checks | [Ver] | Appendix |
| 21 | NEUTRON_LIFETIME_NARRATIVE_SYNTHESIS.md | Complete τ_n story | [Der] | Ch. 9 |
| 22 | SESSION_LOG_NEUTRON_LIFETIME.md | Research session log | [Dev] | Excluded |
| 23 | Z3_SYMMETRY_ANALYSIS_NEUTRON.md | Z₃ symmetry of neutron | [Der] | Ch. 3 |
| 24 | V_B_FROM_Z3_BARRIER_CONJECTURE.md | V_B = 2×Δm_np | [P] | Ch. 3 |
| 25 | S5D_TO_SEFF_Q_REDUCTION.md | 5D → 1D reduction | [Der] | Ch. 6 |
| 26 | ROUTE_F_STATUS_BOX.md | Kramers escape status | [Status] | Reference |

### PART B: Python Scripts (code/)

| # | File | Purpose | Output Type | Chapter Target |
|---|------|---------|-------------|----------------|
| 1 | superheavy_predictions.py | α-decay for Z ≥ 114 | Tables | Ch. 15, App. A |
| 2 | kramers_double_well_v2.py | Langevin escape sims | Validation | Ch. 9, App. B |
| 3 | delta_m_np_options.py | Δm_np calculations | Values | Ch. 3 |
| 4 | prefactor_sensitivity_full.py | Prefactor sensitivity | Analysis | Appendix |
| 5 | prefactor_refit_cv.py | Cross-validation refit | Validation | Appendix |
| 6 | superheavy_oos_test.py | Out-of-sample testing | Validation | Ch. 15 |

### PART C: LaTeX Sources

| # | File | Purpose | Status |
|---|------|---------|--------|
| 1 | BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex | Main book section | Active |
| 2 | TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex | Standalone monograph | Superseded |
| 3 | topological_pinning_standalone_UPDATED_v3.tex | Updated standalone | Superseded |
| 4 | compile_topological_pinning.tex | Compilation driver | Build tool |
| 5 | compile_neutron_section.tex | Neutron section driver | Build tool |

---

## EPISTEMIC STATUS LEGEND

| Tag | Meaning |
|-----|---------|
| [Der] | Derived from first principles |
| [Dc] | Derived with constraints |
| [P] | Postulated (motivated but not derived) |
| [Ver] | Verification/validation |
| [Dev] | Development notes (not canonical) |
| [Summary] | Summary document (cites sources) |
| [Status] | Status tracking |

---

## CANONICAL SOURCES (Source of Truth)

### For Each Topic:

| Topic | Canonical File | Alternates |
|-------|----------------|------------|
| K formula | M6_K_RIGOROUS_DERIVATION.md | M6_PINNING_CONSTANT_DERIVATION.md |
| τ_n derivation | NEUTRON_LIFETIME_NARRATIVE_SYNTHESIS.md | INSTANTON_DERIVATION_CHAIN.md |
| κ = 2π | DERIVE_KAPPA_FROM_5D_HOMOTOPY.md | — |
| L₀/δ ratio | DERIVE_L0_DELTA_PI_SQUARED_V2.md | V1 (earlier) |
| M6 geometry | M6_GEOMETRY_DERIVATION.md | M6_TOPOLOGICAL_MODEL_EXPLORATION.md |
| He-4 binding | M6_HELIUM4_ANALYSIS.md | — |
| α-decay | superheavy_predictions.py | — |

---

## CONTAMINATION STATUS

### Clean EDC (OK for Book IV):

All files in `edc_book_2/src/derivations/` are designed to be EDC-internal.
However, some may contain:
- SM nuclear shell model language (→ Quarantine)
- External empirical comparisons (→ Layer B)
- Fitting procedures (→ Appendix Q)

### Requires Screening:

| File | Potential Issue | Action |
|------|-----------------|--------|
| M6_Li6_Be8_ANALYSIS.md | May reference shell model | Screen for SM terms |
| superheavy_predictions.py | Uses Geiger-Nuttall fit | Fitting → Appendix Q |
| M6_HELIUM4_ANALYSIS.md | May compare to SM values | External → Layer B |

---

## CHAPTER → SOURCE MAPPING

### PART A: Topological Foundations

| Chapter | Title | Primary Source | Secondary |
|---------|-------|----------------|-----------|
| 1 | Proton as Topological Ground State | 04b_proton_anchor.tex | — |
| 2 | Junction Symmetries (Z₆) | 04c_routeB_z6_steiner.tex | M6_GEOMETRY_DERIVATION.md |
| 3 | Neutron as Metastable State | Z3_SYMMETRY_ANALYSIS_NEUTRON.md | V_B_FROM_Z3_BARRIER_CONJECTURE.md |

### PART B: Pinning Mechanism

| Chapter | Title | Primary Source | Secondary |
|---------|-------|----------------|-----------|
| 4 | From σ to K | M6_K_RIGOROUS_DERIVATION.md | M6_PINNING_CONSTANT_DERIVATION.md |
| 5 | M6 Coordination Lattice | M6_GEOMETRY_DERIVATION.md | superheavy_predictions.py |

### PART C: Neutron Lifetime

| Chapter | Title | Primary Source | Secondary |
|---------|-------|----------------|-----------|
| 6 | Instanton Derivation | INSTANTON_DERIVATION_CHAIN.md | S5D_TO_SEFF_Q_REDUCTION.md |
| 7 | κ = 2π from Homotopy | DERIVE_KAPPA_FROM_5D_HOMOTOPY.md | — |
| 8 | L₀/δ Scale Ratio | DERIVE_L0_DELTA_PI_SQUARED_V2.md | DERIVE_L0_RP_MAP.md |
| 9 | τ_n = 880 s Prediction | NEUTRON_LIFETIME_NARRATIVE_SYNTHESIS.md | kramers_double_well_v2.py |

### PART D: Nuclear Binding

| Chapter | Title | Primary Source | Secondary |
|---------|-------|----------------|-----------|
| 10 | Deuterium | M6_MODEL_SUMMARY.md §Deuterium | — |
| 11 | Helium-4 | M6_HELIUM4_ANALYSIS.md | — |
| 12 | Light Nuclei | M6_Li6_Be8_ANALYSIS.md | — |

### PART E: Alpha Decay

| Chapter | Title | Primary Source | Secondary |
|---------|-------|----------------|-----------|
| 13 | Geiger-Nuttall Baseline | superheavy_predictions.py (docs) | → Appendix Q |
| 14 | Coordination Frustration | superheavy_predictions.py (calc_d_n) | — |
| 15 | Superheavy Predictions | superheavy_predictions.py (output) | superheavy_oos_test.py |

### PART F: Synthesis

| Chapter | Title | Primary Source | Secondary |
|---------|-------|----------------|-----------|
| 16 | Unified Picture | All chapters | — |
| 17 | Reproducibility | Python scripts | — |

---

## EXCLUDED CONTENT

| Content | Reason | Destination |
|---------|--------|-------------|
| SESSION_LOG_NEUTRON_LIFETIME.md | Development log | Excluded |
| ROUTE_F_STATUS_BOX.md | Status tracking | Reference only |
| M6_MODEL_SUMMARY.md | Summary (not source) | Reference only |
| Fermion generation content | Wrong book | Book II |
| GUT/proton decay content | Wrong book | Book III |

---

## OPEN ITEMS (from source review)

| Item | Source | Status |
|------|--------|--------|
| f factor derivation | M6_K_RIGOROUS_DERIVATION.md | [OPEN] |
| L₀/δ = π² rigorous derivation | DERIVE_L0_DELTA_PI_SQUARED_V2.md | [P] |
| Prefactor A from first principles | DERIVE_PREFACTOR_A.md | [Dc] |
| g coefficient in d(n) | superheavy_predictions.py | [OPEN] |
| Z₆ → Z₃ breaking mechanism | M6_GEOMETRY_DERIVATION.md | [OPEN] |

---

## FILE STATISTICS

- **Derivation documents:** 26 .md files
- **Python scripts:** 6 .py files
- **LaTeX sources:** 5 .tex files
- **Total source files:** 37

**Canonical sources:** 7 primary files
**Superseded/development:** 6 files
**Reference only:** 4 files

---

## NEXT STEPS

1. Screen all sources for SM/3D contamination
2. Extract numerical tables from Python scripts
3. Build LaTeX chapter structure
4. Create Appendix Q for fitting procedures
5. Create Appendix D for provenance index

---

**CHRONOLOGY MAP COMPLETE. Ready for book structure creation.**
