# EDC Part II: Book File Manifest

**Generated:** 2026-01-23
**Main file:** `EDC_Part_II_Weak_Sector_rebuild.tex`
**Build command:** `latexmk -xelatex EDC_Part_II_Weak_Sector_rebuild.tex`

---

## CRITICAL: DIRECTORY STRUCTURE WARNING

There are **TWO PARALLEL DIRECTORY STRUCTURES** with same file names:

```
paper/
├── sections/                    ← STARA verzija, NE KORISTI SE!
│   ├── 05_three_generations.tex
│   ├── 06_neutrinos_edge_modes.tex
│   └── ...
│
└── rebuild_part2_snapshot/
    └── paper/                   ← TRENUTNA verzija, OVA SE KORISTI!
        ├── EDC_Part_II_Weak_Sector_rebuild.tex  (MAIN FILE)
        ├── CH3_electroweak_parameters.tex
        ├── sections/
        │   ├── 05_three_generations.tex
        │   ├── 06_neutrinos_edge_modes.tex
        │   └── ...
        └── BOOK_FILE_MANIFEST.md (this file)
```

### OTKRIĆE: HARD LINKOVI

Provjerom inodea ustanovljeno je da su fajlovi u `paper/sections/` i
`paper/rebuild_part2_snapshot/paper/sections/` **ISTI FAJLOVI** (hard linkovi):

```
408389777 rebuild_part2_snapshot/paper/sections/05_three_generations.tex
408389777 sections/05_three_generations.tex  ← ISTI INODE!
```

**Implikacija:** Editiranje bilo kojeg editira oba. NEMA inkosistencije.

### PREPORUKA:

1. **Za sada:** Radi u `rebuild_part2_snapshot/paper/` jer tamo je main .tex file.
2. **Dugoročno:** Razmisli o uklanjanju `paper/sections/` symlinka/hardlinka da izbjegneš konfuziju.
3. **Build:** Uvijek pokreći iz `rebuild_part2_snapshot/paper/`:
   ```bash
   cd .../paper/rebuild_part2_snapshot/paper/
   latexmk -xelatex EDC_Part_II_Weak_Sector_rebuild.tex
   ```

---

## CANONICAL CHAPTER → FILE MAP

### Part I: Case Studies (Block 1)

| Line | Chapter | File | Status |
|------|---------|------|--------|
| 310 | Reader Contract | `sections/00_reader_contract.tex` | |
| 311 | How We Got Here | `sections/01_how_we_got_here.tex` | |
| 312 | Geometry Interface | `sections/02_geometry_interface.tex` | |
| 313 | Unified Pipeline | `sections/03_unified_pipeline.tex` | |
| 314 | Master Figure | `sections/04a_unified_master_figure.tex` | |
| 315 | Ontology | `sections/04_ontology.tex` | |
| 316 | Proton Anchor | `sections/04b_proton_anchor.tex` | |
| 317 | Case: Neutron | `sections/05_case_neutron.tex` | |
| 318 | Case: Muon | `sections/06_case_muon.tex` | |
| 319 | Case: Tau | `sections/07_case_tau.tex` | |
| 320 | Case: Electron | `sections/09_case_electron.tex` | |
| 321 | Case: Pion | `sections/08_case_pion.tex` | |
| 322 | Case: Neutrino | `sections/10_case_neutrino.tex` | |
| 323 | G_F Pathway | `sections/11_gf_pathway.tex` | |
| 324 | Summary | `sections/13_summary.tex` | |

### Part II: Core Derivations (Block 2)

| Line | Chapter | File | Narrative Hardened |
|------|---------|------|-------------------|
| 337 | Ch 2: Z6 Content | `Z6_content_full.tex` (root) | NO |
| 349 | **Ch 3: Electroweak** | `CH3_electroweak_parameters.tex` (root) | **YES (2026-01-23)** |
| 361 | Ch 4: Lepton Mass | `CH4_lepton_mass_candidates.tex` (root) | NO |
| 373 | **Ch 5: Three Generations** | `sections/05_three_generations.tex` | **YES (2026-01-23)** |
| 385 | **Ch 6: Neutrinos Edge** | `sections/06_neutrinos_edge_modes.tex` | **YES (2026-01-23)** |
| 397 | Ch 7: CKM/CP | `sections/07_ckm_cp.tex` | YES (earlier) |
| 409 | Ch 8: G_F Derivation | `sections/11_gf_derivation.tex` | YES (earlier) |
| 421 | Ch 9: V-A Structure | `sections/09_va_structure.tex` | YES (earlier) |
| 433 | **Ch 10: Electroweak Bridge** | `sections/ch10_electroweak_bridge.tex` | **YES (2026-01-23)** |
| 445 | Ch 11: Epistemic Map | `sections/12_epistemic_map.tex` | NO |

### Part II: Technical Appendices (Block 3)

