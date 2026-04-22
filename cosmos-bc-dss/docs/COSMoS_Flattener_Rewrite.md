# COSMoS Flattener Rewrite — Step 2 Design

*Step 2 of the cosmos-bc-dss rework. Decision record, not a full specification. Inputs: [COSMoS_Graph_As_Authored.md](COSMoS_Graph_As_Authored.md), [COSMoS_Flattener_Enhancement_Brief.md](COSMoS_Flattener_Enhancement_Brief.md).*

*cdisc-for-ai, April 2026*

---

## 1. Decision

The flattener becomes SchemaView-driven over the existing CDISC Excel export and produces a multi-sheet interim. One pipeline, one artifact, multiple grains. This is "Option B" from the Step 1 close-out.

The input stays on `downloads/cdisc_sdtm_dataset_specializations_latest.xlsx` (plus `cdisc_biomedical_concepts_latest.xlsx` for BC identity). The xlsx is graph-equivalent to the YAML at VLM-row grain (Step 1 audit, 2026-04-22). Switching to the GitHub YAML folder is blocked on upstream coverage (5 of 32 domains published at 2026-Q1); switching to the CDISC Library API is blocked on endpoint verification. Neither blocker matters if the xlsx is the input.

## 2. Sheet inventory

| Sheet | Grain | Rows (2026-Q1) | Purpose |
|---|---|---|---|
| `ReadMe` | — | ~20 | Provenance, audit date, column dictionary links |
| `Identity` | one per DSS | 1,326 | Back-compat projection. Column set = today's 36 columns on `interim/COSMoS_BC_DSS.xlsx/BC_DSS`. Consumer tracks read this and nothing else. |
| `Variables` | one per SDTMVariable | 12,677 | VLM-row grain. Columns = LinkML slots on `SDTMVariable` (name, role, dataType, length, significantDigits, assignedTerm, codelist, subsetCodelist, valueList, mandatoryVariable, mandatoryValue, comparator, originType, originSource, vlmTarget, dataElementConceptId, isNonStandard). One row per variable-within-DSS. |
| `Relationships` | one per reified edge | ~12,364 | Long-format. Columns: `dss_id`, `variable_name`, `subject`, `linking_phrase`, `predicate_term`, `object`. Rows where the xlsx has no quad are omitted (313 rows in the 2026-Q1 audit). |
| `Codelists` | one per unique binding | TBD | Deduped list of (`codelist_concept_id`, `codelist_submission_value`) pairs actually referenced by any variable. NCIt-anchored codelist identity surfaced once, joined by ID from `Variables`. |

`Identity` is derived from `Variables`: one row per `datasetSpecializationId`, picking the canonical per-DSS facts (domain, bc_id, source, short_name, sdtmig_start_version, sdtmig_end_version) and the specimen/method projection columns the consumer tracks depend on. No parallel authoring — `Identity` is a view, not a second source.

## 3. Back-compat guarantee

The `Identity` sheet's column set and semantics match today's `BC_DSS` sheet exactly. Downstream tracks (`sdtm-findings/`, `sdtm-domain-reference/`) continue to read the same columns and see the same values. Diff CSVs between the old and new `Identity` sheet should be zero-row for the 1,326 DSSs currently in `interim/COSMoS_BC_DSS.xlsx` (modulo any bugs fixed along the way, which get flagged explicitly in the release notes).

Consumer tracks requiring VLM-row-grain data (future Step 3 narrative work, cross-domain-class queries) read `Variables` / `Relationships` / `Codelists`.

## 4. Architecture

The driver is `linkml_runtime.SchemaView` over `cosmos_sdtm_model.yaml` (and `cosmos_bc_model.yaml` for the BC side). The schema defines:

