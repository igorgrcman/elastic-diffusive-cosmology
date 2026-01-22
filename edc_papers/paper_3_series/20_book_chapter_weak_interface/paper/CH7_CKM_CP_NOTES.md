# Chapter 7: CKM Matrix and CP Violation — Companion Notes

**Date:** 2026-01-22 (v2 — Attempt 1 complete with Option A/B and ε quantification)
**Status:** YELLOW (computed baseline, falsified, breaking quantified)
**Goal:** Compute Z₃ baseline for CKM, compare to PDG, quantify required breaking

---

## Executive Summary

Chapter 7 applies the same Z₃ DFT analysis used for PMNS (Ch6) to the quark sector:

| Aspect | Result |
|--------|--------|
| Z₃ DFT baseline computed | Yes — all \|V_ij\|² = 1/3 |
| Option A (aligned sectors) | V = 𝟙 — zero mixing (falsified by Cabibbo) |
| Option B (misaligned sectors) | V = U^DFT — democratic mixing (baseline) |
| Comparison to PDG | **STRONGLY FALSIFIED** |
| Worst discrepancy | \|V_ub\|: ×144 off |
| Breaking amplitude ε_ub | ~0.007 (near-complete) |
| CP phase | Not addressed (open) |

**Key finding:** CKM requires ~99% breaking of Z₃ symmetry, compared to ~25% for PMNS. This lepton-quark asymmetry is itself a puzzle.

---

## Chain Box Summary (What Is Independent vs. What Fails)

| Step | Tag | Result |
|------|-----|--------|
| 3 generations ↔ \|Z₃\| = 3 | [I] | Same identification as Ch6 |
| Z₃ DFT baseline computed | [Dc] | V_ij = ω^(-ij)/√3, all \|V_ij\|² = 1/3 |
| Option A: aligned → V = 𝟙 | [Dc] | Zero mixing — falsified |
| Option B: misaligned → V = DFT | [Dc] | Democratic — baseline for comparison |
| Falsification vs PDG | [Dc] | Corner elements off by ×144 |
| Breaking ε quantified | [Dc] | ε_us ~ 0.39, ε_cb ~ 0.07, ε_ub ~ 0.007 |
| Breaking mechanism | [P] | 3 candidates listed, none computed |
| CP phase δ, Jarlskog J | (open) | Not addressed |

---

## Audit Table: Claims → Tags → Evidence → Status

| Claim | Tag | Evidence | Status |
|-------|-----|----------|--------|
| CKM PDG values | [BL] | PDG 2024 | GREEN |
| 3 generations ↔ \|Z₃\| = 3 | [I] | Same as Ch6 | GREEN |
| Z₃ DFT baseline computed | [Dc] | Eq. ch7_dft_ckm | GREEN |
| Option A: V = 𝟙 if aligned | [Dc] | U_u = U_d → V = 𝟙 | GREEN (falsified) |
| Option B: V = U^DFT if misaligned | [Dc] | U_u = 𝟙, U_d = DFT | GREEN (baseline) |
| DFT vs PDG comparison | [Dc] | Table ch7_ckm_comparison | **FALSIFIED** |
| ε_us ~ 0.39 (Cabibbo) | [Dc] | 0.225 / 0.577 | GREEN |
| ε_cb ~ 0.071 | [Dc] | 0.041 / 0.577 | GREEN |
| ε_ub ~ 0.007 | [Dc] | 0.004 / 0.577 | GREEN |
| Wolfenstein λ, λ², λ³ hierarchy | [BL] | Standard parametrization | GREEN |
| Breaking mechanism | [P] | 3 candidates listed | YELLOW |
| CP phase δ | (open) | Not addressed | RED |
| Jarlskog J | [BL] | 3.0×10⁻⁵ stated | RED (not derived) |

---

## Option A vs Option B: Technical Details

### Option A: Both sectors in same Z₃ basis

If U_u = U_d = U^DFT, then:
```
V = (U^DFT)† U^DFT = 𝟙
```
This predicts **zero mixing** — falsified by Cabibbo angle θ_C ≈ 13°.

