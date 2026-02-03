# Derivation v28 — Acceptance Criteria

## Required Checks (AC-P36-*)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P36-1 | Only derivation_v28/ modified/created | PASS |
| AC-P36-2 | FROZEN main.tex MD5 = e592a943... | PASS |
| AC-P36-3 | PDF builds, 0 undefined refs/cites, 0 private paths | PASS |
| AC-P36-4 | >= 18 pages | PASS (19 pages) |
| AC-P36-5 | >= 90 equation environments | PASS (100) |
| AC-P36-6 | Track A (SA) derived with boundary form + SA conditions | PASS [D] |
| AC-P36-7 | Track B (topological) with explicit action and integer n | PASS [Dc/P] |
| AC-P36-8 | Formula λ = c_λ n derived (with c_λ tagged) | PASS |
| AC-P36-9 | recompute.py: x1_of_b + limits + n-scan + tables | PASS (15/15) |
| AC-P36-10 | TikZ 2-panel figure | PASS |
| AC-P36-11 | PAPERS_INDEX updated | PASS |

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | PASS |
| No undefined references | PASS |
| No undefined citations | PASS |
| No private paths in PDF | PASS |

## Python Verification (recompute.py)

| Check | Expected | Computed | Status |
|-------|----------|----------|--------|
| Neumann limit | x_1 → π | 3.1416 | PASS |
| Dirichlet limit | x_1 → π/2 | 1.5708 | PASS |
| Gap bounds b=1 | π/2 < x_1 < π | 2.7984 | PASS |
| Gap bounds b=10 | π/2 < x_1 < π | 1.7434 | PASS |
| Monotonicity | x_1 decreases | verified | PASS |
| Small-b approx | error < 1e-6 | 4.2e-9 | PASS |
| Large-b approx | error < 1e-5 | 1.6e-6 | PASS |
| Residual b=1 | < 1e-10 | 1.1e-16 | PASS |
| Residual b=100 | < 1e-10 | 2.1e-14 | PASS |
| Discrete n=1 | computed | 1.8584 | PASS |
| Discrete n=5 | computed | 2.1767 | PASS |
| Discrete n=10 | computed | 2.9304 | PASS |
| SA continuous b | b ∈ [0,∞) | verified | PASS |
| Topological n ∈ Z+ | integer | verified | PASS |
| Discrete gap | n → m_gap | distinct | PASS |

## Content Verification

| Section | Content | Status |
|---------|---------|--------|
| §1 | Introduction + bridge equations | PASS |
| §2 | Track A: Self-adjointness | PASS |
| §3 | Track B: Topological quantization | PASS |
| §4 | Combined Track A+B | PASS |
| §5 | Detailed c_λ = 2π derivation | PASS |
| §6 | Numerical analysis | PASS |
| §7 | Graphical summary (TikZ) | PASS |
| §8 | Comparison only (isolated) | PASS |
| §9 | Epistemic ledger | PASS |
| §10 | Conclusions | PASS |
| App A | Sturm-Liouville details | PASS |
| App B | Chern-Simons details | PASS |
| App C | Axionic holonomy details | PASS |
| App D | Numerical implementation | PASS |

## Track A: Self-Adjointness Results

| Derivation | Status |
|------------|--------|
| Sturm-Liouville operator L = -d²/dξ² | [D] |
| Green's identity/boundary form | [D] |
| SA condition: [φ*ψ' - (φ')*ψ] = 0 | [D] |
| Robin BC as SA extension | [D] |
| b = m_b L as U(1) parameter | [D] |
| Physical: b ≥ 0 for positivity | [D] |
| Gap bounds: π/2L < m_gap < π/L | [D] |
| SA does NOT quantize b | -- |

## Track B: Topological Quantization Results

| Mechanism | Integer | c_λ | Status |
|-----------|---------|-----|--------|
| Chern-Simons level k | k ∈ Z | 1/(2π) | [Dc] |
| Axionic holonomy n | n ∈ Z+ | O(1) | [P] |
| Orbifold normalization | n ∈ Z+ | π | [P] |
| General form λ = c_λ n | n ∈ Z+ | {1/(2π),1,π,2π} | [Dc/P] |

## Combined Result

| Formula | Tag |
|---------|-----|
| b(n) = c_λ n β | [Dc] |
| m_gap(n) = x_1(b(n))/L | [Dc] |
| β = σL²/M̄_Pl² | [OPEN] |
| **Overall gap** | [I]+[BL] |

## Progress from v27

| v27 | v28 |
|-----|-----|
| λ ∈ R+ (continuous) | λ = c_λ n (discrete) |
| Gap freedom: ∞ | Gap freedom: integers n + c_λ |

## What Remains Open

| Quantity | Status |
|----------|--------|
| c_λ value | [OPEN] — mechanism selection needed |
| β = σL²/M̄_Pl² | [OPEN] — requires EDC geometry |
| L from internal | [OPEN] — no derivation |
| Gap | [I]+[BL] — until above closed |

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

---

*Acceptance recorded: 2026-02-03*
