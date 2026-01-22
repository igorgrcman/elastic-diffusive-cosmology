# Chapter 7: CKM Matrix and CP Violation — Companion Notes

**Date:** 2026-01-22
**Status:** FALSIFIED BASELINE — Z₃ DFT computed, strongly falsified by CKM hierarchy
**Goal:** Apply Z₃ symmetry analysis to quark mixing; identify breaking requirements

---

## Executive Summary

Chapter 7 applies the PMNS baseline analysis to CKM:

| Mechanism | Verdict | Status |
|-----------|---------|--------|
| Z₃ DFT baseline computed | GREEN | [Dc] — All |V_ij|² = 1/3 |
| DFT vs PDG comparison | FALSIFIED | Corner elements off by ×60–140 |
| Breaking requirement | COMPUTED | ~99% breaking needed (vs ~25% for PMNS) |
| Breaking mechanism | RED | [P] — Three candidates postulated |
| CP violation | RED | (open) — Not addressed |

**Bottom line:** The Z₃ symmetric baseline fails dramatically for CKM. The observed hierarchy requires near-complete breaking of Z₃ in the quark sector—a much stronger effect than for leptons. This asymmetry is itself a puzzle that EDC must explain.

---

## Audit Table: Claims → Tags → Evidence → Failure Mode

| Claim | Tag | Evidence | Failure Mode | Next Calc |
|-------|-----|----------|--------------|-----------|
| CKM observed values | [BL] | PDG 2024 | None | — |
| Z₃ DFT = democratic mixing | [Dc] | Fourier transform on Z₃ | None | — |
| |V_ij|²_DFT = 1/3 for all | [Dc] | Direct calculation | None | — |
| |V_ub|_DFT = 0.577 | [Dc] | Eq. ch7_dft_numeric | vs PDG 0.004 (×144) | — |
| |V_cb|_DFT = 0.577 | [Dc] | Eq. ch7_dft_numeric | vs PDG 0.041 (×14) | — |
| CKM requires ~99% breaking | [Dc] | From falsification ratio | None | — |
| Z₂ selection mechanism | [P] | Postulated | Uncomputed | Derive from Z₆ |
| Localization asymmetry | [P] | Postulated | Uncomputed | Compute κ ratios |
| Potential anisotropy | [P] | Postulated | Uncomputed | Derive from EDC action |
| CP phase origin | (open) | Not addressed | — | Future work |

---

## Stoplight Analysis

### Mechanism A: Z₃ DFT Baseline

```
Z₃ symmetric quarks → DFT matrix → All |V_ij|² = 1/3 → Compare with PDG
```

| Step | Status | Issue |
|------|--------|-------|
| Z₃ generation structure | [I] GREEN | Same as leptons |
| DFT calculation | [Dc] GREEN | Standard Fourier transform |
| |V_ij|² = 1/3 prediction | [Dc] GREEN | Follows from symmetry |
| Compare |V_ub|: 0.577 vs 0.004 | FALSIFIED | ×144 off |
| Compare |V_cb|: 0.577 vs 0.041 | FALSIFIED | ×14 off |
| Compare |V_us|: 0.577 vs 0.225 | OFF | ×2.6 off |

**Verdict: STRONGLY FALSIFIED** — Much worse than PMNS (factor 15 → factor 144).

### Comparison: PMNS vs CKM Falsification

| Matrix | Worst element | DFT | PDG | Ratio | Breaking needed |
|--------|---------------|-----|-----|-------|-----------------|
| PMNS | sin²θ₁₃ | 0.333 | 0.022 | ×15 | ~25% |
| CKM | |V_ub| | 0.577 | 0.004 | ×144 | ~99% |

**Key insight:** Quark mixing requires much stronger Z₃ breaking than lepton mixing. This asymmetry is itself a prediction/constraint for any breaking mechanism.

---

## Breaking Mechanism Candidates [P]

### Candidate 1: Z₂ ⊂ Z₆ Generation Selection

