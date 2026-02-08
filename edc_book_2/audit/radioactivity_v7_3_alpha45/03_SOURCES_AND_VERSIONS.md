# SOURCES AND VERSIONS (V7.3)

**Created**: 2026-01-31
**Inherited from**: V7.2, V7.1, V7

---

## BL Source Whitelist

| ID | Source | Authority | URL | Access Date |
|----|--------|-----------|-----|-------------|
| S1 | NNDC/ENSDF | Primary | nndc.bnl.gov/ensdf | 2026-01-31 |
| S2 | NuDat 3.0 | Derived from ENSDF | nndc.bnl.gov/nudat3 | 2026-01-31 |
| S3 | NUBASE2020 | Masses, t₁/₂ | DOI:10.1088/1674-1137/abddae | 2026-01-31 |
| S4 | AME2020 | Atomic masses, Q-values | DOI:10.1088/1674-1137/abddaf | 2026-01-31 |
| S5 | IAEA LiveChart | Cross-check | www-nds.iaea.org/livechart | 2026-01-31 |

---

## Blacklist (NOT Allowed)

- Wikipedia
- Blogs / forums / Stack Exchange
- Undocumented "typical" values
- Random PDFs without DOI
- Textbook approximations without primary source
- Preprints not yet peer-reviewed

---

## Citation Format

Every BL value must include:
```
[BL:S#] (nuclide, field, accessed YYYY-MM-DD)
```

Example:
```
Qα(²¹¹Po) = 7594.5 keV [BL:S2] (Po-211 adopted levels, accessed 2026-01-31)
```

---

## V7.3 Specific Fetches

All new nuclide data fetched 2026-01-31 from NuDat3:

| Nuclide | Fields Retrieved | Source |
|---------|------------------|--------|
| ²¹¹Po | t₁/₂, Qα, Jπ | [BL:S2] |
| ²¹³Po | t₁/₂, Qα, Jπ | [BL:S2] |
| ²¹⁵At | t₁/₂, Qα, Jπ | [BL:S2] |
| ²¹⁶At | t₁/₂, Qα, Jπ | [BL:S2] |
| ²¹⁸At | t₁/₂, Qα, Jπ | [BL:S2] |
| ²¹⁷Rn | t₁/₂, Qα, Jπ | [BL:S2] |
| ²¹⁸Rn | t₁/₂, Qα, Jπ | [BL:S2] |
| ²¹⁹Fr | t₁/₂, Qα, Jπ | [BL:S2] |
| ²²⁵Ac | t₁/₂, Qα, Jπ | [BL:S2] |
| ²²⁹Th | t₁/₂, Qα, Jπ | [BL:S2] |
| ²⁴⁹Cf | t₁/₂, Qα, Jπ | [BL:S2] |
| ²⁵⁰Cf | t₁/₂, Qα, Jπ | [BL:S2] |
| ²⁵¹Cf | t₁/₂, Qα, Jπ | [BL:S2] |

### Daughter Jπ Verifications

| Daughter | Jπ | Source |
|----------|-----|--------|
| ²⁰⁷Pb | 1/2⁻ | [BL:S2] |
| ²⁰⁹Pb | 9/2⁺ | [BL:S2] |
| ²¹¹Bi | 9/2⁻ | [BL:S2] |
| ²¹²Bi | 1⁻ | [BL:S2] |
| ²⁴⁵Cm | 7/2⁺ | [BL:S2] |
| ²⁴⁷Cm | 9/2⁻ | [BL:S2] |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| V7.0 | 2026-01-31 | Initial whitelist |
| V7.1 | 2026-01-31 | Inherited |
| V7.2 | 2026-01-31 | Added daughter Jπ |
| V7.3 | 2026-01-31 | Added access dates; 13 new nuclides |

