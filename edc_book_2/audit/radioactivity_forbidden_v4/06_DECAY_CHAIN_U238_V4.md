# DECAY CHAIN U-238 V4: Radium Series with EDC Blocks

**Created**: 2026-01-31
**Data Status**: t₁/₂ and Q marked [BL:SOURCE_TBD]
**Endpoint**: ²⁰⁶Pb (stable)

---

## Chain Skeleton

| Step | Parent | A | Z | Mode | Daughter | t₁/₂ | Q (MeV) |
|------|--------|---|---|------|----------|------|---------|
| 1 | ²³⁸U | 238 | 92 | α | ²³⁴Th | [BL] | [BL] |
| 2 | ²³⁴Th | 234 | 90 | β⁻ | ²³⁴Pa | [BL] | [BL] |
| 3 | ²³⁴Pa | 234 | 91 | β⁻ | ²³⁴U | [BL] | [BL] |
| 4 | ²³⁴U | 234 | 92 | α | ²³⁰Th | [BL] | [BL] |
| 5 | ²³⁰Th | 230 | 90 | α | ²²⁶Ra | [BL] | [BL] |
| 6 | ²²⁶Ra | 226 | 88 | α | ²²²Rn | [BL] | [BL] |
| 7 | ²²²Rn | 222 | 86 | α | ²¹⁸Po | [BL] | [BL] |
| 8 | ²¹⁸Po | 218 | 84 | α | ²¹⁴Pb | [BL] | [BL] |
| 9 | ²¹⁴Pb | 214 | 82 | β⁻ | ²¹⁴Bi | [BL] | [BL] |
| 10 | ²¹⁴Bi | 214 | 83 | β⁻ | ²¹⁴Po | [BL] | [BL] |
| 11 | ²¹⁴Po | 214 | 84 | α | ²¹⁰Pb | [BL] | [BL] |
| 12 | ²¹⁰Pb | 210 | 82 | β⁻ | ²¹⁰Bi | [BL] | [BL] |
| 13 | ²¹⁰Bi | 210 | 83 | β⁻ | ²¹⁰Po | [BL] | [BL] |
| 14 | ²¹⁰Po | 210 | 84 | α | ²⁰⁶Pb | [BL] | [BL] |
| END | ²⁰⁶Pb | 206 | 82 | STABLE | — | ∞ | — |

**Statistics**: 14 steps, 8α + 6β⁻, ΔA=32, ΔZ=10

---

## EDC Annotation Blocks

### Step 1: ²³⁸U → ²³⁴Th (α)
```
EDC BLOCK:
- n(238) ≈ 37.8 [P] using n = 6.1 × A^(1/3)
- d(n) = 1.8 (toward 36)
- d(n) direction: ↓ decreasing
- Active mechanism: M3 (α-cluster), M4 (metastable)
- Branching: N
- Notes: Primordial, t₁/₂ ~ 10⁹ y, deep in forbidden zone
```

### Step 2: ²³⁴Th → ²³⁴Pa (β⁻)
```
EDC BLOCK:
- n(234) ≈ 37.6 [P]
- d(n) = 1.6
- d(n) direction: ~ (A unchanged, N/Z shifts)
- Active mechanism: M1 (domain mixing adjusts N/Z)
- Branching: N
- Notes: β⁻ adjusts N/Z after α-step
```

### Step 3: ²³⁴Pa → ²³⁴U (β⁻)
```
EDC BLOCK:
- n(234) ≈ 37.6 [P]
- d(n) = 1.6
- d(n) direction: ~ (same A)
- Active mechanism: M1
- Branching: N
- Notes: Second β⁻ completes N/Z adjustment
```

### Step 4: ²³⁴U → ²³⁰Th (α)
```
EDC BLOCK:
- n(234→230): 37.6 → 37.4 [P]
- d(n) = 1.4
- d(n) direction: ↓
- Active mechanism: M3 (α-cluster emission)
- Branching: N
- Notes: α-chain resumes after β⁻ pair
```

### Step 5: ²³⁰Th → ²²⁶Ra (α)
```
EDC BLOCK:
- n(230→226): 37.4 → 37.2 [P]
- d(n) = 1.2
- d(n) direction: ↓
- Active mechanism: M3
- Branching: N
```

### Step 6: ²²⁶Ra → ²²²Rn (α)
```
EDC BLOCK:
- n(226→222): 37.2 → 36.9 [P]
- d(n) = 0.9
- d(n) direction: ↓
- Active mechanism: M3
- Branching: N
- Notes: Approaching allowed n=36
```

