# DECAY CHAIN Th-232 V4: Thorium Series with EDC Blocks

**Created**: 2026-01-31
**Data Status**: t₁/₂ and Q marked [BL:SOURCE_TBD]
**Endpoint**: ²⁰⁸Pb (stable, doubly magic)

---

## Chain Skeleton

| Step | Parent | A | Z | Mode | Daughter | t₁/₂ | Q (MeV) |
|------|--------|---|---|------|----------|------|---------|
| 1 | ²³²Th | 232 | 90 | α | ²²⁸Ra | [BL] | [BL] |
| 2 | ²²⁸Ra | 228 | 88 | β⁻ | ²²⁸Ac | [BL] | [BL] |
| 3 | ²²⁸Ac | 228 | 89 | β⁻ | ²²⁸Th | [BL] | [BL] |
| 4 | ²²⁸Th | 228 | 90 | α | ²²⁴Ra | [BL] | [BL] |
| 5 | ²²⁴Ra | 224 | 88 | α | ²²⁰Rn | [BL] | [BL] |
| 6 | ²²⁰Rn | 220 | 86 | α | ²¹⁶Po | [BL] | [BL] |
| 7 | ²¹⁶Po | 216 | 84 | α | ²¹²Pb | [BL] | [BL] |
| 8 | ²¹²Pb | 212 | 82 | β⁻ | ²¹²Bi | [BL] | [BL] |
| 9A | ²¹²Bi | 212 | 83 | β⁻ (64%) | ²¹²Po | [BL] | [BL] |
| 9B | ²¹²Bi | 212 | 83 | α (36%) | ²⁰⁸Tl | [BL] | [BL] |
| 10A | ²¹²Po | 212 | 84 | α | ²⁰⁸Pb | [BL] | [BL] |
| 10B | ²⁰⁸Tl | 208 | 81 | β⁻ | ²⁰⁸Pb | [BL] | [BL] |
| END | ²⁰⁸Pb | 208 | 82 | STABLE | — | ∞ | — |

**Statistics**: 10 steps (with branching), 6α + 4β⁻, ΔA=24, ΔZ=8

---

## EDC Annotation Blocks

### Step 1: ²³²Th → ²²⁸Ra (α)
```
EDC BLOCK:
- n(232) ≈ 37.5 [P] using n = 6.1 × A^(1/3)
- d(n) = 1.5
- d(n) direction: ↓ decreasing
- Active mechanism: M3 (α-cluster), M4 (primordial metastable)
- Branching: N
- Notes: Primordial, t₁/₂ ~ 10¹⁰ y
```

### Step 2: ²²⁸Ra → ²²⁸Ac (β⁻)
```
EDC BLOCK:
- n(228) ≈ 37.3 [P]
- d(n) = 1.3
- d(n) direction: ~ (A unchanged)
- Active mechanism: M1 (domain mixing)
- Branching: N
- Notes: N/Z adjustment post-α
```

### Step 3: ²²⁸Ac → ²²⁸Th (β⁻)
```
EDC BLOCK:
- n(228) ≈ 37.3 [P]
- d(n) = 1.3
- d(n) direction: ~
- Active mechanism: M1
- Branching: N
- Notes: Second β⁻ completes adjustment
```

### Step 4: ²²⁸Th → ²²⁴Ra (α)
```
EDC BLOCK:
- n(228→224): 37.3 → 37.1 [P]
- d(n) = 1.1
- d(n) direction: ↓
- Active mechanism: M3
- Branching: N
```

### Step 5: ²²⁴Ra → ²²⁰Rn (α)
```
EDC BLOCK:
- n(224→220): 37.1 → 36.8 [P]
- d(n) = 0.8
- d(n) direction: ↓
- Active mechanism: M3
- Branching: N
```

### Step 6: ²²⁰Rn → ²¹⁶Po (α)
```
EDC BLOCK:
- n(220→216): 36.8 → 36.6 [P]
- d(n) = 0.6
- d(n) direction: ↓
- Active mechanism: M3
- Branching: N
- Notes: Thoron gas (short-lived)
```

### Step 7: ²¹⁶Po → ²¹²Pb (α)
```
EDC BLOCK:
- n(216→212): 36.6 → 36.4 [P]
- d(n) = 0.4
- d(n) direction: ↓
- Active mechanism: M3
- Branching: N
```

