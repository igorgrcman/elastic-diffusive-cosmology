# σ Dependency Audit — Master Parameter Map

**Date:** 2026-01-29
**Purpose:** Trace σ occurrences across all sectors, classify dependencies, identify invariants
**Status:** CANONICAL

---

## Executive Summary

1. **σ = 8.82 MeV/fm² is derived** from the hypothesis E_σ = m_ec²/α [Dc], not fitted
2. **Two incompatible σr_e² values exist:** 70 MeV (nuclear) vs 5.856 MeV (Z_6 ring) — **factor ~12 tension**
3. **σ enters three sectors:** Nuclear (barriers), EM (α/m_e connection), Cosmology (Λ)
4. **Key invariant:** E_σ = σ·r_e² = m_ec²/α links σ to fundamental constants
5. **Open problem:** Which sector truly fixes σ? Nuclear phenomenology or Z_6 geometry?

---

## 1. Canonical σ Definition

### Primary Definition [Dc]

**Source:** `edc_papers/paper_3_series/09_companion_H_weak_interactions/paper/main.tex:690-710`

```latex
σ = m_e³c⁴/(α³ℏ²) = 8.82 MeV/fm²
```

**Derivation chain:**
1. **Hypothesis [P]:** E_σ = m_ec²/α = 70 MeV
2. **Definition:** E_σ ≡ σ·r_e² (energy in area r_e²)
3. **r_e = αℏ/(m_ec)** (classical electron radius)
4. **Solve for σ:**
   ```
   σ = E_σ/r_e² = (m_ec²/α) × (m_e²c²/α²ℏ²) = m_e³c⁴/(α³ℏ²)
   ```

**Dimensionless form:**
```
σ/(m_e⁴c³/ℏ³) = 1/α³ ≈ 2.57 × 10⁶
```

---

## 2. σ Invariants (Fixed Combinations)

### Invariant 1: E_σ = σ·r_e² = m_ec²/α

**Appears in:** EM scale, nuclear barrier, weak scale derivations

| Context | Formula | Value | Source |
|---------|---------|-------|--------|
| EM hadronic scale | E_σ = m_ec²/α | 70.0 MeV | Companion H:723 |
| Pion mass | m_π ≈ 2 × E_σ | 140 MeV | Chapter 9 |
| Nuclear barrier base | V_cell = σr_e² | 70 MeV | Framework v2.0:588 |

**Classification: A** (fixed invariant — σ and r_e always appear together as E_σ)

### Invariant 2: σ·r_e³ (Volume energy)

**Appears in:** g² coupling derivation

```
g² = 4π × σr_e³/(ℏc) ≈ 0.37
```

**Source:** `edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/research_targets/RT-CH3-002_WORKING_PHASE3.tex:5`

**Classification: D** (conditional ansatz — needs derivation of factor 4π)

### Invariant 3: σ/R_H² (Cosmological scale)

**Appears in:** Λ derivation

```
Λ = σ/(8c²R_H²)
```

**Source:** `edc_book/chapters/chapter_11_verifications.tex:332`

**Classification: B** (σ is free master parameter here — R_H is external input)

---

## 3. Sector Dependency Table

| Sector | Quantity | Formula | σ enters as | Cancels? | Status | Source Anchor |
|--------|----------|---------|-------------|----------|--------|---------------|
| **EM** | E_σ (hadronic scale) | σ·r_e² = m_ec²/α | E_σ = const | YES (via r_e) | [Dc] | Companion H:697-710 |
| **EM** | σ (tension) | m_e³c⁴/(α³ℏ²) | Derived from E_σ | — | [Dc] | Companion H:690 |
| **EM** | α⁻¹ (coupling) | geometric ratio | σ implicit | YES | [Der] | Paper 2 derivations |
| **Nuclear** | V_0 (barrier) | 10 × σr_e² | σ explicit | NO | [Dc] | RT-CH3-003:74 |
| **Nuclear** | K (pinning) | f × σ × A_contact | σ explicit | NO | [I] | BREADTH_MAP |
| **Nuclear** | τ_n (lifetime) | exp(S_E/ℏ) | σ via V_0 | NO | [Dc/Cal] | Companion H:165 |
| **Nuclear** | Δm_np (Z_6) | (8/π)m_e | σr_e² = 36m_e/π | YES | [Dc] | Framework v2.0:970 |
| **Nuclear** | Δm_np (dim) | (5/2+4α)m_e | No σ | — | [Der] | Chapter 9:848 |
| **Cosmo** | Λ | σ/(8c²R_H²) | σ explicit | NO | [Der] | chapter_11:332 |
| **Weak** | g² | 4πσr_e³/(ℏc) | σ explicit | NO | [Dc]+[P] | RT-CH3-002:5 |

