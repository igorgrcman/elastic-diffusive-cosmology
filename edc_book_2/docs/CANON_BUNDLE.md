# CANON BUNDLE — P0 Mandatory Documents

**Generated:** 2026-01-29 13:15
**Purpose:** Single file containing ALL P0 canonical documents for session loading.
**Usage:** Read this file at the START of every CC session. MANDATORY.

> This file is auto-generated from `docs/CANON_P0.list`.
> Do NOT edit directly — edit source files and run `tools/regenerate_canon_bundle.sh`.

---


# ============================================================================
# DOCUMENT 1: CLAUDE.md
# Source: edc_book_2/CLAUDE.md
# ============================================================================

# CLAUDE.md — NON-NEGOTIABLE WORKFLOW (EDC Book 2)

You are an engineering assistant operating in a **stateless environment**.
Therefore ALL reasoning, derivations, and decisions MUST be written to disk.

---

## 0) Single Source of Truth Files (MUST exist)

| File | Purpose |
|------|---------|
| `docs/STATUS.md` | Current truth — what is true RIGHT NOW |
| `docs/TODO.md` | Next actions, ordered by priority |
| `docs/DECISIONS.md` | ADR-style: decision + rationale |
| `docs/DERIVATIONS.md` | Math chain: assumptions → steps → results |
| `docs/SESSION_LOG.md` | Append-only: every session adds an entry |

**If any file is missing, create it immediately with minimal structure.**

---

## 1) Start-of-Session Protocol (MANDATORY)

Before doing ANY other work:

1. **READ `docs/CANON_BUNDLE.md`** — contains ALL P0 canon in one file. **NO EXCEPTIONS.**
2. If working in specific area, consult `docs/CANON_INDEX.md` for P1 references.
3. **Write** a short "Plan for this session" at the TOP of your response AND append to `docs/SESSION_LOG.md`
4. **Only then** proceed with actual work

> **Why MANDATORY?** CANON_BUNDLE contains verified findings [Der], anti-patterns, and decisions.
> Skipping it leads to re-deriving known results or repeating known errors.

---

## 2) During Work (MANDATORY)

### Derivations
Every nontrivial derivation must be written in `docs/DERIVATIONS.md`:
- Include equation labels / file references (path + line numbers)
- Mark epistemic tags: `[Der]`, `[Dc]`, `[I]`, `[P]`, `[Cal]`, `[BL]`
- Record assumptions and dependencies
- Note any open problems

### Decisions
Every decision (even small ones) must be recorded in `docs/DECISIONS.md`:
- What was decided
- Why (rationale)
- Alternatives considered
- Date

### Status Changes
Every change to narrative logic must be reflected in `docs/STATUS.md`.

---

## 3) End-of-Session Protocol (DEFINITION OF DONE)

You may NOT conclude the session until ALL are true:

- [ ] `docs/SESSION_LOG.md`: appended entry with:
  - Date/time
  - Goals
  - Files touched
  - Key diffs summary
  - Open questions
  - Next steps

- [ ] `docs/DERIVATIONS.md`: updated with any new math/logic

- [ ] `docs/STATUS.md`: updated "Current State" and "Known Issues"

- [ ] `docs/TODO.md`: updated (completed items marked; new items added)

- [ ] `docs/DECISIONS.md`: appended if any decision was made

---

## 4) Output Format (MANDATORY)

At the end of EVERY response that modifies files, include:

```
## Session Summary
**Files changed:** [list]
**Next steps:** [list]
**Open questions:** [list]
```

---

## 5) Epistemic Tags (EDC Standard)

| Tag | Meaning | Use when... |
|-----|---------|-------------|
| `[Der]` | Derived | Explicit derivation from postulates exists |
| `[Dc]` | Derived Conditional | Derived IF certain assumptions hold |
| `[I]` | Identified | Pattern matching / mapping (not unique) |
| `[P]` | Proposed | Postulate / hypothesis / conjecture |
| `[Cal]` | Calibrated | Parameter fitted to data |
| `[BL]` | Baseline | External reference (PDG/CODATA) |

---

## 6) Repo Policy

- **NEVER** delete git branches after merge (forensic audit trail)
- Prefer small commits
- Commit messages must mention which docs were updated
- Build verification required before merge

---

## 7) Red Flags — STOP WORK

If you encounter any of these, STOP and ask the user:

- Dependency graph has a cycle (circularity)
- "Derivation" without explicit steps
- Numerical value used BEFORE derivation
- "Obviously..." without proof
- More than 3 free parameters in one formula
- Inconsistency between documents

---

## 8) Language

- **Croatian** for conversation with Igor
- **English** for technical documents and code
- **Direct** — no hedging
- **Honest** — if something is circular or unknown, say so


# ============================================================================
# DOCUMENT 2: STATUS.md
# Source: edc_book_2/docs/STATUS.md
# ============================================================================

# STATUS.md — Current State of EDC Book 2

**Last updated:** 2026-01-28

---

## Current Truth

### Core Parameters (Established)

| Parameter | Value | Status | Source |
|-----------|-------|--------|--------|
| σ (brane tension) | 8.82 MeV/fm² | [Dc] | Conditional on E_σ = m_e c²/α |
| δ (brane thickness) | 0.105 fm | [Dc] | ℏ/(2m_p c) |
| L₀ (junction extent) | 0.980 fm | [P] | r_p + δ |
| K (pinning constant) | 0.94 MeV | [Dc/I] | f × σ × A_contact |

### Derived Results

| Result | Value | Observed | Error | Status |
|--------|-------|----------|-------|--------|
| τ_n (free neutron) | ~10³ s | 879 s | O(1) | [Dc/Cal]* |
| τ_n (bound neutron) | >10¹³ s | stable | — | [Dc] |
| B.E.(He-4) | 29 MeV | 28.3 MeV | +3% | [I] |
| B.E.(C-12) | 92.0 MeV | 92.2 MeV | -0.2% | [I] |
| B.E.(O-16) | 127.3 MeV | 127.6 MeV | -0.2% | [I] |
| Be-8 instability | Unstable | Unstable | ✓ | [Dc] |

*Note: τ_n prefactor A ≈ 0.84 is [Cal], not derived.

### Weak Sector (from Paper 3)

| Result | Status | Note |
|--------|--------|------|
| V-A structure | [Dc] | From 5D chirality projection |
| Parity violation | [Dc] | 5D geometry enforces |
| sin²θ_W = 1/4 | [Der] | Geometric (exact at tree level) |
| G_F | [Dc/Cal] | Partial — uses measured v (circular) |

### Topological Pinning Model

| Feature | Status | Note |
|---------|--------|------|
| Allowed coordinations | [I] | n = 2^a × 3^b (geometric constraint) |
| Forbidden n = 43 | [P] | Optimal for nuclear matter but topologically forbidden |
| Frustration-Corrected G-N Law | [I/Cal] | R² = 0.9941, 44.7% improvement |

---

## Known Issues

1. ~~**L₀/δ tension**~~ **RESOLVED [Dc]** — Both valid: π² for static, 9.33 for dynamic. See `docs/L0_DELTA_TENSION_RESOLUTION.md`
2. **Prefactor A**: Calibrated, not derived from fluctuation determinant
3. **G_F derivation**: Uses measured v — need pure 5D derivation
4. **Geometric factor f**: Identified as √(δ/L₀) but not derived from first principles

---

## Key Documents

| Document | Location | Status |
|----------|----------|--------|
| Topological Pinning Model | `src/derivations/BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex` | Active |
| Neutron Lifetime | `src/derivations/BOOK_SECTION_NEUTRON_LIFETIME.tex` | Active |
| Frustration G-N code | `src/derivations/frustration_geiger_nuttall.py` | Complete |

---

## Branch Status

- Current branch: `book-routeC-narrative-cleanup-v1`
- Main branch: `main`
- Ready to merge: NO (documentation incomplete)


# ============================================================================
# DOCUMENT 3: DERIVATIONS.md
# Source: edc_book_2/docs/DERIVATIONS.md
# ============================================================================

# DERIVATIONS.md — Mathematical Chain Registry

**Last updated:** 2026-01-28

---

## Format

Each derivation entry follows this structure:
```
### DER-XXX: [Name]
**Status:** [Der]/[Dc]/[I]/[P]/[Cal]
**Depends on:** [list of DER-XXX or assumptions]
**Result:** [equation]
**Location:** [file:line]
**Open issues:** [if any]
```

