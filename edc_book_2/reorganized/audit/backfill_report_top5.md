# Backfill Report: Top 5 Critical Gaps

**Date:** 2026-01-31
**Branch:** backfill/top5-v1
**Method:** tex→tex minimal backfill
**Build:** 149 pages (was 145)

---

## Summary

| Gap | Target (145) | Source (461) | Type | Dictionary Box | SM-risk Addressed |
|-----|--------------|--------------|------|----------------|-------------------|
| 1   | Electron/B3  | Z6_content_full.tex:545-580 | C | ✅ | N/A |
| 2   | sin²θ_W      | CH3_electroweak.tex:198-240 | C | ✅ | ✅ |
| 4   | V−A          | CH3_electroweak.tex:751-830 | C | N/A | ✅ |
| 5   | CKM          | CH3_electroweak.tex:607-632 | C | ✅ | ✅ |
| 6   | M_W/G_F      | CH3_electroweak.tex:26,78-81 | C | ✅ | N/A |

**Skipped:** Gap 3 (PMNS) — no donor content in 461-str sources.

---

## Gap 1: Electron as B³ Vortex

**Target:** `part1/chapter_02_ontology.tex` (lines 71-83)
**Key claim:** Isoperimetric theorem ⇒ electron stability

### Minimal backfill added (15 lines + 1 eq + 1 box):

```latex
% BACKFILL-TOP5: Gap1-ElectronB3 BEGIN
\textbf{Stability---separated claims:}

\textit{Mathematical fact} \tagM{}:
The isoperimetric theorem states that among all surfaces enclosing a fixed volume,
the sphere uniquely minimizes surface area. For the unit 3-ball:
\begin{equation}
\text{Vol}(B^3) = \frac{4\pi}{3}, \quad \text{Area}(\partial B^3) = 4\pi
\end{equation}

\textit{Physical interpretation} \tagI{}/\tagP{}:
Identifying the electron with this minimal-energy configuration requires
\textbf{additional assumptions}:
\begin{enumerate}[nosep]
\item Topological sector label (winding $W$) is conserved under smooth deformations
\item Energy functional $E[\psi] \propto \text{Area}$ (surface tension dominates)
\item No singular transitions or boundary-crossing allowed at accessible energies
\end{enumerate}
Under these assumptions, the $B^3$ vortex sits at a \textbf{local minimum}
protected by topological superselection---not by the isoperimetric theorem alone.

\begin{tcolorbox}[...Dictionary: Geometry → Electron Stability...]
\tagDc{}
\textbf{Model object:} $B^3$ vortex with winding $W = -1$, volume $\frac{4\pi}{3}r^3$.
\textbf{Observable:} Electron stability (no decay to lighter charged state).
\textbf{Identification:} Ground mode of charged brane sector ⟺ electron.
\textbf{Status:} Conditional on topological superselection holding at all accessible energies.
\end{tcolorbox}
% BACKFILL-TOP5: Gap1-ElectronB3 END
```

### Tag changes:
- `\tagM{}/\tagI{}` → separated into `\tagM{}` (pure theorem) and `\tagI{}/\tagP{}` (physical interpretation)
- Added explicit `\tagDc{}` for dictionary identification

### Note:
Dictionary box added. No SM-language risk in this gap.

---

## Gap 2: sin²θ_W Identification

**Target:** `part2/chapter_06_electroweak.tex` (lines 112-115)
**Key claim:** Geometric ratio 1/4 = sin²θ_W

### Minimal backfill added (18 lines + 1 eq + 1 box):

```latex
% BACKFILL-TOP5: Gap2-sin2thetaW BEGIN
\begin{tcolorbox}[...Dictionary: EDC Coupling Ratio → Weinberg Angle...]
\tagDc{}

\textbf{EDC derivation} \tagDerSym{}:
\begin{equation}
\frac{g'^2}{g^2} = \frac{|\mathbb{Z}_2|}{|\mathbb{Z}_6|} = \frac{1}{3}
\quad\Rightarrow\quad
\frac{g'^2}{g^2 + g'^2} = \frac{1}{4}
\end{equation}
This is a \textbf{group-theoretic identity} from $\mathbb{Z}_6 = \mathbb{Z}_2 \times \mathbb{Z}_3$.

\textbf{SM baseline} \tagBL{}:
The electroweak mixing angle is \textit{defined} as $\sin^2\theta_W \equiv g'^2/(g^2 + g'^2)$.

\textbf{Dictionary step} \tagDc{}:
Identifying EDC's geometric ratio with the SM observable $\sin^2\theta_W$ is a
\textbf{conditional mapping}---valid if the $\mathbb{Z}_6$ crystallographic couplings
reduce to SM gauge couplings under dimensional reduction.

\textbf{Tree-level caveat:}
The value $1/4 = 0.25$ applies at the \textit{lattice scale} ($\mu \sim 200$ MeV).
RG running to $M_Z$ gives $\sin^2\theta_W(M_Z) \approx 0.231$, matching PDG to $\sim 8\%$.
Full RG calculation remains \tagOpen{}.
\end{tcolorbox}
% BACKFILL-TOP5: Gap2-sin2thetaW END
```

### Tag changes:
- Explicit `\tagDerSym{}` for geometric ratio
- Explicit `\tagBL{}` for SM definition
- `\tagDc{}` for the identification step

### Note:
Dictionary box added. SM-language risk addressed by separating EDC derivation from SM baseline.

---

## Gap 4: V−A Structure

**Target:** `part2/chapter_10_va_structure.tex` (lines 63-70)
**Key claim:** V−A emerges from geometry

### Minimal backfill added (10 lines + 2 eq):

