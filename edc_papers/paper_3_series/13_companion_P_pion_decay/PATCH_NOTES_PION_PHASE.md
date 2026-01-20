# PATCH NOTES: Pion Decay — Hadron→Lepton Injection Test

**Date:** 2026-01-20
**Document:** Companion P — Pion Decay as Hadron→Lepton Injection Test
**Status:** Draft v0.3 (BabaYaga hardened)

---

## Summary

Companion P extends the thick-brane microphysics framework to charged pion
leptonic decays ($\pi^+ \to \mu^+\nu_\mu$, $\pi^+ \to e^+\nu_e$), providing
the first **hadron→lepton injection test** of the absorption→dissipation→release
pipeline.

**Key design decision:** Structural approach only. No numerical fits.
Helicity suppression treated as [BL] with qualitative EDC interpretation.

---

## Document Structure

| Section | Title | Content |
|---------|-------|---------|
| §1 | Motivation | First hadron→lepton test |
| §2 | Ontology | Brane-dominant composite [P] |
| §2.1 | Junction-Pair | Candidate micro-ontology [P]/[OPEN] |
| §3 | Baselines | PDG 2024 values [BL] |
| §4 | Pipeline | Absorption→Dissipation→Release (same as M/T) |
| §5 | Helicity Suppression | [BL] + projection mechanism [P]/[OPEN] |
| §6 | Existence/Stability | Metastability without mass derivation [P]/[OPEN] |
| §7 | Allowed Outputs | $\mathcal{A}_{\pi^+}$ set [Dc] |
| §8 | Chiral Filter | Universal hypothesis [P]/[OPEN] |
| §9 | Falsifiability | 5 guardrails |
| §10 | Open Problems | 6 items flagged |
| §11 | Conclusion | Position in EDC Weak Program |

---

## Epistemic Tag Map

| Claim | Tag | Status |
|-------|-----|--------|
| Pion is brane-dominant composite | [P] | Postulated |
| Junction-pair micro-ontology | [P]/[OPEN] | Candidate only |
| Helicity suppression $m_\ell^2$ scaling | [BL] | SM/PDG fact |
| EDC projection mechanism | [P]/[OPEN] | Qualitative |
| $m_\ell^2$ derivation from BC | [OPEN] | Not attempted |
| Metastability mechanism | [P]/[OPEN] | Spectral gap hypothesis |
| Allowed output set $\mathcal{A}_{\pi^+}$ | [Dc] | From conservation laws |
| Chiral filter universality | [P]/[OPEN] | Hypothesis |
| $m_\pi$, $\tau_\pi$ values | [BL] | PDG 2024 |
| $m_\pi$ from first principles | [OPEN] | Not attempted |

---

## Key Equations

### SM Helicity Suppression (Eq. 1)
```latex
\Gamma(\pi^+ \to \ell^+\nu_\ell) \propto m_\ell^2 \left(1 - \frac{m_\ell^2}{m_\pi^2}\right)^2
```
Status: [BL] — SM result, not EDC derivation

### Frozen Projection Stack (Eq. 2)
```latex
\mathcal{P}_{\mathrm{frozen}} = \mathcal{P}_{\mathrm{energy}} \circ
\mathcal{P}_{\mathrm{mode}} \circ \mathcal{P}_{\mathrm{chir}}
```
Status: Same structure as Companions M/T

### Allowed Output Set (Eq. 3)
```latex
\mathcal{A}_{\pi^+} = \{(\mu^+, \nu_\mu), (e^+, \nu_e)\}
```
Status: [Dc] — from conservation laws

---

## Figures

| Figure | Description | Content |
|--------|-------------|---------|
| Fig. 1 | Pipeline diagram | Composite pion → absorption → dissipation → P_frozen → μ/e channels |

---

## Numerology Avoidance Checklist

- [x] No attempt to derive $m_\pi = 140$ MeV
- [x] No attempt to derive $\tau_\pi = 26$ ns
- [x] No attempt to derive BR ratio from scratch
- [x] Helicity suppression $m_\ell^2$ treated as [BL] input
- [x] Junction-pair is CANDIDATE, not central ontology
- [x] PDG values in baseline table only
- [x] All "derivation" claims explicitly flagged [OPEN]

---

## Open Problems Flagged