---

## Core Parameters

### DER-001: Brane Tension σ
**Status:** [Dc] — Conditional on hypothesis E_σ = m_e c²/α
**Depends on:** m_e [BL], α [BL], hypothesis E_σ = m_e c²/α [P]
**Result:**
```
σ = m_e³ c⁴ / (α³ ℏ²) = 8.82 MeV/fm²
```
**Location:** Turning point document TP-2026-01-20
**Open issues:** E_σ = m_e c²/α is [P], needs geometric derivation

### DER-002: Brane Thickness δ
**Status:** [Dc]
**Depends on:** m_p [BL], Compton regularization [P]
**Result:**
```
δ = ℏ / (2 m_p c) = 0.105 fm
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:54
**Open issues:** Factor 2 is conventional

### DER-003: Junction Extent L₀
**Status:** [P]
**Depends on:** r_p [BL], δ [DER-002]
**Result:**
```
L₀ = r_p + δ = 0.875 + 0.105 = 0.980 fm
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:153-154
**Open issues:** Alternative: L₀/δ = π² from standing wave argument

---

## Neutron Lifetime

### DER-010: Instanton Action
**Status:** [Dc] — Conditional on S¹ junction topology
**Depends on:** κ = 2π [DER-011], L₀/δ [DER-003]
**Result:**
```
S_E/ℏ = κ × (L₀/δ) = 2π × 9.33 ≈ 58.6
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:260
**Open issues:** L₀/δ tension (9.33 vs π²)

### DER-011: Topological Winding Factor κ
**Status:** [Dc] — Conditional on S¹ topology
**Depends on:** π₁(S¹) = ℤ [M]
**Result:**
```
κ = 2π (from ∮dθ = 2π for minimal winding Δw = 1)
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:128-131
**Open issues:** Need to verify junction has S¹ topology

### DER-012: Attempt Frequency ω₀
**Status:** [P]
**Depends on:** σ [DER-001], M = m_p [P]
**Result:**
```
ω₀ = √(σ/m_p) ≈ 19.1 MeV ≈ 2.9 × 10²² Hz
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:219
**Open issues:** M = m_p is assumed, not derived

### DER-013: Neutron Lifetime Formula
**Status:** [Dc/Cal]
**Depends on:** S_E/ℏ [DER-010], ω₀ [DER-012], A [Cal]
**Result:**
```
τ_n = A × (ℏ/ω₀) × exp(S_E/ℏ)

Uncalibrated (A=1): τ_n ≈ 1050 s
Calibrated (A=0.84): τ_n ≈ 879 s
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:79-81
**Open issues:** A = 0.84 is [Cal], needs derivation from fluctuation determinant

---

## Topological Pinning Model

### DER-020: Contact Area
**Status:** [Dc]
**Depends on:** δ [DER-002], L₀ [DER-003]
**Result:**
```
A_contact = π δ L₀ = π × 0.105 × 1.0 ≈ 0.33 fm²
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:270-271
**Open issues:** Saddle surface assumption

### DER-021: Geometric Factor f
**Status:** [I]
**Depends on:** δ [DER-002], L₀ [DER-003]
**Result:**
```
f = √(δ/L₀) = √(0.105/1.0) ≈ 0.32
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:298-300
**Open issues:** Penetration depth ratio — needs first-principles derivation

### DER-022: Pinning Constant K
**Status:** [Dc/I]
**Depends on:** f [DER-021], σ [DER-001], A_contact [DER-020]
**Result:**
```
K = f × σ × A_contact = 0.32 × 8.82 × 0.33 ≈ 0.93 MeV
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:306-312
**Open issues:** Phenomenological check: 0.7-0.8 MeV needed

### DER-023: Allowed Coordinations
**Status:** [I]
**Depends on:** Y-junction trivalent constraint [P], quantum doubling [P]
**Result:**
```
n = 2^a × 3^b for a,b ≥ 0
Allowed: {6, 8, 9, 12, 24, 36, 48, 72, ...}
Forbidden: {5, 7, 11, 13, 37, 41, 43, 47, ...}
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:60-95
**Open issues:** Geometric argument needs formalization

### DER-024: Bound Neutron Lifetime Enhancement
**Status:** [Dc]
**Depends on:** K [DER-022], S_E/ℏ [DER-010]
**Result:**
```
At saddle point q_barrier ≈ 0.5:
ΔV_eff ≈ ΔV + 6K × q_barrier² ≈ 1.3 + 5.6 × 0.25 ≈ 2.7 MeV
S_eff/ℏ ≈ 60 × √(2.7/1.3) ≈ 86
τ_bound > 10¹³ s
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:373-387
**Open issues:** q_barrier = 0.5 assumed (saddle point)

---

## Frustration-Corrected Geiger-Nuttall Law

### DER-030: Frustration Energy Interpolation
**Status:** [I]
**Depends on:** n_eff(A) interpolation [P]
**Result:**
```
n_eff(A) = 6 + 37(1 - e^(-(A-20)/80))
ε_f(A) = |E/A(n_eff) - E/A(n_allowed)|
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:686-689
**Open issues:** Interpolation is phenomenological

### DER-031: Frustration-Corrected G-N Formula
**Status:** [I/Cal]
**Depends on:** ε_f(A) [DER-030], standard G-N [BL]
**Result:**
```
log₁₀(t½) = 1.63 × Z/√Q - 2.40 × ε_f - 42.1
R² = 0.9941 (vs 0.9822 standard)
44.7% improvement in MAE
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:681-699
**Open issues:** Coefficients a, c, b are [Cal]

---

## Weak Sector (Paper 3 Results)

### DER-040: V-A Structure
**Status:** [Dc]
**Depends on:** 5D chirality projection [P]
**Result:** V-A structure emerges from 5D geometry
**Location:** Paper 3, weak sector section
**Open issues:** None

### DER-041: Parity Violation
**Status:** [Dc]
**Depends on:** 5D geometry [P]
**Result:** Parity violation enforced by 5D structure
**Location:** Paper 3, weak sector section
**Open issues:** None

### DER-042: Weinberg Angle
**Status:** [Der]
**Depends on:** Geometric embedding [P]
**Result:**
```
sin²θ_W = 1/4 (exact at tree level)
```
**Location:** Paper 3
**Open issues:** Radiative corrections not included

### DER-043: Fermi Coupling G_F
**Status:** [Dc/Cal] — CIRCULAR
**Depends on:** measured v [BL] — THIS IS THE PROBLEM
**Result:** Partial derivation, but uses measured Higgs VEV
**Location:** Paper 3
**Open issues:** Need pure 5D derivation without circular input

---

## Dependency Graph Summary

```
[BL] m_e, m_p, α, r_p
        ↓
    [P] E_σ = m_e c²/α
        ↓
    [Dc] σ = 8.82 MeV/fm² (DER-001)
        ↓
    [Dc] δ, L₀ (DER-002, DER-003)
        ↓
    ├── [Dc] S_E/ℏ ≈ 60 (DER-010)
    │       ↓
    │   [Dc/Cal] τ_n ≈ 879 s (DER-013)
    │
    └── [Dc/I] K ≈ 0.94 MeV (DER-022)
            ↓
        [Dc] τ_bound → ∞ (DER-024)
        [I] B.E.(He-4), B.E.(C-12), B.E.(O-16)
        [I/Cal] Frustration G-N Law (DER-031)
