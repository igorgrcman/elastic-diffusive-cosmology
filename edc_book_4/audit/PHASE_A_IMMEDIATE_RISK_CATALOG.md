# Phase A Immediate Risk Catalog

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Seed catalog for immediate-risk assets — no relocation, no deletion,
no stash application, no Wave 1 push execution
**Status:** Seed layer only

---

## 1. Executive Verdict

This document seeds the first concrete catalog records for the highest-risk EDC
assets. It covers:

- **Cataloged:** 7 immediate-risk asset categories (unpushed main, 65 local-only
  branches, 4 stashes, private repo, 2 non-git research folders, standalone Book
  II copy, 44 untracked files)
- **Not yet cataloged:** File-level records, manuscript-level records, branch
  content-depth records, topic-level cross-links
- **Visibility:** The immediate-risk layer is now explicitly addressed. Every
  asset ranked Immediate Risk 1-10 in the governing plan has a catalog presence.

No material was moved, deleted, merged, overwritten, or pushed during this task.

---

## 2. Governing Inputs

| Document | Commit | Role |
|----------|--------|------|
| `FULL_FORENSIC_DISCOVERY_AND_INVENTORY.md` | `4af3f9e` | Primary factual base |
| `MASTER_CATALOG_AND_REORG_PLAN.md` | `ed13756` | Preservation rules, risk table, Protection Gate criteria |
| `MASTER_CATALOG_SCHEMA.md` | `ed13756` | Record types, field definitions, controlled vocabularies, ID convention |

---

## 3. Scope of Phase A

This phase catalogs **only** immediate-risk assets at seed depth. It:

- Assigns catalog IDs per `MASTER_CATALOG_SCHEMA.md` conventions
- Records preservation classes and risk levels
- Documents current status of each asset
- Identifies urgent deferred actions

This phase does **NOT**:

- Relocate any files or directories
- Delete any files, branches, or stashes
- Apply or pop any stashes
- Modify any branch (no merge, no rebase)
- Execute any Wave 1 push actions
- Run any network-facing git commands (`push`, `pull`, `fetch`)
- Rename any source files
- Overwrite any same-name files
- Create any new directories in the repo tree

---

## 4. Immediate-Risk Asset Register

