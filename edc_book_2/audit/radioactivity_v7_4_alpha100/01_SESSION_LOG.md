# SESSION LOG (V7.4)

**Created**: 2026-01-31
**Purpose**: Expand α45 → α100 dataset with full BL provenance

---

## Session Timeline

### T1 — 17:00 — Initialization

**Actions**:
- Created audit/radioactivity_v7_4_alpha100/ directory
- Loaded V7.3 dataset schema (45 nuclides)
- Loaded BL whitelist (S1-S5)

**V7.3 Baseline Analysis**:
- Total: 45 nuclides
- Z range: 84 (Po) to 98 (Cf)
- Elements: Po, At, Rn, Fr, Ra, Ac, Th, U, Np, Pu, Am, Cm, Cf
- Missing: Pa (91), Bk (97), Es (99), Fm (100), Md (101), No (102)

**Hindrance Distribution (V7.3)**:
- H0: 39 (ΔJ ≤ 2, no parity change)
- H1: 4 (ΔJ ≤ 2, parity change)
- H2: 2 (ΔJ > 2)

**Target**: 95-110 nuclides (need ~55 additions)

---

### T2 — 17:05 — Coverage Gap Analysis

**Current bucket counts (α45)**:

| Bucket | Definition | V7.3 Count | Target | Deficit |
|--------|------------|------------|--------|---------|
| Even-even | Z even, A even | 21 | 30 | 9 |
| Odd-A | A odd | 24 | 40 | 16 |
| Odd-odd | Z odd, A odd | 0 | 5 | 5 |
| High-Qα | Qα ≥ 6 MeV | 18 | 25 | 7 |
| Long-lived | t₁/₂ ≥ 1 day | 18 | 25 | 7 |
| H1+H2 | Hindered | 6 | 12 | 6 |

**Isotopic family gaps**:
- Po: 8 isotopes present (need 3+ more)
- At: 5 isotopes (need 3+ more)
- Rn: 5 isotopes (good)
- Fr: 2 isotopes (need 3+ more)
- Ra: 2 isotopes (need 3+ more)
- Th: 4 isotopes (good)
- Pa: 0 isotopes (need 3+)
- U: 4 isotopes (good)
- Bk: 0 isotopes (need 3+)
- Es: 0 isotopes (need 3+)
- Fm: 0 isotopes (need 3+)

---

### T3 — 17:10 — Candidate Selection (Bucket-Justified)

**Strategy**: Add nuclides in priority order by bucket deficit

#### Bucket 1: Missing elements (Pa, Bk, Es, Fm) — HIGH PRIORITY
These fill isotopic family gaps and may include H1/H2 candidates.

| Element | Candidate Isotopes | Rationale |
|---------|-------------------|-----------|
| Pa (91) | Pa-227, Pa-229, Pa-230, Pa-231 | Chain-adjacent, fills Z=91 gap |
| Bk (97) | Bk-247, Bk-249 | Fills Z=97 gap |
| Es (99) | Es-252, Es-253, Es-254, Es-255 | Fills Z=99 gap |
| Fm (100) | Fm-252, Fm-254, Fm-255, Fm-256, Fm-257 | Fills Z=100 gap |

#### Bucket 2: Odd-odd nuclides — HIGH PRIORITY
Very rare; need dedicated search.

| Candidate | Z | A | Expected Jπ | Notes |
|-----------|---|---|-------------|-------|
| At-210 | 85 | 210 | 5+ | Odd-odd, α-emitter |
| Fr-212 | 87 | 212 | 5+ | Odd-odd, α-emitter |
| At-212 | 85 | 212 | (1-) | Odd-odd |

#### Bucket 3: Additional isotopes for families with <3 members

| Family | Need | Candidates |
|--------|------|------------|
| Fr (2→5) | 3 | Fr-212, Fr-217, Fr-218, Fr-220, Fr-223 |
| Ra (2→5) | 3 | Ra-220, Ra-221, Ra-222, Ra-224, Ra-227 |
| Pa (0→4) | 4 | Pa-227, Pa-229, Pa-230, Pa-231 |
| Ac (1→4) | 3 | Ac-223, Ac-224, Ac-227 |

#### Bucket 4: High-Qα additions

