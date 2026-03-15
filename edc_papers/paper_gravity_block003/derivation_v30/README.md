# Derivation v30: Derive or Constrain L from β + λ

**Title**: Derive or Constrain L from β + λ (No Gap Identification)

**Status**: [D]+[P]+[BL] for structure; [OPEN] for point selection

**Date**: 2026-02-03

---

## Summary

This derivation note investigates whether the interval length L can be derived
or constrained using only the control parameter β and the topologically quantized
coupling λ, WITHOUT invoking any gap identification (m_gap = M_Z or similar).

## Key Results

1. **Main Relation** (derived):
   $$L = \frac{\hbar c}{\beta \cdot \bar{M}_{\text{Pl}}^2}$$
   Tag: [D]+[BL]

2. **k-Branch Structure**:
   - For each k ∈ Z⁺, λ = |k|/(2π)
   - b = λβ defines the Robin BC parameter
   - Solutions form discrete k-branches

3. **Closure Status**:
   - **Weak closure achieved**: L constrained to discrete k-branches
   - **Strong closure NOT achieved**: Point selection on branches requires identification

4. **No Identification Used**:
   - M_Z, M_W, v_EW: NOT used
   - ℓ_P, G_N: NOT used
   - R_ξ = ℏc/M_Z: NOT used

## Routes

### Route C (Variational)
- Constructs effective functional E_eff(L)
- Stationarity dE_eff/dL = 0 constrains β
- Combined with λ-quantization gives discrete L_k

### Route D (Spectral)
- Uses spectral condition tan(x) = -b/x
- λ enters via b = λβ
- Continuous family F_k for each k

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (19 pages, 91 equations) |
| `main.pdf` | Compiled PDF |
| `EDC_BLOCK003_DERIVATION_V30_DERIVE_L_FROM_BETA_LAMBDA.pdf` | Export copy |
| `recompute.py` | Numerical verification (15 checks, ALL PASS) |
| `ACCEPTANCE.md` | Acceptance criteria verification |
| `REPORT.md` | Detailed report with inputs table |

## Dependencies

- v28: λ-quantization from SA extension + topology
- v29: β control parameter derivation

## Gap Status

The gap remains **[OPEN]** for unique L determination because:
- L is constrained to discrete k-branches
- Point selection requires one identification or variational principle
- No internal principle uniquely fixes β

---

*EDC Collaboration, February 2026*
