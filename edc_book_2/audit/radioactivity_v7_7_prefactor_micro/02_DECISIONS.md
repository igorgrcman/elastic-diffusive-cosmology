# V7.7 DECISIONS

**Created**: 2026-01-31
**Purpose**: Document method choices and hypothesis definitions

---

## What Counts as "Prefactor Mechanism"

### Definition [Der]

The prefactor interpretation means d(n) enters the decay rate through:
```
λ = ν × P_tunnel × S_α(d)
```

where S_α(d) is the preformation factor that depends on d(n).

**NOT through**:
- P_tunnel modification (barrier height/width)
- ν modification (attempt frequency)

### Justification

From V7.6.1 T3: Model A (additive in log₁₀t₁/₂) beats Model B (multiplicative in barrier term) by AIC Δ = 3.4.

Additive in log-space = multiplicative in rate-space = prefactor.

---

## What Counts as "Crystal Analogy"

### Definition [I]

Crystal analogy maps:
| Crystal Concept | Nuclear Analog |
|-----------------|----------------|
| Coordination number | M-topology n |
| Lattice defect | Forbidden n deviation |
| Defect-enhanced diffusion | Frustration-enhanced S_α |
| Grain boundary | Domain wall (M1) |
| Vacancy | Missing coordination (M2) |

### Validity Conditions

The analogy holds if:
1. Both systems have discrete allowed coordinations
2. Defects/frustration enhance dynamics in both
3. Quantitative scaling is similar (not required, qualitative sufficient)

### Where Analogy Fails

See 06_CRYSTAL_DEFECT_ANALOGY.md for explicit failure modes.

---

## Hypothesis Classifications

### [Der] — Derived

- g = -0.31 ± 0.11, p = 0.006 (from V7.4 OLS)
- CV ΔRMSE = 0.043 (from V7.5)
- T1: g(H0) = -0.34, g(H1) ≈ -0.26, g(H2) ≈ -0.22 (from V7.6.1)
- T2: g = -0.29 after parity control (from V7.6.1)
- T3: AIC(prefactor) - AIC(barrier) = -3.4 (from V7.6.1)

### [I] — Inferred

- M1 domain mixing (from DN-040, 22826edd:2479-2492)
- M3 α-clusterization (from DN-043..044, 22826edd:2450-2478)
- Crystal → nucleus coordination mapping (from DN-050..058)

### [P] — Proposed

- S_α(d) = S₀ × 10^(k×d) functional form
- Frustration → surface dynamics → preformation mechanism
- M2 defects, M4 metastable, M5 quasicrystal, M6 core-mantle

---

## Model Selection Criteria

### Primary: AIC/BIC

Lower is better. Prefer simpler model if ΔAIC < 2.

### Secondary: CV RMSE

Out-of-sample prediction accuracy. Prefer model with lower CV RMSE.

### Tertiary: Physical Plausibility

Among statistically equivalent models, prefer one with clearer physical interpretation.

---

## Falsification Protocol

1. State claim with epistemic tag
2. Identify observable
3. Define threshold for rejection
4. If data exists, test; otherwise mark [Open]
5. Update tag based on result

---

## Scope Boundaries

### In Scope

- α-decay only (V7.4 dataset)
- n ∈ [36, 39] (actual data range)
- Prefactor vs barrier interpretation
- Crystal analogy (qualitative)
- Forbidden zone mechanisms M1-M6

### Out of Scope

- β-decay
- Fission
- Supernova nucleosynthesis
- Quantitative crystal-nucleus parameter matching
- New BL data sourcing

