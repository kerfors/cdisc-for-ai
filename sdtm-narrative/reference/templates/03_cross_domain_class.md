# Template 03 — Cross-Domain_Class

*Reference story: `docs/XRay_COSMoS_Story.html`.*
*Applies to: any BC whose DSSs span more than one Domain_Class.*

---

## Scope

One Tier 2b paragraph per DSS as usual — Template 03 does not replace
Templates 01 or 02. It is the **DataBook-level composition rule** for
the Tier 3 case where a single BC binds DSSs across more than one
Domain_Class, and the DataBook must render the cross-class framing.

X-Ray is the prototype: the `CHEST_XRAY` BC binds a procedure-domain
DSS (PRXR01 — the imaging procedure that was performed) and a
finding-domain DSS (MKXR01 — the morphological observation read from
the image). Neither DSS alone describes the clinical event; the
proposition the BC realises requires both.

The template is important because the clinical legibility argument
(Cagle & Shannon) applies here most visibly: a flat triple
representation scatters the observation across two domains with no
explicit link. The BC-as-reification puts the link back.

## Facts the template reads from the graph

- **Parent BC row** — the cross-class BC. Key facts:
  `BC_ID`, `BC_Name`, `BC_Definition`, `BC_Scope`, `COSMoS_Category`,
  `COSMoS_Subcategory`, `COSMoS_Hierarchy`.
- **Member DSS rows** — all DSSs where `Parent_BC_ID = <this BC>`.
  The template expects `n >= 2` and `distinct(DSS.Domain_Class) >= 2`.
  For each DSS:
  - `DS_Code`, `DS_Name`, `short_name`
  - `Domain`, `Domain_Class`, `TESTCD`
  - `vlm_source`, `SDTMIG_since`
  - All attribute columns Template 01 and 02 use.
- **Pinned variables per DSS** (from `Variables` sheet). The
  template reads not just which variables are pinned but which
  variables are pinned in *each* member DSS, to produce the
  cross-class variable-pinning table (band 3c below).
- **Assigned terms** (from `AssignedTerms` sheet) for all pinned
  variable values across member DSSs.
- **Case specialisations** that refine any member DSS (for
  cross-links — see Template 04).

## Prose form emitted

Tier 2b output: each member DSS emits its own paragraph under
Template 01 or Template 02, unchanged. Template 03 adds one extra
sentence to each member DSS's Band 1 opener:

```
 This specialization is one of {{|member_dss|}} DSSs under
{{BC_Name}} that span {{|distinct_domain_class|}} SDTM Domain_Class
values ({{join(distinct_domain_class, ", ")}}); the BC realises the
proposition that these observations belong together.
```

Tier 3 output: a DataBook opens with Band 1 at BC scope, then
iterates member DSSs. Bands below are DataBook-specific.

### Band 1 (BC-scope) — Tier 3 only

```
The **{{BC_Name}}** BC ({{COSMoS_BC_ID}}) realises a single clinical
event — {{BC_Scope}} — that SDTM models across
{{|distinct_domain_class|}} Domain_Class values:
{{#each distinct_domain_class}}
- **{{Domain_Class}}** — captured by
  {{|member_dss_in_class|}} DSS(es):
  {{join(member_dss_codes, ", ")}}.
{{/each}}

Each member DSS is a row template for one slice of the event. The BC
is the reified proposition that these slices belong together.
```

### Band 3c — cross-class pinning table (Tier 3 only)

Added after the per-DSS Band 3a traversals. Renders the member DSSs
side-by-side to expose which variables are pinned in which DSS:

```
| Variable | {{#each member_dss}}{{member_dss.DS_Code}} | {{/each}}
|---|{{#each member_dss}}---|{{/each}}
{{#each pinned_vars_union}}
| {{var_nn(Variable)}} ({{Variable}}) | {{#each member_dss}}{{assigned_term_or_blank(member_dss, Variable)}} | {{/each}}
{{/each}}
```

The **pinned_vars_union** set is the union of pinned variables across
all member DSSs. Cells render the pinned value where present, or a
muted "—" where that DSS does not pin that variable. The intent is
to make visible which axes each member DSS commits to.

Below the table, a short note:

```
Cells left blank mean the variable is either open at study level or
not applicable to that Domain_Class. The BC does not pin values — its
member DSSs do.
```

### Band 4 — flattened rows (Tier 3 only)

Each member DSS renders its own Band-4 grid per Template 01 / 02.
Additionally, a BC-level flattened row (from `Row_Type = COSMoS-BC`
in `COSMoS_Graph_Flat.xlsx`) is rendered first, establishing the
BC as a first-class row.

### Band 5 — registry-need band (Tier 3 only)

For this template, the registry-need argument is **cross-domain
composition**:

```
> ### Registry gap — cross-domain composition
>
> COSMoS binds PR-domain and MK-domain DSSs (and analogues) under
> shared BCs, but does not carry a first-class registry of *which
> cross-domain-class bindings are expected for which clinical
> events*. {{BC_Name}} is the evidence that one event spans two
> domains; there are dozens of others in the catalogue where the
> same pattern holds silently.
>
> A registry of shape *(BC, {Domain_Class: DSS}, event_type,
> composition_rule)* would make the "two rows, one event"
> proposition machine-addressable. Today this knowledge lives in
> the sibling structure of each BC, one BC at a time.
```

## Natural-English substitutions applied

Per the two-tier rule. The cross-class pinning table exercises the
substitution heavily — one DSS pins `PRCAT`, `PRDECOD`, `PRLOC`;
the other pins `MKMETHOD`, `MKTEST`. Both families are prefix-
composed; both resolve via compositional fallback to `--CAT`,
`--DECOD`, `--LOC`, `--METHOD`, `--TEST`.

## Traversals required

- `BC → DSSs` via `DSS.Parent_BC_ID = BC.BC_ID`, grouped by
  `DSS.Domain_Class`.
- `DSS → Variables` per member DSS.
- `Variables → AssignedTerms` per pinned variable.
- `BC → Flat.Row_Type = COSMoS-BC` row for Band 4 BC-level rendering.
- `DSS → Case_Specialisations` (Template 04 cross-link; optional).

No instrument composition ancestry (that is Template 02 territory,
which may still apply to individual member DSSs if one of them is
QS/FT/RS-domain — Template 03 and Template 02 are not mutually
exclusive).

## Relationship to other templates

Template 03 is a **composition** over Templates 01 and 02, not a
replacement. When a BC satisfies the
`distinct(DSS.Domain_Class) >= 2` condition:

- Each member DSS gets a Tier 2b paragraph under Template 01 or 02,
  with the one-sentence cross-class addendum to Band 1.
- The Tier 3 DataBook wraps those per-DSS renderings in the BC-scope
  bands (Band 1 BC-scope, Band 3c cross-class pinning, Band 4 BC
  flat row, Band 5 cross-domain registry-need).
