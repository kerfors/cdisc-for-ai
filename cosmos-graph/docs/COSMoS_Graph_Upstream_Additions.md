# COSMoS Graph — Upstream Additions

*Design record for a second wave of cosmos-bc-dss work, scoped from findings that surfaced while building the sdtm-narrative layer (Step 3 of that track). Successor to [COSMoS_Flattener_Rewrite.md](COSMoS_Flattener_Rewrite.md) in the same series: what the flattener should carry that it does not carry today.*

*cdisc-for-ai, 2026-04-23*

> **Status (2026-04-23).** Scoping closed. The findings below emerged
> from sdtm-narrative 3b (template catalogue authoring) and 3d (DataBook
> assembly) and motivated the original §3 proposals. A read-only triage
> pass (§6) has since tested each proposal against actual upstream and
> downstream state and re-classified them. Execution for this branch
> follows the revised plan in §6.3, not the original sequencing in §7.

---

## 1. Context

The sdtm-narrative track produces per-DSS paragraphs (Tier 2b) and per-case DataBooks (Tier 3) by reading `interim/COSMoS_Graph.xlsx` and composing prose through a template catalogue. Authoring the catalogue against six reference HTML stories (Glucose, 6MWT, X-Ray, plus three case-specialisation overlays) forced a comparison between *what the stories say the graph carries* and *what the graph actually carries at 2026-Q1*.

Five deltas emerged. Four of them are not narrative-layer concerns — they are things the graph should carry, so that every consumer (narrative assembler, LLM, downstream analytics, future tools) reads the same projection rather than each re-deriving it.

This document records those findings and proposes the minimal set of graph-layer additions to close them. It also introduces one new architectural element: a core-vs-overlay split in the graph, needed to carry content that is not standards-level.

Paired reading: [sdtm-narrative/docs/COSMoS_Narrative_Layer.md](../../sdtm-narrative/docs/COSMoS_Narrative_Layer.md) — the narrative-layer design record that surfaced these findings.

## 2. Findings

### 2.1 DSS attributes are a projection, not source content

The template catalogue for specimen-based Findings (`sdtm-narrative/reference/templates/01_specimen_based_findings.md`) reads "DSS attributes" — Specimen, Method, Result_Scale, Standard_Unit, Allowed_Units, LOINC_Code, Decimal_Places — as if they were columns on the `DSS` sheet. They are not. Confirmed against raw YAML source (`cosmos-bc-dss/downloads/cosmos_yaml/20260331_r16/sdtm/LBGLUC.yaml` and peers), the top-level DSS keys in the source are:

```
packageDate, packageType, datasetSpecializationId, domain,
shortName, source, sdtmigStartVersion, sdtmigEndVersion,
biomedicalConceptId, variables
```

The so-called attributes live inside the `variables` array:

- Specimen → `variables[--SPEC].assignedTerm`
- Method → `variables[--METHOD].assignedTerm`
- Units → `variables[--ORRESU, --STRESU].valueList` or `.assignedTerm`
- LOINC → `variables[--LOINC].assignedTerm`
- Decimal places → `variables[--STRESN].significantDigits` / `.format`
- Result_Scale → not represented in source; it is our inferred classification

So the narrative assembler is computing a projection over `Variables` rows at read time. Every consumer who wants to answer "what specimen is this DSS bound to?" has to re-derive the same projection.

The projection itself is non-trivial: it reads multiple variable rows, filters by role (`Qualifier`) and pinning status, and interprets `significantDigits` / `format` / `valueList` cardinality. It also requires structural-type awareness — specimen-based Findings has a three-axis projection (specimen / method / scale); instrument-based Findings has a different projection (instrument composition / topic within instrument); measurement Findings differs again. No single universal projection exists.

**Implication.** A derived view belongs in the graph. See §3.1.

### 2.2 Root-subset fallback coverage is unproven

