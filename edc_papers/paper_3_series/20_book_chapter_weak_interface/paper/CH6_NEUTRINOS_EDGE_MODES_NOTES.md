# Chapter 6: Neutrinos as Edge Modes — Companion Notes

**Date:** 2026-01-22
**Status:** YELLOW — Mass suppression derived conditionally, mixing postulated
**Goal:** Explain neutrino smallness and flavor structure from edge-mode geometry

---

## Executive Summary

Chapter 6 explains neutrino properties within EDC's 5D framework:

| Mechanism | Verdict | Status |
|-----------|---------|--------|
| Mass suppression (overlap) | YELLOW | [Dc] — Geometrically sound, profiles postulated |
| Three flavors from Z₃ | YELLOW | [I] — Cardinality matches, dynamics not derived |
| Left-handed selection | GREEN | [Dc] — Follows from Ch9 V–A derivation |
| PMNS mixing angles | RED | [P] — Postulated mechanism, no calculation |
| Dirac vs. Majorana | RED | (open) — No prediction |

**Bottom line:** EDC provides structural explanations for neutrino smallness and chirality, identifies flavor count with Z₃, but leaves quantitative mixing predictions open.

---

## Audit Table: Claims → Tags → Dependencies

| Claim | Tag | Dependencies | Gap |
|-------|-----|--------------|-----|
| $m_\nu \lesssim 0.8$ eV | [BL] | PDG 2024 | None (empirical) |
| $N_\nu = 2.984 \pm 0.008$ | [BL] | LEP Z-width | None (empirical) |
| Neutrino is edge mode | [P] | Framework v2.0 | Ontology postulated |
| Overlap integral formalism | [BL] | Standard KK theory | None |
| $m_\nu/m_e \sim e^{-\Delta z/\kappa^{-1}}$ | [Dc] | Edge profile [P], Higgs profile [P] | Profiles not derived |
| Three flavors ↔ Z₃ | [I] | Ch5 Z₆ factorization [Dc] | Why neutrinos couple to Z₃? |
| Left-handed selection | [Dc] | Ch9 V–A derivation [Dc] | None (follows from Ch9) |
| PMNS from overlaps | [P] | Edge ontology [P] | Angles not computed |

---

## Stoplight Summary

### Mechanism A: Mass Suppression via Overlap

```
Edge mode at interface → Suppressed overlap with Higgs → m_ν ≪ m_e
```

| Step | Status | Issue |
|------|--------|-------|
| Overlap integral formula | [BL] GREEN | Standard result |
| Neutrino at interface | [P] YELLOW | Ontology postulated |
| Higgs in brane interior | [P] YELLOW | Profile not derived |
| Exponential suppression | [Dc] GREEN | Follows from spatial separation |
| Ratio m_ν/m_e ~ 10⁻⁶ | [I] YELLOW | Requires Δz/κ⁻¹ ≈ 14 |

**Verdict: YELLOW** — Mechanism geometrically sound but profiles postulated.

### Mechanism B: Three Flavors from Z₃

```
Z₆ = Z₂ × Z₃  [M]  →  |Z₃| = 3  →  N_ν = 3?
```

| Step | Status | Issue |
|------|--------|-------|
| Z₆ hexagonal symmetry | [Dc] GREEN | From Ch2 |
| Z₆ = Z₂ × Z₃ | [M] GREEN | Pure math |
| |Z₃| = 3 matches N_ν | [I] YELLOW | Numerology, not dynamics |
| Why neutrinos couple to Z₃ | [OPEN] RED | No mechanism |

**Verdict: YELLOW** — Structural identification, not derivation.

### Mechanism C: Chirality Selection

```
Ch9 V–A boundary conditions → Left-handed neutrinos localized
```

| Step | Status | Issue |
|------|--------|-------|
| Domain-wall localization | [BL] GREEN | Jackiw-Rebbi/Kaplan |
| Plenum inflow direction | [P] YELLOW | EDC postulate |
| Left-handed survival | [Dc] GREEN | Follows from m(z) sign |
| Applies to neutrinos | [Dc] GREEN | Edge modes also filtered |

**Verdict: GREEN** — Follows directly from Ch9 derivation.

### Mechanism D: PMNS Mixing

```
Flavor wavefunctions × Mass wavefunctions → Overlap matrix → PMNS?
```

| Step | Status | Issue |
|------|--------|-------|
| PMNS observed | [BL] GREEN | Oscillation data |
| Mixing from overlaps | [P] RED | Mechanism not computed |
| θ₁₂ ≈ 33° | [OPEN] RED | Not derived |
| θ₂₃ ≈ 45° | [OPEN] RED | Not derived |
| θ₁₃ ≈ 8.5° | [OPEN] RED | Not derived |

**Verdict: RED** — Pure postulate, no progress.

---

## Falsifiability Analysis

### The Predictions

If edge-mode ontology is correct:
```
1. m_ν ≪ m_e  (from overlap suppression)
2. Only left-handed νL couple  (from boundary conditions)
3. N_ν = 3  (from Z₃ identification)
```

### Falsification Criteria