1. **Derive $m_\pi$ from 5D binding** [OPEN]
2. **Derive $\tau_\pi$ from first principles** [OPEN]
3. **Derive $m_\ell^2$ scaling from BC** [OPEN]
4. **Junction-pair micro-ontology validation** [OPEN]
5. **Neutral pion $\pi^0 \to \gamma\gamma$** [OPEN]
6. **Pion-nucleon interactions** [OPEN]

---

## Build Verification

```bash
cd edc_papers/paper_3_series/13_companion_P_pion_decay/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Output: main.pdf (7 pages)
# Overfull boxes: 2 (minor, ~2pt and ~5pt)
# Undefined references: 0
```

---

## Files Created

```
13_companion_P_pion_decay/
├── paper/
│   ├── main.tex          # Main document (7 pages)
│   └── main.pdf          # Compiled output
└── PATCH_NOTES_PION_PHASE.md  # This file
```

---

## Relationship to Other Companions

| Document | Relationship |
|----------|--------------|
| Companion M (Muon) | Same pipeline; pion is first COMPOSITE input |
| Companion T (Tau) | Same pipeline; validates brane-dominant generalization |
| Companion N (Neutron) | Different ontology (bulk-core vs brane-composite) |
| Companion H (Weak Interactions) | Thick-brane foundation |

---

## EDC Weak Program Status

| Companion | Particle | Ontology | Status |
|-----------|----------|----------|--------|
| N | Neutron | Bulk-core junction | v3.0 |
| M | Muon | Brane-dominant (fundamental) | v0.2 |
| T | Tau | Brane-dominant (higher mode) | v0.1 |
| **P** | **Pion** | **Brane-dominant (composite)** | **v0.3** |

---

## Red-Team Defense Notes

**Anticipated attack:** "You just relabeled SM without adding anything."

**Defense:** EDC adds:
1. Ontological distinction (composite vs fundamental)
2. Pipeline unification (same mechanism for hadron→lepton as lepton→lepton)
3. Structural prediction (if wrong ontology → wrong selection rules)

**Anticipated attack:** "Why not derive the masses?"

**Defense:** Explicitly flagged [OPEN]. Honest about limitations.
Better 7 pages of truth than 20 pages of numerology.

---

*Generated: 2026-01-20 (Pion Hadron→Lepton Phase)*

---

## BabaYaga Pass (v0.3) — 2026-01-20

### What Was Changed

1. **Epistemic Status table added** (Table 2)
   - Explicit listing of [BL], [P], [OPEN] claims
   - Clear separation of baseline facts vs EDC postulates vs open problems

2. **Energy Bookkeeping table added** (Table 3)
   - Qualitative ledger without numeric values
   - Tracks energy through Absorption→Dissipation→Release stages
   - Explicit "suppressed bulk leakage" entry

3. **Falsifiability section enhanced**
   - Added 6th bullet: Ledger consistency
   - Added guardrail box: "No immunity to falsification"
   - Each bullet now specifies what would fail

4. **Version updated to v0.3**
   - Header, date line, and position table updated

### What Was Explicitly NOT Claimed (Anti-Overclaim List)

- ❌ Derivation of $m_\pi$ from first principles
- ❌ Derivation of $\tau_\pi$ from first principles
- ❌ Derivation of $m_\ell^2$ helicity suppression factor
- ❌ Derivation of BR($\mu$)/BR($e$) ratio
- ❌ Explanation of quark confinement in 5D
- ❌ Junction-pair as proven (only candidate [P]/[OPEN])
- ❌ Photon ontology (deferred)
- ❌ Any numerical fits or parameter tuning

### What Remains [OPEN]

1. Derive $m_\pi$ from 5D binding
2. Derive $\tau_\pi$ from first principles
3. Derive $m_\ell^2$ scaling from explicit BC computation
4. Validate or refute junction-pair micro-ontology
5. Neutral pion $\pi^0 \to \gamma\gamma$ (requires photon ontology)
6. Pion-nucleon interactions (coupling to bulk-core junctions)

### Files Modified/Created

- `paper/main.tex` — BabaYaga hardening patches
- `BABA_YAGA_CHECKLIST_P.md` — New file (red-team verification checklist)
- `PATCH_NOTES_PION_PHASE.md` — Updated (this section)

### Build Verification

```bash
cd edc_papers/paper_3_series/13_companion_P_pion_decay/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Expected: ~8 pages, no errors, no undefined refs
```

---

*BabaYaga Pass completed: 2026-01-20*
