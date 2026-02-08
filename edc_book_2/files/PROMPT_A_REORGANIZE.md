# Claude Code Prompt: EDC Part II Book Reorganization

## MISSION
Reorganize EDC Part II book from current 21-chapter structure into new 17-chapter structure with 3 Parts, following the detailed mapping plan. Create entirely new folder structure with copied content - DO NOT modify or delete any existing files.

## CRITICAL CONSTRAINTS

### ❌ WHAT YOU MUST NOT DO:
1. **DO NOT delete or modify ANY existing LaTeX files** in the original directory
2. **DO NOT create symbolic links** - all content must be physically copied
3. **DO NOT add new physics, derivations, or proofs** that don't exist in source
4. **DO NOT change existing epistemic tags** [BL], [D], [Dc], [I], [P], [M]
5. **DO NOT alter mathematical content** - copy equations exactly as written
6. **DO NOT rewrite proofs** - preserve original derivation logic
7. **DO NOT add new citations** unless moving existing ones
8. **DO NOT change numerical values** or their precision

### ✅ WHAT YOU MUST DO:
1. **Create new directory**: `EDC_Part2_Reorganized/` completely separate from source
2. **Copy content verbatim** from source files to new structure
3. **Reorganize** by moving sections according to mapping plan
4. **Preserve** all mathematical content, epistemic tags, and derivations exactly
5. **Add only**:
   - New chapter introductions (clearly marked as NEW)
   - Section transitions/bridges
   - Forward/backward references
   - Part summaries
6. **Keep detailed log** of what content came from which source file

---

## INPUT MATERIALS

You will be given:
1. **Current LaTeX source files** (existing book structure)
2. **Reorganization Plan** (`reorganization_plan.md`)
3. **Content Mapping** (`content_mapping.md`)
4. **Executive Summary** (`executive_summary.md`)

---

## OUTPUT STRUCTURE

Create this directory structure:

```
EDC_Part2_Reorganized/
├── main.tex                          # New main file
├── preamble.tex                      # LaTeX packages & settings
├── metadata.tex                      # Title, author, date, license
├── preface.tex                       # Preserved from original
├── reader_contract.tex               # Preserved from original
├── PART_I_Foundations/
│   ├── chapter_01_weak_sector.tex
│   ├── chapter_02_particle_ontology.tex
│   ├── chapter_03_frozen_regime.tex
│   ├── chapter_04_z6_program.tex
│   └── chapter_05_case_studies.tex
├── PART_II_Quantitative/
│   ├── chapter_06_electroweak_params.tex
│   ├── chapter_07_lepton_masses.tex
│   ├── chapter_08_three_generations.tex
│   ├── chapter_09_neutrinos.tex
│   ├── chapter_10_va_structure.tex
│   └── chapter_11_ckm_cp.tex
├── PART_III_Technical/
│   ├── chapter_12_gf_chain.tex
│   ├── chapter_13_core_derivations.tex
│   ├── chapter_14_bvp.tex
│   ├── chapter_15_mediator_coupling.tex
│   └── chapter_16_epistemic_summary.tex
├── EPILOGUE/
│   └── chapter_17_beyond.tex
├── appendices/
│   ├── appendix_a_notation.tex
│   ├── appendix_b_parameters.tex
│   └── appendix_c_open_problems.tex
├── figures/                          # Copy all figures
├── bibliography/
│   └── references.bib                # Preserved from original
├── CONTENT_LOG.md                    # Detailed source tracking
└── REORGANIZATION_NOTES.md           # Changes made
```

---

## STEP-BY-STEP PROCESS

### PHASE 1: Setup
1. Create `EDC_Part2_Reorganized/` directory
2. Copy all figure files to `figures/`
3. Copy bibliography to `bibliography/references.bib`
4. Create empty chapter files for all 17 chapters
5. Initialize `CONTENT_LOG.md` with headers

### PHASE 2: Extract Content (following content_mapping.md)

For each NEW chapter:

1. **Read the mapping** from `content_mapping.md`
2. **Locate source content** in original LaTeX files
3. **Copy content verbatim** to new chapter file
4. **Log the operation** in `CONTENT_LOG.md`:
   ```
   NEW Chapter 3, Section 3.6 (mp/me derivation)
   SOURCE: old_chapter_02.tex, Section 2.8, Lines 450-580
   ACTION: Copied verbatim
   NOTES: No modifications to math or tags
   ```

