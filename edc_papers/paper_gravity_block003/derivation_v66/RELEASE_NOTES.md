# BLOCK-004 Derivation v66: Release Notes

## Layer B τ_p(σ̃) Bounds Comparison (QUARANTINED)

### Version: v66
### Date: 2026-02-08
### Status: LAYER B ADAPTER

---

## What is v66

This document is a **QUARANTINED** Layer B adapter that compares the EDC proton lifetime prediction to published experimental bounds while maintaining strict layer separation.

### Key Innovation

**Problem:** How to compare τ_p(σ̃) to experimental bounds without contaminating Layer A?

**Solution:** Layer B adapter with quarantine protocol:
1. Import τ_p formula from Layer A (read-only)
2. Define B-API for comparison operations
3. Quarantine all experimental values
4. Enforce no-backflow theorem

### B-API Specification

| API | Function | Purpose |
|-----|----------|---------|
| B-API1 | Template instantiation | Apply envelope bounds |
| B-API2 | Interval computation | [τ_p^(min), τ_p^(max)] |
| B-API3 | Comparison ratio | R(σ̃) = τ_bound/τ_p^(min) |
| B-API4 | Feasibility extraction | σ̃_min^(req) solving R=1 |

### Key Results

**Scaling Law:**
```
τ_p ∝ σ̃^4
```

**Sensitivity:**
```
∂ln(τ_p)/∂ln(σ̃) = 4
```

**Required Minimum (symbolic):**
```
σ̃_min^(req) = [τ_bound · H_p · 16π² / C_X^4 μ*^4]^(1/4)
```

---

## What is OPEN

### Parameters from Layer A

| Parameter | Description | Status |
|-----------|-------------|--------|
| σ̃ | Dimensionless brane tension | [P] |
| H_p^(sym) | Hadronic factor (symbolic) | [P] |
| μ* | Matching scale (symbolic) | [P] |

### Quarantined Inputs

| Parameter | Value | Source |
|-----------|-------|--------|
| τ_bound | 2.4 × 10³⁴ years | Super-K 2020 |
| α_H | 0.0090 ± 0.0015 GeV³ | RBC/UKQCD 2015 |

### Closure Condition

Numeric predictions require:
1. σ̃ from EDC cosmology
2. H_p from lattice QCD or EDC-QCD matching

---

## Layer Architecture

```
Layer A (v65) ──────────────────── [HASH-LOCKED]
    │
    │ τ_p = (C_X^4/16π²) · μ*^4 · σ̃^4 / H_p
    │
    │ READ-ONLY IMPORT
    ▼
Layer B (v66) ──────────────────── [THIS DOCUMENT]
    │
    │ B-API1-4 definitions
    │ Sweep methodology
    │ Feasibility analysis
    │
    │ QUARANTINE BOUNDARY
    ▼
Quarantine (Q) ─────────────────── [ISOLATED]

    τ_bound = 2.4 × 10^34 years [Super-K]
    α_H = 0.0090 GeV³ [lattice QCD]
```

**No-Backflow:** L_B ∩ L_A = ∅ and Q ∩ L_A = ∅

---

## Document Metrics

| Metric | Value |
|--------|-------|
| Pages | 29 |
| Equation environments | 162 |
| Labels | 341 |
| recompute.py checks | 104 |

---

## Release Bundle

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification (104 checks) |
| `quarantine/` | QUARANTINED external inputs |
| `README.md` | Overview |
| `REPORT.md` | Technical details |
| `ACCEPTANCE.md` | Acceptance criteria |
| `RELEASE_NOTES.md` | This file |

---

## Verification

```bash
python3 recompute.py
```

All 104 checks must pass.

---

## Relation to Previous Versions

| Version | Content | Relation |
|---------|---------|----------|
| v65 | BLOCK-004 canonical (Layer A) | Parent |
| v64 | g_X coupling lane | Incorporated in v65 |
| v63 | τ_p interface | Incorporated in v65 |
| v62 | M_X derivation | Incorporated in v65 |
| v61 | Operator catalog | Incorporated in v65 |
| **v66** | Layer B adapter | **This document** |

---

## Hash Chain

| Version | Hash |
|---------|------|
| v55 | 1794377561879613 |
| v60 | 4985a938f5558447 |
| v65 | c4e7f2a1b8d30965 |
| **v66** | **b9d3e4f5a6c71082** |

---

**v66 SoT Hash:** `b9d3e4f5a6c71082`

**Parent Hash (v65):** `c4e7f2a1b8d30965`
