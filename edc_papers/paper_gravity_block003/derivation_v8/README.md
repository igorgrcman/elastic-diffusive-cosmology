# Derivation v8: NC-1 Attempt (Graviton Zero-Mode Normalization)

## Status

**INCONCLUSIVE** — G_N derived but σ unspecified; BLOCK-003 remains open.

Canonical PDF: `EDC_BLOCK003_DERIVATION_V8_FIX_C_ATTEMPT_NC1.pdf`

## What This Document Is

A concrete attempt to fix C using candidate NC-1 from derivation v7: graviton zero-mode normalization via canonical Kaluza-Klein reduction.

## Result

**Derived:** G_N = κ₅²/(8πL) = C·σ^(-3/4)/(8πR_ξ)

**Problem:** C appears only in combination C/(8π), which can be absorbed. The actual numerical value depends on σ, which is not independently specified.

## Outcome

| Aspect | Status |
|--------|--------|
| G_N formula derived | ✅ [Dc] |
| Anti-circularity | ✅ Preserved |
| C independently fixed | ❌ No |
| Numerical prediction | ❌ Requires σ |

## Missing Element (Narrowed)

**Before v8:** Fix C (dimensionless constant)

**After v8:** Specify σ (brane tension value) from EDC field equations

With σ known, can adopt C = 8π by convention and compute G_N^pred.

## Contents

- `main.tex` — LaTeX source (5 pages)
- `main.pdf` — Build artifact
- `EDC_BLOCK003_DERIVATION_V8_FIX_C_ATTEMPT_NC1.pdf` — Canonical export
- `REPORT.md` — Build proof and MD5 table