```

**No cycles detected.**


# ============================================================================
# DOCUMENT 4: TODO.md
# Source: edc_book_2/docs/TODO.md
# ============================================================================

# TODO.md — Prioritized Action Items

**Last updated:** 2026-01-28

---

## Priority 1: Blocking Issues

- [x] **Resolve L₀/δ tension** — RESOLVED [Dc] (2026-01-29): Both valid in context. See `docs/L0_DELTA_TENSION_RESOLUTION.md`
  - Possible: quantum/boundary corrections for dynamic processes
  - Need: explicit calculation from 5D action

- [ ] **Derive prefactor A** from fluctuation determinant
  - Current: A ≈ 0.84 [Cal]
  - Need: [Der] from instanton fluctuation modes

- [ ] **Derive G_F without circular input**
  - Current: uses measured v
  - Need: pure 5D derivation of weak coupling

---

## Priority 2: Model Completion

- [ ] **Derive geometric factor f = √(δ/L₀)** from first principles
  - Current: [I] — identified from penetration depth argument
  - Need: [Der] from contact mechanics in 5D

- [ ] **Derive frustration energy ε_f(A)** from 5D action
  - Current: phenomenological interpolation
  - Need: topological calculation

- [ ] **Include spin/isospin** in topological pinning model
  - Current: single deformation parameter q
  - Need: proper Pauli exclusion treatment

---

## Priority 3: Documentation & Consistency

- [ ] **Run full LaTeX reference sweep before distribution**
  - Current: "undefined references" warning in compile
  - Need: resolve all \ref, \cite, \label mismatches
  - Blocker for any external release

- [ ] **Create comprehensive derivation registry**
  - List all claims with epistemic status
  - Track dependencies

- [ ] **Audit all "~20%" vs "<1%" claims**
  - Ensure consistency between documents
  - Mark calibrated vs derived results clearly

- [ ] **Update turning points document**
  - Add frustration-corrected G-N law results
  - Add red team patches

---

## Priority 4: Extensions

- [ ] **Connect to drip lines** — topological origin of nuclear stability limits
- [ ] **Test superheavy predictions** — compare with experimental data when available
- [ ] **Investigate QCD duality** — is topological pinning dual to lattice QCD?

---

## Completed (Recent)

- [x] ~~Red team patches: precision consistency~~ (2026-01-28)
- [x] ~~Red team patches: barrier calculation~~ (2026-01-28)
- [x] ~~Red team patches: coordination constraint grounding~~ (2026-01-28)
- [x] ~~Rename M6 → Topological Pinning Model~~ (2026-01-28)
- [x] ~~Frustration-Corrected Geiger-Nuttall Law~~ (2026-01-28)
- [x] ~~C-12, O-16 binding energy fix~~ (2026-01-28)


# ============================================================================
# DOCUMENT 5: DECISIONS.md
# Source: edc_book_2/docs/DECISIONS.md
# ============================================================================

# DECISIONS.md — Architectural Decision Records

**Last updated:** 2026-01-28

---

## Format

```
### ADR-XXX: [Title]
**Date:** YYYY-MM-DD
**Status:** Accepted / Superseded / Deprecated
**Context:** [Why decision was needed]
**Decision:** [What was decided]
**Rationale:** [Why this option]
**Alternatives considered:** [Other options]
**Consequences:** [Impact]
```

---

## ADR-001: L₀/δ = 9.33 for Dynamic Processes

**Date:** 2026-01-28
**Status:** Accepted (with noted tension)

**Context:**
Two candidate values exist for L₀/δ:
- Route S (Static): π² ≈ 9.87 — optimizes m_p
- Route D (Dynamic): 9.33 — optimizes τ_n

The difference is only 5.5% but produces factor ~30 difference in τ_n due to exponential sensitivity.

**Decision:**
Use L₀/δ = 9.33 for neutron lifetime calculations.

**Rationale:**
- Gives τ_n ≈ 879 s with reasonable prefactor A ≈ 0.84
- Route S would require A ≈ 0.03 (unrealistic)
- Physical interpretation: dynamic processes "see" effective scale due to quantum/boundary corrections

**Alternatives considered:**
- Use π² everywhere: rejected (τ_n off by factor 30)
- Derive unique value from action: OPEN PROBLEM

**Consequences:**
- m_p prediction has +4.9% error (acceptable)
- Internal tension documented but unresolved
- Need to derive effective scale from 5D action

---

## ADR-002: Rename M6 Model → Topological Pinning Model

**Date:** 2026-01-28
**Status:** Accepted

**Context:**
Original model was called "M6" assuming coordination n = 6 (honeycomb). Analysis showed:
- Multiple coordinations are allowed: n = 2^a × 3^b
- Predictions for α-cluster nuclei are independent of n
- "M6" name is misleading

**Decision:**
Rename to "Topological Pinning Model" throughout.

**Rationale:**
- More accurate description of the mechanism (pinning, not specific coordination)
- Avoids confusion about n = 6 being special
- Emphasizes that K (from σ) is the key parameter, not n

**Alternatives considered:**
- Keep "M6" as historical name: rejected (confusing)
- Use "Mn Model" with variable n: rejected (still implies n is central)

**Consequences:**
- File renamed: BOOK_SECTION_M6_TOPOLOGICAL_MODEL.tex → BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex
- All references updated
- Commit 115177f

---

## ADR-003: Epistemic Honesty on τ_n Precision

**Date:** 2026-01-28
**Status:** Accepted

**Context:**
Red team critique identified inconsistency:
- Some places claimed "<1% error" for τ_n
- This was misleading because prefactor A = 0.84 is calibrated [Cal], not derived

**Decision:**
Distinguish uncalibrated and calibrated results explicitly:
- Uncalibrated (A = 1): τ_n ~ 10³ s (order of magnitude)
- Calibrated (A = 0.84): τ_n ≈ 879 s

**Rationale:**
- Epistemic honesty requires marking [Cal] vs [Dc]
- "<1%" only true because we tuned A
- The real achievement is getting correct ORDER OF MAGNITUDE from topology

**Alternatives considered:**
- Claim "<1%" is valid since A is O(1): rejected (misleading)
- Drop τ_n result entirely: rejected (still valuable)

**Consequences:**
- Updated BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex
- Updated BOOK_SECTION_NEUTRON_LIFETIME.tex
- Summary table status changed to [Dc/Cal]*
- Commits a94a7e0, cc32549

---

## ADR-004: Coordination Constraint Grounding

**Date:** 2026-01-28
**Status:** Accepted

**Context:**
Red team critique noted that "n = 43 forbidden because prime" sounds like numerology.

**Decision:**
Ground the constraint in geometry:
1. Y-junction trivalent constraint → factor 3
2. Quantum spin/isospin doubling → factors of 2
3. Therefore n = 2^a × 3^b

**Rationale:**
- "43 is prime" is consequence, not explanation
- Geometric argument shows WHY only factors 2 and 3 are allowed
- This is a constraint from junction geometry, not numerology

**Alternatives considered:**
- Leave as "prime forbidden": rejected (sounds like numerology)
- Remove n = 43 discussion: rejected (important result)

**Consequences:**
- Added explicit geometric argument in tex files
- Changed language from "prime > 3" to "n ≠ 2^a × 3^b"
- Commit a94a7e0

---

## ADR-005: Adopt Stateless Workflow with Mandatory Docs

**Date:** 2026-01-28
**Status:** Accepted

**Context:**
CC loses context between sessions. Previous work gets forgotten, leading to:
- Re-deriving already-established results
- Inconsistent claims
- Lost decisions

**Decision:**
Implement 3-layer memory system:
1. CLAUDE.md with mandatory workflow rules
2. docs/SESSION_LOG.md as append-only bookkeeping
3. Git hooks/CI to enforce documentation updates

**Rationale:**
- CC is stateless — treat it as a tool, not collaborator
- Externalize memory to repo
- Force documentation through automation

**Alternatives considered:**
- Trust CC to remember: rejected (doesn't work)
- Manual reminders: rejected (unreliable)

**Consequences:**
- Created docs/ directory with 5 mandatory files
- Created CLAUDE.md with workflow rules
- Git hook planned (not yet implemented)

---

## Open Decisions (Pending)

### PENDING-001: Unique Value for L₀/δ
How to resolve π² vs 9.33 tension?

### PENDING-002: Derive Prefactor A
What calculation method for fluctuation determinant?

### PENDING-003: Pure G_F Derivation
How to derive weak coupling without circular input?


# ============================================================================
# DOCUMENT 6: TP-2026-01-20_EDC_Synthesis_Key_Findings.md
# Source: ../EDC_Research_PRIVATE/kb/turning_points/TP-2026-01-20_EDC_Synthesis_Key_Findings.md
# ============================================================================

# TURNING POINT: EDC Sinteza — Ključni Nalazi

**Datum:** 2026-01-20
**Status:** KANONSKI DOKUMENT — ne modificirati bez razloga
**Svrha:** Spriječiti ponavljanje istih otkrića i kruženje u krugovima

---

## 1. DERIVIRANE FUNDAMENTALNE KONSTANTE (BEZ FITANJA)

| Količina | EDC Formula | Predviđeno | Eksperiment | Greška | Status |
|----------|-------------|------------|-------------|--------|--------|
| m_p/m_e | 6π⁵ | 1836.12 | 1836.15 | 0.002% | **[Der]** |
| α⁻¹ | 6π⁵/(4π+5/6) | 136.92 | 137.04 | 0.08% | **[Der]** |
| Δm_np | 8m_e/π | 1.301 MeV | 1.293 MeV | 0.6% | **[Der]** |
| m_μ/m_e | (3/2)(1+α⁻¹) | 207.05 | 206.77 | 0.14% | **[I]** |
| m_τ/m_μ | 16π/3 | 16.76 | 16.82 | 0.37% | **[I]** |

**ZAPAMTI:** Ove formule su GEOMETRIJSKE, ne fitane. Greške < 1% bez slobodnih parametara.

---

## 2. KONCEPTUALNA SLIKA: BRANA KAO "STAKLENI PROZOR"

```
     5D BULK              BRANA (δ)           3D SVEMIR
    (Plenum)           ┌─────────┐          (Opažljivo)
                       │         │
   ════════════ ←──────│  ◀──▶  │──────→ ════════════
                       │         │
    LIJEVA             │ thick   │           DESNA
    strana             │ brane   │           strana
                       └─────────┘
