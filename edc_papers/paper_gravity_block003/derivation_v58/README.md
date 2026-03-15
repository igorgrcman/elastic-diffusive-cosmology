# EDC BLOCK-004 Derivation v58: Layer B Λ_QCD Extraction

## Purpose

This derivation extends the Layer B adapter (v57) with a **Λ_QCD extraction module** and two-route consistency verification. All experimental anchors remain strictly quarantined with no backflow to Layer A.

## Key Features

- Layer A remains **untouched and hash-locked**
- All numerical values tagged with **[Q]** (QUARANTINED)
- Two-route Λ extraction: **Λ₁ = Λ₂** verified
- Threshold invariance: **T1 ≈ T2** verified
- Explicit **NOT A FIT** policy enforced

## Firewall Contract v2

**All operations are Layer B only.** Layer A is:
- Hash-locked (v57 hash verified)
- Read-only (no modifications permitted)
- Uncontaminated (no experimental values injected)

The extracted Λ_QCD is a **Layer B result only**. It does NOT become a Layer A prediction.

## Two-Route Λ Extraction

| Route | Method | Status |
|-------|--------|--------|
| Λ₁ | 1-loop analytic inversion | VERIFIED |
| Λ₂ | Numeric/2-loop | VERIFIED |
| Consistency | Λ₁ ≈ Λ₂ within tolerance | PASS |

## Threshold Policies

| Policy | Method | Status |
|--------|--------|--------|
| T1 | Step-function decoupling | VERIFIED |
| T2 | Matched continuity | VERIFIED |
| Invariance | T1 ≈ T2 within tolerance | PASS |

## Build Instructions

```bash
cd derivation_v58/
pdflatex main.tex
pdflatex main.tex  # for TOC
python3 recompute.py
```

## Expected Output

```
Total: 57/57 CHECKS PASSED
All checks PASS

v57 hash verified: fadd71e1e0adfa69
v58 SoT hash: 67ce04beef9f7f79

Layer A: UNCHANGED
Layer B: QUARANTINED
Two-Route Lambda: CONSISTENT
Threshold Invariance: VERIFIED
```

## Export

```bash
cp main.pdf EDC_BLOCK004_DERIVATION_V58_LAYERB_LAMBDAQCD_EXTRACTION_TWOROUTE_QUARANTINED.pdf
```

## Hash Chain

| Version | Topic | Hash |
|---------|-------|------|
| v57 | Layer B Adapter | fadd71e1e0adfa69 |
| v58 | Λ_QCD Extraction | 67ce04beef9f7f79 |

## Acceptance Criteria

See ACCEPTANCE.md for full checklist.
