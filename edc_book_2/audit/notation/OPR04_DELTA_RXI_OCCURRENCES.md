# OPR-04: δ and R_ξ Occurrences in Book 2

**OPR**: OPR-04 (δ ≡ R_ξ teleport)
**Date**: 2026-01-25
**Branch**: book2-opr04-delta-equals-Rxi-v1

---

## Summary

This document catalogs all occurrences of the brane thickness δ and diffusion scale R_ξ
in Book 2, including the critical identification δ = R_ξ that is required for Robin
parameter derivation (OPR-02).

**Key finding**: Book 2 already contains comprehensive audits of δ = R_ξ identification
in three subsections:
- §13.2.8 (Attempt H): First introduces δ = R_ξ as [Def]
- §13.2.10 (Attempt H2-plus): Stricter audit → concludes [P]
- §13.2.11 (Attempt H2 Hard): Rigorous provenance check

---

## Symbol Collision Warning

**δ has two distinct meanings in Book 2:**

| Symbol | Context | Meaning | First Appearance |
|--------|---------|---------|-----------------|
| δ | Brane physics | Boundary layer / brane thickness | CH10:104 |
| δ | CKM/PMNS | CP-violating phase | CH05 (flavor section) |

**Disambiguation**: In all OPR-20/Robin BC contexts, δ refers to brane thickness.
The CP phase δ appears only in flavor physics sections.

---

## R_ξ Occurrences

### Canonical Definition (Part I / Framework v2.0)

| Label | Location | Statement | Status |
|-------|----------|-----------|--------|
| eq:attemptH_Rxi_correlation | ch11_attemptH:105-108 | ⟨φ(x)φ(x')⟩ ~ exp(-\|x-x'\|/R_ξ) | [Dc] |
| (symbol table) | main:789 | R_ξ = Membrane thickness ~ 10⁻³ fm | [P]+[BL] |

### Interpretations (Chapter 13)

| Label | Location | Interpretation | Status |
|-------|----------|----------------|--------|
| eq:ch11_A1_radius | ch11_attemptD:89 | R_ξ as S¹ radius | [I] |
| eq:ch11_A2_numeric | ch11_attemptD:91 | 2πR_ξ as circumference | [I] |
| eq:ch11_A3_diffusion | ch11_attemptD:92 | R_ξ as diffusion length | [Dc] |

### Derived Relations

| Label | Location | Relation | Status |
|-------|----------|----------|--------|
| eq:ch11_ell_Rxi | ch11:243 | ℓ = 2πR_ξ | [Dc]+[I] |
| eq:ch11_E_ell_derivation | ch11_attemptE:111 | ℓ = 2π√2 R_ξ | [Dc]+[P] |

### Numerical Value

| Source | Value | Derivation | Status |
|--------|-------|------------|--------|
| Part I definition | R_ξ ~ 10⁻³ fm | Diffusion physics | [P] |
| M_Z constraint | R_ξ = ℏc/M_Z | Phenomenological | [BL]+[I] |
| Weak scale match | 2.17×10⁻³ fm | From M_Z = 91.2 GeV | [BL] |

**Critical note**: The numerical value of R_ξ is anchored to M_Z (electroweak observable).
This makes R_ξ value [BL], not purely [Dc].

---

## δ (Brane Thickness) Occurrences

### First Appearance

| Location | Context | Notes |
|----------|---------|-------|
| CH10:104 | Electroweak bridge | Teleported without prior definition |
| ch11_gf_full_closure_plan:240 | "ℓ ~ 1/M_W ~ 0.01 fm (brane thickness)" | Conflates ℓ and δ |

### Formal Definitions

| Label | Location | Definition | Status |
|-------|----------|------------|--------|
| eq:attemptH_alpha_ell_delta | ch11_attemptH:88-91 | α = c_geom · ℓ/δ | [Dc] |
| eq:attemptH_alpha_dimensional | ch11_attemptH:81-83 | α_phys ~ c_geom/δ | [Dc] |

### Physical Meaning

From ch11_opr20_attemptH_delta_equals_Rxi.tex:
- **δ (boundary layer)**: Thickness over which the Robin BC "smooths out" a sharp junction
- Fields relax from bulk to brane behavior over this scale
- Characteristic scale for field transition zone

---

## δ = R_ξ Identification

### Canonical Statement

| Label | Location | Form | Status |
|-------|----------|------|--------|
| eq:attemptH_delta_Rxi | ch11_attemptH:152 | δ = R_ξ (boxed) | [Def]→[P] |

### Evolution of Epistemic Status

| Attempt | Status | Reasoning |
|---------|--------|-----------|
| H (§13.2.8) | [Def] | "Definitional identification based on physical criterion" |
| H2-plus (§13.2.10) | [P] | R_ξ value uses M_Z → chain inherits [P] |
| H2 Hard (§13.2.11) | [P] | Neither route can derive δ = R_ξ from action |

**Final verdict (Book 2)**: δ = R_ξ is **[P]** (postulated), not [Dc] or [Der].

---

## Consequence: α = 2π

When δ = R_ξ is assumed:

| Label | Location | Derivation | Status |
|-------|----------|------------|--------|
| eq:attemptH_alpha_2pi | ch11_attemptH:178-180 | α = ℓ/δ = 2πR_ξ/R_ξ = 2π | [Dc]+[P] |

Status is [Dc]+[P] because:
- [Dc]: The ratio ℓ/δ formula is derived from thick-brane matching
- [P]: The identification δ = R_ξ is postulated

---

## Files Referenced

```
src/sections/ch10_electroweak_bridge.tex           (first δ use)
src/sections/ch11_opr20_attemptH_delta_equals_Rxi.tex  (δ = R_ξ introduced)
src/sections/ch11_opr20_attemptH2plus_delta_Rxi_stricter_audit.tex (strict audit)
src/sections/ch11_opr20_attemptH2_delta_Rxi_hard_audit.tex (hard mode)
src/sections/ch11_opr20_attemptD_interpretation_robin_overcount.tex (R_ξ interpretations)
src/sections/ch11_opr20_attemptE_ell_derivation.tex (ℓ = 2πR_ξ)
src/EDC_Part_II_Weak_Sector_rebuild.tex (symbol table)
```

---

## OPR-04 Crosswalk

| Occurrence | Blocks OPR-04? | Why |
|------------|----------------|-----|
| R_ξ ~ 10⁻³ fm value | YES | Anchored to M_Z ([BL]), not derived |
| R_ξ definition | NO | Formal definition exists [Dc] |
| δ definition | PARTIAL | Definition exists but first use is teleported |
| δ = R_ξ identification | YES | Physical criterion not sufficient for [Dc] |
| α = 2π consequence | YES | Blocked by δ = R_ξ status |

---

*OPR-04 Occurrence Audit Complete*
*Status: OPEN — δ = R_ξ remains [P]*
