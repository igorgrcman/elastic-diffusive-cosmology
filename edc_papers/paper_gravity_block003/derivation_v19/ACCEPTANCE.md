# Acceptance Criteria — P27 (Derivation v19)

## Scope Rules

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-V19-1 | Work only in derivation_v19/ | ✅ | Only files in derivation_v19/ created |
| AC-V19-2 | FROZEN main.tex untouched | ✅ | MD5 = `e592a943b1f5e6a48e661b9ed812109c` |
| AC-V19-3 | No changes to v1–v18 | ✅ | Untouched |
| AC-V19-4 | No changes to edc_book_2/ | ✅ | Untouched |
| AC-V19-5 | No fitting to G_N^obs | ✅ | Only structural derivation |
| AC-V19-6 | Export naming policy | ✅ | `EDC_BLOCK003_DERIVATION_V19_DERIVATION_FIRST.pdf` |

---

## Derivation Steps Present

| ID | Required Content | Status | Location |
|----|------------------|--------|----------|
| AC-V19-7 | 5D manifold + bulk action defined | ✅ | Section 1 |
| AC-V19-8 | Israel junction conditions | ✅ | Section 1.3, Eq. (5)-(6) |
| AC-V19-9 | Linearized gravity + gauge | ✅ | Section 2.1-2.2 |
| AC-V19-10 | KK decomposition explicit | ✅ | Section 2.2, Eq. (9) |
| AC-V19-11 | Mode equation derived | ✅ | Section 2.3, Eq. (11) |
| AC-V19-12 | Zero-mode solution | ✅ | Section 2.4, Eq. (14)-(16) |
| AC-V19-13 | Normalization integral DERIVED | ✅ | Section 3, Eq. (17)-(26) |
| AC-V19-14 | Compact flat $\mathcal{I}=R_\xi$ computed | ✅ | Section 4, Eq. (27)-(36) |
| AC-V19-15 | Newton constant bridge | ✅ | Section 5, Eq. (37)-(41) |
| AC-V19-16 | Non-compact remark | ✅ | Section 5.4 |
| AC-V19-17 | Calibrated closure | ✅ | Section 6 |
| AC-V19-18 | Epistemic tags | ✅ | Throughout + Table 3 |
| AC-V19-19 | Robustness table | ✅ | Section 7, Table 2 |

---

## Page Target

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-V19-20 | Pages ≥ 7 | ✅ | 7 pages |
| AC-V19-21 | Displayed equations ≥ 12 (Sections 2-5) | ✅ | 35+ equations |

---

## Build Verification

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-V19-22 | Undefined refs = 0 | ✅ | grep verified |
| AC-V19-23 | Undefined citations = 0 | ✅ | grep verified |
| AC-V19-24 | Private paths = 0 | ✅ | strings verified |
| AC-V19-25 | Export PDF matches main.pdf | ✅ | Same MD5 |
| AC-V19-26 | No EXPORT_TO_UPLOAD.pdf | ✅ | Verified |
| AC-V19-27 | PAPERS_INDEX.md updated | ⏳ | Pending |

---

## Verification Commands

```bash
# FROZEN check
md5 edc_papers/paper_gravity_block003/main.tex
# Expected: e592a943b1f5e6a48e661b9ed812109c

# Build
cd edc_papers/paper_gravity_block003/derivation_v19
xelatex main.tex && xelatex main.tex && xelatex main.tex

# Undefined refs check
grep -c "undefined" main.log
# Expected: 0

# Private path check
strings main.pdf | grep -c "/Users/"
# Expected: 0

# Equation count (rough)
grep -c "\\\\begin{equation}" main.tex
# Expected: ≥ 30

# MD5s
md5 main.tex main.pdf EDC_BLOCK003_DERIVATION_V19_DERIVATION_FIRST.pdf
```

---

## Summary

All acceptance criteria verified (pending PAPERS_INDEX update). Build complete.

**Outcome:** Derivation-first writeup complete; calibrated closure with explicit steps;
internal $R_\xi$ derivation NO-GO preserved.
