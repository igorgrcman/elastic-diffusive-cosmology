# BLOCK-003 Release Notes — v54 FINAL

## Summary

This release bundle contains the canonical single document for **EDC BLOCK-003**, consolidating the complete derivation chain v45→v54 into a readable, verified reference.

## Canonical Hash

```
v54 tables hash: 19c69e794c9703b7 [VERIFIED]
```

This hash is embedded in the PDF and can be verified by running `python3 recompute.py`.

## What is CLOSED

1. **Track Selection**: Pati-Salam uniquely selected via PASS > CONDITIONAL scoring
2. **Structural Predictions**:
   - sin²θ_W(μ_*) = 5/12
   - G_F = (√2 ζ(2)/48)(g_5²/μ_*² L)
   - c_R + c_{B-L} = 7/5
3. **Invariance Suite**: Scheme, unit, log hygiene, regulator — all verified
4. **Layer Separation**: Layer A (canonical, hash-locked) / Layer B (quarantined, no backflow)

## What is OUT OF SCOPE

- α_3 structure (Strong Sector) → BLOCK-004
- Proton decay rate → BLOCK-004
- Neutrino masses → BLOCK-005
- Dark matter coupling → Future work

## Forbidden Anchors Gate

**No forbidden anchors in Layer A** (grep = 0 hits):
- M_Z, M_W, v_EW, α_EM, G_N, ℓ_P — NOT USED

**Layer B quarantined**: Cannot modify Layer A. Hash firewall enforced.

## Bundle Contents

| File | SHA-256 | Role |
|------|---------|------|
| BLOCK003_CANONICAL_SINGLE_DOCUMENT.pdf | (updated)... | Export PDF (30 pages) |
| main.tex | (updated)... | LaTeX source |
| recompute.py | (updated)... | Verification script (88 checks) |
| REPORT.md | f380305a... | Detailed report |
| ACCEPTANCE.md | 20de5256... | Acceptance criteria |
| README.md | 331112cf... | Documentation |
| RELEASE_NOTES.md | — | This file |

## Verification

```bash
cd release/
python3 recompute.py
# Expected: 88/88 CHECKS PASSED
# v54 hash: 19c69e794c9703b7
```

## Hash Chain

```
v45: a80b3886903152d3 [VERIFIED]
v46: 2742edea37e863ac [VERIFIED]
v47: 7a9682f333d5349e [VERIFIED]
v48: c4f114aa0c662b66 [VERIFIED]
v49: 81010ef2faedcefd [VERIFIED]
v50: cebf3e5baf0de863 [VERIFIED]
v51: ed8fa089897b2d8c [VERIFIED]
v52: ed92d9bc43b8d26b [VERIFIED]
v53: 89a4854b0bdfd332 [VERIFIED]
v54: 19c69e794c9703b7 [VERIFIED]
```

## Build Reproducibility

- **TeX Engine**: pdflatex (TeX Live 2025)
- **Key packages**: amsmath, amssymb, tcolorbox, hyperref, cleveref
- **Build command**: `pdflatex -interaction=nonstopmode main.tex` (2 passes)

## Date

2026-02-07

## Status

**BLOCK-003 CLOSED** — All acceptance criteria satisfied.
