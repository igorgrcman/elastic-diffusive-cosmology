# OPEN QUESTIONS V4

**Created**: 2026-01-31
**Purpose**: Research gaps blocking progress
**Inherits**: V3 OPEN_QUESTIONS.md

---

## Critical Questions (Block Progress)

### OQ-V4-001: n(A) Formula [KINGPIN]

**Question**: What is the exact formula for n as function of A?

**Candidate [P]**: n(A) = 6.1 × A^(1/3)

**Why kingpin**:
- Required for ε_f(A) calculation
- Required for d(n) along chains
- Required for branching predictions
- Blocks TEST-4, TEST-9

**Upgrade path**:
- [P] → [I]: Verify on all 3 chains + stable nuclei
- [I] → [Der]: Derive c = 6.1 from M-topology

**Status**: [Open]
**Priority**: CRITICAL

---

### OQ-V4-002: ε_f(A) Functional Form [GAP-R1]

**Question**: What is frustration energy ε_f as function of A?

**Candidates [P]**:
1. ε_f = κ × d(n(A))
2. ε_f = κ × d(n)^α
3. ε_f from LAW-4: ΔV_eff(n)

**Dependencies**: Requires OQ-V4-001

**Status**: [Open]
**Priority**: HIGH

---

### OQ-V4-003: M5/M6 Source Support

**Question**: Are M5 (quasicrystal) and M6 (core-mantle) mechanisms supported by sources?

**Current status**:
- M5: No source found (grep returned 0 for quasicrystal)
- M6: Partial support (DN-051, DN-085)

**Resolution**: Either find sources or keep [P]

**Status**: [Open]
**Priority**: MEDIUM

---

## Structural Questions

### OQ-V4-004: Why All Pb Isotopes Stable?

**Question**: Why are ²⁰⁶Pb, ²⁰⁷Pb, ²⁰⁸Pb all stable?

**EDC hypothesis [P]**:
- n(206) ≈ 36.0 (allowed)
- n(207) ≈ 36.1 (near allowed)
- n(208) ≈ 36.2 (near allowed)
- Z = 82 magic reinforces

**Test**: Verify n(A) gives ~36 for all three

**Status**: [Open]
**Priority**: MEDIUM

---

### OQ-V4-005: Fissility Criterion

**Question**: Does EDC predict which nuclei are fissile?

**Observation**: ²³⁵U fissile, ²³⁸U not

**Hypothesis [P]**:
- n(235) deeper in forbidden zone?
- Odd-A nuclei have different topology?

**Status**: [Open]
**Priority**: MEDIUM

---

### OQ-V4-006: Branching Ratio Prediction

**Question**: Can EDC quantitatively predict branching ratios?

**Current**: Qualitative only (H1-H5 in 10_BRANCHING_RULES)

**Needed**: Q-value data, n(A) verification

**Status**: [Open]
**Priority**: MEDIUM

---

### OQ-V4-007: f ≈ 0.3 Origin [GAP-R2]

**Question**: Why is phenomenological factor f ≈ 0.3 in LAW-5?

**Candidates [P]**:
- f = 1/(2π) ≈ 0.16
- f = 1/√12 ≈ 0.29 (from packing)
- f = 1/3 (geometric)

**Citation**: DN-055

**Status**: [Open]
**Priority**: LOW

---

### OQ-V4-008: Supernova Mechanism

**Question**: Does extreme gravity/pressure force nuclei into forbidden zone?

**Source search**: 0 matches for "supernova", "r-process", "nucleosynthesis"

**Status**: [P] with no source support
**Priority**: LOW (interesting but speculative)

---

### OQ-V4-009: Domain/Cluster Signature

**Question**: What experimental observable would confirm M1/M3 mechanisms?

**Candidates**:
- NMR line broadening (domains)
- Neutron scattering (α-clusters)
- X-ray diffuse (defects)

**Status**: [Open]
**Priority**: LOW

---

### OQ-V4-010: Shell Effects in n(A)

**Question**: Do magic numbers (Z=82, N=126) modify n(A)?

**Hypothesis [P]**:
- n(A) = n_bulk(A) + Δn_shell(Z, N)
- Shell closure → Δn toward allowed

**Status**: [Open]
**Priority**: MEDIUM

---

## Resolution Priority

| Priority | Questions | Blocking |
|----------|-----------|----------|
| CRITICAL | OQ-V4-001 | Yes (kingpin) |
| HIGH | OQ-V4-002 | Depends on 001 |
| MEDIUM | OQ-V4-003,4,5,6,10 | No |
| LOW | OQ-V4-007,8,9 | No |

---

## Dependency Chain

```
OQ-V4-001 (n(A) formula)
    ↓
OQ-V4-002 (ε_f form)
    ↓
OQ-V4-006 (branching prediction)
    ↓
TEST-4, TEST-5 (falsification)
```

---

## V3 → V4 Question Evolution

| V3 ID | Status in V4 |
|-------|--------------|
| OQ-V3-001 | → OQ-V4-001 (still kingpin) |
| OQ-V3-002 | → OQ-V4-002 (still open) |
| OQ-V3-003 | → OQ-V4-006 (refined) |
| OQ-V3-004 | → OQ-V4-004 (refined) |
| OQ-V3-005 | → OQ-V4-005 (unchanged) |

New in V4: OQ-V4-003 (M5/M6), OQ-V4-010 (shell effects)