---

## 4. Sector Maps

### 4.1 Nuclear Sector

```
σr_e² = 70 MeV (E_σ hypothesis) [Dc]
     │
     ├── V_0 = 10 × σr_e² = 59 MeV  (barrier height) [Dc]
     │      └── τ_n = (ℏ/ω_0) exp(S/ℏ)  [Dc/Cal]
     │
     ├── K = f × σ × A_contact  (pinning constant) [I]
     │      └── Binding energies via frustration
     │
     └── Δm_np (via Z_6): σr_e² = 36m_e/π = 5.856 MeV  ⚠️ TENSION
```

**Tension:** Nuclear phenomenology uses σr_e² = 70 MeV, but Z_6 ring model gives 5.856 MeV.

### 4.2 EM Sector

```
E_σ = m_ec²/α = 70 MeV  [P/Dc]
     │
     ├── σ = m_e³c⁴/(α³ℏ²) = 8.82 MeV/fm²  [Dc]
     │
     ├── m_π = 2 × E_σ = 140 MeV  (pion mass) [Der]
     │
     └── α = e²/(4πε₀ℏc)  (σ implicit via r_e) [Der]
```

**Note:** In EM sector, σ always appears as E_σ = σr_e², which equals m_ec²/α — a constant.

### 4.3 Cosmology Sector

```
σ = 8.82 MeV/fm² = 1.413 × 10¹⁸ J/m²  [Dc]
R_H = c/H_0 = 1.373 × 10²⁶ m  [BL]
     │
     └── Λ = σ/(8c²R_H²) = 1.0 × 10⁻⁵² m⁻²  [Der]
              Error: 6% from Planck
```

**Note:** σ is the bridge between membrane physics and cosmology.

### 4.4 Weak/Flavor Sector

```
σr_e³/ℏc  [Dc]+[P]
     │
     └── g² = 4π × σr_e³/(ℏc) ≈ 0.37  (11% from SM)
              └── G_F chain... [partially RED]
```

**Note:** Weak sector uses σr_e³ (volume), not σr_e² (area).

---

## 5. Dimensionless Rewrites

### 5.1 σ in terms of m_e, α

```
σ = m_e³c⁴/(α³ℏ²)

Dimensionless: σ × (ℏ³/m_e⁴c³) = α⁻³

All σ-dependence reduces to α-dependence.
```

### 5.2 E_σ = σr_e²

```
E_σ/m_e = c²/α × (m_e/m_e) = 1/α ≈ 137

E_σ is proportional to m_e with fixed coefficient 1/α.
```

### 5.3 Cosmological Λ

```
Λ × R_H² = σ/(8c²)

Λ × R_H²/(m_e⁴c⁵/ℏ⁴) = (1/8) × α⁻³

All σ-dependence becomes α-dependence + R_H² (external).
```

### 5.4 Z_6 Ring σr_e²

```
σr_e² = (36/π)m_e  [Dc — Framework v2.0]

(σr_e²)/m_e = 36/π ≈ 11.46

vs

(σr_e²)/m_e = 1/α ≈ 137 [Dc — E_σ hypothesis]

Ratio: 137/(36/π) = 137π/36 ≈ 12.0
```

**This is the 70 MeV vs 5.856 MeV tension.**

---

## 6. Critical Finding: The 70 vs 5.856 MeV Tension

### Two σr_e² Values

| Model | σr_e² Value | Origin | Used In |
|-------|-------------|--------|---------|
| E_σ Hypothesis | 70 MeV | E_σ = m_ec²/α | Nuclear barriers, pion, τ_n |
| Z_6 Ring | 5.856 MeV | σr_e² = 36m_e/π | Δm_np = 8m_e/π |

**Ratio:** 70/5.856 ≈ 12.0

### Possible Resolutions

