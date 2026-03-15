# Derivation v27 — Acceptance Criteria

## Required Checks (AC-P35-*)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P35-1 | Only derivation_v27/ modified/created | PASS |
| AC-P35-2 | FROZEN main.tex MD5 = e592a943... | PASS |
| AC-P35-3 | PDF builds, 0 undefined refs/cites, 0 private paths | PASS |
| AC-P35-4 | >= 16 pages | PASS (19 pages) |
| AC-P35-5 | >= 80 equation environments | PASS (85) |
| AC-P35-6 | $m_b = \lambda\sigma/M_5^3$ derived | PASS [Dc] |
| AC-P35-7 | $b = m_b L$ connection to $\bar{M}_{\mathrm{Pl}}^2 = M_5^3 L$ | PASS [Dc] |
| AC-P35-8 | Topological pinning candidate (discrete $\lambda$) | PASS [P] |
| AC-P35-9 | TikZ 2-panel figure | PASS |
| AC-P35-10 | recompute.py with b-scanning | PASS (12/12 checks) |
| AC-P35-11 | PAPERS_INDEX updated | PASS |

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
| Neumann limit | $x_1 \to \pi$ | 3.1413 | PASS |
| Dirichlet limit | $x_1 \to \pi/2$ | 1.5724 | PASS |
| Gap bounds (b=1) | $\pi/2 < x_1 < \pi$ | 2.7984 | PASS |
| Gap bounds (b=10) | $\pi/2 < x_1 < \pi$ | 1.7434 | PASS |
| Monotonicity | decreasing | verified | PASS |
| Small-b approx | $\pi - b/\pi$ | 3.1384 vs 3.1384 | PASS |
| Large-b approx | $\pi/2 + \pi/(2b)$ | 1.5867 vs 1.5865 | PASS |
| Residual b=1 | < 1e-10 | 4.4e-16 | PASS |
| Residual b=10 | < 1e-10 | 2.2e-16 | PASS |
| Discrete $\lambda$ n=1 | computed | 2.46 | PASS |
| Discrete $\lambda$ n=5 | computed | 1.65 | PASS |
| Discrete $\lambda$ n=10 | computed | 1.58 | PASS |

## Content Verification

| Section | Content | Status |
|---------|---------|--------|
| §1 | Introduction + epistemic framework | PASS |
| §2 | Dimensional analysis | PASS |
| §3 | Action-level derivation | PASS |
| §4 | Dimensionless control parameter $b$ | PASS |
| §5 | Topological pinning candidate | PASS |
| §6 | Connection to v26 spectrum | PASS |
| §7 | Numerical analysis | PASS |
| §8 | Graphical summary (TikZ) | PASS |
| §9 | Comparison with EW scale | PASS |
| §10 | Epistemic ledger | PASS |
| §11 | Conclusions | PASS |
| App A | Detailed dimensional analysis | PASS |
| App B | Action derivation details | PASS |
| App C | Numerical implementation | PASS |

## Key Derivations Verified

| Derivation | Status |
|------------|--------|
| $m_b = \lambda\sigma/M_5^3$ from dimensional analysis | [Dc] |
| $m_b = \lambda\sigma/M_5^3$ from action-level | [Dc] |
| $b = \lambda\sigma L^2/\bar{M}_{\mathrm{Pl}}^2$ | [Dc] |
| Topological pinning ($\lambda = \pi n$) | [P] |
| Connection to v26 transcendental equation | [D] |
| Limiting behaviors (Neumann/Dirichlet) | [D] |
| Small-$b$ expansion | [D] |
| Large-$b$ expansion | [D] |

## Gap Derivability Status

| Component | Tag |
|-----------|-----|
| Spectral mechanism | [D] |
| Transcendental equation | [D] |
| $m_b$ from $\sigma$ | [Dc] |
| Coefficient $\lambda$ | [OPEN] / [P] |
| Compactification scale $L$ | [OPEN] |
| **Overall gap** | [I]+[BL] |

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

---

*Acceptance recorded: 2026-02-03*
