# OPR-01: σ → M₀ Anchor

**Status**: CONDITIONAL [Dc] (upgraded from OPEN)
**Date**: 2026-01-25
**Sprint**: book2-opr01-sigma-anchor-v1

---

## Summary

OPR-01 addresses the derivation of the bulk mass amplitude M₀ from the membrane
tension σ. The 2026-01-25 sprint achieved **CONDITIONAL [Dc]** status by deriving
M₀ as a function of σ and Δ using scalar kink theory.

---

## Main Result

**Derived relation** [Dc]:
```
M₀² = (3/4) y² σ Δ

M₀ = (√3/2) y √(σΔ)  ≈  0.866 y √(σΔ)
```

where:
- σ = membrane tension [P]
- Δ = domain-wall thickness [P]
- y = Yukawa coupling [P]

**Consequence for μ = M₀ℓ** [Dc]:
```
μ = (√3/2) y n √(σΔ³)

where n = ℓ/Δ (domain-size ratio)
```

**Consistency constraint for N_bound = 3**:
```
σ Δ³ ∈ [52, 102]   (for μ ∈ [25, 35) with y=1, n=4)
```

---

## Derivation Chain

### Lemma 1: Scalar Kink Solution [M]

For double-well potential V(φ) = (λ/4)(φ² - v²)²:
```
φ(ξ) = v tanh(ξ/Δ)

Δ = 2/(v√λ)
```

### Lemma 2: Domain-Wall Tension [M]

Integration of stress-energy:
```
σ = ∫ T₀₀ dξ = 4v²/(3Δ)

⟹  σ Δ = 4v²/3
```

### Lemma 3: Yukawa Mass Profile [P]+[Dc]

Fermion mass from scalar coupling:
```
M(ξ) = y φ(ξ) = M₀ tanh(ξ/Δ)

M₀ = y v
```

### Lemma 4: M₀ from σ [Dc]

Combining Lemmas 2 and 3:
```
v = M₀/y   and   σΔ = 4v²/3

⟹  σΔ = 4M₀²/(3y²)

⟹  M₀² = (3y²/4) σΔ
```

---

## Epistemic Tags

| Parameter | Before Sprint | After Sprint |
|-----------|---------------|--------------|
| σ | [P] | [P] (unchanged, still primitive) |
| Δ | [P] | [P] (unchanged) |
| y | [P] | [P] (unchanged) |
| M₀ | [P] | **[Dc]** (derived from σ, Δ, y) |
| μ = M₀ℓ | [P] | **[Dc]** (derived via M₀) |

---

## No-Smuggling Certification

**NOT used as inputs:**
- M_W, M_Z (electroweak masses)
- G_F (Fermi constant)
- v = 246 GeV (Higgs VEV)
- sin²θ_W (weak mixing angle)
- α(M_Z) (running fine structure)
- PMNS/CKM elements
- τ_n (neutron lifetime)
- CODATA fits

**Used as inputs:**
- ✓ Scalar kink theory [M]
- ✓ Domain-wall ansatz [P]
- ✓ Yukawa coupling mechanism [P]

---

## Connection to Other OPRs

| OPR | Relation | Status |
|-----|----------|--------|
| OPR-02 | Robin BC parameter κ may relate to M₀ | Indirect |
| OPR-04 | δ ≡ R_ξ may determine Δ | Potential closure path |
| OPR-12 | V(ξ) from kink determines mode spectrum | Direct input |
| **OPR-21** | **μ = M₀ℓ enters N_bound calculation** | **Direct dependency** |
| OPR-22 | G_F derivation needs M₀ for mode profiles | Downstream |

---

## Remaining Open Items

For full [Der] closure (currently [Dc]):

1. **Derive σ** from independent physics (cosmological, gravitational)
2. **Derive Δ** from junction stability or brane microphysics
3. **Derive y** from gauge embedding or naturalness arguments
4. **Derive n = ℓ/Δ** from domain-size principle

---

## Documentation

| Document | Location |
|----------|----------|
| Derivation (book chapter) | src/sections/ch15_opr01_sigma_anchor_derivation.tex |
| Evidence report | audit/evidence/OPR01_SIGMA_ANCHOR_REPORT.md |
| Numeric check | code/opr01_sigma_anchor_check.py |
| This file | canon/opr/OPR-01.md |

---

## Closure Test

**OPR-01 is CLOSED iff:**
1. M₀ is derived from σ without circular dependency ✓
2. No SM observables used as inputs ✓
3. Derivation chain is explicit and tagged ✓

**Current status: CONDITIONAL [Dc]**
- Condition: Domain-wall ansatz for M(ξ)
- Condition: Yukawa coupling mechanism

---

*Last updated: 2026-01-25*
*Sprint: book2-opr01-sigma-anchor-v1*
