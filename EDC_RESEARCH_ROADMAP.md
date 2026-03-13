# EDC Research Roadmap: Prioritized Directions

**Date**: 2026-03-13
**Governing document**: EDC_GLOBAL_GUARDS.md
**Principle**: Derive from S_EDC. Verify against measurements. Never import SM.

---

## Strategic Assessment

EDC has five strong pillars (α, m_p/m_e, τ_n, sin²θ_W, coordination structure).
The theory's credibility now depends on:

1. **Closing derivation gaps** — promoting [P] and [Cal] to [Dc] or [Der]
2. **Generating discriminating predictions** — where EDC differs from all other approaches
3. **Strengthening the weakest link** — L₀/δ = π² and the BVP

The roadmap is ordered by **impact × feasibility**. High-impact items that
are tractable with current tools come first.

---

## TIER 1: CLOSE FIRST (Highest Priority)

These items have the greatest impact on theory credibility and are tractable
within the existing mathematical framework.

---

### R1. L₀/δ = π² — The Keystone Derivation

**Current status**: [P] (geometric hypothesis)
**Target**: [Dc] or [Der]
**Blocks**: τ_n robustness, α correction, generation count

**Why first**: This single ratio appears in:
- τ_n exponent: S_E/ℏ = 2π × (L₀/δ)
- α correction path (OPR-01)
- Mode spectrum structure

If L₀/δ = π² falls, τ_n falls. If it's derived, τ_n becomes a genuine prediction.

**Approach (EDC-native)**:

1. **Variational principle on the 5D action**: Minimize S_EDC with respect to
   brane separation L₀ at fixed brane thickness δ.

   The 5D energy functional includes:
   - Bulk energy: ∝ ρ_Plenum × Volume(bulk)
   - Brane tension: ∝ σ × Area(brane)
   - Boundary (GHY + Israel): junction conditions at brane surfaces

   The equilibrium separation L₀ is where dE/dL₀ = 0.

2. **Dimensional analysis check**: L₀/δ must be a pure number arising from
   geometry. Candidate origins:
   - Ratio of brane curvature to thickness → involves π
   - Eigenvalue of Laplacian on compact dimension → π² appears naturally
   - Steiner angle constraint propagated to 5th dimension

3. **Sturm-Liouville connection**: If the compact dimension has Dirichlet-like
   conditions, the ground-state eigenvalue is π²/L². This gives L₀/δ = π²
   if the eigenvalue condition fixes the scale ratio.

**Deliverable**: A derivation chain from S_EDC → boundary conditions → eigenvalue equation → L₀/δ = π² with stated assumptions.

**Verification**: Python script computing L₀/δ from the 5D action numerically.

**Falsification**: If the variational principle gives L₀/δ ≠ π², compute the
implied τ_n and compare to measurement. If the deviation is > 10%, the
geometric hypothesis needs revision.

---

### R2. Prefactor A from Fluctuation Determinant

**Current status**: [Cal] (A ≈ 0.9, fitted)
**Target**: [Dc]
**Blocks**: τ_n precision, anti-tuning credibility

**Why important**: Although A enters linearly (not exponentially), having it
derived eliminates the only calibrated component of the τ_n prediction.

**Approach (EDC-native)**:

1. **Explicit bounce solution**: Solve the Euclidean EOM for the double-well
   V(q) established in Book IV Ch. 3.

2. **Fluctuation operator**: Construct -∂²_τ + V''(q_B(τ)) around the bounce.

3. **Determinant ratio**: Compute
   ```
   A = √(S_E / 2πℏ) × |det'(-∂² + V''_bounce) / det(-∂² + ω₀²)|^(-1/2)
   ```

4. **Numerical evaluation**: Implement in Python. Expected: A = O(1).

**Deliverable**: Python script computing A from V(q) parameters. If A ≈ 0.9
emerges naturally, promote to [Dc].

**Anti-tuning check**: Verify that A ∈ [0.5, 2.0] for all reasonable V(q) shapes.

---

### R3. Double-Well V(q) from 5D Action

**Current status**: [P] (postulated shape)
**Target**: [Dc]
**Blocks**: Instanton derivation, prefactor A, τ_n

**Approach (EDC-native)**:

1. **5D → 1D reduction**: Start from S_EDC. Identify the collective coordinate q
   (reaction coordinate between anchor and metastable configurations).

2. **Adiabatic integration**: Integrate out fast modes (transverse fluctuations,
   shape modes) to obtain V_eff(q).

3. **Required structure**: V(q) must have:
   - Global minimum at q = 0 (anchor, Z₆)
   - Local minimum at q = q_n (metastable, Z₃)
   - Barrier at q = q_B with V_B = 2Δm (from energy conservation)

4. **Barrier height**: Currently V_B = 2Δm_np ≈ 2.59 MeV [P]. Must derive
   from the 5D potential landscape.