5. **Add transition text** ONLY if needed to connect moved sections:
   ```latex
   % NEW TRANSITION TEXT - ADDED DURING REORGANIZATION
   Before deriving the proton-electron mass ratio, we first establish...
   % END NEW TEXT
   ```

6. **Add forward/backward references**:
   ```latex
   % ADDED REFERENCE
   (This result will be used in Chapter 12 to derive $G_F$.)
   % END REFERENCE
   ```

### PHASE 3: Build Each Chapter

Follow this template for EVERY chapter:

```latex
\chapter{Chapter Title}
\label{ch:shortname}

% METADATA COMMENT
% SOURCE: Original chapters X, Y, Z
% REORGANIZED: [Date]
% NEW CONTENT: Section introductions only

\section{Introduction}
% NEW CONTENT - Chapter overview
% Explains: (1) What this chapter does
%           (2) What it assumes from previous chapters
%           (3) What later chapters will use
\end{section}

\section{...}
% SOURCE: old_chapter_X.tex, Section X.Y
[COPIED CONTENT - EXACT VERBATIM]
\end{section}

\section{Chapter Summary}
% NEW CONTENT - Brief summary
% Highlights: Key results, epistemic status, forward pointers
\end{section}
```

### PHASE 4: Part Summaries

Create brief summaries at start of each Part:

```latex
\part{Foundations}
\label{part:foundations}

% NEW CONTENT
\chapter*{Part I: Foundations}
\addcontentsline{toc}{chapter}{Part I Overview}

This part establishes the physical framework...

\textbf{What you'll learn:}
\begin{itemize}
\item Chapter 1: ...
\item Chapter 2: ...
\end{itemize}

\textbf{Prerequisites:} EDC Part I knowledge of...

\textbf{What comes next:} Part II builds on these foundations to...
```

### PHASE 5: Main Document

Create `main.tex`:

```latex
\documentclass[11pt,a4paper,twoside,openright]{book}

\input{preamble.tex}
\input{metadata.tex}

\begin{document}

\frontmatter
\maketitle
\input{preface.tex}
\input{reader_contract.tex}
\tableofcontents

\mainmatter

% PART I: FOUNDATIONS
\input{PART_I_Foundations/chapter_01_weak_sector.tex}
\input{PART_I_Foundations/chapter_02_particle_ontology.tex}
\input{PART_I_Foundations/chapter_03_frozen_regime.tex}
\input{PART_I_Foundations/chapter_04_z6_program.tex}
\input{PART_I_Foundations/chapter_05_case_studies.tex}

% PART II: QUANTITATIVE FRAMEWORK
\input{PART_II_Quantitative/chapter_06_electroweak_params.tex}
[... continue for all chapters ...]

% EPILOGUE
\input{EPILOGUE/chapter_17_beyond.tex}

\backmatter
\input{appendices/appendix_a_notation.tex}
\input{appendices/appendix_b_parameters.tex}
\input{appendices/appendix_c_open_problems.tex}

\bibliographystyle{plain}
\bibliography{bibliography/references}

\end{document}
```

---

## CONTENT MAPPING EXECUTION

### Example: Chapter 3 (Frozen Regime)

**Mapping says:**
```
NEW CHAPTER 3: Frozen Regime Foundations
Sources: OLD Ch 2 (mostly intact, reorder for clarity)
3.1 Why Frozen Not Fluid (FROM: Old 2.4)
3.2 Physical Justification (FROM: Old 2.5)
3.3 Ice Wall Analogy (FROM: Old 2.3 - move earlier)
3.4 Electron as Frozen Defect (FROM: Old 2.6)
3.5 Proton as Frozen Y-Junction (FROM: Old 2.7)
3.6 DERIVATION: mp/me = 6π⁵ (FROM: Old 2.8)
3.7 DERIVATION: α (FROM: Old 2.9)
3.8 Numerical Verification (FROM: Old 2.10)
3.9 Integration Map (FROM: Old 2.11)
```

**You do:**
1. Create `chapter_03_frozen_regime.tex`
2. Copy Old 2.4 → New 3.1 (verbatim)
3. Copy Old 2.5 → New 3.2 (verbatim)
4. Copy Old 2.3 → New 3.3 (verbatim) ← Note: reordered
5. Copy Old 2.6 → New 3.4 (verbatim)
6. Copy Old 2.7 → New 3.5 (verbatim)
7. Copy Old 2.8 → New 3.6 (verbatim, keep all math)
8. Copy Old 2.9 → New 3.7 (verbatim, keep all math)
9. Copy Old 2.10 → New 3.8 (verbatim)
10. Copy Old 2.11 → New 3.9 (verbatim)
11. Add chapter introduction (NEW)
12. Add chapter summary (NEW)

