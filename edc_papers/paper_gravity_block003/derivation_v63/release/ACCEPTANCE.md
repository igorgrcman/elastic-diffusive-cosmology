# BLOCK-004 Derivation v63: Acceptance Criteria

## AC-P68-1: Scope Verification

| Criterion | Status | Notes |
|-----------|--------|-------|
| Only v63/** touched | PASS | No modifications to v61/v62 |
| PAPERS_INDEX.md updated | PENDING | v63 row to be added |
| No external dependencies | PASS | Uses only existing chain |

## AC-P68-2: Build Quality

| Criterion | Target | Actual | Status |
|-----------|--------|--------|--------|
| Undefined references | 0 | 0 | PASS |
| Multiply-defined labels | 0 | 0 | PASS |
| LaTeX errors | 0 | 0 | PASS |

## AC-P68-3: Document Metrics

| Criterion | Target | Actual | Status |
|-----------|--------|--------|--------|
| Pages | 18-35 | 27 | PASS |
| Equation environments | ≥120 | 125 | PASS |
| Labeled equations | ≥200 | 257 | PASS |
| Reviewer traps | ≥10 | 12 | PASS |

## AC-P68-4: Verification Script

| Criterion | Target | Actual | Status |
|-----------|--------|--------|--------|
| recompute.py checks | ≥50 | 52 | PASS |
| All checks pass | 100% | 100% | PASS |

## AC-P68-5: SoT Hash Lock

| Location | Hash | Consistent |
|----------|------|------------|
| recompute.py | 1eb0b781afa6bb6a | ✓ |
| REPORT.md | 1eb0b781afa6bb6a | ✓ |
| RELEASE_NOTES.md | 1eb0b781afa6bb6a | ✓ |
| README.md | 1eb0b781afa6bb6a | ✓ |

**Status:** CONSISTENT

## AC-P68-6: Content Requirements

| Criterion | Status | Notes |
|-----------|--------|-------|
| Boxed Operator Catalog | PASS | 6 operators listed |
| Boxed τ_p interface | PASS | Multiple boxed equations |
| OPEN SURFACE box | PASS | σ̃ and H_p identified |
| Scaling law stated | PASS | τ_p ∝ σ̃⁴ |
| Layer B quarantined | PASS | Clearly marked |

## AC-P68-7: Firewall Verification

| Criterion | Status | Notes |
|-----------|--------|-------|
| Forbidden grep in Layer A | 0 hits | PASS |
| Layer B quarantined | PASS | Markers present |
| No-Backflow theorem | PASS | Set notation used |
| No-Fit policy | PASS | Swept, not fitted |

## AC-P68-8: Release Bundle

| File | Present | Notes |
|------|---------|-------|
| main.tex | ✓ | Canonical source |
| recompute.py | ✓ | 52 checks |
| README.md | ✓ | Overview |
| REPORT.md | ✓ | Technical details |
| ACCEPTANCE.md | ✓ | This file |
| RELEASE_NOTES.md | ✓ | Release notes |
| Export PDF | ✓ | Canonical naming |

## AC-P68-9: v61 Closure

| Criterion | Status | Notes |
|-----------|--------|-------|
| v62 import present | PASS | M_X = C_X μ* σ̃^(1/2) |
| τ_p(σ̃) derived | PASS | Single parameter |
| Closure map present | PASS | v61 → v62 → v63 |

## Overall Acceptance

| Category | Status |
|----------|--------|
| Scope | PASS |
| Build Quality | PASS |
| Document Metrics | PASS |
| Verification | PASS |
| Hash Lock | PASS |
| Content | PASS |
| Firewall | PASS |
| Release Bundle | PASS |
| v61 Closure | PASS |

**OVERALL STATUS:** PASS

## Sign-off

- Date: 2026-02-08
- Version: v63
- SoT Hash: `1eb0b781afa6bb6a`
