# EDC BOOK 2 - INTEGRATION GUIDE
## How to Use the Deliverables
**Version 1.0 - 2026-01-30**

---

## OVERVIEW

This guide explains how to integrate all deliverables into EDC Book 2.

**Deliverables**:
1. `EPISTEMIC_STANDARD_COMPLETE.tex` - Full epistemic framework
2. `RESULT_PRESENTATION_TEMPLATE.tex` - Template for every result
3. `BOOK2_REORGANIZATION_PLAN_COMPLETE.md` - Complete reorganization roadmap
4. This integration guide

---

## FILE 1: EPISTEMIC_STANDARD_COMPLETE.tex

### What It Is
Complete LaTeX section defining epistemic framework with all corrections integrated.

### Where It Goes
**Primary location**: Preface or Chapter 0

**Structure**:
```
Book 2
├── Frontmatter
│   ├── Title, TOC, etc.
│   └── [INSERT HERE] → EPISTEMIC_STANDARD_COMPLETE.tex
├── Chapter 0: Bridge (From Book 1 to Book 2)
│   └── Section 0.4: Reference to epistemic standard
├── Part I: Foundations
│   └── ...
```

### How to Integrate

**Option A: As Preface Section** (Recommended)
```latex
% In main.tex or book2.tex

\frontmatter
\input{frontmatter/title}
\tableofcontents

% INSERT EPISTEMIC STANDARD HERE
\input{frontmatter/EPISTEMIC_STANDARD_COMPLETE}

\mainmatter
\input{chapters/chapter_00_bridge}
% ... rest of chapters
```

**Option B: As Chapter 0 Section**
```latex
% In chapters/chapter_00_bridge.tex

\chapter{From Book 1 to Weak Sector}

% ... sections 0.1, 0.2, 0.3 ...

\section{Epistemic Framework}
\input{shared/EPISTEMIC_STANDARD_COMPLETE}

% Continue with chapter
```

### What to Customize
- Table reference `\ref{tab:baseline_constants}` - ensure label exists
- Cross-references to Book 1 chapters
- Add local citation commands if needed

### Dependencies
**Required LaTeX packages**:
```latex
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{tcolorbox}  % for boxes
\usepackage{enumerate}  % for (i), (ii), (iii) lists
```

**Optional (if using macros)**:
```latex
% In preamble
\newcommand{\Cred}{C_{\mathrm{red}}}
\newcommand{\tagDc}{\textbf{[Dc]}}
% ... etc (see end of EPISTEMIC_STANDARD_COMPLETE.tex)
```

---

## FILE 2: RESULT_PRESENTATION_TEMPLATE.tex

### What It Is
LaTeX template to be copied for EVERY major result (m_p/m_e, α, sin²θ_W, G_F, etc.)

### Where It Goes
Individual chapter files, one instance per result.

### How to Use

**Step 1**: Copy template
```bash
cp RESULT_PRESENTATION_TEMPLATE.tex chapters/result_mp_me.tex
```

**Step 2**: Replace all `[PLACEHOLDERS]`
Search for `[` and replace with actual content:
- `[RESULT NAME]` → "Proton-Electron Mass Ratio"
- `[result_label]` → "mp_me_ratio"
- `[quantity]` → "m_p/m_e"
- `[exact formula]` → "6\pi^5"
- etc.

**Step 3**: Delete optional sections
- If no numerical integration: delete `[Der:Num]` verification
- If no 5D mechanism box needed: delete that section
- If no sensitivity analysis: delete that subsection

**Step 4**: Include in chapter
```latex
% In chapters/chapter_03_frozen.tex

\section{Mass Ratios from Geometry}

\input{chapters/result_mp_me}  % First result
\input{chapters/result_alpha}   % Second result
```

### Example: m_p/m_e

See worked example at end of this guide.

### Quality Checklist

Before finalizing each result:
- [ ] All `[PLACEHOLDERS]` replaced
- [ ] Labels unique (no duplicate `eq:result_formula`)
- [ ] Error budget has numbers (not "TBD")
- [ ] Baseline references Table~\ref{tab:baseline_constants}
- [ ] C_red notation used if normalization unclear
- [ ] Epistemic tag correct ([Dc:Sym] vs [Der:Sym])
- [ ] Cross-references point to actual sections

---

## FILE 3: BOOK2_REORGANIZATION_PLAN_COMPLETE.md

### What It Is
Master roadmap for complete reorganization (602 pages → 17 chapters, 3 Parts).

### Where It Goes
**Not LaTeX** - this is project management document.

Keep in: `docs/` or project root alongside book source.

### How to Use

**Phase-by-Phase Implementation**:

1. **Week 1** (Infrastructure)
   - Create directory structure per plan
   - Set up chapter stubs
   - Prepare templates

2. **Weeks 2-3** (Content Migration)
   - Follow chapter-by-chapter mapping
   - Use content migration notes
   - Track progress in checklist

3. **Weeks 4-5** (Content Addition)
   - Add mechanism boxes (locations specified)
   - Complete missing derivations (listed)
   - Create diagrams (list provided)

