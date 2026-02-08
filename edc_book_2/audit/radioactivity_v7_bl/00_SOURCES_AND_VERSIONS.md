# BL SOURCES AND VERSIONS (V7)

**Created**: 2026-01-31
**Purpose**: Document authoritative BL data sources per V7.2

---

## Allowed Sources (Whitelist)

| ID | Source | Description | Version/Date |
|----|--------|-------------|--------------|
| S1 | NNDC/ENSDF | Evaluated Nuclear Structure Data File | Current eval |
| S2 | NuDat | NNDC web interface | Links to ENSDF |
| S3 | NUBASE | Mass/decay evaluation tables | NUBASE2020 |
| S4 | AME | Atomic Mass Evaluation | AME2020 |
| S5 | IAEA LiveChart | Nuclear data visualization | ENSDF-based |

---

## Disallowed Sources (Blacklist)

- Wikipedia
- Random PDFs
- Blogs
- Papers (unless citing original ENSDF eval)
- Memory/heuristics
- "Typical" values without citation

---

## Access Method

For this session:
- Primary: WebFetch to NNDC/NuDat pages
- Backup: If WebFetch fails, record in DATA_GAPS_V7.md

---

## Citation Format

```
[Nuclide] — [Field] = [Value] — [BL:S#] (locator: [specific page/table])
```

Example:
```
212Bi — t1/2 = 60.55 min — BR(β⁻) = 64.06% — [BL:S1 ENSDF] (NuDat decay data)
```

---

## Sources Used in This Session

| Source | Nuclides Accessed | Status |
|--------|-------------------|--------|
| S1/S2 (NNDC/NuDat) | U-238 chain | Pending |
| S1/S2 (NNDC/NuDat) | Th-232 chain | Pending |
| S1/S2 (NNDC/NuDat) | U-235 chain | Pending |
