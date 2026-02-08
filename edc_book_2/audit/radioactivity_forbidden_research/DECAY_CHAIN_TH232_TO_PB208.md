# DECAY CHAIN: Th-232 → Pb-208 (Thorium Series)

**Generated**: 2026-01-31
**Purpose**: Standard decay chain with EDC interpretation
**Data Status**: Nuclear data marked [BL] (external NNDC/IAEA required)

---

## 1. Decay Chain Table

| Step | Parent | Decay Mode | Daughter | Half-Life | Q (MeV) | Notes |
|------|--------|------------|----------|-----------|---------|-------|
| 1 | ²³²Th | α | ²²⁸Ra | [BL] 1.4×10¹⁰ y | [BL] | Primordial |
| 2 | ²²⁸Ra | β⁻ | ²²⁸Ac | [BL] 5.75 y | [BL] | |
| 3 | ²²⁸Ac | β⁻ | ²²⁸Th | [BL] 6.15 h | [BL] | |
| 4 | ²²⁸Th | α | ²²⁴Ra | [BL] 1.91 y | [BL] | |
| 5 | ²²⁴Ra | α | ²²⁰Rn | [BL] 3.66 d | [BL] | |
| 6 | ²²⁰Rn | α | ²¹⁶Po | [BL] 55.6 s | [BL] | Thoron gas |
| 7 | ²¹⁶Po | α | ²¹²Pb | [BL] 0.145 s | [BL] | |
| 8 | ²¹²Pb | β⁻ | ²¹²Bi | [BL] 10.6 h | [BL] | |
| 9 | ²¹²Bi | β⁻ (64%) | ²¹²Po | [BL] 60.6 min | [BL] | Branch A |
| 9' | ²¹²Bi | α (36%) | ²⁰⁸Tl | [BL] 60.6 min | [BL] | Branch B |
| 10A | ²¹²Po | α | ²⁰⁸Pb | [BL] 299 ns | [BL] | From Branch A |
| 10B | ²⁰⁸Tl | β⁻ | ²⁰⁸Pb | [BL] 3.05 min | [BL] | From Branch B |
| END | ²⁰⁸Pb | STABLE | — | ∞ | — | Doubly magic |

**Note**: ²¹²Bi shows branching: 64% β⁻ to ²¹²Po, 36% α to ²⁰⁸Tl. Both routes end at ²⁰⁸Pb.

---

## 2. EDC Attributes per Step

| Step | Nuclide | A | Estimated n(A) | Allowed/Forbidden | ε_f Trend | Mode Comment |
|------|---------|---|----------------|-------------------|-----------|--------------|
| 1 | ²³²Th | 232 | [Open] ≈ 43? | Forbidden | High | Longest α |
| 2 | ²²⁸Ra | 228 | [Open] | [Open] | Medium-High | β⁻ mode |
| 3 | ²²⁸Ac | 228 | [Open] | [Open] | Medium-High | β⁻ mode |
| 4 | ²²⁸Th | 228 | [Open] | [Open] | Medium | α returns |
| 5 | ²²⁴Ra | 224 | [Open] | [Open] | Medium | α chain |
| 6 | ²²⁰Rn | 220 | [Open] | [Open] | Medium | α, thoron |
| 7 | ²¹⁶Po | 216 | [Open] | [Open] | Lower | Short α |
| 8 | ²¹²Pb | 212 | [Open] | [Open] | Lower | β⁻ |
| 9 | ²¹²Bi | 212 | [Open] | [Open] | Lower | BRANCH POINT |
| 10 | ²¹²Po/²⁰⁸Tl | 212/208 | [Open] | [Open] | Low | Converge |
| END | ²⁰⁸Pb | 208 | [Open] ≈ 36? | Allowed? | Zero | Doubly magic |

---

## 3. Special Feature: ²¹²Bi Branching

**Observation**: ²¹²Bi decays by both α (36%) and β⁻ (64%).

**EDC Interpretation [P]**:
- Branching suggests system is near a mode-transition boundary
- If n(212) is in the "ambiguous zone", both channels compete
- The β⁻ pathway may be favored when system prefers to approach n = 48
- The α pathway may be favored when system prefers major n reduction

**Falsification test [P]**: If branching ratio correlates with ε_f for similar nuclei, supports EDC mechanism.

---

## 4. EDC Law Application

**Citation**: MTR-002 (22826edd_full.md:2560-2660)

For α-decay steps:
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f(A) + b
```

### Pattern Analysis

| α-Step | Parent | Z | t₁/₂ | Trend vs A |
|--------|--------|---|------|------------|
| 1 | ²³²Th | 90 | 10¹⁰ y | Highest A → longest |
| 4 | ²²⁸Th | 90 | 1.91 y | A reduced, τ drops |
| 5 | ²²⁴Ra | 88 | 3.66 d | Continuing drop |
| 6 | ²²⁰Rn | 86 | 55.6 s | Minutes now |
| 7 | ²¹⁶Po | 84 | 0.145 s | Sub-second |
| 10A | ²¹²Po | 84 | 299 ns | Nanoseconds |

**Trend [I]**: Lifetime systematically decreases along the chain. Consistent with decreasing ε_f as A decreases toward allowed zone.

---

## 5. ²⁰⁸Pb: The Doubly Magic Endpoint

**Observation**: ²⁰⁸Pb has:
- Z = 82 (magic number)
- N = 126 (magic number)

**EDC Interpretation [P]**:
- Magic numbers may correspond to particularly "allowed" configurations in M-topology
- n(208) could be exactly or near 36 (= 2² × 3²), an allowed value
- Shell closure provides extra stability beyond coordination argument

**Open Question**: Is there a connection between nuclear magic numbers and EDC allowed n?

---

## 6. Data TODO

- [ ] Ingest NNDC data for all half-lives
- [ ] Ingest Q values and branching ratios for ²¹²Bi
- [ ] Calculate n(A) for Thorium series
- [ ] Compare branching ratio to ε_f transition
- [ ] Test if doubly magic ²⁰⁸Pb corresponds to allowed n
