# Option A (Unify to ζ) - NOT RECOMMENDED

**Date:** 2026-01-24
**Status:** REJECTED in favor of Option B

## Why Option A Is Not Recommended

Option A would require changing `z` → `ζ` (zeta) in **54+ files** across Part II:

### Files Requiring Changes
1. `sections/02_frozen_regime_foundations.tex`
2. `sections/09_va_structure.tex`
3. `sections/ch11_opr20_attemptF_mediator_bvp_junction.tex`
4. `sections/ch11_g5_canonical_and_kk.tex`
5. ... (50+ more files)

### Risks
1. **Scope creep:** 54+ files is a massive undertaking
2. **Label breakage:** Many `\label{eq:*_z_*}` would need updating
3. **ζ collision:** Greek ζ might collide with Riemann zeta function notation
4. **Code sync:** BVP verification suite uses `z` throughout

### Conclusion
**Option B (keep z + mapping)** achieves the same clarity with minimal changes:
- Only 2 files modified
- Explicit mapping statement added
- Dimensionless variable changed from ξ → z̃

## If Option A Were Required

The approach would be:
```bash
# Replace z → ζ in math contexts only
sed -i '' 's/\$z\$/\$\\zeta\$/g' sections/*.tex
sed -i '' 's/\\(z\\)/\\(\\zeta\\)/g' sections/*.tex
# ... many more patterns

# Update labels
sed -i '' 's/label{eq:.*_z_/label{eq:.*_zeta_/g' sections/*.tex
```

This is error-prone and not recommended.

---

**RECOMMENDATION:** Use branch `part2-notation-mapping-keep-z` (Option B)
