# BVP ANALYSIS PLAN — EDC Thick-Brane Boundary Value Problem

**Status:** DRAFT v2.0 (reviewer-hardened)
**Date:** 2026-01-24
**Purpose:** Master roadmap for closing OPR-02 (generations) and OPR-21 (mode profiles)

---

## EXECUTIVE SUMMARY

BVP je **master key** EDC teorije — matematički engine koji pretvara 5D postulate u 3D predikcije. Trenutno je infrastruktura definirana, ali fizički V(z) i BC derivacija ostaju OPEN.

**Closure target:**
```
Derive V(z) + BCs from 5D action → Solve BVP → N_bound = 3 → G_F, masses, mixings
```

**Two-Lane Strategy:**
- **Lane 1 (Numerical Closure Framework):** Reviewer-proof numerics + robustness atlas na toy kandidatima
- **Lane 2 (First-Principles Derivation):** V(z) i δ=R_ξ iz 5D akcije (research-hard, milestone-based)

---

## 0. NO-SMUGGLING / NO-CALIBRATION GUARDRAILS

> **KRITIČNO:** Ovi guardrails vrijede za CIJELI plan. Kršenje bilo kojeg invalidira closure.

| Guardrail | Opis | Provjera |
|-----------|------|----------|
| **G1** | NIKAD ne koristiti PDG/CODATA mase za fit/tune V(z) parametara | PDG samo za POST-HOC usporedbu |
| **G2** | NIKAD ne koristiti M_W, G_F, v=246 GeV kao input | Ove vrijednosti su OUTPUT, ne input |
| **G3** | NIKAD ne tunirati V_0, a, α da dobijemo N_bound=3 | N_bound mora biti ROBUSNI output |
| **G4** | SVE numeričke metode moraju proći Verification Ladder | Bez V0-V2, numerika nije vjerodostojna |
| **G5** | Threshold λ_th mora biti intrinsično definiran | Iz gap kriterija ili essential spectrum, NE iz PDG |

**Dozvoljeno:**
- Koristiti (σ, r_e, R_ξ) iz Part I kao membrane parametre [Dc]
- Koristiti PDG za USPOREDBU nakon što su outputi izračunati
- Koristiti matematičke identitete (Sturm-Liouville teorija) [M]

---

## 1. CURRENT STATE ASSESSMENT

### 1.1 Existing Infrastructure

| Component | Status | File |
|-----------|--------|------|
| BVP specification | ✅ [M]/[Def] | `ch14_bvp_closure_pack.tex` |
| Work package definition | ✅ [Def] | `ch12_bvp_workpackage.tex` |
| Toy solver (Pöschl-Teller) | ✅ [M]/[Toy] | `bvp_halfline_toy_demo.py` |
| Thick-brane skeleton | ✅ [M] | `bvp_thick_brane_solver_skeleton.py` |
| OPR-20 mediator BVP | ✅ [Dc]+[P] | `solve_opr20_mediator_bvp.py` |
| V(z) candidates catalogue | ✅ [P]/[Toy] | `ch14_bvp_closure_pack.tex` |
| Robin BC from junction | ✅ [Dc] | `ch11_opr20_attemptF_*.tex` |
| Factor-8 forensics | ⚠️ [Dc]+[P] | `ch11_opr20_factor8_forensic.tex` |

### 1.2 Open Problems (BVP-Related)

| OPR | Description | Status | Blocks |
|-----|-------------|--------|--------|
| **OPR-02** | KK tower truncation (N_gen = 3) | 🔴 RED-C | All generation counting |
| **OPR-21** | Mode profiles f_L(z) | 🔴 RED-C | G_F, neutrino mass, pion |
| **OPR-20** | Mediator mass | 🔴 RED-C | Weak scale |
| OPR-20a | BC provenance | 🟡 YELLOW | Unique derivation |
| OPR-20b | α = ℓ/δ derivation | 🟡 YELLOW+OPEN | Robin parameter |
| OPR-20c | R_ξ from action | 🔴 RED | No EW phenomenology |
| OPR-20d | Boundary-layer theorem | 🔴 RED | δ = R_ξ proof |
| OPR-20e | Unique transverse scale | 🔴 RED | Exclude ratio combinations |
| OPR-20f | δ-robustness band | 🔴 RED | BVP scan for stability |

