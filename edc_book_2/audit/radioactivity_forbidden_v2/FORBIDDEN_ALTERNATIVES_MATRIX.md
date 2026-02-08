# FORBIDDEN ALTERNATIVES MATRIX

**Generated**: 2026-01-31
**Scope**: n = 37..47 (forbidden zone between allowed 36 and 48)

---

## Allowed Set Reference [Der]

**Citation**: [DN-001] 22826edd_full.md:2440-2540

```
n is ALLOWED iff n = 2^a × 3^b for a,b ∈ ℤ≥0
```

Nearest allowed to forbidden zone:
- Below: n = 36 = 2² × 3²
- Above: n = 48 = 2⁴ × 3
- Further: n = 32 = 2⁵, n = 54 = 2 × 3³

---

## Complete Forbidden Zone Table

| n | Prime Factorization | Status | "Bad" Factor | d(n) to 36 | d(n) to 48 | d(n) = min | Closest Allowed |
|---|---------------------|--------|--------------|------------|------------|------------|-----------------|
| 37 | 37 (prime) | FORBIDDEN | 37 | 1 | 11 | 1 | 36 |
| 38 | 2 × 19 | FORBIDDEN | 19 | 2 | 10 | 2 | 36 |
| 39 | 3 × 13 | FORBIDDEN | 13 | 3 | 9 | 3 | 36 |
| 40 | 2³ × 5 | FORBIDDEN | 5 | 4 | 8 | 4 | 36 |
| 41 | 41 (prime) | FORBIDDEN | 41 | 5 | 7 | 5 | 36 |
| 42 | 2 × 3 × 7 | FORBIDDEN | 7 | 6 | 6 | 6 | 36 or 48 |
| **43** | **43 (prime)** | **FORBIDDEN** | **43** | **7** | **5** | **5** | **48** |
| 44 | 2² × 11 | FORBIDDEN | 11 | 8 | 4 | 4 | 48 |
| 45 | 3² × 5 | FORBIDDEN | 5 | 9 | 3 | 3 | 48 |
| 46 | 2 × 23 | FORBIDDEN | 23 | 10 | 2 | 2 | 48 |
| 47 | 47 (prime) | FORBIDDEN | 47 | 11 | 1 | 1 | 48 |

**Key**: n = 43 is the nuclear matter saturation optimum [DN-010, DN-011].

---

## Four Mechanisms for "Apparent Forbidden n"

### Mechanism M1: Domain Mixing [I]

**Description**: Nucleus contains spatial domains with allowed coordinations; global average appears forbidden.

**Construction for each n**:

| n | Domain Mix Recipe | Weights | Verification |
|---|------------------|---------|--------------|
| 37 | 36 + trace 48 | 0.917 × 36 + 0.083 × 48 | 36×0.917 + 48×0.083 = 37.0 ✓ |
| 38 | 36 + 48 | 0.833 × 36 + 0.167 × 48 | 36×0.833 + 48×0.167 = 38.0 ✓ |
| 39 | 36 + 48 | 0.750 × 36 + 0.250 × 48 | 36×0.750 + 48×0.250 = 39.0 ✓ |
| 40 | 36 + 48 | 0.667 × 36 + 0.333 × 48 | 36×0.667 + 48×0.333 = 40.0 ✓ |
| 41 | 36 + 48 | 0.583 × 36 + 0.417 × 48 | 36×0.583 + 48×0.417 = 41.0 ✓ |
| 42 | 36 + 48 | 0.500 × 36 + 0.500 × 48 | 36×0.500 + 48×0.500 = 42.0 ✓ |
| 43 | 36 + 48 | 0.417 × 36 + 0.583 × 48 | 36×0.417 + 48×0.583 = 43.0 ✓ |
| 44 | 36 + 48 | 0.333 × 36 + 0.667 × 48 | 36×0.333 + 48×0.667 = 44.0 ✓ |
| 45 | 36 + 48 | 0.250 × 36 + 0.750 × 48 | 36×0.250 + 48×0.750 = 45.0 ✓ |
| 46 | 36 + 48 | 0.167 × 36 + 0.833 × 48 | 36×0.167 + 48×0.833 = 46.0 ✓ |
| 47 | 36 + 48 | 0.083 × 36 + 0.917 × 48 | 36×0.083 + 48×0.917 = 47.0 ✓ |

**Epistemic**: [I] - physically plausible, no explicit source
**Falsification**: If half-lives show no domain boundary effects (no bimodal spectra), disfavored

---

### Mechanism M2: Topological Defects [P]

**Description**: Perfect allowed lattice (n=48) contains defects that reduce average coordination.

**Construction**:

| n | Base | Defect Count | Coordination Loss | Net |
|---|------|--------------|------------------|-----|
| 47 | 48 | 1 defect per 48 sites | -1 avg | 48-1=47 |
| 46 | 48 | 2 defects per 48 sites | -2 avg | 48-2=46 |
| 45 | 48 | 3 defects per 48 sites | -3 avg | 48-3=45 |
| 44 | 48 | 4 defects per 48 sites | -4 avg | 48-4=44 |
| 43 | 48 | 5 defects per 48 sites | -5 avg | 48-5=43 |
| (42-37) | (complex) | (requires 36 base too) | ... | ... |

**Epistemic**: [P] - proposed, no source
**Citation**: [DN-030] 73d92ff5_full.md:737 mentions "defect stability"
**Falsification**: If defect density doesn't correlate with instability, reject

---

### Mechanism M3: α-Clusterization [I]

**Description**: α-clusters (⁴He units) have internal allowed coordination; global average differs.

**Citation**: [DN-025, DN-026]

**Construction**:
- Each α-cluster: n_internal ≈ 6 (allowed, tetrahedral)
- Cluster-cluster: n_external varies
- Total: weighted average of internal + external

| n_apparent | Interpretation |
|------------|---------------|
| 37-42 | More 36-like cluster packing |
| 43-47 | More 48-like cluster packing |

**Epistemic**: [I] - inferred from α-cluster model success in source
**Falsification**: If α-decay rates don't correlate with frustration, revise

---

### Mechanism M4: Metastable M-Structures [P]

**Description**: Forbidden coordination exists as short-lived configuration.

**Citation**: [DN-027, DN-028, DN-029]

**Construction**:
```
M_n := metastable state with coordination n
Lifetime: τ(M_n) ∝ exp(ΔV_eff(n)/kT)
```

| M-structure | Status | Expected τ relative to allowed |
|-------------|--------|-------------------------------|
| M37 | Metastable | Short (close to M36) |
| M40 | Metastable | Short |
| M43 | Metastable | Moderate (nuclear matter) |
| M47 | Metastable | Very short (close to M48) |

**Epistemic**: [P] - purely speculative
**Falsification**: No isomer spectroscopy signatures → remains [P]

---

## Decay Mode Predictions [P]

Based on d(n) and direction to nearest allowed:

| n | d(n) | Closest | Direction | Predicted Mode | Reasoning |
|---|------|---------|-----------|----------------|-----------|
| 37 | 1 | 36 | down | β⁺/EC or α | Small Δn, α possible |
| 38 | 2 | 36 | down | β⁺/EC | Small Δn |
| 39 | 3 | 36 | down | β⁺/EC or α | Medium Δn |
| 40 | 4 | 36 | down | α preferred | Large Δn |
| 41 | 5 | 36 | down | α preferred | Large Δn |
| 42 | 6 | tie | either | Mixed modes | Transition point |
| **43** | **5** | **48** | **up** | **β⁻ or α** | **Nuclear saturation** |
| 44 | 4 | 48 | up | β⁻ | Approach 48 via N/Z change |
| 45 | 3 | 48 | up | β⁻ | Approach 48 via N/Z change |
| 46 | 2 | 48 | up | β⁻ | Small Δn |
| 47 | 1 | 48 | up | β⁻ | Smallest Δn |

**Epistemic**: [P] - proposed correlation
**Falsification**: If observed modes don't correlate with d(n) direction, reject

---

## How to Falsify Each Mechanism

| Mechanism | Falsification Test | Observable |
|-----------|-------------------|------------|
| M1: Domain mixing | No bimodal α-spectra | Q-value distribution |
| M2: Defects | No defect-instability correlation | τ vs defect density |
| M3: α-clustering | α-preformation uncorrelated with ε_f | Cluster formation factors |
| M4: Metastable | No isomer signatures | Nuclear spectroscopy |

---

## Summary

| n | Best Interpretation | Mechanism | Predicted Decay | d(n) |
|---|---------------------|-----------|-----------------|------|
| 37 | Near-allowed | M1/M3 | β⁺/α | 1 |
| 38 | Domain mix | M1 | β⁺ | 2 |
| 39 | Domain mix | M1 | β⁺/α | 3 |
| 40 | Defected 48 | M2 | α | 4 |
| 41 | Deep forbidden | M3/M4 | α | 5 |
| 42 | Transition | M1 | Mixed | 6 |
| **43** | **Nuclear saturation** | **M1/M3** | **α/β⁻** | **5** |
| 44 | Approaching 48 | M1/M2 | β⁻ | 4 |
| 45 | Approaching 48 | M1 | β⁻ | 3 |
| 46 | Near-allowed | M2 | β⁻ | 2 |
| 47 | Near-allowed | M2 | β⁻ | 1 |

All predictions are [P] until verified against data.
