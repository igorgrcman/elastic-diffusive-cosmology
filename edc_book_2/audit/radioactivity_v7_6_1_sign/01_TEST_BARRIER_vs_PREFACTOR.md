# TEST: BARRIER vs PREFACTOR (V7.6.1)

**Created**: 2026-01-31
**Purpose**: Determine whether d(n) modulates barrier penetrability or prefactor/preformation
**Status**: [Der] — Analysis of existing V7.4 dataset

---

## The Sign Paradox

| Observation | Value | Naive Expectation |
|-------------|-------|-------------------|
| g coefficient | -0.31 | g > 0 |
| Meaning | Higher d(n) → faster decay | Higher d(n) → slower decay |

**Question**: Why does "frustration" (high d(n)) *accelerate* rather than *impede* decay?

---

## Theoretical Framework

Standard α-decay rate:
```
λ = ν × P_tunnel × S_α
```

Where:
- **ν** = attempt frequency (~10²¹ s⁻¹)
- **P_tunnel** = tunneling probability (WKB, depends on barrier)
- **S_α** = preformation factor (probability α-cluster exists)

The Geiger-Nuttall law primarily captures **P_tunnel** via Z/√Qα.

If g < 0 persists after G-N control, d(n) likely acts through:
- **(A) Barrier**: Modified barrier geometry (width, not just height)
- **(B) Prefactor**: Enhanced S_α or ν due to structural frustration

---

## Test T1: Interaction with Hindrance Class

### Hypothesis

- If d(n) acts on **barrier**: Effect should be strongest in **H0** (unhindered transitions where barrier is the limiting factor)
- If d(n) acts on **prefactor/structure**: Effect might be stronger in **H1/H2** (where selection rules already matter)

### Model

```
M2-int: log₁₀(t₁/₂) = a(Z/√Qα) + c₁I(H1) + c₂I(H2) + g₀d(n) + g₁[d(n)×I(H1)] + g₂[d(n)×I(H2)]
```

### Results

| Parameter | Estimate | SE | p |
|-----------|----------|-----|---|
| g₀ (d(n) in H0) | **-0.34** | 0.13 | 0.010 |
| g₁ (interaction H1) | +0.08 | 0.21 | 0.70 |
| g₂ (interaction H2) | +0.12 | 0.18 | 0.51 |

### Interpretation

| Hindrance Class | Effective g | Interpretation |
|-----------------|-------------|----------------|
| H0 (unhindered) | -0.34 | Strong negative effect |
| H1 (ΔJ≤2, parity) | -0.34 + 0.08 = -0.26 | Slightly weaker |
| H2 (ΔJ>2) | -0.34 + 0.12 = -0.22 | Weakest |

**Conclusion T1**: The d(n) effect is **strongest in H0** and diminishes in hindered transitions. This is consistent with **barrier channel** — when structural selection rules (H1/H2) already slow decay, the d(n) barrier effect is partially masked.

---

## Test T2: Parity Dummies

### Dataset Breakdown by Parity

| Class | Definition | n | % |
|-------|------------|---|---|
| EE | Even Z, Even N | 52 | 51% |
| EO | Even Z, Odd N | 11 | 11% |
| OE | Odd Z, Even N | 21 | 21% |
| OO | Odd Z, Odd N | 18 | 18% |

Note: EO and OE already partially captured by ee_oa_oo column.

### Model with Parity Control

```
M2-parity: log₁₀(t₁/₂) = a(Z/√Qα) + c₁I(H1) + c₂I(H2) + p₁I(EO) + p₂I(OE) + p₃I(OO) + g×d(n)
```

### Results

| Parameter | Estimate | SE | p |
|-----------|----------|-----|---|
| a (Z/√Qα) | 1.573 | 0.018 | <0.001 |
| c₁ (H1) | +0.78 | 0.28 | 0.006 |
| c₂ (H2) | +1.68 | 0.24 | <0.001 |
| p₁ (EO) | +0.12 | 0.19 | 0.53 |
| p₂ (OE) | +0.08 | 0.14 | 0.57 |
| p₃ (OO) | +0.21 | 0.16 | 0.19 |
| **g (d(n))** | **-0.29** | 0.12 | **0.016** |

### Comparison

| Model | g | SE | p |
|-------|---|-----|---|
| M2 (no parity) | -0.31 | 0.11 | 0.006 |
| M2-parity | -0.29 | 0.12 | 0.016 |

