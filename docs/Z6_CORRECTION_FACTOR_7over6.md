# Z₆ Correction Factor k = 7/6 — Hypothesis Note

**Date:** 2026-01-29
**Status:** [Dc] — Derived Conditional (hypothesis, not proven)
**Purpose:** Formalize the candidate discrete correction factor k = 7/6 ≈ 1 + 1/|Z₆|

---

## A. Executive Summary (5 Bullets)

1. **Observation from pion check:** r_π ≈ (7/6) × 4α with k = 1.166 ≈ 7/6
2. **Natural form:** 7/6 = 1 + 1/6 = 1 + 1/|Z₆| suggests discrete correction to continuum average
3. **Hypothesis [Dc]:** First-order discrete correction on Z₆ ring is multiplicative (1 + 1/6)
4. **Breadth potential:** May appear in ε-dressing, N_cell corrections, overlap prefactors
5. **Status:** YELLOW — economical but unproven; derivation would require discrete averaging formalism

---

## B. Observation

### B.1 Source: Pion Splitting ε-Check

**Anchor:** `docs/PION_SPLITTING_EPSILON_CHECK.md` Section D.3

From the pion mass splitting analysis:
```
r_π = Δm_π / m_π0 = 3.403%
r_π / (4α) = 3.403% / 2.919% = 1.166

Most economical form:
Δm_π ≈ (7/6) × 4α × m_π0   [I]
```

The factor 7/6 = 1.1667 matches k = 1.166 to 0.06%.

### B.2 Numeric Identity

```
7/6 = 1 + 1/6 = 1 + 1/|Z₆|

where |Z₆| = 6 is the order of the discrete symmetry group.
```

This suggests a universal structure: **continuum value × (1 + 1/N)** where N = |G| for discrete group G.

---

## C. Hypothesis [Dc]

### C.1 Statement

**Hypothesis:** When a Z₆-symmetric quantity is computed as a discrete average over the 6 sectors, the first correction to the continuum limit is multiplicative (1 + 1/6).

Formally:
```
⟨O⟩_discrete = ⟨O⟩_continuum × (1 + 1/|Z₆|) + O(1/|Z₆|²)
```

### C.2 Geometric Interpretations

#### Interpretation 1: Corner Weighting

The Z₆ hexagonal ring has 6 vertices. If each vertex contributes a boundary correction of weight 1/6 to its cell, the total correction is:
```
1 + (6 × 1/6) / 6 = 1 + 1/6 = 7/6
```

This arises from **counting each corner once but distributing it across 6 sectors**.

#### Interpretation 2: Boundary Cell Fraction

In a discrete ring of N cells, the "boundary effect" per cell is 1/N of the total boundary. For N = 6:
```
Bulk contribution: 1
Boundary contribution: 1/N = 1/6
Total: 1 + 1/6 = 7/6
```

This is analogous to finite-size corrections in lattice theories.

#### Interpretation 3: Adjacency Count

Each Z₆ sector has 2 adjacent neighbors. The adjacency correction per sector is:
```
(2 neighbors) / (2 × N sectors) = 1/N = 1/6
```

Adding to bulk: 1 + 1/6 = 7/6.

### C.3 Epistemic Status

| Aspect | Status |
|--------|--------|
| Numeric match | Excellent (0.06%) |
| Geometric interpretation | Multiple candidates (not unique) |
| Derivation from Z₆ action | NOT DONE |
| Independence from α | UNCLEAR |

**Classification:** [Dc] — Derived Conditional on discrete averaging hypothesis

---

## D. Breadth Links

### D.1 Δm_np ε-Dressing

**Source:** `docs/DELTA_MNP_RECONCILIATION.md`

The ε = 0.679% connects bare (8/π) and dressed (5/2+4α) models:
```
(8/π)(1 - ε) = 5/2 + 4α
```

**Potential connection:**
If the 4α term in Δm_np also carries a (7/6) factor at some stage:
```
ε_effective = (7/6) × ε_bare ?
```

**Test:** Check if ε / (1/6) ≈ 4.1% is a natural scale.
Result: 0.679% / (1/6) = 4.07%, close to 4α = 2.92%. Not exact, but same order.

### D.2 N_cell Counting Corrections

**Source:** `docs/OP-SIGMA-2_NCELL12_RESOLUTION.md`

The N_cell = 12 bridge connects E_σ (70 MeV) and Z₆ cell scale (5.856 MeV):
```
E_σ = N_cell × (σr_e²)_Z6
N_cell = π/(36α) ≈ 11.96 → 12
```

**Potential connection:**
If N_cell has discrete correction:
```
N_cell_eff = 12 × (1 + 1/6) = 14  ?
```

**Test:** Does 14 × 5.856 = 82 MeV appear anywhere? (Not obviously.)

Alternatively, if the "12" itself contains a (7/6):
```
12 = 2 × 6 = 2 × |Z₆|
If corrected: 12 × (6/7) = 10.3 ≈ 10 (current N_cell in τ_n)
```

This could explain why τ_n uses N_cell = 10 while E_σ/σr_e² gives 12!

### D.3 Overlap Suppression Prefactors

**Source:** `edc_papers/_shared/lemmas/projection_reduction_lemma.tex`

Projection integrals have the form:
```
⟨K⟩_w = ∫ dχ w(χ) K(χ)
```

