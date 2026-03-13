# EDC Global Development Guards

**Date**: 2026-03-13
**Status**: LOCKED
**Scope**: All EDC development — Books I–V, Papers, Code, Future Work
**Authority**: This document governs ALL future contributions to the EDC repository.

---

## PREAMBLE

Elastic-Diffusive Cosmology derives observable physics from a 5D brane action.
The theory's strength is its **ontological independence**: it does not borrow
constructs from other frameworks. These guards exist to protect that independence
and ensure intellectual honesty at every stage of development.

**Violation of any HARD guard is a blocking failure. Work cannot proceed until resolved.**

---

## GUARD 1: ONTOLOGICAL PURITY (HARD)

### 1.1 The Fundamental Rule

> **EDC derives physics from 5D geometry and topology. The Standard Model
> is not a source of theoretical input. It is another framework making
> predictions about the same measurements. EDC and SM are peers, not
> parent and child.**

### 1.2 Banned Sources of Theoretical Input

The following may **NEVER** appear as inputs, assumptions, or derivation steps
in any EDC Layer A text:

| Category | Banned Items |
|----------|-------------|
| Gauge groups | SU(3), SU(2), U(1), SO(10), E₆, E₈, any Lie group as force structure |
| SM Lagrangian | Any term from L_SM, Yukawa sector, Higgs potential |
| QCD constructs | Color charge, gluons, asymptotic freedom, confinement (QCD sense) |
| EW constructs | W/Z as gauge bosons, Higgs mechanism (SM version), CKM, PMNS |
| QFT apparatus | Feynman diagrams, loop corrections, renormalization group (as SM tool) |
| Nuclear models | Shell model, liquid drop, mean field, Woods-Saxon |
| SM quantum numbers | Isospin, strangeness, charm, beauty, color |
| SM-derived constants | Running couplings evaluated via SM beta functions |

### 1.3 What IS Allowed

| Category | Allowed Items | Reason |
|----------|--------------|--------|
| Pure mathematics | Topology, homotopy, group theory, differential geometry | Framework-independent |
| 5D geometry | Nambu-Goto, Kaluza-Klein (pure geometry), brane dynamics | EDC-native |
| Classical theorems | Steiner, Plateau, Kepler-Hales, Sturm-Liouville | Mathematics |
| Instanton calculus | Euclidean action, WKB, bounce solutions | Mathematical technique |
| Empirical data | Measured masses, lifetimes, binding energies | Verification targets |

### 1.4 Boundary Cases

| Item | Ruling | Justification |
|------|--------|---------------|
| "Renormalization" | ALLOWED if applied to EDC's own 5D action | Mathematical technique |
| "Gauge symmetry" | ALLOWED if derived from brane geometry | Must originate from S_EDC |
| "Kaluza-Klein" | ALLOWED for pure geometric compactification | Not SM content |
| "Instanton" | ALLOWED as mathematical object | Topological, not SM-specific |
| "Winding number" | ALLOWED | Algebraic topology |
| "Running coupling" | BANNED if using SM beta function; ALLOWED if EDC derives its own | Source matters |

### 1.5 Enforcement

```
SCAN COMMAND (run before any commit):

grep -rniE "(standard model|\bSM\b|SU\(3\)|SU\(2\)|U\(1\)|yang-mills|QCD|\
gluon|quark|isospin|CKM|PMNS|Feynman|shell model|magic number|Woods-Saxon|\
Higgs mechanism|gauge boson|electroweak|V-A|Yukawa coupling|beta function|\
asymptotic freedom|running coupling)" \
  --include="*.tex" --include="*.md" --include="*.py" \
  --exclude-dir="appendices" --exclude="*appQ*" --exclude="*appX*" \
  --exclude="*GUARD*" --exclude="*CANON*" --exclude="*CONTAMINATION*"

Expected: 0 hits in Layer A content.
```

---

## GUARD 2: EMPIRICAL DATA PROTOCOL (HARD)

### 2.1 The Rule

> **Empirical data enters EDC as verification targets, never as theoretical
> inputs. The theory predicts; measurements verify. We do not fit to data —
> we compare to data.**

### 2.2 Data Classification

| Tag | Meaning | Usage |
|-----|---------|-------|
| [BL] | Baseline | Empirical datum used as comparison reference |
| [M] | Measurement | Specific measured value with uncertainty |
| [Obs] | Observation | Qualitative empirical fact |

### 2.3 What Data CAN Do

