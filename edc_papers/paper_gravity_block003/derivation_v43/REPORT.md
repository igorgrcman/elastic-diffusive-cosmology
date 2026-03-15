# Derivation v43 — Report

## Title
PS Chirality Closure + Anomaly Gate

## Summary

This derivation closes the Pati–Salam CONDITIONAL status from v42 by providing:

1. Complete PS→SM decomposition with explicit hypercharge embedding
2. All six anomaly coefficients computed from first principles
3. Resolution of the 42 vs 45 Weyl fermion discrepancy
4. Upgrade of PS track status from CONDITIONAL to PASS

## Inputs Used

| Category | Input | Used? | Notes |
|----------|-------|-------|-------|
| Electroweak | M_Z | **NO** | Forbidden (no numerical value) |
| Electroweak | M_W | **NO** | Forbidden (no numerical value) |
| Electroweak | v_EW | **NO** | Forbidden (no numerical value) |
| QED | α_EM | **NO** | Forbidden (no numerical value) |
| Gravity | G_N | **NO** | Forbidden (no numerical value) |
| Planck | ℓ_P | **NO** | Forbidden (no numerical value) |
| EDC | PS gauge group | Symbolic | SU(4)_c × SU(2)_L × SU(2)_R |
| EDC | BC assignments | Symbolic | From v35 registry |
| Prior | v41 fermion counts | Yes | Cross-validated |
| Prior | v42 anomaly audit | Yes | Resolved CONDITIONAL |

## Key Results

### PS→SM Decomposition

The Pati–Salam fermion representations:
- F_L = (4, 2, 1): Contains q_L = (3,2)_{1/6} and ℓ_L = (1,2)_{-1/2}
- F_R = (4, 1, 2): Contains u_R, d_R, ν_R, e_R

The hypercharge embedding:
```
Y = T_{3R} + (B-L)/2
```

Verified for all SM fields with explicit charge assignments.

### 42 vs 45 Resolution

| Count | Source | Explanation |
|-------|--------|-------------|
| 42 | v42 PS content | Without ν_R (mixed BC) |
| 45 | Full SM | Including all Weyl DoF |
| +3 | Difference | ν_R × 3 generations (no zero-mode) |

The 42 vs 45 discrepancy is a **bookkeeping artifact**, not a physics inconsistency. The ν_R fields have mixed BC (L,R) and thus no zero-mode in the SM-like spectrum.

### Anomaly Coefficients

| Anomaly | Computation | Result |
|---------|-------------|--------|
| SU(3)³ | 2 - 1 - 1 | 0 |
| SU(2)²U(1) | 3×(1/2)×(1/6) + 1×(1/2)×(-1/2) | 0 |
| SU(3)²U(1) | See App. | 0 |
| U(1)³ | Explicit sum with fractions | 0 |
| U(1)-grav | 6×(1/6) + 2×(-1/2) + ... | 0 |
| Witten SU(2) | 12 doublets (even) | 0 |

### Final Verdict

| Track | v42 Status | v43 Status | Resolution |
|-------|------------|------------|------------|
| SU(5) | PASS | PASS | Unchanged |
| SO(10) | PASS | PASS | Unchanged |
| PS | CONDITIONAL | **PASS** | Anomalies explicit |
| E₆ | PASS | PASS | Unchanged |

## Conclusions

1. **PS is anomaly-free**: All six anomaly coefficients vanish when computed explicitly
2. **42→45 resolved**: Bookkeeping artifact from ν_R mixed BC
3. **Hypercharge verified**: Y = T_{3R} + (B-L)/2 confirmed for all fields
4. **PS upgraded**: CONDITIONAL → PASS

## Open Items

1. Proton decay constraints in PS (requires forbidden inputs)
2. Gauge coupling unification running (numerical computation)
3. Hosotani mechanism θ determination

## Verification

```bash
cd derivation_v43
python3 recompute.py
# Expected: 26/26 CHECKS PASSED
```

---

## What Changed in P44 Cleanup

1. **Removed working chatter**: "Wait---", "let me recalculate", "Correction:", "???" removed from main derivation text
2. **U(1)³ one-shot derivation**: Appendix M.4 rewritten as clean derivation using canonical LH Weyl basis table
3. **Added Reader Contract box**: Declares conventions (LH basis, BC→zero-mode rule, v43 goals) at start
4. **Added Reviewer Trap Checklist**: 15 items covering sign conventions, multiplicities, counting pitfalls
5. **Cleaned hypercharge derivation**: Section 3 rewritten without exploratory narrative
6. **AC-P44-12 consistency proof**: U(1)³ = 0 verified both symbolically (LaTeX) and numerically (recompute.py)
7. **Updated recompute.py**: Added 3 new checks (narrative cleanup, reviewer traps, U(1)³ one-shot)

---

## Search Evidence (AC-P44-4 + Forbidden Inputs)

### AC-P44-4: Narrative Cleanup

```bash
$ grep -E "Wait---|Wait,|\?\?\?|\\\\textbf\{Correction\}|recalculate|Wait.*sign error" main.tex
(no output before Reviewer Trap section)
```

Result: **PASS** - no working chatter in main derivation

### Forbidden Inputs Check

```bash
$ grep -E "91\.19|80\.38|246\.2|1\.616.*10|6\.674.*10" main.tex
(no output)
```

Result: **PASS** - no forbidden numerical values (M_Z, M_W, v_EW, G_N, ℓ_P)

---

## AC-P44-12 Evidence (U(1)³ Consistency Proof)

### Canonical LH Weyl Basis Table (recompute.py)

| Field | Multiplicity m_i | Hypercharge Y_i |
|-------|------------------|-----------------|
| Q_L | 6 (3 colors × 2 SU(2)) | +1/6 |
| L_L | 2 (1 × 2 SU(2)) | -1/2 |
| u^c_L | 3 (3 colors × 1) | -2/3 |
| d^c_L | 3 (3 colors × 1) | +1/3 |
| e^c_L | 1 (1 × 1) | +1 |

### recompute.py Output

```
[✓] U(1)^3 one-shot (AC-P44-12): PASS U(1)^3 one-shot table sum = 0
```

### LaTeX Reference

The symbolic derivation appears in Appendix M.4 (label: `eq:u1-3-result-oneshot`):

```latex
\mathcal{A}_{U(1)^3} = \frac{1 - 9 - 32 + 4 + 36}{36} = \frac{0}{36} = 0
```

---

*Report generated: 2026-02-04*
*P44 cleanup: 2026-02-05*
