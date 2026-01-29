# Δm_np Sensitivity Analysis

**Date:** 2026-01-29
**Purpose:** Determine robustness of Δm_np = 8m_e/π under parameter variations
**Status:** CANONICAL

---

## Executive Summary

1. **The formula Δm_np = (8/π)m_e is remarkably ROBUST** — it does not depend on σ, δ, L_0, or profile w(χ) as independent parameters
2. **All parameters are geometrically locked to m_e** via Z_6 ring structure
3. **The 8/π ratio is a pure geometric constant** from Z_6 symmetry (36) and circular geometry (π)
4. **Three assumptions control the result:** charge-angle coupling [Dc], elastic energy ansatz [Dc], Z_6 ring normalization [Dc]
5. **Sensitivity class: ROBUST** under plausible variations, but FRAGILE to discrete structure changes

---

## 1. Derivation Spine (Source: Framework v2.0 §10.4-10.5)

**Primary source:** `edc_papers/paper_3_series/00_framework_v2_0/paper/main.tex`
- Lines 964-1028
- Labels: `\label{thm:brane-tension}`, `\label{thm:v3-derived}`, `\label{thm:mass-diff-derived}`

### Step-by-Step Chain

| Step | Equation | Source | Assumptions |
|------|----------|--------|-------------|
| 1 | θ = (1-Q) × 60° | Thm charge-angle | Charge-angle coupling [Dc] |
| 2 | θ_n = 60° | Q_n = 0 | Neutron charge [BL] |
| 3 | q_n = 2sin(θ_n/2)/3 = 1/3 | Thm qn-derived | Half-angle geometry [Der] |
| 4 | σr_e² = (36/π)m_e | Thm brane-tension | Z_6 + ring normalization [Dc] |
| 5 | V_3 = σr_e² × q_n² | Rem q-squared | Elastic energy ∝ q² [Dc] |
| 6 | V_3 = (36/π) × (1/9) × m_e = (4/π)m_e | Substitution | — |
| 7 | Δm_np = 2\|V_3\| = (8/π)m_e | Thm mass-diff | Potential double-well [M] |

**Final result:**
```
Δm_np = (8/π) m_e = 1.301 MeV    [Dc]
Experimental: 1.293 MeV
Error: 0.6%
```

---

## 2. Dimensionless Rewrite

### Isolating the Pure Number

The formula can be written as:
```
Δm_np / m_e = 8/π ≈ 2.546
```

This is a **pure dimensionless ratio** that EDC predicts from geometry.

### Decomposition of 8/π

```
8/π = 2 × 4/π = 2 × (36/π) × (1/9)
    = 2 × (σr_e²/m_e) × q_n²
```

Where:
- Factor **2**: From Δm = 2|V_3| (proton vs neutron potential wells)
- Factor **36 = 6²**: From Z_6 symmetry (k_eff = 36V_0 - 9V_3)
- Factor **9 = 3²**: From q_n⁻² where q_n = 1/3
- Factor **π**: From circular ring geometry

### Key Observation: No Free Parameters

The formula contains:
```
Δm_np / m_e = f(Z_6 structure, ring geometry, charge-angle coupling)
```

All factors are **geometrically fixed**:
- 36 is locked by Z_6 = Z_3 × Z_2 symmetry
- 9 is locked by q = 1/3 from θ = 60°
- π is locked by circular (ring) oscillation geometry
- 2 is locked by potential analysis (symmetric wells)

**There is no independent σ, δ, or L_0 to vary.**

---

## 3. Parameter Sensitivity Table

### Parameters That Could Enter (But Don't)

| Parameter | How It Might Enter | Actually Enters? | Why? |
|-----------|-------------------|------------------|------|
| **σ** (membrane tension) | Via σr_e² energy scale | NO | σr_e² = (36/π)m_e is geometrically fixed |
| **δ** (brane thickness) | Via thick-brane projection | NO | Not a thick-brane calculation |
| **L_0** (junction extent) | Via junction dynamics | NO | Ring model uses angular, not spatial |
| **w(χ)** (brane profile) | Via projection ∫w(χ)dχ | NO | Not a projection calculation |
| **α** (fine structure) | Via EM corrections | NO | Pure Z_6 geometry, no EM loop |
| **m_p** (proton mass) | Via nuclear scale | NO | Only m_e enters explicitly |

### Parameters That Do Enter

| Parameter | Value | How It Enters | Sensitivity ∂ln(Δm)/∂ln(p) |
|-----------|-------|---------------|----------------------------|
| **m_e** | 0.511 MeV | Explicit factor | **+1** (linear) |
| **Z_6 order** | 6 | Via 36 = 6² | Fixed discrete, cannot vary |
| **q_n** | 1/3 | Via q² | **+2** (quadratic) |
| **Ring factor** | π | Denominator | **-1** (inverse) |
| **Factor 2** | 2 | Potential wells | Fixed by symmetry |

### Sensitivity Derivatives (Symbolic)

For the formula F = (8/π)m_e:

```
∂ln(F)/∂ln(m_e) = +1    (direct proportionality)
∂ln(F)/∂ln(q_n) = +2    (quadratic in q)
∂ln(F)/∂ln(π)   = -1    (inverse)
```

The key variables (m_e, π) are **fundamental constants** — no variation possible.

The variable q_n = 1/3 is derived from θ = 60° which comes from Z_6/3 = 60°.

---

## 4. What Would Break 8/π?

### FRAGILE TO (discrete structure changes):

