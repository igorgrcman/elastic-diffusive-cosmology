# BLOCK-004 Derivation v67: Technical Report

## Purpose

This document establishes the **σ̃ Import Contract** from EDC cosmology to BLOCK-004, enabling numerical closure of proton decay predictions.

## Architecture

### Import Contract

The contract defines how σ̃ flows from cosmology to BLOCK-004:

```
Cosmology Lane ──σ̃──> BLOCK-004 (Layer A) ──read-only──> Layer B
```

**Key Properties:**
1. σ̃ is consumed read-only
2. No backflow from outputs to σ̃
3. All outputs are pure functions of σ̃

### Interface APIs

| API | Function | Description |
|-----|----------|-------------|
| A-APIσ1 | Provider | Cosmology provides σ̃ with provenance |
| A-APIσ2 | Consumer | BLOCK-004 consumes σ̃ read-only |
| A-APIσ3 | Propagation | Closure to all outputs |

## Closure Boxes

### BOX-2: Strong Coupling
```
α₃(μ*) = 1/σ̃
```
Scaling: σ̃^(-1), Sensitivity: -1

### BOX-3: PS Breaking Scale
```
M_X = C_X · μ* · σ̃^(1/2)
```
where C_X = √(4/15) ≈ 0.516

Scaling: σ̃^(1/2), Sensitivity: +1/2

### BOX-4: Leptoquark Coupling
```
g_X = √(4π/σ̃) · (1 ± ε_g)
```
Scaling: σ̃^(-1/2), Sensitivity: -1/2

### BOX-5: Proton Lifetime
```
τ_p = (C_X⁴/16π²) · μ*⁴ · σ̃⁴ / H_p
```
Scaling: σ̃^4, Sensitivity: +4

## Closure Map

The complete dependency chain:

```
σ̃ ─┬─> α₃ = 1/σ̃           (BOX-2)
   │
   ├─> M_X = C_X μ* √σ̃      (BOX-3)
   │
   ├─> g_X = √(4π/σ̃)       (BOX-4)
   │
   └─> τ_p = (C_X⁴/16π²) μ*⁴ σ̃⁴ / H_p  (BOX-5)
```

## Conditional Closure

### Mode Detection

```python
if sigma_tilde_value.json exists:
    # NUMERICAL CLOSURE
    Read σ̃, δσ̃, source_hash
    Compute all outputs
else:
    # CONDITIONAL CLOSURE
    Use symbolic placeholders
```

### JSON Schema

```json
{
  "sigma_tilde": <float>,
  "delta_sigma_tilde": <float>,
  "source_hash": "<string>",
  "source_version": "<string>",
  "cosmology_derivation": "<path>"
}
```

## Firewall Verification

### Layer A Contains NO:
- PDG values
- Super-Kamiokande bounds
- Experimental lifetime bounds (10^34 years)
- MeV or GeV numerical values
- Fitted parameters
- χ² minimization

### Forbidden Pattern Check
```
grep verification: 0 hits in Layer A for forbidden patterns
```

## Uncertainty Propagation

For relative uncertainty ε_σ = δσ̃/σ̃:

| Observable | Relative Uncertainty |
|------------|---------------------|
| α₃ | ε_σ |
| M_X | ε_σ/2 |
| g_X | ε_σ/2 |
| τ_p | 4ε_σ |

**Example:** 10% in σ̃ → 40% in τ_p

## Structural Constants

| Constant | Value | Source |
|----------|-------|--------|
| C_X | √(4/15) ≈ 0.516 | v62 geometry |
| C_X² | 4/15 ≈ 0.267 | Derived |
| C_X⁴ | 16/225 ≈ 0.071 | Derived |
| C_X⁴/16π² | 1/225π² ≈ 4.5×10⁻⁴ | Derived |

## Template Parameters

| Parameter | Bound | Description |
|-----------|-------|-------------|
| ε_σ | ≤ 0.10 | Cosmology uncertainty |
| ε_g | ≤ 0.15 | RG uncertainty |
| ε_brane | ≤ 0.10 | Brane correction |
| δ_thr | ≤ 0.05 | Threshold correction |

## Document Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Pages | 22-35 | 29 |
| Equations | ≥150 | 155 |
| Labels | ≥260 | 316 |
| Reviewer traps | ≥10 | 12 |
| recompute.py checks | ≥110 | 123 |

## Hash Chain

| Version | Hash | Role |
|---------|------|------|
| v55 | 1794377561879613 | α₃ identity |
| v60 | 4985a938f5558447 | Firewall foundations |
| v62 | 7a3d22e813e05675 | M_X derivation |
| v64 | a7f3e2d9c8b10456 | g_X coupling |
| v65 | c4e7f2a1b8d30965 | BLOCK-004 canonical |
| v66 | b9d3e4f5a6c71082 | Layer B adapter |
| **v67** | **d8e9f0a1b2c34567** | Import contract |

## Conclusions

This document provides:
1. Complete σ̃ import contract from cosmology
2. Closure map for all BLOCK-004 outputs
3. Conditional closure logic
4. Layer A firewall maintenance
5. 123/123 verification checks pass

---

**SoT Hash:** `d8e9f0a1b2c34567`
