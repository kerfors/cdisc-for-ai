# Template 04 — Case Specialisation

*Reference stories:*
*`docs/Glucose_StudyIntent_Story.html` (study-intent case, over LB).*
*`docs/XRay_PatientBurden_Story.html` (patient-burden case, over MK/PR).*
*Applies to: any DSS that has one or more case-specialisation registry entries.*

---

## Scope

Case specialisations are **overlay templates**: they refine an
existing DSS with additional pinning, slot narrowing, or contextual
rationale, without introducing a new DSS. The Glucose study-intent
case (FPG vs. 2hPG vs. random) refines `LBGLUCFPG` etc. by naming
the *clinical intent* each variant serves. The X-Ray patient-burden
case refines the IV-contrast MK DSS by naming a burden trade-off
rationale that COSMoS does not currently formalise.

The template is overlay because:

- **No new row template.** The SDTM row is still the row the
  underlying DSS describes.
- **Refinement at the proposition level.** The case adds *why* this
  DSS is chosen over a sibling, or *under what study condition* this
  DSS is preferred.
- **Registry-class citizen.** The case-specialisation registry
  itself is what Template 04 argues for — today these cases live in
  the HTML stories, not in the graph.

Template 04 therefore serves two purposes in the narrative layer:

1. A **cross-link stub** emitted inside Template 01/02/03 paragraphs
   (Band 3c in Templates 01 and 02) pointing at any case
   specialisation that refines the DSS.
2. A **case-specialisation page** in Tier 3 DataBooks, rendering the
   refinement in full.

## Facts the template reads (from the case-specialisation registry)

The registry is not yet a graph sheet. Until it is, the template
reads from a flat registry file proposed as
`sdtm-narrative/reference/case_specialisations.xlsx` (scope decision
deferred to §5). Expected shape:

- **Case row**: `case_spec_id`, `case_type` (study-intent,
  patient-burden, …), `parent_dss` (the DS_Code the case refines),
  `composes_with` (optional list of sibling DSSs the case
  distinguishes against), `case_label`, `case_description`,
  `rationale`, `ext_ref` (link to the study-level CRF / protocol /
  literature that motivates the case).
- **Case pinning** (optional): additional variable → value
  refinements the case layers on top of the parent DSS's pinning.
  Same shape as `Variables` pinned rows.
- **Case-relevant open slots** (optional): names of variables whose
  study-level values carry the case distinction (e.g. `LBFAST` for
  FPG study-intent case).

Also read from the parent DSS (via `Template 01` or `Template 02`
data access, scoped to the parent):

- `DS_Code`, `DS_Name`, the parent DSS's pinned variables and
  attributes — as context for the refinement.

## Prose form emitted

### Band 1 — case opener (always emitted per case)

```
**Case: {{case_label}}** ({{case_spec_id}}) — a {{case_type}}
specialisation of **{{parent_dss.DS_Code}}** ({{parent_dss.DS_Name}}).

{{case_description}}
```

### Band 3 — case body

Sub-band 3a — what the case refines:

```
The parent DSS {{parent_dss.DS_Code}} pins
{{|parent_dss.pinned_vars|}} variables at row-template scope. This
case overlays the following additional refinements:

{{#if case.pinning}}
- Additional pinning:
  {{#each case.pinning}}
  - {{var_nn(Variable)}} ({{Variable}}) = **{{assigned_term}}**
  {{/each}}
{{/if}}

{{#if case.open_slots_relevant}}
- Open slots relevant to the specialisation (not pinned by the
  case, but study-level values carry the case distinction):
  {{#each case.open_slots_relevant}}
  - {{var_nn(Variable)}} ({{Variable}}) — expected values:
    {{expected_value_summary}}
  {{/each}}
{{/if}}
```

Sub-band 3b — what the case distinguishes against (emit only if
`composes_with` is populated):

```
The case {{case_spec_id}} exists to distinguish
{{parent_dss.DS_Code}} from its sibling(s)
{{join(composes_with, ", ")}}. The {{case_type}} rationale is:

> {{rationale}}
```

Sub-band 3c — external reference (emit only if `ext_ref` is populated):

```
External reference: {{ext_ref}}.
```

### Band 5 — registry-need band (Tier 3 DataBook only)

Case-specialisations *are* the registry argument — the Tier 3
DataBook's registry-need band for Template 04 states it directly:

```
> ### Registry gap — case specialisations
>
> COSMoS pins row-template values at DSS level, but study-level
> context — *why* this DSS was chosen for this protocol, *what
> study-intent or burden trade-off it represents* — is not
> represented in the graph. The {{case_type}} case layer is the
> shape of knowledge that would fill the gap.
>
> A registry of shape *(case_spec_id, parent_dss, case_type,
> composes_with, rationale, ext_ref)* would make case knowledge
> machine-actionable. Today it lives in HTML stories and in
> sponsor-local SDRG notes.
```

## Natural-English substitutions applied

Per the two-tier rule. Case-specialisation pinning typically hits
variables the parent DSS leaves open (e.g. `LBFAST` for study-intent,
`PRMKGUID` or equivalent for burden rationale). Most of these are
prefix-composed and resolve via compositional fallback.

## Traversals required

- `Case_Specialisations → DSS` via
  `Case_Specialisations.parent_dss = DSS.DS_Code`.
- `Case_Specialisations → Variables` (for case pinning, if any).
- `Case_Specialisations → AssignedTerms` (for case-pinned values).
- Optional: `Case_Specialisations.composes_with → DSS` for each
  sibling named in the composes_with list.

## Relationship to other templates

Template 04 is **additive**. It runs *after* Template 01 or Template
02 has produced the parent DSS's Tier 2b paragraph. Its output
attaches:

- To Tier 2b: a one-line stub in the parent DSS paragraph (Band 3c
  of Template 01/02), pointing to the case.
- To Tier 3: a full case page in the DataBook, following the parent
  DSS's Band 4.

If a DSS has multiple cases (e.g. Glucose with both study-intent and
a hypothetical fasting-compliance case), each case emits its own
Template 04 rendering independently.

## Open: registry location

The case-specialisation registry file location is an open decision
carried under §5 of the design record (see
`../../docs/COSMoS_Narrative_Layer.md`). Candidates:

- `sdtm-narrative/reference/case_specialisations.xlsx` — exploratory
  home in this track.
- `cosmos-graph/interim/COSMoS_Graph.xlsx` new sheet
  `Case_Specialisations` — promotion target if the case registry
  earns first-class graph status.
- Sponsor-local: the registry may be sponsor-scoped rather than
  standard-scoped, in which case the graph carries only a reference
  to the sponsor file.

Decision deferred until Glucose_StudyIntent and XRay_PatientBurden
Tier 3 DataBooks are built and validated.
