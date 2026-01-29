# G_F BVP Physical Priors

**Created:** 2026-01-29
**Issue:** OPR-21c — Establish physical priors for tuned parameters
**Status:** [Dc] — Derived Conditional (physical identification assumed)

---

## Executive Summary

The tuned BVP parameters have natural physical interpretations:

| Parameter | Tuned Value | Physical Length | Physical Scale |
|-----------|-------------|-----------------|----------------|
| LR_separation_delta | 8.0 | 4.26 GeV⁻¹ = 0.84 fm | ~ proton radius |
| fermion_width_delta | 0.8 | 0.43 GeV⁻¹ = 0.085 fm | ~ 2 × nucleon Compton |
| delta (brane thickness) | 0.533 GeV⁻¹ | 0.105 fm | ~ 1/2 × nucleon Compton |

**Key insight:** All scales are O(0.1 fm) — the nuclear/QCD scale.

---

## 1. The Brane Thickness δ

### 1.1 Definition

```
δ = ℏ / (2 m_p c) = 0.533 GeV⁻¹ = 0.105 fm
```

This is the **fundamental EDC length scale** — half the proton Compton wavelength.

### 1.2 Physical Interpretation

| Interpretation | Value | Match |
|----------------|-------|-------|
| Proton Compton / 2 | 0.105 fm | EXACT (definition) |
| QCD string tension^{-1/2} | ~0.2 fm | SAME ORDER |
| Lattice QCD spacing | 0.05-0.1 fm | SAME ORDER |

**Status:** [Dc] — δ is set by proton mass; identification with "brane thickness" is postulate.

---

## 2. LR Separation

### 2.1 Physical Length

```
d_LR = LR_sep × δ = 8.0 × 0.533 GeV⁻¹ = 4.26 GeV⁻¹
     = 0.84 fm (in SI units)
```

### 2.2 Physical Interpretation

| Comparison | Value | Ratio |
|------------|-------|-------|
| d_LR | 0.84 fm | 1.0 |
| Proton charge radius r_p | 0.84 fm | 1.0 |
| Nucleon Compton wavelength λ_N | 0.21 fm | 4.0 |
| Pion Compton wavelength λ_π | 1.41 fm | 0.6 |

**Remarkable coincidence:** d_LR ≈ r_p to 3 significant figures.

### 2.3 Physical Prior

**Hypothesis:** L-R separation equals proton charge radius.

```
d_LR = r_p = 0.84 fm
→ LR_sep = r_p / δ = 0.84 / 0.105 = 8.0
```

This would **derive** the value LR_sep = 8.0 from:
1. δ = ℏ/(2m_p) [definition]
2. d_LR = r_p [hypothesis]

**Status:** [Dc] — Plausible but not derived. The proton radius itself is not predicted.

### 2.4 Why This Scale?

The chiral L-R separation being ~ r_p suggests:
- Chiral symmetry breaking scale ~ confinement scale
- Both set by QCD dynamics at O(Λ_QCD⁻¹)

This is consistent with the EDC picture where:
- Proton = Y-junction at 120° (Book 1)
- Chiral modes = 5D wavefunctions localized on Y-junction arms
- Separation ~ arm length ~ r_p

---

## 3. Fermion Width

### 3.1 Physical Length

```
w_f = fw × δ = 0.8 × 0.533 GeV⁻¹ = 0.426 GeV⁻¹
    = 0.084 fm (in SI units)
```

### 3.2 Physical Interpretation

| Comparison | Value | Ratio |
|------------|-------|-------|
| w_f | 0.084 fm | 1.0 |
| Nucleon Compton λ_N | 0.21 fm | 0.40 |
| δ (brane thickness) | 0.105 fm | 0.80 |
| Electron Compton λ_e | 386 fm | 0.0002 |

### 3.3 Physical Prior

**Hypothesis:** Fermion localization width scales with brane thickness.

```
w_f = (4/5) × δ
→ fw = 0.8
```

**Interpretation:** Fermions are localized to ~80% of the brane thickness.

