# EDC Papers Full Inventory and Nuclear Topology Discovery Report

**Date:** 2026-03-15
**Branch:** `archive/nuclear-topology-discovery`
**Trigger:** Emergency preservation of nuclear topology M-operator material

---

## 1. Executive Summary

Emergency search completed. The nuclear pinning monograph has been located:

**Primary document:** `edc_book_2/src/derivations/topological_pinning_standalone_UPDATED_v3.tex`
(1,461 lines, already tracked in git, commit `92dc33b`)

Title: "Topological Pinning Model for Nuclear Structure"

Additional nuclear material found across 5 locations:
- Book 4 chapters (ch10–ch13): deuterium, helium-4, light nuclei, Geiger-Nuttall
- Private repo: nuclear topology note + parameter ledger + stabilization docs
- Downloads backup: nuclear fusion paper, hydrogen derivation, chemical bonding
- Book 2 radioactivity audit: 179 files across 13 version directories

**All material in git repos is already tracked.** Downloads backup material (15 source
files not in any repo) has been copied to `_archive_nonrepo/nuclear_topology/` for
preservation. Private repo nuclear files (4 files) also copied for backup.

---

## 2. edc_papers/ Directory Structure

### 2.1 Top-level contents

| Directory | Description |
|-----------|-------------|
| `_shared/` | Shared code, derivations, meta, style |
| `paper_2/` | Paper 2 (proton mass ratio 6π⁵) |
| `paper_3_series/` | Paper 3 series (20 companions: 00–20) |
| `paper_gravity_block003/` | Block-003/004 derivation program (v1–v67) |
| `EXPORT_NAMING_POLICY.md` | Naming conventions |

### 2.2 paper_3_series/ companions

| # | Directory | Topic |
|---|-----------|-------|
| 00 | `framework_v2_0` | Framework v2.0 |
| 01 | `paper3_njsr_journal` | Paper 3 NJSR journal version |
| 02 | `companion_A_effective_lagrangian` | Effective Lagrangian |
| 03 | `companion_B_wkb_prefactor` | WKB Prefactor |
| 04 | `companion_C_5d_reduction` | 5D Reduction |
| 05 | `companion_D_selection_rules` | Selection Rules |
| 06 | `companion_E_symmetry_ops` | Symmetry Operations |
| 07 | `companion_F_proton_junction` | Proton Junction (6π⁵) |
| 08 | `companion_G_neutron_proton_mass_split` | n-p Mass Split |
| 09 | `companion_H_weak_interactions` | Weak Interactions |
| 10 | `companion_N_neutron_junction` | Neutron Junction |
| 11 | `companion_M_muon_decay_tomography` | Muon Decay |
| 12 | `companion_T_tau_decay` | Tau Decay |
| 13 | `companion_P_pion_decay` | Pion Decay |
| 14 | `weak_program_overview` | Weak Program Overview |
| 15 | `companion_L_electron_brane_defect` | Electron Brane Defect |
| 16 | `companion_V_neutrino_edge_mode` | Neutrino Edge Mode |
| 17 | `open_W1_GF_toy_derivation` | G_F Toy Derivation |
| 18 | `paper3_2_0_edc_weak_sector` | EDC Weak Sector |
| 19 | `edc_weak_sector_zenodo_article` | Weak Sector Zenodo |
| 20 | `book_chapter_weak_interface` | Book Chapter Weak Interface |

### 2.3 paper_gravity_block003/ — v1 through v67

All 67 derivation versions present (v1–v67). Each contains at minimum:
`main.tex`, `README.md`, `REPORT.md`, `ACCEPTANCE.md`, `recompute.py`

Later versions (v54+) also include `release/` subdirectories.

**Derivation titles (complete list):**

