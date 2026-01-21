# EDC Weak Sector: Consolidated Zenodo Article

**Title:** EDC Weak Sector: A Mechanistic Brane-Interface Framework for Weak Decays

**Subtitle:** Unified Absorption–Dissipation–Release Pipeline from Neutron to Leptons

## Build Instructions

```bash
cd paper
xelatex -interaction=nonstopmode main.tex
bibtex main
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

Or with latexmk:
```bash
latexmk -xelatex -interaction=nonstopmode main.tex
```

## Document Structure

| Section | Content |
|---------|---------|
| §1 | Scope and Empirical Baselines |
| §2 | Mechanistic Dimension Principle |
| §3 | Unified Decay Pipeline |
| §4 | Projection Operators |
| §5 | Case Studies (N, μ, τ, π, e, ν) |
| §6 | Structural Pathway to G_F |
| §7 | Falsifiability and Epistemic Boundaries |
| §8 | Open Problems |

## Key Features

1. **Single consolidated document** — Replaces multiple companion documents
2. **No DOI registry** — This is the primary Zenodo submission
3. **External references only** — PDG, CODATA, standard physics literature
4. **Epistemic tagging** — [BL], [Def], [P], [Dc], [OPEN] throughout
5. **Explicit falsifiability** — Testable predictions and failure conditions

## File Structure

```
19_edc_weak_sector_zenodo_article/
├── README.md
├── PATCH_NOTES_CONSOLIDATION.md
├── paper/
│   ├── main.tex
│   └── sections/
│       ├── 01_scope.tex
│       ├── 02_mechanism.tex
│       ├── 03_pipeline.tex
│       ├── 04_operators.tex
│       ├── 05_cases.tex
│       ├── 06_gf_pathway.tex
│       ├── 07_falsifiability.tex
│       └── 08_open.tex
├── figures/
│   └── fig_pipeline.tex
└── bib/
    └── references.bib
```

## Notes

- This document consolidates content from previous companion documents (N, M, T, P, L, V)
- Previous Zenodo DOIs are deprecated; this article is the canonical source
- All empirical values are baselines [BL] from PDG/CODATA
- All structural elements are definitions [Def] or postulates [P]
- Numerical derivations remain explicitly open [OPEN]