### 1.3 Key Equations (Current Form)

**Sturm-Liouville BVP:**
```
[-d²/dz² + V(z)] f(z) = λ f(z)     domain: z ∈ [0, ℓ]
```

**Dimensionless form:**
```
[-d²/dξ² + Ṽ(ξ)] f̃(ξ) = λ̃ f̃(ξ)   domain: ξ ∈ [0, 1]

where: ξ = z/ℓ, Ṽ = ℓ²V, λ̃ = ℓ²λ
```

**Robin BC (junction-derived):**
```
f'(0) + α_L f(0) = 0
f'(1) + α_R f(1) = 0

Natural value: α = 2π (circumference interpretation)
Status: [P] — derivation from action OPEN
```

**V(z) structure (pipeline target):**
```
V(z) = V_warp(z) + V_mass(z) + V_coupling(z)

- V_warp: from warp factor A(z) derivatives
- V_mass: from bulk mass terms
- V_coupling: from brane-localized couplings
```

---

## 2. VERIFICATION LADDER (Numerics)

> **Svrha:** Eliminirati "numerical artifact" reviewer napad. Svaki numerički rezultat mora proći V0→V1→V2.

### Level V0: Analytic Benchmark Set

**Cilj:** Verificirati solver na problemima s poznatim analitičkim rješenjima.

| Benchmark | Analytic λ_n | Test | Tolerance |
|-----------|--------------|------|-----------|
| Infinite square well | λ_n = (nπ/L)² | Eigenvalues | < 0.01% |
| Harmonic oscillator | λ_n = (2n+1)ω | Eigenvalues | < 0.01% |
| Pöschl-Teller | λ_n = -[s(s+1) - (s-n)²]/a² | Eigenvalues | < 0.1% |

**Provjere:**
- [ ] Eigenvalue greška vs grid size (log-log plot)
- [ ] Eigenfunction oblici kvalitativno ispravni
- [ ] Normalizacija: |∫|ψ_n|² dz - 1| < 10⁻⁸
- [ ] Ortogonalnost: |∫ψ_m*ψ_n dz| < 10⁻⁸ za m≠n

**Acceptance:** PASS ako SVE benchmark provjere prolaze. FAIL blokira sve downstream claims.

### Level V1: Cross-Method Check

**Cilj:** Verificirati da rezultati nisu artefakt specifične numeričke metode.

**Zahtjev:** Implementirati DVA nezavisna solvera:
- **Metoda A:** Finite-difference + sparse eigenvalue solver (scipy.sparse.linalg.eigsh)
- **Metoda B:** Shooting method + root finding (scipy.integrate + bisection)
- **Alternativa B':** Chebyshev collocation (spectral method)

**Provjere:**
- [ ] |λ_n(A) - λ_n(B)| / |λ_n(A)| < 10⁻⁴ za sve bound states
- [ ] N_bound(A) = N_bound(B) identično
- [ ] ψ_n oblici kvalitativno identični (correlation > 0.999)

**Acceptance:** PASS ako svi bound states agree. DISAGREEMENT blokira downstream claims i zahtijeva debugging.

### Level V2: Invariance/Stability Checks

**Cilj:** Pokazati da rezultati nisu sensitvni na numeričke detalje.

**Provjere:**

| Check | Metrika | Tolerance |
|-------|---------|-----------|
| Grid refinement | Δλ pri 2× grid | < 0.1% |
| z_max cutoff stability | Δλ pri z_max ± 20% | < 0.5% |
| Operator symmetry | ‖H - H^T‖ / ‖H‖ | < 10⁻¹² |
| Normalization | |∫|ψ|² - 1| | < 10⁻⁶ |
| Orthogonality | |⟨ψ_m, ψ_n⟩| for m≠n | < 10⁻⁶ |
| BC satisfaction | |f'(0) + αf(0)| / max|f| | < 10⁻⁸ |
| N_bound stability | ΔN pod grid/cutoff varijacijama | = 0 |

