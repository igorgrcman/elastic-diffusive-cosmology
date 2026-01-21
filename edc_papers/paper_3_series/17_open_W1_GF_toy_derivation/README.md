# OPEN-W1: Toy Derivation of G_F Scaling

**Version:** 0.1 (Initial Draft)
**Date:** 2026-01-20
**DOI:** 10.5281/zenodo.18321396

## Purpose

This document presents a **toy derivation** of the effective four-Fermi coupling
G_F from thick-brane mediator exchange. It is explicitly **not a fit** and
**not a numerical claim**. The goal is to establish the structural pathway:

> G_EDC ~ g_eff^2 / m_phi^2 × O_overlap

with all suppression factors made explicit and gaps clearly catalogued.

## Key Results

1. **Toy Lagrangian (§3):** L_phi + L_int with 5D scalar mediator
2. **Effective Lagrangian (§4):** L_eff = -(g_5^2/2m_phi^2) O_overlap J(x)J(x)
3. **Overlap Integral (§5):** ∫dξ ∫dy f_a f_b f_phi [OPEN]
4. **Dimensional Analysis (§6):** [G_EDC] = [E]^-2 ✓

## What This Does NOT Do

- Does NOT derive g_5 from first principles
- Does NOT compute O_overlap numerically
- Does NOT claim numerical agreement with PDG G_F
- Does NOT specify V-A structure (see Companion V)

## Build

```bash
cd paper
xelatex main.tex
xelatex main.tex  # for references
```

## Epistemic Status

| Claim | Status |
|-------|--------|
| L_phi form | [P]/[Def] |
| L_int localized coupling | [P] |
| L_eff via integration out | [Dc] |
| g_eff = g_5 × O_overlap × O_BC | [Def] |
| O_overlap integral | [OPEN] |
| G_F = 1.166 × 10^-5 GeV^-2 | [BL] |

## Gap Closure Targets

1. Fermion mode profiles f_a, f_b
2. Mediator profile f_phi in frozen regime
3. BC operator O(P_frozen, P_chir) from Companion V
4. Mediator mass m_phi from Framework + KK spectrum
5. Coupling g_5 dimensional origin

## Related Documents

- Framework v2.0 (DOI: 10.5281/zenodo.18299085)
- Companion V (Neutrino/Chirality) — this series
- Weak Program Overview (DOI: 10.5281/zenodo.18319921)
