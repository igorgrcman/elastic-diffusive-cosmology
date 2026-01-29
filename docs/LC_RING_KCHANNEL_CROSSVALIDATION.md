# LC Ring k-Channel Cross-Validation

**Created:** 2026-01-29
**Status:** GREEN — mathematical mechanism confirmed in circuit domain
**Code:** `edc_papers/_shared/code/lc_ring_kchannel_test.py`

---

## EDC-Safe Framing

**What this test validates:**
- The mathematical mechanism of discrete vs continuum averaging
- The formula R = 1 + a/c for Z_N symmetric weighting functions
- Under "equal corner share" (a/c = 1/N): R = 1 + 1/N
- Domain independence: same ratio in circuits as in spin chains

**What this test does NOT validate:**
- EDC-specific predictions about pions, N_cell, or nuclear physics
- Any claim that LC circuits are described by EDC
- The physical origin of the "equal corner share" normalization in EDC contexts

**Correct interpretation:**
> "This is a circuit-domain analog test. It validates the averaging correction
> mechanism k(N) = 1 + 1/N, not EDC predictions. The same mathematical ratio
> appears in quantum spin chains and classical circuits."

---

## Circuit Model

### Physical System

**Model:** N identical LC sections in a ring (periodic boundary conditions)

```
Circuit topology:
- N nodes arranged in a ring (n = 0, 1, ..., N-1)
- Each node n has capacitance C to ground
- Each edge (n, n+1 mod N) has inductance L
```

### Eigenvalue Problem

Kirchhoff's equations for node voltages V_n:

```
C·V̈_n = (1/L)(V_{n-1} - 2V_n + V_{n+1})
```

This gives the eigenvalue problem:

```
K·v = ω²·M·v
```

where K is the ring Laplacian (scaled by 1/L) and M = C·I.

**Normal modes:** Eigenvectors are discrete Fourier modes
```
v_m(n) = exp(i·2πmn/N),    m = 0, 1, ..., N-1
```

**Eigenfrequencies:**
```
ω²_m = (4/LC)·sin²(πm/N)
```

### Local Energy Density

For mode m with voltage distribution V_n:

```
eC_n = (1/2)·C·|V_n|²    (capacitor energy at node n)
```

Normalized so mean(|V_n|²) = 1 for comparison across modes.

---

## k-Channel Observable Definition

### Why This is an "Averaging Observable"

The k-channel mechanism applies to observables computed as:
- **Discrete:** sum over N symmetric sample points
- **Continuum:** integral over continuous domain

For the LC ring:
- **Discrete:** Sample energy density at N node positions
- **Continuum:** Integrate energy density over continuous ring (limit N→∞)

### Z_N Symmetric Weighting Function

```
f(θ) = c + a·cos(Nθ)
θ_n = 2πn/N   (angular position of node n)
```

At sample points: cos(N·θ_n) = cos(2πn) = 1 for all n.

### Discrete vs Continuum Observables

**Discrete sampling:**
```
O_disc = (1/N) Σ_{n=0}^{N-1} f(θ_n) · eC_n
```

**Continuum average:**
```
O_cont = (1/2π) ∫_0^{2π} f(θ) dθ · ē = c · ē
```

(The cos(Nθ) term integrates to zero over the full circle.)

### Averaging Ratio

```
R = O_disc / O_cont = 1 + a/c
```

Under **equal corner share** (a/c = 1/N):

```
R = 1 + 1/N = k(N)
```

---

## Results

### Main Results Table (a/c = 1/N)

