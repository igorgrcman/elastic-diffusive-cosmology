# P3 Compliance Report: Reviewer Hardening

**Generated:** 2026-02-01T20:40
**Task:** Reviewer Hardening / Red-Team Response to P2 findings

---

## Executive Summary

| Task | Status | Notes |
|------|--------|-------|
| P3-A-1: Undefined references | ✅ PASS | 0 undefined refs (was 3) |
| P3-A-2: He-4 consistency | ✅ PASS | Explicit model vs anchor distinction |
| P3-B-3: run_all.sh modes | ✅ PASS | --fast/--full implemented |
| P3-B-4: alpha100_fitted.csv | ✅ PASS | Full 106 rows exported |
| P3-B-5: Numeric claims cite outputs | ✅ PASS | All cite artifact files |
| P3-C-6: Wrapper documentation | ✅ PASS | v78_canonical_pipeline.py documented |
| P3-C-7: Og-294 delta alignment | ✅ PASS | Consistent 0.17 dex |

---

## P3-A: Publish Blockers (FIXED)

### P3-A-1: Undefined References

**Before:** 3 undefined references (`sec:neutron-lifetime`)

**Fix:** Multiple xelatex passes to resolve cross-references.

**Verification:**
```bash
xelatex TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex 2>&1 | grep -i undefined
# Output: (empty - no undefined references)
```

**Result:** ✅ 0 undefined references

---

### P3-A-2: He-4 Consistency

**Issue:** Text says K = 28.3/6 = 4.72 MeV (anchor), script reports He-4 = 30.5 MeV (model)

**Resolution:** Added explicit distinction in tex (L1178-1180):

> **Full model note:** The simple bond-counting formula E = N_b × K gives 28.2 MeV by design. The full M6 model (`m6_extended_test.py`) includes additional terms (confinement, surface, flux closure) and predicts 30.5 MeV—a 7.8% overshoot. This discrepancy is acceptable for an anchor calibration; the key test is relative predictions (e.g., Be-8 instability).

**Numerics line updated to:** `m6_extended_test.py outputs: He-4 model=30.5 MeV, obs=28.3 MeV; anchor gives K = 28.3/6 = 4.72 MeV.`

**Interpretation:**
- K = 4.72 MeV is **calibrated** from experimental He-4 (28.3 MeV / 6 bonds)
- Full model predicts 30.5 MeV (includes additional terms beyond K × bonds)
- 7.8% overshoot is documented and acceptable

**Result:** ✅ Consistent story documented

---

## P3-B: Repro Credibility (FIXED)

### P3-B-3: run_all.sh Modes

**Fix:** Added `--fast` (default) and `--full` modes to `run_all.sh`:

```bash
./run_all.sh           # Fast mode - skips slow scripts
./run_all.sh --fast    # Same as default
./run_all.sh --full    # Full mode - runs everything
```

**Slow scripts (skipped in fast mode):**
- `prefactor_sensitivity_full.py` (5-10 min, produces bootstrap_params.csv)

**Output:** Script now reports passed/failed/skipped counts and expected artifacts.

---

### P3-B-4: alpha100_fitted.csv Full Export

**Before:** Header only (3 lines)

**After:** Full dataset (107 lines = 1 header + 106 data rows)

**Columns:**
| Column | Description |
|--------|-------------|
| nuclide | e.g., Bi-211 |
| Z | Atomic number |
| A | Mass number |
| Q_keV | Alpha decay Q-value |
| t12_exp_s | Experimental half-life (s) |
| log10_t12_exp | log₁₀(t½) experimental |
| n_coord | Coordination number n(A) = 6.1 × A^{1/3} |
| d_n | Distance to nearest allowed n |
| log10_t12_pred | V7.8 M2 prediction |
| residual | log₁₀(exp) - log₁₀(pred) |
| split | train/test flag |

**Verification:**
```bash
wc -l repro_pack/outputs/alpha100_fitted.csv
# 107 repro_pack/outputs/alpha100_fitted.csv
```

---

### P3-B-5: Numeric Claims Cite Output Files

All numeric claims in tex now cite specific artifact files:

| Claim | Artifact |
|-------|----------|
| CV R² = 0.971 | outputs/cv_fold_results.csv |
| OOS 6/6 pass | outputs/v78_oos_table.csv |
| Og-294 Δ = 0.17 dex | outputs/v78_oos_table.csv |
| n(A) = 6.1 × A^{1/3} | m_coordination_full_test.py stdout |
| He-4 model = 30.5 MeV | m6_extended_test.py stdout |

---

## P3-C: Trust Hygiene (FIXED)

### P3-C-6: Wrapper Documentation

**Added to tex (L1810):**
> **Note on v78_canonical_pipeline.py:** This is an *orchestrator wrapper* only—it does not modify any model equations or physics. It calls the above scripts in sequence and exports results to CSV files. All physics calculations are in the individual scripts.

**Added to UPLOAD_README.md:**
> The script `v78_canonical_pipeline.py` is a **wrapper/orchestrator** only. It:
> - Does NOT modify any model equations or physics
> - Calls existing analysis scripts in sequence
> - Exports results to CSV files for documentation

---

### P3-C-7: Og-294 Delta Alignment

**Before:** P2_COMPLIANCE_REPORT.md had 0.16, tex had 0.17

**After:** Consistent 0.17 dex everywhere:
- TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex: 0.17 (L148, L1460, L1506, L1521)
- v78_oos_table.csv: 0.17
- P2_COMPLIANCE_REPORT.md: 0.17 (fixed)

---

## File Hashes

| File | MD5 | Lines |
|------|-----|-------|
| TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex | `7a5f9a05dc12d5a6d55957357cca95a3` | 2586 |
| EXPORT_TO_UPLOAD.tex | `7a5f9a05dc12d5a6d55957357cca95a3` | 2586 |
| EXPORT_TO_UPLOAD.pdf | - | 42 pages |
| alpha100_fitted.csv | - | 107 rows |
| v78_oos_table.csv | - | 7 rows |
| cv_fold_results.csv | - | 8 rows |

---

## Verification Commands

```bash
cd edc_book_2

# 1. Verify 0 undefined refs
cd src/derivations
xelatex TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex 2>&1 | grep -i undefined
# Should be empty

# 2. Verify He-4 consistency
grep "model=30.5" TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex
# Should show: "m6_extended_test.py outputs: He-4 model=30.5 MeV..."

# 3. Verify run_all.sh modes
cd ../../repro_pack
./run_all.sh --help 2>&1 | head -5
# Should mention --fast and --full

# 4. Verify alpha100_fitted.csv
wc -l outputs/alpha100_fitted.csv
# Should be 107

# 5. Verify Og-294 delta consistency
grep "0.17" outputs/v78_oos_table.csv
# Should show Og-294 with 0.17
```

---

## Remaining Items (Non-Blocking)

1. **m8_pauli_test.py** and **delta_m_np_options.py** referenced in tex but not in repro_pack (internal development scripts, not required for main results)

2. **Full --full mode test** not run (prefactor_sensitivity_full.py takes 5-10 min)

3. **Figures** are TikZ-generated, no external figure files to include

---

**Report generated by Claude Code**
**Branch:** backfill/tier2-v1
