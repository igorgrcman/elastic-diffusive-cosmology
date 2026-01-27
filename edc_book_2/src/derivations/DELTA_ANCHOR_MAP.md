# δ (Brane Thickness) Anchor Map — Forensic Audit

**Date:** 2026-01-27
**Status:** AUDIT COMPLETE — Multiple δ scales identified, anchoring required
**Branch:** delta-audit-anchor-v1

---

## 1. Executive Summary

This audit identifies **four distinct thickness-like scales** used in EDC:

| Symbol | Value | Context | Status | Book Location |
|--------|-------|---------|--------|---------------|
| R_ξ | ~2×10⁻³ fm | Membrane correlation length | [P]+[BL] | Part I, Framework v2.0 |
| Δ | 3.121×10⁻³ fm | Electron mass formula | [P] | CH4, OPR-04 |
| ℓ | 2π R_ξ ≈ 0.013 fm | Orbifold circumference | [Dc] | CH11–13 |
| **δ** | **0.1 fm** | **Junction core / Put C** | **[I]** | **NOT in book** |

**Critical Finding:**
The δ = 0.1 fm used in junction-core derivations is an **order-of-magnitude estimate**
introduced in the code without book-level anchoring. It is ~50× larger than R_ξ.

---

## 2. Detailed δ Map

### 2.1 R_ξ — Membrane Correlation Length

**Definition:** The correlation length of the frozen membrane.

**Book locations:**
- Part I, Framework v2.0 (primary definition)
- CH11–13 (OPR-20 attempts)

**Value:** R_ξ ≈ 2×10⁻³ fm = ℏc/M_Z [P]+[BL]

**Status:** [P]+[BL] — phenomenologically constrained via M_Z matching, not derived.

**Key equations:**
```
⟨φ(x)φ(x')⟩ ~ exp(-|x-x'|/R_ξ)
R_ξ = ℏc / M_Z ≈ 197.3 MeV·fm / 91200 MeV ≈ 0.00216 fm
```

### 2.2 Δ — Electron Mass Thickness (CH4)

**Definition:** Brane thickness appearing in electron mass candidate formula.

**Book location:** CH4_lepton_mass_candidates.tex, line 36

**Value:** Δ = 3.121×10⁻³ fm [P] (OPR-04, OPEN)

**Status:** [P] — postulated, not derived.

**Key equation:**
```
m_e = π √(α σ Δ ℏc)    [P]
```

**Note:** Uses σ = 5.86 MeV/fm² (different from σ = 8.82 MeV/fm² in junction core!).

### 2.3 ℓ — Orbifold Circumference

**Definition:** Circumference of the compact extra dimension.

**Book locations:** CH11, CH12, CH14

**Value:** ℓ = 2π R_ξ ≈ 0.013 fm [Dc]

**Status:** [Dc] — derived from R_ξ via standard circle geometry.

**Key role:** Enters Robin BC via α = ℓ/δ.

### 2.4 δ — Junction Core Thickness (Put C)

**Definition:** Brane thickness scale used in junction-core model.

**Book location:** **NOT DEFINED IN BOOK**

**Code locations:**
- derivations/code/putC_compute_MV.py:855 — `delta = 0.1  # fm (brane thickness)`
- derivations/code/junction_core_well.py:79 — `DELTA_EDC = 0.1  # fm [I] brane thickness`
- derivations/code/derive_C_integrals.py:48 — `DELTA_EDC = 0.1  # fm [I] brane thickness`

**Value:** δ = 0.1 fm [I]

**Status:** [I] — order-of-magnitude estimate, not anchored.

**Comment in code:**
```python
# Base parameters [I] — order-of-magnitude estimates
L0 = 1.0  # fm (nucleon scale)
delta = 0.1  # fm (brane thickness)
```

---

## 3. Scale Hierarchy

```
R_ξ  ≈  0.002 fm   (electroweak/diffusion scale)
Δ    ≈  0.003 fm   (electron mass formula)
ℓ    ≈  0.013 fm   (orbifold circumference)
δ    ≈  0.1   fm   (junction core / nucleon scale)
L0   ≈  1.0   fm   (nucleon radius)
```

**Ratio:** δ / R_ξ ≈ 50

**Interpretation:** There appear to be TWO distinct thickness scales:
1. **Electroweak thickness** ~ R_ξ ~ 10⁻³ fm (sets KK masses, mediator physics)
2. **Nucleon thickness** ~ δ ~ 10⁻¹ fm (sets junction-core geometry)

---

## 4. How δ = 0.1 fm Enters the C Derivation

In `DERIVE_C_FROM_GEOMETRY.md`, we have:

```
C = (L0/δ)² = (1.0 fm / 0.1 fm)² = 100    [Dc]
```

**Dependencies:**
- L0 = 1.0 fm [I] — nucleon scale (from proton charge radius)
- δ = 0.1 fm [I] — brane thickness (**NOT ANCHORED**)

**Critical:** The [Dc] status of C is **conditional on** the [I] identification δ = 0.1 fm.

If δ were different, C would change:

| δ [fm] | C = (L0/δ)² | E0 = Cσδ² [MeV] |
|--------|-------------|-----------------|
| 0.05 | 400 | 8.82 |
| 0.10 | 100 | 8.82 |
| 0.15 | 44 | 8.82 |
| 0.20 | 25 | 8.82 |

**Note:** E0 = C × σ × δ² = σ × L0² is independent of δ! The "pancake" model gives:

```
E0 = σ × L0²  (transverse area × tension)
```

This suggests a reformulation that doesn't require specifying δ explicitly.

---

## 5. Resolution Proposal

### Option A: Accept Two-Scale Model [I]

