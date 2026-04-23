# COSMoS Narrative Layer — Step 3 Plan

*Plan document for Step 3 of the cosmos-bc-dss rework: assemble the
narrative layer over the COSMoS graph. Drafted as the carry-over into a
fresh Cowork conversation. Decision record will be a separate note
(`COSMoS_Narrative_Layer.md`) once the open decisions are settled.*

*cdisc-for-ai, 2026-04-23*

---

## Location

Work is isolated in a new top-level folder: **`sdtm-narrative/`**.
Flat sibling to `cosmos-bc-dss/`, `sdtm-test-codes/`, `sdtm-findings/`.
Explorative — this track may later promote stable outputs into
`sdtm-test-codes/` (variable identity) and `cosmos-bc-dss/`
(narrative columns on the graph), or stay as its own delivery track.
That decision comes at close-out, not now.

Folder skeleton (matches the repo convention in `CLAUDE.md`):

```
sdtm-narrative/
├── downloads/          # Thesaurus cache reuse or own copies (gitignored)
├── reference/          # variable-identity source extracts, template catalogue
├── interim/            # per-DSS narrative xlsx, template-tested outputs
├── machine_actionable/ # DataBook outputs (html and/or md)
├── notebooks/          # 40_assemble_narrative, 60_assemble_databooks, 70_validate
├── reports/            # narrative_validation_report.{md,json}, close-out audit
└── docs/               # plan, design record, template catalogue
```

The new folder edits nothing in `cosmos-bc-dss/` or `sdtm-test-codes/`
during Step 3 — it only reads from them. Promotion of outputs back into
those tracks, if any, is a later decision.

Git: work happens on `main` directly, or on a branch of your choosing
(naming suggestion `sdtm-narrative-layer` if you want a branch). The
folder isolation already gives exploratory safety; branch isolation is
optional on top.

## Context — what this step exists for

The Step 2 close-out carried three open branches into a new conversation
(see [`../../cosmos-graph/docs/COSMoS_Next_Steps_Brief.md`](../../cosmos-graph/docs/COSMoS_Next_Steps_Brief.md)).
This plan commits to **Branch A** — the narrative layer. Branches B
(consumer rewiring) and C (upstream flags) stay parked.

The Step 2 scoping brief ([`../../cosmos-graph/docs/COSMoS_Step2_Scoping_Brief.md`](../../cosmos-graph/docs/COSMoS_Step2_Scoping_Brief.md))
argued for reification-as-legibility and named a three-tier serialisation
architecture. Step 2 built Tier 1 (the canonical graph in
`COSMoS_Graph*.xlsx`). Tier 2b (per-DSS prose) and Tier 3 (DataBook
case pairs) are what Step 3 builds.

The Cagle & Shannon argument — LLMs read reified proposition-embedding-
proposition structures better than flat triples — is the design principle.
The Tier 1 graph is the canonical source; Tiers 2b and 3 are legibility
projections of it, not separate data.

## Goal

Two deliverables, different grain, shared template library:

**Tier 2b — `VLM_Narrative` per DSS.** One English paragraph per DSS
(1,326 paragraphs), deterministically assembled from the graph and the
variable-identity lookup. Renders each DSS as a proposition about its
bindings, its slots, and what it does not bind.

**Tier 3 — DataBook case studies.** Prose-with-embedded-facts narrative
spanning multiple DSSs per case (BC + siblings + cross-domain-class +
case specialisations). Formalises the template already demonstrated in
the Glucose / 6MWT / X-Ray HTML stories. Deterministic generation from
the graph — no LLM at write time, only at read time.

Both tiers land under `sdtm-narrative/`. Variable-identity enrichment
that feeds them also lands there during the exploratory phase.

## Sub-steps in order

### 3a — Variable Identity (preparatory, blocking)

Build a variable-level identity table covering the NCIt `CDISC Variable
Terminology` and `CDISC Root Variable Terminology` subsets (already
cached in `sdtm-test-codes/downloads/Thesaurus.txt`).

Output (exploratory location): `sdtm-narrative/reference/SDTM_Variable_Identity.xlsx`.

Expected shape (to confirm on build):
- One row per SDTM variable (PRTRT, MKMETHOD, VSPOS, LBFAST, …).
- Columns: `variable`, `nci_code`, `natural_name`, `definition`,
  `subset` (which NCIt subset sourced the row), `applicable_domains`
  (where it appears in COSMoS VLM rows — join against
  `cosmos-graph/interim/COSMoS_Graph.xlsx/Variables`).
