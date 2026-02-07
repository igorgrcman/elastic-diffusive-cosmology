# P63 / Derivation v59: Formal Λ_QCD Two-Route — Report

## Executive Summary

Derivation v59 formalizes the v58 Λ_QCD extraction by replacing all narrative with explicit formulas. Both routes (Λ₁ and Λ₂) are now fully defined with boxed equations. The Newton solver is formally specified with objective function, bracketing, and convergence criteria.

## Firewall Status

| Check | Result |
|-------|--------|
| Layer A modified | NO |
| Hash chain verified | YES |
| Forbidden patterns in non-quarantine | 0 |
| No Backflow v3 theorem | PRESENT |
| Grep verification | IMPLEMENTED |

**FIREWALL: INTACT**

## Document Statistics

| Metric | Value | Requirement | Status |
|--------|-------|-------------|--------|
| Pages | 31 | ≥26 | PASS |
| Equations | 184 | ≥180 | PASS |
| Labels | 374 | ≥240 | PASS |
| Checks | 75 | ≥70 | PASS |
| Traps | 18 | ≥10 | PASS |

## DAG: Derivation Flow

```
σ̃ (Layer A) → α₃(μ*) (Layer A) → RG (Layer B) → αₛ(M_Z) (Layer B) → Λ (Layer B) → PDG Residual (QUARANTINED)
```

## Inputs Table

### Layer A (Read-Only)

| Input | Source | Status |
|-------|--------|--------|
| α₃(μ*) = 1/σ̃ | v56 | Hash-locked |
| μ* = π/L | v51 | Hash-locked |
| σ̃ ∈ [10⁻³, 10³] | v56 | Swept, not fitted |

### Layer B (QUARANTINED)

| Input | Value | Tag |
|-------|-------|-----|
| αₛ(M_Z) | [Q] 0.1180 ± 0.0009 | QUARANTINED |
| M_Z | [Q] 91.1876 GeV | QUARANTINED |
| m_t | [Q] 172.69 GeV | QUARANTINED |
| m_b | [Q] 4.18 GeV | QUARANTINED |
| m_c | [Q] 1.27 GeV | QUARANTINED |
| Λ_MS | [Q] 213 ± 8 MeV | QUARANTINED |

## Key Results

### Route Λ₁ (1-Loop Analytic)
```
Λ₁ = μ × exp(-2π/(b₀αₛ))
```
Formula is explicit, analytic, and reproducible.

### Route Λ₂ (2-Loop Analytic)
```
Λ₂ = Λ₁ × (b₀αₛ/(2π))^(2c₁)
c₁ = b₁/(2b₀²) = 174/529 ≈ 0.329
```
Formula is explicit with power correction.

### Newton Solver
```
Objective: f(Λ) = αₛ(M_Z; Λ) - αₛ^target
Bracket: [Λ₁/10, 10×Λ₁]
Tolerance: 10⁻⁶
Fallback: Bisection
```

### Log Hygiene

| Category | Count | Requirement | Status |
|----------|-------|-------------|--------|
| USED LOGS | 7 | ≥6 | PASS |
| TEMPLATE LOGS | 6 | ≥5 (NOT USED) | PASS |

## Grep Audit Summary

- Forbidden patterns scanned: 13
- Non-quarantine violations: 0
- [Q] tags present: 50+
- Fit-related terms: Only in NO-FIT declaration

## Hash Chain

| Version | Topic | Hash |
|---------|-------|------|
| v54 | BLOCK-003 Canonical | 19c69e794c9703b7 |
| v55 | PS → QCD Structural | 1794377561879613 |
| v56 | α₃ Numerical Closure | 61869b6fddb68c16 |
| v57 | Layer B Adapter | fadd71e1e0adfa69 |
| v58 | Λ Two-Route | 67ce04beef9f7f79 |
| v59 | Formal Two-Route | b07b904c96267465 |

## Verification Results

```
Total: 75/75 CHECKS PASSED
All checks PASS

v58 hash verified: 67ce04beef9f7f79
v59 SoT hash: b07b904c96267465

Layer A: UNCHANGED
Layer B: QUARANTINED
Route Lambda_1: EXPLICIT
Route Lambda_2: EXPLICIT
Newton Solver: SPECIFIED
Log Hygiene: VERIFIED
```

## Files Delivered

| File | Description |
|------|-------------|
| main.tex | LaTeX source (31 pages) |
| main.pdf | Compiled document |
| recompute.py | Verification script (75 checks) |
| REPORT.md | This file |
| README.md | Documentation |
| ACCEPTANCE.md | Acceptance criteria |
| EDC_BLOCK004_DERIVATION_V59_LAYERB_LAMBDAQCD_FORMAL_TWOROUTE_NOHANDWAVE_QUARANTINED.pdf | Export PDF |

## Conclusion

All narrative removed. All formulas explicit. Two routes verified reproducible. Newton solver formally specified. Log hygiene verified. No Backflow v3 proven.

**Status: ACCEPTED**

Date: 2026-02-07
