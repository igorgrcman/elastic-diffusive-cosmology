# NUMERICS REPRO LEDGER — Book 2 Evidence Audit

**Branch**: book2-chapter-audit-v1
**Date**: 2026-01-25
**Phase**: E3 (Numerics Reproducibility Pack)

---

## Classification Legend

| Type | Meaning | Can Support Physics Claims? |
|------|---------|----------------------------|
| **DEMO** | Pedagogical demonstration | NO |
| **REPRO** | Reproducibility artifact | YES (with citation) |
| **AUDIT** | Audit/validation tooling | NO (infrastructure) |

---

## Summary

| Type | Count | Notes |
|------|-------|-------|
| DEMO | 1 | BVP toy model (textbook potential) |
| REPRO | 0 | No physics-supporting scripts yet |
| AUDIT | 5 | Notation/symbol extraction tools |
| Gates | 4 | Build validation scripts |

---

## DEMO Artifacts (1)

### code/bvp_halfline_toy_demo.py

| Field | Value |
|-------|-------|
| **Classification** | DEMO (Pedagogical) |
| **SHA256** | `fc2fb9617b81ee31a3a2e66efccd04ab0ff94b687062348287dd188bba460e2c` |
| **Purpose** | Demonstrate BVP methodology with textbook potential |
| **Dependencies** | numpy, matplotlib (optional), scipy (optional) |
| **Output** | `code/output/bvp_halfline_toy_figure.pdf` |
| **Physics claim support** | **NONE** — toy model only |

**Regeneration Command:**
```bash
cd /Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2
python code/bvp_halfline_toy_demo.py
```

**WARNING**: This script uses the Poschl-Teller potential V(ξ) = -V₀ sech²(ξ/a),
which is a textbook toy model NOT derived from EDC membrane physics.
DO NOT cite this figure as evidence for any physics claims.

---

## REPRO Artifacts (3)

**Status**: 2 complete, 1 stub (blocked by OPR-21)

**Location**: `repro/` directory (primary), `code/repro/` (legacy)

### repro/scripts/repro_sin2_z6_verify.py — COMPLETE

| Field | Value |
|-------|-------|
| **Classification** | REPRO (Complete) |
| **Purpose** | Verify sin²θ_W = 1/4 from Z₆ subgroup counting |
| **Dependencies** | Python 3.8+ (standard library only) |
| **Output** | `repro/output/sin2_z6_verify.json` |
| **Supports claims** | E-CH11-Der-005, E-CH11-Der-013 |

**What it verifies**:
- Z₆ subgroup structure (Z₂ = {0,3}, Z₃ = {0,2,4})
- Coupling ratio g'²/g² = |Z₂|/|Z₆| = 1/3
- sin²θ_W = (1/3)/(1+1/3) = 1/4

**Regeneration Command:**
```bash
cd edc_book_2/repro
bash run_all.sh
```

### repro/scripts/repro_sin2_rg_running.py — COMPLETE (SUPPORTING)

| Field | Value |
|-------|-------|
| **Classification** | REPRO (Supporting) |
| **Purpose** | Verify sin²θ_W RG running from lattice scale to M_Z |
| **Dependencies** | Python 3.8+ (standard library only) |
| **Output** | `repro/output/sin2_rg_running.json` |
| **Supports claims** | E-CH04-Dc-012 (CONDITIONAL) |

**What it verifies**:
- RG shift Δsin²θ_W ≈ -0.019 is consistent with SM
- sin²θ_W(M_Z) = 0.232 matches PDG to 0.18%

**Caveats**:
- Uses phenomenological RG coefficient (not first-principles)
- Lattice scale is [P] postulated

### code/repro/repro_i4_overlap_stub.py — BLOCKED (OPR-21)

| Field | Value |
|-------|-------|
| **Classification** | REPRO (Stub — Blocked) |
| **SHA256** | `8fca6468ef4807a99f2d1c3d00fe5b9a85d08fcc7719f59d89a9380ebf5485fd` |
| **Purpose** | Document I₄ overlap integral requirements |
| **Blocking OPR** | OPR-21 (I₄ overlap from BVP) |
| **Supports claims** | E-CH11-Dc-014, E-CH14-Dc-* (when unblocked) |

