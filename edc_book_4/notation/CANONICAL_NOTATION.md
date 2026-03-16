# Canonical Notation Reference — EDC Research Program

**Date:** 2026-03-16
**Step:** 9 of 9 (Integration Program)
**Authority:** Framework v2.0, Book I, Paper 2, Book II NOTATION_POLICY.md
**Scope:** All EDC books, papers, and code

---

## 1. Executive Summary

### Conflicts Found and Resolved

| # | Conflict | Severity | Resolution |
|---|----------|----------|------------|
| C-01 | ξ vs z vs y (5D coordinate) | HIGH | **ξ** canonical; z only for 3D spatial (x,y,z) |
| C-02 | R_ξ vs L vs ℓ (compactification) | HIGH | **R_ξ** = radius; **ℓ** = 2πR_ξ = circumference |
| C-03 | δ bare (5 distinct scales) | CRITICAL | **Ban bare δ**; use δ_J, δ_BL, Δ, R_ξ always |
| C-04 | σ = 8.82 vs 5.86 MeV/fm² | CRITICAL | **OPEN** (OPR-34); distinguish σ_jun vs σ_cell |
| C-05 | β ambiguity | LOW | β_EDC vs Q_β (context-separated) |
| C-06 | κ (3 meanings) | MEDIUM | κ_3q, κ_pen, κ_ext (subscript disambiguation) |
| C-07 | M_5 (manifold vs mass) | MEDIUM | 𝓜⁵ (manifold), M_{5,Pl} (mass) — RESOLVED |
| C-08 | η (metric vs viscosity) | MEDIUM | η_μν (metric), η (viscosity) — subscript rule |
| C-09 | σ_BookI [M³] vs σ_cov [M⁴] | HIGH | σ_surf [M³] (Book I), σ [M⁴] (covariant brane) |

**Total unique symbols catalogued:** 85+
**Collisions resolved:** 7 (Book II Phase D remediation)
**Collisions remaining:** 2 (σ discrepancy OPR-34, κ anchor)
**Bare δ violations:** >50 (CRITICAL — must fix)

---

## 2. Complete Symbol Table

### 2.1 Manifolds and Topology

| Symbol | LaTeX | Physical Quantity | Dimensions | Tag | Used In | Conflicts |
|--------|-------|-------------------|------------|-----|---------|-----------|
| 𝓜⁵ | `\mathcal{M}^5` | 5D bulk manifold | — | [Def] | All books | M_5 (old) |
| 𝓜⁴ | `\mathcal{M}^4` | 4D spacetime | — | [Def] | All books | — |
| Σ³ | `\Sigma^3` | 3D brane/membrane | — | [Def] | All books | Σ (sum) |
| S¹ | `S^1` | Circle topology | — | [M] | All books | — |
| S¹_ξ | `S^1_\xi` | Circle parameterized by ξ | — | [Def] | Fwk v2.0 | — |
| S³ | `S^3` | 3-sphere | — | [M] | Book I, Paper 2 | — |
| B³ | `B^3` | 3-ball | — | [M] | Book I, Paper 2 | — |
| S⁵ | `S^5` | 5-sphere | — | [M] | Book IV | — |

### 2.2 Coordinates

| Symbol | LaTeX | Physical Quantity | Dimensions | Tag | Used In | Conflicts |
|--------|-------|-------------------|------------|-----|---------|-----------|
| **ξ** | `\xi` | 5D compact coordinate | [L] | [Def] | **CANONICAL** | z (old Book I) |
| ξ̃ | `\tilde{\xi}` | Dimensionless ξ/ℓ | 1 | [Def] | Book II BVP | — |
| ζ | `\zeta` | Rescaled ξ/ℓ (BVP) | 1 | [Def] | Book II Ch.14 | — |
| x^μ | `x^\mu` | 4D spacetime (μ=0,1,2,3) | [L] | [Def] | All | — |
| x, y, z | `x, y, z` | 3D Cartesian spatial | [L] | [Def] | All | z ≠ 5D! |
| r | `r` | 3D radial coordinate | [L] | [Def] | Soliton, nuclear | — |
| q | `q` | Junction collective coordinate | [L] | [Def] | Book II, IV | — |

