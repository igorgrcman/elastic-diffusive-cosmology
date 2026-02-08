# FORBIDDEN TOPOLOGIES V4

**Created**: 2026-01-31
**Purpose**: Systematic catalog of forbidden n∈{37..47} with mechanisms M1-M6
**Citation**: DN-001, DN-002, DN-027..030, DN-080..085

---

## Mechanism Definitions

### M1: Domain Mixing [I]
**Citation**: DN-080 (22826edd:2479-2492)
**State variable**: Domain fraction x = V_allowed / V_total
**n_eff**: n_eff = x × n_allowed + (1-x) × n_forbidden
**ε_f scaling**: ε_f ∝ (1-x) × d(n)
**Decay relief**: Reduces interface energy; favors α when domains large

### M2: Topological Defects [P]
**Citation**: DN-081 (73d92ff5:517-530)
**State variable**: Defect density ρ_d = N_defects / V
**n_eff**: n_eff modified at defect cores (lower n locally)
**ε_f scaling**: ε_f ∝ ρ_d × E_defect
**Decay relief**: Defect annihilation; α removes defect-rich region

### M3: α-Clusterization [I]
**Citation**: DN-082 (22826edd:2465-2478)
**State variable**: Cluster fraction f_α = N_clustered / N_total
**n_eff**: Clusters have n_local ≈ 12; bulk has n_bulk ≈ 43
**ε_f scaling**: ε_f ∝ (1 - f_α) × d(n_bulk)
**Decay relief**: α-emission removes pre-formed cluster

### M4: Metastable M-Structures [P]
**Citation**: DN-083 (73d92ff5:442-450)
**State variable**: Metastable population N_M
**n_eff**: Effective n in metastable phase differs from equilibrium
**ε_f scaling**: ε_f ∝ exp(−ΔV_eff / kT)
**Decay relief**: Tunneling through barrier; α preferred for high barrier

### M5: Quasicrystalline/Aperiodic [P]
**Citation**: DN-084 (no source — proposed)
**State variable**: Aperiodicity measure ξ (correlation length)
**n_eff**: Local n varies; average may be forbidden
**ε_f scaling**: ε_f ∝ |n_avg - n_allowed|
**Decay relief**: Phase transition to periodic; SF for extreme cases

### M6: Core-Mantle Mismatch [P]
**Citation**: DN-085 (22826edd:4847 "domain-wall physical")
**State variable**: Interface area A_interface = 4πR_core²
**n_eff**: n_core ≈ 43, n_mantle ≈ 38, interface frustrated
**ε_f scaling**: ε_f ∝ A_interface × σ_interface
**Decay relief**: α-emission from interface; β adjusts mantle

---

## FT Table: n = 37..47

### FT-37: n = 37

| Property | Value |
|----------|-------|
| Factorization | 37 (prime) |
| Forbidden by | LAW-1: prime > 3 |
| d(n) | 1 (closest to 36) |
| Category | Near-allowed (edge) |

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | HIGH | d=1 easily bridged |
| M2 Defect | MEDIUM | Low defect density needed |
| M3 α-cluster | LOW | Small d, clustering unnecessary |
| M4 Metastable | HIGH | Short-lived |
| M5 Quasicrystal | LOW | Overkill for d=1 |
| M6 Core-mantle | MEDIUM | Interface effect |

**Predicted decay mode**: β (fine-tuning to 36)
**Falsification**: If α dominates at n≈37, M1/M4 less likely

---

### FT-38: n = 38

| Property | Value |
|----------|-------|
| Factorization | 2 × 19 |
| Forbidden by | LAW-1: contains 19 > 3 |
| d(n) | 2 |
| Category | Near-allowed |

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | HIGH | d=2 manageable |
| M2 Defect | MEDIUM | Few defects needed |
| M3 α-cluster | LOW | Small d |
| M4 Metastable | HIGH | |
| M5 Quasicrystal | LOW | |
| M6 Core-mantle | MEDIUM | |