**Note**: This script FAILS LOUDLY by design. It documents exactly what inputs are missing.

**Required for future closure:**

| Claim | Required Script | Status |
|-------|-----------------|--------|
| sin²θ_W = 1/4 | repro_sin2_z6_verify.py | ✅ COMPLETE |
| G_F derivation | repro_i4_overlap_stub.py | BLOCKED by OPR-21 |
| τ_n ≈ 830s | WKB barrier calculation | NOT STARTED |
| m_e/m_p ratio | BVP eigenvalue solver | NOT STARTED |

---

## AUDIT Artifacts (5)

These scripts support audit infrastructure, not physics claims.

### tools/symbol_extract_canon.py
| Field | Value |
|-------|-------|
| **SHA256** | `0782e095f2af1783ff6f131f49915ab8847ee32be360afb669107cc4b97651b7` |
| **Purpose** | Extract symbols from GLOBAL_SYMBOL_TABLE.tex |

### tools/symbol_extract_book2.py
| Field | Value |
|-------|-------|
| **SHA256** | `5de3f3979c944b2416965a8dcee1b41a0b072f1739464c0d064c17ffff81d682` |
| **Purpose** | Extract symbols from Book 2 chapters |

### tools/chapter_audit_extract.py
| Field | Value |
|-------|-------|
| **SHA256** | `1b41696ec68bcccceaa4c55a76448a5dde32cd77eba36027df0930a1eb699b68` |
| **Purpose** | Extract claims and equations per chapter |

### tools/symbol_audit.py
| Field | Value |
|-------|-------|
| **SHA256** | `0a6b060f4f6f2b52add0be5f52573c0d64cac5ddfcedc452c5f4de47ecb163fc` |
| **Purpose** | Cross-check symbols against canon |

### tools/ch1_asset_scan.py
| Field | Value |
|-------|-------|
| **SHA256** | `f9dc0747cc05c14c7000d887a5f7c20c8d7b8e352370970e9d70e08732fb6777` |
| **Purpose** | Scan CH01 for asset references |

---

## Gate Scripts (4)

Build validation infrastructure.

### tools/gate_notation.sh
- Checks for forbidden notation patterns
- Part of CI pipeline

### tools/gate_canon.sh
- Verifies canon symbol consistency
- Part of CI pipeline

### tools/gate_build.sh
- Runs XeLaTeX build, checks page count
- Part of CI pipeline

### tools/gate_assets_ch1.sh
- Validates CH01 asset references
- Part of CI pipeline

---

## Output Files

### code/output/bvp_halfline_toy_figure.pdf

| Field | Value |
|-------|-------|
| **Generated by** | `code/bvp_halfline_toy_demo.py` |
| **Size** | 36,463 bytes |
| **Classification** | DEMO output |
| **Referenced in** | `sections/ch14_bvp_closure_pack.tex:1176` |
| **Physics support** | **NONE** |

---

## Reproducibility Requirements

To regenerate all DEMO outputs:

```bash
cd /Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2
mkdir -p code/output
python code/bvp_halfline_toy_demo.py
```

To run all gates:

```bash
cd /Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2
bash tools/gate_notation.sh
bash tools/gate_canon.sh
bash tools/gate_build.sh
```

---

## Future REPRO Scripts Needed

| Priority | Script | Purpose | Blocking OPR |
|----------|--------|---------|--------------|
| HIGH | `repro_sin2_z6.py` | Verify sin²θ_W = 1/4 from Z₆ | OPR-17 |
| HIGH | `repro_gf_overlap.py` | Compute I₄ overlap integral | OPR-21 |
| MEDIUM | `repro_tau_n_wkb.py` | WKB barrier for neutron lifetime | OPR-20 |
| MEDIUM | `repro_lepton_masses.py` | Lepton mass ratios from BVP | OPR-02 |

**Note**: All future REPRO scripts must include:
1. Explicit input parameter documentation
2. Reference to source equations in Book 2
3. Comparison with [BL] experimental values
4. SHA256 hash tracking in this ledger

---

*Generated: 2026-01-25*
*Evidence Audit Phase E3*
