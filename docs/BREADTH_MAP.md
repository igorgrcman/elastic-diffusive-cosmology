# BREADTH MAP — Cross-Sector Synthesis

**Generated:** 2026-01-29
**Source:** KNOWLEDGE_INVENTORY + CLAIM_LEDGER + OPEN_PROBLEMS_REGISTER
**Purpose:** Identify bridge mechanisms and cross-sector tests

---

## 5 Bridge-Candidate Mechanisms

### 1. Projection Operator 𝒫_w

**Appears in:**
- EM: bulk field → 4D Maxwell
- V-A: chirality selection via L/R overlap ε ≪ 1
- Nuclear: barrier as projected energy profile

**Cross-sector power:** Connects EM ↔ Weak ↔ Nuclear with one formalism.

**Status:** [P] → needs formal lemma (see TP-2026-01-29)

---

### 2. Discrete Group Structure Z_6 = Z_2 × Z_3

**Appears in:**
- sin²(θ_W) = |Z_2|/|Z_6| = 1/4 [Der]
- N_g = |Z_6/Z_2| = |Z_3| = 3 [Der]
- Koide Q = |Z_2|/|Z_3| = 2/3 [I]
- Neutron: θ = 60° = 360°/6 [Dc]

**Cross-sector power:** Connects Weak ↔ Flavor ↔ Nuclear geometry.

**Status:** GREEN for sin²(θ_W), N_g. YELLOW for Koide. Open for full CKM/PMNS.

---

### 3. Membrane Tension σ

**Appears in:**
- Nuclear: V_eff = σ × area terms
- EM: E_σ = m_e c²/α = 70 MeV [Dc]
- Barrier: ΔV ~ σ × geometric factor
- Cosmology: Λ = σ/(8c²R_H²) [Der] (chapter_11)

**Cross-sector power:** Connects Nuclear ↔ EM ↔ Cosmology.

**Status:** [Dc] — formula σ = m_e³c⁴/(α³ℏ²) depends on hypothesis.

---

### 4. Brane Thickness δ and Junction Extent L_0

**Appears in:**
- δ = ℏ/(2m_p c) = 0.105 fm [Dc]
- L_0 = r_p + δ = 0.98 fm [P]
- τ_n via instanton action S_E [Dc]
- Pinning constant K ~ f × σ × A_contact [I]

**Cross-sector power:** Connects Nuclear geometry ↔ tunneling dynamics.

**Status:** TENSION: static prefers L_0/δ = π², dynamic prefers 9.33.

---

### 5. Δm_np = 8m_e/π as Hadronic-Leptonic Bridge

**Appears in:**
- Nuclear: n-p mass difference
- Contains: m_e (lepton sector)
- Factor 8/π: geometric origin?

**Cross-sector power:** Connects Nuclear ↔ Leptonic directly.

**Status:** [Der] with 0.6% error. Robustness test needed.

---

## 2 Fastest Cross-Sector Tests

### Test 1: Projection Lemma Universality

**Objective:** Show that Cases (A), (B), (C) of Projection-Reduction Principle use consistent notation.

**Method:**
1. Write generic projection operator 𝒫_w
2. Apply to EM (check reproduces known result)
3. Apply to V-A (check ε ≪ 1 gives chirality)
4. Apply to barrier (check κ_eff matches pinning)

**Success criterion:** Same formal structure, different sector-specific weights.

**Time estimate:** 1 day

---

### Test 2: Δm_np Dimensionless Robustness

**Objective:** Check if 8m_e/π is stable under parameter variations.

**Method:**
1. Rewrite derivation with only dimensionless ratios
2. Identify which parameters enter (σ, δ, L_0, α?)
3. Compute sensitivity: ∂(Δm_np)/∂(parameter)
4. Check: does formula survive if σ or δ changes by 10%?

**Success criterion:** Low sensitivity → robust bridge. High sensitivity → fragile, needs constraint.

**Time estimate:** 0.5 day

---

## σ/δ/L_0 Dependency Table

| Quantity | Formula | σ | δ | L_0 | α | Status |
|----------|---------|---|---|-----|---|--------|
| **σ** | m_e³c⁴/(α³ℏ²) | — | — | — | α⁻³ | [Dc] |
| **δ** | ℏ/(2m_p c) | — | — | — | — | [Dc] |
| **L_0** | r_p + δ | — | δ | — | — | [P] |
| **K** | f × σ × A_contact | σ | δ | L_0 | — | [I] |
| **τ_n** | (ℏ/ω_0) exp(S_E/ℏ) | σ | δ | L_0 | — | [Dc/Cal] |
| **V_eff** | σ × geometric | σ | — | — | — | [Dc] |
| **Δm_np** | 8m_e/π | ? | ? | ? | — | [Der] |
| **Λ (cosmo)** | σ/(8c²R_H²) | σ | — | — | — | [Der] |

**Observation:** σ is the **master parameter** — appears in nuclear, EM, cosmology.

---

## Dependency Graph (Simplified)

```
                    ┌──────────────┐
                    │   POSTULATES │
                    │  (7 total)   │
                    └──────┬───────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │  Geometry │    │  Plenum  │    │ Membrane │
    │  M⁵=ℝ¹'³×S¹│    │  ρ_P>0   │    │  Σ⁴@ξ=0  │
    └─────┬────┘    └────┬─────┘    └────┬─────┘
          │              │               │
          └──────────────┼───────────────┘
                         ▼
                  ┌─────────────┐
                  │      σ      │ ◄── MASTER PARAMETER
                  │ 8.82 MeV/fm²│
                  └──────┬──────┘
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
   ┌──────────┐    ┌──────────┐    ┌──────────┐
   │ NUCLEAR  │    │    EM    │    │ COSMOLOGY│
   │ τ_n, K   │    │ α, m_e   │    │    Λ     │
   └──────────┘    └──────────┘    └──────────┘
```

---

## Next Actions (Priority Order)

1. **[TODAY]** Formalize Projection Lemma in LaTeX
2. **[TODAY]** Δm_np sensitivity analysis
3. **[NEXT]** σ dependency audit (complete table)
4. **[NEXT]** Flavor Skeleton v0.1
5. **[FUTURE]** G_F constraint note

---

*This map synthesizes breadth opportunities from existing inventory. No new derivations, only structure.*
