# Geometric Structure of Electron and Proton in 5D Membrane Cosmology

**Derivation of the Fine-Structure Constant from First Principles**

## Metadata

- **DOI:** [10.5281/zenodo.18211854](https://doi.org/10.5281/zenodo.18211854)
- **Repository:** [github.com/igorgrcman/elastic-diffusive-cosmology](https://github.com/igorgrcman/elastic-diffusive-cosmology)
- **Author:** Igor Grcman

## Folder Structure

```
paper_2/
├── paper/                          # LaTeX source and compiled PDF
│   ├── main.tex                    # Main document
│   ├── appendix_gl_frozen_numerics.tex
│   ├── appendix_gl_frozen_numerics.py
│   └── derivations/                # Appendix subfiles (LaTeX)
│       ├── EDC_FROZEN_Criterion_From_Action_v1.tex
│       ├── EDC_PLOC_From_Action_v1.tex
│       ├── EDC_PEPSILON_From_Action_v1.tex
│       ├── EDC_SU2_SYM_From_Action_v1.tex
│       ├── EDC_PJUNCTION_From_Action_v1.tex
│       ├── EDC_Q_Factorization_From_Action_v1.tex
│       ├── EDC_PSCALE_From_Action_v1.tex
│       ├── EDC_19ppm_Correction_v1.tex
│       ├── EDC_Sigma_From_Pressure_v1.tex
│       └── EDC_Alpha_Geometric_Ratio_v1.tex
│
├── supplementary/                  # Extended derivations (Markdown)
│   ├── derivations/
│   │   ├── EDC_FROZEN_Criterion_From_Action_v1.md
│   │   ├── EDC_PLOC_From_Action_v1.md
│   │   ├── EDC_PEPSILON_From_Action_v1.md
│   │   ├── EDC_SU2_SYM_From_Action_v1.md
│   │   ├── EDC_PJUNCTION_From_Action_v1.md
│   │   ├── EDC_Q_Factorization_From_Action_v1.md
│   │   └── EDC_PSCALE_From_Action_v1.md
│   └── research_iterations/
│       ├── RESEARCH_ITERATION_1_Alpha_Derivation.md
│       ├── RESEARCH_ITERATION_1_Sigma_Derivation.md
│       └── RESEARCH_ITERATION_1_19ppm_Correction.md
│
├── code/                           # Python scripts for reproducibility
│   └── appendix_gl_frozen_numerics.py
│
├── figures/                        # (empty - no external figures used)
├── bib/                            # (empty - bibliography inline)
└── README.md                       # This file
```

## Building the Paper

### Option 1: Command line (requires TeX Live / MacTeX)

```bash
cd paper/
pdflatex main.tex
pdflatex main.tex   # run twice for cross-references
```

### Option 2: Overleaf

Upload the contents of `paper/` to Overleaf and compile with pdfLaTeX.

### Option 3: latexmk

```bash
cd paper/
latexmk -pdf main.tex
```

## Reproducing the Numerical Results

The Python script computes the excluded-volume coefficient for frozen vs GL profiles:

```bash
cd code/
python appendix_gl_frozen_numerics.py
```

**Expected output:**
```
Frozen vs GL Profile Comparison
============================================================
Target (4*pi/3) = 4.188790204786

Frozen (step):        C = 4.188790204786  Error = 0.000%
GL (delta/a= 0.50): C = 10.560219636209  Error = 152.107%
GL (delta/a= 0.20): C = 5.900185990873  Error = 40.857%
GL (delta/a= 0.10): C = 4.925630703885  Error = 17.591%
GL (delta/a= 0.05): C = 4.529433998143  Error = 8.132%
GL (delta/a= 0.01): C = 4.252660768127  Error = 1.525%
```

**Requirements:** NumPy only (no SciPy dependency).

## Key Results

| Quantity | EDC Prediction | CODATA Value | Error |
|----------|----------------|--------------|-------|
| $m_p/m_e$ | $6\pi^5 = 1836.118...$ | 1836.152... | 0.0018% |
| $\alpha^{-1}$ | $(4\pi + 5/6)/6\pi^5 \to 137.027...$ | 137.036... | 0.0067% |

## License

See repository root for license information.

## Citation

```bibtex
@article{Grcman2026EDC,
  author  = {Gr\v{c}man, Igor},
  title   = {Geometric Structure of Electron and Proton in 5D Membrane Cosmology},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.18211854}
}
```

---

*Some internal research notes are intentionally excluded from the public release.*
