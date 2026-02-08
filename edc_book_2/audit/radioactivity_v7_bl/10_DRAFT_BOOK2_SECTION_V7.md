# DRAFT BOOK 2 SECTION: RADIOACTIVE DECAY AND M-TOPOLOGY

**Version**: V7 BL-Grounded
**Created**: 2026-01-31
**Target**: Book 2, Part II (Weak Sector Interface)
**Status**: Draft for integration

---

## Section Overview

This section tests whether the M-topology coordination law—which successfully constrains particle masses—also constrains radioactive decay. Specifically, we test whether the "coordination distance" d(n) influences decay channel selection at branchpoints.

**Key Finding**: The hypothesis that d(n) predicts branching ratios is **partially falsified**. However, the monotonic decrease of d(n) along decay chains **is confirmed**.

---

## 1. The Coordination Law Applied to Nuclei

### 1.1 The Allowed Set [Der]

From the Z₆ = Z₂ × Z₃ brane symmetry, effective coordination n is allowed if and only if:

$$n \in S = \{2^a \times 3^b : a, b \geq 0\}$$

This gives S = {1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, ...}

### 1.2 The n(A) Mapping [P]

For nuclei with mass number A, we propose:

$$n(A) = c \times A^{1/3}$$

where c ≈ 6.1 [Cal], calibrated so that n(208) ≈ 36 for doubly-magic ²⁰⁸Pb.

### 1.3 The Forbidden Zone [Der]

The interval [37, 47] contains no allowed values—all 11 integers are forbidden. This creates a "forbidden zone" that heavy nuclei must traverse during decay.

| Zone | n Range | Interpretation |
|------|---------|----------------|
| Near-allowed | 35-37 | Approaching n=36 target |
| **Forbidden** | **37-47** | Maximum frustration region |
| Near-allowed | 47-49 | Approaching n=48 target |

---

## 2. The Three Canonical Decay Chains

We analyze the three natural radioactive decay chains:

| Chain | Start | End | Steps | α | β⁻ |
|-------|-------|-----|-------|---|-----|
| U-238 | ²³⁸U | ²⁰⁶Pb | 14 | 8 | 6 |
| Th-232 | ²³²Th | ²⁰⁸Pb | 10 | 6 | 4 |
| U-235 | ²³⁵U | ²⁰⁷Pb | 11 | 7 | 4 |

### 2.1 Chain Trajectory: d(n) Decreases Monotonically [I]

**Confirmed (3/3 chains)**: The coordination distance d(n) decreases monotonically from parent to stable endpoint.

| Chain | d(start) | d(end) | Trend |
|-------|----------|--------|-------|
| U-238 | 1.81 (²³⁸U) | 0.03 (²⁰⁶Pb) | ✓ Monotonic decrease |
| Th-232 | 1.48 (²³²Th) | 0.14 (²⁰⁸Pb) | ✓ Monotonic decrease |
| U-235 | 1.65 (²³⁵U) | 0.09 (²⁰⁷Pb) | ✓ Monotonic decrease |

**Interpretation**: Decay chains "relax" toward the allowed coordination n = 36.

### 2.2 Stable Endpoints at Allowed n [I]

All three stable endpoints (lead isotopes) have d(n) ≈ 0:

| Isotope | n(A) | d(n) | Status |
|---------|------|------|--------|
| ²⁰⁶Pb | 36.03 | 0.03 | At target |
| ²⁰⁷Pb | 36.09 | 0.09 | At target |
| ²⁰⁸Pb | 36.14 | 0.14 | At target |

---

## 3. Testing the Branching Hypothesis

### 3.1 Hypothesis H-N48-01 [P → Partially Falsified]

**Original Statement**:
> At branch points, the channel that reduces d(n) is preferred.

**Prediction**: If a nucleus can decay by either α or β⁻, it should prefer whichever channel produces a daughter with smaller d(n).

### 3.2 The Three Mandatory Branchpoints

We tested this hypothesis on three branchpoints with authoritative BL data from NNDC/ENSDF:

#### Branchpoint 1: ²¹²Bi (Th-232 Series)

| Channel | Daughter | d(daughter) | Δd | Q (keV) | BR (%) |
|---------|----------|-------------|-----|---------|--------|
| α | ²⁰⁸Tl | 0.14 | -0.25 | 6207 | 35.94 |
| β⁻ | ²¹²Po | 0.39 | 0.00 | 2252 | **64.06** |

**Prediction**: α preferred (Δd < 0)
**Observation**: β⁻ dominant
**Result**: ✗ **FAILS**

#### Branchpoint 2: ²²⁷Ac (U-235 Series)

| Channel | Daughter | d(daughter) | Δd | Q (keV) | BR (%) |
|---------|----------|-------------|-----|---------|--------|
| α | ²²³Fr | 0.99 | -0.22 | 5042 | 1.38 |
| β⁻ | ²²⁷Th | 1.21 | 0.00 | 45 | **98.62** |

