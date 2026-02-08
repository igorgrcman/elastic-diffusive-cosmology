# Claude Code Prompt: LaTeX Files Consolidation (Option B)

## MISSION
Consolidate all LaTeX source files from EDC Part II book into a manageable set of files for upload to Claude.ai, preserving complete content while organizing for easy navigation and analysis.

## GOAL
Create a consolidated package that:
1. Contains ALL LaTeX content from the book
2. Is organized in logical chunks (not one massive file)
3. Preserves all equations, derivations, and epistemic tags exactly
4. Can be easily uploaded to Claude.ai (respecting file size limits)
5. Enables human review and reorganization planning

---

## CRITICAL CONSTRAINTS

### ❌ WHAT YOU MUST NOT DO:
1. **DO NOT modify any mathematical content** - copy equations exactly
2. **DO NOT change epistemic tags** [BL], [D], [Dc], [I], [P], [M]
3. **DO NOT alter derivations** - preserve logic flow
4. **DO NOT remove content** - everything must be included
5. **DO NOT compress or minify** LaTeX code

### ✅ WHAT YOU MUST DO:
1. **Consolidate** scattered LaTeX files into organized structure
2. **Preserve** all content verbatim
3. **Document** source file mapping clearly
4. **Organize** by logical sections for easy navigation
5. **Tag** each section with original source file
6. **Create** clear table of contents/index

---

## INPUT
- Directory containing current EDC Part II LaTeX source files
- May include: `main.tex`, chapter files, section files, preamble, etc.

---

## OUTPUT STRUCTURE

Create consolidated package in `EDC_Part2_Consolidated/`:

```
EDC_Part2_Consolidated/
├── 00_METADATA.md                    # Book info, structure, tags
├── 01_PREAMBLE.tex                   # All packages, commands, environments
├── 02_FRONTMATTER.tex                # Title, preface, reader contract, TOC
├── 03_CH01_WeakInterface.tex         # Chapter 1 complete
├── 04_CH02_FrozenRegime.tex          # Chapter 2 complete
├── 05_CH03_Z6Program.tex             # Chapter 3 complete
├── 06_CH04_ElectroweakParams.tex     # Chapter 4 complete
├── 07_CH05_LeptonMasses.tex          # Chapter 5 complete (if exists)
├── 08_CH06_ThreeGenerations.tex      # Chapter 6 complete
├── 09_CH07_Neutrinos.tex             # Chapter 7 complete
├── 10_CH08_CKM_CP.tex                # Chapter 8 complete
├── 11_CH09_FermiConstant.tex         # Chapter 9 complete
├── 12_CH10_VA_Structure.tex          # Chapter 10 complete
├── 13_CH11_ElectroweakBridge.tex     # Chapter 11 complete (if exists)
├── 14_CH12_EpistemicLandscape.tex    # Chapter 12 complete
├── 15_CH13_OPR_Attempts.tex          # Chapter 13 complete
├── 16_CH14_OPR21_BVP.tex             # Chapter 14 complete
├── 17_CH15_OPR01_Sigma.tex           # Chapter 15 complete
├── 18_CH16_OPR04_Delta.tex           # Chapter 16 complete
├── 19_CH17_OPR19_g5.tex              # Chapter 17 complete
├── 20_CH18_OPR20_Mediator.tex        # Chapter 18 complete
├── 21_CH19_OPR22_Geff.tex            # Chapter 19 complete
├── 22_CH20_EpistemicSummary.tex      # Chapter 20 complete
├── 23_CH21_NuclearStructure.tex      # Chapter 21 complete
├── 24_BACKMATTER.tex                 # Appendices, bibliography
├── 25_FIGURES_LIST.md                # List of all figures with descriptions
├── 26_BIBLIOGRAPHY.bib               # Complete bibliography
├── SOURCE_MAP.md                     # Detailed source file mapping
└── CONSOLIDATION_LOG.md              # What was done

```

