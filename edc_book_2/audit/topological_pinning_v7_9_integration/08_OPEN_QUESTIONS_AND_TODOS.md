# V7.9 OPEN QUESTIONS AND TODOS

**Created**: 2026-01-31
**Purpose**: Harmonize with V7.7/V7.8 kingpins; sign-safe language constraints

---

## Harmonized Kingpin Status

### From V7.8 (Current)

| ID | Kingpin | V7.8 Status | Priority | V7.9 Note |
|----|---------|-------------|----------|-----------|
| K1 | True β₂ deformation | Partially resolved | MEDIUM | Shell proxy absorbed; FRDM β₂ would strengthen |
| K2 | Experimental S_α | Open | HIGH | Would definitively test prefactor hypothesis |
| K3 | Pairing residuals | Open | MEDIUM | Not tested |
| K4 | Shell proximity | Addressed | LOW | In deformation proxy |
| K5 | Isomer comparison | Open | MEDIUM | Would test configuration dependence |
| K6 | T-dependence | N/A | LOW | Nuclear rates T-independent |
| K7 | α-anisotropy | Open | MEDIUM | Would test M1 domain mechanism |
| K8 | Charge radii | Open | LOW | Would test M6 core-mantle |
| K9 | Superheavy | Open | MEDIUM | Data limited (Z > 100) |
| K10 | Causation | Open | HIGH | Theoretical development needed |
| K11 | Alternative S_α | Open | HIGH | Buck model, spectroscopic factors |
| K12 | Collinearity | Open | MEDIUM | VIF analysis, ridge regression |

### Priority Summary

| Priority | Kingpins | Action |
|----------|----------|--------|
| **HIGH** | K2, K10, K11 | Block [Der] upgrade; need experimental/theoretical work |
| **MEDIUM** | K3, K5, K7, K9, K12 | Would strengthen claim; not blocking |
| **LOW** | K4, K6, K8 | Addressed or inapplicable |

---

## Path to [Der] Upgrade

### Completed (4/7)

1. ✓ Robust regression (V7.5, V7.8)
2. ✓ Permutation test (V7.5)
3. ✓ Cross-validation (V7.5)
4. ✓ Deformation control (V7.8)

### Remaining (3/7)

5. ⬜ Independent S_α confirmation (K2/K11)
6. ⬜ Causal mechanism demonstration (K10)
7. ⬜ Superheavy validation (K9)

**Current status**: Strong [P], approaching [I]

---

## Sign-Safe Language Constraints for Book Narrative

### MUST Use

| Phrase | Reason |
|--------|--------|
| "correlates with" | Established correlation, not causation |
| "consistent with prefactor/S_α channel" | Sign interpretation |
| "robust to deformation control" | V7.8 result |
| "absorbs deformation variance" | Proxy becomes non-significant |
| "captures variance beyond" | Neutral statement |
| "coordination distance d(n)" | Correct terminology |
| "higher d(n) → shorter t₁/₂" | Correct sign direction |

### MUST AVOID

| Phrase | Problem | Alternative |
|--------|---------|-------------|
| "causes faster decay" | Overclaim | "correlates with faster decay" |
| "proves topological mechanism" | Overclaim | "consistent with mechanism" |
| "frustration impedes tunneling" | Wrong sign | "frustration enhances preformation" |
| "S_α mechanism confirmed" | Overclaim | "consistent with S_α channel" |
| "deformation irrelevant" | Misleading | "absorbed by d(n)" |
| "predicts half-life" | Overclaim | "correlates with half-life" |

### Epistemic Tag Usage

| Tag | Use For | Example |
|-----|---------|---------|
| [Der] | Regression results, numerics | "g = -1.64 ± 0.14 [Der]" |
| [I] | Interpretation supported by data | "d(n) captures topological info [I]" |
| [P] | Proposed mechanism | "frustration → S_α enhancement [P]" |
| [Open] | Unresolved questions | "Causation not established [Open]" |
| [BL:source] | External data source | "[BL:NuDat3]" |

---

## TODOs for Book2 Integration

### If V7.9 Content Goes to Book2

1. **Do not copy verbatim** — derivation style differs from book style
2. **Use paragraph variants** from V7.8/09_BOOK2_PARAGRAPH_V7_8.md
3. **Check abstract numbers** — wrapper says R² = 0.9941, V7.8 gives 0.9812
4. **Maintain epistemic tags** — may need margin notes or footnotes in book
5. **Cross-reference audit** — cite audit package for full provenance

### Specific Book2 Actions

| Section | Action | Note |
|---------|--------|------|
| Abstract | Verify R² = 0.9941 vs V7.8 | May need update |
| Radioactivity chapter | Use Variant B or C from V7.8/09 | Sign-safe |
| Falsification section | Update with V7.8 status | 4/7 complete |
| Open questions | Sync with V7.8/10 | New K11, K12 |

---

## Questions for Future Sessions

1. **R² discrepancy**: Abstract claims 0.9941, V7.8 M7 gives 0.9812. Where does 0.9941 come from?

2. **Effect size interpretation**: V7.4 g = -0.31, V7.8 g = -1.64. Different scaling or different model? Document clearly.

3. **Superheavy extension**: What data exists for Z > 100? Md, No, Lr isotopes?

4. **Theoretical pathway**: How might coordination affect preformation probability mechanistically?

---

## Version History

- 2026-01-31: V7.9 initial creation, harmonized with V7.8

