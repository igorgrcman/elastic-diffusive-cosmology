# α100 DATASET (V7.4)

**Created**: 2026-01-31
**Purpose**: Expanded dataset for improved statistical power
**Count**: 102 nuclides (45 from V7.3 + 57 new)

---

## Dataset Overview

| Metric | V7.3 | V7.4 | Target | Status |
|--------|------|------|--------|--------|
| Total nuclides | 45 | 102 | 95-110 | ✓ |
| Elements covered | 13 | 18 | — | ✓ |
| Z range | 84-98 | 83-100 | — | ✓ |

---

## Hindrance Classification Summary

| Class | V7.3 | V7.4 | Target | Status |
|-------|------|------|--------|--------|
| H0 | 39 | 82 | — | — |
| H1 | 4 | 8 | — | — |
| H2 | 2 | 12 | — | — |
| **H1+H2** | **6** | **20** | **≥12** | **✓ PASS** |

### H1 Nuclides (8 total)

| Nuclide | Jπ(P) → Jπ(D) | ΔJ | ΔΠ | Source |
|---------|---------------|----|----|--------|
| U-235 | 7/2⁻ → 5/2⁺ | 1 | Y | V7.2 |
| Am-241 | 5/2⁻ → 5/2⁺ | 0 | Y | V7.2 |
| Am-243 | 5/2⁻ → 5/2⁺ | 0 | Y | V7.2 |
| Cf-249 | 9/2⁻ → 7/2⁺ | 1 | Y | V7.3 |
| Fr-220 | 1⁺ → 1⁻ | 0 | Y | V7.4 |
| Ac-224 | 0⁻ → 1⁺ | 1 | Y | V7.4 |
| Cm-247 | 9/2⁻ → 7/2⁺ | 1 | Y | V7.4 |
| Es-255 | 7/2⁺ → 3/2⁻ | 2 | Y | V7.4 |

### H2 Nuclides (12 total)

| Nuclide | Jπ(P) → Jπ(D) | ΔJ | ΔΠ | Source |
|---------|---------------|----|----|--------|
| Po-211 | 9/2⁺ → 1/2⁻ | 4 | Y | V7.3 |
| Cf-251 | 1/2⁺ → 9/2⁻ | 4 | Y | V7.3 |
| Bi-211 | 9/2⁻ → 1/2⁺ | 4 | Y | V7.4 |
| Bi-212 | 1⁻ → 5⁺ | 4 | Y | V7.4 |
| At-212 | 1⁻ → 5⁺ | 4 | Y | V7.4 |
| Rn-213 | 9/2⁺ → 1/2⁻ | 4 | Y | V7.4 |
| Np-236 | 6⁻ → 2⁻ | 4 | N | V7.4 |
| Es-250 | 6⁺ → 2⁻ | 4 | Y | V7.4 |
| Es-252 | 5⁻ → 1⁺ | 4 | Y | V7.4 |
| Es-254 | 7⁻ → 2⁻ | 5 | N | V7.4 |
| Fm-253 | 1/2⁺ → 9/2⁻ | 4 | Y | V7.4 |
| Fm-255 | 7/2⁺ → 1/2⁺ | 3 | N | V7.4 |

---

## Even-Even / Odd-A / Odd-Odd Distribution

| Category | Definition | Count | Fraction |
|----------|------------|-------|----------|
| Even-even (EE) | Z even, A even | 42 | 41.2% |
| Odd-A (OA) | A odd | 48 | 47.1% |
| Odd-odd (OO) | Z odd, A odd | 12 | 11.8% |
| **Total** | — | **102** | 100% |

### Odd-Odd Nuclides (12 total)

| Nuclide | Z | A | Jπ(P) | H-class |
|---------|---|---|-------|---------|
| Bi-212 | 83 | 212 | 1- | H2 |
| At-210 | 85 | 210 | 5+ | H0 |
| At-212 | 85 | 212 | 1- | H2 |
| At-216 | 85 | 216 | 1- | H0 |
| At-218 | 85 | 218 | 3- | H0 |
| Fr-212 | 87 | 212 | 5+ | H0 |
| Fr-218 | 87 | 218 | 1- | H0 |
| Fr-220 | 87 | 220 | 1+ | H1 |
| Ac-224 | 89 | 224 | 0- | H1 |
| Ac-226 | 89 | 226 | 1- | H0 |
| Np-236 | 93 | 236 | 6- | H2 |
| Bk-246 | 97 | 246 | 2- | H0 |

---

## Qα Distribution

| Range | V7.3 | V7.4 | Target | Status |
|-------|------|------|--------|--------|
| < 5 MeV | 9 | 11 | — | — |
| 5-6 MeV | 17 | 32 | — | — |
| 6-7 MeV | 8 | 33 | — | — |
| 7-8 MeV | 8 | 17 | — | — |
| ≥ 8 MeV | 3 | 9 | — | — |
| **High-Qα (≥6 MeV)** | **19** | **59** | **≥18** | **✓ PASS** |

