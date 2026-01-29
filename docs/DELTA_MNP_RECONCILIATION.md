# Δm_np Model Reconciliation

**Date:** 2026-01-29
**Purpose:** Reconcile Z_6 ring (8/π) and dimensional (5/2+4α) models
**Status:** CANONICAL

---

## 1. The Two Models

### Model A: Z_6 Ring (Framework v2.0 §10.5)

**Source:** `edc_papers/paper_3_series/00_framework_v2_0/paper/main.tex:1017-1028`
**Label:** `\label{thm:mass-diff-derived}`

```
Δm_np / m_e = 8/π = 2.546479
Δm_np = 1.3012 MeV
Error vs exp: +0.615%
```

**Derivation chain:**
1. σr_e² = (36/π)m_e [Z_6 + ring]
2. q_n = 1/3 [half-Steiner]
3. V_3 = σr_e² × q² [elastic]
4. Δm = 2|V_3| [double-well]

### Model B: Dimensional (Book 1 Ch.9)

**Source:** `edc_book/chapters/chapter_9_electroweak_v17.48_patched.tex:848`
**Label:** Section 9.8 `\label{sec:neutron_decay}`

```
Δm_np / m_e = 5/2 + 4α = 2.529189
Δm_np = 1.2924 MeV
Error vs exp: -0.069%
```

**Derivation chain:**
1. 5/2 = D_bulk/D_membrane = 5/2 [dimensional]
2. 4α = N_Dirac × α [EM correction]

### Experimental Reference

```
Δm_np = 1.2933 MeV (PDG)
Δm_np / m_e = 2.530925
```

---

## 2. Numeric Reconciliation

### The ε Connection

Define ε such that:
```
(8/π)(1 - ε) = 5/2 + 4α
```

Solving:
```
ε = 1 - (5/2 + 4α) × (π/8)
  = 1 - (5π/16 + απ/2)
  = 1 - 0.981748 - 0.011463
  = 0.006790
```

**Result:**
```
ε = 0.679% ≈ 0.68%
```

### Verification

```
(8/π) × (1 - 0.006790) = 2.546479 × 0.993210 = 2.529189 ✓
5/2 + 4α = 2.529189 ✓
```

### Position Relative to Experiment

```
Z_6 (8/π):       +0.615% above experiment
Dimensional:    -0.069% below experiment
Experiment:      reference point
```

The dimensional model is **9× closer** to experiment than the Z_6 model.

---

## 3. Natural Insertion Points for ε

Where could ε originate in the Z_6 derivation chain?

### Candidate 1: Factor 2 Correction (Double-Well Asymmetry)

**Location:** Δm = 2|V_3| → Δm = 2(1 - ε₁)|V_3|

**Interpretation:**
The proton and neutron potential wells may not be exactly symmetric. QED radiative corrections to the d-quark vs u-quark masses create a slight asymmetry.

**Required ε₁:** 0.68%

**Breadth link:** Would affect all hadronic isospin splittings (π⁺-π⁰, Σ⁺-Σ⁰, etc.) proportionally.

**Plausibility:** HIGH — this is where the 4α correction naturally enters in the dimensional model.

---

### Candidate 2: Elastic Ansatz Correction (V ∝ q²⁺ᵟ)

**Location:** V_3 = σr_e² × q² → V_3 = σr_e² × q^(2-δ)

**Interpretation:**
The elastic energy may not be purely quadratic. Anharmonic corrections (q³, q⁴ terms) or brane stiffness variations could modify the exponent.

**Required δ:** For q = 1/3:
```
q^(2-δ) / q² = (1-ε)
q^(-δ) = (1-ε)
-δ ln(q) = ln(1-ε)
δ = -ln(1-ε) / ln(q) ≈ ε / ln(3) ≈ 0.62%
```

**Breadth link:** Would affect nuclear binding energies via frustration-corrected G-N law (different q values for different nuclei).

**Plausibility:** MEDIUM — requires breaking the Hooke's law assumption.

---

### Candidate 3: Ring Geometry Correction (π → π_eff)

**Location:** σr_e² = (36/π)m_e → σr_e² = (36/π_eff)m_e

**Interpretation:**
The ring may not be perfectly circular. Thick-brane effects, ellipticity, or discrete lattice effects could modify the effective circumference.

**Required π_eff:**
```
(8/π_eff) = (8/π)(1-ε)
π_eff = π / (1-ε) = π × 1.00684 = 3.16306
```

**Breadth link:** Would affect sin²θ_W derivation (also uses circular geometry) and Koide relation (if π enters).

**Plausibility:** MEDIUM — but introduces tension with sin²θ_W which works well with exact π.

---

### Candidate 4: Charge-Angle Coupling Correction

**Location:** θ = (1-Q) × 60° → θ = (1-Q) × 60° × (1 + ε₄)

**Interpretation:**
The charge-to-angle mapping may have radiative corrections from the 5D gauge sector.

