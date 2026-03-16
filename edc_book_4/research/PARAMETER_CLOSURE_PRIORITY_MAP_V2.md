# Parameter Closure Priority Map — V2
## Post σ̃ Audit Update
## Date: 2026-03-16
## Status: SUPERSEDES any prior parameter closure planning
## Branch: claude/analyze-codebase-KKY9n

---

## 1. What Changed Since the Original Plan

The original three-line parameter closure plan was conceived before the
σ̃ canonical audit. Five findings from the 2026-03-16 audit session
fundamentally alter the landscape:

### Finding 1: σ_BookI [M³] ≠ σ_covariant [M⁴]

**Impact:** The nuclear brane tension σ_BookI (used in Book I/II for
defect energetics, particle masses, and nuclear scales) is a
**different physical quantity** from the covariant brane tension
σ_covariant (appearing in the RS action, Israel junction conditions,
and 5D gravity). They have different dimensions:

| Symbol | Dimensions | Interpretation | Where used |
|--------|-----------|----------------|------------|
| σ_BookI | [M³] = energy/area | 2D surface tension | Particle masses, nuclear radii, defect energetics |
| σ_covariant | [M⁴] = energy/volume | 4D brane tension | RS fine-tuning, Λ₄, Israel junction, g₅ routes |

**Consequence:** Any derivation route that equates these two is wrong.
The σ̃ definitions in v48–v67 conflated them. The correct dimensionless
ratio is σ̃ = σ_covariant / σ_RS with σ_RS = 3M₅³/(4πℓ).

### Finding 2: σ̃ = 1 from RS geometry + Λ₄

The cosmological constant constraint gives:

```
Λ₄ = (3/ℓ²)(σ̃² − 1)     [EXACT, Der]
```

With |Λ₄| = 2.89 × 10⁻¹²² M_Pl⁴:

```
σ̃ = 1 + O(10⁻⁵⁶)
```

σ̃ is constrained to unity with extraordinary precision. There is no
room for σ̃ ≫ 1 or σ̃ = 100. This is a Layer B result (uses measured Λ₄)
but the constraint is so tight that it is effectively structural.

### Finding 3: Route A/C fail by 7-10 orders of magnitude

v56's routes for fixing g₅:
- Route A (g₅² = 4π/M₅): α₃ = 5.2×10⁻¹² vs 0.118 → off by 10¹⁰
- Route C (g₅² = 4π/σ^{1/4}): off by ~10⁷

The formula α₃ = 1/σ̃ is an artefact of these failed routes. It does not
hold physically.

### Finding 4: g₅^(C) is a free parameter (OPR-32)

The 5D colour gauge coupling cannot be derived from EDC axioms P1–P4.
The gauge kinetic sector (S₅ = -(1/4g₅²)∫F²) and the gravitational
sector (S₅^grav = M₅³∫R) are independent. No EDC axiom couples them
at the level needed to fix g₅.

One measurement — α_s(M_Z) = 0.118 — fixes g₅^(C) completely.
PS unification [P] then determines g₅^(L) = g₅^(C), reducing
3 SM gauge couplings to 1 free parameter.

### Finding 5: OPR-31 is moot

The σ̃ enhancement problem (needing σ̃ ≫ 1 for α₃ ≪ 1) was entirely
an artefact of the invalidated formula α₃ = 1/σ̃. With g₅^(C) as free
parameter, σ̃ = 1 is the correct structural value and no enhancement
mechanism is needed.

---

## 2. LINE 1 — 5D Action First Principles: Updated Assessment

### Original intent
Derive EDC parameters (σ, ℓ, Rξ, g₅) from the 5D action without
external measurement input.

### What the σ̃ audit changes

**σ_covariant is now the correct target, not σ_BookI.**

The 5D gravitational action determines σ_covariant through the Israel
junction conditions:

```
σ_RS = 3M₅³/(4πℓ)     [Dc from Israel junction]
```

This is the RS fine-tuning value. Any deviation from σ_RS produces a
non-zero cosmological constant. The Λ₄ constraint forces σ̃ = 1, meaning:

```
σ_covariant = σ_RS     [to 56 decimal places]
```

**Assessment of remaining routes:**

