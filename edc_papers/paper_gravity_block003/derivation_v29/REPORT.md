# Derivation v29 — Detailed Report

## Executive Summary

Derivation v29 establishes the dimensionless control parameter β = σL²/M̄_Pl² that governs the KK mass gap. Two independent derivation routes confirm consistency. The extremely small value β ≈ 5×10⁻³⁶ reflects the hierarchy M_Z/M̄_Pl ≈ 10⁻¹⁷ and places the system deep in the Neumann limit.

---

## 1. Derivation Routes

### Route A: Direct Derivation

Starting from the metrological anchor σL³ = ℏc:

$$σ = \frac{ℏc}{L³}$$

Substituting into β:

$$β = \frac{σL²}{M̄_{Pl}²} = \frac{ℏc}{LM̄_{Pl}²}$$

**Tag**: [BL] (uses baseline ℏ, M̄_Pl, and open scale L)

### Route B: Via Spectral Equation

Given $b = λβ$ and the spectral equation $\tan(x) = -b/x$:

$$β = \frac{b}{λ}$$

With identification L = πℏc/M_Z:

$$β = \frac{M_Z}{πM̄_{Pl}²}$$

**Tag**: [I]+[BL] (adds identification dependency)

---

## 2. Numerical Results

| Quantity | Value | Tag |
|----------|-------|-----|
| L | 3.445×10⁻² GeV⁻¹ = 6.80×10⁻¹⁸ m | [I]+[BL] |
| σ | 2.45×10⁴ GeV⁴ | [BL] |
| β (reduced Planck) | 4.89×10⁻³⁶ | [BL] / [I]+[BL] |
| β (original Planck) | 1.95×10⁻³⁷ | [BL] / [I]+[BL] |
| δβ/β | 3.2×10⁻⁵ | — |

---

## 3. Convention Audit

### Planck Mass Map

| Convention | M̄_Pl | M_Pl | Ratio |
|------------|-------|------|-------|
| Reduced | 2.435×10¹⁸ GeV | — | 1 |
| Original | — | 1.221×10¹⁹ GeV | √(8π) = 5.01 |

### Length Map

| Convention | Symbol | Value (GeV⁻¹) | Value (m) |
|------------|--------|---------------|-----------|
| Interval | L = R_ξ | 3.445×10⁻² | 6.80×10⁻¹⁸ |
| Old radius | R = L/π | 1.097×10⁻² | 2.16×10⁻¹⁸ |

### β Convention Change

- β_L / β_R = π² = 9.87
- β^(red) / β^(orig) = 8π = 25.1

---

## 4. Control Law Table

Using β = 4.89×10⁻³⁶ and L = 3.445×10⁻² GeV⁻¹:

| k | λ = |k|/(2π) | b = λβ | x₁ | m_gap/M_Z |
|---|------------|--------|--------|-----------|
| 1 | 0.159 | 7.79×10⁻³⁷ | π | 1.000 |
| 2 | 0.318 | 1.56×10⁻³⁶ | π | 1.000 |
| 5 | 0.796 | 3.90×10⁻³⁶ | π | 1.000 |
| 10 | 1.592 | 7.79×10⁻³⁶ | π | 1.000 |

**Note**: All k values give b ≪ 1, placing the system in the Neumann regime.

---

## 5. Uncertainty Budget

### Sources

| Source | Value | Relative | Status |
|--------|-------|----------|--------|
| ℏ | exact | 0 | SI 2019 |
| c | exact | 0 | SI def |
| M_Z | 91.1876±0.0021 GeV | 2.3×10⁻⁵ | [BL] |
| M̄_Pl | via G_N | 1.1×10⁻⁵ | [BL] |

### Propagation

$$\frac{δβ}{β} = \sqrt{(2.3×10^{-5})² + 4(1.1×10^{-5})²} = 3.2×10^{-5}$$

Dominant contributors:
- M_Z: 52.2%
- M̄_Pl: 47.8%

---

## 6. Trap Resolution Summary

| Trap | Concern | Resolution |
|------|---------|------------|
| TRAP-1 | β dimensions | [β] = M⁴·M⁻²/M² = 1 ✓ |
| TRAP-2 | ℏ exact? | Yes, SI 2019 definition |
| TRAP-3 | L vs R | Dictionary provided; L canonical |
| TRAP-4 | Planck convention | Maps provided; reduced used |
| TRAP-5 | M̄_Pl as [BL] | Calibrated program acknowledged |
| TRAP-6 | Double counting | Two forms: L open vs identified |
| TRAP-7 | Circularity | Forward/inverse directions explicit |
| TRAP-8 | Robin origin | Action variation derivation |
| TRAP-9 | Topology | Track A/B separation |
| TRAP-10 | Numerics | Brent, residuals < 10⁻¹⁰ |

---

## 7. Python Verification

All 10 checks passed:

1. β Route A = Route B ✓
2. Planck map M_Pl = √(8π)M̄_Pl ✓
3. Planck map M₅ ratio ✓
4. L = πR consistency ✓
5. Neumann limit x₁ → π ✓
6. Dirichlet limit x₁ → π/2 ✓
7. Monotonicity ✓
8. Residuals < 10⁻¹⁰ ✓
9. Dimension checks ✓
10. Uncertainty computed ✓

---

## 8. Conclusions

1. β is properly defined and dimensionless
2. β ≈ 5×10⁻³⁶ reflects the Planck hierarchy
3. All conventions documented and consistent
4. Full uncertainty budget provided
5. All reviewer traps addressed
6. Gap remains [I]+[BL]

---

*Report generated: 2026-02-03*
