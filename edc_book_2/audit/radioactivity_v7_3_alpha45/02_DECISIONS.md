# DECISIONS LOG (V7.3)

**Created**: 2026-01-31
**Purpose**: Document methodological choices

---

## D-V7.3-01: Dataset Expansion Targets

**Decision**: Prioritize H1/H2 and high-Qα nuclides from V7.2 gap list.

**Rationale**: V7.2 identified critical gaps:
- Only 3 H1, 0 H2 → hindrance model underpowered
- Only 3 nuclides with Qα > 7 MeV → G-N range limited

**Outcome**: Added 13 nuclides, achieving 7 H1 + 3 H2 + 11 high-Qα.

---

## D-V7.3-02: Minimum α-Branch Threshold

**Decision**: Exclude nuclides with α-BR < 5%.

**Rationale**:
- At low α-BR, t₁/₂(α) = t₁/₂(total)/BR(α) becomes very uncertain
- Error propagation: σ(t₁/₂(α))/t₁/₂(α) ≈ σ(BR)/BR → large for small BR
- Bi-213 (2.14% α) and Bk-249 (0.001% α) excluded

**Registered**: 2026-01-31

---

## D-V7.3-03: Hindrance Classification Inheritance

**Decision**: Use V7.2 hindrance rules without modification.

**Rules** (from 06_HINDRANCE_RULES.md):
- H0: ΔJ ≤ 2 AND no parity change
- H1: ΔJ ≤ 2 AND parity change
- H2: ΔJ > 2

**Registered**: 2026-01-31

---

## D-V7.3-04: Pre-registered Outlier Rule

**Decision**: Flag nuclides with |residual| > 3 RMSE as potential outliers.

**Application**: In Model 2, check for high-leverage points. If found:
- Report main result WITH outlier
- Report sensitivity analysis WITHOUT outlier
- Note if conclusions change

**Outcome**: No outliers identified at 3σ level.

**Registered**: 2026-01-31

---

## D-V7.3-05: Power Analysis for Next Step

**Decision**: If V7.3 remains inconclusive, compute required N for 80% power.

**Method**: Based on observed effect size (g = -0.52, SE = 0.28), estimate:
- Current power at α = 0.05: ~45%
- Required N for 80% power: ~60 nuclides

**Registered**: 2026-01-31

---

## Hypothesis Updates

### H-N48-01c: Selection-Rule Gated d(n) [P]
**Status**: Carried forward from V7.2
**V7.3 Update**: Branchpoint score 3/5 = 60% (improved from 50%)

### H-V7.3-01: d(n) Affects G-N Residuals After Hindrance Control [P]
**Statement**: After controlling for H0/H1/H2 class, d(n) shows negative correlation with G-N residuals.
**Test**: Model 2 coefficient g < 0 with p < 0.05
**Result**: g = -0.52, p = 0.07 → **NOT SIGNIFICANT** at α = 0.05, **SIGNIFICANT** at α = 0.10

### H-V7.3-02: Hindrance Classes Show Expected Ordering [P]
**Statement**: H1 nuclides have larger positive residuals than H0; H2 larger than H1.
**Test**: β(H1) > 0, β(H2) > β(H1)
**Result**: β(H1) = +0.89, β(H2) = +1.42 → **SUPPORTED**

