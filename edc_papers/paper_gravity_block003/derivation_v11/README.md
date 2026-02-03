# Derivation v11: Derive σ from EDC Field Equations

## Status

**NO-GO** — σ cannot be derived from EDC-internal field equations; it is calibrated from observed ℏ or α.

Canonical PDF: `EDC_BLOCK003_DERIVATION_V11_SIGMA_FROM_FIELD_EQS.pdf`

## What This Document Is

A systematic attempt to derive the brane tension σ from EDC-internal field equations and variational principles, maintaining strict anti-circularity (no G_N^obs, M_Pl inputs).

## Result

**NO-GO confirmed.** The EDC framework defines σ via:
- ℏ = σ R_ξ³ / c → σ = ℏc / R_ξ³ (calibration from observed ℏ)
- σ = m_e c² / (α r_e²) (calibration from observed α)

No EDC-internal constraint fixes σ independently.

## Attempts Made

| Attempt | Method | Outcome |
|---------|--------|---------|
| A | Israel junction conditions | No closure (C remains free) |
| B | Schwinger limit correspondence | No closure (uses observed ℏ, m_e) |
| C | Variational principle | No closure (σ is parameter, not field) |
| D | Topological quantization | No closure (no rule exists) |

## Missing Element

EDC lacks an independent normalization principle for the membrane tension σ that does not reference observed quantum constants (ℏ, α) or gravitational constants (G_N, M_Pl).

## Contents

- `main.tex` — LaTeX source (5 pages)
- `main.pdf` — Build artifact
- `EDC_BLOCK003_DERIVATION_V11_SIGMA_FROM_FIELD_EQS.pdf` — Canonical export
- `README.md` — This file
- `REPORT.md` — Build proof and evidence log
- `ACCEPTANCE.md` — AC-P20 checklist