- README sheet per repo convention.

This file is reusable by every downstream consumer and is the single
biggest legibility substitution (`LBFAST` → *fasting status*,
`PRDECOD` → *standardised procedure term*). Build it first so both
tiers can join against it.

Half-day scope per the scoping brief §Move 2c. Self-contained — it is
useful independent of the narrative work. Location decision is open
(see Open Decisions §5); the file can be promoted into
`sdtm-test-codes/machine_actionable/` at close-out.

### 3b — Template design (decision, blocking)

Before writing the assembler, settle the template structure. Open
decisions listed below; the new conversation resolves them.

The existing HTML case pairs (Glucose, 6MWT, X-Ray) are the reference —
reverse-engineer the template from what those stories already do, then
formalise it into one template catalogue per Domain_Class + role
pattern.

Deliverable: a short template catalogue under
`sdtm-narrative/reference/templates/`, one entry per Domain_Class +
role pattern, each with:
- The facts the template reads from the graph.
- The prose form the template emits.
- Natural-English substitutions applied via `SDTM_Variable_Identity`.
- Which traversals the template requires (siblings, cross-domain-class,
  instrument parent, case specialisations).

### 3c — Tier 2b assembly

Notebook: `sdtm-narrative/notebooks/40_assemble_narrative.ipynb`.

Inputs:
- `cosmos-graph/interim/COSMoS_Graph.xlsx`
- `cosmos-graph/interim/COSMoS_Graph_CT.xlsx`
- `sdtm-narrative/reference/SDTM_Variable_Identity.xlsx`
- `sdtm-test-codes/downloads/Thesaurus.txt` (for NCIt definitions where
  not already in `AssignedTerms`).

Output: `sdtm-narrative/interim/COSMoS_Graph_Narrative.xlsx`,
containing a `Narratives` sheet — one row per DSS, with the
`VLM_Narrative` paragraph. Keeps the exploratory work out of the
Step 2 graph file. Promotion back into `COSMoS_Graph.xlsx` as a sheet
or column is a close-out decision.

Template-assembled, not LLM-generated. Deterministic, QC-round-trippable
against source facts.

### 3d — Tier 3 assembly

Notebook: `sdtm-narrative/notebooks/60_assemble_databooks.ipynb`.

Inputs: everything 3c uses, plus the case-pair scope list (which DSSs
group into which case).

Output: `sdtm-narrative/machine_actionable/databooks/*.html` (or
`.md`, decide in 3b). Starts with the three case pairs already modelled
in HTML:
- Glucose (LB specimen-based, with study-intent case specialisations)
- 6MWT (FT instrument-based, classification hierarchy)
- X-Ray (PR + MK cross-domain-class)

The first three DataBooks are the template validation. Additional cases
come later.

### 3e — Validation

Notebook: `sdtm-narrative/notebooks/70_validate_narrative.ipynb`.

Checks:
- Round-trip: every fact in a narrative traces to a row in the graph.
- No fabrication: narrative tokens not in the source vocabulary are
  flagged.
- Variable-name substitutions match `SDTM_Variable_Identity`.
- Template coverage: every DSS gets a paragraph; every case pair gets a
  DataBook.

Output: `sdtm-narrative/reports/narrative_validation_report.{md,json}`.

### 3f — Documentation close-out

At step close:
- Design record: `sdtm-narrative/docs/COSMoS_Narrative_Layer.md`
  (analogous to `cosmos-graph/docs/COSMoS_Flattener_Rewrite.md`).
- Audit: `sdtm-narrative/reports/narrative_layer_audit.md`.
- Promotion decisions (Open Decision §5): whether
  `SDTM_Variable_Identity.xlsx` moves to `sdtm-test-codes/`, whether
  the narrative sheet moves into `COSMoS_Graph.xlsx`, whether
  `sdtm-narrative/` stays as its own track.
- Update `CLAUDE.md` three-layer model to name Tier 2b and Tier 3 as
  first-class artefacts, not aspirational.

## Open decisions for the new conversation

1. **Tier 2b grain.** Per-DSS paragraph (grain matches `DSS` sheet) vs
   per-variable phrase (grain matches `Variables` sheet). The scoping
   brief proposed per-DSS. Variables-grain is finer but might fragment
   the prose. Recommendation in the brief: DSS-grain; confirm on day one.