**Prediction**: α preferred (Δd < 0 and Q_α >> Q_β)
**Observation**: β⁻ overwhelmingly dominant
**Result**: ✗ **FAILS STRONGLY**

**Critical Insight**: Q_α exceeds Q_β by a factor of 100, yet β⁻ dominates. This requires explanation beyond both d(n) and Q-value arguments.

**Nuclear Structure Explanation**: The transition ²²⁷Ac (3/2⁻) → ²²⁷Th (1/2⁺) is an allowed Gamow-Teller β transition (ΔJ=1, parity change). Despite the low Q-value, the favorable nuclear matrix element enables β⁻ to dominate.

#### Branchpoint 3: ²¹¹Bi (U-235 Series)

| Channel | Daughter | d(daughter) | Δd | Q (keV) | BR (%) |
|---------|----------|-------------|-----|---------|--------|
| α | ²⁰⁷Tl | 0.09 | -0.23 | 6750 | **99.72** |
| β⁻ | ²¹¹Po | 0.32 | 0.00 | 574 | 0.28 |

**Prediction**: α preferred (Δd < 0)
**Observation**: α dominant
**Result**: ✓ **SUCCESS**

### 3.3 Summary Scorecard

| Branchpoint | d(n) Prediction | Q Favors | Observed | H-N48-01 |
|-------------|-----------------|----------|----------|----------|
| ²¹²Bi | α | α | β⁻ | ✗ FAIL |
| ²²⁷Ac | α | α | β⁻ | ✗ FAIL |
| ²¹¹Bi | α | α | α | ✓ SUCCESS |

**Overall Score**: 1/3 = 33%

---

## 4. What We Learned

### 4.1 What Is Confirmed

1. **Chain trajectory follows d(n) gradient**: All three chains show monotonic d(n) decrease toward stable endpoints.

2. **Stable nuclei are at allowed coordination**: The Pb isotopes terminating the chains have d(n) ≈ 0.

3. **The forbidden zone exists**: Heavy nuclei (A > 220) occupy the forbidden region and must decay to escape it.

### 4.2 What Is Falsified

1. **d(n) does not predict branching**: The hypothesis H-N48-01 scores only 33% on mandatory branchpoints.

2. **Q-value alone is insufficient**: High Q_α does not guarantee α-dominance (see ²²⁷Ac counterexample).

3. **Q-threshold gating fails**: The attempt to rescue H-N48-01 with Q-threshold conditions (H-N48-01b) also fails.

### 4.3 What Remains Open

1. **Spin-parity dependence**: A conditional hypothesis (H-N48-01c) incorporating nuclear selection rules remains untested.

2. **Half-life correlation**: Whether d(n) correlates with deviations from the Geiger-Nuttall law requires expanded data.

3. **n=48 target**: For superheavy elements (A > 350), n=48 may become the relevant target, but data is lacking.

---

## 5. Physical Interpretation

### 5.1 What d(n) Represents

The coordination distance d(n) measures how far a nucleus is from the topologically allowed set. This can be interpreted as:

- **Geometric frustration**: Nuclei with large d(n) cannot achieve optimal packing
- **Thermodynamic drive**: Decay chains flow "downhill" in the d(n) landscape
- **Not a rate constant**: d(n) describes trajectory preference, not kinetics

### 5.2 Why Branching Escapes d(n) Control

At branchpoints, multiple factors compete:

| Factor | Controls | Relevant at Branchpoint? |
|--------|----------|--------------------------|
| Q-value | Available energy | Yes, strongly |
| Coulomb barrier | α penetrability | Yes, for α |
| Spin-parity | Matrix elements | Yes, for β |
| Phase space | Final state density | Yes, for β |
| d(n) | Topological preference | Weak or absent |

The ²²⁷Ac case demonstrates that nuclear structure (spin-parity selection) can completely dominate over both Q-value and topological factors.

---

## 6. Conclusions

The M-topology coordination law provides a useful framework for understanding radioactive decay chains:

**Confirmed**:
- Decay chains relax toward allowed coordination (d → 0)
- The forbidden zone [37-47] must be traversed by heavy nuclei
- Stable endpoints coincide with allowed n values

**Not Confirmed**:
- d(n) does not control branching at individual decay steps
- The topological preference is too weak to override nuclear structure effects

**Implication for Book 2**: The coordination law describes the *overall trajectory* of decay chains but not the *mechanism of individual decays*. This is analogous to thermodynamics describing equilibrium without specifying kinetics.

---

## References

All nuclear data from:
- NNDC/ENSDF (nndc.bnl.gov)
- NUBASE2020: Kondev et al., Chinese Physics C 45 (2021) 030001
- AME2020: Wang et al., Chinese Physics C 45 (2021) 030003

