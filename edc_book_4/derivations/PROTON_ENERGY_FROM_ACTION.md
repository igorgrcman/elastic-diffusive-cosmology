# Proton Elastic Energy from 5D Membrane Action — Prove or Fail

**Date:** 2026-03-16
**Branch:** `claude/analyze-codebase-KKY9n`
**Prerequisite:** `ALPHA_CORRECT_DERIVATION.md` (commit ab87706) — PARTIAL verdict
identified upgrade condition: "Derive the proton's elastic energy from the 5D
membrane action → closes all four gaps."

**Mission:** Derive m_p c² = (4π + 5/6) σ_eff r_e² from the 5D action.
If successful: 5/6 origin revealed, σ_eff derived, α formula upgraded to [Der].

---

## 1. Executive Verdict: FAIL

The proton energy **cannot be derived** from the 5D membrane action (Nambu-Goto
or otherwise). Three independent routes were attempted; all fail at the same
structural point: the bridge between the physical action (which gives string
energy E = τ × length) and the configuration-space volume formula
(which gives E ∝ (2π²)³) is a **postulate**, not a derivation.

| Route | What it gives | What is needed | Gap |
|-------|---------------|----------------|-----|
| A: Nambu-Goto action | E = 3τL (linear string) | E ∝ (2π²)³ | Mass-measure [P] |
| B: Config-space volume | mp/me = 6π⁵ (ratio only) | Absolute m_p | σ_eff needed [Cal] |
| C: Chapter 4 ansatz | m_p = (4π+5/6) σ r_e² | Independent σ | σ from α [circular] |

**The irreducible postulate** is the Mass-Measure Identification (Companion F,
box at line 162): m ∝ C (configuration-space volume). This cannot be derived
from the Nambu-Goto action, from the 5D Einstein-Hilbert action, or from any
known principle. It is a foundational postulate [P] of the EDC framework.

**Consequence:** The α formula α = (4π + 5/6)/(6π⁵) retains its PARTIAL
status from `ALPHA_CORRECT_DERIVATION.md`. The upgrade condition cannot be
satisfied within the current EDC formalism.

---

## 2. Y-Junction Setup

### The Proton in EDC

The proton is a Y-junction of three flux tubes (Companion F, Postulate 1):

```
         Q₂
          \  τ
           \  120°
     P ─────── Q₁      (Steiner configuration)
           /  τ
          /  120°
         Q₃
```

Each arm carries:
- Tension τ (energy/length)
- Direction t̂_i (unit tangent at junction P)
- Flux quantum (color charge)

The Nambu-Goto action (Companion F, Definition 4.3):

```
S_junction = -Σ τᵢ ∫ d²ξ √(-det(γᵢ))
```

In static limit:

```
E_junction = Σ τᵢ ℓᵢ = 3τL    (equal tensions, 3 arms of length L)
```

### What the Action Derives [Der]

From Companion F:
1. Force balance: Σ τᵢ t̂ᵢ = 0 at equilibrium [Der]
2. Equal tensions → 120° Steiner angles [Der]
3. Lami's theorem for unequal tensions [Der]
4. Angle preservation under brane projection [Dc]

### What the Action Does NOT Derive

The action gives E = 3τL (total string length × tension). This is:
- **Linear** in arm length L
- **Proportional** to τ (string tension, E/L)
- **Independent** of any angular integration factor like (2π²)³

The configuration-space volume (2π²)³ = Vol(S³ × S³ × S³) does NOT appear
anywhere in the Nambu-Goto action or its equations of motion.

---

## 3. Flux Tube Tension from Membrane Action

### τ from σ_eff

The relation between string tension τ (E/L) and membrane tension σ (E/L²):

```
τ = σ × (cross-sectional size)
```

Two candidate cross-sections:

| Model | τ formula | τ value | E = 3τr_e |
|-------|-----------|---------|-----------|
| Compact wrap: τ = σ × 2πRξ | σ × 2π × 0.00216 fm | 0.120 MeV/fm | 1.01 MeV |
| EM scale: τ = σ × r_e | σ × 2.818 fm | 24.85 MeV/fm | 210 MeV |

