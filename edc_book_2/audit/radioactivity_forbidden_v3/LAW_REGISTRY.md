# LAW REGISTRY V3: Confirmed Laws and Generalizations

**Created**: 2026-01-31
**Purpose**: Consolidated registry of all EDC laws for radioactivity
**Citation**: All entries traced to DONOR_TRACEBACK.md

---

## Part A: Confirmed Laws [Der]/[I]/[Cal]

### LAW-1: Coordination Law [Der]

**Citation**: DN-001, DN-002, DN-003

**Statement**:
```
n is ALLOWED iff n = 2^a × 3^b for non-negative integers a, b
```

**Equivalent formulations**:
- n ∈ {1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, ...}
- n has no prime factors > 3
- n is 3-smooth

**Origin**: Z₆ = Z₂ × Z₃ brane geometry

**Status**: [Der] — derived from fundamental symmetry

---

### LAW-2: Nuclear Saturation Optimum [Der]

**Citation**: DN-010, DN-011

**Statement**:
```
n_opt ≈ 43.3 for nuclear matter at E/A = -16 MeV, ρ₀ ≈ 0.16 fm⁻³
```

**Paradox**: 43 is prime > 3, hence FORBIDDEN

**Consequence**: Heavy nuclei exist in topologically frustrated state

**Status**: [Der] — derived from nuclear density

---

### LAW-3: Frustration-Corrected Geiger-Nuttall [I]

**Citation**: DN-015, DN-016, DN-017

**Statement**:
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b

Coefficients (from actinide fit):
  a = 1.63
  c = -2.40
  b = -42.1
  R² = 0.9941
```

**Improvement**: 44.7% better fit than standard G-N law

**Gap**: ε_f(A) functional form unspecified (GAP-R1)

**Status**: [I] — inferred from fit quality

---

### LAW-4: Effective Barrier Formula [Der]

**Citation**: DN-020, DN-021

**Statement**:
```
ΔV_eff = ΔV + 6K × q_barrier²

With K ≈ 0.94 MeV, q_barrier = 0.5:
  ΔV_eff ≈ 2.7 MeV for n ≈ 43
```

**Interpretation**: Topological correction to Coulomb barrier

**Gap**: Generalization to other n values (GAP-R5)

**Status**: [Der] for n ≈ 43

---

### LAW-5: Pinning Constant Formula [Der]/[Cal]

**Citation**: DN-023, DN-024

**Statement**:
```
K = f × σ × A_contact

Parameters:
  σ = 8.82 MeV/fm² (surface tension)
  f ≈ 0.3 (phenomenological)
  A_contact ~ 0.3 fm²

Result: K ≈ 0.8–0.94 MeV
```

**Gap**: Origin of f ≈ 0.3 unexplained (GAP-R2)

**Status**: [Der] for formula, [Cal] for f value

---

### LAW-6: α-Cluster Binding [I]

**Citation**: DN-025, DN-026

**Statement**:
```
B.E.(nα) = n × B.E.(α) + n_bonds × E_αα

Accuracy:
  C-12: 92.0 vs 92.2 MeV (−0.2%)
  O-16: 127.3 vs 127.6 MeV (−0.2%)
```

**Interpretation**: Light nuclei as α-clusters with inter-cluster bonds

**Status**: [I] — works for light nuclei

---

## Part B: Proposed Generalizations [P]

### GEN-1: Forbidden Distance Metric [P]

**Statement**:
```
d(n) = min{ |n - m| : m = 2^a × 3^b }
```

**Hypothesis**: d(n) correlates with instability (lifetime, decay mode)

**Falsification**: If d(n) doesn't predict τ, reject

**Status**: [P] — not in original sources

---

### GEN-2: ε_f(A) Ansatz [P]

**Statement**:
```
ε_f(A) = κ × d(n(A))^α