The natural-English substitution rule (per `templates/00_index.md`) is two-tier: direct hit against `SDTM_Variable_Identity.xlsx`, compositional fallback for domain-instantiated forms (strip the two-character prefix, look up the `--REMAINDER` in the Root subset of NCI EVS Variable Terminology). Coverage in theory: 100%. Coverage in practice against the 2026-Q1 graph (from Tier 2b assembly, 1,326 DSSs):

- 575 DSSs carry `has_unresolved = True`.
- 103 distinct variable codes do not resolve, including codes that should (`RSSTRESN`, `MKTESTCD`, `MKTEST`, `MKORRES`, `MKSTRESC`) against canonical roots (`--STRESN`, `--TESTCD`, `--TEST`, `--ORRES`, `--STRESC`). *Triage outcome (see §6.1 §3.5): the four `MK*` codes are narrative-layer bug, not upstream; `RSSTRESN` is a genuine Root-subset gap.*

Two possible causes, pointing different directions:

- *Narrative-layer bug.* The fallback lookup is not running, or the Root-subset matching is off. In that case the fix is in sdtm-narrative, not here.
- *NCI EVS Root-subset gap.* Some codes genuinely have no `--` representation. Candidates: `ISBDAGNT` (IS domain, 290 DSSs — is `--AGNT` a canonical root?), the GF* family (Genomic Findings), the FT* family. These are candidates for a CDISC/EVS content ask.

A diagnostic pass before execution starts is the entry point. One resolved case (e.g. `RSSTRESN`) tells us whether the remainder is an upstream ask at all.

**Implication.** Pass-one check in the next session. The outcome shapes whether this item survives as an upstream concern or collapses into a narrative-layer fix. See §3.5.

### 2.3 Reference stories carry content the graph lacks

Two of the six HTML reference stories describe BCs that the graph does not fully support at 2026-Q1:

- **6MWT.** BC exists with `bc_type = full_no_ds`. Zero DSS rows. The reference story (`sdtm-narrative/docs/6MWT_COSMoS_Story.html`) describes the questionnaire at QS-domain item grain. *Triage outcome (see §6.1 §3.2): the C-code ancestry for the instrument and its items is already materialised in `sdtm-test-codes/machine_actionable/`; what is genuinely missing is DSS rows under the BC.*
- **X-Ray.** BC exists; two PR-domain DSSs present; zero MK-domain DSSs. The reference story (`sdtm-narrative/docs/XRay_COSMoS_Story.html`) describes both the procedure (PR) and the morphology reading (MK) side. The MK side is extrapolation.

The extrapolations are authored content, grounded in SDTMIG modelling, not fabrication. But they are not CDISC-standards-level content. The architectural question is: where does authored-but-not-standards content live?

Three options were considered: (a) upstream fix through CDISC issue tracking, long cycle; (b) a graph-layer overlay carrying sponsor- or track-authored proposed DSSs, schema-identical to the core `DSS` sheet, clearly separated by provenance; (c) overlay stays in HTML stories only, never promoted to machine-actionable. Option (b) is the selected direction — (a) remains correct in parallel and is orthogonal, (c) leaves the narrative layer permanently unable to produce machine-actionable output for any authored-but-not-standards content.

**Implication.** A core-vs-overlay architecture. See §4 and §3.6.

### 2.4 Case specialisations have no registry home

The `Glucose_StudyIntent` and `XRay_PatientBurden` reference stories introduce six case specialisations (`ID001` / `ID002` / `ID003` for Glucose; `ID101` / `ID102` / `ID103` for X-Ray). These are overlays on parent DSSs — they refine a DSS with additional pinning, slot narrowing, or study-intent rationale, without introducing a new DSS row.

The case registry does not exist in the graph. It does not exist anywhere else machine-actionable. Template 04 in the narrative catalogue is authored against the HTML stories directly, and the six case IDs are hard-coded in notebook 60 (`sdtm-narrative/notebooks/60_assemble_databooks.ipynb`). That is expedient for Step 3 output but is not a durable home.

The six cases split cleanly by scope:

