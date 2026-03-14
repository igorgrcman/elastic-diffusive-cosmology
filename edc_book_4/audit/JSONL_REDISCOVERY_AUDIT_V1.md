# JSONL Rediscovery Audit — EDC Session Archives

**Date:** 2026-03-13
**Branch:** `research/topological-pinning-v7_8-integration`
**Type:** Discovery-only archival mining — no canonization, no implementation
**Scope:** All EDC-related JSONL session files in `Claude_Projects_files`

---

## 1. Executive Verdict

The JSONL archive contains **no genuinely overlooked derivation** that would
change the current status of the V(q) node-well problem or the neutron-line
closure chain. The archive is dominated by Book 2 work (OPR-19 through
OPR-22, G_F closure spine, BVP work packages) and early-stage alpha/G_N
derivation attempts — all of which either already live in the repo or have
been superseded by later work on the current branch.

Three items have marginal residual value:

1. **5D analytic failure certificate** (session `a921f1e0`): three named
   missing lemmas (P-sum, P-scale, P-epsilon_0) that block a full 5D
   analytic derivation. Not directly relevant to Book 4, but worth
   preserving as a structural constraint.

2. **Chern-Simons / winding number content** (sessions `73d92ff5`,
   `1ebe75c8`, `ebf566cc`): flavor quantum number F = ∫_Σ₃ ω₃ (mod 3)
   from Chern-Simons 3-form. This is conceptual infrastructure for the
   "topological contribution" escape route listed in the Phase 2 plan.
   However, it is speculative [M] and has never been connected to V(q).

3. **Put C Variant 3 node-well code** (session `22826edd`): the
   phenomenological Gaussian V_node(q) = -V₀ exp(-(q-q*)²/2w²) code
   with explicit metastability detection. Already classified as
   forbidden [P/Cal] donor in the current branch.

**Bottom line:** The rediscovery pass confirms that the current branch
already contains the distilled output of this archive. No new actionable
content was found.

---

## 2. Scope of the Rediscovery Pass

### 2.1 Files Inspected

| # | UUID (short) | Size | Project Area | Date Range |
|---|---|---|---|---|
| 1 | `98cc5184` | 211 MB | EDC-Research-PRIVATE | ~2026-01 |
| 2 | `22826edd` | 202 MB | EDC-Research-PRIVATE | ~2026-01 |
| 3 | `73d92ff5` | 106 MB | EDC-Research-PRIVATE | ~2026-01 |
| 4 | `a921f1e0` | 52 MB | EDC-Research-PRIVATE | 2026-01-13 |
| 5 | `19828e96` | 33 MB | EDC-Research-PRIVATE | 2026-01-13+ |
| 6 | `1ebe75c8` | 9.3 MB | EDC-Research-PRIVATE | ~2026-01 |
| 7 | `d8721dcb` | 7.3 MB | EDC-Research-PRIVATE | 2026-01-12 |
| 8 | `b7ce1b0c` | 2.4 MB | EDC-Research-PRIVATE | 2026-01-12 |
| 9 | `bebfe539` | 1.4 MB | EDC-Research-PRIVATE | 2026-01-11 |
| 10 | `e7793783` | 175 KB | EDC-Research-PRIVATE | 2026-01-23 |
| 11 | `c768e326` | 134 KB | EDC-Research-PRIVATE | 2026-01-24 |
| 12 | `ebf566cc` | 79 MB | paper-gravity-block003 | 2026-02-03+ |
| 13 | `5251e090` | 16 MB | EDC-Research | 2026-01-11 |
| 14 | `ce8dadbd` | 3.3 MB | EDC-Research | 2026-01-11 |
| 15 | `904e1f44` | 438 KB | EDC-Project | 2026-01-29 |
| 16 | `73a19d5e` | 1.9 KB | EDC-Research-PRIVATE | ~2026-01 |

**Total:** 16 main session files, ~724 MB of JSONL content.
Subagent files were excluded (they mirror parent session content).

### 2.2 Scope Limitation

This is a discovery pass only. Archived content is not evidence. Session
conclusions are not canonical truth. No content from this audit is
promoted to [Dc] or [Der] status.

---

## 3. Method

### 3.1 Search Strategy

Each JSONL file was searched with `grep -ci` for four groups of
EDC-specific terms:

- **Group A** (neutron-line): V_node, V_bulk, node well, double well,
  instanton, WKB, prefactor, Put C, S5D_TO_SEFF, thick junction, Israel,
  backreaction, bulk gravity
- **Group B** (audit/epistemic): forensic audit, donor normalization,
  no-go, bounded insufficiency, dead end, circularity, smuggling,
  anti-smuggling, closure pack, route map, gap register
