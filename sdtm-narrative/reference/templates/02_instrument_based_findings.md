# Template 02 — Instrument-based Findings

*Reference stories:*
*`docs/6MWT_COSMoS_Story.html` (DSS grain).*
*`docs/6MWT_NCIt_Story.html` (NCIt composition ancestry).*
*Applies to: QS, FT, RS.*

---

## Scope

One Tier 2b paragraph per DSS in Domain_Class = instrument-based
Findings. The clinical measurement *is* the execution of a named
instrument — a questionnaire, a functional test, or a disease-response
rating. The DSS pins TESTCD to an item (e.g. `DISTWLK1M` for 6MWT
distance walked). The Tier 2b proposition is about a single instrument
item; the Tier 3 DataBook composes the full instrument — item-level
DSSs plus their NCIt composition ancestry.

The distinction from specimen-based Findings is structural: the
qualifier axes here are *instrument identity, item identity, and the
instrument's NCIt class hierarchy*, not specimen/method/result-scale.
Standard Unit and LOINC still apply where the item produces a numeric
result; they are absent on rating-scale items.

## Facts the template reads from the graph

- **DSS row** (as Template 01): `DS_Code`, `DS_Name`, `short_name`,
  `vlm_source`, `Domain`, `Domain_Class`, `TESTCD`, `Parent_BC_ID`,
  `SDTMIG_since`.
- **DSS attributes**: `Domain`, `Standard_Unit`, `Allowed_Units`,
  `Decimal_Places`, `LOINC_Code`. Specimen / Method / Result_Scale
  are typically null for instrument items and are omitted from the
  prose when null.
- **Variables pinned by the DSS** (as Template 01), with the
  additional expectation that `--CAT` and `--SCAT` pin to the
  instrument category (`6MWT`) and sub-category (`DISTANCE WALKED`)
  respectively.
- **Parent BC row** — the instrument-level BC grouping all items of
  this instrument.
- **Sibling item DSSs** (from `DSS` filtered to
  `Parent_BC_ID = <this BC>` and `DS_Code <> <this DSS>`): all items
  of the same instrument. Typically ordered by `TESTCD`.
- **TESTCD identity** (as Template 01), for the NCIt anchor of the
  item code.
