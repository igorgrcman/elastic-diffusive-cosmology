# CANON BUNDLE — EDC_Project Workspace Level

**Generated:** 2026-01-28
**Purpose:** Single entry point for ALL canonical EDC content.
**Usage:** Read this file at the START of every CC session. MANDATORY. NO EXCEPTIONS.

---

## How to Use This Bundle

1. **This file is the MASTER ENTRY POINT** for the entire EDC_Project workspace
2. It includes workspace-level documents AND references to domain-specific canon
3. Read this entire file before doing ANY work
4. For domain-specific work (Book 2, Papers), also consult the domain's CANON_BUNDLE

---

## Workspace-Level Documents (Inline)

### WORKSPACE_MAP.md

See: `docs/WORKSPACE_MAP.md`

Key paths:
- Book 1: `elastic-diffusive-cosmology_repo/edc_book/main.tex`
- Book 2: `elastic-diffusive-cosmology_repo/edc_book_2/`
- Paper 2: `elastic-diffusive-cosmology_repo/edc_papers/paper_2/paper/main.tex`
- Paper 3: `EDC_Research_PRIVATE/releases/paper_3_private/paper/main.tex`
- KB: `EDC_Research_PRIVATE/kb/`

### CONCEPT_INDEX.md

See: `docs/CONCEPT_INDEX.md`

Key concepts defined:
- CONCEPT-001: Proton (Y-junction, 120deg Steiner)
- CONCEPT-002: Neutron (Asymmetric Y-junction, theta=60deg)
- CONCEPT-003: Electron (B^3 vortex)
- CONCEPT-010: Brane tension sigma = 8.82 MeV/fm^2 [Dc]
- CONCEPT-020: Projection principle (5D->3D)
- CONCEPT-021: Frozen boundary criterion [Dc]
- CONCEPT-030: m_p/m_e = 6pi^5 [Der]

---

## Turning Points

### TP-2026-01-28: Nuclear Topology Breakthroughs
**Location:** `docs/TP-2026-01-28_Nuclear_Topology_Breakthroughs.md`

Key discoveries:
1. **Mn Topological Model** — nuclei as topological pinning networks
2. **n = 43 forbidden** — geometric reason for nuclear matter instability
3. **Frustration-Corrected G-N Law** — 45% improvement (R² = 0.9941)
4. **τ_n ≈ 880 s from pure 5D** — no fitting, just σ, L₀, δ

### TP-2026-01-20: EDC Synthesis Key Findings
**Location:** `EDC_Research_PRIVATE/kb/turning_points/TP-2026-01-20_EDC_Synthesis_Key_Findings.md`

Key content: σ derivation, factor 12 = Z₆×Z₂, mass ratios, brane picture.

---

## Domain Canon References

### Book 2 Canon (Active Development)

**Location:** `elastic-diffusive-cosmology_repo/edc_book_2/docs/CANON_BUNDLE.md`

This bundle contains:
1. CLAUDE.md (Book 2 workflow rules)
2. STATUS.md (Current state of Book 2)
3. DERIVATIONS.md (Math chain registry)
4. TODO.md (Book 2 action items)
5. DECISIONS.md (Book 2 ADRs)
6. Turning Points (TP-2026-01-20)
7. Anti-Patterns (15 critical 3D traps)

**When working on Book 2:** Read BOTH this workspace bundle AND the Book 2 domain bundle.

### Research Private Canon

**Location:** `EDC_Research_PRIVATE/CLAUDE.md`

Contains:
- Repo policy (no branch deletion, XeLaTeX, etc.)
- EDC project context
- Turning points reference
- Epistemic codes

---

## Critical Content (Extracted from Book 2 Canon)

### Derived Fundamental Constants (NO FITTING)

| Quantity | EDC Formula | Predicted | Experiment | Error | Status |
|----------|-------------|-----------|------------|-------|--------|
| m_p/m_e | 6pi^5 | 1836.12 | 1836.15 | 0.002% | **[Der]** |
| alpha^-1 | 6pi^5/(4pi+5/6) | 136.92 | 137.04 | 0.08% | **[Der]** |
| Delta_m_np | 8m_e/pi | 1.301 MeV | 1.293 MeV | 0.6% | **[Der]** |
| m_mu/m_e | (3/2)(1+alpha^-1) | 207.05 | 206.77 | 0.14% | **[I]** |
| m_tau/m_mu | 16pi/3 | 16.76 | 16.82 | 0.37% | **[I]** |

**REMEMBER:** These formulas are GEOMETRIC, not fitted. Errors < 1% without free parameters.

### Proton Definition (Canonical)

```
Topology: Y-junction (3 arms at 120deg)
Configuration: S^3 x S^3 x S^3 -> (2pi^2)^3
Charge: W = +1 (winding number)
Color: 3 arms = 3 QCD colors (8 modes = 8 gluons)
Stability: Steiner theorem -> 120deg UNIQUE minimum
```

### Neutron Definition (Canonical)

```
Topology: Asymmetric Y-junction (theta = 60deg)
Parameter: q = 1/3 (half-Steiner)
Charge: W = 0, Q = 0
Instability: Can relax theta: 60deg -> 0deg (toward proton)
```

