# V7.9 BUILD NOTES

**Created**: 2026-01-31
**Purpose**: Compilation guide for integrated document

---

## Build Commands

```bash
cd /Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/src/derivations

# Single pass (fast)
pdflatex compile_topological_pinning.tex

# Full build (with ToC)
pdflatex compile_topological_pinning.tex && pdflatex compile_topological_pinning.tex
```

---

## Required Packages

All packages are standard LaTeX distribution:
- `inputenc`, `fontenc` — encoding
- `amsmath`, `amssymb`, `amsthm` — math
- `geometry` — page layout
- `hyperref` — links
- `tcolorbox` — boxes (with `breakable` library)
- `booktabs` — tables
- `graphicx` — graphics (unused but loaded)
- `ulem` — strikethrough (unused but loaded)

**No external dependencies.**

---

## Files Needed

| File | Status |
|------|--------|
| `compile_topological_pinning.tex` | Wrapper (existing) |
| `BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex` | Content (NEW) |

---

## Known Warnings

1. **Empty bibliography**: No `\cite` commands, so no bib warnings expected.

2. **Hyperref destinations**: May warn about "destination with the same identifier" if labels are duplicated. Check labels if this occurs.

3. **Overfull hbox**: Possible in long equations. Minor cosmetic issue.

---

## Output

- `compile_topological_pinning.pdf` — Main output
- `compile_topological_pinning.aux` — Auxiliary file (labels, refs)
- `compile_topological_pinning.toc` — Table of contents
- `compile_topological_pinning.log` — Build log
- `compile_topological_pinning.out` — Hyperref bookmarks

---

## Troubleshooting

### Error: "File not found: BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex"

**Cause**: The content file wasn't created.
**Fix**: Run the integration script or copy from this audit package.

### Error: "Undefined control sequence: \tcolorbox"

**Cause**: tcolorbox package not installed.
**Fix**: Install texlive-latex-extra or equivalent.

### Error: "Too many unprocessed floats"

**Cause**: Too many tables/figures.
**Fix**: Add `\clearpage` before problematic sections.

---

## Verification Checklist

- [ ] Compiles without errors
- [ ] ToC generates correctly
- [ ] All sections numbered
- [ ] Tables render properly
- [ ] tcolorbox environments work
- [ ] Hyperlinks functional

---

## Clean Build

```bash
rm -f compile_topological_pinning.{aux,log,out,toc,pdf}
pdflatex compile_topological_pinning.tex
pdflatex compile_topological_pinning.tex
```

