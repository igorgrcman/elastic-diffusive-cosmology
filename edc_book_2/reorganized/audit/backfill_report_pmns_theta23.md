# Backfill Report: PMNS theta_23

**Date:** 2026-01-31
**Branch:** backfill/pmns-theta23-v1
**Build:** 145 pages (unchanged — content fits within existing layout)

---

## Summary

| Item | Value |
|------|-------|
| Target file | `part2/chapter_09_neutrinos.tex` |
| Target lines | 253-292 (inserted), 361, 382 (updated) |
| Donor file | `edc_book_2/src/sections/ch6_pmns_attempt2.tex:95-108` |
| Lines added | +40 (backfill block) |
| Equations | 1 |
| Boxes | 2 (success box, epistemic warning) |

---

## What Was Added

### 1. Success Box for sin²θ₂₃

```latex
\begin{tcolorbox}[colback=green!5, colframe=green!50!black,
    title=\textbf{$\sin^2\theta_{23}$: Derived from Discrete Geometry}]

\textbf{Inputs} (from earlier chapters):
\begin{itemize}[nosep]
\item $\mathbb{Z}_6 = \mathbb{Z}_2 \times \mathbb{Z}_3$ lattice symmetry \tagI{}
\item Overlap ansatz: $O_{\alpha i} \propto \exp(-|z_\alpha - z_i|/2\kappa)$ \tagP{}
\item Flavor at $\mathbb{Z}_3$ positions, mass at $\mathbb{Z}_6$ subset
\end{itemize}

\textbf{Output} (no additional free parameters):
\begin{equation}
\sin^2\theta_{23}^{\text{(EDC)}} = 0.564 \quad \tagDc{}
\end{equation}

\textbf{Baseline} \tagBL{}:
$\sin^2\theta_{23}^{\text{(PDG)}} = 0.546 \pm 0.021$ (NuFIT 5.2, 2024)

\textbf{Agreement}: 3\% --- consistent within experimental uncertainty.
\end{tcolorbox}
```

### 2. Epistemic Warning Box

Clarifies per-angle status:
- θ₂₃: **GREEN** [Dc] — derived
- θ₁₂: **YELLOW** [I] — partial
- θ₁₃: **YELLOW** [I/Cal] — partial, may need calibration
- Full U_PMNS: **OPEN**

### 3. Updated Stoplight Table

| Claim | Status | Tag | Note |
|-------|--------|-----|------|
| U_PMNS exists | GREEN | [BL] | Observed |
| Z₆ overlap model | YELLOW | [Dc] | θ₂₃ works, others fail |
| sin²θ₁₂ ≈ 0.31 | YELLOW | [I] | Partial, not derived |
| **sin²θ₂₃ ≈ 0.55** | **GREEN** | [Dc] | Within 3% (A3 variant) |
| sin²θ₁₃ ≈ 0.02 | YELLOW | [I/Cal] | Partial, may need calibration |
| CP phase δ_CP | RED | [Open] | Not addressed |

---

## Tag Rationale

| Tag | Applied To | Justification |
|-----|------------|---------------|
| [Dc] | sin²θ₂₃ = 0.564 | Dictionary mapping from geometry to PMNS observable |
| [P] | Overlap ansatz | Postulated mechanism (not derived from first principles) |
| [I] | Z₆ lattice | Identified from lattice structure |
| [BL] | PDG value 0.546 | Experimental baseline reference |

---

## Observable Semantics

**Critical clarification:** The value 0.564 is explicitly labeled as sin²θ₂₃, not θ₂₃.
This follows standard neutrino physics notation:
- sin²θ₂₃ ∈ [0, 1] (what we compute/measure)
- θ₂₃ ≈ 45° (the angle itself)

---

## What Remains Open

1. **θ₁₂ derivation** — value not derived from geometry
2. **θ₁₃ derivation** — may require calibration parameter
3. **Full U_PMNS** — complete matrix not closed
4. **CP phase** — not addressed

---

*Generated: 2026-01-31 | Branch: backfill/pmns-theta23-v1*