---

## CONSOLIDATION PROCESS

### STEP 1: Analyze Source Structure

1. **Scan directory** for all `.tex` files
2. **Identify main file** (usually `main.tex`)
3. **Map dependencies**:
   - Which files are `\input{}` or `\include{}`
   - Which are chapters, sections, subsections
   - Which are preamble/frontmatter/backmatter
4. **List all figures** referenced
5. **Extract bibliography** file

Create initial report: `SOURCE_ANALYSIS.md`

### STEP 2: Extract and Organize Preamble

Create `01_PREAMBLE.tex`:

```latex
% =============================================================================
% EDC PART II - CONSOLIDATED PREAMBLE
% Source: [list all preamble source files]
% =============================================================================

% -----------------------------------------------------------------------------
% DOCUMENT CLASS
% Source: main.tex line X
% -----------------------------------------------------------------------------
% Original: \documentclass[11pt,a4paper]{book}
% (Comment out for consolidation, but preserved for reference)

% -----------------------------------------------------------------------------
% PACKAGES
% Source: preamble.tex lines Y-Z
% -----------------------------------------------------------------------------
\usepackage{amsmath}
\usepackage{amssymb}
[... all packages ...]

% -----------------------------------------------------------------------------
% CUSTOM COMMANDS
% Source: preamble.tex lines A-B
% -----------------------------------------------------------------------------
\newcommand{\Plenum}{\text{Plenum}}
[... all custom commands ...]

% -----------------------------------------------------------------------------
% CUSTOM ENVIRONMENTS
% Source: preamble.tex lines C-D
% -----------------------------------------------------------------------------
\newtheorem{derivation}{Derivation}
[... all environments ...]

% -----------------------------------------------------------------------------
% FORMATTING SETTINGS
% Source: preamble.tex lines E-F
% -----------------------------------------------------------------------------
\setlength{\parindent}{0pt}
[... all settings ...]
```

### STEP 3: Consolidate Frontmatter

Create `02_FRONTMATTER.tex`:

```latex
% =============================================================================
% EDC PART II - FRONTMATTER
% Source: Multiple files
% =============================================================================

% -----------------------------------------------------------------------------
% TITLE PAGE
% Source: main.tex, metadata.tex
% -----------------------------------------------------------------------------
% Original title, author, date, license information
[... copy verbatim ...]

% -----------------------------------------------------------------------------
% PREFACE
% Source: preface.tex
% -----------------------------------------------------------------------------
\chapter*{Preface}
[... copy verbatim ...]

% -----------------------------------------------------------------------------
% READER CONTRACT
% Source: reader_contract.tex (if exists)
% -----------------------------------------------------------------------------
\chapter*{Reader Contract}
[... copy verbatim ...]

% -----------------------------------------------------------------------------
% TABLE OF CONTENTS
% Source: Generated, but structure preserved
% -----------------------------------------------------------------------------
% [Original TOC structure as comment for reference]
```

### STEP 4: Consolidate Each Chapter

For EACH chapter, create numbered file `0X_CHYY_Title.tex`:

```latex
% =============================================================================
% CHAPTER [N]: [TITLE]
% Source Files: [list all source files that contributed to this chapter]
% Original Location: Chapter [X] in source
% Page Range: [if known]
% =============================================================================

% CHAPTER METADATA
% Original Chapter Number: X
% Original File(s): chapter_X.tex, section_X_Y.tex, etc.
% Sections: [list all section numbers and titles]
% Epistemic Tags Present: [list which tags appear: D, BL, P, etc.]
% Key Results: [brief list]

% =============================================================================
% CHAPTER CONTENT - COPIED VERBATIM FROM SOURCE
% =============================================================================

\chapter{[Title]}
\label{ch:[label]}

% -----------------------------------------------------------------------------
% SECTION X.1: [Title]
% Source: [filename], lines [X-Y]
% -----------------------------------------------------------------------------

[EXACT COPY OF SECTION CONTENT]

% -----------------------------------------------------------------------------
% SECTION X.2: [Title]  
% Source: [filename], lines [A-B]
% -----------------------------------------------------------------------------

[EXACT COPY OF SECTION CONTENT]

[... continue for all sections ...]

% =============================================================================
% END CHAPTER [N]
% =============================================================================
```

