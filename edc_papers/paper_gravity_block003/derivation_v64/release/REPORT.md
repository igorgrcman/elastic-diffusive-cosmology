# BLOCK-004 Derivation v64: Technical Report

## Document Metrics

| Metric | Value | Requirement | Status |
|--------|-------|-------------|--------|
| Pages | 29 | 20-40 | PASS |
| Equation environments | 152 | ≥140 | PASS |
| Labels | 279 | ≥260 | PASS |
| Reviewer traps | 12 | ≥10 | PASS |
| recompute.py checks | 104 | ≥60 | PASS |

## v64 SoT Hash

```
a7f3e2d9c8b10456
```

## Core Results

### Coupling Identity

$$g_X \equiv g_{4C}(M_X)$$

The proton decay coupling is the SU(4)$_C$ gauge coupling at the PS breaking scale.

### Two-Route Derivation

**Route T1 (QCD RG):**
- Start from $g_3(\mu_*) = \sqrt{4\pi/\tilde{\sigma}}$ (v55)
- Run to $M_X$ using $b_3 = -7$
- Apply threshold matching

**Route T2 (PS Direct RG):**
- Start from $g_{4C}(\mu_*) \approx g_3(\mu_*)$
- Run to $M_X$ using $b_{4C} \in [-12, -8]$ (template)

### Consistency Theorem

$$\left|\frac{g_X^{(T1)}}{g_X^{(T2)}} - 1\right| \leq 0.05$$

### Final g_X Interface

$$g_X(M_X) = \sqrt{\frac{4\pi}{\tilde{\sigma}}} \cdot (1 \pm \epsilon_g)$$

with $\epsilon_g \lesssim 0.15$.

### Final τ_p Interface

$$\tau_p(\tilde{\sigma}) = \frac{1}{225\pi^2} \cdot \frac{\mu_*^4 \cdot \tilde{\sigma}^4}{\mathcal{H}_p}$$

### Scaling Law

$$\tau_p \propto \tilde{\sigma}^4$$

## Open Surface

**Remaining free parameters:**
1. $\tilde{\sigma}$ — dimensionless brane tension [P]
2. $\mathcal{H}_p^{(\text{sym})}$ — hadronic factor (symbolic) [P]

**Template parameters:**
- $\epsilon_g \lesssim 0.15$ — coupling envelope [T]
- $b_{4C} \in [-12, -8]$ — PS beta coefficient [T]

**Locked parameters:**
- $\mu_* = \pi/L$ (from v51)
- $C_X = \sqrt{4/15}$ (from v62)
- $b_3 = -7$ (QCD structural)
- $g_X = \sqrt{4\pi/\tilde{\sigma}} \cdot (1 \pm \epsilon_g)$ (absorbed)

## v63 Closure Map

| Aspect | Before v64 | After v64 |
|--------|------------|-----------|
| $g_X$ | Dependency | $g_X(\tilde{\sigma})$ absorbed |
| $\tau_p$ | $\tau_p(M_X, g_X, \ldots)$ | $\tau_p(\tilde{\sigma})$ |
| Free parameters | Multiple | 1 (+ symbolic $\mathcal{H}_p$) |

## APIs Defined

### API-GX1
- **Input:** $\tilde{\sigma}$, corrections
- **Output:** $g_X(M_X)$
- **Formula:** $g_X = \sqrt{4\pi/\tilde{\sigma}} \cdot (1 + \text{corrections})$

### API-GX2
- **Input:** $\tilde{\sigma}$
- **Output:** $g_X^4$
- **Formula:** $g_X^4 = 16\pi^2/\tilde{\sigma}^2 \cdot (1 \pm 4\epsilon_g)$

### API-TAU3
- **Input:** $\tilde{\sigma}$, $\mu_*$, $\mathcal{H}_p$
- **Output:** $\tau_p$
- **Formula:** $\tau_p = (1/225\pi^2) \cdot \mu_*^4 \tilde{\sigma}^4 / \mathcal{H}_p$

### API-GAMMA1
- **Input:** Same as API-TAU3
- **Output:** $\Gamma_p$
- **Formula:** $\Gamma_p = 225\pi^2 \cdot \mathcal{H}_p / (\mu_*^4 \tilde{\sigma}^4)$

## Hash Chain

| Version | Content | Hash | Status |
|---------|---------|------|--------|
| v55 | PS → QCD Structural | 1794377561879613 | CLOSED |
| v60 | Canonical α₃ Document | 4985a938f5558447 | CLOSED |
| v62 | PS Breaking Scale M_X | 7a3d22e813e05675 | CONDITIONAL |
| v63 | τ_p Structural Interface | 1eb0b781afa6bb6a | INTERFACE |
| v64 | Coupling Lane g_X(M_X) | a7f3e2d9c8b10456 | CLOSURE |

## Firewall Verification

| Check | Status |
|-------|--------|
| Layer A markers | PRESENT |
| Layer B markers | PRESENT |
| Forbidden patterns in Layer A | 0 hits |
| Quarantine markers in Layer B | PRESENT |
| No-Backflow theorem | STATED |
| No-Fit policy | ENFORCED |