- **Instrument codelist ancestry** (from
  `cosmos-graph/interim/COSMoS_Graph_CT.xlsx`, sheet `Codelists`,
  and from `sdtm-test-codes/machine_actionable/SDTM_Instrument_Identity.xlsx`):
  - The instrument codelist `C-code` (NCIt `cosmos-container`).
  - Its parent NCIt class (`cosmos-instr`, e.g. C164366
    "Six-Minute Walk Test").
  - Its NCIt container class (C20993 "CDISC Questionnaire/Rating/Scale
    Test Code Terminology") or the functional-test / response-scale
    equivalent.
  - Its NCIt classification class (C211913 or similar).
- **Category / sub-category resolution** (from `Categories` sheet):
  the label strings for `--CAT` and `--SCAT`.

## Prose form emitted

### Band 1 — prose opener

```
The **{{DS_Name}}** specialization ({{DS_Code}}) realises item
**{{TESTCD}}** ({{NCIt_Preferred_Term}}) of the **{{BC_Name}}**
instrument, as a {{Domain}}-domain row template. It belongs to the
{{COSMoS_Category}} / {{COSMoS_Subcategory}} grouping.
```

If the item produces a numeric result (`Standard_Unit` populated):

```
 The item produces a numeric result in {{Standard_Unit}}.
```

If the item produces an ordinal / categorical rating (Standard_Unit
null but a value-list variable is pinned):

```
 The item produces a {{value_list_name}} rating, drawn from the
{{value_list_codelist_code}} codelist.
```

### Band 2 — legend (Tier 3 only)

For Tier 3, the 6MWT_NCIt composition band appears in addition to the
6MWT_COSMoS DSS band. Legend keys emitted verbatim:

```
cosmos-bc, cosmos-dss, sdtm-ct, ncit-class, ncit-container,
ncit-instr.
```

### Band 3 — tree traversal

Sub-band 3a — DSS as proposition (same shape as Template 01 sub-band
3a, differing in attribute labels):

```
As a row template, {{DS_Code}} pins:

- {{var_nn(TESTCD)}} ({{TESTCD}}) = **{{NCIt_Preferred_Term}}**
- {{var_nn(--CAT)}} ({{Domain}}CAT) = **{{COSMoS_Category}}**
- {{var_nn(--SCAT)}} ({{Domain}}SCAT) = **{{COSMoS_Subcategory}}**
{{#each pinned_qualifier_vars}}
- {{var_nn(Variable)}} ({{Variable}}) = **{{assigned_term}}**
{{/each}}

Open slots (value-list constrained but unpinned):

{{#each open_qualifier_vars}}
- {{var_nn(Variable)}} ({{Variable}}) — constrained to
  {{value_list}}.
{{/each}}

Measurement-spec attributes:

| Attribute | Value |
|---|---|
| Domain | {{Domain}} |
| Standard Unit | {{Standard_Unit}}{{#if_null}} — (ordinal rating, no unit){{/if_null}} |
| Allowed Units | {{Allowed_Units}} |
| Decimal Places | {{Decimal_Places}} |
| LOINC | {{LOINC_Code}} |
| vlm_source | {{vlm_source}} |
```

Sub-band 3b — sibling items (emit only if `|siblings| > 0`):

```
The **{{BC_Name}}** instrument comprises {{|siblings|+1}} items.
{{DS_Code}} is one of them:

{{#each siblings}}
- **{{sibling.TESTCD}}** — {{sibling.NCIt_Preferred_Term}}.
{{/each}}

Each item is a separate DSS because SDTM collects one row per item
executed.
```

Sub-band 3c — NCIt composition ancestry (Tier 3 only, from the
6MWT_NCIt pattern):

```
The {{BC_Name}} instrument is anchored in NCIt as follows:

| Layer | NCIt code | Term |
|---|---|---|
| Instrument class | {{ncit_instr_code}} | {{ncit_instr_term}} |
| Container codelist | {{ncit_container_code}} | {{ncit_container_term}} |
| Classification | {{ncit_class_code}} | {{ncit_class_term}} |

The item TESTCD **{{TESTCD}}** is a member of the container codelist
{{ncit_container_code}}; the container codelist is a subtype of the
classification {{ncit_class_code}}.
```

### Band 4 — flattened row (Tier 3 DataBook only)

As Template 01 band 4, with Specimen / Method / Result_Scale fields
present in the key-value grid but rendered empty.

### Band 5 — registry-need band (Tier 3 DataBook only)

For this template, the registry-need argument is the **instrument
composition registry** gap:

```
> ### Registry gap — instrument composition
>
> COSMoS treats each {{BC_Name}} item as an independent DSS under a
> shared parent BC. The instrument-as-artefact — its NCIt class
> ancestry, its item inventory, its published version — is implicit
> in sibling structure and in the codelist's NCIt anchors, not
> explicit.
>
> A registry of shape *(instrument_BC, ncit_instr, ncit_container,
> item_DSSs, version, evidence_of_validation)* would make the
> instrument itself addressable. Today the {{BC_Name}} instrument is
> reconstructed from {{|siblings|+1}} DSSs plus three NCIt codes.
```

## Natural-English substitutions applied

Per the two-tier rule. Variable codes expected:

- Always: `TESTCD`, `--CAT`, `--SCAT`, `--ORRES`, `--STRESC` (or
  `--STRESN` for numeric), `--ORRESU`, `--STRESU`.
- QS-specific: `QSCAT` = instrument name (pinned), `QSSCAT` = item
  group (pinned). These substitute via compositional fallback to
  `--CAT` / `--SCAT`.
- FT-specific: `FTORRES`, `FTSTRESC`, `FTSTRESN` — all via
  compositional fallback.
- RS-specific: `RSCAT` pins to the response-scale name; the
  rating-scale `RSSTRESC` value set is named by the codelist.

## Traversals required

- `BC → DSSs` via `DSS.Parent_BC_ID = BC.BC_ID` (instrument items).
- `DSS → Variables` via `Variables.DS_Code = DSS.DS_Code`.
- `Variables → Codelists` via `Variables.value_list =
  Codelists.codelist_code` (for open slots).
- `DSS → instrument-codelist NCIt ancestry` via
  `SDTM_Instrument_Identity.Codelist_C_code` → container (C20993 or
  analogue) → instrument NCIt class.
- `DSS.TESTCD → SDTM_Test_Identity.TESTCD`.

No cross-Domain_Class traversal (QS, FT, RS do not compose with other
Domain_Class DSSs at BC level in the current graph).