| N | R_num | R_theory | 1+1/N | error | Status |
|---|-------|----------|-------|-------|--------|
| 3 | 1.333333333333 | 1.3333333333 | 1.3333333333 | 0 | **PASS** |
| 4 | 1.250000000000 | 1.2500000000 | 1.2500000000 | 0 | **PASS** |
| 5 | 1.200000000000 | 1.2000000000 | 1.2000000000 | 0 | **PASS** |
| 6 | 1.166666666667 | 1.1666666667 | 1.1666666667 | 0 | **PASS** |
| 8 | 1.125000000000 | 1.1250000000 | 1.1250000000 | 2e-16 | **PASS** |
| 10 | 1.100000000000 | 1.1000000000 | 1.1000000000 | 2e-16 | **PASS** |
| 12 | 1.083333333333 | 1.0833333333 | 1.0833333333 | 0 | **PASS** |

### a/c Scan (General Formula Verification)

For N = 6, scanning a/c values:

| a/c | R_num | R_theory | error |
|-----|-------|----------|-------|
| 0.0 | 1.0000 | 1.0000 | 0 |
| 0.1 | 1.1000 | 1.1000 | 2e-16 |
| 0.2 | 1.2000 | 1.2000 | 0 |
| 0.5 | 1.5000 | 1.5000 | 2e-16 |
| 1.0 | 2.0000 | 2.0000 | 0 |

**All a/c values confirm R = 1 + a/c.**

---

## Verdict

### Status: **GREEN**

**Mathematical mechanism confirmed in circuit domain:**
- R = 1 + a/c holds to machine precision for all N and all a/c tested
- Under equal corner share (a/c = 1/N): R = k(N) = 1 + 1/N exactly
- Errors at floating-point limit (~10⁻¹⁶)

### What This Establishes

1. **The averaging ratio formula R = 1 + a/c is correct** [Der]
   - Verified numerically with circuit observables

2. **Domain independence confirmed** [Der]
   - Same ratio in quantum spin chains and classical LC circuits
   - Mechanism is mathematical, not physics-specific

3. **The k(N) = 1 + 1/N formula works for N ≠ 6** [Der]
   - Tested: N = 3, 4, 5, 6, 8, 10, 12

### What This Does NOT Establish

1. **The "equal corner share" normalization (a/c = 1/N) is NOT derived** from circuit physics
   - In this test, a/c = 1/N is an *input*, not a prediction

2. **EDC predictions are NOT validated** by this test
   - Pion splitting requires EDC-specific physics
   - N_cell renormalization requires 5D brane physics

---

## Comparison: Spin Chain vs LC Ring

| Aspect | Spin Chain | LC Ring |
|--------|------------|---------|
| **Domain** | Quantum mechanics | Classical circuits |
| **System** | XX Heisenberg model | Lumped-element resonator |
| **Observable** | Ground state energy density | Capacitor energy density |
| **Physics** | ⟨ψ₀\|h_n\|ψ₀⟩ | (1/2)C\|V_n\|² |
| **k(N) result** | 1 + 1/N ✓ | 1 + 1/N ✓ |
| **Error** | < 10⁻¹⁵ | < 10⁻¹⁵ |

**Conclusion:** The k-channel averaging ratio is a mathematical identity that appears
in any system with Z_N symmetric weighting. It is not specific to quantum mechanics,
classical mechanics, or any particular physical theory.

---

## Reproducibility

**Run the test:**
```bash
python3 edc_papers/_shared/code/lc_ring_kchannel_test.py
```

**Dependencies:** numpy (standard scientific Python)

**Runtime:** < 1 second

**Note:** This is a "SPICE-equivalent" eigenmode analysis. The lumped-element
ring equations are identical to what SPICE would solve; we compute eigenmodes
directly rather than time-domain simulation.

---

## Cross-References

- Spin chain cross-validation: `docs/SPIN_CHAIN_KCHANNEL_CROSSVALIDATION.md`
- k-channel lemma: `edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex`
- Candidate catalog: `docs/KN_CHANNEL_CROSS_VALIDATION_CANDIDATES.md`
- k-channel universality: `docs/ZN_CHANNEL_UNIVERSALITY_AUDIT.md`

---

*Document created 2026-01-29. Test status: GREEN.*
