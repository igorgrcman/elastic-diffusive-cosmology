# Book IV: TODO Obligations

**Document:** Canonical TODO list for EDC Book IV
**Date:** 2026-02-10
**Status:** Active

---

## Critical Open Items

### 1. Closed-4 Minimality Proof

**Obligation:** Formally prove that the closed-4 unit is the minimal closed
topological configuration in the M₆ lattice, and that this explains the
release bias observed in high-coordination clusters.

**Current Status:** ✅ [RESOLVED] — Theorem~11.6 in Ch. 11 §11.7

**Resolution Details:**
- **Theorem 11.6 (Closed-4 Minimality):** Proves A=4 is minimal via lemma chain
- **5 Lemmas:** No closed-1, no closed-2, no closed-3, closed-4 exists, closed-4 unique
- **Corollary 11.7:** Establishes Closed-4 Release Bias from theorem
- **Definitions:** Junction network, closure invariant, closed-k unit (all [Def])
- **All proofs:** [Der] — purely combinatorial/topological

**Remaining extensions (low priority):**
- Prove closure definition is "canonical" (currently [Def] not [Der])
- Derive localization dominance rigorously in corollary (currently uses [P] estimate)

**No longer blocking:** Ch. 11, Ch. 13–15 now reference theorem

---

### 2. Naming/Ontology Enforcement Across Books

**Obligation:** Establish naming convention and macro usage as a shared
standard for the entire 5-book series, not just Book IV.

**Current Status:** [PARTIAL]
- Book IV has `ontology/EDC_ONTOLOGY_CANON.md` and preamble macros
- Book II has partial adoption
- Books I, III, V need alignment

**Where to resolve:**
- `edc_papers/_shared/ontology/` — cross-book canonical document
- Each book imports shared macros via `\input{../_shared/preamble_macros}`

**Components:**
1. **Macro set:** `\AnchorJunction`, `\MetastableJunction`, `\ClosedFour`, etc.
2. **Banlist:** CONTAMINATION_GUARD propagated to all books
3. **Observerbox:** Each book adopts observerbox pattern for 5D↔observer mapping
4. **Audit hook:** CI/CD check for macro usage and contamination

---

## Secondary Open Items

### 3. "One Unit Per Arm = Δm_np" Derivation (Z₃ Barrier)

**Obligation:** Prove that each Y-junction arm contributes exactly Δm_np to the
barrier energy, establishing V(q_B) = 3 × Δm_np and thus V_B = 2 × Δm_np.

**Current Status:** [OPEN] — Conjecture based on Z₃ symmetry argument

**What needs to be shown:**
1. Derive explicit V(q) from 5D action (Put C corridor)
2. Prove V(q_B) = 3 × Δm_np at the saddle point
3. Identify geometric origin of the energy unit Δm_np

**Key source documents:**
- `edc_book_2/src/derivations/V_B_FROM_Z3_BARRIER_CONJECTURE.md` (lines 88-94, 166-182)
- `edc_book_2/src/derivations/Z3_SYMMETRY_ANALYSIS_NEUTRON.md` (lines 147-156, 287)
- `edc_book_2/src/derivations/S5D_TO_SEFF_Q_REDUCTION.md` (lines 264-314)
- `edc_book_4/chapters/ch03_neutron_metastable.tex` (lines 266-278)

**What IS proven [Dc]:**
- Z₃ symmetry → equal energy partition among 3 arms
- Barrier is Z₃-symmetric (minimal path through saddle)
- Numerical: V_B ≈ 2.01 × Δm_np (calibration discovery)

**Upgrade path:** Put C completion (5D → 1D reduction) → explicit V(q) → [Der]

**Where to resolve:** Ch. 3 OPEN box, Ch. 6 instanton derivation

---

### 4. f-Factor Rigorous Derivation

**Obligation:** Derive the geometric factor f = √(δ/L₀) ≈ 0.32 from first
principles (5D contact geometry, curvature stress, bulk+brane action).

**Current Status:** [I] — Identified, not derived
**Where to resolve:** Ch. 4 OPEN Problem 4.1

---