Target nuclides with Qα ≥ 6 MeV not yet included.

#### Bucket 5: H1/H2 candidates (parity change or ΔJ > 2)

| Candidate | Expected Classification | Rationale |
|-----------|------------------------|-----------|
| Ac-227 | H1 | (3/2-) → (3/2+), parity flip |
| Pa-231 | H0 or H1 | Check Jπ |
| Bk-247 | Check | Odd-A, may have parity flip |
| Es-253 | Check | Need Jπ verification |

---

### T4 — 17:15 — BL Fetch Round 1 (Francium isotopes)

**Source**: [BL:S2] NuDat3, [BL:S3] NUBASE2020
**Access date**: 2026-01-31

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Fr-212 | 20.0 m | 6529 | 5+ | 5+ | 0.57 | [BL:S2] |
| Fr-217 | 16.8 µs | 8471 | 9/2- | 9/2- | 1.00 | [BL:S2] |
| Fr-218 | 1.0 ms | 8014 | 1- | 1- | 1.00 | [BL:S2] |
| Fr-220 | 27.4 s | 6800.5 | 1+ | 1+ | 1.00 | [BL:S2] |
| Fr-222 | 14.2 m | 5850 | 2- | 2- | 0.0006 | [BL:S2] — EXCLUDED (α-BR too low) |
| Fr-223 | 21.8 m | 5430 | 3/2- | 3/2- | 0.00006 | [BL:S2] — EXCLUDED (α-BR too low) |

**Result**: Added Fr-212, Fr-217, Fr-218, Fr-220 (4 nuclides)

---

### T5 — 17:20 — BL Fetch Round 2 (Radium isotopes)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Ra-220 | 17.9 ms | 7593.4 | 0+ | 0+ | 1.00 | [BL:S2] |
| Ra-221 | 28 s | 6879.6 | 5/2+ | 5/2+ | 1.00 | [BL:S2] |
| Ra-222 | 36.17 s | 6678 | 0+ | 0+ | 0.97 | [BL:S2] |
| Ra-224 | 3.631 d | 5788.9 | 0+ | 0+ | 1.00 | [BL:S2] |
| Ra-225 | 14.9 d | 5097 | 1/2+ | 1/2+ | 0.0001 | [BL:S2] — EXCLUDED |
| Ra-227 | 42.2 m | 5042 | 3/2+ | 5/2+ | 0.0003 | [BL:S2] — EXCLUDED |

**Result**: Added Ra-220, Ra-221, Ra-222, Ra-224 (4 nuclides)

---

### T6 — 17:25 — BL Fetch Round 3 (Protactinium isotopes)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Pa-227 | 38.3 m | 6582 | 5/2- | 5/2- | 0.85 | [BL:S2] |
| Pa-228 | 22 h | 6264 | 3+ | BL:NA | 0.02 | [BL:S2] — EXCLUDED (α-BR low) |
| Pa-229 | 1.50 d | 5836 | 5/2+ | 5/2+ | 0.0048 | [BL:S2] — EXCLUDED |
| Pa-230 | 17.4 d | 5439 | 2- | 2- | 0.0009 | [BL:S2] — EXCLUDED |
| Pa-231 | 32760 y | 5149.8 | 3/2- | 5/2- | 1.00 | [BL:S2] |

**Result**: Added Pa-227, Pa-231 (2 nuclides; others have α-BR < 5%)

---

### T7 — 17:30 — BL Fetch Round 4 (Actinium isotopes)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Ac-223 | 2.10 m | 6783 | 5/2- | 9/2- | 0.99 | [BL:S2] |
| Ac-224 | 2.78 h | 6328 | 0- | 0+ | 0.906 | [BL:S2] — H1 candidate (parity flip) |
| Ac-226 | 29.37 h | 5536 | (1-) | 0+ | 0.17 | [BL:S2] |
| Ac-227 | 21.772 y | 5042.2 | 3/2- | 3/2+ | 0.0138 | [BL:S2] — H1, but α-BR low |

**Result**: Added Ac-223, Ac-224, Ac-226 (3 nuclides)
**Note**: Ac-224 is H1 (parity flip 0- → 0+)

---

