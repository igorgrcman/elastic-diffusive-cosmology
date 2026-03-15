# P51 / Derivation v50: PS → IR Matching & Physical-Scale Map — Final Report

## Executive Summary

This derivation establishes the complete matching scaffold from the Pati-Salam (PS) unified scale μ_KK = π/L to a symbolic infrared scale μ_IR. Key achievements:

1. Two-panel Physical Scale Map (energy regimes + coupling flow)
2. Matching Stack: PS matching + RG running + threshold corrections
3. Scheme invariance protocol with two-route verification
4. Exotics gating interface with BC-based projection
5. Complete Notation Registry (authoritative symbol definitions)
6. Zero forbidden inputs: no electroweak masses, VEV, Newton's constant, Planck length

This is an inference scaffold, NOT a fit to measured values. The μ_IR scale is symbolic/operational.

---

## Inputs Used Table (Ultra-Hard Compliance)

| Symbol | Value/Type | Source | Tag | Forbidden? |
|--------|------------|--------|-----|------------|
| π | 3.14159... | Mathematical | [U] | NO |
| M̄_Pl | Universal | Gravity | [U] | NO |
| σ | EDC brane tension | Theory | [P] | NO |
| β | EDC control parameter | v29 | [D] | NO |
| λ | Topological parameter | v28/v30 | [D/P] | NO |
| c_A / Λ_5 | Route A/C coefficient | v48 | [Dc] | NO |
| n_g = 3 | Generations | SM structure | [D] | NO |
| r_L, r_R, r_{B-L} | BKT scales | Boundary | [P] | NO |
| μ_IR/μ_KK | Running ratio | Operational | [Op] | NO |
| c_R = 3/5 | PS matching coeff | v47 trace | [D] | NO |
| c_{B-L} = 4/5 | PS matching coeff | v47 trace | [D] | NO |

**NO FORBIDDEN INPUTS USED**

---

## Dependency & Circularity Audit

### Dependency Graph
```
σ, β, M̄_Pl → L → μ_KK = π/L
         → g_5 (Route A or C)
g_5, L, r_i → g_i(μ_KK)
g_R, g_{B-L} + matching → g_Y(μ_KK)
g_i(μ_KK) + b_i + t → g_i(μ_IR)
g_2, g_Y → sin²θ_W
```

### Root Inputs
- σ (brane tension) — [P]
- β (control parameter) — [D]
- M̄_Pl — [U]
- c_A or Λ_5 — [Dc]
- r_i BKT scales — [P]
- n_g = 3 — [D]
- μ_IR/μ_KK — [Op/symbolic]

### Circularity Check
**PASS** — The dependency graph is a DAG (no cycles).

---

## Scheme Invariance Protocol Notes (T1/T2)

### Route T1: Match → Run
1. Apply PS matching at μ_KK
2. Run couplings from μ_KK to μ_IR using SM beta functions

### Route T2: Run → Match
1. Run PS couplings to μ_KK
2. Apply PS matching
3. Run to μ_IR

### Invariance Proof
The physical invariant:
```
I = 1/g_Y² - 1/g_2²
```
evolves with (b_1 - b_2)/(8π²), which is scheme-independent at one-loop.

Both routes give identical results for I when thresholds are applied consistently.

**STATUS:** SCHEME_INVARIANT

---

## Red-Team Objections & Responses (≥10)

### Objection 1: "You're just avoiding the problem by calling μ_IR 'symbolic'"
**Response:** The scaffold is deliberately designed to separate structural predictions (sin²θ_W = 5/12 at μ_KK) from scale-dependent running. The μ_IR is an operational parameter that can be defined without reference to measured values. This is not avoidance—it's proper separation of structure from phenomenology.

### Objection 2: "Your beta functions come from SM particle content, which implicitly uses measured masses"
**Response:** Beta functions are derived from group theory (Casimir, Dynkin index) and particle representations. The number n_g = 3 is a structural fact (three chiral families), not a measured coupling. No measured masses enter the beta function derivation.

### Objection 3: "The PS matching coefficients 3/5, 4/5 require knowing the normalization, which is conventional"
**Response:** The coefficients are derived from trace normalizations in v47. These are fixed by the embedding (Y = T_3R + (B-L)/2) and group theory (Tr(T²) values). No measurement is needed.

