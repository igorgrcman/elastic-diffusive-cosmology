# FORBIDDEN CATALOG V3: n = 37..47 (Excluding M43)

**Created**: 2026-01-31
**Purpose**: Comprehensive catalog of forbidden coordination numbers
**Citation**: DN-001, DN-002 from DONOR_TRACEBACK.md

---

## Allowed Values (Reference)

| n | Factorization | Status |
|---|---------------|--------|
| 32 | 2⁵ | ALLOWED |
| 36 | 2² × 3² | ALLOWED |
| 48 | 2⁴ × 3 | ALLOWED |
| 54 | 2 × 3³ | ALLOWED |

**Gap**: No allowed value in [37, 47]

---

## Forbidden Zone [37-47]

### Overview

The interval [37, 47] contains NO allowed coordination numbers.
n = 43 (nuclear saturation optimum) is treated separately in LAW-2.

---

### n = 37 [FORBIDDEN]

| Property | Value |
|----------|-------|
| Prime factorization | 37 (prime) |
| Reason forbidden | Prime > 3 |
| d(n) = min distance to allowed | min(|37-36|, |37-48|) = 1 |
| Nearest allowed (below) | 36 |
| Nearest allowed (above) | 48 |
| Physical occurrence | [Open] |

**Escape mechanisms [P]**:
- M1 (Domain mixing): Possible, d=1 is small
- M2 (Defects): Possible
- M3 (α-cluster): Less likely for small d
- M4 (Metastable): Short-lived state

---

### n = 38 [FORBIDDEN]

| Property | Value |
|----------|-------|
| Prime factorization | 2 × 19 |
| Reason forbidden | Contains prime 19 > 3 |
| d(n) | min(|38-36|, |38-48|) = 2 |
| Physical occurrence | [Open] |

---

### n = 39 [FORBIDDEN]

| Property | Value |
|----------|-------|
| Prime factorization | 3 × 13 |
| Reason forbidden | Contains prime 13 > 3 |
| d(n) | 3 |
| Physical occurrence | [Open] |

---

### n = 40 [FORBIDDEN]

| Property | Value |
|----------|-------|
| Prime factorization | 2³ × 5 |
| Reason forbidden | Contains prime 5 > 3 |
| d(n) | 4 |
| Physical occurrence | [Open] |

---

### n = 41 [FORBIDDEN]

| Property | Value |
|----------|-------|
| Prime factorization | 41 (prime) |
| Reason forbidden | Prime > 3 |
| d(n) | 5 |
| Physical occurrence | [Open] |

---

### n = 42 [FORBIDDEN]

| Property | Value |
|----------|-------|
| Prime factorization | 2 × 3 × 7 |
| Reason forbidden | Contains prime 7 > 3 |
| d(n) | 6 |
| Note | Equidistant from 36 and 48 |
| Physical occurrence | [Open] |

**Special**: Maximum frustration point within zone

---

### n = 43 [FORBIDDEN — SPECIAL: NUCLEAR OPTIMUM]

**Treated separately in LAW-2 (DN-010, DN-011)**

| Property | Value |
|----------|-------|
| Prime factorization | 43 (prime) |
| Reason forbidden | Prime > 3 |
| d(n) | min(|43-36|, |43-48|) = 5 |
| Physical significance | n_opt ≈ 43.3 at nuclear saturation |
| Paradox | Optimal packing is topologically forbidden |

**This is the M43 paradox**: Nuclear matter wants n ≈ 43 but topology forbids it.

**Consequence**: Heavy nuclei exist in frustrated metastable state, driving radioactive decay.

---

### n = 44 [FORBIDDEN]

| Property | Value |
|----------|-------|
| Prime factorization | 2² × 11 |
| Reason forbidden | Contains prime 11 > 3 |
| d(n) | 4 |
| Physical occurrence | [Open] |

---

### n = 45 [FORBIDDEN]

| Property | Value |
|----------|-------|
| Prime factorization | 3² × 5 |
| Reason forbidden | Contains prime 5 > 3 |
| d(n) | 3 |
| Physical occurrence | [Open] |

---

### n = 46 [FORBIDDEN]

| Property | Value |
|----------|-------|
| Prime factorization | 2 × 23 |
| Reason forbidden | Contains prime 23 > 3 |
| d(n) | 2 |
| Physical occurrence | [Open] |

---

### n = 47 [FORBIDDEN]

| Property | Value |
|----------|-------|
| Prime factorization | 47 (prime) |
| Reason forbidden | Prime > 3 |
| d(n) | 1 |
| Physical occurrence | [Open] |

---

## Forbidden Distance Distribution

| n | d(n) | Category |
|---|------|----------|
| 37 | 1 | Near-allowed (edge) |
| 38 | 2 | Near-allowed |
| 39 | 3 | Mid-forbidden |
| 40 | 4 | Mid-forbidden |
| 41 | 5 | Deep forbidden |
| 42 | 6 | Maximum forbidden |
| 43 | 5 | Deep forbidden (M43) |
| 44 | 4 | Mid-forbidden |
| 45 | 3 | Mid-forbidden |
| 46 | 2 | Near-allowed |
| 47 | 1 | Near-allowed (edge) |

**Pattern**: Symmetric around n = 42 (equidistant point)

---

## Escape Mechanism Matrix

| n | M1: Domain | M2: Defect | M3: α-cluster | M4: Metastable |
|---|------------|------------|---------------|----------------|
| 37 | ✓ (d=1) | ✓ | ○ | ✓ |
| 38 | ✓ | ✓ | ○ | ✓ |
| 39 | ○ | ✓ | ○ | ✓ |
| 40 | ○ | ✓ | ✓ | ✓ |
| 41 | ○ | ✓ | ✓ | ✓ |
| 42 | ○ | ✓ | ✓ | ✓ |
| 43 | ○ | ✓ | ✓✓ | ✓✓ |
| 44 | ○ | ✓ | ✓ | ✓ |
| 45 | ○ | ✓ | ✓ | ✓ |
| 46 | ✓ | ✓ | ○ | ✓ |
| 47 | ✓ (d=1) | ✓ | ○ | ✓ |

**Legend**:
- ✓ = plausible
- ✓✓ = dominant mechanism
- ○ = less likely

**Source tags**:
- M1 (Domain mixing): [I] from DN-027
- M2 (Defects): [P] from DN-029
- M3 (α-cluster): [I] from DN-030
- M4 (Metastable): [P] from DN-028

---

## Implications for Radioactivity

### Heavy Nuclei (A > 200)

Heavy nuclei have n(A) in forbidden zone (likely 40-44).
They exist as frustrated metastable states.

**Decay = relaxation toward allowed n**:
- α-decay: Δn ≈ -4 (large step toward allowed)
- β-decay: Fine-tune N/Z ratio
- Fission: Split into two allowed fragments

### Stable Endpoints

Pb-206, 207, 208 are stable because n(A) ≈ 36 (allowed).

**Hypothesis [P]**: All stable heavy nuclei have n ≈ 36 or 48.

---

## Cross-Reference

- LAW-1 (Coordination Law): DONOR_TRACEBACK DN-001..003
- LAW-2 (Nuclear Saturation): DONOR_TRACEBACK DN-010..011
- Decay Chains: DECAY_CHAIN_*.md
- n(A) Research: N_A_MAPPING_RESEARCH.md