| Version | Title / Topic |
|---------|---------------|
| v1 | (no README) |
| v2 | Can R_ξ Serve as the Compactification Scale L? |
| v3 | Can κ₅² Be Fixed by σ? |
| v4 | Fix Constant C in κ₅² = C·σ^(-3/4) |
| v5 | Normalization Principle Choices to Fix C |
| v6 | Collective Bulk Dimple and Auto-Trapping Threshold |
| v7 | Normalization Candidate Catalog |
| v8 | NC-1 Attempt (Graviton Zero-Mode Normalization) |
| v9 | NC-2 Attempt (DGP / Induced Gravity) |
| v10 | Tautology Audit + Order-of-Magnitude Check |
| v11 | Derive σ from EDC Field Equations |
| v12 | Part I Gravity & Mercury Precession Audit |
| v13 | Weak-Field 5D→4D Matching: The Normalization Extractor |
| v14 | EDC Candidates for Warp Profile and Zero-Mode |
| v15 | Calibrated Closure with ℓ_P and Error Budget |
| v16 | R_ξ Determination: Internal vs Minimal-Baseline |
| v17 | EW-Scale Calibration Robustness for R_ξ and M₅ |
| v18 | Gravity Sector Closure Summary + Reader Contract |
| v19 | Derivation-First: From 5D Action to 4D Newton Law |
| v20 | Factor & Normalization Audit |
| v21 | KK Mass Gap to R_xi Identification |
| v22 | KK Conventions Unification |
| v23 | BLOCK-003 Canonical Closure Packet |
| v24 | Reproducibility & Unit/Convention Audit |
| v25 | Alternative Gap Identifications & Robustness Analysis |
| v26 | Gap Derivability Program |
| v27 | Brane Mass from Brane Tension (σ Pinning) |
| v28 | λ-Pinning from Self-Adjointness + Topological Quantization |
| v29 | β Control Parameter |
| v30 | Derive or Constrain L from β + λ |
| v31 | Gauge Sector Normalization, BC Registry, and Scale Regime Map |
| v32 | Unified Gauge Sector BC Breaking + Scale Map |
| v33 | Matter + RG Dual-Track Program |
| v34 | Fermi Constant from KK Tower Exchange |
| v35 | GUT BC Survivor Map |
| v36 | G_F Numerical Closure Step: g_5 Fixing |
| v37 | BC Selection Principle Sketch |
| v38 | Hosotani Closure Roadmap |
| v39 | BC Selector Applied to GUT Survivor Map |
| v40 | Numerical ΔE_vac^finite Track Ranking |
| v41 | Matter-Augmented ΔE_vac^finite Ranking |
| v42 | E₆ Anomaly Audit + Exotics Mass Gating |
| v43 | PS Chirality Closure + Anomaly Gate |
| v44 | Anomaly One-Shot: SoT Lock |
| v45 | SoT-Lock Track Compiler |
| v46 | No-Escape Track Selector |
| v47 | Pati-Salam Canonicalization |
| v48 | PS G_F Numerical Closure |
| v49 | PS Weinberg Angle Numerical Closure |
| v50 | PS → IR Matching & Physical-Scale Map |
| v51 | Log Hygiene Lock + Unit-Change Invariance |
| v52 | PS Prediction Pack |
| v53 | PS Observable Interface Without Contamination |
| v54 | BLOCK-003 Canonical Single Document |
| v55 | BLOCK-004 PS → QCD (α₃) Structural Closure |
| v56 | BLOCK-004 α₃(μ*) Numerical Closure |
| v57 | Layer B Adapter (α₃ MZ comparison) |
| v58 | Layer B Λ_QCD Extraction (two-route) |
| v59 | Formal Λ_QCD Two-Route Extraction |
| v60 | BLOCK-004 Canonical Single Document |
| v61 | Proton Decay Program Note (PS) |
| v62 | PS Breaking Scale M_X (Two-Route) |
| v63 | Proton Decay τ_p Structural Interface |
| v64 | Proton Decay Coupling Lane g_X(M_X) |
| v65 | Proton Decay Canonical Single Document |
| v66 | Layer B τ_p(σ̃) Bounds Comparison |
| v67 | σ̃ Import Contract + Closure Map (REAL CLOSED) |

### 2.4 Statistics

| Metric | Value |
|--------|-------|
| Total files in edc_papers/ | 1,365 |
| Total size | 87 MB |
| Git status | All tracked (0 untracked) |
| Derivation versions | v1–v67 (67 versions) |
| Paper 3 companions | 21 (00–20) |

---

## 3. Nuclear Pinning Monograph — Location and Status

### 3.1 Primary Document (FOUND)

**File:** `edc_book_2/src/derivations/topological_pinning_standalone_UPDATED_v3.tex`
**Lines:** 1,461
**Title:** "Topological Pinning Model for Nuclear Structure"
**Git status:** Tracked (commit `92dc33b`)
**Companion files:**
- `compile_topological_pinning.tex` (57 lines, compile wrapper)
- `compile_topological_pinning.pdf` (compiled output)
- `topological_pinning_standalone_UPDATED_v3.pdf` (compiled output)
- `tables/superheavy_predictions.csv` (superheavy α-decay predictions)
- `code/superheavy_predictions.py` (prediction code)
- `code/superheavy_oos_test.py` (out-of-sample test)