### 5. Allowed Set S = {2^a × 3^b} Full Derivation

**Obligation:** Prove S = {2^a × 3^b} from full S⁵ → Z₆ symmetry breaking chain.

**Current Status:** [I] — From Z₆ ≅ Z₂ × Z₃, but not fully rigorous
**Where to resolve:** Ch. 5 OPEN Problem 5.1

---

### 6. Prefactor p = 6.1 First-Principles Derivation

**Obligation:** Derive p = 6.1 (n(A) = p × A^(1/3)) from M₆ lattice filling rules
instead of calibration to Pb-208.

**Current Status:** [Cal] — Calibrated phenomenologically
**Where to resolve:** Ch. 5 OPEN Problem 5.2

---

## Completed Items

- [x] Ch. 4 filled with σ → K derivation
- [x] Ch. 5 filled with M₆ lattice, allowed set, forbidden zone
- [x] Observerbox in all 17 chapters
- [x] Appendix code listings (A, B)
- [x] Appendix tables (C)
- [x] Appendix analogies (X)
- [x] Reader Contract in Preface
- [x] Contamination scan protocol
- [x] **Closed-4 minimality theorem** (Ch. 11 §11.7, Theorem 11.6 + 5 lemmas + corollary)

---

## Acceptance Criteria Tracker

