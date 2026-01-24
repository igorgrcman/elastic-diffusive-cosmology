# NOTATION_POLICY.md

## Canonical Symbols (Framework v2.0)

| Symbol | Meaning | Notes |
|--------|---------|-------|
| ξ (xi) | 5D depth coordinate | Canonical; NOT "z" |
| R_ξ | 5D compactification radius | Canonical |
| Σ | Membrane/brane | |
| M_5 | 5D bulk manifold | |
| σ | Brane tension | |
| G_5 | 5D gravitational coupling | |
| G_4 | 4D gravitational coupling (observed) | |
| J^ν_{bulk→brane} | Bulk-to-brane energy current | Macro: `\Jbb{ν}` |
| α | Fine structure constant (1/137.036...) | |
| G_F | Fermi constant | |

## Epistemic Tags (Mandatory)

| Tag | Meaning | Color |
|-----|---------|-------|
| [BL] | Baseline (PDG/CODATA) | Brown |
| [Der] | Derived from principles | Green |
| [Dc] | Derived conditional | Blue |
| [I] | Identified/pattern | Gray |
| [Cal] | Calibrated/fitted | Red |
| [P] | Proposed/postulated | Red |
| [M] | Mathematical theorem | Gray |
| [Def] | Definition | Blue |
| [OPEN] | Unresolved | Red |

## Forbidden Patterns

The following patterns are forbidden and will trigger gate failure:

1. **z instead of ξ for 5D depth**: Use `ξ` or `\xi`, never `z` for the 5D coordinate
2. **Inconsistent R notation**: Use `R_ξ` or `\Rxi`, not `R_z`, `R_5`, etc.
3. **Missing epistemic tags**: All claims must have explicit tags
4. **Paraphrased bulk-brane statement**: Must cite Framework v2.0 Remark 4.5 verbatim

## LaTeX Macros

```latex
\newcommand{\Rxi}{R_\xi}
\newcommand{\Jbb}[1]{J^{#1}_{\mathrm{bulk}\to\mathrm{brane}}}
```

## Gate Enforcement

Script `tools/gate_notation.sh` checks:
- [ ] No forbidden patterns in source files
- [ ] Epistemic tags present on claims
- [ ] Canonical symbols used consistently
