# CLAUDE.md — EDC_Project Workspace Rules

**Version:** 1.0
**Created:** 2026-01-28

You are Claude Code, operating in a **stateless environment** on the EDC (Elastic Diffusive Cosmology) project. ALL reasoning, derivations, and decisions MUST be written to disk.

---

## SECTION 0: WORKING DIRECTORY (MANDATORY — READ FIRST)

**This repository is located in the subfolder:** `elastic-diffusive-cosmology_repo/`

If the agent starts in a parent workspace (e.g., `EDC_Project/`), it MUST:
1. `cd elastic-diffusive-cosmology_repo`
2. Confirm with `git rev-parse --show-toplevel`
3. THEN read `docs/CANON_BUNDLE.md` and proceed

**All paths in this repository are repo-relative** (from the git repo root).

**Path conventions:**
- `docs/` means `<repo-root>/docs/`
- `edc_book/` means `<repo-root>/edc_book/`
- `edc_book_2/` means `<repo-root>/edc_book_2/`
- `edc_papers/` means `<repo-root>/edc_papers/`

**External directories (outside this repo):**
- `EDC_Research_PRIVATE/` — sibling folder, NOT inside this repo

**NEVER:**
- Use absolute paths in documentation
- Hunt PDFs for "find in book" — always use LaTeX/Markdown sources
- Assume you're in the repo root without verifying

---

## SECTION A: SESSION START PROTOCOL (MANDATORY)

Before doing ANY work, you MUST read these files in order:

### Step 1: Read Workspace Canon (REQUIRED)

```
1. docs/CANON_BUNDLE.md      <- Contains all P0 canonical content
2. docs/WORKSPACE_MAP.md     <- Navigation guide to all sources
3. docs/CONCEPT_INDEX.md     <- Lookup table for key concepts
4. docs/STATUS.md            <- Current state of all domains
5. docs/TODO.md              <- Prioritized actions
6. docs/SESSION_LOG.md       <- Last entry (what was done recently)
```

### Step 2: Read Domain Canon (If applicable)

If working on Book 2:
```
edc_book_2/docs/CANON_BUNDLE.md
```

If working on Research Private (external sibling folder):
```
../EDC_Research_PRIVATE/CLAUDE.md
```

### Step 3: Announce Plan

Write a short "Plan for this session" at the TOP of your response.

> **Why MANDATORY?** The CANON_BUNDLE contains verified findings [Der], canonical definitions, anti-patterns, and past decisions. Skipping it leads to:
> - Re-deriving already-established results
> - Repeating known errors (15 critical 3D traps!)
> - Contradicting past decisions
> - Wasting time

---

## SECTION B: CONCEPT LOOKUP BEHAVIOR

### When user asks "how did we define proton/neutron" or "find X in the book":

1. **FIRST** consult `docs/CONCEPT_INDEX.md`
2. If found: Return the exact .tex/.md path + section title + equation labels
3. If NOT found: Search ONLY within the relevant source root (repo-relative):
   - Book 1: `edc_book/`
   - Book 2: `edc_book_2/`
   - Papers: `edc_papers/`
4. **UPDATE** `docs/CONCEPT_INDEX.md` with the new mapping

### Canonical Definitions (DO NOT RE-DERIVE):

**Proton:**
- Y-junction (3 arms at 120deg)
- S^3 x S^3 x S^3 configuration
- Steiner theorem guarantees uniqueness
- Source: Book 1 chapter_3_confinement.tex, CANON_BUNDLE Section 7.2

**Neutron:**
- Asymmetric Y-junction (theta = 60deg)
- q = 1/3 (half-Steiner deviation)
- Metastable, decays toward proton
- Source: CANON_BUNDLE Section 7.3, 14

---

## SECTION C: FILE ACCESS RULES

### NEVER read:
- PDFs (too large, not source of truth)
- Binary files

### ALWAYS use as sources of truth:
- LaTeX .tex files
- Markdown .md files
- Python .py files (for numerics)

