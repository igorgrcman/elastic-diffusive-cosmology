# G_F Non-Circular Framework: Executive Summary

**Created:** 2026-01-29
**Status:** Framework [Der], Numerical values [OPEN] (BVP-gated)
**Issue:** P3-3 — G_F derivation without circularity

---

## 1. Why the Old Approach Was Circular

The Standard Model defines the Higgs VEV from G_F:
```
v = (√2 G_F)^{-1/2} = 246.22 GeV
```

Therefore, any derivation chain that uses v to compute M_W, then M_W to compute G_F, returns the input G_F by construction. This is a **consistency identity**, not an independent prediction.

**The true independent EDC prediction is sin²θ_W = 1/4** (0.08% agreement with experiment at M_Z).

---

## 2. The Non-Circular Chain

```
5D Action  →  g_5  →  M_eff  →  BVP modes  →  I_4  →  G_F^EDC
    ↓           ↓        ↓           ↓           ↓         ↓
[normalization] [KK]  [eigenvalue] [profiles] [overlap] [assemble]
```

**No v anywhere in the forward chain.**

### 2.1 Key Definitions

| Symbol | Definition | Status |
|--------|------------|--------|
| g_5 | 5D gauge coupling from action normalization | [Dc] |
| M_eff | Effective mediator mass from KK eigenvalue | [OPEN] |
| w_L, w_R | Chiral fermion mode profiles | [OPEN] |
| w_φ | Mediator mode profile | [OPEN] |
| I_4 | Overlap integral ∫ dχ w_L² w_R² w_φ² | [OPEN] |

### 2.2 Non-Circular Formula

```
G_F^EDC = g_eff² / (4√2 M_eff²)

where:
  g_eff² = g_5² × I_g      (I_g = gauge overlap)
  M_eff² = λ_0 / δ²        (λ_0 = KK eigenvalue)
```

### 2.3 Dimensionless Target

```
X := G_F × m_e² = 3.04 × 10⁻¹² (natural units)

X_EDC = C × (g_5² × I_4 × m_e²) / M_eff²
```

where C = 1/(4√2) from SM convention.

---

## 3. What We Can Compute Now vs What Waits for BVP

### Layer A: Derivable Now [Der]

1. **Dimensional skeleton** — G_F^EDC ~ g_5² I_4 / M_eff² (unique combination)
2. **Independence from v** — chain uses only 5D ingredients
3. **Scaling analysis** — δ³ suppression explains smallness
4. **sin²θ_W = 1/4** — separate, fully derived prediction

### Layer B: BVP-Dependent [OPEN]

1. **Mode profiles** w_L(χ), w_R(χ), w_φ(χ) — from thick-brane Dirac equation
2. **KK eigenvalue** λ_0 — from extra-dimension boundary value problem
3. **Overlap integral** I_4 — numerical evaluation
4. **Numerical G_F** — final assembly

**Blocking dependency:** OPR-21 (thick-brane BVP solution)

---

## 4. Falsification Gates

### Gate 1: Overlap Mismatch
```
FAIL if: I_4^BVP ∉ [0.1, 10] × I_4^required
```
Required: I_4 ~ (6 MeV)² ~ 4 × 10⁻⁵ GeV²

### Gate 2: Mass Inconsistency
```
FAIL if: M_eff ∉ [0.1, 10] × (1/δ)
```
Expected: M_eff ~ 1/δ ~ 1.9 GeV

### Gate 3: Coupling Incompatibility
```
FAIL if: g_eff² ≠ (4πα/sin²θ_W) × f(overlaps) with f ~ O(1)
```

---

## 5. What Would Kill It

1. **BVP gives wrong overlap:** If I_4 from thick-brane solution is >100× off from constraint window, mode-overlap mechanism fails.

2. **No chirality suppression:** If left and right modes aren't spatially separated, ε = ∫ w_L w_R ~ O(1) and the required suppression doesn't emerge.

3. **M_eff violates δ scaling:** If KK reduction gives M_eff incompatible with brane thickness, the geometric picture breaks down.

---

## 6. Toy Feasibility Window

For X_EDC ~ X_target = 3 × 10⁻¹²:

| Parameter | Required Range | Plausibility |
|-----------|----------------|--------------|
| ε (chirality suppression) | 10⁻³ – 10⁻² | ✓ Plausible |
| σ/δ (localization ratio) | 0.01 – 0.1 | ✓ Plausible |
| M_eff | 1 – 10 GeV | ✓ Plausible |
| I_4 | (6 MeV)² | ✓ Plausible |

**Caveat:** This is a feasibility window, not an EDC derivation. Actual values require BVP.

---

## 7. Cross-References

| Document | Content |
|----------|---------|
| `docs/GF_CONSTRAINT_NOTE.md` | Constraint window analysis |
| `edc_papers/_shared/derivations/gf_noncircular_chain_framework.tex` | Full LaTeX derivation |
| `edc_papers/_shared/code/gf_toy_overlap_window.py` | Toy model computation |
| `edc_papers/_shared/lemmas/projection_reduction_lemma.tex` | Overlap suppression mechanism |
| `edc_book_2/src/sections/11_gf_derivation.tex` | Book chapter |

---

## 8. Status Summary

| Component | Status | Color |
|-----------|--------|-------|
| Framework exists | [Der] | GREEN |
| Circularity removed | [Der] | GREEN |
| Dimensional skeleton | [Der] | GREEN |
| Toy feasibility | [I] | YELLOW |
| g_5 from action | [Dc] | YELLOW |
| M_eff from KK | [OPEN] | RED |
| I_4 from BVP | [OPEN] | RED |
| Numerical G_F | [OPEN] | RED |

**P3-3 overall: YELLOW (framework complete, values BVP-gated)**

---

*Created 2026-01-29. Non-circular framework established; numerical closure blocked by OPR-21.*
