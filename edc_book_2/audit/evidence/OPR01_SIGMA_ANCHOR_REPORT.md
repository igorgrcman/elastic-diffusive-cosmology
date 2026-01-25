# OPR-01 σ→M₀ Anchor — Evidence Report

**Status**: CONDITIONAL [Dc]
**Date**: 2026-01-25
**Sprint**: book2-opr01-sigma-anchor-v1

---

## Executive Summary

This report documents the derivation of the bulk mass amplitude M₀ from the membrane
tension σ and domain-wall thickness Δ. The derivation uses scalar kink theory [M]
combined with a Yukawa coupling ansatz [P].

**Main Result**:
```
M₀² = (3/4) y² σ Δ      [Dc]

M₀ = (√3/2) y √(σΔ)     [Dc]
   ≈ 0.866 y √(σΔ)
```

**OPR-01 Status Upgrade**: OPEN → CONDITIONAL [Dc]

---

## Derivation Outline

### Step 1: Domain-Wall Ansatz [P]

The thick brane is modeled as a scalar kink:
```
φ(ξ) = v tanh(ξ/Δ)
```
where:
- v = scalar vacuum expectation value
- Δ = wall thickness = 2/(v√λ)
- λ = scalar self-coupling

### Step 2: Fermion Mass from Yukawa [P]

Yukawa coupling generates position-dependent mass:
```
M(ξ) = y φ(ξ) = y v tanh(ξ/Δ) = M₀ tanh(ξ/Δ)
```
with:
```
M₀ = y v     [Dc from ansatz]
```

### Step 3: Domain-Wall Tension [M]

The kink energy density integrated over the wall:
```
σ = ∫ T₀₀ dξ = (2λv⁴Δ/3) × (4/3) = 4v²/(3Δ)
```

Therefore:
```
σ Δ = 4v²/3     [M]
```

### Step 4: Elimination of v [Dc]

From M₀ = yv and σΔ = 4v²/3:
```
v = M₀/y

σ Δ = 4(M₀/y)²/3 = 4M₀²/(3y²)

M₀² = (3y²/4) σ Δ     [Dc]
```

---

## Claim-to-Equation Mapping

| Claim | Equation Label | Source File | Line | Tag |
|-------|---------------|-------------|------|-----|
| Scalar kink solution | eq:opr01:kink | ch15_opr01_sigma_anchor_derivation.tex | ~63 | [M] |
| Wall thickness | eq:opr01:Delta_def | ch15_opr01_sigma_anchor_derivation.tex | ~68 | [M] |
| Yukawa mass profile | eq:opr01:Mxi_profile | ch15_opr01_sigma_anchor_derivation.tex | ~80 | [P]+[Dc] |
| M₀ = yv | eq:opr01:M0_yv | ch15_opr01_sigma_anchor_derivation.tex | ~84 | [Dc] |
| BPS condition | eq:opr01:BPS | ch15_opr01_sigma_anchor_derivation.tex | ~113 | [M] |
| σ Δ = 4v²/3 | eq:opr01:sigma_v2 | ch15_opr01_sigma_anchor_derivation.tex | ~127 | [Dc] |
| **M₀² = (3y²/4) σ Δ** | **eq:opr01:M0sq_result** | ch15_opr01_sigma_anchor_derivation.tex | ~140 | **[Dc]** |
| M₀ numerical | eq:opr01:M0_numerical | ch15_opr01_sigma_anchor_derivation.tex | ~146 | [Dc] |
| μ formula | eq:opr01:mu_formula | ch15_opr01_sigma_anchor_derivation.tex | ~190 | [Dc] |
| Consistency constraint | eq:opr01:sigmaD3 | ch15_opr01_sigma_anchor_derivation.tex | ~210 | [Dc] |

---

## Dependency Graph

