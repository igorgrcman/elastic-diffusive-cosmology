# Submission Checklist — Superheavy Predictions Paper (PRC)

**Paper:** Topological pinning predictions for α-decay half-lives of superheavy elements Z=119 and Z=120
**Version:** v2 (2026-03-16)
**Target journal:** Physical Review C (PRC)
**Submission portal:** https://authors.aps.org/

---

## Pre-Submission Checks

### Format & Compliance
- [ ] Document class: `revtex4-2` with `aps,prc,twocolumn,showpacs`
- [ ] PACS codes included: 21.10.-k, 23.60.+e, 21.60.Cs
- [ ] Abstract ≤ 500 words (current: ~180 words) ✓
- [ ] Total length ≤ 10 journal pages (estimated: ~7 pages) ✓
- [ ] References ≤ 50 (current: 25) ✓
- [ ] Author name: Igor Grčman, Independent researcher, Zagreb, Croatia
- [ ] Email: igor.grcman@protonmail.com

### Content Verification
- [ ] All numerical values cross-checked against V7.8 M2 regression:
  - a = 1.593 ± 0.028, b = −50.77 ± 0.91, g = −1.643 ± 0.142
  - c₁ = 1.121 ± 0.314, c₂ = 1.538 ± 0.265
  - R² = 0.980, CV R² = 0.971, RMSE = 0.810
- [ ] OOS data: 6/6 pass, mean |Δ| = 0.48 dex
- [ ] Predictions verified:
  - ²⁹⁸119: log t = −0.19 ± 1.3 → 0.6 s
  - ³⁰²120: log t = +1.46 ± 1.3 → 29 s
  - ³⁰⁴120: log t = +2.89 ± 1.3 → 780 s
- [ ] Uncertainty budget: σ_Q ≈ 0.8, σ_model ≈ 0.9, σ_OOS ≈ 0.5 → σ_total ≈ 1.3 dex
- [ ] No bare δ (uses δ_J where needed)
- [ ] EDC-specific jargon limited to §II.A; rest is standard nuclear physics

### Figure
- [ ] `figures/superheavy_validation.pdf` — publication quality, 300 dpi
- [ ] Two panels: (a) OOS validation, (b) Z=119,120 predictions
- [ ] Serif fonts (Computer Modern), line widths ≥ 1.0 pt
- [ ] Figure caption complete and self-contained
- [ ] `figures/make_figure.py` — reproducible generation script

### References
- [ ] Gamow (1928) — quantum tunneling origin
- [ ] Geiger & Nuttall (1911) — original GN law
- [ ] EDC Part I — Zenodo DOI: 10.5281/zenodo.18176174
- [ ] EDC Paper 2 — Zenodo DOI: 10.5281/zenodo.18211854
- [ ] EDC Book IV — manuscript in preparation
- [ ] NUBASE2020, AME2020 — nuclear data sources
- [ ] All experimental SHE references current (2024)

### LaTeX Compilation
- [ ] Compiles without errors under `pdflatex`
- [ ] No overfull hboxes > 1pt
- [ ] All cross-references resolve (\ref, \cite)
- [ ] Figure included correctly via \includegraphics

---

## File Inventory

| File | Description | Status |
|------|-------------|--------|
| `SUPERHEAVY_PREDICTIONS_v2.tex` | Main manuscript | Ready |
| `figures/superheavy_validation.pdf` | Figure 1 (two panels) | Ready |
| `figures/superheavy_validation.png` | Figure 1 (raster backup) | Ready |
| `figures/make_figure.py` | Figure generation script | Ready |
| `COVER_LETTER.md` | Cover letter draft | Ready |
| `SUBMISSION_CHECKLIST.md` | This file | Ready |

---

## Submission Steps

1. **Compile locally:** `pdflatex SUPERHEAVY_PREDICTIONS_v2.tex` (×2 for refs)
2. **Proofread** the compiled PDF carefully
3. **Go to** https://authors.aps.org/
4. **Create account** if needed
5. **Select journal:** Physical Review C
6. **Upload files:**
   - Main .tex file
   - Figure .pdf file
   - (Optional) .bib file if converted from thebibliography
7. **Paste cover letter** from COVER_LETTER.md
8. **Suggested reviewers** (optional):
   - A. Sobiczewski (NCBJ Warsaw) — SHE theory
   - W. Nazarewicz (MSU/FRIB) — nuclear structure
   - C. Qi (KTH Stockholm) — alpha decay systematics
9. **Submit**

---

## Post-Submission

- [ ] Record submission ID
- [ ] Archive submitted version with timestamp
- [ ] Prepare responses to likely reviewer questions:
  - Q: "Why should Z₆ symmetry apply to nuclei?"
  - Q: "How does this differ from shell corrections?"
  - Q: "What is the physical origin of p = 6.1?"
  - Q: "Can you predict SF branching ratios?"

---

**Sealed:** 2026-03-16
