# Scale Taxonomy Consistency Audit

**Date**: 2026-01-25
**Sprint**: Scale Consistency Pass (Δ vs δ vs ℓ vs R_ξ)
**Branch**: book2-opr04-delta-derivation-v1

---

## Purpose

Eliminate all implicit or accidental identification of the four EDC length scales
and establish canonical notation with explicit assumption labeling.

---

## Canonical Definitions

| Symbol | Name | Physical Role | Status |
|--------|------|---------------|--------|
| Δ | Kink width | Scalar wall microphysics: φ = v tanh(ξ/Δ) | [M] |
| δ | Boundary-layer | Transport/diffusion regularization for Robin BC | [P] |
| ℓ | Domain support | Sturm-Liouville interval for OPR-21: μ = M₀ℓ | [P] |
| R_ξ | Diffusion scale | Coordinate/correlation length: R_ξ = ℏc/M_Z | [BL] |

**Canonical source**: Chapter 16, §16.1 (`\label{sec:ch16_reader_map}`)

---

## Assumption Labels

| ID | Statement | Meaning |
|----|-----------|---------|
| (A1) | Δ = δ | Kink width equals boundary-layer scale |
| (A2) | δ = R_ξ | Boundary-layer scale equals diffusion scale |
| (A3) | ℓ = nΔ, n = O(1) | Domain size proportional to kink width (modest n) |

**Rule**: No derivation may silently assume any of (A1)–(A3). Each must be tagged [P] with label.

---

## Occurrences Found and Actions Taken

### 1. ch14_opr21_closure_derivation.tex:484

**Before**:
```latex
$M(\xi) = M_0 \tanh((\xi - \ell/2)/\Delta)$ with $\delta = \Delta/\ell = 0.1$.
```

**Problem**: Uses δ as a **dimensionless ratio**, creating symbol collision with boundary-layer scale δ.

**After**:
```latex
$M(\xi) = M_0 \tanh((\xi - \ell/2)/\Delta)$ with wall-to-domain ratio $\rho := \Delta/\ell = 0.1$.
```
Plus footnote referencing Scale Taxonomy.

**Action**: Renamed ratio to ρ to avoid confusion.

---

### 2. ch10_electroweak_bridge.tex:40-45

**Before**: Listed "δ = R_ξ identification: plausible but not proven from action"

**After**: Added explicit "(A2)" label and Scale Taxonomy cross-reference:
```
$\delta = R_\xi$ identification: assumption (A2)---plausible but not proven from action
...
Scale notation: δ = boundary-layer scale, ℓ = domain size, Δ = kink width.
See Scale Taxonomy, Chapter~16, §16.1.
```

**Action**: Added assumption label and cross-reference.

---

### 3. ch15_opr01_sigma_anchor_derivation.tex:46-47

**After No-Smuggling box**: Added Scale Taxonomy cross-reference:
```
Scale notation: Δ = kink/wall thickness (scalar microphysics), ℓ = domain size (BVP interval).
These are a priori distinct; see Scale Taxonomy, Chapter~16, §16.1.
```

**Action**: Added clarification note.

---

### 4. ch11_opr20_attemptH_delta_equals_Rxi.tex (multiple occurrences)

**Status**: NO CHANGE NEEDED

This file explicitly discusses the δ = R_ξ identification as a proposed hypothesis.
All occurrences are intentional and properly tagged as [Def] or [P].
The file title itself indicates this is "Attempt H: δ = R_ξ Gate".

---

### 5. ch16_opr04_delta_derivation.tex

**Status**: Already contains canonical Scale Taxonomy with:
- Table of all four scales
- Assumption labels (A1)–(A3)
- Lemma 16.1 (Conditional Tension)
- Working Default (WD) path designation
- Unit conversion note (1 fm = 5.0677 GeV⁻¹)

---

### 6. OPR_REGISTRY.md

**Action**: Added new "Scale Taxonomy" section at top with:
- Canonical table
- Assumption labels (A1)–(A3)
- Working Default (WD) designation
- Conditional Tension summary

---

## Remaining "brane thickness" Usages

The following files use "brane thickness" language:

| File | Context | Assessment |
|------|---------|------------|
| ch10_electroweak_bridge.tex | "Finite brane thickness δ" | OK - explicitly uses δ |
| ch12_bvp_workpackage.tex | "From Brane Thickness to Effective Couplings" | OK - context clear |
| ch11_gf_full_closure_plan.tex | Various | OK - discusses ℓ value derivation |
| 02_geometry_interface.tex | "across the brane thickness" | OK - qualitative |
| 05_case_neutron.tex | "coordinate across brane thickness" | OK - qualitative |

**Verdict**: No changes needed — these usages are contextually clear and do not create
implicit identifications.

---

## Verification Grep

```bash
# Check for remaining problematic patterns
grep -rn --include="*.tex" "\\\\Delta\s*=\s*\\\\delta" src/sections/
# Result: Only in ch16 (intentional A1 definition) and ch16 (Path A box)

grep -rn --include="*.tex" "\\\\ell\s*=\s*\\\\Delta" src/sections/
# Result: None found

grep -rn --include="*.tex" "\\\\delta\s*=\s*\\\\Delta/\\\\ell" src/sections/
# Result: None found (was fixed to ρ)
```

---

## Summary

| Category | Count | Status |
|----------|-------|--------|
| Symbol collisions fixed | 1 | ✓ (δ → ρ for ratio) |
| Cross-references added | 3 | ✓ (ch10, ch14, ch15) |
| Canonical taxonomy | 1 | ✓ (ch16 §16.1) |
| Registry updated | 1 | ✓ (OPR_REGISTRY.md) |
| Intentional usages verified | ~20 | ✓ (no false positives) |

---

## Acceptance Gates

- [x] Build passes (XeLaTeX via latexmk)
- [x] No forbidden patterns without explicit assumption labels
- [x] Cross-references resolve
- [x] No SM observable smuggling
- [x] Ch14 explicitly states μ = M₀ℓ, not M₀Δ

---

*Audit completed 2026-01-25*
