# Book 2 Canonical Content Map

**Purpose:** Map all topics to their canonical location and identify duplicates for consolidation.
**Created:** 2026-01-29
**Status:** ACTIVE

---

## Structure Overview

The canonical Book 2 reorganizes ~65 section files into 17 chapters across 3 parts + epilogue:

| Part | Focus | Chapters |
|------|-------|----------|
| **I** | Intuition | Ch 1-6: Physical picture, ontology, case studies |
| **II** | Predictions | Ch 7-12: Electroweak params, generations, mixing, V-A |
| **III** | Machinery | Ch 13-16: OPR derivation chain, BVP closure |
| **Epilogue** | | Ch 17: Nuclear applications teaser |

---

## Topic → Canonical Location → Duplicates

### FOUNDATIONAL CONCEPTS

| Topic | Canonical Location | Current Duplicates | Action |
|-------|-------------------|-------------------|--------|
| Epistemic tags (BL/Der/Dc/P/I/M) | Front matter: "How to Read" | 00_reader_contract.tex, 12_epistemic_map.tex, ch20 | **Consolidate** to front matter |
| 5D→Brane→3D projection | Ch 1 §1.1 | 01_how_we_got_here, 02_geometry_interface, 03_unified_pipeline | **Keep in Ch1**, reference elsewhere |
| Unified pipeline (ADR) | Ch 1 §1.2 | 03_unified_pipeline, appears in all case studies | **Define once**, reference in cases |
| Particle ontology (5 classes) | Ch 2 §2.1 | 04_ontology, repeated in case study headers | **Define in Ch2**, cross-ref in cases |
| Proton as topological anchor | Ch 2 §2.2 | 04b_proton_anchor, 04c_routeB_z6_steiner | **Single canonical section** |
| Steiner theorem (120°) | Ch 2 §2.3 | 04b_proton_anchor, Z6_content_full | **Derivation Library**, reference in Ch2 |

### CASE STUDIES

| Particle | Canonical Location | Current Files | Notes |
|----------|-------------------|---------------|-------|
| Neutron | Ch 3 | 05_case_neutron, 05_neutron_story, 05b_neutron_dual_route | **Merge** into single chapter |
| Muon | Ch 4 | 06_case_muon | Clean |
| Tau | Ch 5 | 07_case_tau | Clean |
| Electron | Ch 6 §6.1 | 09_case_electron | Move before pion |
| Pion | Ch 6 §6.2 | 08_case_pion | Combine with electron |
| Neutrino | Ch 6 §6.3 | 10_case_neutrino, 06_neutrinos_edge_modes | **Merge** edge-mode theory |

### ELECTROWEAK PARAMETERS

| Topic | Canonical Location | Current Files | Status |
|-------|-------------------|---------------|--------|
| sin²θ_W derivation | Ch 7 | CH3_electroweak_parameters | [Dc] GREEN |
| g² weak coupling | Ch 7 | CH3_electroweak_parameters | [Dc] GREEN |
| M_W prediction | Ch 7 | CH3_electroweak_parameters | [Dc] GREEN |
| G_F structural pathway | Ch 8 (overview) | 11_gf_pathway, 11_gf_derivation | **Split**: overview Ch8, machinery Ch14 |

### GENERATION STRUCTURE

| Topic | Canonical Location | Current Files | Status |
|-------|-------------------|---------------|--------|
| Why 3 generations | Ch 9 | 05_three_generations, ch14_opr21 | [Dc] depends on BVP |
| μ-window constraint | Ch 9 | ch14_opr21_closure_derivation | [Dc] STRONG PARTIAL |
| BVP bound-state count | Derivation Library | ch14_opr21 (detailed) | Technical → Part III |

### MIXING AND CP

| Topic | Canonical Location | Current Files | Status |
|-------|-------------------|---------------|--------|
| PMNS angles | Ch 10 | ch6_pmns_attempt1-4, 06_neutrinos_edge_modes | [Dc] 1 GREEN, 2 YELLOW |
| θ₂₃ atmospheric | Ch 10 §10.1 | ch6_pmns_attempt3_z6_refinement | [Dc] GREEN |
| θ₁₂, θ₁₃ solar/reactor | Ch 10 §10.2 | ch6_pmns_attempt4_* | [Dc] YELLOW |
| CKM matrix | Ch 11 | 07_ckm_cp | [Dc]/[I] |
| CP phase δ | Ch 11 | ch7_attempt3_cp_phase, ch7_attempt4 | [Dc] 5° from PDG |

### V-A STRUCTURE

| Topic | Canonical Location | Current Files | Notes |
|-------|-------------------|---------------|-------|
| Chiral localization | Ch 12 | 09_va_structure | Clean |
| Why V-A emerges | Ch 12 | 09_va_structure | [Dc] from BC geometry |

### OPR DERIVATION CHAIN (Part III)

| OPR | Canonical Location | Current Files | Status |
|-----|-------------------|---------------|--------|
| OPR-04 Scale Taxonomy | Ch 13 | ch16_opr04_delta_derivation | [P]/[Der] Foundational |
| OPR-01 σ→M₀ | Ch 13 | ch15_opr01_sigma_anchor_derivation | [Der] |
| OPR-21 BVP Framework | Ch 14 | ch12_bvp_workpackage, ch14_opr21, ch14_bvp_closure_pack | [Dc] STRONG PARTIAL |
| OPR-19 g₅ coupling | Ch 15 | ch17_opr19_g5_from_action | [Der] |
| OPR-20 Mediator mass | Ch 15 | ch18_opr20_mediator_mass_from_eigenvalue | RED-C |
| OPR-22 G_eff exchange | Ch 15 | ch19_opr22_geff_from_exchange | [Der] |
| All "attempt" files | Derivation Library | ch11_g5_*, ch11_opr20_attempt* | Move to appendix |