**Acceptance:** PASS ako SVE provjere zadovoljene. Failure u bilo kojoj zahtijeva investigaciju.

---

## 3. ROBUSTNESS DEFINITION FOR N_bound = 3

> **Svrha:** Precizno definirati što znači "N_bound = 3 robusno" da recenzent ne može napasti vague claims.

### 3.1 Parameter Space Definition

**Parameter space Θ:**
```
θ = (V_0, a, α_L, α_R, z_max, N_grid, method_flag) ∈ Θ

where:
- V_0 ∈ [V_min, V_max]: potential depth
- a ∈ [a_min, a_max]: potential width
- α_L, α_R ∈ [0, ∞]: Robin BC parameters (∞ = Dirichlet)
- z_max ∈ [z_min, z_cut]: truncation (numerical)
- N_grid ∈ {N_1, N_2, ...}: grid sizes
- method_flag ∈ {FD, shooting, collocation}
```

### 3.2 Robust Region Definition

**Definition (Robust Region R₃):**

Skup R₃ ⊂ Θ je **robust region za N_bound = 3** ako vrijedi:

1. **Positive measure:**
   ```
   μ(R₃) > 0   (non-zero volume in parameter space)
   ```

2. **Interior point (ε-ball criterion):**
   ```
   ∃ θ* ∈ R₃ i ∃ ε > 0 takav da B_ε(θ*) ⊂ R₃

   tj. postoji točka koja NIJE na granici N=3 regije
   ```

3. **Spectral gap criterion:**
   ```
   Za sve θ ∈ R₃:

   gap_lower = λ_th - λ_3 > δ_gap   (3rd eigenvalue below threshold)
   gap_upper = λ_4 - λ_th > δ_gap   (4th eigenvalue above threshold, if exists)

   gdje δ_gap > 0 je minimalni gap margin (npr. 5% of |λ_3|)
   ```

### 3.3 Acceptance Tests (Blob Criterion)

**Test R1: 2D Slice Visualization**
- Prikaži barem jedan 2D slice (npr. (V_0, a) za fiksni α)
- N=3 regija mora formirati **kompaktni blob**, NE tanku krivulju
- Granice N=2↔N=3 i N=3↔N=4 moraju biti jasno odvojene

**Test R2: Distance-to-Boundary Metric**
- Za referentnu točku θ* (npr. "physical candidate"):
  ```
  d_boundary = min_{θ ∈ ∂R₃} ||θ - θ*||
  ```
- Acceptance: d_boundary > ε_min (nije na rubu)

**Test R3: Gap Margin Report**
- Za svaku točku u robustness scan-u, report:
  ```
  gap_3 = λ_th - λ_3   (how far λ_3 is below threshold)
  gap_4 = λ_4 - λ_th   (how far λ_4 is above threshold, or "N/A")
  ```
- Acceptance: gap_3 > 5% |λ_3| i gap_4 > 5% |λ_4| (if λ_4 exists)

### 3.4 What Counts as "Fine-Tuning" (Anti-Pattern)

**N_bound = 3 je FINE-TUNED ako:**
- R₃ ima nultu mjeru (samo jedna krivulja/točka)
- θ* leži na ∂R₃ (granici)
- gap_3 ili gap_4 je < 1% (numerički ~0)
- N_bound = 3 vrijedi samo za jedan method_flag

**Fine-tuning → OPR-02 ostaje RED.**

---

## 4. GAP ANALYSIS

### 4.1 Critical Gaps (Block Closure)

| Gap ID | Description | Current State | Required |
|--------|-------------|---------------|----------|
| **GAP-1** | V(z) shape | 5 toy candidates [P] | Derivation from 5D action [Dc] |
| **GAP-2** | BC parameters α_L, α_R | Natural value α=2π [P] | From Israel junction [Dc] |
| **GAP-3** | Brane thickness δ | δ = R_ξ hypothesis [P] | From matched asymptotics [Dc] |
| **GAP-4** | N_bound = 3 proof | Phase diagram shows possible | Physical V(z) yields 3 robustly |
| **GAP-5** | G_F numerics | Spine formula [Dc] | x₁, I₄ from physical BVP |