**FORBIDDEN:** z for any 5D depth context. Use ξ.

### 2.3 Length Scales

| Symbol | LaTeX | Physical Quantity | Value | Tag | Used In | Conflicts |
|--------|-------|-------------------|-------|-----|---------|-----------|
| R_ξ | `R_\xi` | Compactification radius | 2.16×10⁻³ fm | [BL] | All books | R, L (old) |
| ℓ | `\ell` | Orbifold circumference = 2πR_ξ | 0.0136 fm | [Dc] | Book II | L (old) |
| L₀ | `L_0` | Junction spatial extent | ~1 fm | [P] | Book IV | — |
| r_e | `r_e` | Classical electron radius | 2.818 fm | [BL] | Paper 2 | — |
| ℓ_P | `\ell_P` | Planck length | 1.6×10⁻³⁵ m | [BL] | All | — |
| **δ_J** | `\delta_J` | Junction core thickness | 0.105 fm | [I] | Book IV | δ (bare) |
| **Δ** | `\Delta` | Kink half-width (λφ⁴) | ~0.003 fm | [P] | Book II | δ (bare) |
| **δ_BL** | `\delta_{BL}` | Boundary layer scale | ~R_ξ | [P] | Book II BVP | δ (bare) |
| d₀ | `d_0` | Equilibrium junction spacing | — | [P] | Book IV Ch.2 | — |

**RULE:** Never use bare δ. Always subscript: δ_J, δ_BL, or use Δ, R_ξ.

### 2.4 Tensions and Energies

| Symbol | LaTeX | Physical Quantity | Dimensions | Tag | Used In | Conflicts |
|--------|-------|-------------------|------------|-----|---------|-----------|
| σ | `\sigma` | Canonical brane tension | [M⁴] | [Dc] | All (covariant) | σ_surf |
| σ_surf | `\sigma_{\mathrm{surf}}` | Book I surface tension | [M³] | [Dc] | Book I | σ |
| σ_eff | `\sigma_{\mathrm{eff}}` | Effective membrane tension | [M/L²] | [Cal] | Paper 2 | — |
| σ_jun | `\sigma_{\mathrm{jun}}` | Junction sector: 8.82 MeV/fm² | [M/L²] | [Dc] | Book IV | σ_cell |
| σ_cell | `\sigma_{\mathrm{cell}}` | Cell sector: 5.86 MeV/fm² | [M/L²] | [Dc] | Book II | σ_jun |
| σ̃ | `\tilde{\sigma}` | Dimensionless σ_cov/T_* | 1 | [Der] | v68 | — |
| T_* | `T_*` | Characteristic tension = 3M₅³/(4πℓ) | [M⁴] | [Der] | v68 | — |
| K | `K` | Pinning constant | [E] | [Dc] | Book IV | — |
| V_B | `V_B` | Barrier height | [E] | [P] | Book IV | — |
| E₀ | `E_0` | Ground-state junction energy = σL₀² | [E] | [Dc] | Book II | — |

**NOTE:** σ_jun vs σ_cell discrepancy (ratio ≈ 3/2) is tracked by OPR-34.

### 2.5 Masses

| Symbol | LaTeX | Physical Quantity | Dimensions | Tag | Used In |
|--------|-------|-------------------|------------|-----|---------|
| M_{5,Pl} | `M_{5,\mathrm{Pl}}` | 5D Planck mass | [M] | [BL] | All |
| M̄_Pl | `\bar{M}_{\mathrm{Pl}}` | Reduced 4D Planck mass | [M] | [BL] | Block-003 |
| m_e | `m_e` | Electron mass | [M] | [BL] | All |
| m_p | `m_p` | Proton mass | [M] | [BL] | All |
| m_n | `m_n` | Neutron mass | [M] | [BL] | All |
| Δm_np | `\Delta m_{np}` | Neutron-proton mass split | [M] | [BL] | Book II, IV |
| M₀ | `M_0` | Bulk Dirac mass scale | [1/L] | [P] | Book II BVP |
| M_X | `M_X` | Unification mass | [M] | [Dc] | Block-003 |

