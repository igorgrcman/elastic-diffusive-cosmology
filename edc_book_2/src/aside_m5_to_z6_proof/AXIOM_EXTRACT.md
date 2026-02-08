# AXIOM EXTRACT: EDC Premises for Z6 Derivation Attempt

**Created:** 2026-01-26
**Purpose:** Numbered list of premises available for deriving Z6 from M5 + EDC structure

---

## CORE POSTULATES [P] (From 02_frozen_regime_foundations.tex)

### A1: 5D Bulk Manifold
**Source:** `02_frozen_regime_foundations.tex:86-90`
```latex
\begin{postulate}[5D Bulk]
Physical reality consists of a 5-dimensional manifold $\mathcal{M}^5$ with metric signature
$(-,+,+,+,+)$, filled with an energetic fluid called the \textbf{Plenum}.
\end{postulate}
```
**Status:** [P] — Foundational axiom, not derived

### A2: 3D Membrane
**Source:** `02_frozen_regime_foundations.tex:92-96`
```latex
\begin{postulate}[3D Membrane]
Our observable universe is a 3+1 dimensional hypersurface $\Sigma^3$ embedded in $\mathcal{M}^5$.
All Standard Model fields are confined to this membrane.
\end{postulate}
```
**Status:** [P] — Foundational axiom, not derived

### A3: Compact Fifth Dimension
**Source:** `02_frozen_regime_foundations.tex:98-102`
```latex
\begin{postulate}[Compact Fifth Dimension]
The extra dimension has topology $\xi \cong S^1$ with characteristic scale $R_\xi \ll 1$ mm,
below current experimental detection.
\end{postulate}
```
**Status:** [P] — Foundational axiom, not derived

### A4: Membrane Tension
**Source:** `02_frozen_regime_foundations.tex:104-108`
```latex
\begin{postulate}[Membrane Tension]
The membrane has surface tension $\sigma$ [J/m$^2$] that resists deformation.
The bulk fluid has viscosity $\eta$ [Pa$\cdot$s] and pressure $P_{\text{bulk}}$.
\end{postulate}
```
**Status:** [P] — Foundational axiom, not derived

---

## DERIVED STRUCTURE [Dc] (From Core Postulates)

### A5: Particles as Topological Defects
**Source:** `02_frozen_regime_foundations.tex:112-116`
```latex
\begin{definition}[Particle]
A particle is a stable, localized region where Plenum energy from the bulk $\mathcal{M}^5$
is confined to the membrane $\Sigma^3$, protected by topological constraints from dissipating.
\end{definition}
```
**Status:** [Def] — Definition, follows from framework

### A6: Charge as Winding Number
**Source:** `02_frozen_regime_foundations.tex:121`
```latex
\item \textbf{Charge} $\propto$ topological winding number
```
**Status:** [P] — Postulated mapping, not derived

---

## MATHEMATICAL THEOREMS [M] (No EDC assumptions)

### T1: Steiner Minimum Theorem (1834)
**Source:** `Z6_content_full.tex:94-121`
```
For three points with equal line tensions, the Fermat point with 120° angles minimizes total length.
```
**Status:** [M] — Pure mathematics, proven

### T2: Kepler-Hales Packing Theorem (2005)
**Source:** `Z6_content_full.tex:225-237`
```latex
\begin{theorem}[Kepler Conjecture, Hales 2005]
The densest packing of equal spheres in 3D is FCC/HCP with packing fraction ~74.05%.
\end{theorem}

\begin{corollary}[2D Optimal Packing]
The densest packing of equal circles in 2D is hexagonal, with packing fraction ~90.69%.
\end{corollary}
```
**Status:** [M] — Pure mathematics, proven

---

## POSTULATES USED IN CURRENT Z6 DERIVATION [P]