### NEVER delete or rename:
- Existing scientific content
- Git branches (forensic audit trail)

### Canon files ONLY in:
- `/docs` at repo root (workspace-level)
- `/docs` in domain directories (domain-level)

---

## SECTION D: DURING WORK

### Derivations

Every nontrivial derivation must be documented:
- Include equation labels / file references (path + line numbers)
- Mark epistemic tags: `[Der]`, `[Dc]`, `[I]`, `[P]`, `[Cal]`, `[BL]`
- Record assumptions and dependencies
- Note any open problems

### Decisions

Every decision must be recorded with:
- What was decided
- Why (rationale)
- Alternatives considered
- Date

### New Concepts

If you establish a new canonical definition:
- Add entry to `docs/CONCEPT_INDEX.md`
- Include source path, location, epistemic tag, usage

---

## SECTION E: END OF SESSION PROTOCOL

You may NOT conclude until:

- [ ] `docs/SESSION_LOG.md` appended with:
  - Date/time
  - Goals
  - Files read
  - Files created/modified
  - What workspace canon now guarantees
  - Next steps
  - Open questions

- [ ] `docs/STATUS.md` updated if state changed

- [ ] `docs/TODO.md` updated (completed marked, new added)

- [ ] `docs/CONCEPT_INDEX.md` updated if new concepts

---

## SECTION F: OUTPUT FORMAT

At the end of EVERY response that modifies files:

```
## Session Summary
**Files changed:** [list]
**Next steps:** [list]
**Open questions:** [list]
```

---

## SECTION G: EPISTEMIC TAGS (EDC Standard)

| Tag | Meaning | Use when... |
|-----|---------|-------------|
| `[Der]` | Derived | Explicit derivation from postulates exists |
| `[Dc]` | Derived Conditional | Derived IF certain assumptions hold |
| `[I]` | Identified | Pattern matching / mapping (not unique) |
| `[P]` | Proposed | Postulate / hypothesis / conjecture |
| `[Cal]` | Calibrated | Parameter fitted to data |
| `[BL]` | Baseline | External reference (PDG/CODATA) |
| `[M]` | Mathematics | Mathematical theorem (not EDC-specific) |

---

## SECTION H: RED FLAGS — STOP WORK

If you encounter any of these, STOP and ask the user:

- Dependency graph has a cycle (circularity)
- "Derivation" without explicit steps
- Numerical value used BEFORE derivation
- "Obviously..." without proof
- More than 3 free parameters in one formula
- Inconsistency between documents
- Attempt to re-derive canonical definitions (check CONCEPT_INDEX first!)

---

## SECTION I: LANGUAGE POLICY

- **Croatian** for conversation with Igor
- **English** for technical documents and code
- **Direct** — no hedging
- **Honest** — if something is circular or unknown, say so

---

## SECTION J: ANTI-PATTERNS (CRITICAL)

**THE GOLDEN RULE:**
> NEVER trust your 3D intuition in 5D calculations.
> Every geometric factor must be DERIVED, not assumed.

See CANON_BUNDLE for 15 critical traps including:
- KB-TRAP-001: Wrong Volume (4pi/3 vs 2pi^2)
- KB-TRAP-010: "Obviously 4pi"
- KB-TRAP-014: Assuming Spherical Symmetry
- KB-TRAP-015: Volume Ratio = Mass Ratio

---

## Quick Reference

| Question | Action |
|----------|--------|
| "What is proton definition?" | Check CONCEPT_INDEX.md CONCEPT-001 |
| "What is neutron definition?" | Check CONCEPT_INDEX.md CONCEPT-002 |
| "Where is X in the book?" | Check CONCEPT_INDEX.md, then search source root |
| "How did we derive Y?" | Check CANON_BUNDLE derivations section |
| "What was decided about Z?" | Check domain DECISIONS.md |

---

*This file defines workspace-level behavior. Domain-specific rules are in domain CLAUDE.md files.*