**Deliverable**: Explicit V(q) with coefficients traced to σ, δ, L₀.

---

### R4. N_bonds = 3 for A=2 Cluster (Deuterium)

**Current status**: [P]
**Target**: [Der]
**Blocks**: Deuterium binding derivation

**Approach (EDC-native)**:

1. **Junction topology**: Two junctions (anchor + metastable) share bonds.
   The Y-junction geometry gives each junction 3 legs.

2. **Contact graph**: When two Y-junctions approach, each leg of junction 1
   can bond with one leg of junction 2. Maximum bonds = 3 (not 6, because
   each leg bonds to exactly one partner).

3. **Energy minimization**: Show that the 3-bond configuration minimizes
   the total energy (brane tension + contact curvature).

**Deliverable**: Topological proof that N_bonds(A=2) = 3 from Y-junction geometry.

---

## TIER 2: STRENGTHEN (High Priority)

These items strengthen existing results and extend the theory's reach.

---

### R5. Closed-4 Surface and Closure Terms

**Current status**: [P]+[OPEN]
**Target**: [Dc]
**Impact**: He-4 binding budget (currently 4 terms, 2 are [P])

**Approach**: Variational principle on the M₆ lattice for the 4-junction
cluster. The surface term measures boundary reduction when 4 junctions merge.
The closure term measures flux cancellation in the complete K₄ graph.

**Key question**: Can the surface and closure terms be computed from σ and
the contact geometry alone?

---

### R6. Frustration Coefficient g — Sign and Magnitude

**Current status**: [P]+[Cal] (g < 0 postulated, magnitude fitted)
**Target**: [Dc]
**Impact**: Release systematics, high-coordination predictions

**Approach (EDC-native)**:

1. **Frustration mechanism**: When n(A) ∉ S = {2ᵃ×3ᵇ}, the cluster has
   geometric stress. This stress can either:
   - Enhance preformation (lower effective barrier) → g < 0
   - Reduce barrier (direct geometric effect) → g < 0

2. **From 5D**: The frustration distance d(n) measures deviation from
   Z₆-compatible coordination. The energy cost of frustration must be
   derivable from the M₆ lattice deformation energy.

3. **Prediction**: If g is derived from σ and lattice geometry, the
   corrected release times become parameter-free predictions.

---

### R7. A=3 Cluster (Triangular Binding)

**Current status**: [OPEN]
**Target**: [Dc]
**Impact**: Light cluster systematics

**Approach**: Three junctions in triangular configuration. Expected:
N_bonds = 3 (ring topology). Binding = 3K ≈ 2.2 MeV. But triangular
symmetry (Z₃) may introduce additional effects vs. linear A=2.

---

### R8. Coordination Function p from 5D

**Current status**: [Cal] (p fitted in n(A) = p·A^(1/3))
**Target**: [Dc]
**Impact**: Removes calibration from release systematics

**Approach**: The coordination function n(A) = p·A^(1/3) comes from
packing geometry. The exponent 1/3 is the volume-to-surface scaling
(dimensional). The prefactor p should emerge from M₆ lattice geometry:
how many neighbors does a junction have in a cluster of A junctions?

---

## TIER 3: EXTEND (Medium Priority)

These open new sectors of the theory.

---

### R9. BVP Closure — V_eff(ξ) Shape

**Current status**: OPR-21, shape-dependent
**Target**: Unique V_eff(ξ) from S_EDC
**Impact**: 3-generation proof, mass spectrum, α correction

**The challenge**: The boundary value problem in the compact ξ-direction:
```
−ψ″(ξ) + V(ξ)ψ(ξ) = μψ(ξ),   ξ ∈ [0, R_ξ]
```

The potential V(ξ) must be derived from S_EDC. Currently, different shapes
give different generation counts:
- Generic well: μ₃ ∈ [25, 35)
- Domain-wall: μ₃ ∈ [13, 17]

**Approach**: Start from S_EDC, perform KK reduction, identify the effective
potential in the compact dimension. The shape of V(ξ) is not a choice —
it must follow from the 5D dynamics.

**Why Tier 3**: This is the hardest problem. It requires the full 5D action
reduction, which depends on solving the bulk equations of motion. But the
payoff is enormous: closing OPR-21 unlocks the mass spectrum.

---

### R10. ω₀ (Attempt Frequency) from 5D Junction Dynamics

**Current status**: [P] (dimensional estimate, ω₀ ~ 19 MeV)
**Target**: [Dc]
**Impact**: τ_n precision

**Approach**: The oscillation frequency at the metastable minimum is:
```
ω₀ = √(V''(q_n) / M)
```

Once V(q) (R3) and M(q) (effective mass from 5D kinetic terms) are derived,
ω₀ follows automatically.