**Example for Chapter 2:**

```latex
% =============================================================================
% CHAPTER 2: FROZEN REGIME FOUNDATIONS
% Source Files: chapter_02_frozen.tex, frozen_regime.tex
% Original Location: Chapter 2
% Page Range: 85-98
% =============================================================================

% CHAPTER METADATA
% Original Chapter Number: 2
% Original File(s): chapter_02_frozen.tex
% Sections: 2.1-2.11 (11 sections total)
% Epistemic Tags Present: [D] (2.8, 2.9), [P] (2.5), [BL] (2.10)
% Key Results: 
%   - mp/me = 6π^5 [D]
%   - α = (4π + 5/6)/(6π^5) [D]

% =============================================================================
% CHAPTER CONTENT
% =============================================================================

\chapter{Frozen Regime Foundations}
\label{ch:frozen-regime}

% -----------------------------------------------------------------------------
% SECTION 2.1: Reader Map
% Source: chapter_02_frozen.tex, lines 15-45
% -----------------------------------------------------------------------------

\section{Reader Map}
\label{sec:frozen-reader-map}

[EXACT VERBATIM COPY]

% -----------------------------------------------------------------------------
% SECTION 2.2: EDC Framework Recap
% Source: chapter_02_frozen.tex, lines 46-120
% -----------------------------------------------------------------------------

\section{EDC Framework Recap}
\label{sec:frozen-framework}

[EXACT VERBATIM COPY]

% ... [continue for all 11 sections]

% -----------------------------------------------------------------------------
% SECTION 2.8: Mass Ratio mp/me = 6π^5
% Source: chapter_02_frozen.tex, lines 450-620
% ⚠️ EPISTEMIC TAG: [D] - DERIVED RESULT
% ⚠️ CRITICAL DERIVATION - PRESERVE EXACTLY
% -----------------------------------------------------------------------------

\section{Mass Ratio $m_p/m_e = 6\pi^5$}
\label{sec:mass-ratio}

\begin{derivation}[Proton-Electron Mass Ratio] % [D]

[EXACT VERBATIM COPY OF FULL DERIVATION]

\begin{equation}
\boxed{\frac{m_p}{m_e} = 6\pi^5 = 1836.118} \tag{[D]}
\end{equation}

Empirical value [BL]: $1836.152$

Relative error: $\frac{1836.152 - 1836.118}{1836.152} = 0.0018\%$

\end{derivation}

% =============================================================================
% END CHAPTER 2
% =============================================================================
```

### STEP 5: Extract Figures Information

Create `25_FIGURES_LIST.md`:

```markdown
# EDC Part II - Figures Inventory

## Chapter 1: The Weak Interface

### Figure 1.1: Interface Pipeline Diagram
- File: `figures/ch1_pipeline.pdf` or `.png`
- Caption: "Energy flow through brane-bulk interface..."
- Referenced in: Section 1.4.8
- Source: chapter_01.tex, line 456

### Figure 1.2: Ontology Map
- File: `figures/ch1_ontology.pdf`
- Caption: "Five particle ontological categories..."
- Referenced in: Section 1.5.7
- Source: chapter_01.tex, line 678

[... continue for all figures ...]

## Chapter 2: Frozen Regime Foundations

### Figure 2.1: Ice Wall Analogy
- File: `figures/ch2_ice_wall.pdf`
- Caption: "Schematic of frozen vs fluid..."
- Referenced in: Section 2.3
- Source: chapter_02.tex, line 123

[... etc ...]

## Statistics
- Total figures: [count]
- Missing files: [list any referenced but not found]
- File formats: PDF, PNG, etc.
```

