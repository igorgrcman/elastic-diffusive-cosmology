# BLOCK-004 Derivation v62: Release Notes

## PS Breaking Scale M_X from EDC (Two-Route)

### Version: v62
### Date: 2026-02-08
### Status: CONDITIONAL CLOSURE

---

## What is CLOSED

### Core Derivation

1. **M_X Definition**
   - PS breaking scale: $SU(4)_C \times SU(2)_L \times SU(2)_R \to SU(3)_c \times SU(2)_L \times U(1)_Y$
   - Heavy gauge boson identification (leptoquarks)
   - Scale parameter from EDC internal quantities

2. **Route A: Geometric/Topological**
   - Brane-localized boundary condition breaking
   - Geometric factor $\mathcal{G} = \sqrt{4/15} \approx 0.516$
   - Formula: $M_X^{(A)} = \mu_* \cdot \tilde{\sigma}^{1/2} \cdot \mathcal{G}$

3. **Route B: EFT Matching**
   - RG running from reference scale to unification
   - Uses v55 prediction: $\alpha_3(\mu_*) = 1/\tilde{\sigma}$
   - Formula: $M_X^{(B)} = \mu_* \cdot \exp(2\pi\tilde{\sigma}(1-1/\kappa_g)/b_0)$

4. **Two-Route Consistency**
   - Ratio: $M_X^{(A)}/M_X^{(B)} = 1 \pm 0.1$
   - Threshold bound: $|\epsilon_{\rm thr}| \lesssim 0.1$

5. **Boxed Final Form**
   - $M_X = 0.516 \cdot \mu_* \cdot \tilde{\sigma}^{1/2}$
   - Dimensionally consistent
   - Expressed in EDC parameters

6. **v61 Closure**
   - Open variable $M_X$ resolved
   - Dependency reduced from 2 to 1 parameter

7. **API-MX1**
   - M_X calculator from $\tilde{\sigma}$

8. **Firewall Structure**
   - No-Backflow theorem
   - No-Fit policy
   - Forbidden Gate specification
   - 12 reviewer traps

---

## What is OPEN

### Remaining Free Parameter

| Parameter | Description | Source |
|-----------|-------------|--------|
| $\tilde{\sigma}$ | Dimensionless brane tension | EDC cosmology/field equations |

### Closure Condition

This derivation becomes FULLY CLOSED when:
1. $\tilde{\sigma}$ is derived from EDC cosmology (primary condition)
2. Allowed range: $\tilde{\sigma} \in (0.1, 4)$ for hierarchy consistency

---

## Layer Architecture

- **Layer A (Hash-Locked):** Structural derivations, group theory, RG coefficients
- **Layer B (Quarantined):** Experimental comparison hooks (isolated)

**No backflow:** $\mathcal{L}_B \cap \mathcal{L}_A = \emptyset$

---

## Release Bundle Contents

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (canonical) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script |
| `README.md` | Overview and usage |
| `REPORT.md` | Technical details |
| `ACCEPTANCE.md` | Acceptance criteria |
| `RELEASE_NOTES.md` | This file |
| `release/` | Export bundle |

---

## Verification

Run `python3 recompute.py` to verify:
- All structural checks pass
- Forbidden patterns absent from Layer A
- APIs defined
- Traps counted
- Document metrics met

---

## Relation to v61

v62 closes v61's open variable:
- **v61:** Proton lifetime formula with $M_X$ as free parameter
- **v62:** Provides $M_X = f(\tilde{\sigma}, \mu_*)$
- **Result:** Proton lifetime now depends only on $\tilde{\sigma}$

---

## Known Limitations

1. $\tilde{\sigma}$ value undetermined (requires EDC cosmology)
2. Threshold corrections bounded but not computed exactly
3. Higher-loop RG effects subdominant but present
4. Flavor structure not addressed (trivial mixing assumed)

---

## Next Steps

1. Derive $\tilde{\sigma}$ from EDC cosmology/field equations
2. Compute proton lifetime using v61 + v62
3. Compare with Layer B experimental bounds
4. Close program note fully

---

**Document Hash**: v62 SoT
**v62 SoT Hash**: `7a3d22e813e05675`
**Parent Hash (v61)**: `353955cb1eacc053`
