# SESSION LOG (V7.2)

**Created**: 2026-01-31

---

## Session Timeline

### 2026-01-31 — V7.2 Build

**15:00** — Initiated V7.2 "Hindered α + Structure First" audit
- Created directory: audit/radioactivity_v7_2_hindered_alpha/
- Inherited V7.1 α17 dataset as base

**15:05** — BL fetch round 1 (expansion nuclides)
- At-211: [BL:S2] NuDat3 — t₁/₂=7.214 h, Qα=5982.4 keV, Jπ=9/2⁻, α=41.8%
- Rn-219: [BL:S2] NuDat3 — t₁/₂=3.96 s, Qα=6946.2 keV, Jπ=5/2⁺
- Ra-223: [BL:S2] NuDat3 — t₁/₂=11.43 d, Qα=5978.99 keV, Jπ=3/2⁺
- Th-230: [BL:S2] NuDat3 — t₁/₂=75584 y, Qα=4770.0 keV, Jπ=0⁺

**15:10** — BL fetch round 2
- Fr-221: [BL:S2] NuDat3 — t₁/₂=4.9 m, Qα=6457.8 keV, Jπ=5/2⁻
- Po-215: [BL:S2] NuDat3 — t₁/₂=1.781 ms, Qα=7526.3 keV, Jπ=9/2⁺
- Np-237: [BL:S2] NuDat3 — t₁/₂=2.144×10⁶ y, Qα=4958.5 keV, Jπ=5/2⁺
- Cf-252: [BL:S2] NuDat3 — t₁/₂=2.647 y, Qα=6216.95 keV, Jπ=0⁺, α=96.9%

**15:15** — BL fetch round 3
- U-233: [BL:S2] NuDat3 — t₁/₂=1.59×10⁵ y, Qα=4908.7 keV, Jπ=5/2⁺
- Am-243: [BL:S2] NuDat3 — t₁/₂=7364 y, Qα=5438.8 keV, Jπ=5/2⁻
- Pu-242: [BL:S2] NuDat3 — t₁/₂=3.73×10⁵ y, Qα=4984.2 keV, Jπ=0⁺
- Cm-248: [BL:S2] NuDat3 — t₁/₂=3.48×10⁵ y, Qα=5161.81 keV, Jπ=0⁺, α=91.6%

**15:20** — BL fetch round 4
- At-217: [BL:S2] NuDat3 — t₁/₂=32.6 ms, Qα=7201.4 keV, Jπ=9/2⁻
- Cm-246: [BL:S2] NuDat3 — t₁/₂=4706 y, Qα=5475.1 keV, Jπ=0⁺
- Pu-239: [BL:S2] NuDat3 — t₁/₂=24110 y, Qα=5244.50 keV, Jπ=1/2⁺
- Bi-207 (daughter): [BL:S2] NuDat3 — Jπ=9/2⁻

**15:25** — Dataset compilation
- Merged V7.1 α17 with new 15 nuclides
- Total: 32 nuclides (α32)
- Computed daughter Jπ for hindrance classification

**15:30** — Hindrance classification
- Defined H0/H1/H2 classes (see 06_HINDRANCE_RULES.md)
- Assigned class to each nuclide based on ΔJ and parity change
- Note: daughter Jπ lookup required for some nuclides

**15:35** — d(n) computation
- Applied n(A) = 6.1 × A^(1/3) [P]
- Computed d(n) = |n(A) - 36| for A < 326 region
- Range: 0.20 (Po-209) to 2.51 (Cf-252)

**15:40** — G-N baseline fit
- Model 0: log₁₀(t₁/₂) = a × (Z/√Qα) + b
- Result: R² = 0.985, a = 1.49, b = -48.3

**15:45** — Hierarchical regression
- Model 1: residual ~ HindranceClass → H1/H2 significant
- Model 2: residual ~ HindranceClass + d(n) → g = -0.58, p = 0.11
- Model 3: residual ~ HindranceClass + d(n) + d(n)² → quadratic not significant

**15:50** — Branchpoint scorecard update
- Expanded to 5 branchpoints (added At-211, Cf-252)
- Score: 2/5 for H-N48-01c

**15:55** — Target switching analysis
- Computed crossover A for 36↔48 and 48↔54
- No nuclides in dataset near crossover points

**16:00** — Documentation complete
- All 12 deliverable files written
- Data gaps documented

---

## BL Fetch Summary

| Source | Queries | Success | Missing |
|--------|---------|---------|---------|
| NuDat3 (S2) | 16 | 16 | 0 |
| ENSDF (S1) | 4 | 4 | 0 |

**Total nuclides**: 32 (17 from V7.1 + 15 new)

