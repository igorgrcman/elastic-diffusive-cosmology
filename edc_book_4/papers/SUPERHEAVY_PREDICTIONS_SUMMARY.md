# Superheavy Predictions Paper Summary

**Draft v1 — 2026-03-16**
**Step 8 of 9 (Integration Program)**

---

## Core Predictions

| Z | A | N | n(A) | d(n) | Q_α (MeV) | log₁₀(t₁/₂/s) | t₁/₂ | Note |
|---|---|---|------|------|-----------|---------------|------|------|
| 119 | 298 | 179 | 40.74 | 4.74 | 10.5 ± 0.5 | −0.19 ± 1.3 | **0.6 s** (+20/−0.6) | — |
| 120 | 302 | 182 | 40.93 | 4.93 | 10.0 ± 0.5 | +1.46 ± 1.3 | **29 s** (+900/−28) | — |
| 120 | 304 | 184 | 41.02 | 5.02 | 9.5 ± 0.5 | +2.89 ± 1.3 | **780 s** (+24000/−760) | N=184 shell |

**Uncertainty budget:** ±1.3 dex total = Q_α propagation (0.8 dex) + model coefficients (0.9 dex) + OOS scatter (0.5 dex), added in quadrature.

---

## The Model

### Frustration-Corrected Geiger-Nuttall Law (V7.8 M2)

```
log₁₀(t₁/₂/s) = a × Z_d/√Q_α + g × d(n) + c₁×I(H1) + c₂×I(H2) + b
```

### Fitted Coefficients (ALPHA100 dataset, 106 nuclides, Z=83–100)

| Parameter | Value | SE | Description |
|-----------|-------|-----|-------------|
| a | 1.593 | 0.028 | GN slope |
| b | −50.77 | 0.91 | Intercept |
| g | −1.643 | 0.142 | Frustration coupling |
| c₁ | 1.121 | 0.314 | H1 hindrance |
| c₂ | 1.538 | 0.265 | H2 hindrance |

### Performance

- R² = 0.980 (training)
- CV R² = 0.971 (10-fold cross-validation)
- RMSE = 0.810 dex

### Key Functions

```
Coordination:    n(A) = 6.1 × A^(1/3)
Allowed set:     S = {2^a × 3^b : a,b ≥ 0}
Frustration:     d(n) = min_{k ∈ S} |n(A) − k|
Forbidden zone:  [37, 47] (all SHE fall here)
```

---

## Out-of-Sample Validation (6 Measured SHE)

| Nuclide | Q_α (MeV) | d(n) | Δ_baseline (dex) | Δ_corrected (dex) | Pass |
|---------|-----------|------|-----------------|------------------|------|
| ²⁸⁹Fl | 9.82 | 4.33 | 7.26 | 0.38 | ✓ |
| ²⁹⁰Fl | 9.19 | 4.38 | 8.27 | 0.55 | ✓ |
| ²⁹⁰Mc | 10.41 | 4.38 | 6.59 | 1.12 | ✓ |
| ²⁹³Lv | 10.67 | 4.52 | 7.43 | 0.53 | ✓ |
| ²⁹⁴Ts | 10.81 | 4.56 | 7.92 | 0.12 | ✓ |
| ²⁹⁴Og | 11.65 | 4.56 | 7.87 | 0.17 | ✓ |

**Summary:**
- Mean |Δ|: 7.56 dex (baseline) → 0.48 dex (corrected) = **16× improvement**
- Pass rate: 0/6 (baseline) → 6/6 (corrected) at |Δ| < 1.5 dex criterion

---

## What Makes This Paper Publishable

1. **Specific falsifiable predictions** for Z=119, Z=120 with explicit error bars
2. **Out-of-sample validation** on 6 measured SHE (not just in-sample fit)
3. **Single additional parameter** (g) beyond standard GN — minimal model complexity
4. **16× error reduction** over baseline in the superheavy regime
5. **Physical mechanism** (coordination frustration) provides explanation, not just fit
6. **Timely:** GSI, RIKEN, JINR actively pursuing Z=119, Z=120 synthesis

---

## Experimental Facilities

| Facility | Target Reaction | Element | Status |
|----------|----------------|---------|--------|
| JINR Dubna (SHE Factory) | ⁵⁴Cr + ²⁴⁸Cm → ³⁰²120* | Z=120 | Active |
| GSI Darmstadt (TASCA) | ⁵⁰Ti + ²⁴⁹Bk → ²⁹⁹119* | Z=119 | Planned |
| RIKEN (GARIS-III) | ⁵⁰Ti + ²⁴⁹Bk → ²⁹⁹119* | Z=119 | Planned |

---

## Falsifiability Hooks

1. ²⁹⁸119: t₁/₂ within [0.02, 20] s (factor 30 window)
2. ³⁰²120: t₁/₂ within [1, 900] s
3. ³⁰⁴120: t₁/₂ within [25 s, 7 hr]
4. Standard GN prediction (~10⁷ s for ³⁰²120) is too long by ≥ 4 orders of magnitude

---

## Model Limitations (Honestly Stated)

1. **Q_α values are theoretical** — dominant uncertainty source (±0.5 MeV → ±0.8 dex)
2. **Prefactor p = 6.1 is calibrated** [Cal] to Pb-208, not derived
3. **No spontaneous fission** — α-decay half-lives only (SF may compete)
4. **Linear frustration** — no nonlinear or threshold effects included
5. **Training gap** — Z=101–113 not in ALPHA100, creates extrapolation uncertainty

---

## Comparison with Standard Predictions

For ³⁰²120:

| Model | Method | t₁/₂ |
|-------|--------|-------|
| **This work** | Frustration-corrected GN | ~30 s |
| Standard GN | Uncorrected baseline | ~10⁷ s |
| Sobiczewski (2007) | WKB + WS potential | ~1–100 s |
| Bao et al. (2015) | Viola-Seaborg | ~0.1–10 s |

Our prediction falls within existing theoretical range but provides a distinct physical mechanism.

---

## N=184 Shell Closure Note

³⁰⁴120 (N=184) is a candidate for the predicted spherical shell closure:
- If shell closure realized: additional binding → lower Q_α → longer t₁/₂ (possibly >> 800 s)
- If no shell closure: higher Q_α → shorter t₁/₂
- Our prediction uses Q_α = 9.5 MeV without explicit shell correction
- The frustration term partially captures shell-like effects through coordination structure

---

**Sealed:** 2026-03-16. Step 8 of 9. Superheavy predictions paper draft complete.