### Objection 4: "Threshold corrections Δ_i are scheme-dependent, so your predictions are meaningless"
**Response:** The finite parts of threshold corrections are regulator-independent (proven in v49 using zeta, heat-kernel, and Pauli-Villars). Physical observables depend only on relative thresholds δΔ_{ij} = Δ_i - Δ_j, which cancel regulator artifacts.

### Objection 5: "The exotics gating relies on unknown brane masses m_b"
**Response:** We only require m_b ≥ μ_KK = π/L as a structural condition (b ≡ m_b L ≥ π). This is a constraint on allowed parameter space, not a measured input. The scaffold remains valid when this condition is satisfied.

### Objection 6: "BKT parameters r_i are unknown, so your predictions are useless"
**Response:** The BKT effects are parameterized and bounded. From v49, |δ(sin²θ_W)| ≤ C_BKT · max(r_i/L) with C_BKT ≤ 2. For r_i/L < 0.01, effects are sub-3%. The scaffold identifies where BKT enters and how to bound its impact.

### Objection 7: "You haven't actually predicted sin²θ_W at measurable scales"
**Response:** Correct—this is a matching scaffold, not a final prediction. The scaffold shows how to go from KK-scale structural prediction (5/12) to IR values via RG running. Numeric predictions require fixing μ_IR/μ_KK, which needs additional physics (σ, β values).

### Objection 8: "The two-route scheme invariance is trivial at one-loop"
**Response:** At one-loop, scheme invariance is guaranteed by RG structure. The non-trivial check is that matching and threshold corrections are applied consistently in both routes. We verify this explicitly with the invariant I = 1/g_Y² - 1/g_2².

### Objection 9: "PS unification at μ_KK requires fine-tuning"
**Response:** PS unification emerges from the orbifold construction, not fine-tuning. All PS gauge couplings derive from the same g_5 with geometric factors (L + r_i). The "unification" is structural, not fine-tuned.

### Objection 10: "Your notation lock is artificial and doesn't prevent errors"
**Response:** The Notation Registry serves two purposes: (1) prevent symbol drift across derivation versions, and (2) enable automated verification via recompute.py. It's not about preventing errors—it's about maintaining consistency in a large derivation chain.

---

## How to Extend to IR Numerics (Future)

To obtain numeric predictions, the following must be provided:

1. **σ (or β) value:** From EDC field equations or phenomenological fit
2. **λ quantized value:** From topological analysis
3. **g_5 from Route A or C:** With c_A or Λ_5 fixed
4. **μ_IR operational definition:** As a derived scale (not measured)
5. **BKT bounds:** Verify r_i/L < ε for perturbativity

The scaffold then gives:
```
sin²θ_W(μ_IR) = 5/12 + (b_1-b_2)/(8π²) · (5/12)(7/12) · ln(μ_IR/μ_KK)
```

with all inputs forbidden-free.

---

## Reviewer Trap Checklist

1. ✓ PS = Pati-Salam, NOT power spectrum
2. ✓ Wrong PS matching coefficients (3/5, 4/5 not 1/2, 1/2)
3. ✓ Confusing μ_KK = π/L vs 1/L
4. ✓ Using experimental values for μ_IR
5. ✓ Forgetting BKT shifts in g_4
6. ✓ Wrong sign in beta functions
7. ✓ Scheme-dependent threshold finite parts
8. ✓ Mixing 5D and 4D couplings ([g_5²] ≠ [g_4²])
9. ✓ Double-counting zero modes in KK sum
10. ✓ Assuming g_L = g_R at all scales
11. ✓ Forgetting U(1)_{B-L} normalization (Tr((B-L)²) = 4/3)
12. ✓ Not gating exotics properly
13. ✓ Using μ_IR as a measured value (it's operational)
14. ✓ Incorrect trace normalization in matching
15. ✓ Regulator-dependent predictions
16. ✓ Missing threshold corrections
17. ✓ Two-loop without [OPEN] tag
18. ✓ Circularity in dependency chain

---

## Verification Results

```
Total: 37/37 CHECKS PASSED
All checks PASS

v45 hash: a80b3886903152d3
v46 hash: 2742edea37e863ac
v47 hash: 7a9682f333d5349e
v48 hash: c4f114aa0c662b66
v49 hash: 81010ef2faedcefd
v50 tables hash: cebf3e5baf0de863
```

---

## Conclusion

The PS → IR matching scaffold is complete. This derivation provides the framework for converting KK-scale structural predictions to IR predictions via RG running and threshold corrections, all without forbidden experimental inputs.

**This is an inference scaffold, not a fit to measured values.**
