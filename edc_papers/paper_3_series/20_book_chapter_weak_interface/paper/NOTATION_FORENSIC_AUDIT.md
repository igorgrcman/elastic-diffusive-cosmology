# Notation Forensic Audit: z vs ξ for 5D Depth Coordinate

**Date:** 2026-01-24
**Baseline commit:** 09c29fd (branch: part2-vz-catalogue-va-inequality)
**Purpose:** Resolve notation collision between Part I (Paper 2) and Part II (Book)

---

## A) Part I (Paper 2) Canonical Definitions

**Source:** `edc_papers/paper_2/paper/main.tex`

### 1. Extra dimension coordinate
```latex
\begin{postulate}[Compact Fifth Dimension]
The extra dimension has topology $\xi \cong S^1$ with characteristic scale
$R_\xi \ll 1$ mm, below current experimental detection.
\end{postulate}
```
**Symbol:** ξ
**Role:** Physical 5D coordinate
**Topology:** S¹ (circle)
**Units:** Length

### 2. 5D density
```latex
\rho_5(x,\xi) = |\Psi(x,\xi)|^2
```
**Note:** ξ appears as the 5D coordinate argument.

### 3. Coherence length (GL regime)
```latex
f(r) = \tanh\left(\frac{r}{\sqrt{2}\xi}\right)
```
**Collision warning:** ξ is ALSO used for GL coherence length in Part I!
This is an internal Part I collision, not just Part I vs Part II.

---

## B) Part II (Book) Canonical Definitions

**Source:** `edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/sections/`

### 1. Physical 5D coordinate (z)
From `ch11_opr20_attemptF_mediator_bvp_junction.tex`:
```latex
-\frac{d^2 f}{dz^2} + V(z) f(z) = m^2 f(z)
```
```latex
The domain is $z \in [0, \ell]$ with boundary conditions to be specified.
```

From `09_va_structure.tex`:
```latex
Throughout this chapter we work on the half-line $z \in [0, \infty)$ with
the observer boundary at $z = 0$ and the bulk extending to $z \to \infty$.
```

**Symbol:** z
**Role:** Physical 5D coordinate (transverse to brane)
**Domain:** [0, ℓ] (compact) or [0, ∞) (half-line)
**Units:** Length

### 2. Dimensionless coordinate (ξ in Part II)
From `ch11_opr20_attemptF_mediator_bvp_junction.tex`:
```latex
Define dimensionless coordinate $\xi = z/\ell \in [0,1]$ and rescaled quantities:
```

**Symbol:** ξ
**Role:** Dimensionless coordinate (COLLISION with Part I!)
**Definition:** ξ = z/ℓ
**Domain:** [0, 1]
**Units:** Dimensionless

### 3. KK scale (ℓ)
```latex
where $M,N \in \{0,1,2,3,5\}$, the extra dimension $z \in [0,\ell]$, and $g_5$ is the
5D gauge coupling with dimension $[g_5] = [E]^{-1/2}$ in natural units.
```

**Symbol:** ℓ
**Role:** Domain size / KK scale
**Units:** Length

---

## C) EQUIVALENCE MAP

| Symbol | Part I (Paper 2) | Part II (Book) | Relation | Units | Notes |
|--------|------------------|----------------|----------|-------|-------|
| **ξ** | Physical 5D coordinate (S¹) | Dimensionless: ξ = z/ℓ | **COLLISION** | Part I: Length, Part II: Dimensionless | Root cause of confusion |
| **z** | Not used for 5D | Physical 5D coordinate | Part II z ≈ Part I ξ | Length | Part II standard |
| **ℓ** | Not explicitly used | KK scale (domain size) | - | Length | Part II only |
| **R_ξ** | 5D compactification radius | Same meaning | R_ξ = ℓ/(2π) for S¹ | Length | Consistent |
| **ξ (GL)** | Coherence length (tanh profile) | Not used | - | Length | Internal Part I collision |

---

## D) COLLISION ANALYSIS

### The Core Problem
**Part I:** Uses ξ for the physical 5D coordinate
**Part II:** Uses z for the physical 5D coordinate, BUT reuses ξ for z/ℓ (dimensionless)

This creates confusion when:
1. A reader familiar with Part I sees ξ in Part II and expects the physical 5D coordinate
2. The BVP code uses "z" but Part I's ρ_5(x,ξ) suggests ξ
3. Cross-referencing between parts requires mental translation

### Secondary Collision (Part I internal)
Part I also uses ξ for GL coherence length, making the symbol overloaded even within Paper 2.

---

## E) RECOMMENDATION

### Option A: UNIFY TO ζ (zeta)
- Change Part II's z → ζ everywhere
- Eliminates z/ξ confusion
- Requires updating ~100+ equations in Part II
- **Risk:** ζ may collide with zeta function notation

### Option B: KEEP z + MAPPING (Recommended)
- Keep Part II using z
- Add explicit mapping statement at start of Part II
- Change Part II's dimensionless variable from ξ → ζ̃ (zeta-tilde) or η (eta)
- **Minimal changes, clear separation**

### Proposed Mapping Statement (Option B)
```latex
\begin{tcolorbox}[colback=cyan!5!white, colframe=cyan!50!black,
    title=\textbf{Notation Convention (Part II vs Part I)}]
\textbf{Part I (Paper 2)} uses $\xi$ for the physical 5D coordinate.

\textbf{Part II (this Book)} uses $z$ for the physical 5D coordinate.

The correspondence is: $z \equiv \xi_{\text{Part I}}$

For dimensionless coordinates, we define $\tilde{z} = z/\ell \in [0,1]$
(avoiding reuse of $\xi$).
\end{tcolorbox}
```

---

## F) FILES REQUIRING CHANGES

### Option A (unify to ζ) - Major changes:
- `sections/ch11_opr20_attemptF_mediator_bvp_junction.tex` - BVP equations
- `sections/ch11_g5_canonical_and_kk.tex` - KK reduction
- `sections/09_va_structure.tex` - V-A derivation
- `code/bvp_verification_suite.py` - Variable names
- All figures with z-axis labels

### Option B (keep z + mapping) - Minimal changes:
- `sections/02_frozen_regime_foundations.tex` - Add mapping box
- `sections/ch11_opr20_attemptF_mediator_bvp_junction.tex` - Change ξ = z/ℓ to z̃ = z/ℓ
- Any other files using ξ for dimensionless coordinate

---

## G) DECISION RECORD

**Selected:** Option B (keep z + mapping)
**Rationale:**
1. Minimal code changes
2. z is more common in BVP literature
3. Clear explicit mapping is sufficient for readers
4. Avoids potential ζ/zeta-function collision
