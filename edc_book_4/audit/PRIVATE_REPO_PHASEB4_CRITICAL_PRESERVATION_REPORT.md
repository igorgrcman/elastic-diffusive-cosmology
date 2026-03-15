# Private Repo Phase B.4 Critical Preservation Report

**Date:** 2026-03-14
**Branch (private repo):** `restructure/paper3-companion-doi-split`
**Branch (main repo):** `research/topological-pinning-v7_8-integration`
**Scope:** Narrow source-only preservation of `derivations/critical/`
**Status:** Complete

---

## 1. Executive Verdict

The critical preservation commit was **completed successfully**. 5 source-only files
(2,951 lines) were committed and pushed to origin. All 5 are `.md` research documents
related to the α (fine-structure constant) 5D derivation program.

The cluster is small (12 total files) and clean — no build artifacts, no ambiguous
binaries, no PDFs. 7 of the 12 files were already tracked from a prior commit. The
remaining 5 were all clearly source-only and were committed without ambiguity.

Among the already-tracked files, 2 are high-value negative-result documents:
- `task_b5_power_derivation.md` — the documented G-exponent negative result (OPR-28 source)
- `EDC_Alpha_5D_Derivation_v1.md` — the α derivation negative result (now also committed)

No ambiguity remains.

---

## 2. Governing Inputs

| Document | Location | Role |
|----------|----------|------|
| `PRIVATE_REPO_WAVE1_EXECUTION_REPORT.md` | `edc_book_4/audit/` | Wave 1 baseline |
| `PRIVATE_REPO_PHASEB_TRIAGE_REPORT.md` | `edc_book_4/audit/` | Phase B triage (identified cluster) |
| `PRIVATE_REPO_PHASEB2_PRESERVATION_REPORT.md` | `edc_book_4/audit/` | Phase B.2 precedent (mass_difference) |
| `PRIVATE_REPO_PHASEB3_ANALYTIC_PRESERVATION_REPORT.md` | `edc_book_4/audit/` | Phase B.3 precedent (analytic) |
| `BOOK2_OPR_G_EXPONENT_AUDIT.md` | `edc_book_4/audit/` | OPR-28 (references task_b5) |
| `P_EPSILON_V11_AUDIT.md` | `edc_book_4/audit/` | P-ε assessment (analytic lane context) |

---

## 3. Target Cluster

| Property | Value |
|----------|-------|
| **Path** | `derivations/critical/` |
| **Why selected** | Phase B triage identified this as a smaller untracked cluster containing critical derivation documents, including `task_b5_power_derivation.md` (the source document for OPR-28) |
| **Why high-value** | Contains documented negative results for two major open problems (G-exponent powers, α derivation from 5D), epistemic classification audit (`EDC_Trijaza_v1`), and critical derivation attempts for proton structure |
| **Total files in cluster** | 12 |
| **Already tracked** | 7 files |
| **Untracked (committed in this pass)** | 5 files |
| **Build artifacts** | 0 |

---

## 4. Candidate File Register

### 4.1 Already Tracked Files (7 files — no action needed)

| File | Type | Category | Notes |
|------|------|----------|-------|
| `task_b5_power_derivation.md` | Negative result | Source / high-value | G-exponent negative result; OPR-28 source document |
| `EDC_56_DOF_Derivacija_v1.md` | Derivation | Source | κ = 5/6 DOF argument (Croatian) |
| `EDC_Alpha_Verification_v1.md` | Critical analysis | Source / negative-result | α = (4π+5/6)/(6π⁵) tautology check |
| `EDC_Cisti_Rezultati_v2.md` | Classification catalog | Source | Clean results catalog v2 (Croatian) |
| `EDC_Proton_PureDerivation_v2.md` | Derivation | Source | Pure proton derivation from P1-P6 (Croatian) |
| `EDC_Proton_Spherical_Symmetry_v1.md` | Derivation | Source | 4π from energy minimization (Croatian) |
| `EDC_Trijaza_v1.md` | Epistemic audit | Source / high-value | Classification of all 42 prior claims into D/I/Cal/P/rejected |

### 4.2 Untracked Files — INCLUDED in Commit (5 files)

| File | Lines | Type | Category | Included | Reason |
|------|-------|------|----------|----------|--------|
| `EDC_Alpha_5D_Derivation_v1.md` | 839 | Negative result | Source / high-value | **YES** | α derivation v1: NEGATIVE RESULT — all 3 routes blocked |
| `EDC_Alpha_5D_Derivation_v2.md` | 981 | Partial result | Source | **YES** | α derivation v2: corrects v1 error, identifies geometric structure |
| `EDC_Alpha_5D_Ledger_Update.md` | 345 | Ledger update | Source | **YES** | Records α status confirmation after v1 (remains [I]) |
| `EDC_Alpha_5D_Ledger_Update_v2.md` | 334 | Ledger update | Source | **YES** | Records v2 correction and partial success |
| `EDC_5D_KK_Reduction_IR_Screening.md` | 452 | Analytic derivation | Source | **YES** | 5D→4D KK reduction with IR screening |