Neither gives m_p = 938.3 MeV:

```
Model A (compact wrap):  E = 1.01 MeV     → off by 928×
Model B (EM scale):      E = 210 MeV      → off by 4.5×
Target:                  m_p = 938.3 MeV
```

### The Scale Mismatch

The Nambu-Goto energy E = 3τL is fundamentally a **string** quantity. It
depends on τ (tension) and L (length) — two one-dimensional quantities.
There is no mechanism within the string action to generate the factor
(2π²)³ ≈ 779.3, which is a **9-dimensional volume** (three copies of
Vol(S³) = 2π²).

This is because the Nambu-Goto action describes a physical string sweeping
out a 2D worldsheet. The (2π²)³ factor comes from the **configuration space**
of internal orientations — a completely different mathematical object.

---

## 4. Y-Junction Energy Calculation

### Route A: Nambu-Goto (Physical Action) → FAILS

```
E_p = 3τL

Ingredients:
  τ = σ_eff × a    (flux tube cross-section a)
  L = r_e           (arm length ~ electron radius)

E_p = 3 × σ_eff × a × r_e

For mp/me = 6π⁵:
  mp/me = E_p/E_e = (3 × σ_eff × a × r_e) / (α × σ_eff × r_e²)
        = 3a / (α × r_e)

  → a = α × r_e × 6π⁵ / 3 = (1/137) × 2.818 × 612 = 12.6 fm

This requires the flux tube cross-section a ≈ 12.6 fm ≈ 4.5 × r_e.
This is physically unreasonable — the flux tube would be wider than
the junction itself.
```

**Verdict:** The Nambu-Goto action cannot reproduce mp/me = 6π⁵ with
physically reasonable parameters.

### Route B: Configuration-Space Volume (Paper 2) → WORKS for ratio only

```
m ∝ C (configuration-space volume)              [P — postulated]

C_e = Vol(B³) = 4π/3                            [Der]
C_p = Vol(S³ × S³ × S³) = (2π²)³              [Dc]

mp/me = C_p/C_e = (2π²)³ / (4π/3) = 6π⁵       [Der — algebraic identity]
```

But this gives only the **ratio**, not absolute masses. The proportionality
constant is unknown. Paper 2 line 1090 states: "For characteristic scales
where τL² ~ σa³" — this equality is **assumed**, not derived.

Numerically, E = σ × C × r_e³ gives:

```
E_e = σ × (4π/3) × r_e³ = 8.818 × 4.189 × 22.37 = 826.6 MeV
E_p = σ × (2π²)³ × r_e³ = 1,517,687 MeV

E_e/m_e = 1618     (off by factor 1618)
E_p/m_p = 1618     (off by same factor)
E_p/E_e = 6π⁵      (ratio exact ✓)
```

The factor of 1618 is absorbed into the unknown proportionality constant.
Without fixing this constant, no absolute prediction is possible.

### Route C: Chapter 4 Ansatz → WORKS but circular

```
m_e c² = α × σ_eff × r_e²                     [Identity — defines α]
m_p c² = (4π + 5/6) × σ_eff × r_e²            [P — ansatz]

m_e = (1/137.036) × 8.818 × 7.941 = 0.511 MeV ✓
m_p = 13.400 × 8.818 × 7.941 = 938.3 MeV      ✓
```

Both values agree because σ_eff was **extracted from α**. This is
circular: σ_eff = m_e c²/(α r_e²) by definition.

---

## 5. The 5/6 Factor — Does It Emerge from the Action?

### Short Answer: No

The Nambu-Goto action for the Y-junction produces:
- 120° angles [Der]
- Force balance Σ τᵢ t̂ᵢ = 0 [Der]
- Coplanarity of junction [Der]
- Dimension counting: dim(constraint manifold) = 4 on base [Dc]

**None of these produce 5/6.**

### Dimension Counting (Companion F, lines 778-785)

```
dim(S² × S² × S²) = 6         (three arm directions)
Constraints: Σ t̂ᵢ = 0 → -2    (vector constraint in 2D plane)
dim(Σ_base) = 4                (constrained base manifold)
Fiber: S¹ × S¹ × S¹ → +3      (internal phases)
dim(total) = 7
```