### Brane Picture ("Glass Window")

```
     5D BULK              BRANE (delta)           3D UNIVERSE
    (Plenum)           +-------------+          (Observable)
                       |             |
   ============= <-----+    <-->     +-----> =============
                       |             |
    LEFT               |   thick     |           RIGHT
    side               |   brane     |           side
                       +-------------+

Key idea [P]: Brane has TWO sets of boundary conditions:
- Left side: BC toward 5D bulk (Plenum, energy fluid)
- Right side: BC toward 3D observable universe (our physics)

5D physics is CAUSE, 3D observations are EFFECT.
```

### Epistemology: 5D vs 3D

**Causal direction (ONE-WAY):**
```
     5D (CAUSE)                      3D (EFFECT)
    --------------------------------------------------
    Brane geometry        ->       Electron mass
    Junction configuration ->      Proton mass
    Membrane tension sigma ->      Nuclear scales
    Z_6 breaking          ->       Delta_m_np

    IF 5D CHANGES         ->       3D CHANGES

    BUT:
    3D measurements       X->      CANNOT change 5D
```

**Calibration vs Validation — CRITICAL DISTINCTION:**

| Term | Definition | Example | Status |
|------|------------|---------|--------|
| **Calibration [Cal]** | Fitting parameter TO GET result | "Tune V_B to get tau_n = 878.4 s" | Parameter depends on measurement |
| **Validation** | Model PREDICTS result WITHOUT fitting | "6pi^5 = 1836.12, experiment says 1836.15" | Model success |
| **Fact [BL]** | Measurement that IS (with error) | m_p/m_e = 1836.15267343(11) | Input for validation |

**KEY:** 3D facts [BL] are NOT calibration — they are HARD FACTS.

### Anti-Patterns: 3D Traps (Summary)

**THE GOLDEN RULE:**
> NEVER trust your 3D intuition in 5D calculations.
> Every geometric factor must be DERIVED, not assumed.

Critical traps (see full list in Book 2 CANON_BUNDLE):
- **KB-TRAP-001:** Wrong Volume Formula (4pi/3 vs 2pi^2)
- **KB-TRAP-002:** Wrong Surface Area (4pi vs 2pi^2)
- **KB-TRAP-003:** Wrong Radial Integration Measure
- **KB-TRAP-010:** "Obviously 4pi" without derivation
- **KB-TRAP-014:** Assuming Spherical Symmetry (proton is Y-junction!)
- **KB-TRAP-015:** "Volume Ratio = Mass Ratio" (requires P-sum postulate!)

### Epistemic Tags (EDC Standard)

| Tag | Meaning | Use when... |
|-----|---------|-------------|
| **[Der]** | Derived | Explicit derivation from postulates exists |
| **[Dc]** | Derived Conditional | Derived IF certain assumptions hold |
| **[I]** | Identified | Pattern matching / mapping (not unique) |
| **[P]** | Proposed | Postulate / hypothesis / conjecture |
| **[Cal]** | Calibrated | Parameter fitted to data |
| **[BL]** | Baseline | External reference (PDG/CODATA) |
| **[M]** | Mathematics | Mathematical theorem (not EDC-specific) |

### Red Flags — STOP WORK

If you encounter any of these, STOP and ask the user:
- Dependency graph has a cycle (circularity)
- "Derivation" without explicit steps
- Numerical value used BEFORE derivation
- "Obviously..." without proof
- More than 3 free parameters in one formula
- Inconsistency between documents

---

## Open Problems (Priority)

### P1: Blocking Issues

1. **L_0/delta tension:** Static (m_p) prefers pi^2 ~ 9.87; Dynamic (tau_n) prefers 9.33
2. **Prefactor A:** Calibrated (A ~ 0.84), not derived from fluctuation determinant
3. **G_F derivation:** Uses measured v — need pure 5D derivation

### P2: Model Completion

1. Derive geometric factor f = sqrt(delta/L_0) from first principles
2. Derive frustration energy epsilon_f(A) from 5D action
3. Include spin/isospin in topological pinning model

---

## Session Protocol

### Start of Session (MANDATORY)

1. READ this file (`docs/CANON_BUNDLE.md`)
2. READ `docs/WORKSPACE_MAP.md` to locate relevant sources
3. CONSULT `docs/CONCEPT_INDEX.md` for definitions
4. CHECK `docs/STATUS.md` and `docs/TODO.md`
5. READ last entry of `docs/SESSION_LOG.md`
6. If working on Book 2: ALSO read `elastic-diffusive-cosmology_repo/edc_book_2/docs/CANON_BUNDLE.md`

### End of Session (MANDATORY)

1. UPDATE `docs/SESSION_LOG.md` (append entry)
2. UPDATE `docs/STATUS.md` if state changed
3. UPDATE `docs/TODO.md` (mark done, add new)
4. UPDATE `docs/CONCEPT_INDEX.md` if new concepts established

---

## Language Policy

- **Croatian** for conversation with Igor
- **English** for technical documents and code
- **Direct** — no hedging
- **Honest** — if something is circular or unknown, say so

---

*This is the WORKSPACE-LEVEL canon. For domain-specific details, see the domain's own CANON_BUNDLE.*

*Last updated: 2026-01-28*
