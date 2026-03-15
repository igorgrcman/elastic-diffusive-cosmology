# Derivation v32 — Detailed Report

## Executive Summary

Derivation v32 establishes how boundary conditions (BC) and orbifold projections can
break a 5D parent gauge group to produce the Standard Model gauge structure. Four
parallel tracks are developed: SU(5), SO(10), E_6, and Pati-Salam. For each, explicit
generator survival matrices and closure proofs are provided.

**NO FORBIDDEN INPUTS** are used anywhere in this derivation.

---

## 1. Inputs Used Table (AC-P40-8 Dependency-Proof)

**CRITICAL**: This table lists EVERY symbol with a numerical value used in v32.
NONE are from the forbidden list.

| Symbol | Value | Units | Source File:Line | Tag |
|--------|-------|-------|------------------|-----|
| pi | 3.14159265... | -- | recompute.py:17 | mathematical |
| L_TEST | 1.0 | arbitrary | recompute.py:18 | [TEST] |
| b_test | 1.0 | dimensionless | recompute.py:203 | [TEST] |
| c_Y | 5/3 | dimensionless | main.tex:eq(41) | [Dc] |
| dim(SU(5)) | 24 | count | main.tex, recompute.py | [D] |
| dim(SO(10)) | 45 | count | main.tex, recompute.py | [D] |
| dim(E_6) | 78 | count | main.tex, recompute.py | [D] |
| dim(PS) | 21 | count | main.tex, recompute.py | [D] |
| dim(SM) | 12 | count | main.tex, recompute.py | [D] |

**Verification**: NONE of these are {M_Z, M_W, v_EW, l_P, G_N, alpha_EM}.

**AC-P40-8 STATUS: PASS**

---

## 2. Gauge Coupling Bridge (Section 5)

### Main Result

$$\frac{1}{g_4^2} = \frac{1}{g_5^2} \int_0^L d\xi \, e^{-2A(\xi)} |f_0(\xi)|^2 \equiv \frac{I_{\text{gauge}}}{g_5^2}$$

**Tag**: [D]

### Flat Limit

$$I_{\text{gauge}}^{\text{flat}} = 1 \Rightarrow g_4^2 = g_5^2$$

### With Brane Terms

$$\frac{1}{g_4^2} = \frac{1}{g_5^2}\left( I_{\text{gauge}} + r_0 |f_0(0)|^2 + r_L |f_0(L)|^2 \right)$$

---

## 3. BC Registry (Section 6)

| Field | BC Type | Zero Mode? | Gap |
|-------|---------|------------|-----|
| Graviton | N/N | Yes | pi/L |
| Gauge (kept) | N/N | Yes | pi/L |
| Gauge (broken) | D/D | No | pi/L |
| Scalar (even) | N/N | Yes | pi/L |
| Scalar (odd) | D/D | No | pi/L |
| Fermion L | (+,+) | Yes (chiral) | -- |
| Fermion R | (-,-) | No | -- |

**AC-P40-10 STATUS: PASS** (4+ field types covered)

---

## 4. Track S: SU(5) Breaking (Section 7)

### Generator Survival

| Generators | Count | Parity | Zero Mode |
|------------|-------|--------|-----------|
| SU(3)_c | 8 | (+,+) | Yes |
| SU(2)_L | 3 | (+,+) | Yes |
| U(1)_Y | 1 | (+,+) | Yes |
| X bosons | 6 | (-,-) | No |
| Y bosons | 6 | (-,-) | No |

**Total**: 24 = 12 (surviving) + 12 (broken)

### Closure Proof

Surviving generators close under commutation:
- [T_SU(3), T_SU(3)] in su(3)
- [T_SU(2), T_SU(2)] in su(2)
- [T_Y, anything] = 0

Residual: su(3) + su(2) + u(1) direct sum

**AC-P40-14 STATUS: PASS**

---

## 5. Track O: SO(10) Breaking (Section 8)

### Generator Survival

| Generators | Count | Zero Mode |
|------------|-------|-----------|
| SM (via SU(5)) | 12 | Yes |
| U(1)_chi | 1 | No |
| Coset | 32 | No |

**Total**: 45 = 12 + 33

### Closure

Same SM algebra: su(3) + su(2) + u(1)

---

## 6. Track P: Pati-Salam (Section 9)

### SO(10) -> PS Count

$$45 = 21 \text{ (PS)} + 24 \text{ (coset)}$$

### Hypercharge Formula

$$Y = T_{3R} + \frac{B-L}{2}$$

**AC-P40-11 STATUS: PASS** (PS track with Y formula)

---

## 7. Track E: E_6 Breaking (Section 10)

### E_6 -> SO(10) Count

$$78 = 45 \text{ (SO(10))} + 33 \text{ (broken)}$$

### Two-Step Breaking

E_6 -> SO(10) -> SM

---

## 8. Python Verification Summary

`recompute.py`: ALL 16 CHECKS PASSED

1. Forbidden token grep gate (numeric values) PASS
2. SU(5) survival count: 8+3+1=12 PASS
3. SO(10) survival count: 45-33=12 PASS
4. PS count: 45=21+24 PASS
5. PS -> SM count: 8+3+1=12 PASS
6. E_6 survival: 78=45+33 PASS
7. Neumann zero mode exists PASS
8. Dirichlet no zero mode PASS
9. Robin spectrum PASS
10. Gap monotonicity PASS
11. Dimensional audit PASS
12. Hypercharge normalization c_Y=5/3 PASS
13. Scale map TikZ present PASS
14. Algebra closure PASS
15. No private paths PASS
16. Equation count >= 120 PASS

---

## 9. Trap Resolution

| # | Trap | Status |
|---|------|--------|
| 1 | Hidden alpha_EM | PASS |
| 2 | Hypercharge norm | PASS (c_Y = 5/3) |
| 3 | A_5 scalar | PASS (Section 11) |
| 4 | Orbifold factor | PASS |
| 5 | BC from variation | PASS (Theorem 2.1) |
| 6 | Closure proof | PASS |
| 7 | Generator count | PASS |
| 8 | Dimension g_5 | PASS |
| 9 | Brane kinetic | PASS |
| 10 | Gauge fixing | PASS |
| 11 | Warp exponent | PASS |
| 12 | Scale map | PASS (TikZ) |
| 13 | Anomaly note | PASS ([OPEN]) |
| 14 | PS hypercharge | PASS |

---

## 10. Closure Status

### Structural Closure: ACHIEVED

- BC classes derived [D]
- Gauge bridge derived [D]
- Generator survival matrices complete [D]
- Closure proofs complete [D]

### Point Selection: OPEN

- Parent group G_5 is [P]
- Specific k-branch is [OPEN]

---

## 11. Conclusions

1. **Gauge Bridge**: g_4^{-2} = g_5^{-2} I_gauge [D]
2. **Four Tracks**: SU(5), SO(10), PS, E_6 all demonstrated
3. **Generator Survival**: Complete matrices with closure proofs
4. **Scale Map**: TikZ figure with UV/KK/IR regimes
5. **No Forbidden Inputs**: Verified by grep gate

---

*Report generated: 2026-02-03*