### Option B: Sectors in different bases

If U_u = 𝟙 (site basis) and U_d = U^DFT, then:
```
V = 𝟙† · U^DFT = U^DFT
```
This predicts **democratic mixing** — all |V_ij|² = 1/3.

**Assessment:** Option B is "less wrong" (closer to data) and serves as the baseline for breaking analysis.

**Variant (not computed):** If sectors are misaligned by a Z₃ element (U_d = ω^k U_u), V becomes a permutation matrix — also falsified.

---

## Breaking Amplitude ε: Quantitative Analysis

Define breaking amplitude ε such that off-diagonal elements scale as:
```
|V_ij|_obs ~ ε · |V_ij|_DFT    for i ≠ j
```

### Complete table from PDG

| Element | PDG value | DFT value | ε = PDG/DFT | Wolfenstein |
|---------|-----------|-----------|-------------|-------------|
| \|V_ud\| | 0.974 | 0.577 | 1.69 | ~1 |
| \|V_us\| | 0.225 | 0.577 | 0.39 | λ |
| \|V_ub\| | 0.004 | 0.577 | 0.007 | λ³ |
| \|V_cd\| | 0.225 | 0.577 | 0.39 | λ |
| \|V_cs\| | 0.973 | 0.577 | 1.69 | ~1 |
| \|V_cb\| | 0.041 | 0.577 | 0.071 | λ² |
| \|V_td\| | 0.009 | 0.577 | 0.016 | λ³ |
| \|V_ts\| | 0.040 | 0.577 | 0.069 | λ² |
| \|V_tb\| | 0.999 | 0.577 | 1.73 | ~1 |

### Key observations

1. **Diagonal elements:** ε > 1 means DFT underpredicts (should be ~1, not 0.577)
2. **First off-diagonal:** ε ~ 0.39 corresponds to λ ~ 0.225 (Cabibbo)
3. **Second off-diagonal:** ε ~ 0.07 corresponds to λ² ~ 0.05
4. **Corners:** ε ~ 0.007-0.016 corresponds to λ³ ~ 0.01

The Wolfenstein hierarchy (λ, λ², λ³) is an empirical pattern [BL], not derived from EDC.

---

## Comparison: PMNS vs CKM Breaking

| Aspect | PMNS (Ch6) | CKM (Ch7) |
|--------|------------|-----------|
| Baseline prediction | \|U_αi\|² = 1/3 | \|V_ij\|² = 1/3 |
| Worst DFT error | θ₁₃: ×15 off | \|V_ub\|: ×144 off |
| ε needed | ~0.26 (for θ₁₃) | ~0.007 (for \|V_ub\|) |
| Breaking scale | ~25% | ~99% |
| Pattern | Large angles (45°, 33°, 8.5°) | Near-diagonal |
| Status | Moderate breaking | Near-complete breaking |

**The puzzle:** Why is Z₃ nearly preserved for leptons but almost completely broken for quarks?

---

## Stoplight Analysis

### GREEN: What is established

1. **Z₃ DFT baseline computed** [Dc]
   - Both Option A (identity) and Option B (democratic) derived
   - Option B serves as reference baseline

2. **Quantitative falsification** [Dc]
   - Table with all 9 elements: baseline vs PDG
   - Worst case: |V_ub| off by factor 144

3. **Breaking amplitude ε quantified** [Dc]
   - ε_us ~ 0.39 (Cabibbo scale)
   - ε_cb ~ 0.071 (λ² scale)
   - ε_ub ~ 0.007 (λ³ scale)

### YELLOW: Mechanism identified but not computed

1. **Z₂×Z₃ structure** [P]
   - Z₂ ⊂ Z₆ could distinguish generations
   - Not computed: which eigenmode gets suppressed

2. **Localization asymmetry** [P]
   - Up vs down sectors could have different κ⁻¹
   - Not computed: what ratio is needed

3. **Potential anisotropy** [P]
   - Quarks may see stronger angular breaking than leptons
   - Not computed: why quarks ≠ leptons

### RED: Open problems

