# OPEN-22-4: Physical V(ξ) + Physical BVP Closure Report

**Status**: CONDITIONAL [Dc]
**Date**: 2026-01-25
**Sprint**: OPEN-22-4

---

## Executive Summary

This report documents the upgrade of OPR-22 from toy-verified to physical-verified
by implementing the complete pipeline:

```
OPR-01 (σ→M₀) → OPR-21 (V(ξ)→modes) → OPEN-22-1 (f₁(0)²) → OPR-22 (G_eff)
```

**Key Results**:
- Pipeline operational with physical V(ξ) = M² - M' from 5D Dirac
- N_bound = 3 regime identified at μ ≈ 10
- Physical |f₁(0)|² = 0.57, x₁ = 7.77 in target regime
- G_eff = (g₅²ℓ) × 0.0048 computed for physical parameters

---

## Input Primitives and Epistemic Tags

### DERIVED [Dc] — Used as structural inputs

| Quantity | Formula | Source |
|----------|---------|--------|
| V_L(ξ) | M² - M' | OPR-21 L2: 5D Dirac reduction |
| M₀² | (3/4) y² σ Δ | OPR-01 Lemma 4: sigma anchor |
| μ = M₀ℓ | (√3/2) y n √(σΔ³) | OPR-01 consequence |
| f₁(0) extraction | f₁ = f̃₁√ℓ | OPEN-22-1 resolution |
| G_eff | g₅²ℓ\|f₁(0)\|²/(2x₁²) | OPR-22 L9 |

### POSTULATED [P] — Remain as primitives

| Parameter | Physical Role | Required For |
|-----------|---------------|--------------|
| σ | Membrane tension | M₀ computation |
| Δ | Domain wall width | V(ξ) shape |
| ℓ (or n = ℓ/Δ) | Domain size | BVP eigenvalues |
| y | Yukawa coupling | M₀ computation |
| g₅ | 5D gauge coupling | G_eff absolute value |

---

## V(ξ) Derivation Path

### Source: OPR-21 L2 (5D Dirac Reduction)

Starting from 5D Dirac equation with domain-wall mass profile:

```
M(ξ) = M₀ tanh((ξ - ℓ/2)/Δ)
```

The effective potential for left-handed fermions (flat space, A = 0):

```
V_L(ξ) = M(ξ)² - M'(ξ)
       = M₀² tanh²(...) - (M₀/Δ) sech²(...)
```

**Derivation status**: [Dc] — structure derived from 5D Dirac equation

### Chirality Asymmetry

The right-handed potential differs by sign of M' term:

```
V_R(ξ) = M(ξ)² + M'(ξ)
V_R - V_L = 2M'
```

This asymmetry is the **geometric origin of V−A structure** in weak interactions.

---

## Connection to OPR-01 (σ Anchor)

### M₀ from Membrane Tension

From OPR-01 Lemma 4 (scalar kink theory):

```
M₀² = (3/4) y² σ Δ
M₀ = (√3/2) y √(σΔ) ≈ 0.866 y √(σΔ)
```

### Dimensionless Parameter μ

```
μ = M₀ ℓ = (√3/2) y n √(σΔ³)
```

where n = ℓ/Δ is the domain-size ratio.

### Consistency Constraint

For N_bound = 3 with physical V(ξ) = M² - M':
- Original OPR-21 estimate: μ ∈ [25, 35] (for Pöschl-Teller-like potential)
- Physical domain wall result: μ ≈ 10 gives N_bound = 3

**Important note**: The domain wall potential V = M² - M' has different spectral
properties than the reference Pöschl-Teller potential. The N_bound = 3 window
occurs at lower μ values.

---

## Numerical Results

### μ Scan (n = 4, Δ = 1)

| μ | M₀ | N_bound | x₁ | \|f₁(0)\|² | G_eff/(g₅²ℓ) | Regime |
|---|----|---------|----|------------|--------------|--------|
| 5 | 1.25 | 2 | 6.05 | 1.10 | 0.0150 | N=2 |
| 10 | 2.50 | 3 | 7.77 | 0.57 | 0.0048 | **TARGET** |
| 15 | 3.75 | 4 | 9.16 | 0.40 | 0.0024 | N=4 |
| 20 | 5.00 | 5 | 10.38 | 0.31 | 0.0014 | N=5 |
| 25 | 6.25 | 5 | 11.48 | 0.26 | 0.0010 | N=5 |
| 30 | 7.50 | 6 | 12.50 | 0.22 | 0.0007 | N=6 |

