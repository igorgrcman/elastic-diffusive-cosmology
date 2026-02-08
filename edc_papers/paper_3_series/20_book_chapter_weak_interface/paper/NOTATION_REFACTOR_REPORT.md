# Notation Refactor Report: z → ξ

**Total replacements:** 265
**Files modified:** 20

## 05_three_generations.tex

Replacements: 6

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 201 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 201 | coordinate $z$ | `coordinate $z$` | `coordinate $\\xi$` |
| 288 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 310 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 320 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 493 | Potential V(z) | `V(z)` | `V(\\xi)` |

## 06_neutrinos_edge_modes.tex

Replacements: 18

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 50 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 63 | Domain z>0 | `z > 0` | `\\xi > 0` |
| 68 | Wavefunction psi(z) | `\psi(z)` | `\\psi(\\xi)` |
| 239 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 241 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 242 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 243 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 243 | Domain z>0 | `z > 0` | `\\xi > 0` |
| 248 | Domain z>0 | `z > 0` | `\\xi > 0` |
| 258 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 266 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 272 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 350 | Domain z>0 | `z > 0` | `\\xi > 0` |
| 414 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 419 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 426 | Domain z>0 | `z > 0` | `\\xi > 0` |
| 442 | at $z = | `at $z =` | `at $\\xi =` |
| 448 | Boundary z=0 | `z = 0` | `\\xi = 0` |

## 07_ckm_cp.tex

Replacements: 2

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 760 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 978 | Profile f(z) | `f(z)` | `f(\\xi)` |

## 09_va_structure.tex

Replacements: 80

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 16 | Half-line domain | `z \in [0, \infty)` | `\\xi \\in [0, \\infty)` |
| 23 | Mass profile m(z) | `m(z)` | `m(\\xi)` |
| 23 | Mass profile m(z) | `m(z)` | `m(\\xi)` |
| 23 | Domain z>0 | `z > 0` | `\\xi > 0` |
| 37 | Mass profile m(z) | `m(z)` | `m(\\xi)` |
| 37 | Domain z>0 | `z > 0` | `\\xi > 0` |
| 54 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 54 | coordinate $z$ | `coordinate $z$` | `coordinate $\\xi$` |
| 57 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 80 | coordinate $z$ | `coordinate $z$` | `coordinate $\\xi$` |
| 81 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 86 | Domain z>0 | `z > 0` | `\\xi > 0` |
| 113 | Mass profile m(z) | `m(z)` | `m(\\xi)` |
| 121 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 139 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 218 | Mass profile m(z) | `m(z)` | `m(\\xi)` |
| 224 | Half-line domain | `z \in [0, \infty)` | `\\xi \\in [0, \\infty)` |
| 225 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 225 | Limit z→∞ | `z \to \infty` | `\\xi \\to \\infty` |
| 236 | Half-line domain | `z \in [0, \infty)` | `\\xi \\in [0, \\infty)` |
| ... | 60 more | ... | ... |

## 11_gf_derivation.tex

Replacements: 5

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 368 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 387 | Mass profile m(z) | `m(z)` | `m(\\xi)` |
| 395 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 474 | Measure dz' standalone | `dz'` | `d\\xi'` |
| 475 | Measure dz' standalone | `dz'` | `d\\xi'` |

## 12_epistemic_map.tex

Replacements: 1

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 511 | Potential V(z) | `V(z)` | `V(\\xi)` |

## ch10_electroweak_bridge.tex

Replacements: 10

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 87 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 88 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 123 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 139 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 173 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 173 | at $z = | `at $z =` | `at $\\xi =` |
| 195 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 218 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 218 | at $z = | `at $z =` | `at $\\xi =` |
| 240 | Profile f(z) | `f(z)` | `f(\\xi)` |

## ch11_g5_canonical_and_kk.tex

Replacements: 4

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 28 | Compact domain | `z \in [0,\ell]` | `\\xi \\in [0, \\ell]` |
| 43 | Mass profile m(z) | `m(z)` | `m(\\xi)` |
| 89 | Boundary z=0 | `z=0` | `\\xi = 0` |
| 111 | Boundary z=0 | `z=0` | `\\xi = 0` |

## ch11_g5_ell_suppression_attempt2.tex