| Route | Target | Status after audit |
|-------|--------|-------------------|
| σ_RS from Israel junction | σ_covariant | CLOSED [Dc] — fully derived from M₅, ℓ |
| σ̃ from Λ₄ constraint | dimensionless ratio | CLOSED [Dc+BL] — σ̃ = 1 |
| M₅ from hierarchy relation | 5D Planck mass | CONDITIONAL [I+BL] — M₅³ℓ = M̄_Pl² |
| ℓ from M₅ and M̄_Pl | compactification length | CONDITIONAL [I+BL] — ℓ = M̄_Pl²/M₅³ |
| g₅^(C) from action | gauge coupling | **BLOCKED** — proven impossible (OPR-32) |
| Rξ from 5D diffusion | correlation length | OPEN — still [I+BL] via Rξ = ℏc/M_Z |
| σ_BookI from Plenum | nuclear tension | OPEN — distinct from σ_covariant |

**Key insight:** The gravitational sector is largely closed (σ_covariant,
σ_RS, ℓ, M₅ form a self-consistent system given M̄_Pl). The gauge sector
(g₅^(C)) is provably irreducible. The nuclear sector (σ_BookI, Rξ) is
the remaining open frontier — but it targets a different physical
quantity from the cosmological σ_covariant.

**Routes now blocked:**
- Any route that conflates σ_BookI with σ_covariant
- Any route that derives g₅ from gravitational parameters
- Route A (g₅² = 4π/M₅) — fails by 10¹⁰
- Route C (g₅² = 4π/Λ₅) — fails by 10⁷
- Any route that targets σ̃ ≫ 1

**Routes still valid:**
- σ_BookI from Plenum membrane energetics (independent of σ_covariant)
- Rξ from 5D diffusion equation in EDC geometry (could reduce [BL])
- ℓ from Rξ or from M₅ hierarchy (two independent paths → cross-check)

---

## 3. LINE 2 — Empirical Consistency Network: Updated Assessment

### Original intent
Build a network of consistency relations between EDC parameters using
multiple independent constraints (Λ₄, particle masses, nuclear radii,
gauge couplings, etc.) to check for soft circularity.

### What the σ̃ audit changes

**The σ_BookI ≠ σ_covariant separation doubles the parameter space but
makes the network cleaner.** Constraints that were previously thought
to link σ (one quantity) to multiple observables now split into two
independent subnetworks:

#### Subnetwork A: Cosmological/gravitational (σ_covariant)
| Constraint | Inputs | Determines | Status |
|-----------|--------|-----------|--------|
| RS fine-tuning | M₅, ℓ | σ_RS = σ_covariant | [Dc] — CLOSED |
| Λ₄ detuning | σ̃, ℓ | σ̃ = 1 | [Dc+BL] — CLOSED |
| Hierarchy relation | M₅, ℓ, M̄_Pl | M₅³ℓ = M̄_Pl² | [I+BL] — CLOSED |
| Warp factor | ℓ, M₅ | kℓ = ln(M_Pl/M_EW) ≈ 37 | [Dc] — standard RS |

**Status: This subnetwork is fully closed.** No new derivations needed.
All parameters are determined by M₅ and M̄_Pl (or equivalently by ℓ and M̄_Pl).

#### Subnetwork B: Nuclear/defect (σ_BookI)
| Constraint | Inputs | Determines | Status |
|-----------|--------|-----------|--------|
| Particle masses | σ_BookI, Rξ | m_e, m_μ, etc. | [P]+[BL] — OPEN |
| Nuclear radii | σ_BookI, ℓ | R ~ ℓ | [P] — OPEN |
| Proton stability | σ_BookI, topology | τ_p | [P] — OPEN |
| Neutron lifetime | σ_BookI, V(q) | τ_n | [P]+[Cal] — OPEN |
| Defect energetics | σ_BookI, δ | E_defect | [P] — OPEN |

**Status: This subnetwork is largely open.** It uses σ_BookI [M³],
which is a nuclear/condensed-matter-like quantity not constrained by
cosmological data.

#### What constraints are now invalidated?
- α₃ = 1/σ̃ — INVALIDATED (required Route A)
- β = σ̃⁴ — INVALIDATED (Route A consistency condition artifact)
- Any constraint linking σ̃ to gauge couplings — INVALIDATED

#### What constraints remain independent?
- Λ₄ constraint on σ̃ (Subnetwork A) — independent of Subnetwork B
- σ_BookI from Plenum pressure (Subnetwork B) — independent of Subnetwork A
- Rξ = ℏc/M_Z (Subnetwork B) — independent of both but uses M_Z [BL]
- g₅^(C) from α_s(M_Z) (neither subnetwork) — free parameter

**The soft circularity warning from the original plan is now resolved:**
the apparent circularity arose because σ_BookI and σ_covariant were
conflated, creating false loops. With the separation, each subnetwork
has clean input/output structure.

---

## 4. LINE 3 — 5D Reinterpretation of Experiments: Updated Assessment

### Original intent
Use experimental measurements (particle lifetimes, radii, masses,
decay rates) to constrain or measure EDC parameters directly.

