# BLOCK-004 Derivation v64: Release Notes

## Proton Decay Coupling Lane g_X(M_X)

### Version: v64
### Date: 2026-02-08
### Status: COUPLING LANE CLOSED

---

## What is CLOSED

### Core Derivation

1. **Coupling Identity**
   - $g_X := g_{4C}(M_X)$ (SU(4)$_C$ at PS breaking scale)
   - Trace normalization consistent with v55
   - Generator decomposition explicit

2. **Route T1: QCD RG**
   - Start: $g_3(\mu_*) = \sqrt{4\pi/\tilde{\sigma}}$
   - Run: $\mu_* \to M_X$ with $b_3 = -7$
   - Match: threshold correction $\delta_{\text{thr}}$

3. **Route T2: PS Direct RG**
   - Start: $g_{4C}(\mu_*) \approx g_3(\mu_*)$
   - Run: with template $b_{4C} \in [-12, -8]$
   - Direct evolution in unbroken PS regime

4. **Consistency Theorem**
   - $|g_X^{(T1)}/g_X^{(T2)} - 1| \leq 0.05$
   - Two routes agree within 5%

5. **Final g_X Interface**
   - $g_X(M_X) = \sqrt{4\pi/\tilde{\sigma}} \cdot (1 \pm \epsilon_g)$
   - Envelope: $\epsilon_g \lesssim 0.15$

6. **τ_p Closure**
   - $\tau_p = (C_X^4/16\pi^2) \cdot \mu_*^4 \tilde{\sigma}^4 / \mathcal{H}_p$
   - **Scaling:** $\tau_p \propto \tilde{\sigma}^4$

7. **APIs Defined**
   - API-GX1: Coupling from σ̃
   - API-GX2: Fourth power from σ̃
   - API-TAU3: Lifetime from σ̃ (coupling absorbed)
   - API-GAMMA1: Decay rate from σ̃

---

## What is OPEN

### Remaining Parameters

| Parameter | Description | Status |
|-----------|-------------|--------|
| $\tilde{\sigma}$ | Dimensionless brane tension | [P] |
| $\mathcal{H}_p$ | Hadronic factor (symbolic) | [P] |

### Template Parameters

| Parameter | Range | Status |
|-----------|-------|--------|
| $\epsilon_g$ | ≤ 0.15 | [T] |
| $b_{4C}$ | [-12, -8] | [T] |

### Closure Condition

Numeric predictions require:
1. $\tilde{\sigma}$ from EDC cosmology
2. $\mathcal{H}_p$ from lattice QCD or EDC-QCD matching

---

## Layer Architecture

- **Layer A (Hash-Locked):** Coupling identity, matching, RG, consistency
- **Layer B (Quarantined):** Illustrative sweeps

**No backflow:** $\mathcal{L}_B \cap \mathcal{L}_A = \emptyset$

---

## Release Bundle

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification (104 checks) |
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

All 104 checks must pass.

---

## Relation to v55/v60/v62/v63

- **v55:** PS → QCD matching ($\alpha_3(\mu_*) = 1/\tilde{\sigma}$)
- **v60:** Canonical $\alpha_3$ document
- **v62:** $M_X(\tilde{\sigma})$ derivation
- **v63:** $\tau_p$ structural interface (with $g_X$ as dependency)
- **v64:** $g_X(M_X)$ closure (this document)

The chain: v55 → v60 → v62 → v63 → v64 closes the proton decay prediction.

---

**v64 SoT Hash:** `a7f3e2d9c8b10456`
**Parent Hash (v63):** `1eb0b781afa6bb6a`
**Parent Hash (v62):** `7a3d22e813e05675`
**Parent Hash (v60):** `4985a938f5558447`
**Parent Hash (v55):** `1794377561879613`
