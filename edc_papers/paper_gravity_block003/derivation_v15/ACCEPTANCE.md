# Acceptance Criteria — P23 (Derivation v15)

## AC-P23 Checklist

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-P23-1 | Work confined to derivation_v15 + PAPERS_INDEX update only | ✅ | Only files in derivation_v15/ created |
| AC-P23-2 | FROZEN main.tex MD5 unchanged | ✅ | MD5 = `e592a943b1f5e6a48e661b9ed812109c` verified |
| AC-P23-3 | No edc_book_2 modifications | ✅ | Directory untouched |
| AC-P23-4 | v13 recap present | ✅ | Section 1.1 |
| AC-P23-5 | v14 Model A insert | ✅ | Section 1.2: I = R_ξ |
| AC-P23-6 | Both calibration options shown | ✅ | Section 2.2 (M_Pl) and 2.3 (ℓ_P) |
| AC-P23-7 | Why 1-scale calibration not failure | ✅ | Section 2.1 with QED/QCD/EW/GR examples |
| AC-P23-8 | Closure formulas derived | ✅ | Section 3: M₅ = M_Pl^{2/3} R_ξ^{-1/3} |
| AC-P23-9 | Consistency check for G_N | ✅ | Section 3.2 |
| AC-P23-10 | M₅ propagation to numeric | ✅ | Section 4 with example table |
| AC-P23-11 | Epistemic ledger table | ✅ | Table 1: full input/output classification |
| AC-P23-12 | Closure statement boxed | ✅ | Section 5.2 |
| AC-P23-13 | Error budget section | ✅ | Section 6 with formula and cases |
| AC-P23-14 | Build: 0 undefined refs/cites | ✅ | 0 undefined |
| AC-P23-15 | Export naming policy respected | ✅ | `EDC_BLOCK003_DERIVATION_V15_CALIBRATED_CLOSURE_LP.pdf` |
| AC-P23-16 | PAPERS_INDEX updated | ✅ | v15 entry added |
| AC-P23-17 | Figure with 2 panels (A,B) | ✅ | Figure 1: calibration flow + scaling |
| AC-P23-18 | Figure caption: "schematic only" | ✅ | Caption includes disclaimer |
| AC-P23-19 | One-line outcome matches allowed | ✅ | "CLOSED (calibrated)" |

---

## Verification Commands

```bash
# FROZEN check
md5 edc_papers/paper_gravity_block003/main.tex
# Expected: e592a943b1f5e6a48e661b9ed812109c

# Build
cd edc_papers/paper_gravity_block003/derivation_v15
xelatex main.tex && xelatex main.tex

# Undefined refs check
grep -c "undefined" main.log
# Expected: 0

# Export
cp main.pdf EDC_BLOCK003_DERIVATION_V15_CALIBRATED_CLOSURE_LP.pdf

# MD5s
md5 main.tex main.pdf EDC_BLOCK003_DERIVATION_V15_CALIBRATED_CLOSURE_LP.pdf
```

---

## Summary

All acceptance criteria verified. Build complete.

**Outcome:** CLOSED (calibrated) — BLOCK-003 closed under one-scale [BL] calibration; 5D scale inferred as M₅(R_ξ) = M_Pl^{2/3} R_ξ^{-1/3}.