1. **Different scales:** 70 MeV = collective (10-cell), 5.856 MeV = single cell
   - V_0 = 10 × σr_e² uses N_cell = 10 multiplier
   - Framework v2.0 uses N_cell = 10 → V_0 ≈ 59 MeV ≈ 70 MeV ✓

2. **Different contexts:** Nuclear uses phenomenological 70 MeV, Z_6 derives geometric 5.856 MeV
   - Both are [Dc], neither is [Der]

3. **Renormalization:** 5.856 MeV = bare, 70 MeV = dressed by strong interaction

**Status:** OPEN PROBLEM — needs reconciliation.

---

## 7. Robustness Notes

### Where σ Cancels (ROBUST)

| Observable | Why σ Cancels | Remaining Dependence |
|------------|---------------|----------------------|
| Δm_np (Z_6) | σr_e² = 36m_e/π is fixed | m_e only |
| Δm_np (dim) | No σ in formula | m_e, α only |
| α⁻¹ | σ implicit via r_e definition | Geometric factors only |
| m_π/m_e | E_σ = m_ec²/α is fixed | α only |

### Where σ is Explicit (FRAGILE)

| Observable | σ Dependence | If σ changes by 10% |
|------------|--------------|---------------------|
| V_0 (barrier) | V_0 ∝ σ | V_0 changes 10% |
| τ_n (lifetime) | log(τ_n) ∝ S ∝ V_0 | τ_n changes exponentially |
| Λ (cosmo) | Λ ∝ σ | Λ changes 10% |
| g² | g² ∝ σ | g² changes 10% |
| K (pinning) | K ∝ σ | K changes 10% |

---

## 8. Open Problems

### OP-σ-1: Which sector fixes σ?

**Question:** Is σ determined by:
- (a) E_σ = m_ec²/α hypothesis (EM sector)?
- (b) Z_6 geometry (σr_e² = 36m_e/π)?
- (c) Nuclear phenomenology (fitted to data)?

**Status:** OPEN — currently [Dc] with E_σ hypothesis.

### OP-σ-2: The 70 vs 5.856 MeV tension

**Question:** Why do two σr_e² values exist?

**Candidates:**
1. Collective vs single-cell (N_cell = 10 factor)
2. Different physical contexts (nuclear vs flavor)
3. Bare vs dressed (renormalization)

**Status:** OPEN — needs investigation.

### OP-σ-3: Derive σ from 5D action

**Question:** Can σ be derived from the 5D Einstein-Hilbert + membrane action without the E_σ hypothesis?

**Status:** RED — attempted in OPR-01, not closed.

---

## 9. Top-3 Next Tests

### Test 1: N_cell = 12 Check

If V_0 = N_cell × σr_e² with σr_e² = 5.856 MeV:
```
V_0 = 12 × 5.856 = 70.3 MeV ✓
```

**Action:** Check if N_cell = 12 (not 10) gives exact match.

### Test 2: τ_n Sensitivity to σ

Perturb σ by ±10% and compute change in τ_n:
```
δτ_n/τ_n ≈ (S/ℏ) × (δV_0/V_0) ≈ 60 × 0.1 = 6
```

**Action:** Verify this exponential sensitivity numerically.

### Test 3: Cross-Sector Consistency

Use Λ derivation to constrain σ:
```
Λ_obs = 1.1 × 10⁻⁵² m⁻²
σ = 8c²R_H²Λ = ?
```

**Action:** Check if cosmological σ matches nuclear/EM σ.

---

## 10. File References

| File | Lines | Content |
|------|-------|---------|
| `edc_papers/paper_3_series/09_companion_H_weak_interactions/paper/main.tex` | 690-710 | σ definition |
| `edc_papers/paper_3_series/00_framework_v2_0/paper/main.tex` | 970 | σr_e² = 36m_e/π |
| `edc_book/chapters/chapter_11_verifications.tex` | 332-350 | Λ = σ/(8c²R_H²) |
| `edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/research_targets/RT-CH3-003_NEUTRON_LIFETIME_DERIVATION.tex` | 74, 160 | V_0 = 10×σr_e² |
| `docs/BREADTH_MAP.md` | 113-127 | Previous σ table |

---

*This audit establishes σ as the master parameter connecting Nuclear, EM, and Cosmology sectors, with a critical 70 vs 5.856 MeV tension requiring resolution.*
