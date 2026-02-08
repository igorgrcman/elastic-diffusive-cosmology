# DATA GAPS (V7)

**Created**: 2026-01-31
**Purpose**: Document missing BL data needed for complete testing
**Status**: ~30 intermediate nuclides lack full BL coverage

---

## Gap Categories

### Category A: Intermediate Chain Nuclides (Low Priority)

These nuclides have BL data for t₁/₂ and decay mode, but were not fully extracted:

| Chain | Nuclide | Missing Data | Impact |
|-------|---------|--------------|--------|
| U-238 | ²³⁴Th | Q-values, BR details | Low — pure β⁻ |
| U-238 | ²³⁴Pa | Isomer data | Low — complex but not branchpoint |
| U-238 | ²³⁴U | None critical | Already covered |
| U-238 | ²³⁰Th | None critical | Already covered |
| U-238 | ²²⁶Ra | None critical | Already covered |
| U-238 | ²²²Rn | None critical | Already covered |
| U-238 | ²¹⁸Po | Minor branches | Low — α dominant |
| U-238 | ²¹⁴Pb | None critical | Pure β⁻ |
| U-238 | ²¹⁴Bi | Detailed BR | Medium — minor α branch |
| U-238 | ²¹⁴Po | None critical | Pure α |
| U-238 | ²¹⁰Pb | None critical | Pure β⁻ |
| U-238 | ²¹⁰Bi | Minor α branch | Low |
| U-238 | ²¹⁰Po | None critical | Pure α |

**U-238 Gap Count**: 3 medium, 10 low

---

### Category B: Th-232 Chain (Partial Coverage)

| Nuclide | Missing Data | Impact |
|---------|--------------|--------|
| ²²⁸Ra | None critical | Pure β⁻ |
| ²²⁸Ac | None critical | Pure β⁻ |
| ²²⁸Th | None critical | Pure α |
| ²²⁴Ra | None critical | Pure α |
| ²²⁰Rn | None critical | Pure α |
| ²¹⁶Po | None critical | Pure α |
| ²¹²Pb | None critical | Pure β⁻ |
| **²¹²Bi** | **COMPLETE** | **Mandatory branchpoint** |
| ²¹²Po | None critical | Pure α |
| ²⁰⁸Tl | None critical | Pure β⁻ |

**Th-232 Gap Count**: 0 critical (branchpoint covered)

---

### Category C: U-235 Chain (Partial Coverage)

| Nuclide | Missing Data | Impact |
|---------|--------------|--------|
| ²³¹Th | None critical | Pure β⁻ |
| ²³¹Pa | None critical | Pure α |
| **²²⁷Ac** | **COMPLETE** | **Mandatory branchpoint** |
| ²²⁷Th | Minor branches | Low |
| ²²³Fr | Minor α branch | Low |
| ²²³Ra | None critical | Pure α |
| ²¹⁹Rn | None critical | Pure α |
| ²¹⁵Po | None critical | Pure α |
| ²¹¹Pb | None critical | Pure β⁻ |
| **²¹¹Bi** | **COMPLETE** | **Mandatory branchpoint** |
| ²¹¹Po | None critical | Pure α |
| ²⁰⁷Tl | None critical | Pure β⁻ |

**U-235 Gap Count**: 0 critical (branchpoints covered)

---

## Category D: Missing for Half-Life Correlation (High Priority)

To test whether d(n) improves Geiger-Nuttall predictions, we need:

| Requirement | Current Status | Gap |
|-------------|----------------|-----|
| 15-20 α-emitters | 6 available | **9-14 needed** |
| Wide d(n) range [0.2, 2.0] | Narrow range [0.3, 1.8] | **Extend range** |
| Precise Q_α (< 1%) | 6 with AME2020 | OK |
| Precise t₁/₂ (< 10%) | 6 with NUBASE2020 | OK |

### Recommended Additional Nuclides for G-N Test

| Nuclide | Z | Q_α (MeV) | t₁/₂ | d(n) est. | Why Include |
|---------|---|-----------|------|-----------|-------------|
| ²⁴⁴Cm | 96 | 5.902 | 18.1 y | ~2.0 | High d(n) |
| ²⁴⁰Pu | 94 | 5.256 | 6564 y | ~1.9 | Actinide |
| ²⁴²Pu | 94 | 4.985 | 3.75×10⁵ y | ~1.9 | Long-lived |
| ²²⁸Th | 90 | 5.520 | 1.91 y | ~1.3 | Th-232 chain |
| ²²⁴Ra | 88 | 5.789 | 3.63 d | ~1.0 | Th-232 chain |
| ²²⁰Rn | 86 | 6.405 | 55.6 s | ~0.8 | Short-lived |
| ²¹⁶Po | 84 | 6.906 | 145 ms | ~0.6 | Very short |
| ²¹⁰Po | 84 | 5.407 | 138.4 d | ~0.3 | U-238 chain |
| ²⁰⁹Po | 84 | 4.979 | 124 y | ~0.2 | Low d(n) |

**Status**: [BL:SOURCE_NEEDED] — These Q_α and t₁/₂ need NNDC verification

---

## Category E: Superheavy Element Data (Future)

For testing H-N48-04 (n=48 target for A > 350):

| Region | A Range | Available Data | Gap |
|--------|---------|----------------|-----|
| Oganesson | 294 | t₁/₂ only | Q_α uncertain |
| Flerovium | 284-289 | Partial | Decay modes uncertain |
| Moscovium | 287-290 | Minimal | Most data tentative |
| Island of Stability | ~298-310 | Theoretical | No experimental data |

**Status**: [P] — SHE data insufficient for d(n) testing

---

## Category F: Spin-Parity Data for H-N48-01c

To test the conditional d(n) rule with spin-parity:

| Branchpoint | Parent Jπ | α-Daughter Jπ | β-Daughter Jπ | Status |
|-------------|-----------|---------------|---------------|--------|
| ²¹²Bi | 1⁻ | 5⁺ (²⁰⁸Tl) | 0⁺ (²¹²Po) | Need verification |
| ²²⁷Ac | 3/2⁻ | 3/2⁻ (²²³Fr) | 1/2⁺ (²²⁷Th) | **Available** |
| ²¹¹Bi | 9/2⁻ | 1/2⁺ (²⁰⁷Tl) | 9/2⁺ (²¹¹Po) | Need verification |

**Key Insight from ²²⁷Ac**:
- ²²⁷Ac (3/2⁻) → ²²⁷Th (1/2⁺): ΔJ=1, parity change — **Allowed GT**
- ²²⁷Ac (3/2⁻) → ²²³Fr (3/2⁻): ΔJ=0, no parity change — but Coulomb barrier

This explains why β⁻ dominates despite Q_α >> Q_β.

---

## Summary: Gap Priorities

| Priority | Gap Type | Count | Action Required |
|----------|----------|-------|-----------------|
| **Critical** | Mandatory branchpoints | 0 | ✓ All 3 covered |
| **High** | G-N correlation dataset | 9-14 | Expand α-emitter list |
| **Medium** | Spin-parity for H-N48-01c | 2 | Verify Jπ assignments |
| **Low** | Intermediate chain nuclides | ~20 | Not blocking |
| **Future** | SHE for n=48 target | Many | Await experimental data |

---

## Recommended Next Steps

1. **Immediate**: Accept current BL coverage as sufficient for V7 conclusions
2. **Short-term**: Build 15-nuclide α-emitter dataset for G-N + d(n) regression
3. **Medium-term**: Verify spin-parity for all branchpoints to test H-N48-01c
4. **Long-term**: Monitor SHE discoveries for n=48 target evidence

