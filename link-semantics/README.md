# link-semantics — what kind of link is it?

`link-semantics/` measures the links to NCIt and LOINC codes in the
`cdisc-for-ai` reference files and asks, for each of them: what statement does
this link actually make?

## Why

In RDF, `skos:exactMatch` is the natural default for "this thing relates to
that NCIt concept". The published content makes several different statements
with the same C-code. A test code *is* a concept. A term is a *member* of a
codelist. A variable is *bound* to a codelist, *pinned* to one value, or
restricted to a *list* of values. Only a small share of the links are mappings
between terminologies.

This matters when graphs are merged. `skos:exactMatch` is transitive, so two
subjects sharing one C-code become equivalent to each other. Nothing in the
sources asserts that. One predicate per link kind has to be decided before the
content is rendered as RDF.

None of the link kinds is declared in the CDISC models. They are inferred from
how each column behaves. This is the same line of work as
[`COSMoS_Behavioural_Analysis.md`](../docs/archive/behavioural-analysis-2026-03/COSMoS_Behavioural_Analysis.md) (March 2026, archived):
behaviour that the published content exhibits but the schema does not state.

## Link kinds and provenance classes

| Link kind | Statement | Mapping? |
|---|---|---|
| `identity` | this thing **is** that NCIt concept (the C-code is its identifier) | no |
| `membership` | this concept is a permissible value in that codelist | no |
| `binding` | this variable draws its values from that codelist | no |
| `denotation` | this model element **means** that concept | no |
| `pinned_value` | this variable is fixed to that value in this specialization | no |
| `value_list` | this variable is restricted to these values in this specialization | no |
| `category_tag` | this BC carries that category token - the object end is a label, not an identifier | no |
| `mapping` | this concept corresponds to a concept in another terminology | yes |

| Provenance class | Meaning | Needs a justification? |
|---|---|---|
| `published` | CDISC / NCI EVS asserts it in a release | no - record the release |
| `derived` | computed by a rule from published inputs | record the rule and the inputs |
| `curated` | a judgement | yes |

The assignment of link kind and provenance class to each source column is
authored. It lives in one `INVENTORY` list in `Link_Kind_Audit.ipynb`, and that
is the part to review. All counts are measured.

## Scope discipline

**In scope.** Measure what the published content exhibits. Every number in the
track's documentation has a cell in one of the two notebooks.

**Out of scope.** Choosing predicates, and any change to `cosmos-rdf` or
`usdm-rdf`. Those decisions are taken in the RDF repositories, with this track
as evidence. No reading is attached to a measurement here.

## Notebooks and outputs

| Notebook | Question | Output |
|---|---|---|
| [`Link_Kind_Audit.ipynb`](notebooks/Link_Kind_Audit.ipynb) | Which link kinds and provenance classes are there, and how many rows are behind each? Also: assignment states per variable suffix, LOINC at two grains, category token resolution. | [`Link_Kind_Audit.xlsx`](interim/Link_Kind_Audit.xlsx) |
| [`Code_Collision_Check.ipynb`](notebooks/Code_Collision_Check.ipynb) | Which C-codes are used in more than one role, or more than once within a role? Where would a transitive predicate bite? Includes the overlap with the USDM anchors in `usdm-rdf`. | [`Code_Collision_Check.xlsx`](interim/Code_Collision_Check.xlsx) |

Each workbook has a `Pins` sheet: the `cdisc-for-ai` commit, the COSMoS package
date, the generation dates of the input workbooks and, for the collision check,
the `usdm-rdf` commit and `owl:versionInfo`. The counts are package-bound. A
change between packages is a finding, not a failure, so there is no validation
baseline for this track.

The category resolution in the audit is a copy of the mechanism in
`cosmos-graph/notebooks/50_instrument_category_resolution.ipynb` (exact name,
then unique lower-cased synonym), applied to all domains.

## Inputs

```
cosmos-graph/interim/COSMoS_Graph.xlsx ──────────────────────────┐
cosmos-graph/interim/COSMoS_Graph_CT.xlsx ───────────────────────┤
sdtm-test-codes/machine_actionable/SDTM_Test_Identity.xlsx ──────┤
sdtm-test-codes/machine_actionable/SDTM_Instrument_Identity.xlsx ┼──→ link-semantics/
sdtm-test-codes/interim/Codelist_Cross_References.xlsx ──────────┤
../usdm-rdf/usdm_v4.ttl (collision check only) ──────────────────┘
```

Reads only repo artefacts, plus `usdm_v4.ttl` from a git checkout of
[`kerfors/usdm-rdf`](https://github.com/kerfors/usdm-rdf) beside this
repository. Nothing in the repo reads from this track.

## Running

Run from `link-semantics/notebooks/`. The repo root is resolved two levels up.
`Code_Collision_Check.ipynb` needs `rdflib`, and fails at the first cell if the
`usdm-rdf` checkout is not there.

## Folder conventions

- `notebooks/` — the two notebooks.
- `interim/` — their workbooks. Named `interim/` because they are evidence for
  the document, not deliverables. Same precedent as `cosmos-graph/interim/`.
- `docs/` — [`Link_Semantics.md`](docs/Link_Semantics.md), the durable output
  of the track: the link kinds, the provenance classes and the evidence for
  each. Narrative first, then a dated snapshot with the counts.

Folders not present: `downloads/` (reads only repo artefacts and `usdm-rdf`),
`machine_actionable/` (no consumer file is produced).

## Cross-references

- [`COSMoS_Behavioural_Analysis.md`](../docs/archive/behavioural-analysis-2026-03/COSMoS_Behavioural_Analysis.md) — the behavioural analysis this track continues (March 2026, archived).
- [`Identity_Needs_by_Behavioural_Group.md`](../docs/archive/behavioural-analysis-2026-03/Identity_Needs_by_Behavioural_Group.md) — identity patterns per behavioural group (March 2026, archived).
- [`kerfors/cosmos-rdf`](https://github.com/kerfors/cosmos-rdf) and [`kerfors/usdm-rdf`](https://github.com/kerfors/usdm-rdf) — where predicates are chosen.
- Repo-root `CLAUDE.md` — repo conventions.