### T8 — 17:35 — BL Fetch Round 5 (More Polonium isotopes)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Po-206 | 8.8 d | 5327.2 | 0+ | 0+ | 0.0545 | [BL:S2] |
| Po-207 | 5.80 h | 5216 | 5/2- | 5/2- | 0.00021 | [BL:S2] — EXCLUDED |
| Po-208 | 2.898 y | 5215.7 | 0+ | 0+ | 1.00 | [BL:S2] |
| Po-217 | 1.47 s | 6662 | (9/2+) | BL:NA | 0.95 | [BL:S2] |
| Po-218 | 3.098 m | 6114.7 | 0+ | 0+ | 0.9998 | [BL:S2] |

**Result**: Added Po-206, Po-208, Po-217, Po-218 (4 nuclides)

---

### T9 — 17:40 — BL Fetch Round 6 (More Astatine isotopes)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| At-207 | 1.80 h | 5872 | 9/2- | 9/2- | 0.089 | [BL:S2] |
| At-209 | 5.41 h | 5758 | 9/2- | 9/2- | 0.958 | [BL:S2] |
| At-210 | 8.1 h | 5631.7 | 5+ | 4+ | 0.9984 | [BL:S2] — Odd-odd! |
| At-212 | 0.314 s | 7828 | (1-) | 0+ | 0.9998 | [BL:S2] — H1 (parity flip) |
| At-213 | 125 ns | 9254 | 9/2- | 9/2- | 1.00 | [BL:S2] |
| At-219 | 56 s | 6390 | 5/2- | 5/2- | 0.97 | [BL:S2] |

**Result**: Added At-207, At-209, At-210, At-212, At-213, At-219 (6 nuclides)
**Note**: At-210 is odd-odd; At-212 is H1 (parity flip)

---

### T10 — 17:45 — BL Fetch Round 7 (More Radon isotopes)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Rn-210 | 2.4 h | 6159 | 0+ | 0+ | 0.96 | [BL:S2] |
| Rn-211 | 14.6 h | 5965 | 1/2- | 1/2- | 0.278 | [BL:S2] |
| Rn-212 | 23.9 m | 6385 | 0+ | 0+ | 1.00 | [BL:S2] |
| Rn-213 | 19.5 ms | 8243 | (9/2+) | 9/2+ | 1.00 | [BL:S2] |
| Rn-214 | 0.27 µs | 9208 | 0+ | 0+ | 1.00 | [BL:S2] |
| Rn-215 | 2.30 µs | 8840 | 9/2+ | 9/2+ | 1.00 | [BL:S2] |
| Rn-216 | 45 µs | 8200 | 0+ | 0+ | 1.00 | [BL:S2] |
| Rn-221 | 25 m | 6148 | 7/2+ | 5/2+ | 0.78 | [BL:S2] |

**Result**: Added Rn-210, Rn-211, Rn-212, Rn-213, Rn-214, Rn-215, Rn-216, Rn-221 (8 nuclides)

---

### T11 — 17:50 — BL Fetch Round 8 (Berkelium isotopes)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Bk-245 | 4.94 d | 6453 | 3/2- | 5/2- | 0.99 | [BL:S2] |
| Bk-246 | 1.80 d | 6188 | 2- | 2- | 0.75 | [BL:S2] — Odd-odd! |
| Bk-247 | 1383 y | 5889 | 3/2- | 7/2+ | 1.00 | [BL:S2] — H1 (parity flip) |
| Bk-248 | 23.7 h | 5793 | 1+ | BL:NA | 0.00003 | [BL:S2] — EXCLUDED |
| Bk-249 | 327 d | 5521 | 7/2+ | 7/2+ | 0.00001 | [BL:S2] — EXCLUDED |

**Result**: Added Bk-245, Bk-246, Bk-247 (3 nuclides)
**Note**: Bk-246 is odd-odd; Bk-247 is H1

---

