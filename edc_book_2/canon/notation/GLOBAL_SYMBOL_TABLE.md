# GLOBAL SYMBOL TABLE — EDC Canonical Notation

**Authority**: Published artifacts (Framework v2.0, Paper 2, Companions A–H, Book Part I)
**Status**: CANON LAW — Book 2 must conform
**Generated**: 2026-01-24
**Git Branch**: book2-global-symbol-table-v1

---

## Purpose

This is the **single source of truth** for all EDC notation across:
1. **Book Part I** (EDC_Book_v17.49.pdf) — CANON
2. **Paper 2** (EDC_Paper2.pdf) — CANON
3. **Framework v2.0** (DOI: 10.5281/zenodo.18299085) — CANON-PRIMARY
4. **Paper 3 + Companions A–H** (paper3_bundle) — CANON
5. **Book 2 / Part II** (edc_book_2/src/) — WORKING, must conform

No notation changes are permitted without updating this table first.

---

## Column Legend

| Column | Meaning |
|--------|---------|
| Symbol | Rendered symbol (Unicode) |
| LaTeX | LaTeX code |
| Name | Human-readable name |
| Meaning | One-sentence definition |
| Domain | Context tag: 5D bulk, brane, SM, Z6, BVP, kinematics, units |
| Units | SI dimensions if applicable |
| Canon Status | CANON / CANON-PRIMARY / WORKING |
| Canon Anchor | PDF page + snippet or section reference |
| Book2 Anchor | File:line or label reference |
| Collision Risk | NONE / AMBIGUOUS / COLLISION |
| Resolution | Canon rule or NEEDS HUMAN DECISION |

---

## Part I: Manifolds and Topology

| Symbol | LaTeX | Name | Meaning | Domain | Units | Canon | Canon Anchor | Book2 Anchor | Risk | Resolution |
|--------|-------|------|---------|--------|-------|-------|--------------|--------------|------|------------|
| M⁵ | `\mathcal{M}^5` | 5D manifold | Complete 5D bulk spacetime = M⁴ × S¹_ξ | 5D bulk | — | CANON-PRIMARY | Fwk v2.0 Eq.(1), p.2 | 05_three_generations:§manifold | NONE | — |
| M⁴ | `\mathcal{M}^4` | 4D spacetime | Observable 4D spacetime manifold | 5D bulk | — | CANON | Fwk v2.0 Eq.(1) | — | NONE | — |
| Σ³ | `\Sigma^3` | 3D brane | Observable 3D spatial hypersurface | brane | — | CANON-PRIMARY | Fwk v2.0 Eq.(2), §2.1 | 05_case_neutron:5 uses | NONE | — |
| S¹ | `S^1` | Circle | Compact circle topology | topology | — | CANON | Fwk v2.0 §1.1 | — | NONE | — |
| S¹_ξ | `S^1_\xi` | ξ-circle | Circle parameterized by ξ | topology | — | CANON | Fwk v2.0 Eq.(1) | — | NONE | — |
| B³ | `B^3` | 3-ball | Electron configuration space | topology | — | CANON | Fwk v2.0 §5.1 | — | NONE | — |
| S³ | `S^3` | 3-sphere | Proton angular space | topology | — | CANON | Fwk v2.0 §5.2 | 04b_proton_anchor | NONE | — |

### FORBIDDEN MANIFOLD PATTERNS

| WRONG | Correct | Reason |
|-------|---------|--------|
| `M5` | `\mathcal{M}^5` | Looks like mass × 5 |
| `M_5` | `\mathcal{M}^5` | Looks like mass subscript |
| `M^5` | `\mathcal{M}^5` | Missing calligraphic |

---

## Part II: Coordinates

| Symbol | LaTeX | Name | Meaning | Domain | Units | Canon | Canon Anchor | Book2 Anchor | Risk | Resolution |
|--------|-------|------|---------|--------|-------|-------|--------------|--------------|------|------------|
| ξ | `\xi` | 5D depth | Compact coordinate ∈ [0, 2πR_ξ) | 5D bulk | m | CANON-PRIMARY | Fwk v2.0 Eq.(3), "compact coordinate ξ" p.3 | 910 uses | NONE | — |
| x^μ | `x^\mu` | 4D coords | Spacetime coordinates (μ=0,1,2,3) | 4D | m | CANON | Fwk v2.0 Eq.(3) | — | NONE | — |
| x, y, z | `x, y, z` | 3D spatial | Cartesian spatial coordinates | 3D | m | CANON | — | (x,y,z) tuples only | HIGH | Use ONLY in (x,y,z) tuples |
| z | **CONTEXT** | **SEE BELOW** | Context-sensitive — see z-matrix | varies | — | — | — | — | HIGH | See z-classification |
| z₁, z₂ | `z_1, z_2` | Z6 complex | Complex roots in Z6 program | Z6 | — | CANON | Fwk v2.0 §11 | — | LOW | OK for Z6 only |
| ξ_i | `\xi_i` | Generation position | 5D depth of generation i | 5D bulk | m | WORKING | — | 07_ckm_cp:460-462 | NONE | — |

