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

Commit 7014cbd (2026-01-24): Phase D notation remediation complete.

### Category A: M_5 → \mathcal{M}^5 (Manifold Context) — COMPLETED

| VR-ID | File | Lines | Status |
|-------|------|-------|--------|
| VR-001 to VR-007 | 05_three_generations.tex | 334,339,341,369-370,378,385,402,501,605 | ✅ DONE |

### Category B: M_5 → M_{5,Pl} (Mass Context) — COMPLETED

| VR-ID | File | Lines | Status |
|-------|------|-------|--------|
| VR-008 | 11_gf_derivation.tex | 404,406 | ✅ DONE |
| VR-009, VR-010 | ch11_opr20_attemptD*.tex | 248,259,261 | ✅ DONE |
| VR-011, VR-012 | ch14_bvp_closure_pack.tex | 276,280,297,305 | ✅ DONE |

### Category C: z/Δz → ξ/Δξ (5D Depth Context) — COMPLETED

| VR-ID | File | Lines | Status |
|-------|------|-------|--------|
| VR-013 to VR-019 | 06_neutrinos_edge_modes.tex | 70-71,93,434-437,457-458,465-467,485,530,536,701,757 | ✅ DONE |
| VR-020 to VR-023 | 07_ckm_cp.tex | 66,97,102,446,505,511,521-541,572,693-724,803-808,1012-1047 | ✅ DONE |
| VR-024 | 09_va_structure.tex | 275-276,309 | ✅ DONE |
| VR-025 | ch11_opr20_attemptF*.tex | 23-24 | ✅ DONE |

---

## Pending Replacements (Approved but not yet executed)

### Category A: M_5 → \mathcal{M}^5 (Manifold Context)

| ID | File | Line(s) | Old | New | Class | Canon | Reason | Decision |
|----|------|---------|-----|-----|-------|-------|--------|----------|
| VR-001 | 05_three_generations.tex | 334 | `$\pi_1(M_5)$` | `$\pi_1(\mathcal{M}^5)$` | (E) Manifold | Fwk v2.0 Eq.(1) | Homotopy group of manifold | MUST-FIX |
| VR-002 | 05_three_generations.tex | 339 | `$M_5$` | `$\mathcal{M}^5$` | (E) Manifold | Fwk v2.0 Eq.(1) | "5D bulk manifold" context | MUST-FIX |
| VR-003 | 05_three_generations.tex | 341 | `$\pi_1(M_5)$` | `$\pi_1(\mathcal{M}^5)$` | (E) Manifold | Fwk v2.0 Eq.(1) | Fundamental group | MUST-FIX |
| VR-004 | 05_three_generations.tex | 369-370 | `$M_5$` | `$\mathcal{M}^5$` | (E) Manifold | Fwk v2.0 Eq.(1) | Topology table entries | MUST-FIX |
| VR-005 | 05_three_generations.tex | 378,385 | `$M_5$` | `$\mathcal{M}^5$` | (E) Manifold | Fwk v2.0 Eq.(1) | "global topology of M_5" | MUST-FIX |
| VR-006 | 05_three_generations.tex | 402 | `$\pi_1(M_5)$` | `$\pi_1(\mathcal{M}^5)$` | (E) Manifold | Fwk v2.0 Eq.(1) | Table entry | MUST-FIX |
| VR-007 | 05_three_generations.tex | 501,605 | `$\pi_1(M_5)$` | `$\pi_1(\mathcal{M}^5)$` | (E) Manifold | Fwk v2.0 Eq.(1) | Summary/table | MUST-FIX |

### Category B: M_5 → M_{5,Pl} (Mass Context)

