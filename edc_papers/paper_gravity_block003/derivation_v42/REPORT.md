# Derivation v42 — Report

## Title
E₆ Anomaly Audit + Exotics Mass Gating

## Summary

This derivation performs a rigorous audit of the E₆ track's victory in v41, addressing two critical questions:

1. **Anomaly Safety**: Does the BC-projected chiral spectrum remain anomaly-free?
2. **Exotic Decoupling**: Can the 36 exotic fermions be gated from the IR window?

## Inputs Used

| Category | Input | Used? | Notes |
|----------|-------|-------|-------|
| Electroweak | M_Z | **NO** | Forbidden (no numerical value) |
| Electroweak | M_W | **NO** | Forbidden (no numerical value) |
| Electroweak | v_EW | **NO** | Forbidden (no numerical value) |
| QED | α_EM | **NO** | Forbidden (no numerical value) |
| Gravity | G_N | **NO** | Forbidden (no numerical value) |
| Planck | ℓ_P | **NO** | Forbidden (no numerical value) |
| EDC | L (extra dimension size) | Symbolic | Parameter |
| EDC | σ (brane tension) | Symbolic | From v27 |
| EDC | β = σL²/M̄_Pl² | Symbolic | From v27 |
| Prior | v41 fermion counts | Yes | Cross-validated |
| Prior | v37 regulator protocol | Yes | Referenced |

## Key Results

### Anomaly Risk Matrix

| Track  | SU(3)³ | SU(2)²U(1) | U(1)³ | U(1)-grav | Overall |
|--------|--------|------------|-------|-----------|---------|
| SU(5)  | PASS   | PASS       | PASS  | PASS      | **PASS** |
| SO(10) | PASS   | PASS       | PASS  | PASS      | **PASS** |
| PS     | COND   | COND       | COND  | COND      | **COND** |
| E₆     | PASS   | PASS       | PASS  | PASS      | **PASS** |

### Mass Gating Verdict

| Track  | Exotic Count | Gating Condition | Verdict |
|--------|--------------|------------------|---------|
| SU(5)  | 0            | None             | **SAFE** |
| SO(10) | 3            | π/(2L) > μ_IR    | **SAFE** |
| PS     | 6            | π/(2L) > μ_IR    | **SAFE** |
| E₆     | 36           | π/(2L) ≫ μ_IR    | **CONDITIONAL** |

### Final Admissibility

| Track  | ΔE Rank | Anomaly | Gating | Final |
|--------|---------|---------|--------|-------|
| SU(5)  | 3rd     | PASS    | SAFE   | ADMISSIBLE |
| SO(10) | 4th     | PASS    | SAFE   | ADMISSIBLE |
| PS     | 2nd     | COND    | SAFE   | CONDITIONAL |
| E₆     | **1st** | PASS    | COND   | CONDITIONAL |

## Conclusions

1. **E₆ passes anomaly gate**: Zero-mode spectrum is pure SM, anomaly-free
2. **E₆ requires mass gating**: 36 exotics must decouple via KK, bulk, or Wilson-line masses
3. **Trade-off identified**: E₆ wins on vacuum energy but requires stronger parameter constraints
4. **Conservative choice**: If full admissibility required, SU(5) or SO(10) are safer

## Open Items

1. Loop corrections from 36 E₆ exotics (requires numerical computation)
2. PS hypercharge embedding verification
3. Hosotani mechanism θ determination
4. Numerical constraints on L (requires forbidden inputs)

## Verification

```bash
cd derivation_v42
python3 recompute.py
# Expected: 27/27 CHECKS PASSED
```

---

*Report generated: 2026-02-04*
