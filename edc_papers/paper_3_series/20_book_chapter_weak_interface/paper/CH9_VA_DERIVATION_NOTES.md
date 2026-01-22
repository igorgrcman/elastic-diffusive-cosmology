# Chapter 9: V–A Structure Derivation Notes

**Date:** 2026-01-22
**Status:** Book-ready chapter created
**Goal:** Derive the V–A (left-chiral) weak current structure from EDC 5D geometry

---

## Executive Summary

Chapter 9 derives the V–A structure from first principles using:
1. Standard 5D Dirac equation with position-dependent mass [BL]
2. Domain-wall chiral localization (Jackiw-Rebbi/Kaplan) [BL]
3. EDC postulate: Plenum inflow determines mass profile sign [P]

**Key result:** Left-handed modes localize at the boundary; right-handed modes are expelled into bulk. This gives V–A without assuming it.

---

## Derivation Outline

### Step 1: 5D Dirac Equation [BL]
```
(iγ^μ ∂_μ + iγ^5 ∂_z - m(z)) Ψ = 0
```

### Step 2: Chiral Decomposition [BL]
```
Ψ = Ψ_L + Ψ_R  where  P_{L/R} = (1 ∓ γ^5)/2
```

### Step 3: Mode Equations [BL]
For profiles f_L(z), f_R(z):
```
∂_z f_L = -m(z) f_L    →   f_L(z) = f_L(0) exp(-∫ m dz)
∂_z f_R = +m(z) f_R    →   f_R(z) = f_R(0) exp(+∫ m dz)
```

### Step 4: EDC Mass Profile [P]
Plenum inflow creates stress gradient:
```
m(z) ~ κ (T^zz(z) - T^zz(0)) > 0  for z > 0
```
Explicit form:
```
m(z) = m_0 (1 - e^{-z/λ})
```

### Step 5: Localization Result [Dc]
- **Left-handed:** f_L(z) decreases as z increases → **localized at boundary**
- **Right-handed:** f_R(z) increases as z increases → **expelled into bulk**

### Step 6: V–A Emergence [Dc]
Effective coupling:
```
g_eff^(L) = O(1)  (normalizable)
g_eff^(R) → 0     (not normalizable)
```
Therefore:
```
L_eff ~ ψ̄ γ^μ P_L ψ W_μ = (1/2) ψ̄ γ^μ (1 - γ^5) ψ W_μ
```

---

## Assumptions Audit

| Assumption | Status | Source |
|------------|--------|--------|
| 5D Dirac structure | [BL] | Standard QFT |
| γ^5 = iγ^0γ^1γ^2γ^3 | [BL] | Clifford algebra |
| Domain wall localization | [BL] | Jackiw-Rebbi 1976, Kaplan 1992 |
| Plenum inflow toward boundary | [P] | EDC Framework v2.0 |
| m(z) ~ κ T^zz | [P] | Physical hypothesis |
| κ > 0 | [P] | Assumed positive coupling |

---

## What Is NOT Claimed

1. **SU(2)_L gauge structure** — not derived, remains (open)
2. **W, Z mass generation** — not addressed
3. **CKM/PMNS mixing** — not derived
4. **Numerical G_F value** — deferred to Ch. 11
5. **Neutrino mass** — not addressed
6. **Three generations** — not explained by this mechanism alone

---

## Sanity Checks

### Dimensional Analysis
- [Ψ] = mass^2 in 5D (canonical)
- [f_{L/R}] = mass^{1/2}
- [ψ_{L/R}] = mass^{3/2} in 4D
- [m(z)] = mass
- [λ] = length

All equations dimensionally consistent.

### Limiting Cases
1. **m(z) = const:** No localization (uniform mass gives plane waves)
2. **m(z) = m_0 tanh(z/L):** Standard Jackiw-Rebbi; left-handed localized ✓
3. **m(z) → -m(z):** Reverses which chirality is localized (right-handed instead)

### Sign Consistency
- Plenum inflow: J^z > 0 (toward boundary)
- Stress: T^zz larger in bulk
- Mass: m(z) > 0 for z > 0
- Result: Left-handed localized ✓

---

## Connection to Research Targets

This chapter synthesizes results from:
- `RT-CH3-001_VA_FROM_INFLOW.tex` — original research target formulation
- `RT-CH3-001_WORKING_PHASE1.tex` — Phase 1 complete (toy model)
- `RT-CH3-002_WORKING_PHASE1.tex` — asymmetric profile analysis

The chapter presents the Phase 1 results in book-ready form.

---

## Open Problems (status: open)

1. **Full SU(2)_L embedding:** How does the localized left-handed mode couple to SU(2) gauge fields?

2. **W, Z masses:** Spontaneous symmetry breaking in 5D context.

3. **CKM/PMNS mixing:** Generational structure from mode overlaps.

4. **G_F from geometry:** Quantitative derivation (see Ch. 11 pathway).

5. **Z_2 chirality selection:** Does Z_2 ⊂ Z_6 provide a second mechanism?
   ```
   P_{Z_2}: Ψ → γ^5 Ψ
   ```
   If Z_6 boundary conditions select odd modes, this reinforces inflow argument.

6. **Helicity suppression:** Can |A|^2 ∝ m_ℓ^2 be derived from mode overlaps?

7. **Neutrino mass:** Majorana vs. Dirac in 5D context.

---

## Verification Commands

```bash
# Check for [OPEN] tags (should return nothing)
grep -R "\[OPEN\]" sections/09_va_structure.tex

# Check for undefined references
grep -i "undefined" EDC_Part_II_Weak_Sector.log

# Check for multiply-defined labels
grep -i "multiply" EDC_Part_II_Weak_Sector.log

# Build Part II
latexmk -xelatex -interaction=nonstopmode EDC_Part_II_Weak_Sector.tex
```

---

## Epistemic Summary

| Claim | Status | Confidence |
|-------|--------|------------|
| V–A from 5D localization | [Dc] | High (mathematically clean) |
| Inflow determines mass sign | [P] | Medium (physical but not derived from action) |
| f_L localized, f_R expelled | [Dc] | High (follows from equations) |
| No chirality smuggling | Verified | High (only input is inflow direction) |
| MIT bag analogy | [I] | Low (structural, not derived) |

**Overall verdict:** This is a "low-risk" derivation chapter. The core mechanism (domain-wall localization) is [BL], and the EDC-specific input (inflow direction) is minimal and physically motivated [P].

---

*Chapter 9 notes complete. The chapter is ready for integration into Part II.*