After quotienting by SO(3) global rotation: dim = 7 - 3 = 4 physical DOF.

This gives the dimension count (4, 6, 7) but NOT the ratio 5/6.

### Attempting to Extract 5/6 from Junction Geometry

**Attempt 1: Constrained/total base DOF**

```
Constrained DOF / Total DOF = 4/6 = 2/3     (NOT 5/6)
```

**Attempt 2: With fiber**

```
Physical DOF / Total unconstrained = 4/7     (NOT 5/6)
(Total - 1) / Total = 6/7                    (NOT 5/6)
```

**Attempt 3: Face counting (Chapter 5 heuristic)**

```
"Cubic topology": 6 faces, 1 used for closure → 5/6
```

This argument (Chapter 5, lines 537-544) is not connected to the Nambu-Goto
action. It is a heuristic: "3 orthogonal strands define a cubic topology with
6 degrees of freedom (like the 6 faces of a cube)." But why cubic? The
Y-junction at 120° is **not** cubic (120° ≠ 90°). The cube has nothing to
do with the Steiner configuration.

**Attempt 4: Phase space argument (Paper 2)**

```
"6 DOF in phase space (3 position + 3 momentum)" → (6-1)/6 = 5/6
```

This is the standard non-relativistic phase space dimension. But the
membrane is 3D (not 2D), so confinement TO the membrane doesn't obviously
remove exactly 1 DOF. A particle on a 3D membrane has 3 position + 3
momentum = 6 phase-space DOF, same as a free particle in 3D. Confinement
to the membrane removes the fifth-dimension DOF — but that would give
(4+4-1)/(4+4) = 7/8, not 5/6, starting from a 4D spatial + 4D momentum
phase space.

**Attempt 5: Steiner angle connection**

```
cos(120°) = -1/2
1 + cos(120°) = 1/2
3 × (1 + cos(120°)) / 3 = 1/2
```

No natural combination of 120° angles produces 5/6.

### Verdict on 5/6

The 5/6 factor does **not** emerge from:
- The Nambu-Goto action
- The Y-junction variational principle
- The dimension counting of the constraint manifold
- The Steiner angle geometry
- Any rigorous argument in the EDC corpus

It remains **[P]** (postulated) with two independent heuristic motivations
that are both questionable under scrutiny.

---

## 6. σ_eff from Action (Non-Circular)

### Previously Established: FAIL

`SIGMA_BOOKL_FROM_PLENUM.md` (same date) already established:

```
σ_BookI CANNOT be derived from the 5D EDC action.

Route P1 (bulk Λ₅):  off by 10⁴¹
Route P2 (Casimir):   off by 10⁴
Route P3 (back-reaction): wrong dimensions
```

**Root cause:** σ_BookI ≈ 8.82 MeV/fm² is a nuclear-scale quantity. The 5D
gravitational action operates at M₅ ~ 10¹² GeV. No mechanism bridges 40
orders of magnitude. This is a variant of the hierarchy problem.

### Implication for This Derivation

Since σ_eff cannot be independently derived, any formula using σ_eff to
compute absolute masses (m_e, m_p) is circular — σ_eff is defined by
those same masses.

The configuration-space route (Route B) avoids this by computing only the
**ratio** mp/me = 6π⁵, where σ_eff cancels. But absolute masses and α
require σ_eff, which requires α. The circle cannot be broken within the
current framework.

---

## 7. Consistency Check: mp/me = 6π⁵?

### From Paper 2 (Configuration-Space Volume)

```
mp/me = C_p/C_e = (2π²)³ / (4π/3) = 6π⁵ = 1836.118
CODATA: mp/me = 1836.153
Error: 0.0019%
```

This works. The ratio is geometrically determined and does not depend
on σ_eff, τ, or any dimensional parameter. **Status: [Der]** (given the
Mass-Measure postulate and the topological identifications).

### From Chapter 4 (Ansatz)

```
mp/me = (4π + 5/6)/α

Using α_CODATA: (4π + 5/6) × 137.036 = 1836.242
CODATA: 1836.153
Error: 0.0049%
```