**Note**: This depends on R3, so it cannot be closed independently.

---

### R11. Lepton Mass Spectrum from Mode Profiles

**Current status**: [P] candidates, OPR-20
**Target**: [Dc]
**Impact**: m_e, m_μ, m_τ ratios

**Approach (EDC-native)**: Lepton masses come from S¹-loop mode profiles
on the brane. Different winding numbers give different masses.

**Depends on**: R9 (BVP closure for mode spectrum)

---

### R12. CP Violation from Z₆ Orientation

**Current status**: Attempt (OPR-05)
**Target**: [Dc]
**Impact**: Explanation of matter-brane asymmetry

**Approach**: Z₆ has an orientation (clockwise vs. counterclockwise).
The brane may prefer one orientation, breaking C and CP. The CP-violating
phase should emerge from the relative orientation of Z₆ patches.

---

## TIER 4: FRONTIER (Future Directions)

---

### R13. Dark Matter as Bulk Mode

**Current status**: Speculative (OPR-10)
**Approach**: If the 5D bulk supports stable modes that couple gravitationally
but not electromagnetically to the brane, these are dark matter candidates.
The bulk mode spectrum depends on ρ_Plenum and the bulk geometry.

### R14. Cosmological Constant from ρ_Plenum Vacuum

**Current status**: Open (OPR-11)
**Approach**: The cosmological constant might emerge as the residual energy
density of the 5D Plenum after brane formation. This requires understanding
the Plenum equation of state.

### R15. Gravitational Wave Signatures

**Current status**: Not yet explored
**Approach**: 5D brane dynamics may produce distinctive gravitational wave
signatures (e.g., from brane oscillation modes). These could provide
discriminating predictions testable by LISA or future detectors.

### R16. Boundary Reconfiguration Dynamics

**Current status**: OPEN (Book IV)
**Approach**: Beyond the scalar frustration d(n), clusters may undergo
topological transitions (boundary reconfigurations) not captured by the
current coordination model.

---

## Recommended Execution Order

```
PHASE 1 (Immediate — 5D Action Analysis)
├── R1: L₀/δ = π² derivation     ← HIGHEST PRIORITY
├── R3: V(q) from 5D action       ← enables R2
└── R4: N_bonds = 3 proof         ← quick win

PHASE 2 (Near-term — Prefactor and Binding)
├── R2: Prefactor A (needs R3)
├── R5: Closed-4 terms
├── R7: A=3 binding
└── R8: Coordination p from 5D

PHASE 3 (Medium-term — Extensions)
├── R6: Frustration g derivation
├── R10: ω₀ from 5D (needs R3)
└── R9: BVP closure (hardest)

PHASE 4 (Long-term — New Physics)
├── R11: Lepton masses (needs R9)
├── R12: CP violation
├── R13: Dark matter
├── R14: Cosmological constant
└── R15: GW signatures
```

---

## Decision Matrix

| Item | Impact | Feasibility | Risk | Priority Score |
|------|--------|-------------|------|---------------|
| R1: L₀/δ = π² | 10 | 6 | Medium | **60** |
| R4: N_bonds = 3 | 5 | 9 | Low | **45** |
| R3: V(q) from 5D | 9 | 5 | High | **45** |
| R2: Prefactor A | 6 | 7 | Low | **42** |
| R5: Closed-4 terms | 6 | 6 | Medium | **36** |
| R8: Coordination p | 5 | 7 | Low | **35** |
| R6: Frustration g | 7 | 5 | Medium | **35** |
| R7: A=3 binding | 4 | 8 | Low | **32** |
| R9: BVP closure | 10 | 3 | High | **30** |
| R10: ω₀ | 4 | 5 | Medium | **20** |
| R11: Lepton masses | 8 | 2 | High | **16** |
| R12: CP violation | 7 | 2 | High | **14** |

**Score = Impact × Feasibility / (1 + Risk_penalty)**

---

## What NOT To Do

1. **Do not import SM results** to "shortcut" any derivation
2. **Do not calibrate** more parameters — reduce the [Cal] count
3. **Do not attempt** BVP closure (R9) before V(q) (R3) is understood
4. **Do not write** new chapters before closing open problems in existing ones
5. **Do not compare** to SM predictions — compare to measurements
6. **Do not publish** without discriminating predictions (R15-type)

---

## Success Criteria

The theory achieves **publishable status** when:

- [ ] L₀/δ = π² derived [P → Der/Dc]
- [ ] Prefactor A derived [Cal → Dc]
- [ ] τ_n prediction has zero calibrated inputs
- [ ] At least one discriminating prediction identified
- [ ] All Layer A text passes contamination scan
- [ ] Sensitivity analysis complete for all key results
- [ ] Falsifiability conditions stated for all pillars

---

*Roadmap version 1.0. Updated upon closure of any item.*
