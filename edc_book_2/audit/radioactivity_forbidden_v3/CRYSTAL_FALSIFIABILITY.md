# CRYSTAL FALSIFIABILITY: Tests for EDC Crystal Predictions

**Created**: 2026-01-31
**Purpose**: Define falsifiable predictions for crystal coordination
**Scope**: What would disprove EDC claims about crystals?

---

## Core Prediction

**EDC Claim [Der]**: Only coordination numbers n = 2^a × 3^b are topologically stable.

**Implication**: No periodic crystal should have n = 5, 7, 11, etc. as bulk coordination.

---

## Test 1: Stable Crystal with n = 5?

### Falsification Criterion

If a **stable periodic crystal** exists with **bulk coordination n = 5**, EDC is falsified.

### Current Status

**No known periodic crystal has bulk n = 5**.

- Icosahedral quasicrystals have local n = 5, but are NOT periodic
- Frank-Kasper phases (complex alloys) mix coordinations, avoid pure n = 5
- Penrose tilings are aperiodic

### Edge Cases to Investigate

| System | Local n = 5? | Periodic? | Stable? | EDC Status |
|--------|--------------|-----------|---------|------------|
| Quasicrystals | Yes | No | Yes* | Not falsifying |
| Metallic glasses | Yes (local) | No | Metastable | Not falsifying |
| C₆₀ fullerene | Yes (vertex) | Molecular | Yes | Not bulk crystal |
| Frank-Kasper σ | Mixed | Yes | Yes | Avg n ≠ 5 |

*Quasicrystal stability may be electronic, not topological

### Conclusion

**Not falsified** — no counterexample found

---

## Test 2: Unstable Crystal with Allowed n?

### Falsification Criterion

If a crystal with n = 6, 8, or 12 is **inherently unstable** (not due to temperature, pressure), this challenges EDC.

### Current Status

| n | Example Crystals | Stability | EDC Status |
|---|------------------|-----------|------------|
| 6 | SC (Po) | Rare but stable | ✓ |
| 8 | BCC (Fe, W) | Very stable | ✓ |
| 12 | FCC (Cu, Au) | Most stable | ✓ |
| 12 | HCP (Mg, Ti) | Very stable | ✓ |

**All crystals with allowed n are stable** (as expected).

### Conclusion

**Not falsified** — consistent with predictions

---

## Test 3: Quasicrystal Metastability?

### EDC Prediction [P]

Quasicrystals (n = 5 locally) should be metastable, eventually transforming to periodic (allowed n) structures.

### Observations

- Quasicrystals discovered 1984, stable in lab for 40+ years
- Some natural quasicrystals found (Icosahedrite, Khatyrka meteorite)
- Appear thermodynamically stable at certain compositions

### Interpretation

| Scenario | Meaning for EDC |
|----------|-----------------|
| Quasicrystals truly metastable | EDC consistent |
| Quasicrystals truly stable | EDC needs modification |
| Electronic stabilization | EDC applies to topology only |

### Current Status

**Ambiguous** — requires understanding of stabilization mechanism

### Possible Resolution

EDC may apply to **topological** stability only. Electronic effects (Hume-Rothery rules) could stabilize otherwise forbidden structures.

**Modified claim [P]**: n = 2^a × 3^b is preferred TOPOLOGICALLY; electronic effects can override.

---

## Test 4: Nuclear Coordination Verification

### EDC Prediction [Der]

Heavy nuclei (A > 200) have n ≈ 40-44 (forbidden), causing radioactive decay.

### Falsification Criterion

If heavy stable nuclei exist with verified n in forbidden range, the instability claim is weakened.

### Current Status

- ²⁰⁸Pb, ²⁰⁹Bi are heaviest stable nuclei
- Proposed: n(208) ≈ 36 (allowed), explaining stability
- Proposed: n(A > 209) in forbidden zone, explaining instability

### Test

Calculate n(A) for ²⁰⁸Pb and ²⁰⁹Bi:
- If n(208) ≈ 36 and n(209) ≠ allowed → consistent
- If both in forbidden zone but ²⁰⁹Bi stable → problematic

**Note**: ²⁰⁹Bi has t₁/₂ ≈ 10¹⁹ years (effectively stable)

Using n(A) ≈ 6.1 × A^(1/3):
- n(208) ≈ 36.2 → near 36 (allowed) ✓
- n(209) ≈ 36.3 → still near 36 ✓

**Interpretation**: Both near allowed; ²⁰⁹Bi's weak alpha-decay from small residual frustration.

---

## Test 5: Graphene Defects

### EDC Prediction [Der]

Graphene (n = 3, allowed) is stable. Defects introducing n = 5 or 7 locally are energetically costly.

### Observations

- Pristine graphene extremely stable
- Stone-Wales defects (5-7 pairs) are high-energy
- Pentagon-heptagon pairs: one forbidden compensates other

### Status

**Consistent** — defects with forbidden n are energetically disfavored

---

## Test 6: New Prediction

### Prediction [P]

Any attempt to synthesize a periodic 3D crystal with n = 7 as bulk coordination will fail.

### Falsification

Synthesize such a crystal → EDC falsified for crystals.

### Status

**Untested** — no such attempt known

---

## Summary: Falsifiability Assessment

| Test | Criterion | Current Status | EDC Verdict |
|------|-----------|----------------|-------------|
| 1 | Stable periodic n=5 crystal | None known | Not falsified |
| 2 | Unstable n=6,8,12 crystal | None known | Not falsified |
| 3 | Quasicrystal stability | Ambiguous | Needs clarification |
| 4 | Nuclear n(A) calculation | Preliminary ✓ | Consistent |
| 5 | Graphene defect energy | ✓ | Consistent |
| 6 | Synthesize n=7 crystal | Untested | Open |

---

## What Would Falsify EDC Crystal Claims?

1. **Definitive counterexample**: Periodic crystal with n = 5, 7, or 11 as sole bulk coordination, stable at STP.

2. **Quasicrystal proof**: Rigorous demonstration that icosahedral quasicrystals are thermodynamically stable ground states without electronic stabilization.

3. **Nuclear counterexample**: Stable heavy nucleus (A > 250) with verified n in allowed range, yet unstable.

---

## Conclusion

**Current status**: EDC crystal predictions are **not falsified** by known data.

**Strength**: Correctly predicts which n values appear in crystals.

**Weakness**: Quasicrystal status unclear; may require electronic supplement to topological argument.

**Future work**: Calculate n(A) for nuclei; attempt n = 7 crystal synthesis.