4. **Week 6** (Epistemic Integration)
   - Apply EPISTEMIC_STANDARD_COMPLETE.tex
   - Use RESULT_PRESENTATION_TEMPLATE.tex
   - Systematic application

5. **Week 7** (Polish)
   - Cross-references
   - Consistency
   - Quality metrics

6. **Week 8** (Review)
   - Final checks
   - Peer review
   - Corrections

### Key Sections to Reference

- **NEW STRUCTURE** (pages 3-15): Complete outline, 17 chapters
- **IMPLEMENTATION PLAN** (pages 15-17): Week-by-week tasks
- **CONTENT ADDITIONS** (pages 17-20): What needs creating
- **QUALITY METRICS** (pages 20-21): Success criteria
- **DELIVERABLES CHECKLIST** (page 22): Final verification

---

## WORKED EXAMPLE: Integrating m_p/m_e Result

### Step 1: Start with Template
```bash
cp RESULT_PRESENTATION_TEMPLATE.tex temp_mp_me.tex
```

### Step 2: Fill Placeholders
```latex
% Replace:
\subsection{[RESULT NAME]}
% With:
\subsection{Proton-Electron Mass Ratio}

% Replace:
\label{sec:[result_label]}
% With:
\label{sec:mp_me_ratio}

% Replace:
[\text{quantity}] = [\text{exact formula}]
% With:
\frac{m_p}{m_e} = 6\pi^5
```

### Step 3: Add Content
```latex
\textbf{Geometric setup} [P]:

From Book 1, Chapter 3, we established:
\begin{itemize}
\item Proton: Y-junction with 3 strings at 120° (Steiner minimum)
\item Electron: Spherical B³ vortex defect
\item Frozen regime: defects stable at low temperature
\end{itemize}

Energy ratio from defect analysis yields [Dc:Sym]:
\begin{equation}
  \frac{m_p}{m_e} = 6\pi^5 = 1836.1181148335...
  \label{eq:mp_me_formula}
\end{equation}
```

### Step 4: Add Error Budget
```latex
\begin{table}[h]
\centering
\begin{tabular}{llcc}
\hline
\textbf{Correction Source} & \textbf{Mechanism} & \textbf{Estimate} & \textbf{Status} \\
\hline
EM self-energy & $O(\alpha)$ loops & $\sim 0.1\%$ & [Open] \\
RG running & $\beta$-functions & $\sim 0.01\%$ & [Open] \\
Finite-size & $(r_e/R_\xi)^2$ & $< 10^{-6}$ & Negligible \\
$C_{\mathrm{red}}^{(m)}$ & Normalization & Unknown & \textbf{[Open]} \\
\hline
\textbf{Total expected} & & \textbf{0.1--1\%} & --- \\
\textbf{Observed} & & \textbf{0.002\%} & [BL] \\
\hline
\end{tabular}
\caption{Error budget for $m_p/m_e$ ratio}
\label{tab:error_budget_mp_me}
\end{table}
```

### Step 5: Add Comparison
```latex
\textbf{Baseline data} [BL]: Table~\ref{tab:baseline_constants}

PDG 2024 value:
\begin{equation}
  (m_p/m_e)_{\text{exp}} = 1836.15267343 \pm 1.1 \times 10^{-8}
\end{equation}

\textbf{Agreement calculation:}
\begin{align}
\text{EDC prediction:} \quad &1836.1181148... \\
\text{Measurement:} \quad &1836.15267343 \\
\text{Absolute difference:} \quad &|\Delta| = 0.0346 \\
\text{Relative difference:} \quad &\frac{0.0346}{1836.153} = 0.0019\% = 19\,\text{ppm}
\end{align}
```

### Step 6: Include in Chapter
```latex
% In chapters/chapter_03_frozen.tex

\section{Mass Ratios from Geometry}

This section presents geometric predictions for fundamental mass ratios.
All results reference Book 1 for derivational details; here we state 
predictions and compare to measurement.

\input{chapters/result_mp_me}

\input{chapters/result_alpha}

% Continue...
```

---

## DIRECTORY STRUCTURE

Recommended organization:

```
edc_book_2/
├── main.tex                           # Main LaTeX file
├── docs/
│   ├── BOOK2_REORGANIZATION_PLAN_COMPLETE.md
│   ├── INTEGRATION_GUIDE.md (this file)
│   └── progress_tracking.md
├── frontmatter/
│   ├── title.tex
│   ├── abstract.tex
│   └── EPISTEMIC_STANDARD_COMPLETE.tex  ← FILE 1
├── chapters/
│   ├── chapter_00_bridge.tex
│   ├── chapter_01_weak_interface.tex
│   ├── chapter_02_ontology.tex
│   ├── chapter_03_frozen.tex
│   ├── ...
│   ├── chapter_17_beyond.tex
│   ├── result_mp_me.tex              ← From FILE 2 template
│   ├── result_alpha.tex
│   └── ...
├── templates/
│   ├── RESULT_PRESENTATION_TEMPLATE.tex  ← FILE 2
│   ├── mechanism_box_template.tex
│   └── numerical_verification_template.tex
├── figures/
│   ├── 5d_projection_cartoon.pdf
│   ├── y_junction_geometry.pdf
│   └── ...
├── appendices/
│   ├── app_notation.tex
│   ├── app_epistemic.tex
│   ├── app_antipatterns.tex
│   └── app_opr.tex
└── shared/
    ├── macros.tex                    # LaTeX macros
    └── baseline_constants.tex        # Table data
```