### What the σ̃ audit changes

**The σ_BookI / σ_covariant separation clarifies which experiments
constrain which parameters:**

#### Experiments relevant for σ_covariant (cosmological)
| Experiment | What it constrains | Status |
|-----------|-------------------|--------|
| Λ₄ measurement (Type Ia SNe, CMB) | σ̃ = 1 | [BL] — DONE |
| Gravitational measurements | M̄_Pl | [BL] — DONE |
| Collider hierarchy (M_EW/M_Pl) | kℓ, M₅ | [I+BL] — DONE |

**Assessment:** The cosmological side is fully constrained.
No new experiments would help here — the parameters are already
determined.

#### Experiments relevant for σ_BookI (nuclear)
| Experiment | What it constrains | Status |
|-----------|-------------------|--------|
| Particle masses (m_e, m_μ, etc.) | σ_BookI · Rξ products | OPEN — [P]+[BL] |
| Nuclear radii | σ_BookI · ℓ products | OPEN — [P] |
| Neutron lifetime | V(q) from σ_BookI, δ | OPEN — [P]+[Cal] |
| Proton lifetime | Topology + σ_BookI | OPEN — [P] |
| Particle radii (r_p, r_n) | σ_BookI, wavefunction overlap | OPEN — [P] |

**Assessment:** The nuclear side has many open constraints, but they
all involve σ_BookI [M³] — the nuclear surface tension, not the
cosmological brane tension.

#### Experiments relevant for g₅^(C)
| Experiment | What it constrains | Status |
|-----------|-------------------|--------|
| α_s(M_Z) = 0.1180 ± 0.0009 | g₅^(C) directly | [BL] — SUFFICIENT |
| QCD jet rates, τ decays, lattice | α_s consistency | [BL] — redundant |

**Assessment:** One measurement suffices. Additional QCD measurements
provide consistency checks but no new information for EDC.

#### Which experimental domains are still relevant?

For σ_covariant: **None needed** — fully determined.

For σ_BookI: **All nuclear/particle experiments** remain relevant.
The neutron lifetime program (Phase 2 plans on the research branch)
targets exactly this: deriving V(q) from the 5D action with σ_BookI
as the brane tension. Particle masses, radii, and lifetimes all
constrain σ_BookI and the nuclear geometry.

For g₅^(C): **Only α_s(M_Z)** — a single measurement fixes it.

---

## 5. New Top Priorities Given Today's Findings

### Priority ranking after σ̃ audit

| Rank | Target | What it would achieve | Difficulty | Value |
|------|--------|----------------------|------------|-------|
| 1 | **σ_BookI from Plenum** | Derive nuclear tension from 5D Plenum field | HIGH | CRITICAL |
| 2 | **Rξ from 5D diffusion** | Remove [BL] (M_Z input) from Rξ | MEDIUM | HIGH |
| 3 | **V(q) from 5D action** | Derive double-well for neutron lifetime | HIGH | HIGH |
| 4 | **ℓ from independent derivation** | Cross-check with M₅ hierarchy | MEDIUM | MEDIUM |
| 5 | **Thick-junction core energy** | Phase 2 Lane B (N7) | MEDIUM | MEDIUM |
| 6 | **PS hook from symmetry breaking** | Reduce [P] status of g₅^(C) = g₅^(L) | HIGH | LOW |

### Why these priorities?

**Rank 1 (σ_BookI from Plenum)** is highest because:
- σ_BookI is the single most-used parameter in nuclear derivations
- It enters particle masses, nuclear radii, defect energetics
- It is currently [P] (postulated as σ = 8.82 MeV/fm²)
- The Plenum field is the unique EDC mechanism for brane energetics
- After today's separation, σ_BookI is clearly defined as a [M³] quantity
- σ_covariant is already derived — σ_BookI is the remaining gap

**Rank 2 (Rξ from 5D diffusion)** because:
- Rξ appears in nearly every particle mass formula
- Currently Rξ = ℏc/M_Z [I+BL] — uses M_Z as input
- A derivation from 5D diffusion dynamics would remove the [BL] tag
- This is structurally independent of σ_BookI

**Rank 3 (V(q) from 5D action)** because:
- Directly addresses the neutron lifetime program
- Phase 2 (Lane B, N7 thick-junction) is already planned
- But today's finding clarifies: V(q) uses σ_BookI, not σ_covariant

### What is now deprioritized?

