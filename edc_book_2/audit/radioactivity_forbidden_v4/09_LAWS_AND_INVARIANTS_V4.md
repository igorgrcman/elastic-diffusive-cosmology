# LAWS AND INVARIANTS V4

**Created**: 2026-01-31
**Purpose**: Consolidated law registry with formal statements and falsification ledger
**Inherits**: V3 LAW_REGISTRY.md

---

## Part A: Confirmed Laws

### LAW-1: Coordination Law [Der]

**Formal Statement**:
```
∀n ∈ ℤ⁺: n is ALLOWED ⟺ n = 2^a × 3^b for a,b ∈ ℤ≥0
```

**Dependencies**: None (axiom from Z₆ = Z₂ × Z₃ symmetry)

**Citation**: DN-001, DN-002, DN-003

**Consequence**: Allowed = {1,2,3,4,6,8,9,12,16,18,24,27,32,36,48,...}

**Status**: [Der]

---

### LAW-2: Nuclear Saturation Optimum [Der]

**Formal Statement**:
```
At ρ = ρ₀ ≈ 0.16 fm⁻³, E/A = -16 MeV:
n_opt ≈ 43.3

But 43 is prime > 3, hence FORBIDDEN by LAW-1
```

**Dependencies**: LAW-1

**Citation**: DN-010, DN-011

**Consequence**: Heavy nuclei are topologically frustrated (M43 paradox)

**Status**: [Der]

---

### LAW-3: Frustration-Corrected Geiger-Nuttall [I]

**Formal Statement**:
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b

Fitted: a = 1.63, c = -2.40, b = -42.1
R² = 0.9941
```

**Dependencies**: ε_f(A) functional form (GAP-R1)

**Citation**: DN-015, DN-016, DN-017

**Status**: [I]

---

### LAW-4: Effective Barrier Formula [Der]

**Formal Statement**:
```
ΔV_eff = ΔV + 6K × q_barrier²

For n ≈ 43: K ≈ 0.94 MeV, q = 0.5 → ΔV_eff ≈ 2.7 MeV
```

**Dependencies**: LAW-2 (for n ≈ 43)

**Citation**: DN-020, DN-021

**Status**: [Der] for n ≈ 43; [Open] for general n

---

### LAW-5: Pinning Constant [Der/Cal]

**Formal Statement**:
```
K = f × σ × A_contact

σ = 8.82 MeV/fm² (surface tension)
f ≈ 0.3 (phenomenological)
→ K ≈ 0.8-0.94 MeV
```

**Dependencies**: Surface tension σ from nuclear physics

**Citation**: DN-023, DN-024

**Status**: [Der] for formula, [Cal] for f

---

### LAW-6: α-Cluster Binding [I]

**Formal Statement**:
```
B.E.(nα) = n × B.E.(α) + n_bonds × E_αα

Accuracy: C-12 -0.2%, O-16 -0.2%
```

**Dependencies**: None

**Citation**: DN-025, DN-026

**Status**: [I] — works for light nuclei

---

## Part B: Proposed Generalizations

### GEN-1: Forbidden Distance Metric [P]

**Statement**:
```
d(n) = min{ |n - m| : m = 2^a × 3^b }
```

**Status**: [P]

---

### GEN-2: ε_f Scaling [P]

**Statement**:
```
ε_f(A) = κ × d(n(A))^α
Simplest: ε_f ∝ d(n)
```

**Dependencies**: GEN-1, n(A) formula

**Status**: [P]

---

### GEN-3: Mode Selection [P]

**Statement**:
```
d(n) < 2  → β preferred (domain mixing)
d(n) 2-4 → α/β competitive
d(n) > 4  → α preferred (cluster escape)
d(n) = 6  → α or SF (maximum stress)
```

**Status**: [P]

---

### GEN-4: d(n) Monotonic Decrease [P]

**Statement**:
```
Along any decay chain: d(n_{step+1}) ≤ d(n_{step})
```

**Evidence**:
- U-238 chain: 1.8 → 1.6 → ... → 0.0 ✓
- Th-232 chain: 1.5 → 1.3 → ... → 0.2 ✓
- U-235 chain: 1.6 → 1.4 → ... → 0.1 ✓

**Status**: [P] → could be [I] if verified on more chains

---

### GEN-5: Chain Termination at Allowed n [P]

**Statement**:
```
Decay chains terminate when n(A) ≈ n_allowed