### Step 7: ²²²Rn → ²¹⁸Po (α)
```
EDC BLOCK:
- n(222→218): 36.9 → 36.7 [P]
- d(n) = 0.7
- d(n) direction: ↓
- Active mechanism: M3, M1 (domain mixing significant)
- Branching: N
- Notes: Radon gas; short-lived
```

### Step 8: ²¹⁸Po → ²¹⁴Pb (α)
```
EDC BLOCK:
- n(218→214): 36.7 → 36.5 [P]
- d(n) = 0.5
- d(n) direction: ↓
- Active mechanism: M3
- Branching: N
```

### Step 9: ²¹⁴Pb → ²¹⁴Bi (β⁻)
```
EDC BLOCK:
- n(214) ≈ 36.5 [P]
- d(n) = 0.5
- d(n) direction: ~ (A unchanged)
- Active mechanism: M1 (N/Z fine-tuning)
- Branching: N
- Notes: Close to allowed; β⁻ adjusts ratio
```

### Step 10: ²¹⁴Bi → ²¹⁴Po (β⁻)
```
EDC BLOCK:
- n(214) ≈ 36.5 [P]
- d(n) = 0.5
- d(n) direction: ~
- Active mechanism: M1
- Branching: N (minor α branch exists but <<1%)
```

### Step 11: ²¹⁴Po → ²¹⁰Pb (α)
```
EDC BLOCK:
- n(214→210): 36.5 → 36.3 [P]
- d(n) = 0.3
- d(n) direction: ↓
- Active mechanism: M3
- Branching: N
- Notes: Ultra-short t₁/₂ ~ μs
```

### Step 12: ²¹⁰Pb → ²¹⁰Bi (β⁻)
```
EDC BLOCK:
- n(210) ≈ 36.3 [P]
- d(n) = 0.3
- d(n) direction: ~
- Active mechanism: M1
- Branching: N
```

### Step 13: ²¹⁰Bi → ²¹⁰Po (β⁻)
```
EDC BLOCK:
- n(210) ≈ 36.3 [P]
- d(n) = 0.3
- d(n) direction: ~
- Active mechanism: M1
- Branching: N
```

### Step 14: ²¹⁰Po → ²⁰⁶Pb (α)
```
EDC BLOCK:
- n(210→206): 36.3 → 36.0 [P]
- d(n) = 0.0 at endpoint!
- d(n) direction: ↓ to ZERO
- Active mechanism: M3 (final α)
- Branching: N
- Notes: Final step reaches allowed n=36
```

### Endpoint: ²⁰⁶Pb (STABLE)
```
EDC BLOCK:
- n(206) ≈ 36.0 [P]
- d(n) = 0 (ALLOWED)
- Status: STABLE — chain terminates
- Mechanism: None needed; n is allowed
- Notes: Z=82 magic reinforces stability
```

---

## Chain Closure Analysis [P]

### Why Termination at Pb-206?

1. **n(206) ≈ 36** using n = 6.1 × A^(1/3)
2. **36 = 2² × 3²** — ALLOWED by LAW-1
3. **d(n) = 0** — no frustration
4. **Z = 82** — magic number (shell closure)
5. **Combined**: Topological + shell stability

### d(n) Progression

| Step | A | n(A) | d(n) | Trend |
|------|---|------|------|-------|
| 1 | 238 | 37.8 | 1.8 | start |
| 4 | 234 | 37.6 | 1.6 | ↓ |
| 5 | 230 | 37.4 | 1.4 | ↓ |
| 6 | 226 | 37.2 | 1.2 | ↓ |
| 7 | 222 | 36.9 | 0.9 | ↓ |
| 8 | 218 | 36.7 | 0.7 | ↓ |
| 11 | 214 | 36.5 | 0.5 | ↓ |
| 14 | 210 | 36.3 | 0.3 | ↓ |
| END | 206 | 36.0 | 0.0 | ✓ |

**Monotonic decrease** ✓ — consistent with GEN-5

---

## Branching Analysis Appendix

### No Major Branching in U-238 Chain

Main path is essentially linear (>99.9% for each step).

Minor branches exist but negligible:
- ²¹⁸Po: small α branch to ²¹⁴Bi
- ²¹⁴Bi: minor α branch (<0.1%)

### Why No Branching?

**EDC Interpretation [P]**:
- n(A) smoothly decreases along chain
- Clear direction toward n=36
- No point where d(n) is equidistant to two allowed values
- Compare to Th-232 chain where ²¹²Bi has d(n)≈6 (competitive)

---

## Missing Data Points

Recorded in 12_DATA_REQUESTS_V4.md:
- t₁/₂ for all 14 steps
- Q_α for 8 α-decays
- Q_β for 6 β-decays