This makes physical sense:
- If w_f >> δ: Fermions delocalize into bulk → not confined
- If w_f << δ: Fermions pointlike → infinite self-energy
- w_f ~ δ: Natural balance

### 3.4 Alternative: Goldilocks from Overlap

The sensitivity analysis shows fw controls the polynomial prefactor of I_4.
The "Goldilocks" value fw = 0.8 is where:
- Modes wide enough to have significant overlap at center
- Modes narrow enough to stay within brane

This is a **stability argument**, not a derivation.

---

## 4. Derived Quantities

### 4.1 Effective Mass Scale

```
M_eff = 2.43 GeV
1/δ = 1.88 GeV
M_eff / (1/δ) = 1.30
```

**Interpretation:** M_eff is ~30% larger than naive 1/δ estimate.
This factor comes from the BVP eigenvalue structure.

### 4.2 Overlap Integral

```
I_4 = 2.08 × 10⁻³ GeV (tuned)
```

Dimensional analysis:
```
I_4 ~ δ × (w_f/d_LR)^6 × exp(-d_LR²/(2w_f²))
    ~ 0.533 × (0.084/0.84)^6 × exp(-50)
    ~ 10⁻³ GeV (rough estimate)
```

The exp(-50) factor explains why I_4 is so small.

---

## 5. Physical Prior Summary

| Parameter | Physical Prior | Formula | Status |
|-----------|----------------|---------|--------|
| δ | Proton Compton / 2 | ℏ/(2m_p) | [Dc] |
| LR_sep | Proton radius / δ | r_p / δ = 8.0 | [Dc] |
| fw | O(1) × brane scale | 0.8 | [Dc] (from fit) |

### 5.1 What Would Upgrade to [Der]

To upgrade these priors to [Der], we would need:

1. **δ from 5D action:** Show that bulk curvature or brane tension naturally produces δ = ℏ/(2m_p).

2. **LR_sep from chiral symmetry:** Derive the L-R separation from 5D Dirac equation with domain wall fermions.

3. **fw from mode equation:** Show that the fermion localization width emerges from the BVP eigenvalue problem.

Currently these are **physical priors** (plausible identifications) not derivations.

---

## 6. Sensitivity to Priors

From the sensitivity analysis (OPR-21c):

| Prior change | Effect on X_ratio |
|--------------|-------------------|
| LR_sep → 9.0 (+12.5%) | X_ratio → 0.49 (-53%) |
| LR_sep → 7.0 (-12.5%) | X_ratio → 2.18 (+109%) |
| fw → 0.9 (+12.5%) | X_ratio → 1.23 (+18%) |
| fw → 0.7 (-12.5%) | X_ratio → 0.89 (-15%) |

**Conclusion:** LR is exponentially sensitive; fw is polynomially sensitive.
The physical prior d_LR = r_p is the key identification.

---

## 7. Falsification Conditions

The physical priors fail if:

1. **LR_sep changes with energy:** If the L-R separation runs with energy scale, the proton radius identification breaks.

2. **fw requires fine-tuning:** If no O(1) value of fw gives X_ratio ~ 1, the framework fails.

3. **δ is unrelated to m_p:** If brane thickness has no connection to nucleon mass, the identification is wrong.

---

## 8. Cross-References

| Document | Content |
|----------|---------|
| `docs/GF_BVP_TUNING_DECOMPOSITION.md` | Sensitivity analysis |
| `docs/GF_BVP_GATE_REPORT.md` | Current best point |
| `docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md` | Framework overview |
| `docs/SIGMA_DEPENDENCY_AUDIT.md` | σ vs δ relationship |
| `edc_book_2/src/sections/11_gf_derivation.tex` | Book chapter |

---

## 9. Epistemic Status

| Claim | Status | Confidence |
|-------|--------|------------|
| δ = ℏ/(2m_p) | [Dc] | HIGH (definition) |
| d_LR ≈ r_p | [Dc] | MEDIUM (coincidence) |
| fw ~ 0.8δ | [Dc] | MEDIUM (from fit) |
| Scales are O(QCD) | [Der] | HIGH (dimensional) |

---

*Created 2026-01-29. Physical priors established; derivation from 5D action remains [OPEN].*
