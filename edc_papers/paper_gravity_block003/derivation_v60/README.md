# P64 / Derivation v60: BLOCK-004 Canonical Single Document

## Overview

This is the canonical consolidation document for BLOCK-004 (Strong Coupling from Planck to QCD Scale). It brings together derivations v55-v59 into a single, readable reference document.

## Document Structure

### Main Sections

1. **Executive Summary** - What BLOCK-004 establishes and does not establish
2. **Layer A (Hash-Locked)** - EDC structural prediction
3. **Layer B (Quarantined)** - External adapter with RG running
4. **Invariances** - Scheme, threshold, route equivalence
5. **Hard Policies** - No Backflow v3, No-Fit, Forbidden Gate
6. **Log Hygiene** - USED vs TEMPLATE logs
7. **Status** - BLOCK-004 closure status
8. **DAG** - Derivation dependency graph
9. **Formula Catalog** - Complete formula reference
10. **Reviewer Traps** - FAQ for reviewers

### Appendices

- Detailed derivations (1-loop, 2-loop, thresholds)
- Extended RG analysis
- Numerical tables
- Hash chain verification
- Log hygiene audit

## Key Results

### Layer A (Hash-Locked)
- Structural prediction: `α₃(μ*) = 1/σ̃ × (1 ± ε)`
- Reference scale: `μ* = π/L`
- Parameter domain: `σ̃ ∈ [10⁻³, 10³]`, `ε ≲ 0.1`

### Layer B (Quarantined)
- RG running: `μ* → M_Z` with threshold matching
- Λ extraction: Two explicit routes (Λ₁, Λ₂)
- PDG comparison: Informational only (no fitting)

### Hard Policies
- No Backflow v3: L_B ∩ L_A = ∅
- No-Fit: σ̃ swept, not fitted
- Forbidden Gate: Experimental values only in QUARANTINED

## Files

| File | Description |
|------|-------------|
| main.tex | LaTeX source (36 pages) |
| main.pdf | Compiled document |
| recompute.py | Verification script (98 checks) |
| README.md | This file |
| REPORT.md | Detailed report |
| ACCEPTANCE.md | Acceptance criteria |
| release/ | Release bundle |

## Verification

```bash
python3 recompute.py
```

Expected: 98/98 CHECKS PASSED

## Hash Chain

| Version | Topic | Hash |
|---------|-------|------|
| v55 | PS → QCD Structural | 1794377561879613 |
| v56 | α₃ Numerical Closure | 61869b6fddb68c16 |
| v57 | Layer B Adapter | fadd71e1e0adfa69 |
| v58 | Λ Two-Route | 67ce04beef9f7f79 |
| v59 | Formal Two-Route | b07b904c96267465 |
| v60 | Canonical Document | 4985a938f5558447 |

## Status

**BLOCK-004: CLOSED** (conditional on σ̃ from cosmology)

Date: 2026-02-07
