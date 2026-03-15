# Acceptance Criteria — P24 (Derivation v16)

## AC-P24 Checklist

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-P24-1 | Work confined to derivation_v16 + PAPERS_INDEX update only | ✅ | Only files in derivation_v16/ created |
| AC-P24-2 | FROZEN main.tex MD5 unchanged | ✅ | MD5 = `e592a943b1f5e6a48e661b9ed812109c` verified |
| AC-P24-3 | No edc_book_2 modifications | ✅ | Directory untouched |
| AC-P24-4 | v15 recap present | ✅ | Section 1.1 |
| AC-P24-5 | Track A (internal derivation) attempted | ✅ | Section 2 |
| AC-P24-6 | Candidate Relation Table present | ✅ | Table 1 with 6 candidates |
| AC-P24-7 | Track A verdict stated | ✅ | NO-GO boxed in Section 2.3 |
| AC-P24-8 | Track B (minimal baseline) executed | ✅ | Section 3 |
| AC-P24-9 | R_ξ = ℏc/M_Z formula explicit | ✅ | Eq. (2) boxed |
| AC-P24-10 | Numerical R_ξ value | ✅ | 2.165 × 10⁻¹⁸ m |
| AC-P24-11 | Uncertainty propagation to M₅ | ✅ | Section 3.3-3.5 |
| AC-P24-12 | Bridge Closure Matrix table | ✅ | Table 3 |
| AC-P24-13 | What would remove last [BL] stated | ✅ | Section 5.1, 7.2 |
| AC-P24-14 | Build: 0 undefined refs/cites | ✅ | 0 undefined |
| AC-P24-15 | Export naming policy respected | ✅ | `EDC_BLOCK003_DERIVATION_V16_R_XI_DETERMINATION.pdf` |
| AC-P24-16 | PAPERS_INDEX updated | ✅ | v16 entry added |
| AC-P24-17 | Figure with 2 panels (A,B) | ✅ | Figure 1: dependency graph + error budget |
| AC-P24-18 | Figure caption disclaimer | ✅ | "schematic only; not to scale; no overclaim" |
| AC-P24-19 | One-line outcome correct format | ✅ | Track A: NO-GO, Track B: CLOSED |

---

## Verification Commands

```bash
# FROZEN check
md5 edc_papers/paper_gravity_block003/main.tex
# Expected: e592a943b1f5e6a48e661b9ed812109c

# Build
cd edc_papers/paper_gravity_block003/derivation_v16
xelatex main.tex && xelatex main.tex

# Undefined refs check
grep -c "undefined" main.log
# Expected: 0

# Export
cp main.pdf EDC_BLOCK003_DERIVATION_V16_R_XI_DETERMINATION.pdf

# MD5s
md5 main.tex main.pdf EDC_BLOCK003_DERIVATION_V16_R_XI_DETERMINATION.pdf
```

---

## Summary

All acceptance criteria verified. Build complete.

**Outcome:**
- Track A: **NO-GO** — R_ξ not derivable from EDC internal geometry
- Track B: **CLOSED** — R_ξ = 2.165 × 10⁻¹⁸ m; M₅ = 2.4 × 10¹³ GeV ± 0.001%
