# FIGURE_FIX_NOTES.md — Companion N Figure Hygiene Pass

**Date:** 2026-01-20
**Document:** Companion N (Neutron as Excited 5D Junction)
**Build:** 21 pages, XeLaTeX

---

## Summary

This patch implements a comprehensive figure hygiene pass for Companion N:
1. Created reusable TikZ style file (`tikz_style_edc.tex`)
2. Refactored all 6 TikZ figures to use consistent styles
3. Eliminated text/diagram overlaps
4. Standardized positioning using the `positioning` library

---

## Files Created

### `paper/tikz_style_edc.tex`

Reusable style definitions for all EDC papers:

| Style Category | Styles Defined |
|----------------|----------------|
| **Box styles** | `edc box`, `bulk box`, `brane box`, `output box`, `process box`, `label box` |
| **Arrow styles** | `edc arrow`, `edc flow`, `edc dashed`, `edc bidir` |
| **Region styles** | `bulk region`, `brane region`, `observer region` |
| **Label styles** | `phase label`, `eq label`, `section label` |
| **Particle styles** | `junction point`, `flux arm`, `particle`, `neutrino` |
| **Decoration styles** | `spring`, `wave field` |
| **Boundary styles** | `bulk boundary`, `observer boundary`, `brane edge` |

---

## Figures Refactored

### 1. Figure 1: Thick-Brane Geometry (lines 283-343)

**Changes:**
- Applied `bulk region`, `brane region` background styles
- Used `bulk boundary`, `observer boundary` line styles
- Replaced ad-hoc junction drawing with `junction point` and `flux arm` styles
- Used `particle` and `neutrino` styles for 3D outputs
- Repositioned labels with explicit `yshift`/`xshift` to avoid overlaps
- Applied `wave field` style for brane-layer mode $\phi(y,t)$
- Used `label box` style for criterion box

### 2. Conceptual Picture: Glass Window (lines 350-377)

**Changes:**
- Applied `bulk region`, `brane region`, `observer region` styles
- Used `section label` for region titles
- Applied `edc flow` arrow style
- Reduced scale to 0.95 for better fit in tcolorbox

### 3. Figure 2: Potential V(q) (lines 519-548)

**Changes:**
- Adjusted scale from 1.8 to 1.6 for better proportions
- Used `edc bidir` style for energy difference arrow
- Repositioned labels with explicit offsets
- Added pointer arrow for barrier label
- Standardized particle dot sizes

### 4. Ring + Springs Diagram (lines 567-585)

**Changes:**
- Applied `junction point` style for center
- Used `spring` decoration style
- Adjusted scale to 1.1
- Repositioned angle labels with explicit offsets

### 5. Energy Pathway Diagram (lines 671-696)

**Changes:**
- Applied `bulk box`, `brane box`, `output box` styles
- Used `edc flow` arrow style
- Reduced scale to 0.85
- Applied `edc compact` node distance

### 6. Figure 3: Energy-Flow Diagram (lines 964-1008)

**Changes:**
- Reduced scale to 0.88 (was causing 70pt overfull hbox)
- Applied `edc compact` with tight node distances (1.0cm × 1.2cm)
- Reduced box minimum widths (2.0cm, 1.8cm, 1.5cm)
- Used `\tiny` font for labels above diagram
- Repositioned ledger annotation closer

---

## Build Verification

```bash
cd edc_papers/paper_3_series/10_companion_N_neutron_junction/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Output: main.pdf (21 pages)
# No figure-related overfull/underfull warnings
```

---

## Remaining Minor Warnings

| Line | Type | Cause |
|------|------|-------|
| 230-231 | Overfull hbox (5pt) | Long definition text |
| 265-267 | Overfull hbox (4pt) | Long itemize text |
| 1072-1073 | Overfull hbox (1pt) | Long quote text |
| 1413-1414 | Underfull hbox | Table column spacing |

These are paragraph/text issues (not figures) and are within acceptable tolerances.

---

## Reusability

The `tikz_style_edc.tex` file can be included in other companions:

```latex
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes,decorations.markings,decorations.pathmorphing,positioning}
\input{tikz_style_edc}
```

---

*Generated: 2026-01-20 (Figure Hygiene Pass)*
