# Baseline Build Record

## Audit Session: book2-chapter-audit-v1

| Date | Branch | Commit | Pages | SHA256 | Status |
|------|--------|--------|-------|--------|--------|
| 2026-01-24 | book2-chapter-audit-v1 | e8f55f8 (base) | 387 | 23aee0d7c31520c4dee53299ab45c219a50372bdaa1126f53c553ac2c7e731b9 | PASS |
| 2026-01-24 | book2-chapter-audit-v1 | 6e1a2af (CTX-001) | 387 | 02922e3dbb5200b8dd4885e35b1217ae8edae6925537d3115455ee47a06a3625 | PASS |
| 2026-01-24 | book2-chapter-audit-v1 | CH04 pre-audit | 387 | dfc39cd35ecf750b8a522046def8195d52273143faf679c422d698dfa1ea1bf7 | PASS |
| 2026-01-25 | book2-opr04-delta-equals-Rxi-v1 | 9d2621c (CH05 pre-audit) | 387 | ff207df0ec3f690f84991cf89955ef7453dcc48c93e67cd2a60c260a9f2e94c8 | PASS |
| 2026-01-25 | book2-ch07-openq-remediation-v1 | 6796707 (baseline) | 387 | a32ff75178db20e105864809d5fb5d6c084c6e7bd6e0fae86d7521f279129ef2 | PASS |

## Build Command
```bash
./tools/gate_build.sh
```

## Notes
- Baseline established from book2-global-symbol-table-v1
- All chapter audits must maintain 387 pages
- Build verification required after each chapter's mechanical fixes
