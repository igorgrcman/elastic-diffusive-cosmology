# NOTATION_POLICY.md

Updated: 2026-01-24
Authority: Framework v2.0 (DOI: 10.5281/zenodo.18299085)
Full reference: See `SYMBOL_TABLE.md` for complete symbol dictionary

## Canonical Symbols (Framework v2.0)

| Symbol | LaTeX | Meaning | Notes |
|--------|-------|---------|-------|
| ξ | `\xi` | 5D compact coordinate | **CANONICAL 5D depth** |
| R_ξ | `R_\xi` or `\Rxi` | Compactification radius | Canonical |
| Σ³ | `\Sigma^3` | 3D brane/membrane | |
| M⁵ | `\mathcal{M}^5` | 5D bulk manifold | **NEVER use M5 or M_5** |
| σ | `\sigma` | Brane tension | |
| G_5 | `G_5` | 5D gravitational coupling | |
| G_4 | `G_4` | 4D gravitational coupling (observed) | |
| J^ν_{bulk→brane} | `\Jbb{\nu}` | Bulk-to-brane energy current | Macro defined |
| α | `\alpha` | Fine structure constant | |
| G_F | `G_F` | Fermi constant | |
| M_{5,Pl} | `M_{5,\mathrm{Pl}}` | 5D Planck mass | Disambiguated from manifold |

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
2. **M5 or M_5 for manifold**: Use `\mathcal{M}^5`, never `M5` or `M_5`
3. **Inconsistent R notation**: Use `R_ξ` or `\Rxi`, not `R_z`, `R_5`, etc.
4. **Missing epistemic tags**: All claims must have explicit tags
5. **Paraphrased bulk-brane statement**: Must cite Framework v2.0 Remark 4.5 verbatim

## Symbol Replacement Policy

**CRITICAL**: NO blind grep/replace. Every symbol change requires:
1. Context classification (see `audit/notation/CHAPTER_VARIABLE_CONTEXT_LEDGER.md`)
2. Entry in `audit/notation/REPLACEMENT_RISK_LEDGER.md`
3. Canon anchor (Framework v2.0 Eq. or §)
4. Build verification after change

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

Script `tools/symbol_audit.py` provides context-aware symbol audit:
- Classifies each symbol occurrence
- Detects violations vs. legitimate usage
- Generates machine-readable report

## Related Documents

| Document | Purpose |
|----------|---------|
| `canon/SYMBOL_TABLE.md` | Complete canonical symbol dictionary |
| `audit/notation/SYMBOL_AUDIT_REPORT.md` | Current audit status |
| `audit/notation/SYMBOL_USAGE_BOOK2.md` | Per-symbol usage summary |
| `audit/notation/CHAPTER_VARIABLE_CONTEXT_LEDGER.md` | Per-chapter variable cards |
| `audit/notation/COLLISION_AND_AMBIGUITY_TODO.md` | Tracked violations |
| `audit/notation/REPLACEMENT_RISK_LEDGER.md` | Change tracking |

---

Last updated: 2026-01-24