Simplest form: ε_f(A) ∝ d(n(A))
```

**Purpose**: Close GAP-R1 (ε_f functional form)

**Requirement**: Need n(A) formula first (OQ-V3-001)

**Status**: [P] — proposed to close gap

---

### GEN-3: Mode Selection from d(n) [P]

**Statement**:
```
| d(n) Direction       | Predicted Mode |
|----------------------|----------------|
| n slightly above 36  | β⁺/EC (reduce) |
| n far from allowed   | α (large Δn)   |
| n slightly below 48  | β⁻ (increase)  |
| n >> 48              | Fission        |
```

**Falsification**: Compare with observed branching ratios

**Status**: [P] — no direct source support

---

### GEN-4: Metastable M-Structures [P]

**Citation**: DN-028

**Statement**:
```
τ(M_n) ∝ exp(ΔV_eff(n) / kT)
```

**Interpretation**: Forbidden n values exist as short-lived metastable states

**Falsification**: If no isomer signatures → reject

**Status**: [P] — speculative extension

---

### GEN-5: Chain Termination at Allowed n [P]

**Statement**:
```
Decay chains end when n(A) reaches allowed value

Evidence:
  U-238 → ²⁰⁶Pb (stable)
  Th-232 → ²⁰⁸Pb (stable)
  U-235 → ²⁰⁷Pb (stable)

Hypothesis: n(206), n(207), n(208) ≈ 36 (allowed)
```

**Falsification**: If n(Pb) ≠ allowed, reject

**Status**: [P] — plausible, needs n(A) calculation

---

## Part C: Supernova Hypothesis [P]

**Citation**: None (grep returned 0 matches for "supernova")

**Statement**:
```
Supernova / extreme gravity → nuclei compressed into forbidden n
→ decay chains as relaxation back to allowed values
```

**Mechanism [P]**:
1. High density: ρ >> ρ₀ in supernova/neutron star
2. Compression: n(ρ) pushed beyond equilibrium
3. Forbidden zone: n > 48 (deep forbidden)
4. Relaxation: Decay toward allowed n when pressure released
5. Observable: r-process heavy element synthesis

**What would make it [Der]**:
1. Derive n(ρ) from nuclear equation of state
2. Show r-process nuclei have n > 48 initially
3. Derive decay sequence from frustration relaxation
4. Match to observed r-process abundances

**Status**: [P] — no source support, interesting speculation

---

## Part D: Gap Registry

| ID | Gap | What's Missing | Priority |
|----|-----|----------------|----------|
| GAP-R1 | ε_f(A) form | Functional dependence on A | HIGH |
| GAP-R2 | f ≈ 0.3 origin | Why this value? | LOW |
| GAP-R3 | Prefactor A | Gamow prefactor derivation | MEDIUM |
| GAP-R4 | Y-junction proof | Topological proof | LOW |
| GAP-R5 | ΔV_eff general | Extension beyond n ≈ 43 | MEDIUM |
| GAP-R6 | Domain signature | Experimental observable | LOW |

---

## Summary Table

| ID | Statement | Status | Citation |
|----|-----------|--------|----------|
| LAW-1 | n = 2^a × 3^b allowed | [Der] | DN-001..003 |
| LAW-2 | n_opt ≈ 43.3 | [Der] | DN-010..011 |
| LAW-3 | Frustration-corrected G-N | [I] | DN-015..017 |
| LAW-4 | ΔV_eff = ΔV + 6Kq² | [Der] | DN-020..021 |
| LAW-5 | K = f × σ × A | [Der]/[Cal] | DN-023..024 |
| LAW-6 | α-cluster B.E. | [I] | DN-025..026 |
| GEN-1 | d(n) metric | [P] | New |
| GEN-2 | ε_f ∝ d(n) | [P] | New |
| GEN-3 | Mode selection | [P] | New |
| GEN-4 | Metastable M | [P] | DN-028 |
| GEN-5 | Chain termination | [P] | New |
| SN-1 | Supernova hypothesis | [P] | None |
