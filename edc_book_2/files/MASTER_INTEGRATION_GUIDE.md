# MASTER INTEGRATION GUIDE FOR EDC BOOK 2

**Version**: 1.0 Final  
**Date**: 2026-01-30  
**Purpose**: Step-by-step guide for integrating all epistemic framework components

---

## OVERVIEW

This guide provides complete instructions for integrating:
1. Epistemic Standard (revised)
2. Baseline Constants Table
3. Result Presentation Template
4. LaTeX Macros
5. Reorganization Structure

---

## FILE INVENTORY

All files ready for integration:

| File | Purpose | Integration Location |
|------|---------|---------------------|
| `EPISTEMIC_STANDARD_COMPLETE_FINAL.tex` | Core framework | Chapter 0 or Preface |
| `BASELINE_CONSTANTS_TABLE.tex` | [BL] reference | Chapter 0 or Appendix A |
| `RESULT_TEMPLATE_COMPLETE.tex` | Template | Use for every major result |
| `EDC_MACROS_COMPLETE.tex` | Macros | Preamble of main.tex |
| `BOOK2_REORGANIZATION_PLAN_FINAL.md` | Structure guide | Implementation reference |

---

## STEP-BY-STEP INTEGRATION

### STEP 1: Prepare Repository

```bash
# Navigate to Book 2 directory
cd edc_book_2/

# Create backup of current state
git checkout -b backup-before-reorganization

# Create new reorganization branch
git checkout -b reorganization-v1-epistemic-framework

# Create new directory structure
mkdir -p reorganized/{part1,part2,part3,epilogue,bridge}
mkdir -p reorganized/includes
mkdir -p reorganized/figures
```

---

### STEP 2: Add Macros to Preamble

**File**: `main.tex` (or your main LaTeX file)

**Location**: After `\documentclass` and package imports, before `\begin{document}`

**Action**:
```latex
% ============================================================
% EDC Epistemic Framework Macros
% ============================================================
\input{includes/EDC_MACROS_COMPLETE}
```

**Copy file**:
```bash
cp EDC_MACROS_COMPLETE.tex reorganized/includes/
```

---

### STEP 3: Create Bridge Chapter 0

**File**: `reorganized/bridge/chapter_0_bridge.tex`

**Action**: Create new file with content:

```latex
\chapter{Bridge: From Book 1 to Weak Sector}
\label{ch:bridge}

\section{What Book 1 Established}

\subsection{Derived Fundamental Constants \tagDer}

Book 1 derived these from pure 5D geometry:

\begin{itemize}
\item \textbf{Proton-Electron Mass Ratio}:
  \begin{equation}
  \mpme = 6\pi^5 = 1836.12
  \end{equation}
  Observed: $1836.15$ \tagBL{} --- Error: $0.002\%$
  
  \textit{Derivation location}: Book 1, Chapter [X]
  
  \textit{Key insight}: Ratio of Y-junction to spherical defect energies

\item \textbf{Fine Structure Constant}:
  \begin{equation}
  \alphaInv = \frac{6\pi^5}{4\pi + 5/6} = 136.92
  \end{equation}
  Observed: $137.04$ \tagBL{} --- Error: $0.08\%$
  
  \textit{Derivation location}: Book 1, Chapter [Y]

\item \textbf{Neutron-Proton Mass Difference}:
  \begin{equation}
  \DeltaMnp = \frac{8m_e}{\pi} = 1.301 \text{ MeV}
  \end{equation}
  Observed: $1.293$ MeV \tagBL{} --- Error: $0.6\%$
  
  \textit{Derivation location}: Book 1, Chapter [Z]
\end{itemize}

\textbf{Important}: These are NOT fitted! They are geometric predictions.

[Continue with remaining sections from reorganization plan...]

\section{What Book 2 Adds}
[Content from plan]

\section{Reading Strategy}
[Content from plan]
```

---

### STEP 4: Integrate Epistemic Standard

**File**: `reorganized/bridge/epistemic_standard.tex`

**Action**: 
```bash
cp EPISTEMIC_STANDARD_COMPLETE_FINAL.tex reorganized/bridge/epistemic_standard.tex
```

**In main.tex**, add after Bridge Chapter 0:
```latex
\input{bridge/epistemic_standard}
```

---

### STEP 5: Add Baseline Constants Table

**Option A**: In Preface (recommended for frequent reference)
```latex
% In main.tex, before \mainmatter
\input{bridge/BASELINE_CONSTANTS_TABLE}
```