**Predicted decay mode**: β or α (competitive)
**Falsification**: Check U-238 chain (n≈38 at A≈238)

---

### FT-39: n = 39

| Property | Value |
|----------|-------|
| Factorization | 3 × 13 |
| Forbidden by | LAW-1: contains 13 > 3 |
| d(n) | 3 |
| Category | Mid-forbidden |

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | MEDIUM | Larger domain fraction needed |
| M2 Defect | MEDIUM | |
| M3 α-cluster | MEDIUM | Clustering starts to help |
| M4 Metastable | HIGH | |
| M5 Quasicrystal | LOW | |
| M6 Core-mantle | MEDIUM | |

**Predicted decay mode**: α emerging
**Falsification**: Lifetime should be shorter than n=37-38

---

### FT-40: n = 40

| Property | Value |
|----------|-------|
| Factorization | 2³ × 5 |
| Forbidden by | LAW-1: contains 5 > 3 |
| d(n) | 4 |
| Category | Mid-forbidden |

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | MEDIUM | Significant mixing needed |
| M2 Defect | MEDIUM | |
| M3 α-cluster | HIGH | Clustering relieves frustration |
| M4 Metastable | HIGH | |
| M5 Quasicrystal | LOW-MEDIUM | |
| M6 Core-mantle | HIGH | Interface stress significant |

**Predicted decay mode**: α favored
**Falsification**: If β dominates, M3/M6 unlikely

---

### FT-41: n = 41

| Property | Value |
|----------|-------|
| Factorization | 41 (prime) |
| Forbidden by | LAW-1: prime > 3 |
| d(n) | 5 |
| Category | Deep forbidden |

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | LOW | Large mixing needed |
| M2 Defect | MEDIUM | Many defects |
| M3 α-cluster | HIGH | Strong clustering |
| M4 Metastable | HIGH | Long metastable |
| M5 Quasicrystal | MEDIUM | Aperiodic helps |
| M6 Core-mantle | HIGH | Strong interface |

**Predicted decay mode**: α strongly favored
**Falsification**: If stable at A with n≈41, reject

---

### FT-42: n = 42 [MAXIMUM FRUSTRATION]

| Property | Value |
|----------|-------|
| Factorization | 2 × 3 × 7 |
| Forbidden by | LAW-1: contains 7 > 3 |
| d(n) | 6 (equidistant 36↔48) |
| Category | Maximum forbidden |

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | LOW | Can't easily bridge |
| M2 Defect | MEDIUM | |
| M3 α-cluster | HIGH | Essential |
| M4 Metastable | HIGH | Most stressed |
| M5 Quasicrystal | MEDIUM | |
| M6 Core-mantle | HIGH | Peak interface stress |

**Predicted decay mode**: α or SF (maximum relief)
**Special**: No clear direction toward 36 or 48
**Falsification**: Branching ratio α:β should be near 50:50

---

### FT-43: n = 43 [NUCLEAR OPTIMUM — M43 PARADOX]

| Property | Value |
|----------|-------|
| Factorization | 43 (prime) |
| Forbidden by | LAW-1: prime > 3 |
| d(n) | 5 (toward 48) |
| Category | Deep forbidden — SPECIAL |
| Physical significance | n_opt ≈ 43.3 at ρ₀ |

**THE M43 PARADOX**: Nuclear matter optimizes at forbidden n

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | LOW | Optimal density resists mixing |
| M2 Defect | MEDIUM | Defects costly |
| M3 α-cluster | HIGH✓ | Primary escape |
| M4 Metastable | HIGH✓ | Long-lived metastable |
| M5 Quasicrystal | MEDIUM | |
| M6 Core-mantle | HIGH | Core at optimum |

**Predicted decay mode**: α strongly preferred (forms clusters)
**Falsification**: If n_opt derived to be allowed, paradox dissolves

---

### FT-44: n = 44

