# Derivation Attempt v3: Can κ₅² Be Fixed by σ?

## Status

**WORKING / OPEN** — Derivation attempt; not a results paper.

Canonical PDF: `EDC_BLOCK003_DERIVATION_V3_KAPPA5_FROM_SIGMA.pdf`

## Question Tested

Can the 5D gravitational coupling κ₅² be determined by the brane tension σ alone?

## Outcome

**INCONCLUSIVE.**

- Dimensional analysis gives κ₅² = C·σ^(-3/4) as the unique consistent form
- Israel junction conditions satisfied for any C > 0
- The constant C cannot be fixed by σ alone
- σ provides length scale ℓ_σ = σ^(-1/4) but not κ₅² uniquely

## Missing Element

An independent scale or normalization condition to fix C.

## Contents

- `main.tex` — LaTeX source (5 pages)
- `main.pdf` — Build artifact
- `EDC_BLOCK003_DERIVATION_V3_KAPPA5_FROM_SIGMA.pdf` — Canonical export
- `REPORT.md` — Build proof and outcome summary

## Relationship to Other Documents

- **derivation_v1**: Derived G_N = κ₅²/(6πL)
- **derivation_v2**: Tested L = R_ξ; blocked by unknown κ₅²
- **derivation_v3 (this)**: Tests κ₅² = f(σ); finds C undetermined
- **Program note (FROZEN)**: Not modified

## Build

```
xelatex main.tex
xelatex main.tex
```