### 4.3 Build Artifacts — EXCLUDED (0 files)

No build artifacts exist in this cluster. All 12 files are `.md` source documents.

---

## 5. Preservation Commit Performed

| Property | Value |
|----------|-------|
| **Repository** | `EDC_Research_PRIVATE` |
| **Branch** | `restructure/paper3-companion-doi-split` |
| **Commit hash** | `06f874d` |
| **Commit message** | `preserve: untracked critical derivation sources (alpha 5D derivations and KK reduction)` |
| **Files committed** | 5 |
| **Total lines** | 2,951 insertions |
| **Push status** | SUCCESS (`8c26d30..06f874d`) |
| **Push target** | `origin/restructure/paper3-companion-doi-split` |

---

## 6. Negative-Result / Critical Record Preservation

**4 negative-result or critical epistemic documents found in the cluster:**

| # | File | Type | Status | Why It Matters |
|---|------|------|--------|----------------|
| 1 | `task_b5_power_derivation.md` | G-exponent negative result | Already tracked | Documents that powers 12, 13 are NOT derived — source for OPR-28 |
| 2 | `EDC_Alpha_5D_Derivation_v1.md` | α derivation negative result | **Committed in this pass** | Documents 3 blocked routes for deriving α from 5D geometry |
| 3 | `EDC_Alpha_Verification_v1.md` | α tautology check | Already tracked | Critically honest assessment of whether α formula is derivation or tautology |
| 4 | `EDC_Trijaza_v1.md` | Epistemic classification audit | Already tracked | Classified 42 claims into D/I/Cal/P/rejected — found multiple "derivations" are actually identifications |

**Why they matter:**
- Negative-result documents prevent redundant investigation
- `task_b5_power_derivation.md` is the direct source for OPR-28
- `EDC_Alpha_5D_Derivation_v1.md` documents why α cannot currently be derived from 5D geometry
  (3 routes attempted, all blocked — missing lemma: independent derivation of e or σ)
- `EDC_Trijaza_v1.md` is a foundational epistemic audit that identified 3 circular claims
  among 42 total — this kind of self-critical assessment is high forensic value

All 4 negative-result / critical documents are now tracked on origin.

---

## 7. Excluded Files

**No files were excluded.** All 12 files in the cluster are `.md` source documents.
There are no build artifacts, no PDFs, no log files, no LaTeX intermediates, and
no `.DS_Store` in this cluster.

This is the cleanest of the three `derivations/` clusters preserved so far.

---

## 8. Remaining Ambiguities

**None.** All 12 files in `derivations/critical/` are clearly source-only textual
research documents. All are now tracked on origin (7 previously, 5 in this pass).

---

## 9. Effect on Private Repo Safety

**Materially improved.**

| Dimension | Before | After |
|-----------|--------|-------|
| `derivations/critical/` untracked source files | 5 untracked | 0 untracked (all committed) |
| Research content at risk of local disk loss | 2,951 lines in 5 files | 0 lines at risk |
| α negative-result document preserved | No (untracked) | Yes (committed) |
| Total tracked files in cluster | 7 / 12 | 12 / 12 |

Combined with Phase B.2 and B.3, all three `derivations/` sub-clusters are now
fully source-preserved on origin:
- `derivations/mass_difference/` — 12 files (Phase B.2)
- `derivations/analytic/` — 85 source files (Phase B.3)
- `derivations/critical/` — 12 files (7 prior + 5 in Phase B.4)

---

## 10. Recommended Next Step

**Assess the remaining private repo untracked clusters for a broader Phase C triage.**

The three `derivations/` sub-clusters are now fully preserved. The remaining untracked
material (~200+ entries across `releases/`, `kb/`, and smaller clusters) is less
urgent but should be triaged to identify any additional high-value research documents
at risk of loss.

---

## 11. Bottom Line

Phase B.4 preserved 5 source-only files (2,951 lines) from `derivations/critical/`,
completing the preservation of the entire `derivations/` tree in the private repo.
The cluster is exceptionally clean — all 12 files are `.md` research documents with
zero build artifacts. Among them, 4 are high-value negative-result or critical
epistemic documents, including the source for OPR-28 and a documented α derivation
failure. All `derivations/` sub-clusters are now fully source-preserved on origin.
