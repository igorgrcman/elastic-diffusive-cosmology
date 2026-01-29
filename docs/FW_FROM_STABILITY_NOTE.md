# fw from Stability and Spectrum: Executive Summary

**Created:** 2026-01-29
**Source:** `edc_papers/_shared/derivations/fw_from_stability_and_spectrum.tex`
**Code:** `edc_papers/_shared/bvp_gf/fw_measure.py`
**Status:** [Dc/Cal] — Window derived, specific value calibrated

---

## Key Result

**Derived window:**
```
fw ∈ [0.5, 1.2]
```

**Tuned value:**
```
fw = 0.8 ✓ (inside window)
```

---

## Derived Constraints

| Constraint | Bound | Status | Origin |
|------------|-------|--------|--------|
| Normalizability | fw > 0.5 | [Der] | Zero mode must be L² |
| Strict localization | fw < 1.2 | [Dc] | 95% within ±2δ |
| Confinement | fw < 2 | [Dc] | Mode stays on brane |
| Spectral gap | fw < 1.7 | [Dc] | Ground state dominates |
| Variational | fw ~ 1 | [Dc] | Energy minimization |

**Combined:** fw ∈ [0.5, 1.2] from physics, not arbitrary.

---

## Is fw = 0.8 Inside the Window?

**YES** — 0.8 lies comfortably within [0.5, 1.2].

The value 0.8 is:
- **Physically natural:** Within all derived bounds
- **Not fine-tuned:** 30% variation allowed without leaving window
- **Calibrated:** Specific value comes from I_4 gate matching [Cal]

---

## Why fw Affects Overlap Polynomially

The overlap integral scales as:
```
I_4 ∝ (fw)^p × exp(-d_LR²/(2σ²))
```

- **fw controls polynomial prefactor** (p > 0)
- **d_LR controls exponential suppression**

From sensitivity analysis:
- fw elasticity: **+1.3** (polynomial, secondary)
- d_LR elasticity: **-6.5** (exponential, dominant)

Larger fw increases the prefactor, which is needed to get I_4 ~ 10⁻³ GeV.

---

## What Is NOT Derived

The **specific value** fw = 0.8 (vs 0.7 or 0.9) comes from:
1. BVP parameter scan
2. I_4 gate matching with d_LR = 8δ

To derive it, we would need:
- Exact V(χ) from 5D action
- Exact m(χ) from bulk Yukawa structure
- Solve exact BVP eigenvalue problem

**Status:** fw = 0.8 is [Cal] (calibrated within derived window)

---

## Verdict

**YELLOW [Dc/Cal]**

| Claim | Status |
|-------|--------|
| fw ∈ [0.5, 1.2] | [Dc] — Derived from stability/localization |
| fw = 0.8 inside window | [Der] — Verified |
| fw = 0.8 specifically | [Cal] — From BVP scan |
| Polynomial sensitivity | [Der] — From overlap structure |

---

## Defendable Statement

> The fermion width fw ≈ 0.8 is **physically natural** (lies within the
> derived stability window [0.5, 1.2]) but **not uniquely derived** (the
> specific value comes from matching the I_4 gate).

This is honest: we have a principled window, the tuned value is inside it,
but the exact value remains a calibration.

---

*See also: GF_BVP_DEFENSE_NOTES.md Q7*
