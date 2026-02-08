# PREFACTOR MECHANISM MODEL (V7.7)

**Created**: 2026-01-31
**Purpose**: Mechanistic narrative for d(n) → S_α channel
**Status**: [Der] for regression results, [P] for mechanism

---

## Standard α-Decay Rate Framework

### Rate Equation [Der]

```
λ = ν × P_tunnel × S_α
```

where:
- **ν** ≈ 10²¹ s⁻¹ = attempt frequency (nucleon collision rate at surface)
- **P_tunnel** = tunneling probability through Coulomb barrier
- **S_α** = preformation factor (probability α-cluster exists at surface)

### Geiger-Nuttall Control [Der]

The Geiger-Nuttall law:
```
log₁₀(t₁/₂) = a × (Z/√Q_α) + b
```

primarily captures **P_tunnel**, since:
- Higher Z → higher Coulomb barrier → lower P_tunnel → longer t₁/₂
- Higher Q_α → more energy to penetrate → higher P_tunnel → shorter t₁/₂

With a = 1.574 ± 0.018 (from V7.4 M2), GN explains R² = 0.9847 of variance.

---

## The Residual: What GN Doesn't Capture

### After GN + Hindrance [Der]

Model M1 (GN + hindrance):
```
log₁₀(t₁/₂) = a(Z/√Q) + b + c₁×I(H1) + c₂×I(H2)
```
R² = 0.9912

Adding d(n) (Model M2):
```
log₁₀(t₁/₂) = a(Z/√Q) + b + c₁×I(H1) + c₂×I(H2) + g×d(n)
```
R² = 0.9933, g = -0.31, p = 0.006

### What d(n) Captures [Der]

ΔR² = 0.0021 (0.21 percentage points)

This residual variance is:
- Too small to be major barrier physics (already in GN)
- Too significant to ignore (p = 0.006)
- Consistent with prefactor variation

---

## Prefactor vs Barrier: Model Comparison

### Model A (Prefactor-like) [Der]

d(n) enters additively in log₁₀(t₁/₂):
```
log₁₀(t₁/₂) = ... + g×d(n)
```

Interpretation: d(n) multiplies the rate → acts on S_α or ν.

### Model B (Barrier-like) [Der]

d(n) modifies the GN slope:
```
log₁₀(t₁/₂) = (a + g'×d(n)) × (Z/√Q) + ...
```

Interpretation: d(n) changes effective barrier → acts on P_tunnel.

### Comparison [Der]

| Model | AIC | BIC | CV RMSE |
|-------|-----|-----|---------|
| A (Prefactor) | 198.4 | 211.2 | 0.682 |
| B (Barrier) | 201.8 | 214.6 | 0.694 |

**Result**: Model A wins by ΔAIC = 3.4. Prefactor interpretation preferred.

---

## Mechanism: Frustration → S_α Enhancement

### Physical Picture [P]

```
Low d(n) → Near allowed M-topology:
  - Stable nuclear configuration
  - α-cluster forms slowly (needs fluctuation)
  - Low S_α
  - Rate limited by preformation

High d(n) → Far from allowed (frustrated):
  - Unstable/strained configuration
  - Enhanced surface dynamics
  - α-cluster forms easily (structural reorganization)
  - High S_α
  - Rate limited by barrier (already in GN)
```

### Quantitative Estimate [Der → P]

If g = -0.31 acts entirely through S_α:
```
log₁₀(S_α) = k₀ + 0.31 × d(n)
```

For d(n) = 0 → 3:
- S_α increases by factor 10^(0.31×3) ≈ 8
- This is within plausible S_α range (10⁻⁴ to 10⁻¹)

---

## Reconciling T1 and T3

### Apparent Tension

- **T1**: Effect strongest in H0 → suggests barrier (when barrier matters most)
- **T3**: Additive model wins → suggests prefactor

### Resolution [P]

These are not contradictory:

**T3** tells us WHERE d(n) enters the rate equation: multiplicatively (prefactor).

**T1** tells us WHEN the effect is visible: when other factors (selection rules) aren't dominating.

In H0 (unhindered):
- No selection rule penalty
- Barrier is the limiting factor
- Any boost to S_α immediately translates to shorter t₁/₂
- Full g = -0.34 visible

In H1/H2 (hindered):
- Selection rules add large penalty
- Barrier + selection rules both limit
- S_α boost partially masked by structure factor
- Reduced g ≈ -0.26, -0.22 visible

**Analogy**: A fast engine (high S_α) matters most when the road is clear (H0). On a congested road (H1/H2), engine speed matters less.

---

## Falsifiable Predictions

### Prediction 1 [P]

**If frustration enhances S_α**, then:

Independent S_α measurements (from spectroscopic factors) should correlate positively with d(n).

**Test**: Obtain S_α values from nuclear reaction data; regress on d(n).
**Threshold**: r > 0.5 supports mechanism; r < 0.3 rejects.
**Status**: [Open] — S_α data not in BL whitelist.

### Prediction 2 [P]

**If mechanism is surface dynamics**, then:

Effect should be stronger for surface-dominated nuclei (lighter actinides) vs volume-dominated (heavier).

**Test**: Split dataset at Z = 92; compare g.
**Threshold**: |g(light)| > |g(heavy)| by factor 1.5 supports.
**Status**: [Open] — V7.6.1 relativistic test showed no significant Z-dependence.

### Prediction 3 [P]

**If S_α enhancement is the channel**, then:

Nuclei with known high S_α (N≈Z, cluster nuclei) should show weaker d(n) effect (already have high S_α).

**Test**: Add cluster indicator to model; check interaction.
**Threshold**: Negative interaction supports.
**Status**: [Open] — Cluster data not in BL whitelist.

---

## Summary

| Component | Source | Interpretation |
|-----------|--------|----------------|
| g = -0.31 | V7.4 M2 [Der] | Higher d(n) → faster decay |
| AIC favors additive | V7.6.1 T3 [Der] | Prefactor channel |
| Strongest in H0 | V7.6.1 T1 [Der] | Effect visible when barrier limits |
| Frustration → S_α | This document [P] | Proposed mechanism |

**Verdict**: d(n) most likely modulates α-preformation probability S_α, not barrier penetrability P_tunnel.

