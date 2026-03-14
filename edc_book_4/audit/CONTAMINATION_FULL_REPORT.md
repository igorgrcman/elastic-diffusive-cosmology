# Contamination Full Report

**Date:** 2026-02-10
**Scope:** edc_book_4/
**Status:** ✅ PASS

---

## Summary

| Check | Result |
|-------|--------|
| TIER-1 scan (alpha.particle, helion, triton, nucleon, nucleus) | 0 hits |
| TIER-2 scan (proton, neutron, alpha, nuclear, QCD, quark) | 0 hits in Layer A |
| Observerbox mechanism words | 0 hits |
| Path leaks (edc_book_2/src) | 0 hits |
| Content pending placeholders | 0 hits |

---

## Scan Protocol

### TIER-1: Absolute Prohibitions

```bash
perl -0777 -pe 's/\\begin\{observerbox\}.*?\\end\{observerbox\}//sg; \
               s/\\begin\{verbatim\}.*?\\end\{verbatim\}//sg' \
    chapters/*.tex | grep -cEi 'alpha.particle|helion|triton|nucleon|nucleus'
```

**Result:** 0

### TIER-2: Soft Prohibitions (Layer A)

```bash
perl -0777 -pe 's/\\begin\{observerbox\}.*?\\end\{observerbox\}//sg; \
               s/\\begin\{verbatim\}.*?\\end\{verbatim\}//sg' \
    chapters/*.tex | grep -cEi 'proton|neutron|alpha|nuclear|QCD|quark'
```

**Result:** 0 (all TIER-2 terms properly routed to observerbox or Appendix X)

### Observerbox Mechanism Check

```bash
for file in chapters/ch*.tex; do
  perl -0777 -ne 'print $1 while /\\begin\{observerbox\}(.*?)\\end\{observerbox\}/sg' "$file"
done | grep -cEi 'decay|emit|radiat|fission|fusion|tunneling'
```

**Result:** 0 (observerbox contains only projection labels, no mechanism words)

---

## Allowed Content

The following are **allowed** and not counted as contamination:

1. **Observerbox projection labels:** "proton", "neutron" etc. as measurement labels
2. **Appendix X (analogies):** SM comparisons for pedagogical purposes
3. **Appendix Q (quarantine):** Calibrated parameters with empirical origin
4. **Ch. 17 verbatim blocks:** Contamination scan protocol documentation
5. **Source file references:** \source{...} metadata

---

## Observerbox Count

```bash
grep -c '\\begin{observerbox}' chapters/*.tex | grep -v ':0$' | wc -l
```

**Result:** 17 (one per chapter)

---

## Files Scanned

### Chapters (17)
- ch01_proton_ground.tex through ch17_reproducibility.tex

### Appendices (6)
- appA_superheavy_code.tex through appX_analogies.tex

---

## Conclusion

Book IV maintains strict Layer A vocabulary discipline:
- All derivations use EDC-native terminology
- Observer projection labels are quarantined in observerbox
- SM analogies are isolated in Appendix X
- No contamination in main text

**Status:** ✅ PASS — Reader-grade PDF ready