- Glucose FPG / 2hPG / random — **clinically universal.** Applies wherever glucose is measured. Not sponsor-specific.
- X-Ray patient-burden rationale — **arguably protocol-scoped.** Depends on study design trade-offs.

So the registry is not one thing. It is at least two: a CDISC-scope set (graph-native) and a sponsor-scope set (overlay). Same schema; same shape; different provenance.

**Implication.** Same core-vs-overlay architecture as §2.3. Two `Case_Specialisations` sheets — one core, one overlay. See §3.4 and §4.

### 2.5 The four "registry gaps" are not four registries

The narrative catalogue surfaces four registry-need arguments across Templates 01-04:

1. Specimen-test qualification (Template 01)
2. Instrument composition (Template 02)
3. Cross-domain composition (Template 03)
4. Case specialisations (Template 04)

Reframed against the graph:

- **(1) Specimen-test qualification** is *not* a new registry. It is an enrichment of existing `DSS` rows (a flag or derivation identifying clinically-meaningful test × specimen × method × scale combinations). Most of this content already exists in the `Variables` sheet as pinned qualifier rows; the missing element is a first-class boolean or a named-pattern column. Covered by §3.1 (DSS_Attributes), possibly with an additional qualifying column.
- **(2) Instrument composition** was proposed as a new content sheet. *Triage outcome (see §6.1 §3.2): already materialised in `sdtm-test-codes/machine_actionable/`. The reason it felt missing to the narrative assembler is a consumer-side column-name typo, not an upstream gap.*
- **(3) Cross-domain composition** is *not* a registry — it is a derived view. `GROUP BY bc_id, HAVING COUNT(DISTINCT domain_class) > 1`. No new content; a flag column or a view. See §3.3.
- **(4) Case specialisations** — two sheets per §2.4 and §3.4.

Net: four gaps resolve to three graph additions (§3.1, §3.2, §3.3) plus one overlay-pattern pair (§3.4).

## 3. Proposed upstream additions

Target file is `interim/COSMoS_Graph.xlsx` unless noted. All additions produced by an extension of the flattener driver (SchemaView-based, per `COSMoS_Flattener_Rewrite.md §4`), not hand-assembled.

### 3.1 `DSS_Attributes` — derived sheet

**Grain.** Long-format: one row per (DSS, attribute, value).

**Columns.**

```
ds_id, attribute_name, attribute_value, source_variable,
source_role, source_origin, structural_type_context
```

**Derivation.** For each DSS, read its `Variables` rows; for each row that matches a known attribute pattern (specimen = pinned `--SPEC`, method = pinned `--METHOD`, units = pinned/enumerated `--ORRESU` and `--STRESU`, LOINC = pinned `--LOINC`, decimal_places = `significantDigits` on `--STRESN`), emit one row of the output.

**Why long-format.** Honest about provenance — the `source_variable` column makes clear which variable the attribute was projected from. Wide-format is ergonomic for humans but implicit about derivation. A wide-format view can be built on top for read ergonomics; canonical form stays long.

**Why structural-type-context column.** Different structural types project different attribute sets. Specimen-based Findings has specimen/method/scale; instrument-based Findings has topic-within-instrument; etc. Rather than emit sparse columns, carry the structural-type label so consumers can filter.

**Size estimate.** ~5 attributes × 1,326 DSSs = ~6,600 rows upper bound; likely less because not every DSS pins every attribute.

**Open: Result_Scale.** Not in source YAML. If retained in the output, it is a narrative-track-inferred classification, not a flattener-native derivation. Options: drop (honest), keep and label `source_origin = inferred-by-classification` (practical), or defer to a separate enrichment pass after the flattener. Deferred to execution-session discussion.

### 3.2 `Instrument_Composition` — new content sheet

**Grain.** One row per (parent_instrument, child, relationship_type).

**Columns.**

```
parent_ncit_code, parent_label, child_ncit_code, child_label,
relationship_type, relationship_source, depth_from_parent
```

