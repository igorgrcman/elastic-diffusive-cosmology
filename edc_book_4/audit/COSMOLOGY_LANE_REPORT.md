# Cosmology Lane Assessment — σ̃ = 100 Derivation

**Date:** 2026-03-15
**Branch:** `archive/nuclear-topology-discovery`
**Scope:** Locate, read, and assess the cosmology lane that produces σ̃ = 100.0
**Reference:** `EDC-COSMO-TSTAR-5D-ROUTEAB` (provenance tag in `sigma_tilde_value.json`)

---

## 1. Where the Document Was Found

**Primary location:** `edc_papers/paper_gravity_block003/cosmology_sigma_tilde_lane/`

This directory contains 11 files constituting the cosmology lane:

| File | Size | Role |
|------|------|------|
| `TSTAR_DERIVATION_5D.md` | 620 lines | Main derivation document |
| `TSTAR_DEFINITION.md` | 270 lines | Definitional roadmap with TODO items |
| `sigma_tilde_value.json` | 51 lines | Machine-readable σ̃ output |
| `PROVENANCE_SEAL.md` | ~40 lines | SHA-256 hash + Layer A certification |
| `SIGMA_TILDE_EXPORT_CONTRACT.md` | ~80 lines | Interface APIs (A-APIσ1–3) |
| `README.md` | ~60 lines | Import contract overview |
| `REPORT.md` | ~50 lines | Layer A firewall report |

**Discovery method:** Searched entire repo for files containing `sigma_tilde`, `T_star`,
`COSMO`, and `ROUTEAB`. The `cosmology_sigma_tilde_lane/` directory is the sole source.
No duplicate or alternative derivation exists elsewhere in the repository.

---

## 2. What T* Is Physically

**T_* (T-star)** is the "characteristic tension scale" of the 5D brane world — the
natural tension unit set by the 5D gravitational coupling.

**Structural form:**

```
T_* = C · M₅³
```

where:
- **M₅** = 5D fundamental mass scale (related to κ₅, the 5D gravitational coupling)
- **C** = dimensionless geometric coefficient encoding warped geometry, junction
  conditions, and compactification details

**Physical interpretation:** T_* is the tension scale at which the 5D bulk gravitational
dynamics sets the natural magnitude for brane tension σ. The dimensionless ratio
σ̃ = σ/T_* (or equivalently M̄_Pl⁴/σ per v56) measures how the physical brane tension
compares to this gravitationally determined scale.

**Role in the derivation chain:**

```
5D action → Israel junction conditions → T_* = C·M₅³
                                              ↓
                                         σ̃ = σ/T_*
                                              ↓
                                    α₃ = 1/σ̃ → M_X → g_X → τ_p
```

---

## 3. How σ̃ = 100 Is Derived (Claimed)

The TSTAR_DERIVATION_5D.md document presents two routes:

### Route A: Junction/Geometry

Starting from the 5D Einstein-Hilbert action with brane sources, apply Israel junction
conditions at the brane location to relate the brane tension σ to the bulk geometry.
This yields:

```
T_*^(A) = C_A · M₅³
```

where C_A encodes the junction geometry (brane embedding angles, bulk curvature profile).

### Route B: 4D Effective Reduction

Integrate over the compact extra dimension to obtain the 4D effective theory. Match the
4D Planck mass to the 5D parameters. This yields:

```
T_*^(B) = M₅³ / C_B
```

where C_B encodes the compactification volume and warping profile.

### Consistency Condition

Routes A and B must agree: T_*^(A) = T_*^(B), which requires:

```
C_A · C_B = 1
```

This is presented as a non-trivial consistency check.

### The Gap: From T_* to σ̃ = 100

The derivation document does NOT contain the step that produces σ̃ = 100. Specifically:

1. **C_A and C_B are tagged [P] (pending).** The document states: *"explicit values
   require solving warped geometry equations, which is not done here."*

2. **T_* has no numeric value.** The JSON file has `t_star.value: null`.

3. **σ_dimensional has no numeric value.** The JSON file has `sigma_dimensional.value: null`.

