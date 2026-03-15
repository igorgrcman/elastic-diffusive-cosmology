# Acceptance Criteria — P20 (Derivation v11)

## AC-P20 Checklist

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-P20-1 | Work confined to derivation_v11 + PAPERS_INDEX update only | ✅ | Only files in derivation_v11/ created; PAPERS_INDEX.md updated |
| AC-P20-2 | FROZEN main.tex MD5 unchanged | ✅ | MD5 = `e592a943b1f5e6a48e661b9ed812109c` (verified) |
| AC-P20-3 | No forbidden observational calibration inputs used | ✅ | G_N^obs, M_Pl not used; finding is that σ *requires* calibration |
| AC-P20-4 | Outcome stated unambiguously | ✅ | **NO-GO** stated in abstract, Section 5, and REPORT.md |
| AC-P20-5 | Build: 0 undefined refs/cites; private paths 0 | ✅ | Build log shows 0 undefined |
| AC-P20-6 | Export naming policy respected; no EXPORT_TO_UPLOAD.pdf | ✅ | Export = `EDC_BLOCK003_DERIVATION_V11_SIGMA_FROM_FIELD_EQS.pdf` |
| AC-P20-7 | PAPERS_INDEX updated with MD5s + status | ✅ | Entry added with MD5s and NO-GO status |

---

## Verification Commands

```bash
# FROZEN check
md5 edc_papers/paper_gravity_block003/main.tex
# Expected: e592a943b1f5e6a48e661b9ed812109c

# No EXPORT_TO_UPLOAD.pdf
find edc_papers -name "EXPORT_TO_UPLOAD.pdf" -print
# Expected: (empty)

# Build clean
grep -c "undefined" derivation_v11/main.log
# Expected: 0
```

---

## Summary

All AC-P20 criteria satisfied. Derivation v11 complete with NO-GO outcome.