Acknowledge that EDC has two thickness scales:
- R_ξ ~ 10⁻³ fm for electroweak physics
- δ ~ 10⁻¹ fm for nucleon/junction physics

**Anchoring:** δ = L0/10 [I] (nucleon scale divided by 10)

This is phenomenologically motivated but not derived.

### Option B: Reformulate Without Explicit δ

Rewrite the junction-core result as:

```
E0 = σ × L0²    [Dc] (transverse area × tension)
V_core(q) = -E0 × f(q/δ)    [Dc]
```

where:
- E0 depends only on L0 (not δ)
- δ only enters the **shape** f(q/δ), not the magnitude
- The shape function can be written as f(q × L0/A) where A is a numerical constant

**Advantage:** Removes explicit δ dependence from the energy scale.

### Option C: Derive δ from L0 and R_ξ

Attempt to derive δ as a geometric mean or other combination:

```
δ = √(L0 × R_ξ) = √(1.0 × 0.002) ≈ 0.045 fm    [Dc]?
```

This gives δ ~ 0.05 fm, which is order-of-magnitude correct but not exactly 0.1 fm.

### Recommended: Option B (Reformulation)

The cleanest approach is to reformulate so that:
1. **E0 = σ × L0²** [Dc] — depends on nucleon scale, not brane thickness
2. **f(q/δ)** [P] — shape function with decay scale δ as [I] input

This keeps the [Dc] status for E0 while honestly tagging the shape dependence.

---

## 6. Conflicts and Inconsistencies

### 6.1 σ Value Conflict

| Location | σ Value | Status |
|----------|---------|--------|
| CH4 (electron mass) | 5.86 MeV/fm² | [P] |
| Junction core code | 8.82 MeV/fm² | [Dc] |

**Resolution:** The 8.82 MeV/fm² value is derived from E_σ = m_e c²/α [Dc].
The 5.86 MeV/fm² in CH4 appears to be an older/different definition.

**Action needed:** Harmonize σ values or clarify when each applies.

### 6.2 Multiple δ-like Symbols

| Symbol | Meaning |
|--------|---------|
| δ | Brane thickness (generic) |
| Δ | Electron mass thickness (CH4) |
| R_ξ | Correlation length |
| ℓ | Orbifold circumference |
| δ_b | Sometimes used for boundary layer |

**Recommendation:** Use distinct symbols:
- **R_ξ** for electroweak scale
- **δ_nucl** or **δ_J** for nucleon/junction scale
- **Δ** for electron formula (if retained)

---

## 7. Book Insertion Text (Patch-Ready)

The following can be inserted into the book (suggested location: after §11.3 in
S5D_TO_SEFF_Q_REDUCTION.md or as a new subsection in the neutron chapter):

---

### Brane Thickness Scale for Junction-Core Model [I]

The junction-core energy scale requires a characteristic thickness δ for the
decay profile f(q/δ). In the nucleon/neutron context, we identify:

**Definition [I]:**
```
δ ≡ L0/10 ≈ 0.1 fm
```

where L0 ≈ 1.0 fm is the nucleon transverse scale (comparable to proton charge
radius r_p ≈ 0.88 fm [BL]).

**Physical interpretation:**
The brane thickness δ represents the scale over which the junction-core
attraction decays into the bulk. It is identified as 1/10 of the nucleon
scale based on the aspect ratio of the "pancake" model:
- Transverse extent: L0 (nucleon-sized)
- Bulk extent: δ (10× smaller)

**Epistemic status:**
- δ = L0/10 [I] — geometric identification, not derived
- C = (L0/δ)² = 100 [Dc] conditional on this identification
- E0 = C × σ × δ² = σ × L0² [Dc] — the energy scale depends on L0, not δ

**Note on scale hierarchy:**
This nucleon-scale δ ≈ 0.1 fm should not be confused with the electroweak
scale R_ξ ≈ 0.002 fm, which governs KK mode spectra and mediator physics.
The ratio δ/R_ξ ≈ 50 reflects the hierarchy between nucleon and electroweak
length scales.

---

## 8. Required Document Updates

### 8.1 derivations/DERIVE_C_FROM_GEOMETRY.md

Add explicit statement that δ = 0.1 fm is [I] (identified) with anchor δ = L0/10.
Update epistemic box to clarify C is [Dc] conditional on δ [I].

### 8.2 derivations/S5D_TO_SEFF_Q_REDUCTION.md

Add subsection "Brane Thickness Anchor" referencing this audit.

### 8.3 derivations/V_B_FROM_Z3_BARRIER_CONJECTURE.md

Note that V_B [Dc] status is conditional on both C [Dc] and δ [I].

### 8.4 Code files

Update comments to reference δ = L0/10 identification with book cross-reference.

---

## 9. Conclusions

1. **δ = 0.1 fm is NOT anchored in the book** — it is an order-of-magnitude
   estimate introduced in the code.

2. **The value δ = L0/10** provides a reasonable geometric identification [I]
   based on the pancake aspect ratio of the junction core.

3. **C = (L0/δ)² = 100 [Dc]** remains valid as a derived-conditional result,
   with the condition being δ = L0/10 [I].

4. **E0 = σ × L0² [Dc]** — the energy scale can be expressed without explicit
   δ, which strengthens the derivation.

5. **Multiple thickness scales exist in EDC** — R_ξ (electroweak) vs δ (nucleon) —
   and these should be clearly distinguished.

---

## 10. Reproducibility

This audit was performed by searching:
```
grep -rn "brane thickness" edc_book_2/src/
grep -rn "delta.*=.*0\.1" edc_book_2/src/
grep -rn "R_xi\|R_\\xi" edc_book_2/src/
```

All file paths and line numbers are as of 2026-01-27.

---

## 11. Version History

- 2026-01-27: Initial forensic audit completed
