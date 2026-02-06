# Derivation v47: Pati-Salam Canonicalization

## Title
**PATI-SALAM CANONICALIZATION: Coupling Matching + Weinberg Hook + G_F Closure Readiness (Zero-Handwave Normalization)**

## Summary

This derivation converts Pati-Salam into the canonical working track for the EDC unification program after v46 selection. Key contributions:

1. **Coupling matching:** Derives exact relation `1/g_Y^2 = 3/(5g_R^2) + 4/(5g_{B-L}^2)` with complete trace audit
2. **Weinberg hook:** Constructs structural formula for sin^2(theta_W) in terms of PS couplings (no numbers)
3. **G_F readiness:** PS-specialized map integrating v34/v36/v29/v30 for weak sector closure

## Key Results

### Coupling Matching (Zero-Handwave)
```
1/g_Y^2 = 3/(5g_R^2) + 4/(5g_{B-L}^2)
```

All factors derived from:
- Tr(T_3R^2) = 1/2 (SU(2) fundamental)
- Tr((B-L)^2) = 4/3 (SU(4) fundamental)
- Tr(Y^2) = 5/6 (embedding)

### Weinberg Hook (Structural)
```
sin^2(theta_W) = 1 / (1 + g_L^2 * (3/(5g_R^2) + 4/(5g_{B-L}^2)))
```

### G_F Readiness Map
- FIXED: PS track selection (v46)
- FIXED: Coupling matching (v47)
- DERIVED: G_F sum structure (v34)
- DERIVED: g_5 → g_4 relation (v36)
- OPEN: g_5 fixing (routes A/B/C)
- OPEN: L determination
- OPEN: KK sum convergence

## Hash Locks

| Version | Hash |
|---------|------|
| v45 (SoT) | `a80b3886903152d3` |
| v46 (Selector) | `2742edea37e863ac` |
| v47 (Tables) | `7a9682f333d5349e` |

## Reproduction

```bash
cd derivation_v47
python3 recompute.py      # Generate tables + run 38 checks
pdflatex main.tex         # Build PDF
pdflatex main.tex         # Resolve references
```

## Metrics

| Metric | Required | Achieved |
|--------|----------|----------|
| Pages | ≥24 | 26 |
| Equations | ≥160 | 194 |
| Labels | ≥240 | 303 |
| Checks | ≥35 | 38 |
| Traps | ≥18 | 18 |

## Files

- `main.tex` — Main document
- `main.pdf` — Compiled PDF (26 pages)
- `recompute.py` — Verification engine + checks
- `tables_generated.tex` — Auto-generated tables
- `EDC_BLOCK003_DERIVATION_V47_PS_COUPLING_MATCHING_WEINBERG_HOOK_GF_READINESS.pdf` — Export
- `README.md`, `REPORT.md`, `ACCEPTANCE.md` — Documentation

## Hard Rule Compliance

**HR-P48-N0 (Zero-Handwave Normalization):** Every factor (1/2, 1/4, 3/5, 4/5, etc.) is derived from trace conventions and embedding relations. No "known from SU(5)" or "by convention" statements.

## Date
February 2026
