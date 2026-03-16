# Junction-Core C = 100 Assessment

**Date:** 2026-03-16
**Branch assessed:** `junction-core-derive-C-v1`
**Branch created:** 2026-01-27
**Commits unique to branch:** 9 (from putC computation through C derivation)
**Files changed vs main:** 29 (derivations, code, artifacts, figures)
**Created by:** Corpus Synthesis Step 2 of 9

---

## 1. Executive Summary

**C = (L₀/δ)² = 100 is a dimensional-analysis result, NOT a genuine first-principles derivation.**

The number 100 arises from identifying L₀ = 1.0 fm [I] and δ = 0.1 fm [I], giving (L₀/δ)² = (10)² = 100. Both inputs are **pattern identifications** [I], not derived quantities. The geometric argument for WHY E₀ = C·σ·δ² with C = (L₀/δ)² is valid [Dc] — it correctly identifies the pancake aspect ratio as the origin of the large coefficient. But the numerical value 100 is only as good as the inputs L₀ = 1 fm and δ = 0.1 fm.

**This C is completely unrelated to σ̃ = 100 in the cosmology lane.** Different physics, different sectors, different derivation chains. The numerical coincidence (both equal 100) appears to be accidental.

**Correct epistemic tag: [Dc] conditional on [I] inputs** — geometric structure derived, numerical value identified.

---

## 2. What C Is (Exact Physical Definition)

### 2.1 Definition

C is the dimensionless coefficient in the junction-core well depth:

```
E₀ = C × σ × δ²
```

where:
- E₀ = depth of the attractive core potential V_core(q) at q = 0
- σ = 8.82 MeV/fm² = EDC brane tension [Dc]
- δ = 0.1 fm = brane thickness [I]

### 2.2 Physical Role

The junction-core model gives the total potential for the collective coordinate q (neutron→proton transition):

```
V_total(q) = V_NG(q) + V_core(q)
```

where:
- V_NG(q) = 3τ√(L₀² + q²) is the Nambu-Goto stretching cost (single-well, minimum at q=0)
- V_core(q) = −E₀·f(q/δ) is the localized core attraction (creates the secondary minimum)

**Without V_core:** V_total is single-well → no metastability → no neutron lifetime
**With V_core and C ~ 100:** V_total has a double-well structure with V_B ≈ 2.6 MeV → τ_n ≈ 880 s

### 2.3 How C Was Found

**Before this branch:** C was scanned over a range [0.5, 200] in the junction_core_well.py computation. The scan found:
- 2340 configurations tested
- 635 metastable (C >> 1 required)
- C ~ 100 gives V_B ≈ 2.6 MeV, matching 2×Δm_np [Cal]

**On this branch:** The DERIVE_C_FROM_GEOMETRY.md derives C = (L₀/δ)² from the geometric structure of the junction core.

---

## 3. The Derivation (Is It Genuine?)

### 3.1 The Argument

The junction core occupies a 3D region where three flux tubes meet:
- **Transverse extent:** ~L₀ (nucleon scale, ~1 fm)
- **Bulk thickness:** ~δ (brane thickness, ~0.1 fm)

The core action density separates [Dc]:
```
ρ_core(x, y, q) = σ × g_⊥(r_⊥/r₀) × f(q/δ)
```

Integrating out transverse directions:
```
V_core(q) = −σ × A_eff × f(q/δ)
```

where A_eff = r₀² × I_⊥ with I_⊥ = π for well-behaved profiles (Gaussian, Lorentzian², disk — all give π).

Written as E₀ = C × σ × δ²:
```
C = I_⊥ × (r₀/δ)²
```

### 3.2 Assessment of Each Step

| Step | Content | Tag | Assessment |
|------|---------|-----|------------|
| 3D core has transverse extent ~L₀ | Physical picture | [Dc] | Reasonable — junction IS nucleon-scale |
| Separable density ansatz | Simplification | [P] | Not proven from S_5D; an assumption |
| I_⊥ = π for standard profiles | Mathematical | [M] | Correct for Gaussian, Lorentzian², disk |
| I_⊥ factor absorbed into L₀ identification | Convention | [Def] | The document chooses C = (L₀/δ)² rather than C = π(L₀/δ)² |
| r₀ = L₀ = 1.0 fm | Identification | [I] | Pattern-matched to proton charge radius |
| δ = 0.1 fm | Identification | [I] | Pattern-matched to brane thickness |
| C = (L₀/δ)² = 100 | Final result | [Dc\|I] | Geometric structure [Dc], numerical value [I] |

