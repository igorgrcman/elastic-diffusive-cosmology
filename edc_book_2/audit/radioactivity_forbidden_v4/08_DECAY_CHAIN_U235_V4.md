# DECAY CHAIN U-235 V4: Actinium Series with EDC Blocks

**Created**: 2026-01-31
**Data Status**: t₁/₂ and Q marked [BL:SOURCE_TBD]
**Endpoint**: ²⁰⁷Pb (stable)
**Special**: Two branching points

---

## Chain Skeleton

| Step | Parent | A | Z | Mode | Daughter | t₁/₂ | Q (MeV) |
|------|--------|---|---|------|----------|------|---------|
| 1 | ²³⁵U | 235 | 92 | α | ²³¹Th | [BL] | [BL] |
| 2 | ²³¹Th | 231 | 90 | β⁻ | ²³¹Pa | [BL] | [BL] |
| 3 | ²³¹Pa | 231 | 91 | α | ²²⁷Ac | [BL] | [BL] |
| 4A | ²²⁷Ac | 227 | 89 | β⁻ (98.6%) | ²²⁷Th | [BL] | [BL] |
| 4B | ²²⁷Ac | 227 | 89 | α (1.4%) | ²²³Fr | [BL] | [BL] |
| 5A | ²²⁷Th | 227 | 90 | α | ²²³Ra | [BL] | [BL] |
| 5B | ²²³Fr | 223 | 87 | β⁻ | ²²³Ra | [BL] | [BL] |
| 6 | ²²³Ra | 223 | 88 | α | ²¹⁹Rn | [BL] | [BL] |
| 7 | ²¹⁹Rn | 219 | 86 | α | ²¹⁵Po | [BL] | [BL] |
| 8 | ²¹⁵Po | 215 | 84 | α | ²¹¹Pb | [BL] | [BL] |
| 9 | ²¹¹Pb | 211 | 82 | β⁻ | ²¹¹Bi | [BL] | [BL] |
| 10A | ²¹¹Bi | 211 | 83 | α (99.7%) | ²⁰⁷Tl | [BL] | [BL] |
| 10B | ²¹¹Bi | 211 | 83 | β⁻ (0.3%) | ²¹¹Po | [BL] | [BL] |
| 11A | ²⁰⁷Tl | 207 | 81 | β⁻ | ²⁰⁷Pb | [BL] | [BL] |
| 11B | ²¹¹Po | 211 | 84 | α | ²⁰⁷Pb | [BL] | [BL] |
| END | ²⁰⁷Pb | 207 | 82 | STABLE | — | ∞ | — |

**Statistics**: 11 steps, 7α + 4β⁻ (main path), ΔA=28, ΔZ=10
**Branching**: 2 points (²²⁷Ac, ²¹¹Bi)

---

## EDC Annotation Blocks

### Step 1: ²³⁵U → ²³¹Th (α)
```
EDC BLOCK:
- n(235) ≈ 37.6 [P] using n = 6.1 × A^(1/3)
- d(n) = 1.6
- d(n) direction: ↓
- Active mechanism: M3 (α-cluster), M4 (metastable)
- Branching: N
- Notes: FISSILE isotope — special M-topology?
```

### Step 2: ²³¹Th → ²³¹Pa (β⁻)
```
EDC BLOCK:
- n(231) ≈ 37.4 [P]
- d(n) = 1.4
- d(n) direction: ~
- Active mechanism: M1
- Branching: N
```

### Step 3: ²³¹Pa → ²²⁷Ac (α)
```
EDC BLOCK:
- n(231→227): 37.4 → 37.2 [P]
- d(n) = 1.2
- d(n) direction: ↓
- Active mechanism: M3
- Branching: N
```

### Step 4: ²²⁷Ac → BRANCHING POINT #1
```
EDC BLOCK:
- n(227) ≈ 37.2 [P]
- d(n) = 1.2
- d(n) direction: competitive
- Active mechanism: M1/M3 competitive
- Branching: YES — 98.6% β⁻, 1.4% α
- Notes: STRONGLY β⁻ favored
```

**Branch 4A: ²²⁷Ac → ²²⁷Th (β⁻, 98.6%)**
```
EDC BLOCK:
- Mode: β⁻ (98.6% — DOMINANT)
- n unchanged at 37.2
- Interpretation: Strong N/Z preference
- Active mechanism: M1 dominant
```

**Branch 4B: ²²⁷Ac → ²²³Fr (α, 1.4%)**
```
EDC BLOCK:
- Mode: α (1.4% — MINOR)
- n: 37.2 → 36.9 [P]
- Interpretation: Small α channel
- Active mechanism: M3 minor
```

### Step 5: Convergence at ²²³Ra
```
EDC BLOCK:
- Both paths converge to ²²³Ra
- n(223) ≈ 36.9 [P]
- d(n) = 0.9
```

### Step 6: ²²³Ra → ²¹⁹Rn (α)
```
EDC BLOCK:
- n(223→219): 36.9 → 36.7 [P]
- d(n) = 0.7
- d(n) direction: ↓
- Active mechanism: M3
- Branching: N
```

