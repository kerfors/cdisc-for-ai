# COSMoS As A Graph — What CDISC Actually Authors

*Step 1 of a three-step rework of the cosmos-bc-dss track: make the inherent graph model explicit before changing the flattener. A companion to [COSMoS_Specification_Focus.md](COSMoS_Specification_Focus.md), [COSMoS_Behavioural_Analysis.md](COSMoS_Behavioural_Analysis.md), [COSMoS_Collection_vs_Ontology.md](COSMoS_Collection_vs_Ontology.md) and [COSMoS_Instrument_Layer.md](COSMoS_Instrument_Layer.md).*

*cdisc-for-ai, April 2026*

---

## 1. Why this document

The current `cosmos-bc-dss` pipeline downloads the published Excel exports and flattens them into `interim/COSMoS_BC_DSS.xlsx` — one row per Dataset Specialization (DSS), 36 columns. That interim file is structurally complete for the specimen-driven Findings work it was built for. It is not sufficient for the cross-domain-class questions the X-Ray case pair surfaces, because the shape of those questions is graph-shaped (concept identity across PR and MK) and the xlsx has already thrown the graph away.

Before changing the flattener the model itself needs to be written down. CDISC publishes COSMoS as a LinkML schema plus LinkML-conformant instance YAML. The xlsx is a derived projection. This document describes what the authored graph contains, what the projection preserves, and what it drops. It is the input to the next two steps: making the flattener graph-walk-driven rather than column-list-driven (Step 2), and carrying NCIt semantics through to the narrative layer (Step 3).

Scope is the authored graph. Consumer design, the three-tier serialisation idea from the enhancement brief, and case-specialisation layering stay out of scope here.

## 2. What CDISC publishes

`cdisc-org/COSMoS` on GitHub holds the authoritative sources. Four folders matter for this document.

The `model/` folder contains three LinkML schema files — `cosmos_bc_model.yaml`, `cosmos_sdtm_model.yaml`, `cosmos_crf_model.yaml`. These are the class definitions for Biomedical Concepts, SDTM Dataset Specializations, and CRF Specializations. LinkML is explicitly designed as a graph-native modelling language (classes, typed slots, relationships, enumerations with external ontology anchors), and these three files describe the concept graph the working group is actually curating.

The `yaml/` folder contains LinkML-conformant instance data, organised by package date. The 2026-Q1 release at `yaml/20260331_r16/` has two subfolders: `bc/` (249 files) and `sdtm/` (227 files). CRF Specializations as instance YAML appear only in the draft package `yaml/20251231_draft/crf/` (303 files) — no released package carries CRF instances yet, though the `cosmos_crf_model.yaml` schema is published. Each BC, DSS and CRF Specialization is published as its own YAML file — one graph node per file, with inlined child objects (variables, codelists, relationships). A verified example is `yaml/20260331_r16/sdtm/sdtm_abi.yaml`, which Section 5 walks through.

The `openapi/` folder contains OpenAPI specifications auto-generated from the LinkML schemas. These describe the HTTP shape of the CDISC Library API. They are a derivation, not an independent source.

The `export/` folder (served at `cdisc-org.github.io/COSMoS/export/`) contains the flat Excel and CSV exports the current cosmos-bc-dss pipeline downloads. These are the lossiest of the available serialisations and the only one in use today.

The LinkML schema is the authoritative source. Everything else is generated from it.

## 3. The three schemas

### 3.1 Biomedical Concepts (`cosmos_bc_model.yaml`)

Root class `BiomedicalConcept` (tree_root), with inlined `Coding` and `DataElementConcept` children.

A BC carries its NCIt anchor explicitly — `conceptId` (the COSMoS primary key, always equal to the NCIt C-code when the concept exists in NCIt), `ncitCode`, `href` (a canonical NCIt URI), `parentConceptId` (the NCIt hierarchical parent), `shortName` (the NCIt preferred term), `synonyms`, `definition`, `resultScales` (from the enumeration `Ordinal | Narrative | Nominal | Quantitative | Temporal`), and `categories` (the multi-value grouping field discussed in [COSMoS_Instrument_Layer.md](COSMoS_Instrument_Layer.md)).

