# V7.8 MODEL SPECIFICATION

**Created**: 2026-01-31
**Purpose**: Pre-register model set and decision thresholds

---

## Model Hierarchy

### Base Models

| Model | Formula | Purpose |
|-------|---------|---------|
| M0 | log₁₀(t₁/₂) = a(Z/√Q) + b | GN baseline |
| M1 | M0 + c₁I(H1) + c₂I(H2) | Add hindrance |
| M2 | M1 + g×d(n) | V7.4 model (reference) |

### Proxy Models

| Model | Formula | Tests |
|-------|---------|-------|
| M3 | M1 + δ×proxy_deform | Does deformation predict? |
| M4 | M1 + σ×proxy_Salpha | Does S_α predict? |

### Combined Models (Mediation Tests)

| Model | Formula | Tests |
|-------|---------|-------|
| M5 | M1 + g×d(n) + δ×proxy_deform | Does g survive deformation control? |
| M6 | M1 + g×d(n) + σ×proxy_Salpha | Does g survive S_α control? |
| M7 | M1 + g×d(n) + δ×proxy_deform + σ×proxy_Salpha | Full control |

---

## Pre-Registered Primary Tests

### P1: d(n) Significance in M2

**Null**: g = 0 in M2
**Alternative**: g ≠ 0
**Threshold**: p < 0.01
**Expected**: PASS (from V7.4)

### P2: d(n) Survives Deformation Control (M5)

**Null**: g = 0 when proxy_deform included
**Alternative**: g < 0 and significant
**Threshold**: p < 0.05 AND g < 0
**Decision**:
- PASS → d(n) is not just a deformation proxy
- FAIL → d(n) may be confounded with deformation

### P3: d(n) Survives S_α Control (M6)

**Null**: g = 0 when proxy_Salpha included
**Alternative**: g < 0 and significant
**Threshold**: p < 0.05 AND g < 0
**Decision**:
- PASS → d(n) is not just an S_α proxy
- FAIL → d(n) may be mediated by S_α

### P4: Stability of g Coefficient

**Metric**: |Δg| / |g_M2| (percent change from M2 to M7)
**Threshold**:
- < 20% → STABLE
- 20-50% → PARTIAL MEDIATION
- > 50% → COLLAPSE

---

## Pre-Registered Secondary Tests

### S1: AIC Comparison

Compare AIC across models:
- M2 vs M3: Does deformation alone explain as well as d(n)?
- M2 vs M5: Does adding deformation to M2 improve fit?
- M2 vs M6: Does adding S_α to M2 improve fit?

**Threshold**: ΔAIC > 2 is meaningful

### S2: Proxy Significance When d(n) Excluded

| Comparison | Question |
|------------|----------|
| M3 vs M1 | Is proxy_deform significant alone? |
| M4 vs M1 | Is proxy_Salpha significant alone? |

### S3: Proxy Significance When d(n) Included

| Comparison | Question |
|------------|----------|
| M5 vs M2 | Is proxy_deform significant with d(n)? |
| M6 vs M2 | Is proxy_Salpha significant with d(n)? |

If proxy is significant alone (S2) but not with d(n) (S3), this suggests d(n) captures the proxy's variance.

---

## Decision Matrix

| P1 | P2 | P3 | P4 | Verdict | Interpretation |
|----|----|----|-----|---------|----------------|
| ✓ | ✓ | ✓ | STABLE | **ROBUST** | d(n) independent of both proxies |
| ✓ | ✓ | ✓ | PARTIAL | **MEDIATION** | Proxies partially explain d(n) |
| ✓ | ✓ | ✗ | — | **S_α MEDIATION** | d(n) proxies S_α |
| ✓ | ✗ | ✓ | — | **DEFORM COLLAPSE** | d(n) proxies deformation |
| ✓ | ✗ | ✗ | — | **COLLAPSE** | d(n) is confounded |
| ✗ | — | — | — | **BASELINE FAIL** | V7.4 not replicated |

---

## Covariates

### Fixed Covariates (all models)

| Covariate | Definition | Source |
|-----------|------------|--------|
| Z/√Q | Geiger-Nuttall term | V7.4 dataset |
| I(H1) | Hindrance class 1 indicator | V7.4 dataset |
| I(H2) | Hindrance class 2 indicator | V7.4 dataset |

### Test Covariates

| Covariate | Definition | Source |
|-----------|------------|--------|
| d(n) | M-topology coordination distance | V7.4: n_A column |
| proxy_deform | |N-126|×|Z-82|/1000 | Derived from Z, A |
| proxy_Salpha | Royer log₁₀(P_α) | Royer 2010 formula |

---

## Random Seed

For any CV or bootstrap: seed = 42 (inherited from V7.5)

---

## Expected Outcomes

Based on V7.7 prefactor hypothesis:

1. **M2**: g = -0.31, p = 0.006 (replicate V7.4)
2. **M3**: proxy_deform significant (expected, correlates with A)
3. **M4**: proxy_Salpha may be significant (captures preformation)
4. **M5**: g remains significant, proxy_deform may become non-significant
5. **M6**: g remains significant; if mechanism is S_α, proxy_Salpha may absorb some g
6. **M7**: Key test — if g survives both proxies, strong evidence for independent d(n) effect

---

## Signature

Pre-registered: 2026-01-31
Analysis run: 2026-01-31

