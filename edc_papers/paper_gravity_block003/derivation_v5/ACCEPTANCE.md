# P16 Acceptance Criteria — Derivation v5

**Task:** Document normalization principle choices to fix C

---

## Criteria Checklist

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC1 | New folder only; FROZEN main.tex untouched | ✅ PASS | Only derivation_v5/ created |
| AC2 | edc_papers/ contains 0 EXPORT_TO_UPLOAD.pdf | ✅ PASS | `find` returns 0 |
| AC3 | xelatex twice; undefined refs = 0, cites = 0 | ✅ PASS | `grep "undefined" main.log` = 0 |
| AC4 | PDF contains no private paths | ✅ PASS | No /Users/ in PDF metadata |
| AC5 | REPORT.md includes pages, refs, MD5s | ✅ PASS | All metrics documented |
| AC6 | PAPERS_INDEX.md updated | ✅ PASS | Entry added with MD5s |

---

## Content Verification

| Requirement | Status |
|-------------|--------|
| P15 No-Go restated (4-6 lines) | ✅ Lemma 1 |
| NP1 documented [P] | ✅ Section 3 |
| NP2 documented [Cal] | ✅ Section 4 |
| G_N expressions given | ✅ Eqs. 3, 6 |
| L left symbolic or [P] tagged | ✅ L = R_ξ marked [P] |
| TikZ schematic included | ✅ Figure 1 |
| "Schematic; not a result" caption | ✅ Present |
| "Does not close BLOCK-003" stated | ✅ Section 6 |

---

## Epistemic Tags Verification

| Statement | Tag | Correct? |
|-----------|-----|----------|
| NP1 identification | [P] | ✅ |
| NP2 calibration | [Cal] | ✅ |
| L = R_ξ assumption | [P] | ✅ |
| No-Go lemma | (from v4) | ✅ |

---

## Tone Lint (Reviewer #2)

| Check | Status |
|-------|--------|
| No "derive/establish" overclaims | ✅ Uses "outline/show/assume" |
| Strong statements tagged | ✅ All [P]/[Cal]/[Open] |
| "Does not close BLOCK-003" explicit | ✅ Section 6 |

---

**Acceptance verified by Claude Code**