A BC also carries `coding` (a list of `Coding` objects, one per external code system it maps to — LOINC, SNOMED CT, etc., with `code`, `system`, `systemName`) and `dataElementConcepts` (a list of `DataElementConcept` objects, each with its own `conceptId`, `ncitCode`, `href`, `shortName`, `dataType` from the enumeration `boolean | date | datetime | decimal | duration | float | integer | string | uri`, and an `exampleSet`).

The `dataElementConcepts` list is the internal decomposition of the BC into its observable properties. "Glucose Measurement" (C105585) decomposes into DECs for the measured value, the specimen, the method, the units, etc. This level is not visible in the current xlsx.

### 3.2 SDTM Dataset Specializations (`cosmos_sdtm_model.yaml`)

Root class `SDTMGroup` (tree_root), with inlined `SDTMVariable` children, and each variable carrying inlined `CodeList`, `SubsetCodeList`, `AssignedTerm`, and `RelationShip` objects.

An `SDTMGroup` is one DSS — one VLM row template on a specified `domain` and `source` variable, identified by `datasetSpecializationId` (the DS_Code mnemonic, e.g. `ABI`, `GLUCSER`, `XRAYCHEST`). It carries `shortName`, `sdtmigStartVersion`, `sdtmigEndVersion`, `biomedicalConceptId` (the FK into the BC graph), and `variables` (the list of SDTMVariable objects).

The `source` slot is the VLM source — the `<domain>.<variable>` the DSS is a value-level specialisation of (e.g. `VS.VSTESTCD` for ABI, `PR.PRTRT` for X-Ray procedure specialisations, `MK.MKTESTCD` for MK method-qualified specialisations). This is the hinge between the DSS and the SDTM IG — it tells a consumer which variable carries the VLM pinning. It is not in the current xlsx.

