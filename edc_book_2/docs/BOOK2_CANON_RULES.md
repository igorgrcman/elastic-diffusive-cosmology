# Book 2 Canon Rules

**Version:** 1.0
**Generated:** 2026-01-29
**Purpose:** Conventions enforced during consolidation pass

---

## 1. Unit Conventions

### 1.1 Natural Units Declaration

When using natural units (ℏ = c = 1), this must be explicitly stated near first usage.

**Preferred patterns:**
- "In this chapter, we use natural units where ℏ = c = 1."
- "Throughout, we work in units where ℏ = c = 1."

**Conversion reminders:**
- 1 fm ≈ 5.068 GeV⁻¹
- ℏc ≈ 197.3 MeV·fm

### 1.2 δ Scale Convention

EDC uses multiple thickness scales. The subscript convention prevents confusion:

| Context | Symbol | Definition | Value |
|---------|--------|------------|-------|
| Nuclear/nucleon chapters | δ, δ_nucl | ℏ/(2m_p c) | 0.105 fm |
| Electroweak BVP chapters | δ_EW | ℏc/M_Z | ~0.002 fm |
| CP phase (angles) | δ | Angle in degrees/radians | ~65° (CKM) |

**Rules:**
- Never use bare δ when both thickness scales appear
- CP phase δ is always an angle (context makes this clear)
- Conversion: δ_nucl/δ_EW ≈ 50

**Canon source:** `src/_shared/scale_disambiguation_box.tex`

### 1.3 Mixed Unit Expressions

When mixing fm and GeV⁻¹ in the same derivation:
- Provide explicit conversion factor
- OR work entirely in one system
- NEVER assume reader will convert mentally

---

## 2. Notation Standards

### 2.1 Symbol Conventions

| Correct | Incorrect | Notes |
|---------|-----------|-------|
| $m_p$ | mp, M_p | Proton mass (lowercase subscript) |
| $M_W$ | m_W, Mw | W boson mass (uppercase both) |
| $G_F$ | GF, g_F | Fermi constant (uppercase G) |
| $g_5$ | g5, g_{5} | 5D coupling (numeric subscript) |
| $I_4$ | I4, I_{4} | Overlap integral |
| $\psi_L$, $\psi_R$ | psi_L | Greek with backslash |

### 2.2 Identifiers vs. Math

**Important distinction:**
- TikZ node names: `\node (g5)` - OK to use short form
- Labels: `\label{eq:I4}` - OK to use short form
- PDF bookmarks: `\texorpdfstring{$g_5$}{g5}` - fallback is OK
- Mathematical content: Always use subscript ($g_5$, $I_4$, $m_p$)

### 2.3 Macro Definitions

Macros should be defined ONCE in a central location (main.tex or preamble file):

```latex
\newcommand{\EDCPAPERS}{../../edc_papers}  % Path macro
\newcommand{\tagDer}{\texttt{[Der]}}       % Epistemic tag
```

---

## 3. Epistemic Tags

### 3.1 Tag Definitions

| Tag | Meaning | When to Use |
|-----|---------|-------------|
| [Der] | Derived | Explicit derivation from postulates exists |
| [Dc] | Derived Conditional | Derived IF certain assumptions hold |
| [I] | Identified | Pattern matching (not unique) |
| [P] | Proposed | Postulate/hypothesis |
| [Cal] | Calibrated | Parameter fitted to data |
| [BL] | Baseline | External reference (PDG/CODATA) |
| [M] | Mathematics | Mathematical theorem (not EDC-specific) |

### 3.2 Usage Rules

- Every claim in a Stoplight Verdict must have an epistemic tag
- Tags appear AFTER the claim, not before
- Use LaTeX macros: `\tagDer{}`, `\tagDc{}`, etc.
- Multiple tags allowed: `\tagDc{}+\tagP{}`

### 3.3 Tag Hygiene

**ALLOWED:**
- Prose without tags if not making claims
- Definitions that aren't claims don't need tags
- References to external work use [BL]

**REQUIRED:**
- Quantitative predictions must have tags
- Derivation conclusions must have tags
- Status summaries must have tags

---

## 4. Label Conventions

