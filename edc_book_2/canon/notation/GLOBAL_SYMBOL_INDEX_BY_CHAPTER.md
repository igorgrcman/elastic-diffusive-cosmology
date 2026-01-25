# GLOBAL SYMBOL INDEX BY CHAPTER — Book 2

**Generated**: 2026-01-24
**Source**: Automated extraction from edc_book_2/src/

This index lists symbols used in each Book 2 chapter/section file with their canonical meanings.
Use for quick reference during editing or review.

---

## Legend

| Status | Meaning |
|--------|---------|
| ✅ | Canon-anchored, correct usage |
| ⚠️ | Working symbol (no canon anchor yet) |
| 🔴 | Violation or ambiguity (see COLLISIONS report) |

---

## Main Entry Files

### src/main.tex
- **Document root** — includes all sections
- No direct symbol usage

### src/Z6_content_full.tex
- Z₆ (`\mathbb{Z}_6`) ✅ — Y-junction symmetry
- Z₃ (`\mathbb{Z}_3`) ✅ — Generation subgroup
- Z₂ (`\mathbb{Z}_2`) ✅ — Matter/antimatter
- θ (`\theta`) ✅ — Angular position
- σ (`\sigma`) ✅ — Brane tension

---

## Chapter Files (src/sections/)

### 00_canon_notation.tex
- **Notation definitions** — canonical reference
- R_ξ (`R_\xi`, `\Rxi`) ✅ — Compactification radius
- ξ (`\xi`) ✅ — 5D depth coordinate
- σ (`\sigma`) ✅ — Brane tension
- M⁵ (`\mathcal{M}^5`) ✅ — 5D manifold
- Σ³ (`\Sigma^3`) ✅ — 3D brane

### 01_how_we_got_here.tex
- Overview chapter — minimal symbols
- ξ ✅, σ ✅, R_ξ ✅

### 02_frozen_regime_foundations.tex
- ξ (`\xi`) ✅ — 5D depth
- κ (`\kappa`) ⚠️ — Penetration depth⁻¹ (Working)
- σ (`\sigma`) ✅ — Brane tension
- η (`\eta`) ✅ — Bulk viscosity

### 02_geometry_interface.tex
- M⁵ (`\mathcal{M}^5`) ✅ — 5D manifold
- Σ³ (`\Sigma^3`) ✅ — 3D brane
- ξ (`\xi`) ✅ — 5D depth
- G_AB (`G_{AB}`) ✅ — 5D metric
- g_μν (`g_{\mu\nu}`) ✅ — 4D induced metric

### 03_unified_pipeline.tex
- σ ✅, R_ξ ✅, ξ ✅
- G_F (`G_F`) ✅ — Fermi constant
- α (`\alpha`) ✅ — Fine structure

### 04_ontology.tex
- Conceptual chapter
- M⁵ ✅, Σ³ ✅

### 04a_unified_master_figure.tex
- Figure definitions
- All symbols canonical

### 04b_proton_anchor.tex
- S³ (`S^3`) ✅ — Proton angular space
- m_p (`m_p`) ✅ — Proton mass
- R_ξ ✅, σ ✅

### 05_case_neutron.tex
- m_n (`m_n`) ✅ — Neutron mass
- Δm_np (`\Delta m_{np}`) ✅ — n-p mass split
- Σ³ ✅ — 3D brane (5 uses)
- ξ ✅, σ ✅

### 05_neutron_story.tex
- Similar to 05_case_neutron
- m_n ✅, m_p ✅, Δm_np ✅

### 05_three_generations.tex
- Z₆ ✅, Z₃ ✅, Z₂ ✅
- M⁵ (`\mathcal{M}^5`) ✅ — Manifold (remediated from M_5)
- ξ_i (`\xi_i`) ⚠️ — Generation positions (Working)

### 06_case_muon.tex
- m_μ (`m_\mu`) ✅ — Muon mass
- ξ ✅, σ ✅

### 06_neutrinos_edge_modes.tex
- κ (`\kappa`) ⚠️ — Localization scale
- Δξ (`\Delta\xi`) ✅ — 5D separation (remediated from Δz)
- ξ_H (`\xi_H`) ✅ — Horizon position (remediated from z_H)
- f(ξ) ✅ — Profile function
- δ_CP (`\delta_{\text{CP}}`) ✅ — PMNS CP phase (disambiguated from δ thickness)

### 07_case_tau.tex
- m_τ (`m_\tau`) ✅ — Tau mass
- ξ ✅, σ ✅

### 07_ckm_cp.tex
- ξ_i (`\xi_i`) ⚠️ — Generation positions (remediated from z_i)
- O_ij — Overlap integrals (Working)
- CKM matrix elements
- Δξ ✅ — 5D separation

### 08_case_pion.tex
- m_π — Pion mass (BL)
- σ ✅, ξ ✅

### 09_case_electron.tex
- m_e (`m_e`) ✅ — Electron mass
- B³ (`B^3`) ✅ — Electron config space
- r_e ✅ — Knot radius

### 09_va_structure.tex
- Ψ(x^μ, ξ) ⚠️ — 5D fermion (remediated)
- Ψ_L, Ψ_R — Chiral components
- V-A structure

### 10_case_neutrino.tex
- Neutrino masses
- ξ ✅, κ ⚠️

### 11_gf_derivation.tex
- G_F (`G_F`) ✅ — Fermi constant
- M_{5,Pl} (`M_{5,\mathrm{Pl}}`) ✅ — 5D Planck mass (remediated)
- g₅ (`g_5`) ⚠️ — 5D gauge coupling
- R_ξ ✅

### 11_gf_pathway.tex
- Similar to 11_gf_derivation
- G_F ✅, g₅ ⚠️

### 12_epistemic_map.tex
- Meta-chapter — epistemic tags
- All symbols reference earlier definitions

### 13_summary.tex
- Summary chapter
- References all major symbols

---

## Attempt/Development Files (src/sections/ch11_*)

### ch11_opr20_attemptD*.tex
- M_{5,Pl} ✅ — 5D Planck mass (remediated from M_5)
- g₅ ⚠️, G_F ✅

### ch11_opr20_attemptF_mediator_bvp_junction.tex
- φ(x^μ, ξ) ⚠️ — Scalar field (remediated)
- BVP notation

### ch14_bvp_closure_pack.tex
- M_{5,Pl} ✅ — Lines 276, 280, 297, 305 (remediated)
- S_GHY (`S_{\mathrm{GHY}}`) ⚠️ — Line 305
- K_ab — Extrinsic curvature
- Junction conditions

---

## Symbol Frequency Summary

| Symbol | Total Uses | Files | Status |
|--------|------------|-------|--------|
| ξ | 910 | 40+ | ✅ |
| R_ξ | 382 | 30+ | ✅ |
| σ | 150+ | 25+ | ✅ |
| Z₆ | 80+ | 10+ | ✅ |
| m_e | 50+ | 15+ | ✅ |
| m_p | 40+ | 12+ | ✅ |
| G_F | 30+ | 8+ | ✅ |
| M_{5,Pl} | 8 | 4 | ✅ |
| κ | 20+ | 5+ | ⚠️ |
| g₅ | 15+ | 4+ | ⚠️ |

---

## Notes

1. All z → ξ remediations completed in Phase D (commit ed8006f, 7014cbd, cbbba70)
2. All M_5 → M_{5,Pl} or `\mathcal{M}^5` remediations completed
3. Working symbols (⚠️) need canon anchors in future Framework updates
4. No remaining violations after Phase D remediation

---

*Last updated: 2026-01-24*