### Step 7: ²¹⁹Rn → ²¹⁵Po (α)
```
EDC BLOCK:
- n(219→215): 36.7 → 36.5 [P]
- d(n) = 0.5
- d(n) direction: ↓
- Active mechanism: M3
- Notes: Actinon (short-lived)
```

### Step 8: ²¹⁵Po → ²¹¹Pb (α)
```
EDC BLOCK:
- n(215→211): 36.5 → 36.3 [P]
- d(n) = 0.3
- d(n) direction: ↓
- Active mechanism: M3
```

### Step 9: ²¹¹Pb → ²¹¹Bi (β⁻)
```
EDC BLOCK:
- n(211) ≈ 36.3 [P]
- d(n) = 0.3
- d(n) direction: ~
- Active mechanism: M1
- Branching: N
```

### Step 10: ²¹¹Bi → BRANCHING POINT #2
```
EDC BLOCK:
- n(211) ≈ 36.3 [P]
- d(n) = 0.3
- d(n) direction: ↓ (toward 36)
- Active mechanism: M3 dominant
- Branching: YES — 99.7% α, 0.3% β⁻
- Notes: STRONGLY α favored (opposite to ²²⁷Ac!)
```

**Branch 10A: ²¹¹Bi → ²⁰⁷Tl (α, 99.7%)**
```
EDC BLOCK:
- Mode: α (99.7% — DOMINANT)
- n: 36.3 → 36.1 [P]
- Interpretation: Strong α preference
- Active mechanism: M3 dominant
```

**Branch 10B: ²¹¹Bi → ²¹¹Po (β⁻, 0.3%)**
```
EDC BLOCK:
- Mode: β⁻ (0.3% — MINOR)
- n unchanged at 36.3
- Interpretation: Tiny N/Z channel
- Active mechanism: M1 minor
```

### Step 11: Convergence at ²⁰⁷Pb
```
EDC BLOCK:
- Both paths converge to ²⁰⁷Pb
- n(207) ≈ 36.1 [P]
- d(n) ≈ 0.1 (essentially allowed)
```

### Endpoint: ²⁰⁷Pb (STABLE)
```
EDC BLOCK:
- n(207) ≈ 36.1 [P]
- d(n) ≈ 0.1 (very close to 36)
- Status: STABLE
- Z = 82 (magic)
- N = 125 (one below magic 126)
- Notes: Stable despite odd N
```

---

## Branching Analysis Appendix

### Branch #1: ²²⁷Ac — 98.6% β⁻ / 1.4% α

**EDC Interpretation [P]**:

At A=227, n(227) ≈ 37.2, d(n) = 1.2:
- d(n) is SMALL → N/Z adjustment sufficient
- β⁻ strongly preferred (98.6%)
- α channel minor (1.4%)

**Mechanism**:
- M1 (domain mixing) → β⁻ (98.6%)
- M3 (α-cluster) → α (1.4%)
- Small d(n) means domain mixing handles frustration

### Branch #2: ²¹¹Bi — 99.7% α / 0.3% β⁻

**EDC Interpretation [P]**:

At A=211, n(211) ≈ 36.3, d(n) = 0.3:
- d(n) is VERY SMALL → close to allowed
- BUT α strongly preferred!

**Why opposite pattern from ²²⁷Ac?**

Hypothesis [P]:
1. At A=211, Q_α >> Q_β (α energetically favorable)
2. Pre-formed α-cluster ready for emission
3. N/Z already near optimal for Pb endpoint
4. α gives direct path to stable ²⁰⁷Pb

**Key insight**: Branching depends on BOTH d(n) AND Q-values

### Comparison Table

| Nuclide | d(n) | β⁻ % | α % | Interpretation |
|---------|------|------|-----|----------------|
| ²²⁷Ac | 1.2 | 98.6 | 1.4 | N/Z adjustment needed |
| ²¹¹Bi | 0.3 | 0.3 | 99.7 | Direct α to endpoint |

**Pattern [P]**: Branching is NOT purely d(n) dependent
- ²²⁷Ac: Higher d(n) → β⁻ favored
- ²¹¹Bi: Lower d(n) → α favored (counterintuitive!)

**Explanation [P]**: At low d(n), system is close to endpoint and α is most efficient path.

---

## Special: ²³⁵U Fissility

### Observation
²³⁵U is FISSILE (chain reaction possible)
²³⁸U is NOT fissile (only fissionable)

### EDC Hypothesis [P]
- Odd-A nuclei (A=235) have different M-topology
- n(235) slightly deeper in forbidden zone?
- Fissility = extreme M-topology instability
- Fission = splitting into two "allowed" chunks

**Open question**: Does n(A) formula distinguish odd/even A?

---

## Chain Closure [P]

### Why Termination at Pb-207?

1. **n(207) ≈ 36.1** — essentially allowed
2. **Z = 82** — magic number
3. **N = 125** — one below magic 126 but stable
4. **Combined**: Near-allowed n + shell stability

---

## Missing Data Points

Recorded in 12_DATA_REQUESTS_V4.md:
- t₁/₂ for all steps
- Q_α, Q_β for all decays
- Exact branching ratios at ²²⁷Ac and ²¹¹Bi
