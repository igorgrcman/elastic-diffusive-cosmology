# Derivation v25 — Alternative Gap Identifications & Robustness Analysis

**Purpose:** Address the reviewer question "Why M_Z and not M_W or v_EW?" with a systematic robustness analysis of proxy selection.

## What This Note Does

1. **Defines proxy family**: M_* ∈ {M_Z, M_W, v_EW}
2. **Propagates each proxy** through the canonical derivation chain
3. **Computes R_ξ(M_*)** and **M_5(M_*)** (both Planck conventions)
4. **Quantifies robustness** via Δlog₁₀(M_5) and factor spread
5. **Justifies M_Z** as metrologically optimal selection

## Key Results

| Proxy | M_* (GeV) | R_ξ (m) | M_5^(red) (GeV) | Δlog₁₀(M_5) |
|-------|-----------|---------|-----------------|-------------|
| M_Z   | 91.19     | 6.80e-18 | 5.56e12        | 0           |
| M_W   | 80.37     | 7.71e-18 | 5.33e12        | -0.018      |
| v_EW  | 246.2     | 2.52e-18 | 7.74e12        | +0.143      |

## Robustness Metrics

- **Total spread**: Δlog₁₀(M_5) = 0.162 (less than 0.2 decades)
- **Factor spread**: 1.45 (all values same order of magnitude)
- **Conclusion**: GUT-scale M_5 is robust against proxy selection

## Metrological Justification for M_Z

1. **Best precision**: δM_Z/M_Z = 2.3×10⁻⁵
2. **Pole mass stability**: gauge-invariant, scheme-independent
3. **Minimal EDC dependence**: avoids θ_W circularity
4. **Definitional simplicity**: primary observable

## Accompanying Script

```bash
python3 recompute.py
```

Output: ALL CHECKS PASSED (15 checks)

## Files

| File | Description |
|------|-------------|
| `main.tex` | Source document (79 equation environments) |
| `main.pdf` | Compiled output (17 pages) |
| `EDC_BLOCK003_DERIVATION_V25_PROXY_ROBUSTNESS.pdf` | Export copy |
| `recompute.py` | Python verification script |
| `REPORT.md` | Build verification report |
| `ACCEPTANCE.md` | Acceptance criteria |

## Epistemic Status

- Identification m_gap = M_Z is **[I]+[BL]**, not **[D]**
- Selection is metrologically justified, not physically derived
- Closure is **robust**: GUT-scale conclusion is proxy-independent