```

**Ključna ideja [P]:** Brana ima DVA seta boundary conditions:
- **Lijeva strana:** BC prema 5D bulku (Plenum, energetski fluid)
- **Desna strana:** BC prema 3D opažljivom svemiru (naša fizika)

Fizika 5D je UZROK, 3D opažanja su POSLJEDICA.

---

## 3. EPISTEMOLOGIJA: 5D vs 3D — KAUZALNOST I PRECIZNOST

### 3.1 Kauzalni smjer (JEDNOSMJERAN)

```
     5D (UZROK)                      3D (POSLJEDICA)
    ──────────────────────────────────────────────────
    Geometrija brane        →       Masa elektrona
    Junction konfiguracija  →       Masa protona
    Membrana tension σ      →       Nuklearne skale
    Z₆ breaking             →       Δm_np

    AKO SE 5D PROMIJENI     →       3D SE MIJENJA

    ALI:
    3D mjerenja             ✗→      NE MOGU promijeniti 5D
```

**Pitanje:** Što se treba dogoditi da se fizika i mjerenja u 3D promjene?
**Odgovor:** Mora se promijeniti nešto u 5D. Mi u 3D NE MOŽEMO direktno utjecati na 5D.

### 3.2 Preciznost: Egzaktnost vs Pogreška mjerenja

```
     5D (LIJEVA STRANA)              3D (DESNA STRANA)
    ─────────────────────────────────────────────────────
    EGZAKTNA MATEMATIKA              MJERENJA S POGREŠKOM

    6π⁵ = 1836.1181346...           1836.15267343 ± 0.00000011
    (beskonačno precizan)            (ograničena preciznost)

    ČISTA GEOMETRIJA                 REALNI INSTRUMENTI
    π, e, geometrijski faktori       detektori, vaganje, brojanje

    NEMA POGREŠKE*                   UVIJEK IMA POGREŠKU (±σ)
```

***IZNIMKA:** Ako 5D derivacija koristi bilo koju vrijednost iz 3D mjerenja,
tada nasljeđuje pogrešku tog mjerenja. Čista 5D geometrija → egzaktan broj.

### 3.3 Kalibracija vs Validacija — KRITIČNA DISTINKCIJA

| Pojam | Definicija | Primjer | Status |
|-------|------------|---------|--------|
| **Kalibracija [Cal]** | Fitanje parametra DA BI SE dobio rezultat | "Namjestimo V_B da dobijemo τ_n = 878.4 s" | Parametar ovisi o mjerenju |
| **Validacija** | Model PREDVIĐA rezultat BEZ fitanja | "6π⁵ = 1836.12, eksperiment kaže 1836.15" | Uspjeh modela |
| **Činjenica [BL]** | Mjerenje koje JEST (± pogreška) | m_p/m_e = 1836.15267343(11) | Input za validaciju |

**KLJUČNO:** 3D činjenice [BL] NISU kalibracija — one su TVRDI FAKTI.
- Ako EDC iz čiste geometrije (bez slobodnih parametara) kaže m_p/m_e = 6π⁵
- I to se poklapa s mjerenjem unutar razumne greške
- → To je **PREDIKCIJA koja je VALIDIRANA**, NE kalibracija!

### 3.4 Pogreška mjerenja je REALNOST, ne mana

Svako 3D mjerenje ima pogrešku ±σ jer:
- Instrumenti nisu savršeni
- Kvantna mehanika postavlja granice (Heisenberg)
- Statistička fluktuacija u konačnom broju mjerenja

To NIJE problem — to je REALNOST 3D svemira i naše sposobnosti mjerenja.

5D matematika je egzaktna. 3D mjerenja su aproksimacije stvarnosti.

---

## 4. FILOZOFSKA IMPLIKACIJA: "THREE-BODY PROBLEM" SCENARIJ

### 4.1 EDC vs Standard Model — Priroda konstanti

```
STANDARD MODEL                      EDC
─────────────────────────────────────────────────────────
Konstante su...                    Konstante su...
FUNDAMENTALNE                      GEOMETRIJSKE POSLJEDICE

α = 1/137.036...                   α = f(5D geometrija)
"Jednostavno jest tako"            "Jer brana ima tu strukturu"

Može li se α promijeniti?          Može li se α promijeniti?
NE (bez razloga zašto)             DA — ako se 5D promijeni

Tko može promijeniti?              Tko može promijeniti?
Nitko (nema mehanizma)             Entitet s pristupom 5D
```

### 4.2 Scenarij: Vanjska inteligencija

Ako postoji entitet s pristupom 5D bulk-u (analogno Trisolarima u "Three-Body Problem"):

```
"VANJSKA INTELIGENCIJA" s pristupom 5D bulk-u
                │
                ▼
        Mijenja geometriju brane
        Mijenja membrane tension σ
        Mijenja junction topologiju
                │
                ▼
        MI U 3D MJERIMO DRUGE VRIJEDNOSTI

        α se promijenio!
        m_p/m_e se promijenio!
        Nuklearna fizika je drugačija!
```

### 4.3 Ključna razlika

| Pitanje | Standard Model | EDC |
|---------|----------------|-----|
| Zašto je α = 1/137? | Nema odgovora | Geometrija 5D brane |
| Može li se α promijeniti? | Ne (aksiom) | Da (promjenom 5D) |
| Postoji li mehanizam? | Ne | Da (5D manipulacija) |
| Tko bi mogao? | Nitko | Entitet u 5D |

**ZAKLJUČAK [P]:** U EDC-u, "fundamentalne konstante" NISU fundamentalne —
one su EMERGENTNE iz 5D geometrije. Teoretski, entitet koji može
manipulirati 5D mogao bi mijenjati našu 3D fiziku.

Ovo ne znači da takav entitet postoji — samo da EDC DOPUŠTA takvu mogućnost,
dok Standard Model je NE DOPUŠTA jer nema mehanizam.

---

## 5. SIGMA DERIVACIJA — POD HIPOTEZOM

### 3.1 Lijeva strana (5D Uzrok)

**Ključna hipoteza [P]:**
```
E_σ = m_e c² / α = 70.0 MeV
```
Ovo je energetska skala membrane — PRETPOSTAVKA, ne derivacija!

**Derivacija membrane tension σ [Dc] (uvjetno na hipotezu):**
```
σ = E_σ / r_e² = (m_e c²/α) / r_e²

Koristeći r_e = αℏ/(m_e c):

σ = (m_e c²/α) × (m_e c/αℏ)² = m_e³ c⁴ / (α³ ℏ²)