### 4.2 Dependency Graph

```
                    ┌─────────────────┐
                    │ 5D Membrane     │
                    │ Action S[g,Φ]   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
       ┌──────────┐   ┌──────────┐   ┌──────────┐
       │ Warp     │   │ Bulk     │   │ Brane    │
       │ Factor   │   │ Mass     │   │ Coupling │
       │ A(z)     │   │ Terms    │   │ Terms    │
       └────┬─────┘   └────┬─────┘   └────┬─────┘
            │              │              │
            └──────────────┼──────────────┘
                           ▼
                    ┌─────────────────┐
                    │   V(z) = Sum    │ ◄── GAP-1 (Lane 2)
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              │              ▼
       ┌──────────┐          │       ┌──────────┐
       │ Israel   │          │       │ GHY      │
       │ Junction │          │       │ Boundary │
       └────┬─────┘          │       └────┬─────┘
            │                │             │
            └────────────────┼─────────────┘
                             ▼
                    ┌─────────────────┐
                    │ Robin BC: α_L,R │ ◄── GAP-2 (Lane 2)
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ SOLVE BVP       │ ◄── Lane 1 (numerics)
                    │ [-d²/dz²+V]f=λf │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
  ┌────────────┐      ┌────────────┐      ┌────────────┐
  │ Eigenvalues│      │ N_bound    │      │ Overlap    │
  │ λ_n        │      │ (count)    │      │ I₄         │
  └─────┬──────┘      └─────┬──────┘      └─────┬──────┘
        │                   │                   │
        ▼                   ▼                   ▼
  ┌────────────┐      ┌────────────┐      ┌────────────┐
  │ Mass Ratios│      │ OPR-02     │      │ G_F        │
  │ m_μ/m_e    │      │ N_gen = 3  │      │ Closure    │
  └────────────┘      └────────────┘      └────────────┘
```

---

## 5. RESEARCH TRACKS

### TRACK A: V(z) Derivation from 5D Action [Lane 2]

**Objective:** Derive explicit V(z) form from EDC 5D action

**Steps:**
1. **A.1** Write complete 5D action with all terms
   - S_bulk (Einstein-Hilbert + Plenum)
   - S_brane (tension σ + matter coupling)
   - S_GHY (Gibbons-Hawking-York)

2. **A.2** Solve background Einstein equations for warp factor A(z)
   - Ansatz: ds² = e^{2A(z)} η_μν dx^μ dx^ν + dz²
   - Junction conditions at brane

3. **A.3** Dimensional reduction for fermion modes
   - 5D Dirac equation → 4D mode expansion
   - Identify effective potential V(z)

4. **A.4** Express V(z) in terms of (σ, r_e, R_ξ)
   - Map warp factor A(z) to membrane parameters
   - Verify dimensional consistency

**Deliverables:**
- [ ] Explicit V(z) formula (or bounds)
- [ ] Parameter table: V_0, width, asymptotic behavior
- [ ] Comparison with toy candidates
- [ ] Shape discrimination: volcano vs kink vs other

**Effort:** HIGH (3-6 weeks, **risk: may extend ×2**)
**Risk:** May require additional ansätze; uniqueness not guaranteed

**Partial success output:** Even without full V(z), deliver:
- Asymptotic constraints (V(z→0), V(z→∞))
- Shape class discrimination (volcano-like vs kink-like)
- Parameter bounds compatible with membrane physics

---

### TRACK B: Robin BC from Israel Junction [Lane 1+2]

**Objective:** Derive admissible BC class + bounds (not necessarily unique α)

**Steps:**
1. **B.1** Write Israel junction conditions for fermion fields
   - [K_ab] - g_ab[K] = -(1/M₅³) S_ab
   - Specialize to brane at z = 0 and z = ℓ

2. **B.2** Translate to Robin form
   - Junction → f'(0) + α_L f(0) = 0
   - Identify α in terms of physical quantities