1. **CP phase δ**
   - Not addressed in Attempt 1
   - Would require computing complex phase in breaking mechanism

2. **Jarlskog invariant J**
   - J = Im(V_us V_cb V*_ub V*_cs) ~ 3×10⁻⁵
   - Stated as [BL], not derived from geometry

3. **Why quarks ≠ leptons**
   - PMNS: ~25% breaking needed
   - CKM: ~99% breaking needed
   - No explanation provided

---

## Candidate Breaking Mechanisms [P] — Menu

### A) Z₂×Z₃ structure from Z₆

- **Idea:** Z₂ ⊂ Z₆ distinguishes even/odd modes
- **Effect:** Could suppress inter-generational mixing hierarchically
- **What would change:** Hierarchy between generations (1-2 vs 2-3 vs 1-3)
- **Needed calculation:** Which Z₂ eigenvalue for each generation? How does this produce λ, λ², λ³?

### B) Asymmetric localization (different κ⁻¹)

- **Idea:** Up-type quarks have different penetration depth than down-type
- **Effect:** Overlap integrals become asymmetric → CKM ≠ democratic
- **What would change:** Diagonal enhanced, off-diagonal suppressed
- **Needed calculation:** What ratio κ_u/κ_d gives Wolfenstein hierarchy?

### C) Anisotropic Yukawa/Higgs overlap

- **Idea:** Quark-sector profile has stronger angular anisotropy than leptons
- **Effect:** Enhances Z₃ breaking specifically for quarks
- **What would change:** Explains why quarks ≠ leptons
- **Needed calculation:** What anisotropy strength is needed?

---

## Falsifiability Conditions

| Condition | Would falsify... | Current status |
|-----------|------------------|----------------|
| 4th generation discovered | N_g = 3 from \|Z₃\| | Not triggered |
| No geometric ε mechanism exists | EDC flavor picture | Open (needs computation) |
| PMNS ≈ CKM hierarchy found | Lepton-quark asymmetry | Contradicted by data |

---

## Attempt 2 Roadmap (for future work)

If Attempt 2 is pursued, the recommended path:

1. **Start with Option B (localization asymmetry)**
   - Most testable: compute overlap integrals with different κ values
   - Compare to Wolfenstein parametrization
   - Target: derive λ ~ 0.22 from geometry

2. **Check Z₂ structure**
   - Does Z₂ ⊂ Z₆ naturally produce λ, λ², λ³ hierarchy?
   - If so, this is the minimal EDC explanation

3. **CP phase last**
   - Requires complex phases in the breaking mechanism
   - Higher risk, defer until hierarchy mechanism is established

---

## Verification Commands

```bash
# Check for forbidden bracket tags
grep -R "\[OPEN\]\|\[Def\]" sections/07_ckm_cp.tex

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
| **Is CKM explained?** | No — baseline falsified, breaking postulated |
| **Is baseline computed?** | Yes — Option A and B both [Dc] |
| **Is falsification rigorous?** | Yes — direct comparison with PDG [BL] |
| **Is ε quantified?** | Yes — ε_us, ε_cb, ε_ub all computed [Dc] |
| **Is breaking mechanism derived?** | No — three candidates [P] |
| **Is CP violation addressed?** | No — (open) |
| **Risk level** | MEDIUM — tight negative result closes loop |
| **Falsifiable?** | Yes — 4th gen, no geometric mechanism, etc. |

**Honest conclusion:** Attempt 1 establishes a rigorous negative baseline. The Z₃ DFT matrix fails by factors of 2.6–144 depending on the element. The required breaking amplitudes are computed: ε_us ~ 0.39, ε_cb ~ 0.07, ε_ub ~ 0.007. These correspond to the Wolfenstein λ, λ², λ³ hierarchy. The asymmetry between quark and lepton sectors (~99% vs ~25% breaking) is a concrete puzzle for future work.

---

*Chapter 7 notes v2 complete. Attempt 1 establishes the Z₃ baseline with Option A/B analysis, quantifies falsification, and computes breaking amplitudes ε.*
