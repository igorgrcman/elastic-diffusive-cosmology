# Derivation v23 — BLOCK-003 Canonical Closure Packet

**Purpose:** Reviewer-grade derivation-first closure document incorporating all convention decisions from v20 (factor audit) and v22 (KK conventions unification).

## What This Note Does

1. **Full derivation chain** from 5D action to 4D Newton constant in one unbroken sequence
2. **Convention lock** using v22 canonical choice (R_ξ ≡ L = interval length)
3. **Both Planck mass conventions** with explicit (8π)^{1/3} conversion factor
4. **Conventions dictionary** mapping between all parametrizations (v15-v21)
5. **Error budget** with complete propagation analysis
6. **Epistemic ledger** with all tags ([D], [I], [BL], NO-GO, OPEN)
7. **Compatibility section** for translating v15-v21 results

## Key Results

| Convention | R_ξ (m) | M_5 (GeV) |
|------------|---------|-----------|
| Canonical (reduced M̄_Pl) | 6.80 × 10⁻¹⁸ | 5.6 × 10¹² |
| Alternative (original M_Pl) | 6.80 × 10⁻¹⁸ | 1.6 × 10¹³ |

**Conversion:** M_5^(original) = (8π)^{1/3} × M_5^(reduced) ≈ 2.92 × M_5^(reduced)

## Convention Mappings

| Parameter | Canonical (v22+) | Old (v15-v20) |
|-----------|------------------|---------------|
| R_ξ definition | L (interval) | R (radius) |
| R_ξ from M_Z | πℏc/M_Z | ℏc/M_Z |
| Numerical R_ξ | 6.80e-18 m | 2.17e-18 m |
| m_gap formula | π/R_ξ | 1/R_ξ |

**Translation:** R_ξ^(canon) = π × R_ξ^(old); M_5^(canon) = π^{-1/3} × M_5^(old)

## Error Budget

- δM_5/M_5 ≈ 1.1 × 10⁻⁵ ≈ 0.001%
- Dominated by M_Z uncertainty through R_ξ

## Files

| File | Description |
|------|-------------|
| `main.tex` | Source document (97 equation environments) |
| `main.pdf` | Compiled output (15 pages) |
| `EDC_BLOCK003_DERIVATION_V23_CANONICAL_CLOSURE_PACKET.pdf` | Export copy |
| `REPORT.md` | Build verification report |
| `ACCEPTANCE.md` | Acceptance criteria |

## What This Note Does NOT Do

- Does NOT modify v15-v22 (they remain as written)
- Does NOT derive M_Z from EDC axioms (still [I]+[BL])
- Does NOT resolve internal R_ξ derivation (remains NO-GO)
