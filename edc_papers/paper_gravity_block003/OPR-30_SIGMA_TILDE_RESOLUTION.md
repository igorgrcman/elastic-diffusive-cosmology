# OPR-30: σ̃ Definition Inconsistency — Resolution

## Version: 1.0
## Date: 2026-03-15
## Status: RESOLUTION DOCUMENT

---

## 1. Problem Statement

The symbol σ̃ (dimensionless brane tension) has been **redefined three times**
without acknowledgment across derivation versions v29–v67. This breaks the
derivation chain for the entire BLOCK-004 program (α₃, M_X, g_X, τ_p).

---

## 2. Four Incompatible Definitions Found

### DEF-A: v28–v29 (β only, no σ̃)

| Property | Value |
|----------|-------|
| **Symbol** | β (NOT σ̃ — σ̃ does not appear) |
| **Definition** | β ≡ σL²/M̄_Pl² |
| **First appearance** | v28 line 737 |
| **Boxed in** | v29 line 215 |
| **Numeric** | β = M_Z/(π M̄_Pl²) = 4.89 × 10⁻³⁶ |
| **Dimensions** | [M⁴·M⁻²/M²] = [M⁰] ✓ |
| **Status** | **CORRECT** |

### DEF-B: v48–v56 (first error)

| Property | Value |
|----------|-------|
| **Symbol** | σ̃ |
| **Definition** | σ̃ ≡ σ/M̄_Pl⁴ |
| **First appearance** | **v48 line 367** |
| **Reiterated** | v48 line 929, v56 line 544 |
| **Dimensions** | [M⁴/M⁴] = [M⁰] ✓ (if [σ]=M⁴) |
| **Numeric** | Not evaluated in text |
| **Status** | **PROBLEMATIC** — different quantity from β |

**Critical algebraic error in v56:**

v56 line 541 claims:
```
β = σ⁴/M̄_Pl⁴ = σ̃⁴
```

But σ̃ = σ/M̄_Pl⁴ implies σ̃⁴ = σ⁴/M̄_Pl¹⁶ ≠ σ⁴/M̄_Pl⁴.

The correct identity would be σ⁴/M̄_Pl⁴ = (σ/M̄_Pl)⁴, which requires
σ̃ = σ/M̄_Pl (not σ/M̄_Pl⁴). **Error: factor M̄_Pl¹² discrepancy.**

### DEF-C: v62–v66 (silent redefinition #1)

| Property | Value |
|----------|-------|
| **Symbol** | σ̃ |
| **Definition** | σ̃ ≡ σL²/M̄_Pl² (= β from DEF-A) |
| **First appearance** | v62 line 367 |
| **Boxed** | v62 line 814 |
| **Explicit equivalence** | v62 line 458: β = σ̃ |
| **Numeric** | ~10⁻³⁶ (same as β) |
| **Dimensions** | [M⁰] ✓ |
| **Status** | **SILENT REDEFINITION** from DEF-B |

**False provenance claim:** v62 line 1692 states "Using β = σ̃ (from v29)",
but v29 never defined σ̃. This retroactively attributes DEF-C to v29.

### DEF-D: v67 (silent redefinition #2)

| Property | Value |
|----------|-------|
| **Symbol** | σ̃ (macro \st) |
| **Definition** | σ̃ ≡ σ/T_* |
| **First appearance** | v67 line 185 |
| **Macro** | v67 line 48: \newcommand{\st}{\tilde{\sigma}} |
| **Numeric** | σ̃ ~ 100 (from α₃ = 1/σ̃ ≈ 0.01) |
| **Dimensions** | [M⁴/[T_*]] — depends on [T_*] |
| **Status** | **SILENT REDEFINITION** from DEF-C |

---

## 3. Chain of Inconsistency (Timeline)

```
v28 ─── β = σL²/M̄_Pl² introduced (line 737)
  │
v29 ─── β formalized, boxed (line 215). β = 4.89 × 10⁻³⁶. NO σ̃.
  │
v30 ─── Uses β from v29. No σ̃. No change.
  │
  ╳ ← FIRST ERROR HERE
  │
v48 ─── σ̃ = σ/M̄_Pl⁴ introduced (line 367). Different from β.
  │      Both β and σ̃ coexist as independent parameters.
  │
v56 ─── Inherits DEF-B. Derives β = σ̃⁴ (line 541, ALGEBRAIC ERROR).
  │      Boxed as consistency constraint (line 550).
  │
  ╳ ← SILENT REDEFINITION #1
  │
v62 ─── σ̃ changed to σL²/M̄_Pl² = β (line 367). Incompatible with v48/v56.
  │      Claims "from v29" (line 1692) — FALSE.
  │
v65 ─── Follows v62's DEF-C (line 501).
  │
  ╳ ← SILENT REDEFINITION #2
  │
v67 ─── σ̃ changed to σ/T_* (line 185). σ̃ ~ 100.
         Incompatible with ALL prior definitions.
```