**Content.** Instrument-as-container → sub-instrument → item hierarchy for QS, FT, RS domains. Source: NCIt C20993 (Questionnaire) descendants traversed via the CDISC instrument codelist (C211913) and NCIt parent relations.

**Scope.** Covers all instrument codelists referenced in the graph via `variables.codelist_concept_id`. Expect ~50-200 instrument codelists × average ~30 items = 1,500-6,000 rows.

**Why materialised.** The 6MWT DataBook (from sdtm-narrative/machine_actionable/databooks/6mwt.md) hand-assembles this ancestry from NCIt. Every instrument story would repeat the same traversal. Materialise once in the graph.

**Sourcing.** Pulls from the same NCI EVS 2026-03-27 package the CT enrichment uses (`notebooks/20_resolve_ct.ipynb`). Could live in `COSMoS_Graph_CT.xlsx` rather than `COSMoS_Graph.xlsx` since it is NCIt-sourced enrichment, not flattened-from-source content. Target file decision deferred to execution.

### 3.3 BC sheet enrichment — cross-domain flags

**Grain.** Additional columns on the existing `BC` sheet. No new sheet.

**New columns.**

```
distinct_domain_classes,  -- integer count
is_cross_domain_class,    -- boolean, True where count > 1
domain_class_list         -- comma-separated, e.g. "Findings,Interventions"
```

**Derivation.** `BC → DSSs → distinct(Domain_Class)` per BC. Joined in the flattener, not re-derived per query.

**Why.** Template 03 in the narrative catalogue asks "is this BC cross-domain?" on every DSS render. Today the answer is a grouped query; materialising it as a flag makes it a column read.

**Complementary view.** A `Cross_Domain_BCs` sheet could enumerate only the cross-domain subset, as a convenience. Probably unnecessary — filtering `BC` on `is_cross_domain_class = True` gives the same result. Decision deferred.

### 3.4 `Case_Specialisations` — new sheet (CDISC-scope)

**Grain.** One row per case specialisation.

**Columns.**

```
case_spec_id, parent_ds_id, case_type, case_label,
case_description, composes_with, rationale, ext_ref, scope
```

**`scope` column.** Values: `core` (CDISC-authored), `sponsor` (sponsor-local overlay). In the core sheet, all rows have `scope = core`. See §4 for how `sponsor` rows reach the graph.

**Content at first cut.** Three Glucose StudyIntent rows (`ID001`, `ID002`, `ID003`) per the `Glucose_StudyIntent_Story.html` as the seed set. The three X-Ray PatientBurden rows (`ID101`-`ID103`) are candidates but may be sponsor-scope rather than core — see §2.4. Classification of the six seed cases deferred to execution-session.

**Companion sheet.** `Case_Specialisation_Pinning` — one row per (case_spec_id, variable_name, assigned_term) for cases that layer additional variable pinning on top of the parent DSS. Same grain as `Variables` but filtered to the case-refinement layer.

**Size estimate.** Tiny at first — six rows and maybe 15 pinning rows for the seed. Grows as more case-scope knowledge is captured.

### 3.5 Root-subset fallback diagnostic

**Not a sheet addition — a diagnostic pass.**

Before any other item executes, confirm whether the 103 unresolved codes from §2.2 are narrative-layer (fallback code is wrong) or upstream (NCI EVS Root subset is incomplete). One worked case resolves the direction:

- Take `RSSTRESN`. Strip `RS` → `--STRESN`. Look up `--STRESN` in `SDTM_Variable_Identity.xlsx` with `Subset = Root`.
- If found — narrative-layer bug. Fix in the assembler; no upstream ask.
- If not found — check NCI EVS Variable Terminology Root subset directly. If truly absent there, it is a CDISC/EVS content ask.

The diagnostic costs nothing and keeps this document from carrying a speculative upstream concern.

### 3.6 Overlay file — new companion

**Purpose.** Carry authored content that is schema-identical to core graph sheets but is not CDISC-standards-level: the 6MWT questionnaire items (§2.3), the X-Ray MK-side DSSs (§2.3), sponsor-scope case specialisations (§2.4).

