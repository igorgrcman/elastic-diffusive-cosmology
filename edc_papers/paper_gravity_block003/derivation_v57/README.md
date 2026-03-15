# EDC BLOCK-004 Derivation v57: Layer B Adapter

## Purpose

This derivation implements a **Layer B external-data adapter** to compare the Layer A bounded prediction for α₃(μ*) (from v56) with experimental α_s(M_Z) from PDG.

## Key Features

- Layer A remains **untouched and hash-locked**
- All experimental inputs tagged **QUARANTINED**
- Parameter sweep over σ̃ (no fitting)
- Two-route RG verification (T1 = T2)
- Explicit **NOT A FIT** policy

## Firewall Contract

**Layer B is evaluation-only.** It may:
- Read Layer A exports (hash-verified)
- Perform numerical RG running
- Compare with external experimental values
- Report residuals and bands

**Layer B may NOT:**
- Modify any Layer A source files
- Inject experimental values into Layer A equations
- Choose σ̃ or ε to force agreement
- Claim experimental values as "derived"

## B-API Definitions

| API | Function | Status |
|-----|----------|--------|
| B-API1 | (σ̃, ε) → α₃(μ*) | READ-ONLY |
| B-API2 | RG running μ* → M_Z | QUARANTINED |
| B-API3 | Threshold corrections | QUARANTINED |
| B-API4 | Residual Δ vs PDG | QUARANTINED |

## No-Fit Policy

**This is NOT a fit.** The parameter σ̃ is swept, not fitted:
- No χ² optimization
- No optimal value claimed
- No parameter extraction

## Build Instructions

```bash
cd derivation_v57/
pdflatex main.tex
pdflatex main.tex  # for TOC
python3 recompute.py
```

## Expected Output

```
Total: 51/51 CHECKS PASSED
All checks PASS

v57 SoT hash: fadd71e1e0adfa69

Layer A: UNCHANGED
Layer B: QUARANTINED
```

## Export

```bash
cp main.pdf EDC_BLOCK004_DERIVATION_V57_LAYERB_ADAPTER_ALPHA3_MZ_COMPARISON_QUARANTINED.pdf
```

## Hash Chain

| Version | Topic | Hash |
|---------|-------|------|
| v56 | α₃(μ*) Numerical Closure | 61869b6fddb68c16 |
| v57 | Layer B Adapter | fadd71e1e0adfa69 |

## Acceptance Criteria

See ACCEPTANCE.md for full checklist.
