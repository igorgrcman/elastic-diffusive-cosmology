# E5 REPRO Report — Reproducibility Scripts

**Date**: 2026-01-25
**Branch**: book2-opr-registry-v1
**Phase**: E5 (Evidence Remediation)

---

## Summary

| Metric | Before E5 | After E5 |
|--------|-----------|----------|
| DEMO scripts | 1 | 1 |
| REPRO scripts (complete) | 0 | 1 |
| REPRO scripts (stub) | 0 | 1 |
| Total REPRO | 0 | 2 |

---

## New REPRO Scripts

### 1. repro_sin2_z6_verify.py — COMPLETE

| Field | Value |
|-------|-------|
| **Path** | `code/repro/repro_sin2_z6_verify.py` |
| **Classification** | REPRO (Complete) |
| **SHA256** | `3d3a76ac1a9173104932bcf56ee9655b16d61220dc5cdaad0391580e442c2653` |
| **Status** | RUNNABLE |

**Supports claims**:
- E-CH11-Der-005: sin²θ_W = 1/4 from Z₆ subgroup counting
- E-CH11-Der-013: sin²θ_W(μ_lattice) = |Z₂|/(|Z₂|+|Z₆|) = 1/4

**What it verifies**:
1. Z₆ subgroup structure (Z₂ = {0,3}, Z₃ = {0,2,4})
2. Coupling ratio g'²/g² = |Z₂|/|Z₆| = 2/6 = 1/3
3. sin²θ_W = (1/3)/(1+1/3) = 1/4
4. Alternative formula: |Z₂|/(|Z₂|+|Z₆|) = 2/8 = 1/4
5. Comparison with PDG: 8.1% deviation (bare), ~0.5% after RG

**Output**:
- `code/output/repro_sin2_z6_result.txt`
- SHA256: `afb13677d8e2fd22564da90eb701c340a4994b8dd8dc0f08ba199462ad1ae472`

**Run command**:
```bash
cd edc_book_2
python code/repro/repro_sin2_z6_verify.py
```

---

### 2. repro_i4_overlap_stub.py — BLOCKED (OPR-21)

| Field | Value |
|-------|-------|
| **Path** | `code/repro/repro_i4_overlap_stub.py` |
| **Classification** | REPRO (Stub — OPR-21 Blocked) |
| **SHA256** | `8fca6468ef4807a99f2d1c3d00fe5b9a85d08fcc7719f59d89a9380ebf5485fd` |
| **Status** | BLOCKED |

**Supports claims** (when unblocked):
- E-CH11-Dc-014: G_F = G₅ ∫|f_L|⁴ dξ
- E-CH14-Dc-*: BVP eigenvalue claims

**Blocking OPRs**:
- OPR-21: I₄ overlap from BVP
- OPR-02: Robin α from action (upstream)
- OPR-20: V(ξ) and ℓ from membrane (upstream)

**Failure behavior**:
Script exits with code 1 and prints clear error message:
```
REPRO SCRIPT BLOCKED: repro_i4_overlap_stub.py

This script is blocked by OPR-21: I₄ overlap from BVP

MISSING INPUTS:
  - f_L_profile: output/bvp_fL_profile.npy
  - bvp_params: output/bvp_params.json
```

**Run command**:
```bash
cd edc_book_2
python code/repro/repro_i4_overlap_stub.py
# Expected: Exit code 1, clear error message
```

---

## Build Infrastructure

### tools/build.sh — NEW

| Field | Value |
|-------|-------|
| **Purpose** | Single-command deterministic build |
| **Output** | `build/main.pdf` |
| **Verification** | Page count (387) + SHA256 |

**Features**:
- Dependency checking (xelatex, latexmk)
- Page count verification via pdfinfo
- SHA256 hash recording
- Clean failure modes

**Run command**:
```bash
cd edc_book_2
bash tools/build.sh --verify
```

### audit/evidence/BUILD_DEPS.md — NEW

Documents all build dependencies with installation instructions for:
- macOS (Homebrew + MacTeX)
- Ubuntu/Debian
- Conda environments

---

## OPR-07 Status Update

**Before E5**: OPEN (no REPRO scripts)

**After E5**: PARTIAL
- 1 complete REPRO script (sin²θ_W verification)
- 1 stub REPRO script (I₄ overlap, blocked by OPR-21)
- Build infrastructure documented

**To close OPR-07 fully**:
- Close OPR-21 to enable I₄ calculation
- Run repro_i4_overlap_stub.py successfully
- Add REPRO scripts for other numerical claims (τ_n, lepton masses)

---

## Claim Status Updates

| Claim | Old Status | New Status | Reason |
|-------|------------|------------|--------|
| E-CH11-Der-005 | COMPLETE | COMPLETE (REPRO) | Now has reproducibility script |
| E-CH11-Der-013 | COMPLETE | COMPLETE (REPRO) | Now has reproducibility script |
| E-CH11-Dc-014 | PARTIAL | PARTIAL (REPRO-stub) | Stub documents what's missing |
| E-CH14-Dc-* | PARTIAL | PARTIAL (REPRO-stub) | Stub documents what's missing |

---

## Files Created

| File | Purpose |
|------|---------|
| `code/repro/repro_sin2_z6_verify.py` | Verify sin²θ_W = 1/4 from Z₆ |
| `code/repro/repro_i4_overlap_stub.py` | Stub for I₄ calculation (OPR-21) |
| `code/output/repro_sin2_z6_result.txt` | Verification output |
| `tools/build.sh` | Deterministic build script |
| `audit/evidence/BUILD_DEPS.md` | Build dependencies documentation |

---

*Generated: 2026-01-25*
*Evidence Audit Phase E5*
