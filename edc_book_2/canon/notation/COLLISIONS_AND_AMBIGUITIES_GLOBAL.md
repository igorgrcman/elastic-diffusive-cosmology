# COLLISIONS AND AMBIGUITIES — Global Report

**Generated**: 2026-01-24
**Status**: POST-REMEDIATION (Phase D complete)
**Git Branch**: book2-global-symbol-table-v1

This document tracks all symbol collisions and ambiguities across:
- Canon sources (Book Part I, Paper 2, Framework v2.0, Companions A–H)
- Book 2 working files (edc_book_2/src/)

---

## Summary

| Category | Count | Status |
|----------|-------|--------|
| **RESOLVED Collisions** | 2 | ✅ Fixed |
| **Remaining Ambiguities** | 3 | NEEDS HUMAN DECISION |
| **Context-Sensitive Symbols** | 2 | Classified (z, η) |

---

## RESOLVED COLLISIONS

### COLLISION-001: M_5 (Manifold vs Mass)

**Status**: ✅ RESOLVED

| Context | Old Symbol | Correct Symbol | Resolution |
|---------|------------|----------------|------------|
| Topology (π₁, homotopy) | M_5 | `\mathcal{M}^5` | Manifold context |
| Mass scale (G_F derivation) | M_5 | `M_{5,\mathrm{Pl}}` | Planck mass context |
| Einstein-Hilbert action | M_5³ | `M_{5,\mathrm{Pl}}^3` | Planck mass context |

**Files Remediated**:
- 05_three_generations.tex: M_5 → `\mathcal{M}^5` (10 occurrences)
- 11_gf_derivation.tex: M_5 → `M_{5,\mathrm{Pl}}` (2 occurrences)
- ch11_opr20_attemptD*.tex: M_5 → `M_{5,\mathrm{Pl}}` (3 occurrences)
- ch14_bvp_closure_pack.tex: M_5 → `M_{5,\mathrm{Pl}}` (4 occurrences)

**Canon Rule**: Framework v2.0 uses `\mathcal{M}^5` for manifold, `M_{5,Pl}` for mass.

---

### COLLISION-002: z (3D vs 5D vs Z6 Complex)

**Status**: ✅ RESOLVED for 5D depth cases

| Context | Old Symbol | Correct Symbol | Files |
|---------|------------|----------------|-------|
| 5D coordinate tuple | (x^μ, z) | (x^μ, ξ) | 09_va_structure.tex |
| 5D field argument | φ(x, z) | φ(x, ξ) | ch11_opr20_attemptF*.tex |
| 5D separation | Δz | Δξ | 06_neutrinos, 07_ckm |
| 5D horizon | z_H | ξ_H | 06_neutrinos |
| Generation position | z_i | ξ_i | 07_ckm_cp |
| 5D profile | f(z) | f(ξ) | Multiple files |

**NOT Changed (Correctly Preserved)**:
- 3D spatial: (x, y, z) — Remains z
- Z6 complex roots: z₁, z₂ — Remains z₁, z₂

**Canon Rule**: Framework v2.0 Eq.(3) defines ξ as the 5D compact coordinate.

---

## REMAINING AMBIGUITIES

### AMBIGUITY-001: η (Metric vs Bulk Viscosity)

**Status**: 🟡 NEEDS HUMAN DECISION

**Issue**: Symbol η appears in two contexts:
1. **Metric signature**: η_μν = diag(-1, +1, +1, +1) in 4D
2. **Bulk viscosity**: η_bulk in 5D fluid dynamics

**Canon Anchors**:
- Fwk v2.0 §3.2: "bulk viscosity η"
- Standard physics: Minkowski metric η_μν

**Proposal**:
- Use `\eta` for bulk viscosity (EDC-specific)
- Use `\eta_{\mu\nu}` explicitly for metric (with subscripts)
- Book 2 should clarify in context

**Decision Required**: Igor to confirm notation split.

---

### AMBIGUITY-002: κ (Penetration Depth vs Curvature)

**Status**: 🟡 NEEDS CANON ANCHOR

**Issue**: Symbol κ used in Book 2 for inverse penetration depth, but also appears in GR as:
- Extrinsic curvature trace K
- Surface gravity κ (black holes)
- Einstein κ = 8πG/c⁴

**Book 2 Usage** (Working):
- 06_neutrinos_edge_modes.tex: κ as localization scale
- BVP chapters: κ as inverse length

**Proposal**:
- Keep κ for EDC penetration scale (context-specific)
- Add to Framework v3.0 as canonical if retained

**Decision Required**: Confirm κ definition for EDC or choose alternative symbol.

---

### AMBIGUITY-003: P_bulk (Bulk Pressure)

**Status**: 🟡 NEEDS CANON ANCHOR

**Issue**: Symbol P_bulk or P_{\mathrm{bulk}} used conceptually but no explicit canon anchor found in extraction.

**Expected Definition**: Pressure in the 5D bulk (Plenum fluid)

**Proposal**:
- Add explicit definition to Framework v3.0
- For now, mark as WORKING in Book 2

**Decision Required**: Confirm P_bulk definition and add canon anchor.

---

## CONTEXT-SENSITIVE SYMBOLS

### z — Full Classification

| Pattern | Context | Correct Usage | Book 2 Status |
|---------|---------|---------------|---------------|
| (x, y, z) | 3D Cartesian | z | ✅ OK |
| (x^μ, z) | 5D tuple | ξ | ✅ Remediated |
| φ(x, z) | 5D field | ξ | ✅ Remediated |
| Δz | 5D separation | Δξ | ✅ Remediated |
| z_H | 5D boundary | ξ_H | ✅ Remediated |
| z_i (generation) | 5D position | ξ_i | ✅ Remediated |
| z₁, z₂ | Z6 complex | z₁, z₂ | ✅ Preserved |
| ∫...dz | 5D integral | ∫...dξ | ✅ Remediated |
| z (code output) | Plot axis | z or ξ | ⚠️ Check context |

### η — Classification

| Pattern | Context | Usage | Status |
|---------|---------|-------|--------|
| η_μν | Minkowski metric | η_μν | OK (with subscript) |
| η | Bulk viscosity | η | OK (EDC context) |
| η_bulk | Explicit bulk | η_bulk | OK (explicit) |

---

## NOTATION DRIFT DETECTED

### Same Meaning, Different Symbols

| Meaning | Symbol A | Symbol B | Resolution |
|---------|----------|----------|------------|
| 5D coordinate | z (old) | ξ (canon) | Use ξ |
| 5D Planck mass | M_5 | M_{5,Pl} | Use M_{5,Pl} |
| 5D manifold | M_5, M^5 | \mathcal{M}^5 | Use \mathcal{M}^5 |
| Compactification radius | R_z (forbidden) | R_ξ | Use R_ξ |

All drift cases resolved in Phase D remediation.

---

## ACTION ITEMS

| ID | Item | Owner | Status |
|----|------|-------|--------|
| AMB-001 | Decide η notation split | Igor | PENDING |
| AMB-002 | Confirm κ as EDC symbol | Igor | PENDING |
| AMB-003 | Add P_bulk canon anchor | Future Fwk | PENDING |
| DRIFT-ALL | Remediate notation drift | Claude | ✅ DONE |

---

## Change Log

| Date | Change | Commit |
|------|--------|--------|
| 2026-01-24 | Initial creation from extraction | — |
| 2026-01-24 | Phase D remediation completed | 7014cbd, ed8006f, cbbba70 |

---

*This report must be updated whenever new collisions or ambiguities are discovered.*
