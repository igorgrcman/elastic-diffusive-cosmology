# 2-Column Dependency Test: α vs σ

**Date:** 2026-02-02
**Context:** Clarification of v11 NO-GO finding

---

## Test A: α Derivation Isolation

**Question:** Can α be derived from purely dimensionless geometric parameters?

### Finding: **YES**

EDC Book I (Chapter 4, line 452) provides:

```
α = (4π + 5/6) / (6π⁵)
```

**Numerical verification:**
```python
>>> (4*π + 5/6) / (6*π⁵)
= 0.00729784
= 1/137.0268
```

**Observed:** 1/α = 137.036

**Agreement:** 0.007% (excellent)

### Analysis

| Component | Type | Dimensional? |
|-----------|------|--------------|
| 4π | Geometric | No |
| 5/6 | Rational | No |
| 6π⁵ | Geometric | No |
| **Result α** | **Dimensionless** | **No** |

**Conclusion:** α IS a genuine geometric derivation. No σ, ℏ, m_e, G_N, or any dimensional constant appears.

---

## Test B: σ Origin

**Question:** Where is σ first numerically fixed?

### Finding: σ is **CALIBRATED** from observed constants

From Chapter 6 (line 758):
```
σ_eff = m_e c² / (α · r_e²) = 1.41 × 10¹⁸ J/m²
```

From Chapter 0 Theory Core (line 1499):
```
C1: σ_eff ≈ 1.41 × 10¹⁸ J/m² (from α, m_e, r_e) | Fixed by α
```

From Chapter 6 (line 791):
> "Since σ_eff was **extracted from α** using equation (eq:alpha_final), and both α and ℏ are related to the same underlying constants (m_e, c, r_e), recovering ℏ demonstrates **internal consistency of the EDC relations—not predictive power**."

### Dependency Chain

```
σ = m_e c² / (α · r_e²)
    ↑      ↑     ↑
    |      |     └── r_e = 2.82×10⁻¹⁵ m (observed/defined)
    |      └──────── α = 1/137 (geometric OR observed)
    └─────────────── m_e = 9.11×10⁻³¹ kg (observed)
```

Even if α is taken from geometry (Test A), **m_e and r_e are still observed/dimensional**.

**Conclusion:** σ IS calibrated. v11 NO-GO stands.

---

## Combined Analysis

### What EDC CAN Do (Dimensionless Predictions)

| Quantity | Formula | Type |
|----------|---------|------|
| α | (4π + 5/6)/(6π⁵) | Pure geometry |
| m_p/m_e | 6π⁵ · α | Geometric ratio |
| m_μ/m_e | (3/2)/α | Geometric ratio |
| Koide Q | 2/3 | Geometric |

### What EDC CANNOT Do (Absolute Scale)

| Quantity | Status |
|----------|--------|
| σ (J/m²) | Requires m_e or ℏ calibration |
| ℏ (J·s) | Requires σ or m_e calibration |
| G_N (m³/kg/s²) | Requires σ (thus m_e) calibration |

---

## Interpretation

**This is NOT a contradiction.** It means:

1. **EDC predicts dimensionless physics** — ratios like α, m_p/m_e, Koide formula
2. **EDC does NOT close the absolute scale** — needs one baseline constant

This is analogous to:
- **QCD:** Predicts hadron mass ratios, but Λ_QCD must be measured
- **String theory:** Predicts dimensionless couplings, but string scale M_s is free

### The One Calibration Point

EDC's "one free parameter" can be chosen as:
- m_e (electron mass) — most natural
- ℏ (Planck constant) — equivalent via σ = ℏc/R_ξ³
- σ (brane tension) — equivalent via σ = m_e c²/(α r_e²)
- r_e (electron radius) — equivalent (r_e = e²/(4πε₀ m_e c²))

All are related by EDC identifications. Fixing ONE fixes all.

---

## v11 NO-GO Clarification

**Original v11 statement:**
> "EDC lacks an independent normalization principle for σ"

**Refined statement:**
> "EDC derives all dimensionless ratios from pure geometry, but the absolute scale (σ, ℏ, m_e, G_N) requires ONE calibration point from observation."

This is **structural**, not a failure. The v11 NO-GO correctly identifies that σ is calibrated.

---

## Summary Table

| Test | Question | Result |
|------|----------|--------|
| **A** | Is α purely geometric? | **YES** — α = (4π+5/6)/(6π⁵) |
| **B** | Is σ calibrated? | **YES** — σ = m_e c²/(α r_e²) |
| **C** | Is m_p/m_e purely geometric? | **YES** — m_p/m_e = 6π⁵ |
| **D** | Is m_e (absolute scale) geometric? | **NO** — Steiner gives ratio, not scale |

**Conclusion:** EDC has genuine geometric content (predicts α, mass ratios) but one unavoidable calibration point for absolute scale.

