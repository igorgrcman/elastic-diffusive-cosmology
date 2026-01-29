# OP-σ-2 Resolution: N_cell = 12 Bridge

**Date:** 2026-01-29
**Problem:** 70 MeV vs 5.856 MeV tension (factor ~12)
**Status:** CANDIDATE RESOLUTION — awaiting geometric derivation of N_cell

---

## A. Tension Statement

### The Two σr_e² Values

| Model | Formula | Value | Source Anchor |
|-------|---------|-------|---------------|
| E_σ Hypothesis | σr_e² = m_ec²/α | **70.03 MeV** | Companion H main.tex:697-710 |
| Z_6 Ring | σr_e² = (36/π)m_e | **5.856 MeV** | Framework v2.0 main.tex:970 |

**Ratio:** 70.03 / 5.856 = **11.96 ≈ 12**

### Source Anchors (Exact)

**E_σ Hypothesis:**
```
File: edc_papers/paper_3_series/09_companion_H_weak_interactions/paper/main.tex
Lines: 697-710
Label: Section "Membrane Tension Derivation"

E_σ ≡ σ·r_e² = m_ec²/α = 70.0 MeV  [P]
σ = m_e³c⁴/(α³ℏ²) = 8.82 MeV/fm²  [Dc]
```

**Z_6 Ring:**
```
File: edc_papers/paper_3_series/00_framework_v2_0/paper/main.tex
Lines: 964-978
Label: Theorem "Brane Tension Formula" \label{thm:brane-tension}

σr_e² = (36/π)m_e = 5.856 MeV  [Dc]
where 36 = 6² from Z_6 symmetry
```

**V_0 = N_cell × σr_e² (current N_cell = 10):**
```
File: edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/research_targets/RT-CH3-003_NEUTRON_LIFETIME_DERIVATION.tex
Lines: 74, 156, 165, 279, 312, 325, 350

V_0 = N_cell × σr_e² ≈ 10 × 5.86 ≈ 59 MeV  [Dc]
N_cell = 10 "geometric estimate, not fitted"
```

---

## B. Algebraic Bridge: N_cell = 12

### The Key Equation

If the E_σ scale (70 MeV) and Z_6 cell scale (5.856 MeV) are related by:

```
E_σ = N_cell × (σr_e²)_Z6
```

Then:
```
N_cell = E_σ / (σr_e²)_Z6
       = (m_ec²/α) / ((36/π)m_e)
       = (π/36) × (1/α)
       = π / (36α)
       = 11.9586...
```

### N_cell = 12 Approximation

| N_cell | V_0 = N × 5.856 MeV | Error vs E_σ |
|--------|---------------------|--------------|
| 10 | 58.56 MeV | -16.4% |
| 11 | 64.41 MeV | -8.0% |
| **12** | **70.27 MeV** | **+0.35%** |
| 13 | 76.12 MeV | +8.7% |

**Result:** N_cell = 12 gives **0.35% agreement** with E_σ = 70.03 MeV.

### Exact Relation [I]

```
N_cell = π/(36α) ≈ 11.96

Approximating: N_cell ≈ 12

Residual: 12 - π/(36α) = 0.041 ≈ 0.35%
```

This suggests:
```
E_σ ≈ 12 × (36/π) × m_e = (432/π) × m_e = 137.5 × m_e

vs exact: E_σ = m_e/α = 137.04 × m_e

Error: (137.5 - 137.04)/137.04 = 0.34%
```

---

## C. Consistency Analysis

### C.1 What Changes if N_cell = 10 → 12?

**Affected quantities:**

| Quantity | Current (N=10) | New (N=12) | Change | Downstream Effect |
|----------|----------------|------------|--------|-------------------|
| V_0 (barrier) | 58.6 MeV | 70.3 MeV | +20% | τ_n increases |
| S/ℏ (action) | ~34 | ~36 | +6% | exp(S) × 7 |
| τ_n | ~830 s | ~5800 s | ×7 | Worse match |

**Problem:** N_cell = 12 worsens τ_n prediction.

### C.2 Files Requiring Update

If N_cell = 12 is adopted:

```
edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/research_targets/RT-CH3-003_NEUTRON_LIFETIME_DERIVATION.tex
  - Line 74: "10 × 5.86" → "12 × 5.86"
  - Line 156: "N_cell = 10" → "N_cell = 12"
  - Line 165: "10 × 5.856" → "12 × 5.856"
  - Line 279: "10 × σr_e²" → "12 × σr_e²"
  - Line 312: "10 ×" → "12 ×"
  - Line 325: "N_cell = 10" → "N_cell = 12"
```

### C.3 The τ_n Compensation Problem

If V_0 increases by 20% (from N=10 to N=12):
```
S ∝ √V_0 increases by ~10%
exp(S) increases by factor exp(0.1 × S) ≈ exp(3.4) ≈ 30

τ_n would increase from ~830 s to ~25,000 s (way off!)
```

