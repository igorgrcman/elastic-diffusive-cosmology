# FORENSIC BUILD CONTEXT
# ======================
# Generated: 2026-01-24
# Purpose: Explain 277 vs 387 page difference
# Status: READ-ONLY analysis (no changes made)

## STEP 1 — Repository Context

```
pwd:              /Users/igor/ClaudeAI/EDC_Project/EDC_Research_PRIVATE
repo root:        /Users/igor/ClaudeAI/EDC_Project/EDC_Research_PRIVATE
branch:           restructure/paper3-companion-doi-split
HEAD:             6ad3fd0
```

**CRITICAL FINDING**: The 277 vs 387 page builds are in a DIFFERENT repository:
```
/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/
```

---

## STEP 2 — Build Artifacts Located

### 277-Page Build (MAIN)
```
Path:     .../20_book_chapter_weak_interface/paper/EDC_Part_II_Weak_Sector.pdf
Root TeX: .../20_book_chapter_weak_interface/paper/EDC_Part_II_Weak_Sector.tex
Built:    2026-01-24 12:15:52
Size:     1,266,196 bytes
Pages:    277
INPUT count: 660
```

### 387-Page Build (REBUILD SNAPSHOT)
```
Path:     .../20_book_chapter_weak_interface/paper/rebuild_part2_snapshot/paper/EDC_Part_II_Weak_Sector_rebuild.pdf
Root TeX: .../20_book_chapter_weak_interface/paper/rebuild_part2_snapshot/paper/EDC_Part_II_Weak_Sector_rebuild.tex
Built:    2026-01-24 07:59:59
Size:     1,685,050 bytes
Pages:    387
INPUT count: 815
```

---

## STEP 3 — Root Cause: Missing Sections

The 277-page build is missing **16 sections** that exist in the 387-page rebuild:

| # | Missing Section |
|---|-----------------|
| 1 | 02_frozen_regime_foundations.tex |
| 2 | ch10_electroweak_bridge.tex |
| 3 | ch11_g5_ell_suppression_attempt2.tex |
| 4 | ch11_g5_value_closure_attempt2_coefficient.tex |
| 5 | ch11_g5_value_closure_attempt3_derive_4pi.tex |
| 6 | ch11_opr20_attemptD_interpretation_robin_overcount.tex |
| 7 | ch11_opr20_attemptE_prefactor8_derivation.tex |
| 8 | ch11_opr20_attemptF_mediator_bvp_junction.tex |
| 9 | ch11_opr20_attemptG_BC_provenance.tex |
| 10 | ch11_opr20_attemptG_derive_alpha_from_action.tex |
| 11 | ch11_opr20_attemptH_delta_equals_Rxi.tex |
| 12 | ch11_opr20_attemptH1_mediator_identity.tex |
| 13 | ch11_opr20_attemptH2_delta_Rxi_hard_audit.tex |
| 14 | ch11_opr20_attemptH2plus_delta_Rxi_stricter_audit.tex |
| 15 | ch11_opr20_factor8_forensic.tex |
| 16 | ch11_opr20_geometric_factor8_attemptC.tex |

### CH3/CH4 Status
Both builds include CH3_electroweak_parameters.tex and CH4_lepton_mass_candidates.tex.
These are NOT the cause of the page difference.

---

## STEP 4 — Input Count Comparison

| Build | INPUT lines | Local .tex | Pages |
|-------|-------------|------------|-------|
| MAIN (277) | 660 | 35 sections | 277 |
| REBUILD (387) | 815 | 51 sections | 387 |

Difference: 815 - 660 = **155 additional INPUT lines** in rebuild
Difference: 51 - 35 = **16 additional sections** in rebuild

---

## STEP 5 — Conclusion

### Q1: Did the 277 build come from a different root .tex than the rebuild snapshot?
**YES.** Two different root files:
- MAIN: `EDC_Part_II_Weak_Sector.tex`
- REBUILD: `EDC_Part_II_Weak_Sector_rebuild.tex`

### Q2: What explains the difference?
**Different wiring/includes.** The main root .tex does not include the 16 sections listed above.
The rebuild root .tex includes all 51 sections.

### Q3: Is this a regression?
**UNKNOWN without historical context.** Possibilities:
1. Main build was intentionally stripped down (curated subset)
2. Main build is out of sync and missing \input commands
3. Rebuild is the "full" version, main is "published subset"

---

## Exact Paths (for copy/paste)

### MAIN BUILD (277 pages)
```
ROOT_TEX=/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/EDC_Part_II_Weak_Sector.tex
PDF=/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/EDC_Part_II_Weak_Sector.pdf
```

### REBUILD SNAPSHOT (387 pages)
```
ROOT_TEX=/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/rebuild_part2_snapshot/paper/EDC_Part_II_Weak_Sector_rebuild.tex
PDF=/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/rebuild_part2_snapshot/paper/EDC_Part_II_Weak_Sector_rebuild.pdf
```

---

## No Actions Taken

This is a READ-ONLY forensic report. No files were modified, no builds were run, no commits were made.

**Decision required**: Which is the canonical build target?
