# V7.6.1 — SIGN PARADOX RESOLUTION

**Created**: 2026-01-31
**Purpose**: Explain why g < 0 and determine barrier vs prefactor mechanism
**Verdict**: **PREFACTOR (S_α enhancement)**

---

## The Paradox

| Naive expectation | Measured |
|-------------------|----------|
| Forbidden zone → higher barrier → slower decay → g > 0 | g = -0.31 < 0 |

**Question**: Why does "topological frustration" *accelerate* decay?

---

## Resolution in One Paragraph

The negative sign of g is not paradoxical once we recognize that α-decay rates depend on two factors: tunneling probability (captured by Geiger-Nuttall) and preformation probability S_α (how often an α-cluster exists at the nuclear surface). Statistical tests show that d(n) acts primarily through the **prefactor channel**: the additive model (d(n) multiplying rate) fits better than the multiplicative model (d(n) modifying barrier slope). Physically, topological frustration corresponds to structural strain or defects in the nuclear "lattice" — and in condensed matter physics, defects typically *enhance* dynamics (diffusion, nucleation, reorganization). Applied to nuclei: frustration → enhanced surface dynamics → easier α-cluster formation → higher S_α → faster decay. The effect is most visible in unhindered (H0) transitions where the barrier is the limiting factor; in hindered transitions, selection rules mask the S_α enhancement.

---

## Key Test Results

| Test | Result | Interpretation |
|------|--------|----------------|
| T1: Hindrance interaction | g strongest in H0 | Effect visible when barrier limits |
| T2: Parity control | g = -0.29, p = 0.016 | Not a pairing proxy |
| T3: Model comparison | AIC favors additive | Prefactor mechanism |

---

## Implications for Book 2

### What to say:
- d(n) correlates with faster decay (g < 0)
- Most consistent with preformation enhancement
- Frustration → enhanced dynamics → easier α-cluster formation

### What NOT to say:
- ❌ "Forbidden zones impede tunneling" (contradicted by data)
- ❌ "d(n) increases barrier height" (model comparison rejects this)
- ❌ Overclaim causation (this is still correlation)

### Recommended wording:
> "Nuclei with coordination indices farther from allowed M-topology values exhibit enhanced α-decay rates, consistent with frustration-induced preformation dynamics rather than barrier modification."

---

## Physical Analogy

| System | Frustration effect |
|--------|-------------------|
| Crystal diffusion | Defects enhance mobility |
| Grain boundaries | Facilitate nucleation |
| Frustrated magnets | Enhanced spin dynamics |
| **α-decay** | Enhanced S_α preformation |

Frustration ≠ stability. Frustration = metastable dynamics = faster transitions.

---

## Epistemic Status

- **Mechanism**: [Hyp] — Prefactor interpretation is hypothesis, consistent with data
- **Correlation**: [Der] — g < 0 is robustly derived from BL data
- **Causation**: Not established — d(n) could still proxy for unmeasured nuclear structure

---

## Files in This Folder

| File | Content |
|------|---------|
| 00_README.md | This summary |
| 01_TEST_BARRIER_vs_PREFACTOR.md | Detailed T1/T2/T3 analysis |
| 02_BOOK2_PARAGRAPH_SIGN_SAFE.md | Conservative paragraph variants |

