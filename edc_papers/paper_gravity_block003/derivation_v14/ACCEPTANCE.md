# Acceptance Criteria — P22 (Derivation v14)

## AC-P22 Checklist

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-P22-1 | Work confined to derivation_v14 + PAPERS_INDEX update only | ✅ | Only files in derivation_v14/ created |
| AC-P22-2 | FROZEN main.tex MD5 unchanged | ✅ | MD5 = `e592a943b1f5e6a48e661b9ed812109c` verified |
| AC-P22-3 | No edc_book_2 modifications | ✅ | Directory untouched |
| AC-P22-4 | v13 formulas recapped | ✅ | Section 1, Eq. (1) |
| AC-P22-5 | EDC geometry hooks identified | ✅ | Section 2: σ, R_ξ, ρ_P, K_ij, h |
| AC-P22-6 | Sturm-Liouville form stated | ✅ | Section 2.3, Eq. (2)-(3) |
| AC-P22-7 | Model A (compact) presented | ✅ | Section 3: L = R_ξ, I = R_ξ |
| AC-P22-8 | Model B (warped) presented | ✅ | Section 4: A = -k|ξ|, I = 1/k |
| AC-P22-9 | Decision point: can EDC fix parameters? | ✅ | Section 5 with parameter tables |
| AC-P22-10 | Epistemic ledger table | ✅ | Table 2: assumptions, derived, open, circularity |
| AC-P22-11 | Build: 0 undefined refs/cites | ✅ | 0 undefined |
| AC-P22-12 | Export naming policy respected | ✅ | `EDC_BLOCK003_DERIVATION_V14_I_FROM_EDC_WARP_CANDIDATES.pdf` |
| AC-P22-13 | PAPERS_INDEX updated | ✅ | v14 entry added |
| AC-P22-14 | Figure with 3 panels (A,B,C) | ✅ | Figure 1: warp profiles, |ψ₀|², convergence |
| AC-P22-15 | Figure caption: "schematic only" | ✅ | Caption includes disclaimer |
| AC-P22-16 | One-line outcome matches allowed options | ✅ | "PARTIAL BRIDGE" |
| AC-P22-17 | Preferred model stated | ✅ | Model A preferred (lower circularity) |

---

## Verification Commands

```bash
# FROZEN check
md5 edc_papers/paper_gravity_block003/main.tex
# Expected: e592a943b1f5e6a48e661b9ed812109c

# Build
cd edc_papers/paper_gravity_block003/derivation_v14
xelatex main.tex && xelatex main.tex

# Undefined refs check
grep -c "undefined" main.log
# Expected: 0

# Export
cp main.pdf EDC_BLOCK003_DERIVATION_V14_I_FROM_EDC_WARP_CANDIDATES.pdf

# MD5s
md5 main.tex main.pdf EDC_BLOCK003_DERIVATION_V14_I_FROM_EDC_WARP_CANDIDATES.pdf
```

---

## Summary

All acceptance criteria verified. Build complete.

**Outcome:** PARTIAL BRIDGE — I computed up to one EDC parameter; requires 1 calibration scale (ℓ_P or M_Pl).

**Preferred:** Model A with I = R_ξ.
