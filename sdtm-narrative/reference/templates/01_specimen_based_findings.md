# Template 01 — Specimen-based Findings

*Reference story: `docs/Glucose_COSMoS_Story.html`.*
*Applies to: LB, MB, MI, CP, BS, MS, PC, PP.*

---

## Scope

One Tier 2b paragraph per DSS in Domain_Class = specimen-based
Findings. DSSs in this class pin three qualifier axes: specimen
(matrix), method (how measured), and result scale (what is produced).
The BC-to-DSS ratio is many — a single biochemistry BC (e.g. glucose)
typically has 2–6 sibling DSSs that differ only in specimen / method /
scale.

## Facts the template reads from the graph

- **DSS row** (from `DSS` sheet): `DS_Code`, `DS_Name`, `short_name`,
  `vlm_source`, `Domain`, `Domain_Class`, `TESTCD`, `Parent_BC_ID`,
  `SDTMIG_since` where populated.
- **DSS attributes** (from `DSS` sheet columns): `Specimen`,
  `Specimen_NCIt`, `Method`, `Method_NCIt`, `Result_Scale`,
  `Allowed_Units`, `Standard_Unit`, `Decimal_Places`, `LOINC_Code`,
  `LOINC_Code_Count`.
- **Variables pinned by the DSS** (from `Variables` sheet filtered to
  `DS_Code = <this DSS>`): one row per `Variable`, carrying `Role`
  (topic / qualifier / timing), `assigned_term` or `value_list`
  reference, `origin` (pinned / open).
- **Assigned terms** (from `AssignedTerms` sheet): CT codes and
  preferred terms for the variables pinned to a single value.
- **Parent BC row** (from `BC` sheet, joined on `Parent_BC_ID`):
  `BC_Name`, `BC_Definition`, `BC_Synonyms`, `COSMoS_Category`,
  `COSMoS_Subcategory`.
- **Sibling DSSs** (from `DSS` sheet filtered to
  `Parent_BC_ID = <this BC>` and `DS_Code <> <this DSS>`): list for
  the sibling-summary sub-band. Order by
  `Specimen` → `Method` → `Result_Scale`.
- **TESTCD identity** (from
  `sdtm-test-codes/machine_actionable/SDTM_Test_Identity.xlsx`):
  `NCIt_Code`, `NCIt_Preferred_Term`, `NCIt_Definition`, `NCIt_Synonyms`,
  `UMLS_CUI`, `NCIm_CUI` for the TESTCD the DSS pins.
- **Case specialisations** (if any, from Case-Specialisation layer —
  see Template 04): list of `case_spec_id` that refine this DSS, for
  a cross-link stub in Band 3.

## Prose form emitted

Markdown fragments with `{{slot}}` placeholders. Slot names match
identity or graph column names; `{{var_nn(X)}}` is the natural-name
substitution helper (two-tier rule per `00_index.md`).

### Band 1 — prose opener (always emitted)

```
The **{{DS_Name}}** specialization ({{DS_Code}}) realises the
**{{BC_Name}}** biomedical concept as a {{Domain}}-domain row template:
a {{var_nn(TESTCD)}} of {{NCIt_Preferred_Term}} measured in
{{Specimen}} by {{Method}}, producing a {{Result_Scale}} result in
{{Standard_Unit}}.
```

If `SDTMIG_since` is populated, append:

```
 Added to SDTMIG in {{SDTMIG_since}}.
```

### Band 3 — tree traversal (always emitted)

Sub-band 3a: the DSS as proposition (always):

```
As a row template, {{DS_Code}} pins the following SDTM variables to
fixed values:

- {{var_nn(TESTCD)}} ({{TESTCD}}) = **{{NCIt_Preferred_Term}}**
- {{var_nn(--CAT)}} ({{Domain}}CAT) = **{{COSMoS_Category}}**
{{#each pinned_qualifier_vars}}
- {{var_nn(Variable)}} ({{Variable}}) = **{{assigned_term}}**
{{/each}}

It leaves the following variables open for study-level specification:

{{#each open_qualifier_vars}}
- {{var_nn(Variable)}} ({{Variable}}) — constrained to the
  {{value_list}} codelist.
{{/each}}

It carries these measurement-spec attributes (not SDTM variables, but
DSS-level design decisions that shape the row):

| Attribute | Value |
|---|---|
| Specimen | {{Specimen}} ({{Specimen_NCIt}}) |
| Method | {{Method}} ({{Method_NCIt}}) |
| Result Scale | {{Result_Scale}} |
| Standard Unit | {{Standard_Unit}} |
| Allowed Units | {{Allowed_Units}} |
| LOINC | {{LOINC_Code}}{{#if LOINC_Code_Count>1}} (+{{LOINC_Code_Count-1}} more){{/if}} |
| vlm_source | {{vlm_source}} |
```

