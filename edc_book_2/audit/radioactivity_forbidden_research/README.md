# Radioactivity Forbidden Research: Index & Summary

**Generated**: 2026-01-31
**Session**: Forbidden Topologies Beyond M43
**Git Commit**: e016c3c

---

## Deliverables Index

| File | Description | Lines | Status |
|------|-------------|-------|--------|
| `SESSION_LOG.md` | Activity log with timestamps | ~30 | Complete |
| `DECISIONS.md` | Key decisions with rationale | ~40 | Complete |
| `OPEN_QUESTIONS.md` | Gaps blocking [Der] upgrades | ~50 | Complete |
| `CHAIN_BASELINE.md` | Canonical excerpts from MTR-001..005 | ~150 | Complete |
| `FORBIDDEN_TOPOLOGIES.md` | Systematization of n ∈ {37-47} | ~300 | Complete |
| `DECAY_CHAIN_U238_TO_PB206.md` | Radium series with EDC interpretation | ~150 | Complete |
| `DECAY_CHAIN_TH232_TO_PB208.md` | Thorium series with EDC interpretation | ~130 | Complete |
| `DECAY_CHAIN_U235_TO_PB207.md` | Actinium series with EDC interpretation | ~160 | Complete |
| `LAWS_AND_INVARIANTS.md` | Extracted patterns and generalizations | ~200 | Complete |
| `README.md` | This index file | ~200 | Complete |

**Total**: 10 files, ~1400 lines

---

## Epistemic Classification Summary

### What Is Firmly Established [Der]

| Claim | Source | Notes |
|-------|--------|-------|
| Allowed n = 2^a × 3^b | MTR-001 (22826edd_full.md:2440-2540) | From Z₆ geometry |
| Forbidden = primes > 3 + composites | MTR-001 | Follows from allowed rule |
| n ≈ 43.3 optimal for saturation | MTR-005 (22826edd_full.md:11790-11860) | From nuclear density |
| 43 is prime → forbidden | Number theory | Not EDC-specific |
| Nearest allowed: 36, 48 | MTR-005 | Follows from rule |
| ΔV_eff = ΔV + 6K·q² | MTR-005 (22826edd_full.md:11862-11926) | Barrier formula |

### What Is Calibrated [Cal]

| Claim | Value | Source |
|-------|-------|--------|
| σ (surface tension) | 8.82 MeV/fm² | MTR-004 (22826edd_full.md:11040-11100) |
| K (pinning constant) | 0.8-0.93 MeV | MTR-004 |
| G-N coefficients | a=1.63, c=-2.40, b=-42.1 | MTR-002 (22826edd_full.md:2580-2610) |
| q_barrier | 0.5 | MTR-005 |
| ΔV_eff | 2.7 MeV | MTR-005 |

### What Is Inferred [I]

| Claim | Evidence | Falsifiable By |
|-------|----------|----------------|
| Frustration-Corrected G-N Law | R² = 0.9941, 44.7% improvement | Poor fit with new data |
| ε_f correlates with forbidden-distance | Implied by G-N success | d(n) vs t₁/₂ test |
| α-decay relieves frustration | Chain patterns | α-cluster model failure |
| Lifetime decreases along chains | All 3 chains show this | Exception found |

### What Is Proposed [P]

| Claim | Mechanism | Test |
|-------|-----------|------|
| Domain mixing gives apparent forbidden n | Local allowed, global average forbidden | Scattering for domains |
| Topological defects absorb forbidden | Defect density ∝ instability | Correlation test |
| α-clusterization as frustration valve | Local allowed within clusters | α-preformation study |
| Metastable M40-M47 structures | Short-lived forbidden configurations | Isomer search |
| Decay mode ∝ n deviation direction | β if close to allowed, α if far | Branching ratio analysis |
| Magic numbers = allowed coordinations | Shell closure ↔ M-topology | Calculate n at magic |
| Chains terminate at allowed n | n(Pb) ≈ 36 | Calculate n(Pb) |

### What Is Open [Open]

