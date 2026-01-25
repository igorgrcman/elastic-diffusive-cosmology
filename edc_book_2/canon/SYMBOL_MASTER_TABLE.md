# EDC Symbol Master Table

Authority: Published artifacts (Framework v2.0, Paper 2, Companions A–H, Book Part I)
Status: CANON LAW — Book 2 must conform
Generated: 2026-01-24
DOI References: Framework v2.0 (10.5281/zenodo.18299085), Paper 3 (10.5281/zenodo.18262721)

---

## Purpose

This is the **single source of truth** for all EDC notation. Every symbol used in Book 2
must conform to the definitions in this table.

---

## Table Legend

| Column | Meaning |
|--------|---------|
| Symbol | Rendered symbol |
| LaTeX | LaTeX code |
| Type | coordinate / manifold / field / mass / scale / operator / topology / index / dummy |
| Meaning | One-sentence definition |
| Allowed | Contexts where this symbol is valid |
| Forbidden | Contexts where this symbol is NEVER used |
| Canon | Source artifact + section/equation |
| Book2 | Representative file:line refs + count |
| Risk | NONE / LOW / MED / HIGH |
| Action | OK / TODO / MUST-FIX |

---

## Part I: Geometry and Manifolds

| Symbol | LaTeX | Type | Meaning | Allowed | Forbidden | Canon | Book2 | Risk | Action |
|--------|-------|------|---------|---------|-----------|-------|-------|------|--------|
| M⁵ | `\mathcal{M}^5` | manifold | 5D bulk manifold = M⁴ × S¹_ξ | Topology, geometry, global structure | As mass symbol | Fwk v2.0 Eq.(1) | 0 uses | NONE | OK |
| M⁴ | `\mathcal{M}^4` | manifold | 4D spacetime | Geometry, GR | — | Fwk v2.0 Eq.(1) | — | NONE | OK |
| Σ³ | `\Sigma^3` | hypersurface | 3D brane embedded in M⁵ | Brane actions, embedding | Without superscript | Fwk v2.0 Eq.(2) | 05_case_neutron:5 | LOW | OK |
| S¹ | `S^1` | topology | Compact circle topology | Topology statements | As coordinate | Fwk v2.0 Eq.(1) | — | LOW | OK |
| S¹_ξ | `S^1_\xi` | topology | Circle parameterized by ξ | M⁵ = M⁴ × S¹_ξ | — | Fwk v2.0 Eq.(1) | — | NONE | OK |
| B³ | `B^3` | topology | 3-ball (electron config space) | Electron structure | — | Fwk v2.0 §5.1 | — | NONE | OK |
| S³ | `S^3` | topology | 3-sphere (proton angular space) | Proton structure | — | Fwk v2.0 §5.2 | — | NONE | OK |

### FORBIDDEN PATTERNS — MANIFOLD

| WRONG | Correct | Reason | Violation Count |
|-------|---------|--------|-----------------|
| M5 | `\mathcal{M}^5` | Looks like mass × 5 | 1 |
| M_5 | `\mathcal{M}^5` | Looks like mass subscript 5 | 21 |
| M^5 | `\mathcal{M}^5` | No calligraphic | 0 |

---

## Part II: Coordinates

| Symbol | LaTeX | Type | Meaning | Allowed | Forbidden | Canon | Book2 | Risk | Action |
|--------|-------|------|---------|---------|-----------|-------|-------|------|--------|
| ξ | `\xi` | coordinate | 5D compact coordinate ∈ [0, 2πR_ξ) | ALL 5D depth contexts | Coherence length (use ξ_GL) | Fwk v2.0 Eq.(3) | 382 uses of R_ξ | NONE | OK |
| x^μ | `x^\mu` | coordinate | 4D spacetime coords (μ=0,1,2,3) | 4D physics | — | Fwk v2.0 Eq.(3) | — | NONE | OK |
| x, y, z | `x, y, z` | coordinate | 3D spatial coordinates | (x,y,z) tuples ONLY | As 5D depth | Fwk v2.0 | 0 clean | HIGH | — |
| z | `z` | **CONTEXT-SENSITIVE** | See classification below | 3D spatial (x,y,z) | 5D depth | Fwk v2.0 | see violations | HIGH | MUST-FIX |
| z₁, z₂ | `z_1, z_2` | complex var | Z6 program complex variables | Z6 symmetry, polynomials | As coordinates | Fwk v2.0 §11 | — | LOW | OK |

### z-SYMBOL CLASSIFICATION MATRIX

| Context Pattern | Physical Meaning | Correct Symbol | Action |
|-----------------|------------------|----------------|--------|
| (x, y, z) | 3D spatial | z | OK |
| (x^μ, z) | 5D coordinate tuple | ξ | MUST-FIX |
| φ(x^μ, z) | Field in 5D | ξ | MUST-FIX |
| Δz (5D separation) | 5D depth difference | Δξ | MUST-FIX |
| f(z) profile | 5D profile function | f(ξ) | MUST-FIX |
| z_H (horizon) | 5D boundary | ξ_H | MUST-FIX |
| z₁, z₂ (subscripted) | Z6 complex | z₁, z₂ | OK |
| integration dummy | generic | context-dependent | TODO |

