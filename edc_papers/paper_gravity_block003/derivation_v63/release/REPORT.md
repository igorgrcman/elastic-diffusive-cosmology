# BLOCK-004 Derivation v63: Technical Report

## Document Metrics

| Metric | Value | Requirement | Status |
|--------|-------|-------------|--------|
| Pages | 27 | 18-35 | PASS |
| Equation environments | 125 | ≥120 | PASS |
| Labels | 257 | ≥200 | PASS |
| Reviewer traps | 12 | ≥10 | PASS |
| recompute.py checks | 52 | ≥50 | PASS |

## v63 SoT Hash

```
1eb0b781afa6bb6a
```

## Core Result

The proton lifetime structural interface:

$$\tau_p(\tilde{\sigma}) = \frac{C_X^4}{16\pi^2} \cdot \frac{\mu_*^4 \cdot \tilde{\sigma}^4}{\mathcal{H}_p^{(\text{sym})}}$$

### Scaling Law

$$\tau_p \propto \tilde{\sigma}^4$$

The extra $\tilde{\sigma}^2$ factor (beyond $M_X^4 \propto \tilde{\sigma}^2$) comes from
$g_X^4 \propto \tilde{\sigma}^{-2}$ via the v55 relation.

## Operator Catalog

| Operator | Structure | Selection Rule |
|----------|-----------|----------------|
| $\mathcal{O}_1$ | LLLL | $\Delta B = -1$, $\Delta L = +1$ |
| $\mathcal{O}_2$ | RRRR | $\Delta B = -1$, $\Delta L = +1$ |
| $\mathcal{O}_3$ | LLRR | $\Delta B = -1$, $\Delta L = +1$ |
| $\mathcal{O}_4$ | RRLL | $\Delta B = -1$, $\Delta L = +1$ |
| $\mathcal{O}_5$ | LRLR | $\Delta B = -1$, $\Delta L = +1$ |
| $\mathcal{O}_6$ | RLRL | $\Delta B = -1$, $\Delta L = +1$ |

## Open Surface

**Remaining free parameters:**
1. $\tilde{\sigma}$ — dimensionless brane tension [P]
2. $\mathcal{H}_p^{(\text{sym})}$ — hadronic factor (symbolic) [P]

**Locked parameters:**
- $\mu_* = \pi/L$ (from v51)
- $C_X = \sqrt{4/15}$ (from v62)
- $g_X = \sqrt{4\pi/\tilde{\sigma}}$ (from v55)

## v61 Closure

| Aspect | Before v62/v63 | After v62/v63 |
|--------|----------------|---------------|
| $M_X$ | Free parameter | $M_X(\tilde{\sigma})$ |
| $\tau_p$ | $\tau_p(M_X, g_X, \ldots)$ | $\tau_p(\tilde{\sigma})$ |
| Free parameters | 2+ | 1 (+ symbolic $\mathcal{H}_p$) |
| Scaling | Unknown | $\tau_p \propto \tilde{\sigma}^4$ |

## APIs Defined

### API-TAU1
- **Input:** $\tilde{\sigma}$, $\mu_*$, $\mathcal{H}_p$
- **Output:** $\tau_p$
- **Formula:** $\tau_p = (1/225\pi^2) \cdot \mu_*^4 \tilde{\sigma}^4 / \mathcal{H}_p$

### API-TAU2
- **Input:** Same as API-TAU1
- **Output:** $\Gamma_p$
- **Formula:** $\Gamma_p = 225\pi^2 \cdot \mathcal{H}_p / (\mu_*^4 \tilde{\sigma}^4)$

## Hash Chain

| Version | Content | Hash | Status |
|---------|---------|------|--------|
| v61 | Proton Decay Program (PS) | 353955cb1eacc053 | OPEN→CLOSED |
| v62 | PS Breaking Scale M_X | 7a3d22e813e05675 | CONDITIONAL |
| v63 | τ_p Structural Interface | 1eb0b781afa6bb6a | INTERFACE |

## Firewall Verification

| Check | Status |
|-------|--------|
| Layer A markers | PRESENT |
| Layer B markers | PRESENT |
| Forbidden patterns in Layer A | 0 hits |
| Quarantine markers in Layer B | PRESENT |
| No-Backflow theorem | STATED |
| No-Fit policy | ENFORCED |