---

## LATEX COMPILATION

### Required Packages
```latex
% In preamble (main.tex or book2.tex)

\usepackage{amsmath, amssymb, amsthm}
\usepackage{tcolorbox}         % For mechanism boxes
\usepackage{enumerate}         % For (i), (ii), (iii)
\usepackage{graphicx}          % Figures
\usepackage{booktabs}          % Professional tables
\usepackage{hyperref}          % Cross-references (load last)
\usepackage[margin=1in]{geometry}

% Optional macros
\input{shared/macros}
```

### Compilation Sequence
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or with XeLaTeX (if using Unicode):
```bash
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```

---

## QUALITY ASSURANCE

### Pre-Integration Checks
- [ ] All files compile individually
- [ ] No undefined references in epistemic standard
- [ ] Template has no `[PLACEHOLDER]` left in it
- [ ] Baseline table exists and has label

### Post-Integration Checks
- [ ] Book compiles without errors
- [ ] All cross-references resolve
- [ ] Table/figure numbers correct
- [ ] Epistemic tags consistent
- [ ] No duplicate labels

### Final Audit
- [ ] Every [Dc] result has error budget
- [ ] Every [Der:Num] has verification table
- [ ] All [BL] citations reference baseline table
- [ ] C_red appears wherever normalization mentioned
- [ ] No "TBD" or "TODO" in final version

---

## TROUBLESHOOTING

### Issue: "Undefined reference to tab:baseline_constants"
**Solution**: Ensure baseline table exists and is compiled before referencing chapters.
```latex
% In frontmatter/EPISTEMIC_STANDARD_COMPLETE.tex
\label{tab:baseline_constants}
```

### Issue: "C_{\mathrm{red}} not defined"
**Solution**: Use macro or write out each time.
```latex
% Option 1: Define macro in preamble
\newcommand{\Cred}{C_{\mathrm{red}}}

% Option 2: Write out explicitly
C_{\mathrm{red}}
```

### Issue: Template feels repetitive
**Solution**: This is intentional! Consistency is key. Readers appreciate predictable structure.

### Issue: Some sections don't apply to my result
**Solution**: Delete those subsections. Template is maximal; not every result needs every section.

---

## VERSION CONTROL

### Git Workflow
```bash
# Create feature branch for reorganization
git checkout -b reorganization-v1

# Commit infrastructure
git add chapters/ frontmatter/ templates/
git commit -m "Set up new structure"

# Commit content migrations chapter-by-chapter
git add chapters/chapter_01_weak_interface.tex
git commit -m "Reorganize Ch 1: front-load neutron lifetime"

# Commit epistemic integration
git add frontmatter/EPISTEMIC_STANDARD_COMPLETE.tex
git commit -m "Integrate epistemic standard"

# etc.
```

### Backup Strategy
- Keep `main` branch as original version
- Work on `reorganization-v1` branch
- Tag milestones: `v1.0-infrastructure`, `v1.0-migration`, etc.
- Merge to `main` only after full review

---

## SUPPORT & QUESTIONS

### If You Need Help
1. Check this integration guide first
2. Review BOOK2_REORGANIZATION_PLAN_COMPLETE.md
3. Look at worked example (m_p/m_e above)
4. Consult original session transcript

### Common Questions

**Q: Do I have to reorganize everything at once?**
A: No. Start with high-priority items:
   1. Epistemic standard integration
   2. Bridge Chapter 0
   3. Ch 1 reorganization
   Then proceed chapter-by-chapter.

**Q: What if I find new issues during reorganization?**
A: Document them in `docs/issues_found.md` and decide:
   - Critical (fix now)
   - Important (fix in this version)
   - Minor (defer to next edition)

**Q: Can I modify the template?**
A: Yes, but keep it consistent across all results. 
   If you improve the template, update ALL instances.

**Q: What about the 160-page Chapter 21?**
A: Reduce to 20-page teaser (Chapter 17 in new structure).
   Save full development for Book 3 (Strong Sector).

---

## SUCCESS CRITERIA

Reorganization is complete when:

✅ All 17 chapters exist and compile
✅ Epistemic standard integrated and referenced
✅ Every major result follows template
✅ Bridge Chapter 0 connects Book 1 → Book 2
✅ OPR chapters consolidated (no fragmentation)
✅ Learning curve improved (result by page 20)
✅ All quality metrics met (see plan document)
✅ Peer review completed
✅ Final manuscript ready for publication

---

**END OF INTEGRATION GUIDE**

*Keep this guide alongside reorganization work for reference.*
*Update as you discover better practices during implementation.*