- Serve as **target** for EDC predictions
- Appear in **comparison tables** alongside EDC results
- Provide **falsification hooks** (if EDC predicts X but measurement gives Y)
- Motivate which problems to solve next

### 2.4 What Data CANNOT Do

- Appear inside a derivation chain as an input
- Be used to "fix" or "calibrate" a parameter that should be derived
- Justify an assumption ("we assume X because experiments show X")
- Serve as the sole evidence for a claim tagged [Der]

### 2.5 Calibration Quarantine

When calibration is unavoidable (e.g., prefactor A ≈ 0.9 in τ_n):

1. The calibrated parameter MUST be tagged [Cal]
2. It MUST be documented in Appendix Q with:
   - Fitted value and uncertainty
   - Natural-range argument (why O(1) is expected)
   - Anti-tuning firewall (sensitivity analysis)
3. An OPEN problem MUST be registered to derive it from first principles
4. The [Cal] parameter MUST NOT dominate the prediction (exponent > prefactor)

### 2.6 Anti-Tuning Firewall Template

For any [Cal] parameter P:

```
1. What is P?                    [description]
2. Fitted value:                 [value ± range]
3. Natural range:                [lower, upper] with physics justification
4. Sensitivity:                  [how much does the result change if P varies by 2×?]
5. Exponent dominance:           [does P enter linearly or exponentially?]
6. Registered OPR for derivation: [OPR-XX or BOOK4-X]
7. Target promotion:             [Cal] → [Dc] or [Der]
```

---

## GUARD 3: EPISTEMIC HONESTY (HARD)

### 3.1 The Rule

> **Every claim carries a provenance tag. No claim may be promoted to a higher
> epistemic status without explicit justification and audit trail.**

### 3.2 Tag Hierarchy

```
[Der]  — Derived: follows from S_EDC alone, no auxiliary input
[Dc]   — Derived-conditional: follows from S_EDC + stated assumptions
[P]    — Postulated: motivated conjecture, not derived
[Cal]  — Calibrated: fitted to data (quarantined)
[BL]   — Baseline: empirical reference datum
[I]    — Input: fundamental parameter of the theory
[M]    — Mathematics: framework-independent formal result
[OPEN] — Open: derivation gap acknowledged
```

### 3.3 Promotion Rules

| From | To | Requirement |
|------|-----|-------------|
| [P] → [Dc] | Must provide derivation chain with stated assumptions |
| [P] → [Der] | Must derive from S_EDC alone with no auxiliary input |
| [Dc] → [Der] | Must eliminate all auxiliary assumptions |
| [Cal] → [Dc] | Must derive the parameter from 5D dynamics |
| [Cal] → [Der] | Must derive with zero free parameters |
| [OPEN] → any | Must close the registered open problem with evidence |

### 3.4 Demotion Rules

| Trigger | Action |
|---------|--------|
| New evidence contradicts a [Der] claim | Demote to [Dc] or [P] with explanation |
| Auxiliary assumption found to be necessary | Demote [Der] → [Dc] |
| Shape-dependence discovered | Flag as "conditional on V(ξ) form" |
| Numerical error found | Demote until corrected and re-verified |

### 3.5 The Overclaiming Ban

