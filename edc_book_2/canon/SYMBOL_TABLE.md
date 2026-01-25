# EDC Canonical Symbol Table

Generated: 2026-01-24
Authority: Framework v2.0 (DOI: 10.5281/zenodo.18299085)
Status: CANON LAW — Book 2 must conform

## Manifold and Geometry

| Symbol | LaTeX | Object Type | Meaning | Canon Source | Notes |
|--------|-------|-------------|---------|--------------|-------|
| M⁵ | `\mathcal{M}^5` | manifold | 5D bulk manifold = M⁴ × S¹_ξ | Framework v2.0 Eq.(1) | **NEVER use M5, M_5** |
| M⁴ | `\mathcal{M}^4` | manifold | 4D spacetime | Framework v2.0 Eq.(1) | |
| Σ³ | `\Sigma^3` | hypersurface | 3D brane embedded in M⁵ | Framework v2.0 Eq.(2) | Also called "membrane" |
| S¹ | `S^1` | topology | Compact circle topology | Framework v2.0 Eq.(1) | NOT a coordinate |
| S¹_ξ | `S^1_\xi` | topology | Circle parameterized by ξ | Framework v2.0 Eq.(1) | |

## Coordinates

| Symbol | LaTeX | Object Type | Meaning | Canon Source | Notes |
|--------|-------|-------------|---------|--------------|-------|
| ξ | `\xi` | coordinate | 5D compact coordinate ∈ [0, 2πR_ξ) | Framework v2.0 Eq.(3) | **CANONICAL 5D depth** |
| x^μ | `x^\mu` | coordinate | 4D spacetime coordinates (μ=0,1,2,3) | Framework v2.0 Eq.(3) | |
| x, y, z | `x, y, z` | coordinate | 3D spatial coordinates | Framework v2.0 | **3D ONLY, never 5D depth** |

### CRITICAL: z vs ξ Disambiguation

| Context | Correct Symbol | WRONG Symbol | Rule |
|---------|---------------|--------------|------|
| 5D depth/compact coordinate | ξ | z | ALWAYS use ξ |
| 3D spatial axis | z | ξ | Use z for spatial |
| Z6 complex variables | z₁, z₂ | z | Subscripted only |
| Dummy integration variable | (context-dependent) | - | Document explicitly |

## Scales and Radii

| Symbol | LaTeX | Object Type | Meaning | Value | Canon Source |
|--------|-------|-------------|---------|-------|--------------|
| R_ξ | `R_\xi` or `\Rxi` | length scale | Compactification radius | ~10⁻¹⁸ m | Framework v2.0 Def.1.1 |
| ℓ_P | `\ell_P` | length scale | Planck length | ~10⁻³⁵ m | Framework v2.0 Def.1.1 |
| r_e | `r_e` | length scale | Topological knot radius | ~10⁻¹⁵ m | Framework v2.0 Def.1.1 |

**Hierarchy**: ℓ_P ≪ R_ξ ≪ r_e (Eq. 7)

## Physical Parameters

| Symbol | LaTeX | Object Type | Meaning | Units | Canon Source |
|--------|-------|-------------|---------|-------|--------------|
| σ | `\sigma` | parameter | Membrane/brane tension | J/m² | Framework v2.0 Eq.(10) |
| G₅ | `G_5` | coupling | 5D gravitational coupling | m³/(kg·s²) | Framework v2.0 Eq.(9) |
| Λ₅ | `\Lambda_5` | parameter | 5D cosmological constant | m⁻² | Framework v2.0 Eq.(9) |
| A_μ | `A_\mu` | field | Kaluza-Klein photon (EM gauge field) | - | Framework v2.0 Eq.(3) |
| g_μν | `g_{\mu\nu}` | metric | 4D induced metric | - | Framework v2.0 Eq.(3) |

## Particle Properties

| Symbol | LaTeX | Object Type | Meaning | Canon Source |
|--------|-------|-------------|---------|--------------|
| m_e | `m_e` | mass | Electron mass | Framework v2.0 Thm.7.1 |
| m_p | `m_p` | mass | Proton mass | Framework v2.0 Thm.7.2 |
| m_μ | `m_\mu` | mass | Muon mass | Framework v2.0 §15 |
| m_τ | `m_\tau` | mass | Tau mass | Framework v2.0 §15.7 |
| m_n | `m_n` | mass | Neutron mass | Framework v2.0 §10 |
| Δm_np | `\Delta m_{np}` | mass difference | Neutron-proton mass difference | Framework v2.0 §10.5 |
| W | `W` | quantum number | Winding number around S¹_ξ | Framework v2.0 Def.3.1 |