### 2.6 Couplings and Constants

| Symbol | LaTeX | Physical Quantity | Dimensions | Tag | Used In |
|--------|-------|-------------------|------------|-----|---------|
| α | `\alpha` | Fine structure constant | 1 | [Dc] | Paper 2, All |
| α₃ | `\alpha_3` | Strong coupling at KK scale = 1/σ̃ | 1 | [Dc] | Block-003 |
| G₅ | `G_5` | 5D gravitational constant | [L³/M/T²] | [Dc] | Book I, Block-003 |
| G_N | `G_N` | 4D Newton constant | [L³/M/T²] | [BL] | All |
| G_F | `G_F` | Fermi constant | [1/E²] | [BL] | Book II |
| g₅ | `g_5` | 5D gauge coupling | [L^{1/2}] | [P] | Book II |
| g₅^(C) | `g_5^{(C)}` | Corrected 5D gauge coupling | [L^{1/2}] | [P] | OPR-32 |

### 2.7 Symmetry Groups

| Symbol | LaTeX | Physical Quantity | Tag | Used In |
|--------|-------|-------------------|-----|---------|
| Z₆ | `\mathbb{Z}_6` | Full junction symmetry | [Dc] | Book II, IV |
| Z₃ | `\mathbb{Z}_3` | Arm permutation / color | [Dc] | Book II, IV |
| Z₂ | `\mathbb{Z}_2` | Parity / weak isospin | [Dc] | Book II, IV |

### 2.8 BVP and Weak Sector

| Symbol | LaTeX | Physical Quantity | Dimensions | Tag | Used In |
|--------|-------|-------------------|------------|-----|---------|
| V_L | `V_L` | Left-chirality potential = M²−M' | [1/L²] | [Dc] | Book II |
| V_R | `V_R` | Right-chirality potential = M²+M' | [1/L²] | [Dc] | Book II |
| f_n(ξ) | `f_n(\xi)` | n-th KK mode profile | 1 | [Dc] | Book II |
| m_n | `m_n` | n-th KK eigenvalue | [M] | [P] | Book II |
| μ | `\mu` | Dimensionless BVP parameter = M₀ℓ | 1 | [P] | Book II |
| ρ | `\rho` | Shape parameter = Δ/ℓ | 1 | [I] | Book II |
| κ_BC | `\kappa_{BC}` | Robin BC parameter = m_b/2 | [1/L] | [Dc] | Book II |
| sin²θ_W | `\sin^2\theta_W` | Weak mixing angle | 1 | [Dc] | Book II |

### 2.9 Neutron Lifetime (Path B)

| Symbol | LaTeX | Physical Quantity | Dimensions | Tag | Used In |
|--------|-------|-------------------|------------|-----|---------|
| τ_n | `\tau_n` | Neutron lifetime | [T] | [Dc+P+Cal] | Book II, IV |
| κ | `\kappa` | Topological winding = 2π | 1 | [Dc] | Book IV |
| S_E | `S_E` | Euclidean bounce action | [E·T] | [Dc+P] | Book IV |
| ω₀ | `\omega_0` | Attempt frequency | [1/T] | [P] | Book IV |
| A | `A` | WKB prefactor | 1 | [Cal] | Book IV |

### 2.10 Nuclear Topology (Book IV)

| Symbol | LaTeX | Physical Quantity | Dimensions | Tag | Used In |
|--------|-------|-------------------|------------|-----|---------|
| n(A) | `n(A)` | Effective coordination number = pA^{1/3} | 1 | [Cal] | Book IV |
| p | `p` | Coordination prefactor | 1 | [Cal] | Book IV |
| S | `S` | Allowed set = {2^a × 3^b} | — | [Der] | Book IV |
| d(n) | `d(n)` | Frustration distance to S | 1 | [Der] | Book IV |
| X | `X` | GN barrier ratio = Z_d/√Q_α | [Z/√E] | [BL] | Book IV |
| g | `g` | Frustration coupling | dex | [Cal] | Book IV |