This also works but with larger error. The two predictions are
**incompatible** at the 0.007% level:

```
Paper 2:   mp/me = 6π⁵ = 1836.118
Chapter 4: mp/me = (4π + 5/6)/α_CODATA = 1836.242
Difference: 0.124 (0.0067%)
```

This is the same 0.0067% discrepancy seen in the α formula.

### From Nambu-Goto (Physical Action)

```
mp/me = E_p/E_e = 3τL / (α σ r_e²)
```

This involves τ, L, σ, r_e — four parameters. Without an independent
determination of τ and L, no prediction is possible.

**The Nambu-Goto action does not predict mp/me = 6π⁵.**

---

## 8. Epistemic Status Table

| Step | Content | Tag | Source |
|------|---------|-----|--------|
| **Postulates** | | | |
| P1 | Universe = 3D membrane in 5D bulk | [P] | EDC axiom |
| P2 | Particles = frozen defects | [P] | EDC axiom |
| P3 | Baryon = 3-arm flux-tube junction | [P] | Companion F, Post. 1 |
| P4 | Mass ∝ config-space volume (m ∝ C) | [P] | Companion F, box line 162 |
| P5 | Arm internal S¹ phase (Hopf structure) | [P] | Companion F, Post. 4 |
| | | | |
| **Derivations** | | | |
| D1 | Force balance: Σ τᵢ t̂ᵢ = 0 | [Der] | Companion F, Thm 4.1 |
| D2 | Equal tensions → 120° Steiner angles | [Der] | Companion F, Thm 4.2 |
| D3 | C_e = Vol(B³) = 4π/3 | [Der] | Paper 2 §5 |
| D4 | C_p = Vol(S³)³ = (2π²)³ | [Dc] | Companion F, Thm 6.3 |
| D5 | mp/me = C_p/C_e = 6π⁵ | [Der] | Paper 2 §7, algebraic |
| | | | |
| **Gaps** | | | |
| G1 | Mass-measure: m ∝ C | [P] | NOT from action |
| G2 | τL² ~ σa³ (dimensional matching) | [P] | Paper 2 line 1090 |
| G3 | 5/6 = (6-1)/6 DOF factor | [P] | Paper 2 §8, Ch 5 §5 |
| G4 | σ_eff = 8.82 MeV/fm² | [Cal] | From α (circular) |
| G5 | α = (4π+5/6)/(6π⁵) structure | [P] | Ch 4 ansatz |
| | | | |
| **Failed attempts** | | | |
| F1 | σ_eff from bulk Λ₅ | FAIL | 10⁴¹× off |
| F2 | σ_eff from Casimir | FAIL | 10⁴× off |
| F3 | E_p from Nambu-Goto | FAIL | Gives E=3τL, not (2π²)³ |
| F4 | 5/6 from junction dimension counting | FAIL | Gives 4/6=2/3, not 5/6 |
| F5 | 5/6 from Steiner angles | FAIL | No natural 5/6 combination |

---

## 9. What Remains Open — New OPR

### OPR-NEW: Mass-Measure Identification

**The central open problem is P4: m ∝ C (mass proportional to
configuration-space volume).**

This is the most important postulate in the EDC particle sector.
Without it, the geometric factors (4π/3, (2π²)³, 6π⁵) have no
connection to physical masses.

**What would a derivation look like?**

It would need to show that the partition function (or energy functional)
of a frozen defect is:

```
Z_defect ∝ ∫_C dμ × exp(-S[φ])
```

where C is the configuration space and the integral over C (with
appropriate measure dμ) produces a factor proportional to Vol(C).
The mass would then arise as:

```
m c² = σ_eff r_e² × Vol(C) × f(boundary)
```

from saddle-point or adiabatic evaluation of Z.

**Key difficulty:** Standard quantum field theory gives
Z ∝ exp(-Vol × energy_density), where Vol is the **physical** volume,
not the configuration-space volume. The identification of mass with
configuration-space volume (rather than physical volume) is the
non-standard step that defines EDC's particle physics.

### OPR-EXISTING: 5/6 Factor

