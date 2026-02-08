# OPEN QUESTIONS V3: Research Gaps and Unknowns

**Created**: 2026-01-31
**Purpose**: Track unresolved questions with upgrade paths

---

## Critical Questions (Block Progress)

### OQ-V3-001: n(A) Formula [KINGPIN]

**Question**: What is the exact formula for coordination number n as function of mass number A?

**Current state**:
- n_opt ≈ 43.3 at nuclear saturation [Der] from DN-010
- n(A) functional form not specified in sources

**Source references**:
- 22826edd_full.md:11793-11856 mentions n ≈ 43.3
- No explicit n(A) = f(A, Z, ρ) formula found

**Candidates [P]**:
1. n(A) = n₀ × (ρ(A)/ρ₀)^(1/3) — density-based
2. n(A) = c × A^(1/3) — geometric scaling
3. n(A) = f(N, Z) — isospin-dependent

**Upgrade path**:
- [P] → [I]: If any formula predicts observed decay patterns
- [I] → [Der]: If derivable from M-topology axioms

**Priority**: CRITICAL — unlocks chain verification

---

### OQ-V3-002: ε_f(A) Functional Form

**Question**: How does frustration energy ε_f depend on A?

**Current state**:
- ε_f appears in G-N law: log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b [I]
- c = -2.40 [Cal] from fit (DN-017)
- ε_f(A) functional form is GAP-R1

**Candidates [P]**:
1. ε_f(A) = κ × d(n(A)) — linear in forbidden distance
2. ε_f(A) = κ × d(n(A))^α — power law
3. ε_f(A) = κ × exp(−d(n(A))/d₀) — exponential

**Upgrade path**:
- Need n(A) formula first (OQ-V3-001)
- Then fit ε_f(A) to lifetime data

**Priority**: HIGH — depends on OQ-V3-001

---

### OQ-V3-003: Branching Ratio Prediction

**Question**: Can EDC predict branching ratios at bifurcation points?

**Cases**:
- ²¹²Bi: 64% β⁻ / 36% α
- ²¹¹Bi: 99.7% α / 0.3% β⁻
- ²²⁷Ac: 98.6% β⁻ / 1.4% α

**Hypothesis [P]**: Branching correlates with d(n) direction
- If n slightly above allowed → β⁻ favored
- If n far from allowed → α favored

**Falsification**: Compare predicted vs observed ratios once n(A) known

**Priority**: MEDIUM

---

## Structural Questions

### OQ-V3-004: Why 3 Stable Pb Endpoints?

**Question**: Why are ²⁰⁶Pb, ²⁰⁷Pb, ²⁰⁸Pb all stable?

**EDC hypothesis [P]**:
- n(206), n(207), n(208) all ≈ 36 (allowed)
- Shell effects (Z=82 magic, N=124-126) reinforce stability

**Test**: Calculate n(A) for A=206,207,208

**Priority**: MEDIUM

---

### OQ-V3-005: Fissility Criterion

**Question**: Does EDC predict which nuclei are fissile?

**Observation**: ²³⁵U is fissile, ²³⁸U is not

**Hypothesis [P]**:
- Fissile nuclei have n(A) deeper in forbidden zone
- Fission = splitting into two "allowed" chunks
- Odd-A nuclei may have different n(A) characteristics

**No source support**: Speculative

**Priority**: LOW (interesting but not blocking)

---

### OQ-V3-006: f ≈ 0.3 Origin (GAP-R2)

**Question**: Why is the phenomenological factor f ≈ 0.3 in K = f × σ × A_contact?

**Current state**:
- K ≈ 0.8-0.94 MeV [Cal]
- σ = 8.82 MeV/fm² [Der] from nuclear surface tension
- f ≈ 0.3 is fitted [Cal]

**Candidates [P]**:
1. f = 1/3 from geometric factor
2. f = effective coverage fraction
3. f = quantum correction factor

**Priority**: LOW (doesn't block main results)

---

### OQ-V3-007: Domain Mixing Signature (GAP-R6)

**Question**: What experimental signature would confirm domain mixing?

**Current state**:
- Domain mixing proposed as escape mechanism [I]
- Source: 22826edd_full.md:2479-2492

**Candidates**:
- NMR line broadening
- X-ray diffuse scattering
- Neutron scattering anomalies

**Priority**: LOW (experimental, not theoretical)

---

## Crystal/Lattice Questions

### OQ-V3-008: Allowed vs Forbidden Lattices

**Question**: Which crystal structures have allowed vs forbidden coordination?

**Allowed (n = 2^a × 3^b)**:
- FCC: n = 12 = 4 × 3 ✓
- BCC: n = 8 = 2³ ✓
- Simple cubic: n = 6 = 2 × 3 ✓

**Forbidden**:
- n = 5 (no standard lattice)
- n = 7 (no standard lattice)
- n = 11 (no standard lattice)

**Question**: Do any real materials have forbidden coordination?

**Priority**: MEDIUM (crystal add-on scope)

---

### OQ-V3-009: Quasicrystal Status

**Question**: How do quasicrystals (5-fold symmetry) fit into EDC?

**Current state**: No source support found in mined sessions

**Hypothesis [P]**: Quasicrystals might be topologically forbidden but stabilized by electronic effects

**Priority**: LOW (no source coverage)

---

## Resolved from V2

| V2 ID | Question | Resolution |
|-------|----------|------------|
| OQ-V2-001 | Where is forbidden zone? | n ∈ [37, 47] — see FORBIDDEN_CATALOG |
| OQ-V2-002 | Citation format? | D-V3-001: file:line-range |
| OQ-V2-003 | Decay chains complete? | Yes, 3 chains to stable Pb |

---

## Priority Summary

| Priority | Questions | Blocking? |
|----------|-----------|-----------|
| CRITICAL | OQ-V3-001 (n(A)) | Yes — kingpin |
| HIGH | OQ-V3-002 (ε_f) | Depends on 001 |
| MEDIUM | OQ-V3-003, 004, 008 | No |
| LOW | OQ-V3-005, 006, 007, 009 | No |
