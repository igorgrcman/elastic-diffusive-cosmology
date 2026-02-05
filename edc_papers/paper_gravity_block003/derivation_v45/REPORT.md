# P46 / Derivation v45: SoT-Lock Track Compiler — Final Report

## Objective

Create a unified "track compiler" that processes GUT track definitions and produces:
- Full anomaly audit (all 6 + Witten) for all four tracks
- ΔE_vac^finite scoring inputs
- Mass-gating constraints for exotics

All from a Single Source of Truth (SoT_TRACKS) with hash-locked verification.

## Implementation

### 1. SoT_TRACKS Structure

Defined in `recompute.py`:
```python
SoT_TRACKS = {
    "SU5": {
        "name": "SU(5)",
        "gauge_sector": { ... },
        "matter_fields": [ ... ],
        "exotics": [ ... ],
        ...
    },
    "SO10": { ... },
    "PS": { ... },
    "E6": { ... },
}
```

Each track contains:
- Group data (parent G, survivors H, rank)
- Gauge sector (generator counts by BC class)
- Matter fields (LH Weyl basis with BC, zero-mode, Y, reps)
- Exotics (with decoupling mechanism)
- BC reference for ΔE_vac

### 2. Auto-Generated Tables (8 total)

| Table | Content |
|-------|---------|
| T1 | Track overview |
| T2 | Field inventory |
| T3 | Anomaly coefficients |
| T4 | ΔE_vac ingredients |
| T5 | Exotics and gating |
| T6 | Admissibility |
| T7 | Detailed U(1)³ |
| T8 | Two-route verification |

### 3. Anomaly Calculations

All 6 gauge anomalies + Witten computed per track:
- SU(3)³ = 0 (all tracks)
- SU(2)²U(1) = 0 (all tracks)
- SU(3)²U(1) = 0 (all tracks)
- U(1)³ = 0 (all tracks)
- U(1)-grav = 0 (all tracks)
- Witten = even (all tracks)

### 4. ΔE_vac Scoring

Score = (n_gauge_mixed - n_gauge_NN) - 4*(n_ferm_mixed - n_ferm_NN)

| Track | Score | Rank |
|-------|-------|------|
| PS | 25 | 1 (best) |
| SU(5) | 32 | 2 |
| SO(10) | 49 | 3 |
| E6 | 82 | 4 |

### 5. Mass Gating Analysis

| Track | Exotics | Mechanism | Status |
|-------|---------|-----------|--------|
| SU(5) | T_H, T̄_H | Brane mass | CONDITIONAL |
| SO(10) | --- | --- | PASS |
| PS | LQ | Mixed BC | PASS |
| E6 | D, D̄, H_d, H_u, S | Mixed/Brane/Hosotani | CONDITIONAL |

### 6. Admissibility Results

- **SU(5)**: CONDITIONAL (brane mass tuning required)
- **SO(10)**: PASS (minimal, no exotics)
- **PS**: PASS (BC projection works)
- **E6**: CONDITIONAL (Hosotani + brane mass required)

## Verification Results

```
Total: 56/56 CHECKS PASSED
Check count requirement (>=30): PASS
ALL CHECKS PASSED
Tables hash: a80b3886903152d3
```

## Metrics Achieved

| Metric | Required | Achieved | Status |
|--------|----------|----------|--------|
| Pages | ≥28 | 28 | ✓ |
| Equations | ≥160 | 192 | ✓ |
| Labels | ≥220 | 291 | ✓ |
| Checks | ≥30 | 56 | ✓ |
| Reviewer traps | ≥16 | 18 | ✓ |

## Document Structure

**Main Sections:**
1. Introduction and Motivation
2. Single Source of Truth: Track Definitions
3. Track Inventory (SU5, SO10, PS, E6)
4. Auto-Generated Tables
5. Anomaly Coefficient Calculations
6. Vacuum Energy Analysis
7. Mass Gating Analysis
8. Lock Protocol
9. Verification Results
10. Epistemic Status Summary
11. Reviewer Traps (18 items)
12. Reproduction Instructions
13. Conclusion

**Appendices:**
- A: Detailed Anomaly Calculations
- B: Vacuum Energy Details
- C: Group Theory Review
- D: Hypercharge Assignments
- E: Track-Specific Details
- F: Witten Anomaly Details
- G: Two-Route Verification Details
- H: Exotic Field Catalog
- I: Rational Arithmetic
- J: Hash Algorithm
- K: GUT Rank Analysis
- L: Generator Counting
- M: Complete Verification Checklist
- N: Detailed Track-by-Track Analysis
- O: BC Projection Algebra
- P: Vacuum Energy Regularization
- Q: GUT Breaking Mechanisms
- R: Proton Decay Constraints
- S: Gauge Coupling Unification
- T: Anomaly Polynomial Method
- U: Extended SoT Field Details

## Files Produced

- `main.tex` — Main document (1700+ lines)
- `main.pdf` — Compiled PDF
- `recompute.py` — SoT + 56-check verification
- `tables_generated.tex` — Auto-generated tables
- `EDC_BLOCK003_DERIVATION_V45_SOT_LOCK_TRACK_COMPILER.pdf` — Export
- `README.md`, `REPORT.md`, `ACCEPTANCE.md` — Documentation

## Conclusion

Derivation v45 successfully implements the SoT-lock track compiler, providing
a unified framework for auditing all four GUT tracks. The recommended tracks
are SO(10) and PS based on anomaly freedom, exotic gating, and vacuum stability.