- **Group C** (gravity/KK): OPR-19..22, G_F, G_N, Fermi, AdS5,
  Einstein-Hilbert, GHY, Robin BC, Sturm-Liouville, BVP, full5d
- **Group D** (physics lanes): Helfrich, xi-BC, flux quantization,
  non-monotone, non-separable, higher-order brane, Chern-Simons, winding

Files with significant hit counts were context-searched with
`grep -o '.{0,120}PATTERN.{0,120}'` to extract snippets.

### 3.2 High-Value Criteria

An item qualified as "high-value rediscovery" if it:
- Contains a derivation idea not obviously present in current branch
- Contains a dead-end/no-go result worth preserving
- Contains a circularity warning still relevant
- Contains a branch/file pointer to forgotten material

---

## 4. Top Rediscovered Items

### 4.1 5D Analytic Derivation Failure Certificate

- **Provenance:** `a921f1e0` (52 MB)
- **Classification:** R3 (dead-end worth preserving)
- **Content:** Full 5D analytic derivation attempt with **RESULT: PARTIAL
  FAILURE**. Three critical lemmas cannot be derived from 5D action alone:
  P-sum (mass summation), P-scale (mass scale selection), P-epsilon_0
  (permittivity origin). The sigma-from-pressure derivation
  σ = 2πR_ξ² ρ_P succeeded independently.
- **Current integration:** Not explicitly preserved in Book 4.
  The failure certificate is relevant as a structural constraint on
  what S_EH + S_NG cannot produce, paralleling the N1/N7/N2 results.

### 4.2 Chern-Simons Flavor Quantum Number

- **Provenance:** `73d92ff5` (106 MB), `1ebe75c8` (9.3 MB), `ebf566cc` (79 MB)
- **Classification:** R2 (supporting note)
- **Content:** F = ∫_Σ₃ ω₃ (mod 3), where ω₃ is the Chern-Simons 3-form
  on the defect worldvolume. Tagged [M] (model-level). Used for flavor
  assignment in the vortex defect framework. 103 Chern-Simons hits in
  `73d92ff5` alone, plus winding number content (943 hits).
- **Current integration:** Not integrated into Book 4. The Chern-Simons
  form is part of the "topological contribution" escape route identified
  in the Phase 2 plan, but has never been connected to V(q) or the
  node-well sector. Remains speculative.

### 4.3 OPR-19 through OPR-22: G_F Closure Spine

- **Provenance:** `22826edd` (202 MB), `98cc5184` (211 MB), `ebf566cc` (79 MB)
- **Classification:** R5 (already integrated)
- **Content:** G_F = g₅² ℓ² I₄/x₁² [Dc] with no-smuggling guardrails.
  OPR-19 (g₅ value, 4π derivation), OPR-20 (mediator mass, attempts D-H),
  OPR-21 (BVP mode profiles), OPR-22 (full G_F closure plan).
  Extensive content across all three large sessions.
- **Current integration:** All OPR content lives in Book 2 branches
  (`book2-opr19-*`, `book2-opr20-*`, `book2-opr21-*`, `book2-opr22-*`)
  and the gravity paper. This is NOT Book 4 content.

### 4.4 Put C Variant 3: Phenomenological Node Well

- **Provenance:** `22826edd` (202 MB)
- **Classification:** R4 (circularity warning)
- **Content:** V_node(q) = -V₀ exp(-(q-q*)²/2w²) with three free
  parameters (V₀, q*, w). Computational code demonstrating that this
  form produces metastability when V₀ ~ few MeV, q* ~ 0.1-0.3 fm.
  The code explicitly detects barrier position, barrier height, and
  metastable minimum.
- **Current integration:** Classified as forbidden [P/Cal] donor in
  `PHASE2_WP1_DONOR_NORMALIZATION.md`. The code is on branch
  `putC-computation-v1`. The phenomenological form is the KNOWN gap —
  it works but is not derived.

### 4.5 G_N Derivation Chain (Gravity Paper)

- **Provenance:** `ebf566cc` (79 MB)
- **Classification:** R5 (already integrated)
- **Content:** Full chain from 5D action to G_N. Multiple derivation
  versions (v6 through v28+). Key result: G_N = κ₅²/(6πL). Bridge
  slot identified: G_N reduces to M₅³ I. Tautology audit (MEDIUM risk:
  underdetermination not circularity). σ_tilde definition and
  dimensional verification.
- **Current integration:** Lives in `edc_papers/paper_gravity_block003/`
  and gravity-related branches. Already sealed in repo.

### 4.6 Prove-or-Fail Anti-Smuggling Framework