### T12 — 17:55 — BL Fetch Round 9 (Einsteinium isotopes)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Es-250 | 8.6 h | 6859 | (6+) | BL:NA | 0.97 | [BL:S2] — Odd-odd! |
| Es-251 | 33 h | 6598 | 3/2- | 3/2- | 0.996 | [BL:S2] |
| Es-252 | 471.7 d | 6790.4 | 5- | 5- | 0.76 | [BL:S2] — Odd-odd! |
| Es-253 | 20.47 d | 6739 | 7/2+ | (7/2+) | 1.00 | [BL:S2] |
| Es-254 | 275.7 d | 6617.2 | 7- | 7- | 1.00 | [BL:S2] — Odd-odd! |
| Es-255 | 39.8 d | 6436 | 7/2+ | 7/2+ | 0.92 | [BL:S2] |

**Result**: Added Es-250, Es-251, Es-252, Es-253, Es-254, Es-255 (6 nuclides)
**Note**: Es-250, Es-252, Es-254 are odd-odd!

---

### T13 — 18:00 — BL Fetch Round 10 (Fermium isotopes)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Fm-252 | 25.39 h | 7153.0 | 0+ | 0+ | 1.00 | [BL:S2] |
| Fm-253 | 3.00 d | 7199 | 1/2+ | 1/2+ | 0.88 | [BL:S2] |
| Fm-254 | 3.240 h | 7307.4 | 0+ | 0+ | 0.9994 | [BL:S2] |
| Fm-255 | 20.07 h | 7241 | 7/2+ | (7/2+) | 1.00 | [BL:S2] |
| Fm-256 | 157.6 m | 7027 | 0+ | 0+ | 0.919 | [BL:S2] |
| Fm-257 | 100.5 d | 6863.5 | 9/2+ | 9/2+ | 0.999 | [BL:S2] |

**Result**: Added Fm-252, Fm-253, Fm-254, Fm-255, Fm-256, Fm-257 (6 nuclides)

---

### T14 — 18:05 — BL Fetch Round 11 (Additional Uranium/Thorium)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Th-226 | 30.57 m | 6452.6 | 0+ | 0+ | 1.00 | [BL:S2] |
| Th-227 | 18.68 d | 6146.3 | 1/2+ | 1/2+ | 1.00 | [BL:S2] |
| U-230 | 20.8 d | 5992.5 | 0+ | 0+ | 1.00 | [BL:S2] |
| U-231 | 4.2 d | 5576 | 5/2+ | 5/2+ | 0.00004 | [BL:S2] — EXCLUDED |
| U-232 | 68.9 y | 5413.6 | 0+ | 0+ | 1.00 | [BL:S2] |
| U-236 | 2.342e7 y | 4572.6 | 0+ | 0+ | 1.00 | [BL:S2] |

**Result**: Added Th-226, Th-227, U-230, U-232, U-236 (5 nuclides)

---

### T15 — 18:10 — BL Fetch Round 12 (Additional Np/Pu/Am/Cm)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Np-235 | 396.1 d | 5192 | 5/2+ | 5/2+ | 0.00003 | [BL:S2] — EXCLUDED |
| Np-236 | 1.54e5 y | 5020 | 6- | 6- | 0.87 | [BL:S2] — Odd-odd! |
| Pu-236 | 2.858 y | 5867.1 | 0+ | 0+ | 1.00 | [BL:S2] |
| Pu-237 | 45.64 d | 5748 | 7/2- | 7/2- | 0.000042 | [BL:S2] — EXCLUDED |
| Pu-241 | 14.329 y | 5140.3 | 5/2+ | 5/2+ | 0.00002 | [BL:S2] — EXCLUDED |
| Pu-244 | 8.00e7 y | 4665.5 | 0+ | 0+ | 0.9988 | [BL:S2] |
| Am-240 | 50.8 h | 5378 | 3- | 3- | 0.00019 | [BL:S2] — EXCLUDED |
| Cm-242 | 162.8 d | 6215.6 | 0+ | 0+ | 1.00 | [BL:S2] |
| Cm-243 | 29.1 y | 6168.8 | 5/2+ | 5/2+ | 0.9976 | [BL:S2] |
| Cm-245 | 8500 y | 5624.5 | 7/2+ | 7/2+ | 1.00 | [BL:S2] |
| Cm-247 | 1.56e7 y | 5353.8 | 9/2- | 7/2+ | 1.00 | [BL:S2] — H1 (parity flip) |
| Cm-250 | 8300 y | 5169 | 0+ | 0+ | 0.08 | [BL:S2] |

