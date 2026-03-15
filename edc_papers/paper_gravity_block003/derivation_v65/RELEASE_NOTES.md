# BLOCK-004 Derivation v65: Release Notes

## Proton Decay Canonical Single Document

### Version: v65
### Date: 2026-02-08
### Status: CANONICAL CLOSURE

---

## What is v65

This document is the **canonical single reference** for BLOCK-004 (Proton Decay). It consolidates derivations v61-v64 into one firewall-locked document.

### Consolidated Content

| Source | Content | Hash |
|--------|---------|------|
| v61 | Program Note: Operator catalog, selection rules | 353955cb1eacc053 |
| v62 | M_X(σ̃) derivation: Two-route geometric + EFT | 7a3d22e813e05675 |
| v63 | τ_p interface: M_X absorbed | 1eb0b781afa6bb6a |
| v64 | Coupling lane: g_X(M_X) derived, absorbed | a7f3e2d9c8b10456 |

### Key Results

**Five Canonical Boxes:**
1. BOX-1: Color matching at μ*
2. BOX-2: Strong coupling α₃(μ*) = 1/σ̃
3. BOX-3: PS breaking scale M_X = C_X μ* σ̃^½
4. BOX-4: Leptoquark coupling g_X = √(4π/σ̃)(1±ε_g)
5. BOX-5: Proton lifetime τ_p = (C_X⁴/16π²) μ*⁴ σ̃⁴ / H_p

**Scaling Law:** τ_p ∝ σ̃⁴

**Two-Route Theorems:**
- M_X: Route A (geometric) ↔ Route B (EFT)
- g_X: Route T1 (QCD RG) ↔ Route T2 (PS direct)

---

## What is OPEN

### Remaining Parameters

| Parameter | Description | Status |
|-----------|-------------|--------|
| σ̃ | Dimensionless brane tension | [P] |
| H_p^(sym) | Hadronic factor (symbolic) | [P] |

### Template Parameters

| Parameter | Range | Status |
|-----------|-------|--------|
| ε_g | ≤ 0.15 | [T] |
| b_{4C} | [-12, -8] | [T] |

### Closure Condition

Numeric predictions require:
1. σ̃ from EDC cosmology
2. H_p from lattice QCD or EDC-QCD matching

---

## Layer Architecture

- **Layer A (Hash-Locked):** All structural derivations
- **Layer B (Quarantined):** Illustrative sweeps

**No backflow:** L_B ∩ L_A = ∅

---

## Document Metrics

| Metric | Value |
|--------|-------|
| Pages | 46 |
| Equation environments | 244 |
| Labels | 509 |
| Reviewer traps | 12 |
| recompute.py checks | 132 |

---

## Release Bundle

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification (132 checks) |
| `README.md` | Overview |
| `REPORT.md` | Technical details |
| `ACCEPTANCE.md` | Acceptance criteria |
| `RELEASE_NOTES.md` | This file |
| `release/` | Export bundle |

---

## Verification

```bash
python3 recompute.py
```

All 132 checks must pass.

---

## Relation to v61-v64

- **v61:** Program Note (operator catalog)
- **v62:** M_X(σ̃) derivation
- **v63:** τ_p interface (M_X absorbed)
- **v64:** g_X(M_X) closure (coupling absorbed)
- **v65:** Canonical consolidation (this document)

The chain: v61 + v62 → v63 → v64 → v65 completes BLOCK-004.

---

**v65 SoT Hash:** `c4e7f2a1b8d30965`

**Parent Hashes:**
- v55: `1794377561879613`
- v60: `4985a938f5558447`
- v61: `353955cb1eacc053`
- v62: `7a3d22e813e05675`
- v63: `1eb0b781afa6bb6a`
- v64: `a7f3e2d9c8b10456`