### COLLISION WARNING: ξ (Coordinate vs. Coherence)

| Context | Meaning | Resolution |
|---------|---------|------------|
| EDC 5D | Compact coordinate | ξ (canonical) |
| GL/Paper 2 | Coherence length | Use ξ_GL or λ |

---

## Part III: Scales and Parameters

| Symbol | LaTeX | Type | Meaning | Value | Canon | Book2 | Risk | Action |
|--------|-------|------|---------|-------|-------|-------|------|--------|
| R_ξ | `R_\xi` or `\Rxi` | scale | Compactification radius | ~10⁻¹⁸ m | Fwk v2.0 Def.1.1 | 382 uses | NONE | OK |
| ℓ_P | `\ell_P` | scale | Planck length | ~10⁻³⁵ m | Fwk v2.0 Def.1.1 | — | NONE | OK |
| r_e | `r_e` | scale | Topological knot radius | ~10⁻¹⁵ m | Fwk v2.0 Def.1.1 | — | NONE | OK |
| δ | `\delta` | scale | Brane thickness | ~R_ξ | Fwk v2.0 | — | LOW | OK |
| κ | `\kappa` | scale | Inverse penetration depth | — | Book 2 | 06_neutrinos:* | LOW | OK |
| σ | `\sigma` | parameter | Brane tension | ~8.8 MeV/fm² | Fwk v2.0 Eq.(10) | — | NONE | OK |

**Hierarchy**: ℓ_P ≪ R_ξ ≪ r_e (Framework v2.0 Eq.(7))

---

## Part IV: Masses and Couplings

| Symbol | LaTeX | Type | Meaning | Canon | Book2 | Risk | Action |
|--------|-------|------|---------|-------|-------|------|--------|
| M_{5,Pl} | `M_{5,\mathrm{Pl}}` | mass | 5D Planck mass | Derived | 0 uses | HIGH | MUST-FIX |
| m_e | `m_e` | mass | Electron mass | Fwk v2.0 §7.1 | — | NONE | OK |
| m_p | `m_p` | mass | Proton mass | Fwk v2.0 §7.2 | — | NONE | OK |
| m_n | `m_n` | mass | Neutron mass | Fwk v2.0 §10 | — | NONE | OK |
| m_μ | `m_\mu` | mass | Muon mass | Fwk v2.0 §15 | — | NONE | OK |
| m_τ | `m_\tau` | mass | Tau mass | Fwk v2.0 §15.7 | — | NONE | OK |
| Δm_np | `\Delta m_{np}` | mass | Neutron-proton mass difference | Fwk v2.0 §10.5 | — | NONE | OK |
| G₅ | `G_5` | coupling | 5D gravitational coupling | Fwk v2.0 Eq.(9) | 8 uses | NONE | OK |
| G₄ | `G_4` | coupling | 4D gravitational coupling | Fwk v2.0 | — | NONE | OK |
| G_F | `G_F` | coupling | Fermi constant | Fwk v2.0 §14 | — | NONE | OK |
| g₅ | `g_5` | coupling | 5D gauge coupling | Book 2 | 11_gf:* | LOW | OK |
| α | `\alpha` | constant | Fine structure constant | Fwk v2.0 §6 | — | NONE | OK |

### M_5 DISAMBIGUATION MATRIX

| Pattern | Physical Meaning | Correct Symbol | Files Affected |
|---------|------------------|----------------|----------------|
| π₁(M_5) | Manifold topology | `\pi_1(\mathcal{M}^5)` | 05_three_generations.tex (10) |
| g²/M_5² | Mass scale | `g^2/M_{5,\mathrm{Pl}}^2` | 11_gf_derivation.tex (2) |
| σ/M_5³ | Planck mass | `\sigma/M_{5,\mathrm{Pl}}^3` | ch11_opr20_attemptD.tex (3) |
| M_5³ R_5 | Planck mass | `M_{5,\mathrm{Pl}}^3 R_5` | ch14_bvp_closure_pack.tex (4) |

---

## Part V: Fields and Operators

| Symbol | LaTeX | Type | Meaning | Canon | Book2 | Risk | Action |
|--------|-------|------|---------|-------|-------|------|--------|
| A_μ | `A_\mu` | field | KK photon (EM gauge) | Fwk v2.0 Eq.(3) | — | NONE | OK |
| g_μν | `g_{\mu\nu}` | metric | 4D induced metric | Fwk v2.0 Eq.(3) | — | NONE | OK |
| G_AB | `G_{AB}` | metric | 5D bulk metric | Fwk v2.0 | — | NONE | OK |
| Ψ | `\Psi` | field | 5D fermion field | Book 2 | 09_va:* | LOW | OK |
| φ | `\phi` | field | Scalar/mediator field | Book 2 | ch11_*:* | LOW | OK |
| J^A | `J^A` | current | 5D energy current | Fwk v2.0 Def.3.2 | — | NONE | OK |
| J^ν_b→b | `\Jbb{\nu}` | current | Bulk-to-brane flux | Fwk v2.0 Rmk.4.5 | — | NONE | OK |

