# Breadth Synthesis — 2026-01-29

**Status:** Canonical summary of cross-sector breadth work
**Purpose:** Front-door document for EDC cross-sector synthesis
**Scope:** What is derived, what is constrained, what fails

---

## A. Executive Summary (6 Bullets)

1. **Universal mechanism exists** — Projection-Reduction Lemma connects EM, Weak, and Nuclear via single formalism
2. **Three GREEN anchors** — N_g=3 [Der], sin²θ_W=1/4 [Der], Δm_np [Der/Dc] with ε=0.68% reconciliation
3. **G_F is a constraint window** — Target: g_eff²/M_eff² ∈ [0.9,1.1]×G_F; first-principles derivation OPEN
4. **N_cell=12 bridges scales** — 70 MeV / 5.856 MeV tension resolved algebraically (0.35% match)
5. **σ is master parameter** — Cancels in EM/Δm_np (ROBUST); explicit in τ_n/Λ/g² (FRAGILE)
6. **Four NO-GO results documented** — Z₃ DFT fails for CKM (×144), PMNS (×15), CP (J=0), Gaussian profiles (×100)

---

## B. Universal Mechanism: Projection-Reduction

**Source:** `edc_papers/_shared/lemmas/projection_reduction_lemma.tex`

**Statement:** Bulk→brane observation is linear projection; 4D observables are weighted averages of bulk structure.

**Three Cases:**

| Case | Mechanism | 4D Result | Sector |
|------|-----------|-----------|--------|
| (A) | Lagrangian integration | Z_eff, V_eff as integrals | EM, Nuclear |
| (B) | Chirality selection | ε ≪ 1 → V-A structure | Weak |
| (C) | Barrier projection | κ_eff from energy profile | Nuclear tunneling |

**Cross-sector power:** Same 𝒫_w operator unifies EM↔Weak↔Nuclear.

---

## C. GREEN Anchors (True Predictions)

### C.1 N_g = 3 (Generation Count) [Der]

```
N_g = |Z_6/Z_2| = |Z_3| = 3
```
**Source:** Framework v2.0 §10.3
**Status:** GREEN — discrete group structure, no free parameters

### C.2 sin²θ_W = 1/4 (Weinberg Angle) [Der]

```
sin²θ_W = |Z_2|/|Z_6| = 2/6 = 1/4 (bare)
         → 0.2314 at M_Z (0.08% from PDG after RG)
```
**Source:** Framework v2.0 §10.4
**Status:** GREEN — geometric ratio, RG evolution standard

### C.3 Δm_np = (8/π)m_e (Mass Difference) [Der/Dc]

**Two models coexist:**

| Model | Formula | Value | Error |
|-------|---------|-------|-------|
| Z_6 Ring (bare) | (8/π)m_e | 1.301 MeV | +0.6% |
| Dimensional (renormalized) | (5/2+4α)m_e | 1.292 MeV | -0.07% |

**Reconciliation [I]:**
```
(8/π)(1 - ε) = 5/2 + 4α   where ε = 0.679%
```
**Interpretation:** 8/π = bare geometry; 5/2+4α = EM-corrected
**Source:** `docs/DELTA_MNP_RECONCILIATION.md`

---

## D. Falsification Channels

### D.1 G_F Constraint Window

**Target [Dc]:**
```
g_eff²/M_eff² ∈ [0.9, 1.1] × G_F
Dimensionless: X = G_F m_e² = 3.04 × 10⁻¹² (natural units)
```

**Fail modes (any → EDC falsified):**
1. BVP yields I₄ incompatible with G_F (>10× mismatch)
2. KK reduction gives M_eff inconsistent with δ
3. g_eff from 5D action inconsistent with sin²θ_W structure

**Status:** RED-C (first-principles derivation open)
**Source:** `docs/GF_CONSTRAINT_NOTE.md`, `edc_papers/_shared/boxes/gf_constraint_box.tex`

### D.2 N_cell = 12 Bridge

**The tension:**
```
E_σ = 70 MeV (EM scale, m_ec²/α)
(σr_e²)_Z6 = 5.856 MeV (Z_6 ring, 36m_e/π)
Ratio: 70/5.856 = 11.96 ≈ 12
```

**Algebraic resolution [I]:**
```
N_cell = π/(36α) = 11.96 → 12 gives 0.35% match
```

**Candidate meanings of 12:**

| Decomposition | Meaning | Breadth Link |
|---------------|---------|--------------|
| 2 × 6 | Z_2 × Z_6 | Chirality |
| 3 × 4 | N_g × N_Dirac | Flavor/Weak |
| 12 | HCP coordination | Spatial geometry |

**Fail mode:** If no geometric derivation of 12, then OP-σ-2 remains open.
**Source:** `docs/OP-SIGMA-2_NCELL12_RESOLUTION.md`

---

## E. σ Map: Robust vs Fragile

| Observable | σ enters as | Cancels? | Status |
|------------|-------------|----------|--------|
| Δm_np (Z_6) | σr_e² = 36m_e/π | YES | **ROBUST** |
| Δm_np (dim) | — | — | **ROBUST** |
| α⁻¹ | implicit via r_e | YES | **ROBUST** |
| m_π/m_e | E_σ = m_ec²/α | YES | **ROBUST** |
| V_0 (barrier) | σ explicit | NO | *FRAGILE* |
| τ_n | exp(S) ∝ V_0 | NO | *FRAGILE* |
| Λ (cosmo) | σ/(8c²R_H²) | NO | *FRAGILE* |
| g² | 4πσr_e³/(ℏc) | NO | *FRAGILE* |

**Master parameter:** σ = m_e³c⁴/(α³ℏ²) = 8.82 MeV/fm² [Dc]
**Source:** `docs/SIGMA_DEPENDENCY_AUDIT.md`

---

## F. Next 3 Tests (Ranked: Cheap → Expensive)

### Test 1: Pion Mass Splitting [CHEAP]

**Question:** Does π⁺-π⁰ splitting show same ε ≈ 0.68% EM correction pattern?
**Method:** Check if existing EDC formula contains 2(1-ε) factor
**Falsifies:** Candidate 1 for ε origin (double-well asymmetry)

### Test 2: N_cell Geometric Derivation [MEDIUM]

**Question:** Which 12-decomposition (2×6, 3×4, HCP) is correct?
**Method:** Check consistency with other EDC predictions (V-A, N_g, Dirac structure)
**Falsifies:** OP-σ-2 if no consistent interpretation found

### Test 3: BVP Mode Profiles [EXPENSIVE]

**Question:** Does I₄ = ∫f_L⁴ fall in G_F constraint window?
**Method:** Solve 5D thick-brane BVP, extract mode profiles, compute overlap
**Falsifies:** G_F constraint (decisive channel)
**Source:** OPR-04 in Open Problems Register

---

## Cross-References

| Document | Content |
|----------|---------|
| `edc_papers/_shared/lemmas/projection_reduction_lemma.tex` | Projection-Reduction Lemma |
| `docs/FLAVOR_SKELETON_v0.1.md` | N_g, sin²θ_W, mixing details |
| `docs/DELTA_MNP_RECONCILIATION.md` | ε = 0.679% bridge |
| `docs/SIGMA_DEPENDENCY_AUDIT.md` | σ master parameter map |
| `docs/GF_CONSTRAINT_NOTE.md` | G_F constraint window |
| `docs/OP-SIGMA-2_NCELL12_RESOLUTION.md` | N_cell = 12 analysis |

---

*This document synthesizes cross-sector breadth work from 2026-01-29. No new derivations; all claims anchored to existing canon.*