| Catalog ID | Asset / Area | Type | Repo / Location | Current Status | Risk Basis | Preservation Class | Surfacing Priority | Notes |
|-----------|-------------|------|-----------------|---------------|-----------|-------------------|-------------------|-------|
| IR-001 | `main` ahead of `origin/main` | Branch (default) | `elastic-diffusive-cosmology_repo` | 14 commits ahead: `bd27917..9a7f570`. Includes Put C skeleton, Z3 argument tightening, dual-route merge, frozen-brane investigation, layout fixes. | Unpushed canonical work on default branch; disk failure = permanent loss | PC-ACTIVE | standard | HEAD at `bd27917`, origin/main at `9a7f570` |
| IR-002 | 65 local-only branches | Branch set | `elastic-diffusive-cosmology_repo` | 65 branches with no upstream tracking. Topics: audit/gap (9), OPR (20+), CKM/PMNS (5), G_F closure (8), notation (5), junction/core (8), epistemic reorg (3), misc (7). | No remote backup; disk failure = permanent loss of hundreds of thousands of lines | PC-LOCAL-BRANCH | standard | See §5 for full list |
| IR-003 | 4 git stashes | Stash set | `elastic-diffusive-cosmology_repo` | stash@{0}: WIP on `book-routeC-narrative-cleanup-v1`; stash@{1}: build artifacts on `book2-opr04-delta-derivation-v1`; stash@{2}: WIP on `part2-notation-canon-xi`; stash@{3}: WIP on OPR-20 suppression (`part2-gf-opr20-suppression-attempt2`) | Fragile; any `git stash drop/clear` destroys permanently | PC-STASH | standard | stash@{3} contains active OPR-20 research |
| IR-004 | `EDC_Research_PRIVATE/` | Separate git repo | `/Users/igor/ClaudeAI/EDC_Project/EDC_Research_PRIVATE/` | HAS remote: `origin` at `https://github.com/igorgrcman/EDC_Research.git`. 14 tracked branches (main + 13 neutron-pathB variants + restructure). **Backup status: PARTIALLY BACKED UP** — remote exists, but local-vs-remote sync state unknown without fetch. | Contains 30+ KB files, organized derivations, P7 program — unique material | PC-PRIVATE | standard | Remote exists but sync unknown |
| IR-005 | `current/` (12 files) | Non-git folder | `/Users/igor/ClaudeAI/EDC_Project/current/` | 12 files present. Croatian-language summaries, task derivations (a1-a3, b2, b4-b5), quick reference, findings. No version control. | No backup; any disk event or accidental deletion = permanent loss | PC-NONREPO | standard | Personal analysis in native language |
| IR-006 | `aside_proof_audit/` (5 files) | Non-git folder | `/Users/igor/ClaudeAI/EDC_Project/aside_proof_audit/` | 5 files: PROOF_LEDGER.md, MISSING_LEMMAS.md, CONSISTENCY_CHECKLIST.md, CLAIM_SITE_LOCATOR.md, SOURCE_MAP.csv. No version control. | No backup; unique audit infrastructure | PC-NONREPO | standard | Systematic proof verification |
| IR-007 | `EDC_Book_2/` standalone copy | Non-git folder | `/Users/igor/ClaudeAI/EDC_Project/EDC_Book_2/` | 2 files: `EDC_Book_II_main.tex` (53 KB), `EDC_Book_II_Emergent_Gravity.pdf` (368 KB). No version control. | May contain earlier/alternate Book II version not present elsewhere; overwrite risk if confused with `edc_book_2/` | PC-SNAPSHOT | standard | Needs comparison with `edc_book_2/reorganized/` |
| IR-008 | 44 untracked files in `edc_book_4/` | Untracked in git | `elastic-diffusive-cosmology_repo` working tree | 5 appendices (.tex), 4 code files (.py), 5 PDF builds, 2 .tex.bak files, 15+ audit reports (.md/.csv), build_info.tex, Makefile, tools/ dir, stray gravity copy | Not in git; `git clean -f` or careless checkout = permanent loss | PC-UNTRACKED | standard | Includes main_final.pdf, appendix sources, code |
| IR-009 | `edc_paper_2_archive/` | Non-git folder | `/Users/igor/ClaudeAI/EDC_Project/edc_paper_2_archive/` | Frozen Paper 2 release. Private assumption ledgers, traceability matrices. | Duplicate of some repo content, but private components may be unique | PC-SNAPSHOT | archival | Private release components need comparison |
| IR-010 | Standalone planning docs | Non-git files | `/Users/igor/ClaudeAI/EDC_Project/` root | `EDC_Clean_Core_Paper_Structure_with_Doc_References.txt` (7 KB), `EDC_Path_Forward_Claim_Ledger_and_Dependency_Graph.md` (4 KB) | No backup | PC-NONREPO | archival | Planning/structural documents |

---

## 5. Branch Seed Register

**Total local branches:** 83
**Local-only (no upstream):** 65
**Remote-tracked:** 18

### Full local-only branch list (65 branches)

