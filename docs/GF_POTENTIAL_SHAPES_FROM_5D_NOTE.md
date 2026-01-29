# G_F BVP Potential Shapes from 5D: Summary Note

**Created:** 2026-01-29
**Source:** `edc_papers/_shared/derivations/gf_potential_shapes_from_5d.tex`
**Status:** [Dc] — Derived Conditional (specific background choices)

---

## Executive Summary

The 1D BVP potential V(χ) has three standard derivations from 5D physics:

| Background | V(χ) Shape | Origin | Status |
|------------|-----------|--------|--------|
| Gaussian Wall | -V₀ exp(-χ²/2w²) | Soft brane energy density | [Dc] |
| RS-like | V₀ - V₁ δ(χ) | AdS warp factor | [Der] |
| Tanh Domain Wall | M₀² ∓ (M₀/δ) sech²(χ/δ) | 5D Dirac with kink mass | [Der] |

**Universal feature:** All backgrounds produce attractive well of depth ~1/δ² and width ~δ.

---

## Key Results

### 1. Mode Equation

From 5D Dirac action, KK reduction gives:
```
-d²w/dχ² + V(χ)w = λw
```
This is Schrödinger-like with V(χ) determined by background geometry.

### 2. Potential Depth Scaling

**Derived [Der]:** For bound state with mass M_eff ~ 1/δ:
```
V₀ ~ 1/δ²
```
This follows from dimensional analysis and virial theorem.

### 3. Chirality Separation (Domain Wall)

For tanh mass profile M(χ) = M₀ tanh(χ/δ):
- V_L has **dip** at χ=0 → left mode localized at wall
- V_R has **bump** at χ=0 → right mode expelled from wall

This is the mechanism for L-R spatial separation.

---

## Why Gaussian Wall in BVP?

The pipeline uses Gaussian wall because:
1. Simplest localized profile
2. Smooth for numerical stability
3. Tunable width parameter
4. Other shapes give qualitatively similar results

**The specific shape is not critical** for order-of-magnitude gate evaluation.

---

## Open Questions

1. Derive δ = ℏ/(2m_p) from 5D action
2. Derive wall_width parameter from brane dynamics
3. Quantify shape dependence of gate results

---

## Cross-References

| Document | Content |
|----------|---------|
| `edc_papers/_shared/derivations/gf_potential_shapes_from_5d.tex` | Full derivation |
| `edc_papers/_shared/bvp_gf/config.yaml` | BVP configuration |
| `docs/GF_BVP_PHYSICAL_PRIORS.md` | Physical length scales |
| `docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md` | Framework overview |

---

*Created 2026-01-29. V(χ) shapes connected to 5D physics; specific choice remains [Dc].*
