# DECAY CHAIN: U-235 → Pb-207 (Actinium Series)

**Generated**: 2026-01-31
**Purpose**: Standard decay chain with EDC interpretation
**Data Status**: Nuclear data marked [BL] (external NNDC/IAEA required)

---

## 1. Decay Chain Table

| Step | Parent | Decay Mode | Daughter | Half-Life | Q (MeV) | Notes |
|------|--------|------------|----------|-----------|---------|-------|
| 1 | ²³⁵U | α | ²³¹Th | [BL] 7.04×10⁸ y | [BL] | Fissile isotope |
| 2 | ²³¹Th | β⁻ | ²³¹Pa | [BL] 25.5 h | [BL] | |
| 3 | ²³¹Pa | α | ²²⁷Ac | [BL] 3.28×10⁴ y | [BL] | Protactinium |
| 4 | ²²⁷Ac | β⁻ (98.6%) | ²²⁷Th | [BL] 21.8 y | [BL] | Branch A |
| 4' | ²²⁷Ac | α (1.4%) | ²²³Fr | [BL] 21.8 y | [BL] | Branch B (minor) |
| 5A | ²²⁷Th | α | ²²³Ra | [BL] 18.7 d | [BL] | |
| 5B | ²²³Fr | β⁻ | ²²³Ra | [BL] 22 min | [BL] | Converges |
| 6 | ²²³Ra | α | ²¹⁹Rn | [BL] 11.4 d | [BL] | |
| 7 | ²¹⁹Rn | α | ²¹⁵Po | [BL] 3.96 s | [BL] | Actinon gas |
| 8 | ²¹⁵Po | α | ²¹¹Pb | [BL] 1.78 ms | [BL] | |
| 9 | ²¹¹Pb | β⁻ | ²¹¹Bi | [BL] 36.1 min | [BL] | |
| 10 | ²¹¹Bi | α (99.7%) | ²⁰⁷Tl | [BL] 2.14 min | [BL] | Main branch |
| 10' | ²¹¹Bi | β⁻ (0.3%) | ²¹¹Po | [BL] 2.14 min | [BL] | Minor branch |
| 11 | ²⁰⁷Tl | β⁻ | ²⁰⁷Pb | [BL] 4.77 min | [BL] | Main path |
| 11' | ²¹¹Po | α | ²⁰⁷Pb | [BL] 0.52 s | [BL] | Minor path |
| END | ²⁰⁷Pb | STABLE | — | ∞ | — | End of chain |

**Note**: Multiple branching points at ²²⁷Ac and ²¹¹Bi.

---

## 2. EDC Attributes per Step

| Step | Nuclide | A | Estimated n(A) | Allowed/Forbidden | ε_f Trend | Mode Comment |
|------|---------|---|----------------|-------------------|-----------|--------------|
| 1 | ²³⁵U | 235 | [Open] ≈ 43? | Forbidden | High | Long-lived α |
| 2 | ²³¹Th | 231 | [Open] | [Open] | High | Quick β⁻ |
| 3 | ²³¹Pa | 231 | [Open] | [Open] | Medium-High | Long α |
| 4 | ²²⁷Ac | 227 | [Open] | [Open] | Medium | BRANCH |
| 5 | ²²⁷Th/²²³Fr | 227/223 | [Open] | [Open] | Medium | Converge |
| 6 | ²²³Ra | 223 | [Open] | [Open] | Medium | α |
| 7 | ²¹⁹Rn | 219 | [Open] | [Open] | Lower | α, actinon |
| 8 | ²¹⁵Po | 215 | [Open] | [Open] | Lower | Very short α |
| 9 | ²¹¹Pb | 211 | [Open] | [Open] | Lower | β⁻ |
| 10 | ²¹¹Bi | 211 | [Open] | [Open] | Lower | BRANCH |
| 11 | ²⁰⁷Tl/²¹¹Po | 207/211 | [Open] | [Open] | Low | Converge |
| END | ²⁰⁷Pb | 207 | [Open] ≈ 36? | Allowed? | Zero | Stable |

---

