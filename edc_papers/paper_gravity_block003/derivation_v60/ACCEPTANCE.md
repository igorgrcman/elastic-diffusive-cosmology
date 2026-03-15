# P64 / Derivation v60: BLOCK-004 Canonical Single Document — Acceptance Criteria

## AC-P64 Checklist

### Scope Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P64-1 | Scope-only: derivation_v60/ + release/ + PAPERS_INDEX.md | PASS |

### Build Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P64-2 | Build clean: 0 undefined refs, 0 multiply-defined | PASS |
| AC-P64-3 | Pages: 30–45 | PASS (36 pages) |
| AC-P64-4 | Eq env ≥ 200; Labels ≥ 300 | PASS (212 eq, 556 labels) |
| AC-P64-5 | recompute.py ≥ 90 checks; ALL PASS | PASS (98/98) |

### Content Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P64-6 | Layer A (hash-locked) section present | PASS |
| AC-P64-7 | Layer B (quarantined) section present | PASS |
| AC-P64-8 | Invariances section present | PASS |
| AC-P64-9 | Hard Policies section present | PASS |
| AC-P64-10 | Log Hygiene section present | PASS |
| AC-P64-11 | STATUS box with CLOSED/OPEN items | PASS |
| AC-P64-12 | DAG diagram present | PASS |
| AC-P64-13 | Formula catalog (comprehensive) | PASS |
| AC-P64-14 | Reviewer Traps ≥ 10 | PASS |

### Firewall Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P64-15 | No Backflow v3 theorem present | PASS |
| AC-P64-16 | No-Fit policy explicitly stated | PASS |
| AC-P64-17 | Forbidden Gate section present | PASS |
| AC-P64-18 | All external values [Q] tagged | PASS |

### Hash Chain Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P64-19 | v55-v59 hashes documented | PASS |
| AC-P64-20 | v60 SoT hash computed | PASS |

### Release Bundle Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P64-21 | release/ directory exists | PASS |
| AC-P64-22 | Bundle contains required files | PASS |

### Export Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P64-23 | Export filename exact | PASS |

---

## Verification Summary

```
Total: 98/98 CHECKS PASSED
All checks PASS

v59 hash verified: b07b904c96267465
v60 SoT hash: 4985a938f5558447
```

---

## Document Statistics

| Metric | Value | Requirement | Status |
|--------|-------|-------------|--------|
| Pages | 36 | 30-45 | PASS |
| Equations | 212 | ≥200 | PASS |
| Labels | 556 | ≥300 | PASS |
| Checks | 98 | ≥90 | PASS |
| Reviewer Traps | 10 | ≥10 | PASS |
| Sections | 20+ | ≥8 | PASS |
| Appendices | 21 | ≥5 | PASS |

---

## Files Delivered

| File | Description |
|------|-------------|
| main.tex | LaTeX source (36 pages) |
| main.pdf | Compiled document |
| recompute.py | Verification script (98 checks) |
| README.md | Documentation |
| REPORT.md | Detailed report |
| ACCEPTANCE.md | This file |
| release/ | Release bundle |
| EDC_BLOCK004_DERIVATION_V60_BLOCK004_CANONICAL_SINGLE_DOCUMENT.pdf | Export PDF |

---

## Key Results (Summary)

```
Layer A (Hash-Locked):    α₃ = 1/σ̃          [VERIFIED]
Layer B (Quarantined):    RG + Λ extraction  [VERIFIED]
No Backflow v3:           L_B ∩ L_A = ∅      [THEOREM]
No-Fit Policy:            σ̃ swept            [ENFORCED]
Hash Chain:               v55-v60 complete   [VERIFIED]
BLOCK-004 Status:         CLOSED             [CONDITIONAL]
```

---

## Acceptance Decision

**ACCEPTED** — All AC-P64 criteria satisfied.

Date: 2026-02-07