Numerički: σ = 8.82 MeV/fm²
```

**VAŽNO:** σ formula je [Dc], NE [Der]. Ovisi o hipotezi E_σ = m_e c²/α.

### 3.2 Desna strana (3D Opažanje)

- E_σ = σ × r_e² = 70 MeV ✓ (matches nuclear scale)
- Attempt frequency: Γ₀ = m_e c² / (α ℏ)

### 3.3 KRITIČNO: Dvije vrijednosti σr_e²

| Izvor | Formula | Vrijednost | Dokument |
|-------|---------|------------|----------|
| Companion H | E_σ = m_e c²/α | **70 MeV** | weak interactions |
| Framework v2.0 | σr_e² = (36/π)m_e | **5.856 MeV** | Z₆ geometry |

**Omjer: 70 / 5.856 = 12 (TOČNO!)**

---

## 6. FAKTOR 12 — Z₆ × Z₂ STRUKTURA [I]

### 6.1 Matematička veza
```
12 = 6 × 2 = |Z₆| × |Z₂|
```

### 6.2 Fizikalna interpretacija (HIPOTEZA)
- **σr_e² = 5.856 MeV** = energija PO JEDNOJ POZICIJI na Z₆ prstenu
- **E_σ = 70 MeV** = UKUPNA energija membrane (sve pozicije + faze)
- **Veza:** E_σ = 12 × (σr_e²)_single

### 6.3 Dodatna potvrda: S/ℏ = 60
```
S/ℏ = 60 ≈ 12 × ln(1/α) + 1 = 12 × 4.92 + 1 ≈ 60.04
```
Opet faktor 12 pojavljuje se u barrier action!

**ZAKLJUČAK:** Faktor 12 = Z₆ × Z₂ nije slučajnost. Potrebna rigorozna derivacija.

---

## 7. TOPOLOŠKA STRUKTURA ČESTICA

### 7.1 Elektron [Der]
```
Topologija: B³ (3D kugla) — jednostavni vrtlog
Konfiguracija: Vol(B³) = 4π/3
Naboj: W = -1 (winding number)
Stabilnost: Izoperimetrijski teorem → JEDINSTVEN minimum
```

### 7.2 Proton [Der]
```
Topologija: Y-junction (3 kraka pod 120°)
Konfiguracija: S³ × S³ × S³ → (2π²)³
Naboj: W = +1 (ukupni winding)
Boja: 3 kraka = 3 QCD boje (8 modova = 8 gluona)
Stabilnost: Steinerov teorem → 120° JEDINSTVEN minimum
```

### 7.3 Neutron [Dc]
```
Topologija: Asimetrični Y-junction (θ = 60°)
Parametar: q = 1/3 (half-Steiner)
Naboj: W = 0, Q = 0
Nestabilnost: Može relaksirati θ: 60° → 0° (prema protonu)
```

### 7.4 Z₆ simetrija [Dc]
```
Z₆ = Z₃ × Z₂
├── Z₃: Ciklička permutacija 3 kraka (θ → θ + 120°)
└── Z₂: Oscilacijska faza (φ → φ + π)

Proton: θ = 0° (minimum)
Neutron: θ = 60° (metastabilno)
Formula: θ = (1 - Q) × 60°
```

---

## 8. WEAK INTERAKCIJE — COMPANION H MODEL

### 8.1 Struktura
```
BULK-CORE (Y-junction: |0⟩=proton, |1⟩=neutron)
    │
    ▼ pumping kroz frozen boundary
    │
BRANE-LAYER (debljina δ, lokalizirani modovi)
    │
    ▼ izlaz na observer-facing stranu
    │
3D ČESTICE (e⁻, ν̄_e)
```

### 8.2 Jednosmjerni ventil [P]
- **Inflow** (bulk → brane): DOZVOLJEN (spontan)
- **Outflow** (brane → bulk): POTISNUT

### 8.3 β⁻ decay mapping
```
5D uzrok: n(|1⟩) → p(|0⟩), junction rotira θ: 60° → 0°
3D opažanje: n → p + e⁻ + ν̄_e
```

---

## 9. KALIBRACIJE vs DERIVACIJE

### 9.1 Kalibrirano [Cal] — potrebne derivacije
| Parametar | Vrijednost | Kalibriran na | Potrebno |
|-----------|------------|---------------|----------|
| V_B (barrier height) | ~2.6 MeV | τ_n = 878.4 s | Derivacija iz 5D akcije |
| V₃ (flavor-breaking) | -0.65 MeV | Δm_np = 1.293 MeV | Derivacija iz Z₆ |
| S/ℏ | 60 | τ_n = 878.4 s | Veza s 12×ln(1/α)+1 |

### 9.2 Derivirano [Der] / [Dc] — potvrđeno
- m_p/m_e = 6π⁵ iz Vol(B³) i Area(S³)³
- α iz geometrijskih faktora
- Δm_np iz Z₆ breaking
- 120° Steiner angles iz varijacijskog principa
- SU(3) algebra iz Y-junction modova
- Confinement iz beskonačne string energije
- **Frozen criterion [Dc]** iz 5D akcije (Paper 2, dva puta: instanton + topološka)
- **C = 4π/3 [Der]** za step funkciju (egzaktno, parameter-free)

---

## 10. OTVORENI PROBLEMI — PRIORITETI

### 10.1 KRITIČNI (moraju se riješiti)
| ID | Problem | Trenutni status |
|----|---------|-----------------|
| **KB-OPEN-033** | Deriviraj V_B iz 5D akcije | [Cal] |
| **KB-OPEN-040** | Razriješi σr_e² = 70 vs 5.856 MeV (faktor 12) | [OPEN] |
| **KB-OPEN-041** | Deriviraj S/ℏ = 12×ln(1/α)+1 | [I] pattern |

### 10.2 VAŽNI (za kompletnost)
- Neutrino kao ξ-val — dinamika
- 5/6 faktor u α formula

### 10.3 VEĆ RIJEŠENI (dokumentirano u Paper 2)

| Problem | Rješenje | Dokument |
|---------|----------|----------|
| Frozen boundary iz 5D akcije | **DVA PUTA:** Route A (instanton) + Route B (topološka) | `EDC_FROZEN_Criterion_From_Action_v1.tex` |
| Step funkcija implementacija | `f(r) = Θ(r-a)` → C = 4π/3 EGZAKTNO | `appendix_gl_frozen_numerics.py` |
| GL vs Frozen usporedba | Frozen je parameter-free, GL zahtijeva fine-tuning | Python numerika |

**Route A (Large-σ Instanton Barrier) [Dc]:**
```
Γ ∼ Γ₀ exp(-σ·ΔA/ℏ)
Frozen criterion: σ·ΔA_min > ℏ·ln(Γ₀·τ_obs)
```

**Route B (Topological Superselection) [Dc]:**
```
B1 [M]: Winding numbers su topološki invarijanti
B2 [P]: Nema topology-changing procesa tijekom τ_obs
B3 [Dc]: Γ = 0 (egzaktno, ne aproksimativno)
```

**Python step funkcija:**
```python
def frozen_profile(r, a):
    return np.where(r < a, 0.0, 1.0)  # Θ(r-a)
```

---

## 11. METODOLOŠKI PRINCIPI — NE ZABORAVI

### 11.1 Dvosmjerno čitanje
```
LIJEVA STRANA (5D)          DESNA STRANA (3D/4D)
─────────────────────────────────────────────────
5D geometrija         →     Opažene čestice
Bulk + brane akcija   →     Mase, naboji, lifetime
Topološki defekti     →     Elektron, proton, neutron
Junction dinamika     →     Weak decay
```

### 11.2 Epistemički kodovi
| Kod | Značenje | Primjer |
|-----|----------|---------|
| **[Der]** | Derivirano | m_p/m_e = 6π⁵ |
| **[Dc]** | Derivirano uvjetno | M(q), V(q) pod ansatzom |
| **[I]** | Identificirano | m_μ/m_e pattern |
| **[Cal]** | Kalibrirano | V_B na τ_n |
| **[P]** | Postulirano | 5D bulk postoji |
| **[BL]** | Baseline | PDG/CODATA vrijednosti |

### 11.3 Anti-cirkularity check
- NIKADA ne koristi X da deriviraš Y ako Y ovisi o X
- [BL] fakti su INPUTI za validaciju, ne za derivaciju
- Ako model reproducira [BL] → to je VALIDACIJA, ne kružnost

---

## 12. HIJERARHIJA DOKUMENATA — COMPANION F KAO "BACKBONE"

### 12.1 Zašto je F kičma serije?

**Kanonski opis:**
> "Companion F provides the 5D object model (proton as a junction) and the
> canonical 5D→brane→3D projection mechanism (Hopf + thick-brane + frozen
> boundary), which the weak and decay companions then use as process-level
> applications."

### 12.2 Šest razloga zašto F nosi kičmu

| # | Razlog | Objašnjenje |
|---|--------|-------------|
| 1 | **Ontologija** | F daje "ŠTO proton JEST" u 5D, ne samo "što izračunamo" |
| 2 | **120° nije QCD** | Steiner optimum dolazi iz geometrije minimizacije, ne iz SU(3) |
| 3 | **Hopf bridge** | Rješava S³ vs S² konfuziju: interno S³ → opažajno S² |
| 4 | **Frozen mehanizam** | Nije samo "fraza" — boundary law s kriterijem |
| 5 | **Epistemic kontrola** | Eksplicitne kutije [Der]/[Dc]/[P]/[OPEN] sprječavaju overclaim |
| 6 | **Spojni komad** | Povezuje Paper 2, Framework, G, H u koherentnu cjelinu |

### 12.3 Struktura luka dokumenata

```
Framework v2.0
    │   Formalna konzervacija + ledger, 5D zatvaranje
    │   = AKSIOMATIKA / PRAVILA IGRE
    ▼