### Key Observation

The domain wall potential V = M² - M' has a **wider well** than assumed
in the original OPR-21 phase diagram. N_bound = 3 is achieved at μ ≈ 10,
not μ ∈ [25, 35] as estimated for Pöschl-Teller.

---

## G_eff Formula Verification

### Structure (OPR-22 L9)

```
G_eff = g₅² ℓ |f₁(0)|² / (2 x₁²)
      = (1/2) C_eff |f₁(0)|²
```

where C_eff = g₅² ℓ / x₁² from OPR-20.

### Dimensional Analysis

| Quantity | Dimension |
|----------|-----------|
| g₅² | L |
| ℓ | L |
| \|f₁(0)\|² | 1 (natural norm) |
| x₁² | 1 |
| G_eff | L² = GeV⁻² ✓ |

### Numerical Factor in Target Regime

At μ = 10 (N_bound = 3):
```
G_eff = (g₅² ℓ) × |f₁(0)|² / (2 x₁²)
      = (g₅² ℓ) × 0.57 / (2 × 60.4)
      = (g₅² ℓ) × 0.0048
```

---

## No-Smuggling Certification

### NOT Used as Inputs

- M_W (W boson mass)
- M_Z (Z boson mass)
- G_F (Fermi constant)
- v = 246 GeV (Higgs VEV)
- sin²θ_W (weak mixing angle)
- α(M_Z) (running fine structure)
- PMNS/CKM matrix elements
- τ_n (neutron lifetime)
- CODATA fits

### Used as Inputs

- ✓ Scalar kink theory [M]
- ✓ 5D Dirac reduction [Dc]
- ✓ Domain wall mass profile [P]
- ✓ Yukawa coupling mechanism [P]
- ✓ Sturm-Liouville eigenvalue theory [M]

**Certification**: PASS

---

## Closure Status

### What is DERIVED [Dc]

1. V(ξ) = M² - M' structure from 5D Dirac equation
2. M₀ = f(σ, Δ, y) from sigma anchor (OPR-01)
3. |f₁(0)|² extraction procedure from BVP (OPEN-22-1)
4. G_eff = g₅²ℓ|f₁(0)|²/(2x₁²) structure from EFT (OPR-22)

### What Remains [P] Postulated

1. σ — membrane tension (awaits cosmological derivation)
2. Δ — domain wall width (awaits brane microphysics)
3. ℓ — domain size (awaits domain-size principle)
4. y — Yukawa coupling (awaits gauge embedding)
5. g₅ — 5D gauge coupling (awaits UV completion)

### Upgrade Path to Full [Der]

- Derive σ from independent physics (gravitational, cosmological)
- Derive Δ from junction stability or scalar potential
- Derive g₅ from membrane stiffness/conductivity

---

## Files Generated

| File | Type | Purpose |
|------|------|---------|
| code/opr22_open22_4_physical_run.py | Code | Physical BVP pipeline |
| code/output/open22_4_physical_summary.json | Data | Machine-readable results |
| code/output/open22_4_physical_table.md | Report | Human-readable table |
| audit/evidence/OPEN22_4_PHYSICAL_VEFF_REPORT.md | Evidence | This report |

---

## Conclusion

OPEN-22-4 is **CONDITIONAL [Dc]**:
- The pipeline OPR-01 → OPR-21 → OPEN-22-1 → OPR-22 is fully operational
- Physical V(ξ) produces quantitative outputs
- All structural elements are derived [Dc]
- Parameter values remain postulated [P]

The key finding: N_bound = 3 occurs at μ ≈ 10 for the physical domain wall
potential, which differs from the original estimate (μ ∈ [25, 35]) based on
Pöschl-Teller-like potentials. This is not a failure — it reflects the actual
spectral properties of V = M² - M'.

---

*Generated: 2026-01-25*
*Sprint: OPEN-22-4*
*Status: CONDITIONAL [Dc]*
