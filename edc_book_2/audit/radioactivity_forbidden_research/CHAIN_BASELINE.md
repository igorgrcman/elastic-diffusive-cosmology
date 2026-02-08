# CHAIN BASELINE: M-Topology → Radioactivity

**Generated**: 2026-01-31
**Source**: MTR-001..006 blocks from `radioactivity_mtopology_chain_locator.md`

---

## What We Already Know (Canonical Excerpts)

### MTR-001: Coordination Rules
**Source**: 22826edd_full.md:2440-2540 (JSONL Line 48288)
**Epistemic**: [Der], [M]

```
Koordinacija:
- Dopušteno: n ∈ {6, 8, 9, 12}
- Zabranjeno: n = 5, 7, 11, ... (prosti > 3)
- Preporučeno: n = 8 (Pauli) ili n = 12 (close packing)
```

**Interpretation**: Allowed n = 2^a × 3^b; forbidden = primes > 3 and any n that doesn't factor only into 2 and 3.

---

### MTR-002: Frustration-Corrected Geiger-Nuttall Law
**Source**: 22826edd_full.md:2560-2660 (JSONL Line 48432)
**Epistemic**: [I], [Cal]

```latex
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b

Fitted parameters:
a = 1.63  (Geiger-Nuttall coefficient)
c = -2.40 (frustration coefficient)
b = -42.1 (intercept)

Result: R² = 0.9941, 44.7% improvement over standard G-N
```

**Interpretation**: Frustration parameter ε_f(A) encodes deviation from allowed coordination; negative c means higher frustration → longer half-life.

---

### MTR-003: Geometric Frustration (n ≈ 43 Forbidden)
**Source**: 22826edd_full.md:7280-7430 (JSONL Line 48432)
**Epistemic**: [Der], [P]

```
Geometric Frustration: Optimal n≈43 for nuclear matter saturation
but 43 is prime (forbidden)
Allowed coordinations: Only n values with factors of 2 and 3:
{6, 8, 9, 12, 24, 36, 48, 72...}
```

**Interpretation**: Nuclear matter density requires ~43 neighbors but topology forbids it → system is inherently frustrated.

---

### MTR-004: Pinning Constant K Derivation
**Source**: 22826edd_full.md:11040-11290 (JSONL Lines 47834, 47846)
**Epistemic**: [Der], [Cal]

```
σ = 8.82 MeV/fm²
       │
       ▼
K ≈ 0.8 MeV/veza (pinning)
       │
       ├──► τ_n = 880 s (slobodan neutron)
       ├──► τ → ∞ (vezan neutron)

K = f × σ × A_contact
f ≈ 0.3 (geometric factor - ORIGIN OPEN)

K dobiješ numerički: 0.32 × 8.82 × 0.33 = 0.93 MeV
```

**Interpretation**: Surface tension σ determines bond strength K; K ≈ 0.8-0.93 MeV explains nuclear binding and τ_n.

---

### MTR-005: Nuclear Matter Saturation Analysis
**Source**: 22826edd_full.md:11790-11990 (JSONL Lines 48324, 48432, 48762)
**Epistemic**: [Der], [Cal]

```
n = 36:  E/A = -7.4 MeV   → greška +8.6 MeV (premalo veže)
n = 48:  E/A = -21.6 MeV  → greška -5.6 MeV (previše veže)

Optimalno: n ≈ 43.3
Ali 43 je ZABRANJEN (prost broj > 3)!

Najbliži dozvoljeni: n = 48 → |greška| = 5.6 MeV ← BOLJI

Barrier calculation:
ΔV_eff ≈ ΔV + 6K × q_barrier²
       ≈ 1.3 + 6 × 0.94 × 0.25 ≈ 2.7 MeV
q_barrier = 0.5 (saddle point between proton q=0 and neutron q=1)
```

**Interpretation**: Optimal n is forbidden; nearest allowed (36, 48) has MeV-scale errors. This frustration drives decay.

---

## What is Still Open (GAPs)

| Gap ID | Description | Status | Blocks |
|--------|-------------|--------|--------|
| GAP-R1 | ε_f(A) formula - how frustration depends on A | [I] | MTR-002 |
| GAP-R2 | f ≈ 0.3 geometric factor origin | [Open] | MTR-004 |
| GAP-R3 | Prefactor A in τ_n formula | [Dc] | τ_n calibration |
| GAP-R4 | Y-junction + quantum doubling → n = 2^a × 3^b proof | [Open] | MTR-001 |
| GAP-R5 | Generalization of ΔV_eff to n ≠ 43 | [Open] | NEW |
| GAP-R6 | Domain vs true forbidden - experimental signature | [Open] | NEW |

---

## Derivation Flow (Confirmed)

```
Z₆ = Z₂ × Z₃
      │
      ▼
n = 2^a × 3^b ALLOWED
primes > 3   FORBIDDEN
      │
      ▼
Nuclear saturation wants n ≈ 43.3
43 is prime → FORBIDDEN
      │
      ├─────────────────────┐
      ▼                     ▼
GEOMETRIC              σ = 8.82 MeV/fm²
FRUSTRATION                  │
      │                      ▼
      │                 K ≈ 0.8 MeV/bond
      │                      │
      └──────────┬───────────┘
                 │
                 ▼
         ΔV_eff ≈ 2.7 MeV
         q_barrier = 0.5
                 │
                 ▼
    FRUSTRATION-CORRECTED G-N LAW [I]
    log₁₀(t₁/₂) = a(Z/√Q) + c·ε_f + b
    R² = 0.9941
```

---

## Key Numbers (Canonical)

| Parameter | Value | Source | Status |
|-----------|-------|--------|--------|
| σ (surface tension) | 8.82 MeV/fm² | MTR-004 | [Cal] |
| K (pinning constant) | 0.8-0.93 MeV/bond | MTR-004 | [Der]/[Cal] |
| n_opt (optimal coordination) | 43.3 | MTR-005 | [Der] |
| Nearest allowed n | 36, 48 | MTR-005 | [Der] |
| ΔV_eff (barrier) | 2.7 MeV | MTR-005 | [Der] |
| q_barrier (saddle point) | 0.5 | MTR-005 | [Der] |
| a (G-N coefficient) | 1.63 | MTR-002 | [Cal] |
| c (frustration coefficient) | -2.40 | MTR-002 | [Cal] |
| b (intercept) | -42.1 | MTR-002 | [Cal] |
| R² (G-N fit) | 0.9941 | MTR-002 | [I] |

---

## STEP 1 COMPLETE

Baseline established from MTR-001..005 with canonical excerpts and gaps identified.