**Option B**: In Appendix (if cleaner structure preferred)
```latex
% In main.tex, in appendices section
\appendix
\chapter{Baseline Constants}
\input{appendices/BASELINE_CONSTANTS_TABLE}
```

**Copy file**:
```bash
cp BASELINE_CONSTANTS_TABLE.tex reorganized/bridge/
# or
cp BASELINE_CONSTANTS_TABLE.tex reorganized/appendices/
```

---

### STEP 6: Apply Result Template

**For each major result** (m_p/m_e, α, sin²θ_W, G_F, etc.):

1. **Copy template**:
```bash
cp RESULT_TEMPLATE_COMPLETE.tex reorganized/part1/result_mp_me.tex
```

2. **Fill in placeholders**:
   - Replace `[Result Name]` → "Proton-Electron Mass Ratio"
   - Replace `[result_label]` → "mp_me_ratio"
   - Fill in all `[...]` bracketed sections
   - Delete unused rows in error budget
   - Update cross-references

3. **Include in chapter**:
```latex
% In chapter file
\input{part1/result_mp_me}
```

**Repeat for each major result**.

---

### STEP 7: Reorganize Chapter Structure

**Current structure** (original):
```
chapters/
  chapter_01_weak_interface.tex  (84 pages)
  chapter_02_frozen_regime.tex
  ...
  chapter_13_OPR_first_attempts.tex
  ...
  chapter_21_nuclear_teaser.tex
```

**New structure**:
```
reorganized/
  bridge/
    chapter_0_bridge.tex          (NEW - 15 pages)
    epistemic_standard.tex
  part1/
    chapter_1_weak_interface.tex  (REVISED - 50 pages)
    chapter_2_ontology.tex
    chapter_3_frozen.tex
    chapter_4_z6_program.tex
    chapter_5_case_studies.tex
  part2/
    chapter_6_electroweak.tex
    chapter_7_leptons.tex
    chapter_8_generations.tex
    chapter_9_neutrinos.tex
    chapter_10_va_structure.tex
    chapter_11_ckm.tex
  part3/
    chapter_12_gf_chain.tex       (CONSOLIDATED)
    chapter_13_foundation_params.tex
    chapter_14_bvp.tex
    chapter_15_mw_gf.tex
    chapter_16_epistemic_summary.tex
  epilogue/
    chapter_17_beyond.tex
```

**In main.tex**:
```latex
\mainmatter

% Bridge
\input{bridge/chapter_0_bridge}

% Part I
\part{Foundations \& Mechanisms}
\input{part1/chapter_1_weak_interface}
\input{part1/chapter_2_ontology}
\input{part1/chapter_3_frozen}
\input{part1/chapter_4_z6_program}
\input{part1/chapter_5_case_studies}

% Part II
\part{Predictions \& Observables}
\input{part2/chapter_6_electroweak}
\input{part2/chapter_7_leptons}
\input{part2/chapter_8_generations}
\input{part2/chapter_9_neutrinos}
\input{part2/chapter_10_va_structure}
\input{part2/chapter_11_ckm}

% Part III
\part{Technical Derivations}
\input{part3/chapter_12_gf_chain}
\input{part3/chapter_13_foundation_params}
\input{part3/chapter_14_bvp}
\input{part3/chapter_15_mw_gf}
\input{part3/chapter_16_epistemic_summary}

% Epilogue
\input{epilogue/chapter_17_beyond}

% Appendices
\appendix
\input{appendices/opr_register}
\input{appendices/notation}
```

---

### STEP 8: Migration Script for Content

**Create**: `migrate_content.sh`

```bash
#!/bin/bash
# Content migration script

# Source directory
SRC="chapters"
# Destination directory
DST="reorganized"

# Map old chapters to new structure
# Chapter 1 → Chapter 1 (revised)
echo "Migrating Chapter 1..."
cp $SRC/chapter_01_weak_interface.tex $DST/part1/chapter_1_weak_interface_OLD.tex

# Chapter 2 → Chapter 3 (frozen regime)
echo "Migrating Chapter 2..."
cp $SRC/chapter_02_frozen_regime.tex $DST/part1/chapter_3_frozen_OLD.tex

# Chapters 13-19 → Consolidate to 12-15
echo "Consolidating OPR chapters..."
mkdir -p $DST/part3/OPR_fragments
cp $SRC/chapter_13*.tex $DST/part3/OPR_fragments/
cp $SRC/chapter_14*.tex $DST/part3/OPR_fragments/
# ... continue for 15-19

echo "Migration complete. Review OLD files and integrate into new structure."
```