### 3.3 Honest Assessment

The derivation document itself reveals the struggle (§6):

1. First attempt: C = π × (L₀/δ)² = 314 — "Wait — this is too large!"
2. Second attempt: Three-leg overlap → C ≈ 44 — "Still not quite 100"
3. Third attempt: r₀ = L₀/2 → C ≈ 78.5 — "Closer to 100!"
4. Final answer: "No I_⊥ factor" → C = (L₀/δ)² = 100 — "This matches exactly!"

**The derivation was tuned to reproduce the known best-fit answer.** The choice to drop I_⊥ (or absorb it) and use r₀ = L₀ (not L₀/2, not L₀/3) was made because it gives 100. This is a calibration disguised as a derivation.

### 3.4 What IS Genuine

The key insight that IS derived:
```
C ∝ (L₀/δ)²    [Dc]
```

The fact that C scales as the **square of the aspect ratio** is a genuine geometric result. The pancake structure (wide transverse, thin bulk) naturally produces a large dimensionless coefficient. This explains WHY C >> 1, even if it doesn't pinpoint C = 100.

---

## 4. Epistemic Status

### 4.1 Correct Tag Assignment

| Quantity | Claimed Tag | Correct Tag | Reason |
|----------|------------|-------------|--------|
| C ∝ (L₀/δ)² | [Dc] | **[Dc]** | Geometric aspect ratio is correctly identified |
| L₀ = 1.0 fm | [I] | **[I]** | Pattern-matched to nucleon size |
| δ = 0.1 fm | [I] | **[I]** | Pattern-matched to brane thickness |
| C = 100 | [Dc] | **[I] or [Cal]** | Numerical value depends on [I] inputs |
| E₀ = C·σ·δ² = 8.82 MeV | [Dc] | **[Dc\|I]** | Dimensional analysis [Dc], value [I] |
| V_B ≈ 2.6 MeV | [Dc] | **[Dc\|I]+[P]** | Depends on C [I] and Z₃ barrier conjecture [P] |

### 4.2 The Chain

```
L₀ = 1.0 fm [I]  ─────┐
                        ├──→  C = (L₀/δ)² = 100 [I]
δ = 0.1 fm  [I]  ─────┘
                                    │
σ = 8.82 MeV/fm² [Dc] ────────────┼──→ E₀ = C·σ·δ² = 8.82 MeV [Dc|I]
                                    │
V_B = 2×Δm_np [P] ────────────────┼──→ V_B ≈ 2.6 MeV [P]
                                    │
                                    └──→ τ_n ≈ 880 s [Dc+P+Cal]
```

### 4.3 Comparison with Book IV Ch.8

Book IV Ch.8 proposes L₀/δ = π² ≈ 9.87. On this branch, L₀/δ = 10.0.

If L₀/δ = π² exactly:
- C = (π²)² = π⁴ ≈ 97.4

This is within 3% of 100. The connection L₀/δ = π² → C = π⁴ ≈ 97 is tantalizing but NOT explored on this branch.

---

## 5. Connection to σ̃ = 100 (Same or Different?)

### 5.1 Answer: COMPLETELY DIFFERENT

| Property | Junction-core C | Cosmology σ̃ |
|----------|----------------|-------------|
| **Physical system** | Neutron metastability well depth | Dimensionless brane tension ratio |
| **Definition** | C = E₀/(σδ²) | σ̃ = σ/T_* (or σ̃ = 100 from α₃ = 1/σ̃) |
| **Physics sector** | Nuclear (Book IV Ch.3-9) | Cosmology (Block-003 v67) |
| **Derivation chain** | L₀, δ → geometric ratio | T_*, M₅ → 5D gravity |
| **Derivation path** | 3D→1D reduction of junction core | 5D warped geometry |
| **References to other** | ZERO | ZERO |
| **The number 100** | (1.0/0.1)² = 100 | Calibrated from α₃ ≈ 0.01 |

