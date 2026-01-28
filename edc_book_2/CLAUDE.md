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

1. **Read** all 5 docs files: `STATUS.md`, `TODO.md`, `DERIVATIONS.md`, `DECISIONS.md`, `SESSION_LOG.md`
2. **Write** a short "Plan for this session" at the TOP of your response AND append to `docs/SESSION_LOG.md`
3. **Only then** proceed with actual work

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
