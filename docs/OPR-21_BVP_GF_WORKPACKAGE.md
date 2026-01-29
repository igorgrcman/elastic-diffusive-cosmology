# OPR-21: Thick-Brane BVP Pipeline for G_F

**Created:** 2026-01-29
**Status:** Pipeline [Der], Physics background [Dc], Numerical values [OPEN]
**Issue:** OPR-21 — Thick-brane BVP solution for G_F non-circular chain
**Blocking:** P3-3 (G_F derivation without circularity)

---

## 1. Purpose

This workpackage implements a reproducible BVP (Boundary Value Problem) pipeline
that computes the mode profiles and overlap integrals required for the non-circular
G_F derivation chain:

```
5D Action → g_5 → M_eff → BVP modes → I_4 → G_F^EDC
```

**Reference:** `docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md`

---

## 2. What Equations Are Solved

### 2.1 Mode Equations

The pipeline solves 1D Schrödinger-like eigenvalue problems:

```
-d²w/dχ² + V(χ)w = λw
```

where χ is the extra-dimension coordinate and V(χ) depends on the mode type.

### 2.2 Mediator Mode (w_φ)

For the scalar/gauge mediator, V(χ) is the background potential:

| Background Type | V(χ) |
|-----------------|------|
| Gaussian wall | V₀ exp(-χ²/2w²) with V₀ < 0 |
| RS-like | (15/4)k² − 3k δ_smooth(χ) |
| Tanh wall | −V₀ sech²(χ/w) |

The eigenvalue λ_0 determines M_eff² = λ_0/δ².

**Reference:** `gf_noncircular_chain_framework.tex`, eq. (111)

### 2.3 Fermion Modes (w_L, w_R)

For domain wall fermions with mass profile m(χ) = m₀ tanh(χ/δ):

```
V_L = m² − m'    (left-handed, localized at χ < 0)
V_R = m² + m'    (right-handed, localized at χ > 0)
```

This gives spatially separated chiral modes.

**Reference:** `gf_noncircular_chain_framework.tex`, Section 3

---

## 3. What Is Assumed vs Derived

### Derived [Der]

| Quantity | Method | Status |
|----------|--------|--------|
| Mode profile shapes | BVP eigenvalue solution | [Der] |
| Normalizations | ∫\|w\|² dχ = 1 | [Der] |
| Overlap I_4 | Numerical integration | [Der] |
| Gate evaluation | Comparison to windows | [Der] |

### Derived Conditional [Dc]

| Quantity | Assumption | Status |
|----------|------------|--------|
| g_5² | Natural 5D scaling: g_5² ~ δ × (4πα/sin²θ_W) | [Dc] |
| Background V(χ) | Gaussian/RS/tanh ansatz | [Dc] |
| Fermion m(χ) | Domain wall: m₀ tanh(χ/δ) | [Dc] |

### Open [OPEN]

| Quantity | Blocking Issue |
|----------|----------------|
| Physical V(χ) | 5D action reduction |
| Physical m(χ) | Fermion localization from brane |
| Numerical G_F | Depends on above |

---

## 4. Normalization Convention

All mode profiles are L² normalized with flat weight:

```
∫ dχ |w(χ)|² = 1
```

The overlap integral has dimension [energy]:

```
I_4 = ∫ dχ w_L² w_R² w_φ²    [dimension: GeV]
```

**Reference:** `gf_noncircular_chain_framework.tex`, eq. (eq:I4_def)

---

## 5. How to Reproduce Results

### 5.1 Quick Test (Toy Profiles)

```bash
cd edc_papers/_shared/bvp_gf
python3 bvp_driver.py --config config.yaml --quick-run
```

This uses exponential ansatz profiles, NOT BVP solutions.

### 5.2 Full BVP Run

```bash
cd edc_papers/_shared/bvp_gf
python3 bvp_driver.py --config config.yaml
```

### 5.3 Modify Parameters

Edit `config.yaml` to change:
- `background.type`: "gaussian_wall", "rs_like", "tanh_wall"
- `modes.fermion_width_delta`: Fermion localization width
- `modes.LR_separation_delta`: Chiral mode separation
- `domain.n_points`: Grid resolution

---

## 6. Output Mapping to X_EDC

### 6.1 Pipeline Outputs