**Log it:**
```
Chapter 3: Frozen Regime Foundations
├─ Section 3.1: Copied from old_ch2.tex Section 2.4 (lines 120-180)
├─ Section 3.2: Copied from old_ch2.tex Section 2.5 (lines 181-250)
├─ Section 3.3: Copied from old_ch2.tex Section 2.3 (lines 80-119) ⚠️ REORDERED
├─ Section 3.4: Copied from old_ch2.tex Section 2.6 (lines 251-320)
├─ Section 3.5: Copied from old_ch2.tex Section 2.7 (lines 321-410)
├─ Section 3.6: Copied from old_ch2.tex Section 2.8 (lines 411-580) ⚠️ CONTAINS [D] DERIVATION
├─ Section 3.7: Copied from old_ch2.tex Section 2.9 (lines 581-720) ⚠️ CONTAINS [D] DERIVATION
├─ Section 3.8: Copied from old_ch2.tex Section 2.10 (lines 721-780)
├─ Section 3.9: Copied from old_ch2.tex Section 2.11 (lines 781-850)
├─ Chapter Intro: NEW CONTENT - 15 lines
└─ Chapter Summary: NEW CONTENT - 20 lines

⚠️ No epistemic tags changed
⚠️ No equations modified
⚠️ All numerical values preserved
```

---

## SPECIAL CASES

### Case 1: Consolidating Multiple OPR Chapters → Chapter 13

**Mapping says:**
```
NEW CHAPTER 13: Core Derivations
Sources: OLD Ch 15 (OPR-01), Ch 16 (OPR-04), Ch 17 (OPR-19)
13.1 DERIVATION: Membrane Tension (FROM: Old Ch 15)
13.2 DERIVATION: Wall Thickness (FROM: Old Ch 16)
13.3 DERIVATION: 5D Gauge Coupling (FROM: Old Ch 17)
13.4 Integration Check (NEW)
```

**You do:**
1. Copy entire OLD Ch 15 → New 13.1 (keep all subsections)
2. Copy entire OLD Ch 16 → New 13.2 (keep all subsections)
3. Copy entire OLD Ch 17 → New 13.3 (keep all subsections)
4. Add Section 13.4 (NEW) - cross-checks between the three:
   ```latex
   \section{Integration Check}
   % NEW CONTENT
   Having derived $\sigma$ (Section 13.1), $\Delta$ (Section 13.2), 
   and $g_5$ (Section 13.3), we verify consistency:
   
   \begin{itemize}
   \item Check 1: $\sigma \Delta$ relation from Sections 13.1-13.2
   \item Check 2: Dimensional analysis across all three
   \item Check 3: Parameter ledger consistency (Table 13.1)
   \end{itemize}
   ```

### Case 2: Splitting Chapter 1 → Multiple New Chapters

**Mapping says:**
```
OLD Chapter 1 splits into:
- NEW Ch 1: Sections 1.1-1.4 (overview)
- NEW Ch 2: Section 1.5 (ontology)
- NEW Ch 5: Sections 1.6-1.9 (case studies)
```

**You do:**
1. Copy Old 1.1-1.4 → New Ch 1
2. Copy Old 1.5 → New Ch 2
3. Copy Old 1.6-1.9 → New Ch 5
4. Add transitions in each:
   ```latex
   % In NEW Ch 1 (end):
   This ontological framework is detailed in Chapter 2.
   
   % In NEW Ch 2 (start):
   Building on the interface mechanics from Chapter 1...
   
   % In NEW Ch 5 (start):
   We now apply the ontology (Chapter 2) and frozen regime 
   (Chapter 3) to specific decay processes...
   ```

### Case 3: Expanding Stub Chapters (Ch 5, Ch 11)

**For Chapter 7 (Lepton Masses - currently stub):**

**Mapping says:**
```
NEW CHAPTER 7: Lepton Mass Hierarchy
Sources: OLD Ch 5 (stub - needs expansion)
7.1 The Mass Problem (NEW)
7.2 Candidate Relations (OLD Ch 5.1 + new material)
7.3 Predictions vs Observations (NEW)
7.4 Open Questions (NEW)
```