**Content verified:** Contains superheavy element predictions, binding energy
analysis, magic number discussion, α-decay predictions, Geiger-Nuttall law
treatment (53 occurrences of nuclear-related terms).

### 3.2 Book 4 Nuclear Chapters (FOUND — already in git)

| File | Lines | Topic | Git |
|------|-------|-------|-----|
| `edc_book_4/chapters/ch10_deuterium.tex` | 518 | Deuterium binding | Tracked |
| `edc_book_4/chapters/ch11_helium4.tex` | 954 | Helium-4 structure | Tracked |
| `edc_book_4/chapters/ch12_light_nuclei.tex` | 708 | Light nuclei (Li, Be, C) | Tracked |
| `edc_book_4/chapters/ch13_geiger_nuttall.tex` | 514 | Geiger-Nuttall law | Tracked |

### 3.3 Private Repo Nuclear Files (FOUND — tracked in private repo)

| File | Lines | Content |
|------|-------|---------|
| `NUCLEAR_TOPOLOGY_NOTE.md` | 479 | Nuclear graph topology formalization (Croatian) |
| `NUCLEAR_TOPOLOGY_PARAMETER_LEDGER.md` | 106 | 20-parameter model definition |
| `NUCLEAR_STABILIZATION.md` | 178 | Nuclear stabilization analysis |
| `NUCLEAR_STABILIZATION_CHECK.md` | 173 | Stabilization verification |

All tracked in private repo (commit `b0e2827`).
Copies preserved in `_archive_nonrepo/nuclear_topology/private_repo_nuclear/`.

### 3.4 Book 2 Radioactivity Audit (FOUND — extensive, all tracked)

179 files across 13 version directories:
- `radioactivity_forbidden_research/` — initial research
- `radioactivity_forbidden_v2/` through `v5/` — forbidden topology iterations
- `radioactivity_n48_v1/` — N=48 analysis
- `radioactivity_v7_1_alpha15/` through `v7_8_Salpha_deformation/` — α-decay versions
- `radioactivity_v7_bl/` — baseline version
- `topological_pinning_v7_9_integration/` — integration pass

Contains: decay chains (U238→Pb206, U235→Pb207, Th232→Pb208), forbidden
topologies, crystal structures, N-A mapping, branching rules, α-decay
calculations for 15, 45, and 100+ isotopes, S_alpha deformation model,
prefactor microphysics, hindered α-decay, superheavy predictions.

### 3.5 Downloads Backup (FOUND — NOT in any repo, NOW PRESERVED)

15 source files from `/Users/igor/Downloads/EDC ALL BACKUP/2026.01.09/EDC Research Papers/`
and `files (14)/` — now copied to `_archive_nonrepo/nuclear_topology/downloads_edc_research_papers/`:

| File | Lines | Topic |
|------|-------|-------|
| `EDC_Nuclear_Fusion_Paper.md` | 603 | Nuclear fusion from 5D geometry |
| `EDC_Nuclear_Fusion_Paper.tex` | 831 | Same, LaTeX version |
| `EDC_Paper_06_Nuclear_Fusion.tex` | 784 | Earlier version of fusion paper |
| `EDC_5D_Hydrogen_Derivation.md` | 699 | 5D hydrogen atom derivation |
| `EDC_5D_Hydrogen_Derivation.tex` | 780 | Same, LaTeX version |
| `EDC_5D_Atom_Derivation.tex` | ~800 | 5D atom derivation |
| `EDC_Chemical_Bonding_Paper.md` | 410 | Chemical bonding from EDC |
| `EDC_Coherent_Bulk_Focusing_Paper.md` | ~650 | Coherent bulk focusing |
| `EDC_Coherent_Bulk_Focusing_Paper.tex` | ~900 | Same, LaTeX version |
| `EDC_Complete_Knowledge_Base_v1.md` | ~500 | Complete EDC knowledge base |
| `EDC_Jeans_Mass_Paper.md` | ~530 | Jeans mass from EDC |
| `EDC_Part2_Draft_Electron_Topology_Insight.md` | ~120 | Part II electron topology |
| `Part_II_Atom_Complete.tex` | ~900 | Part II complete atom |
| `Part_II_Bohr_Radius_Derivation.tex` | ~700 | Bohr radius derivation |
| `EDC_Hydrogen_Simulation.jsx` | ~500 | Hydrogen simulation code |