| Observable | If Found | EDC Status |
|------------|----------|------------|
| Right-handed W coupling | At SM strength | FALSIFIED |
| m_ν > 1 eV | Direct measurement | CHALLENGED (geometry inconsistent) |
| 4th sequential neutrino | Couples to Z | FALSIFIED |
| Bulk-like propagation | Modified dispersion | CHALLENGED |
| Strong neutrino interactions | Cross-section anomaly | FALSIFIED |

### Current Experimental Status [BL]

- **Direct mass:** m_νe < 0.8 eV (KATRIN)
- **Oscillations:** Δm²₂₁ = 7.53 × 10⁻⁵ eV², |Δm²₃₁| = 2.453 × 10⁻³ eV²
- **N_ν from LEP:** 2.984 ± 0.008 (light neutrinos)
- **0νββ:** Not observed (Majorana mass < 0.1–0.5 eV depending on experiment)

**Assessment:** Data consistent with EDC predictions, but SM also consistent. EDC gains predictive power only if quantitative derivations are completed.

---

## What's Missing (Critical Gaps)

### Gap 1: Penetration Depth κ⁻¹

**Need:** Derive κ⁻¹ from EDC thick-brane structure.

**Possible approaches:**
1. Solve mode equation at interface with boundary conditions
2. Extract from EDC action via variation
3. Relate to Plenum diffusion scale

**Status:** Not attempted.

### Gap 2: Higgs Profile h(z)

**Need:** Derive or constrain h(z) from EDC.

**Possible approaches:**
1. Assume scalar field localized at elastic minimum
2. Couple to stress-energy profile
3. Use Rξ variation to induce profile

**Status:** Not attempted.

### Gap 3: PMNS Angle Calculation

**Need:** Explicit computation of overlap integrals.

**Possible approaches:**
1. Assume Gaussian profiles for flavor modes
2. Compute overlaps with Higgs-coupled mass modes
3. Extract PMNS matrix from result

**Status:** Not attempted.

### Gap 4: Mass Hierarchy

**Need:** Explain normal vs. inverted ordering.

**Possible approaches:**
1. Mode number ordering in KK tower
2. Interference effects in Z₃ structure
3. Connection to charged lepton hierarchy

**Status:** Not attempted.

---

## Connection to Other Chapters

| Chapter | Connection to Ch6 |
|---------|------------------|
| Ch4 (Lepton Masses) | Electron interior vs. neutrino interface |
| Ch5 (Generations) | Z₃ structure → three neutrino flavors |
| Ch9 (V–A) | Chirality selection applies to neutrinos |
| Ch10 (Case Neutrino) | Detailed ledger role in decays |
| Ch11 (G_F) | Overlap suppression may contribute to G_F |

---

## Recommended Development Path

### Priority 1: Penetration Depth Derivation

1. Solve Schrödinger-type equation at bulk-brane interface
2. Extract κ from boundary conditions
3. Compute Δz required for m_ν/m_e ~ 10⁻⁶

If successful: Upgrades mass suppression to [Der].

### Priority 2: Consistency Check with m_e

1. Verify that electron overlap with Higgs is O(1)
2. Confirm neutrino overlap is exponentially smaller
3. Check that same Higgs profile works for both

If successful: Strengthens [Dc] → potential [Der].

### Priority 3: One PMNS Angle

1. Start with θ₂₃ (maximal mixing suggests symmetry)
2. Try Z₃ symmetric profiles
3. Check if θ₂₃ ≈ 45° emerges naturally

If successful: First quantitative PMNS prediction.

---

## Verification Commands

```bash
# Check for [OPEN] tags (should return nothing in final version)
grep -R "\[OPEN\]" sections/06_neutrinos_edge_modes.tex

# Check for undefined references
grep -i "undefined" EDC_Part_II_Weak_Sector.log

# Check for multiply-defined labels
grep -i "multiply" EDC_Part_II_Weak_Sector.log

# Build Part II
latexmk -xelatex -interaction=nonstopmode EDC_Part_II_Weak_Sector.tex
```

---

## Epistemic Summary

| Aspect | Status |
|--------|--------|
| **Is m_ν ≪ m_e explained?** | Partially — mechanism identified [Dc], profiles postulated [P] |
| **Is N_ν = 3 explained?** | Identified [I], not derived |
| **Is chirality explained?** | Yes — follows from Ch9 [Dc] |
| **Is PMNS derived?** | No — postulated [P] |
| **Risk level** | MEDIUM — core mechanism plausible but gaps remain |
| **Falsifiable?** | Yes — specific observables identified |
| **Reviewer-proof?** | Partially — honest about gaps, clear stoplight |

**Honest conclusion:** This chapter provides a coherent structural picture of why neutrinos are unusual (edge modes with suppressed overlap). The mass suppression mechanism is geometrically well-motivated [Dc]. However, the edge-mode ontology is postulated [P], and PMNS mixing remains at the "just a hypothesis" level [P]. The chapter is honest about these limitations.

---

*Chapter 6 notes complete. The chapter explains neutrino smallness and chirality but leaves quantitative predictions as future work.*
