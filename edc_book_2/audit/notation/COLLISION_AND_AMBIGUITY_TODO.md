# Symbol Collision and Ambiguity TODO

Generated: 2026-01-24
Status: OPEN (61 violations, 20 items needing review)

This document tracks symbol usage issues that require manual remediation.

## Summary

| Category | Count | Status |
|----------|-------|--------|
| M5/M_5 instead of \mathcal{M}^5 | 22 | TODO |
| z/Δz used as 5D depth | 39 | TODO |
| Needs manual review | 20 | TODO |

---

## HIGH PRIORITY: M5/M_5 → \mathcal{M}^5

These use `M5` or `M_5` to refer to the 5D manifold. Canon requires `\mathcal{M}^5`.

**Reason**: `M_5` looks like mass times 5, causing confusion. Canon uses calligraphic M.

### Files Affected:

| TODO ID | File | Lines | Context | Recommended Fix |
|---------|------|-------|---------|-----------------|
| TODO-M5-001 | 02_frozen_regime_foundations.tex | 133 | Paper 2 reference | Review context |
| TODO-M5-002 | 05_three_generations.tex | 334,339,341,369,370,378,385,402,501,605 | π₁(M₅) topology | Replace all M_5 with \mathcal{M}^5 |
| TODO-M5-003 | 11_gf_derivation.tex | 404,406 | G₅ ~ g₅²/M₅² | Replace M_5 with \mathcal{M}^5 or define M_5 as Planck mass |
| TODO-M5-004 | ch11_opr20_attemptD_interpretation_robin_overcount.tex | 248,259,261 | M₅ Planck mass | Disambiguate: use M_{5,\text{Pl}} for Planck mass |
| TODO-M5-005 | ch14_bvp_closure_pack.tex | 276,280,297,305 | M₅ Planck mass | Disambiguate: use M_{5,\text{Pl}} for Planck mass |

### Closure Criterion:
- All M5/M_5 replaced with \mathcal{M}^5 when referring to manifold
- If M_5 means 5D Planck mass, use explicit `M_{5,\mathrm{Pl}}` or `M_{(5)}^{\mathrm{Pl}}`
- Gate passes with zero M5/M_5 violations

---

## HIGH PRIORITY: z/Δz → ξ/Δξ for 5D Depth

These use `z` or `Δz` for the 5D compact coordinate. Canon requires `ξ`.

**Reason**: Canon Framework v2.0 Eq.(3) defines ξ as the compact 5D coordinate.

### Files Affected:

| TODO ID | File | Line Range | Pattern | Context | Risk |
|---------|------|------------|---------|---------|------|
| TODO-Z5D-001 | 06_neutrinos_edge_modes.tex | 70-757 | Δz | Neutrino mass from 5D separation | HIGH |
| TODO-Z5D-002 | 07_ckm_cp.tex | 66-1047 | Δz | CKM from generation separation | HIGH |
| TODO-Z5D-003 | 09_va_structure.tex | 275-1079 | (x^μ,z), f(z) | V-A structure from 5D profiles | HIGH |
| TODO-Z5D-004 | ch11_opr20_attemptF_mediator_bvp_junction.tex | 23-24 | φ(x^μ,z) | Mediator in 5D | MED |
| TODO-Z5D-005 | ch14_bvp_closure_pack.tex | 331+ | V(z), f(z) | BVP profiles | MED |

### Recommended Remediation:

For each file:
1. **Check physical context**: Is this truly the 5D compact dimension?
2. **If yes**: Replace z → ξ, Δz → Δξ, z_H → ξ_H, etc.
3. **If uncertain**: Add to NEEDS_REVIEW list with rationale
4. **Document each change** in REPLACEMENT_RISK_LEDGER.md

### Closure Criterion:
- All 5D depth usages of z replaced with ξ
- Each replacement documented with canon anchor
- Gate passes with zero z-as-5D violations

---

## MEDIUM PRIORITY: Needs Manual Review

These occurrences are ambiguous and require human judgment.

| File | Line | Pattern | Question |
|------|------|---------|----------|
| 06_neutrinos_edge_modes.tex | 442 | f_e(z) | Profile function — is z spatial or 5D? |
| 07_ckm_cp.tex | 462 | f_j(z) | Generation profile — likely 5D |
| 09_va_structure.tex | 250 | f_{L/R}(z) | Chiral profile — likely 5D |
| ch12_bvp_workpackage.tex | 222 | f_n(z) = sin(nπz/ℓ) | Mode function — check if z is 5D |
| ch14_bvp_closure_pack.tex | 331 | V(ξ) = V_warp(z) | MIXED notation: V(ξ) but V_warp(z) |

### Review Protocol:
1. Read surrounding context (±10 lines)
2. Identify if "z" is:
   - CLASS_5D_DEPTH → needs ξ replacement
   - CLASS_3D_Z → OK as-is
   - CLASS_DUMMY → OK if documented
3. Add classification to this file
4. If 5D, add to remediation TODO

---

## Policy Reminder

Per CLAUDE.md and canon policy:
- **NO blind grep/replace**: Every symbol change requires context classification
- **Document all changes**: Use REPLACEMENT_RISK_LEDGER.md
- **Canon is law**: Framework v2.0 definitions are authoritative
- **When uncertain**: Create TODO, don't guess

---

## Completion Checklist

- [ ] All M5/M_5 instances resolved
- [ ] All z-as-5D instances resolved
- [ ] All NEEDS_REVIEW items classified
- [ ] REPLACEMENT_RISK_LEDGER.md complete
- [ ] Symbol audit gate PASS
- [ ] Build gate PASS (387 pages)

---

## Version History

| Date | Change | By |
|------|--------|-----|
| 2026-01-24 | Initial creation from symbol audit | Claude |