Replacements: 5

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 138 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 150 | Boundary z=0 | `z=0` | `\\xi = 0` |
| 268 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 271 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 278 | Potential V(z) | `V(z)` | `V(\\xi)` |

## ch11_gf_full_closure_plan.tex

Replacements: 3

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 111 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 266 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 321 | Potential V(z) | `V(z)` | `V(\\xi)` |

## ch11_gf_sanity_skeleton.tex

Replacements: 1

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 193 | Mass profile m(z) | `m(z)` | `m(\\xi)` |

## ch11_opr20_attemptF_mediator_bvp_junction.tex

Replacements: 9

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 24 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 25 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 28 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 28 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 28 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 32 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 33 | Compact domain | `z \in [0, \ell]` | `\\xi \\in [0, \\ell]` |
| 107 | at $z = | `at $z =` | `at $\\xi =` |
| 137 | Boundary z=0 | `z = 0` | `\\xi = 0` |

## ch11_opr20_attemptG_BC_provenance.tex

Replacements: 7

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 31 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 32 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 33 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 34 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 55 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 61 | Field phi(z) | `\phi(z)` | `\\phi(\\xi)` |
| 63 | Field phi(z) | `\phi(z)` | `\\phi(\\xi)` |

## ch11_opr20_attemptG_derive_alpha_from_action.tex

Replacements: 3

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 241 | Boundary z=0 | `z=0` | `\\xi = 0` |
| 249 | Boundary z=0 | `z=0` | `\\xi = 0` |
| 257 | Boundary z=0 | `z = 0` | `\\xi = 0` |

## ch11_opr20_attemptH1_mediator_identity.tex

Replacements: 7

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 62 | Compact domain | `z \in [0, \ell]` | `\\xi \\in [0, \\ell]` |
| 75 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 76 | Field phi(z) | `\phi(z)` | `\\phi(\\xi)` |
| 79 | Field phi(z) | `\phi(z)` | `\\phi(\\xi)` |
| 83 | Field phi(z) | `\phi(z)` | `\\phi(\\xi)` |
| 90 | Boundary z=0 | `z=0` | `\\xi = 0` |
| 123 | Boundary z=0 | `z=0` | `\\xi = 0` |

## ch11_opr20_attemptH2_delta_Rxi_hard_audit.tex

Replacements: 4

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 151 | Limit z→0 | `z \to 0` | `\\xi \\to 0` |
| 184 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 530 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 533 | Boundary z=0 | `z = 0` | `\\xi = 0` |

## ch11_opr20_attemptH_delta_equals_Rxi.tex

Replacements: 2

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 366 | Field phi(z) | `\phi(z)` | `\\phi(\\xi)` |
| 425 | Potential V(z) | `V(z)` | `V(\\xi)` |

## ch12_bvp_workpackage.tex

Replacements: 30

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 21 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 34 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 54 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 54 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 101 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 107 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 107 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 116 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 117 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 127 | Boundary z=0 | `z = 0` | `\\xi = 0` |
| 134 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 148 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 152 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 152 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 152 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 152 | Second derivative d²/dz² | `\frac{d^2}{dz^2}` | `\\frac{d^2}{d\\xi^2}` |
| 158 | Compact domain | `z \in [0, \ell]` | `\\xi \\in [0, \\ell]` |
| 159 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 161 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 167 | Potential V(z) | `V(z)` | `V(\\xi)` |
| ... | 10 more | ... | ... |

## ch14_bvp_closure_pack.tex

Replacements: 67

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 43 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 79 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 83 | Mass profile m(z) | `m(z)` | `m(\\xi)` |
| 91 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 107 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 110 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 117 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 119 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 157 | Profile f(z) | `f(z)` | `f(\\xi)` |
| 215 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 218 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 243 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 255 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 261 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 269 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 331 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 347 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 355 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 377 | Potential V(z) | `V(z)` | `V(\\xi)` |
| 388 | Potential V(z) | `V(z)` | `V(\\xi)` |
| ... | 47 more | ... | ... |

## ch7_z2_parity_origin.tex

Replacements: 1

| Line | Pattern | Before | After |
|------|---------|--------|-------|
| 59 | Boundary z=0 | `z = 0` | `\\xi = 0` |