Evidence:
n(206) ≈ 36 → ²⁰⁶Pb stable
n(207) ≈ 36 → ²⁰⁷Pb stable
n(208) ≈ 36 → ²⁰⁸Pb stable
```

**Status**: [P]

---

### GEN-6: n(A) Geometric Scaling [P]

**Statement**:
```
n(A) = c × A^(1/3)
c ≈ 6.1 (calibrated to Pb-206)
```

**Status**: [P] — candidate formula

---

## Part C: Falsification Ledger (8+ Tests)

### TEST-1: Periodic Crystal with n=5

**Prediction**: No stable periodic crystal has bulk coordination n=5
**Falsification**: Find such a crystal
**Current status**: Not falsified (no counterexample)
**Priority**: HIGH

---

### TEST-2: n_opt ≠ 43

**Prediction**: Nuclear saturation optimum is n ≈ 43 (forbidden)
**Falsification**: Show n_opt is actually allowed (e.g., 36 or 48)
**Current status**: Not tested (requires EOS calculation)
**Priority**: HIGH

---

### TEST-3: d(n) Non-Monotonic in Chain

**Prediction**: d(n) decreases monotonically along decay chains
**Falsification**: Find chain where d(n) increases at some step
**Current status**: Not falsified (3 chains consistent)
**Priority**: MEDIUM

---

### TEST-4: Stable Nucleus with Forbidden n

**Prediction**: All stable heavy nuclei have n ≈ 36 or 48 (allowed)
**Falsification**: Find stable nucleus with n in forbidden zone
**Current status**: Not testable without n(A) formula
**Priority**: HIGH (requires OQ-V4-001)

---

### TEST-5: Branching Uncorrelated with d(n)

**Prediction**: Branching ratios correlate with d(n) direction
**Falsification**: Show no correlation across isotopes
**Current status**: Preliminary support (²¹²Bi, ²¹¹Bi, ²²⁷Ac)
**Priority**: MEDIUM

---

### TEST-6: G-N Fit Without ε_f

**Prediction**: Standard G-N law has lower R² than frustration-corrected
**Falsification**: Show comparable R² without ε_f term
**Current status**: Not falsified (44.7% improvement claimed)
**Priority**: MEDIUM

---

### TEST-7: α-Cluster Local n ≠ 12

**Prediction**: α-clusters have local coordination n = 12 (FCC-like)
**Falsification**: Measure n ≠ 12 in cluster
**Current status**: Not directly testable
**Priority**: LOW

---

### TEST-8: Defect Energy Non-Linear

**Prediction**: E_defect ∝ defect length (Nambu-Goto)
**Falsification**: Show E ∝ L² or other scaling
**Current status**: Not tested
**Priority**: LOW

---

### TEST-9: Fissility Uncorrelated with n(A)

**Prediction**: Fissile nuclei (²³⁵U) have n(A) deeper in forbidden zone than fissionable (²³⁸U)
**Falsification**: Show same n(A) for both
**Current status**: Not testable without n(A) formula
**Priority**: MEDIUM

---

### TEST-10: Quasicrystal Thermodynamically Stable

**Prediction**: Quasicrystals (n=5 local) are metastable, not true ground state
**Falsification**: Prove icosahedral QC is ground state
**Current status**: Ambiguous (QC stability debated)
**Priority**: LOW

---

## Part D: Dependency Graph

```
LAW-1 (Coordination)
   ↓
LAW-2 (Saturation) → M43 Paradox
   ↓
GEN-1 (d(n) metric)
   ↓
GEN-2 (ε_f scaling) ← requires n(A) formula [OQ-V4-001]
   ↓
LAW-3 (G-N law)
   ↓
GEN-3 (Mode selection)
   ↓
GEN-4 (d(n) monotonic)
   ↓
GEN-5 (Chain termination)
```

---

## Part E: Gap Registry

| ID | Gap | Status | Priority |
|----|-----|--------|----------|
| GAP-R1 | ε_f(A) form | [Open] | HIGH |
| GAP-R2 | f ≈ 0.3 origin | [Open] | LOW |
| GAP-R3 | Gamow prefactor | [Open] | MEDIUM |
| GAP-R4 | Y-junction proof | [Open] | LOW |
| GAP-R5 | ΔV_eff generalization | [Open] | MEDIUM |
| GAP-R6 | Domain signature | [Open] | LOW |
| GAP-R7 | n(A) derivation | [Open] | HIGH |
| GAP-R8 | M5/M6 source | [Open] | LOW |
