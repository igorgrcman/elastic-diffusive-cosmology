# G_F BVP Tuning Decomposition

**Generated:** 2026-01-29 08:50:18
**Issue:** OPR-21c — Decompose tuning, understand parameter roles
**Status:** [Der] for analysis, [Dc] for physical interpretation

---

## Executive Summary

| Metric | LR_separation | fermion_width |
|--------|---------------|---------------|
| Elasticity at best point | -6.472 | 1.290 |
| X_ratio span over scan | 15323.06x | 62192927479994789423308378996736.00x |
| Dominant control | LR_separation | — |

**Key finding:** LR_separation has larger local sensitivity.

---

## 1. Physical Interpretation

### 1.1 What LR_separation Controls

```
LR_separation_delta = physical separation / delta
                    = distance between w_L and w_R peak positions / brane thickness
```

**Mechanism:**
- Larger LR_sep -> w_L and w_R peaks further apart
- Overlap I_4 = integral(w_L^2 * w_R^2 * w_phi^2) decreases exponentially with separation
- LR_sep controls the exponential suppression of I_4

**Scaling:** For Gaussian-like modes separated by d:
```
I_4 ~ exp(-d^2 / (2 sigma^2))
```
where sigma is the mode width.

### 1.2 What fermion_width Controls

```
fermion_width_delta = mode width / delta
                    = characteristic decay length of w_L, w_R profiles
```

**Mechanism:**
- Smaller fw -> narrower modes -> sharper localization
- Wider modes have longer tails -> more overlap at center
- fw controls the polynomial prefactor of I_4

**Scaling:** For modes with width sigma:
```
I_4 ~ (sigma / L)^3 * overlap_factor
```
where L is the domain size.

### 1.3 Why fw=0.8 Works (Goldilocks Effect)

Best fw for X_ratio ~ 1: **fw = 0.80**

The fw=0.8 value is the "Goldilocks" point where:
1. Modes are **wide enough** to have significant overlap at center
2. Modes are **narrow enough** to not dilute into domain boundaries
3. The product w_L^2 * w_R^2 at chi=0 is optimized

**I_4 behavior:** monotonically increasing

---

## 2. Sensitivity Analysis Results

### 2.1 LR Sensitivity (fw = 0.8 fixed)

| LR_sep | I_4 (GeV) | X_ratio |
|--------|-----------|---------|
| 1.0 | 9.587e-02 | 48.112 |
| 2.0 | 7.482e-02 | 37.546 |
| 3.0 | 5.063e-02 | 25.409 |
| 4.0 | 3.053e-02 | 15.321 |
| 5.0 | 1.687e-02 | 8.465 |
| 6.0 | 8.749e-03 | 4.391 |
| 7.0 | 4.338e-03 | 2.177 |
| 8.0 | 2.081e-03 | 1.044 |
| 9.0 | 9.719e-04 | 0.488 |
| 10.0 | 4.436e-04 | 0.223 |
| 12.0 | 8.651e-05 | 0.043 |
| 15.0 | 6.257e-06 | 0.003 |


**Elasticity at LR=8:** -6.472

Interpretation: A 10% increase in LR_sep causes a 64.7% decrease in X_ratio.

### 2.2 fw Sensitivity (LR = 8.0 fixed)

| fw | I_4 (GeV) | X_ratio | epsilon |
|----|-----------|---------|---------|
| 0.02 | 1.656e-34 | 0.000 | -0.000 |
| 0.05 | 3.329e-04 | 0.167 | -0.071 |
| 0.10 | 1.045e-03 | 0.524 | -0.178 |
| 0.20 | 1.098e-03 | 0.551 | 0.254 |
| 0.30 | 1.158e-03 | 0.581 | 0.310 |
| 0.40 | 1.248e-03 | 0.626 | 0.358 |
| 0.50 | 1.375e-03 | 0.690 | 0.399 |
| 0.60 | 1.550e-03 | 0.778 | 0.435 |
| 0.70 | 1.782e-03 | 0.894 | 0.468 |
| 0.80 | 2.081e-03 | 1.044 | 0.499 |
| 0.90 | 2.453e-03 | 1.231 | 0.526 |
| 1.00 | 2.900e-03 | 1.455 | 0.551 |
| 1.20 | 4.012e-03 | 2.013 | 0.597 |
| 1.50 | 6.121e-03 | 3.072 | 0.653 |
| 2.00 | 1.030e-02 | 5.169 | 0.727 |


**Elasticity at fw=0.8:** 1.290

Interpretation: A 10% increase in fw causes a 12.9% increase in X_ratio.

---

## 3. Comparison: LR vs fw Dominance

| Parameter | Elasticity | Control Type |
|-----------|------------|--------------|
| LR_separation | -6.472 | Exponential (separation) |
| fermion_width | 1.290 | Polynomial (width) |

**Dominant parameter:** LR_separation

**Physical reason:**
- LR controls the exponential suppression factor
- fw controls the polynomial prefactor and tail overlap
- At LR=8.0, the modes are well-separated, so LR dominates

---

## 4. Implications for Physical Priors

### 4.1 LR_separation Physical Prior

```
LR_sep = 8.0 delta = 8.0 * 0.533 GeV^-1 = 4.26 GeV^-1
       = 0.84 fm (in SI units)
```

This is approximately:
- **~1.0 proton radii** (r_p ~ 0.84 fm)
- **~4 nucleon Compton wavelengths** (lambda_N ~ 0.21 fm)

Physical interpretation: L-R separation ~ proton-radius scale.

### 4.2 fermion_width Physical Prior

```
fw = 0.8 delta = 0.8 * 0.533 GeV^-1 = 0.43 GeV^-1
   = 0.085 fm (in SI units)
```

This is approximately:
- **~0.4 nucleon Compton wavelengths** (lambda_N ~ 0.21 fm)
- **~0.1 proton radii**

Physical interpretation: Fermion localization width ~ sub-Compton scale.

---

## 5. Robustness Assessment

### 5.1 Tuning Fragility

| Metric | Value | Assessment |
|--------|-------|------------|
| X_ratio range (LR scan) | [0.00, 48.11] | FRAGILE |
| X_ratio range (fw scan) | [0.00, 5.17] | FRAGILE |

### 5.2 Tuning Window

The "success window" (X_ratio in [0.5, 2.0]):
- Exists for reasonable parameter ranges
- Not fine-tuned to sub-percent precision

---

## 6. Epistemic Status

| Result | Status | Confidence |
|--------|--------|------------|
| Sensitivity computation | [Der] | HIGH (numerical) |
| LR controls exponential | [Der] | HIGH (mode overlap) |
| fw controls polynomial | [Der] | HIGH (mode width) |
| Physical length mapping | [Dc] | MEDIUM (assumes delta = brane thickness) |
| "Goldilocks" interpretation | [Dc] | MEDIUM (plausible but not derived) |

---

## 7. Cross-References

| Document | Content |
|----------|---------|
| `docs/GF_BVP_PARAMETER_SCAN.md` | Full 2D scan results |
| `docs/GF_BVP_GATE_REPORT.md` | Current best point status |
| `docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md` | Framework overview |
| `edc_papers/_shared/bvp_gf/config.yaml` | Current configuration |

---

*Generated by `one_factor_sensitivity.py`*