| ID | File | Line(s) | Old | New | Class | Canon | Reason | Decision |
|----|------|---------|-----|-----|-------|-------|--------|----------|
| VR-008 | 11_gf_derivation.tex | 404,406 | `$M_5$` | `$M_{5,\mathrm{Pl}}$` | (D) Mass | Derived | G_5 ~ g²/M² is mass formula | MUST-FIX |
| VR-009 | ch11_opr20_attemptD*.tex | 248 | `$M_5$` | `$M_{5,\mathrm{Pl}}$` | (D) Mass | Derived | "5D Planck scale" explicit | MUST-FIX |
| VR-010 | ch11_opr20_attemptD*.tex | 259,261 | `$M_5$` | `$M_{5,\mathrm{Pl}}$` | (D) Mass | Derived | σ/M³ mass formula | MUST-FIX |
| VR-011 | ch14_bvp_closure_pack.tex | 276,280 | `$M_5$` | `$M_{5,\mathrm{Pl}}$` | (D) Mass | Derived | "5D Planck mass" explicit | MUST-FIX |
| VR-012 | ch14_bvp_closure_pack.tex | 297,305 | `$M_5$` | `$M_{5,\mathrm{Pl}}$` | (D) Mass | Derived | Junction/GHY action | MUST-FIX |

### Category C: z/Δz → ξ/Δξ (5D Depth Context)

| ID | File | Line(s) | Old | New | Class | Canon | Reason | Decision |
|----|------|---------|-----|-----|-------|-------|--------|----------|
| VR-013 | 06_neutrinos_edge_modes.tex | 70-71 | `$\Delta z$` | `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | "separation" in 5D | MUST-FIX |
| VR-014 | 06_neutrinos_edge_modes.tex | 93 | `$\Delta z$` | `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | Same context | MUST-FIX |
| VR-015 | 06_neutrinos_edge_modes.tex | 434-437 | `$\Delta z$` | `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | Neutrino mass suppression | MUST-FIX |
| VR-016 | 06_neutrinos_edge_modes.tex | 457-458 | `$z_H$`, `$\Delta z$` | `$\xi_H$`, `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | Horizon and separation | MUST-FIX |
| VR-017 | 06_neutrinos_edge_modes.tex | 465-467,485 | `$\Delta z$` | `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | Mass ratio formula | MUST-FIX |
| VR-018 | 06_neutrinos_edge_modes.tex | 530,536 | `$\Delta z$` | `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | Mode-dependent separation | MUST-FIX |
| VR-019 | 06_neutrinos_edge_modes.tex | 701,757 | `$\Delta z$` | `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | Constraint discussion | MUST-FIX |
| VR-020 | 07_ckm_cp.tex | 66 | `$\Delta z$` | `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | Generation separation | MUST-FIX |
| VR-021 | 07_ckm_cp.tex | 97,102 | `$\Delta z$` | `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | Wolfenstein parameter | MUST-FIX |
| VR-022 | 07_ckm_cp.tex | 446 | `$\Delta z$` | `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | CKM diagonal structure | MUST-FIX |
| VR-023 | 07_ckm_cp.tex | 505,511 | `$\Delta z$` | `$\Delta\xi$` | (A) 5D depth | Fwk v2.0 Eq.(3) | Figure caption | MUST-FIX |
| VR-024 | 09_va_structure.tex | 275-276 | `$\Psi(x^\mu, z)$` | `$\Psi(x^\mu, \xi)$` | (A) 5D depth | Fwk v2.0 Eq.(3) | 5D field coordinate | MUST-FIX |
| VR-025 | ch11_opr20_attemptF*.tex | 23 | `$\phi(x^\mu, z)$` | `$\phi(x^\mu, \xi)$` | (A) 5D depth | Fwk v2.0 Eq.(3) | Mediator in 5D bulk | MUST-FIX |

### Category D: Notation Comment (Documentation)

| ID | File | Line(s) | Old | New | Class | Canon | Reason | Decision |
|----|------|---------|-----|-----|-------|-------|--------|----------|
| VR-026 | 02_frozen_regime_foundations.tex | 133 | Comment about M_5 | Update comment | (H) Other | Fwk v2.0 Eq.(1) | Documentation consistency | TODO |

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