Sub-band 3b: sibling summary (emit only if `|siblings| > 0`):

```
Within the **{{BC_Name}}** BC, {{DS_Code}} is one of
{{|siblings|+1}} specialisations. The sibling cards vary by
specimen, method, or result scale:

{{#each siblings}}
- **{{sibling.DS_Code}}** — {{sibling.Specimen}} /
  {{sibling.Method}} / {{sibling.Result_Scale}} /
  {{sibling.Standard_Unit}}.
{{/each}}

The proposition "{{BC_Name}} can be measured under specialisation X"
is what the BC expresses; {{DS_Code}} is one such X.
```

Sub-band 3c: case-specialisation stub (emit only if case-specialisations
exist for this DSS — see Template 04):

```
{{DS_Code}} is refined by {{|case_specs|}} case specialisation(s):
{{#each case_specs}} `{{case_spec_id}}` ({{case_type}}){{/each}}. See
Template 04.
```

### Band 4 — flattened row (Tier 3 DataBook only)

Rendered as a key-value table using `flat-label` text verbatim from
the story CSS. Source: `COSMoS_Graph_Flat.xlsx` row where
`DS_Code = <this DSS>`. Fields in band-4 order:

```
COSMoS_BC_ID, COSMoS_BC_Name / short_name, BC_Name / short_name,
BC_Definition, BC_Scope, BC_Synonyms, BC_Type, COSMoS_Category,
COSMoS_Subcategory, COSMoS_Hierarchy, COSMoS_DSS_Count,
COSMoS_Domains, DS_Code / vlm_group_id, DS_Name / short_name,
Domain, Domain_Class, TESTCD, TESTCD_NCIt, TEST, NCIt_Code,
NCIt_Preferred_Term, NCIt_Definition, NCIt_Synonyms, UMLS_CUI,
NCIm_CUI, Specimen, Specimen_NCIt, Method, Method_NCIt,
Result_Scale, Standard_Unit, Allowed_Units, Decimal_Places,
LOINC_Code, LOINC_Code_Count, Parent_Label, Hierarchy_Path,
Row_Type.
```

Emit one row per field. Empty values render as a muted "—". The
`flat-note` class below the grid carries:

```
Row_Type = {{Row_Type}} — flattened from
`cosmos-bc-dss/interim/COSMoS_Graph_Flat.xlsx`. Round-trip to graph:
`BC.BC_ID = {{COSMoS_BC_ID}}` ∧ `DSS.DS_Code = {{DS_Code}}`.
```

### Band 5 — registry-need band (Tier 3 DataBook only)

For this template, the registry-need argument is the **specimen-test
qualification registry** gap. Emitted as:

```
> ### Registry gap — specimen-test qualification
>
> The COSMoS graph models {{BC_Name}} at the BC level and its
> {{|siblings|+1}} specialisations at the DSS level, but does not
> carry a first-class registry of *which test–specimen–method
> combinations are clinically meaningful*. {{DS_Code}} and its
> siblings are the practical evidence that such combinations exist,
> but the graph represents them only as separate DSS rows, not as
> a qualified proposition.
>
> A registry of shape *(BC, TESTCD, specimen, method, result_scale,
> qualified_by)* would make specimen-test qualification machine-
> actionable. Today this knowledge is distributed across DSS
> attribute columns and sibling structure.
```

## Natural-English substitutions applied

Per the two-tier rule in `00_index.md`. Variable codes expected in
this template:

- Always: `TESTCD`, `--CAT` (e.g. `LBCAT`), the pinned qualifier vars
  per DSS (typically `--METHOD`, `--SPEC`, `--ORRESU`, `--STRESU`,
  `--STNRLO`, `--STNRHI`, `--FAST`).
- Per-domain suffix forms (`LBMETHOD`, `MBMETHOD`, `LBSPEC`, etc.)
  resolve via compositional fallback to the root (`--METHOD`,
  `--SPEC`).

## Traversals required

- `BC → DSSs` via `DSS.Parent_BC_ID = BC.BC_ID` (sibling scope).
- `DSS → Variables` via `Variables.DS_Code = DSS.DS_Code`
  (pinning and openness).
- `Variables → AssignedTerms` via `Variables.assigned_term_id =
  AssignedTerms.term_id` (pinned values).
- `DSS.TESTCD → SDTM_Test_Identity.TESTCD` (NCIt identity of the test).
- `DSS → Case_Specialisations` via
  `Case_Specialisations.parent_dss = DSS.DS_Code` (Template 04 cross-
  link; optional).

No cross-Domain_Class traversal. No instrument parent traversal.
