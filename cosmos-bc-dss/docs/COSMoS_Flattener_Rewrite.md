# COSMoS Flattener Rewrite — Step 2 Design

*Step 2 of the cosmos-bc-dss rework. Decision record, not a full specification. Inputs: [COSMoS_Graph_As_Authored.md](COSMoS_Graph_As_Authored.md), [COSMoS_Flattener_Enhancement_Brief.md](COSMoS_Flattener_Enhancement_Brief.md).*

*cdisc-for-ai, April 2026*

> **Status (2026-04-22).** Build complete. Two planned items changed during
> implementation and are explicit in §2, §3, §5, §7 below: the `Identity`
> back-compat sheet was abandoned in favour of consumer-track rewiring, and
> three additional notebooks (20, 30, 50) were added beyond the original
> deliverable list. See [reports/flattener_rewrite_audit.md](../reports/flattener_rewrite_audit.md)
> for the full close-out, sheet shapes, and validation triage.

---

## 1. Decision

The flattener becomes SchemaView-driven over the existing CDISC Excel export and produces a multi-sheet interim. One pipeline, one artifact, multiple grains. This is "Option B" from the Step 1 close-out.

The input stays on `downloads/cdisc_sdtm_dataset_specializations_latest.xlsx` (plus `cdisc_biomedical_concepts_latest.xlsx` for BC identity). The xlsx is graph-equivalent to the YAML at VLM-row grain (Step 1 audit, 2026-04-22). Switching to the GitHub YAML folder is blocked on upstream coverage (5 of 32 domains published at 2026-Q1); switching to the CDISC Library API is blocked on endpoint verification. Neither blocker matters if the xlsx is the input.

## 2. Sheet inventory

**Planned (one file, 5 sheets including `Identity`).** Revised during build: output split across two files and the `Identity` back-compat sheet dropped (see §3). What was built, as of the 2026-04-22 run:

`interim/COSMoS_Graph.xlsx`

| Sheet | Grain | Rows (2026-Q1) | Purpose |
|---|---|---|---|
| `ReadMe` | — | 22 | Provenance, column dictionary links. |
| `DSS` | one per DSS | 1,326 | DSS-level identity. 8 columns — `ds_id`, `bc_id`, `domain`, `source`, `ds_short_name`, `sdtmig_start_version`, `sdtmig_end_version`, `package_date`. Not a back-compat projection of `BC_DSS` — see §3. |
| `Variables` | one per SDTMVariable | 12,677 | VLM-row grain. 26 columns — the LinkML slots on `SDTMVariable` plus the inlined reification quad (subject, linking_phrase, predicate_term, object). |
| `Relationships` | one per reified edge | 12,364 | Long-format. 6 columns — `ds_id`, `variable_name`, `subject`, `linking_phrase`, `predicate_term`, `object`. Rows where the source has no quad are omitted (313 rows in the 2026-Q1 build). |
| `Codelists` | one per binding | 291 | Deduped `(codelist_concept_id, codelist_submission_value)` pairs referenced by any variable, with `variable_uses_count`. |
| `BC` | one per BC | 1,345 | BC-level identity, classification, and hierarchy. Added during build — BC identity needs to ride with the graph for the cookbook and consumer tracks, not re-join from `downloads/` on every query. |

`interim/COSMoS_Graph_CT.xlsx` (added during build — NCI CT enrichment lifted out of the flattener so `COSMoS_Graph.xlsx` stays lossless-over-source):

| Sheet | Grain | Rows (2026-Q1) | Purpose |
|---|---|---|---|
| `ReadMe` | — | 32 | Provenance, CT package version. |
| `Codelists` | one per bound codelist | 291 | Enriched with `codelist_name`, `codelist_extensible`, NCI preferred term. |
| `CodelistTerms` | one per (codelist, term) pair | 17,523 | Permissible values expanded from SDTM CT. |
| `AssignedTerms` | one per unique assigned-term concept | 1,170 | NCI definition + preferred term for each pinned concept. |
| `Unresolved` | — | 6 | Concept IDs not found in SDTM CT 2026-03-27. |
| `Anomalies` | — | 1 | Pinned-term-not-in-bound-codelist cases. |

## 3. Back-compat — decision revised during build

**Planned.** An `Identity` sheet mirroring the 36 columns of today's
`BC_DSS` sheet, so consumer tracks could switch files with no code change.

**Built.** No `Identity` sheet. Consumer tracks will be rewired to read
the new multi-sheet graph instead.

Reason. The legacy `BC_DSS` sheet conflates three grains (BC, DSS, and
flattened-collection rows, distinguished by `Row_Type`) into one table
shape. The rewrite already separates those grains into `BC`, `DSS`, and
`Variables`. Reproducing the conflated shape on top of the separated
grains means re-collapsing them, which defeats the purpose. Consumer
tracks that filter on `Row_Type` today can instead pick the right sheet.

