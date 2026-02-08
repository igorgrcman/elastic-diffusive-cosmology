# LAW MINING AND INVARIANTS V2

**Generated**: 2026-01-31
**Purpose**: Confirmed laws from sources + new generalizations

---

## A) Confirmed from Mined Sources

### LAW-1: Coordination Law [Der]

**Citation**: [DN-001] 22826edd_full.md:2440-2540

```
n is ALLOWED iff n = 2^a × 3^b for non-negative integers a, b
```

**Source quote**:
> "Dopušteno: n ∈ {6, 8, 9, 12}"
> "Zabranjeno: n = 5, 7, 11, ... (prosti > 3)"

**Status**: [Der] from Z₆ = Z₂ × Z₃ geometry

---

### LAW-2: Nuclear Saturation Optimum [Der]

**Citation**: [DN-010, DN-011] 22826edd_full.md:11793-11856

```
n_opt ≈ 43.3 for nuclear matter at E/A = -16 MeV
```

**Source quote**:
> "Optimalno: n ≈ 43.3"
> "Ali 43 je ZABRANJEN (prost broj > 3)!"

**Status**: [Der] from nuclear density ρ₀ ≈ 0.16 fm⁻³

---

### LAW-3: Frustration-Corrected Geiger-Nuttall [I]

**Citation**: [DN-015, DN-017] 22826edd_full.md:2555-2610

```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b
a = 1.63, c = -2.40, b = -42.1
R² = 0.9941 (44.7% improvement)
```

**Status**: [I] - Inferred from fit quality
**Note**: ε_f(A) functional form not specified (GAP-R1)

---

### LAW-4: Barrier Formula [Der]

**Citation**: [DN-020, DN-021] 22826edd_full.md:7322-7390

```
ΔV_eff = ΔV + 6K × q_barrier²
```

With K ≈ 0.94 MeV, q_barrier = 0.5, giving ΔV_eff ≈ 2.7 MeV

**Status**: [Der] for n ≈ 43
**Open**: Generalization to other n (GAP-R5)

---

### LAW-5: Pinning from Surface Tension [Der/Cal]

**Citation**: [DN-023, DN-024] 22826edd_full.md:10915-11072

```
K = f × σ × A_contact
σ = 8.82 MeV/fm², f ≈ 0.3, K ≈ 0.8-0.94 MeV
```

**Status**: [Der]/[Cal] - formula derived, f phenomenological (GAP-R2)

---

### LAW-6: α-Cluster Binding [I]

**Citation**: [DN-025, DN-026] 22826edd_full.md:2452-2453

```
B.E.(nα) = n × B.E.(α) + n_bonds × E_αα
C-12: 92.0 vs 92.2 MeV (−0.2% error)
O-16: 127.3 vs 127.6 MeV (−0.2% error)
```

**Status**: [I] - works for light nuclei

---

## B) New Generalizations [P]

### GENERALIZATION-1: Forbidden Distance Metric

**Proposed**:
```
d(n) = min{ |n - m| : m = 2^a × 3^b }
```

**Hypothesis**: d(n) correlates with instability.

**Status**: [P] - Not in original sources
**Falsification**: If d(n) doesn't correlate with τ, reject

---

### GENERALIZATION-2: ε_f(A) Ansatz

**Proposed**:
```
ε_f(A) = κ × d(n(A))^α
```

Simplest: ε_f(A) ∝ d(n(A))

**Status**: [P] - Proposed to close GAP-R1
**Verification**: Check if this form gives R² ≈ 0.9941

---

### GENERALIZATION-3: Mode Selection from d(n) Direction

**Proposed**:

| d(n) Direction | Predicted Mode |
|----------------|----------------|
| n slightly above allowed | β⁺/EC (reduce n) |
| n far from both | α (large Δn) |
| n slightly below next allowed | β⁻ (increase n) |
| n >> next allowed | Fission |

**Status**: [P] - No source support
**Falsification**: Compare with actual branching ratios

---

### GENERALIZATION-4: Metastable M-Structures

**Proposed**: Forbidden n values exist as short-lived metastable states.

**Citation**: [DN-027, DN-028] 73d92ff5_full.md:442, 517 (mentions "metastable")

```
τ(M_n) ∝ exp(ΔV_eff(n) / kT)
```

**Status**: [P] - Speculative extension
**Falsification**: No isomer signatures → reject

---

### GENERALIZATION-5: Chain Termination at Allowed n