| Former priority | Why deprioritized |
|----------------|------------------|
| σ̃ enhancement | MOOT — OPR-31 closed |
| g₅ from geometry | IMPOSSIBLE — OPR-32 proven |
| Route A/C refinement | INVALIDATED — fail by 10 orders |
| α₃ = 1/σ̃ derivation | INVALIDATED — artefact |
| Λ₅ from Plenum for σ_covariant | LOW VALUE — σ_covariant already determined by RS |

---

## 6. The Single Highest-Value Next Step

### Given the constraints:

1. σ_covariant requires Λ₅ from Plenum → but σ_covariant is already
   determined (σ_RS from Israel junction, σ̃ = 1 from Λ₄). Deriving
   Λ₅ would be a consistency check, not a new result.

2. g₅^(C) is fixed by α_s(M_Z) as free parameter → no derivation
   possible. Accept and move on.

3. σ̃ = 1 is the structural baseline → no enhancement needed.

4. Rξ = ℏc/M_Z remains [I+BL] → derivable in principle from 5D
   diffusion equation, but the route is not yet identified.

### The highest-value open derivation is:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   DERIVE σ_BookI FROM PLENUM MEMBRANE ENERGETICS            │
│                                                             │
│   Target: σ_BookI [M³] = energy/area of the brane-defect   │
│   Method: Plenum field σ in EDC 5D action (P1-P4)          │
│   Current status: [P] (postulated as 8.82 MeV/fm²)         │
│   If successful: Promotes ~40 nuclear claims from [P] to    │
│   [Dc] (highest multiplier in entire EDC program)           │
│                                                             │
│   Key advantage: σ_BookI is now CLEANLY SEPARATED from      │
│   σ_covariant. The derivation target is precise:            │
│   derive the [M³] nuclear surface tension from the          │
│   Plenum field energy density on the brane-defect.          │
│                                                             │
│   Why not Rξ: Rξ uses M_Z [BL] but is a single parameter   │
│   used as identification, not a structural postulate.       │
│   σ_BookI is used as structural input in ~40 claims.        │
│                                                             │
│   Why not V(q): V(q) derivation (Phase 2 Lane B) requires  │
│   σ_BookI as input. Deriving σ_BookI first feeds into V(q)  │
│   and amplifies its value.                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Concrete next steps for σ_BookI derivation:

1. **Clarify the Plenum field action.** What is the EDC 5D action term
   that produces the brane defect? Is it S_Plenum = ∫d⁵x √(-G) ρ_P?

2. **Compute energy per unit area.** Integrate the Plenum energy density
   across the extra dimension on the brane defect: σ_BookI = ∫dξ ρ_P(ξ).

3. **Express in terms of EDC axioms.** Can ρ_P be related to P1–P4
   parameters (M₅, Rξ, ℓ)?

4. **Compare with postulated value.** σ_BookI = 8.82 MeV/fm² is the
   target. If the derived value matches, ~40 claims are promoted.
   If it doesn't, the discrepancy is a meaningful result.

5. **Cross-check with σ_covariant.** Verify that the relationship
   between σ_BookI [M³] and σ_covariant [M⁴] is σ_covariant = σ_BookI · L_char
   where L_char is a characteristic length (possibly ℓ or Rξ).

### Fallback if σ_BookI derivation is blocked:

If the Plenum field structure is insufficiently defined in current EDC
axioms, the fallback priority is:

**Rξ from 5D diffusion equation** — deriving the correlation length
from the diffusion dynamics in the EDC geometry, without M_Z input.
This would promote Rξ from [I+BL] to [Dc] and feed into all particle
mass formulas.

---

## 7. Summary: What the σ̃ Audit Accomplished

| Before audit | After audit |
|-------------|-------------|
| σ̃ = 100 ± 10 (v67) | σ̃ = 1 + O(10⁻⁵⁶) |
| σ_BookI and σ_covariant conflated | Cleanly separated: [M³] ≠ [M⁴] |
| α₃ = 1/σ̃ (derivable) | α₃ from free g₅^(C) (measurement input) |
| OPR-31 OPEN (enhancement needed) | OPR-31 CLOSED (MOOT) |
| g₅ potentially derivable | g₅ proven irreducible (OPR-32) |
| Gravitational sector: partially open | Gravitational sector: fully closed |
| Nuclear sector: entangled with cosmological | Nuclear sector: independent, clearly defined |
| 3 SM gauge couplings | 1 free parameter via PS hook |
| Parameter closure plan: 3 lines active | LINE 1 gravitational: CLOSED; LINE 2 simplified; LINE 3 clarified |

The audit transformed the parameter closure landscape from a confused
tangle of σ definitions into two clean, independent subnetworks. The
gravitational side is done. The nuclear side (σ_BookI, Rξ) is the
remaining frontier, with σ_BookI from Plenum as the highest-value target.
