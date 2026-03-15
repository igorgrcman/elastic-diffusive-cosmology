# P15 Acceptance Criteria — Derivation v4

**Task:** Fix constant C in κ₅² = C·σ^(-3/4) from EDC-internal postulates

---

## Criteria Checklist

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| P15-AC1 | Scope respected (no edc_book_2/ changes) | ✅ PASS | `git status` shows only derivation_v4/ changes |
| P15-AC2 | paper_gravity_block003/main.tex untouched | ✅ PASS | Hash unchanged from FROZEN version |
| P15-AC3 | At least 2 independent attempt branches | ✅ PASS | Attempts A, B, C all present |
| P15-AC4 | Each attempt has dimensional check | ✅ PASS | Explicit [dim] annotations in each section |
| P15-AC5 | Clear statement of what would fix C | ✅ PASS | Section 6.2 lists 4 options |
| P15-AC6 | Formal NO-GO if unsuccessful | ✅ PASS | Lemma 1 (Dimensional Counting No-Go) proven |
| P15-AC7 | Zero undefined refs/cites | ✅ PASS | `grep "undefined" main.log` = font warning only |
| P15-AC8 | Zero private paths in PDF | ✅ PASS | No /Users/ paths in PDF metadata |
| P15-AC9 | Canonical export name unique | ✅ PASS | `EDC_BLOCK003_DERIVATION_V4_FIX_C.pdf` |
| P15-AC10 | REPORT.md with MD5 table | ✅ PASS | All checksums recorded |

---

## Anti-Circularity Verification

| Input | Source | Used to Fit G_N? |
|-------|--------|------------------|
| σ | EDC brane tension | NO |
| ρ_P | EDC Plenum density | NO |
| R_ξ | ℏc/M_Z (weak scale) | NO |
| G_N^obs | Forbidden | NOT USED |

✅ Anti-circularity preserved

---

## Outcome Summary

**NO-GO proven via Lemma 1:**
- Available inputs: {σ, ρ_P, R_ξ} with pressure-balance constraint
- Independent scales: 2
- Required to fix C: 3
- Deficit: 1 normalization principle missing

---

## BLOCK-003 Impact

| Before v4 | After v4 |
|-----------|----------|
| "C undetermined" (v3) | "C provably underdetermined by σ, ρ_P, R_ξ" |
| Missing element unclear | Missing element = 1 normalization principle |

Progress: Problem sharpened from "find f(σ)" to "find additional principle"

---

**Acceptance verified by Claude Code**
