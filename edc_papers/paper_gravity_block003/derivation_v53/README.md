# P54 / Derivation v53: PS Observable Interface Without Contamination

## Summary

This derivation establishes a clean "observable interface layer" that enables future comparison with real-world observables **without contaminating** the canonical derivation chain.

## Key Features

1. **Two-Layer Architecture**
   - Layer A (Canonical): Hash-locked predictions and structural results
   - Layer B (Quarantined): External data adapter with symbolic placeholders

2. **Observable Interface API**
   - API-1: Reference scale μ_* := π/L
   - API-2: sin²θ_W(μ_*) = 5/12 (PREDICTION)
   - API-3: sin²θ_W RG running connector
   - API-4: Invariant I(μ) evolution
   - API-5: sin²θ_W ↔ couplings mapping
   - API-6: G_F(μ_*) formula (PREDICTION)
   - API-7: G_F running connector
   - API-8: α_3 structure (OPEN)

3. **Hard Separation Tables**
   - Table 1: Predictions (structure-only)
   - Table 2: Conditionals (parameter-dependent)
   - Table 3: External Anchors (quarantined)

4. **Hash Firewall**
   - Layer A is read-only for Layer B
   - No experimental values in canonical chain

## Files

| File | Description |
|------|-------------|
| main.tex | LaTeX source |
| main.pdf | Compiled document |
| recompute.py | Verification script (≥55 checks) |
| REPORT.md | Interface specification |
| README.md | This file |
| ACCEPTANCE.md | Acceptance criteria |

## Verification

```bash
python3 recompute.py
```

All checks should PASS.

## Hash Chain

| Version | Topic | Hash |
|---------|-------|------|
| v45 | SoT Lock Track Compiler | a80b3886903152d3 |
| v46 | No-Escape Track Selector | 2742edea37e863ac |
| v47 | PS Coupling Matching | 7a9682f333d5349e |
| v48 | G_F Numerical Closure | c4f114aa0c662b66 |
| v49 | Weinberg Angle Closure | 81010ef2faedcefd |
| v50 | PS→IR Matching Scalemap | cebf3e5baf0de863 |
| v51 | Log Hygiene + Unit Inv | ed8fa089897b2d8c |
| v52 | PS Prediction Pack | ed92d9bc43b8d26b |
| v53 | Observable Interface | (computed) |

## Export

`EDC_BLOCK003_DERIVATION_V53_PS_OBSERVABLE_INTERFACE_NO_CONTAMINATION.pdf`

## Important Note

**This is NOT a claim of matching experiment.** It is engineering-grade methodology for future comparison without breaking the canonical chain.