### z-SYMBOL CLASSIFICATION MATRIX

| Context Pattern | Physical Meaning | Correct Symbol | Action |
|-----------------|------------------|----------------|--------|
| (x, y, z) | 3D spatial tuple | z | OK |
| (x^μ, z) | 5D coordinate tuple | ξ | MUST-FIX |
| φ(x^μ, z) | Field in 5D | ξ | MUST-FIX |
| Δz (5D separation) | 5D depth difference | Δξ | MUST-FIX |
| f(z) profile | 5D profile function | f(ξ) | MUST-FIX |
| z_H (horizon) | 5D boundary | ξ_H | MUST-FIX |
| z₁, z₂ (subscripted) | Z6 complex | z₁, z₂ | OK |
| z_i (generation) | 5D generation position | ξ_i | MUST-FIX |
| ∫...dz (bulk integral) | 5D integration | ∫...dξ | MUST-FIX |

---

## Part III: Scales and Parameters

| Symbol | LaTeX | Name | Meaning | Domain | Units | Canon | Canon Anchor | Book2 Anchor | Risk | Resolution |
|--------|-------|------|---------|--------|-------|-------|--------------|--------------|------|------------|
| R_ξ | `R_\xi` or `\Rxi` | Compactification radius | Size of S¹_ξ circle | 5D bulk | m | CANON-PRIMARY | Fwk v2.0 Def.1.1, "R_ξ ~ 10⁻¹⁸ m" p.3 | 382 uses | NONE | — |
| ℓ_P | `\ell_P` | Planck length | Quantum gravity scale | units | m | CANON | Fwk v2.0 Def.1.1 | — | NONE | — |
| r_e | `r_e` | Knot radius | Topological knot scale | topology | m | CANON | Fwk v2.0 Def.1.1 | — | NONE | — |
| δ | `\delta` | Brane thickness | Effective membrane width | brane | m | CANON | Fwk v2.0 §2.3 | — | LOW | — |
| δ_CP | `\delta_{\text{CP}}` | PMNS CP phase | CP-violating phase in PMNS matrix | PMNS | rad | BASELINE | PDG 2024 | 06_neutrinos:172,620,760 | NONE | Disambiguated from δ (thickness) |
| κ | `\kappa` | Penetration depth⁻¹ | Inverse localization scale | BVP | m⁻¹ | WORKING | — | 06_neutrinos:* | LOW | — |
| σ | `\sigma` | Brane tension | Membrane surface tension | brane | MeV/fm² | CANON-PRIMARY | Fwk v2.0 Eq.(10), "σ ~ 8.8 MeV/fm²" | — | NONE | — |
| η | `\eta` | Bulk viscosity | 5D fluid viscosity | 5D bulk | — | CANON | Fwk v2.0 §3.2 | — | LOW | Context: η_bulk vs η_metric |
| ξ_GL | `\xi_{\mathrm{GL}}` | GL coherence length | Ginzburg-Landau coherence length (condensed matter analogy) | brane | m | WORKING | — | 02_frozen_regime:237,240,267,311,317 | NONE | Distinct from 5D coord ξ |

**Hierarchy (CANON)**: ℓ_P ≪ R_ξ ≪ r_e (Framework v2.0 Eq.(7))

---

## Part IV: Masses and Couplings