### 2.11 Soliton Profile

| Symbol | LaTeX | Physical Quantity | Dimensions | Tag | Used In |
|--------|-------|-------------------|------------|-----|---------|
| f(r) | `f(r)` | Brane displacement profile | [L] | [Dc] | Paper 3 |
| φ | `\varphi` | Golden ratio tail exponent = (1+√5)/2 | 1 | [Dc] | Paper 3 |
| Q | `Q` | Topological charge | 1 | [Def] | Paper 3 |

### 2.12 Actions

| Symbol | LaTeX | Physical Quantity | Tag | Used In |
|--------|-------|-------------------|-----|---------|
| S_EDC | `S_{\mathrm{EDC}}` | Total EDC action | [Def] | All |
| S_bulk | `S_{\mathrm{bulk}}` | 5D Einstein-Hilbert | [Def] | All |
| S_brane | `S_{\mathrm{brane}}` | Nambu-Goto membrane | [Def] | All |
| S_defect | `S_{\mathrm{defect}}` | Topological defect | [Def] | All |
| S_GHY | `S_{\mathrm{GHY}}` | Gibbons-Hawking-York | [Def] | Block-003 |
| S_eff[q] | `S_{\mathrm{eff}}[q]` | Effective 1D action | [Dc] | Book II, IV |

---

## 3. Conflict Resolution Log

### C-01: 5D Coordinate (ξ vs z)

**Problem:** Book I and some papers use z for the 5D depth coordinate; Book II uses ξ (canonical).

**Resolution:**
- **ξ** is canonical (Framework v2.0 Eq.3, 910 uses in Book II)
- z is reserved exclusively for 3D spatial coordinate in (x,y,z) tuples
- y is never used for 5D depth
- ζ = ξ/ℓ is acceptable as dimensionless rescaling in BVP context

**Book II status:** REMEDIATED (Phase D, 39+ z→ξ fixes applied)
**Book I status:** DRIFT — ~15 z→ξ fixes needed
**Book IV status:** Clean (uses ξ throughout)

### C-02: Compactification Length

**Problem:** Three symbols (R_ξ, L, ℓ) used for compactification-related lengths.

**Resolution:**
- **R_ξ** = compactification radius (canonical, 382 uses in Book II)
- **ℓ** = orbifold circumference = 2πR_ξ (distinct quantity, both valid)
- **L** is NOT used for compactification (reserved for Lagrangian density)
- L₀ = junction extent (different quantity entirely)

### C-03: Thickness Scales (δ ambiguity)

**Problem:** Bare δ used for 5 physically distinct scales spanning 50× range.

**Resolution:** Mandatory subscripts:

| Old | New | Value | Sector |
|-----|-----|-------|--------|
| δ (junction context) | **δ_J** | 0.105 fm | Nucleon |
| δ (boundary layer) | **δ_BL** | ~R_ξ | BVP |
| δ (kink width) | **Δ** | 0.003 fm | Scalar |
| δ (electroweak) | **R_ξ** | 0.002 fm | KK |
| δ (generic) | **BANNED** | — | — |

### C-04: σ Discrepancy

**Problem:** Two numerically different values both called σ.

| Context | Value | Source |
|---------|-------|--------|
| σ_jun | 8.82 MeV/fm² | m_e³c⁴/(α³ℏ²) from junction |
| σ_cell | 5.86 MeV/fm² | ε_cell/r_e² from Z₆ lattice |
| Ratio | 1.505 ≈ 3/2 | Geometric factor? |

**Resolution:** OPEN (OPR-34). Use σ_jun and σ_cell with subscripts until resolved.

### C-05: β Ambiguity

