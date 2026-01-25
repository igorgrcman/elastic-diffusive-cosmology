# REPRO Pack — Book 2 Reproducibility Artifacts

**Status**: OPR-07 PARTIAL
**Date**: 2026-01-25
**Branch**: book2-opr07-repropack-v1

---

## Overview

This directory contains **physics-grade reproducibility scripts** that verify
specific numerical claims in EDC Book 2. Each script maps to explicit claim IDs
and/or equation labels.

**Classification**:
- **REPRO**: Supports physics claims with deterministic, verifiable output
- **DEMO**: Pedagogical only (not physics evidence)

## Quick Start

```bash
# From edc_book_2/ directory:
cd repro
bash run_all.sh

# Verify outputs:
python ../tools/repro_gate.py
```

## Requirements

- **Python**: 3.8+ (tested on 3.11)
- **Dependencies**: See `requirements.txt`
- **No randomness**: All scripts are deterministic (fixed seeds where applicable)

## Scripts

| Script | Classification | Supports Claims |
|--------|---------------|-----------------|
| `scripts/repro_sin2_z6_verify.py` | REPRO | E-CH11-Der-005, E-CH11-Der-013 |
| `scripts/repro_sin2_rg_running.py` | REPRO | E-CH04-Dc-012 |

## Outputs

All outputs are written to `output/` with deterministic content:

| File | Format | Script |
|------|--------|--------|
| `sin2_z6_verify.json` | JSON | repro_sin2_z6_verify.py |
| `sin2_rg_running.json` | JSON | repro_sin2_rg_running.py |
| `checksums.sha256` | SHA256 | run_all.sh |

## Verification

After running, verify hashes match:
```bash
cd output
sha256sum -c checksums.sha256
```

Or use the gate script:
```bash
python tools/repro_gate.py
```

## Claim Mappings

See `REPRO_MANIFEST.yml` for complete mapping:
- Script → Claim IDs → Chapter anchors → Output files

## Notes

1. **Determinism**: No random seeds, fixed solver tolerances
2. **No physics edits**: Scripts verify existing claims, don't create new ones
3. **Honest scope**: Each script states exactly what it proves/supports

---

*Part of OPR-07 closure pack*