```latex
% BACKFILL-TOP5: Gap4-VA BEGIN
\textbf{Chiral selection mechanism} \tagDc{}:
For an asymmetric mass profile $m(\xi) = m_0(1 - e^{-\xi/\lambda})$, the zero-mode equations are:
\begin{align}
\text{Left-handed:} \quad (\partial_\xi + m(\xi))\psi_L &= 0
  \;\Rightarrow\; \psi_L \propto e^{-\int_0^\xi m(\xi')\,d\xi'} \quad \text{(normalizable)} \\
\text{Right-handed:} \quad (\partial_\xi - m(\xi))\psi_R &= 0
  \;\Rightarrow\; \psi_R \propto e^{+\int_0^\xi m(\xi')\,d\xi'} \quad \text{(non-normalizable)}
\end{align}
\textbf{Physical meaning:} Left-handed modes are \textit{attracted} to the brane ($\xi = 0$);
right-handed modes are \textit{repelled} into the bulk and decouple from brane-localized gauge fields.
% BACKFILL-TOP5: Gap4-VA END
```

### Tag changes:
- Kept existing `\tagDc{}` for the mechanism
- No new tag changes needed

### Note:
No dictionary box added (mechanism box already present). SM-language risk addressed by providing explicit equations showing the geometric origin.

---

## Gap 5: CKM Hierarchy

**Target:** `part2/chapter_11_ckm.tex` (lines 71-78)
**Key claim:** CKM hierarchy from overlap suppression

### Minimal backfill added (15 lines + 2 eq + 1 box):

```latex
% BACKFILL-TOP5: Gap5-CKM BEGIN
\textbf{Step 2: Flavor mixing = overlap integral} \tagDc{}.

The geometric mechanism for CKM suppression:
\begin{equation}
V_{ij} \propto \int_0^\infty f_i^{(u)}(\xi) \, f_j^{(d)}(\xi) \, d\xi
\quad\text{(wavefunction overlap)}
\end{equation}

For exponentially localized profiles $f_i \propto e^{-m_i \xi}$ centered at different $\xi$-positions,
the overlap is exponentially suppressed with generation separation:
\begin{equation}
|V_{ij}| \sim e^{-|m_i - m_j| \cdot \Delta\xi} \quad \Rightarrow \quad
\text{hierarchical mixing}
\end{equation}

\begin{tcolorbox}[...Dictionary: Overlap → CKM Element...]
\tagDc{}
\textbf{Model object:} Generation wavefunctions $f_i(\xi)$ localized at different bulk depths.
\textbf{Observable:} CKM matrix elements $|V_{ij}|$ (PDG).
\textbf{Identification:} Overlap integral ⟺ flavor mixing amplitude.
\textbf{Status:} Cabibbo angle $\lambda \approx 0.22$ is \tagCal{} (calibrated from data).
\end{tcolorbox}
% BACKFILL-TOP5: Gap5-CKM END
```

### Tag changes:
- Added explicit `\tagDc{}` for overlap identification
- Added `\tagCal{}` note for Cabibbo calibration

### Note:
Dictionary box added. SM-language risk addressed by clarifying calibration status.

---

## Gap 6: M_W / G_F Closure

**Target:** `part3/chapter_15_mw_gf.tex` (lines 168-171)
**Key claim:** G_F is consistency check, not prediction

### Minimal backfill added (18 lines + 1 box):

```latex
% BACKFILL-TOP5: Gap6-MWGF BEGIN
\begin{tcolorbox}[...Dictionary: Electroweak Closure...]
\tagDc{}

\textbf{What EDC provides:}
\begin{itemize}[nosep]
\item $\sin^2\theta_W = 1/4$ from $\mathbb{Z}_6$ partition \tagDerSym{}
\item $\delta \sim \hbar c / M_W$ anchored to match W mass \tagCal{}
\end{itemize}

\textbf{SM relations used} \tagBL{}:
\begin{itemize}[nosep]
\item $g^2 = 4\pi\alpha/\sin^2\theta_W$ (definition)
\item $M_W = gv/2$ (Higgs mechanism)
\item $G_F = g^2/(4\sqrt{2}M_W^2)$ (Fermi constant)
\end{itemize}

\textbf{Self-consistency, not prediction:}
Given $\sin^2\theta_W$ and $\delta$ (calibrated), the EW relations are
\textit{automatically satisfied}---this is a closure check, not an independent output.
Deriving $\delta$ from $(\sigma, r_e)$ without EW input is \OPR{20}.
\end{tcolorbox}
% BACKFILL-TOP5: Gap6-MWGF END
```

### Tag changes:
- Added explicit `\tagDerSym{}` for sin²θ_W derivation
- Added explicit `\tagCal{}` for δ calibration
- Added explicit `\tagBL{}` for SM relations

### Note:
Dictionary box added. Clear separation of EDC derivation vs calibration vs SM baseline.

---

## Files Modified

| File | Lines Added | Dictionary Boxes |
|------|-------------|------------------|
| part1/chapter_02_ontology.tex | +27 | 1 |
| part2/chapter_06_electroweak.tex | +24 | 1 |
| part2/chapter_10_va_structure.tex | +11 | 0 |
| part2/chapter_11_ckm.tex | +22 | 1 |
| part3/chapter_15_mw_gf.tex | +22 | 1 |
| **Total** | **+106** | **4** |

---

## Remaining Work

1. **Gap 3 (PMNS):** No donor content — remains `[Open]` for new derivation text
2. **Remaining C gaps (17):** Next pass should cover all Type C
3. **B gaps (56):** Lower priority, some may resolve with C fixes
4. **A gaps (12):** Definition/notation cleanup

---

*Generated: 2026-01-31 | Branch: backfill/top5-v1*
