# Derivation v19 — Derivation-First: From 5D Action to 4D Newton Law

**Status:** DERIVATION / CLOSED (calibrated)
**Date:** 2026-02-02

## Purpose

This is a **derivation document**, not a summary. It explicitly derives the bridge
relation $M_{\rm Pl}^2 = M_5^3 \mathcal{I}$ from the 5D Einstein-Hilbert action,
evaluates the normalization integral for a flat compact extra dimension, and
presents the calibrated closure with full epistemic tagging.

## One-Line Outcome

> Derivation-first writeup of gravity sector closure.
> $M_5 = 2.41 \times 10^{13}$ GeV under [BL] inputs; internal $R_\xi$ derivation NO-GO preserved.

## What Was Derived Explicitly

1. **Bridge relation** $M_{\rm Pl}^2 = M_5^3 \mathcal{I}$ from 5D→4D KK reduction
2. **Zero-mode equation** $\psi_0'' + 4A'\psi_0' = 0$ and its solution
3. **Normalization integral** $\mathcal{I} = \int d\xi\, e^{4A}|\psi_0|^2$
4. **Compact flat case** $\mathcal{I} = R_\xi$ with explicit steps
5. **Newton constant bridge** $G_N = 1/(8\pi M_5^3 R_\xi)$
6. **Closure formula** $M_5 = M_{\rm Pl}^{2/3} R_\xi^{-1/3}$

## Inputs Used

| Input | Value | Tag |
|-------|-------|-----|
| $M_{\rm Pl}^{\rm obs}$ | $1.221 \times 10^{19}$ GeV | [BL] |
| $M_Z^{\rm obs}$ | $91.1876 \pm 0.0021$ GeV | [BL] |
| $R_\xi = \hbar c / M_Z$ | identification | [I] |

## Key Results

| Quantity | Value | Tag |
|----------|-------|-----|
| $R_\xi$ | $2.165 \times 10^{-18}$ m | [I]+[BL] |
| $M_5$ | $2.41 \times 10^{13}$ GeV | [D] |
| $\delta M_5/M_5$ | $1.1 \times 10^{-5}$ | — |

## Displayed Equations Count

Sections 2–5 contain **35+ displayed equations** showing explicit derivation steps.

## Contents

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (7 pages) |
| `main.pdf` | Compiled PDF |
| `EDC_BLOCK003_DERIVATION_V19_DERIVATION_FIRST.pdf` | Canonical export |
| `README.md` | This file |
| `REPORT.md` | Build report with MD5s |
| `ACCEPTANCE.md` | P27 acceptance checklist |

## Build

```bash
cd edc_papers/paper_gravity_block003/derivation_v19
xelatex main.tex && xelatex main.tex && xelatex main.tex
```