**These files were NOT in any git repo and are now preserved for the first time.**

---

## 4. Binding Energy Tables

| Location | Contains BE tables? | Detail |
|----------|-------------------|--------|
| `topological_pinning_standalone_UPDATED_v3.tex` | **Yes** | Superheavy predictions, α-decay systematics |
| `tables/superheavy_predictions.csv` | **Yes** | Machine-readable predictions |
| `ch10_deuterium.tex` | **Yes** | Deuterium binding energy |
| `ch11_helium4.tex` | **Yes** | He-4 binding energy |
| `ch12_light_nuclei.tex` | **Yes** | Light nuclei BE comparison |
| `radioactivity_v7_*` | **Yes** | Extensive α-decay energy tables |
| `EDC_Nuclear_Fusion_Paper.md` | Partial | Fusion energetics |

---

## 5. Magic Numbers Coverage

| Location | Addresses magic numbers? |
|----------|------------------------|
| `topological_pinning_standalone_UPDATED_v3.tex` | **Yes** — coordination/topology explanation |
| `ch12_light_nuclei.tex` | **Yes** — light nuclei shell closures |
| `radioactivity_forbidden_v4/05_BULK_CRYSTAL_NUCLEI_MODELS.md` | **Yes** — crystal model |
| `NUCLEAR_TOPOLOGY_NOTE.md` | Partial — graph-theoretic framework |

---

## 6. Heavy Elements Coverage

| Location | Heavy element range |
|----------|-------------------|
| `topological_pinning_standalone_UPDATED_v3.tex` | Superheavy (Z > 100) predictions |
| `superheavy_predictions.csv` | Specific isotope predictions |
| `superheavy_predictions.py` + `superheavy_oos_test.py` | Computational verification |
| `radioactivity_v7_4_alpha100/` | 100+ α-decay isotopes |
| `radioactivity_v7_8_Salpha_deformation/` | Deformation corrections |
| `radioactivity_n48_v1/` | N=48 shell analysis |
| Decay chains | U238, U235, Th232 → Pb isotopes |

---

## 7. Protection Status Summary

| Material | Location | Git status | Action taken |
|----------|----------|------------|--------------|
| Pinning monograph (v3) | `edc_book_2/src/derivations/` | **Tracked** | None needed |
| Book 4 nuclear chapters | `edc_book_4/chapters/ch10-ch13` | **Tracked** | None needed |
| Book 2 radioactivity audit | `edc_book_2/audit/radioactivity_*` | **Tracked** | None needed |
| Private repo nuclear files | `EDC_Research_PRIVATE/` | **Tracked** (private) | Copied to `_archive_nonrepo/` |
| Downloads backup papers | `~/Downloads/EDC ALL BACKUP/` | **NOT tracked** | **Copied and committed** |
| edc_papers/ (all) | `edc_papers/` | **Tracked** | None needed |

---

## 8. What v1–v67 Derivations Cover

The 67-version derivation program covers the gravity/gauge sector closure:

- **v1–v10:** Parameter closure attempts for κ₅², σ, R_ξ, C
- **v11–v18:** σ derivation, gravity audit, normalization, closure summary
- **v19–v26:** 5D→4D derivation-first approach, KK conventions, gaps
- **v27–v30:** Brane mass, λ-pinning, β parameter, L constraints
- **v31–v46:** Gauge sector: BC selection, GUT survivors, anomaly audit, SoT lock
- **v47–v54:** Pati-Salam canonicalization: G_F, Weinberg angle, PS→IR, predictions
- **v55–v60:** BLOCK-004: α₃, Λ_QCD extraction, canonical document
- **v61–v67:** Proton decay program, τ_p bounds, σ̃ import contract, REAL CLOSED

---

## 9. Bottom Line

The nuclear pinning monograph is the 1,461-line standalone document at
`edc_book_2/src/derivations/topological_pinning_standalone_UPDATED_v3.tex`,
titled "Topological Pinning Model for Nuclear Structure." It is already
tracked in git. The broader nuclear program spans Book 4 chapters (ch10–ch13),
179 radioactivity audit files in Book 2, and 4 private repo documents. All
repo material is tracked. 15 source files from the Downloads backup (including
the nuclear fusion paper, hydrogen derivation, and chemical bonding paper)
were NOT in any repo and have been preserved for the first time in
`_archive_nonrepo/nuclear_topology/`.