Paper 2 (Frozen)
    │   Frozen režim i projekcija (temelj mapiranja)
    │   = PROJEKCIJSKI MEHANIZAM
    ▼
╔═══════════════════════════════════════════════════════╗
║  COMPANION F (Proton Junction) — BACKBONE             ║
║  • Konkretan 5D objekt (junction + 3 kraka)           ║
║  • Geometrija (120° Steiner optimum)                  ║
║  • Projekcija 5D→brane→3D (Hopf + thick-brane)        ║
║  = ONTOLOGIJA + PROJEKCIJA                            ║
╚═══════════════════════════════════════════════════════╝
    │
    ├──► Companion G (n–p mass)
    │       Kako odstupanje/nesimetrija daje Δm
    │       = FENOMENOLOGIJA (masa)
    │
    └──► Companion H (weak)
            Kako relaksacija isporuči energiju brani → e⁻ + ν̄
            = FENOMENOLOGIJA (procesi)

Companions A–E: Specifične redukcije i alati
```

### 12.4 Što F rješava za čitatelja

| Pitanje čitatelja | Odgovor u F |
|-------------------|-------------|
| "Što je proton u 5D?" | Junction s 3 kraka, 120° kutovi |
| "Zašto 120°?" | Steiner/Lami optimum (geometrija, ne QCD) |
| "Zašto S³ interno, a S² vidimo?" | Hopf fibration: ψ ∈ S³ → t̂ ∈ S² |
| "Kako 5D postaje 3D?" | Frozen projection boundary + thick-brane |
| "Je li to [Der] ili [P]?" | Eksplicitne epistemic oznake |

### 12.5 Bez F, G i H "vise u zraku"

- **S F:** G i H su "process-level applications" jasnog objekta
- **Bez F:** G i H izgledaju kao "modeli procesa" bez slike objekta

F daje **sidro** — čitatelj zna na što se odnose efektivne veličine (q, V(q), selection rules).

---

## 13. DOKUMENT REFERENCE

| Dokument | DOI | Ključni sadržaj |
|----------|-----|-----------------|
| Framework v2.0 | 10.5281/zenodo.18299085 | Svi postulati, σr_e²=5.856 MeV |
| **Paper 2** | (lokalno) | **Frozen derivacija, step funkcija, C=4π/3** |
| Paper 3 | 10.5281/zenodo.18262721 | Neutron lifetime WKB |
| Companion F | 10.5281/zenodo.18302953 | Proton Y-junction |
| Companion G | 10.5281/zenodo.18303494 | Δm_np, σr_e²=70 MeV |
| Companion H | 10.5281/zenodo.18307539 | Weak interactions, E_σ=70 MeV |

**Paper 2 ključni fajlovi:**
- `releases/paper_2_private/supplementary/postulate_derivations/EDC_FROZEN_Criterion_From_Action_v1.tex`
- `releases/paper_2_private/code/numerics/appendix_gl_frozen_numerics.py`

---

## 14. COMPANION N: NEUTRON KAO UZBUĐENI 5D JUNCTION — PLAN

### 14.1 Uloga u seriji

Companion N daje **objekt-model neutrona** u 5D, analogno Companion F za proton.

**Kanonski opis:**
> "In EDC, the neutron is modeled as an excited 5D junction state: the same
> three-arm junction core as the proton, but displaced from the local Steiner
> minimum. This excitation couples to the bulk-facing side of a thick brane,
> pumping energy into brane-layer modes. The observer-side frozen projection
> then organizes the released energy into allowed weak-channel outputs."

### 14.2 Ontologija: Što je neutron u 5D [P]

```
PROTON (Companion F)              NEUTRON (Companion N)
────────────────────────────────────────────────────────
Isti topološki junction           Isti topološki junction
3 kraka + čvor                    3 kraka + čvor + ring mode

Steiner minimum (120°)            UZBĐENO STANJE (θ ≠ 120°)
Statički minimum energije         Metastabilni paket

STABILAN                          NESTABILAN → relaksira prema protonu
```

**Ključ [P]:** Neutron NIJE "druga životinja" — nego pobuđeni režim ISTE 5D geometrije.

### 14.3 Relaksacija prema 120° [Der/Dc]

Odstupanje od optimuma:
```
θ_i(t) = 2π/3 + δθ_i(t)     gdje δθ_i ≠ 0 znak uzbuđenja [Def]
```

**Lemma [Dc]:** Svako |δθ| nosi geometrijsku energiju:
```
E_geom ~ κ_θ (δθ)²          (Taylor oko minimuma)
```

Nema novih brojeva — samo: "ako minimum postoji, odstupanje ima energiju i vraća se".

### 14.4 Junction + Ring Mode (Harmonički oscilator) [P/I]

**Model [P]:** Kolektivni način pobude (ring/collective constraint) veže tri kraka tako da ne mogu odmah pasti u Steiner minimum → sustav OSCILIRA oko metastabilnog položaja.

**Heuristic Interpretation [I/P]:** U 1D efektivi:
```
ẍ + 2γẋ + ω₀²x = 0

gdje:
  γ  = efektivno prigušenje (brane-dissipation) [OPEN]
  ω₀ = "stiffness" krakova [P]
```

**BITNO:** Ovo nije "SM oscillator" — ovo je mehanička linearizacija oko geometrijskog minimuma.

### 14.5 Thick-Brane Pumpa [P/OPEN]

```
     BULK-CORE                BRANE LAYER (δ)           OBSERVER
   (junction relaksira)    ┌─────────────────┐        (3D čestice)
                           │                 │
   x(t) oscilira  ───────► │  φ(y,t) modes   │ ───────►  e⁻ + ν̄
                           │                 │
                      y=-δ/2              y=+δ/2
                    bulk-facing        observer-facing
