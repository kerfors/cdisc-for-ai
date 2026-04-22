# Flattener Rewrite Audit — Step 2 Close-out

*cosmos-bc-dss, 2026-04-22. Companion to [COSMoS_Flattener_Rewrite.md](../docs/COSMoS_Flattener_Rewrite.md).*

---

## 1. Outcome

The flattener rewrite is built. Notebooks 10, 20, 30 produce two multi-sheet
interim workbooks (`COSMoS_Graph.xlsx`, `COSMoS_Graph_CT.xlsx`) plus a
validation report. The query cookbook (notebook 50) proves the graph shape
is traversable for the questions the HTML story pairs pose narratively.

Two items from the original design note did not land as drafted, both by
considered decision rather than oversight:

- The `Identity` back-compat sheet was not built. Consumer tracks will be
  rewired to read the new multi-sheet graph instead.
- Notebook 11 (`11_backcompat_diff.ipynb`) was therefore not created.

Both decisions are recorded in §4 below.

## 2. What was built

### 2.1 Notebooks

| Notebook | Purpose | In design note? |
| --- | --- | --- |
| `10_flatten_schema_driven.ipynb` | Schema-driven flatten from the CDISC Excel export into `COSMoS_Graph.xlsx`. | Yes |
| `20_resolve_ct.ipynb` | Joins `COSMoS_Graph.xlsx` bindings against NCI EVS SDTM CT, emits `COSMoS_Graph_CT.xlsx`. | No (added) |
| `30_validate_graph.ipynb` | Emits `reports/graph_validation_report.md/json`. | No (added) |
| `50_query_examples.ipynb` | Query cookbook — eight queries pinned to the story-pair DSSs. | No (added) |

The Step 1 exploratory notebooks (`01_verify_graph_walk.ipynb`,
`02_xlsx_source_audit.ipynb`) were removed after Step 2 closure; their
findings are cited in
[docs/COSMoS_Graph_As_Authored.md §9](../docs/COSMoS_Graph_As_Authored.md).

Notebooks 20, 30, 50 are scope expansion beyond the original design note.
They are kept because each one answers a question the design note left
implicit: "are the NCIt anchors real" (20), "what breaks" (30), "does the
graph answer the narrative questions" (50).

### 2.2 Interim workbooks

**`interim/COSMoS_Graph.xlsx`** — schema-driven flatten, 2026-04-22 build:

| Sheet | Grain | Rows × Cols |
| --- | --- | --- |
| `ReadMe` | — | 22 × 1 |
| `DSS` | one per Dataset Specialization | 1,326 × 8 |
| `Variables` | one per SDTMVariable (VLM-row grain) | 12,677 × 26 |
| `Relationships` | one per reification quad | 12,364 × 6 |
| `Codelists` | deduped (codelist_concept_id, codelist_submission_value) | 291 × 3 |
| `BC` | one per Biomedical Concept | 1,345 × 10 |

**`interim/COSMoS_Graph_CT.xlsx`** — CT-resolved view, 2026-04-22 build:

| Sheet | Grain | Rows × Cols |
| --- | --- | --- |
| `ReadMe` | — | 32 × 1 |
| `Codelists` | one per bound codelist, enriched with NCI CT labels | 291 × 7 |
| `CodelistTerms` | one per (codelist, term) pair | 17,523 × 7 |
| `AssignedTerms` | one per unique assigned-term concept | 1,170 × 4 |
| `Unresolved` | concept IDs not found in SDTM CT 2026-03-27 | 6 × 4 |
| `Anomalies` | pinned-term-not-in-bound-codelist cases | 1 × 7 |

### 2.3 Reports

- `reports/graph_validation_report.md` — human-readable summary table + per-check detail.
- `reports/graph_validation_report.json` — structured output for downstream consumption.

## 3. Divergences from the design note

The original design note committed to three sheets (`Identity`, `Variables`,
`Relationships`) plus `ReadMe` and a `Codelists` sheet. What was built:

| Design note | Built | Reason |
| --- | --- | --- |
| `Identity` (36 cols, back-compat of `BC_DSS`) | **Not built** — replaced by `DSS` (8 cols) | See §4. |
| `Variables` (VLM-row grain) | Built, 26 cols | Matches intent. |
| `Relationships` (reification quad) | Built, 6 cols | Matches intent. |
| `Codelists` (deduped) | Built, 3 cols in base + 7 cols in CT-resolved | Split across two files: identity in `COSMoS_Graph.xlsx`, NCI CT enrichment in `COSMoS_Graph_CT.xlsx`. |
| *(not in design note)* | `BC` sheet added | BC-level identity and hierarchy are needed by the cookbook and by consumer tracks; carrying them as a separate sheet avoids re-joining against `downloads/` on every query. |
| *(not in design note)* | `CodelistTerms`, `AssignedTerms` | NCI CT resolution lifted out of the flattener into its own notebook so the flattener stays lossless-over-source. |

