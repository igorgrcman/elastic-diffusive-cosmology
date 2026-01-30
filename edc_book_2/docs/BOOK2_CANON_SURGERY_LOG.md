# Book 2 Canonical Surgery Log

**Purpose:** Document all consolidation, removal, and reorganization decisions.
**Created:** 2026-01-29
**Status:** IN PROGRESS

---

## Summary of Changes

### Structure Reorganization

| Old Location | New Location | Action |
|--------------|--------------|--------|
| Ch 1 (mega-chapter with 15+ inputs) | Split into Ch 1-6 | **SPLIT** |
| Ch 11 GF closure attempts (15 files) | Part III Ch 15 summary + Derivation Library | **CONSOLIDATED** |
| Meta appendices | Removed from reader path | **MOVED** to editorial |
| Quarantine appendix | Removed | **DELETED** (was empty) |

### Part I: Physical Picture (Ch 1-6)

| Chapter | Source Files | Surgery Notes |
|---------|--------------|---------------|
| Ch 1: Weak Interface | 01_how_we_got_here, 02_geometry_interface, 03_unified_pipeline | Merged into coherent intro |
| Ch 2: Ontology | 04_ontology, 04b_proton_anchor, 04a_unified_master_figure | Added Steiner reference |
| Ch 3: Neutron | 05_case_neutron, 05b_neutron_dual_route | Merged Route A/B analysis |
| Ch 4: Muon | 06_case_muon | Clean, no changes |
| Ch 5: Tau | 07_case_tau | Clean, no changes |
| Ch 6: Stability | 09_case_electron, 08_case_pion, 10_case_neutrino | Combined three particles |

### Part II: Predictions (Ch 7-12)

| Chapter | Source Files | Surgery Notes |
|---------|--------------|---------------|
| Ch 7: Electroweak | CH3_electroweak_parameters | Clean, no changes |
| Ch 8: GF Overview | 11_gf_pathway | Extracted overview, moved derivation to Part III |
| Ch 9: Generations | 05_three_generations | Clean, no changes |
| Ch 10: PMNS | 06_neutrinos_edge_modes | Summary only; attempts to Derivation Library |
| Ch 11: CKM/CP | 07_ckm_cp | Clean, no changes |
| Ch 12: V-A | 09_va_structure | Clean, no changes |

### Part III: Machinery (Ch 13-16)

| Chapter | Source Files | Surgery Notes |
|---------|--------------|---------------|
| Ch 13: Scales | ch16_opr04, ch15_opr01 | OPR-04 + OPR-01 combined |
| Ch 14: BVP | ch12_bvp_workpackage, ch14_opr21, ch10_electroweak_bridge | Full BVP chain |
| Ch 15: Coupling | ch17_opr19, ch18_opr20, ch19_opr22 | Full coupling chain |
| Ch 16: Status | ch20_epistemic_summary | Consolidated closure status |

### Epilogue (Ch 17)

| Chapter | Source Files | Surgery Notes |
|---------|--------------|---------------|
| Ch 17: Nuclear | XX_teaser_book3 | Unchanged |

---

## Files Moved to Derivation Library

These files contain valuable derivations but were too detailed for reader flow:

### GF Closure Attempts (15 files)
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
```

### PMNS Attempts (6 files)
```
ch6_pmns_attempt1.tex
ch6_pmns_attempt2.tex
ch6_pmns_attempt3_z6_refinement.tex
ch6_pmns_attempt4_1_derive_epsilon.tex
ch6_pmns_attempt4_2_theta12_origin.tex
ch6_pmns_attempt4_menu.tex
```

### CP Phase Attempts (3 files)
```
ch7_attempt3_cp_phase.tex
ch7_attempt4_cp_refinement.tex
ch7_z2_parity_origin.tex
```

**Status:** These files remain in `sections/` but are NOT included in the canonical
spine. They are referenced from the Derivation Library for specialists.

---

## Duplicate Content Consolidated

### 1. Overlap Integral I₄

**Problem:** Definition appeared in 5+ locations with slight variations.

**Solution:**
- Canonical definition: Derivation Library, `projection_reduction_lemma`
- All other locations now reference: "See Projection-Reduction Lemma in Appendix"

### 2. Scale Taxonomy (δ, Δ, ℓ, R_ξ)

**Problem:** Four scales defined inconsistently across OPR chapters.

**Solution:**
- Canonical definition: Ch 13 §13.1 (OPR-04)
- Assumption labels (A1-A3) defined once
- All other locations: "Scales defined in §13.1; we use them here."

### 3. Robin BC Derivation

**Problem:** Derived from scratch in 3 different attempt files.

**Solution:**
- Canonical derivation: Ch 14 §14.2 (BVP Framework)
- Derivation Library: "Frozen Brane BC Complete Analysis"
- Attempt files: Moved to Derivation Library archive

### 4. Pipeline Mechanism (ADR)

**Problem:** Full pipeline explained in every case study intro.

**Solution:**
- Canonical definition: Ch 1 §1.2 (Unified Pipeline)
- Case studies now say: "The ADR pipeline (Ch 1) applies here."

### 5. Z₆ Steiner Geometry

**Problem:** Derivation repeated in 04b_proton_anchor and Z6_content_full.

**Solution:**
- Canonical proof: Derivation Library, "Z_N Discrete Averaging Lemma"
- Ch 2 references: "Steiner theorem proven in Appendix"

---

## Removed from Reader Path

### 1. Quarantine Appendix
- **Was:** Empty appendix pointing to internal audit file
- **Action:** Removed entirely (previous session)
- **Reason:** No quarantined content; exposed internal path

### 2. Meta Appendices
- **Files:** meta_part2/00-05 (claim ledger, decision log, timeline, evidence map)
- **Action:** NOT included in canonical spine
- **Reason:** Editorial documentation, not reader-facing
- **Status:** Files remain for editors; not compiled in canonical PDF

### 3. "See X.md" References
- **Count:** 16 footnotes eliminated (previous session)
- **Action:** Converted to internal book references or Derivation Library
- **Reason:** Readers don't have repo access

### 4. "Companion M/T/N" References
- **Action:** Replaced with section cross-references
- **Reason:** Legacy terminology from pre-integration phase

---

## Chapter Recaps Added

Each chapter now ends with a 5-line recap box:

```latex
\begin{chapterRecap}
\textbf{What you learned:} [1-2 sentences]
\textbf{What was derived:} [list with tags]
\textbf{What was assumed:} [list with tags]
\textbf{What remains open:} [list]
\textbf{Full proofs:} [location in Derivation Library]
\end{chapterRecap}
```

---

## Transition Prose Added

### Part Introductions
- Part I: "builds intuition through concrete examples"
- Part II: "derives observables without fitting"
- Part III: "technical OPR chain for specialists"

### Chapter Quotes
- Each chapter opens with italicized summary quote
- Explains chapter's role in overall narrative

### Dependency Notes
- "How to Read This Book" includes derivation chain map
- Reading paths defined (quick tour, full narrative, technical deep-dive)

---

## Status

| Task | Status |
|------|--------|
| Content Map created | ✓ DONE |
| Spine created | ✓ DONE |
| Surgery Log created | ✓ DONE |
| Compile test | PENDING |
| Build report | PENDING |
| Commit | PENDING |

---

## Next Steps

1. Test compile `EDC_BOOK2_WEAK_CANON.tex`
2. Fix any undefined references
3. Create build report
4. Commit with clear message
