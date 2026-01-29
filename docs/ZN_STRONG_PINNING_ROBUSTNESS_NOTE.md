# Z_N Strong Pinning Regime Robustness Note

**Date:** 2026-01-29
**Source:** `edc_papers/_shared/derivations/zn_strong_pinning_regimes.tex`
**Code:** `edc_papers/_shared/code/zn_strong_pinning_scan.py`
**Status:** [Der] for mode index stability; [Dc] for localization bounds

---

## Summary

**Mode index m = N is STABLE across ALL pinning regimes.**

The Selection Lemma (Z_N symmetry) protects the mode index regardless of pinning strength ρ.
This extends the previous weak-pinning analysis to the full range ρ ∈ (0, ∞).

---

## Regime Classification

| Regime | Condition | Eigenvalue | Mode Shape | Localization |
|--------|-----------|------------|------------|--------------|
| **Weak** | ρ << N² | μ_N ≈ N² | cos(Nθ) | uniform |
| **Intermediate** | ρ ~ N² | crossover | deformed | partial |
| **Strong** | ρ >> N² | μ_N ∝ ρ | cusp-like | concentrated |

Critical scale: ρ* = N²

---

## Why Mode Index Is Protected

The Selection Lemma states:
```
Σ_n exp(im θ_n) = { N  if m ≡ 0 (mod N)
                  { 0  otherwise
```

This is a **geometric identity** about anchor positions θ_n = 2πn/N.
It holds regardless of:
- Pinning strength ρ
- Mode amplitude
- Mode shape details

Therefore:
1. Only m = kN modes couple to anchors (at ANY ρ)
2. Modes with m ≢ 0 (mod N) have zero coupling (at ANY ρ)
3. The lowest anisotropic coupled mode is always m = N

---

## Numerical Verification

```
Z_6 (ρ* = 36):   m = 6 stable for ρ ∈ [0.01, 10⁵]  ✓
Z_3 (ρ* = 9):    m = 3 stable for ρ ∈ [0.01, 10⁵]  ✓
Z_12 (ρ* = 144): m = 12 stable for ρ ∈ [0.01, 10⁵] ✓
```

All tests: **PASS**

---

## What Changes vs What Doesn't

| Property | Weak → Strong | Status |
|----------|---------------|--------|
| Mode index m | N → N | **UNCHANGED** |
| Z_N periodicity | preserved → preserved | **UNCHANGED** |
| Eigenvalue | N² → ∝ρ | changes |
| Mode shape | cosine → cusp | changes |
| Energy distribution | uniform → localized | changes |

---

## Localization in Strong Pinning

In the strong pinning limit (ρ >> N²):
- Field is "clamped" near v = 0 at anchor sites
- Gradient energy concentrates in boundary layers of width δ ~ 1/√ρ
- Mode develops cusp-like structure near anchors

Numerical observation:
- Weak regime: localization ~ 4-5%
- Strong regime: localization ~ 20-27%

---

## Eigenvalue Asymptotics

**Weak pinning (ρ << N²):**
```
μ_N = N² + ρN/π + O(ρ²/N³)
```

**Strong pinning (ρ >> N²):**
```
μ_N ∝ ρN/π (linear in ρ)
```

**Crossover:** at ρ ~ N²

---

## Implications for k-Channel

The k(N) = 1 + 1/N correction formula was derived in the weak-pinning regime.
This analysis shows the underlying mode selection (m = N) is valid at ANY ρ.

Therefore the k-channel correction is not limited to weak pinning.

---

## Epistemic Status

| Result | Status |
|--------|--------|
| Mode index stability (all ρ) | [Der] |
| Weak eigenvalue formula | [Der] |
| Strong eigenvalue scaling | [Der] |
| Localization bounds | [Dc] |
| Interpolation formula | [Dc] |

---

## Cross-References

- Derivation: `edc_papers/_shared/derivations/zn_strong_pinning_regimes.tex`
- Code: `edc_papers/_shared/code/zn_strong_pinning_scan.py`
- Mode selection (quadratic): `edc_papers/_shared/derivations/zn_ring_delta_pinning_modes.tex`
- Non-quadratic W robustness: `edc_papers/_shared/derivations/zn_mode_selection_nonlinear_W.tex`
