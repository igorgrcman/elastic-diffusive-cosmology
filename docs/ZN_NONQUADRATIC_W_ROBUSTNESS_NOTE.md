# Z_N Non-Quadratic W(u) Robustness Note

**Date:** 2026-01-29
**Source:** `edc_papers/_shared/derivations/zn_mode_selection_nonlinear_W.tex`
**Code:** `edc_papers/_shared/code/zn_nonlinear_W_harmonics_demo.py`
**Status:** [Der] for second-variation theorem; [Dc] for amplitude corrections

---

## Summary

**Mode index selection (m = N) is ROBUST under non-quadratic W(u).**

This note addresses Open Question #1 from the mode structure verification:
"Does non-quadratic W(u) change the dominant mode selection?"

**Answer: NO.** The mode index is determined by the Hessian (second variation),
which depends only on W''(u₀) = κ, not on higher derivatives.

---

## The Robustness Theorem

**Theorem (Mode Selection Robustness) [Der]:**

Let W: ℝ → ℝ be a C² function with:
1. Stable equilibrium at u₀: W'(u₀) = 0, W''(u₀) = κ > 0
2. Identical anchors at Z_N fixed points θ_n = 2πn/N

Then for sufficiently small amplitude |A| ≪ L_W:

> **The leading anisotropic mode is cos(Nθ)**

where L_W ~ min(κ/|g|, √(κ/|h|)) is the scale of validity.

---

## What Changes vs What Doesn't

| Property | Quadratic W | General W |
|----------|-------------|-----------|
| Mode index (m = N) | Fixed | **Unchanged** |
| Selection Lemma | Exact | **Unchanged** |
| Gradient ordering | Exact | **Unchanged** |
| Amplitude relation | Linear | Nonlinear corrections |
| Harmonic content | Pure cos(Nθ) | cos(Nθ) + higher (2N, 3N, ...) |

---

## Why Mode Index Is Robust

The second variation (Hessian) of the energy is:

```
δ²E[η,η] = T ∫(η')² dθ + λκ Σ_n η(θ_n)²
```

This has **exactly the same form** as the quadratic case, depending only on κ = W''(u₀).

Higher derivatives (g = W''', h = W'''', ...) only enter at O(η³) and beyond,
which contribute to:
- Amplitude-dependent energy shifts
- Higher harmonic generation (2N, 3N, ...)
- Shape distortion near equilibrium

But they do **NOT** change:
- Which modes couple to anchors (Selection Lemma)
- Which coupled mode has lowest gradient energy (m = N)

---

## Harmonic Generation Table

| Order | Source | Harmonics Generated | Relative Amplitude |
|-------|--------|---------------------|-------------------|
| O(A) | Linear (κ) | cos(Nθ) | A |
| O(A²) | --- | (none) | --- |
| O(A³) | Cubic (g) | cos(Nθ), cos(3Nθ) | ~ gA³/κ |
| O(A⁴) | Quartic (h) | const, cos(2Nθ), cos(4Nθ) | ~ hA⁴/κ |

**Key:** All generated harmonics are multiples of N. No m < N modes appear.

---

## Regime of Validity

The perturbative analysis holds when:

```
ε₃ = |g|A/κ ≪ 1   (cubic nonlinearity small)
ε₄ = |h|A²/κ ≪ 1  (quartic nonlinearity small)
```

Equivalently: |A| ≪ min(κ/|g|, √(κ/|h|))

---

## Numerical Verification

```
Testing Z_6 with various nonlinearities:

Case                  ε₃=gA/κ  ε₄=hA²/κ  Dominant  Status
----------------------------------------------------------
Linear (baseline)     0.000    0.000     m=6       PASS
Weak cubic            0.100    0.000     m=6       PASS
Moderate cubic        0.200    0.000     m=6       PASS
Weak quartic          0.000    0.040     m=6       PASS
Mixed nonlinear       0.150    0.022     m=6       PASS
Strong cubic          0.250    0.000     m=6       PASS

All tests: PASS
```

---

## Failure Modes (When Theorem Does NOT Apply)

1. **Non-smooth W:** If W is not C², Hessian may not exist
2. **Metastability:** If W''(u₀) ≤ 0, equilibrium is unstable
3. **Large amplitude:** If |A| ≳ L_W, perturbation theory fails
4. **Symmetry breaking:** Non-identical anchors or non-Z_N positions
5. **Multiple minima:** System jumping between equilibria

---

## Impact on k-Channel Derivation

This robustness result strengthens the physical foundation of the k-channel:

| Component | Status |
|-----------|--------|
| k(N) = 1 + 1/N formula | [Der] |
| a/c = 1/N from energy minimization | [Der] |
| Identical anchors from Z_N symmetry | [Der] |
| cos(Nθ) mode selection (quadratic W) | [Der] |
| **cos(Nθ) mode selection (general W)** | **[Der] — NOW PROVEN** |

The ansatz u(θ) = u₀ + a₁cos(Nθ) is now validated for **any smooth potential**
with stable equilibrium, not just quadratic W.

---

## Cross-References

- Derivation: `edc_papers/_shared/derivations/zn_mode_selection_nonlinear_W.tex`
- Code: `edc_papers/_shared/code/zn_nonlinear_W_harmonics_demo.py`
- Linear mode selection: `edc_papers/_shared/derivations/zn_ring_delta_pinning_modes.tex`
- Mode structure BVP note: `docs/ZN_MODE_STRUCTURE_BVP_NOTE.md`
