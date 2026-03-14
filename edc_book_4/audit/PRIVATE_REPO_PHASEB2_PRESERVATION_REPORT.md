# Private Repo Phase B.2 Preservation Report

**Date:** 2026-03-14
**Branch (private repo):** `restructure/paper3-companion-doi-split`
**Branch (main repo):** `research/topological-pinning-v7_8-integration`
**Scope:** Narrow source-only preservation commit for `derivations/mass_difference/`
**Status:** Complete

---

## 1. Executive Verdict

The narrow preservation commit was **completed successfully**. 12 source-only files
(8 `.md` + 4 `.tex`, totaling 6,575 lines) were committed and pushed to origin. No
build artifacts, no PDFs, no logs, no ambiguous files were included. The commit is
narrow, coherent, and source-only.

Minor ambiguity remains in the cluster: 9 excluded files (4 `.log`, 3 `.pdf`, 1 `.log`
in subdirectory, 1 `.pdf` with space in filename) are build artifacts that remain
untracked. These are regenerable and present no preservation risk.

---

## 2. Governing Inputs

| Document | Location | Role |
|----------|----------|------|
| `PRIVATE_REPO_WAVE1_EXECUTION_REPORT.md` | `edc_book_4/audit/` | Wave 1 baseline |
| `PRIVATE_REPO_WAVE1_STATUS.md` | `edc_book_4/audit/` | Wave 1 status |
| `PRIVATE_REPO_PHASEB_TRIAGE_REPORT.md` | `edc_book_4/audit/` | Phase B triage (identified this cluster) |
| `PRIVATE_REPO_PHASEB_STATUS.md` | `edc_book_4/audit/` | Phase B status (recommended this action) |

---

## 3. Target Cluster

| Property | Value |
|----------|-------|
| **Path** | `derivations/mass_difference/` (+ one subdirectory file) |
| **Why selected** | Phase B identified this as the narrowest, safest, highest-value preservation target |
| **Why safe** | All 12 files are clearly research source (.md research notes, .tex derivation papers); no ambiguous binaries; coherent single-topic cluster (neutron-proton mass difference + 5D topology) |
| **Total untracked before** | 21 files in cluster |
| **Source-only subset** | 12 files (all .md and .tex) |
| **Excluded** | 9 files (all build artifacts: .log, .pdf) |

---

## 4. Candidate File Assessment

| # | File Path | Type | Lines | Include? | Reason | Notes |
|---|-----------|------|-------|----------|--------|-------|
| 1 | `derivations/mass_difference/AUDIT_Neutron_Proton_Derivation.md` | Research audit | 226 | **YES** | Source research document | Audit of derivation quality |
| 2 | `derivations/mass_difference/COMPANION_STRUCTURE.md` | Structure doc | 131 | **YES** | Source document | Paper 3 companion F and G structure |
| 3 | `derivations/mass_difference/EDC_Neutron_Junction_Oscillation_Model.tex` | LaTeX source | 1,005 | **YES** | Derivation paper source | Neutron junction oscillation model |
| 4 | `derivations/mass_difference/EDC_Neutron_Proton_Derivation.tex` | LaTeX source | 818 | **YES** | Derivation paper source | Core neutron-proton derivation |
| 5 | `derivations/mass_difference/EDC_Proton_Junction_Model.tex` | LaTeX source | 896 | **YES** | Derivation paper source | Proton junction model |
| 6 | `derivations/mass_difference/H2_MOLECULE_5D_Investigation.md` | Research note | 604 | **YES** | Source research document | H₂ molecule from 5D perspective |
| 7 | `derivations/mass_difference/HYDROGEN_5D_Investigation.md` | Research note | 666 | **YES** | Source research document | Hydrogen atom from 5D perspective |
| 8 | `derivations/mass_difference/HYPOTHESIS_Antimatter_5D_Conservation_Artifact.md` | Hypothesis doc | 381 | **YES** | Source research document | Antimatter as 5D conservation artifact |
| 9 | `derivations/mass_difference/Mass_As_Inflow_Resistance_Investigation.md` | Research note | 694 | **YES** | Source research document | Mass as resistance to 5D inflow |
| 10 | `derivations/mass_difference/PATCH_SUMMARY_NEUTRON_OSCILLATION_MODEL.md` | Patch summary | 176 | **YES** | Source document | Companion H patch summary |
| 11 | `derivations/mass_difference/SYNTHESIS_Mass_Inflow_Complete_Picture.md` | Synthesis doc | 507 | **YES** | Source research document | Mass inflow complete picture |
| 12 | `derivations/mass_difference/paper/framework/sections/08_gravity_topological_ops.tex` | LaTeX source | 471 | **YES** | Framework section source | Gravity + topological ops (KK reduction) |
| 13 | `derivations/mass_difference/EDC_5D_Complete_Mathematical_Framework.log` | Build log | — | **NO** | Build artifact | Regenerable from .tex |
| 14 | `derivations/mass_difference/EDC_Neutron_Junction_Oscillation_Model.log` | Build log | — | **NO** | Build artifact | Regenerable from .tex |
| 15 | `derivations/mass_difference/EDC_Neutron_Junction_Oscillation_Model.pdf` | Compiled PDF | — | **NO** | Build output | Regenerable from .tex |
| 16 | `derivations/mass_difference/EDC_Neutron_Proton_Derivation.log` | Build log | — | **NO** | Build artifact | Regenerable from .tex |
| 17 | `derivations/mass_difference/EDC_Neutron_Proton_Derivation.pdf` | Compiled PDF | — | **NO** | Build output | Regenerable from .tex |
| 18 | `derivations/mass_difference/EDC_Proton_Junction_Model.log` | Build log | — | **NO** | Build artifact | Regenerable from .tex |
| 19 | `derivations/mass_difference/EDC_Proton_Junction_Model.pdf` | Compiled PDF | — | **NO** | Build output | Regenerable from .tex |
| 20 | `derivations/mass_difference/paper/EDC_Weak_Interactions_5D_Model.log` | Build log | — | **NO** | Build artifact | Regenerable |
| 21 | `derivations/mass_difference/paper/framework/5D Brane-World...pdf` | Named PDF | — | **NO** | Binary with space in name | Ambiguous provenance; defer |

