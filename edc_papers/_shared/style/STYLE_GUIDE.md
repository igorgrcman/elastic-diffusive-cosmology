# EDC Paper Style Guide

**Version:** 1.0
**Date:** 2026-01-20
**Applies to:** Paper 3 series and future EDC publications

---

## Quick Start

Add these lines to your document preamble (after loading packages):

```latex
% Load required packages first
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes,decorations.markings,decorations.pathmorphing,positioning}
\usepackage{tcolorbox}
\usepackage{xcolor}

% Then load shared EDC styles
\input{../../../_shared/style/edc_style}       % Epistemic tags, tcolorbox, symbols
\input{../../../_shared/style/tikz_style_edc}  % TikZ figure styles
```

Adjust the relative path (`../../../`) based on your document location.

---

## Example: Epistemic Tags

```latex
The neutron is modeled as an excited junction \tagP{}.
Given the Steiner minimum property \tagDer{}, the excitation
carries geometric energy \tagDc{}.
The neutron lifetime $\tau_n = 878.4$ s is \tagBL{} (PDG).
The thick-brane coupling constant $g$ remains \tagOpen{}.
```

**Output:**
- `[P]` in purple — Postulated
- `[Der]` in green — Derived
- `[Dc]` in blue — Deduced/Constrained
- `[BL]` in gray — Baseline (external fact)
- `[OPEN]` in dark orange — Open problem

---

## Example: tcolorbox Styles

### Cornerstone Box

```latex
\begin{tcolorbox}[edcCornerstone, title=\textbf{Cornerstone: Neutron in EDC}]
In the EDC program, the neutron is modeled as an excited 5D junction state:
the same three-arm junction core as the proton, but displaced from the
local Steiner minimum.
\end{tcolorbox}
```

### Guardrail Box

```latex
\begin{tcolorbox}[edcGuardrail, title=\textbf{Epistemic Guardrail}]
\textbf{$\tau_n$ is not a control knob:} We treat $\tau_n$ as a
\textbf{benchmark} \tagBL{}, not as a tuning target.
\end{tcolorbox}
```

### Physical Process Narrative Box

```latex
\begin{tcolorbox}[edcPPN, title=\textbf{Physical Process Narrative}]
\begin{enumerate}[nosep]
    \item[\textbf{(i)}] \textbf{Bulk cause:} Junction relaxation
    \item[\textbf{(ii)}] \textbf{Injection:} Energy pumped to brane
    \item[\textbf{(iii)}] \textbf{Absorption:} Brane stores energy
    \item[\textbf{(iv)}] \textbf{Dissipation:} Mode redistribution
    \item[\textbf{(v)}] \textbf{Projection:} Frozen $\to$ 3D outputs
    \item[\textbf{(vi)}] \textbf{Ledger:} Conservation closes in 5D
\end{enumerate}
\end{tcolorbox}
```

---

## Example: TikZ Figure with Styles

### Simple Energy Flow Diagram

```latex
\begin{figure}[htbp]
\centering
\begin{tikzpicture}[edc compact, node distance=1.2cm and 1.5cm]

% Nodes using predefined styles
\node[bulk box] (bulk) {Bulk junction\\$q > 0$};
\node[brane box, right=of bulk] (brane) {Brane store\\$\mathcal{E}(t)$};
\node[output box, right=of brane] (out) {3D outputs\\$e^-, \bar{\nu}_e$};

% Arrows using predefined styles
\draw[edc arrow, red!70!black] (bulk) -- node[above, font=\scriptsize] {pump} (brane);
\draw[edc arrow, blue!60!black] (brane) -- node[above, font=\scriptsize] {project} (out);

% Phase labels
\node[phase label, below=0.2cm of bulk] {5D Cause};
\node[phase label, below=0.2cm of brane] {Absorption};
\node[phase label, below=0.2cm of out] {Observation};

\end{tikzpicture}
\caption{Energy flow from bulk to 3D via brane mediation.}
\label{fig:example_flow}
\end{figure}
```

### Region Backgrounds

```latex
\begin{tikzpicture}[scale=0.8]
    % Background regions
    \fill[bulk region] (-3,-1.5) rectangle (-0.5,1.5);
    \fill[brane region] (-0.5,-1.5) rectangle (0.5,1.5);
    \fill[observer region] (0.5,-1.5) rectangle (3,1.5);

    % Labels
    \node[section label] at (-1.75,1.8) {\textbf{5D Bulk}};
    \node[section label] at (0,1.8) {\textbf{Brane}};
    \node[section label] at (1.75,1.8) {\textbf{3D}};

    % Boundaries
    \draw[bulk boundary] (-0.5,-1.5) -- (-0.5,1.5);
    \draw[observer boundary] (0.5,-1.5) -- (0.5,1.5);
\end{tikzpicture}
```

### Junction with Flux Arms

```latex
\begin{tikzpicture}[scale=1.2]
    % Draw junction point
    \node[junction point] (j) at (0,0) {};

    % Draw flux arms at 120° angles
    \draw[flux arm] (j) -- (90:1);
    \draw[flux arm] (j) -- (210:1);
    \draw[flux arm] (j) -- (330:1);

    % Particle outputs
    \node[particle] at (2,0) {};
    \node[neutrino] at (2.5,0) {};
\end{tikzpicture>
```

---

## Common Symbols (from edc_style.tex)

| Command | Output | Meaning |
|---------|--------|---------|
| `\Ztwo` | $\mathbb{Z}_2$ | Z₂ symmetry |
| `\Zthree` | $\mathbb{Z}_3$ | Z₃ symmetry |
| `\Zsix` | $\mathbb{Z}_6$ | Z₆ symmetry |
| `\Sthree` | $S^3$ | 3-sphere |
| `\Bthree` | $B^3$ | 3-ball |
| `\Mfive` | $\mathcal{M}_5$ | 5D manifold |
| `\Bfour` | $\mathcal{B}_4$ | 4D brane |
| `\Pfrozen` | $\mathcal{P}_\mathrm{frozen}$ | Frozen projection |
| `\Ebrane` | $\mathcal{E}_\mathrm{brane}$ | Brane energy |
| `\Jbb{\nu}` | $J^\nu_\mathrm{bulk\to brane}$ | Bulk-brane current |
| `\tension` | $\tau$ | Flux-tube tension |

---

## Checklist Before Commit

- [ ] All `\tagXXX` tags used appropriately
- [ ] All tcolorbox uses predefined styles (`edcCornerstone`, etc.)
- [ ] All TikZ figures use shared styles
- [ ] No figure-related overfull hbox warnings
- [ ] References use "Title (DOI: ...)" format, NOT "Paper 2/3"

---

## File Locations

```
edc_papers/
├── _shared/
│   └── style/
│       ├── edc_style.tex        # Main style file
│       ├── tikz_style_edc.tex   # TikZ styles
│       └── STYLE_GUIDE.md       # This file
└── paper_3_series/
    ├── 10_companion_N_neutron_junction/
    │   └── paper/
    │       └── main.tex         # Uses shared styles
    └── ...
```

---

*Style consistency is a form of scientific rigor.*
