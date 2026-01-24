# ROBUSTNESS ATLAS REPORT — BVP Numerical Results

**Status:** TEMPLATE (popuniti nakon pokretanja numerike)
**Date:** [YYYY-MM-DD]
**Run ID:** [git commit short hash]

---

## A. EXECUTIVE SUMMARY

| Metrika | Rezultat | Status |
|---------|----------|--------|
| V0 Benchmarks | [ ] PASS / [ ] FAIL | |
| V1 Cross-Method | [ ] PASS / [ ] FAIL | |
| V2 Stability | [ ] PASS / [ ] FAIL | |
| N_bound = 3 (any candidate) | [ ] YES / [ ] NO | |
| Blob criterion satisfied | [ ] YES / [ ] NO | |
| Gap margins > 5% | [ ] YES / [ ] NO | |

**Overall Assessment:**
- [ ] FULL CLOSURE: Sve provjere PASS, N_bound = 3 robusno
- [ ] PARTIAL CLOSURE: Numerika OK, N_bound = 3 za toy V(z) [P]
- [ ] NO CLOSURE: N_bound ≠ 3 ili verification FAIL

**Key Findings:**
1. [Popuniti]
2. [Popuniti]
3. [Popuniti]

**Remaining OPEN:**
1. [Popuniti]

---

## B. GUARDRAILS (No-Fit / No-Tune)

> **KRITIČNO:** Ovi guardrails moraju biti zadovoljeni. Kršenje invalidira sve rezultate.

| Guardrail | Provjera | Status |
|-----------|----------|--------|
| G1: PDG mase nisu korištene za fit V(z) | [ ] DA | [ ] PASS |
| G2: M_W, G_F, v nisu input | [ ] DA | [ ] PASS |
| G3: V_0, a, α nisu tunirani za N=3 | [ ] DA | [ ] PASS |
| G4: Verification Ladder prošao | [ ] DA | [ ] PASS |
| G5: Threshold intrinsično definiran | [ ] DA | [ ] PASS |

**PDG Usage Disclaimer:**
> PDG vrijednosti (ako prikazane) korištene su ISKLJUČIVO za post-hoc usporedbu.
> Nijedna PDG vrijednost nije korištena kao input u BVP izračun.

---

## C. DEFINITIONS

### C.1 Parameter Space Θ

```
θ = (V_0, a, α_L, α_R, z_max, N_grid, method_flag)

Ranges used in this report:
- V_0 ∈ [_____, _____]
- a ∈ [_____, _____]
- α_L = α_R ∈ [_____, _____]
- z_max ∈ [_____, _____]
- N_grid ∈ {_____, _____, _____}
- method_flag ∈ {FD, shooting}
```

### C.2 Essential Spectrum Threshold

```
λ_th = lim_{z→∞} V(z) = _____

Definition: Bound states are eigenvalues λ_n < λ_th
Source: [Intrinsic from potential asymptotics, NOT PDG]
```

### C.3 Robust Region R₃

**Definition:**
```
R₃ = { θ ∈ Θ : N_bound(θ) = 3 }
```

**Blob Criterion:**
- [ ] R₃ ima pozitivnu mjeru (volumen > 0)
- [ ] Postoji ε-ball: B_ε(θ*) ⊂ R₃ za neku točku θ*
- [ ] Gap margins > δ_gap za sve θ ∈ R₃

**Distance-to-Boundary:**
```
d_boundary(θ*) = min_{θ ∈ ∂R₃} ||θ - θ*|| = _____
ε_min criterion: d_boundary > _____ ?  [ ] YES / [ ] NO
```

---

## D. VERIFICATION LADDER

### D.1 Level V0: Analytic Benchmarks

#### Infinite Square Well (L = 1)

| n | λ_analytic | λ_numerical | Error (%) | Status |
|---|------------|-------------|-----------|--------|
| 0 | π² = 9.8696 | | | [ ] PASS |
| 1 | 4π² = 39.478 | | | [ ] PASS |
| 2 | 9π² = 88.826 | | | [ ] PASS |

**FIGURE SLOT:** `FIGURES/v0_infinite_well_convergence.png`

#### Harmonic Oscillator (ω = 1)

| n | λ_analytic | λ_numerical | Error (%) | Status |
|---|------------|-------------|-----------|--------|
| 0 | 1 | | | [ ] PASS |
| 1 | 3 | | | [ ] PASS |
| 2 | 5 | | | [ ] PASS |

**FIGURE SLOT:** `FIGURES/v0_harmonic_convergence.png`

#### Pöschl-Teller (V_0 = 6, a = 1)

| n | λ_analytic | λ_numerical | Error (%) | Status |
|---|------------|-------------|-----------|--------|
| 0 | | | | [ ] PASS |
| 1 | | | | [ ] PASS |

