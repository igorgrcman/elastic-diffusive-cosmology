# Chapter Map — Book IV

**Date:** 2026-02-10

---

## Part I: Foundation (Ch 1–3)

### Chapter 1: Anchor Junction as Topological Ground State
**Purpose:** Establish the Z₆ anchor junction as the stable ground state via Steiner geometry.
- Key results: 120° Y-junction, hexagonal tiling, energy minimum
- Tables: —
- OPEN: S⁵ → Z₆ crystallization map formalization

### Chapter 2: Junction Symmetries
**Purpose:** Derive Z₆ symmetry from M₆ graph duality; prove n=6 coordination.
- Key results: Primal/dual graph theorem, n=6 derivation (Eq. deriv:n_equals_6)
- Tables: —
- OPEN: Full 5D topological descent proof

### Chapter 3: The Metastable Junction
**Purpose:** Introduce Z₃ metastable branch and barrier height conjecture.
- Key results: V_B conjecture (Eq. eq:VB_conjecture), Δm mapping
- Tables: —
- OPEN: Barrier quantization from first principles

---

## Part II: Instanton Chain (Ch 4–9)

### Chapter 4: From Brane Tension to Pinning Constant
**Purpose:** Derive K from σ via contact geometry.
- Key results: K = f × σ × A_contact (Tab. tab:sigmaK:chain)
- OPEN: f-factor from 5D action

### Chapter 5: The M₆ Coordination Lattice
**Purpose:** Construct M₆ lattice; derive allowed set S = {2ᵃ3ᵇ} and forbidden zone.
- Key results: S derivation, forbidden zone [37,47], d(n) metric
- Tables: tab:M6:graphs, tab:M6:status
- OPEN: Uniqueness of S

### Chapter 6: The Instanton Chain
**Purpose:** 5D → effective action reduction for tunneling.
- Key results: S_E formula, exponential suppression
- OPEN: Full path-integral derivation

### Chapter 7: The Homotopy Factor κ
**Purpose:** Derive κ = 2π from π₁(S¹) = ℤ.
- Key results: κ = 2π [Der]
- OPEN: —

### Chapter 8: The L₀/δ Ratio
**Purpose:** Establish L₀/δ ≈ π² as key sensitivity parameter.
- Key results: L₀/δ = π² [P]
- OPEN: **Critical** — derivation from 5D geometry (boss-dependency)

### Chapter 9: Metastable Lifetime Prediction
**Purpose:** Synthesize τ_n ≈ 880 s from all parameters.
- Key results: τ formula, numerical evaluation
- Tables: metastable parameter summary
- OPEN: Prefactor A derivation

---

## Part III: Cluster Physics (Ch 10–12)

### Chapter 10: Deuterium Binding
**Purpose:** Derive B₂ ≈ 2.22 MeV from junction geometry.
- Key results: Binding formula
- OPEN: —

### Chapter 11: The Closed-4 Unit
**Purpose:** Establish Closed-4 as minimal stable cluster with binding budget.
- Key results: B₄ ≈ 28.3 MeV, localization sharing
- Tables: Multiple binding tables
- OPEN: **Critical** — Closed-4 minimality proof (TODO obligation)

### Chapter 12: Light Cluster Systematics
**Purpose:** Extend to A = 2–10 clusters (Li-6, Be-8, etc.).
- Key results: Systematic predictions
- Tables: Light cluster binding table
- OPEN: —

---

## Part IV: High-Coordination (Ch 13–15)

### Chapter 13: Barrier-Release Law (Geiger-Nuttall Lane)
**Purpose:** Establish baseline GN lane for Closed-4 release.
- Key results: log t = a·GN + b formula
- Tables: tab:variables (baseline dictionary)
- Tags: [BL]

### Chapter 14: Coordination Frustration
**Purpose:** Introduce d(n) frustration correction to baseline.
- Key results: Δ ≈ g·d(n), improved fit
- Tags: [Cal]
- OPEN: Why d(n) is the right metric

### Chapter 15: High-Coordination Predictions
**Purpose:** Superheavy (Z = 114–120) predictions with uncertainties.
- Key results: Prediction table with error bars
- Tables: Superheavy predictions
- Tags: [P]

---

## Part V: Synthesis (Ch 16–17)

### Chapter 16: The Unified Picture
**Purpose:** Synthesize all threads; derivation tree; reading paths.
- Key results: Ontology glossary, derivation ledger, epistemic summary
- Tables: tab:unified:glossary, tab:unified:tree, tab:unified:epistemic

### Chapter 17: Reproducibility & Verification
**Purpose:** Exact reproduction recipes; contamination scan protocol.
- Key results: 4 recipes (R1–R4), hash manifest
- Tables: tab:repro:artifacts, tab:repro:layerAB
- OPEN: CI/CD pipeline (OPEN Problem 17.1)

---

## Appendices

| App | Purpose | Key Content |
|-----|---------|-------------|
| A | Code | superheavy_predictions.py listing |
| B | Code | kramers_double_well_v2.py listing |
| C | Tables | Numerical data tables |
| D | Provenance | Chapter → source file mapping |
| Q | Quarantine | Calibrated parameters [Cal]/[BL] |
| X | Analogies | SM translations (allow-zone) |

---

## Critical OPEN Items (Boss Dependencies)

1. **L₀/δ derivation** — τ is exponentially sensitive; π² needs rigorous derivation
2. **Closed-4 minimality proof** — why A=4 is optimal (TODO obligation)
3. **Prefactor A derivation** — currently [Cal]/[OPEN]
4. **S⁵ → Z₆ crystallization** — formalization needed