| File | Contents |
|------|----------|
| `out/results.json` | All quantities + gate results |
| `out/profiles_w_L.csv` | Left fermion mode |
| `out/profiles_w_R.csv` | Right fermion mode |
| `out/profiles_w_phi.csv` | Mediator mode |
| `docs/GF_BVP_GATE_REPORT.md` | Human-readable report |

### 6.2 Key Results in results.json

```json
{
  "overlaps": {
    "I_4_GeV": <float>,
    "M_eff_GeV": <float>,
    "g5_squared_GeV_inv": <float>
  },
  "target_comparison": {
    "X_EDC": <float>,
    "X_target": 3.04e-12,
    "X_ratio": <float>
  },
  "gates": {
    "all_pass": <bool>,
    "verdict": <string>
  }
}
```

### 6.3 Formula

```
X_EDC = C × (g_5² × I_4 × m_e²) / M_eff²

where:
  C = 1/(4√2) ≈ 0.177
  X_target = 3.04 × 10⁻¹²
```

---

## 7. Falsification Gates

### Gate 1: Overlap Mismatch

**Criterion:** I_4 must be within [0.1, 10] × I_4_required

where I_4_required is computed from X_target, g_5², M_eff.

**Fail codes:**
- `FAIL_I4_TOO_SMALL`
- `FAIL_I4_TOO_LARGE`

### Gate 2: Mass Inconsistency

**Criterion:** M_eff must be within [0.1, 10] × (1/δ)

**Fail codes:**
- `FAIL_MASS_TOO_SMALL`
- `FAIL_MASS_TOO_LARGE`

### Gate 3: Coupling Incompatibility

**Criterion:** g_eff² must be within [0.1, 10] × (4πα/sin²θ_W)

**Fail codes:**
- `FAIL_COUPLING_TOO_SMALL`
- `FAIL_COUPLING_TOO_LARGE`

---

## 8. File Inventory

### Pipeline Code

```
edc_papers/_shared/bvp_gf/
├── config.yaml      # Configuration
├── bvp_driver.py    # Main entry point
├── bvp_core.py      # BVP solver
├── overlaps.py      # Overlap computation
├── report.py        # Report generator
├── README.md        # Usage instructions
└── out/             # Output directory
    ├── results.json
    └── profiles_*.csv
```

### Documentation

```
docs/
├── OPR-21_BVP_GF_WORKPACKAGE.md   # This file
├── GF_BVP_GATE_REPORT.md          # Auto-generated
└── GF_NONCIRCULAR_FRAMEWORK_NOTE.md  # Framework
```

---

## 9. Caveats

1. **Physics background provisional [Dc]:**
   The potential V(χ) is a working assumption (Gaussian/RS/tanh).
   Physical identification requires 5D action reduction.

2. **g_5 from scaling [Dc]:**
   g_5² ~ δ × (4πα/sin²θ_W) uses dimensional analysis only.

3. **Fermion model [Dc]:**
   Domain wall mass m(χ) = m₀ tanh(χ/δ) is an ansatz.

4. **Quick-run mode:**
   Uses toy exponential profiles, NOT BVP solutions.
   Demonstrates pipeline only.

---

## 10. Status Summary

| Component | Status | Color |
|-----------|--------|-------|
| Pipeline code | [Der] | GREEN |
| Gate evaluation | [Der] | GREEN |
| Config structure | [Der] | GREEN |
| Background V(χ) | [Dc] | YELLOW |
| Fermion m(χ) | [Dc] | YELLOW |
| g_5 value | [Dc] | YELLOW |
| Physical G_F | [OPEN] | RED |

**OPR-21 overall: YELLOW (pipeline complete, physics provisional)**

---

## 11. Cross-References

| Document | Content |
|----------|---------|
| `docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md` | Framework overview |
| `edc_papers/_shared/derivations/gf_noncircular_chain_framework.tex` | LaTeX derivation |
| `edc_papers/_shared/code/gf_toy_overlap_window.py` | Toy feasibility scan |
| `edc_papers/_shared/bvp_gf/README.md` | Pipeline usage |
| `docs/PRIORITY3_WORKPLAN.md` | P3 blocking issues |

---

*Created 2026-01-29. OPR-21 workpackage for G_F BVP pipeline.*
