# Derivation v21 — Acceptance Criteria

## Required Checks (AC-P29-*)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P29-1 | Only derivation_v21/ modified/created | ✅ PASS |
| AC-P29-2 | PDF builds, 0 undefined refs/cites, 0 private paths | ✅ PASS |
| AC-P29-3 | ≥ 25 displayed equations in Sections 2-5 | ✅ PASS (42 total) |
| AC-P29-4 | Includes BC1+BC2 explicitly with m_n formulas | ✅ PASS |
| AC-P29-5 | Includes explicit inversion R_xi = pi/m_gap | ✅ PASS |
| AC-P29-6 | Includes proxy table (M_Z, M_W, v_EW) with R_xi and M_5 | ✅ PASS |
| AC-P29-7 | Includes TikZ figure with two panels | ✅ PASS |
| AC-P29-8 | Pages ≥ 7 | ✅ PASS (9 pages) |

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | ✅ |
| No undefined references | ✅ |
| No undefined citations | ✅ |
| No private paths in PDF | ✅ |

## Content Verification

| Section | Content | Status |
|---------|---------|--------|
| §1 | Factor Lock box (v20 conventions) | ✅ |
| §2 | 5D mode equation derivation | ✅ |
| §3 | BC1, BC2, BC3 with spectra | ✅ |
| §4 | Mass gap definition and inversion | ✅ |
| §5 | EW proxy selection and table | ✅ |
| §6 | Closure chain and open items | ✅ |
| §7 | TikZ figure | ✅ |
| §8 | Epistemic summary table | ✅ |

## Derived Quantities

| Quantity | Formula | Tag |
|----------|---------|-----|
| BC1 spectrum | m_n = n*pi/R_xi | [D] |
| Mass gap | m_gap = pi/R_xi | [D] |
| Inversion | R_xi = pi/m_gap | [D] |
| Identification | m_gap = M_Z | [I]+[BL] |
| R_xi value | 6.80 x 10^-18 m | [I]+[BL] |
| M_5 value | 4.3 x 10^12 GeV | [D] |

## Proxy Table Included

| Proxy | M_* (GeV) | R_xi (m) | M_5 (GeV) |
|-------|-----------|----------|-----------|
| M_Z | 91.19 | 6.80e-18 | 4.28e12 |
| M_W | 80.38 | 7.72e-18 | 4.07e12 |
| v_EW | 246.2 | 2.52e-18 | 5.98e12 |

## Final Status

**✅ ALL ACCEPTANCE CRITERIA MET**

---

*Acceptance recorded: 2026-02-03*
