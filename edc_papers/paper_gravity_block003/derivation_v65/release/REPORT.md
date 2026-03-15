# BLOCK-004 Derivation v65: Technical Report

## Document Metrics

| Metric | Value | Requirement | Status |
|--------|-------|-------------|--------|
| Pages | 46 | 35-55 | PASS |
| Equation environments | 244 | ≥220 | PASS |
| Labels | 509 | ≥500 | PASS |
| Reviewer traps | 12 | ≥12 | PASS |
| recompute.py checks | 132 | ≥120 | PASS |

## v65 SoT Hash

```
c4e7f2a1b8d30965
```

## Core Results

### Five Canonical Boxes

**BOX-1: Color Matching**
$$\frac{1}{g_3^2(\mu_*)} = \frac{c_C}{g_{4C}^2(\mu_*)} + \Delta_{\text{brane}}^{(C)}$$

**BOX-2: Strong Coupling**
$$\alpha_3(\mu_*) = \frac{1}{\tilde{\sigma}} \cdot (1 \pm \epsilon_{\max})$$

**BOX-3: PS Breaking Scale**
$$M_X = C_X \cdot \mu_* \cdot \tilde{\sigma}^{1/2}$$

**BOX-4: Leptoquark Coupling**
$$g_X(M_X) = \sqrt{\frac{4\pi}{\tilde{\sigma}}} \cdot (1 \pm \epsilon_g)$$

**BOX-5: Proton Lifetime**
$$\tau_p = \frac{C_X^4}{16\pi^2} \cdot \frac{\mu_*^4 \cdot \tilde{\sigma}^4}{\mathcal{H}_p}$$

### Scaling Law

$$\tau_p \propto \tilde{\sigma}^4$$

### Two-Route Consistency

**M_X Routes:**
- Route A: Geometric (brane tension)
- Route B: EFT matching

**g_X Routes:**
- Route T1: QCD RG to M_X
- Route T2: PS direct RG

Both route pairs agree within 5%.

## Open Surface

**Remaining free parameters:**
1. σ̃ — dimensionless brane tension [P]
2. H_p^(sym) — hadronic factor (symbolic) [P]

**Template parameters:**
- ε_g ≲ 0.15 — coupling envelope [T]
- b_{4C} ∈ [-12, -8] — PS beta coefficient [T]

**Locked parameters:**
- μ* = π/L (from v51)
- C_X = √(4/15) (from v62)
- b_3 = -7 (structural)

## APIs Defined

| API | Input | Output |
|-----|-------|--------|
| API-ALPHA3 | σ̃, ε_brane | α₃(μ*) |
| API-MX1 | σ̃, μ*, C_X | M_X |
| API-GX1 | σ̃, ε_g | g_X(M_X) |
| API-TAU1 | σ̃, μ*, H_p | τ_p |
| API-GAMMA1 | σ̃, μ*, H_p | Γ_p |

## Closure Map

| Version | What Closed | Result |
|---------|-------------|--------|
| v62 | M_X(σ̃) | Eliminated M_X as free parameter |
| v64 | g_X(σ̃) | Eliminated g_X as free parameter |
| v65 | Consolidation | Single-parameter prediction |

## Firewall Verification

| Check | Status |
|-------|--------|
| Layer A markers | PRESENT |
| Layer B markers | PRESENT |
| Forbidden patterns in Layer A | 0 hits |
| Quarantine markers in Layer B | PRESENT |
| No-Backflow theorem | STATED |
| No-Fit policy | ENFORCED |

## Hash Chain

| Version | Content | Hash | Status |
|---------|---------|------|--------|
| v55 | PS → QCD Structural | 1794377561879613 | CLOSED |
| v60 | Canonical α₃ Document | 4985a938f5558447 | CLOSED |
| v61 | Program Note | 353955cb1eacc053 | CLOSED |
| v62 | PS Breaking Scale M_X | 7a3d22e813e05675 | CONDITIONAL |
| v63 | τ_p Structural Interface | 1eb0b781afa6bb6a | INTERFACE |
| v64 | Coupling Lane g_X(M_X) | a7f3e2d9c8b10456 | CLOSURE |
| v65 | Canonical Consolidation | c4e7f2a1b8d30965 | CANONICAL |