### STEP 6: Create Source Mapping

Create `SOURCE_MAP.md`:

```markdown
# Source File Mapping

## Original Structure → Consolidated Files

### Preamble and Settings
- `preamble.tex` → `01_PREAMBLE.tex`
- `packages.tex` → `01_PREAMBLE.tex`
- `custom_commands.tex` → `01_PREAMBLE.tex`

### Frontmatter
- `title.tex` → `02_FRONTMATTER.tex`
- `preface.tex` → `02_FRONTMATTER.tex`
- `reader_contract.tex` → `02_FRONTMATTER.tex`

### Chapter 1
- `chapter_01.tex` → `03_CH01_WeakInterface.tex`
- `chapter_01_section_1.tex` → `03_CH01_WeakInterface.tex` (lines X-Y)
- `chapter_01_section_2.tex` → `03_CH01_WeakInterface.tex` (lines A-B)

### Chapter 2  
- `chapter_02_frozen.tex` → `04_CH02_FrozenRegime.tex`
- `frozen_regime_derivations.tex` → `04_CH02_FrozenRegime.tex` (Section 2.8-2.9)

[... continue for all chapters ...]

### Backmatter
- `appendix_a.tex` → `24_BACKMATTER.tex`
- `appendix_b.tex` → `24_BACKMATTER.tex`
- `references.bib` → `26_BIBLIOGRAPHY.bib`

## File Statistics
- Original files: [count]
- Consolidated files: [count]
- Total content preserved: 100%
- Equations preserved: [count]
- Figures referenced: [count]
```

### STEP 7: Create Metadata File

Create `00_METADATA.md`:

```markdown
# EDC Part II - Consolidated Package Metadata

## Book Information
- **Title**: Elastic Diffusive Cosmology - Part II: The Weak Sector
- **Author**: Igor Grčman
- **Version**: [extract from source]
- **Date**: [extract from source]
- **DOI**: [extract from source]
- **License**: CC BY-NC-SA 4.0

## Consolidation Information
- **Consolidated**: 2026-01-30
- **Source**: Original LaTeX files from EDC Part II
- **Tool**: Claude Code
- **Purpose**: Package for upload to Claude.ai for reorganization analysis

## Structure Overview

### Current Book Structure (21+ Chapters)
1. The Weak Interface
2. Frozen Regime Foundations
3. The Z6 Program
4. Electroweak Parameters from Geometry
5. [Lepton Masses - stub]
6. Why Exactly Three Generations?
7. Neutrinos as Edge Modes
8. CKM Matrix and CP Violation
9. The Fermi Constant from Geometry
10. V–A Structure from 5D Chiral Localization
11. [Electroweak Bridge - stub]
12. Epistemic Landscape and Open Problems
13. GF Chain Closure Attempts
14. OPR-21: The BVP as Master Key
15. OPR-01 Closure
16. OPR-04: Wall Thickness
17. OPR-19: 5D Gauge Coupling
18. OPR-20: Mediator Mass
19. OPR-22: Effective Fermi Coupling
20. Epistemic Summary & Closure Status
21. Teaser: Topological Model for Nuclear Structure

### Consolidation Files (27 files)
- 01: Preamble (packages, commands, environments)
- 02: Frontmatter (title, preface, TOC)
- 03-23: Individual chapters (21 chapters)
- 24: Backmatter (appendices)
- 25: Figures list
- 26: Bibliography

## Epistemic Tags Used

- **[BL]** - Baseline literature value (CODATA, PDG)
- **[D]** - Derived from postulates/geometry
- **[Dc]** - Derived with calibration
- **[I]** - Identified/constrained by observations
- **[P]** - Postulated
- **[M]** - Measured/target value

## Key Derived Results [D]

### From Chapter 2 (Frozen Regime)
- mp/me = 6π^5 (0.0018% error)
- α = (4π + 5/6)/(6π^5) (0.0067% error)

### From Chapter 4 (Electroweak)
- Weinberg angle from Z6 partition
- Neutron lifetime from WKB

### From Chapters 13-19 (OPR Series)
- Membrane tension σ (OPR-01)
- Wall thickness Δ (OPR-04)
- 5D gauge coupling g5 (OPR-19)
- Mediator mass MW (OPR-20)
- Effective coupling Geff (OPR-22)

## Content Statistics
- Total pages: ~602
- Total chapters: 21+
- Total sections: [count from TOC]
- Total equations: [estimate]
- Total figures: [count]
- Total citations: [count from bib]

## File Size Information
- 01_PREAMBLE.tex: ~X KB
- 02_FRONTMATTER.tex: ~X KB
- 03-23 Chapter files: ~X KB each
- Total package size: ~X MB

## Usage Instructions

### For Claude.ai Upload
1. Upload files in numerical order (01, 02, 03, ...)
2. Start with 00_METADATA.md for context
3. Upload 01_PREAMBLE.tex for definitions
4. Upload chapters as needed for analysis

### For Reorganization Analysis
1. Review 00_METADATA.md for structure
2. Check SOURCE_MAP.md for original locations
3. Examine individual chapter files for content
4. Use FIGURES_LIST.md to track visual content

### For Human Review
1. Each chapter file is self-contained
2. Source annotations in comments
3. Epistemic tags marked inline
4. Section headers clearly labeled

## Verification Checklist
- [x] All source files accounted for
- [x] All equations preserved exactly
- [x] All epistemic tags unchanged
- [x] All figures listed
- [x] Bibliography complete
- [x] Source mapping documented

## Notes
- No content was modified during consolidation
- All mathematical expressions copied verbatim
- All LaTeX commands preserved
- Original structure documented in SOURCE_MAP.md
- Ready for reorganization analysis
```