- The slot list on `SDTMVariable` — becomes the `Variables` column list.
- The slot list on `SDTMGroup` (ex-variables) — becomes the DSS-level columns on `Identity`.
- The `RelationShip` class — becomes the `Relationships` sheet's column schema.
- The NCIt-anchored enumerations (`OriginTypeEnum`, `OriginSourceEnum`, `RoleEnum`, `ComparatorEnum`) — used to validate values on the fly and surface their `meaning:` NCIT anchors in the `ReadMe`.

The xlsx-to-slot bridge is the rename table in `COSMoS_Graph_As_Authored.md §7.1`. Either hardcoded in the flattener module, or regenerated at build time from SchemaView by matching slot `name` against normalised column names. The rename table is small (32 entries) and stable across releases — hardcoding is fine.

The flatten step reads the VLM-sheet into a pandas DataFrame, applies the rename bridge to get LinkML slot names as column headers, then projects to the three sheets using SchemaView's class/slot metadata. No hand-written column list anywhere.

## 5. Open decisions

Three questions need answers before the flattener is written. None block starting the design work; all three block finalising the sheet schemas.

**DEC materialisation.** The BC export has `dataElementConcepts` per BC; the SDTM export carries `dec_id` (FK) on each variable. Option (a): materialise the DEC join as columns on `Variables` (`dec_id`, `dec_label`, `dec_ncit_code`). Option (b): leave `Variables.dec_id` as FK only, provide a separate `DECs` sheet. Recommendation: (a) — consumers need DEC labels more often than DEC-level metadata, and the join is cheap.

**subsetCodelist serialisation.** The xlsx stores it as a string. Option (a): pass through as string. Option (b): parse to a structured representation (parent codelist + subset definition + term list) at flatten time. Recommendation: (a) for now — only 16% of DSSs use it, the string form is what the authoring working group produces, and structured parsing can be added later without breaking columns. Revisit if the case-study work needs the structure.

**Anomaly policy.** Three known data issues from the audit:
1. `vlm_source` has `MB-MBTESTCD` (7 rows) alongside `MB.MBTESTCD` (3 rows) — dot-vs-hyphen split.
2. 313 rows (~2.5%) have no reification quad.
3. 4 DSSs have no relationship edge at all.

Recommendation: flag but don't silently fix. Add a `data_issues` sheet (one row per anomaly, with `dss_id` / `row_index` / `issue_type` / `details`) and surface counts in `ReadMe`. Fix-in-place is out of scope — the flattener should be lossless over the source.

## 6. Non-goals for Step 2

- CRF Specializations. No released COSMoS package carries CRF YAML; the 2026-Q1 release has CRF only in `yaml/20251231_draft/`. Deferred until a released package includes it. The flattener is BC + SDTM only at Step 2.
- NCIt enrichment beyond what the source xlsx already carries. `codelist.conceptId`, `assignedTerm.conceptId`, `originType`/`originSource` NCIt anchors are surfaced as-is (IDs passed through). Resolving these to definitions, synonyms, UMLS/LOINC mappings is Step 3.
- Narrative generation. The reification-as-legibility pattern (linking phrase + predicate term) is surfaced in the `Relationships` sheet. Rendering it into DataBook prose is Step 3.
- Sheet-level diffs against the previous release. Release-note generation stays on the existing workflow; this note does not change it.

## 7. Deliverables

- `cosmos-bc-dss/notebooks/10_flatten_schema_driven.ipynb` — the new flattener. Replaces the hand-column-list flatten step. Inputs from `downloads/`, outputs to `interim/COSMoS_BC_DSS.xlsx` (same path, new sheet schema).
- `cosmos-bc-dss/notebooks/11_backcompat_diff.ipynb` — generates the zero-row diff between the new `Identity` sheet and the pre-rewrite `BC_DSS` sheet.
- `cosmos-bc-dss/reports/flattener_rewrite_audit.md` — short QA narrative: sheet shapes, row counts, anomalies, back-compat diff result.

Consumer track changes (sdtm-findings reads updating from `BC_DSS` to `Identity`) are a follow-up and sit outside this branch's scope — `Identity` preserves column names, so consumer notebooks need only a sheet-name change at most.
