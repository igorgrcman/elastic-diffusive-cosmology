# BLOCK-004 Derivation v63: Release Notes

## Proton Decay τ_p Structural Interface

### Version: v63
### Date: 2026-02-08
### Status: STRUCTURAL INTERFACE

---

## What is CLOSED

### Core Derivation

1. **Operator Catalog**
   - PS leptoquark-induced dimension-6 operators
   - 6 independent $\Delta B = 1$ structures
   - Selection rules: $\Delta B = -1$, $\Delta L = +1$
   - Dominant channels: $p \to e^+ \pi^0$, $p \to \bar{\nu} \pi^+$

2. **Decay Rate Structure**
   - $\Gamma_p \sim g_X^4 / M_X^4 \cdot \mathcal{H}_p$
   - Hadronic factor symbolic (not fitted)
   - Phase space factors included

3. **M_X Import from v62**
   - $M_X = C_X \cdot \mu_* \cdot \tilde{\sigma}^{1/2}$
   - $C_X = \sqrt{4/15} \approx 0.516$
   - Fourth power: $M_X^4 = C_X^4 \mu_*^4 \tilde{\sigma}^2$

4. **Coupling from v55**
   - $g_X = g_{\text{PS}} = \sqrt{4\pi/\tilde{\sigma}}$
   - Fourth power: $g_X^4 = 16\pi^2 / \tilde{\sigma}^2$

5. **Final τ_p Interface**
   - $\tau_p = (C_X^4/16\pi^2) \cdot \mu_*^4 \tilde{\sigma}^4 / \mathcal{H}_p$
   - **Scaling:** $\tau_p \propto \tilde{\sigma}^4$

6. **v61 Closure**
   - Open variable $M_X$ resolved via v62
   - Dependency reduced: $\tau_p(M_X, g_X, \ldots) \to \tau_p(\tilde{\sigma})$

7. **APIs Defined**
   - API-TAU1: Proton lifetime from σ̃
   - API-TAU2: Decay rate from σ̃

---

## What is OPEN

### Remaining Parameters

| Parameter | Description | Status |
|-----------|-------------|--------|
| $\tilde{\sigma}$ | Dimensionless brane tension | [P] |
| $\mathcal{H}_p$ | Hadronic factor (symbolic) | [P] |

### Closure Condition

Numeric predictions require:
1. $\tilde{\sigma}$ from EDC cosmology
2. $\mathcal{H}_p$ from lattice QCD or EDC-QCD matching

---

## Layer Architecture

- **Layer A (Hash-Locked):** Structural derivation, no experimental anchors
- **Layer B (Quarantined):** Parameter sweep, experimental comparison

**No backflow:** $\mathcal{L}_B \cap \mathcal{L}_A = \emptyset$

---

## Release Bundle

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification (52 checks) |
| `README.md` | Overview |
| `REPORT.md` | Technical details |
| `ACCEPTANCE.md` | Acceptance criteria |
| `RELEASE_NOTES.md` | This file |
| `release/` | Export bundle |

---

## Verification

```bash
python3 recompute.py
```

All 52 checks must pass.

---

## Relation to v61/v62

- **v61:** Proton decay program note with $M_X$ as open variable
- **v62:** $M_X(\tilde{\sigma})$ two-route derivation
- **v63:** $\tau_p(\tilde{\sigma})$ structural interface (this document)

The chain: v61 → v62 → v63 closes the proton decay prediction.

---

**v63 SoT Hash:** `1eb0b781afa6bb6a`
**Parent Hash (v62):** `7a3d22e813e05675`
**Parent Hash (v61):** `353955cb1eacc053`
