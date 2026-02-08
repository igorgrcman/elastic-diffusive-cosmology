# M6 Model Sensitivity Report

**Date:** 2026-01-28
**Status:** ANALYSIS COMPLETE
**Finding:** Model is ROBUST to coordination n

---

## 1. Executive Summary

The M6 model predictions are **largely independent of the coordination number n**.

| Prediction | Depends on n? | Result |
|------------|---------------|--------|
| K (pinning constant) | NO | K = 0.94 MeV from σ |
| τ_n (free neutron) | NO | ~880 s |
| τ_n (bound neutron) | YES | Stable for ALL n ≥ 4 |
| B.E.(d) | NO | ~2.8 MeV |
| B.E.(He-4) | NO | ~30 MeV (tetrahedron geometry) |
| B.E.(Li-6) | NO | ~35 MeV (cluster model) |
| Be-8 instability | NO | Predicted for all n |

**Conclusion:** The model is "nosiv" (viable) without proving n=6 exactly.

---

## 2. What Depends on n?

### 2.1 Independent of n (Local Geometry)

Small nuclei predictions depend on **local geometry**, not lattice coordination:

- **Deuterium**: 1 p-n bond (Y-junction contact)
- **He-4**: Tetrahedron with 6 edges (fixed geometry)
- **Li-6**: α+d cluster (fixed geometry)
- **Be-8**: Cube with 12 edges vs 2×tetrahedron

These are determined by the **shape of the configuration**, not by "how many neighbors does the lattice allow".

### 2.2 Dependent on n (Bulk/Lattice Properties)

The coordination n matters for:

1. **Bound neutron in large nucleus**: Barrier raised by nK
   - But stable for ALL n ≥ 4
   - n=4: τ ~ 10^13 s (stable)
   - n=6: τ ~ 10^16 s (very stable)
   - n=8: τ ~ 10^19 s (extremely stable)

2. **Nuclear matter saturation**: Not yet tested, but likely n-dependent

3. **Interpretation of "closed" structures**: Semantic, not predictive

---

## 3. Sensitivity Test Results

### 3.1 Bound Neutron Stability vs n

| n | ΔV_eff (MeV) | S_eff/ℏ | τ_bound (s) | Status |
|---|--------------|---------|-------------|--------|
| 4 | 2.24 | 78.9 | 1.8×10^13 | STABLE |
| 5 | 2.47 | 83.0 | 1.1×10^15 | STABLE |
| 6 | 2.71 | 86.8 | 5.1×10^16 | STABLE |
| 7 | 2.94 | 90.5 | 2.1×10^18 | STABLE |
| 8 | 3.18 | 94.1 | 7.2×10^19 | STABLE |

**Key observation:** Bound neutron is stable for ALL n ≥ 4.

### 3.2 Binding Energies vs n

| Observable | n=4 | n=5 | n=6 | n=7 | n=8 | Observed |
|------------|-----|-----|-----|-----|-----|----------|
| B.E.(d) | 2.83 | 2.83 | 2.83 | 2.83 | 2.83 | 2.22 MeV |
| B.E.(He-4) | 30.5 | 30.5 | 30.5 | 30.5 | 30.5 | 28.3 MeV |
| B.E.(Li-6) | 35.2 | 35.2 | 35.2 | 35.2 | 35.2 | 32.0 MeV |
| Be-8 < 2α | YES | YES | YES | YES | YES | YES |

**Key observation:** Binding energies are IDENTICAL for all n.

---

## 4. Epistemological Implications

### 4.1 Original Claim (Too Strong)

> "n=6 is derived from Steiner dual graph" [Der]

**Problems identified:**
- Planar duality doesn't extend to 5D automatically
- Z₆ symmetry is not automatic from Y-junction (which has C₃)
- Exterior angle argument requires planar embedding

### 4.2 Revised Claim (Correct)

> "M6 model with effective coordination n_eff ≈ 6 reproduces nuclear observables.
> The exact value of n does not significantly affect predictions for small nuclei.
> n ≈ 6 is plausible from local planarity + honeycomb minimization." [I]

This is **honest** and **sufficient** for model validity.

### 4.3 What We Learned

1. **The physics is in K, not in n**
   - K = f × σ × A_contact ≈ 0.94 MeV
   - This is the key derived quantity

2. **Small nuclei test K, not n**
   - Their predictions don't depend on lattice coordination
   - They depend on local geometry (tetrahedron, cube, etc.)

3. **n matters only for bulk properties**
   - Large nuclei saturation
   - Nuclear matter equation of state
   - These are future tests

---

## 5. Recommended Status Updates

| Component | Old Status | New Status | Rationale |
|-----------|------------|------------|-----------|
| n=6 coordination | [Der] | **[I]** | Not derivable without more assumptions |
| K derivation | [Dc/I] | **[Dc/I]** | Unchanged (correct) |
| τ_n predictions | [Dc] | **[Dc]** | Unchanged |
| B.E. predictions | [I] | **[I]** | Unchanged |
| Be-8 instability | [Dc] | **[Dc]** | Unchanged |
| Model overall | [Der/I] | **[Dc/I]** | Honest assessment |

---

## 6. Path Forward

### 6.1 M6-Weak (Current, Robust)

- "Effective coordination n_eff ≈ 6" [I]
- Works for n ∈ {4, 5, 6, 7, 8}
- Sufficient for all current tests

### 6.2 M6-Strong (Target, Requires Proof)

To claim n=6 exactly [Der], need:
1. Define cell complex in 5D (Voronoi/Delaunay or local planarity)
2. Prove hexagonal tiling minimizes energy
3. Show dual has coordination 6

This is a **future goal**, not current status.

---

## 7. Summary Box

```
┌─────────────────────────────────────────────────────────────────────┐
│  M6 SENSITIVITY TEST: KEY FINDINGS                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  THE MODEL IS ROBUST TO n ∈ {4, 5, 6, 7, 8}                        │
│                                                                     │
│  WHY?                                                               │
│    • K comes from σ, NOT from n                                     │
│    • Small nuclei depend on LOCAL geometry                          │
│    • n only affects bulk/large-nucleus properties                   │
│                                                                     │
│  IMPLICATION:                                                       │
│    • Don't need exact proof of n=6                                  │
│    • "n_eff ≈ 6" [I] is sufficient                                  │
│    • Model is "nosiv" (viable) as-is                                │
│                                                                     │
│  HONEST STATUS:                                                     │
│    • n ≈ 6: [I] (plausible, not derived)                           │
│    • K ≈ 0.94 MeV: [Dc/I] (derived from σ)                         │
│    • Model overall: [Dc/I] (partially derived)                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8. Version History

- 2026-01-28 v1.0: Initial sensitivity analysis