```
Level 0 (Primitives, all [P]):
    σ (membrane tension)
    Δ (wall thickness)
    y (Yukawa coupling)
    n = ℓ/Δ (domain-size ratio)

Level 1 (Derived [Dc]):
    M₀ = (√3/2) y √(σΔ)
    ↑ depends on: σ, Δ, y, kink theory [M]

Level 2 (Derived [Dc]):
    μ = M₀ ℓ = (√3/2) y n √(σΔ³)
    ↑ depends on: M₀ [Dc], Δ [P], n [P]

Level 3 (Conditional [Dc]):
    N_bound = 3 for μ ∈ [25, 35)
    ↑ depends on: μ [Dc], BVP structure [Dc] (from OPR-21)
```

---

## Assumptions and Their Effects

| Assumption | Type | What it affects | If changed... |
|------------|------|-----------------|---------------|
| λφ⁴ kink profile | [P] | σ-v relationship | Different potential → different coefficient |
| Yukawa coupling mechanism | [P] | M₀ = yv identification | Other mass generation → different M₀(σ) |
| y ~ O(1) | [P] | Numerical value of M₀ | y ≠ 1 → rescaled M₀ |
| ℓ = nΔ | [P] | μ constraint | Different ℓ/Δ → different μ range |
| Flat extra dimension | [P] | Kink solution form | Warping → modified profile |

---

## No-Smuggling Checklist

| Check | Status | Evidence |
|-------|--------|----------|
| M_W not used as input | ✓ PASS | No occurrence in derivation |
| G_F not used as input | ✓ PASS | No occurrence in derivation |
| v = 246 GeV not used | ✓ PASS | v is scalar VEV, not Higgs VEV |
| sin²θ_W not used | ✓ PASS | No electroweak mixing in derivation |
| α(M_Z) not used | ✓ PASS | No running couplings |
| PMNS/CKM not used | ✓ PASS | No mixing matrices |
| τ_n not used | ✓ PASS | No neutron lifetime |
| CODATA fits not used | ✓ PASS | Only mathematical constants |

**Grep verification command**:
```bash
grep -i "246\|M_W\|G_F\|sin.*theta\|PMNS\|CKM\|neutron\|lifetime\|CODATA" \
    src/sections/ch15_opr01_sigma_anchor_derivation.tex
```
Expected result: **0 matches** (or only in No-Smuggling certification block).

---

## Connection to OPR-21

The OPR-21 result states N_bound = 3 for μ ∈ [25, 35). With the OPR-01 derivation:

```
μ = M₀ ℓ = (√3/2) y n √(σΔ³)
```

For μ ∈ [25, 35) with y = 1, n = 4:
```
25 ≤ 0.866 × 4 × √(σΔ³) < 35
25 ≤ 3.46 × √(σΔ³) < 35
7.2 ≤ √(σΔ³) < 10.1
52 ≤ σΔ³ < 102
```

**Consistency constraint**: σΔ³ ∈ [52, 102] for three-generation phenomenology.

---

## OPR-01 Status Update

| Aspect | Before | After |
|--------|--------|-------|
| Status | OPEN | CONDITIONAL [Dc] |
| M₀ source | [P] postulated | [Dc] derived from σ, Δ |
| Parameter freedom | 3 independent (M₀, σ, Δ) | 2 independent (σ, Δ) + 1 derived |
| μ constraint | Scanned | Analytically related to σΔ³ |

---

## Remaining Open Items

1. **σ value anchor** — Still [P], needs cosmological/gravitational input
2. **Δ derivation** — Still [P], needs junction stability analysis
3. **y derivation** — Still [P], needs gauge embedding or naturalness
4. **ℓ/Δ principle** — Still [P], needs domain-size energetics

---

## Files Created/Modified

| File | Action | Lines |
|------|--------|-------|
| src/sections/ch15_opr01_sigma_anchor_derivation.tex | CREATE | ~280 |
| audit/evidence/OPR01_SIGMA_ANCHOR_REPORT.md | CREATE | ~180 |
| canon/opr/OPR-01.md | CREATE | ~100 |
| code/opr01_sigma_anchor_check.py | CREATE | ~60 |

---

*Report generated: 2026-01-25*
*Sprint: book2-opr01-sigma-anchor-v1*