3. **B.3** Define admissible BC family
   - Bounds: α ∈ [α_min, α_max]
   - Special points: α = 2π (natural), α → 0 (Neumann), α → ∞ (Dirichlet)

4. **B.4** Sensitivity analysis
   - x₁(α), I₄(α), N_bound(α) maps
   - Identify "stable plateau" regions

**Deliverables:**
- [ ] Admissible BC class definition
- [ ] α bounds (or full derivation if achievable)
- [ ] Sensitivity maps: x₁(α), N_bound(α)
- [ ] Identification of "natural" α points

**Effort:** MEDIUM (2-4 weeks)
**Risk:** MEDIUM — may not have unique solution; deliver family instead

---

### TRACK C: Numerical BVP Solver Enhancement [Lane 1 — LOW RISK]

**Objective:** Production-quality solver with full Verification Ladder compliance

**Steps:**
1. **C.1** Implement V0 benchmark suite
   - Infinite well, harmonic oscillator, Pöschl-Teller
   - Automated comparison vs analytic

2. **C.2** Implement cross-method verification (V1)
   - Method A: FD + sparse eigen
   - Method B: Shooting + root finding
   - Agreement checks

3. **C.3** Extend to all V(z) candidates
   - Volcano, Kink, Compact, Double-well, Exponential
   - Parameter space coverage

4. **C.4** Implement full Robin BC class
   - α ∈ [0, ∞) continuous sweep
   - Mixed BC combinations (α_L ≠ α_R)

5. **C.5** Phase diagram automation
   - N_bound(V_0, a, α) 3D scan
   - Critical surface identification
   - Gap margin computation

6. **C.6** Stability checks (V2)
   - Grid refinement convergence
   - z_max cutoff stability
   - Operator symmetry sanity

7. **C.7** Output pipeline
   - x₁, I₄, N_bound extraction with error bars
   - LaTeX table generation
   - Reproducibility packaging

**Deliverables:**
- [ ] Enhanced solver: `bvp_physical_solver.py`
- [ ] V0 benchmark report (PASS required)
- [ ] V1 cross-method report (PASS required)
- [ ] V2 stability report (PASS required)
- [ ] Phase diagram atlas (all candidates)
- [ ] Robustness atlas with blob criterion
- [ ] Reproducibility package

**Effort:** MEDIUM (2-3 weeks)
**Risk:** LOW (infrastructure, not physics)

---

### TRACK D: δ = R_ξ Derivation (OPR-20c/d) [Lane 2 — UPGRADE, NOT BLOCKER]

**Objective:** Prove δ = R_ξ from matched asymptotics

> **VAŽNO:** Track D je **upgrade/strengthening**, NE blocker za Lane 1 numerical closure.
> Ako D ne uspije, δ ostaje [P] s robustness band analizom.

**Steps:**
1. **D.1** Define inner and outer regions
   - Inner: z = O(δ), boundary layer
   - Outer: z = O(ℓ), bulk region

2. **D.2** Solve inner problem
   - Rescale: ζ = z/δ
   - Boundary layer equation

3. **D.3** Solve outer problem
   - Standard KK reduction
   - Bulk solution

4. **D.4** Matching condition
   - Overlap region: δ ≪ z ≪ ℓ
   - Require agreement

5. **D.5** Identification
   - Show δ emerges as R_ξ from matching
   - Or document obstruction if fails

**Deliverables:**
- [ ] Matched asymptotics derivation (or failure certificate)
- [ ] δ formula (or bounds)
- [ ] Fail-safe narrative update

**Effort:** HIGH (4-8 weeks, **risk: may extend significantly**)
**Risk:** HIGH — may not close; requires new mathematics

**Fail-safe:** If D fails:
- δ treated as additional parameter with [OPEN] tag
- Define scaling band: δ/ℓ ∈ [10⁻ᵏ¹, 10⁻ᵏ²]
- Show key results (N_bound) stable within band
- OPR-20c/d remain RED, but Lane 1 proceeds

---

### TRACK E: N_bound = 3 Verification [Lane 1 finale]

