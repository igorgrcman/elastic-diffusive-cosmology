# G_F BVP Pipeline — OPR-21

**Issue:** OPR-21 — Thick-brane BVP solution for G_F non-circular chain
**Status:** [OPEN] — Pipeline implemented, physics values provisional
**Created:** 2026-01-29

---

## Purpose

This pipeline computes the mode profiles and overlap integrals required for
the non-circular G_F derivation chain:

```
5D Action → g_5 → M_eff → BVP modes → I_4 → G_F^EDC
```

Reference: `docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md`

---

## Quick Start

```bash
# Run with default config (BVP solution)
python3 bvp_driver.py --config config.yaml

# Quick test with toy profiles (no BVP solve)
python3 bvp_driver.py --config config.yaml --quick-run

# Verbose output
python3 bvp_driver.py --config config.yaml -v 2
```

---

## Files

| File | Purpose |
|------|---------|
| `config.yaml` | Pipeline configuration |
| `bvp_driver.py` | Main entry point |
| `bvp_core.py` | BVP solver (eigenvalue problem) |
| `overlaps.py` | Overlap integral computation |
| `report.py` | Gate report generator |
| `README.md` | This file |

---

## Outputs

| File | Description |
|------|-------------|
| `out/results.json` | Machine-readable results with git hash |
| `out/profiles_w_L.csv` | Left fermion mode profile |
| `out/profiles_w_R.csv` | Right fermion mode profile |
| `out/profiles_w_phi.csv` | Mediator mode profile |
| `docs/GF_BVP_GATE_REPORT.md` | Human-readable gate evaluation |

---

## Configuration

### Physical Parameters

```yaml
physical:
  delta_GeV_inv: 0.533      # δ = ℏ/(2 m_p c) [Dc]
  m_e_GeV: 0.00051099895    # Electron mass [BL]
  alpha: 0.0072973525693    # Fine structure constant [BL]
  sin2_theta_W: 0.25        # sin²θ_W = 1/4 [Der]
  X_target: 3.04e-12        # G_F × m_e² [BL]
```

### Background Geometry

Available types:
- `gaussian_wall` — Gaussian confining potential
- `rs_like` — Randall-Sundrum-like warp factor
- `tanh_wall` — Hyperbolic tangent domain wall

```yaml
background:
  type: "gaussian_wall"
  wall_width_delta: 1.0     # Wall width in units of δ
```

### Domain and Grid

```yaml
domain:
  L_delta: 10.0             # Domain: χ ∈ [-L, +L] in units of δ
  n_points: 1001            # Grid resolution
  grid_type: "uniform"      # "uniform" or "chebyshev"
```

### Mode Configuration

```yaml
modes:
  compute_w_L: true
  compute_w_R: true
  compute_w_phi: true
  fermion_model: "domain_wall"
  fermion_width_delta: 0.1   # Fermion localization width
  LR_separation_delta: 2.0   # Left-right mode separation
  n_eigenvalues: 5
```

---

## Equations Solved

### Mediator Mode (w_φ)

Schrödinger eigenvalue problem:

```
-d²w_φ/dχ² + V(χ) w_φ = λ w_φ
```

where V(χ) is the background potential (e.g., Gaussian well).

### Fermion Modes (w_L, w_R)

For domain wall fermions with mass profile m(χ):

```
-d²w/dχ² + V_±(χ) w = λ w

V_± = m(χ)² ∓ m'(χ)
```

where `+` is for right-handed and `-` is for left-handed.

### Overlap Integral

```
I_4 = ∫ dχ w_L(χ)² w_R(χ)² w_φ(χ)²
```

Dimension: [I_4] = [energy]

### Non-Circular Formula

```
X_EDC = C × (g_5² × I_4 × m_e²) / M_eff²

where:
  C = 1/(4√2) ≈ 0.177
  g_5² ~ δ × (4πα/sin²θ_W)  [Dc]
  M_eff = √λ_0 / δ          [from BVP]
```

---

## Falsification Gates

### Gate 1: Overlap Window

```
FAIL if: I_4 ∉ [0.1, 10] × I_4_required
```

### Gate 2: Mass Scaling

```
FAIL if: M_eff ∉ [0.1, 10] × (1/δ)
```

### Gate 3: Coupling Compatibility

```
FAIL if: g_eff² ∉ [0.1, 10] × (4πα/sin²θ_W)
```

---

## Caveats

1. **Background is provisional:** The potential V(χ) is a working assumption.
   Physical identification with EDC brane structure requires validation.

2. **g_5 from scaling:** The 5D coupling g_5² ~ δ × (4πα/sin²θ_W) uses
   dimensional analysis, not first-principles derivation.

3. **Fermion localization:** The domain wall model assumes m(χ) = m_0 tanh(χ/δ).
   Actual EDC fermion profile may differ.

4. **Quick-run mode:** Uses toy exponential profiles, NOT BVP solutions.
   Results demonstrate pipeline functionality only.

---

## Cross-References

| Document | Content |
|----------|---------|
| `docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md` | Framework overview |
| `docs/OPR-21_BVP_GF_WORKPACKAGE.md` | Workpackage specification |
| `edc_papers/_shared/derivations/gf_noncircular_chain_framework.tex` | LaTeX derivation |
| `edc_papers/_shared/code/gf_toy_overlap_window.py` | Toy model feasibility |

---

*Created 2026-01-29. Pipeline for OPR-21.*
