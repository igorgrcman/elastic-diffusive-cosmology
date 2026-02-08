# DECISIONS LOG: Radioactivity Forbidden Research

**Session**: 2026-01-31

---

## Decision Format

Each decision:
- **ID**: D-XXX
- **Decision**: What was decided
- **Reason**: Why
- **Citation**: Source reference (file:line or MTR block)
- **Alternatives rejected**: What else was considered

---

## Decisions

### D-001: Use MTR blocks as primary navigation
**Decision**: Navigate 22826edd_full.md via MTR-001..006 line ranges rather than grep
**Reason**: Chain locator already has precise locations; avoids expensive scans
**Citation**: radioactivity_mtopology_chain_locator.md
**Alternatives rejected**: Full-file grep (wasteful)

### D-002: Mark all nuclear half-life data as [BL] unless in repo
**Decision**: Do not invent or recall nuclear data from training; mark [BL] external nuclear data required
**Reason**: Hard guardrail - no hallucination of t₁/₂, Q, branching
**Citation**: User mega-prompt constraint
**Alternatives rejected**: Using approximate values from memory

### D-003: "Forbidden n≠43" mechanisms are [I] or [P] only
**Decision**: Any mechanism for n∈{44,45,46,47} is inference or proposal, not [Der]
**Reason**: Original chain only proves n=43 forbidden; extension is hypothesis
**Citation**: MTR-003 (22826edd_full.md:7280-7430)
**Alternatives rejected**: Claiming [Der] status for untested hypotheses