### 4.1 Prefix Patterns

| File Type | Prefix Pattern | Example |
|-----------|----------------|---------|
| Main chapters | sec:, eq:, fig:, tab: | `\label{sec:gf_derivation}` |
| Include files (.include.tex) | DL:\<filename\>: | `\label{DL:delta_from_5d:eq:main}` |
| Shared boxes | box: | `\label{box:scale-disambiguation}` |
| OPR sections | opr:\<number\>: | `\label{opr:21:closure}` |

### 4.2 Anti-Collision Scheme

Include files from edc_papers/_shared/ use the DL: (Derivation Library) prefix
to prevent label collisions when multiple includes define similar equations.

**Pattern:** `DL:<short-filename>:<standard-prefix>:<name>`

Example: `\label{DL:dlr-from-chiral-loca:eq:chiral_decomp}`

---

## 5. Canon Files (Single Source of Truth)

### 5.1 Shared Definitions

| Concept | File | Label |
|---------|------|-------|
| Scale disambiguation | `_shared/scale_disambiguation_box.tex` | `box:scale-disambiguation` |
| Overlap integral I₄ | `_shared/overlap_integral_canon.tex` | `box:overlap-integral-canon` |
| Stoplight template | `_shared/stoplight_stub.tex` | (template) |
| Gate registry | `sections/12_epistemic_map.tex` | `sec:gate_registry` |

### 5.2 Usage Rule

**Do NOT duplicate** canonical definitions. Instead:
- Use `\input{_shared/...}` to include the box
- Or use `\ref{box:...}` to cross-reference

### 5.3 When Duplication is OK

Pedagogical introductions may briefly re-explain a concept before referencing
the canonical definition. Keep such introductions SHORT (1-2 sentences).

---

## 6. Status Boxes and Stoplights

### 6.1 Stoplight Colors

| Color | Meaning | LaTeX |
|-------|---------|-------|
| GREEN | Derived/verified | `\textcolor{OliveGreen}{\textbf{GREEN}}` |
| YELLOW | Conditional/partial | `\textcolor{YellowOrange}{\textbf{YELLOW}}` |
| RED | Open/unresolved | `\textcolor{BrickRed}{\textbf{RED}}` |
| RED-C | Candidate identified | `\textcolor{BrickRed}{\textbf{RED-C}}` |

### 6.2 Equivalent Status Structures

The following are functionally equivalent to a Stoplight Verdict:
- "Dependency & Status (IF/THEN)" boxes
- "Bottom Line" boxes with explicit status
- "Takeaway" boxes with upgrade conditions

All must include:
1. Current status with color
2. What would upgrade the status
3. Epistemic tags on claims

---

## 7. k-Channel Applicability

### 7.1 Where k-channel Applies

The k-channel correction k(N) = 1 + 1/N applies ONLY to:
- Averaging observables over discrete vs continuous distributions
- Spin-chain cross-validated contexts (N = 3–12 verified)

### 7.2 Where k-channel Does NOT Apply

- Overlap integrals
- Cardinality ratios
- Arbitrary multiplication
- Volume ratios
- Any calculation not involving discrete averaging

**Canon source:** See `box:zn-kchannel-robustness` in epistemic map.

---

## 8. Include Path Conventions

### 8.1 Path Macros

```latex
\newcommand{\EDCPAPERS}{../../edc_papers}
```

Use: `\input{\EDCPAPERS/_shared/boxes/example.tex}`

### 8.2 Relative Paths

From `edc_book_2/src/sections/`:
- To shared: `../_shared/`
- To edc_papers: `../../../edc_papers/`
- Or use `\EDCPAPERS` macro

---

## 9. Build Requirements

### 9.1 Compilation

```bash
cd edc_book_2/src
latexmk -xelatex main.tex
```

### 9.2 Success Criteria

- 0 undefined references
- 0 multiply-defined labels
- PDF generates without errors

### 9.3 Known Acceptable Warnings

- Font warnings (fallback fonts)
- Overfull hbox warnings (minor)

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-01-29 | Initial version | Claude Code |

---

*These rules ensure consistency across Book 2 chapters and derivations.*
