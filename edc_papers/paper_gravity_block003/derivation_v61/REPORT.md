# BLOCK-004 Derivation v61: Technical Report
## Proton Decay Program Note (PS)

### Document Summary

| Property | Value |
|----------|-------|
| Version | v61 |
| Title | Proton Decay Program Note (PS) |
| Status | PROGRAM NOTE — OPEN |
| Layer A | Structural derivations (CLOSED) |
| Layer B | Comparison framework (DEFINED) |
| Condition | OPEN until M_X derived |

### Scope

This derivation establishes the structural framework for proton decay within
the Pati-Salam (PS) gauge unification scenario. It provides:

1. Complete group-theoretic structure of PS proton decay
2. Leptoquark gauge boson identification and quantum numbers
3. Dimension-6 baryon-violating operator catalog
4. Symbolic proton lifetime formula with explicit parameter dependence
5. API specifications for future EDC predictions

### Layer A Content (Hash-Locked)

#### Group Theory
- PS gauge group: $SU(4)_C \times SU(2)_L \times SU(2)_R$
- Fermion representations: $(4,2,1)_L + (4,1,2)_R$
- Generator normalization: $\text{Tr}(T^A T^B) = \frac{1}{2}\delta^{AB}$
- Symmetry breaking chain: PS → SM → QCD×QED

#### Leptoquark Sector
- Gauge boson decomposition: $15 \to 8_0 + 3_{-4/3} + \bar{3}_{4/3} + 1_0$
- X boson charges: $Q_X = \pm 4/3$, color triplet
- Coupling to fermions: derived from PS gauge structure

#### Effective Operators
- Dimension-6 operators: 4 independent structures
- Chirality: LL, RR, LR contributions
- Color contraction: antisymmetric $\epsilon^{\alpha\beta\gamma}$

#### Lifetime Formula
$$\tau_p = \frac{32\pi M_X^4}{g_{PS}^4 |C_{CG}|^2 |\alpha_H|^2} \cdot \frac{m_p^3}{(m_p^2 - m_\pi^2)^2}$$

### Layer B Content (Quarantined)

- Comparison protocol (structural only)
- Hadronic matrix element input structure
- Experimental bounds format (no numeric values)

### API Specifications

#### API-PD1: Proton Lifetime Calculator
- **Inputs**: $M_X$, $g_{PS}$, $\alpha_H$, $C_{CG}$
- **Output**: $\tau_p$ (symbolic)
- **Status**: Structural formula derived

#### API-PD2: Operator Coefficients
- **Inputs**: $g_{PS}$, $M_X$, chirality specification
- **Output**: Wilson coefficients $C_i$
- **Status**: Form derived; group factors depend on Higgs sector

### Required Future Derivations

| Parameter | Required From | Priority |
|-----------|---------------|----------|
| $M_X$ | EDC PS breaking scale | HIGH |
| $\alpha_H$ | Hadronic physics (Layer B) | MEDIUM |
| Threshold corrections | Matching at $M_X$ | MEDIUM |
| Flavor structure | Generation mixing | LOW |

### Firewall Verification

| Check | Result |
|-------|--------|
| No numeric $\tau_p$ in Layer A | ✓ PASS |
| No PDG bounds in Layer A | ✓ PASS |
| $M_X$ not fitted | ✓ PASS |
| $\alpha_H$ symbolic in Layer A | ✓ PASS |
| No experiment names in Layer A | ✓ PASS |

### Reviewer Traps

12 traps defined covering:
- Numeric lifetime values
- PDG bounds
- Implicit fitting
- Hidden anchors
- Lattice results
- Experiment names
- Exclusion claims
- Symbolic mass scales
- Fine-tuning arguments
- Normalization conventions

### Document Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Pages | 24-40 | ~32 |
| Equations | ≥160 | ~180 |
| Labels | ≥240 | ~260 |
| Traps | ≥8 | 12 |
| recompute.py checks | ≥80% pass | 100% |

### Hash Chain

| Version | Content | Hash | Status |
|---------|---------|------|--------|
| v60 | Canonical Single Document | `4985a938f5558447` | CLOSED |
| v61 | Proton Decay Program (PS) | [computed] | OPEN |

### Acceptance Status

**ACCEPTED** as Program Note (OPEN).

Closure requires:
- Derivation of $M_X$ from EDC field equations
- Integration with EDC cosmology

### Relation to Other Blocks

- **BLOCK-004 v60**: Provides QCD running structure
- **Future PS block**: Will derive $M_X$
- **Hadronic block**: Will provide $\alpha_H$ (if derived)

---

**Report Date**: 2026-02-07

**Status**: PROGRAM NOTE — OPEN until M_X derived
