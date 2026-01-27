# V_B Derivation Attempt: Z₃ Barrier Conjecture

**Date:** 2026-01-27 (updated)
**Status:** [Dc] — Derived conditional on Z₃ barrier ansatz
**Target:** Upgrade V_B from [Cal] to [Der]

---

## 1. Numerical Discovery

From WKB calibration: V_B ≈ 2.6 MeV reproduces τ_n ≈ 879 s.

**Observation:** V_B / Δm_np = 2.6 / 1.293 ≈ 2.01 (within 0.5%)

This suggests:
```
V_B = 2 × Δm_np
```

---

## 2. Δm_np Options

**IMPORTANT:** The neutron-proton mass difference can be treated two ways:

### Option B: PDG Baseline [BL]
```
Δm_np = 1.2933 MeV   [BL] (PDG)
```
This is the experimental value, taken as input.

### Option A: Book Formula [Dc]
```
Δm_np = (5/2 + 4α) m_e = 1.2924 MeV   [Dc]
```
Where:
- 5/2 = D_bulk / D_membrane (dimensional projection factor)
- 4α = electromagnetic correction from Dirac spinor structure
- Error vs PDG: 0.07%

**Note:** A previous version of this document incorrectly stated "Δm_np = 8 m_e / π [Der]".
This formula was not supported by the codebase and has been removed.

---

## 3. The Question

**Why factor of 2?**

The conjecture is:
```
V_B = 2 × Δm_np    [Dc] — needs geometric reason
```

---

## 4. Candidate Explanation: Z₃ Symmetric Barrier

### 4.1 Energy Structure

| Configuration | Energy above proton | Physical interpretation |
|---------------|---------------------|------------------------|
| Proton (q=0) | 0 | Steiner-balanced Y-junction (ground state) |
| Neutron (q=q_n) | Δm_np | One collective mode excited |
| **Barrier (q=q_B)** | **3 × Δm_np** | **Z₃-symmetric excited state** |

Therefore:
```
V_B = E_barrier - E_neutron = 3×Δm_np - Δm_np = 2×Δm_np
```

### 4.2 Physical Picture

The Y-junction has **Z₃ symmetry** (3 flux tubes at 120°).

**Proton:** All 3 legs equivalent, at equilibrium (Steiner point).
- Energy cost: 0 (reference)
- Symmetry: Full Z₃

**Neutron:** The junction is displaced by q_n into the bulk. This breaks Z₃ partially — effectively, one "direction" is excited while the other two remain balanced.
- Energy cost: Δm_np
- Symmetry: Z₃ → Z₁ (partial breaking)

**Barrier:** To transition from neutron back to proton, the system must pass through a configuration where the Z₃ symmetry is **restored but at higher energy**. This is the "activated" Z₃-symmetric state where all three legs are equally stressed.
- Energy cost: 3 × Δm_np (one unit per leg)
- Symmetry: Full Z₃ (but excited)

### 4.3 Why 3 × Δm_np for the barrier?

**Argument:** The deformation that produces Δm_np is associated with a specific topological/geometric displacement. In the neutron, this deformation affects the Y-junction asymmetrically (1 leg vs 2). At the barrier, the configuration is Z₃-symmetric, meaning all three legs must carry the deformation equally.

If the "cost per leg" is Δm_np, then the Z₃-symmetric barrier has cost 3 × Δm_np.

**OPEN:** "One unit per leg = Δm_np" requires 5D action verification.

---

## 5. Epistemic Status

| Claim | Status | Justification |
|-------|--------|---------------|
| Δm_np = 1.2933 MeV | [BL] | PDG value (Option B) |
| Δm_np = (5/2 + 4α) m_e | [Dc] | Book formula (Option A) |
| Z₃ invariance of junction sector | [Dc] | Identical BC on edges + Steiner ⇒ τ₁=τ₂=τ₃ |
| No low-lying doublet partners | [BL] | Observed: no near-degenerate neutron multiplet |
| Doublet mode constrained | [BL]+[M] | Absence of partners ⇒ a(q_n)>0 OR splitting suppressed |
| Neutron Z₃-symmetric (favored) | [Dc] | Natural interpretation within EDC |
| Barrier is Z₃-symmetric | [Dc] | Minimal transition path through symmetric saddle |
| Each leg costs Δm_np | [Dc] | Z₃ symmetry ⇒ equal partition; **OPEN: unit quantization** |
| V_B = 3Δm - Δm = 2Δm | [Dc] | Follows from above |