---

## 4. Numeric Incompatibility

| Definition | σ̃ value | α₃ = 1/σ̃ | Physical? |
|-----------|---------|-----------|----------|
| DEF-A/C | ~10⁻³⁶ | ~10³⁶ | NO — α₃ > 1 is unphysical for coupling |
| DEF-B | ~10⁻⁵⁸ to 10⁻⁶⁸ | ~10⁵⁸ to 10⁶⁸ | NO — absurdly large |
| DEF-D | ~100 | ~0.01 | YES — reasonable strong coupling |

**Only DEF-D gives physically meaningful α₃.**

---

## 5. Resolution: Canonical Definition

### 5.1 Canonical σ̃

**[Dc]** The canonical definition of σ̃ is:

```
σ̃ ≡ σ / T_*                                          (OPR-30-CAN)
```

where:
- σ is the dimensional brane tension, [σ] = M⁴ (3-brane in 5D)
- T_* = C · M₅³ is the characteristic tension scale from 5D geometry
  (derived in TSTAR_DERIVATION_5D.md)
- C is a dimensionless O(1) geometric factor from Israel junction conditions

### 5.2 Justification

1. **Physical**: T_* is the natural scale of the 5D bulk-brane system.
   Normalizing σ by T_* measures brane tension in its own natural units.

2. **Dimensional**: [T_*] = [M₅³] = [M³].
   For [σ] = M⁴, we need T_* with [M⁴] as well.
   **Correction**: Under the convention [σ] = M⁴ (3-brane tension),
   T_* must also have [T_*] = M⁴, which means T_* = C · M₅⁴/Λ₅^{1/2}
   or another combination with the right dimension.
   Under [σ] = M³ (2-brane / EDC convention), T_* = C · M₅³ works.
   **The dimension convention for σ must be fixed first.**

3. **Numeric**: σ̃ ~ 100 gives α₃ ~ 0.01, physically reasonable.

4. **No back-calculation**: T_* must be derived from 5D geometry (forward),
   NOT from α₃ = 0.01 → σ̃ = 100 → T_* = σ/100 (backward).

### 5.3 Dimension Convention for σ

**[Dc]** In EDC, the brane is a **2-brane** (codimension-1 defect in 5D):

```
[σ_EDC] = [Energy]/[Area] = M · L⁻² = M³     (natural units)
```

This is consistent with:
- TSTAR_DEFINITION.md Section 2.1: [σ] = M³
- EDC Book I Chapter 7: σ ≈ 1.41 × 10¹⁸ J/m²
- The action S_brane = -σ ∫ d⁴x √{-g} being dimensionless

**The v48 convention [σ] = M⁴ is for a 3-brane tension (energy/volume),
which is appropriate in RS models but NOT in EDC where σ is energy/area.**

Under [σ] = M³:
- DEF-B: σ̃ = σ/M̄_Pl⁴ has [M³/M⁴] = [M⁻¹] — **dimensionally WRONG**
- DEF-A/C: β = σL²/M̄_Pl² has [M³·M⁻²/M²] = [M⁻¹] — **also wrong!**

**This means v29's β is ALSO dimensionally incorrect under EDC conventions.**

The resolution: β must be redefined as β = σL²/(M̄_Pl² · L) = σL/M̄_Pl²,
or the normalization must use a quantity with [M³].

### 5.4 Corrected Definitions (EDC Convention [σ] = M³)

**[Dc]** Under EDC's [σ] = M³:

```
T_* = C · M₅³                    [T_*] = M³ ✓
σ̃ = σ / T_*                      [σ̃] = M⁰ ✓     (OPR-30-CAN)
```

The old β must be rewritten:
```
β = σ / (M̄_Pl² / L²)  →  needs [M̄_Pl²/L²] = M⁴
```

But [M̄_Pl²/L²] = M²·M² = M⁴, and [σ]/[M⁴] = M³/M⁴ = M⁻¹ ≠ 1.

**Therefore β = σL²/M̄_Pl² is dimensionally wrong under [σ] = M³.**

This means the error actually starts **earlier than v48** — it starts
at v28/v29 where β is defined with an implicit [σ] = M⁴ convention
that conflicts with EDC's [σ] = M³.

---

## 6. Root Cause Analysis

The root cause is a **dimension convention mismatch**:

| Convention | [σ] | Used in | β dimensionless? |
|-----------|-----|---------|------------------|
| RS/brane-world | M⁴ | v28–v66 | YES (β = σL²/M̄_Pl²) |
| EDC native | M³ | Book I Ch.7, TSTAR docs | NO (β off by M⁻¹) |

The entire derivation chain v28–v66 implicitly uses the RS convention
[σ] = M⁴ (energy per volume). The TSTAR_DERIVATION_5D.md and EDC core
use [σ] = M³ (energy per area).

**v67 (DEF-D) is the only version that works under either convention**,
because T_* is defined to have the same dimensions as σ, whatever those are.

