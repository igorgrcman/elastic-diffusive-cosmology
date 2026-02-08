# EDC Papers — Export Naming Policy

## Canonical Export Name Convention

Each paper in `edc_papers/` must have a **uniquely named canonical export PDF** in its folder root.

### Format

```
EDC_<SHORTTOPIC>_<TYPE>.pdf
```

Examples:
- `EDC_BLOCK003_GRAVITY_PROGRAM.pdf`
- `EDC_NUCLEAR_PINNING_RESULTS.pdf`

Version suffix (`_v1`, `_v2`) is optional and only needed if multiple versions must coexist.

### Rules

1. **Unique names required** — No two papers may share the same export filename.
2. **`main.pdf`** — May exist as a build artifact, but is not the canonical export name.
3. **`EXPORT_TO_UPLOAD.pdf`** — Forbidden in `edc_papers/`. This generic name is reserved only for the legacy monograph workflow in `edc_book_2/`.
4. **Index listing** — All canonical export PDFs must be listed in `PAPERS_INDEX.md`.

### Rationale

Generic names like `EXPORT_TO_UPLOAD.pdf` cause confusion when multiple papers exist. Unique, descriptive names prevent accidental overwrites and make file identification immediate.