**Objective:** Demonstrate N_bound = 3 robustly per Section 3 criteria

**Steps:**
1. **E.1** Use V(z) from Track A (or best toy candidate if A incomplete)
2. **E.2** Use α from Track B (admissible class, or natural value)
3. **E.3** Solve BVP numerically (Track C solver, V0-V2 verified)
4. **E.4** Count bound states below threshold
5. **E.5** Robustness scan over parameter space Θ
6. **E.6** Verify blob criterion (Section 3.3)
7. **E.7** Report gap margins

**Acceptance criteria (from Section 3):**
- [ ] N_bound = 3 for derived/candidate V(z) and α
- [ ] R₃ has positive measure (blob, not curve)
- [ ] ε-ball exists (not on boundary)
- [ ] Gap margins > 5%
- [ ] Stable across V0-V2 verification

**Deliverables:**
- [ ] N_bound verification report
- [ ] 2D slice plots showing R₃ blob
- [ ] Gap margin table
- [ ] OPR-02 closure assessment

**Effort:** LOW-MEDIUM (1-2 weeks, after C complete)
**Risk:** Depends on V(z) quality; toy candidates may still work

---

## 6. TWO-LANE CRITICAL PATH

### Lane 1: Numerical Closure Framework (Fast, Low-Risk)

```
Tjedan 1-2:   Track C (solver + V0-V2 verification)
              ├── V0 benchmarks PASS
              ├── V1 cross-method PASS
              └── V2 stability PASS

Tjedan 2-3:   Track C (all V(z) candidates + phase atlas)
              ├── 5 potencijala implementirano
              ├── Phase diagrams generirani
              └── N_bound(V_0, a) maps

Tjedan 3-4:   Track B (admissible BC family + sensitivity)
              ├── α bounds definirani
              ├── x₁(α), N_bound(α) maps
              └── "Natural points" identificirani

Tjedan 4-5:   Track E (robustness verification)
              ├── R₃ blob criterion verificiran
              ├── Gap margins reported
              └── OPR-02 status: YELLOW [P] ili RED

OUTPUT:       Reviewer-proof numerical framework
              N_bound = 3 demonstriran za toy V(z) + admissible BC class
              Explicit [P] tags where derivation missing
```

### Lane 2: First-Principles Derivation (Research-Hard, Milestone-Based)

```
Tjedan 1-6:   Track A (V(z) derivation attempt)
              ├── M1: Action written
              ├── M2: Einstein eqs attempted
              ├── M3: V(z) shape constraints (even if not full formula)
              └── Partial success: shape class + asymptotic bounds

Tjedan 4-8+:  Track D (δ = R_ξ matched asymptotics)
              ├── Inner/outer problems formulated
              ├── Matching attempted
              └── Success → OPR-20c/d GREEN
              └── Failure → fail-safe + scaling band

OUTPUT:       If successful: OPR-02/21 upgrade to GREEN [Dc]
              If partial: Shape constraints feed back to Lane 1
              If failed: Lane 1 results stand with [P] tags
```

### Combined Timeline

```
Week  1: C.1-C.2 (benchmarks)         | A.1 (action)
Week  2: C.3-C.4 (candidates, BC)     | A.2 (Einstein eqs)
Week  3: C.5-C.6 (phase atlas)        | A.3 (reduction)
Week  4: B.1-B.4 (BC family)          | A.4 (V(z) formula attempt)
Week  5: E.1-E.4 (N_bound scan)       | D.1-D.2 (inner/outer)
Week  6: E.5-E.7 (robustness proof)   | D.3-D.4 (matching)
Week  7: Report consolidation         | D.5 (identification)
Week  8: Publication prep             | Track D wrap-up
```

**Minimum Viable Closure (Lane 1 only):**
- OPR-02/21: YELLOW [P] (N_bound = 3 za toy V(z) s admissible BC)
- Framework intact; derivation deferred to Lane 2
- Publishable: "Numerical framework demonstrates generation counting mechanism"

---

## 7. OUTPUTS-TO-DOWNSTREAM CONTRACT