| Branch Seed ID | Branch Name | Repo | Local-only? | Upstream | Known Topic | Why Immediate-Risk | Depth Needed |
|---------------|-------------|------|------------|----------|-------------|-------------------|-------------|
| BS-001 | `audit/donor-hunt-pass3-v1` | edc | YES | none | Gap donor hunt pass 3 | No remote | content-summary |
| BS-002 | `audit/donor-hunt-pmns-v1` | edc | YES | none | PMNS backfill candidates | No remote | content-summary |
| BS-003 | `audit/gap-register-full-v1` | edc | YES | none | Systematic 17-gap search (+18k lines) | No remote; large unique content | content-summary |
| BS-004 | `audit/prelet-scan-v1` | edc | YES | none | Prioritized Gap Register (90 entries) | No remote; planning infrastructure | content-summary |
| BS-005 | `backfill/pmns-theta23-v1` | edc | YES | none | PMNS θ₂₃ success case | No remote; positive result | content-summary |
| BS-006 | `backfill/tier0-v1` | edc | YES | none | GAP-4 sin²θ_W, GAP-10 G_F, GAP-1 V-A | No remote; critical gap fills | content-summary |
| BS-007 | `backfill/tier1-v1` | edc | YES | none | GAP-5 SSB, GAP-11 Yukawa, GAP-14 generations | No remote | content-summary |
| BS-008 | `backfill/tier2-v1` | edc | YES | none | GAP-8 θ₁₂, GAP-19 g₅ reduction | No remote | content-summary |
| BS-009 | `backfill/top5-v1` | edc | YES | none | Minimal donor derivations for critical gaps | No remote | content-summary |
| BS-010 | `backup-original-602pages` | edc | YES | none | Backup of original 602-page state | No remote; historical snapshot | verify-content |
| BS-011 | `book2-ch07-openq-remediation-v1` | edc | YES | none | Book 2 Ch07 open-question remediation | No remote | content-summary |
| BS-012 | `book2-ch1-asset-inventory-v1` | edc | YES | none | Symbol master table + context-aware audit | No remote; unique infrastructure | content-summary |
| BS-013 | `book2-ch1-audit-v1` | edc | YES | none | Book 2 Ch1 audit | No remote | content-summary |
| BS-014 | `book2-chapter-audit-v1` | edc | YES | none | Book 2 chapter-level audit | No remote | content-summary |
| BS-015 | `book2-cleanup20-legacy-v1` | edc | YES | none | Book 2 legacy cleanup | No remote | content-summary |
| BS-016 | `book2-figures-fill-placeholders-v1` | edc | YES | none | Book 2 figure placeholder fills | No remote | content-summary |
| BS-017 | `book2-global-symbol-table-v1` | edc | YES | none | Global symbol table + extraction tools | No remote; unique infrastructure | content-summary |
| BS-018 | `book2-neutron-dual-route-v1` | edc | YES | none | Neutron dual-route forensic audit | No remote | content-summary |
| BS-019 | `book2-open22-4-physical-veff-v1` | edc | YES | none | Physical V_eff derivation | No remote | content-summary |
| BS-020 | `book2-open22-4b-fd-robin-fix-v1` | edc | YES | none | Robin BC fix | No remote | content-summary |
| BS-021 | `book2-open22-4b-physical-mu-sweep-v1` | edc | YES | none | Physical mu-sweep | No remote | content-summary |
| BS-022 | `book2-open22-4b1-slice-family-v1` | edc | YES | none | Slice family analysis | No remote | content-summary |
| BS-023 | `book2-open22-f1-amplitude-v1` | edc | YES | none | f1 amplitude investigation | No remote | content-summary |
| BS-024 | `book2-opr-registry-v1` | edc | YES | none | Master OPR registry (verified 387 pages) | No remote; canonical registry | content-summary |
| BS-025 | `book2-opr01-sigma-anchor-v1` | edc | YES | none | OPR-01 sigma anchor derivation | No remote | content-summary |
| BS-026 | `book2-opr02-robin-alpha-from-action-v1` | edc | YES | none | Robin alpha from action | No remote | content-summary |
| BS-027 | `book2-opr04-delta-derivation-v1` | edc | YES | none | Delta derivation + TikZ | No remote | content-summary |
| BS-028 | `book2-opr04-delta-equals-Rxi-v1` | edc | YES | none | CH07 full coverage + delta_CP | No remote | content-summary |
| BS-029 | `book2-opr07-repropack-v1` | edc | YES | none | Physics-grade numerics infrastructure | No remote; unique code | content-summary |
| BS-030 | `book2-opr19-g5-derivation-v1` | edc | YES | none | g₅ normalization derivation | No remote | content-summary |
| BS-031 | `book2-opr20-mediator-mass-v1` | edc | YES | none | x_n definition fix | No remote | content-summary |
| BS-032 | `book2-opr21-closure-writeup-v1` | edc | YES | none | OPR-21 closure chapter (387→393 pages) | No remote; closure result | content-summary |
| BS-033 | `book2-opr21-physics-closure-v1` | edc | YES | none | V_eff and BC derivations | No remote | content-summary |
| BS-034 | `book2-opr21r-mu-window-recalibration-v1` | edc | YES | none | mu-window shape dependence | No remote | content-summary |
| BS-035 | `book2-opr21r-propagation-sweep-v1` | edc | YES | none | mu-window consistency sweep | No remote | content-summary |
| BS-036 | `book2-opr22-geff-derivation-v1` | edc | YES | none | Dimensional analysis fix for G_eff | No remote | content-summary |
| BS-037 | `book2-physical-path-lock-v1` | edc | YES | none | Canonical reader path for weak sector | No remote | content-summary |
| BS-038 | `book2-symbol-audit-remediation-v1` | edc | YES | none | Symbol audit remediation | No remote | content-summary |
| BS-039 | `delta-audit-anchor-v1` | edc | YES | none | Delta anchor map with Compton anchor | No remote | content-summary |
| BS-040 | `frozen-brane-bc-v1` | edc | YES | none | Dual-route proof (Route A + Route B) | No remote | content-summary |
| BS-041 | `helfrich-well-from-action-v1` | edc | YES | none | Helfrich route NO-GO (+12k lines, 18 files) | No remote; large forensic record | content-summary |
| BS-042 | `junction-core-derive-C-v1` | edc | YES | none | C derivation closes OPEN item | No remote | content-summary |
| BS-043 | `junction-core-well-v1` | edc | YES | none | Junction core well (+72k lines, 27 files) | No remote; LARGEST local-only branch | content-summary |
| BS-044 | `part2-bvp-workpackage-opr02-21` | edc | YES | none | BVP workpackage OPR-02 to OPR-21 | No remote | content-summary |
| BS-045 | `part2-ckm-attempt4-delta-refinement` | edc | YES | none | CKM attempt 4 with √2 bridge | No remote | content-summary |
| BS-046 | `part2-ckm-opr11-z2-parity` | edc | YES | none | Z₂ parity origin for CKM sign | No remote | content-summary |
| BS-047 | `part2-gf-g5-kk-tightening` | edc | YES | none | g₅ KK tightening | No remote | content-summary |
| BS-048 | `part2-gf-opr19-20-value-closure-attempt` | edc | YES | none | g₅ and l from membrane params | No remote | content-summary |
| BS-049 | `part2-gf-opr20-factor8-attempt3` | edc | YES | none | Factor-8 forensic attempt 3 | No remote; investigation record | content-summary |
| BS-050 | `part2-gf-opr20-factor8-forensic` | edc | YES | none | Factor-8 BC eigenvalue sweep | No remote; investigation record | content-summary |
| BS-051 | `part2-gf-opr20-factor8-geometric-attemptC` | edc | YES | none | Geometric factor-8 route | No remote; investigation record | content-summary |
| BS-052 | `part2-gf-opr20-suppression-attempt2` | edc | YES | none | f_geom = R_ξ/r_e suppression | No remote; also has stash@{3} | content-summary |
| BS-053 | `part2-gf-opr22-full-closure-plan` | edc | YES | none | G_F full closure plan | No remote | content-summary |
| BS-054 | `part2-gf-sanity-skeleton` | edc | YES | none | G_F sanity check skeleton | No remote | content-summary |
| BS-055 | `part2-notation-canon-xi` | edc | YES | none | Fix undefined refs in Part II | No remote; also has stash@{2} | content-summary |
| BS-056 | `part2-notation-mapping-keep-z` | edc | YES | none | z vs ξ mapping documentation | No remote | content-summary |
| BS-057 | `part2-notation-unify-zeta` | edc | YES | none | Why Option A not recommended | No remote | content-summary |
| BS-058 | `part2-orphan-notation-cleanup` | edc | YES | none | Orphan notation cleanup | No remote | content-summary |
| BS-059 | `part2-pmns-attempt4-2-theta12-origin` | edc | YES | none | θ₁₂ geometric origin arctan(1/√2) | No remote; specific result | content-summary |
| BS-060 | `part2-rebuild-snapshot-ch10-12` | edc | YES | none | Rebuild snapshot chapters 10-12 | No remote | verify-content |
| BS-061 | `putC-computation-v1` | edc | YES | none | S₅D→S_eff[q] reduction (+3.4k lines) | No remote; computation record | content-summary |
| BS-062 | `reorganization-epistemic-framework` | edc | YES | none | v2.0 epistemic framework (+16k, 46 files) | No remote; major structural work | content-summary |
| BS-063 | `taskB-derive-Mq-v1` | edc | YES | none | M(q) supermetric derivation | No remote | content-summary |
| BS-064 | `taskC-derive-Gamma0-v1` | edc | YES | none | Γ₀ prefactor from mode spectrum | No remote | content-summary |
| BS-065 | `taskD-bounce-scaling-audit-v1` | edc | YES | none | 2D bounce test NO-GO | No remote; negative result | content-summary |