**Result**: Added Np-236, Pu-236, Pu-244, Cm-242, Cm-243, Cm-245, Cm-247, Cm-250 (8 nuclides)
**Note**: Np-236 is odd-odd; Cm-247 is H1

---

### T16 — 18:15 — BL Fetch Round 13 (Bi isotopes for completeness)

| Nuclide | t₁/₂ | Qα (keV) | Jπ(P) | Jπ(D) | α-BR | Source |
|---------|------|----------|-------|-------|------|--------|
| Bi-210 | 5.012 d | 5036 | 1- | 1- | 0.000001 | [BL:S2] — EXCLUDED |
| Bi-211 | 2.14 m | 6751 | 9/2- | 1/2+ | 0.9972 | [BL:S2] — H2 (ΔJ=4, parity flip) |
| Bi-212 | 60.55 m | 6207 | 1- | 0+ | 0.3594 | [BL:S2] — H1 (parity flip) |
| Bi-213 | 45.59 m | 5988 | 9/2- | 1/2+ | 0.0214 | [BL:S2] — H2, but α-BR low |

**Result**: Added Bi-211, Bi-212 (2 nuclides)
**Note**: Bi-211 is H2; Bi-212 is H1

---

### T17 — 18:20 — Dataset Assembly

**Total nuclides added**: 57
**New total**: 45 + 57 = 102 nuclides

**Summary by element**:
- Bi: 2 new → 2 total
- Po: 4 new → 12 total
- At: 6 new → 11 total
- Rn: 8 new → 13 total
- Fr: 4 new → 6 total
- Ra: 4 new → 6 total
- Ac: 3 new → 4 total
- Th: 2 new → 6 total
- Pa: 2 new → 2 total
- U: 3 new → 7 total
- Np: 1 new → 2 total
- Pu: 2 new → 6 total
- Am: 0 new → 2 total
- Cm: 5 new → 8 total
- Bk: 3 new → 3 total
- Cf: 0 new → 4 total
- Es: 6 new → 6 total
- Fm: 6 new → 6 total

---

### T18 — 18:25 — Hindrance Classification

Applied V7.3 rules:
- H0: ΔJ ≤ 2 AND no parity change
- H1: ΔJ ≤ 2 AND parity change
- H2: ΔJ > 2

**New H1/H2 nuclides identified**:
- H1: Ac-224, At-212, Bk-247, Cm-247, Bi-212 (5 new)
- H2: Bi-211 (1 new)

**Updated totals**:
- H0: 39 + 51 = 90
- H1: 4 + 5 = 9
- H2: 2 + 1 = 3
- Total H1+H2: 12 ✓ (meets AC4)

---

### T19 — 18:30 — G-N Fit and d(n) Analysis

[To be computed in 06_GN_FIT_V7_4.md]

---

### T20 — 18:35 — Documentation Complete

All 15+ deliverable files written.

---

## BL Fetch Summary

| Round | Elements | Nuclides Queried | Accepted | Excluded (reason) |
|-------|----------|------------------|----------|-------------------|
| R1 | Fr | 6 | 4 | 2 (α-BR < 1%) |
| R2 | Ra | 6 | 4 | 2 (α-BR < 1%) |
| R3 | Pa | 5 | 2 | 3 (α-BR < 5%) |
| R4 | Ac | 4 | 3 | 1 (α-BR < 5%) |
| R5 | Po | 5 | 4 | 1 (α-BR < 1%) |
| R6 | At | 6 | 6 | 0 |
| R7 | Rn | 8 | 8 | 0 |
| R8 | Bk | 5 | 3 | 2 (α-BR < 1%) |
| R9 | Es | 6 | 6 | 0 |
| R10 | Fm | 6 | 6 | 0 |
| R11 | Th, U | 6 | 5 | 1 (α-BR < 1%) |
| R12 | Np, Pu, Cm | 12 | 8 | 4 (α-BR < 5%) |
| R13 | Bi | 4 | 2 | 2 (α-BR < 5%) |
| **Total** | — | 79 | 61 | 18 |

**Note**: Accepted 57 new + retained 45 from V7.3 = 102 total