### Step 8: ²¹²Pb → ²¹²Bi (β⁻)
```
EDC BLOCK:
- n(212) ≈ 36.4 [P]
- d(n) = 0.4
- d(n) direction: ~
- Active mechanism: M1
- Branching: N
- Notes: Pre-branching β⁻
```

### Step 9: ²¹²Bi → BRANCHING POINT
```
EDC BLOCK:
- n(212) ≈ 36.4 [P]
- d(n) = 0.4 (close to 36)
- d(n) direction: ~ (competitive modes)
- Active mechanism: M1/M3 competitive
- Branching: YES — 64% β⁻, 36% α
- Notes: CRITICAL BRANCHING POINT (see appendix)
```

**Branch 9A: ²¹²Bi → ²¹²Po (β⁻, 64%)**
```
EDC BLOCK:
- Mode: β⁻ (64%)
- n unchanged at 36.4
- Interpretation: N/Z adjustment preferred
- Next: ²¹²Po → ²⁰⁸Pb (α)
```

**Branch 9B: ²¹²Bi → ²⁰⁸Tl (α, 36%)**
```
EDC BLOCK:
- Mode: α (36%)
- n: 36.4 → 36.2 [P]
- Interpretation: Direct A reduction
- Next: ²⁰⁸Tl → ²⁰⁸Pb (β⁻)
```

### Step 10A: ²¹²Po → ²⁰⁸Pb (α)
```
EDC BLOCK:
- n(212→208): 36.4 → 36.2 [P]
- d(n) = 0.2
- d(n) direction: ↓
- Active mechanism: M3
- Notes: Ultra-short t₁/₂ ~ ns
```

### Step 10B: ²⁰⁸Tl → ²⁰⁸Pb (β⁻)
```
EDC BLOCK:
- n(208) ≈ 36.2 [P]
- d(n) = 0.2
- d(n) direction: ~
- Active mechanism: M1
- Notes: Short-lived
```

### Endpoint: ²⁰⁸Pb (STABLE — DOUBLY MAGIC)
```
EDC BLOCK:
- n(208) ≈ 36.2 [P]
- d(n) ≈ 0.2 (very close to 36)
- Status: STABLE — doubly magic
- Z = 82 (magic)
- N = 126 (magic)
- Notes: Shell + topological stability
```

---

## Chain Closure Analysis [P]

### Why Termination at Pb-208?

1. **n(208) ≈ 36.2** — very close to allowed 36
2. **36 = 2² × 3²** — ALLOWED
3. **Z = 82, N = 126** — DOUBLY MAGIC
4. **Combined stability**: Topology + shells

### d(n) Progression (α-steps only)

| Step | A | n(A) | d(n) | Trend |
|------|---|------|------|-------|
| 1 | 232 | 37.5 | 1.5 | start |
| 4 | 228 | 37.3 | 1.3 | ↓ |
| 5 | 224 | 37.1 | 1.1 | ↓ |
| 6 | 220 | 36.8 | 0.8 | ↓ |
| 7 | 216 | 36.6 | 0.6 | ↓ |
| 10 | 212→208 | 36.4→36.2 | 0.4→0.2 | ↓ |

---

## Branching Analysis Appendix

### ²¹²Bi Branching: 64% β⁻ / 36% α

**Observed ratio**: [BL:SOURCE_TBD] (literature value ~64:36)

**EDC Interpretation [P]**:

At A=212, n(212) ≈ 36.4:
- d(n) = 0.4 — very close to allowed
- Both modes competitive:
  - β⁻: Adjusts N/Z, keeps A=212, then α to 208
  - α: Directly reduces A to 208

**Why 64:36 and not 50:50?**

Hypothesis [P]:
- β⁻ is energetically slightly favored at this N/Z ratio
- α-barrier slightly higher than β Q-value barrier
- 64:36 ≈ 2:1 suggests ~kT difference in activation energies

**Mechanism interpretation**:
- M1 (domain mixing) → β⁻ path (64%)
- M3 (α-cluster) → α path (36%)
- Competition reflects comparable d(n) for both directions

**Falsification test**:
If branching ratio correlates with d(n) across nuclei:
- Near d=0: β dominated
- Near d=6 (max): α dominated
- d≈0.4 → slight β preference ✓

---

## Missing Data Points

Recorded in 12_DATA_REQUESTS_V4.md:
- t₁/₂ for all steps
- Q_α, Q_β for all decays
- Exact branching ratio at ²¹²Bi