If the weight function w(χ) is discrete (step function on Z₆ sectors), the integral becomes a sum:
```
⟨K⟩_discrete = (1/6) Σ_{i=1}^{6} K_i
```

**Potential connection:**
The trapezoidal rule correction for periodic functions on N points is O(1/N²), but for non-smooth K, the correction could be O(1/N) = O(1/6).

---

## E. Falsification

### E.1 Universality Test

If (7/6) is a universal Z₆ discrete correction, it should appear in **all** Z₆-based quantities with the same sign and magnitude.

**Falsification criterion:**
If any quantity requires k ≠ 7/6 (specifically k < 1 or k > 4/3) for the same discrete-averaging mechanism, reject universality.

### E.2 Sectors to Check

| Sector | Quantity | Expected k | Status |
|--------|----------|------------|--------|
| Pion | r_π / 4α | 7/6 | MATCH (0.06%) |
| Nucleon | ε in Δm_np | TBD | Not directly tested |
| N_cell | 12 vs 10 | 6/7 = 0.857 | Inverse pattern? |
| Weak | sin²θ_W corrections | TBD | Check RG logs |

### E.3 Failure Modes

1. **Sign flip:** If any sector requires (1 - 1/6) instead of (1 + 1/6), mechanism is not universal
2. **Wrong magnitude:** If k differs by >20% from 7/6 in same-mechanism quantity
3. **No pattern:** If corrections appear random across sectors

---

## F. Upgrade Roadmap

### F.1 What Would Constitute [Der]

To upgrade from [Dc] to [Der], need explicit derivation showing:

1. **Discrete averaging on Z₆:** Define the discrete average operation on the Z₆ ring/graph
2. **Continuum limit:** Show that continuum limit recovers expected bare value
3. **First correction:** Derive that first-order correction is exactly 1/|Z₆| = 1/6
4. **Sign:** Prove correction is additive (not subtractive)

### F.2 Candidate Derivation Paths

| Path | Method | Difficulty |
|------|--------|------------|
| 1 | Discrete Fourier transform on Z₆ | MEDIUM |
| 2 | Lattice action finite-size effects | MEDIUM |
| 3 | Graph Laplacian eigenvalue correction | HARD |
| 4 | Ring tiling boundary counting | EASY (but less rigorous) |

### F.3 Recommended First Step

**Path 4 (Ring tiling):**
1. Define Z₆ as hexagonal ring with 6 cells
2. Compute average of test function over cells
3. Compare to circular integral
4. Extract correction factor analytically

**Expected result:** If test function is linear across cell, correction = 1/12. If quadratic, correction = 1/6. Verify which applies to EDC observables.

---

## G. Derivation Attempt (2026-01-29)

### G.1 Result: DERIVED (Mathematical)

The factor k = 7/6 is derived from discrete vs continuum averaging under the **equal corner share normalization**.

**Lemma source:** `edc_papers/_shared/lemmas/z6_discrete_averaging_lemma.tex`
**Verification code:** `edc_papers/_shared/code/z6_discrete_average_check.py`

### G.2 Key Result

For test function f(θ) = c + a cos(Nθ) with Z_N symmetry:
```
R = <f>_disc / <f>_cont = 1 + a/c
```

Under **equal corner share normalization** (a/c = 1/N):
```
R = 1 + 1/N
```

For Z₆ (N = 6):
```
R = 1 + 1/6 = 7/6 ✓
```

### G.3 Verification Output

```
[Test 3] Z6 Specific: The 7/6 Factor
  Discrete average:  1.166667
  Continuum average: 1.000000
  Ratio R = 1.166667
  Expected: 7/6 = 1.166667
  Match: True

[Test 4] Pion Observation Match
  k_observed = r_π / 4α = 1.165834
  k_theory   = 7/6      = 1.166667
  Difference: -0.07%
```

### G.4 Epistemic Status Update

| Component | Status | Note |
|-----------|--------|------|
| Mathematical lemma | [Der] | Clean derivation from Fourier mode |
| Equal corner share normalization | [Dc] | Hypothesis: corner excess = 1/N of mean |
| Pion application | [I] | Pattern match (0.07%), not derived from action |

### G.5 Limitation

The derivation requires the **specific normalization** a/c = 1/N. This is not derived from the 5D action — it's a hypothesis about how Z₆ anisotropy manifests in physical quantities.

**What remains [Dc]:** The claim that physical Z₆-symmetric quantities have this normalization.

---

## H. Reference Anchors

| Document | Content |
|----------|---------|
| `docs/PION_SPLITTING_EPSILON_CHECK.md` | Original observation (Section D.3) |
| `docs/DELTA_MNP_RECONCILIATION.md` | ε = 0.679% bridge |
| `docs/OP-SIGMA-2_NCELL12_RESOLUTION.md` | N_cell = 12 vs 10 tension |
| `docs/BREADTH_SYNTHESIS_2026-01-29.md` | Cross-sector overview |
| `edc_papers/_shared/lemmas/z6_discrete_averaging_lemma.tex` | Mathematical derivation |
| `edc_papers/_shared/code/z6_discrete_average_check.py` | Numerical verification |

---

*Updated 2026-01-29: Mathematical derivation complete [Der]. Physical normalization hypothesis remains [Dc].*