**Proposed**: Decay chains end when n(A) reaches allowed value.

**Evidence**:
- U-238 → ²⁰⁶Pb (stable)
- Th-232 → ²⁰⁸Pb (stable)
- U-235 → ²⁰⁷Pb (stable)

**Hypothesis**: n(206), n(207), n(208) ≈ 36 (allowed)

**Status**: [P] - Plausible, needs n(A) calculation
**Falsification**: If n(Pb) ≠ allowed, reject

---

## C) Supernova Hypothesis [P]

**Igor's hypothesis**:
> "Supernova / ekstremna gravitacija nabije jezgre u forbidden konfiguracije → raspad kao relaksacija"

### Minimal Mechanism [P]

1. **High density**: ρ >> ρ₀ in supernova/neutron star
2. **Compression**: n(ρ) increases beyond equilibrium value
3. **Forbidden zone**: n pushed deep into forbidden region (e.g., n > 48)
4. **Relaxation**: When pressure released, nuclei decay toward allowed n
5. **Observable**: Heavy element synthesis in r-process

### Formalization [P]

```
n(ρ) = n₀ × (ρ/ρ₀)^(1/3)    (approximate scaling)

At ρ = 10 × ρ₀:
n ≈ 43 × 10^(1/3) ≈ 93

But 93 = 3 × 31 contains prime 31 → FORBIDDEN
```

**Status**: [P] - No source support (grep found 0 matches for "supernova")
**Note**: Not in any mined session

### What Would Make It [Der]

1. Derive n(ρ) from nuclear equation of state
2. Show that r-process nuclei have n > 48 initially
3. Derive decay sequence from frustration relaxation
4. Match to observed r-process abundances

---

## D) Explaining Different Decay Paths

### Why α vs β⁻?

**Proposed framework [P]**:

| Condition | Favored Mode | Mechanism |
|-----------|--------------|-----------|
| n < n_opt (underbinding) | β⁻ | Increase N/Z → increase n |
| n > n_opt (overbinding) | β⁺/EC | Decrease N/Z → decrease n |
| n far from any allowed | α | Remove 4 nucleons → large Δn |
| n >> 48 | Fission | Split into two allowed chunks |

**Source support**: Limited
- [DN-033] 98cc5184_snippets.json:295 mentions "Junction relaxation: weak decay"
- No explicit mode selection formula

---

### Why Different Paths in Same Chain?

Example: U-238 chain has 8 α and 6 β⁻

**Hypothesis [P]**:
- α-steps: large frustration relief (Δn ~ -4)
- β⁻-steps: fine-tuning N/Z between α-steps
- Pattern: (α)(β⁻β⁻)(α)(α)... with β⁻ "interludes"

**Interpretation [P]**:
- After α-decay, N/Z ratio may be "wrong" for next α
- β⁻ adjusts ratio before next α is energetically favorable
- Alternation reflects multi-dimensional optimization (A and N/Z)

---

### Why Branching at Certain Points?

**Observed**: ²¹²Bi has 64/36 branching; ²¹¹Bi has 99.7/0.3

**Hypothesis [P]**:
- Branching occurs when modes are nearly degenerate
- ²¹²Bi: n(212) is near equidistant from 36 and 48
- ²¹¹Bi: n(211) strongly favors α

**Prediction [P]**: Plot branching ratio vs d(n) → should see correlation

---

## E) Summary: Laws/Invariants Status

| ID | Statement | Status | Citation |
|----|-----------|--------|----------|
| LAW-1 | n = 2^a × 3^b allowed | [Der] | DN-001 |
| LAW-2 | n_opt ≈ 43.3 | [Der] | DN-010, DN-011 |
| LAW-3 | Frustration-corrected G-N | [I] | DN-015, DN-017 |
| LAW-4 | ΔV_eff = ΔV + 6Kq² | [Der] | DN-020, DN-021 |
| LAW-5 | K = f × σ × A | [Der]/[Cal] | DN-023, DN-024 |
| LAW-6 | α-cluster B.E. formula | [I] | DN-025, DN-026 |
| GEN-1 | d(n) metric | [P] | New |
| GEN-2 | ε_f(A) ∝ d(n(A)) | [P] | New |
| GEN-3 | Mode from d(n) direction | [P] | New |
| GEN-4 | Metastable M-structures | [P] | DN-027, DN-028 |
| GEN-5 | Chains end at allowed n | [P] | New |
| SN-1 | Supernova → forbidden → decay | [P] | No source |