## 3. Unique Features of Actinium Series

### 3.1 ²³⁵U: Fissile Character

**Observation**: Unlike ²³⁸U (non-fissile), ²³⁵U undergoes induced fission.

**EDC Interpretation [P]**:
- Odd-A nuclei (²³⁵U has A=235, odd) may have different n(A) characteristics
- The fissile nature might relate to M-topology instability at specific A
- Fission = "large-scale frustration relief" splitting into two allowed chunks

### 3.2 Two Branching Points

**²²⁷Ac**: 98.6% β⁻ vs 1.4% α
**²¹¹Bi**: 99.7% α vs 0.3% β⁻

**EDC Interpretation [P]**:
- Strongly asymmetric branching suggests one mode is clearly energetically favored
- At ²²⁷Ac: β⁻ favored → system prefers to adjust Z rather than emit α
- At ²¹¹Bi: α favored → system prefers major n reduction at this A

**Hypothesis [P]**: Branching ratio correlates with position in forbidden zone:
- n slightly off allowed → β preferred (fine tuning)
- n deep in forbidden → α preferred (large correction)

---

## 4. EDC Law Application

**Citation**: MTR-002 (22826edd_full.md:2560-2660)

For α-decay steps:
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f(A) + b
```

### Lifetime Pattern

| α-Step | Parent | Z | t₁/₂ | Lifetime Order |
|--------|--------|---|------|----------------|
| 1 | ²³⁵U | 92 | 7×10⁸ y | Longest |
| 3 | ²³¹Pa | 91 | 3×10⁴ y | Very long |
| 5A | ²²⁷Th | 90 | 18.7 d | Days |
| 6 | ²²³Ra | 88 | 11.4 d | Days |
| 7 | ²¹⁹Rn | 86 | 3.96 s | Seconds |
| 8 | ²¹⁵Po | 84 | 1.78 ms | Milliseconds |
| 10 | ²¹¹Bi | 83 | 2.14 min | Minutes |

**Pattern [I]**: Same trend as other chains - lifetime decreases with decreasing A/Z, consistent with decreasing ε_f.

---

## 5. ²⁰⁷Pb: Odd-N Stable Endpoint

**Observation**: ²⁰⁷Pb has:
- Z = 82 (magic)
- N = 125 (one below magic 126)

**EDC Question [Open]**:
- Why is ²⁰⁷Pb stable despite N = 125 not being magic?
- Does n(207) fall in allowed zone regardless?

**Comparison [P]**:
| Endpoint | A | Z | N | Magic Status | EDC n Status |
|----------|---|---|---|--------------|--------------|
| ²⁰⁶Pb | 206 | 82 | 124 | Z magic | [Open] |
| ²⁰⁷Pb | 207 | 82 | 125 | Z magic | [Open] |
| ²⁰⁸Pb | 208 | 82 | 126 | Doubly magic | [Open] |

All three Pb isotopes are stable. EDC should explain all three.

---

## 6. Cross-Chain Comparison (All Three Series)

| Property | ²³⁸U Series | ²³²Th Series | ²³⁵U Series |
|----------|-------------|--------------|-------------|
| Parent A | 238 | 232 | 235 |
| Endpoint | ²⁰⁶Pb | ²⁰⁸Pb | ²⁰⁷Pb |
| α-steps | 8 | 6 | 7 |
| β⁻-steps | 6 | 4 | 4 |
| Total ΔA | 32 | 24 | 28 |
| Total ΔZ | 10 | 8 | 9 |
| Branching | ²¹⁴Bi | ²¹²Bi | ²²⁷Ac, ²¹¹Bi |

**EDC Prediction [P]**: Chains with more α-steps (larger ΔA) should show larger cumulative frustration relief.

---

## 7. Data TODO

- [ ] Ingest NNDC data for all half-lives
- [ ] Ingest Q values and branching ratios
- [ ] Calculate n(A) for Actinium series
- [ ] Compare branching asymmetry to n(A) position
- [ ] Test fissile character vs M-topology
- [ ] Explain all three Pb stable isotopes in unified framework