---

## 5. Preservation Commit Performed

| Property | Value |
|----------|-------|
| **Repository** | `EDC_Research_PRIVATE` (`https://github.com/igorgrcman/EDC_Research.git`) |
| **Branch** | `restructure/paper3-companion-doi-split` |
| **Commit hash** | `203771e` |
| **Commit message** | `preserve: untracked mass-difference research sources + gravity topology section` |
| **Files committed** | 12 (8 `.md` + 4 `.tex`) |
| **Total lines** | 6,575 insertions |
| **Push status** | SUCCESS (`6ad3fd0..203771e`) |
| **Push target** | `origin/restructure/paper3-companion-doi-split` |

---

## 6. Excluded Files

| # | File | Reason |
|---|------|--------|
| 1 | `EDC_5D_Complete_Mathematical_Framework.log` | Build artifact (LaTeX log) — regenerable |
| 2 | `EDC_Neutron_Junction_Oscillation_Model.log` | Build artifact (LaTeX log) — regenerable |
| 3 | `EDC_Neutron_Junction_Oscillation_Model.pdf` | Compiled PDF — regenerable from committed .tex |
| 4 | `EDC_Neutron_Proton_Derivation.log` | Build artifact (LaTeX log) — regenerable |
| 5 | `EDC_Neutron_Proton_Derivation.pdf` | Compiled PDF — regenerable from committed .tex |
| 6 | `EDC_Proton_Junction_Model.log` | Build artifact (LaTeX log) — regenerable |
| 7 | `EDC_Proton_Junction_Model.pdf` | Compiled PDF — regenerable from committed .tex |
| 8 | `paper/EDC_Weak_Interactions_5D_Model.log` | Build artifact (LaTeX log) — regenerable |
| 9 | `paper/framework/5D Brane-World Framework for Particle Properties.pdf` | Named PDF with space in filename — ambiguous provenance, deferred |

All excluded files are either regenerable build artifacts or ambiguous binaries.
None contain unique research content that is not recoverable from the committed sources.

---

## 7. Remaining Ambiguities

| # | Item | Nature | Risk |
|---|------|--------|------|
| 1 | `5D Brane-World Framework for Particle Properties.pdf` | Named PDF with space in filename — may be a reference document or external paper, not clearly regenerable from committed .tex | LOW — if it's an external reference, it exists elsewhere; if compiled, source is committed |
| 2 | Whether the 3 excluded `.pdf` files are "canonical" compiled outputs | They match committed .tex source names, so they're almost certainly regenerable | VERY LOW |

No high-ambiguity items remain.

---

## 8. Effect on Private Repo Safety

**Materially improved.**

| Dimension | Before | After |
|-----------|--------|-------|
| `derivations/mass_difference/` untracked source files | 12 untracked | 0 untracked (all committed) |
| Research content at risk of local disk loss | 6,575 lines in 12 files | 0 lines at risk (all on origin) |
| `08_gravity_topological_ops.tex` (gravity/KK section) | Untracked | Committed and pushed |
| Remaining untracked in cluster | 21 files | 9 files (all build artifacts) |

The 12 most valuable files in this cluster — all research source — are now durably
versioned and pushed to origin. The remaining 9 files are build artifacts that can be
regenerated from the committed sources.

---

## 9. Recommended Next Step

**Assess and optionally preserve `derivations/analytic/` source files.**

This is the next-largest untracked research cluster (~73 files including `.md` research
notes, `.tex` derivations, and failure certificates). It contains:
- 11 versioned failure certificates (v1–v11)
- 11 derivation ledger versions (v3–v11)
- Multiple `.tex` derivation files (FROZEN, PEPSILON, PJUNCTION, etc.)
- Action-from-principle derivation attempts

A similar narrow source-only preservation pass (excluding `.pdf` and build artifacts)
would further reduce preservation risk.

---

## 10. Bottom Line

Phase B.2 completed its single mission: a narrow, source-only preservation commit of
12 research files (6,575 lines) from `derivations/mass_difference/` in the private repo.
The commit (`203771e`) is pushed to origin. No build artifacts, no PDFs, no ambiguous
files were included. The narrow-commit rule held. The most valuable untracked research
content in this cluster is now durably preserved.
