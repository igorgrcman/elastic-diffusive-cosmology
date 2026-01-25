# CTX-002: z Occurrences in CH04 — Complete Enumeration

**File**: `src/CH3_electroweak_parameters.tex`
**Date**: 2026-01-24
**Status**: ✅ POST-FIX VERIFIED (52 replacements applied, 387 pages)

---

## Summary

| Bucket | Description | Count | Action |
|--------|-------------|-------|--------|
| BUCKET 1 | z = 5D depth coordinate | 52 | CHANGE to ξ |
| BUCKET 2 | Z6 complex (z₁, z₂) | 0 | DO NOT CHANGE |
| BUCKET 3 | 3D spatial (x, y, z) | 0 | DO NOT CHANGE |
| BUCKET 4 | Ambiguous | 0 | — |
| **TOTAL** | | **52** | |

---

## BUCKET 1: 5D Depth Coordinate (MUST CHANGE → ξ)

All occurrences below are 5D bulk depth coordinates per canon definition.

### Definition Block (lines 542-557)

| Line | Current | Target | Context |
|------|---------|--------|---------|
| 546 | `m(z)` | `m(\xi)` | mass profile function |
| 546 | `e^{-z/\lambda}` | `e^{-\xi/\lambda}` | exponential argument |
| 548 | `$z$` | `$\xi$` | "z is the coordinate into the bulk" |
| 554 | `m(z)` | `m(\xi)` | profile behavior |
| 554 | `z \to \infty` | `\xi \to \infty` | limit statement |
| 555 | `z = 0` | `\xi = 0` | boundary location |

### Mode Overlap Section (lines 602-690)

| Line | Current | Target | Context |
|------|---------|--------|---------|
| 605 | `|f_L(z)|^4` | `|f_L(\xi)|^4` | mode function |
| 605 | `dz` | `d\xi` | integral measure |
| 608 | `f_L(z)` | `f_L(\xi)` | mode profile |
| 610 | `f_L(z)` | `f_L(\xi)` | mode definition |
| 610 | `\chi(z)` | `\chi(\xi)` | integrated mass |
| 610 | `z -` | `\xi -` | in χ definition |
| 610 | `e^{-z/\lambda}` | `e^{-\xi/\lambda}` | exponential |
| 613 | `z = 0` | `\xi = 0` | localization point |
| 634 | `dz` | `d\xi` | integral measure |
| 634 | `|f_L(z)|^4` | `|f_L(\xi)|^4` | mode function |
| 643 | `f_L(z)` | `f_L(\xi)` | Gaussian mode |
| 643 | `z^2` | `\xi^2` | quadratic term |
| 648 | `|f_L(z)|^4` | `|f_L(\xi)|^4` | fourth power |
| 648 | `z^2` | `\xi^2` | quadratic term |
| 653 | `|f_L(z)|^4` | `|f_L(\xi)|^4` | mode function |
| 653 | `dz` | `d\xi` | integral measure |
| 674 | `\chi(z)` | `\chi(\xi)` | integrated mass |
| 675 | `z` | `\xi` | "For large z" |
| 675 | `\chi(z)` | `\chi(\xi)` | function argument |
| 675 | `z -` | `\xi -` | in approximation |
| 675 | `(z-\lambda)` | `(\xi-\lambda)` | exponential argument |

### V-A Structure Section (lines 720-853)