The DEC materialisation decision flagged as open in the design note (Option
a vs Option b) resolved to **Option a**: `dec_id` carried on `Variables`
as a scalar. DEC labels and NCIt codes are deferred to Step 3. No separate
`DECs` sheet was created.

The subsetCodelist serialisation decision resolved to **Option a**:
passed through as the string the authoring working group produces. The
`Variables.subset_codelist` column carries it verbatim. Structured parsing
deferred until a case study needs it.

## 4. Back-compat decision — `Identity` sheet abandoned

The design note committed to an `Identity` sheet that reproduced the
legacy `BC_DSS` sheet's 36 columns (as observed on `interim/COSMoS_BC_DSS.xlsx`,
1,768 rows of mixed BC + DSS + mixed `Row_Type`). This was not built.

Reason. The legacy `BC_DSS` sheet conflates three distinct grains into one
row shape — BC rows, DSS rows, and some flattened-collection rows —
distinguished by the `Row_Type` column. Reproducing that shape on top of
a schema-driven flatten that has already separated the grains (`BC` sheet,
`DSS` sheet, `Variables` sheet) means re-collapsing them, which defeats
the purpose of the rewrite. Consumer tracks that read `BC_DSS` today read
it with `Row_Type` filters anyway — the filter logic can instead become a
sheet selection (`BC` vs `DSS` vs `Variables`) on the new file.

Consequence. Consumer tracks (`sdtm-findings/notebooks/*.ipynb`,
`sdtm-domain-reference/`) are not back-compatible across this branch
without rewiring. The rewiring is tracked as a separate task (Option B
in the Step 2 follow-up plan) and is out of scope for this branch.

Files preserved. The legacy `interim/COSMoS_BC_DSS.xlsx` is left in place;
nothing in this branch deletes it. Consumer tracks can continue to read it
until they are rewired, at which point it can be retired.

## 5. Validation triage

`reports/graph_validation_report.md` carries eight checks. Three INFO items
are documented-and-accepted anomalies from the Step 1 audit. Three FAILs
warrant explicit triage here.

### 5.1 FAIL — `schema_column_coverage` (13)

Not a data issue. The check compares the `Variables` sheet's column names
against LinkML slot names on `SDTMVariable`. Mismatches are all naming-
convention artefacts of the flattening:

- xlsx uses snake_case scalars (`assigned_term_concept_id`,
  `assigned_term_value`), LinkML uses nested objects (`assigned_term`
  with `conceptId` and `value`). Same for `codelist`. This is the flatten
  step doing its job.
- `dec_id` vs schema's `data_element_concept_id`, `is_nonstandard` vs
  `is_non_standard`, `variable_name` vs `name` — snake_case vs LinkML
  naming. Documented in the xlsx→slot rename table
  (`docs/COSMoS_Graph_As_Authored.md §7.1`).
- `relationship` is a schema slot whose subordinate fields are inlined
  on `Variables` as (`subject`, `linking_phrase`, `predicate_term`,
  `object`) and also projected to the `Relationships` sheet. Expected.

Action. Tighten the validator (30) to account for the documented flatten
rules rather than reclassify the check. Low priority — the check's current
FAIL status does not reflect data damage. Deferred.

### 5.2 FAIL — `ct_unresolved_concept_ids` (6)

Six concept IDs in the graph that the CT resolver (notebook 20) does not
find in the 2026-03-27 NCI EVS SDTM Terminology file. Triage places them
into three patterns — none is a resolver bug, all three are upstream
authoring-or-subset issues:

*Pattern A — CT-subset gap, COSMoS semantically correct*

| Concept ID | NCIt preferred term | Semantic type | Pinned on |
| --- | --- | --- | --- |
| C132388 | Treponema pallidum Antibody Measurement | Laboratory Procedure | MB TPLAB (TESTCD/TEST) |
| C171439 | SARS-CoV-2 Antibody Measurement | Laboratory Procedure | MB SAR2ABDET (TESTCD/TEST) |

Valid NCIt concepts of the right class (Laboratory Procedure), but not
yet lifted into the MBTESTCD (C120527) / MBTEST (C120528) subset in
SDTM CT 2026-03-27. Upstream owner: CDISC SDTM CT team.

*Pattern B — COSMoS authoring error, wrong concept class*

| Concept ID | NCIt preferred term | Semantic type | Pinned on | Correct anchor (already in SDTM CT) |
| --- | --- | --- | --- | --- |
| C94525 | Matted Tumor Mass Present | Finding (state) | TU TUMERGE, TUMERGE_RECIST1_1 | **C225437** "Confluent Tumor Masses Assessment" (Laboratory Procedure, in C96784 TUTESTCD) |
| C96642 | Tumor Fragmentation / Tumor Split | Finding (state) | TU TUSPLIT, TUSPLIT_RECIST1_1 | **C225438** "Tumor Fragmentation Assessment" (Laboratory Procedure, in C96784 TUTESTCD) |