| Gap | Description | Blocking |
|-----|-------------|----------|
| GAP-R1 | ε_f(A) explicit formula | G-N law derivation |
| GAP-R2 | f ≈ 0.3 geometric factor origin | K derivation closure |
| GAP-R3 | Prefactor A in τ_n | Neutron lifetime [Der] |
| GAP-R4 | Y-junction → n = 2^a × 3^b proof | Coordination law proof |
| GAP-R5 | ΔV_eff generalization to n ≠ 43 | Barrier formula extension |
| GAP-R6 | Domain vs true forbidden signature | Falsification of domain model |
| n(A) formula | How A maps to coordination | All EDC predictions |
| Nuclear data | t₁/₂, Q values for chains | Quantitative tests |

---

## Citation Index

All citations to primary source (22826edd_full.md):

| Block | Line Range | Topic |
|-------|------------|-------|
| MTR-001 | 2440-2540 | Coordination rules |
| MTR-002 | 2560-2660 | Frustration-Corrected G-N Law |
| MTR-003 | 7280-7430 | Geometric frustration, n≈43 |
| MTR-004 | 11040-11290 | Pinning K from σ |
| MTR-005 | 11790-11990 | Saturation analysis, ΔV_eff |

Equation registry (22826edd_equations.md):

| Equation ID | Topic |
|-------------|-------|
| EQ-0493 | G-N law formula |
| EQ-0494 | Fitted parameters |
| EQ-0496, EQ-0497 | n ≈ 43 forbidden |
| EQ-0509 | q_barrier = 0.5 |
| EQ-0515 | ΔV_eff ≈ 2.7 MeV |

---

## Key Results

### 1. Forbidden Zone [37-47] Fully Characterized

All 11 values in the gap between allowed n=36 and n=48 are forbidden:
- 37, 41, 43, 47 (primes)
- 38, 39, 40, 42, 44, 45, 46 (composites with prime factors > 3)

Nuclear matter optimum n ≈ 43.3 falls squarely in this forbidden zone.

### 2. Four Mechanisms for "Apparent Forbidden n" Proposed

1. **Domain mixing** [I/P]: Local allowed, global average forbidden
2. **Topological defects** [P]: Defects absorb excess coordination
3. **α-clusterization** [I/P]: Local allowed within clusters
4. **Metastable M-structures** [P]: Short-lived forbidden configurations

### 3. Three Decay Chains Documented

All chains (U-238, Th-232, U-235 series) show:
- Lifetime systematically decreases with A
- Consistent with decreasing ε_f as system approaches allowed n
- Multiple branching points suggest mode competition
- All terminate at Pb isotopes (hypothesized allowed n)

### 4. Forbidden Distance Metric Proposed

```
d(n) = min{ |n - m| : m = 2^a × 3^b }
```

Hypothesis: t₁/₂ correlates with d(n(A)).

---

## Acceptance Criteria Check

| Criterion | Status |
|-----------|--------|
| 7+ new audit files | ✅ 10 files created |
| Epistemic tags on claims | ✅ All claims tagged |
| 10+ citations to 22826edd_full.md | ✅ 15+ citations |
| Forbidden n ∈ {44,45,46,47} covered | ✅ Full systematization |
| 2+ mechanisms for apparent forbidden | ✅ 4 mechanisms proposed |
| 3 decay chains complete to Pb | ✅ All 3 chains documented |
| Nuclear data marked [BL] where needed | ✅ All t₁/₂, Q marked |

---

## Next Steps

1. **Ingest nuclear data**: NNDC/IAEA for t₁/₂, Q, branching
2. **Derive n(A)**: Formula linking mass to coordination
3. **Test d(n) correlation**: With actual half-life data
4. **Resolve GAP-R1**: Explicit ε_f(A) formula
5. **Calculate n(Pb)**: Verify termination at allowed
6. **Book 2 integration**: Per `radioactivity_mtopology_book2_integration_plan.md`

---

**MEGA-PROMPT COMPLETE**
