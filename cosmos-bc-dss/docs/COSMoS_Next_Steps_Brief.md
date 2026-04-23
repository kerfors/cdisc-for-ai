# COSMoS — Next Steps Brief

**Purpose.** Carry-over brief for a new conversation after Step 2 of the
`cosmos-bc-dss` rework has landed on `main`. Frames the three branches
that are open and the state each one starts from. Not a plan — a scoping
document so the next conversation can pick a branch and commit to it.

**Status at hand-off (2026-04-22).** Step 1 (make the inherent graph
model explicit) and Step 2 (schema-driven flattener over the CDISC
Excel export) are both complete and merged. Legacy `COSMoS_BC_DSS.xlsx`
pipeline is left in place until consumer tracks are rewired.

---

## Where Step 2 landed

Two interim workbooks, one per concern:

- `cosmos-bc-dss/interim/COSMoS_Graph.xlsx` — lossless-over-source graph
  projection of COSMoS. Sheets: `BC`, `DSS`, `Variables` (VLM-row grain,
  carries the reification quad inline), `Relationships` (reified edges,
  long format), `Codelists`.
- `cosmos-bc-dss/interim/COSMoS_Graph_CT.xlsx` — NCI EVS SDTM CT
  enrichment of the bindings and pinned terms. Sheets: `Codelists`,
  `CodelistTerms`, `AssignedTerms`, `Unresolved`, `Anomalies`.

Notebooks (numbered to reflect pipeline position, not chronological order):

- `10_flatten_schema_driven.ipynb` — SchemaView-driven flatten, xlsx → Graph.
- `20_resolve_ct.ipynb` — Graph + SDTM CT 2026-03-27 → Graph_CT.
- `30_validate_graph.ipynb` — eight checks; emits
  `reports/graph_validation_report.{md,json}`.
- `50_query_examples.ipynb` — query cookbook, eight queries pinned to
  the story-pair DSSs (GLUCPL, SIXMW101, SGBESCR + X-Ray cross-domain).

Design decisions, counts, and validation triage are in
[`docs/COSMoS_Flattener_Rewrite.md`](COSMoS_Flattener_Rewrite.md) and
[`reports/flattener_rewrite_audit.md`](../reports/flattener_rewrite_audit.md).
The graph model itself is documented in
[`docs/COSMoS_Graph_As_Authored.md`](COSMoS_Graph_As_Authored.md).

## What Step 2 validated from the scoping brief

The [Step 2 scoping brief](COSMoS_Step2_Scoping_Brief.md) (frozen
2026-04-21, pre-build) argued for *reification-as-legibility*: make
every COSMoS fact readable as a proposition embedded in a larger
propositional structure, rather than as a flat row. The build
validated that frame but replaced the richer-flat-row path with a
schema-driven split:

- The reification quad (`subject`, `linking_phrase`, `predicate_term`,
  `object`) that the scoping brief proposed inventing in a
  `VLM_Summary` grammar was already authored by CDISC in the COSMoS
  LinkML schema and the xlsx source. Step 1 surfaced that; Step 2
  promoted it to a first-class sheet (`Relationships`) and inlined it
  on `Variables`.
- The scoping brief's coverage-matrix proposal (Move 6) becomes a
  `GROUP BY codelist_concept_id` over `Variables` — one-liner against
  the graph. Materialising it as a sheet is optional.
- The scoping brief's cross-reference columns with reified descriptions
  (Move 4) become graph traversals. The X-Ray query in notebook 50
  exercises this and exposes the codelist-reuse caveat noted below.
- The natural-English variable and codelist names (Move 2c) stay
  aspirational and migrate to Step 3 (see below).

The three case pairs (Glucose, 6MWT, X-Ray) that motivated the scoping
brief are still the reference cases — same files under `docs/` and
`outputs/`. The POSITION coverage asymmetry on imaging DSSs and the
X-Ray cross-domain-class concept traversal both answer cleanly from
the new graph shape.

## Open branches

Three branches are open. They are independent — any one can be picked
up first without blocking the others. Listed in the order that matches
the Step 2 close-out; the next conversation should pick one.

### Branch A — Step 3: NCIt narrative layer

Take the `Relationships` quads plus NCIt concept anchors and assemble
DSS-level prose. The scoping brief called this Tier 2b (`VLM_Narrative`)
and Tier 3 (DataBooks).

Inputs available now:
- `Relationships` sheet (reified quads, 12,364 rows).
- `AssignedTerms` sheet (1,170 unique NCIt concept IDs with NCI CT
  definitions and preferred terms).
- `Thesaurus.txt` cache in `sdtm-test-codes/downloads/` (NCIt broader
  than the SDTM CT subset).