2. **Tier 3 unit.** One DataBook per case pair (Glucose / 6MWT / X-Ray)
   vs per Domain_Class vs per structural-type. Case-pair-grain matches
   the existing HTML stories. Broader grain is larger documents but
   fewer of them.

3. **Order.** Tier 2b first (refine templates on 1,326 units) vs Tier 3
   first (refine templates on three rich cases). Either works; the
   argument for Tier 3 first is that the HTML stories are the ground
   truth for what "good" looks like, so working from them backwards
   into a template is less speculative. The argument for Tier 2b first
   is bulk coverage and earlier QC surface.

4. **Output format for Tier 3.** Markdown, HTML, or xlsx-embedded. The
   existing case stories are HTML with CSS styling. A markdown Tier 3
   gives git diffability; HTML gives browser rendering. Could be both —
   generate markdown as canonical, render HTML as a view.

5. **Exploratory-vs-promoted paths.** At close-out, three questions:
   (a) does `SDTM_Variable_Identity.xlsx` stay under `sdtm-narrative/`
   or promote to `sdtm-test-codes/machine_actionable/`?
   (b) does the `Narratives` sheet stay in `COSMoS_Graph_Narrative.xlsx`
   or merge into `COSMoS_Graph.xlsx`?
   (c) does `sdtm-narrative/` stay as its own delivery track or fold
   into `cosmos-bc-dss/`?
   Defer all three decisions until Tier 2b templates are validated.

6. **NCIt enrichment scope.** `AssignedTerms` already carries NCI CT
   definitions for 1,170 concept IDs — does the narrative need more
   (synonyms, UMLS/LOINC)? Keep minimal for first cut; extend only if a
   template needs it.

## Success criteria

Step 3 closes when:
- `SDTM_Variable_Identity.xlsx` exists, with a README sheet, covering
  every SDTM variable that appears in any
  `cosmos-graph/interim/COSMoS_Graph.xlsx/Variables` row.
- Every DSS has a `VLM_Narrative` paragraph, deterministically
  assembled, QC-round-trippable.
- The three case pairs (Glucose, 6MWT, X-Ray) have DataBooks of the
  chosen format, regenerable from the graph.
- Validation report passes: no fabrication, full coverage.
- Design note `sdtm-narrative/docs/COSMoS_Narrative_Layer.md` and
  audit `sdtm-narrative/reports/narrative_layer_audit.md` are
  written.
- Open Decision §5 (promotion paths) is resolved.

## Reference artefacts

Graph and CT (read-only inputs):
- `cosmos-graph/interim/COSMoS_Graph.xlsx`
- `cosmos-graph/interim/COSMoS_Graph_CT.xlsx`
- `cosmos-graph/reports/graph_validation_report.{md,json}`

Identity sources (read-only inputs):
- `sdtm-test-codes/downloads/SDTM_Terminology.txt` (SDTM CT 2026-03-27)
- `sdtm-test-codes/downloads/Thesaurus.txt` (NCIt, full)
- `sdtm-test-codes/machine_actionable/SDTM_Test_Identity.xlsx`

Case-pair ground truth (the HTML stories to reverse-engineer from):
- `docs/Glucose_COSMoS_Story.html`
- `docs/Glucose_StudyIntent_Story.html`
- `docs/6MWT_COSMoS_Story.html`
- `docs/6MWT_NCIt_Story.html`
- `outputs/XRay_COSMoS_Story.html`
- `outputs/XRay_PatientBurden_Story.html`

Design context (read-only inputs):
- `cosmos-graph/docs/COSMoS_Next_Steps_Brief.md` — the three-branch
  hand-off this step implements Branch A of.
- `cosmos-graph/docs/COSMoS_Graph_As_Authored.md` — Step 1 graph
  model.
- `cosmos-graph/docs/COSMoS_Flattener_Rewrite.md` — Step 2 design.
- `cosmos-graph/reports/flattener_rewrite_audit.md` — Step 2
  close-out.
- `cosmos-graph/docs/COSMoS_Step2_Scoping_Brief.md` — frozen pre-build
  brief; Moves 2c (variable identity) and 2b (VLM_Narrative) are what
  Step 3 lifts into the plan.

## Meta — how to use this document

Drop a pointer to this file in the first message of the new
conversation:

> *Starting Step 3. Plan in
> `sdtm-narrative/docs/COSMoS_Narrative_Layer_Plan.md`. Working in
> `sdtm-narrative/` (new folder). First decision — 3b open decisions.*

The plan is deliberately scoped at the design-decision level; the new
conversation drives the build.
