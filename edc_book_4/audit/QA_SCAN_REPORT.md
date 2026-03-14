# QA Scan Report — Book IV Final

**Date:** 2026-02-10
**PDF:** main.pdf (224 pages)

---

## 1. Contamination Scans

### TIER-1: Absolute Prohibitions
**Pattern:** `alpha.particle|helion|triton|nucleon|nucleus`

```bash
for f in chapters/*.tex; do
  perl -0777 -pe 's/\\begin\{observerbox\}.*?\\end\{observerbox\}//sg;
                  s/\\begin\{verbatim\}.*?\\end\{verbatim\}//sg' "$f"
done | grep -ciE 'alpha.particle|helion|triton|nucleon|nucleus'
```

**Result:** 0

### TIER-2: Layer A Strict
**Pattern:** `proton|neutron|alpha|nuclear|QCD|quark`
**Exclusions:** observerbox, verbatim, comments (`%`), `\source{}`

```bash
for f in chapters/*.tex; do
  perl -0777 -pe 's/\\begin\{observerbox\}.*?\\end\{observerbox\}//sg;
                  s/\\begin\{verbatim\}.*?\\end\{verbatim\}//sg;
                  s/^%.*$//gm; s/\\source\{[^}]*\}//g' "$f"
done | grep -ciE 'proton|neutron|alpha|nuclear|QCD|quark'
```

**Result:** 0

### Allow-Zone Hits (acceptable)
**Count:** 15 (all in `% Source:` comments or `\source{}` metadata)

| Location | Pattern | Zone |
|----------|---------|------|
| ch01 lines 4,12,77 | `proton_anchor` | comment |
| ch02 lines 4,13 | `NEUTRON` | comment |
| ch03 lines 4,12 | `NEUTRON` | comment |
| ch09 lines 4,7,14 | `NEUTRON` | comment |
| ch13 lines 4,14 | `alpha15` | comment/source |
| ch14 lines 4,7,14 | `alpha` | comment/source |

---

## 2. Observerbox Mechanism-Word Scan

**Banlist:** `decay|emit|radiat|fission|fusion|tunneling|beta|gamma`

```bash
for f in chapters/*.tex; do
  perl -0777 -ne 'print $1 while /\\begin\{observerbox\}(.*?)\\end\{observerbox\}/sg' "$f"
done | grep -ciE 'decay|emit|radiat|fission|fusion|tunneling|beta|gamma'
```

**Result:** 0

---

## 3. Placeholder Scan

### Sources (.tex files)

| Pattern | Count |
|---------|-------|
| `Content pending` | 0 |
| `[Content pending:` | 0 |
| `INSERT` | 0 |
| `TODO: insert` | 0 |

### PDF

| Pattern | Count |
|---------|-------|
| `Content pending` | 0 |
| `Chapter ??` | 0 |
| `??` (unresolved refs) | 0 |

---

## 4. Path Leak Scan

### Sources

| Pattern | Count |
|---------|-------|
| `edc_book_` | 0 (in .tex) |
| `/Users/` | 0 |
| `src/derivations` | 0 (in .tex) |

### PDF

| Pattern | Count |
|---------|-------|
| `edc_book_` | **0** |
| `src/derivations` | **0** |
| `/Users/` | **0** |
| `elastic-diffusive-cosmology` | **0** |

---

## Summary

| Gate | Result |
|------|--------|
| TIER-1 contamination | ✅ 0 |
| TIER-2 Layer A | ✅ 0 |
| Observerbox mechanism words | ✅ 0 |
| Placeholders (source) | ✅ 0 |
| Placeholders (PDF) | ✅ 0 |
| Path leaks (PDF) | ✅ 0 |

**Status:** ✅ ALL PASS