**Problem:** β used for EDC control parameter, QCD beta function, and decay Q-value.

**Resolution:** Context-separated (low severity):
- β_EDC: geometric vortex parameter
- Q_β: decay Q-value (not bare β)
- β(μ): QCD running (standard notation, keep)

### C-06: κ Ambiguity

**Problem:** κ used for topological winding (2π), penetration depth, junction geometry (κ_3q), and Robin BC.

**Resolution:** Subscript disambiguation:
- κ = 2π: topological winding number (Book IV Path B) — contextually clear
- κ_3q = 5/6: junction geometric factor (Paper 2)
- κ_BC = m_b/2: Robin boundary condition parameter (Book II BVP)
- κ_pen: inverse penetration depth (Book II neutrino)

### C-07: M_5 (Manifold vs Mass)

**Problem:** M_5 used for both the 5D manifold topology and the 5D Planck mass.

**Resolution:** RESOLVED in Book II (Phase D):
- 𝓜⁵ (`\mathcal{M}^5`): 5D manifold (calligraphic M)
- M_{5,Pl} (`M_{5,\mathrm{Pl}}`): 5D Planck mass (Roman subscript)

### C-08: η Ambiguity

**Problem:** η for Minkowski metric and bulk viscosity.

**Resolution:** Subscript rule:
- η_μν: always with indices for metric
- η (bare): bulk viscosity (EDC-specific)

### C-09: σ Dimensional Mismatch

**Problem:** Book I σ has dimensions [M³] (energy per 2D area); covariant σ has [M⁴] (energy per 3D volume).

**Resolution:**
- σ_surf: Book I surface tension [M³] — historical, retained in Book I context
- σ: covariant brane tension [M⁴] — canonical for 5D gravity
- Relation: σ = σ_surf × f(geometry) where f carries [M¹]
- Tracked by OPR-29

---

## 4. Deprecated Symbols

| Deprecated | Replacement | Reason | Files Affected |
|------------|-------------|--------|----------------|
| z (5D depth) | ξ | Framework v2.0 Eq.3 | Book I Ch.0, Papers |
| y (5D depth) | ξ | Consistency | Book II §06 |
| M_5 (manifold) | 𝓜⁵ | Collision with mass | Book II (fixed) |
| M_5 (mass) | M_{5,Pl} | Collision with manifold | Book II (fixed) |
| δ (bare) | δ_J, δ_BL, Δ, R_ξ | 50× scale ambiguity | ALL (>50 occurrences) |
| L (compactification) | R_ξ or ℓ | Collision with Lagrangian | Various |
| R (compactification) | R_ξ | Collision with Ricci | Various |
| σ̃ = 100 | σ̃ = 1 | v68 invalidation | v67 documents |

---

## 5. LaTeX Macro Reference

See `edc_macros.sty` for the complete macro file. Key categories:

| Category | Macros | Count |
|----------|--------|-------|
| Manifolds & topology | `\Mbulk`, `\brane`, `\Sone`, `\Sthree` | 8 |
| Coordinates | `\xifive`, `\xitilde`, `\Rxi` | 5 |
| Scales | `\deltaJ`, `\deltaBL`, `\kinkwidth`, `\Lzero` | 6 |
| Tensions | `\sigmasurf`, `\sigmabrane`, `\sigmaeff`, `\sigmatilde` | 6 |
| Masses | `\MfivePl`, `\MPlbar` | 4 |
| Couplings | `\alphaEDC`, `\alphathree`, `\gfive` | 5 |
| Symmetry | `\Zsix`, `\Zthree`, `\Ztwo` | 3 |
| BVP | `\Veff`, `\kappaBC`, `\sintwW` | 5 |
| Actions | `\SEDC`, `\Sbulk`, `\Sbrane`, `\Sdefect` | 5 |
| Epistemic tags | `\tagDer`, `\tagDc`, `\tagP`, etc. | 9 |
| Ontology | `\AnchorJunction`, `\MetastableJunction`, etc. | 5 |
| **Total** | | **61** |