| Change | Effect on Δm_np | New Value |
|--------|-----------------|-----------|
| Z_8 instead of Z_6 | 64/π instead of 36/π | × 64/36 ≈ 1.78 |
| Z_4 instead of Z_6 | 16/π instead of 36/π | × 16/36 ≈ 0.44 |
| q_n = 1/2 instead of 1/3 | q² = 1/4 instead of 1/9 | × 9/4 = 2.25 |
| θ_n = 45° instead of 60° | q = 2sin(22.5°)/3 ≈ 0.254 | × (0.254/0.333)² ≈ 0.58 |

### ROBUST TO (continuous parameter variations):

| Variation | Why No Effect |
|-----------|---------------|
| σ ± 10% | σ is not an independent input; it's derived from (36/π)m_e |
| δ ± 10% | δ doesn't appear in this derivation |
| L_0 ± 10% | L_0 doesn't appear in this derivation |
| w(χ) profile change | This is not a thick-brane projection calculation |
| Normalization ∫w = 1 | No projection integral involved |

---

## 5. Comparison: Two Different Δm_np Derivations in EDC

The repo contains **two** derivations with different formulas:

| Source | Formula | Value | Error | Key Parameters |
|--------|---------|-------|-------|----------------|
| Framework v2.0 | (8/π)m_e | 1.301 MeV | 0.6% | Z_6, q=1/3 |
| Book 1 Ch.9 | (5/2 + 4α)m_e | 1.292 MeV | 0.07% | D_bulk/D_mem, Dirac |

### Framework v2.0 (Z_6 Ring Model)
- Uses Z_6 symmetry of Y-junction ring oscillation
- q = 1/3 from half-Steiner angle
- σr_e² = (36/π)m_e from Z_6 normalization
- **No dependence on σ, δ, L_0 as independent parameters**

### Book 1 Chapter 9 (Dimensional Model)
- Uses 5/2 = D_bulk/D_membrane = 5/2 dimensional ratio
- Uses 4α = Dirac spinor correction
- **Different physical picture** (dimensional counting vs ring oscillation)

### Tension Between Models

Both predict Δm_np ≈ 1.29-1.30 MeV, but:
- 8/π ≈ 2.546
- 5/2 + 4α ≈ 2.529

These differ by **0.7%**. The experimental value lies between them.

**Status:** Two models coexist; neither is falsified. Need reconciliation.

---

## 6. Error Budget Form

For the canonical formula:
```
Δm_np/m_e = (8/π) × [1 + ε_Z6 + ε_q + ε_ring + ε_V3]
```

Where:
- ε_Z6 = sensitivity to discrete group (ZERO unless group changes)
- ε_q = 2 × (δq/q) = sensitivity to asymmetry parameter
- ε_ring = sensitivity to ring vs non-ring geometry
- ε_V3 = sensitivity to V ∝ q² elastic ansatz

**Current values:**
```
ε_Z6 = 0        (Z_6 is locked)
ε_q = 0         (q = 1/3 follows from θ = 60°)
ε_ring = 0      (ring geometry is postulated)
ε_V3 = 0        (elastic ansatz is postulated)
```

**All corrections are zero** because the formula is derived from discrete geometry, not continuous parameters.

---

## 7. Robust/Fragile Conclusion

### ROBUST Aspects

1. **m_e as fundamental scale** — No other mass scale enters
2. **8/π as pure geometric ratio** — Locked by Z_6 + ring
3. **No σ/δ/L_0 sensitivity** — These aren't independent inputs
4. **No profile w(χ) sensitivity** — Not a thick-brane projection

### FRAGILE Aspects

1. **Z_6 structure** — If discrete symmetry were Z_8 or Z_4, result would change
2. **Charge-angle coupling** — θ = (1-Q)×60° is [Dc], not [Der]
3. **Elastic energy ansatz** — V ∝ q² is assumed, not derived
4. **Ring oscillation model** — Assumes angular motion, not spatial deformation

### CLAIM_LEDGER Entry (Proposed)

```
CL-ΔMNP: Δm_np = 8m_e/π

Status: YELLOW

Justification:
- ROBUST to continuous parameters (σ, δ, L_0, w) because they don't enter independently
- FRAGILE to discrete structure (Z_6 → Z_N would change 36 → N²)
- Depends on 3 unproven assumptions:
  1. Charge-angle coupling [Dc]
  2. V ∝ q² elastic ansatz [Dc]
  3. Z_6 ring normalization σr_e² = (36/π)m_e [Dc]

Cross-check: (5/2 + 4α)m_e from dimensional model gives 0.7% different value

Upgrade path to GREEN:
- Derive charge-angle coupling from 5D gauge sector
- Derive 36/π from first principles
- Reconcile with (5/2 + 4α) model
```

---

## 8. Next Actions

1. **[DONE]** Document derivation spine with exact labels
2. **[DONE]** Show dimensionless form and parameter cancellations
3. **[TODO]** Reconcile 8/π with (5/2 + 4α) — why two models?
4. **[TODO]** Derive charge-angle θ = (1-Q)×60° from 5D gauge
5. **[TODO]** Derive 36/π normalization from first principles

---

## 9. Files Referenced

| File | Content |
|------|---------|
| `edc_papers/paper_3_series/00_framework_v2_0/paper/main.tex:964-1028` | Primary derivation |
| `edc_book/chapters/chapter_9_electroweak_v17.48_patched.tex:829-876` | Alternative (5/2+4α) model |
| `edc_papers/paper_3_series/08_companion_G_neutron_proton_mass_split/paper/main.tex` | κ=1/6 calibration model |
| `docs/CONCEPT_INDEX.md:CONCEPT-032` | Canonical entry |

---

*This document establishes that Δm_np = 8m_e/π is robust to continuous parameter variations but depends on discrete Z_6 structure and three [Dc] assumptions.*
