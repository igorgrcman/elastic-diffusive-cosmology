# Chapter Variable Context Ledger

Generated: 2026-01-24
Purpose: Per-chapter variable classification for context-aware symbol remediation
Status: OPEN — tracks symbol context for each chapter

## Overview

This ledger documents variable usage context per chapter. Each entry classifies
how symbols are used to prevent blind grep/replace accidents.

---

## Chapter Variable Cards

### CH-05: Three Generations (`05_three_generations.tex`)

**Status**: HAS VIOLATIONS (M_5 pattern)

| Variable | Classification | Context | Remediation |
|----------|---------------|---------|-------------|
| M_5 | CLASS_VIOLATION_MANIFOLD | π₁(M₅) homotopy, topological | Replace with \mathcal{M}^5 |
| ξ | CLASS_5D_DEPTH | Compact coordinate | OK (canonical) |
| θ | CLASS_ANGLE | Angular position | OK |
| z₁, z₂ | CLASS_Z6 | Z6 complex variables | OK (not coordinates) |

**Lines with violations**: 334, 339, 341, 369, 370, 378, 385, 402, 501, 605

**Recommended fix**: Global replace M_5 → \mathcal{M}^5 in topology context.

---

### CH-06: Neutrinos and Edge Modes (`06_neutrinos_edge_modes.tex`)

**Status**: HAS VIOLATIONS (Δz as 5D separation)

| Variable | Classification | Context | Remediation |
|----------|---------------|---------|-------------|
| Δz | CLASS_VIOLATION_Z_AS_5D | Neutrino mass from 5D separation | Replace with Δξ |
| z | NEEDS_REVIEW | Profile function f(z) | Check if 5D depth |
| f_e(z) | NEEDS_REVIEW | Electron profile | Likely 5D → f_e(ξ) |
| ξ | CLASS_5D_DEPTH | Some correct usages | Keep |

**Violation range**: Lines 70-757

**Context snippet**: "The neutrino mass arises from the separation Δz between..."

**Recommended fix**: Replace Δz → Δξ where it represents 5D separation.
Document each replacement with physical rationale.

---

### CH-07: CKM and CP (`07_ckm_cp.tex`)

**Status**: HAS VIOLATIONS (Δz as generation separation)

| Variable | Classification | Context | Remediation |
|----------|---------------|---------|-------------|
| Δz | CLASS_VIOLATION_Z_AS_5D | Generation separation in 5D | Replace with Δξ |
| f_j(z) | NEEDS_REVIEW | Generation profile | Likely 5D → f_j(ξ) |
| z | NEEDS_REVIEW | Multiple contexts | Case-by-case |
| δ | CLASS_CP_PHASE | CP violation phase | OK |

**Violation range**: Lines 66-1047

**Context snippet**: "The CKM hierarchy arises from generation localization Δz..."

**Recommended fix**: Replace Δz → Δξ for 5D generation separation.
Keep z for Z6 program contexts if subscripted as z₁, z₂.

---

### CH-09: V-A Structure (`09_va_structure.tex`)

**Status**: HAS VIOLATIONS ((x^μ, z) coordinate tuples)

| Variable | Classification | Context | Remediation |
|----------|---------------|---------|-------------|
| (x^μ, z) | CLASS_VIOLATION_Z_AS_5D | 5D coordinate tuple | Replace with (x^μ, ξ) |
| f(z) | CLASS_VIOLATION_Z_AS_5D | Profile in 5D | Replace with f(ξ) |
| f_{L/R}(z) | CLASS_VIOLATION_Z_AS_5D | Chiral profiles | Replace with f_{L/R}(ξ) |
| z | CLASS_VIOLATION_Z_AS_5D | Used as 5D depth | Replace with ξ |

**Violation range**: Lines 275-1079

**Context snippet**: "The field φ(x^μ, z) has profiles f_L(z) and f_R(z) that..."

**Recommended fix**: Systematic z → ξ replacement for all 5D usages.
This chapter has extensive z-as-5D-depth patterns.

---

### CH-11: G_F Derivation (`11_gf_derivation.tex`)

**Status**: HAS VIOLATIONS (M_5 as mass scale)

| Variable | Classification | Context | Remediation |
|----------|---------------|---------|-------------|
| M_5 | NEEDS_DISAMBIGUATION | G₅ ~ g₅²/M₅² | Could be Planck mass M_{5,Pl} |
| G_5 | CLASS_5D_COUPLING | 5D Newton constant | OK |
| g_5 | CLASS_5D_COUPLING | 5D gauge coupling | OK |
| ξ | CLASS_5D_DEPTH | 5D coordinate | OK |

**Lines with violations**: 404, 406

**Context snippet**: "G_5 ~ g_5^2/M_5^2 where M_5 is the..."

