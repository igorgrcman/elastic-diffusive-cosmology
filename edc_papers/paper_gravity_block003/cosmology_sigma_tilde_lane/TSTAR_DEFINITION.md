# T_* Definition and Derivation Roadmap

## Version: 2.0
## Date: 2026-03-16
## Status: STRUCTURAL — corrected dimensions per Task 1+2
## Changelog: v2.0 — [σ] corrected M³→M⁴; [T_*] corrected M³→M⁴; C derived = 3/(4π)

---

## 1. Definition of T_*

**[Dc]** T_* is the **characteristic tension scale** that renders the brane tension
dimensionless when forming the ratio:

```
σ̃ = σ / T_*                                          (OPR-30-CAN)
```

where:
- σ is the covariant 3-brane tension (units: [M]⁴ in natural units)
- T_* is the characteristic scale (same units as σ, [M]⁴)
- σ̃ is the dimensionless brane tension parameter

**WARNING (v2.0):** σ here is σ_covariant [M⁴], NOT σ_BookI = 8.82 MeV/fm² [M³].
See DIMENSION_CONVENTION_SIGMA.md for the proof that these are different quantities.

**[Dc]** T_* is NOT a free parameter. It must be derived from the fundamental
constants of the 5D bulk-brane system using only internal EDC axioms.

**[Dc]** This is the **unique canonical definition** of σ̃ per OPR-30 resolution.
Prior definitions (σ̃ = σ/M̄_Pl⁴ in v48, σ̃ = σL²/M̄_Pl² in v62) are
**deprecated** — see `OPR-30_SIGMA_TILDE_RESOLUTION.md` for full analysis.

---

## 2. Dimensional Analysis

### 2.1 Dimensions of σ (brane tension) — v2.0 corrected

**[Dc] DIMENSION CONVENTION (Task 1 resolution):**

In EDC, the brane Σ³ is a 3-brane (codimension-1 in 5D spacetime).
Its worldvolume is 4-dimensional. The brane action is:

```
S_brane = −σ_covariant ∫ d⁴x √{−h}
```

For S to be dimensionless: [σ]·[M]⁻⁴ = M⁰, therefore:

```
[σ_covariant] = [M]⁴     (3-brane tension = energy per 3-volume)
```

**CORRECTION (v2.0):** The v1.0 stated [σ] = M³ (energy per 2D area).
That dimension belongs to σ_BookI = 8.82 MeV/fm² (nuclear membrane
tension), which is a DIFFERENT physical quantity — a 2D defect WITHIN
the brane, not the brane itself. See DIMENSION_CONVENTION_SIGMA.md.

**WARNING:** The old β = σL²/M̄_Pl² was dimensionally inconsistent under
BOTH conventions. Under [σ] = M⁴: [β] = M⁴·M⁻²/M² = M⁰ ✓, but the
physical identification of σ with σ_BookI was wrong.

### 2.2 Dimensions of T_* — v2.0 corrected

**[Dc]** For σ̃ to be dimensionless, T_* must have the same dimensions as σ:

```
[T_*] = [σ_covariant] = [M]⁴ (natural units)
```

**[Der]** From TASK2_GEOMETRIC_FACTOR_C.md, the explicit form is:

```
T_* = 3M₅³/(4πℓ) = σ_RS     (RS fine-tuning tension)
```

where ℓ = √{−6/Λ₅} is the AdS radius.

### 2.3 Dimensionless Ratio

**[I]** The dimensionless brane tension is:

```
σ̃ = σ / T_*    [dimensionless]
```

This ratio appears in the BLOCK-004 closure chain:
- α₃(μ*) = 1/σ̃
- M_X = C_X μ* σ̃^{1/2}
- g_X = √(4π/σ̃)
- τ_p ∝ σ̃⁴

---

## 3. Derivation Roadmap

### 3.1 Required Ingredients

**[P]** T_* must be derived from the following 5D action components:

| Component | Symbol | Role |
|-----------|--------|------|
| Bulk action | S_bulk | 5D Einstein-Hilbert + cosmological term |
| Brane action | S_brane | Localized matter on 3-brane |
| Gibbons-Hawking-York | S_GHY | Boundary terms for well-posed variational problem |
| Israel junction | [K] | Extrinsic curvature matching at brane |

**[P]** Optional: Helfrich curvature terms if brane rigidity is non-zero.

### 3.2 Derivation Steps (TODO)

**Step 1: Define the 5D action** [P]

```
S_5D = S_bulk + S_brane + S_GHY
```

where:
```
S_bulk = ∫ d⁵x √{-g₅} (R₅ / 2κ₅² - Λ₅)
S_brane = -∫ d⁴x √{-g₄} σ
S_GHY = ∫ d⁴x √{-g₄} K / κ₅²
```

TODO: Write explicit 5D action with all terms.

**Step 2: Apply Israel junction conditions** [P]

```
[K_μν] - g_μν [K] = -κ₅² (T_μν - (1/3) g_μν T)
```

For a tension-dominated brane:
```
T_μν = -σ g_μν
```