- **Provenance:** `b7ce1b0c` (2.4 MB), `bebfe539` (1.4 MB)
- **Classification:** R5 (already integrated, generalized)
- **Content:** Explicit prove-or-fail protocol: lemma structure
  (E1-E3, P1-P4) with D/Dc/P/FAIL status labels. Rules:
  "No smuggling (4π/3 and (2π²)³ must EMERGE from integrals)",
  "Fail fast (if stuck, say WHY)". Three alpha derivation routes
  with negative results accepted.
- **Current integration:** The anti-smuggling framework has been
  generalized and strengthened in Book 4's contamination policy
  (CR1-CR16). The specific lemma structure is historical.

### 4.7 Lambda Pinning from Self-Adjointness + Topological Quantization

- **Provenance:** `ebf566cc` (79 MB), derivation v28 P36
- **Classification:** R2 (supporting note)
- **Content:** Two tracks: (A) Sturm-Liouville self-adjoint extensions
  with Robin BC → parameter constraints. (B) Chern-Simons/WZW boundary
  quantization → integer quantization condition λ = c_λ · n. Target:
  derive λ from topological quantization.
- **Current integration:** Not integrated into Book 4. This belongs
  to the "higher-order brane terms" or "topological contributions"
  escape routes. No V(q) connection established.

---

## 5. Reusable Donors

| # | Item | Provenance | Why Useful | Integration Status | Recommended Action |
|---|------|-----------|------------|-------------------|-------------------|
| — | — | — | — | — | — |

**None identified.** All potentially reusable content is either already
integrated (OPR items, Put C corridor, G_N chain) or too speculative to
qualify as a donor (Chern-Simons, lambda pinning).

---

## 6. Supporting Notes

| # | Item | Provenance | Note |
|---|------|-----------|------|
| 1 | Chern-Simons flavor quantum number | `73d92ff5`, `1ebe75c8` | F = ∫ω₃ (mod 3). Tagged [M]. Not connected to V(q). |
| 2 | Lambda pinning via topological quantization | `ebf566cc` P36 | Track A (SL extensions) + Track B (CS/WZW). Conceptual only. |
| 3 | sigma-from-pressure derivation | `a921f1e0` | σ = 2πR_ξ²ρ_P. Book 2 scope, not Book 4. |
| 4 | WKB turning points forensic audit | `19828e96` | Detailed audit of WKB structure. Already reflected in ch06/ch09. |

---

## 7. Dead Ends Worth Preserving

| # | Dead End | Provenance | Why It Still Matters |
|---|---------|-----------|---------------------|
| 1 | 5D analytic partial failure (P-sum, P-scale, P-epsilon_0) | `a921f1e0` | Constrains what pure 5D action can derive. Named missing lemmas identify the gap. Relevant if the node-well search eventually broadens beyond S_EH + S_NG. |
| 2 | Put C V1-V2 no-go | `22826edd` | Minimal NG action produces no metastability. Already integrated in `PHASE2_WP1_DONOR_NORMALIZATION.md`. |
| 3 | Helfrich route NO-GO (260/260) | `22826edd`, `98cc5184` | Membrane bending energy does not generate node well within action class. Already classified in Phase 2 plan. |
| 4 | G_N tautology audit: MEDIUM risk | `ebf566cc` | Underdetermination, not strict circularity. σ ~ 10⁵³ GeV⁴ reproduces G_N but the problem is underdetermination. |

---

## 8. Circularity / Smuggling Warnings

| # | Warning | Provenance | Current Relevance |
|---|---------|-----------|-------------------|
| 1 | Put C V3 node well is [P/Cal] with 3 free parameters | `22826edd` | Already classified as forbidden donor (F-2 in WP1 normalization). Still relevant: any future V_node attempt must NOT import V₀, q*, w from this variant. |
| 2 | "No chirality smuggling" — chirality is consequence of inflow, not assumption | `22826edd` | Book 2 scope. Not directly relevant to Book 4 neutron line. |
| 3 | sigma = ℏc/r_e³ is circular if r_e = α·ℏ/(m_e·c) | `d8721dcb` | Already encoded in Book 4's forbidden-import list (CR5, CR7). |
| 4 | G_N derivation has underdetermination risk (calibrate σ from G_N, then derive G_N — circular) | `ebf566cc` | Book 2/gravity paper scope. Book 4 uses σ as [Dc] from R_ξ route, avoiding this loop. |

---

## 9. Duplicate / Already Integrated Items