| ID | Criterion | Status |
|----|-----------|--------|
| AC-1 | Book compiles clean; final PDF has 0 "??" | Pending build |
| AC-2 | Grep for [Content pending: returns 0 | Pending verify |
| AC-3 | No Layer-A contamination hits | Pending scan |
| AC-4 | Ch4/Ch5 have real narrative + tables + tags | ✅ Done |
| AC-5 | Preface Reader Contract + TODO obligations | ✅ Done |
| AC-6 | No path leaks in PDF | Pending verify |

---

## Future Research Directions (Long-Term)

The following research directions represent the broader potential for EDC theory
development beyond Book IV's immediate scope. These are organized into four pillars.

---

### Pillar 1: Theoretical Refinement (Postulates → Derivations)

**Goal:** Elevate key geometric postulates from [P] to [Der] status via rigorous
derivation from the 5D action.

#### 1.1 L₀/δ Ratio Derivation

**Obligation:** Derive L₀/δ = π² directly from solving field equations for brane
thickness (δ) and topological length (L₀) in curved 5D spacetime.

**Current Status:** [P] — Taken as resonance condition (Ch. 3)
**Approach:** Solve bulk+brane action with thick-brane boundary conditions;
extract eigenvalue spectrum; identify π² as fundamental mode ratio.
**Links to:** Ch. 3 OPEN Problem 3.x, Item #3 (f-factor)

#### 1.2 M₆ Lattice Dynamics (Phase Transition)

**Obligation:** Model the phase transition from "liquid" branes to crystallized
M₆ cluster lattice using 5D statistical mechanics.

**Current Status:** [OPEN] — Not yet addressed
**Approach:**
- Apply partition function methods to 5D worldsheet configurations
- Derive stability of n = 2^a × 3^b coordination at high temperatures
- Explain crystallization as symmetry-breaking S⁵ → Z₆

**Links to:** Ch. 5, Item #4 (Allowed Set S derivation)

---

### Pillar 2: High-Coordination Systems (Heavy Elements)

**Goal:** Extend Book IV coverage from light clusters (A ≤ 4) and Pb-208 anchor
to full nuclide chart mapping.

#### 2.1 Forbidden Zone Analysis

**Obligation:** Detailed analysis of n ∈ [37, 47] region where theory predicts
instability due to M₆ frustration.

**Current Status:** [P] — Qualitative prediction in Ch. 5
**Approach:**
- Map forbidden zone boundaries precisely from Z₆ constraints
- Correlate with observed "islands of instability" in 4D projection
- Quantify frustration energy penalty

**Where to resolve:** Ch. 5 extension or new chapter in Book V

#### 2.2 Closed-4 Emission Mechanism

**Obligation:** Develop detailed theory of how A=4 units (observer projection:
alpha particles) release from frustrated clusters via topological lattice
relaxation rather than classical Coulomb barrier tunneling.

**Current Status:** [Dc] — Corollary 11.7 establishes bias; mechanism is [P]
**Approach:**
- Model release as M₆ lattice reconfiguration (not tunneling)
- Derive release rate from 5D instanton action
- Compare with Geiger-Nuttall phenomenology (Appendix X only)

**Links to:** Ch. 11 Corollary 11.7, Ch. 13–15 (Part E)

---

### Pillar 3: Astrophysical & Cosmological Implications

**Goal:** Extend EDC from nuclear-scale to cosmological-scale predictions.

#### 3.1 Dark Matter as Unpinned States

**Obligation:** Investigate whether "dark matter" could be Layer A objects that
failed to pin into M₆ lattice, thus lacking SM projection but retaining
gravitational influence through 5D tension.

**Current Status:** [OPEN] — Speculative, not yet formalized
**Approach:**
- Define "pinning failure" condition in 5D action
- Calculate gravitational signature of unpinned worldsheets
- Compare with dark matter halo profiles

**Where to resolve:** Book V (Cosmology) or dedicated paper

#### 3.2 Time-Evolution of Fundamental Constants

**Obligation:** If 5D geometry (e.g., fifth dimension radius R₅) evolves with
cosmic expansion, then "constants" like metastable junction lifetime τ_n should
drift over cosmological time.

**Current Status:** [OPEN] — Speculative, falsifiable
**Approach:**
- Derive τ_n dependence on R₅(t)
- Predict drift rate Δτ_n/τ_n per Gyr
- Compare with primordial nucleosynthesis constraints

**Where to resolve:** Book V or Paper Block 004
**Falsifiability:** Direct test via early-universe nucleosynthesis abundance ratios

---

### Pillar 4: Computational Simulation Development

**Goal:** Develop EDC-specific software for lattice simulation and prediction.

#### 4.1 5D Lattice Growth Simulator

**Obligation:** Create software to simulate cluster growth via energy
minimization of 5D junction networks (Steiner trees in M₆ lattice).

**Current Status:** [OPEN] — No implementation
**Approach:**
- Implement junction network as graph with Z₆-constrained edge weights
- Use simulated annealing or gradient descent for energy minimization
- Output: predicted binding energies, coordination numbers, stability

#### 4.2 Exotic Isotope Binding Energy Predictions

**Obligation:** Generate blind predictions for binding energies of isotopes not
yet synthesized, as ultimate objectivity test.

**Current Status:** [OPEN] — Requires simulator (4.1)
**Approach:**
- Run simulator for A > 304 (beyond current synthesis)
- Publish predictions before experimental measurement
- Compare when data becomes available

**Where to resolve:** Dedicated prediction paper after simulator development

---

### Summary: Research Priority Matrix

| ID | Direction | Priority | Status | Blocking |
|----|-----------|----------|--------|----------|
| P1.1 | L₀/δ derivation | HIGH | [P]→[Der] | Ch. 3 rigor |
| P1.2 | M₆ phase transition | MEDIUM | [OPEN] | Ch. 5 extension |
| P2.1 | Forbidden zone map | MEDIUM | [P] | Part E predictions |
| P2.2 | Closed-4 emission | HIGH | [Dc] | Ch. 13–15 mechanism |
| P3.1 | Dark matter as unpinned | LOW | [OPEN] | Book V scope |
| P3.2 | Constant evolution | MEDIUM | [OPEN] | Falsifiable test |
| P4.1 | 5D lattice simulator | HIGH | [OPEN] | All predictions |
| P4.2 | Exotic isotope predictions | HIGH | [OPEN] | Requires P4.1 |

---

### Unification Vision

The ultimate potential of EDC lies in unifying nuclear physics and cosmology.
While modern physics treats these domains separately (quantum mechanics vs.
general relativity), EDC offers a framework where masses and stability of
clusters are direct consequences of global 5D spacetime geometry.

**Next logical step:** Formal publication of Book IV and opening the model
for independent mathematical verification of M₆ lattice postulates.

---

## Feasibility Assessment

Independent assessment of research direction feasibility, with risk analysis
and recommended prioritization.

### Feasibility by Pillar

```
                        FEASIBILITY
Pillar 1 (Theory)       ████████░░  80%
Pillar 2 (Heavy elem)   ███████░░░  70%
Pillar 3 (Cosmo)        ███░░░░░░░  30%
Pillar 4 (Simulation)   █████████░  90%
```

### Detailed Assessment

| ID | Item | Feasibility | Rationale |
|----|------|-------------|-----------|
| P1.1 | L₀/δ derivation | ✅ HIGH (80%) | Standard BVP in thick-brane literature. Mathematical tools exist (Sturm-Liouville, WKB). Computational work, not conceptual barrier. |
| P1.2 | M₆ phase transition | ⚠️ MEDIUM (60%) | Requires 5D partition function for worldsheet ensemble. 2D analogy (Kosterlitz-Thouless) exists but 5D generalization non-trivial. |
| P2.1 | Forbidden zone | ✅ HIGH (85%) | Combinatorial analysis of Z₆ constraints. Can be done with existing tools. Quick win. |
| P2.2 | Closed-4 emission | ⚠️ MEDIUM (55%) | Critical question: can instanton action for lattice reconfiguration be derived without ad-hoc parameters? If yes—revolutionary. If no—remains [P]. |
| P3.1 | Dark matter | ⛔ LOW (20%) | Attractive idea but "unpinned states" requires new physics not in current EDC. No clear derivation path. |
| P3.2 | Constant evolution | ⚠️ MEDIUM (45%) | Testable if τ_n(R₅) derivable. Problem: R₅(t) dynamics undefined in EDC. Requires cosmology integration. |
| P4.1 | Lattice simulator | ✅ HIGH (90%) | Graph-based energy minimization well-understood. Python/NumPy sufficient. Steiner tree algorithms exist. |
| P4.2 | Exotic predictions | ✅ HIGH (90%) | Direct application of P4.1. Blind predictions are gold standard for falsification. |

### Recommended Priority Order

Based on feasibility × impact analysis:

1. **P4.1 → P4.2** (Simulator first)
   - Highest ROI
   - Concrete output, falsifiable predictions
   - Enables all other quantitative work

2. **P1.1** (L₀/δ derivation)
   - Pure mathematical work
   - Elevates theory credibility
   - No external dependencies

3. **P2.1** (Forbidden zone)
   - Quick win
   - Combinatorics already exists in Ch. 5
   - Strengthens Part E narrative

4. **P2.2** (Emission mechanism)
   - Critical for Part E
   - Higher risk but highest reward
   - Work in parallel with P4.1

5. **P1.2, P3.2** (Medium priority)
   - After items 1-4 resolved
   - P3.2 provides falsifiable cosmological test

6. **P3.1** (Dark matter)
   - Keep as speculative vision
   - Do not invest resources until model is stronger
   - Revisit after Book V

### Critical Risk: Make-or-Break Item

**P2.2 (Closed-4 Emission Mechanism)** is the linchpin of EDC predictive power.

- If emission rate derives cleanly from 5D instanton action → EDC becomes
  predictive theory with quantitative falsifiability
- If emission requires phenomenological fitting → EDC reduces to sophisticated
  curve-fitting framework

**Recommendation:** Focus significant effort on P2.2 as the decisive test of
whether EDC is a predictive theory or a descriptive model.

### Dependencies Graph

```
P4.1 (Simulator)
  └── P4.2 (Exotic predictions)
  └── P2.1 (Forbidden zone quantification)
  └── P2.2 (Emission rates)

P1.1 (L₀/δ)
  └── P1.2 (Phase transition)
  └── P3.2 (Constant evolution)

P3.1 (Dark matter) ← standalone, low priority
```

### Assessment Summary

| Category | Items | Verdict |
|----------|-------|---------|
| Near-term achievable | P4.1, P4.2, P1.1, P2.1 | Proceed immediately |
| Medium-term with risk | P2.2, P1.2, P3.2 | Parallel development |
| Long-term speculative | P3.1 | Defer to Book V+ |

---

**Last updated:** 2026-02-10