Decisions to make up front:
- Tier 2b vs Tier 3 first — one prose paragraph per DSS (2b) is the
  shorter deliverable; a full DataBook per case pair (3) is the more
  ambitious one.
- Natural-English variable names: build `SDTM_Variable_Identity.xlsx`
  (subset `CDISC Variable Terminology` / `CDISC Root Variable
  Terminology` from Thesaurus) before starting, or inline the lookup.
- Template approach: deterministic assembly per Domain_Class, not
  LLM-generated. QC round-trips against the source.

Out of scope: resolving the four Pattern-A NCIt concepts (TPLAB,
SAR2AB, TUMERGE, TUSPLIT) — those belong in Branch C.

### Branch B — Consumer-track rewiring

Rewire `sdtm-findings/` (and, downstream of it, `sdtm-domain-reference/`
where it depends on COSMoS coverage) to read `COSMoS_Graph*.xlsx`
instead of the legacy `COSMoS_BC_DSS.xlsx`.

Starting state:
- Legacy `interim/COSMoS_BC_DSS.xlsx` still builds and still feeds the
  existing consumers — nothing is broken right now.
- The `Identity` back-compat sheet was not built (audit §4); consumers
  cannot switch files with a column-rename.
- The two-sheet consumer output shape (Test_Identity + Measurement_Specs)
  should be preserved — that's the contract downstream readers rely on.

Decisions to make up front:
- Rewire one structural-type consumer first (specimen-based, measurement,
  or instrument) vs. all three in one pass. The specimen-based consumer
  has the richest coverage; the instrument consumer has the cleanest
  joins.
- Retire `COSMoS_BC_DSS.xlsx` at the end of the rewire, or leave both
  pipelines in place. If retiring, the legacy flattener notebooks
  (`COSMoS_BC_DSS_Flatten*.ipynb`) also go.

### Branch C — Upstream flags

Four findings from the Step 2 validation triage, documented in the
audit (§5.2, §5.3). Each is an authoring or subset issue outside this
repo, but the next conversation is where the flags get drafted and
sent.

To the COSMoS authoring working group:
1. TU TUMERGE / TUSPLIT — `assigned_term_concept_id` points at
   finding-state concepts (C94525, C96642). Correct TESTCD anchors
   already exist in SDTM CT: C225437 "Confluent Tumor Masses Assessment"
   and C225438 "Tumor Fragmentation Assessment".
2. DM ETHNIC / RACE — `codelist_concept_id` points at legacy codes
   (C66790, C74457). Superseded by C128690 ETHNICC and C128689 RACEC.

To the CDISC SDTM CT team:
3. MBTESTCD / MBTEST subset does not yet carry C132388 "Treponema
   pallidum Antibody Measurement" or C171439 "SARS-CoV-2 Antibody
   Measurement" — valid NCIt Laboratory Procedures, referenced by MB
   TPLAB and MB SAR2ABDET.
4. VSRESU (C66770) codelist does not carry C105484 "fraction of 1",
   needed for OXYSAT.VSSTRESU.

This is paperwork, not code. Lightest of the three branches.

## Reference artefacts

Primary:
- `cosmos-bc-dss/interim/COSMoS_Graph.xlsx`
- `cosmos-bc-dss/interim/COSMoS_Graph_CT.xlsx`
- `cosmos-bc-dss/docs/COSMoS_Graph_As_Authored.md`
- `cosmos-bc-dss/docs/COSMoS_Flattener_Rewrite.md`
- `cosmos-bc-dss/reports/flattener_rewrite_audit.md`
- `cosmos-bc-dss/reports/graph_validation_report.{md,json}`
- `cosmos-bc-dss/notebooks/{10,20,30,50}_*.ipynb`

Scoping / history:
- `cosmos-bc-dss/docs/COSMoS_Step2_Scoping_Brief.md` — original brief
  that motivated the rework, frozen pre-build.
- `cosmos-bc-dss/docs/COSMoS_Behavioural_Analysis.md`
- `cosmos-bc-dss/docs/COSMoS_Collection_vs_Ontology.md`
- `cosmos-bc-dss/docs/COSMoS_Instrument_Layer.md`

Case pair references (still the working examples):
- `docs/Glucose_COSMoS_Story.html`, `docs/Glucose_StudyIntent_Story.html`
- `docs/6MWT_COSMoS_Story.html`, `docs/6MWT_NCIt_Story.html`
- `outputs/XRay_COSMoS_Story.html`, `outputs/XRay_PatientBurden_Story.html`

---

*Brief drafted 2026-04-22 after Step 2 merged to main. Supersedes
`COSMoS_Step2_Scoping_Brief.md` for the purpose of opening the next
conversation; that file is retained as the frozen pre-build record.*