| # | Item | Provenance | Where Integrated |
|---|------|-----------|-----------------|
| 1 | OPR-19 through OPR-22 | `22826edd`, `98cc5184`, `ebf566cc` | Book 2 branches (book2-opr19-*, etc.) |
| 2 | Put C corridor (V1-V3) | `22826edd` | `putC-computation-v1` branch + `PHASE2_WP1_DONOR_NORMALIZATION.md` |
| 3 | Helfrich NO-GO | `22826edd`, `98cc5184` | `helfrich-well-from-action-v1` branch + Phase 2 plan |
| 4 | ξ-BC NO-GO | `22826edd` | `frozen-brane-bc-v1` branch + Phase 2 plan |
| 5 | V_geom(q) R3 closure | `22826edd` | `app_Vq_chosen_path.tex` on current branch |
| 6 | G_N derivation chain | `ebf566cc` | `edc_papers/paper_gravity_block003/` |
| 7 | σ_tilde definition/verification | `ebf566cc`, `98cc5184` | `sigma_tilde_value.json` on main |
| 8 | Plan A/B gravity derivation | `5251e090`, `ce8dadbd` | `EDC_Research/results/` |
| 9 | Epistemic tag system ([Der], [Dc], [P], [Cal], [BL]) | Multiple | `preamble.tex`, contamination policy |
| 10 | Anti-smuggling framework | `b7ce1b0c`, `bebfe539` | CR1-CR16 in Book 4 |

---

## 10. Crosswalk to Current Research State

### 10.1 Closed Lanes (N1, N7, N2)

- **N1 (Israel thin-junction):** Put C V1-V2 no-go in archive matches
  the N1 bounded no-go on current branch. Archive provides historical
  context but no new information.
- **N7 (thick-junction core):** No direct archive content for N7
  (this lane was opened after the archive sessions ended).
- **N2 (bulk backreaction):** Archive contains Israel/backreaction
  references (465-1339 lines per file) but these are in the gravity
  derivation context (G_N, G_F), not in the V(q) node-well context.
  The N2 WP2 result (κ₅²-suppression) is new work not in the archive.

### 10.2 Remaining Escape Routes

- **Non-monotone core profile (N7 escape):** Archive contains the
  Put C V3 phenomenological Gaussian well centered at q* > 0.
  This is exactly the shape that the N7 no-go theorem identifies as
  the escape route — but the archive version is [P/Cal], not derived.
  No new physics connection found.
- **Higher-order brane terms:** Lambda pinning from topological
  quantization (P36 in `ebf566cc`) is conceptually adjacent.
  No V(q) calculation exists.
- **Topological contributions (Chern-Simons, winding):** Archive
  contains flavor quantum number F = ∫ω₃ (mod 3). This is infrastructure
  for defect classification, not for V(q). No connection to node-well
  sector has been established in any session.
- **M₅ < 200 MeV:** No archive session explores low-M₅ scenarios.

### 10.3 General EDC Infrastructure

The archive contains the complete historical development of:
- Epistemic tagging system (evolved from simple D/P labels to the
  current [Der]/[Dc]/[P]/[Cal]/[BL]/[I] framework with CR1-CR16)
- Anti-smuggling methodology (prove-or-fail, named missing lemmas,
  forbidden-import lists)
- G_F/G_N derivation chains (Book 2 scope)

All of this is already integrated into the current branch in mature form.

### 10.4 Irrelevant but Preserved

- Alpha derivation attempts (5D harmonic, vortex, 3-route)
- Matter-antimatter research summaries
- Visual consistency audits
- MacTeX build infrastructure

---

## 11. Recommended Follow-up

1. **No implementation action required.** The archive contains no
   overlooked derivation that would advance the node-well problem.

2. **Optional provenance note:** The 5D analytic failure certificate
   (P-sum, P-scale, P-epsilon_0 missing lemmas from `a921f1e0`) could
   be referenced in a future "what we tried" appendix if Book 4 ever
   gets a comprehensive dead-end register beyond the current Phase 2
   appendices.

3. **No re-mining recommended.** The session archive has been
   comprehensively searched. Future rediscovery passes on the same
   files are unlikely to yield new value.

---

## 12. Bottom Line

The rediscovery pass was worth doing as a completeness check. It confirms
that the current working branch already contains the distilled, classified,
and epistemically tagged output of ~724 MB of archived Claude sessions.

**What was found:** Historical derivation attempts (G_N, G_F, alpha),
dead-end certificates (Helfrich, Put C V1-V2, 5D analytic), circularity
warnings (V3 node well, σ from r_e), and infrastructure (epistemic tags,
anti-smuggling rules). All either already integrated or irrelevant to
the current Book 4 neutron-line program.

**What was NOT found:** No overlooked V(q) derivation. No forgotten
node-well mechanism. No hidden donor that could advance the closed
N1/N7/N2 lanes. No suppressed negative result that changes the
current assessment.

The archive is clean. The current branch is the canonical state.

---

*Generated by JSONL rediscovery pass, 2026-03-13. Discovery only — no
content from this audit is promoted to canonical status.*
