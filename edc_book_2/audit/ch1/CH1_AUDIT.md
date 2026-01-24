# CH1 Audit: The Weak Interface

Generated: 2026-01-24
Status: **IN_PROGRESS**

## Scope

**Chapter 1: The Weak Interface** is the first main chapter of EDC Book 2.
It establishes the unified pipeline for weak processes and presents case studies.

### Included Files (14)

```
sections/01_how_we_got_here.tex
sections/02_geometry_interface.tex
sections/03_unified_pipeline.tex
sections/04a_unified_master_figure.tex
sections/04_ontology.tex
sections/04b_proton_anchor.tex
sections/05_case_neutron.tex
sections/06_case_muon.tex
sections/07_case_tau.tex
sections/09_case_electron.tex
sections/08_case_pion.tex
sections/10_case_neutrino.tex
sections/11_gf_pathway.tex
sections/13_summary.tex
```

## Equation Inventory Summary

| Metric | Count |
|--------|-------|
| equation environments | 54 |
| align environments | 5 |
| Total equation blocks | ~59 |
| Labeled equations | 40 |
| Unlabeled equations | ~19 |

**Key equations:**
- `eq:brane_energy_balance` - Fundamental energy balance
- `eq:ledger_closure` - Conservation constraint
- `eq:n_Q_beta` - Neutron Q-value
- `eq:Pfrozen_def` - Frozen regime criterion

See: `CH1_EQUATION_INDEX.md` for full list.

## Claim Inventory Summary

| Tag | Count |
|-----|-------|
| [BL] | 92 |
| [P] | 99 |
| [Dc] | 59 |
| [I] | 5 |
| [Cal] | 3 |
| [Der] | 2 |
| **Total** | **260** |

See: `CH1_CLAIM_INDEX.md` for details.

## Code References Summary

- 1 TikZ figure input (`fig_master_weak_pipeline.tex`)
- 2 figure references (`fig:master_pipeline`, `fig:n_potential`)
- No external code dependencies in CH1

See: `CH1_CODE_REFERENCES.md` for details.

## Verification Checklist

| Check | Status | Notes |
|-------|--------|-------|
| **Math consistency** | UNVERIFIED | Equations need dimensional analysis |
| **Units** | UNVERIFIED | Check all numerical values have proper units |
| **Notation canon (ξ)** | PASS | gate_notation.sh passed |
| **No smuggling** | UNVERIFIED | Check no circular dependencies |
| **Citation sanity** | UNVERIFIED | Verify all \cite{} resolve |
| **Cross-chapter deps** | UNVERIFIED | List equations referenced from other chapters |
| **Label uniqueness** | UNVERIFIED | No duplicate labels |

## Known Gaps

### [OPEN] Items

1. **Missing full derivations**: 99 [P] claims need derivation path or explicit postulate status
2. **Low [Der] count**: Only 2 fully derived results in entire chapter
3. **Unlabeled equations**: ~19 equations without labels (harder to reference)
4. **Cross-chapter figure**: `fig:n_potential` referenced but may be defined elsewhere

### Dependencies on Other Chapters

- CH2 (Frozen Regime Foundations): Defines P_frozen criterion used here
- CH3 (Z6 Program): Provides symmetry framework referenced
- CH9 (Fermi Constant): G_F derivation summarized in 11_gf_pathway

### Reviewer Attack Surface

1. **Circular reasoning check**: Do any [Dc] claims secretly use their own conclusions?
2. **Numerical coincidence vs derivation**: Are numerical matches explained or just observed?
3. **SM compatibility**: Do [BL] facts match current PDG values?

## Gate Results (at audit time)

```
gate_notation.sh: PASS
gate_canon.sh: PASS
gate_build.sh: PASS (387 pages)
```

## Action Items

- [ ] Verify all equations have consistent notation
- [ ] Add labels to 19 unlabeled equations
- [ ] Document derivation chain for key [Dc] claims
- [ ] Check all [BL] values against PDG 2024
- [ ] Resolve `fig:n_potential` reference
- [ ] Dimensional analysis pass on all equations

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Auditor | Claude | 2026-01-24 | IN_PROGRESS |
| Reviewer | - | - | PENDING |
| Author | - | - | PENDING |