---

## Part VI: Y-Junction and Z6 Program

| Symbol | LaTeX | Type | Meaning | Canon | Book2 | Risk | Action |
|--------|-------|------|---------|-------|-------|------|--------|
| θ | `\theta` | angle | Angular position on Z6 ring | Fwk v2.0 §10.2 | — | NONE | OK |
| q | `q` | parameter | Asymmetry parameter | Fwk v2.0 Def.10.1 | — | NONE | OK |
| Z₆ | `Z_6` or `\mathbb{Z}_6` | group | Y-junction symmetry = Z₃ × Z₂ | Fwk v2.0 §9 | 05_three_gen:* | NONE | OK |
| Z₃ | `Z_3` or `\mathbb{Z}_3` | group | Generation subgroup | Fwk v2.0 §9 | — | NONE | OK |
| Z₂ | `Z_2` or `\mathbb{Z}_2` | group | Matter/antimatter | Fwk v2.0 §9 | — | NONE | OK |
| V₀ | `V_0` | potential | Z6-symmetric well depth | Fwk v2.0 §9.3 | — | NONE | OK |
| V₃ | `V_3` | potential | Flavor-breaking term | Fwk v2.0 §9.3 | — | NONE | OK |
| z₁, z₂ | `z_1, z_2` | complex | Z6 program roots | Fwk v2.0 §11 | — | LOW | OK |
| W | `W` | quantum | Winding number on S¹_ξ | Fwk v2.0 Def.3.1 | — | NONE | OK |

---

## Part VII: Actions

| Symbol | LaTeX | Type | Meaning | Canon | Book2 | Risk | Action |
|--------|-------|------|---------|-------|-------|------|--------|
| S_tot | `S_{\mathrm{tot}}` | action | Total action | Fwk v2.0 Eq.(8) | — | NONE | OK |
| S_bulk | `S_{\mathrm{bulk}}` | action | 5D Einstein-Hilbert | Fwk v2.0 Eq.(9) | — | NONE | OK |
| S_brane | `S_{\mathrm{brane}}` | action | Nambu-Goto membrane | Fwk v2.0 Eq.(10) | — | NONE | OK |
| S_defect | `S_{\mathrm{defect}}` | action | Defect action | Fwk v2.0 §2.4 | — | NONE | OK |
| S_GHY | `S_{\mathrm{GHY}}` | action | Gibbons-Hawking-York | Book 2 | ch14:305 | LOW | OK |

---

## Part VIII: Violation Summary

### By Type

| Violation Type | Count | Files | Priority |
|----------------|-------|-------|----------|
| M_5 as manifold | 10 | 05_three_generations.tex | HIGH |
| M_5 as mass | 9 | 11_gf, ch11_attemptD, ch14 | HIGH |
| z as 5D depth | 39+ | 06_neutrinos, 07_ckm, 09_va | HIGH |
| (x^μ, z) tuple | 3 | 09_va, ch11_attemptF | HIGH |
| Δz as 5D sep | 20+ | 06_neutrinos, 07_ckm | HIGH |

### By File

| File | M_5 | z-as-5D | Total | Status |
|------|-----|---------|-------|--------|
| 05_three_generations.tex | 10 | 0 | 10 | MUST-FIX |
| 06_neutrinos_edge_modes.tex | 0 | 15+ | 15+ | MUST-FIX |
| 07_ckm_cp.tex | 0 | 10+ | 10+ | MUST-FIX |
| 09_va_structure.tex | 0 | 15+ | 15+ | MUST-FIX |
| 11_gf_derivation.tex | 2 | 0 | 2 | MUST-FIX |
| ch11_opr20_attemptD*.tex | 3 | 0 | 3 | MUST-FIX |
| ch11_opr20_attemptF*.tex | 0 | 2 | 2 | MUST-FIX |
| ch14_bvp_closure_pack.tex | 4 | 2 | 6 | MUST-FIX |

---

## Appendix: Canonical Formulas (Reference)

| Formula | LaTeX | Canon Source |
|---------|-------|--------------|
| m_p/m_e = 6π⁵ | `m_p/m_e = 6\pi^5` | Fwk v2.0 Thm.5.3 |
| α = (4π + 5/6)/(6π⁵) | `\alpha = (4\pi + 5/6)/(6\pi^5)` | Fwk v2.0 Thm.6.1 |
| Δm_np = 8m_e/π | `\Delta m_{np} = 8m_e/\pi` | Fwk v2.0 §10.5 |
| M⁵ = M⁴ × S¹_ξ | `\mathcal{M}^5 = \mathcal{M}^4 \times S^1_\xi` | Fwk v2.0 Eq.(1) |

---

## Version History

| Date | Change | By |
|------|--------|-----|
| 2026-01-24 | Initial creation — comprehensive cross-document extraction | Claude |