Consequence. Consumer tracks are not back-compatible across this branch
without rewiring. Tracked as a follow-up task outside this branch. The
legacy `interim/COSMoS_BC_DSS.xlsx` is left in place until the rewiring
lands, so consumer tracks can continue to read it in the interim.

## 4. Architecture

The driver is `linkml_runtime.SchemaView` over `cosmos_sdtm_model.yaml` (and `cosmos_bc_model.yaml` for the BC side). The schema defines:

- The slot list on `SDTMVariable` — becomes the `Variables` column list.
- The slot list on `SDTMGroup` (ex-variables) — becomes the DSS-level columns on `DSS`.
- The `RelationShip` class — becomes the `Relationships` sheet's column schema.
- The NCIt-anchored enumerations (`OriginTypeEnum`, `OriginSourceEnum`, `RoleEnum`, `ComparatorEnum`) — used to validate values on the fly and surface their `meaning:` NCIT anchors in the `ReadMe`.

The xlsx-to-slot bridge is the rename table in `COSMoS_Graph_As_Authored.md §7.1`. Either hardcoded in the flattener module, or regenerated at build time from SchemaView by matching slot `name` against normalised column names. The rename table is small (32 entries) and stable across releases — hardcoding is fine.

The flatten step reads the VLM-sheet into a pandas DataFrame, applies the rename bridge to get LinkML slot names as column headers, then projects to the five data sheets (`DSS`, `Variables`, `Relationships`, `Codelists`, `BC`) using SchemaView's class/slot metadata. No hand-written column list anywhere.

## 5. Open decisions — resolved during build

**DEC materialisation.** Resolved to **Option (a)** as recommended, with
a caveat: `dec_id` rides on `Variables` as a scalar, but the DEC label
and NCIt code are deferred to Step 3 (not looked up by the flattener).
No separate `DECs` sheet.

**subsetCodelist serialisation.** Resolved to **Option (a)**:
pass-through as string, via `Variables.subset_codelist`. Structured
parsing deferred until a case study needs it.

**Anomaly policy.** Resolved: flag, don't silently fix. The approach is
slightly revised from the original plan — anomalies land in three places
rather than one consolidated `data_issues` sheet:

- `COSMoS_Graph_CT.xlsx/Unresolved` — CT concept IDs not in the package.
- `COSMoS_Graph_CT.xlsx/Anomalies` — pinned-term-not-in-bound-codelist cases.
- `reports/graph_validation_report.md` + `.json` — full enumeration of
  the eight validation checks, with per-check counts and details.

Triage of the FAIL items is in
[reports/flattener_rewrite_audit.md §5](../reports/flattener_rewrite_audit.md#5-validation-triage).

## 6. Non-goals for Step 2

- CRF Specializations. No released COSMoS package carries CRF YAML; the 2026-Q1 release has CRF only in `yaml/20251231_draft/`. Deferred until a released package includes it. The flattener is BC + SDTM only at Step 2.
- NCIt enrichment beyond what the source xlsx already carries. `codelist.conceptId`, `assignedTerm.conceptId`, `originType`/`originSource` NCIt anchors are surfaced as-is (IDs passed through). Resolving these to definitions, synonyms, UMLS/LOINC mappings is Step 3.
- Narrative generation. The reification-as-legibility pattern (linking phrase + predicate term) is surfaced in the `Relationships` sheet. Rendering it into DataBook prose is Step 3.
- Sheet-level diffs against the previous release. Release-note generation stays on the existing workflow; this note does not change it.

## 7. Deliverables — as built

Revised from the original two-notebook plan. Output path also changed:
new file `interim/COSMoS_Graph.xlsx` alongside the legacy
`interim/COSMoS_BC_DSS.xlsx`, not in place of it.

- `cosmos-bc-dss/notebooks/10_flatten_schema_driven.ipynb` — flattener.
  Inputs from `downloads/`, outputs `interim/COSMoS_Graph.xlsx`.
- `cosmos-bc-dss/notebooks/20_resolve_ct.ipynb` — **added.** Joins
  codelist and assigned-term concept IDs against NCI EVS SDTM CT
  2026-03-27. Outputs `interim/COSMoS_Graph_CT.xlsx`.
- `cosmos-bc-dss/notebooks/30_validate_graph.ipynb` — **added.**
  Enumeration, referential integrity, schema column coverage,
  CT-resolution FAILs, and anomaly counts. Outputs
  `reports/graph_validation_report.md` / `.json`.
- `cosmos-bc-dss/notebooks/50_query_examples.ipynb` — **added.** Query
  cookbook, eight queries pinned to the story-pair DSSs (GLUCPL,
  SIXMW101, SGBESCR). Proves the graph shape answers the narrative
  questions. No sheet output.
- `cosmos-bc-dss/reports/flattener_rewrite_audit.md` — close-out
  narrative: sheet shapes, build counts, back-compat decision,
  validation triage.

The planned `11_backcompat_diff.ipynb` was not created — no `Identity`
sheet to diff against. Consumer-track rewiring is follow-up work,
outside this branch's scope.