**Target file.** `interim/COSMoS_Graph_Overlay.xlsx` — parallel to `COSMoS_Graph.xlsx`, not merged. Same sheet names (`DSS`, `Variables`, `Case_Specialisations`) on the sheets that the overlay populates.

**Why parallel file.** Core graph stays CDISC-authored and lossless-over-source (per `COSMoS_Flattener_Rewrite.md §4` principle). Overlay is provenance-separated at the file level — a consumer can choose core-only, core+overlay, or overlay-only depending on use case.

**Provenance column.** Every overlay row carries `source = 'overlay'` and `overlay_reason` (e.g. `proposed-dss-cdisc-ask`, `sponsor-local-case`, `track-authored-extrapolation`). Ingestion of the overlay into any consumer is explicit, not accidental.

**Schema synchronisation.** Overlay schema follows the core schema. If core `DSS` adds a column, overlay `DSS` adds the same column. Enforced at build time by reusing the same SchemaView.

See §4 for the architectural frame.

## 4. Core vs. overlay — architectural element

A new pattern in the graph layer.

**Core (`COSMoS_Graph.xlsx`).** Lossless projection of CDISC-authored content. Input: `cosmos-bc-dss/downloads/cdisc_*.xlsx` + CDISC YAML. Every row provenance-traceable to a CDISC artefact. No interpretation, no extrapolation, no sponsor content.

**Overlay (`COSMoS_Graph_Overlay.xlsx`).** Content authored in this repo (track-authored extrapolations like the 6MWT items) or by a sponsor deployment (sponsor-scope cases). Schema-identical to core. Provenance-labelled at row level.

**Consumer contract.** Every consumer declares which slice it reads:

- Core-only — the narrative layer at this stage, until overlay is introduced.
- Core + overlay — consumers that want the richest available content, trading provenance uniformity for coverage (e.g. the Tier 3 DataBook for 6MWT, which otherwise produces a gap-argument page).
- Overlay-only — validation and diff tools that want to see only what is authored in this repo, separate from CDISC content.

**Why parallel files, not one file with a scope column.** Read-time filter works either way. But a single-file design makes it easier to accidentally ingest overlay content as if it were CDISC-authored, and harder to diff what changed in overlay-only vs. core-only. Parallel-file design makes the boundary enforceable by file path.

**Alignment with existing practice.** The cosmos-graph track already follows this pattern with `COSMoS_Graph.xlsx` (core) vs. `COSMoS_Graph_CT.xlsx` (NCI EVS enrichment layered on top, separate file). Overlay is a third file following the same split logic.

## 5. Non-goals for this wave

- No change to the flattener's source-side contract. Inputs stay on the `cosmos-bc-dss/downloads/cdisc_*.xlsx` files.
- No change to the LinkML schema. The new sheets (`DSS_Attributes`, `Instrument_Composition`, `Case_Specialisations`) are derivations over existing classes, not new classes in the schema.
- No back-compat requirement with legacy `interim/COSMoS_BC_DSS.xlsx`. That file stays as-is until consumer tracks fully migrate to `COSMoS_Graph.xlsx`.
- No SDRG integration, no sponsor-onboarding tooling. If the overlay file is produced (see §6.3), mechanisms for sponsors to contribute overlay content are out of scope.
- No case-specialisation narrative format. Template 04 stays in sdtm-narrative. This document adds the data layer it reads.

## 6. Triage outcome (2026-04-23)

Executed as a read-only pass after §3.5 landed. For each §3 item, the triage asks two questions: (a) does the finding hold up against actual upstream and downstream state, and (b) if it does, is the proposed cosmos-graph addition the right response, or is the work better located in a consumer track or in upstream CDISC. The evidence is captured per-item; the revised execution plan for this branch is in §6.3.

### 6.1 Per-item verdict