---

## 6. Stash Seed Register

| Stash Seed ID | Repo | Stash Ref | Label / Message | Apparent Scope | Why Immediate-Risk | Next Step Later |
|--------------|------|-----------|----------------|---------------|-------------------|----------------|
| SS-001 | edc | `stash@{0}` | "WIP before reorganization branch" | On `book-routeC-narrative-cleanup-v1`. Narrative cleanup WIP. | Fragile; any `git stash drop` = permanent loss | Convert to named branch or inspect + commit |
| SS-002 | edc | `stash@{1}` | "build artifacts" | On `book2-opr04-delta-derivation-v1`. Build artifacts from delta derivation. | Fragile | Inspect; likely low-value build output but verify |
| SS-003 | edc | `stash@{2}` | "WIP before merge" | On `part2-notation-canon-xi`. Notation unification WIP. | Fragile; may contain notation decisions | Convert to branch or inspect + commit |
| SS-004 | edc | `stash@{3}` | "WIP on part2-gf-opr20-suppression-attempt2: 29d9192 OPR-20 suppression mechanism (Attempt A2): f_geom = R_xi/r_e" | On `part2-gf-opr20-suppression-attempt2`. Active OPR-20 research WIP with specific commit reference. | Fragile; contains active research on G_F factor-8 problem | Convert to named branch — highest-value stash |

