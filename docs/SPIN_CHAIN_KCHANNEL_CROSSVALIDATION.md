# Spin Chain k-Channel Cross-Validation

**Created:** 2026-01-29
**Status:** GREEN — mathematical mechanism confirmed
**Code:** `edc_papers/_shared/code/spin_chain_kchannel_ed_test.py`

---

## EDC-Safe Framing

**What this test validates:**
- The mathematical mechanism of discrete vs continuum averaging
- The formula R = 1 + a/c for Z_N symmetric weighting functions
- Under "equal corner share" (a/c = 1/N): R = 1 + 1/N

**What this test does NOT validate:**
- EDC-specific predictions about pions, N_cell, or nuclear physics
- Any claim that spin chains are described by EDC
- The physical origin of the "equal corner share" normalization in EDC contexts

**Correct interpretation:**
> "The discrete averaging mechanism underlying EDC's k-channel correction appears in
> independent physical systems. This confirms the mathematical formula, not the
> physics-specific applications."

---

## Model and Observable Definitions

### Physical System

**Model:** XX spin chain with periodic boundary conditions

```
H = -J Σ_{n=0}^{N-1} (S^x_n S^x_{n+1} + S^y_n S^y_{n+1})
```

where `S^a = (1/2)σ^a` and indices are mod N (periodic BC).

### Local Energy Density

```
o_n = ⟨ψ_0|h_n|ψ_0⟩
```

where `h_n` is the local Hamiltonian for bond (n, n+1) and `|ψ_0⟩` is the ground state.

**Property:** In translational-invariant ground state, `o_n ≈ ō` (constant).

### Z_N Symmetric Weighting Function

```
f(θ) = c + a·cos(Nθ)
θ_n = 2πn/N   (angular position of site n)
```

### Discrete vs Continuum Observables

**Discrete sampling:**
```
O_disc = (1/N) Σ_{n=0}^{N-1} f(θ_n) · o_n
```

**Continuum average:**
```
O_cont = (1/2π) ∫_0^{2π} f(θ) dθ · ō = c · ō
```

(The cos(Nθ) term integrates to zero.)

### Averaging Ratio

```
R = O_disc / O_cont
```

**Why this is an "averaging observable":**
- Discrete: samples at N symmetric points where cos(Nθ_n) = cos(2πn) = 1
- Continuum: averages over full circle where cos integrates to zero
- The discrete sampling "sees" the Z_N Fourier mode that continuum washes out

---

## Theoretical Prediction

For translational-invariant state (o_n ≈ ō):

```
O_disc = (1/N) Σ [c + a·cos(N·2πn/N)] · ō
       = (1/N) Σ [c + a·1] · ō
       = (c + a) · ō

O_cont = c · ō

R = (c + a) / c = 1 + a/c
```

Under **equal corner share normalization** (a/c = 1/N):

```
R = 1 + 1/N = k(N)
```

---

## Results

### Summary Table

| N | R_num (a/c=1/N) | R_theory | 1+1/N | err vs theory | err vs 1+1/N | Status |
|---|-----------------|----------|-------|---------------|--------------|--------|
| 3 | 1.333333333333 | 1.3333333333 | 1.3333333333 | 2.22e-16 | 2.22e-16 | **PASS** |
| 4 | 1.250000000000 | 1.2500000000 | 1.2500000000 | 0.00e+00 | 0.00e+00 | **PASS** |
| 5 | 1.200000000000 | 1.2000000000 | 1.2000000000 | 2.22e-16 | 2.22e-16 | **PASS** |
| 6 | 1.166666666667 | 1.1666666667 | 1.1666666667 | 0.00e+00 | 0.00e+00 | **PASS** |
| 8 | 1.125000000000 | 1.1250000000 | 1.1250000000 | 0.00e+00 | 0.00e+00 | **PASS** |
| 10 | 1.100000000000 | 1.1000000000 | 1.1000000000 | 2.22e-16 | 2.22e-16 | **PASS** |
| 12 | 1.083333333333 | 1.0833333333 | 1.0833333333 | 0.00e+00 | 0.00e+00 | **PASS** |

### Translational Invariance Check

| N | σ/|μ| of o_n | Quality |
|---|--------------|---------|
| 3 | 1.67e-16 | exact |
| 4 | 0.00e+00 | exact |
| 5 | 2.17e-16 | exact |
| 6 | 1.67e-16 | exact |
| 8 | 2.48e-16 | exact |
| 10 | 3.21e-16 | exact |
| 12 | 3.07e-16 | exact |

All variations are at machine precision (floating-point rounding), confirming
translational invariance of the ground state.

---

## Verdict

### Status: **GREEN**

**Mathematical mechanism confirmed:**
- R = 1 + a/c holds to machine precision for all N tested
- Under equal corner share (a/c = 1/N): R = k(N) = 1 + 1/N exactly
- Errors are at floating-point limit (~10⁻¹⁶)

### What this establishes

1. **The averaging ratio formula R = 1 + a/c is correct** [Der]
   - Verified numerically with physical observables (not just trigonometric identity)

2. **The spin chain provides a valid analog system** [Der]
   - Local energy densities o_n from ground state are used
   - Translational invariance confirmed numerically

3. **The k(N) = 1 + 1/N formula works for N ≠ 6** [Der]
   - Tested: N = 3, 4, 5, 6, 8, 10, 12
   - All pass with machine-precision accuracy

### What this does NOT establish

1. **The "equal corner share" normalization (a/c = 1/N) is NOT derived** from spin chain physics
   - In this test, a/c = 1/N is an *input*, not a prediction
   - The spin chain confirms R = 1 + a/c, not why a/c should equal 1/N

2. **EDC predictions are NOT validated** by this test
   - Pion splitting (r_π/4α ≈ 7/6) requires EDC-specific physics
   - N_cell renormalization (12→10) requires 5D brane physics
   - This test only validates the mathematical averaging mechanism

---

## Reproducibility

**Run the test:**
```bash
python3 edc_papers/_shared/code/spin_chain_kchannel_ed_test.py
```

**Dependencies:** numpy, scipy (standard scientific Python)

**Runtime:** ~10 seconds for N ≤ 12

---

## Cross-References

- k-channel lemma: `edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex`
- Candidate catalog: `docs/KN_CHANNEL_CROSS_VALIDATION_CANDIDATES.md`
- k-channel universality: `docs/ZN_CHANNEL_UNIVERSALITY_AUDIT.md`
- Toy overlap test: `docs/TOY_OVERLAP_KCHANNEL_TEST.md`

---

*Document created 2026-01-29. Test status: GREEN.*
