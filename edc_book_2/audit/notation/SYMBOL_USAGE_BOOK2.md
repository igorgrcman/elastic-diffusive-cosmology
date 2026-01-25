# Symbol Usage Summary — Book 2

Generated: 2026-01-24
Source: Symbol audit of 55 .tex files in edc_book_2/src/sections/
Authority: Framework v2.0 (DOI: 10.5281/zenodo.18299085)

## Summary Statistics

| Category | Count | Status |
|----------|-------|--------|
| Files scanned | 55 | — |
| Total findings | 81 | — |
| VIOLATIONS | 61 | TODO |
| NEEDS_REVIEW | 20 | TODO |
| OK | 0 | — |

**Gate status**: FAIL (61 violations)

---

## Per-Symbol Usage Report

### ξ (5D compact coordinate) — CANONICAL

| Status | Count | Files |
|--------|-------|-------|
| Correct usage | many | Throughout Book 2 |
| Collision (coherence) | rare | See Paper 2 legacy |

**Canon**: Framework v2.0 Eq.(3) — ξ ∈ [0, 2πR_ξ)

**Note**: Some chapters correctly use ξ. The violations are where z is used instead.

---

### z (3D spatial OR violation)

| Classification | Count | Key Files |
|----------------|-------|-----------|
| CLASS_VIOLATION_Z_AS_5D | 39 | 06, 07, 09, ch11, ch14 |
| CLASS_3D_Z | 0 | (none detected by audit) |
| NEEDS_REVIEW | ~20 | Various |

**Violation patterns detected**:
- `Δz` for 5D separation: 06_neutrinos, 07_ckm
- `(x^μ, z)` coordinate tuple: 09_va_structure
- `f(z)` profile functions: Multiple chapters
- `φ(x^μ, z)` field arguments: ch11_attemptF

**Canon rule**: z is ONLY for 3D spatial. 5D depth MUST use ξ.

---

### M_5 / M5 (manifold violation)

| Classification | Count | Key Files |
|----------------|-------|-----------|
| CLASS_VIOLATION_MANIFOLD | 22 | 05, 11, ch11, ch14 |
| NEEDS_DISAMBIGUATION | ~5 | May be Planck mass |

**Files affected**:
- `05_three_generations.tex`: 10 occurrences (topology context)
- `11_gf_derivation.tex`: 2 occurrences (mass scale context)
- `ch11_opr20_attemptD*.tex`: 3 occurrences (Planck mass)
- `ch14_bvp_closure_pack.tex`: 4 occurrences (Planck mass)

**Canon rule**:
- Manifold → `\mathcal{M}^5`
- 5D Planck mass → `M_{5,\mathrm{Pl}}`

---

### R_ξ (compactification radius) — CANONICAL

| Status | Usage |
|--------|-------|
| Correct | Most chapters |

**Canon**: Framework v2.0 Def.1.1 — R_ξ ~ 10⁻¹⁸ m

---

### Σ³ (3D brane) — CANONICAL

| Status | Usage |
|--------|-------|
| Correct | Most chapters |

**Canon**: Framework v2.0 Eq.(2)

---

### z₁, z₂ (Z6 complex variables) — CANONICAL

| Status | Usage |
|--------|-------|
| Correct | Used in Z6 symmetry contexts |

**Canon**: Framework v2.0 §11

**Note**: These are NOT coordinates. Do not confuse with z-as-5D-depth violations.

---

## Files by Violation Count

| File | M_5 Violations | z-as-5D Violations | Needs Review |
|------|----------------|-------------------|--------------|
| 05_three_generations.tex | 10 | 0 | 0 |
| 06_neutrinos_edge_modes.tex | 0 | ~8 | 2 |
| 07_ckm_cp.tex | 0 | ~10 | 2 |
| 09_va_structure.tex | 0 | ~15 | 5 |
| 11_gf_derivation.tex | 2 | 0 | 0 |
| ch11_opr20_attemptD*.tex | 3 | 0 | 0 |
| ch11_opr20_attemptF*.tex | 0 | 2 | 0 |
| ch12_bvp_workpackage.tex | 0 | 0 | 1 |
| ch14_bvp_closure_pack.tex | 4 | 2 | 3 |

---

## Remediation Priority

### Priority 1: Unambiguous M_5 → \mathcal{M}^5

Files: `05_three_generations.tex`

All 10 occurrences are in topology context (π₁(M_5)). Clear violation.

### Priority 2: Disambiguate M_5 as Planck mass

Files: `11_gf_derivation.tex`, `ch11_opr20_attemptD*.tex`, `ch14_bvp_closure_pack.tex`

~7 occurrences where M_5 appears in mass formulas. Should become M_{5,Pl}.

### Priority 3: z → ξ for 5D depth

Files: `06_neutrinos_edge_modes.tex`, `07_ckm_cp.tex`, `09_va_structure.tex`

~33 occurrences. Requires case-by-case context check.

### Priority 4: Manual review

Files: Various

~20 occurrences with ambiguous context.

---

## Gate Definition

**Symbol audit gate PASSES when**:
1. Zero M5/M_5 violations (all replaced with \mathcal{M}^5 or M_{5,Pl})
2. Zero z-as-5D violations (all replaced with ξ)
3. All NEEDS_REVIEW items classified
4. REPLACEMENT_RISK_LEDGER.md complete
5. Build gate PASS (387 pages)

---

## Version History

| Date | Change | By |
|------|--------|-----|
| 2026-01-24 | Initial creation from symbol audit | Claude |