---

## 7. Untracked / Outside-Version-Control Seed Register

### 7A. Non-git research folders

| Item ID | Path | Type | Why It Matters | Why Risky | Preservation Class | Next Catalog Step |
|---------|------|------|---------------|----------|-------------------|------------------|
| NR-001 | `/Users/igor/ClaudeAI/EDC_Project/current/EDC_Kompletni_Sazetak_Igor.md` | Croatian summary | Complete personal analysis in native language | No VCS, no backup | PC-NONREPO | Capture checksum, assess uniqueness |
| NR-002 | `/Users/igor/ClaudeAI/EDC_Project/current/EDC_Quick_Reference.md` | Quick reference | Fast-access EDC summary | No VCS | PC-NONREPO | Capture checksum |
| NR-003 | `/Users/igor/ClaudeAI/EDC_Project/current/EDC_Sto_Vrijedi_Sto_Ne.md` | What works/doesn't | Personal assessment of EDC validity | No VCS | PC-NONREPO | Capture checksum |
| NR-004 | `/Users/igor/ClaudeAI/EDC_Project/current/Nalaz_M_me_alpha.md` | M, m_e, α findings | Specific research finding | No VCS | PC-NONREPO | Capture checksum |
| NR-005 | `/Users/igor/ClaudeAI/EDC_Project/current/task_a1_euler_laplace_derivation.md` | Task A1 | Euler-Laplace derivation | No VCS | PC-NONREPO | Capture checksum |
| NR-006 | `/Users/igor/ClaudeAI/EDC_Project/current/task_a2_superposition_proof.md` | Task A2 | Superposition proof | No VCS | PC-NONREPO | Capture checksum |
| NR-007 | `/Users/igor/ClaudeAI/EDC_Project/current/task_a3_viscosity_bound.md` | Task A3 | Viscosity bound derivation | No VCS | PC-NONREPO | Capture checksum |
| NR-008 | `/Users/igor/ClaudeAI/EDC_Project/current/task_b2_REVISED_v2.md` | Task B2 revised | Revised vortex core derivation | No VCS | PC-NONREPO | Capture checksum |
| NR-009 | `/Users/igor/ClaudeAI/EDC_Project/current/Task_B2_Revision_Findings.md` | Task B2 findings | Revision findings | No VCS | PC-NONREPO | Capture checksum |
| NR-010 | `/Users/igor/ClaudeAI/EDC_Project/current/task_b4_F_bulk_derivation.md` | Task B4 | F_bulk derivation | No VCS | PC-NONREPO | Capture checksum |
| NR-011 | `/Users/igor/ClaudeAI/EDC_Project/current/task_b5_power_derivation.md` | Task B5 | Power derivation | No VCS | PC-NONREPO | Capture checksum |
| NR-012 | `/Users/igor/ClaudeAI/EDC_Project/current/Claude_Code_Dokumenti_Provjera.md` | Doc verification | Document verification checklist | No VCS | PC-NONREPO | Capture checksum |
| NR-013 | `/Users/igor/ClaudeAI/EDC_Project/aside_proof_audit/PROOF_LEDGER.md` | Proof ledger | Systematic proof verification infrastructure | No VCS; unique | PC-NONREPO | Capture checksum, high priority |
| NR-014 | `/Users/igor/ClaudeAI/EDC_Project/aside_proof_audit/MISSING_LEMMAS.md` | Missing lemmas | Identifies gaps in proof chain | No VCS; unique | PC-NONREPO | Capture checksum |
| NR-015 | `/Users/igor/ClaudeAI/EDC_Project/aside_proof_audit/CONSISTENCY_CHECKLIST.md` | Consistency check | Cross-consistency verification | No VCS; unique | PC-NONREPO | Capture checksum |
| NR-016 | `/Users/igor/ClaudeAI/EDC_Project/aside_proof_audit/CLAIM_SITE_LOCATOR.md` | Claim locator | Maps claims to source locations | No VCS; unique | PC-NONREPO | Capture checksum |
| NR-017 | `/Users/igor/ClaudeAI/EDC_Project/aside_proof_audit/SOURCE_MAP.csv` | Source map | Structured claim-source mapping | No VCS; unique | PC-NONREPO | Capture checksum |

