# P45 / Derivation v44: ANOMALY ONE-SHOT SoT LOCK — Final Report

## Objective

Create an engineering-grade Single Source of Truth (SoT) for SM anomaly calculations
with hash-locked LaTeX↔Python synchronization, eliminating drift between documentation
and verification code.

## Implementation

### 1. Single Source of Truth (SoT_FIELDS)

Defined in `recompute.py`:
```python
SoT_FIELDS = [
    {"name": "Q_L", "Y": Fraction(1,6), "multiplicity": 6, ...},
    {"name": "L_L", "Y": Fraction(-1,2), "multiplicity": 2, ...},
    {"name": "u_L^c", "Y": Fraction(-2,3), "multiplicity": 3, ...},
    {"name": "d_L^c", "Y": Fraction(1,3), "multiplicity": 3, ...},
    {"name": "e_L^c", "Y": Fraction(1,1), "multiplicity": 1, ...},
    {"name": "nu_L^c", "Y": Fraction(0,1), "multiplicity": 1, "BC": "LR", ...},
]
```

Each field contains:
- Name, LaTeX representation
- SU(3), SU(2) representations
- Hypercharge Y (exact Fraction)
- Multiplicity, color factor, SU(2) factor
- Boundary condition (RR/LL/LR)
- Zero-mode status, epistemic tag

### 2. Auto-Generated Tables

`generate_tables()` produces `tables_generated.tex` containing:
- Canonical LH Weyl basis table
- U(1)³ anomaly calculation table
- U(1)-gravitational anomaly table
- Complete anomaly summary table
- SU(2)²U(1) anomaly table

### 3. Hash Lock Protocol

```python
def compute_hash(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()[:16]
```

Any modification to `tables_generated.tex` that doesn't match regeneration causes FAIL.

### 4. Anomaly Calculations (all = 0)

| Anomaly | Formula | Result |
|---------|---------|--------|
| SU(3)³ | Σ A(R) × n_SU2 | 0 |
| SU(2)²U(1) | Σ n_c × T(R) × Y | 0 |
| SU(3)²U(1) | Σ n_SU2 × T(R) × Y | 0 |
| U(1)³ | Σ m_i × Y_i³ | 0 |
| U(1)-grav | Σ m_i × Y_i | 0 |
| Witten | n_doublets mod 2 | 0 |

### 5. Two-Route Verification

- Route 1: Direct sum over all fields
- Route 2: Grouped by sector (quarks vs leptons)
- Both routes produce identical results

## Verification Results

```
Total: 26/26 CHECKS PASSED
Check count requirement (>=25): PASS
ALL CHECKS PASSED
Tables hash: ea07022b108f0721
```

## Metrics Achieved

| Metric | Required | Achieved | Status |
|--------|----------|----------|--------|
| Pages | ≥24 | 30 | ✓ |
| Equations | ≥140 | 155 | ✓ |
| Labels | ≥180 | 242 | ✓ |
| Checks | ≥25 | 26 | ✓ |
| Reviewer traps | ≥14 | 16 | ✓ |

## Document Structure

1. Introduction and Motivation
2. Single Source of Truth Definition
3. Auto-Generated Tables
4. Anomaly Coefficient Definitions
5. Lock Protocol
6. Verification Results
7. Epistemic Status Summary
8. Normalization Conventions
9. Common Pitfalls and Reviewer Traps
10. Reproduction Instructions
11. Conclusion

Appendices:
- A: Anomaly Coefficient Formulas
- B: SoT Field Details
- C: Detailed U(1)³ Calculation
- D: Python SoT Structure
- E: Extended Anomaly Analysis
- F: Cross-Track Comparison
- G: Boundary Condition Analysis
- H: Group Theory Review
- I: Rational Arithmetic Verification
- J: Hash Algorithm Details
- K: Partial Sum Verification
- L: Complete Verification Checklist
- M: Detailed Anomaly Triangle Diagrams
- N: Pati-Salam Origin of Hypercharges
- O: Hypercharge Quantization
- P: Generation Structure
- Q: Alternative Anomaly Bases
- R: Relation to GUT Anomaly Freedom
- S: Numerical Stability Analysis
- T: Extended Two-Route Verification
- U: Witten Anomaly Details

## Files Produced

- `main.tex` — Main document
- `main.pdf` — Compiled PDF
- `recompute.py` — SoT + verification
- `tables_generated.tex` — Auto-generated tables
- `EDC_BLOCK003_DERIVATION_V44_ANOMALY_ONESHOT_SOT_LOCK.pdf` — Export
- `README.md` — This file
- `REPORT.md` — This report
- `ACCEPTANCE.md` — Acceptance criteria

## Conclusion

Derivation v44 successfully implements the SoT lock protocol, providing audit-proof
anomaly calculations with zero drift between LaTeX and Python. All acceptance criteria
are met.
