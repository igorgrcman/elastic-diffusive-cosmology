# Reproducibility Manifest

**Generated:** 2026-02-01
**Canonical source:** `src/derivations/TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex`
**MD5:** `7aea7614d621e06b9774c9b0b5c52779`

---

## Summary

| Category | OK | Missing | Needs Run |
|----------|-----|---------|-----------|
| Scripts | 9 | 0 | - |
| Data | 1 | 0 | - |
| Outputs | 0 | 0 | 4 |
| Documentation | 2 | 0 | - |
| **Total** | **12** | **0** | **4** |

---

## Scripts (9/9 OK)

| Script | Lines in TeX | Source Location | Status |
|--------|--------------|-----------------|--------|
| `v78_canonical_pipeline.py` | 1826 | Created for repro_pack | ✅ OK |
| `m_coordination_full_test.py` | 1024, 1767, 1797 | src/derivations/ | ✅ OK |
| `m6_extended_test.py` | 1781, 1799 | src/derivations/ | ✅ OK |
| `m6_sensitivity_test.py` | 1798 | src/derivations/ | ✅ OK |
| `prefactor_refit_cv.py` | 1772, 1803, 2029 | src/derivations/code/ | ✅ OK |
| `prefactor_sensitivity_full.py` | 1804, 2031 | src/derivations/code/ | ✅ OK |
| `superheavy_oos_test.py` | 1801 | src/derivations/code/ | ✅ OK |
| `superheavy_predictions.py` | 1780, 1802 | src/derivations/code/ | ✅ OK |
| `kramers_double_well_v2.py` | 940, 1805, 2431 | src/derivations/code/ | ✅ OK |

---

## Data Files (1/1 OK)

| File | Lines in TeX | Source | Provenance | Status |
|------|--------------|--------|------------|--------|
| `alpha100_nndc_2025.csv` | 1980 | audit/radioactivity_v7_4_alpha100/04_ALPHA100_DATASET.csv | NNDC Brookhaven, 2025-06-15 | ✅ OK |

---

## Output Files (Need Generation)

| Output | Produced By | Status |
|--------|-------------|--------|
| `v78_oos_table.csv` | v78_canonical_pipeline.py | ⏳ NEEDS_RUN |
| `cv_fold_results.csv` | prefactor_refit_cv.py | ⏳ NEEDS_RUN |
| `bootstrap_params.csv` | prefactor_sensitivity_full.py | ⏳ NEEDS_RUN |
| `alpha100_fitted.csv` | m_coordination_full_test.py | ⏳ NEEDS_RUN |

**To generate:** Run `./repro_pack/run_all.sh` or `python repro_pack/scripts/v78_canonical_pipeline.py --export-all`

---

## Documentation (2/2 OK)

| File | Lines in TeX | Location | Status |
|------|--------------|----------|--------|
| `master_blockers.md` | 2541 | audit/jsonl_mining/ | ✅ OK |
| `master_claims_registry.md` | 1694 | audit/jsonl_mining/ | ✅ OK |

---

## Script Execution Status

Run on 2026-02-01:

| Script | Exit | Notes |
|--------|------|-------|
| `m_coordination_full_test.py` | ✅ 0 | Coordination law verified |
| `m6_extended_test.py` | ✅ 0 | He-4, Li-6, Be-8 tested |
| `superheavy_oos_test.py` | ✅ 0 | 6/6 OOS pass |
| `prefactor_refit_cv.py` | ⏳ | Not yet run |
| `kramers_double_well_v2.py` | ⏳ | Not yet run |

---

## Open Blockers

The following items are documented as open in the monograph and cannot be fully reproduced:

1. **BLOCK-001: V(ξ) Potential** - Not derived from first principles
2. **BLOCK-003: G Formula Powers** - Powers 12, 13 identified by fitting, not derived
3. **BLOCK-004: V_B Barrier** - Calibrated to τ_n = 879s, not derived
4. **K = 4.7 MeV** - Calibrated from He-4 anchor, microscopic derivation OPEN

These do not affect the reproducibility of the empirical results (V7.8 fit, OOS validation).

---

## Verification Commands

```bash
# Verify canonical file
md5 src/derivations/TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex
# Expected: 7aea7614d621e06b9774c9b0b5c52779

# Run all scripts
cd repro_pack && ./run_all.sh

# Check outputs
ls -la repro_pack/outputs/
cat repro_pack/outputs/v78_oos_table.csv
```