### 7B. Standalone copies

| Item ID | Path | Type | Why It Matters | Why Risky | Preservation Class | Next Catalog Step |
|---------|------|------|---------------|----------|-------------------|------------------|
| NR-018 | `/Users/igor/ClaudeAI/EDC_Project/EDC_Book_2/EDC_Book_II_main.tex` | Standalone Book II tex | May be earlier/alternate version | No VCS; confusion risk with `edc_book_2/` | PC-SNAPSHOT | Compare with `edc_book_2/reorganized/main.tex` |
| NR-019 | `/Users/igor/ClaudeAI/EDC_Project/EDC_Book_2/EDC_Book_II_Emergent_Gravity.pdf` | Standalone Book II PDF | May capture a build state not in repo | No VCS | PC-SNAPSHOT | Compare with repo builds |

### 7C. Untracked files in git working tree (44 items)

| Item ID | Relative Path | Type | Content Category | Preservation Class |
|---------|--------------|------|-----------------|-------------------|
| UT-001 | `edc_book_4/CC_PROMPT_HEADER.md` | .md | Prompt/routing config | PC-UNTRACKED |
| UT-002 | `edc_book_4/CHRONOLOGY_MAP.md` | .md | Chronology map | PC-UNTRACKED |
| UT-003 | `edc_book_4/Makefile` | Makefile | Build infrastructure | PC-UNTRACKED |
| UT-004 | `edc_book_4/NARRATIVE_SPINE.md` | .md | Narrative architecture | PC-UNTRACKED |
| UT-005 | `edc_book_4/TODO.md` | .md | Task tracking | PC-UNTRACKED |
| UT-006 | `edc_book_4/appendices/appA_superheavy_code.tex` | .tex | Appendix source | PC-UNTRACKED |
| UT-007 | `edc_book_4/appendices/appB_kramers_code.tex` | .tex | Appendix source | PC-UNTRACKED |
| UT-008 | `edc_book_4/appendices/appD_provenance.tex` | .tex | Appendix source | PC-UNTRACKED |
| UT-009 | `edc_book_4/appendices/appQ_quarantine.tex` | .tex | Appendix source | PC-UNTRACKED |
| UT-010 | `edc_book_4/appendices/appX_analogies.tex` | .tex | Appendix source | PC-UNTRACKED |
| UT-011 | `edc_book_4/audit/CHAPTER_MAP.md` | .md | Chapter map | PC-UNTRACKED |
| UT-012 | `edc_book_4/audit/CONTAMINATION_FULL_REPORT.md` | .md | Audit report | PC-UNTRACKED |
| UT-013 | `edc_book_4/audit/EXTRACT_DEFINITIONS.csv` | .csv | Extract data | PC-UNTRACKED |
| UT-014 | `edc_book_4/audit/EXTRACT_DEFINITIONS_FINAL.csv` | .csv | Extract data | PC-UNTRACKED |
| UT-015 | `edc_book_4/audit/EXTRACT_EQUATIONS.csv` | .csv | Extract data | PC-UNTRACKED |
| UT-016 | `edc_book_4/audit/EXTRACT_EQUATIONS_FINAL.csv` | .csv | Extract data | PC-UNTRACKED |
| UT-017 | `edc_book_4/audit/EXTRACT_TABLES.csv` | .csv | Extract data | PC-UNTRACKED |
| UT-018 | `edc_book_4/audit/EXTRACT_TABLES_FINAL.csv` | .csv | Extract data | PC-UNTRACKED |
| UT-019 | `edc_book_4/audit/LABEL_REF_AUDIT.md` | .md | Audit report | PC-UNTRACKED |
| UT-020 | `edc_book_4/audit/LABEL_REF_AUDIT_FINAL.md` | .md | Audit report | PC-UNTRACKED |
| UT-021 | `edc_book_4/audit/PENDING_PLACEHOLDERS_REPORT.md` | .md | Audit report | PC-UNTRACKED |
| UT-022 | `edc_book_4/audit/POST_RUN_CHECK_REPORT.md` | .md | Build check report | PC-UNTRACKED |
| UT-023 | `edc_book_4/audit/POST_RUN_CHECK_REPORT_HARD.md` | .md | Build check report | PC-UNTRACKED |
| UT-024 | `edc_book_4/audit/POST_RUN_PREFACE_CH04_HARD.md` | .md | Build check report | PC-UNTRACKED |
| UT-025 | `edc_book_4/audit/PREFACE_PATCH_NOTE.md` | .md | Patch note | PC-UNTRACKED |
| UT-026 | `edc_book_4/audit/QA_SCAN_REPORT.md` | .md | QA report | PC-UNTRACKED |
| UT-027 | `edc_book_4/audit/RED_TEAM_MEMO.md` | .md | Red team review | PC-UNTRACKED |
| UT-028 | `edc_book_4/audit/RELEASE_FINGERPRINT.md` | .md | Release fingerprint | PC-UNTRACKED |
| UT-029 | `edc_book_4/audit/RELEASE_PACK.md` | .md | Release pack | PC-UNTRACKED |
| UT-030 | `edc_book_4/audit/TOC_FINAL.csv` | .csv | Table of contents | PC-UNTRACKED |
| UT-031 | `edc_book_4/build_info.tex` | .tex | Build metadata | PC-UNTRACKED |
| UT-032 | `edc_book_4/chapters/ch01_proton_ground.tex.bak` | .bak | Chapter backup | PC-UNTRACKED |
| UT-033 | `edc_book_4/chapters/ch03_neutron_metastable.tex.bak` | .bak | Chapter backup | PC-UNTRACKED |
| UT-034 | `edc_book_4/code/book4_highcoord_predictions.py` | .py | Computation code | PC-UNTRACKED |
| UT-035 | `edc_book_4/code/book4_kramers_validation.py` | .py | Validation code | PC-UNTRACKED |
| UT-036 | `edc_book_4/code/kramers_double_well_v2.py` | .py | Kramers code | PC-UNTRACKED |
| UT-037 | `edc_book_4/code/superheavy_predictions.py` | .py | Prediction code | PC-UNTRACKED |
| UT-038 | `edc_book_4/main.pdf` | .pdf | Current build PDF | PC-UNTRACKED |
| UT-039 | `edc_book_4/main_216_pages_12022061014.pdf` | .pdf | Dated snapshot | PC-UNTRACKED |
| UT-040 | `edc_book_4/main_224_pages.pdf` | .pdf | Dated snapshot | PC-UNTRACKED |
| UT-041 | `edc_book_4/main_228_pages.pdf` | .pdf | Dated snapshot | PC-UNTRACKED |
| UT-042 | `edc_book_4/main_final.pdf` | .pdf | Final build PDF | PC-UNTRACKED |
| UT-043 | `edc_book_4/tools/` | dir | Tool scripts | PC-UNTRACKED |
| UT-044 | `edc_papers/paper_gravity_block003/edc_book_4/` | dir | Stray copy of book4 in gravity dir | PC-UNTRACKED |

