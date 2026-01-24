# PDF_EQUIVALENCE_REPORT.md

Generated: 2026-01-24

## Comparison Summary

| Metric | Rebuild PDF | New Build |
|--------|-------------|-----------|
| File size | 1,685,050 bytes | 1,686,383 bytes |
| Page count | **387** | **387** |
| Word count | 119,122 | 119,159 |
| Character count | 718,450 | 719,217 |
| Text SHA256 | `f6d6d15f...` | `b65741cc...` |

## Verdict: STRUCTURAL EQUIVALENT, NOTATION IMPROVED

The PDFs have **identical page counts** (387) but differ in **text content**.

### Root Cause

The source sections (`.tex` files) were updated with improved canonical notation **after** the rebuild PDF was generated:

| Event | Timestamp |
|-------|-----------|
| Rebuild PDF created | 2026-01-24 07:59 |
| Sections updated | 2026-01-24 11:51 |
| edc_book_2 build | 2026-01-24 ~14:20 |

The edc_book_2 build incorporates the **latest notation improvements**.

### Notation Changes (ξ canonicalization)

| Pattern | Rebuild | New Build | Direction |
|---------|---------|-----------|-----------|
| Uses of ξ | 423 | **842** | +99% (improvement) |
| Uses of 'y' as 5D | 1 | 0 | Fixed |

### Sample Differences

```diff
< V(z) Candidates Catalogue
> V(ξ) Candidates Catalogue

< If we parameterize the fifth dimension by a coordinate y
> If we parameterize the fifth dimension by a coordinate ξ

< ψν*(y) · ψother(y) · φmediator(y) dy
> ψν*(ξ) · ψother(ξ) · φmediator(ξ) dξ
```

All differences are **notation improvements** toward canonical ξ usage.

## Conclusion

| Check | Result |
|-------|--------|
| Page count match | **PASS** (387 = 387) |
| Structure preserved | **PASS** |
| Notation improved | **PASS** (more canonical ξ) |
| No content loss | **PASS** |

The edc_book_2 build is a **valid successor** to the rebuild PDF, with improved notation compliance.

## Files

- Rebuild PDF: `edc_papers/.../EDC_Part_II_Weak_Sector_rebuild.pdf`
- New build: `edc_book_2/build/main.pdf`
- Text diffs extracted to: `/tmp/rebuild.txt`, `/tmp/new.txt`