```

**Coupling [P/OPEN]:**
```
L_int ~ g · x(t) · φ(y=-δ/2, t)
```

**Ledger closure:** Energija se zatvara u 5D, brana prima inflow J^ν_bulk→brane (Framework v2.0, Remark 4.5) [BL].

### 14.6 Frozen Projection: Zašto 3D čestice [Dc/P]

1. Neutron nastaje u frozen režimu → energija "zaključana" [Dc/P]
2. Bulk-core relaksira prema proton optimumu → energija u branu [P]
3. Observer-facing frozen projekcija "izbacuje" dopuštene izlaze [Dc/P]:
   - e⁻ + ν̄ + recoil
   - BEZ tvrdnje da smo izveli V–A!

**Minimalna, sigurna formulacija:**
> "In EDC, neutron decay is modeled as relaxation of an excited 5D junction
> that pumps energy into the brane layer; the observer-side frozen projection
> organizes that energy into allowed weak-channel outputs."

### 14.7 Kompatibilnost s Paper 3 WKB [OPEN]

Dva efektivna opisa ISTOG prijelaza:

| Opis | Dokument | Status |
|------|----------|--------|
| WKB kroz barijeru u V(q) | Paper 3 | [Dc/Der] u 1D |
| Mehanika metastabilnosti + brane pumping | Companion N | [P/OPEN] |

**Bridge statement [OPEN]:**
> Cilj: pokazati limit u kojem dissipativni model reducira na efektivnu WKB stopu (ili obrnuto).

### 14.8 Cornerstone Box (Short) — za početak papera

```
┌─────────────────────────────────────────────────────────────────────┐
│  CORNERSTONE (Neutron in EDC)                                       │
├─────────────────────────────────────────────────────────────────────┤
│  In the EDC program, the neutron is modeled as an excited 5D        │
│  junction state: the same three-arm junction core as the proton,    │
│  but displaced from the local Steiner minimum (the universal 120°   │
│  optimum in the tangent metric). This excitation couples to the     │
│  bulk-facing side of a thick brane, pumping energy into brane-layer │
│  modes. The observer-side frozen projection boundary then organizes │
│  the released energy into allowed weak-channel outputs (e.g., e⁻    │
│  and ν̄), while overall bulk–brane conservation remains anchored    │
│  to Framework v2.0, Remark 4.5.                                     │
│                                                                     │
│  Epistemic status:                                                  │
│  • 120° as local optimum: [Der]/[Dc] (geometric)                    │
│  • Thick-brane pumping + frozen output mapping: [P]/[OPEN]          │
└─────────────────────────────────────────────────────────────────────┘
```

### 14.9 Epistemic Tags Summary

| Tvrdnja | Status | Komentar |
|---------|--------|----------|
| 120° Steiner optimum | [Der/Dc] | Geometrijski, iz F |
| Neutron = excited junction | [P] | Object assumption |
| Ring/collective mode | [P] | Model |
| Thick-brane coupling | [OPEN] | Mikrofizika |
| Damping γ | [OPEN] | Mehanizam nepoznat |
| Frozen projection output | [Dc/P] | Paper 2 / Companion H |
| Ledger closure | [BL] | Framework v2.0, Remark 4.5 |

---

## 15. SLJEDEĆI KORACI (2026-01-21+)

### 15.1 Prioriteti istraživanja

| # | Zadatak | Status | Napomena |
|---|---------|--------|----------|
| 1 | **Companion N** — Neutron backbone LaTeX | PLAN SPREMAN (Sekcija 14) | Cornerstone box gotov |
| 2 | Faktor 12 = Z₆ × Z₂ derivacija | [OPEN] | Je li 70/5.856 = 12 namjerno? |
| 3 | S/ℏ = 12×ln(1/α)+1 geometrija | [I] → [Der]? | Potvrdi numerički, traži objašnjenje |
| 4 | V_B derivacija iz 5D akcije | [Cal] → [Der]? | Ako uspije → τ_n PREDIKCIJA |

### 15.2 Companion N — Checklist za izradu

- [ ] Kreirati LaTeX strukturu (F-style: tcolorbox, epistemic tags)
- [ ] Cornerstone box (tekst spreman u 14.8)
- [ ] Sekcije: Ontologija, Steiner relaxation, Oscillator, Thick-brane, Frozen, WKB bridge
- [ ] Related Documents blok s DOI-ima
- [ ] Build PDF + dodati u INVENTORY.md + SHA256SUMS.txt

---

## 16. UPOZORENJE ZA BUDUĆEG CLAUDEA

**OBAVEZNO PROČITAJ PRIJE RADA:**

1. **NE ponavljaj analize** koje su već napravljene (vidi sekcije 1-14)

2. **Ključni rezultati:**
   - σ = m_e³c⁴/(α³ℏ²) je **[Dc]** (POD hipotezom E_σ = m_e c²/α)
   - Faktor 12 i S/ℏ=60 su **[I]** patterni — istraži ih
   - Frozen derivacija je **GOTOVA** u Paper 2

3. **Konceptualne slike:**
   - Brana = "stakleni prozor" (LIJEVA=5D, DESNA=3D)
   - 5D je UZROK, 3D su OPAŽANJA
   - 3D činjenice [BL] su VALIDACIJA, ne kalibracija

4. **Hijerarhija dokumenata:**
   - Companion F = BACKBONE za proton
   - Companion N = BACKBONE za neutron (plan u sekciji 14)

5. **Filozofska implikacija:**
   - EDC DOPUŠTA promjenu konstanti (5D manipulacija)
   - SM NE DOPUŠTA (nema mehanizam)

---

*Dokument kreiran: 2026-01-20*
*Zadnja izmjena: 2026-01-20*
*Autori: Claude Opus 4.5 + Igor Grčman*
*Verzija: 1.0 (kanonski)*


# ============================================================================
# DOCUMENT 7: ANTI_PATTERNS_3D_TRAPS.md
# Source: ../EDC_Research_PRIVATE/kb/5d_universe/ANTI_PATTERNS_3D_TRAPS.md
# ============================================================================

# Anti-Patterns: 3D Traps to Avoid

**Knowledge Base: 5D Universe**
**Last Updated:** 2026-01-13

---

## Purpose

Comprehensive catalog of errors where 3D intuition leads to incorrect 5D physics.
**MEMORIZE THESE TRAPS.** They have destroyed derivations.

---

## THE GOLDEN RULE

> **NEVER trust your 3D intuition in 5D calculations.**
> Every geometric factor must be DERIVED, not assumed.

---

## KB Entries: 3D Traps

---

### KB-TRAP-001: Wrong Volume Formula (4π/3 vs 2π²)

**Status:** VERIFIED (Known error pattern)
**Scope:** Any calculation involving "spherical" objects
**Dependencies:** KB-VOL-003, KB-VOL-004
**Pitfalls:** This is the #1 most common error

**The Trap:**
Using $V = \frac{4\pi}{3}r^3$ for a "sphere" in 5D without checking which sphere.

**Why It's Wrong:**
- $\frac{4\pi}{3}r^3$ = Vol(B³) = volume of 3-ball in ℝ³
- $2\pi^2 r^3$ = Vol(S³) = volume of 3-sphere in ℝ⁴

In EDC, particles are S³ defects (boundary of B⁴), NOT B³ objects.

**Correct Approach:**
1. Identify embedding dimension
2. Determine if you need ball (Bⁿ) or sphere (Sⁿ⁻¹)
3. Use correct formula from KB-VOL-001 or KB-VOL-002

**Error Cost:** Factor of ~4.7 error in mass calculations

---

### KB-TRAP-002: Wrong Surface Area (4π vs 2π²)

**Status:** VERIFIED (Known error pattern)
**Scope:** Flux calculations, boundary terms
**Dependencies:** KB-VOL-002
**Pitfalls:** Leads to wrong flux quantization

**The Trap:**
Using $A = 4\pi r^2$ for any "spherical surface" in 5D.

**Why It's Wrong:**
- $4\pi r^2$ = Area(S²) = surface of 2-sphere
- $2\pi^2 r^2$ = "Area"(S³) = the 3-volume of S³ at radius r

**Correct Approach:**
Match surface formula to the dimensionality of the object.

---

### KB-TRAP-003: Wrong Radial Integration Measure

**Status:** VERIFIED (Known error pattern)
**Scope:** Energy integrals, volume integrals
**Dependencies:** KB-VOL-006
**Pitfalls:** Invalidates entire derivations

**The Trap:**
Using $\int 4\pi r^2 dr$ as the "spherical radial measure" in 5D.

**Why It's Wrong:**
| Dimension | Correct Measure |
|-----------|-----------------|
| 3D | $4\pi r^2 dr$ |
| 4D | $2\pi^2 r^3 dr$ |
| 5D | $(8\pi^2/3) r^4 dr$ |

**Correct Approach:**
Always use $\int r^{n-1} d\Omega_{n-1} dr$ with correct n.

---

### KB-TRAP-004: S³ = S² (Dimensional Confusion)

**Status:** VERIFIED (Known error pattern)
**Scope:** Topology arguments, defect classification
**Dependencies:** KB-GEO-005
**Pitfalls:** Wrong topology = wrong physics

**The Trap:**
Thinking S³ is "just a bigger S²" or "a 3D sphere."

**Why It's Wrong:**
- S² = 2-sphere = surface of ball in ℝ³ = {x² + y² + z² = r²}
- S³ = 3-sphere = surface of ball in ℝ⁴ = {x² + y² + z² + w² = r²}

They have completely different topology:
- π₃(S²) = ℤ (Hopf fibration)
- π₃(S³) = ℤ (identity map)

**Correct Approach:**
Always specify the EMBEDDING dimension, not just the sphere number.

---

### KB-TRAP-005: "Particle is a Ball in 3D Space"

**Status:** VERIFIED (Known error pattern)
**Scope:** All particle models
**Dependencies:** KB-GEO-003, KB-POST-004
**Pitfalls:** Fundamentally wrong picture

**The Trap:**
Visualizing a particle as a "little ball" sitting in 3D space.

**Why It's Wrong:**
In EDC, particles are:
- Topological DEFECTS, not balls
- Located at ξ = 0 (membrane) or extending through bulk
- Have S³ topology (boundary condition in 4D)
- "Radius" a is defect core size, not a ball radius

**Correct Approach:**
Think of particles as:
- Vortex cores on membrane (electron)
- Y-junctions through bulk (proton)
- NOT as "tiny balls of stuff"

---

### KB-TRAP-006: Projecting Without Integration

**Status:** VERIFIED (Known error pattern)
**Scope:** 5D → 4D effective physics
**Dependencies:** KB-GEO-007
**Pitfalls:** Loses factors of 2πR_ξ or worse

**The Trap:**
"Projecting" a 5D quantity to 4D by just dropping ξ.

**Why It's Wrong:**
Proper dimensional reduction requires:
$$Q_{4D} = \int_0^{2\pi R_\xi} Q_{5D}(x^\mu, \xi) \, d\xi$$

The ξ-integral may give:
- Factors of 2πR_ξ (zero modes)
- Sums over KK modes
- Boundary terms from compactification

**Correct Approach:**
Always perform explicit integration over ξ.

---

### KB-TRAP-007: Wrong Energy Density Units

**Status:** VERIFIED (Known error pattern)
**Scope:** Dimensional analysis
**Dependencies:** KB-GEO-007
**Pitfalls:** Factor errors that look "small"

**The Trap:**
Using [J/m³] for energy density in 5D.

**Why It's Wrong:**
| Space | Energy Density Units |
|-------|---------------------|
| 5D bulk | [J/m⁴] |
| 4D membrane | [J/m³] (after ξ-integration) |
| 3D spatial | [J/m³] |
| 2D surface | [J/m²] = σ |

**Correct Approach:**
Track dimensions at every step. ρ₄ ≠ ρ₃.

---

### KB-TRAP-008: "Membrane is 3D"

**Status:** VERIFIED (Known error pattern)
**Scope:** All brane physics
**Dependencies:** KB-GEO-003
**Pitfalls:** Wrong counting of degrees of freedom

**The Trap:**
Calling the membrane "3D" because we live in "3D space."

**Why It's Wrong:**
- Membrane Σ⁴ is 4-DIMENSIONAL (3 space + 1 time)
- The spatial slice Σ³ is 3-dimensional
- This distinction matters for action principles

**Correct Approach:**
Use "4D membrane" or "Σ⁴" for spacetime membrane.
Use "Σ³" or "spatial slice" for 3D space.

---

### KB-TRAP-009: Sign of 5th Dimension

**Status:** VERIFIED (Known error pattern)
**Scope:** Metric calculations
**Dependencies:** KB-GEO-002
**Pitfalls:** Flips sign of mass terms

**The Trap:**
Treating ξ as just "another spatial dimension" without checking signature.

**Why It's Wrong:**
The sign ε in $ds^2 = ... + \varepsilon \, d\xi^2$ determines:
- ε = +1: spacelike extra dimension
- ε = -1: timelike extra dimension

These give DIFFERENT physics (stability, causality, etc.).

**Correct Approach:**
Always specify ε and track its effects on signs.

---

### KB-TRAP-010: "Obviously 4π"

**Status:** VERIFIED (Known error pattern)
**Scope:** All geometric calculations
**Dependencies:** None
**Pitfalls:** Hidden 3D assumption

**The Trap:**
Writing "the factor is obviously 4π" without derivation.

**Why It's Wrong:**
In 5D, "obvious" factors change:
- 4π → 2π² (for S³)
- 4π/3 → π²/2 (for B⁴)
- 1/r² → 1/r³ (for 4D force law)

**Correct Approach:**
NEVER use "obviously" for geometric factors.
ALWAYS derive from integral or definition.

---

### KB-TRAP-011: Wrong Counting of DOF

**Status:** VERIFIED (Known error pattern)
**Scope:** Particle physics, field theory
**Dependencies:** KB-GEO-001
**Pitfalls:** Wrong number of particles, gauge bosons

**The Trap:**
Counting degrees of freedom as if in 4D.

**Why It's Wrong:**
| Object | 4D DOF | 5D DOF |
|--------|--------|--------|
| Scalar | 1 | 1 (but KK tower) |
| Vector | 4 | 5 (but A_ξ special) |
| Metric | 10 | 15 |

KK decomposition adds infinite towers of states.

**Correct Approach:**
Count in 5D first, then reduce.

---

### KB-TRAP-012: Boundary Conditions from 3D Intuition

**Status:** VERIFIED (Known error pattern)
**Scope:** All field equations
**Dependencies:** KB-GEO-001
**Pitfalls:** Misses junction conditions

**The Trap:**
Assuming "natural" boundary conditions without derivation.

**Why It's Wrong:**
5D boundary conditions include:
- Membrane junction conditions (Israel)
- Compactification conditions (periodic, orbifold)
- Behavior at ξ → ∞
- Source conditions at defects

**Correct Approach:**
Derive ALL boundary conditions from the action.

---

### KB-TRAP-013: Mass vs Energy in 5D

**Status:** VERIFIED (Known error pattern)
**Scope:** Particle mass formulas
**Dependencies:** KB-POST-003
**Pitfalls:** mc² = E only in rest frame

**The Trap:**
Equating 5D energy directly to 4D mass.

**Why It's Wrong:**
The 5D energy includes:
- Rest mass contribution
- KK momentum (p_ξ = n/R_ξ)
- Kinetic energy

4D mass emerges after projecting out ξ-dependence.

**Correct Approach:**
$$m_{4D}^2 c^4 = E_{5D}^2 - p_\xi^2 c^2$$

---

### KB-TRAP-014: Assuming Spherical Symmetry

**Status:** VERIFIED (Known error pattern)
**Scope:** Particle models, especially proton
**Dependencies:** None
**Pitfalls:** Proton is Y-junction, NOT sphere

**The Trap:**
Treating all particles as spherically symmetric.

**Why It's Wrong:**
- Electron: approximately spherical
- Proton: Y-junction of 3 strings (C₃ symmetry, not SO(3))
- Neutron: asymmetric Y-junction

Spherical symmetry is emergent for proton (KB-DERIV-002).

**Correct Approach:**
Derive symmetry from configuration, don't assume it.

---

### KB-TRAP-015: "Volume Ratio = Mass Ratio"

**Status:** VERIFIED (Known error pattern)
**Scope:** m_p/m_e derivation
**Dependencies:** KB-VOL-005
**Pitfalls:** Requires P-sum postulate!

**The Trap:**
Assuming $m_p/m_e = V_p/V_e$ without justification.

**Why It's Wrong:**
Standard variational principle gives:
$$E = \min_{\text{config}} \mathcal{E}$$

NOT:
$$E = \int_{\text{config}} \varepsilon \, d\mu$$

The integral (P-sum) requires a NEW physical mechanism.

**Correct Approach:**
Acknowledge P-sum as a POSTULATE until derived.

---

## Self-Check Checklist

Before finalizing ANY 5D calculation:

- [ ] Did I use any formula from 3D without verifying it in 5D?
- [ ] Are my volume/area formulas correct for the dimension?
- [ ] Did I handle the ξ integration explicitly?
- [ ] Are boundary conditions derived, not assumed?
- [ ] Did I verify by dimensional analysis?
- [ ] Does the result reduce correctly in limiting cases?
- [ ] Did I avoid "obviously" for geometric factors?

---

## Error Log

| Date | Error | KB-TRAP | Location | Resolution |
|------|-------|---------|----------|------------|
| 2026-01-11 | Used "π⁵ has no geometry" | KB-TRAP-001 | Alpha_v1 | Corrected: 6π⁵ = (2π²)³/(4π/3) |

---

*Your 3D intuition is your enemy in 5D. Trust only derivations.*


# ============================================================================
# END OF CANON BUNDLE
# ============================================================================

**Total P0 documents:** 7
**Action:** Read this entire file at the start of every session. MANDATORY.