**Zero cross-references exist between these two quantities.** The derivation documents for C never mention σ̃, T_*, α₃, proton decay, or the cosmology lane. The cosmology lane documents never mention junction-core wells, L₀/δ, or V_core.

### 5.2 Why Both Are 100: Coincidence Analysis

| Source of "100" | Physics |
|----------------|---------|
| Junction C = (L₀/δ)² | (1 fm / 0.1 fm)² = (10)² = 100. The 10 comes from nucleon/brane scale ratio |
| Cosmology σ̃ = 100 | Calibrated from α₃(μ_*) = 1/σ̃ ≈ 0.01. The 100 comes from 1/α_s |

These are physically unrelated: one comes from a geometric aspect ratio in nuclear physics, the other from a coupling constant at the GUT scale. The coincidence is numerical only.

### 5.3 Could There Be a Deep Connection?

**Speculative:** If L₀/δ = π² and C = π⁴, then C ≈ 97, not exactly 100. Meanwhile σ̃ was proven to NOT be 100 (the DERIVED claim was retracted; σ̃ = 1 from RS geometry per the latest session). So the "coincidence" is actually between a number ≈97 and a number that turned out to be wrong (σ̃ ≠ 100).

**Verdict:** No deep connection. The numbers are different after correction.

---

## 6. Connection to L₀/δ = π² (Critical Observation)

### 6.1 The Tantalizing Near-Match

Book IV Ch.8 proposes L₀/δ = π² ≈ 9.87 as a geometric hypothesis [P].
This branch uses L₀/δ = 10.0.

If L₀/δ = π² exactly:
```
C = (L₀/δ)² = (π²)² = π⁴ ≈ 97.4
```

This is a pure mathematical constant, not a calibrated number. The difference from 100 is only 2.6%.

### 6.2 What This Would Mean

If L₀/δ = π² could be DERIVED from the 5D action:
1. C = π⁴ would be determined [Der] (no free parameters)
2. E₀ = π⁴ × σ × δ² ≈ 8.59 MeV
3. V_B = 2Δm_np ≈ 2.59 MeV (if Z₃ barrier conjecture holds)
4. S_E/ℏ = 2π³ ≈ 62.0 (as in Ch.9)
5. τ_n would have fewer free parameters

### 6.3 Status of L₀/δ = π²

From Book IV Ch.8 and the R1_GLOBAL_DISCOVERY.md:
- L₀/δ = π² is [P] — physically motivated but not rigorously derived
- Three geometric motivations (standing wave, two-fold winding, Steiner) — none rigorous
- BVP route gives L₀/δ = F(η) as continuous family; π² at η ≈ 0.052 but not uniquely selected
- This is the **single most impactful open problem** for the τ_n chain

### 6.4 Was L₀/δ = π² Explored on This Branch?

**No.** The DERIVE_C_FROM_GEOMETRY.md uses L₀ = 1.0 fm and δ = 0.1 fm throughout, giving L₀/δ = 10.0 exactly. The π² hypothesis is not mentioned. The sensitivity analysis tests L₀ = 0.8, 1.0, 1.2 and δ = 0.08, 0.10, 0.12 but does NOT test L₀/δ = π².

### 6.5 Recommendation

This connection should be explicitly investigated:
- If L₀/δ = π²: C = π⁴ ≈ 97.4 (pure constant)
- If L₀/δ = 10: C = 100 (pattern-matched)
- The 2.6% difference is within the sensitivity range documented in §8.1 of the derivation

---

## 7. Should This Be in Canonical Text?

### 7.1 What SHOULD Be Canonical

1. **The geometric insight C ∝ (L₀/δ)²** — This explains WHY C >> 1. The pancake aspect ratio is a genuine and important result. [Dc]

2. **The junction-core model** — V_total(q) = V_NG(q) + V_core(q) with three mechanisms (A1/A2/A3) tested. [Dc within model]

3. **The NO-GO for C = O(1)** — With C ~ 1-5, V_B ≈ 0.22 MeV, far too small. This eliminates the naive unit-coefficient scenario. [Dc]

4. **The Helfrich NO-GO** — 260/260 configurations failed. Bending rigidity cannot generate metastability. [Dc]

### 7.2 What Should NOT Be Presented as Derivation