**FIGURE SLOT:** `FIGURES/v0_poschl_teller_convergence.png`

#### V0 Summary

- [ ] Svi benchmarks PASS (error < 0.1%)
- [ ] Normalizacija OK (|∫|ψ|² - 1| < 10⁻⁸)
- [ ] Ortogonalnost OK (|⟨ψ_m,ψ_n⟩| < 10⁻⁸ za m≠n)

**V0 STATUS:** [ ] PASS / [ ] FAIL

---

### D.2 Level V1: Cross-Method Check

#### Method A: Finite-Difference + Sparse Eigen
```
Solver: scipy.sparse.linalg.eigsh
Grid: N = _____
Discretization: 2nd order central differences
```

#### Method B: Shooting + Root Finding
```
Solver: scipy.integrate.solve_ivp + bisection
Tolerance: _____
```

#### Agreement Table (za Pöschl-Teller, V_0 = 10)

| n | λ(A) | λ(B) | |λ(A)-λ(B)|/|λ(A)| | Status |
|---|------|------|-------------------|--------|
| 0 | | | | [ ] < 10⁻⁴ |
| 1 | | | | [ ] < 10⁻⁴ |
| 2 | | | | [ ] < 10⁻⁴ |

**N_bound agreement:** N(A) = _____, N(B) = _____ → [ ] MATCH / [ ] MISMATCH

**V1 STATUS:** [ ] PASS / [ ] FAIL

---

### D.3 Level V2: Stability Checks

#### Grid Refinement

| N_grid | λ_0 | Δλ_0 (%) vs prev | Status |
|--------|-----|------------------|--------|
| 100 | | — | |
| 200 | | | [ ] < 0.1% |
| 400 | | | [ ] < 0.1% |
| 800 | | | [ ] < 0.1% |

**FIGURE SLOT:** `FIGURES/v2_grid_convergence.png`

#### z_max Cutoff Stability

| z_max | λ_0 | Δλ_0 (%) | N_bound | Status |
|-------|-----|----------|---------|--------|
| 10 | | | | |
| 12 | | | | [ ] stable |
| 15 | | | | [ ] stable |

#### Operator Symmetry

```
||H - H^T|| / ||H|| = _____
Tolerance: < 10⁻¹²
Status: [ ] PASS / [ ] FAIL
```

#### Normalization Check

| n | ∫|ψ_n|² dz | |1 - integral| | Status |
|---|------------|----------------|--------|
| 0 | | | [ ] < 10⁻⁶ |
| 1 | | | [ ] < 10⁻⁶ |
| 2 | | | [ ] < 10⁻⁶ |

#### BC Satisfaction

| n | |f'(0) + αf(0)| / max|f| | Status |
|---|-------------------------|--------|
| 0 | | [ ] < 10⁻⁸ |
| 1 | | [ ] < 10⁻⁸ |
| 2 | | [ ] < 10⁻⁸ |

**V2 STATUS:** [ ] PASS / [ ] FAIL

---

## E. RESULTS: TOY V(z) ATLAS

### E.1 Pöschl-Teller (Kink)

**Formula:** V(ξ) = -V_0 sech²(ξ/a)

**Sweep:** V_0 ∈ [1, 30], a ∈ [0.5, 2.0], α = 2π

**FIGURE SLOT:** `FIGURES/phase_diagram_poschl_teller.png`

**TABLE SLOT:** `TABLES/phase_table_poschl_teller.csv`

| V_0 | a | N_bound | λ_0 | λ_1 | λ_2 | gap_3 | gap_4 |
|-----|---|---------|-----|-----|-----|-------|-------|
| | | | | | | | |

**N=3 Region:**
- [ ] Blob postoji
- [ ] Kompaktna regija (nije tanka krivulja)
- [ ] Gap margins > 5%

---

### E.2 Volcano (Warp Localization)

**Formula:** V(ξ) = V_0 [ξ²/(ξ² + a²) - 1]

**Sweep:** V_0 ∈ [_____, _____], a ∈ [_____, _____]

**FIGURE SLOT:** `FIGURES/phase_diagram_volcano.png`

**TABLE SLOT:** `TABLES/phase_table_volcano.csv`

**N=3 Region:** [ ] Exists / [ ] Does not exist

---

### E.3 Compact Well (Box)

**Formula:** V(ξ) = -V_0 za ξ ∈ [0,1], else 0

**FIGURE SLOT:** `FIGURES/phase_diagram_box.png`

**TABLE SLOT:** `TABLES/phase_table_box.csv`

**N=3 Region:** [ ] Exists / [ ] Does not exist

---

### E.4 Double-Well

**Formula:** V(ξ) = -V_0 [sech²(ξ-d) + sech²(ξ+d)]

**FIGURE SLOT:** `FIGURES/phase_diagram_double_well.png`