### Highest Qα Nuclides

| Nuclide | Qα (keV) | t₁/₂ |
|---------|----------|------|
| At-213 | 9254 | 125 ns |
| Rn-214 | 9208 | 0.27 µs |
| Po-212 | 8954 | 294 ns |
| Rn-215 | 8840 | 2.30 µs |
| Fr-217 | 8471 | 16.8 µs |
| Po-213 | 8536 | 3.71 µs |
| Rn-213 | 8243 | 19.5 ms |
| Rn-216 | 8200 | 45 µs |
| At-215 | 8178 | 0.10 ms |

---

## d(n) Distribution

Using n(A) = 6.1 × A^(1/3) [P]

| d(n) Range | Count | Fraction |
|------------|-------|----------|
| 0.0 - 0.5 | 17 | 16.7% |
| 0.5 - 1.0 | 30 | 29.4% |
| 1.0 - 1.5 | 17 | 16.7% |
| 1.5 - 2.0 | 14 | 13.7% |
| 2.0 - 2.5 | 14 | 13.7% |
| 2.5 - 3.0 | 10 | 9.8% |
| **Total** | **102** | 100% |

### d(n) Extremes

| Type | Nuclide | A | n(A) | d(n) |
|------|---------|---|------|------|
| Lowest d(n) | Po-206 | 206 | 36.04 | 0.04 |
| Highest d(n) | Fm-257 | 257 | 38.83 | 2.83 |

---

## Element Coverage

| Element | Z | Isotopes | Mass Range |
|---------|---|----------|------------|
| Bi | 83 | 2 | 211-212 |
| Po | 84 | 12 | 206-218 |
| At | 85 | 11 | 207-219 |
| Rn | 86 | 13 | 210-222 |
| Fr | 87 | 6 | 212-221 |
| Ra | 88 | 6 | 220-226 |
| Ac | 89 | 4 | 223-226 |
| Th | 90 | 6 | 226-232 |
| Pa | 91 | 2 | 227, 231 |
| U | 92 | 7 | 230-238 |
| Np | 93 | 2 | 236-237 |
| Pu | 94 | 6 | 236-244 |
| Am | 95 | 2 | 241, 243 |
| Cm | 96 | 8 | 242-250 |
| Bk | 97 | 3 | 245-247 |
| Cf | 98 | 4 | 249-252 |
| Es | 99 | 6 | 250-255 |
| Fm | 100 | 6 | 252-257 |

### Isotopic Families with ≥3 Members

| Family | Count | Status |
|--------|-------|--------|
| Po | 12 | ✓ |
| At | 11 | ✓ |
| Rn | 13 | ✓ |
| Fr | 6 | ✓ |
| Ra | 6 | ✓ |
| Th | 6 | ✓ |
| U | 7 | ✓ |
| Pu | 6 | ✓ |
| Cm | 8 | ✓ |
| Es | 6 | ✓ |
| Fm | 6 | ✓ |
| **Families with ≥3** | **11** | **≥5 target met** |

---

## Half-life Distribution

| Range | Count | Examples |
|-------|-------|----------|
| < 1 µs | 5 | Po-212, Rn-214, At-213 |
| 1 µs - 1 ms | 12 | Rn-215, Rn-216, Fr-217 |
| 1 ms - 1 s | 13 | Po-211, At-212, Fr-218 |
| 1 s - 1 h | 18 | Rn-219, Fr-220, Ra-222 |
| 1 h - 1 d | 16 | At-211, Rn-211, Fm-254 |
| 1 d - 1 y | 20 | Ra-224, Th-227, Cm-242 |
| 1 y - 1 ky | 8 | Th-228, Cf-251, Bk-247 |
| 1 ky - 1 My | 7 | Pa-231, Cm-245, Cm-247 |
| > 1 My | 3 | U-235, U-238, Pu-244 |
| **Total** | **102** | — |

### Long-lived (t₁/₂ ≥ 1 day)

| Count | Target | Status |
|-------|--------|--------|
| 56 | ≥25 | ✓ PASS |

---

## Data Quality Summary

| Metric | Value |
|--------|-------|
| Total nuclides | 102 |
| Full t₁/₂ coverage | 102/102 (100%) |
| Full Qα coverage | 102/102 (100%) |
| Full Jπ(P) coverage | 102/102 (100%) |
| Jπ(D) coverage | 99/102 (97%) |
| Hindrance classified | 102/102 (100%) |
| BL provenance | 102/102 (100%) |
| α-BR ≥ 5% | 100/102 (98%) |

**Notes**:
- 3 nuclides have uncertain Jπ(D): Po-217, Es-250, Es-254
- 2 nuclides have α-BR slightly below 5% but included for family coverage: Po-206 (5.45%), Cm-250 (8%)

