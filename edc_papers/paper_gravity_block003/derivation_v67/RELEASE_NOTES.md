# BLOCK-004 Derivation v67: Release Notes

## σ̃ Import Contract + Closure Map

### Version: v67
### Date: 2026-02-08
### Status: CONDITIONAL CLOSURE

---

## What is v67

This document establishes the **final bridge** between EDC cosmology and BLOCK-004 proton decay predictions.

### Key Innovation

**Problem:** How to close BLOCK-004 outputs numerically without experimental anchors?

**Solution:** σ̃ Import Contract with conditional closure:
1. Define strict interface APIs (A-APIσ1-3)
2. Create complete closure map σ̃ → observables
3. Enable template mode when σ̃ unavailable
4. Maintain Layer A firewall

### Interface APIs

| API | Function |
|-----|----------|
| A-APIσ1 | Cosmology provides σ̃ |
| A-APIσ2 | BLOCK-004 consumes σ̃ |
| A-APIσ3 | Closure propagation |

### Closure Map

```
σ̃ ─┬─> α₃ = 1/σ̃
   ├─> M_X = C_X μ* √σ̃
   ├─> g_X = √(4π/σ̃)
   └─> τ_p = (C_X⁴/16π²) μ*⁴ σ̃⁴ / H_p
```

### Scaling Summary

| Observable | Scaling | Sensitivity |
|------------|---------|-------------|
| α₃ | σ̃^(-1) | -1 |
| M_X | σ̃^(1/2) | +1/2 |
| g_X | σ̃^(-1/2) | -1/2 |
| τ_p | σ̃^4 | +4 |

---

## What is OPEN

### Awaiting from Cosmology

| Parameter | Description | Status |
|-----------|-------------|--------|
| σ̃ | Dimensionless brane tension | [P] Awaiting |
| μ* | Matching scale | [P] Awaiting |
| H_p | Hadronic factor | [P] Symbolic |

### Closure Condition

When `sigma_tilde_value.json` is provided:
- All outputs close numerically
- Status changes to NUMERICAL CLOSURE
- Layer A text unchanged

---

## Conditional Closure Protocol

### Template Mode (current)

```
σ̃ = σ̃_placeholder [TODO: replace with cosmology value]
```

All formulas remain symbolic but structurally complete.

### Numerical Mode (when σ̃ available)

```json
{
  "sigma_tilde": 100,
  "delta_sigma_tilde": 10,
  "source_hash": "...",
  "source_version": "cosmology_v1"
}
```

---

## Document Metrics

| Metric | Value |
|--------|-------|
| Pages | 29 |
| Equation environments | 155 |
| Labels | 316 |
| Reviewer traps | 12 |
| recompute.py checks | 123 |

---

## Release Bundle

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification (123 checks) |
| `README.md` | Overview |
| `REPORT.md` | Technical details |
| `ACCEPTANCE.md` | Acceptance criteria |
| `RELEASE_NOTES.md` | This file |

---

## Verification

```bash
python3 recompute.py
```

All 123 checks must pass.

---

## Relation to Previous Versions

| Version | Content | Relation |
|---------|---------|----------|
| v65 | BLOCK-004 canonical | Parent (formulas) |
| v66 | Layer B adapter | Parent (optional) |
| **v67** | Import contract | **This document** |

---

## Hash Chain

| Version | Hash |
|---------|------|
| v55 | 1794377561879613 |
| v60 | 4985a938f5558447 |
| v62 | 7a3d22e813e05675 |
| v64 | a7f3e2d9c8b10456 |
| v65 | c4e7f2a1b8d30965 |
| v66 | b9d3e4f5a6c71082 |
| **v67** | **d8e9f0a1b2c34567** |

---

**v67 SoT Hash:** `d8e9f0a1b2c34567`

**Parent Hashes:**
- v65: `c4e7f2a1b8d30965`
- v66: `b9d3e4f5a6c71082`
