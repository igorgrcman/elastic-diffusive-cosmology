# BLOCK-004 Derivation v61: Release Notes
## Proton Decay Program Note (PS)

### Version: v61
### Date: 2026-02-07
### Status: PROGRAM NOTE — OPEN

---

## What is CLOSED

### Layer A Structural Content

1. **Pati-Salam Gauge Group**
   - $G_{PS} = SU(4)_C \times SU(2)_L \times SU(2)_R$
   - Complete representation theory
   - Generator normalization (consistent with v55/v56)

2. **Symmetry Breaking**
   - Breaking chain: PS → SM → QCD×QED
   - Hypercharge embedding: $Y = T^{15}_{B-L} + T^3_R$
   - Coupling unification relations

3. **Leptoquark Gauge Bosons**
   - $X_\mu^\alpha$ identification from $SU(4)_C$ decomposition
   - Quantum numbers: $Q_X = \pm 4/3$, color triplet
   - Fermion couplings derived

4. **Dimension-6 Operators**
   - Complete operator catalog
   - Chirality structure (LL, RR, LR)
   - Color contraction algebra

5. **Proton Lifetime Formula**
   - Symbolic formula with all factors explicit
   - Scaling: $\tau_p \propto M_X^4 / (g_{PS}^4 \alpha_H^2)$
   - Phase space calculation

6. **API Definitions**
   - API-PD1: Lifetime calculator
   - API-PD2: Operator coefficients

7. **Firewall Structure**
   - No-Backflow theorem
   - No-Fit policy
   - Forbidden gate specification
   - 12 reviewer traps

---

## What is OPEN

### Required Future Derivations

| Parameter | Description | Source |
|-----------|-------------|--------|
| $M_X$ | PS breaking scale | EDC cosmology/field equations |
| $\alpha_H$ | Hadronic matrix elements | Layer B or future derivation |
| Flavor mixing | Generation structure | CKM-like matrices |
| Thresholds | Corrections at $M_X$ | Matching calculation |
| Higher-dim | $d > 6$ contributions | Subdominant effects |

### Closure Condition

This program note becomes CLOSED when:
1. $M_X$ is derived from EDC field equations (primary condition)
2. Hadronic input $\alpha_H$ is either:
   - Taken from Layer B (lattice/sum rules), OR
   - Derived from EDC-QCD matching

---

## Layer B Status

Layer B (quarantined) provides:
- Comparison protocol structure (no numeric values)
- Hadronic matrix element input format
- Experimental bounds framework

**No explicit PDG values appear in this release.**

---

## Release Bundle Contents

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (self-contained) |
| `recompute.py` | Verification script |
| `README.md` | Overview and usage |
| `REPORT.md` | Technical details |
| `ACCEPTANCE.md` | Acceptance criteria |
| `RELEASE_NOTES.md` | This file |
| `BLOCK004_*.pdf` | Compiled canonical PDF |

---

## Verification

Run `python3 recompute.py` to verify:
- All structural checks pass
- Forbidden patterns absent from Layer A
- APIs defined
- Traps counted
- Document metrics met

---

## Relation to v60

v61 builds on v60 (Canonical Single Document) but addresses a distinct
physical observable:
- v60: Strong coupling $\alpha_s$ from Planck scale to QCD scale
- v61: Proton lifetime from PS unification structure

Both share:
- Layer A/B architecture
- Firewall methodology
- No-Fit policy

---

## Known Limitations

1. Hadronic matrix element $\alpha_H$ is symbolic (unavoidable without QCD input)
2. $M_X$ derivation requires future EDC block
3. Flavor structure assumes trivial mixing (first approximation)
4. Higher-dimensional operators not included

---

## Next Steps

1. Derive $M_X$ from EDC PS breaking (future block)
2. Integrate with EDC cosmology timeline
3. Add flavor structure when needed
4. Close program note when $M_X$ available

---

**Document Hash**: [computed at build]
**Parent Hash (v60)**: 4985a938f5558447