4. **Document hashes are "TBD".** Both TSTAR_DERIVATION_5D.md and TSTAR_DEFINITION.md
   set their document hash to "TBD (to be set when geometric coefficients determined)"
   and "TBD (to be set when derivation complete)" respectively.

5. **TSTAR_DEFINITION.md contains multiple TODO items:** "Write full 5D action",
   "Derive Israel junction", "Extract T_* form", among others. The numeric value
   is tagged [P] — "TBD".

**Yet** `sigma_tilde_value.json` claims:
- `sigma_tilde.value.central: 100.0` (±10.0)
- `sigma_tilde.status: "DERIVED"`
- `provenance.notes: "PHYSICAL_DERIVATION: sigma_tilde = 100 +/- 10 from 5D brane world (Route A + B)"`
- `provenance.epistemic_tags: ["derived", "structural", "no_external_anchors"]`

---

## 4. Epistemic Status Assessment

### 4.1 What IS established

| Claim | Status | Evidence |
|-------|--------|----------|
| T_* = C·M₅³ structural form | **[Dc]** | Follows from dimensional analysis of 5D action |
| Route A/B consistency (C_A·C_B = 1) | **[Dc]** | Algebraic consequence of matching |
| σ̃ = σ/T_* definition | **[D]** | Pure definition |
| σ̃ → α₃ → M_X → τ_p chain | **[Dc]** | Algebraically verified (v67 Layer A firewall) |
| Layer A firewall (no PDG values inside chain) | **VERIFIED** | All 6 checks pass |

### 4.2 What is NOT established

| Claim | Actual status | JSON claims | Gap |
|-------|--------------|-------------|-----|
| C_A numeric value | **[P] — pending** | Not explicit | C_A undetermined |
| C_B numeric value | **[P] — pending** | Not explicit | C_B undetermined |
| T_* numeric value | **null** | Not explicit | Cannot compute without C |
| σ_dimensional numeric value | **null** | Not explicit | Cannot compute without T_* |
| **σ̃ = 100.0** | **[P] or [I] at best** | **"DERIVED"** | **No traceable derivation chain produces this number** |

### 4.3 The provenance gap

The JSON file claims σ̃ = 100.0 with status "DERIVED" and tag "PHYSICAL_DERIVATION",
but the derivation documents it references do not contain the calculation that produces
this number. The intermediate quantities (C, T_*, σ_dimensional) are all null or pending.

**Possible explanations:**
1. The value was derived in an external calculation not committed to the repo
2. The value was estimated from phenomenological constraints (e.g., requiring α₃ ≈ 0.01)
3. The value was set as a placeholder with intent to derive later
4. The derivation exists but in a document not found in the repo search

**What the repo evidence supports:** The structural framework is sound (T_* = C·M₅³),
but the numeric value σ̃ = 100.0 cannot be traced through the documented derivation
chain. The "DERIVED" status tag in the JSON is not supported by the referenced documents.

### 4.4 Correct epistemic tag

Based on the documented evidence:

| If σ̃ = 100 came from... | Correct tag |
|--------------------------|-------------|
| Solving warped geometry for C | [Dc] — derived conditional on 5D action |
| Matching α₃ to experimental α_s(M_Z) | [Cal] — calibrated to data |
| Order-of-magnitude estimate | [I] — identified |
| Placeholder awaiting derivation | [P] — postulated |

**Without documentation of the actual calculation, the honest tag is [I] or [P],
not [D] or [Dc].**

---

## 5. Does This Close Parameter Closure for σ?

### Short answer: NO.

### Long answer:

The v67 "REAL CLOSURE" architecture established that all BLOCK-004 outputs (α₃, M_X,
g_X, τ_p) are pure functions of σ̃. This is a genuine structural achievement — the
algebraic chain has no hidden parameters.

However, "closure" has two meanings:
1. **Structural closure:** All outputs are determined once σ̃ is specified. ✓ ACHIEVED.
2. **Parameter closure:** σ̃ itself is derived from first principles. ✗ NOT ACHIEVED.

