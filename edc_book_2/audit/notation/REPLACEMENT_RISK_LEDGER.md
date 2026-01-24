# Replacement Risk Ledger

Generated: 2026-01-24
Purpose: Document EVERY symbol replacement with semantic justification
Status: TRACKING — append entries before any notation changes

## Policy

**CRITICAL**: This ledger must be updated BEFORE any symbol replacement in Book 2.

Per CLAUDE.md and project rules:
- NO blind grep/replace on symbols
- Every change requires context classification
- Canon (Framework v2.0) is authoritative
- Document reason in 1 sentence

## Entry Format

For each changed instance:
```
| File | Line | Old | New | Class | Canon Anchor | Reason |
```

---

## Completed Replacements

(None yet — this section logs replacements after they are made)

| File | Line | Old Symbol | New Symbol | Classification | Canon Anchor | Reason |
|------|------|------------|------------|----------------|--------------|--------|
| — | — | — | — | — | — | — |

---

## Pending Replacements (Approved but not yet executed)

| ID | File | Line(s) | Old Symbol | New Symbol | Classification | Canon Anchor | Reason | Approved |
|----|------|---------|------------|------------|----------------|--------------|--------|----------|
| — | — | — | — | — | — | — | — | — |

---

## Rejected Replacements (Considered but NOT appropriate)

| File | Line | Candidate | Reason for Rejection |
|------|------|-----------|---------------------|
| ch12_bvp_workpackage.tex | 222 | z → ξ | TBD: May be generic mode function variable |

---

## Risk Categories

| Risk Level | Criteria | Action Required |
|------------|----------|-----------------|
| LOW | Unambiguous context, clear 5D depth usage | Proceed with care |
| MEDIUM | Some ambiguity, but context suggests 5D | Document rationale |
| HIGH | Multiple valid interpretations | Human review required |
| CRITICAL | Symbol has dual meaning in same file | Resolve collision first |

---

## Workflow for Symbol Replacement

### Before changing ANY symbol:

1. **Read context** (±10 lines minimum)
2. **Classify** using CHAPTER_VARIABLE_CONTEXT_LEDGER.md
3. **Find canon anchor** in Framework v2.0 or canon PDFs
4. **Add entry** to this ledger (Pending section)
5. **Get approval** if HIGH/CRITICAL risk
6. **Make change**
7. **Move entry** to Completed section
8. **Verify build** passes

### Required fields for each entry:

- **File**: Exact filename
- **Line**: Line number(s) affected
- **Old Symbol**: What is being replaced (LaTeX form)
- **New Symbol**: What it becomes (LaTeX form)
- **Classification**: From CHAPTER_VARIABLE_CONTEXT_LEDGER.md
- **Canon Anchor**: Framework v2.0 Eq.(N) or §N.M
- **Reason**: One sentence explaining WHY this is correct

---

## Canon Anchors Quick Reference

| Pattern | Canon Reference | Correct Symbol |
|---------|-----------------|----------------|
| 5D manifold | Framework v2.0 Eq.(1) | \mathcal{M}^5 |
| 5D compact coordinate | Framework v2.0 Eq.(3) | ξ |
| 3D spatial | Framework v2.0 | x, y, z |
| 5D radius | Framework v2.0 Def.1.1 | R_ξ |
| 5D Planck mass | (derived) | M_{5,\mathrm{Pl}} |
| Z6 complex variables | Framework v2.0 §11 | z_1, z_2 |

---

## Collision Warnings

### ξ collision (Paper 2 legacy)

Paper 2 uses ξ for BOTH:
1. 5D compact coordinate (canonical)
2. GL coherence length (collision)

**Resolution**: In EDC canon, ξ = 5D depth. If coherence length appears, use ξ_GL or λ.

### M_5 ambiguity

M_5 can mean:
1. 5D manifold → should be \mathcal{M}^5
2. 5D Planck mass → should be M_{5,\mathrm{Pl}}

**Resolution**: Check physical context. Mass formulas (G_5 ~ 1/M_5²) → M_{5,Pl}.
Topology (π₁(M_5)) → \mathcal{M}^5.

---

## Audit Trail

| Date | Action | Files Affected | By |
|------|--------|----------------|-----|
| 2026-01-24 | Ledger created | (none yet) | Claude |

---

## Version History

| Date | Change | By |
|------|--------|-----|
| 2026-01-24 | Initial creation | Claude |

