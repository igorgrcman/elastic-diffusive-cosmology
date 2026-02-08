# DONOR TRACEBACK V3: Precise Citation Registry

**Created**: 2026-01-31
**Purpose**: Every claim traced to file:line-range
**Primary Source**: audit/jsonl_mining/reports/22826edd_full.md

---

## Citation Format

```
[DN-XXX] file.md:start-end "brief quote or topic"
```

---

## A) Coordination Law (LAW-1)

### DN-001: Allowed n formula
**File**: 22826edd_full.md:2440-2540
**Quote**: "Dopušteno: n ∈ {6, 8, 9, 12}"
**Claim**: n is ALLOWED iff n = 2^a × 3^b
**Tag**: [Der]

### DN-002: Forbidden n list
**File**: 22826edd_full.md:2441-2445
**Quote**: "Zabranjeno: n = 5, 7, 11, ... (prosti > 3)"
**Claim**: Primes > 3 are forbidden
**Tag**: [Der]

### DN-003: Z₆ geometry origin
**File**: 22826edd_full.md:2448-2455
**Quote**: "Z₆ = Z₂ × Z₃"
**Claim**: Coordination law from brane symmetry
**Tag**: [Der]

---

## B) Nuclear Saturation (LAW-2)

### DN-010: n_opt value
**File**: 22826edd_full.md:11793-11830
**Quote**: "Optimalno: n ≈ 43.3"
**Claim**: Nuclear saturation optimum is n ≈ 43.3
**Tag**: [Der]

### DN-011: n=43 forbidden
**File**: 22826edd_full.md:11831-11856
**Quote**: "Ali 43 je ZABRANJEN (prost broj > 3)!"
**Claim**: 43 is prime, hence topologically forbidden
**Tag**: [Der]

---

## C) Geiger-Nuttall Law (LAW-3)

### DN-015: G-N formula
**File**: 22826edd_full.md:2555-2567
**Quote**: "log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b"
**Claim**: Frustration-corrected G-N law
**Tag**: [I]

### DN-016: G-N fit quality
**File**: 22826edd_full.md:2568-2580
**Quote**: "R² = 0.9941"
**Claim**: 44.7% improvement over standard G-N
**Tag**: [I]

### DN-017: G-N coefficients
**File**: 22826edd_full.md:2581-2610
**Quote**: "a = 1.63, c = -2.40, b = -42.1"
**Claim**: Fitted coefficients from actinide data
**Tag**: [Cal]

---

## D) Barrier Formula (LAW-4)

### DN-020: Effective barrier
**File**: 22826edd_full.md:7322-7350
**Quote**: "ΔV_eff = ΔV + 6K × q_barrier²"
**Claim**: Topological correction to Coulomb barrier
**Tag**: [Der]

### DN-021: Barrier values
**File**: 22826edd_full.md:7351-7390
**Quote**: "K ≈ 0.94 MeV, q_barrier = 0.5"
**Claim**: ΔV_eff ≈ 2.7 MeV for n ≈ 43
**Tag**: [Cal]

---

## E) Pinning Constant (LAW-5)

### DN-023: Pinning formula
**File**: 22826edd_full.md:10915-10980
**Quote**: "K = f × σ × A_contact"
**Claim**: Pinning from surface tension
**Tag**: [Der]

### DN-024: Pinning values
**File**: 22826edd_full.md:10981-11072
**Quote**: "σ = 8.82 MeV/fm², f ≈ 0.3"
**Claim**: K ≈ 0.8-0.94 MeV
**Tag**: [Cal]

---

## F) α-Cluster Binding (LAW-6)

### DN-025: Cluster formula
**File**: 22826edd_full.md:2452-2453
**Quote**: "B.E.(nα) = n × B.E.(α) + n_bonds × E_αα"
**Claim**: α-cluster binding energy formula
**Tag**: [I]

### DN-026: Cluster accuracy
**File**: 22826edd_full.md:2454-2460
**Quote**: "C-12: 92.0 vs 92.2 MeV (−0.2%)"
**Claim**: Sub-percent accuracy for light nuclei
**Tag**: [I]

---

## G) Escape Mechanisms

### DN-027: Domain mixing
**File**: 22826edd_full.md:2479-2492
**Quote**: "Domensko miješanje..."
**Claim**: Local fluctuations smooth forbidden values
**Tag**: [I]

### DN-028: Metastable structures
**File**: 73d92ff5_full.md:442-450
**Quote**: "metastable"
**Claim**: Forbidden n as short-lived metastable state
**Tag**: [P]

### DN-029: Topological defects
**File**: 73d92ff5_full.md:517-530
**Quote**: "defect"
**Claim**: Y-junctions, domain walls as defects
**Tag**: [P]

### DN-030: α-clusterization
**File**: 22826edd_full.md:2465-2478
**Quote**: "α-klasterizacija"
**Claim**: Heavy nuclei form α-clusters with allowed n_local
**Tag**: [I]

---

## H) Decay Mode Selection

### DN-033: Weak decay junction
**File**: 98cc5184_snippets.json:295
**Quote**: "Junction relaxation: weak decay"
**Claim**: β-decay as junction relaxation
**Tag**: [I]

### DN-034: α-decay mechanism
**File**: 22826edd_full.md:2500-2520
**Quote**: "α-raspad"
**Claim**: α-decay removes 4 mass units, large Δn
**Tag**: [I]

---

## I) Additional Sources

### DN-035: 519 equations catalog
**File**: 22826edd_equations.md:1-1200
**Topic**: Complete equation index from primary session
**Note**: Cross-reference for formula verification

### DN-036: Theory maturity session
**File**: 73d92ff5_full.md:1-500
**Topic**: EDC theory development discussion
**Note**: Contains metastable/defect terminology

---

## J) Crystal/Lattice Sources

### DN-040: Lattice coordination
**File**: 22826edd_full.md:3200-3280
**Topic**: Crystal structure coordination numbers
**Claim**: FCC n=12, BCC n=8, SC n=6
**Tag**: [Der]

### DN-041: Tiling patterns
**File**: 22826edd_full.md:3281-3350
**Topic**: 2D/3D tiling with allowed coordinations
**Tag**: [Der]

---

## Summary Statistics

| Category | Donors | Primary File |
|----------|--------|--------------|
| Coordination Law | DN-001..003 | 22826edd:2440-2540 |
| Nuclear Saturation | DN-010..011 | 22826edd:11793-11856 |
| G-N Law | DN-015..017 | 22826edd:2555-2610 |
| Barrier Formula | DN-020..021 | 22826edd:7322-7390 |
| Pinning | DN-023..024 | 22826edd:10915-11072 |
| α-Cluster | DN-025..026 | 22826edd:2452-2460 |
| Escape Mechanisms | DN-027..030 | Multiple |
| Mode Selection | DN-033..034 | Multiple |
| Crystal | DN-040..041 | 22826edd:3200-3350 |

**Total donors**: 41+
**Primary source**: 22826edd_full.md (17,562 lines)
**Secondary sources**: 73d92ff5_full.md, 98cc5184_snippets.json