| Line | Section | File |
|------|---------|------|
| 448 | g5 Canonical/KK | `sections/ch11_g5_canonical_and_kk.tex` |
| 449 | g5 ell value | `sections/ch11_g5_ell_value_closure_attempt.tex` |
| 450 | g5 coefficient | `sections/ch11_g5_value_closure_attempt2_coefficient.tex` |
| 451 | g5 4pi derivation | `sections/ch11_g5_value_closure_attempt3_derive_4pi.tex` |
| 452 | g5 suppression | `sections/ch11_g5_ell_suppression_attempt2.tex` |
| 456 | OPR-20 forensic | `sections/ch11_opr20_factor8_forensic.tex` |
| 457 | OPR-20 attemptC | `sections/ch11_opr20_geometric_factor8_attemptC.tex` |
| 458 | OPR-20 attemptD | `sections/ch11_opr20_attemptD_interpretation_robin_overcount.tex` |
| 459 | OPR-20 attemptE | `sections/ch11_opr20_attemptE_prefactor8_derivation.tex` |
| 460 | OPR-20 attemptF | `sections/ch11_opr20_attemptF_mediator_bvp_junction.tex` |
| 461 | OPR-20 attemptG | `sections/ch11_opr20_attemptG_derive_alpha_from_action.tex` |
| 462 | OPR-20 BC | `sections/ch11_opr20_attemptG_BC_provenance.tex` |
| 463 | OPR-20 attemptH | `sections/ch11_opr20_attemptH_delta_equals_Rxi.tex` |
| 464 | OPR-20 H1 | `sections/ch11_opr20_attemptH1_mediator_identity.tex` |
| 465 | OPR-20 H2+ | `sections/ch11_opr20_attemptH2plus_delta_Rxi_stricter_audit.tex` |
| 469 | GF sanity | `sections/ch11_gf_sanity_skeleton.tex` |
| 470 | GF closure plan | `sections/ch11_gf_full_closure_plan.tex` |
| 495 | **BVP Work Package** | `sections/ch12_bvp_workpackage.tex` | **YES (2026-01-23)** |

### Meta Appendices

| Line | Section | File |
|------|---------|------|
| 721 | Meta Index | `meta_part2/00_meta_index.tex` |
| 722 | Claim Ledger | `meta_part2/01_claim_ledger.tex` |
| 723 | Decision Log | `meta_part2/02_decision_log.tex` |
| 724 | Research Timeline | `meta_part2/03_research_timeline.tex` |
| 725 | Evidence Map | `meta_part2/04_evidence_map.tex` |
| 726 | Historical Log | `meta_part2/05_historical_log_pointer.tex` |

---

## FILES NOT INCLUDED (orphans or alternatives)

| File | Reason |
|------|--------|
| `Z6_content.tex` (root) | Older version; `Z6_content_full.tex` is used |
| `EDC_Part_II_original.tex` | Older main file; `_rebuild.tex` is current |
| `sections/05_neutron_story.tex` | Not included (alternative?) |
| `sections/ch4_attempt3B_em_options.tex` | Sub-include of CH4? Check. |
| `sections/ch6_pmns_attempt*.tex` | Sub-includes of Ch6 (included via 06_neutrinos) |
| `sections/ch7_attempt*.tex` | Sub-includes of Ch7 (included via 07_ckm_cp) |

---

## NARRATIVE HARDENING STATUS (2026-01-23)

| Chapter | File | Status | Deliverables |
|---------|------|--------|--------------|
| Ch 3 (Electroweak) | `CH3_electroweak_parameters.tex` | **DONE** | PPN, Toy Model, 2 Fig, Closure box, IF/THEN, Failure |
| Ch 5 (3 Generations) | `sections/05_three_generations.tex` | **DONE** | PPN, Toy Model, 2 Fig, IF/THEN |
| Ch 6 (Neutrinos) | `sections/06_neutrinos_edge_modes.tex` | **DONE** | PPN, Toy Model, 2 Fig, IF/THEN, Failure |
| Ch 7 (CKM/CP) | `sections/07_ckm_cp.tex` | Earlier | - |
| Ch 8 (G_F) | `sections/11_gf_derivation.tex` | Earlier | - |
| Ch 9 (V-A) | `sections/09_va_structure.tex` | Earlier | - |
| **Ch 10 (EW Bridge)** | `sections/ch10_electroweak_bridge.tex` | **DONE** | PPN (9 steps), Toy Model, 2 Fig, OPR-20a/b summaries, IF/THEN |
| **Ch 12 (BVP)** | `sections/ch12_bvp_workpackage.tex` | **DONE** | PPN (8 steps), Toy Model, 2 Fig, F5/F6, IF/THEN, Dependency box |

---

## IMPORTANT NOTES

1. **ROOT vs sections/**: Some chapters are in root (`CH3_*.tex`, `CH4_*.tex`, `Z6_*.tex`), others in `sections/`. This is historical; consider consolidating.

2. **File naming inconsistency**:
   - `05_three_generations.tex` vs `05_case_neutron.tex` (same prefix, different content!)
   - `11_gf_derivation.tex` vs `11_gf_pathway.tex` (both start with 11_)
   - Recommend: rename to avoid confusion

3. **Sub-includes**: Ch6 and Ch7 include additional attempt files (ch6_pmns_attempt*.tex, ch7_attempt*.tex). These are part of those chapters.

4. **Backup location**: `backups/` directory contains pre-modification copies.

---

## QUICK REFERENCE: Which file to edit?

| If you want to edit... | Edit this file |
|------------------------|----------------|
| Weinberg angle / sin²θ_W / G_F via EW | `CH3_electroweak_parameters.tex` |
| Three generations / Z6 | `sections/05_three_generations.tex` |
| Neutrino edge modes / PMNS | `sections/06_neutrinos_edge_modes.tex` |
| CKM matrix / CP violation | `sections/07_ckm_cp.tex` |
| G_F detailed derivation | `sections/11_gf_derivation.tex` |
| V-A structure / chirality | `sections/09_va_structure.tex` |
| **Electroweak Bridge / OPR-20** | `sections/ch10_electroweak_bridge.tex` |
| BVP work package | `sections/ch12_bvp_workpackage.tex` |
| Epistemic status summary | `sections/12_epistemic_map.tex` |
