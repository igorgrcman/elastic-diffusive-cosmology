# EDC BLOCK-004 Derivation v59: Formal Λ_QCD Two-Route Extraction

## Purpose

This derivation provides a **fully formal** Λ_QCD extraction engine with two explicitly defined routes:
- **Route Λ₁**: 1-loop analytic inversion (explicit formula)
- **Route Λ₂**: 2-loop analytic with power correction (explicit formula)

All formulas are explicit, all algorithms are specified, and all numerical evaluations are reproducible. No narrative explanations, no informal approximations, no injected numbers.

## Key Features

- **No Handwave**: All formulas explicit and boxed
- **No Narrative**: Removed all "wait/issue" language from v58
- **Route Λ₁**: `Λ = μ × exp(-2π/(b₀αₛ))`
- **Route Λ₂**: `Λ = Λ₁ × (b₀αₛ/(2π))^(2c₁)`
- **Newton Solver**: Formal specification with objective, bracket, convergence
- **USED LOGS vs TEMPLATE LOGS**: Full audit with equation references
- **No Backflow v3**: Theorem with grep verification

## Firewall Contract v3

**All operations are Layer B only.** Layer A is:
- Hash-locked (v58 hash verified)
- Read-only (no modifications permitted)
- Uncontaminated (no experimental values injected)

## Build Instructions

```bash
cd derivation_v59/
pdflatex main.tex
pdflatex main.tex  # for TOC/refs
python3 recompute.py
```

## Expected Output

```
Total: 75/75 CHECKS PASSED
All checks PASS

v58 hash verified: 67ce04beef9f7f79
v59 SoT hash: b07b904c96267465

Layer A: UNCHANGED
Layer B: QUARANTINED
Route Lambda_1: EXPLICIT
Route Lambda_2: EXPLICIT
Newton Solver: SPECIFIED
Log Hygiene: VERIFIED
```

## Export

```bash
cp main.pdf EDC_BLOCK004_DERIVATION_V59_LAYERB_LAMBDAQCD_FORMAL_TWOROUTE_NOHANDWAVE_QUARANTINED.pdf
```

## Hash Chain

| Version | Topic | Hash |
|---------|-------|------|
| v58 | Λ Two-Route | 67ce04beef9f7f79 |
| v59 | Formal Two-Route | b07b904c96267465 |

## Acceptance Criteria

See ACCEPTANCE.md for full checklist.
