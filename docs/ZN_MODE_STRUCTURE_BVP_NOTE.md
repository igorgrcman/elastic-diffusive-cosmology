# Z_N Mode Structure BVP Verification Note

**Date:** 2026-01-29
**Source:** `edc_papers/_shared/derivations/zn_ring_delta_pinning_modes.tex`
**Code:** `edc_papers/_shared/code/zn_delta_pinning_mode_check.py`
**Status:** [Der] for delta-pinning ring model; [Dc] for 5D mapping

---

## Why This Matters

The k-channel derivation assumes `u(θ) = u₀ + a₁ cos(Nθ)` as the dominant
anisotropic perturbation. This note verifies that cos(Nθ) is indeed the
unique leading mode under Z_N delta-pinning, providing physical justification
for the ansatz used in deriving `a/c = 1/N` and `k(N) = 1 + 1/N`.

---

## VERDICT: PASS

**cos(Nθ) is the unique leading anisotropic mode under Z_N delta-pinning.**

---

## Proof Summary

### 1. Selection Lemma [Der]

For a mode `exp(imθ)`, the coupling to N identical anchors at `θ_n = 2πn/N` is:

```
Σ_n exp(im·θ_n) = N   if m ≡ 0 (mod N)
                = 0   otherwise
```

**Result:** Only Z_N-symmetric modes (m = 0, N, 2N, ...) couple to the anchors.
Modes with m ≢ 0 (mod N) have ZERO coupling and cannot be excited by anchor forcing.

### 2. Gradient Energy Ordering [Der]

Among Z_N-symmetric modes:
- m = 0: constant (isotropic), gradient energy = 0
- m = N: cos(Nθ), gradient energy ∝ N²
- m = 2N: cos(2Nθ), gradient energy ∝ 4N²
- ...

**Result:** The first anisotropic mode that couples to anchors is m = N.

### 3. Combined Result [Der]

Since:
1. Only m = kN modes couple to anchors
2. Among these, m = N has the lowest gradient energy

Therefore: **cos(Nθ) is the unique leading anisotropic mode**.

---

## Numerical Verification

**Selection Lemma (all N):** PASS
```
Z_3: Coupled modes = [0, 3, 6]
Z_4: Coupled modes = [0, 4, 8]
Z_5: Coupled modes = [0, 5, 10]
Z_6: Coupled modes = [0, 6, 12]
Z_8: Coupled modes = [0, 8, 16]
```

**Eigenmode overlap with cos(Nθ):** ALL PASS (>99% overlap)
```
Z_3: 99.71%
Z_4: 99.82%
Z_5: 99.88%
Z_6: 99.92%
Z_8: 99.95%
```

---

## Conditions for PASS

1. **Identical anchors** at Z_N fixed points (verified in Israel derivation)
2. **Quadratic W(u)** near equilibrium (standard linearization)
3. **Ring geometry** with periodic boundary conditions
4. **Weak-to-moderate pinning** (gradient-dominated regime)

---

## Remaining Gaps (Marked [Dc])

1. **Mapping to 5D:** The ring δ-pinning model is a toy model.
   Full 5D bulk solution would strengthen the physical basis.

2. **Non-quadratic W(u):** If W(u) has significant cubic/higher terms,
   mode mixing could occur. This is not expected to change the dominant mode.

3. **Strong pinning limit:** In extreme strong pinning (ρ >> N²),
   the mode structure becomes localized near anchors. The Z_N periodicity
   is preserved, so cos(Nθ) remains the leading angular dependence.

---

## Upgrade to k-Channel Credibility

This verification closes the last major gap in the k-channel derivation:

| Component | Status |
|-----------|--------|
| k(N) = 1 + 1/N formula | [Der] |
| a/c = 1/N from energy minimization | [Der] |
| Identical anchors from Z_N symmetry | [Der] |
| **cos(Nθ) mode selection** | **[Der] — NOW VERIFIED** |
| Mapping to 5D physics | [Dc] |

The complete chain from Z_N symmetry to k(N) = 1 + 1/N is now derived [Der]
within the delta-pinning ring model.

---

## Cross-References

- Derivation: `edc_papers/_shared/derivations/zn_ring_delta_pinning_modes.tex`
- Code: `edc_papers/_shared/code/zn_delta_pinning_mode_check.py`
- Energy minimization: `edc_papers/_shared/derivations/zn_anisotropy_normalization_from_action.tex`
- Israel anchors: `edc_papers/_shared/derivations/israel_zn_fixed_points_anchors.tex`