Remains [P]. No derivation from action exists or was found.

The two heuristic arguments (phase space DOF, cubic topology) are
inconsistent with each other and with the actual junction geometry:
- Phase space: Why exactly 1 DOF removed from 6? The membrane is 3D.
- Cubic: The 120° Steiner junction is NOT cubic (120° ≠ 90°).

**Internal inconsistency remains:** Chapter 4 says "key open task" to
derive κ₃q, Chapter 5 claims "SOLVED." Paper 2 tags it [P].

### OPR-EXISTING: σ_eff Independence

Remains blocked. `SIGMA_BOOKL_FROM_PLENUM.md` established FAIL.
σ_eff = m_e c²/(α r_e²) is the only determination available.

---

## 10. The Incompatibility Between Action and Config-Space Routes

### The Deep Problem

EDC has two descriptions of the proton that give **different physics**:

**Description 1: Physical (Nambu-Goto)**
```
S = -Σ τ ∫ d²ξ √(-det(γ))
E_proton = 3τL
```
- Energy is proportional to string LENGTH
- Junction angles are 120° [Der]
- No (2π²)³ factor appears anywhere
- Absolute energy depends on τ and L

**Description 2: Geometric (Config-Space Volume)**
```
m ∝ C = Vol(configuration space)
m_p/m_e = (2π²)³ / (4π/3) = 6π⁵
```
- Mass is proportional to configuration-space VOLUME
- The factor (2π²)³ = Vol(SU(2)³) comes from orientation counting
- Only the ratio is determined; absolute mass requires σ_eff
- The 6π⁵ result has 0.0019% agreement with experiment

These descriptions are **not derivable from each other.** The Nambu-Goto
action gives the string energy, not the configuration-space volume. The
configuration-space volume gives the mass ratio, not the string energy.

The bridge between them — the Mass-Measure Identification (m ∝ C) — is
the foundational postulate [P] that makes EDC's particle physics work.
It is not derived from any action principle.

### Is This a Bug or a Feature?

In standard physics, similar situations arise:
- Microcanonical entropy S = k ln Ω (mass of states) is a postulate
- The path integral ∫ Dφ e^{iS} is a postulate
- AdS/CFT duality (bulk gravity ↔ boundary CFT) is a conjecture

EDC's m ∝ C could be analogous — a new principle relating physical
energy to geometric state-counting. But until it is either:
(a) derived from a deeper principle, or
(b) confirmed by independent experimental prediction,
it remains [P].

---

## 11. Bottom Line

**Verdict: FAIL**

The proton elastic energy **cannot be derived** from the 5D membrane action.
The Nambu-Goto action gives E = 3τL (string energy), which is incompatible
with the configuration-space volume formula mp ∝ (2π²)³ that produces the
remarkable 6π⁵ mass ratio.

The bridge between physical action and geometric mass formula is the
**Mass-Measure Identification** (m ∝ C), which is:
- Postulated [P] in Companion F
- Not derivable from Nambu-Goto or Einstein-Hilbert actions
- The deepest foundational assumption in EDC particle physics

**Consequences for α formula:**

1. The upgrade condition from `ALPHA_CORRECT_DERIVATION.md` **cannot be met.**
2. α = (4π + 5/6)/(6π⁵) retains status **[Dc]** — derived conditional on:
   - Mass-Measure Identification [P]
   - 5/6 DOF factor [P]
   - Proton energy ansatz [P]
3. σ_eff remains [Cal] (extracted from α, not independently derived)

**What EDC has genuinely derived:**
- 120° Steiner angles from energy minimization [Der]
- C_p = (2π²)³ from SU(2)³ Hopf bridge [Dc, given arm structure postulate]
- mp/me = 6π⁵ as algebraic identity [Der]
- The 6π⁵ = 1836.118 agreement with CODATA mp/me = 1836.153 (0.0019%)

**What EDC has NOT derived:**
- WHY mass is proportional to configuration-space volume
- WHERE the 5/6 factor comes from
- HOW σ_eff is determined independently of α
- WHY α = (4π + 5/6)/(6π⁵) has this specific structure
