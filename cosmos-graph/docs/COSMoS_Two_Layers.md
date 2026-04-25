# Two Layers Over COSMoS Data

*How cdisc-for-ai works on the COSMoS publication: a layered approach from
authored content to consumer-shaped views. Provisional home — may move once
the consumer-rewire work lands.*

*cdisc-for-ai, package 2026-Q1.*

---

CDISC publishes COSMoS as an authored graph: Biomedical Concepts (clinical
concepts with NCIt anchors), Dataset Specializations (CRF row templates pinned
to SDTM variables), and the relationships between them. The cdisc-for-ai repo
works on this content in two layers. Neither layer adds editorial judgment —
that stays in the consumer.

## Layer 1: `cosmos-graph/` — make the authored graph queryable

Read the COSMoS Excel export. Use the published LinkML schema to drive a
multi-sheet flatten — when CDISC adds a slot, we pick it up automatically.
Output is two workbooks:

- **`COSMoS_Graph.xlsx`** (11 sheets) — lossless over source. Every BC, every
  DSS, every SDTMVariable pin, every reified relationship edge, every
  BC-to-Category and BC-to-BC-parent edge. Same content as source, restructured
  so it can be queried as tables instead of parsed as YAML.
- **`COSMoS_Graph_CT.xlsx`** (5 sheets) — joins each codelist binding and each
  pinned NCIt concept with NCI EVS SDTM CT, so each resolves to a definition
  and preferred term.

Two files because the core stays version-independent; the CT layer depends on
the EVS package version. Source data anomalies (e.g. LOINC `system` URI
inconsistency in the BC `Coding` list) are projected verbatim and recorded in
[`COSMoS_Graph.md`](COSMoS_Graph.md).

## Layer 2: `consumer-bases/` — turn the queryable graph into consumer-shaped views

Layer 2 turns the normalised graph into denormalised, consumer-shaped views.
Every consumer would otherwise repeat the same joins (DSS → BC for context,
BC → `Coding` for LOINC, `Variables` → `AssignedTerms` for NCIt resolution)
and the same pivot (`Variables` long form → one row per DSS with pinned
attributes wide). `consumer-bases/` does that work once.

First output: **`DSS_View.xlsx`** with two sheets:

- **`Test_Identity`** — one row per TESTCD that COSMoS pins. NCIt enrichment
  from both the graph CT layer (graph-native definitions and preferred terms)
  and the cdisc-for-ai reference track (synonyms, UMLS_CUI, NCIm_CUI, full
  domain membership). Conflicts between the two are flagged, not resolved.
- **`Measurement_Specs`** — one row per DSS. DSS identity + BC identity joined
  in; external codings (LOINC, …) pivoted from the BC `Coding` sheet; every
  `Variables` pin (specimen, method, units, location, laterality, …) pivoted
  with the leading domain code stripped, so `_SPEC_value` carries the LB
  specimen for LB DSSs and the MB specimen for MB DSSs.

Same scope discipline as Layer 1: no sub-typing, no behavioural classification,
no narrative framing. Those belong to the consumer track.

## The boundary

| | `cosmos-graph/` (Layer 1) | `consumer-bases/` (Layer 2) |
|---|---|---|
| In | CDISC COSMoS Excel export, LinkML schemas, NCI EVS SDTM CT | `COSMoS_Graph*.xlsx`, repo reference tracks |
| Out | `COSMoS_Graph.xlsx` + `COSMoS_Graph_CT.xlsx` | `DSS_View.xlsx` |
| Operation | Restructure: YAML/Excel → queryable tables | Join + pivot: long form → wide; pinned attributes assembled |
| Adds | NCIt resolution from EVS CT (in CT workbook) | Cross-track NCIt enrichment; BC/DSS join; Variables pin pivot |
| What stays out | Editorial content of any kind | Sub-typing, behavioural classification, narrative framing |

**Layer 1 turns authored content into queryable form. Layer 2 turns queryable
form into consumable form.** The consumer adds the editorial judgment.