### ELECTROWEAK BRIDGE

| Topic | Canonical Location | Current Files | Notes |
|-------|-------------------|---------------|-------|
| δ→mediator physics | Ch 14 §14.3 | ch10_electroweak_bridge | Integrate with BVP |

---

## Duplicate Content Registry

### HIGH PRIORITY (Remove duplicates)

1. **Overlap integral I₄**
   - Appears: 11_gf_derivation, ch19_opr22, multiple boxes
   - Canonical: Derivation Library `projection_reduction_lemma`
   - Action: Define once, reference everywhere

2. **δ scale disambiguation**
   - Appears: ch16_opr04, ch10_electroweak_bridge, ch14_opr21, OPR_REGISTRY.md
   - Canonical: Ch 13 (OPR-04 chapter)
   - Action: Single definition with assumption labels (A1-A3)

3. **Robin BC derivation**
   - Appears: ch11_opr20_attemptF, ch11_opr20_attemptG, ch18_opr20
   - Canonical: Ch 14 §14.2 (BVP chapter)
   - Action: One derivation, others reference it

4. **Z₆ Steiner geometry**
   - Appears: 04c_routeB_z6_steiner, Z6_content_full, multiple boxes
   - Canonical: Derivation Library
   - Action: Reference from Ch 2

5. **Pipeline mechanism (ADR)**
   - Appears: 03_unified_pipeline, every case study intro
   - Canonical: Ch 1 §1.2
   - Action: Define once, "applies here" in cases

### MEDIUM PRIORITY (Consolidate narratives)

6. **Neutron decay story**
   - Current: 05_case_neutron, 05_neutron_story, 05b_neutron_dual_route
   - Action: Merge into single Ch 3

7. **PMNS attempts**
   - Current: ch6_pmns_attempt1-4 (4 files)
   - Action: Extract final result to Ch 10, move attempts to Derivation Library

8. **G_F closure attempts**
   - Current: ch11_g5_*, ch11_opr20_* (15+ files)
   - Action: Summary in Ch 15, details to Derivation Library

---

## Files to Move to Derivation Library

These contain valuable derivations but are too detailed for reader flow:

```
ch11_g5_canonical_and_kk.tex
ch11_g5_ell_value_closure_attempt.tex
ch11_g5_value_closure_attempt2_coefficient.tex
ch11_g5_value_closure_attempt3_derive_4pi.tex
ch11_g5_ell_suppression_attempt2.tex
ch11_opr20_factor8_forensic.tex
ch11_opr20_geometric_factor8_attemptC.tex
ch11_opr20_attemptD_interpretation_robin_overcount.tex
ch11_opr20_attemptE_prefactor8_derivation.tex
ch11_opr20_attemptF_mediator_bvp_junction.tex
ch11_opr20_attemptG_derive_alpha_from_action.tex
ch11_opr20_attemptG_BC_provenance.tex
ch11_opr20_attemptH_delta_equals_Rxi.tex
ch11_opr20_attemptH1_mediator_identity.tex
ch11_opr20_attemptH2_delta_Rxi_hard_audit.tex
ch11_opr20_attemptH2plus_delta_Rxi_stricter_audit.tex
ch6_pmns_attempt1.tex
ch6_pmns_attempt2.tex
ch6_pmns_attempt3_z6_refinement.tex
ch6_pmns_attempt4_1_derive_epsilon.tex
ch6_pmns_attempt4_2_theta12_origin.tex
ch6_pmns_attempt4_menu.tex
ch7_attempt3_cp_phase.tex
ch7_attempt4_cp_refinement.tex
ch7_z2_parity_origin.tex
```

---

## Critical Cross-References

### Dependency Chain (must be defined before use)

```
Notation (Ch 0)
  → Projection principle (Ch 1)
    → Ontology (Ch 2)
      → Case studies (Ch 3-6)
        → Electroweak params (Ch 7)
          → G_F overview (Ch 8)

Scale taxonomy (Ch 13)
  → σ anchor (Ch 13)
    → BVP framework (Ch 14)
      → Coupling chain (Ch 15)
        → G_F closure (Ch 15)
```

### Chapter Recaps (5-line format)

Each chapter ends with:
1. What you learned
2. What was derived [Der]/[Dc]
3. What was assumed [P]
4. What remains open
5. Where the full proof lives (if in Derivation Library)

---

## Status Legend

| Symbol | Meaning |
|--------|---------|
| [Der] | Fully derived from postulates |
| [Dc] | Derived conditional (assumptions stated) |
| [P] | Postulated/proposed |
| [I] | Identified (pattern matched) |
| GREEN | Publication ready |
| YELLOW | Needs review |
| RED | Blocked/open |

---

## Next Steps

1. Create `EDC_BOOK2_WEAK_CANON.tex` spine
2. Write chapter intro/transition prose
3. Consolidate duplicates per registry above
4. Add 5-line recaps to each chapter
5. Move attempt files to Derivation Library
6. Compile and verify zero undefined refs
