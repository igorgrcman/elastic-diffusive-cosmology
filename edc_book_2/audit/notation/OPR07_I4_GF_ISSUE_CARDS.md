# OPR-07 I₄/G_F Issue Cards — Comprehensive Audit

**Date**: 2026-01-25
**Auditor**: Claude (AI assistant)
**Branch**: book2-ch07-openq-remediation-v1

---

## Scan Patterns Used

```bash
grep -rn "I_4\|I₄" src/**/*.tex
grep -rn "dimension.*length\|has dimension of" src/**/*.tex
grep -rn "Wait—\|Let me re-examine" src/**/*.tex
grep -rn "Gaussian.*overlap\|sigma_L\|mode overlap" src/**/*.tex
```

---

## Issue Cards

### CARD-01: ch12_bvp_workpackage.tex:240 — Gaussian Missing Domain
| Field | Value |
|-------|-------|
| File | `sections/ch12_bvp_workpackage.tex` |
| Lines | 237-243 |
| Pattern | Gaussian formula without domain specification |
| What's Wrong | Formula `I_4 = 1/(√(2π)σ)` is full-line result used without stating domain |
| Proposed Fix | Add explicit "full-line normalized" caveat + cross-ref to CH3 half-line treatment |
| Tag | [M] (pedagogy) |
| Severity | **MEDIUM** — misleading but marked as pedagogy |

**Current text:**
```latex
If $f$ is normalized to 1, then $I_4$ measures ``peakedness.'' A Gaussian profile
$f \propto e^{-z^2/2\sigma^2}$ gives:
\[
    I_4 = \frac{1}{\sqrt{2\pi}\sigma}
\]
```

**Issue:** Uses variable `z` instead of `ξ`; no domain stated; missing factor 1/2 for half-line.

---

### CARD-02: ch11_g5_ell_value_closure_attempt.tex:268 — Dimensionally Wrong σ_L Heuristic
| Field | Value |
|-------|-------|
| File | `sections/ch11_g5_ell_value_closure_attempt.tex` |
| Lines | 266-271 |
| Pattern | σ_L heuristic with wrong dimensional relation |
| What's Wrong | `σ_L⁻¹ ~ I₄^{1/4}` is dimensionally inconsistent ([I₄]=E, so [I₄^{1/4}]=E^{1/4} ≠ 1/length) |
| Proposed Fix | Remove or replace with honest statement that localization scale ~ I₄ (both have dimension E) |
| Tag | [P]/OPEN |
| Severity | **HIGH** — dimensional error in published text |

**Current text:**
```latex
The required $I_4 \approx 8$ MeV corresponds to a localization scale:
\begin{equation}
    \sigma_L^{-1} \sim I_4^{1/4} \sim (8 \text{ MeV})^{1/4}
\end{equation}
```

**Issue:** [σ_L⁻¹] = 1/length = Energy. [I₄^{1/4}] = E^{1/4}. These don't match.

---

### CARD-03: ch10_electroweak_bridge.tex:123-124 — Missing Domain & Dimension
| Field | Value |
|-------|-------|
| File | `sections/ch10_electroweak_bridge.tex` |
| Lines | 122-125 |
| Pattern | I₄ definition without domain or dimension check |
| What's Wrong | No explicit domain for integral; no dimensional check |
| Proposed Fix | Add domain specification; add dimension note |
| Tag | [Dc] |
| Severity | **LOW** — conceptual overview, not derivation |

**Current text:**
```latex
\textbf{Step 8: The overlap integral $I_4$ controls $G_F$.}
Given the mode profile $f(\xi)$, the four-fermion overlap $I_4 = \int |f_L|^4 d\xi$
determines how strongly fermions couple at a point.
```

---

### CARD-04: 11_gf_derivation.tex:59,71 — σ_L Heuristic Used
| Field | Value |
|-------|-------|
| File | `sections/11_gf_derivation.tex` |
| Lines | 59, 71 |
| Pattern | σ_L notation used without definition |
| What's Wrong | σ_L is used but relation to I₄ not made explicit; heuristic `G_F ~ G_5/σ_L` not justified |
| Proposed Fix | Note that σ_L is informal; refer to exponential profile for rigorous treatment |
| Tag | [P] |
| Severity | **MEDIUM** — heuristic is informal but not wrong dimensionally |

---

### CARD-05: ch12_bvp_workpackage.tex:237 — Uses `z` Instead of `ξ`
| Field | Value |
|-------|-------|
| File | `sections/ch12_bvp_workpackage.tex` |
| Lines | 222, 238 |
| Pattern | Uses `z` for 5D coordinate |
| What's Wrong | Should use `ξ` per GLOBAL_SYMBOL_TABLE canon |
| Proposed Fix | Replace `z` → `ξ` in Gaussian profile |
| Tag | Notation violation |
| Severity | **HIGH** — violates canon notation |

---

### CARD-06: ch11_gf_full_closure_plan.tex — COMPLIANT ✓
| Field | Value |
|-------|-------|
| File | `sections/ch11_gf_full_closure_plan.tex` |
| Lines | 53, 60 |
| Status | **COMPLIANT** |
| Evidence | Domain [0,ℓ] explicit; dimension check present: "[I₄]=[E]; total [G_F]=[E]⁻² ✓" |

---

### CARD-07: CH3_electroweak_parameters.tex — COMPLIANT ✓
| Field | Value |
|-------|-------|
| File | `CH3_electroweak_parameters.tex` |
| Lines | 638-693 |
| Status | **COMPLIANT** (patched in commit 905830e) |
| Evidence | Domain explicit; dimension check eq:ch3_I4_dimension; half-line factor present; exponential exact result |

---

### CARD-08: 11_gf_derivation.tex:360-400 — COMPLIANT ✓
| Field | Value |
|-------|-------|
| File | `sections/11_gf_derivation.tex` |
| Lines | 360-400 |
| Status | **COMPLIANT** (patched in commit 865bdec) |
| Evidence | Dimension check present; exponential profile; OPR-19 marked |

---

## Summary Table

| Card | File | Severity | Action Required |
|------|------|----------|-----------------|
| CARD-01 | ch12_bvp_workpackage.tex:240 | MEDIUM | Add domain + caveat |
| CARD-02 | ch11_g5_ell_value_closure_attempt.tex:268 | **HIGH** | Remove σ_L heuristic |
| CARD-03 | ch10_electroweak_bridge.tex:123 | LOW | Add domain |
| CARD-04 | 11_gf_derivation.tex:59,71 | MEDIUM | Add informal note |
| CARD-05 | ch12_bvp_workpackage.tex:222,238 | **HIGH** | z → ξ |
| CARD-06 | ch11_gf_full_closure_plan.tex | — | COMPLIANT ✓ |
| CARD-07 | CH3_electroweak_parameters.tex | — | COMPLIANT ✓ |
| CARD-08 | 11_gf_derivation.tex | — | COMPLIANT ✓ |

---

## Patches Required

1. **PATCH-A**: ch12_bvp_workpackage.tex — Fix z→ξ, add domain caveat
2. **PATCH-B**: ch11_g5_ell_value_closure_attempt.tex — Remove dimensional error
3. **PATCH-C**: ch10_electroweak_bridge.tex — Add domain specification
4. **PATCH-D**: 11_gf_derivation.tex — Add informal heuristic note

---

*Audit complete: 2026-01-25*
