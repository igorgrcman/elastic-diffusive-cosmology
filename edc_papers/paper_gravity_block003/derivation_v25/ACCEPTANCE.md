# Derivation v25 — Acceptance Criteria

## Required Checks (AC-P33-*)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P33-1 | Only derivation_v25/ modified/created | ✅ PASS |
| AC-P33-2 | FROZEN main.tex MD5 = e592a943... | ✅ PASS |
| AC-P33-3 | PDF builds, 0 undefined refs/cites, 0 private paths | ✅ PASS |
| AC-P33-4 | ≥ 12 pages | ✅ PASS (17 pages) |
| AC-P33-5 | ≥ 60 equation environments | ✅ PASS (79) |
| AC-P33-6 | Proxy table includes Z/W/v with R_xi & M5 (both conventions) | ✅ PASS |
| AC-P33-7 | Robustness metric computed (Δlog10 & factor) | ✅ PASS |
| AC-P33-8 | TikZ figure 2 panels | ✅ PASS |
| AC-P33-9 | recompute.py matches main.tex numbers | ✅ PASS |
| AC-P33-10 | PAPERS_INDEX updated | ✅ PASS |

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | ✅ |
| No undefined references | ✅ |
| No undefined citations | ✅ |
| No private paths in PDF | ✅ |

## Python Verification (recompute.py)

| Check | Expected | Computed | Status |
|-------|----------|----------|--------|
| R_ξ(M_Z) | 6.80e-18 m | 6.798e-18 m | ✅ PASS |
| M_5^red(M_Z) | 5.56e12 GeV | 5.562e12 GeV | ✅ PASS |
| M_5^orig(M_Z) | 1.63e13 GeV | 1.629e13 GeV | ✅ PASS |
| R_ξ(M_W) | 7.71e-18 m | 7.713e-18 m | ✅ PASS |
| M_5^red(M_W) | 5.33e12 GeV | 5.333e12 GeV | ✅ PASS |
| R_ξ(v_EW) | 2.52e-18 m | 2.518e-18 m | ✅ PASS |
| M_5^red(v_EW) | 7.74e12 GeV | 7.746e12 GeV | ✅ PASS |
| Δlog₁₀(M_5) for M_W | -0.018 | -0.0183 | ✅ PASS |
| Δlog₁₀(M_5) for v_EW | +0.143 | +0.1438 | ✅ PASS |
| Total spread | 0.161 | 0.1621 | ✅ PASS |
| Factor spread | 1.45 | 1.452 | ✅ PASS |
| (8π)^{1/3} | 2.929 | 2.9292 | ✅ PASS |

## Content Verification

| Section | Content | Status |
|---------|---------|--------|
| §1 | Introduction + epistemic status | ✅ |
| §2 | Derivation chain recap (self-contained) | ✅ |
| §3 | Proxy family definition | ✅ |
| §4 | Propagation through derivation chain | ✅ |
| §5 | Numerical results | ✅ |
| §6 | Robustness analysis | ✅ |
| §7 | Graphical summary (TikZ 2-panel) | ✅ |
| §8 | Metrological justification for M_Z | ✅ |
| §9 | Error propagation | ✅ |
| §10 | Conclusions + epistemic ledger | ✅ |
| App A | Derivation identities | ✅ |
| App B | Numerical constants | ✅ |
| App C | Python script reference | ✅ |

## Robustness Results Verified

| Metric | Value |
|--------|-------|
| M_5 range (reduced) | [5.33, 7.75] × 10¹² GeV |
| M_5 range (original) | [1.56, 2.27] × 10¹³ GeV |
| Total spread Δlog₁₀ | 0.162 |
| Factor spread | 1.45 |
| All proxies GUT scale | ✅ |

## Final Status

**✅ ALL ACCEPTANCE CRITERIA MET**

---

*Acceptance recorded: 2026-02-03*