| Property | Value |
|----------|-------|
| Factorization | 2² × 11 |
| Forbidden by | LAW-1: contains 11 > 3 |
| d(n) | 4 (toward 48) |
| Category | Mid-forbidden |

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | MEDIUM | Moderate mixing |
| M2 Defect | MEDIUM | |
| M3 α-cluster | HIGH | |
| M4 Metastable | HIGH | |
| M5 Quasicrystal | LOW-MEDIUM | |
| M6 Core-mantle | HIGH | |

**Predicted decay mode**: α favored, β⁻ possible
**Falsification**: Similar to FT-40 (symmetric)

---

### FT-45: n = 45

| Property | Value |
|----------|-------|
| Factorization | 3² × 5 |
| Forbidden by | LAW-1: contains 5 > 3 |
| d(n) | 3 (toward 48) |
| Category | Mid-forbidden |

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | MEDIUM | |
| M2 Defect | MEDIUM | |
| M3 α-cluster | MEDIUM | |
| M4 Metastable | HIGH | |
| M5 Quasicrystal | LOW | |
| M6 Core-mantle | MEDIUM | |

**Predicted decay mode**: Mixed α/β⁻
**Falsification**: Similar to FT-39 (symmetric)

---

### FT-46: n = 46

| Property | Value |
|----------|-------|
| Factorization | 2 × 23 |
| Forbidden by | LAW-1: contains 23 > 3 |
| d(n) | 2 (toward 48) |
| Category | Near-allowed |

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | HIGH | Easy bridging |
| M2 Defect | MEDIUM | |
| M3 α-cluster | LOW | Unnecessary |
| M4 Metastable | HIGH | |
| M5 Quasicrystal | LOW | |
| M6 Core-mantle | MEDIUM | |

**Predicted decay mode**: β⁻ (push toward 48)
**Falsification**: If α dominates, M1 less likely

---

### FT-47: n = 47

| Property | Value |
|----------|-------|
| Factorization | 47 (prime) |
| Forbidden by | LAW-1: prime > 3 |
| d(n) | 1 (toward 48) |
| Category | Near-allowed (edge) |

| Mechanism | Likelihood | Rationale |
|-----------|------------|-----------|
| M1 Domain | HIGH | d=1 easy |
| M2 Defect | MEDIUM | |
| M3 α-cluster | LOW | |
| M4 Metastable | HIGH | |
| M5 Quasicrystal | LOW | |
| M6 Core-mantle | MEDIUM | |

**Predicted decay mode**: β⁻ (fine-tune to 48)
**Falsification**: If α dominates, reject M1 dominance

---

## Summary Table

| FT | n | d(n) | Dominant Mechanism | Preferred Decay |
|----|---|------|-------------------|-----------------|
| FT-37 | 37 | 1 | M1, M4 | β (→36) |
| FT-38 | 38 | 2 | M1, M4 | β/α |
| FT-39 | 39 | 3 | M3, M4 | α emerging |
| FT-40 | 40 | 4 | M3, M6 | α |
| FT-41 | 41 | 5 | M3, M4, M6 | α strong |
| FT-42 | 42 | 6 | M3, M4, M6 | α/SF (max) |
| FT-43 | 43 | 5 | M3✓, M4✓ | α (M43 paradox) |
| FT-44 | 44 | 4 | M3, M6 | α |
| FT-45 | 45 | 3 | M3, M4 | α/β⁻ |
| FT-46 | 46 | 2 | M1, M4 | β⁻ (→48) |
| FT-47 | 47 | 1 | M1, M4 | β⁻ (→48) |

---

## Decay Mode Logic Map [P]

```
d(n) < 2   → Domain mixing sufficient → β preferred
d(n) 2-4   → Moderate stress → α/β competitive
d(n) > 4   → High stress → α strongly preferred
d(n) = 6   → Maximum → α or SF
n = 43     → M43 paradox → α (clustering escape)
```

**Tag**: [P] — qualitative framework, not sourced