**Current overall status: [Dc]** — conditionally derived within Z₃ framework.

### 5.1 Observational Constraint on Doublet Mode [BL]+[M]

**[BL]:** No low-lying "neutron partners" are observed corresponding to a
Z₃-multiplet structure (singlet + doublet states with tunnel splitting).

**[M]:** In a Z₃-symmetric quantum system with three equivalent classical minima,
quantization typically yields 1 singlet + 2 doublet states with splitting ~ e^{-S/ℏ}.
If doublet instability (a(q_n) < 0) were present, we would expect visible multiplet
structure or transitions between Z₃ sectors.

**Conclusion [BL]+[M] (constraint, not strict proof):**
> Absence of observed doublet partners constrains doublet mode to be either
> stable (a(q_n) > 0) or with splitting pushed above observable range.
> Within EDC, a(q_n) > 0 is the natural interpretation.

**Caveat:** This is a constraint, not a mathematical proof. Rigorous closure
requires explicit Hessian calculation or convexity lemma.

---

## 6. V_B Numerical Results (Option A vs Option B)

### Option B: Using PDG Baseline
```
V_B^(B) = 2 × 1.2933 MeV = 2.5867 MeV
E_barrier^(B) = 3 × 1.2933 MeV = 3.8800 MeV
```
Error vs V_B_cal (2.6 MeV): **0.51%**

### Option A: Using Book Formula
```
V_B^(A) = 2 × (5/2 + 4α) m_e = 2.5848 MeV
E_barrier^(A) = 3 × (5/2 + 4α) m_e = 3.8772 MeV
```
Error vs V_B_cal (2.6 MeV): **0.58%**

### Cross-Check: Barrier Above Proton
```
E_barrier_cal = V_B_cal + Δm_np = 2.6 + 1.293 = 3.893 MeV
```

| Quantity | Option B | Option A | Calibrated |
|----------|----------|----------|------------|
| Δm_np | 1.2933 MeV [BL] | 1.2924 MeV [Dc] | — |
| V_B | 2.5867 MeV | 2.5848 MeV | 2.6 MeV [Cal] |
| E_barrier | 3.8800 MeV | 3.8772 MeV | 3.893 MeV |
| Error vs cal | 0.51% | 0.58% | — |

Both options give V_B within 0.6% of the calibrated value.

---

## 7. What's Needed to Upgrade to [Der]

To make V_B = 2 × Δm_np fully derived [Der], need to show from 5D action:

1. **Existence:** V(q) has a local maximum at some q_B ∈ (0, q_n)

2. **Z₃ symmetry at barrier:** The configuration at q_B has full Z₃ symmetry (all 3 flux tube legs equivalent)

3. **Energy quantization:** The barrier energy is exactly 3× the unit of Z₆ breaking — this is the key OPEN step: "one unit per leg = Δm_np"

4. **Doublet stability (optional):** Explicit Hessian showing a(q_n) > 0, upgrading [BL]+[M] constraint to [Der]

**Possible approaches:**
- Explicit V(q) derivation from S_5D (currently OPEN)
- Convexity/symmetrization lemma for Nambu-Goto + Z₃-invariant interactions
- Topological argument for Z₃ restoration at transition
- Instanton/bounce calculation showing symmetric saddle

---

## 8. Guardrail Statement

EDC is a 5D geometric "why"-framework; it does not replace 3D microscopic
descriptions of particle processes. In this analysis:
- τ_n^BL ≈ 879 s is used only as an empirical benchmark [BL]
- V_B is calibrated [Cal] to match this benchmark in the effective WKB model
- The Z₃ analysis aims to derive V_B from geometric structure
- No external microscopic mechanism language is employed; we stay within
  the effective 5D→1D EDC framework

---

## 9. Alternative Interpretations for Factor 2