| Symbol | LaTeX | Name | Meaning | Domain | Units | Canon | Canon Anchor | Book2 Anchor | Risk | Resolution |
|--------|-------|------|---------|--------|-------|-------|--------------|--------------|------|------------|
| M_{5,Pl} | `M_{5,\mathrm{Pl}}` | 5D Planck mass | Fundamental 5D gravity scale | 5D bulk | GeV | CANON | Fwk v2.0 §2.2 | ch14:276,280,297,305 | NONE | Disambiguated from manifold |
| m_e | `m_e` | Electron mass | Observed electron mass | SM | MeV/c² | CANON | Book I p.57, Fwk v2.0 §7.1, 142 anchors | — | NONE | — |
| m_p | `m_p` | Proton mass | Observed proton mass | SM | MeV/c² | CANON | Book I p.68, Fwk v2.0 §7.2, 36 anchors | — | NONE | — |
| m_n | `m_n` | Neutron mass | Observed neutron mass | SM | MeV/c² | CANON | Fwk v2.0 §10 | 05_case_neutron | NONE | — |
| m_μ | `m_\mu` | Muon mass | Observed muon mass | SM | MeV/c² | CANON | Fwk v2.0 §15 | 06_case_muon | NONE | — |
| m_τ | `m_\tau` | Tau mass | Observed tau mass | SM | MeV/c² | CANON | Fwk v2.0 §15.7 | 07_case_tau | NONE | — |
| Δm_np | `\Delta m_{np}` | n-p mass split | Neutron-proton mass difference | SM | MeV/c² | CANON | Fwk v2.0 §10.5, "Δm_np = 8m_e/π" | — | NONE | — |
| G₅ | `G_5` | 5D Newton | 5D gravitational coupling | 5D bulk | m³/kg/s² | CANON | Fwk v2.0 Eq.(9) | 8 uses | NONE | — |
| G₄ | `G_4` | 4D Newton | Observed gravitational constant | SM | m³/kg/s² | CANON | Fwk v2.0 | — | NONE | — |
| G_F | `G_F` | Fermi constant | Weak interaction coupling | SM | GeV⁻² | CANON | Fwk v2.0 §14 | 11_gf_derivation | NONE | — |
| g₅ | `g_5` | 5D gauge | 5D gauge coupling | 5D bulk | — | WORKING | — | 11_gf:* | LOW | — |
| α | `\alpha` | Fine structure | Electromagnetic coupling | SM | — | CANON | Book I p.57, Fwk v2.0 §6, 11 anchors | — | NONE | — |

### M_5 DISAMBIGUATION (CRITICAL)

| Pattern | Physical Meaning | Correct Symbol |
|---------|------------------|----------------|
| π₁(M_5) | Manifold topology | `\pi_1(\mathcal{M}^5)` |
| M_5² in denominator | Mass scale | `M_{5,\mathrm{Pl}}^2` |
| M_5³ R_5 | Planck mass | `M_{5,\mathrm{Pl}}^3 R_5` |
| σ/M_5³ | Planck mass | `\sigma/M_{5,\mathrm{Pl}}^3` |

---

## Part V: Fields and Operators

| Symbol | LaTeX | Name | Meaning | Domain | Units | Canon | Canon Anchor | Book2 Anchor | Risk | Resolution |
|--------|-------|------|---------|--------|-------|-------|--------------|--------------|------|------------|
| A_μ | `A_\mu` | KK photon | Electromagnetic gauge field | SM | — | CANON | Fwk v2.0 Eq.(3) | — | NONE | — |
| g_μν | `g_{\mu\nu}` | 4D metric | Induced metric on brane | brane | — | CANON | Fwk v2.0 Eq.(3) | — | NONE | — |
| G_AB | `G_{AB}` | 5D metric | Bulk metric tensor | 5D bulk | — | CANON | Fwk v2.0 | — | NONE | — |
| Ψ | `\Psi` | 5D fermion | Bulk fermion field | 5D bulk | — | WORKING | — | 09_va:* | LOW | — |
| φ | `\phi` | Scalar/mediator | Scalar field or mediator | varies | — | WORKING | — | ch11_*:* | LOW | Context-dependent |
| J^A | `J^A` | 5D current | Energy-momentum current | 5D bulk | — | CANON | Fwk v2.0 Def.3.2 | — | NONE | — |
| J^ν_{b→b} | `\Jbb{\nu}` | Bulk-brane flux | Energy current from bulk to brane | brane | — | CANON-PRIMARY | Fwk v2.0 Rmk.4.5 | — | NONE | >0 = INFLOW |

---

## Part VI: Y-Junction and Z6 Program

| Symbol | LaTeX | Name | Meaning | Domain | Units | Canon | Canon Anchor | Book2 Anchor | Risk | Resolution |
|--------|-------|------|---------|--------|-------|-------|--------------|--------------|------|------------|
| θ | `\theta` | Angular position | Position on Z6 ring | Z6 | rad | CANON | Fwk v2.0 §10.2 | — | NONE | — |
| q | `q` | Asymmetry param | Junction asymmetry parameter | Z6 | — | CANON | Fwk v2.0 Def.10.1 | — | NONE | — |
| Z₆ | `Z_6` or `\mathbb{Z}_6` | Z6 group | Y-junction discrete symmetry = Z₃ × Z₂ | Z6 | — | CANON | Fwk v2.0 §9, 5 anchors | 05_three_gen:* | NONE | — |
| Z₃ | `Z_3` or `\mathbb{Z}_3` | Generation group | Three-generation subgroup | Z6 | — | CANON | Fwk v2.0 §9 | — | NONE | — |
| Z₂ | `Z_2` or `\mathbb{Z}_2` | Matter/antimatter | Matter-antimatter subgroup | Z6 | — | CANON | Fwk v2.0 §9 | — | NONE | — |
| V₀ | `V_0` | Well depth | Z6-symmetric potential minimum | Z6 | MeV | CANON | Fwk v2.0 §9.3 | — | NONE | — |
| V₃ | `V_3` | Flavor breaking | Flavor-breaking potential term | Z6 | MeV | CANON | Fwk v2.0 §9.3 | — | NONE | — |
| W | `W` | Winding number | Topological winding on S¹_ξ | topology | — | CANON | Fwk v2.0 Def.3.1 | — | NONE | — |

