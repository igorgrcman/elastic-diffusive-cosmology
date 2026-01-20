# Canon Addendum: Mechanistic Dimensions in EDC

**Status:** Canon Rule (applies to all future EDC documents)
**Date:** 2026-01-20
**KB Reference:** KB-CANON-001

---

## The Principle

> **"In EDC, extra dimensions are not added spatial lengths; they encode physical mechanisms. The brane is a manifestation of the mechanism (bulk → brane → 3D observation), not merely a geometric hypersurface."**

---

## What This Means for Writers

When introducing any of the following concepts:
- Fifth dimension (y, ξ)
- Brane / membrane
- Bulk-brane energy exchange
- Frozen projection operator
- Absorption → dissipation → release pipeline

You **must** include a **Physical Mechanism Paragraph** (2–6 sentences) explaining:

1. **5D Cause:** What happens in the bulk?
2. **Brane Process:** How does the brane absorb/redistribute?
3. **3D Output:** What observers detect
4. **Ledger:** Conservation closure statement

---

## LaTeX Support

Use the helper macro:

```latex
\edcMechanismNote{<bulk cause>}{<brane process>}{<3D output>}
```

See `_shared/style/STYLE_GUIDE.md` for full documentation.

---

## Published DOI Documents

**This canon applies going forward.**

Published DOI documents remain unchanged:
- Weak Program Overview (10.5281/zenodo.18319921)
- Companions N/M/T/P
- Framework v2.0, Paper 3, etc.

These documents already embody the principle but were not written with the explicit `\edcMechanismNote` macro. Future versions or new documents must use the macro.

---

## Related Documents

- **Weak Program Overview §2** — Formal definition of the principle
- **KB-CANON-001** — Full canon rule specification
- **STYLE_GUIDE.md** — Implementation details

---

*Canon established: 2026-01-20*
