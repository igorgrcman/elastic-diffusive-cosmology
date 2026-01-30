# Content Migration Map

## Original → New Structure

### Part I: Foundations (Chapters 1-5)
| New Chapter | Source | Migration Notes |
|-------------|--------|-----------------|
| Ch 1: Weak Interface | Original Ch 1 | **RESTRUCTURE** - neutron lifetime first! |
| Ch 2: Ontology | Original Ch 3-4 | Consolidate particle types |
| Ch 3: Frozen Regime | Original Ch 2 | Use Book 1 results as [Der] |
| Ch 4: Z6 Program | Original Ch 5-7 | Consolidate Z6 structure |
| Ch 5: Case Studies | Original Ch 8-12 | Consolidate decay cases |

### Part II: Predictions (Chapters 6-11)
| New Chapter | Source | Migration Notes |
|-------------|--------|-----------------|
| Ch 6: Electroweak | Scattered content | Consolidate sin²θ_W derivation |
| Ch 7: Leptons | Scattered content | Consolidate mass hierarchy |
| Ch 8: Generations | Scattered content | Z6→Z3 quotient |
| Ch 9: Neutrinos | Scattered content | Edge modes |
| Ch 10: V-A Structure | Original Ch 10 | **COPY** (already excellent!) |
| Ch 11: CKM | Scattered content | CKM origin |

### Part III: Technical (Chapters 12-16)
| New Chapter | Source | Migration Notes |
|-------------|--------|-----------------|
| Ch 12: GF Chain | Original Ch 13-19 | g5→GF derivation chain |
| Ch 13: Foundation Params | Scattered OPR | **CONSOLIDATE** OPR-01, 04, 19 |
| Ch 14: BVP | Scattered OPR | **CONSOLIDATE** OPR-21 |
| Ch 15: MW & GF | Scattered OPR | **CONSOLIDATE** OPR-20, 22 |
| Ch 16: Epistemic Summary | New | Summary of what's proven vs open |

### Epilogue
| New Chapter | Source | Migration Notes |
|-------------|--------|-----------------|
| Ch 17: Beyond | Original Ch 20-21 | **TRIM** to brief teaser only |

---

## Priority Migration Order

### Week 2
1. **Ch 1** (Weak Interface) - RESTRUCTURE with neutron first
2. **Ch 10** (V-A) - COPY (already good)
3. **Ch 13** (Foundation Params) - CONSOLIDATE OPR

### Week 3
4. Ch 2-5 (Foundations)
5. Ch 6-9, 11 (Predictions except V-A)
6. Ch 14-16 (Technical)

### Week 4-5
- Add 20+ 5D Mechanism boxes
- Add error budgets
- Add visual dependency graphs

### Week 6
- Polish cross-references
- Fix all undefined refs
- Final TOC cleanup

### Week 7
- Review
- Final corrections
- Release

---

## Key Files to Migrate

### From src/sections/
- `01_weak_interface.tex` → Ch 1
- `02_frozen_regime.tex` → Ch 3
- `03a_particle_types.tex` → Ch 2
- `04b_proton_anchor.tex` → Ch 2
- `05_z6_crystallography.tex` → Ch 4
- `09_va_structure.tex` → Ch 10 (**priority**)
- Various OPR files → Ch 13-15

### Key Consolidations
1. **OPR-01, 04, 19** → All go to Ch 13 (Foundation Params)
2. **OPR-21** → All goes to Ch 14 (BVP)
3. **OPR-20, 22** → All go to Ch 15 (MW & GF)

---

## Verification Checklist

After each chapter migration:
- [ ] Chapter compiles without errors
- [ ] All \label{} tags present
- [ ] All \ref{} resolve correctly
- [ ] Epistemic tags applied
- [ ] Error budget included (where applicable)
- [ ] Cross-references to Book 1 correct
- [ ] 5D Mechanism box added (where applicable)