> **Svrha:** Definirati minimalni format za svaki BVP output koji Part II/III očekuju.
> Ovo sprječava ad-hoc interpretaciju brojeva.

### 7.1 N_bound (Generation Count)

| Field | Required Content |
|-------|------------------|
| **Definition** | "Number of eigenvalues λ_n < λ_th where λ_th is [intrinsic threshold definition]" |
| **Threshold** | Gap criterion formula OR essential spectrum onset — NOT PDG-derived |
| **Value** | N_bound = [integer] |
| **Error** | N_bound is exact integer; stability = "unchanged under V0-V2 checks" |
| **Robustness** | 2D slice plot + blob criterion assessment + gap margins |
| **Sensitivity** | ΔN_bound under α ± 10%, V_0 ± 10% |

### 7.2 x₁ (First Eigenvalue)

| Field | Required Content |
|-------|------------------|
| **Definition** | "Lowest positive eigenvalue of dimensionless BVP" OR "|E_ground|" |
| **Value** | x₁ = [number] |
| **Error bar** | From grid refinement: x₁ ± δx₁ |
| **BC dependence** | x₁(α) curve with slope at natural point |
| **Stability** | V0-V2 verification status |

### 7.3 I₄ (Overlap Integral)

| Field | Required Content |
|-------|------------------|
| **Definition** | I₄ = ∫|ψ_0(z)|⁴ dz (ground state four-point overlap) |
| **Value** | I₄ = [number] |
| **Error** | From grid refinement: I₄ ± δI₄ |
| **Convergence** | I₄ vs N_grid plot showing asymptote |
| **Units** | Dimensionless (using ξ = z/ℓ normalization) |

### 7.4 ψ_n(z) (Mode Profiles)

| Field | Required Content |
|-------|------------------|
| **Normalization** | ∫|ψ_n|² dz = 1 verified to tolerance |
| **Orthogonality** | |⟨ψ_m, ψ_n⟩| < tolerance for m≠n |
| **BC satisfaction** | |f'(0) + αf(0)| / max|f| < tolerance |
| **Parity/shape** | Node count = n (for bound states) |
| **Plot** | ψ_n(z) vs z with V(z) overlay |

### 7.5 No-Fit Guardrail

> **KRITIČNO:** PDG vrijednosti (m_e, m_μ, m_τ, M_W, G_F, itd.) NIKAD ne smiju biti input.
>
> PDG se smije koristiti SAMO u finalnoj sekciji "External Comparison" s eksplicitnim
> disclaimerom: "Ove PDG vrijednosti nisu korištene u izračunu; prikazane su samo za usporedbu."

---

## 8. REVIEWER ATTACK SURFACE

> **Svrha:** Anticipirati reviewer napade i pokazati kako je svaki adresiran.

| Attack | Response |
|--------|----------|
| **"Numerical artifact"** | → Verification Ladder V0-V2 s explicit PASS kriterijima |
| **"N=3 is a slogan / fine-tuned"** | → Robust region R₃ definicija + blob criterion + gap margins > 5% |
| **"Circular calibration"** | → No-smuggling guardrails G1-G5; PDG only post-hoc |
| **"δ=R_ξ unproven breaks everything"** | → Track D je upgrade, ne blocker; fail-safe s scaling band |
| **"V(z) is arbitrary"** | → 5 toy kandidata surveyed; Lane 2 attempts derivation; shape constraints |
| **"BC choice is arbitrary"** | → Admissible BC family from Track B; sensitivity maps; natural points |
| **"Results method-dependent"** | → V1 cross-method check: FD vs shooting agreement |
| **"Error bars missing"** | → Outputs-to-Downstream Contract zahtijeva error bars za sve |

---

## 9. ACCEPTANCE CRITERIA BY MILESTONE

### Milestone M1: Solver Verified (Week 2)
- [ ] V0 benchmarks: ALL PASS
- [ ] V1 cross-method: ALL PASS
- [ ] V2 stability: ALL PASS
- [ ] At least 3 V(z) candidates implemented

### Milestone M2: Phase Atlas Complete (Week 3)
- [ ] All 5 V(z) candidates covered
- [ ] N_bound(V_0, a) phase diagrams for each
- [ ] Critical surfaces identified

