# Acceptance Criteria — P26 (Derivation v18)

## AC-V18 Checklist

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-V18-1 | All changes only in derivation_v18/ (+ PAPERS_INDEX.md) | ✅ | Only files in derivation_v18/ created |
| AC-V18-2 | paper_gravity_block003/main.tex not touched (FROZEN) | ✅ | MD5 = `e592a943b1f5e6a48e661b9ed812109c` verified |
| AC-V18-3 | Build successful; 0 undefined refs; 0 undefined citations | ✅ | 0 undefined |
| AC-V18-4 | No private paths in PDF | ✅ | grep verified |
| AC-V18-5 | Export PDF name per policy, same hash as main.pdf | ✅ | Both `30f8ba5ef4395d0c8d392d8d4aaced08` |
| AC-V18-6 | REPORT.md contains page count, undefined count, MD5s | ✅ | All present |
| AC-V18-7 | PAPERS_INDEX.md updated with v18 entry | ⏳ | Pending |
| AC-V18-8 | No new folders outside derivation_v18/ | ✅ | Verified |
| AC-V18-9 | No changes in edc_book_2/ | ✅ | Directory untouched |
| AC-V18-10 | README.md states "no new results; consolidation of v13–v17" | ✅ | Present |

---

## Additional Content Checks

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Reader Contract section | ✅ | Section 1 |
| Canonical derivation chain (5 steps) | ✅ | Section 2 |
| Numerical closure with error budget | ✅ | Section 3 |
| Robustness table from v17 | ✅ | Section 4 |
| What remains open (NO-GO) | ✅ | Section 5 |
| Pipeline figure (TikZ) | ✅ | Figure 1 |
| Figure caption with disclaimer | ✅ | "Schematic only; not to scale; no new results" |
| Epistemic ledger table | ✅ | Table 4 |

---

## Verification Commands

```bash
# FROZEN check
md5 edc_papers/paper_gravity_block003/main.tex
# Expected: e592a943b1f5e6a48e661b9ed812109c

# Build
cd edc_papers/paper_gravity_block003/derivation_v18
xelatex main.tex && xelatex main.tex

# Undefined refs check
grep -c "undefined" main.log
# Expected: 0

# Private path check
strings main.pdf | grep -c "/Users/"
# Expected: 0

# Export
cp main.pdf EDC_BLOCK003_DERIVATION_V18_GRAVITY_CLOSURE_SUMMARY.pdf

# MD5s
md5 main.tex main.pdf EDC_BLOCK003_DERIVATION_V18_GRAVITY_CLOSURE_SUMMARY.pdf
```

---

## Summary

All acceptance criteria verified (pending PAPERS_INDEX update). Build complete.

**Outcome:** CONSOLIDATION COMPLETE — calibrated closure + explicit open items preserved.