The cosmology lane provides:
- A structural form for T_* (good)
- A consistency condition between two routes (good)
- A numeric value σ̃ = 100.0 without traceable intermediate steps (insufficient)

**Parameter closure requires:** C_A (or C_B) computed from the warped geometry, yielding
T_* numerically, yielding σ̃ = σ/T_* from known σ. The derivation documents explicitly
state this computation is "not done here."

### What would genuine closure look like?

```
5D action (specified)
    ↓
Warped geometry solution (computed)
    ↓
C_A = [specific number] from junction conditions
    ↓
T_* = C_A · M₅³ = [specific value in natural units]
    ↓
σ̃ = σ/T_* = [number derived from above]
    ↓
Compare: does this equal 100 ± 10?
```

None of the steps after "Warped geometry solution" exist in the documented chain.

---

## 6. Impact on the EDC Knowledge Map

### 6.1 The σ̃ → τ_p chain remains conditionally closed

v67's algebraic structure is unaffected. Given any σ̃, the chain produces τ_p.
The question is whether σ̃ = 100 is a derived input or an assumed one.

### 6.2 The "DERIVED" tag in sigma_tilde_value.json needs correction

The JSON metadata overclaims. Based on the documented evidence:
- `sigma_tilde.status` should be **"STRUCTURAL"** or **"PENDING"**, not "DERIVED"
- `provenance.notes` should not say "PHYSICAL_DERIVATION" without the intermediate steps
- `provenance.epistemic_tags` should include "pending_numerics" or similar

### 6.3 Priority implications

1. **Solving the warped geometry for C** is the single highest-value open task in the
   entire EDC program. It would simultaneously:
   - Close σ̃ genuinely (parameter closure)
   - Close BLOCK-004 proton decay prediction
   - Provide an independent cross-check on σ = 8.82 MeV/fm² (from nuclear topology)

2. **The TSTAR_DEFINITION.md TODO list** provides a clear roadmap for what remains:
   - Write full 5D action with all terms
   - Derive Israel junction conditions for the specific EDC geometry
   - Extract C from the junction solution
   - Compute T_* numerically
   - Verify σ̃ = σ/T_* yields a value consistent with phenomenology

### 6.4 Relationship to nuclear topology

The nuclear topology program (topological pinning, V7.8 M2) uses σ = 8.82 MeV/fm²
directly. The cosmology lane uses σ̃ = σ/T_*. If both σ and T_* were independently
derived, the nuclear and cosmological σ values would provide a powerful cross-check.
Currently, σ = 8.82 is [Dc] (from P6) and σ̃ = 100 is at best [I], so this cross-check
is not yet available.

---

## 7. Summary of Findings

| Question | Answer |
|----------|--------|
| Where is the cosmology lane? | `edc_papers/paper_gravity_block003/cosmology_sigma_tilde_lane/` |
| What is T_*? | Characteristic brane tension scale T_* = C·M₅³ |
| How is σ̃ = 100 derived? | **It is not derived in the documented chain.** Structural form exists; numeric value lacks traceable intermediate steps. |
| Is it genuine derivation? | **No.** The geometric coefficient C is [P] (pending), T_* is null, σ_dimensional is null. |
| Epistemic status? | Structural framework: [Dc]. Numeric value σ̃ = 100: **[I] or [P]**, not [D]. |
| Does this close σ? | **No.** Structural closure achieved (v67); parameter closure not achieved. |

---

## 8. Bottom Line

The cosmology lane is a well-architected structural framework that correctly identifies
T_* = C·M₅³ as the key quantity and establishes the σ̃ → τ_p algebraic chain. The
Layer A firewall is clean. The export contract is well-defined.

However, the numeric value σ̃ = 100.0 ± 10.0 cannot be traced through the documented
derivation chain. The intermediate quantities (C, T_*, σ_dimensional) are null or
pending in the very documents the JSON file references. The "DERIVED" status tag and
"PHYSICAL_DERIVATION" provenance note in `sigma_tilde_value.json` are not supported
by the current state of the derivation documents.

**Solving the warped geometry for the geometric coefficient C remains the critical
path to genuine parameter closure in the EDC program.**