**Run**:
```bash
chmod +x migrate_content.sh
./migrate_content.sh
```

---

### STEP 9: Add "5D Mechanism" Boxes

**Template** for mechanism box:
```latex
\begin{mdframed}[frametitle={\colorbox{white}{\textbf{5D Mechanism: [Title]}}},
                 linewidth=2pt,
                 linecolor=blue]

\textbf{Physical Picture in 5D:}
[Describe what's actually happening in 5D geometry]

\textbf{Key Geometric Features:}
\begin{itemize}
\item Feature 1 [with parameter values]
\item Feature 2 [with parameter values]
\end{itemize}

\textbf{Mathematical Framework:}
[Key equations, brief derivation sketch]

\textbf{3D Observable Consequence:}
[What 3D observer sees/measures]

\textbf{Validation:}
[Comparison to experiment, error bars]

\textbf{Epistemic Status:} [tag with explanation]

\end{mdframed}
```

**Required boxes** (from reorganization plan):
1. Thick brane necessity (Ch 1)
2. Neutrino edge mode (Ch 1, 9)
3. Z6→SU(3) emergence (Ch 4)
4. Frozen projection (Ch 3)
5. Junction relaxation (Ch 5)
... [continue for all 20]

**Add to each relevant chapter**.

---

### STEP 10: Create Visual Dependency Graph

**File**: `reorganized/figures/dependency_graph_opr.tex`

**Using TikZ**:
```latex
\begin{tikzpicture}[
  node distance=2cm,
  box/.style={rectangle, draw, thick, minimum width=3cm, minimum height=1cm},
  arrow/.style={->, thick}
]

% Nodes
\node[box] (sigma) {$\sigma$ [Dc] \\ OPR-01};
\node[box, right of=sigma] (delta) {$\delta$ [Dc] \\ OPR-04};
\node[box, below of=sigma] (g5) {$g_5$ [Dc] \\ OPR-19};
\node[box, below of=delta] (bvp) {BVP [Open] \\ OPR-21};
\node[box, below of=bvp] (mw) {$M_W$ [Blocked] \\ OPR-20};
\node[box, below of=g5] (gf) {$G_F$ [Partial] \\ OPR-22};

% Arrows
\draw[arrow] (sigma) -- (bvp);
\draw[arrow] (delta) -- (bvp);
\draw[arrow] (bvp) -- (mw);
\draw[arrow] (g5) -- (gf);
\draw[arrow] (mw) -- (gf);

% Legend
\node[below of=gf, yshift=-1cm] {
  \begin{tabular}{ll}
  [Dc] & Established \\
  [Open] & Not solved \\
  [Blocked] & Depends on [Open]
  \end{tabular}
};

\end{tikzpicture}
```

**Include in Chapter 12**:
```latex
\begin{figure}[h]
\centering
\input{figures/dependency_graph_opr}
\caption{Dependency graph for G_F derivation chain}
\label{fig:dependency_opr}
\end{figure}
```

---

### STEP 11: Audit All Epistemic Tags

**Create audit script**: `audit_tags.sh`

```bash
#!/bin/bash
# Audit epistemic tags across all files

echo "=== Epistemic Tag Audit ==="
echo ""

# Find all uses of old-style tags without subtags
echo "Checking for [Der] without subtag..."
grep -rn "\\[Der\\]" reorganized/*.tex | grep -v "Der:Sym" | grep -v "Der:Num"

echo ""
echo "Checking for [Dc] without subtag..."
grep -rn "\\[Dc\\]" reorganized/*.tex | grep -v "Dc:Sym" | grep -v "Dc:Num" | grep -v "Dc:Approx"

echo ""
echo "Checking for uses of C_red..."
grep -rn "C_{\\\\mathrm{red}}" reorganized/*.tex | wc -l

echo ""
echo "Checking for baseline table references..."
grep -rn "Table~\\\\ref{tab:baseline_constants}" reorganized/*.tex | wc -l

echo "Audit complete."
```

**Run and fix issues**:
```bash
chmod +x audit_tags.sh
./audit_tags.sh
```

**Fix**: Add appropriate subtags where missing.

---

### STEP 12: Compile and Test