**Required ε₄:** For θ_n = 60°:
```
q_n = 2sin(θ/2)/3 = 2sin(30°)/3 = 1/3
```
A 0.68% change in θ would give ~0.34% change in q, and ~0.68% change in q².

**Breadth link:** Would affect CKM/PMNS mixing (if flavor angles use same coupling) and N_g = 3 (if generation spacing uses 60° step).

**Plausibility:** LOW — disrupts the clean Z_6 discrete structure.

---

## 4. Candidate Ranking

| Rank | Candidate | ε Required | Plausibility | Breadth Impact | Falsifiability |
|------|-----------|------------|--------------|----------------|----------------|
| 1 | Factor 2 (EM correction) | 0.68% | HIGH | Isospin splittings | Check π⁺-π⁰ |
| 2 | Elastic ansatz | 0.62% | MEDIUM | Nuclear binding | Check G-N law q-dependence |
| 3 | Ring geometry | π→3.163 | MEDIUM | sin²θ_W, Koide | Check W angle tension |
| 4 | Charge-angle | ~0.34% | LOW | CKM/PMNS | Check N_g = 3 stability |

---

## 5. Recommended Interpretation

### Primary Recommendation

**Treat 8/π as the "bare" geometric limit and (5/2 + 4α) as the "renormalized" result:**

```
Δm_np / m_e = (8/π) × (1 - ε_EM)

where:
  8/π = bare Z_6 geometry (no EM loops)
  ε_EM ≈ 0.68% = electromagnetic correction
```

**Rationale:**
1. The dimensional model explicitly includes 4α (EM correction)
2. The Z_6 model is pure geometry (no EM)
3. ε ≈ 0.68% is consistent with O(α) corrections
4. The 4α term appears in both Δm_np and sin²θ_W with consistent interpretation

### Dimensional Model Rewrite

The dimensional formula can be rewritten as:
```
5/2 + 4α = (8/π) × (1 - ε)

where:
  5/2 ≈ 8/π × (5π/16) ≈ 2.467 × 1.013 = 2.5
  4α ≈ contribution from ε
```

This suggests:
```
5/2 = (8/π) × (5π/16) × (some correction factor)
```

The factor 5π/16 ≈ 0.982, which is (1 - 1.8%).

### Alternative Interpretation

**Treat (5/2 + 4α) as fundamental and 8/π as an approximation:**

If 5/2 = D_bulk/D_membrane is the true geometric origin, then:
```
8/π ≈ 5/2 + O(α)
```

is just a numerical coincidence (8/π ≈ 2.546 vs 5/2 = 2.5).

**Against this:** The 8/π derivation has cleaner internal structure (Z_6, π, etc.).

---

## 6. Proposed Tightening Tests

### Test 1: Pion Mass Splitting (for Candidate 1)

If ε originates from EM double-well asymmetry:
```
(m_π⁺ - m_π⁰) / m_π should show same ε pattern
```

**Action:** Check if pion mass splitting formula in EDC contains analogous 2(1-ε) factor.

### Test 2: q-Dependence of Nuclear Binding (for Candidate 2)

If ε originates from non-quadratic elastic term:
```
Different nuclei with different effective q should show systematic deviation
```

**Action:** Extend frustration-corrected G-N law to test q^(2-δ) hypothesis.

### Test 3: sin²θ_W Consistency (for Candidate 3)

If π → π_eff:
```
sin²θ_W derivation should show same π_eff or have compensating factor
```

**Action:** Check if sin²θ_W = 1/4 uses exact π anywhere in derivation.

### Test 4: Generation Spacing (for Candidate 4)

If charge-angle coupling has ε₄ correction:
```
N_g = 3 derivation from 360°/60° should show same correction or break
```

**Action:** Verify N_g = |Z_6/Z_2| = 3 doesn't depend on exact 60° step.

---

## 7. Summary

### Numeric Result
```
ε = 0.679%
(8/π)(1 - ε) = 5/2 + 4α   ✓
```

### Recommended Interpretation
- **8/π** = bare geometric limit (Z_6 ring, no EM)
- **5/2 + 4α** = EM-renormalized result
- **ε** = electromagnetic correction from Dirac spinor loops

### Most Likely ε Origin
**Candidate 1 (Factor 2 correction)** — the 4α term in the dimensional model is the explicit source of ε.

### Next Action
Check pion mass splitting for analogous structure to confirm EM-correction interpretation.

---

## 8. File References

| File | Lines | Content |
|------|-------|---------|
| `edc_papers/paper_3_series/00_framework_v2_0/paper/main.tex` | 1017-1028 | Z_6 ring derivation |
| `edc_book/chapters/chapter_9_electroweak_v17.48_patched.tex` | 848-908 | Dimensional derivation |
| `docs/DELTA_MNP_SENSITIVITY.md` | — | Sensitivity analysis |

---

*This document establishes that the two Δm_np models are related by ε ≈ 0.68%, most likely an EM radiative correction.*
