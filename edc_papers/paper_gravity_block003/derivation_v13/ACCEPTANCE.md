# Acceptance Criteria — P21 (Derivation v13)

## AC-P21 Checklist

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-P21-1 | Work confined to derivation_v13 + PAPERS_INDEX update only | ✅ | Only files in derivation_v13/ created |
| AC-P21-2 | FROZEN main.tex MD5 unchanged | ✅ | MD5 = `e592a943b1f5e6a48e661b9ed812109c` verified |
| AC-P21-3 | No edc_book_2 modifications | ✅ | Directory untouched |
| AC-P21-4 | Non-compact 1/r² failure explained | ✅ | Section 3, 3-6 lines |
| AC-P21-5 | Normalizable zero-mode → 1/r recovery | ✅ | Section 4 |
| AC-P21-6 | Normalization integral explicit | ✅ | Eq. (8): I = ∫ dξ e^{4A} |ψ₀|² |
| AC-P21-7 | M_Pl² = M₅³ I derived | ✅ | Eq. (8) boxed |
| AC-P21-8 | G_N = 1/(8π M_Pl²) stated | ✅ | Eq. (9) |
| AC-P21-9 | Bridge slot identified | ✅ | Section 5.3 boxed |
| AC-P21-10 | Epistemic tags applied | ✅ | [M]/[D]/[P]/[I]/[BL] in Table 2 |
| AC-P21-11 | Build: 0 undefined refs/cites | ✅ | 0 undefined |
| AC-P21-12 | Export naming policy respected | ✅ | `EDC_BLOCK003_DERIVATION_V13_WEAKFIELD_MATCHING.pdf` |
| AC-P21-13 | PAPERS_INDEX updated | ✅ | v13 entry added |
| AC-P21-14 | Figure with 2 panels (A,B) | ✅ | Figure 1 with mode profile + potential |
| AC-P21-15 | Figure caption: "schematic only, not to scale" | ✅ | Caption includes disclaimer |
| AC-P21-16 | One-line outcome matches allowed options | ✅ | "BRIDGE SLOT FOUND" |
| AC-P21-17 | Minimal citations (RS, GHY, York, Maartens) | ✅ | 5 references |

---

## Verification Commands

```bash
# FROZEN check
md5 edc_papers/paper_gravity_block003/main.tex
# Expected: e592a943b1f5e6a48e661b9ed812109c

# Build
cd edc_papers/paper_gravity_block003/derivation_v13
xelatex main.tex && xelatex main.tex

# Undefined refs check
grep -c "undefined" main.log
# Expected: 0

# Export
cp main.pdf EDC_BLOCK003_DERIVATION_V13_WEAKFIELD_MATCHING.pdf

# MD5s
md5 main.tex main.pdf EDC_BLOCK003_DERIVATION_V13_WEAKFIELD_MATCHING.pdf
```

---

## Summary

All acceptance criteria verified. Build complete.

**Outcome:** BRIDGE SLOT FOUND — G_N reduces to M₅³ I; EDC must compute I or provide one calibration scale.