### Milestone M3: BC Family Characterized (Week 4)
- [ ] Admissible BC class defined with bounds
- [ ] x₁(α), N_bound(α) sensitivity maps
- [ ] "Natural" α points identified

### Milestone M4: Robustness Proven (Week 6)
- [ ] R₃ blob criterion satisfied (at least one 2D slice)
- [ ] Gap margins > 5% for representative points
- [ ] N_bound = 3 stable under V0-V2

### Milestone M5: Lane 2 Assessment (Week 8)
- [ ] Track A: V(z) formula OR shape constraints OR failure certificate
- [ ] Track D: δ derivation OR fail-safe + scaling band
- [ ] Final OPR-02/21 status determination

---

## 10. RISK ASSESSMENT (Updated)

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| V(z) not derivable | MEDIUM | HIGH | Lane 1 proceeds with toy candidates [P] |
| N_bound ≠ 3 for all V(z) | LOW | CRITICAL | Would falsify model; document as failure |
| α not unique | MEDIUM | LOW | Deliver admissible class instead of single value |
| δ ≠ R_ξ | MEDIUM | LOW | Fail-safe: scaling band + [OPEN] tag |
| Numerical instability | LOW | LOW | V0-V2 verification catches this |
| Cross-method disagreement | LOW | MEDIUM | Debug before proceeding; blocks downstream |
| Lane 2 delayed | HIGH | LOW | Lane 1 publishable independently |

---

## 11. FILES TO CREATE/MODIFY

### New Files
- [ ] `code/bvp_physical_solver.py` — enhanced solver with V0-V2
- [ ] `code/bvp_phase_atlas.py` — automated phase diagrams
- [ ] `code/bvp_verification_suite.py` — V0-V2 test harness
- [ ] `code/output/phase_atlas/` — generated figures
- [ ] `bvp_reports/ROBUSTNESS_ATLAS_REPORT.md` — results template
- [ ] `sections/ch14_bvp_vz_derivation.tex` — Track A results (if successful)
- [ ] `sections/ch14_bvp_bc_derivation.tex` — Track B results

### Modified Files
- [ ] `ch14_bvp_closure_pack.tex` — add derivation results
- [ ] `ch11_opr20_attemptH_delta_equals_Rxi.tex` — Track D results
- [ ] `OPEN_PROBLEMS_REGISTER.md` — status updates
- [ ] `CHANGELOG.md` — milestone entries

---

## 12. IMMEDIATE NEXT ACTIONS

1. **Implement V0 benchmark suite**
   ```bash
   # Create verification test harness
   python3 code/bvp_verification_suite.py --level V0
   ```

2. **Run V1 cross-method comparison**
   ```bash
   python3 code/bvp_verification_suite.py --level V1
   ```

3. **Generate baseline phase atlas**
   ```bash
   python3 code/bvp_phase_atlas.py --all-candidates
   ```

4. **Create robustness report template**
   - See `bvp_reports/ROBUSTNESS_ATLAS_REPORT.md`

---

## 13. SUCCESS DEFINITION (Updated)

**FULL CLOSURE (OPR-02/21 GREEN):**
- V(z) derived from 5D action [Dc]
- BC parameters derived from junction [Dc]
- N_bound = 3 robustly verified (R₃ blob + gaps)
- V0-V2 verification ALL PASS
- No SM/PDG inputs used

**PARTIAL CLOSURE (OPR-02/21 YELLOW):**
- V(z) from best toy candidate [P]
- BC parameters from admissible class [P]
- N_bound = 3 for this configuration, robustly
- V0-V2 verification ALL PASS
- Framework intact; derivation deferred

**NO CLOSURE (OPR-02/21 RED):**
- N_bound ≠ 3 for all reasonable V(z)/BC combinations
- OR V0-V2 verification FAIL
- Model falsified or needs fundamental revision

---

*This plan is a living document. Update as tracks progress.*
*Version 2.0: Added verification ladder, robustness definition, two-lane strategy, reviewer attack surface.*