---

## Test C: Proton-Electron Mass Ratio

**Question:** Is m_p/m_e derived from pure 5D geometry?

### Finding: **YES**

From EDC Paper 2 (edc_papers/paper_2/paper/main.tex):

```
m_p/m_e = Area(S³)³ / Vol(B³) = (2π²)³ / (4π/3) = 6π⁵ = 1836.118
```

**Observed:** m_p/m_e = 1836.15267 (CODATA)

**Agreement:** 0.0018% (excellent)

### The Steiner Minimum Mechanism

From `edc_book_2/src/sections/04b_proton_anchor.tex` and `04c_routeB_z6_steiner.tex`:

**Route A (Topology + Nambu-Goto):**
1. π₁ topological protection [M]+[P]
2. E = τ·L (Nambu-Goto) [Der]
3. Steiner 120° geometry [M]
4. Proton as local minimum [Dc]

**Route B (Z₆ Crystallization):**
1. P2 flux tube repulsion + confinement [P]
2. Kepler-Hales optimal packing [M]
3. Hexagonal lattice [Dc]
4. Equal tensions from Z₆ [Dc]
5. Steiner 120° [M]

Both routes converge on **120° Y-junction geometry**.

### What Steiner Provides vs. What It Doesn't

| Provides (Pure Geometry) | Does NOT Provide |
|--------------------------|------------------|
| 120° angles | Absolute τ (string tension) |
| m_p/m_e = 6π⁵ ratio | m_p in MeV |
| Y-junction topology | m_e in MeV |
| Minimum configuration | σ in J/m² |

---

## Test D: Absolute Mass Scale (m_e)

**Question:** Can m_e be derived from pure 5D geometry?

### Finding: **NO**

The Steiner minimum derivation gives the **ratio** m_p/m_e = 6π⁵, but not the **absolute scale**.

From EDC Book I (chapter_4_leptons.tex, line 582):
```
"The electron is the reference particle—a pure electromagnetic surface defect.
 Its mass defines the unit: m_e c² = α · σ_eff · r_e²."
```

This is an **identification**, not a derivation. The electron mass m_e enters as the calibration point.

### Why No Absolute Scale Derivation Exists

The Steiner minimum mechanism provides:
- **Geometry:** 120° Y-junction (from Steiner theorem)
- **Ratio:** m_p/m_e = 6π⁵ (from S³/B³ volumes)
- **NOT:** The absolute energy scale

To get absolute masses, you need one of:
- m_e (electron mass) — observed
- ℏ (Planck constant) — observed
- σ (brane tension) — calibrated from m_e
- τ (string tension) — calibrated from σ

All are equivalent (fixing one fixes all), but **none are derived**.

---

## Final Assessment

```
                    ┌────────────────────────────────────────┐
                    │     WHAT EDC DERIVES (Pure Geometry)   │
                    ├────────────────────────────────────────┤
                    │  α = (4π + 5/6)/(6π⁵)  →  1/137.027    │
                    │  m_p/m_e = 6π⁵         →  1836.118     │
                    │  Steiner 120° geometry →  Y-junction   │
                    │  Koide formula Q       →  2/3          │
                    └────────────────────────────────────────┘
                                     │
                                     │ All dimensionless
                                     ▼
                    ┌────────────────────────────────────────┐
                    │     CALIBRATION POINT (1 required)     │
                    ├────────────────────────────────────────┤
                    │  Choose ONE of:                        │
                    │   • m_e = 0.511 MeV (electron mass)    │
                    │   • ℏ = 1.055×10⁻³⁴ J·s               │
                    │   • σ = 1.41×10¹⁸ J/m² (brane tension)│
                    │   • r_e = 2.82×10⁻¹⁵ m                │
                    └────────────────────────────────────────┘
                                     │
                                     │ Fixes absolute scale
                                     ▼
                    ┌────────────────────────────────────────┐
                    │     ALL DERIVED (From calibration)     │
                    ├────────────────────────────────────────┤
                    │  σ, ℏ, m_e, m_p, G_N, Λ, ...          │
                    └────────────────────────────────────────┘
```

### v11 NO-GO Confirmed

The Steiner minimum hypothesis provides the **proton geometry and mass ratio**, but NOT the absolute mass scale. Therefore:

- σ remains calibrated from observed m_e (or equivalent)
- G_N derivation requires σ
- BLOCK-003 remains OPEN

**This is the expected structure of a predictive theory:**
- QCD predicts hadron mass ratios, but Λ_QCD is measured
- String theory predicts dimensionless couplings, but M_s is free
- EDC predicts α and m_p/m_e, but m_e is measured

---

## Test E: Optimal Calibration Point (Metrological Analysis)

**Question:** Which measured constant minimizes error propagation into EDC?

### Finding: **ℏ is optimal** (exact since SI 2019)

