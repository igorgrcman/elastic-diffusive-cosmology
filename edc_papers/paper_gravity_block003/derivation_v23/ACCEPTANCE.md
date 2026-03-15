# Derivation v23 — Acceptance Criteria

## Required Checks (AC-P31-*)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P31-1 | Only derivation_v23/ modified/created | ✅ PASS |
| AC-P31-2 | FROZEN main.tex MD5 = e592a943... | ✅ PASS |
| AC-P31-3 | PDF builds, 0 undefined refs/cites, 0 private paths | ✅ PASS |
| AC-P31-4 | ≥ 12 pages | ✅ PASS (15 pages) |
| AC-P31-5 | ≥ 60 equation environments | ✅ PASS (97) |
| AC-P31-6 | v22 convention explicitly used (R_ξ ≡ L; m_gap = π/R_ξ) | ✅ PASS |
| AC-P31-7 | Both Planck conventions + (8π)^{1/3} conversion | ✅ PASS |
| AC-P31-8 | Final Ledger table + Compatibility section | ✅ PASS |
| AC-P31-9 | Export name correct | ✅ PASS |

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | ✅ |
| No undefined references | ✅ |
| No undefined citations | ✅ |
| No private paths in PDF | ✅ |

## Content Sections

| Section | Content | Status |
|---------|---------|--------|
| §1 | Convention lock box | ✅ |
| §2 | 5D action (bulk + GHY + brane) | ✅ |
| §3 | Background and linearization | ✅ |
| §4 | KK decomposition | ✅ |
| §5 | BCs and spectrum | ✅ |
| §6 | Normalization integral and bridge | ✅ |
| §7 | Newton constant bridge | ✅ |
| §8 | R_ξ identification | ✅ |
| §9 | M_5 closure (both conventions) | ✅ |
| §10 | Error budget | ✅ |
| §11 | Conventions dictionary | ✅ |
| §12 | Epistemic ledger | ✅ |
| §13 | Compatibility with v15-v21 | ✅ |
| §14 | Final canonical values | ✅ |
| §15 | Summary of derivation chain | ✅ |

## Canonical Values Derived

| Quantity | Value | Tag |
|----------|-------|-----|
| R_ξ | 6.80 × 10⁻¹⁸ m | [BL] |
| M_5 (reduced) | 5.6 × 10¹² GeV | [D] |
| M_5 (original) | 1.6 × 10¹³ GeV | [D] |
| δM_5/M_5 | 1.1 × 10⁻⁵ | [D] |

## Epistemic Ledger Present

- [P] Postulates: 5D action, flat background
- [D] Derived: KK spectrum, bridge relation, M_5 closure, G_N
- [I]+[BL] Identification: m_gap = M_Z
- [BL] Baselines: M_Z^obs, M̄_Pl
- NO-GO: Internal R_ξ derivation
- OPEN: m_gap = M_Z proof

## Compatibility Mappings Verified

| Conversion | Formula |
|------------|---------|
| R_ξ | R_ξ^(canon) = π × R_ξ^(old) |
| M_5 | M_5^(canon) = π^{-1/3} × M_5^(old) |

## Final Status

**✅ ALL ACCEPTANCE CRITERIA MET**

---

*Acceptance recorded: 2026-02-03*