The full hexagonal symmetry is Z₆ = Z₂ × Z₃. The Z₂ factor distinguishes:
- Even generations (1, 3) vs odd generation (2)
- Or: up-type vs down-type coupling patterns

**How it could work:**
- If d-quarks couple to Z₂ differently than u-quarks
- Inter-generational mixing suppressed by Z₂ selection rule
- Diagonal elements enhanced, off-diagonal suppressed

**Status:** Mechanism postulated, not computed.

### Candidate 2: Different Localization Depths

Quarks may have different penetration depths κ⁻¹ for up-type vs down-type:

```
κ_u ≠ κ_d → Overlap integrals non-democratic → CKM hierarchy
```

**Required asymmetry:**
- To get |V_ub| ~ 0.004 vs |V_ud| ~ 0.974
- Need exponential suppression: e^{-Δz · κ} ~ 0.004
- Requires significant localization difference between generations

**Status:** Mechanism postulated, not computed.

### Candidate 3: Quark-Sector Potential Anisotropy

The confining potential for quarks (from QCD + EDC) may have stronger angular dependence than for leptons:

```
V_quark(φ) has larger Z₃-breaking terms than V_lepton(φ)
```

**Physical motivation:**
- Quarks feel strong force (gluon exchange)
- Leptons only feel electroweak
- Extra interactions could induce anisotropy

**Status:** Mechanism postulated, not computed.

---

## Why Quarks ≠ Leptons? (Open Problem)

The central puzzle identified by this chapter:

| Sector | Z₃ breaking | Mixing pattern |
|--------|-------------|----------------|
| Leptons (PMNS) | ~25% | Large angles, θ₂₃ ≈ 45° |
| Quarks (CKM) | ~99% | Nearly diagonal, |V_us| ≈ 0.22 |

**Possible explanations (all [P]):**
1. Quarks confined by QCD → different effective potential
2. Up/down mass splitting larger than charged/neutral lepton
3. Color charge introduces additional localization mechanism
4. Historical: quarks formed first, leptons "inherited" cleaner Z₃

**Status:** All speculative. This asymmetry is a key target for future EDC development.

---

## CP Violation (Not Addressed)

### What we know [BL]
- Jarlskog invariant: J ≈ 3.0 × 10⁻⁵
- CP violation required for matter-antimatter asymmetry
- SM: complex phase in CKM unitarity triangle

### EDC candidates (all speculative)
1. Complex phases in Z₆ lattice structure
2. Asymmetric boundary conditions (bulk → brane vs brane → bulk)
3. CP-violating terms in Plenum stress tensor

**Status:** Not addressed in current chapter. Major open problem.

---

## Connection to Other Chapters

| Chapter | Connection to Ch7 |
|---------|------------------|
| Ch5 (Generations) | Z₃ structure applies to quarks too |
| Ch6 (Neutrinos) | PMNS baseline: same method, different result |
| Ch9 (V–A) | Chirality selection for quarks |
| Ch11 (G_F) | Quark weak vertices involve CKM |

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
| **Is baseline computed?** | Yes — DFT matrix [Dc] |
| **Is falsification rigorous?** | Yes — direct comparison with PDG [BL] |
| **Is breaking mechanism derived?** | No — three candidates [P] |
| **CP violation addressed?** | No — (open) |
| **Risk level** | MEDIUM — tight negative result closes loop |
| **Falsifiable?** | Yes — if Z₃ breaking mechanism derived, predicts specific ratios |

**Honest conclusion:** This chapter demonstrates that the Z₃ symmetric baseline fails dramatically for quark mixing—even more so than for lepton mixing. The ~99% breaking requirement is a concrete constraint that any successful EDC extension must satisfy. The asymmetry between quark and lepton sectors is itself a puzzle that points toward differences in the underlying physics (QCD effects, localization patterns, etc.).

---

*Chapter 7 notes complete. The chapter establishes a tight negative result for Z₃ baseline CKM and identifies the breaking asymmetry as a key open problem.*