COSMoS pins the finding-state concept ("a mass is matted", "a mass has
fragmented") rather than the assessment concept ("the act of assessing
whether the mass is matted / fragmented"). The correct TESTCD anchors
already exist in the 2026-03-27 SDTM CT package. Upstream owner: COSMoS
authoring working group.

*Pattern C — Legacy codelist codes, superseded in SDTM CT*

| Concept ID | Submission value | Pinned on | Supersession in 2026-03-27 CT |
| --- | --- | --- | --- |
| C66790 | ETHNIC | DM ETHNIC (codelist_concept_id) | **C128690** ETHNICC "Ethnicity As Collected" |
| C74457 | RACE | DM RACE (codelist_concept_id) | **C128689** RACEC "Race As Collected" |

COSMoS authoring still references the pre-supersession codelist codes.
Upstream owner: COSMoS authoring working group.

Action. No resolver extension required — all six are upstream authoring
or subset issues, not scope gaps in the flattener. Flag Patterns B and C
to the COSMoS working group with the corrected anchors; flag Pattern A
to CDISC SDTM CT as a subset-coverage request. Resolver behaviour stays
as-is: concept IDs that do not resolve land in `Unresolved` and validator
check `ct_unresolved_concept_ids` remains FAIL until upstream closes.

### 5.3 FAIL — `pinned_term_not_in_bound_codelist` (1)

One DSS-level inconsistency:

`OXYSAT.VSSTRESU` pins `C105484 "fraction of 1"` as the standard unit,
but the bound codelist is `VSRESU (C66770)` and C105484 is not a
permitted term in it. C105484 lives in the general `UNIT (C71620)`
codelist; VSRESU's 29 permissible values cover %, mmHg, beats/min etc.
but not fraction-of-1.

Semantically the pin is correct — SpO2 is routinely reported as a
decimal fraction between 0 and 1 — so this surfaces as a SDTM CT content
gap (VSRESU missing "fraction of 1") rather than a COSMoS authoring
error. Upstream owner: CDISC SDTM CT team, not COSMoS.

Action. Flag for the SDTM CT team alongside Pattern A above. Do not
silently fix — policy from the design note §5 stands.

### 5.4 INFO items accepted

- `vlm_source_hyphen_detail` (4): MB SARS-CoV-2 DSSs authored with
  `MB-MBTESTCD` (hyphen) alongside the `MB.MBTESTCD` (dot) convention.
  Documented as an upstream authoring convention anomaly.
- `empty_reification_quad_rows` (313): 2.5% of Variables rows have no
  reification quad. The rows still carry their non-relational slots
  (name, role, codelist, etc.); they are simply not counted in the
  `Relationships` sheet.
- `dss_without_any_edge` (4): BRTHDTC, ETHNIC, RACE, SEX — Demographics
  identity DSSs that do not follow the Findings reification pattern.
  Structural, not a defect.

## 6. Items deferred beyond Step 2

Tracked as separate tasks so the end-state is visible:

- **Rewire consumer tracks** (`sdtm-findings/`, `sdtm-domain-reference/`)
  to read `COSMoS_Graph.xlsx` / `COSMoS_Graph_CT.xlsx` instead of
  `COSMoS_BC_DSS.xlsx`. Preserves the two-sheet output shape downstream
  (Test_Identity + Measurement_Specs).
- **Upstream flags** — raise the four authoring/subset findings from §5.2
  and §5.3 with the relevant working groups: TU TUMERGE / TUSPLIT
  (wrong concept class) and DM ETHNIC / RACE (legacy codes) to COSMoS;
  MB TPLAB / SAR2AB (subset gap) and VSRESU "fraction of 1" (codelist
  content gap) to CDISC SDTM CT.
- **Step 3 narrative layer** — `relationship.linking_phrase` plus NCIt
  anchors into DataBook Tier-3 prose. Design not started.

## 7. Step 2 closure

Step 2 is closed with the following caveats made explicit above:

1. `Identity` back-compat sheet was abandoned by considered decision; the
   legacy `interim/COSMoS_BC_DSS.xlsx` remains in place until consumer
   rewiring lands.
2. Two FAIL checks carry deferred actions: validator tightening (§5.1)
   and upstream flags to the COSMoS and SDTM CT working groups (§5.2,
   §5.3). Neither blocks downstream work — the graph itself is sound.
3. The OXYSAT/VSSTRESU anomaly is flagged for upstream SDTM CT, not
   fixed.

The companion design note (`docs/COSMoS_Flattener_Rewrite.md`) has been
updated to match what was built.