### P1: Z6-Invariant Boundary Conditions
**Source:** `Z6_content_full.tex:155-166`
```latex
\begin{postulate}[$\mathbb{Z}_6$-Invariant Boundary Conditions]
The boundary conditions on the thick-brane preserve $\mathbb{Z}_6$ rotational
symmetry in the transverse plane.
\end{postulate}
```
**Status:** [P] — **THIS IS WHAT WE WANT TO DERIVE**

### P2: Flux Tube Interactions
**Source:** `Z6_content_full.tex:239-253`
```latex
\begin{postulate}[Flux Tube Interactions]
Flux tubes (defect lines) in the thick-brane have:
  1. Short-range repulsion (excluded volume)
  2. Long-range attraction or confinement
The combined potential has the form V(r) = V_rep(r) + V_att(r) with minimum at r_0.
\end{postulate}
```
**Status:** [P] — **CRITICAL: The derivation chain depends on this**

---

## ADDITIONAL POSTULATES FOUND IN SOURCES

### P3: Isotropy Assumption
**Source:** `ch11_g5_value_closure_attempt3_derive_4pi.tex:43-45`
```latex
We assume the brane interaction is isotropic \tagP{}
The isotropy assumption is the only new postulate; under it, $4\pi$ is derived.
```
**Status:** [P] — Independent postulate, not derived from A1-A4

### P4: Transverse 2D Plane
**Source:** `Z6_content_full.tex:158-159, 424`
```
The boundary conditions on the thick-brane preserve Z6 rotational symmetry in the transverse plane.
The hexagonal lattice lives in the 2D transverse plane of the thick-brane.
```
**Status:** [Dc] from A1-A3 — The existence of a 2D transverse plane follows from 5D → 3D embedding

---

## BULK/BRANE ACTION SKELETON (NOT COMPLETE)

### Bulk Action
**Source:** `ch14_bvp_closure_pack.tex:274-280`
```latex
S_{\text{bulk}} = \int d^5x \sqrt{-g_5} \left[
    \frac{M_{5,\mathrm{Pl}}^3}{2} R_5 + \mathcal{L}_{\text{bulk matter}}
\right]
```
**Status:** [P] — Skeleton only, matter Lagrangian not specified

### Brane Action
**Source:** `ch14_bvp_closure_pack.tex:284-291`
```latex
S_{\text{brane}} = -\int d^4x \sqrt{-g_4} \left[
    \sigma + \mathcal{L}_{\text{brane matter}}
\right]
```
**Status:** [P] — Skeleton only, matter Lagrangian not specified

### Israel Junction Condition
**Source:** `ch14_bvp_closure_pack.tex:293-298`
```latex
[K_{ab}] - g_{ab}[K] = -\frac{1}{M_{5,\mathrm{Pl}}^3} S_{ab}
```
**Status:** [M] — Standard GR result, but application to EDC requires completing S_ab

---

## SUMMARY: What We Have vs What We Need

| Axiom | Status | Available? |
|-------|--------|------------|
| A1-A4 (Core 5D structure) | [P] | YES |
| T1-T2 (Math theorems) | [M] | YES |
| P1 (Z6-BC) | [P] | TARGET (want to derive) |
| P2 (Flux tube interactions) | [P] | YES (but want to eliminate) |
| P3 (Isotropy) | [P] | YES (implicit in current chain) |
| Complete 5D action | [MISSING] | NO |
| π₁(M⁵) or π₂(M/G) | [MISSING] | NO |
| Explicit V(r) derivation | [MISSING] | NO |

---

## CRITICAL OBSERVATION

The current derivation chain is:
```
P2 (Flux Tubes) + T2 (Packing) → L1 (Hex Ground State) → L2 (Z6 Emergence)
```

To eliminate P2 and derive Z6 from M5 structure alone, we would need:
1. Derive V(r) from S_bulk + S_brane + junction conditions
2. Show V(r) has repulsion + attraction + minimum at r_0
3. Then T2 gives hexagonal packing → Z6

**Current status:** Neither (1) nor (2) has been done. The 5D action is a skeleton only.