Each `SDTMVariable` carries: `name`, `dataElementConceptId` (FK to the BC's DEC list), `isNonStandard`, `codelist`, `subsetCodelist`, `valueList`, `assignedTerm`, `role`, `relationship`, `dataType`, `length`, `format`, `significantDigits`, `mandatoryVariable`, `mandatoryValue`, `originType`, `originSource`, `comparator`, `vlmTarget`.

Three of these slots carry reification — see Section 4.

Four enumerations carry NCIt-anchored semantic content that the xlsx currently drops:

`OriginTypeEnum` (code_set NCIT:C170449) — `Assigned` (NCIT:C170547), `Collected` (NCIT:C170548), `Derived` (NCIT:C170549), `Predecessor` (NCIT:C170550), `Protocol` (NCIT:C170551). Each value has an NCIt anchor and an authoritative definition.

`OriginSourceEnum` (code_set NCIT:C170450) — `Investigator` (NCIT:C25936), `Sponsor` (NCIT:C70793), `Subject` (NCIT:C41189), `Vendor` (NCIT:C68608). Again each value is NCIt-anchored.

`RoleEnum` — `Identifier | Qualifier | Timing | Topic`. The SDTM structural role of the variable inside the DSS. Not NCIt-anchored in the schema but directly aligned to the SDTM IG variable role taxonomy.

`ComparatorEnum` — how a value is pinned in VLM (`EQ`, `NE`, `IN`, etc.). Matters for the "identity pin vs qualifier slot" distinction used in the X-Ray analysis.

### 3.3 CRF Specializations (`cosmos_crf_model.yaml`)

Root class `CRFGroup` (tree_root), with inlined `CRFItem` children, each CRFItem carrying inlined `CodeList`, `ListValue`, `PrepopulatedValue`, and `SDTMTarget` objects.

A `CRFGroup` is one CRF specialisation, identified by `crfSpecializationId`, linked to a BC via `biomedicalConceptId` and to a DSS via `sdtmDatasetSpecializationId` (the cross-reference slot noted in [COSMoS_Specification_Focus.md](COSMoS_Specification_Focus.md)). It carries an `implementationOption` (`Normalized | Denormalized`), a `scenario`, `categories`, and `items`.

Each `CRFItem` carries the collection-moment facts the DSS does not: `questionText`, `prompt`, `completionInstructions`, `selectionType` (`Multiple | Single`), `prepopulatedValue`, and `sdtmTarget` (the `SDTMTarget` object with `sdtmAnnotation`, `sdtmVariables`, `sdtmTargetMapping` — i.e. the SDTM annotation on the CRF plus the list of target variables plus the mapping rule).

CRF Specializations are in the flattener's scope for later work (see [COSMoS_Specification_Focus.md](COSMoS_Specification_Focus.md) on their draft status) but not in the current xlsx.

## 4. Reification at source

Three of the four inlined child objects on `SDTMVariable` carry reified graph facts that the current xlsx flattens away. This is the specific property of the authored graph that matters most for the X-Ray pair and for the enhancement brief's Tier-2 argument.

### 4.1 `RelationShip` — a typed edge on every variable

Every SDTMVariable carries a `relationship` object with four slots: `subject`, `linkingPhrase`, `predicateTerm`, `object`. This is an RDF-star-style edge attached directly to the variable node.

- `subject` — the variable itself (e.g. `VSTESTCD`).
- `linkingPhrase` — one of roughly one hundred natural-English phrases enumerated in `LinkingPhraseEnum`: "is the code for the value in", "is the result of the test in", "is the date of occurrence for", "is the subject position during performance of the test in", "is the specimen tested in", "is the method for the test in". These are the strings that show up verbatim in narrative prose.
- `predicateTerm` — one of about thirty programmatic terms enumerated in `PredicateTermEnum`: `IS_DECODED_BY`, `IS_RESULT_OF`, `IS_TIMING_FOR`, `IS_UNIT_FOR`, `IS_SPECIMEN_TESTED_IN`, `IS_POSITION_FOR`, `IS_SUBJECT_STATE_FOR`, etc. These are the programmatic types for traversal.
- `object` — the other variable or concept the relationship targets (e.g. `VSTEST`, `VSTESTCD`).

The `LinkingPhraseEnum` / `PredicateTermEnum` pairing is the reification-as-legibility pattern: the programmatic term indexes the relation for machine traversal, the linking phrase reads as English for the narrative layer. Both are authored; neither needs to be inferred.

### 4.2 `AssignedTerm` — the NCIt-anchored concept pin

`AssignedTerm` has two attributes: `conceptId` (the NCIt C-code, pattern `C\d+` or `CNEW`) and `value` (the submission value).

When a DSS pins a variable to a specific value (e.g. VSTESTCD = "ABI" in the ABI DSS), the pin carries both the submission value and its NCIt identity. This is the join key that answers the X-Ray question: the same X-Ray concept (NCIt C38101) appears as `assignedTerm.conceptId: C38101` in a PR DSS and as a value in an MK method codelist. One concept, two structural roles. The traversal is one hop, not string-matching.

### 4.3 `CodeList` and `SubsetCodeList` — NCIt-anchored codelist identity

`CodeList` has `conceptId` (NCIt C-code for the codelist), `href` (canonical NCIt URI), and `submissionValue` (the CDISC codelist name). `SubsetCodeList` narrows a parent codelist to a specific subset of terms — in the LinkML schema it has slots for the parent and the subset definition, and in the xlsx projection it is serialised as a string with `range: string`.

This means every variable's codelist binding is already anchored to NCIt at source. The "closed-world question: does this DSS allow X-RAY as a method value" is answerable by reading `subsetCodelist` — no CT re-lookup needed. `codelist` is populated on ~54% of variable rows (99.9% of DSSs); `subsetCodelist` is the less common case, populated on 2.2% of rows (16% of DSSs) per the 2026-Q1 audit.

## 5. Walk-through: `sdtm_abi.yaml`

This is the authored graph for one DSS, in full, verbatim from `yaml/20260331_r16/sdtm/sdtm_abi.yaml`. It shows how the schema concepts above appear on a real specialisation.

```yaml
packageDate: "2026-03-31"
packageType: sdtm
datasetSpecializationId: ABI
domain: VS
shortName: "Ankle-Brachial Index"
source: VS.VSTESTCD
sdtmigStartVersion: "3-2"
biomedicalConceptId: C87304
variables:
  - name: VSTESTCD
    codelist:
      conceptId: C66741
      href: https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C66741
      submissionValue: VSTESTCD
    assignedTerm:
      conceptId: C87304
      value: "ABI"
    role: Topic
    relationship:
      subject: VSTESTCD
      linkingPhrase: is the code for the value in
      predicateTerm: IS_DECODED_BY
      object: VSTEST
    mandatoryVariable: true
    mandatoryValue: true
    comparator: EQ
  - name: VSORRES
    dataElementConceptId: C70856
    role: Qualifier
    dataType: float
    significantDigits: 3
    relationship:
      subject: VSORRES
      linkingPhrase: is the result of the test in
      predicateTerm: IS_RESULT_OF
      object: VSTESTCD
    originType: Collected
    originSource: Investigator
    vlmTarget: true
  # ... VSTEST, VSSTRESC, VSSTRESN, VSDTC similarly
```

Every fact the xlsx carries is here — domain, TESTCD, decimal precision. Three layers of fact the xlsx does not carry are also here:

1. The `source: VS.VSTESTCD` slot tells a consumer this is a VLM pinning on VSTESTCD. Different DSS patterns pin on different source variables (PR: `PR.PRTRT`, MK: `MK.MKTESTCD`, LB: `LB.LBTESTCD`). The enhancement brief calls this the "mode" of the DSS.
2. Each variable carries `role` (Topic / Qualifier / Timing / Identifier), `relationship` (the typed edge with both the NCIt predicate and the English linking phrase), `mandatoryVariable`, `mandatoryValue`, `originType`, `originSource`, and `comparator`. On VSTESTCD specifically, `mandatoryValue: true` plus `comparator: EQ` plus `assignedTerm: {conceptId: C87304, value: "ABI"}` is the formal definition of "this DSS pins VSTESTCD = ABI" — i.e. identity pinning. On VSORRES, `mandatoryValue: false` plus no comparator is the formal "this is a qualifier slot, result value is not pinned".
3. `assignedTerm.conceptId: C87304` on VSTESTCD is the NCIt anchor for the pinned value (Ankle-Brachial Index). This is the join key for cross-DSS concept traversal.

The identity-pin-vs-qualifier-slot distinction that had to be inferred from narrative prose in [COSMoS_Behavioural_Analysis.md](COSMoS_Behavioural_Analysis.md) is a structural fact here, readable directly from `mandatoryValue` and `comparator`.

## 6. What the current xlsx preserves and drops

The Flatten notebook produces a 36-column `BC_DSS` sheet with one row per DSS. Two columns carry the BC↔DSS FK (`COSMoS_BC_ID`, `DS_Code`). The remaining 34 columns hold a subset of the graph, selected by hand.

What is preserved:

- BC-level identity (`COSMoS_BC_ID`, `NCIt_Code`, `BC_Name`, `BC_Definition`, `BC_Synonyms`, `BC_Type`, `BC_Scope`, `Categories`, `Hierarchy_Path`, `Parent_Label`).
- TESTCD identity — but only the TESTCD value, not the per-variable graph around it (`TESTCD`, `TEST`, `TESTCD_NCIt`).
- DSS identity (`DS_Code`, `DS_Name`, `Domain`, `Domain_Class`).
- A projected summary of three qualifier variables — result scale, specimen (with NCIt code and CT submission value), method (with NCIt code and CT submission value): `Result_Scale`, `Specimen`, `Specimen_NCIt`, `Specimen_CL`, `Method`, `Method_NCIt`, `Method_CL`. Everything else at the variable level is dropped.
- LOINC join (`LOINC_Code_Count`, `LOINC_Code`).
- Unit metadata (`Allowed_Units`, `Standard_Unit`, `Decimal_Places`) — not as a structured value list, only as pipe-delimited strings.
- SDTM-side grouping (`COSMoS_Category`, `COSMoS_Subcategory`).
- A fixed set of finding-qualifier columns (`location`, `laterality`, `evaluator`).

What is dropped:

- **The whole `RelationShip` layer.** No linking phrases, no predicate terms. The narrative text that the enhancement brief's Tier 2 and Tier 3 consume cannot be reconstructed from the xlsx — it can only be re-authored by a downstream consumer who does not have the source edges.
- **The `source` slot.** The xlsx knows the DSS belongs to VS but does not know whether it pins on VSTESTCD, VSTEST, or something else. For PR, the difference between "pins on PRTRT" vs "pins on PRTRTCAT" is lost.
- **Per-variable `assignedTerm`.** Only the TESTCD is projected (as `TESTCD_NCIt`). Identity pins on PRLOC, PRINDC, MKTEST etc. that live on variables other than TESTCD are not visible.
- **Per-variable `codelist` / `subsetCodelist`.** Only the specimen and method codelists are projected (`Specimen_CL`, `Method_CL`). Codelists on result qualifiers, on units, on position/laterality are dropped. Subset codelists (the MK `MKMETHOD` value_list example from the X-Ray case) are entirely dropped.
- **Per-variable `role`, `mandatoryVariable`, `mandatoryValue`, `comparator`.** The identity-pin / qualifier-slot distinction that drives the X-Ray PR↔MK asymmetry is a pattern that can only be re-inferred, not read.
- **Per-variable `originType`, `originSource`.** The NCIt-anchored definitions for "Collected by Investigator" vs "Derived" vs "Assigned" are dropped — they were never in the xlsx.
- **`valueList`.** Enumerated permitted-value lists per variable are dropped. The only place a value list survives is `Allowed_Units` as a delimited string.
- **`Coding` on the BC.** LOINC is projected into two columns. SNOMED, other code systems in `BC.coding` are not surfaced.
- **`DataElementConcept` on the BC.** The internal decomposition of the BC into DECs — the join key that could connect a variable's `dataElementConceptId` back to its BC-level semantic identity — is entirely dropped.
- **CRF Specializations.** Out of scope for the current flattener.

The xlsx is a projection of a graph onto a fixed column set. It works for specimen-driven Findings because that pattern uses the projected columns. It fails for cross-domain-class queries and for narrative generation because those need the columns that are not projected.

## 7. Three access modes

CDISC publishes COSMoS in three forms. All three derive from the LinkML schema.

**Graph-native YAML in GitHub (`yaml/<packageDate>/{bc,sdtm}/`, plus `crf/` in draft packages).** One file per object, LinkML-conformant, no information loss. Version-pinned by package date. No authentication. Stable URL pattern at `github.com/cdisc-org/COSMoS/tree/main/yaml/...`. This is the shape the `sdtm_abi.yaml` walk-through uses. Practical properties: a full package is a few thousand small YAML files; consumption is a `git clone` plus a walk of three folders. **Caveat: the 2026-Q1 release publishes YAML for 5 of the 32 domains present in the package (RE, VS, DS, LB, GF — 227 of 1,326 DSSs). The YAML folder is a partial publication at this release. Audit: `cosmos-bc-dss/notebooks/02_xlsx_source_audit.ipynb`, 2026-04-22.**

**CDISC Library API (`library.cdisc.org`).** REST endpoints documented by the OpenAPI specs in the `openapi/` folder. Requires an API key. Same object shape as the YAML — the API is a dynamic serve-layer over the same LinkML-conformant data. Practical properties: supports "give me the latest", supports per-object fetch, has request rate limits, requires credential management. The OpenAPI file list was not enumerated in preparing this document (GitHub tree pages exceed the fetch token limit); the exact endpoint layout for `/api/cosmos/v2/sdtm/...` should be confirmed against the live CDISC Library documentation before implementation.

**Flat Excel exports (`cdisc_sdtm_dataset_specializations_latest.xlsx`, `cdisc_biomedical_concepts_latest.xlsx`).** A full tabular serialisation of the authored graph at VLM-row grain. The SDTM DSS export is 12,677 rows × 32 columns for the 2026-Q1 package (1,326 DSSs across 32 domains). Every column maps 1:1 to a LinkML slot — 0 unmapped columns, column-to-slot rename table in Section 7.1. ABI xlsx rows and `sdtm_abi.yaml` agree fact-for-fact at variable level. Reification quad (`subject/linking_phrase/predicate_term/object`) is populated on 97.5% of rows / 99.7% of DSSs; `assigned_term` / `codelist` / `mandatory_*` / `comparator` / `origin_type/source` are populated where expected. The xlsx is therefore graph-equivalent to the YAML at VLM-row grain, not a lossy projection. Useful both for human review and as the pipeline input.

Implication for the cosmos-bc-dss pipeline: the loss in the current pipeline is introduced by the *flattener* (`interim/COSMoS_BC_DSS.xlsx` collapses 12,677 VLM rows into 1,326 one-row-per-DSS records against a hand-picked column list), not by the CDISC export. Options for Step 2 — in preference order — are (1) keep the existing Excel export as input and rewrite the flattener as a schema-driven walk over the VLM-row grain; (2) switch to the GitHub YAML folder when it becomes complete across all 32 domains; (3) switch to the CDISC Library API. Option 1 is available today with no unknowns; option 2 is blocked on upstream YAML coverage; option 3 is blocked on API endpoint verification and credential management.

### 7.1 xlsx column → LinkML slot mapping

The SDTM Dataset Specializations xlsx uses snake_case column names; the LinkML schema uses camelCase slot names; some are renamed further when a slot sits on an inlined class. All 32 xlsx columns map to LinkML slots with zero unmapped (audit: notebook 02, 2026-04-22). The table below is the canonical mapping.

| xlsx column | LinkML slot | notes |
|---|---|---|
| `package_date` | `packageDate` (SDTMGroup) | |
| `bc_id` | `biomedicalConceptId` (SDTMGroup) | FK to BC graph |
| `sdtmig_start_version` | `sdtmigStartVersion` (SDTMGroup) | |
| `sdtmig_end_version` | `sdtmigEndVersion` (SDTMGroup) | |
| `domain` | `domain` | direct |
| `vlm_source` | `source` (SDTMGroup) | `<domain>.<variable>` pinning |
| `vlm_group_id` | `datasetSpecializationId` (SDTMGroup) | the DS_Code mnemonic |
| `short_name` | `shortName` (SDTMGroup) | |
| `sdtm_variable` | `name` (SDTMVariable) | |
| `dec_id` | `dataElementConceptId` (SDTMVariable) | FK to BC's DEC list |
| `nsv_flag` | `isNonStandard` (SDTMVariable) | |
| `codelist` | `codelist.conceptId` (CodeList) | NCIt C-code |
| `codelist_submission_value` | `codelist.submissionValue` (CodeList) | CDISC codelist name |
| `subset_codelist` | `subsetCodelist` | direct, range=string |
| `value_list` | `valueList` | direct |
| `assigned_term` | `assignedTerm.conceptId` (AssignedTerm) | NCIt C-code of pinned value |
| `assigned_value` | `assignedTerm.value` (AssignedTerm) | submission value of pinned value |
| `role` | `role` | direct |
| `subject` | `relationship.subject` (RelationShip) | reification quad |
| `linking_phrase` | `relationship.linkingPhrase` (RelationShip) | reification quad |
| `predicate_term` | `relationship.predicateTerm` (RelationShip) | reification quad |
| `object` | `relationship.object` (RelationShip) | reification quad |
| `data_type` | `dataType` | direct |
| `length` | `length` | direct |
| `format` | `format` | direct |
| `significant_digits` | `significantDigits` | direct |
| `mandatory_variable` | `mandatoryVariable` | direct |
| `mandatory_value` | `mandatoryValue` | direct |
| `origin_type` | `originType` | direct |
| `origin_source` | `originSource` | direct |
| `comparator` | `comparator` | direct |
| `vlm_target` | `vlmTarget` | direct |

Renames come in three forms: (i) snake_case → camelCase (`sdtmig_start_version` → `sdtmigStartVersion`); (ii) xlsx flattens an inlined child object onto the parent row (`codelist` + `codelist_submission_value` → `codelist.conceptId` + `codelist.submissionValue` on the inlined `CodeList` class); (iii) xlsx uses a shortened external name for a slot whose LinkML name reflects the model (`vlm_group_id` → `datasetSpecializationId`, `vlm_source` → `source`). A schema-driven flattener reads the rename pairs from this table (or regenerates them via SchemaView at build time).

## 8. Implications for Steps 2 and 3

### Step 2 — dynamic flattening driven by graph walk

The current flattener has a hardcoded column list (`Specimen`, `Specimen_NCIt`, `Specimen_CL`, `Method`, …). Every new variable role the COSMoS working group adds — e.g. position and laterality in the 2026-03 VS expansion — requires the flattener to be updated by hand, and roles the working group adds that the flattener does not know about are silently dropped.

A graph-walk flattener operates on the LinkML schema. It enumerates the actual classes, slots, and enumerations in the model, walks the authored YAML, and produces column names (or long-format row keys) from the slot names. Three shapes the flattener then supports that it does not today:

- Every `SDTMVariable` with a `codelist`, a `subsetCodelist`, an `assignedTerm` or a `valueList` becomes a set of columns or long-format rows keyed by the variable name, without the column list being known in advance. The XRAYCHEST `subsetCodelist` on MKMETHOD, the PRLOC `assignedTerm`, the POSITION codelist on VSPOS — all appear automatically once the graph walk encounters them.
- Every `RelationShip` on a variable becomes an edge in a long-format "relationships" sheet. The enhancement brief's `VLM_Rows` sheet is effectively this table.
- Every `role`, `mandatoryVariable`, `mandatoryValue`, `originType`, `originSource`, `comparator` becomes a per-variable column. The identity-pin vs qualifier-slot distinction is readable directly.

The flattener becomes a projection function over the LinkML model rather than a hand-written list of columns. The authored graph is what's consumed; the projection is what's published.

### Step 3 — NCIt semantics for the narrative layer

NCIt enrichment in the current pipeline is a one-way lookup: for each TESTCD_NCIt code, fetch the NCIt definition, synonyms, UMLS mappings from the cached NCI EVS FLAT. This is the identity layer — "what concept is this TESTCD".

What the graph carries beyond that:

- `codelist.conceptId` — the NCIt C-code for each codelist the DSS uses. Enriching these adds codelist-level semantics (e.g. C66741 "CDISC SDTM Vital Signs Test Code Terminology" as the codelist for VSTESTCD).
- `assignedTerm.conceptId` — the NCIt C-code for every pinned value, not only TESTCD. Every variable that is pinned to a specific concept (PRDECOD=X-RAY, PRLOC=CHEST, MKMETHOD in {X-RAY, MRI, …}) becomes an NCIt-enrichable entity.
- `predicateTerm` + `linkingPhrase` — the NCIt-adjacent vocabulary for describing what a variable *does* inside the DSS. The linking phrase is the narrative English; the predicate term is the programmatic index. Together they are what the Tier 3 DataBook narrative consumes.
- `OriginTypeEnum` and `OriginSourceEnum` are already NCIt-coded in the schema. Each value has an NCIt definition via `meaning: NCIT:Cxxxxxx` — these can be surfaced directly without a lookup step.
- `dataElementConceptId` on each variable resolves back to the BC's `dataElementConcepts` list, which is NCIt-coded. The DEC layer is the join between the SDTM variable and the BC's internal semantic decomposition — currently unused because the xlsx drops it.

The NCIt enrichment step is therefore less about "enrich with information the graph doesn't have" and more about "make authored NCIt anchors resolvable". Most of what the narrative layer needs is already in the authored graph; the enrichment fills in definitions, synonyms and external-ontology mappings for the anchors already present.

## 9. What this means concretely for next work

The pipeline change is architecturally smaller than initially assumed. The download step stays on the CDISC Excel exports (the YAML folder is a partial publication; the API is an unverified alternative). The parse step stays on `openpyxl`, reading the full 12,677-row VLM-grain sheet rather than collapsing to one-row-per-DSS. The flatten step replaces the hand-written column list with a schema-driven walk over the LinkML slots — using the column-to-slot rename table in §7.1 to bridge between the xlsx's snake_case surface and the LinkML schema. The `interim/COSMoS_BC_DSS.xlsx` output either stays as a backwards-compatible projection (same columns) or gets replaced by a richer set of sheets (identity, variables long-format, relationships long-format, codelists) — the consumer tracks determine the shape.

### Verification status (2026-04-22)

1. **YAML folder structure.** Resolved. `yaml/20260331_r16/` contains `bc/` (249 yaml) and `sdtm/` (227 yaml) only. CRF instances exist solely under `yaml/20251231_draft/crf/` (303 yaml). The sdtm folder covers only 5 of the 32 domains present in the xlsx (RE, VS, DS, LB, GF). YAML consumption is therefore **blocked on upstream coverage** for the full-domain flattener; the xlsx covers all 32.
2. **LinkML runtime compatibility.** Resolved. `linkml-runtime.SchemaView` parses `cosmos_sdtm_model.yaml` and `cosmos_bc_model.yaml`; `linkml.validator.validate` returns zero errors on `sdtm_abi.yaml`. Ran in `cosmos-bc-dss/notebooks/01_verify_graph_walk.ipynb`.
3. **xlsx ↔ LinkML equivalence.** New, resolved. All 32 xlsx columns map to LinkML slots (0 unmapped). Reification quad populated on 97.5% of rows / 99.7% of DSSs. ABI xlsx rows and `sdtm_abi.yaml` agree fact-for-fact on all 6 variables (`VSTESTCD`, `VSTEST`, `VSORRES`, `VSSTRESC`, `VSSTRESN`, `VSDTC`). Ran in `cosmos-bc-dss/notebooks/02_xlsx_source_audit.ipynb`. Implication: the xlsx is graph-equivalent to YAML at VLM-row grain; schema-driven flattening is tractable against the xlsx today.
4. **CDISC Library API endpoint shape.** Open, not blocking. If API consumption becomes preferred over the xlsx (e.g. to eliminate the download step or fetch on-demand), the OpenAPI specs in `openapi/` are the definitive source; live API testing against Kerstin's credential is the fastest way to verify.

### Anomalies to track (xlsx audit, 2026-Q1)

- `vlm_source` has 37 distinct values including `MB-MBTESTCD` (7 rows) alongside `MB.MBTESTCD` (3 rows) — a dot-vs-hyphen inconsistency at source. The flattener should normalise or flag.
- 313 rows (~2.5%) have no reification quad populated; 4 DSSs have no relationship edge at all. Characterise during Step 2.
- `subsetCodelist` is populated on only 16% of DSSs — the subset-codelist handling in Step 2 should not assume it is the dominant case.

None of these block Step 2 starting.