---

## 8. Book II Priority Record

**Catalog ID:** M-edc-main-002 (schema-compliant manuscript ID)

**Location:** `edc_book_2/reorganized/main.tex` (canonical driver)
with supporting material in `edc_book_2/src/`, `edc_book_2/build/`,
`edc_book_2/canon/`, `edc_book_2/code/`, `edc_book_2/audit/`

**What makes it special:**
- Full 17-chapter `\documentclass{book}` manuscript, not a note or sketch
- Three parts covering the complete weak sector: Foundations, Electroweak, BVP/G_F
- Contains the five-category particle classification (`04_ontology.tex`)
- Contains per-particle case studies for neutron, muon, tau, pion, electron, neutrino
- Has its own OPR registry (22+ entries) and audit evidence directory (17+ reports)
- Has 16 Python computation scripts
- Has multiple build PDFs including a verified 387-page state
- Confirmed as developed by `FULL_FORENSIC_DISCOVERY_AND_INVENTORY.md` (commit `4af3f9e`)

**Why it is not just another artifact:**
Book II contains exactly the particle anatomy, decay ontology, and weak-sector
derivation material that is being actively searched for in the current research
program. It was identified by the `PARTICLE_ANATOMY_AND_DECAY_REDISCOVERY_INDEX.md`
as the primary ontology hub.

**Surfacing priority:** `first_class` (per `MASTER_CATALOG_SCHEMA.md` §4.7)

**Later catalog depth required:**
- Chapter-level content map
- Cross-reference links to Book IV and paper_3_series
- Comparison with standalone `EDC_Book_2/` copy (NR-018, NR-019)
- Assessment of which 20+ local-only OPR branches feed into it

**Operational fragility:**
Book II is in a stable repo location on `main` branch. However:
- `main` is 14 commits ahead of `origin/main` (IR-001), so it is not
  fully backed up to remote
- 20+ OPR-related local-only branches contain derivation work that
  feeds into Book II chapters but exists only locally
- The standalone `EDC_Book_2/` copy (NR-018) has not been compared

