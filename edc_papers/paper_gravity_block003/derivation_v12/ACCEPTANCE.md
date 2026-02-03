# Acceptance Criteria — P20 (Derivation v12)

## AC-P20 Checklist

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| AC-P20-1 | Work confined to derivation_v12 + PAPERS_INDEX update only | ✅ | Only files in derivation_v12/ created |
| AC-P20-2 | FROZEN main.tex MD5 unchanged | ✅ | MD5 = `e592a943b1f5e6a48e661b9ed812109c` verified |
| AC-P20-3 | No new broad theory expansion | ✅ | Audit only, no new physics |
| AC-P20-4 | Outcome stated unambiguously | ✅ | "NO BRIDGE" in abstract and Section 5 |
| AC-P20-5 | Build: 0 undefined refs/cites | ✅ | 0 undefined references |
| AC-P20-6 | Export naming policy respected | ✅ | `EDC_BLOCK003_DERIVATION_V12_PART1_GRAVITY_AUDIT.pdf` |
| AC-P20-7 | PAPERS_INDEX updated with MD5s + status | ✅ | v12 entry added |
| AC-P20-8 | Bridge map table present | ✅ | Section 4, Table with 6 rows |
| AC-P20-9 | Epistemic tags applied | ✅ | [M]/[D]/[Dc]/[P]/[I]/[BL] used |
| AC-P20-10 | Mercury precession formula documented | ✅ | Section 2, eq. (2) |

---

## Verification Commands

```bash
# FROZEN check
md5 edc_papers/paper_gravity_block003/main.tex
# Expected: e592a943b1f5e6a48e661b9ed812109c

# Build
cd edc_papers/paper_gravity_block003/derivation_v12
xelatex main.tex && xelatex main.tex

# Undefined refs check
grep -c "undefined" main.log
# Expected: 0

# Export
cp main.pdf EDC_BLOCK003_DERIVATION_V12_PART1_GRAVITY_AUDIT.pdf

# MD5s
md5 main.tex main.pdf EDC_BLOCK003_DERIVATION_V12_PART1_GRAVITY_AUDIT.pdf
```

---

## Summary

All acceptance criteria verified. Build complete.

**Outcome:** NO BRIDGE — Part I imports 4D gravity as [I]/[P]; BLOCK-003 remains open.