TODO: Derive junction equations explicitly.

**Step 3: Extract characteristic scale** [P]

From the Israel conditions and 5D coupling κ₅, extract:

```
T_* = f(κ₅, Λ₅, geometric factors)
```

TODO: Identify exact functional form of f.

**Step 4: Verify dimensional consistency** [P]

Confirm [T_*] = [M]⁴ in natural units. (v2.0: corrected from M³)

TODO: Complete dimensional verification.

**Step 5: Compute σ̃** [P]

```
σ̃ = σ / T_*
```

TODO: Propagate uncertainties.

### 3.3 Candidate Forms (to be derived, NOT assumed)

**[P]** Possible structural forms for T_* (derivation required):

| Candidate | Form | Status |
|-----------|------|--------|
| κ₅-based | T_* ~ κ₅⁻² | [P] Needs derivation |
| Λ₅-based | T_* ~ Λ₅^{3/2} | [P] Needs derivation |
| Mixed | T_* ~ (Λ₅/κ₅²)^{3/4} | [P] Needs derivation |

**WARNING:** These are structural placeholders. NO numeric values should be
inserted until a complete derivation with hash-locked provenance is available.

---

## 4. Epistemic Status

### 4.1 Tag Legend

| Tag | Meaning |
|-----|---------|
| [I] | Invariant: mathematical identity or definition |
| [Dc] | Definitional contract: structural choice |
| [P] | Pending: requires derivation not yet completed |

### 4.2 Current Status Summary

| Claim | Tag | Status |
|-------|-----|--------|
| σ̃ = σ_covariant / T_* | [Dc] | Definitional |
| [σ_covariant] = [M]⁴ | [I] | Proven in Task 1 (v2.0) |
| [T_*] = [M]⁴ | [I] | Invariant from [σ̃] = M⁰ (v2.0 corrected) |
| T_* = 3M₅³/(4πℓ) = σ_RS | [Der] | Derived in Task 2 |
| C = 3/(4π) | [I] | From Israel junction |
| σ̃ = 1 at RS fine-tuning | [I] | Follows from T_* = σ_RS |
| Numeric value of ℓ | [P] | Requires Λ₅ from Plenum |
| Numeric value of σ_covariant | [P] | Requires EDC deviation from RS |
| Numeric value of σ̃ | [P] | Depends on σ_covariant and ℓ |

---

## 5. Provenance Requirements

### 5.1 When T_* is Derived

The derivation must provide:

1. **Source document** with explicit steps
2. **Hash lock** to parent derivations
3. **Uncertainty envelope** (if applicable)
4. **Epistemic upgrade**: change status from [P] to [D]

### 5.2 Propagation to σ̃

Once T_* is available:

```json
{
  "t_star": {
    "value": <derived_value>,
    "units": "MeV/fm^2",
    "status": "DERIVED"
  },
  "sigma_tilde": {
    "value": <sigma / t_star>,
    "status": "DERIVED"
  }
}
```

---

## 6. No-Backflow Statement

**[Dc]** Information flows ONE WAY only:

```
5D Cosmology → T_* → σ̃ = σ/T_* → BLOCK-004
                                    ↓
                              (read-only)
```

**BLOCK-004 MUST NOT:**
- Modify T_* or σ̃ values
- Infer T_* from τ_p predictions
- Feed back constraints to cosmology lane
- Override firewall protections

This ensures derivation chain integrity and prevents circular logic.

---

## 7. Firewall Compliance

This document is **Layer A only**.

**Forbidden content (not present):**
- No particle data group references
- No neutrino detector data
- No QCD simulation values
- No observational constraints
- No numeric predictions

**Status:** LAYER A COMPLIANT

---

## 8. TODO Summary

| Task | Priority | Status |
|------|----------|--------|
| Write full 5D action | HIGH | DONE (TSTAR_DERIVATION_5D.md §2) |
| Derive Israel junction | HIGH | DONE (§3) |
| Extract T_* form | HIGH | DONE (§4, v2.0: T_* = 3M₅³/(4πℓ)) |
| Derive geometric factor C | HIGH | DONE (Task 2: C = 3/(4π)) |
| Dimensional verification | MEDIUM | DONE (§7, v2.0) |
| Determine Λ₅ from Plenum | HIGH | OPEN (Companion C §13) |
| Determine σ_covariant | HIGH | OPEN (depends on EDC vs RS) |
| Compute σ̃ numerically | LOW | BLOCKED by Λ₅ and σ_covariant |
| Propagate to BLOCK-004 | LOW | BLOCKED by σ̃ value |

---

## 9. References

| Reference | Role |
|-----------|------|
| v65 (c4e7f2a1b8d30965) | BLOCK-004 canonical |
| v67 (d8e9f0a1b2c34567) | σ̃ import contract |
| SIGMA_TILDE_EXPORT_CONTRACT.md | Interface specification |
| sigma_tilde_schema.json | JSON export schema |

---

**Document Hash:** TBD (to be set when derivation complete)