---

## 9. Same-Name File Risk Note

The forensic inventory identified 97 files named `main.tex` and numerous files
named `main.pdf` across the repo. At the Phase A seed level, the relevant
same-name risks are:

- **`main.pdf` untracked instances:** UT-038 (`edc_book_4/main.pdf`) is one of
  5 untracked PDFs with similar basenames. Any bulk `git clean` or careless copy
  could overwrite these distinct artifacts.

- **`main.tex` across books:** `edc_book/main.tex` (Book I), `edc_book_2/reorganized/main.tex`
  (Book II), `edc_book_4/main.tex` (Book IV) are three entirely different books
  sharing the same basename. Any re-housing that flattens directory structure
  would create overwrite collisions.

- **Standalone copy risk:** `EDC_Book_2/EDC_Book_II_main.tex` (NR-018) is
  NOT named `main.tex` but IS a version of the same conceptual document as
  `edc_book_2/reorganized/main.tex`. Confusion between these is a provenance
  risk even without name collision.

The no-overwrite rule from `MASTER_CATALOG_AND_REORG_PLAN.md` §12 applies.
No future re-housing may place same-basename files in the same directory
without disambiguation.

---

## 10. Urgent But Deferred Wave 1 Actions

| Action | Why Urgent | Why Deferred | Later Owner |
|--------|-----------|-------------|-------------|
| `git push origin main` | 14 unpushed commits on default branch; disk failure = permanent loss | This prompt explicitly forbids network-facing git commands | Next prompt with explicit push authorization |
| Push all 65 local-only branches to `origin` | Hundreds of thousands of lines of unique computation/research exist only locally | Network-facing; also needs review of whether all branch names are safe to push as-is | Next prompt with explicit push authorization |
| Verify `EDC_Research_PRIVATE` sync with `origin` | Remote exists (`github.com/igorgrcman/EDC_Research.git`) but sync state unknown without `git fetch` | Network-facing; also requires `cd` into private repo | Next prompt with explicit push authorization |
| Convert 4 stashes to named branches | Stashes are fragile; accidental `drop`/`clear` = permanent loss | Stash-to-branch conversion modifies git state beyond catalog scope | Next prompt with explicit stash conversion authorization |
| Commit 44 untracked files in `edc_book_4/` | Not in git; `git clean` = permanent loss | Requires careful review of which files belong in git vs. .gitignore | Next prompt with explicit commit authorization |
| Archive `current/` and `aside_proof_audit/` to preservation branch | No VCS; disk event = permanent loss | Requires creating new branch and copying files into repo | Next prompt with explicit archive authorization |

---

## 11. What Phase A Did NOT Do

- **No relocation.** No files were moved between directories.
- **No merge.** No branches were merged.
- **No rename.** No source files were renamed.
- **No deduplication.** No duplicates were resolved.
- **No overwrite.** No same-name files were copied over each other.
- **No archival housing.** No new umbrella directories were created.
- **No push execution.** No `git push`, `git pull`, `git fetch`, or any
  network-facing git command was run.
- **No stash application.** No stashes were applied, popped, or dropped.
- **No branch modification.** No branches were created, deleted, or modified
  (beyond the current branch receiving this catalog commit).
- **No content-depth catalog.** Branch content was identified by name and topic
  only; full content-depth records (file lists, diff stats, include trees)
  remain for Phase B.

---

## 12. Recommended Phase A.2 Next Step

**Execute Wave 1 protection actions** (from `MASTER_CATALOG_AND_REORG_PLAN.md`
§16) in a dedicated prompt with explicit authorization for:

1. Push `main` to `origin/main`
2. Push all 65 local-only branches to `origin`
3. Verify `EDC_Research_PRIVATE` sync state
4. Convert 4 stashes to named branches and push
5. Commit untracked research files in `edc_book_4/`
6. Archive non-git research folders to a preservation branch

After Wave 1, create `PROTECTION_GATE_PASSAGE.md` confirming PG-1 through PG-8.

---

## 13. Bottom Line

The immediate-risk layer is now visible. Every asset ranked as immediate risk
in the governing plan has a catalog ID, preservation class, and risk basis.
The 65 local-only branches are enumerated by name. The 4 stashes are recorded
with their messages. The 44 untracked files are listed. The non-git research
folders are itemized. Book II is explicitly marked as first-class surfacing
priority.

Nothing has been moved, deleted, merged, pushed, or overwritten. The catalog
exists as a seed layer only. The urgent Wave 1 actions are staged but deferred
pending explicit authorization. The Protection Gate remains unpassed.
