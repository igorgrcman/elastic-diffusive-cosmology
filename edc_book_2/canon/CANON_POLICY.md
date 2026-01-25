# CANON_POLICY.md

## Published Canon with DOIs

The following artifacts are **immutable law** — definitions, results, and notation in these documents cannot be contradicted by Book 2.

| DOI | Title | Status |
|-----|-------|--------|
| 10.5281/zenodo.14538403 | Framework v2.0 | CANON |
| 10.5281/zenodo.14538507 | Paper 1 | CANON |
| 10.5281/zenodo.14564310 | Paper 2 | CANON |
| 10.5281/zenodo.14576217 | Companion: Mass From Geometry | CANON |
| 10.5281/zenodo.14576239 | Companion: Classical Limit | CANON |
| 10.5281/zenodo.14576219 | Companion: Quantum Corrections | CANON |
| 10.5281/zenodo.14576221 | Companion: Gauge Fields | CANON |
| 10.5281/zenodo.14576223 | Companion: Tensor Mode | CANON |
| 10.5281/zenodo.14576225 | Companion: Thick Brane Numerics | CANON |
| 10.5281/zenodo.14576227 | Companion: Horizon Exit | CANON |
| 10.5281/zenodo.14576229 | Companion: Defect Taxonomy | CANON |
| 10.5281/zenodo.18328508 | Book Part II (387-page baseline) | CANON |

## Policy

1. **No contradictions**: Book 2 content must not contradict definitions or results in canonical documents.

2. **Explicit citation**: When referencing canonical results, cite with DOI.

3. **Extension allowed**: New content may extend canonical results but not redefine them.

4. **Notation inheritance**: Notation from Framework v2.0 is canonical for all documents.

5. **Conflict resolution**: If apparent conflict exists, canonical documents take precedence. Document the conflict in `mapping/CONFLICTS.md`.

## Enforcement

Gate script `tools/gate_canon.sh` checks:
- [ ] No redefinition of canonical symbols
- [ ] No contradictory claims to published results
- [ ] Proper DOI citations for canonical references
