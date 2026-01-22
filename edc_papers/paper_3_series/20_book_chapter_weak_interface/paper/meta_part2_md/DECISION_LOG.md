# Decision Log — Part II: The Weak Interface

**Version:** 1.0
**Created:** 2026-01-22
**Purpose:** Document key architectural and methodological decisions

---

## DEC-001: GREEN-A/YELLOW-B/RED-C Naming

**Date:** 2026-01-20
**Commit:** `aba4822`

### Problem Statement
Previous stoplight system (GREEN/YELLOW/RED) was ambiguous. "GREEN" could mean:
- (a) Derived from first principles
- (b) Numerically correct
- (c) Logically consistent

This caused confusion in reviews when claims at different certainty levels all appeared "GREEN."

### Decision
Adopt three-level naming for derivation status:
- **GREEN-A**: Electroweak consistency closure (uses SM relations, may have circularity)
- **YELLOW-B**: Geometric mechanism identified (qualitative understanding, OOM agreement)
- **RED-C**: First-principles open (requires explicit 5D calculation not yet done)

### Rationale
1. **Clarity**: Each level has specific meaning
2. **Honesty**: Acknowledges what is truly derived vs. consistent vs. open
3. **Reviewable**: Reviewer can check if classification is appropriate

### Alternatives Considered
| Option | Description | Why Rejected |
|--------|-------------|--------------|
| A | Keep simple GREEN/YELLOW/RED | Insufficiently granular |
| B | Use numbered levels 1/2/3 | Non-intuitive, no semantic meaning |
| C | Per-claim custom levels | Inconsistent across chapters |

---

## DEC-002: G_F v-Circularity Acknowledgment

**Date:** 2026-01-21
**Commit:** `b4ff06a`

### Problem Statement
G_F "exact agreement" appears impressive but may be attacked as circular:
- In SM, Higgs VEV v = (√2 G_F)^{-1/2}
- Using v to compute M_W, then deriving G_F from M_W is G_F → v → M_W → G_F

### Decision
Acknowledge circularity explicitly in Ch. 11 rather than hide it:
1. State that G_F closure is a **consistency identity**, not independent prediction
2. Redirect attention to **sin²θ_W = 1/4** as the true independent prediction
3. Explain why consistency is still valuable (rules out gross errors)

### Rationale
- **Preemptive defense**: Reviewer cannot "catch" us if we state it first
- **Intellectual honesty**: Builds credibility
- **Focus on strength**: sin²θ_W prediction is genuinely non-trivial

### Alternatives Considered
| Option | Description | Why Rejected |
|--------|-------------|--------------|
| A | Claim G_F as independent prediction | Intellectually dishonest |
| B | Remove G_F discussion entirely | Loses valid consistency check |
| C | Use different v definition | Still circular, more confusing |

---

## DEC-003: CKM Falsify-First Approach

**Date:** 2026-01-22
**Commit:** `a2e9a6e`

### Problem Statement
How to present CKM treatment in Ch. 7? Options:
- Jump directly to working model (overlap)
- Show baseline failure first

### Decision
Compute Z₃ DFT baseline first, explicitly falsify it, then present overlap model:
1. **Attempt 1**: Simplest geometric ansatz (Z₃ DFT)
2. **Falsification**: Show |V_ij|² = 1/3 is ×144 off
3. **Attempt 2**: Overlap model that works

### Rationale
"Null hypothesis" approach:
- Shows we tested simplest option honestly
- Quantifies how much Z₃ breaking is needed
- Makes overlap model success more convincing by contrast

### Alternatives Considered
| Option | Description | Why Rejected |
|--------|-------------|--------------|
| A | Skip baseline, go directly to overlap | Loses pedagogical value |
| B | Only show baseline failure | No constructive path forward |
| C | Present both simultaneously | Confusing narrative |

---

## DEC-004: Exponential Overlap Ansatz

**Date:** 2026-01-22
**Commit:** `3b1aa94`

### Problem Statement
What profile ansatz to use for localized fermion wavefunctions?

### Decision
Use exponential profile: f(z) ∝ exp(-|z - z₀|/κ)

### Rationale
1. **Analytically tractable**: Overlap integrals have closed form
2. **Physically motivated**: Exponential localization from mass gap
3. **Correct scaling**: Gives O_ij ∝ λ^|i-j| directly
4. **Single parameter**: Only κ matters for hierarchy

### Alternatives Considered
| Option | Description | Why Rejected |
|--------|-------------|--------------|
| A | Gaussian profiles | More complex, same qualitative result |
| B | Numeric BVP solution | RED-C level, not available |
| C | Delta functions | Too singular, no overlap |

---

## DEC-005: CKM vs PMNS via Localization

**Date:** 2026-01-22
**Commit:** `3b1aa94`

### Problem Statement
Why is CKM near-diagonal (small mixing) but PMNS has large angles?

### Decision
Explain via localization width κ:
- **Quarks**: Color coupling → tight localization → small κ → suppressed off-diagonal
- **Neutrinos**: Color-neutral edge modes → broad κ → large PMNS angles
- **Same Z₃ structure**, different localization → different mixing

### Rationale
- **Unifying**: One mechanism explains both
- **Physical**: Color coupling has natural effect on localization
- **Falsifiable**: Predicts relationship between color and mixing

### Alternatives Considered
| Option | Description | Why Rejected |
|--------|-------------|--------------|
| A | Separate mechanisms for CKM/PMNS | Loses unification |
| B | Claim numerical κ prediction | κ ratio not computed |
| C | Ignore PMNS entirely | Leaves obvious question unanswered |

---

## DEC-006: Meta-Documentation with Compile Switch

**Date:** 2026-01-22
**Commit:** pending

### Problem Statement
Research narrative is valuable for reproducibility but adds 20+ pages to document.
Journals have page limits; archive needs full record.

### Decision
Create meta-documentation appendix with optional compile switch:
- `\ifMetaPartII` toggle in main .tex
- Default OFF for submissions
- ON for archive/full builds
- Separate Markdown files for machine parsing

### Rationale
1. **Flexibility**: Same source, different outputs
2. **Traceability**: Full record preserved in repo
3. **Practicality**: Meets journal page limits

### Alternatives Considered
| Option | Description | Why Rejected |
|--------|-------------|--------------|
| A | Always include meta | Too long for journals |
| B | Separate document entirely | Loses traceability to main text |
| C | Only Markdown, no LaTeX | Loses formatted appendix option |

---

## Statistics

| Category | Count |
|----------|-------|
| Total decisions | 6 |
| With commits | 5 |
| Pending | 1 |

---

*Decision Log v1.0 — Last updated 2026-01-22*