**This means:** N_cell = 12 cannot be adopted for V_0 without compensating changes elsewhere.

### C.4 Resolution Hypothesis

**Two distinct scales may coexist:**

1. **E_σ = 70 MeV** = electromagnetic scale (α-related)
2. **V_0 = 60 MeV** = nuclear barrier scale (different physics)

The factor 12 connects them, but they play different roles:
- E_σ sets the fundamental membrane energy
- V_0 is the effective barrier seen by nuclear tunneling

**Alternative:** The τ_n calculation uses wrong prefactor or different effective mass.

---

## D. Geometric Meanings of 12

### D.1 Candidate: 12 = 2 × 6 (Z_2 × Z_6)

**Interpretation [Dc]:**
The Z_6 hexagonal ring has 6 cells. The factor 2 comes from the membrane having **two sides** (bulk above and below), or from **particle-antiparticle** doubling.

```
N_cell = 2 × |Z_6| = 2 × 6 = 12
```

**Breadth link:** Connects to chirality (V-A structure uses Z_2 for L/R separation).

**Source connection:** Framework v2.0 uses Z_6/Z_2 quotient for N_g = 3 generations.

### D.2 Candidate: 12 = 3 × 4 (Z_3 × Z_4)

**Interpretation [Dc]:**
- Z_3 = 3 generations (flavor)
- Z_4 = 4 Dirac components (spinor)

```
N_cell = N_g × N_Dirac = 3 × 4 = 12
```

**Breadth link:** Connects nuclear scale to flavor (generations) and weak sector (Dirac structure).

**Source connection:** Chapter 9 uses factor 4 in (5/2 + 4α) for Dirac correction.

### D.3 Candidate: 12 = 12/1 (Hexagonal Close Packing)

**Interpretation [Dc]:**
In hexagonal close packing (HCP), each sphere touches 12 neighbors. The Y-junction may have 12 neighboring cells in the thick-brane geometry.

```
N_cell = coordination number (HCP) = 12
```

**Breadth link:** Connects to 3D spatial structure of the brane (crystallography).

**Source connection:** Framework v2.0 mentions hexagonal ring geometry.

### D.4 Candidate Summary Table

| Decomposition | Meaning | Epistemic | Breadth Link |
|---------------|---------|-----------|--------------|
| 2 × 6 | Z_2 × Z_6 (sides × ring) | [Dc] | Chirality, V-A |
| 3 × 4 | N_g × N_Dirac | [Dc] | Flavor, weak |
| 12 | HCP coordination | [Dc] | Spatial geometry |

---

## E. Conclusions

### E.1 Status

**OP-σ-2 has a CANDIDATE RESOLUTION:**
```
N_cell = 12 gives 0.35% match between E_σ and Z_6 scales
```

**But it is NOT CLOSED because:**
1. No first-principles derivation of N_cell = 12
2. Adopting N_cell = 12 in τ_n calculation worsens the fit
3. Multiple geometric interpretations exist without discrimination

### E.2 Recommended Path

1. **Accept algebraic bridge as [I]:**
   ```
   E_σ ≈ 12 × (36/π) m_e  [I]
   ```

2. **Keep N_cell = 10 for nuclear barrier:**
   - The 70 MeV (E_σ) and 60 MeV (V_0) may be distinct physical scales
   - τ_n calculation should not change

3. **Open new subproblem:**
   - Derive N_cell from ring/brane geometry
   - Explain why V_0 ≠ E_σ (factor 10/12 ≈ 0.83)

### E.3 New Subproblem

**OP-σ-2a: Derive N_cell = 12 from geometry**

```yaml
id: OP-σ-2a
status: OPEN
priority: P1
claim: "N_cell = 12 connects E_σ and Z_6 ring scales"
question: "What geometric structure gives exactly 12 cells?"
candidates:
  - Z_2 × Z_6 (chirality × ring)
  - N_g × N_Dirac (flavor × spinor)
  - HCP coordination number
next_test: "Check which decomposition is consistent with other EDC predictions"
```

---

## F. File References

| File | Lines | Content |
|------|-------|---------|
| `edc_papers/paper_3_series/09_companion_H_weak_interactions/paper/main.tex` | 697-710 | E_σ hypothesis |
| `edc_papers/paper_3_series/00_framework_v2_0/paper/main.tex` | 964-978 | Z_6 ring σr_e² |
| `edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/research_targets/RT-CH3-003_NEUTRON_LIFETIME_DERIVATION.tex` | 74, 156, 279 | N_cell = 10 usage |
| `docs/SIGMA_DEPENDENCY_AUDIT.md` | — | Parent audit |

---

*This document establishes N_cell = 12 as a candidate resolution for OP-σ-2, achieving 0.35% agreement, but notes that full adoption requires geometric derivation and τ_n recalibration.*