### 9.1 Two-Layer Brane (Z₂)

The factor 12 = Z₆ × Z₂ suggests the brane has a two-layer structure. The barrier could involve crossing **two layers**, each costing Δm_np.

**Problem:** Why would neutron → proton require crossing two layers?

### 9.2 Bounce/Instanton Doubling

In quantum tunneling, the bounce solution is time-symmetric. The barrier appears "twice" in the Euclidean action.

**Problem:** V_B is defined as a single barrier height, not related to action doubling.

### 9.3 Domain Wall Pair

The transition might require creating and annihilating a domain wall pair, with each wall costing Δm_np.

**Promising:** This connects to Z₆ breaking mechanism.

---

## 10. Summary

**CONJECTURE:**
```
V_B = 2 × Δm_np ≈ 2.59 MeV   [Dc]
```

Numeric depends on Δm_np option:
- Option B (PDG): V_B ≈ 2.587 MeV
- Option A (Book): V_B ≈ 2.585 MeV

**Physical interpretation (Z₃ barrier ansatz):**
> The barrier configuration corresponds to a Z₃-symmetric excited state of the Y-junction, where all three flux tube legs are equally stressed. Each leg contributes one unit of the deformation energy (Δm_np), giving a total barrier of 3×Δm_np above the proton. Since the neutron is already at Δm_np, the effective barrier height is V_B = 2×Δm_np.

**Status:** [Dc] — awaiting 5D action proof of Z₃ barrier structure.

**Impact if confirmed:** τ_n would no longer be "blindly calibrated" — the entire WKB calculation would become parameter-free.

---

## 11. Next Steps

1. **Explicit V(q) derivation** — Show from 5D membrane action that V(q) has a maximum at q_B with Z₃ symmetry

2. **Alternative geometric arguments** — Explore domain wall, layer crossing, or instanton interpretations

3. **Cross-validation** — Check if V_B = 2×Δm_np is consistent with other EDC predictions

4. **Document in main text** — Add [Dc] claim to neutron dual-route section with explicit conditional statement

---

## 11.1 Put C Corridor (5D→1D Reduction)

**Link:** See `derivations/S5D_TO_SEFF_Q_REDUCTION.md`

Put C establishes the formal pathway:
```
S_5D (bulk + brane + GHY + Israel) → S_eff[q] = ∫ dt (½ M(q) q̇² − V(q))
```

When Put C is completed:
- V(q) becomes [Der] instead of [P]
- V_B = V(q_B) − V(q_n) becomes [Der] instead of [Cal]
- The Z₃ barrier picture provides a consistency check

**OPEN:** "One unit per leg = Δm_np" remains conditional until V(q) is explicitly
computed and shows E_barrier = 3×Δm_np structure.

### 11.1.1 Tested Routes for V(q) Metastability (2026-01-27)

**Summary of Put C execution attempts:**

| Route | Status | Result | Report |
|-------|--------|--------|--------|
| Flat bulk Nambu-Goto | [Dc] | NO metastability | `PUTC_EXECUTION_REPORT.md` |
| Warped RS-like bulk | [Dc/P] | NO metastability | `PUTC_EXECUTION_REPORT.md` |
| Warped + node well | [P/Cal] | YES, V_B ≈ 2.8 MeV | `PUTC_EXECUTION_REPORT.md` |
| **Helfrich bending** | **[Dc/Cal]** | **NO-GO** | `HELFRICH_EXECUTION_REPORT.md` |

**Helfrich Route Closure [Dc]:**
The Helfrich (brane bending) term with parameter closure κ ~ σδ² was tested
as a purely geometric source for the metastable well. Result: NO-GO.
- With c₀ = 0: V_bend ~ +q² adds to NG cost (mathematical no-go)
- With c₀ ≠ 0: 250 parameter combinations tested, 0 metastable

**Current status:** The phenomenological node well [P] remains the only viable
route for metastability. Its physical origin (junction core, bulk field coupling,
or other mechanism) is OPEN.

---

## 12. Reproducibility

Calculations are in: `derivations/code/delta_m_np_options.py`

Run: `python3 derivations/code/delta_m_np_options.py`