### Measurement Precision of Candidate Constants

| Constant | Relative Uncertainty | Notes |
|----------|---------------------|-------|
| **ℏ** | **0 (EXACT)** | SI 2019 redefinition |
| **c** | 0 (exact) | Definition of metre |
| **e** | 0 (exact) | SI 2019 redefinition |
| **α** | ~8 × 10⁻¹¹ | Most precisely measured |
| **m_e** | ~3 × 10⁻¹⁰ | Very precise |
| **m_p** | ~3 × 10⁻¹⁰ | Similar to m_e |
| **G_N** | ~2 × 10⁻⁵ | **Worst measured!** |

### SI 2019 Redefinition Impact

Since 2019, the Planck constant is defined exactly:
```
ℏ ≡ 1.054571817... × 10⁻³⁴ J·s  (exact, by definition)
```

In EDC:
```
ℏ = σ R_ξ³ / c
```

Therefore:
```
σ R_ξ³ = ℏc = EXACT (zero measurement error)
```

### Candidate Analysis

**Option 1: ℏ (Planck constant)**
- Measurement error: 0 (exact since 2019)
- EDC relation: σ R_ξ³ = ℏc
- Advantage: Zero error propagation
- Limitation: Does not separate σ from R_ξ

**Option 2: m_e (electron mass)**
- Physical motivation: Fundamental particle, lowest energy state, stable
- Measurement error: ~3 × 10⁻¹⁰
- EDC relation: m_e c² = α · σ · r_e²
- Limitation: α enters (though EDC derives α)

**Option 3: ℏ + geometry (EDC optimum)**
- ℏ = exact → σ R_ξ³ = ℏc (exact)
- R_ξ/r_e = f(α) from EDC geometry
- r_e = α² · a₀ (Bohr radius, very precise)
- Result: σ and R_ξ separated with minimal error

### Metrological Recommendation

```
┌─────────────────────────────────────────────────────────────┐
│              OPTIMAL CALIBRATION STRATEGY                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PRIMARY: ℏ (Planck constant)                              │
│  ─────────────────────────────                              │
│  • Error contribution: ZERO (exact by SI definition)       │
│  • Fixes: σ R_ξ³ = ℏc                                      │
│                                                             │
│  SECONDARY: EDC geometric relations                         │
│  ──────────────────────────────────                         │
│  • R_ξ/r_e from α derivation                               │
│  • r_e from atomic physics (very precise)                  │
│  • Separates σ and R_ξ                                     │
│                                                             │
│  RESULT: All EDC predictions have error only from          │
│          theory itself (e.g., 19 ppm for m_p/m_e),         │
│          NOT from input calibration.                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Physical vs Metrological Choice

| Criterion | Best Choice | Reason |
|-----------|-------------|--------|
| **Metrological** | ℏ | Zero measurement error |
| **Physical intuition** | m_e | Fundamental particle, stable |
| **Practical** | ℏ + α | Separates all scales |

### Conclusion

**ℏ is the metrologically optimal calibration point** because it introduces zero measurement uncertainty into EDC predictions.

The electron mass m_e is a natural "physical" choice (fundamental, stable, lowest energy), but **metrologically ℏ is superior** since the 2019 SI redefinition made it exact by definition.

Using ℏ as input:
- σ R_ξ³ = ℏc is fixed exactly
- All derived quantities inherit zero calibration error
- Remaining discrepancies (e.g., 19 ppm in m_p/m_e) reflect theory accuracy, not input precision

---

## Complete Derivation Chain Status

### Summary Table (Updated)

| Quantity | Status | Evidence |
|----------|--------|----------|
| **α** | [Dc] | Derived with postulates |
| **m_p/m_e** | [M] | Pure geometry (6π⁵) |
| **σ** | [Dc] | σ = 2π R_ξ² ρ_P, but R_ξ, ρ_P are [P] |
| **R_ξ** | [P/Dc] | NOT derived from pure geometry |
| **ρ_P** | [P] | POSTULATE — never derived |
| **m_e** | [BL] | Calibration from observation |
| **ℏ** | [BL] | Calibration (exact since SI 2019) |
| **G_N** | — | Depends on σ → depends on ρ_P, R_ξ |

### Epistemic Classification Legend

- **[M]** — Mathematical (pure geometry, no physics input)
- **[D]** — Derived (follows from axioms)
- **[Dc]** — Derived conditional (requires postulates)
- **[P]** — Postulate (assumed, not derived)
- **[I]** — Identified (definition/correspondence)
- **[BL]** — Baseline (calibration from measurement)

### Final Statement

> **EDC has no independent normalization principle for the absolute energy scale.**
> This is structural, not a failure — analogous to QCD needing Λ_QCD.
> The metrologically optimal calibration point is ℏ (exact since SI 2019).

---

*Updated: 2026-02-02*
*Analysis: Claude Code*