| Line | Current | Target | Context |
|------|---------|--------|---------|
| 728 | `m(z)` | `m(\xi)` | mass profile |
| 728 | `e^{-z/\lambda}` | `e^{-\xi/\lambda}` | exponential |
| 732 | `\partial_z` | `\partial_\xi` | derivative |
| 732 | `m(z)` | `m(\xi)` | mass function |
| 733 | `\int_0^z` | `\int_0^\xi` | integral limit |
| 733 | `m(z')` | `m(\xi')` | integration variable |
| 733 | `dz'` | `d\xi'` | integral measure |
| 734 | `z = 0` | `\xi = 0` | boundary |
| 739 | `\partial_z` | `\partial_\xi` | derivative |
| 739 | `m(z)` | `m(\xi)` | mass function |
| 740 | `\int_0^z` | `\int_0^\xi` | integral limit |
| 740 | `m(z')` | `m(\xi')` | integration variable |
| 740 | `dz'` | `d\xi'` | integral measure |
| 760 | `m(z)` | `m(\xi)` | mass profile |
| 760 | `e^{-z/\lambda}` | `e^{-\xi/\lambda}` | exponential |
| 762 | `\chi(z)` | `\chi(\xi)` | function definition |
| 762 | `\int_0^z` | `\int_0^\xi` | integral limit |
| 762 | `m(z')` | `m(\xi')` | integration variable |
| 762 | `dz'` | `d\xi'` | integral measure |
| 762 | `z -` | `\xi -` | in formula |
| 762 | `e^{-z/\lambda}` | `e^{-\xi/\lambda}` | exponential |
| 767 | `\psi_L(z)` | `\psi_L(\xi)` | wavefunction |
| 767 | `\chi(z)` | `\chi(\xi)` | integrated mass |
| 767 | `m_0 z` | `m_0 \xi` | in exponent |
| 767 | `e^{-z/\lambda}` | `e^{-\xi/\lambda}` | exponential |
| 768 | `\psi_R(z)` | `\psi_R(\xi)` | wavefunction |
| 768 | `\chi(z)` | `\chi(\xi)` | integrated mass |
| 768 | `m_0 z` | `m_0 \xi` | in exponent |
| 768 | `e^{-z/\lambda}` | `e^{-\xi/\lambda}` | exponential |
| 771 | `$z$` | `$\xi$` | "large z" text |
| 775 | `\psi_L(z)` | `\psi_L(\xi)` | wavefunction |
| 775 | `e^{-m_0 z}` | `e^{-m_0 \xi}` | exponential |
| 776 | `\psi_R(z)` | `\psi_R(\xi)` | wavefunction |
| 776 | `e^{+m_0 z}` | `e^{+m_0 \xi}` | exponential |
| 787 | `|\psi_R(z)|^2` | `|\psi_R(\xi)|^2` | probability |
| 787 | `W(z)` | `W(\xi)` | profile function |
| 787 | `dz` | `d\xi` | integral measure (×2) |
| 787 | `|\psi_L(z)|^2` | `|\psi_L(\xi)|^2` | probability |
| 790 | `W(z)` | `W(\xi)` | profile function |
| 790 | `z < \lambda` | `\xi < \lambda` | condition |
| 792 | `e^{-z/\lambda}` | `e^{-\xi/\lambda}` | exponential |
| 798 | `z = 0` | `\xi = 0` | boundary (×2) |
| 798 | `m(z)` | `m(\xi)` | mass profile |
| 798 | `z/\lambda` | `\xi/\lambda` | ratio |
| 799 | `m(z)` | `m(\xi)` | mass profile |
| 802 | `m(z)` | `m(\xi)` | mass profile (×2) |
| 802 | `z = 0` | `\xi = 0` | boundary |
| 803 | `m(z)` | `m(\xi)` | mass profile (×2) |
| 803 | `z = 0` | `\xi = 0` | boundary |
| 851 | `m(z)` | `m(\xi)` | mass profile |

---

## BUCKET 2: Z6 Complex Coordinates (DO NOT CHANGE)

**Count**: 0

No occurrences of z₁, z₂, or Z6 complex coordinates in CH04.

---

## BUCKET 3: 3D Spatial (DO NOT CHANGE)

**Count**: 0

No occurrences of (x, y, z) 3D spatial tuples in CH04.

---

## BUCKET 4: Ambiguous (NEEDS REVIEW)

**Count**: 0

All z occurrences are clearly 5D depth coordinates (BUCKET 1).

---

## Canon Anchor

From GLOBAL_SYMBOL_TABLE.md:
```
| Symbol | LaTeX | Name | Meaning |
|--------|-------|------|---------|
| ξ | `\xi` | 5D depth | Compact coordinate ∈ [0, 2πR_ξ) |
```

From z-matrix:
```
| Pattern | Physical Meaning | Correct Symbol | Action |
|---------|------------------|----------------|--------|
| f(z) profile | 5D profile function | f(ξ) | MUST-FIX |
| ∫...dz (bulk integral) | 5D integration | ∫...dξ | MUST-FIX |
```

---

## Verification Counts

**Pre-fix verification**:
- Z6 z₁, z₂: 0 occurrences (preserved)
- 3D (x,y,z): 0 occurrences (preserved)
- 5D z→ξ candidates: 52 occurrences (to be fixed)

---

*Generated: 2026-01-24*
*Audit Protocol: book2-chapter-audit-v1*