**FORBIDDEN phrases in Layer A:**
- "We have shown that..." (unless tagged [Der] with complete proof)
- "It follows immediately..." (show the steps)
- "It is obvious that..." (nothing is obvious)
- "As expected from the Standard Model..." (SM is not our reference)
- "This confirms the theory..." (measurements verify; they don't confirm)
- "QED" at the end of a derivation (literally a banned acronym)

**REQUIRED phrases:**
- "This result is tagged [Dc] because it requires assumption X"
- "The open problem OPR-XX tracks the derivation gap"
- "Sensitivity analysis shows the result is robust/fragile to..."

---

## GUARD 4: VOCABULARY DISCIPLINE (HARD)

### 4.1 The Rule

> **Layer A text uses EDC-native vocabulary exclusively. Conventional particle
> names appear only in observerboxes (as projection labels) and quarantine
> appendices (Q, X).**

### 4.2 Mandatory Substitutions

| BANNED (Layer A) | USE (EDC-Native) | Macro |
|------------------|-------------------|-------|
| proton | anchor junction | `\AnchorJunction` |
| neutron | metastable junction | `\MetastableJunction` |
| electron | loop state | `\LoopState` |
| nucleus | cluster state / pinning cluster | `\ClusterState` |
| alpha particle | closed-4 unit | `\ClosedFour` |
| beta decay | junction transition | `\JunctionTransition` |
| alpha decay | closed-4 release | `\ClosedFourRelease` |
| nuclear binding | pinning energy | — |
| nuclear shell | coordination boundary | — |
| magic number | stable coordination | — |
| strong force | topological binding / pinning | — |
| weak force | junction tunneling / instanton | — |
| photon | edge-mode excitation | `\EdgeMode` |
| graviton | bulk mode | `\BulkMode` |

### 4.3 Observerbox Protocol

Each chapter may contain **exactly one** observerbox that maps 5D objects
to 3D/4D measurement labels:

```latex
\begin{observerbox}
Observer-side projection note: quoted terms are measurement labels for the
3D/4D projection of the 5D objects defined in this chapter; they do not
imply any conventional mechanism.

\begin{itemize}
    \item \AnchorJunction{} $\leftrightarrow$ ``proton'' (projection label)
\end{itemize}
\end{observerbox}
```

**Rules:**
- Projection labels in quotes with "(projection label)" suffix
- No mechanism explanations inside observerbox
- Banned mechanism words forbidden even inside observerbox

### 4.4 Appendix Routing

| Content | Destination | Tag |
|---------|-------------|-----|
| "In other frameworks, this corresponds to..." | Appendix Q | [Cal] or [BL] |
| "Historically known as..." | Appendix X | [Analog] |
| Empirical dataset with conventional labels | Appendix Q | [BL] |
| Translation table (EDC ↔ conventional) | Appendix X | [Analog] |

---

## GUARD 5: DERIVATION CHAIN INTEGRITY (HARD)

### 5.1 The Rule

> **Every derivation must be traceable from S_EDC to the final result.
> Every step must cite its inputs, state its assumptions, and tag its
> epistemic status. No gaps in the chain.**

### 5.2 Required Documentation for Each Derivation

```
DERIVATION TEMPLATE:

1. INPUTS:     [list with tags: σ [I], V(q) [P], ...]
2. ASSUMPTIONS: [numbered, each tagged]
3. CHAIN:      [step-by-step with equation references]
4. OUTPUT:     [result with tag]
5. SENSITIVITY: [how robust is the result to input variations?]
6. FALSIFIABILITY: [what measurement would kill this result?]
7. OPEN GAPS:  [what remains to be derived?]
```

### 5.3 Cross-Book Provenance

When Book IV uses a result from Book I:
- State: "σ = 8.82 MeV/fm² [I, Book I]"
- Do not re-derive
- If the Book I result changes, propagate the change

When a derivation spans multiple chapters:
- Chapter Spine must list all dependencies
- Bridge paragraph at chapter end must link forward

---

## GUARD 6: COMPUTATIONAL REPRODUCIBILITY (HARD)

### 6.1 The Rule

> **Every numerical claim must be reproducible from a deterministic script
> with fixed inputs and documented outputs.**

### 6.2 Requirements

| Requirement | Specification |
|-------------|---------------|
| Script location | `code/` or `edc_book_N/code/` |
| Language | Python 3.10+ preferred |
| Random seeds | Fixed where applicable |
| Output format | Printed to stdout with labeled values |
| Checksums | SHA256 of output stored in REPRO_MANIFEST |
| Dependencies | Listed in requirements.txt |

### 6.3 Verification Tiers

| Tier | What | How |
|------|------|-----|
| 1 | Compile | LaTeX builds without error |
| 2 | Dimensional | All equations dimensionally consistent |
| 3 | Numerical | Python script reproduces stated values |
| 4 | Sensitivity | Variation of inputs produces expected range |
| 5 | Falsification | Edge cases checked against claimed bounds |

---

## GUARD 7: NO RETROACTIVE CONTAMINATION (HARD)

### 7.1 The Rule

> **When new results are derived, they must be expressed in EDC-native
> terms from the start. It is forbidden to derive a result using SM
> constructs and then "translate" it to EDC vocabulary.**

### 7.2 The Translation Trap

**FORBIDDEN workflow:**
1. Think in SM terms ("the proton has quarks...")
2. Derive using SM constructs
3. Replace SM words with EDC words
4. Claim "EDC derives this"

**REQUIRED workflow:**
1. Start from S_EDC or its consequences
2. Derive using 5D geometry and topology
3. Obtain result in EDC-native terms
4. Compare to measurement (not to SM prediction)

### 7.3 Circular Reference Ban

**FORBIDDEN:**
- "EDC predicts X, which agrees with the SM prediction of X"
- "We calibrate using the SM value of..."
- "Following the SM derivation, but replacing..."

**ALLOWED:**
- "EDC predicts X. Measurement gives X ± δ. Deviation: Y ppm."
- "The 5D boundary condition yields eigenvalue μ₃, corresponding to..."

---

## GUARD 8: FUTURE DEVELOPMENT PROTOCOL (SOFT)

### 8.1 Before Starting New Work

Checklist:
- [ ] Does this work derive from S_EDC or its established consequences?
- [ ] Does it use EDC-native vocabulary throughout?
- [ ] Are all inputs tagged with epistemic markers?
- [ ] Is there a falsifiability hook?
- [ ] Does it avoid all GUARD 1 banned items?
- [ ] Is there a Python verification script?

### 8.2 Before Committing

Checklist:
- [ ] Run contamination scan (GUARD 1.5 command)
- [ ] Run epistemic tag check (all claims tagged)
- [ ] Run numerical verification (all scripts pass)
- [ ] Update REPRO_MANIFEST if numerical claims changed
- [ ] Update OPR registry if open problems changed
- [ ] Update EDC_UNIFIED_SYNTHESIS.md if results changed

### 8.3 Before Publishing/Sharing

Checklist:
- [ ] Full 4-phase audit complete
- [ ] All [Cal] parameters documented with anti-tuning firewalls
- [ ] All [OPEN] problems registered in OPR
- [ ] Sensitivity analysis for all key results
- [ ] Falsifiability conditions stated
- [ ] No SM vocabulary in Layer A (zero tolerance)

---

## GUARD 9: NOVEL PREDICTION PROTOCOL (SOFT)

### 9.1 The Rule

> **EDC must generate predictions that are (a) unique to EDC, (b) quantitative,
> and (c) testable with current or near-future technology.**

### 9.2 Prediction Classification

| Type | Definition | Example |
|------|-----------|---------|
| Retrodiction | Explains known measurement | α = 1/137.028 |
| Conditional prediction | Prediction with stated assumptions | τ_n from instanton |
| Novel prediction | Not predicted by any other framework | Forbidden zone [37, 47] |
| Discriminating prediction | EDC and SM give different values | — (needed!) |

### 9.3 Priority for Novel Predictions

The theory urgently needs **discriminating predictions** — quantities where
EDC gives a different answer than other approaches, testable by experiment.

Candidates:
1. Sub-ppm α correction (requires BVP closure)
2. Specific coordination stability pattern at high Z
3. Closed-4 release time deviations from baseline
4. Mode spectrum in ξ-direction (if experimentally accessible)

---

## GUARD 10: CROSS-BOOK CONSISTENCY (HARD)

### 10.1 Symbol Canon

All books share a common symbol canon. Collisions are resolved and documented:

| Symbol | Book I | Book II | Book IV | Resolution |
|--------|--------|---------|---------|------------|
| σ | Brane tension | Brane tension | Brane tension | Consistent |
| μ | — | BVP eigenvalue | — | Book II owns |
| R | Ricci scalar | R_ξ | — | Context-qualified |
| K | — | — | Pinning constant | Book IV owns |
| δ | Brane thickness | Brane thickness | Brane thickness | Consistent |

### 10.2 Parameter Flow

```
Book I: σ, δ, L₀, T* (fundamental inputs [I])
    ↓
Book II: + BVP eigenvalue μ, frozen projection P_frozen
    ↓
Book IV: + K_pin, coordination n(A), frustration d(n)
```

Any change to Book I parameters propagates to all downstream books.

---

## ENFORCEMENT SUMMARY

| Guard | Type | Scan/Check Available? | Blocking? |
|-------|------|----------------------|-----------|
| G1: Ontological purity | HARD | grep scan | YES |
| G2: Empirical protocol | HARD | Manual review | YES |
| G3: Epistemic honesty | HARD | Tag audit | YES |
| G4: Vocabulary | HARD | grep scan | YES |
| G5: Derivation chain | HARD | Manual review | YES |
| G6: Reproducibility | HARD | Script execution | YES |
| G7: No retroactive contamination | HARD | Manual review | YES |
| G8: Development protocol | SOFT | Checklist | NO |
| G9: Novel predictions | SOFT | Manual review | NO |
| G10: Cross-book consistency | HARD | Symbol canon check | YES |

---

**GLOBAL GUARDS LOCKED. Modification requires explicit justification, version bump, and audit trail.**

**Version**: 1.0
**Effective**: 2026-03-13