### STEP 8: Create Consolidation Log

Create `CONSOLIDATION_LOG.md`:

```markdown
# Consolidation Process Log

## Process Started: [timestamp]

## Step 1: Source Analysis
- Scanned directory: [path]
- Found [N] .tex files
- Identified main file: main.tex
- Mapped dependencies: [list]

## Step 2: Preamble Extraction
- Source files: preamble.tex, packages.tex, custom_commands.tex
- Output: 01_PREAMBLE.tex
- Packages found: [count]
- Custom commands: [count]
- Custom environments: [count]

## Step 3: Frontmatter Consolidation
- Sources: title.tex, preface.tex, reader_contract.tex
- Output: 02_FRONTMATTER.tex
- Sections: Title, Preface, Reader Contract

## Step 4: Chapter Consolidation

### Chapter 1
- Source: chapter_01.tex, [other files]
- Output: 03_CH01_WeakInterface.tex
- Sections: 1.1 - 1.11 (11 sections)
- Lines: [count]
- Equations: [count]
- Figures: [count]

### Chapter 2
- Source: chapter_02_frozen.tex
- Output: 04_CH02_FrozenRegime.tex
- Sections: 2.1 - 2.11 (11 sections)
- Lines: [count]
- Equations: [count]
- ⚠️ Contains [D] derivations in 2.8, 2.9

[... continue for all chapters ...]

## Step 5: Backmatter Consolidation
- Sources: appendix_a.tex, appendix_b.tex, appendix_c.tex
- Output: 24_BACKMATTER.tex
- Appendices: [count]

## Step 6: Figures Inventory
- Total figures found: [count]
- Figures listed in: 25_FIGURES_LIST.md
- Missing files: [list if any]

## Step 7: Bibliography
- Source: references.bib
- Output: 26_BIBLIOGRAPHY.bib
- Total entries: [count]

## Step 8: Documentation
- Created: 00_METADATA.md
- Created: SOURCE_MAP.md
- Created: CONSOLIDATION_LOG.md (this file)

## Verification Performed
- [x] All source files processed
- [x] All content copied verbatim
- [x] No equations modified
- [x] No tags changed
- [x] All figures documented
- [x] Source mapping complete

## Statistics
- Original files: [count]
- Consolidated files: 27
- Total size: [X] MB
- Processing time: [duration]

## Process Completed: [timestamp]
```