**You do:**
1. Copy OLD Ch 5.1 → New 7.2 (if exists)
2. Add NEW sections 7.1, 7.3, 7.4:
   ```latex
   \section{The Mass Problem}
   % NEW CONTENT
   The observed lepton masses are [BL]:
   \begin{align}
   m_e &= 0.511 \text{ MeV} \\
   m_\mu &= 105.7 \text{ MeV} \\
   m_\tau &= 1777 \text{ MeV}
   \end{align}
   
   The mass ratios pose a fundamental question...
   
   \section{Candidate Relations}
   % COPIED from old Ch 5.1 if exists
   [...]
   
   \section{Predictions vs Observations}
   % NEW CONTENT - Compare numerical values
   Table 7.1 compares geometric predictions to measurements...
   
   \section{Open Questions}
   % NEW CONTENT - List what's not yet understood
   \begin{enumerate}
   \item Origin of generation hierarchy
   \item Connection to Z6 structure
   \item Testable predictions
   \end{enumerate}
   ```

---

## CONTENT LOG FORMAT

Create `CONTENT_LOG.md` with this structure:

```markdown
# EDC Part II Reorganization - Content Log

## Chapter 1: The Weak Sector in EDC
- Section 1.1: NEW CONTENT (intro)
- Section 1.2: FROM old_ch1.tex Section 1.2 (lines 45-120)
- Section 1.3: FROM old_ch1.tex Section 1.2.2 (lines 121-180)
- Section 1.4: FROM old_ch1.tex Section 1.2.3 (lines 181-250)
- Section 1.5: FROM old_ch1.tex Section 1.4 (lines 400-580), SIMPLIFIED
- Section 1.6: NEW CONTENT (roadmap)

## Chapter 2: Particle Ontology
- Section 2.1: FROM old_ch1.tex Section 1.5.1-1.5.6 (lines 600-900)
- Section 2.2: FROM old_ch1.tex Section 1.5.8 (lines 950-1050)
- Section 2.3: FROM old_ch1.tex Section 1.5.9 (lines 1051-1100)
- Section 2.4: NEW CONTENT (selection rules)

[Continue for all chapters...]

## Statistics
- Total sections copied verbatim: XXX
- Total sections with minor additions: YYY
- Total new sections: ZZZ
- Epistemic tags changed: 0 (NONE - as required)
- Equations modified: 0 (NONE - as required)
```

---

## VERIFICATION CHECKLIST

After completing reorganization, verify:

### ✅ Structural Checks
- [ ] All 17 chapters exist and compile
- [ ] All figures copied to new directory
- [ ] Bibliography compiles correctly
- [ ] Table of contents generates properly
- [ ] All cross-references valid

### ✅ Content Integrity Checks
- [ ] Every [D] derivation from source appears in new structure
- [ ] All epistemic tags [BL][D][Dc][I][P][M] unchanged
- [ ] All equations identical to source (LaTeX code exact match)
- [ ] All numerical values unchanged (same precision)
- [ ] All citations preserved

### ✅ Completeness Checks
- [ ] No orphaned content (everything from source mapped)
- [ ] No missing sections per mapping plan
- [ ] All "stub" chapters expanded with NEW content clearly marked
- [ ] All consolidations properly merged

### ✅ Documentation Checks
- [ ] CONTENT_LOG.md complete for all chapters
- [ ] REORGANIZATION_NOTES.md lists all changes
- [ ] Source line numbers recorded for major derivations
- [ ] NEW content clearly marked in LaTeX comments

---

## FINAL DELIVERABLE

The `EDC_Part2_Reorganized/` directory should be:
1. **Self-contained**: Compiles independently of source
2. **Documented**: Clear log of what came from where
3. **Preserved**: All original physics/math intact
4. **Enhanced**: Better structure, navigation, readability
5. **Auditable**: Easy to verify no content was lost or changed

---

## EXAMPLE SNIPPET

Here's what a properly reorganized section looks like:

```latex
% =============================================================================
% CHAPTER 3: FROZEN REGIME FOUNDATIONS
% SOURCE: old_chapter_02.tex (Chapter 2)
% REORGANIZED: 2026-01-30
% =============================================================================

\chapter{Frozen Regime Foundations}
\label{ch:frozen-regime}

% -----------------------------------------------------------------------------
% METADATA COMMENT
% This chapter reorganizes content from original Chapter 2
% All mathematical content preserved verbatim
% New additions: Chapter intro (Sec 3.0) and summary (Sec 3.10)
% -----------------------------------------------------------------------------

\section*{Chapter Overview}
\addcontentsline{toc}{section}{Overview}
% NEW CONTENT - ADDED DURING REORGANIZATION
This chapter establishes the ``frozen regime'' -- the fundamental ansatz
that distinguishes EDC from Ginzburg-Landau field theory...

\textbf{What this chapter delivers:}
\begin{itemize}
\item Physical justification for frozen limit (Sec 3.1-3.2)
\item Electron and proton as frozen defects (Sec 3.4-3.5)  
\item Two fundamental derivations [D]:
  \begin{itemize}
  \item Mass ratio: $m_p/m_e = 6\pi^5$ (Sec 3.6)
  \item Fine structure constant: $\alpha$ (Sec 3.7)
  \end{itemize}
\end{itemize}

\textbf{Prerequisites:} EDC Part I, basic QFT

\textbf{Forward dependencies:} Z6 program (Ch 4), weak sector (Ch 6-11)
% END NEW CONTENT

% -----------------------------------------------------------------------------
\section{Why Frozen Not Fluid}
\label{sec:frozen-vs-fluid}
% SOURCE: old_chapter_02.tex, Section 2.4, Lines 120-180
% COPIED VERBATIM - NO MODIFICATIONS
% -----------------------------------------------------------------------------

The crucial difference between EDC and conventional Ginzburg-Landau theory...

[EXACT COPY OF ORIGINAL CONTENT]

% -----------------------------------------------------------------------------
\section{Physical Justification for Frozen Limit}
\label{sec:frozen-justification}
% SOURCE: old_chapter_02.tex, Section 2.5, Lines 181-250  
% COPIED VERBATIM - NO MODIFICATIONS
% -----------------------------------------------------------------------------

We justify the frozen limit through three arguments...

[EXACT COPY OF ORIGINAL CONTENT]

% ... [continue for all sections]

% -----------------------------------------------------------------------------
\section{Derivation: Mass Ratio $m_p/m_e = 6\pi^5$}
\label{sec:mass-ratio-derivation}
% SOURCE: old_chapter_02.tex, Section 2.8, Lines 411-580
% ⚠️ EPISTEMIC TAG: [D] - DERIVED RESULT
% ⚠️ COPIED VERBATIM - ALL EQUATIONS PRESERVED EXACTLY
% -----------------------------------------------------------------------------

\begin{derivation}[Mass Ratio from Frozen Y-Junction Geometry] % [D]
Starting from the frozen Y-junction configuration...

\begin{align}
m_p &= \frac{3\sigma \ell_p}{r_e} \tag{junction energy} \\
m_e &= \frac{\sigma r_e}{2} \tag{spherical defect energy}
\end{align}

[EXACT COPY OF FULL DERIVATION - ALL STEPS PRESERVED]

Therefore:
\begin{equation}
\boxed{\frac{m_p}{m_e} = 6\pi^5 = 1836.118} \tag{[D]}
\end{equation}

Empirical value [BL]: $1836.152$

Error: $0.0018\%$
\end{derivation}

% END VERBATIM COPY

% -----------------------------------------------------------------------------
\section*{Chapter Summary}
\addcontentsline{toc}{section}{Summary}
% NEW CONTENT - ADDED DURING REORGANIZATION
% -----------------------------------------------------------------------------

\textbf{Key Results:}
\begin{itemize}
\item Frozen regime justified physically and topologically
\item Two fundamental constants derived from geometry [D]:
  \begin{itemize}
  \item $m_p/m_e = 6\pi^5$ (0.0018\% error)
  \item $\alpha = (4\pi + 5/6)/(6\pi^5)$ (0.0067\% error)
  \end{itemize}
\end{itemize}

\textbf{Forward to Chapter 4:} The Z6 program extends these results to...
% END NEW CONTENT
```

---

## IMPORTANT REMINDERS

1. **Never modify original files** - work only in `EDC_Part2_Reorganized/`
2. **Copy equations exactly** - including spacing, alignment, tags
3. **Preserve all comments** from original LaTeX
4. **Keep epistemic tags** [BL][D][Dc][I][P][M] unchanged
5. **Mark NEW content** with clear comments
6. **Log everything** in CONTENT_LOG.md
7. **Compile frequently** to catch errors early
8. **Ask before adding** any content not in mapping plan

---

## SUCCESS CRITERIA

✅ Book compiles without errors
✅ All content from source present in reorganized version  
✅ No epistemic tags changed
✅ No equations modified
✅ Content log complete and accurate
✅ Original files untouched
✅ New structure matches mapping plan exactly

---

**READY TO START?**

Begin with Chapter 1 (simplest) as test case, then proceed systematically through all 17 chapters following the content mapping.