---

## 7. Required Corrections

### Phase A: Fix dimension convention (root fix)

1. **Declare canonical [σ]** in BLOCK-003 preamble.
   If EDC: [σ] = M³ → rewrite β = σL³/M̄_Pl³ or use T_* normalization.
   If RS: [σ] = M⁴ → β = σL²/M̄_Pl² is fine, but must be declared.

2. **Reconcile with EDC Book I Chapter 7** which uses σ in J/m² = M³.

### Phase B: Fix σ̃ chain (consequence)

3. **Adopt DEF-D as canonical**: σ̃ = σ/T_*, T_* = C · M₅^{d-1}
   where d-1 matches the dimension of σ.

4. **Deprecate DEF-B**: σ̃ = σ/M̄_Pl⁴ is wrong under both conventions.
   Under [σ]=M⁴: dimensionless but physically meaningless (too small).
   Under [σ]=M³: dimensionally wrong.

5. **Deprecate DEF-C**: σ̃ = β absorbs dimension error from β.

6. **Delete or flag β = σ̃⁴** from v56 — algebraic error regardless
   of convention.

### Phase C: Propagate

7. **Create canonical v68** with corrected definitions.
8. **Update SIGMA_TILDE_EXPORT_CONTRACT.md** to reference OPR-30-CAN.
9. **Update TSTAR_DEFINITION.md** with explicit dimension convention.

---

## 8. Version Triage

| Version | σ̃-related content | Action |
|---------|-------------------|--------|
| v1–v27 | No σ̃ or β | No action |
| v28–v29 | β defined | Flag dimension convention |
| v30–v47 | β used | Flag dimension convention |
| v48 | DEF-B introduced | **DEPRECATE** DEF-B, flag line 367 |
| v49–v55 | DEF-B inherited | **DEPRECATE** σ̃ usage |
| v56 | β = σ̃⁴ derived | **DELETE** — algebraic error |
| v57–v61 | Transitional | Review case-by-case |
| v62–v66 | DEF-C (σ̃ = β) | **DEPRECATE** — inherits β dimension issue |
| v67 | DEF-D (σ̃ = σ/T_*) | **ADOPT** as canonical |

---

## 9. Canonical Closure Chain (Corrected)

Under OPR-30-CAN (σ̃ = σ/T_*):

```
σ (dimensional brane tension, [σ] = M³ or M⁴)
    │
    ├─ T_* = C · M₅^{dim(σ)}  (from 5D geometry, OPEN)
    │
    ▼
σ̃ = σ/T_*  [dimensionless]
    │
    ├── α₃(μ*) = 1/σ̃          → strong coupling at GUT scale
    ├── M_X = C_X μ* σ̃^{1/2}   → GUT mass
    ├── g_X = √(4π/σ̃)          → GUT coupling
    └── τ_p ∝ σ̃⁴               → proton lifetime
```

**All four observables require σ̃ ~ O(100) for physical values.**

---

## 10. Open Items After Resolution

| Item | Priority | Status |
|------|----------|--------|
| Fix [σ] convention across all BLOCK-003 versions | HIGH | THIS DOCUMENT |
| Derive T_* numerically from 5D geometry | HIGH | TSTAR_DERIVATION_5D.md [P] |
| Determine C_A, C_B geometric factors | HIGH | [P] |
| Create canonical v68 with corrected definitions | HIGH | TODO |
| Verify σ̃ ~ 100 follows from derived T_* | MEDIUM | [P] |
| Reconcile M₅ with EDC Book I parameters | MEDIUM | [P] |

---

## 11. Epistemic Status

| Claim | Tag |
|-------|-----|
| σ̃ = σ/T_* is canonical definition | [Dc] (definitional contract) |
| T_* = C · M₅^{dim(σ)} structural form | [Dc] |
| DEF-B is algebraically wrong | [Der] (proven, Section 2) |
| DEF-C inherits dimension ambiguity | [Der] (proven, Section 5) |
| v56 β = σ̃⁴ is algebraic error | [Der] (proven, Section 2) |
| σ̃ ~ 100 numeric value | [Cal] (back-calculated from α₃) |
| T_* numeric value | [P] (pending 5D geometry solution) |
| [σ] = M³ vs M⁴ convention choice | [Dc] (must be declared) |

---

## 12. Guard Compliance

- **G1 (Ontological purity)**: No SM input. T_* from 5D geometry only.
- **G2 (Empirical protocol)**: α₃ ≈ 0.01 used only as verification target.
- **G3 (Epistemic honesty)**: σ̃ = 100 tagged [Cal], not [Der].
- **G7 (No contamination)**: σ̃ must be derived forward (5D → T_* → σ̃),
  never backward (α₃ → σ̃ → T_*).

---

**Document Hash:** TBD
**Parent Documents:** v29 (β canonical), v67 (DEF-D), TSTAR_DERIVATION_5D.md