**§3.1 `DSS_Attributes` — deferred (pre-investment).** The `dss_attributes()` helper in `sdtm-narrative/notebooks/60_assemble_databooks.ipynb` cell 8 is a 20-line loop over a fixed suffix list (`SPEC, METHOD, CAT, SCAT, ORRESU, STRESU, LOINC, FAST, POS, LOC, DECOD`). No structural-type branching in the actual code — the "structural_type_context column" in §3.1 is a forward-looking hedge, not reflected in current consumer logic. One consumer uses the projection today. Materialising a new long-format sheet adds storage and a new schema surface for a projection that fits in twenty lines. Revisit when a second consumer appears.

**§3.2 `Instrument_Composition` — not needed in cosmos-graph (consumer-side fix).** The payload §3.2 describes — instrument → item ancestry with NCIt C-codes — is already materialised in `sdtm-test-codes/machine_actionable/`. `SDTM_Instrument_Identity.xlsx` carries SIXMW1TC with `Instrument_NCIt_Code = C115789`; `SDTM_Instrument_Test_Identity.xlsx` carries its six SIXMW101–106 items with C-codes C115800–C115805. The 10,311 rows across 359 instrument codelists cover the full scope §3.2 estimated. The reason this did not feel available to the narrative layer is a column-name typo in `60_assemble_databooks.ipynb` cell 16 (`NCIt_Instrument_Code` vs actual `Instrument_NCIt_Code`). Fix belongs in sdtm-narrative on a separate branch, not here.

**§3.3 BC cross-domain flags — contingent on §3.6.** Of the 903 BCs with at least one DSS row in `cosmos-graph/interim/COSMoS_Graph.xlsx` (1,345 total; 442 have `bc_type = full_no_ds` and are structurally incapable of cross-class), zero are cross-Observation_Class at 2026-Q1. The proposed `is_cross_domain_class` column would be uniformly `False`. Template 03 in the narrative catalogue has no standards-scope data to render against. The flag becomes meaningful only if authored content (e.g. an X-Ray MK-side DSS via §3.6 overlay) introduces a cross-class pairing. Defer until §3.6 decides.

**§3.4 `Case_Specialisations` — downstream concern, not upstream.** Six cases hard-coded in `60_assemble_databooks.ipynb` cell 10 with HTML-story provenance. They belong in a proper registry — but the registry is narrative-layer authored interpretation, not CDISC COSMoS source content. Putting them in the core graph would stretch §4's lossless-over-source contract. Registry upgrade stays in sdtm-narrative on a separate branch. Cosmos-graph owns no §3.4 work.

**§3.5 Root-subset fallback diagnostic — closed.** Output at `cosmos-graph/reports/root_subset_fallback_diagnostic.{md,csv}` and diagnostic script at `cosmos-graph/scripts/root_subset_fallback_diagnostic.py`. Result: 66 of 103 unresolved codes (1,245 DSS-rows) collapse into a one-line `var_nn` fix in `sdtm-narrative` (strip the two-char prefix; do not prepend `--`); 37 codes (806 DSS-rows) are genuine EVS Root-subset gaps, dominated by GF* family, `STRESN` across domains, and `ISBDAGNT`. No cosmos-graph action. Narrative-layer fix and CDISC/EVS content ask both tracked outside this branch.

**§3.6 Overlay file — decision-pending, payload smaller than §3.6 implied.** The overlay's claimed payload was (a) 6MWT questionnaire items, (b) X-Ray MK-side DSSs, (c) sponsor-scope cases. Breakdown:

- *6MWT items.* The C-code ancestry (parent instrument C115789 + six items) is already in `sdtm-test-codes/` — not overlay-shaped content, it is upstream content the consumer is not reading. What is overlay-shaped is authoring DSS rows under the 6MWT BC, which has `bc_type = full_no_ds` in `COSMoS_Graph.xlsx`. That is a separate, much smaller payload than "the 6MWT track-authored items" implies.
- *X-Ray MK-side.* Confirmed absent: `COSMoS_Graph.xlsx` BC sheet has bc_id `C38101` ("X-Ray Imaging") with two DSSs — `XRAY` and `XRAYCHEST`, both PR-domain. No MK-domain coverage. If authored, these are the cleanest candidates for overlay — genuinely net-new and unambiguously track-authored extrapolation.
- *Sponsor-scope cases.* Tied to §3.4 outcome (X-Ray pinning vocabularies).