**Compile document**:
```bash
cd reorganized/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

**Check**:
- [ ] Document compiles without errors
- [ ] All references resolve (no ?? marks)
- [ ] Table of contents correct
- [ ] All figures display
- [ ] Cross-references work
- [ ] Epistemic tags render correctly
- [ ] Baseline table accessible

---

### STEP 13: Quality Checks

**Checklist**:

- [ ] All major results use template
- [ ] All [Dc] results reference $C_{\mathrm{red}}$
- [ ] All [BL] comparisons cite Table~\ref{tab:baseline_constants}
- [ ] All [Der:Num] results have 3-method verification
- [ ] No [Der] without complete derivation
- [ ] No circular reasoning (check dependency graph)
- [ ] All forward references resolve
- [ ] All "5D Mechanism" boxes present
- [ ] Status boxes after each major result
- [ ] Bridge Chapter 0 complete
- [ ] OPR consolidated (not scattered)

---

### STEP 14: Version Control

**Commit structure**:

```bash
# Stage changes incrementally
git add reorganized/bridge/
git commit -m "Add Bridge Chapter 0 and Epistemic Standard"

git add reorganized/includes/EDC_MACROS_COMPLETE.tex
git commit -m "Add epistemic framework macros"

git add reorganized/part1/
git commit -m "Reorganize Part I: Foundations"

git add reorganized/part2/
git commit -m "Reorganize Part II: Predictions"

git add reorganized/part3/
git commit -m "Consolidate Part III: Technical (OPR chapters)"

git add reorganized/epilogue/
git commit -m "Add Epilogue"

# Final commit
git commit -m "Complete reorganization v1.0 - epistemic framework integrated"
```

---

## VERIFICATION CHECKLIST

### Before Going Live

- [ ] Backup original version tagged
- [ ] All files compile without errors
- [ ] All cross-references resolve
- [ ] Epistemic tags consistent throughout
- [ ] Baseline table complete and referenced
- [ ] Result template applied to all major results
- [ ] "5D Mechanism" boxes present (~20)
- [ ] Visual dependency graph included
- [ ] Missing derivations completed or clearly marked [Open]
- [ ] Book 1 integration clear (Bridge Ch 0)
- [ ] OPR consolidated (Ch 12-15)
- [ ] No circular reasoning detected
- [ ] Learning curve improved (result in first 20 pages)
- [ ] Peer review completed
- [ ] Final proofread done

---

## TROUBLESHOOTING

### Common Issues

**Issue**: References not resolving
```
Solution: Run pdflatex + bibtex + pdflatex + pdflatex (3 times total)
```

**Issue**: Macros not found
```
Solution: Check \input{includes/EDC_MACROS_COMPLETE} is before \begin{document}
```

**Issue**: Baseline table not displaying
```
Solution: Check table label: \label{tab:baseline_constants}
          Check reference: \ref{tab:baseline_constants}
```

**Issue**: Epistemic tags rendering as plain text
```
Solution: Check macros loaded: \tagDcSym should render as [Dc:Sym]
```

**Issue**: Dependency graph not showing
```
Solution: Install tikz package: \usepackage{tikz}
```

---

## POST-INTEGRATION

### After Successful Integration

1. **Archive old version**:
```bash
git tag -a v0-original -m "Original 602-page version before reorganization"
```

2. **Tag new version**:
```bash
git tag -a v1.0-reorganized -m "Reorganized version with epistemic framework"
```

3. **Update documentation**:
   - README
   - Build instructions
   - Contributor guide

4. **Announce to collaborators**:
   - New structure
   - New templates required
   - Epistemic framework mandatory

---

## MAINTENANCE

### Going Forward

**For new results**:
1. Always use `RESULT_TEMPLATE_COMPLETE.tex`
2. Reference `\refBaseline` for [BL] values
3. Use macros (`\tagDcSym`, `\Cred`, etc.)
4. Add to appropriate Part (I/II/III)
5. Update dependency graph if relevant

**For corrections**:
1. Check if affects error budget
2. Update status box
3. Verify cross-references still valid
4. Re-run audit script

---

## CONTACT & SUPPORT

**Questions about integration**:
- Refer to this guide first
- Check reorganization plan for detailed explanations
- Consult epistemic standard for tag usage

**Technical issues**:
- LaTeX compilation errors → check package versions
- Reference issues → verify labels match
- Macro issues → verify macros file loaded in preamble

---

*End of Integration Guide*