---

## Part VII: Actions

| Symbol | LaTeX | Name | Meaning | Domain | Units | Canon | Canon Anchor | Book2 Anchor | Risk | Resolution |
|--------|-------|------|---------|--------|-------|-------|--------------|--------------|------|------------|
| S_tot | `S_{\mathrm{tot}}` | Total action | Complete EDC action | action | — | CANON | Fwk v2.0 Eq.(8) | — | NONE | — |
| S_bulk | `S_{\mathrm{bulk}}` | Bulk action | 5D Einstein-Hilbert + matter | action | — | CANON | Fwk v2.0 Eq.(9) | — | NONE | — |
| S_brane | `S_{\mathrm{brane}}` | Brane action | Nambu-Goto membrane action | action | — | CANON | Fwk v2.0 Eq.(10) | — | NONE | — |
| S_defect | `S_{\mathrm{defect}}` | Defect action | Topological defect contribution | action | — | CANON | Fwk v2.0 §2.4 | — | NONE | — |
| S_GHY | `S_{\mathrm{GHY}}` | GHY term | Gibbons-Hawking-York boundary | action | — | WORKING | — | ch14:305 | LOW | — |

---

## Part VIII: Canonical Formulas (Reference)

| Formula | LaTeX | Canon Source | Status |
|---------|-------|--------------|--------|
| m_p/m_e = 6π⁵ | `m_p/m_e = 6\pi^5` | Fwk v2.0 Thm.5.3 | [Der] |
| α = (4π + 5/6)/(6π⁵) | `\alpha = (4\pi + 5/6)/(6\pi^5)` | Fwk v2.0 Thm.6.1 | [Der] |
| Δm_np = 8m_e/π | `\Delta m_{np} = 8m_e/\pi` | Fwk v2.0 §10.5 | [Der] |
| M⁵ = M⁴ × S¹_ξ | `\mathcal{M}^5 = \mathcal{M}^4 \times S^1_\xi` | Fwk v2.0 Eq.(1) | [P] |
| σ = m_e³c⁴/(α³ℏ²) | `\sigma = m_e^3 c^4 / (\alpha^3 \hbar^2)` | Fwk v2.0 §3.1 | [Dc] |

---

## Appendix A: Tier-1 Symbol Checklist

These symbols MUST have canon anchors:

| Symbol | Canon Anchored | Book2 Present | Status |
|--------|----------------|---------------|--------|
| ξ | ✅ Fwk v2.0 Eq.(3), 12 anchors | ✅ 910 uses | OK |
| R_ξ | ✅ Fwk v2.0 Def.1.1, 12 anchors | ✅ 382 uses | OK |
| σ | ✅ Fwk v2.0 Eq.(10), 31 anchors | ✅ present | OK |
| η | ✅ Fwk v2.0 §3.2, 1 anchor | ✅ present | OK |
| M⁵ | ✅ Fwk v2.0 Eq.(1), 18 anchors | ✅ present | OK |
| Σ³ | ✅ Fwk v2.0 Eq.(2), 7 anchors | ✅ 5 uses | OK |
| M_{5,Pl} | ✅ Fwk v2.0 §2.2 | ✅ ch14:* | OK |
| z₁, z₂ | ✅ Fwk v2.0 §11, 2 anchors | — | OK (Z6 only) |
| P_bulk | — | — | NEEDS CANON ANCHOR |
| J^ν_{b→b} | ✅ Fwk v2.0 Rmk.4.5 | — | OK |

---

## Appendix B: Extraction Statistics

**Run Date**: 2026-01-24
**Book2 Files Scanned**: 75
**Canon Sources Processed**: 12

**Tier-1 Coverage**: 9/10 (P_bulk needs anchor)
**Total Unique Symbols**: 47
**Violations Found After Remediation**: 0
**Ambiguities Requiring Human Decision**: 3

---

## Version History

| Date | Change | By |
|------|--------|-----|
| 2026-01-24 | Initial creation — comprehensive cross-document extraction | Claude |
| 2026-01-24 | Added ξ_GL for GL coherence length (CTX-001 resolution) | Claude |

---

*This table is authoritative. No notation changes without updating GLOBAL_SYMBOL_TABLE + collision report + chapter anchors.*