---

## 6. Per-Book Status

### 6.1 Book I (edc_book/)

| Issue | Count | Severity | Action |
|-------|-------|----------|--------|
| z→ξ (5D coordinate) | ~15 | HIGH | Replace in Ch.0, Ch.6 |
| M_5→𝓜⁵ or M_{5,Pl} | ~3 | MEDIUM | Replace in Ch.0 |
| Bare δ→subscripted | ~10 | HIGH | Add _J or _BL context |
| σ_surf labeling | ~5 | LOW | Add _surf where [M³] intended |

### 6.2 Book II (edc_book_2/)

| Issue | Count | Severity | Action |
|-------|-------|----------|--------|
| z→ξ remediation | 39+ | — | **COMPLETED** (Phase D) |
| M_5 disambiguation | 19 | — | **COMPLETED** (Phase D) |
| Bare δ→subscripted | ~20 | HIGH | Replace in Ch.5, Ch.14 |
| κ disambiguation | ~8 | MEDIUM | Add _BC, _pen, _3q |
| η clarification | ~3 | LOW | Add _μν where metric |

### 6.3 Book IV (edc_book_4/)

| Issue | Count | Severity | Action |
|-------|-------|----------|--------|
| 5D coordinate | 0 | — | Clean (uses ξ) |
| Bare δ→subscripted | ~15 | HIGH | Add _J in Ch.4, Ch.8 |
| σ value consistency | ~5 | CRITICAL | Await OPR-34 resolution |
| L₀/δ → L₀/δ_J | ~20 | HIGH | Clarify which δ |

### 6.4 Papers (edc_papers/)

| Issue | Count | Severity | Action |
|-------|-------|----------|--------|
| z→ξ (Paper 3) | ~5 | MEDIUM | Replace in rebuild snapshot |
| σ_eff circularity note | ~2 | LOW | Already documented |
| Macro alignment | — | LOW | Import edc_macros.sty |

---

## 7. Future Writing Standards

### 7.1 Mandatory Rules

1. **5D coordinate:** Always ξ. Never z, y, or w for 5D depth.
2. **Thickness:** Always subscripted (δ_J, δ_BL, Δ, R_ξ). Never bare δ.
3. **Manifold vs mass:** 𝓜⁵ (calligraphic) for manifold, M_{5,Pl} for Planck mass.
4. **Tension:** σ for canonical [M⁴] brane tension. σ_surf for Book I [M³]. σ_eff for effective.
5. **Epistemic tags:** Every quantitative claim must carry a tag ([Der], [Dc], [P], [Cal], [BL], [I], [M]).
6. **Macros:** Use `edc_macros.sty` for all new writing. Import via `\usepackage{edc_macros}`.

### 7.2 Recommended Practices

1. At first use in any chapter, define the physical meaning of each symbol.
2. When a symbol has multiple uses across EDC, state explicitly which meaning is intended.
3. Use the `\observerbox{}` environment for epistemic status declarations.
4. Run `gate_notation.sh` before committing any .tex file.

### 7.3 Scale Hierarchy Reference

For quick reference, the canonical length scales in decreasing order:

```
L₀     ≈ 1 fm           Junction extent           [P]
δ_J    ≈ 0.105 fm       Junction core (Compton)   [I]
ℓ      = 2πR_ξ ≈ 0.014 fm  Orbifold circumference [Dc]
Δ      ≈ 0.003 fm       Kink half-width           [P]
R_ξ    ≈ 0.002 fm       Compactification radius   [BL]
ℓ_P    ≈ 1.6×10⁻²⁰ fm  Planck length             [BL]

Hierarchy: L₀ ≫ δ_J ≫ ℓ > Δ ~ R_ξ ≫ ℓ_P
```

---

**Sealed:** 2026-03-16. Step 9 of 9. Canonical notation reference complete.
85+ symbols catalogued, 9 conflicts resolved or tracked, 61 prior violations remediated.