**TABLE SLOT:** `TABLES/phase_table_double_well.csv`

**N=3 Region:** [ ] Exists / [ ] Does not exist

---

### E.5 Exponential Tail

**Formula:** V(ξ) = -V_0 exp(-ξ/a)

**FIGURE SLOT:** `FIGURES/phase_diagram_exponential.png`

**TABLE SLOT:** `TABLES/phase_table_exponential.csv`

**N=3 Region:** [ ] Exists / [ ] Does not exist

---

### E.6 Summary: Best Candidates for N=3

| Candidate | N=3 Exists? | Blob Size | Gap Margin | Robustness |
|-----------|-------------|-----------|------------|------------|
| Pöschl-Teller | | | | |
| Volcano | | | | |
| Box | | | | |
| Double-Well | | | | |
| Exponential | | | | |

**Best candidate:** [Popuniti]

---

## F. RESULTS: PHYSICAL V(z) (Derived)

> **Status:** [OPEN] — V(z) još nije deriviran iz 5D akcije

### F.1 Placeholder

Kada V(z) bude deriviran (Track A):

**Formula:** V(z) = V_warp + V_mass + V_coupling = [OPEN]

**Parameters from membrane:** σ = _____, r_e = _____, R_ξ = _____

**FIGURE SLOT:** `FIGURES/phase_diagram_physical.png`

**N_bound:** [OPEN]

---

## G. OUTPUT OBJECTS (Contract Compliance)

### G.1 N_bound

| Field | Value |
|-------|-------|
| Definition | Number of λ_n < λ_th |
| Threshold λ_th | [intrinsic, NOT PDG] |
| Value | N_bound = _____ |
| Error | Exact integer; stable under V0-V2 |
| Robustness | See Section E.X |
| Sensitivity | ΔN under α±10%: _____ |

### G.2 x₁ (First Eigenvalue)

| Field | Value |
|-------|-------|
| Definition | |λ_0| (ground state) |
| Value | x₁ = _____ |
| Error bar | x₁ ± _____ (from grid refinement) |
| BC dependence | dx₁/dα = _____ at α = 2π |
| V0-V2 status | [ ] PASS |

### G.3 I₄ (Overlap Integral)

| Field | Value |
|-------|-------|
| Definition | I₄ = ∫|ψ_0|⁴ dξ |
| Value | I₄ = _____ |
| Error | I₄ ± _____ |
| Convergence | [ ] Asymptote reached |

**FIGURE SLOT:** `FIGURES/I4_convergence.png`

### G.4 ψ_n(z) (Mode Profiles)

| n | Normalization | Orthogonality | BC Check | Nodes |
|---|---------------|---------------|----------|-------|
| 0 | [ ] OK | — | [ ] OK | 0 |
| 1 | [ ] OK | [ ] OK | [ ] OK | 1 |
| 2 | [ ] OK | [ ] OK | [ ] OK | 2 |

**FIGURE SLOT:** `FIGURES/mode_profiles.png`

---

## H. FAILURE MODES & TRIAGE

| ID | Failure | If Occurs | Triage |
|----|---------|-----------|--------|
| F1 | V0 benchmark FAIL | Solver bug | Debug discretization |
| F2 | V1 cross-method FAIL | Method-dependent artifact | Compare implementations |
| F3 | V2 grid instability | Poor convergence | Increase grid / use spectral |
| F4 | N_bound ≠ 3 for all V(z) | Model tension | Document; check BCs |
| F5 | Fine-tuning detected | θ* on boundary | Report as YELLOW, not GREEN |
| F6 | Gap margin < 1% | Near-critical | Flag as fragile |

---

## I. EXTERNAL COMPARISON (Optional, Post-Hoc)

> **DISCLAIMER:** Ove PDG vrijednosti NISU korištene kao input.
> Prikazane su isključivo za informativnu usporedbu NAKON što su BVP outputi izračunati.

| Quantity | BVP Output | PDG Value | Discrepancy |
|----------|------------|-----------|-------------|
| N_gen | N_bound = _____ | 3 | |
| [Other] | | | |

---

## J. APPENDICES

### J.1 Run Manifest

```yaml
git_commit: [hash]
date: [YYYY-MM-DD HH:MM]
machine: [hostname]
python_version: [X.Y.Z]
numpy_version: [X.Y.Z]
scipy_version: [X.Y.Z]
```

See `run_manifest_template.yml` for full format.

### J.2 Parameter Grids

**TABLE SLOT:** `TABLES/parameter_grid_full.csv`

### J.3 Raw Output Files

| File | Description |
|------|-------------|
| `TABLES/eigenvalues_all.csv` | All computed eigenvalues |
| `TABLES/phase_transitions.csv` | N_bound transition points |
| `FIGURES/*.png` | All generated figures |

---

*Report generated: [timestamp]*
*Template version: 1.0*
