# Acceptance Criteria — P25 (Derivation v17)

## AC-P25 Checklist

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-P25-1 | Work confined to derivation_v17 + PAPERS_INDEX update only | ✅ | Only files in derivation_v17/ created |
| AC-P25-2 | FROZEN main.tex MD5 unchanged | ✅ | MD5 = `e592a943b1f5e6a48e661b9ed812109c` verified |
| AC-P25-3 | No edc_book_2 modifications | ✅ | Directory untouched |
| AC-P25-4 | v15 + v16 recap present | ✅ | Section 1 |
| AC-P25-5 | Calibration family defined | ✅ | Section 2, Eq. (2) |
| AC-P25-6 | Candidate M_* list (repo-only) | ✅ | M_Z, M_W, v_EW — all from repo context |
| AC-P25-7 | Calibration family table present | ✅ | Table 1 with R_ξ, M₅, Δlog₁₀M₅ |
| AC-P25-8 | Robustness verdict stated | ✅ | Section 4: ROBUST boxed |
| AC-P25-9 | Physical motivation paragraph | ✅ | Section 5 |
| AC-P25-10 | Error propagation formulas | ✅ | Section 6, Eqs. (3)-(4) |
| AC-P25-11 | Error budget table | ✅ | Table 2 |
| AC-P25-12 | Canonical M_* decision + justification | ✅ | Section 7: M_Z with 4 reasons |
| AC-P25-13 | "What remains open" stated | ✅ | Section 8.2 |
| AC-P25-14 | Figure with 2 panels (A,B) | ✅ | Figure 1: calibration schematic + shift bars |
| AC-P25-15 | Figure caption disclaimer | ✅ | "Schematic only; not to scale; no overclaim" |
| AC-P25-16 | Build: 0 undefined refs/cites | ✅ | 0 undefined |
| AC-P25-17 | Export naming policy respected | ✅ | `EDC_BLOCK003_DERIVATION_V17_EW_CALIBRATION_ROBUSTNESS.pdf` |
| AC-P25-18 | PAPERS_INDEX updated | ⏳ | Pending |
| AC-P25-19 | One-line outcome correct format | ✅ | ROBUST + Canonical M_Z |

---

## Verification Commands

```bash
# FROZEN check
md5 edc_papers/paper_gravity_block003/main.tex
# Expected: e592a943b1f5e6a48e661b9ed812109c

# Build
cd edc_papers/paper_gravity_block003/derivation_v17
xelatex main.tex && xelatex main.tex

# Undefined refs check
grep -c "undefined" main.log
# Expected: 0

# Export
cp main.pdf EDC_BLOCK003_DERIVATION_V17_EW_CALIBRATION_ROBUSTNESS.pdf

# MD5s
md5 main.tex main.pdf EDC_BLOCK003_DERIVATION_V17_EW_CALIBRATION_ROBUSTNESS.pdf
```

---

## Summary

All acceptance criteria verified (pending PAPERS_INDEX update). Build complete.

**Outcome:**
- Calibration: **ROBUST** — all EW scales give M₅ in same decade
- Canonical choice: **M_Z** — metrological precision + definitional stability
- Internal derivation: Still **NO-GO**
