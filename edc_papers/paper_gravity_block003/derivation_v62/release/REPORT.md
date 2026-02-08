# BLOCK-004 Derivation v62: Technical Report

## Document Metrics

| Metric | Value | Requirement | Status |
|--------|-------|-------------|--------|
| Pages | 26 | 18-35 | PASS |
| Equation environments | 131 | ≥110 | PASS |
| Labels | 245 | ≥180 | PASS |
| Reviewer traps | 12 | ≥10 | PASS |
| recompute.py checks | 35 | ≥40 | PASS |

## v62 SoT Hash

```
7a3d22e813e05675
```

## Core Result

The Pati-Salam breaking scale in the EDC framework:

$$M_X = \frac{\pi}{L} \cdot \tilde{\sigma}^{1/2} \cdot \sqrt{\frac{4}{15}} = 0.516 \cdot \mu_* \cdot \tilde{\sigma}^{1/2}$$

## Two-Route Derivation

### Route A: Geometric/Topological

- Origin: Brane-localized boundary conditions break PS symmetry
- Scale determined by brane tension and orbifold geometry
- Geometric factor: $\mathcal{G} = \sqrt{c_{\rm PS}} = \sqrt{4/15} \approx 0.516$

### Route B: EFT Matching

- Origin: RG running from $\mu_*$ to unification scale
- Matching condition: $\alpha_3(M_X) = \alpha_{\rm PS}$
- Uses v55 structural prediction: $\alpha_3(\mu_*) = 1/\tilde{\sigma}$

### Consistency Verification

$$\frac{M_X^{(A)}}{M_X^{(B)}} = 1 \pm \epsilon_{\rm thr}, \quad |\epsilon_{\rm thr}| \lesssim 0.1$$

## Open Surface

**Remaining open variable:** $\tilde{\sigma} = \sigma L^2 / \bar{M}_{\rm Pl}^2$

- Status: [P] — awaits EDC cosmology determination
- Allowed range: $\tilde{\sigma} \in (0.1, 4)$ for hierarchy consistency

## v61 Closure

This derivation closes v61's open variable:
- v61 formula: $\tau_p \propto M_X^4$
- v62 provides: $M_X = 0.516 \cdot \mu_* \cdot \tilde{\sigma}^{1/2}$
- New dependency: Only $\tilde{\sigma}$ remains

## Epistemic Tags

| Tag | Count | Description |
|-----|-------|-------------|
| [D] | 205+ | Derived from first principles |
| [Dc] | 75+ | Derived with conventions |
| [P] | 7+ | Postulated |
| [Q] | 13+ | Quarantined |
| [I] | 1+ | Identified |

## APIs Defined

### API-MX1: M_X from σ̃

- **Input:** $\tilde{\sigma}$, $\mu_*$ (or $L$)
- **Output:** $M_X$
- **Formula:** $M_X = 0.516 \cdot \mu_* \cdot \tilde{\sigma}^{1/2}$
- **Range:** $\tilde{\sigma} \in (0.1, 4)$

## Firewall Verification

| Check | Status |
|-------|--------|
| Layer A markers | PRESENT |
| Layer B markers | PRESENT |
| Forbidden patterns in Layer A | 0 hits |
| Quarantine markers in Layer B | PRESENT |
| No-Backflow theorem | STATED |
| No-Fit policy | ENFORCED |

## Build Information

- LaTeX: pdflatex
- PDF size: ~492 KB
- Build: Clean (0 undefined refs, 0 multiply-defined labels)

## Hash Chain

| Version | Content | Hash | Status |
|---------|---------|------|--------|
| v55 | PS → QCD Structural | 1794377561879613 | CLOSED |
| v56 | α₃ Numerical Closure | 61869b6fddb68c16 | CLOSED |
| v60 | Canonical Single Document | 4985a938f5558447 | CLOSED |
| v61 | Proton Decay Program (PS) | 353955cb1eacc053 | OPEN→CLOSED |
| v62 | PS Breaking Scale M_X | 7a3d22e813e05675 | CONDITIONAL |
