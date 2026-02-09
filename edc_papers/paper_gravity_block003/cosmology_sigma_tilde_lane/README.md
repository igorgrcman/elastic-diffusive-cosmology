# Cosmology σ̃ Export Lane

## Purpose

This lane provides the infrastructure to export the dimensionless brane tension
parameter σ̃ (sigma-tilde) from EDC cosmology to BLOCK-004 proton decay predictions.

## Status

**NO NUMERICS HERE** — This is a skeleton only.

- σ̃ value: TBD (awaiting cosmology derivation)
- T_* scale: TBD (awaiting TSTAR_DEFINITION.md)
- σ dimensional: TBD (awaiting upstream connection)

## Contents

| File | Description |
|------|-------------|
| `sigma_tilde_schema.json` | JSON Schema for export format |
| `SIGMA_TILDE_EXPORT_CONTRACT.md` | Interface contract (A-APIσ1/2/3) |
| `build_sigma_tilde_stub.py` | Generates stub JSON with TBD values |
| `recompute.py` | Verification checks (≥25) |

## Consumer

BLOCK-004 derivation v67 imports `sigma_tilde_value.json` via A-APIσ2.

## TODO

1. Derive T_* from 5D brane dynamics (P74b)
2. Compute σ̃ = σ/T_* with uncertainty
3. Generate production sigma_tilde_value.json
