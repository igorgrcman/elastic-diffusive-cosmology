# Derivation v29: β Control Parameter

**Title**: The β Control Parameter: $β = σL²/\bar{M}_{Pl}²$

**Status**: [D] core algebra + [BL] inputs + [I] identification dependencies

**Date**: 2026-02-03

---

## Summary

This derivation note establishes and evaluates the dimensionless control parameter β that governs the KK mass gap in the brane-world scenario.

## Key Results

1. **Definition**: $β ≡ σL²/\bar{M}_{Pl}²$ (dimensionless)

2. **Route A** (direct derivation):
   $$β = \frac{ℏc}{L \bar{M}_{Pl}²}$$
   Tag: [BL]

3. **Route B** (via spectral equation):
   $$β = b/λ$$
   where $b = λβ$ controls the Robin BC spectrum.
   Tag: [Dc]

4. **Numeric value** (with identification $L = πℏc/M_Z$):
   $$β = \frac{M_Z}{π\bar{M}_{Pl}²} = 4.89 × 10^{-36}$$
   Tag: [I]+[BL]

5. **Uncertainty**: $δβ/β = 3.2 × 10^{-5}$

## Control Law

Given integer level $k$ and β:
1. $λ(k) = |k|/(2π)$
2. $b(k) = λ(k) · β$
3. Solve $\tan(x_1) = -b/x_1$ for $x_1 ∈ (π/2, π)$
4. $m_{gap}(k) = x_1(b(k))/L$

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (18 pages, 91 equations) |
| `main.pdf` | Compiled PDF |
| `EDC_BLOCK003_DERIVATION_V29_BETA_DERIVATION.pdf` | Export copy |
| `recompute.py` | Numerical verification (10 checks) |
| `ACCEPTANCE.md` | Acceptance criteria verification |
| `REPORT.md` | Detailed report |

## Reviewer Trap Checklist

All 10 traps addressed with explicit equation references:
- TRAP-1: Dimensions (eq:beta-dim-check)
- TRAP-2: ℏ exact (eq:hbar-exact)
- TRAP-3: L vs R (conv:length-dict)
- TRAP-4: Planck conventions (eq:Mpl-map, eq:M5-map)
- TRAP-5: M̄_Pl as [BL] (tab:ledger)
- TRAP-6: Double counting L (eq:beta-L-open, eq:beta-L-identified)
- TRAP-7: Circularity (sec:route-a, sec:route-b)
- TRAP-8: Robin BC origin (sec:robin-origin)
- TRAP-9: Topological quantization (sec:trap9)
- TRAP-10: Numerical stability (sec:numerical, tab:residuals)

## Dependencies

- v26: Gap mechanism with Robin BC
- v27: m_b = λσ/M_5³ derivation
- v28: λ-quantization program

## Gap Status

The mass gap remains **[I]+[BL]** because:
- L is identified via m_gap = M_Z, not derived
- λ has topological postulate [P]
- β uses baseline inputs

---

*EDC Collaboration, February 2026*
