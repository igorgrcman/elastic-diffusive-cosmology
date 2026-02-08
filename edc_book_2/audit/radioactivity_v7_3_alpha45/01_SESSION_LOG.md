# SESSION LOG (V7.3)

**Created**: 2026-01-31

---

## Session Timeline

### 2026-01-31 — V7.3 Build

**16:00** — Initiated V7.3 dataset expansion
- Read V7.2 artifacts: 10_DATA_GAPS_V7_2.md, 06_HINDRANCE_RULES.md
- Created directory: audit/radioactivity_v7_3_alpha45/
- Goal: Expand α32 → α45 with focus on H1/H2 and high-Qα

**16:05** — BL fetch round 1 (V7.2 gap candidates)
- Po-211: [BL:S2] NuDat3 — t₁/₂=0.516 s, Qα=7594.5 keV, Jπ=9/2⁺ (accessed 2026-01-31)
- Po-213: [BL:S2] NuDat3 — t₁/₂=3.706 µs, Qα=8536 keV, Jπ=9/2⁺
- Rn-218: [BL:S2] NuDat3 — t₁/₂=33.75 ms, Qα=7262.5 keV, Jπ=0⁺
- At-216: [BL:S2] NuDat3 — t₁/₂=0.30 ms, Qα=7950 keV, Jπ=1⁻

**16:10** — BL fetch round 2 (H1/H2 candidates)
- At-215: [BL:S2] NuDat3 — t₁/₂=0.10 ms, Qα=8178 keV, Jπ=9/2⁻
- At-218: [BL:S2] NuDat3 — t₁/₂=1.28 s, Qα=6874 keV, Jπ=(3⁻,2⁻)
- Bi-213: [BL:S2] NuDat3 — t₁/₂=45.59 m, Qα=5988 keV, Jπ=9/2⁻, α=2.14% (excluded: too low BR)
- Fr-219: [BL:S2] NuDat3 — t₁/₂=24 ms, Qα=7448.6 keV, Jπ=9/2⁻

**16:15** — Daughter Jπ verification
- Pb-207: [BL:S2] NuDat3 — Jπ=1/2⁻ (daughter of Po-211)
- Pb-209: [BL:S2] NuDat3 — Jπ=9/2⁺ (daughter of Po-213)
- Bi-211: [BL:S2] NuDat3 — Jπ=9/2⁻ (daughter of At-215)
- Bi-212: [BL:S2] NuDat3 — Jπ=1⁻ (daughter of At-216)

**16:20** — BL fetch round 3 (actinide expansion)
- Ac-225: [BL:S2] NuDat3 — t₁/₂=9.920 d, Qα=5935.1 keV, Jπ=(3/2⁻)
- Th-229: [BL:S2] NuDat3 — t₁/₂=7907 y, Qα=5167.6 keV, Jπ=5/2⁺
- Cm-245: [BL:S2] NuDat3 — t₁/₂=8423 y, Qα=5624.5 keV, Jπ=7/2⁺
- Cm-247: [BL:S2] NuDat3 — t₁/₂=1.56×10⁷ y, Qα=5354 keV, Jπ=9/2⁻

**16:25** — BL fetch round 4 (Cf isotopes for H1/H2)
- Cf-249: [BL:S2] NuDat3 — t₁/₂=351 y, Qα=6293.3 keV, Jπ=9/2⁻
- Cf-250: [BL:S2] NuDat3 — t₁/₂=13.08 y, Qα=6128.44 keV, Jπ=0⁺
- Cf-251: [BL:S2] NuDat3 — t₁/₂=898 y, Qα=6177.0 keV, Jπ=1/2⁺
- Rn-217: [BL:S2] NuDat3 — t₁/₂=0.54 ms, Qα=7887.2 keV, Jπ=9/2⁺

**16:30** — Hindrance classification
Classified all 45 nuclides using V7.2 rules:
- H2 found: Po-211 (ΔJ=4, ΔΠ=Y), Cf-251 (ΔJ=4, ΔΠ=Y) — 2 total
- H1 found: Cf-249 (ΔJ=1, ΔΠ=Y), plus existing U-235, Am-241, Am-243 — 4 total
- H0: remaining 39 nuclides
- Excluded Bi-213 (α-BR=2.14% too low), Es-253 (daughter Jπ uncertain)

**16:35** — d(n) computation
- Applied n(A) = 6.1 × A^(1/3) [P]
- Computed d(n) for all 45 nuclides
- Range: 0.20 (Po-209) to 2.56 (Cf-252)
- All nuclides target n* = 36 (none near 48 crossover)

**16:40** — G-N fit and regression
- Model 0: R² = 0.983
- Model 1 (+Hindrance): R² = 0.986, H1/H2 coefficients positive as expected
- Model 2 (+d(n)): g = -0.52, p = 0.07 — borderline significant
- Model 3 (+d(n)²): quadratic not significant

**16:45** — Documentation complete
- All 13 deliverable files written
- Acceptance criteria evaluated

---

## BL Fetch Summary

| Source | Queries | Success | Failures |
|--------|---------|---------|----------|
| NuDat3 (S2) | 20 | 20 | 0 |
| ENSDF (S1) | 5 | 5 | 0 |

**Total nuclides**: 45 (32 from V7.2 + 13 new)

---

## Excluded Nuclides

| Nuclide | Reason |
|---------|--------|
| Bi-213 | α-BR = 2.14% (too low; t₁/₂(α) unreliable) |
| Bk-249 | α-BR = 0.001% (essentially pure β⁻) |
| Es-253 | Daughter Jπ uncertain |