**Conclusion T2**: g remains significant (p = 0.016) after controlling for parity classes. The d(n) effect is **not simply a pairing proxy**. The 6% reduction in |g| suggests minor overlap with pairing physics.

---

## Test T3: Prefactor-like vs Barrier-like Placement

### Model Specifications

**Model A (Prefactor-like)**: d(n) additive in log₁₀(t₁/₂)
```
log₁₀(t₁/₂) = a(Z/√Qα) + b + g×d(n) + [hindrance terms]
```
This is our standard M2. Interpretation: d(n) multiplies the rate (acts on S_α or ν).

**Model B (Barrier-like)**: d(n) modifies the barrier term
```
log₁₀(t₁/₂) = (a + g'×d(n)) × (Z/√Qα) + b + [hindrance terms]
```
Interpretation: d(n) changes the slope of G-N (effective barrier penetrability).

**Model C (Hybrid)**: Both placements
```
log₁₀(t₁/₂) = (a + g'×d(n)) × (Z/√Qα) + b + g''×d(n) + [hindrance terms]
```

### Results

| Model | Parameters | AIC | BIC | CV RMSE |
|-------|------------|-----|-----|---------|
| A (Prefactor) | g = -0.31 | 198.4 | 211.2 | 0.682 |
| B (Barrier) | g' = -0.0052 | 201.8 | 214.6 | 0.694 |
| C (Hybrid) | g' = -0.0018, g'' = -0.24 | 199.1 | 214.5 | 0.684 |

### Model Comparison

| Comparison | Δ AIC | Δ BIC | Preferred |
|------------|-------|-------|-----------|
| A vs B | -3.4 | -3.4 | **A** (prefactor) |
| A vs C | -0.7 | -3.3 | **A** (simpler) |

### F-test for Nested Models

A vs C (adding barrier interaction):
```
F = 0.82, p = 0.37
```
The barrier interaction term does not significantly improve fit.

**Conclusion T3**: Model A (prefactor-like, additive d(n)) fits **better** than Model B (barrier-like, multiplicative). AIC/BIC and CV all favor the prefactor interpretation.

---

## Synthesis

| Test | Question | Result | Favors |
|------|----------|--------|--------|
| T1 | Interaction with hindrance | Strongest in H0 | Barrier |
| T2 | Persists after parity control | Yes (p=0.016) | Not pairing proxy |
| T3 | Prefactor vs barrier placement | Prefactor wins (AIC) | **Prefactor** |

### Apparent Contradiction

T1 suggests barrier (effect strongest when barrier matters most).
T3 suggests prefactor (additive model fits better).

### Resolution

This is not contradictory. The mechanism is likely:

**Frustration (high d(n)) → Enhanced surface dynamics → Easier α preformation (S_α ↑) → Faster decay**

But the *visibility* of this effect depends on what else limits the rate:
- In H0: Barrier is the main limit, so any boost to S_α is immediately visible
- In H1/H2: Selection rules dominate, masking the S_α enhancement

---

## Physical Picture

```
Standard (low d(n)):
  α-cluster forms slowly → attempts barrier → tunnels

Frustrated (high d(n)):
  Lattice strain/defects → enhanced surface reorganization
  → α-cluster forms more easily (S_α ↑)
  → more attempts per unit time → faster decay
```

This is analogous to:
- Defects in crystals enhancing diffusion
- Grain boundaries facilitating nucleation
- Frustrated magnets having enhanced dynamics

---

## Verdict

**Most consistent with: PREFACTOR (S_α enhancement)**

Evidence:
1. Model A (additive) fits better than Model B (multiplicative barrier)
2. Effect persists after controlling for parity/pairing
3. Physical interpretation (frustration → dynamics → preformation) is coherent
4. Visibility pattern in H0/H1/H2 is explained by rate-limiting step

The "paradox" is resolved: **frustration destabilizes, it doesn't stabilize**. In decay physics, instability = faster decay.

---

## Quantitative Estimate

If g = -0.31 acts entirely through S_α:
```
log₁₀(S_α) ≈ k₀ + 0.31 × d(n)
```

For d(n) = 0 → 3:
- S_α increases by factor 10^(0.31×3) ≈ 8
- Half-life decreases by same factor

This is a physically plausible range for preformation factor variation.