## Fundamental Constants (Derived)

| Symbol | LaTeX | Meaning | EDC Formula | Canon Source |
|--------|-------|---------|-------------|--------------|
| α | `\alpha` | Fine structure constant | (4π + 5/6)/(6π⁵) | Framework v2.0 Thm.6.1 |
| m_p/m_e | - | Proton-electron mass ratio | 6π⁵ | Framework v2.0 Thm.5.3 |

## Configuration Spaces

| Symbol | LaTeX | Object Type | Meaning | Canon Source |
|--------|-------|-------------|---------|--------------|
| B³ | `B^3` | topological space | 3-ball (electron config. space) | Framework v2.0 Thm.5.1 |
| S³ | `S^3` | topological space | 3-sphere (proton arm angular space) | Framework v2.0 Thm.5.2 |
| Vol(B³) | `\mathrm{Vol}(B^3)` | volume | = 4π/3 | Framework v2.0 §5.1 |
| Area(S³) | `\mathrm{Area}(S^3)` | area | = 2π² | Framework v2.0 §5.2 |

## Y-Junction and Z6 Program

| Symbol | LaTeX | Object Type | Meaning | Canon Source |
|--------|-------|-------------|---------|--------------|
| θ | `\theta` | angle | Angular position on Z6 ring | Framework v2.0 §10.2 |
| q | `q` | parameter | Asymmetry parameter | Framework v2.0 Def.10.1 |
| Z₆ | `Z_6` | symmetry group | Y-junction symmetry = Z₃ × Z₂ | Framework v2.0 Thm.9.1 |
| V₀ | `V_0` | potential | Z6-symmetric well depth | Framework v2.0 Thm.9.2 |
| V₃ | `V_3` | potential | Flavor-breaking term | Framework v2.0 Thm.9.2 |
| z₁, z₂ | `z_1, z_2` | complex variable | Z6 program roots | Framework v2.0 §11 |

**Note**: z₁, z₂ are Z6 complex variables, NOT coordinates.

## Energy/Current Bookkeeping

| Symbol | LaTeX | Object Type | Meaning | Canon Source |
|--------|-------|-------------|---------|--------------|
| J^A | `J^A` | current | 5D energy current | Framework v2.0 Def.3.2 |
| J^ν_{bulk→brane} | `\Jbb{\nu}` | current | Bulk-to-brane energy flux | Framework v2.0 Rmk.4.2 |
| T^{AB}_{(5)} | `T^{AB}_{(5)}` | tensor | 5D stress-energy tensor | Framework v2.0 Rmk.4.2 |

## Actions

| Symbol | LaTeX | Object Type | Meaning | Canon Source |
|--------|-------|-------------|---------|--------------|
| S_tot | `S_{\mathrm{tot}}` | action | Total action | Framework v2.0 Eq.(8) |
| S_bulk | `S_{\mathrm{bulk}}` | action | 5D Einstein-Hilbert action | Framework v2.0 Eq.(9) |
| S_brane | `S_{\mathrm{brane}}` | action | Nambu-Goto membrane action | Framework v2.0 Eq.(10) |
| S_defect | `S_{\mathrm{defect}}` | action | Defect action | Framework v2.0 §2.4 |

## Forbidden Symbols and Patterns

| WRONG | CORRECT | Reason |
|-------|---------|--------|
| M5, M_5 | `\mathcal{M}^5` | Looks like mass M times 5 |
| z (for 5D depth) | ξ | Canon uses ξ for compact coordinate |
| R_z, R_5 | R_ξ | Must match ξ notation |
| "topology ξ ≃ S¹" | "topology S¹ parameterized by ξ" | ξ is coordinate, S¹ is topology |

## COLLISION WARNING: ξ in Paper 2

Paper 2 uses ξ in TWO contexts:
1. **5D compact coordinate** (Postulate 3): "extra dimension has topology ξ ≃ S¹"
2. **Coherence length** (GL context): "where ξ is the coherence length"

**Resolution**: In EDC canon, ξ = 5D depth coordinate. GL coherence length should use ξ_GL or λ when context requires distinction.

---

## Version History

| Date | Change | By |
|------|--------|-----|
| 2026-01-24 | Initial creation from Framework v2.0 extraction | Claude |