**Disambiguation needed**:
- If M_5 = 5D Planck mass → use M_{5,\mathrm{Pl}}
- If M_5 = manifold → use \mathcal{M}^5
Check physical meaning before changing.

---

### CH-11 Attempt D: Robin/Overcount (`ch11_opr20_attemptD_interpretation_robin_overcount.tex`)

**Status**: HAS VIOLATIONS (M_5 as Planck mass)

| Variable | Classification | Context | Remediation |
|----------|---------------|---------|-------------|
| M_5 | CLASS_PLANCK_MASS_5D | "M₅ Planck mass" | Replace with M_{5,\mathrm{Pl}} |
| R_ξ | CLASS_5D_RADIUS | Compactification radius | OK (canonical) |

**Lines with violations**: 248, 259, 261

**Recommended fix**: Use M_{5,\mathrm{Pl}} to distinguish from manifold \mathcal{M}^5.

---

### CH-11 Attempt F: Mediator BVP Junction (`ch11_opr20_attemptF_mediator_bvp_junction.tex`)

**Status**: HAS VIOLATIONS (φ(x^μ, z) pattern)

| Variable | Classification | Context | Remediation |
|----------|---------------|---------|-------------|
| φ(x^μ, z) | CLASS_VIOLATION_Z_AS_5D | Mediator field in 5D | Replace with φ(x^μ, ξ) |
| z | CLASS_VIOLATION_Z_AS_5D | 5D bulk coordinate | Replace with ξ |

**Lines with violations**: 23-24

**Recommended fix**: Replace z → ξ for 5D field arguments.

---

### CH-12: BVP Workpackage (`ch12_bvp_workpackage.tex`)

**Status**: NEEDS REVIEW

| Variable | Classification | Context | Remediation |
|----------|---------------|---------|-------------|
| f_n(z) = sin(nπz/ℓ) | NEEDS_REVIEW | Mode function | Check if z is 5D |
| z | NEEDS_REVIEW | May be dummy variable | Case-by-case |
| ℓ | CLASS_LENGTH_SCALE | Domain size | OK |

**Review needed**: Line 222 — determine if z is 5D coordinate or dummy variable.
Mode functions often use generic z for interval [0, ℓ].

---

### CH-14: BVP Closure Pack (`ch14_bvp_closure_pack.tex`)

**Status**: HAS VIOLATIONS (M_5 and mixed V(ξ)/V_warp(z))

| Variable | Classification | Context | Remediation |
|----------|---------------|---------|-------------|
| M_5 | CLASS_PLANCK_MASS_5D | Planck mass context | Replace with M_{5,\mathrm{Pl}} |
| V(ξ) | CLASS_5D_POTENTIAL | Correct notation | OK |
| V_warp(z) | CLASS_VIOLATION_Z_AS_5D | Warp potential | Replace with V_warp(ξ) |
| f(z) | NEEDS_REVIEW | Profile function | Check context |

**Lines with violations**: 276, 280, 297, 305, 331+

**CRITICAL**: Line 331 has MIXED notation: V(ξ) = V_warp(z)
This must be fixed to V(ξ) = V_warp(ξ) for consistency.

---

## Classification Reference

| Class | Meaning | Action |
|-------|---------|--------|
| CLASS_5D_DEPTH | Correct ξ usage for 5D coordinate | OK |
| CLASS_3D_Z | Correct z usage for 3D spatial | OK |
| CLASS_Z6 | z₁, z₂ for Z6 complex variables | OK |
| CLASS_ANGLE | θ, φ for angular variables | OK |
| CLASS_CP_PHASE | δ for CP phase | OK |
| CLASS_5D_COUPLING | G_5, g_5 for 5D couplings | OK |
| CLASS_5D_RADIUS | R_ξ for compactification radius | OK |
| CLASS_PLANCK_MASS_5D | M_{5,Pl} for 5D Planck mass | Use explicit notation |
| CLASS_VIOLATION_Z_AS_5D | z used as 5D depth | VIOLATION → replace with ξ |
| CLASS_VIOLATION_MANIFOLD | M5/M_5 for manifold | VIOLATION → use \mathcal{M}^5 |
| NEEDS_REVIEW | Ambiguous, requires human judgment | Document decision |
| NEEDS_DISAMBIGUATION | Multiple valid interpretations | Choose and document |

---

## Completion Checklist

For each chapter with violations:
- [ ] Read context ±10 lines for each flagged line
- [ ] Classify using table above
- [ ] Document classification in this ledger
- [ ] If VIOLATION: add to REPLACEMENT_RISK_LEDGER.md before changing
- [ ] If NEEDS_REVIEW: add decision rationale here
- [ ] Verify build after any changes

---

## Version History

| Date | Change | By |
|------|--------|-----|
| 2026-01-24 | Initial creation from symbol audit | Claude |