The overlay *architecture* (§4 pattern) is sound and is the right place for (b) and (c) if authored. But building the file as a skeleton in this branch is only worth doing if at least one row is authored. Otherwise the skeleton sits empty and the architectural decision stays on paper. Recommendation: with §3.4 moved downstream, the overlay file has no payload in this session. Overlay stays as a documented architectural pattern for the two remaining candidates (6MWT DSSs under `full_no_ds`, X-Ray MK-side DSSs), both of which are out of scope for this branch.

### 6.2 Cross-cutting observation

Three of the six original items (§3.1, §3.2, §3.3) are not content the graph is missing — they are projections or fixes that belong in a consumer track or in a follow-up after overlay content exists. The triage narrows the upstream work for this branch to the items where cosmos-graph genuinely owns the content: §3.4 and §3.6.

### 6.3 Revised execution plan (this branch)

1. **§3.5.** Closed. No further work.
2. **§3.4, §3.6.** Reclassified as out of scope for cosmos-graph. Case specialisations are narrative-layer authored interpretation, not COSMoS source projection — they stay in sdtm-narrative. With §3.4 moved downstream, §3.6 overlay has no payload in this session and stays a documented pattern.
3. **§3.1, §3.2, §3.3.** Not executed in this branch. §3.2 migrates to a sdtm-narrative-side column-name fix. §3.3 waits on §3.6 outcome. §3.1 waits on a second consumer.
4. **Net deliverable for this branch:** §3.5 diagnostic + triage documentation. That is all.

Narrative-track follow-ups (separate branches off main, not this one):

- `var_nn` two-char strip fix in `sdtm-narrative/notebooks/40_assemble_narrative.ipynb` cell 4 and `60_assemble_databooks.ipynb` cell 4.
- `Instrument_NCIt_Code` typo fix in `60_assemble_databooks.ipynb` cell 16, with rewire to read `sdtm-test-codes/machine_actionable/SDTM_Instrument_Identity.xlsx` + `SDTM_Instrument_Test_Identity.xlsx`.

## 7. Original sequencing (pre-triage)

Superseded by §6.3. Kept for the record.

1. **§3.5 diagnostic first.** Cheap. Collapses or confirms §3.5 and possibly narrows §2.2 before anything else runs.
2. **§3.3 BC enrichment.** Smallest change. Pure addition to an existing sheet. Unblocks Template 03 reads.
3. **§3.1 `DSS_Attributes`.** Largest derivation logic but no new content sourcing. Unblocks Template 01 and Template 02 reads at grain.
4. **§3.4 `Case_Specialisations` core sheet.** Small content payload, six rows. Source: HTML stories, manual authoring this time.
5. **§3.6 overlay file skeleton.** Before §3.4 proper if X-Ray cases classify as sponsor-scope, otherwise after. Carries the 6MWT track-authored items.
6. **§3.2 `Instrument_Composition`.** Largest content sourcing (NCIt traversal). Arguably belongs in `COSMoS_Graph_CT.xlsx` — deferred to execution.

## 8. Cross-references

- [COSMoS_Flattener_Rewrite.md](COSMoS_Flattener_Rewrite.md) — Step 2 design record. This document is the natural successor.
- [COSMoS_Graph_As_Authored.md](COSMoS_Graph_As_Authored.md) — source-side schema reference.
- [sdtm-narrative/docs/COSMoS_Narrative_Layer.md](../../sdtm-narrative/docs/COSMoS_Narrative_Layer.md) — narrative-layer design record. Findings in §2 of this document map directly to concerns raised there.
- [sdtm-narrative/reference/templates/](../../sdtm-narrative/reference/templates/) — template catalogue whose authoring surfaced the findings.