1. **C = 100 exactly** — This is [I], not [Der]. The derivation was tuned (§3.3 above).

2. **V_B "derived" from C** — V_B still depends on [P] barrier conjecture and [I] inputs.

3. **"No free parameters"** — The document claims "no free parameters remain" but L₀ and δ are both [I].

### 7.3 Current Status in Books

- **Book IV Ch.3:** Uses V_B = 2Δm_np [P] without referencing C or this derivation
- **Book IV Ch.8:** Uses L₀/δ as a ratio but doesn't connect to C
- **Book II:** The derivation is on this branch but not in the main text

### 7.4 Recommendation

**YES, the C ∝ (L₀/δ)² result should be in canonical text**, with correct tags:
- Insert in Book IV between Ch.3 (where V(q) is introduced) and Ch.6 (where S_E is computed)
- Emphasize the geometric insight: C >> 1 is explained by pancake aspect ratio
- Explicitly note the [I] status of L₀ and δ
- Note the tantalizing L₀/δ = π² → C = π⁴ connection
- Do NOT present C = 100 as a closed derivation

---

## 8. Action Items

### 8.1 Integration

- [ ] Add C ∝ (L₀/δ)² to Book IV Ch.4 or new section in Ch.3 (where V(q) is defined)
- [ ] Update Ch.8 to note that L₀/δ = π² implies C = π⁴ ≈ 97
- [ ] Add junction-core well model to derivation tree ledger in Ch.16
- [ ] Reference the Helfrich NO-GO (260/260) as supporting evidence for non-minimal physics

### 8.2 Investigation Needed

- [ ] Test L₀/δ = π² explicitly in the junction-core model: does C = π⁴ give acceptable V_B?
- [ ] If V_B = 2Δm_np with C = π⁴: what is τ_n? (Expected: close to 880 s since π⁴ ≈ 97 vs 100)
- [ ] Is there a 5D action derivation of L₀/δ = π²? (This is OPR step 4, highest impact)
- [ ] The factor I_⊥ = π was dropped — should it be? If retained: C = π(L₀/δ)² = π³ × π² = π⁵ ≈ 306. This is too large. Resolution needed.

### 8.3 Corrective

- [ ] The claim "C: [P/Cal] → [Dc]" in the derivation document overclaims. Correct to: "C ∝ (L₀/δ)²: [Dc]; C = 100: [I]"
- [ ] The claim "V_B: [Cal] → [Dc]" overclaims. V_B still requires [P] barrier conjecture.

---

## 9. Branch Content Summary

**29 files changed vs main**, including:

| File | Content | Key Finding |
|------|---------|-------------|
| DERIVE_C_FROM_GEOMETRY.md | C = (L₀/δ)² derivation | Central result [Dc\|I] |
| JUNCTION_CORE_EXECUTION_REPORT.md | 2340 configs, 635 metastable | C ~ 100 needed for V_B match |
| HELFRICH_EXECUTION_REPORT.md | 260/260 NO-GO | Bending cannot create well |
| PUTC_EXECUTION_REPORT.md | Put C corridor variants | Framework for 5D→1D reduction |
| S5D_TO_SEFF_Q_REDUCTION.md | Formal reduction pathway | S_eff[q] from 5D action (incomplete) |
| V_B_FROM_Z3_BARRIER_CONJECTURE.md | V_B = 2Δm_np [Dc] | Z₃ symmetric barrier argument |
| derive_C_integrals.py | Numerical verification | All profiles give I_⊥ = π |
| junction_core_well.py | Full scan code | 2340 configurations |
| putC_compute_MV.py | Put C computation | 3 variants tested |
| putC_helfrich_well.py | Helfrich scan | 260 configs, 0 metastable |

---

*Assessment produced from complete reading of DERIVE_C_FROM_GEOMETRY.md (282 lines), JUNCTION_CORE_EXECUTION_REPORT.md (150+ lines), V_B_FROM_Z3_BARRIER_CONJECTURE.md (120+ lines), S5D_TO_SEFF_Q_REDUCTION.md (100+ lines), HELFRICH_EXECUTION_REPORT.md (80+ lines), and derive_C_integrals.py (250 lines). All on branch junction-core-derive-C-v1.*