---

## VERIFICATION PROCEDURE

After consolidation, perform these checks:

### 1. Content Completeness
```bash
# Count equations in source
grep -r "\\begin{equation}" source_directory/ | wc -l

# Count equations in consolidated
grep "\\begin{equation}" EDC_Part2_Consolidated/*.tex | wc -l

# Should match!
```

### 2. Epistemic Tags Preserved
```bash
# Check all tags present
grep -E "\[BL\]|\[D\]|\[Dc\]|\[I\]|\[P\]|\[M\]" EDC_Part2_Consolidated/*.tex > tags.txt

# Verify counts match source
```

### 3. Figures Accounted For
```bash
# List all figure references
grep "\\includegraphics" EDC_Part2_Consolidated/*.tex

# Cross-check with FIGURES_LIST.md
```

### 4. Bibliography Complete
```bash
# Check all citations
grep "\\cite{" EDC_Part2_Consolidated/*.tex | sort | uniq

# Verify all in 26_BIBLIOGRAPHY.bib
```

---

## FILE SIZE MANAGEMENT

If individual chapter files are too large (>10 MB):

### Option A: Split Large Chapters
```
06_CH04_ElectroweakParams_Part1.tex  (Sections 4.1-4.5)
06_CH04_ElectroweakParams_Part2.tex  (Sections 4.6-4.9)
```

### Option B: Extract Heavy Derivations
```
13_CH13_OPR_Main.tex              (Overview and short sections)
13_CH13_OPR_Derivation_01.tex     (OPR-19 full derivation)
13_CH13_OPR_Derivation_02.tex     (OPR-20 full derivation)
```

Document splits in SOURCE_MAP.md

---

## UPLOAD SEQUENCE FOR CLAUDE.AI

Recommend uploading in this order:

1. **First**: `00_METADATA.md` (context)
2. **Second**: `01_PREAMBLE.tex` (definitions)
3. **Third**: `02_FRONTMATTER.tex` (structure)
4. **Then**: Chapters 1-5 (foundations)
5. **Then**: Chapters 6-11 (quantitative)
6. **Then**: Chapters 12-21 (technical)
7. **Last**: `24_BACKMATTER.tex`, `SOURCE_MAP.md`

Or upload selectively based on what needs analysis.

---

## SUCCESS CRITERIA

✅ All source content consolidated
✅ Each chapter in separate file
✅ All math preserved exactly
✅ All tags unchanged
✅ Complete documentation
✅ Source mapping clear
✅ Figures inventoried
✅ Bibliography complete
✅ Files ready for upload
✅ Human-readable organization

---

## FINAL PACKAGE STRUCTURE

```
EDC_Part2_Consolidated/
├── 00_METADATA.md                 ← START HERE
├── 01_PREAMBLE.tex                ← Definitions
├── 02_FRONTMATTER.tex             ← Context
├── 03-23_CH*.tex                  ← Main content (21 files)
├── 24_BACKMATTER.tex              ← Appendices
├── 25_FIGURES_LIST.md             ← Visual inventory
├── 26_BIBLIOGRAPHY.bib            ← References
├── SOURCE_MAP.md                  ← Traceability
└── CONSOLIDATION_LOG.md           ← Process record
```

**Total: 27 files, organized, documented, ready for analysis**

---

**READY TO CONSOLIDATE?**

This process preserves every equation, every tag, every derivation - just organizes them into uploadable, analyzable chunks.
