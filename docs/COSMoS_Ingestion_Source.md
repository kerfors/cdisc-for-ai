# COSMoS ingestion source — Excel vs LinkML/API

**v2, 2026-08-05.** Supersedes v1. v1 recommended switching `cosmos-graph`
ingestion from the published Excel to the COSMoS LinkML YAML; a source-availability
correction plus an access test have since **reversed that recommendation on fact**.
This version states the settled conclusion and carries the finding across to the
usdm-rdf → COSMoS bridge (the join named at the end of the third #usdmrdf article).
It covers **both COSMoS layers** — Biomedical Concepts (identity) and Dataset
Specializations (the measurement specification) — because the join a study designer
actually needs lands at the DSS, not the BC.

Reference package: COSMoS BC/DSS **Package 18 (2026-07-14)** — 1,475 BCs, 1,475 DSSs.
`cdisc-for-ai` currently pins 2026-05-26 (r17). Schemas vendored in
`cosmos-graph/reference/cosmos_linkml/`.

## One-line answer

Keep ingesting the public cumulative Excel/CSV. The richer (nested) route runs into
a **CDISC membership wall, proven by test**, not a technical one — and staying on the
Excel loses no analytical content, because notebook 10 already reconstructs the only
two things the flattening drops.

## 1. The source chain

```
curation spreadsheets  ──convert_*_xlsx2yaml.sas──▶  YAML instances (validated: linkml-validate)
                                                          │
                            ┌─────────────────────────────┼───────────────────────────────┐
                            ▼                             ▼                                 ▼
              export/*.xlsx + *.csv            gen-json-schema → *.json            CDISC Library API (v2, JSON)
              (cumulative, FLAT, public)       (JSON Schema, public)               (cumulative, NESTED, gated)
```

The Excel you download is a **generated, lossy flattening** of the canonical nested
form (`create_cosmos_sdtm_excel.py` reads the YAML dir *or* the API and writes
xlsx/csv). Correction to a prior belief: `gen-json-schema` / `linkml-validate` ship
in the repo (`validate_yaml.py`, the `*_generate.cmd` scripts) and run in curation,
but there is **no GitHub Actions gate in `main`** running them on publish.

## 2. What the Excel loses — and why it doesn't bite

`create_cosmos_sdtm_excel.py`, read against a nested instance:

| Aspect | YAML instance | Excel export | Bites? |
|---|---|---|---|
| Concept boundary | one nested object per DSS | N rows keyed by `(domain, vlm_group_id)` | No — notebook 10 rebuilds it by dedup |
| Variable order | inherent list order | computed as `v_order`, then **dropped** | No — but only because file row order is preserved; it is not a field |
| `valueList`, `categories`, `synonyms` | lists | `;`-joined strings | No — re-split on read |
| `subsetCodelist` (when an object) | `SubsetCodeList` + `codelistTerm[…]` | `str(dict)` | Latent — current instances author it as a plain string (`NY_NY`), so no live loss |
| `codelist.href` | present | dropped (C-code kept) | No — derivable |

Net: the Excel is a flat *view*; the YAML is the lossless *model instance*. This is
your own repo's "flat files are views, not the architecture" thesis one layer up —
but the losses are cosmetic for the current pipeline.

The flattening does **more work at the DSS layer than at the BC layer**, because the
DSS is the deeply nested object: a required, ordered `variables` list, with a
per-variable reification quad (`RelationShip`) and optional `SubsetCodeList` /
`CodeListTerm` nesting. The VLM-row-grain export carries the fields but collapses the
structure — variable order becomes row order, the `SDTMGroup` boundary becomes a
`ds_id` group, the quad becomes four columns. Notebook 10 rebuilds all of it
(`DSS`, `Variables`, `Relationships` sheets), so it is recovered — but the DSS is
where "view, not model" is most true.

## 3. The correction that killed the YAML swap

v1 said "point notebook 10 at `yaml/20260526_r17/{bc,sdtm}`." That is **wrong**: the
per-package `yaml/<pkg>/` folders in the COSMoS repo are **per-package deltas, not
cumulative snapshots**. Evidence:

- 6MWT `C115805` appears only in r12's folder, not r17 or r18.
- Per-package BC counts swing (581, 182, 258, 46, 249, 87, 156) — not converging to 1,475.
- Distinct SDTM filenames across all packages total **1,880** > the 1,475 cumulative
  "latest" (names churn; concepts get renamed/retired across versions).

So the cumulative standard is **not** reconstructable from any single YAML folder, and
assembling deltas with last-writer-wins is fragile (the 1,880-vs-1,475 churn).
**COSMoS publishes no public cumulative *nested* artifact** — only public flat
(`export/*.csv|xlsx`), public nested *deltas* (`yaml/<pkg>/`), and the gated nested
API.

## 4. The access test — settled fact

The remaining question was purely "does your key reach the cumulative nested API." An
auth-probe notebook run with your own key settled it:

- Header `api-key` is correct; **your key is valid** (recognized, not rejected).
- `GET /api/mdr/products` under `api-key` returns **401**, body:
  `{"message":"Members-only content. Visit https://www.cdisc.org/membership/rates-benefits ..."}`
  — a **membership** gate, not an invalid-key error.
- `Ocp-Apim-Subscription-Key` returns "missing subscription key" (wrong header; ignore).

Conclusion, on evidence: your tier is **non-member**; the entire Library API (general
MDR *and* COSMoS) is behind CDISC membership for your key. The nested/cumulative API
route is **closed to you**. The COSMoS *content* remains openly licensed on GitHub —
only the API's cumulative-nested *delivery* is paywalled.

## 5. Decision

Keep the Excel/CSV ingest. One free robustness tweak available without any access
change: read the public `export/cdisc_*_latest.csv` rather than the downloaded
`.xlsx` — same cumulative content, cleaner parsing, and it is the artifact CDISC
generates first. The LinkML **schema** stays valuable as your column and validation
authority regardless of tier (which half of "schema-driven" you already use).

## 6. Carry-over to usdm-rdf: the COSMoS join is asymmetric with USDM

The third #usdmrdf article's thesis — *the identifiers, and then the constraints, were
already published; read them as data, don't regenerate them* — rests on a property
USDM has that **COSMoS does not**: USDM ships **one cumulative, self-describing
`dataStructure.yml`** (plus `USDM_CT.xlsx`), which `usdm-rdf` reads directly and even
generates 80 structural SHACL shapes / 619 property constraints from, with nothing to
hand-author on the structural side. That is why the USDM lift is "mechanical."

For the join the article names next — USDM `Activity.biomedicalConceptId` → COSMoS BC,
"protocol to dataset, no mapping table in between" — the COSMoS side does **not** offer
the same affordance, and this is a real design input, not a blocker:

**Symmetric (both public as data):** the *constraint/model* layer, for BC **and** DSS.
USDM publishes its cardinality in `dataStructure.yml`; COSMoS publishes its BC
constraints in `cosmos_bc_model.yaml` and — more richly — its DSS constraints in
`cosmos_sdtm_model.yaml`. The BC model gives required slots, the `conceptId` pattern
`^(C[0-9]+|NEW_[A-Z_]*[0-9]*)$`, and the `resultScales`/`dataType` enums. The **DSS
model publishes considerably more**: a required, ordered `variables` cardinality;
identifier patterns on `datasetSpecializationId` and variable `name`; codelist
`conceptId` patterns; and, notably, the **reification vocabulary itself as controlled
enums** — `PredicateTermEnum` (~40 predicates), `LinkingPhraseEnum` (~100 phrases) —
plus the Define-XML origin terminology carried with NCIt meanings (`OriginType` →
NCIT:C170449, `OriginSource` → NCIT:C170450), `RoleEnum`, `ComparatorEnum`. LinkML can
emit SHACL (`gen-shacl`) or JSON Schema from either model exactly as usdm-rdf emits
SHACL from the USDM YAML. So "the constraints were already published" **transfers to
COSMoS, and transfers *more strongly* at the DSS layer** — the relationship semantics a
reviewer would otherwise hand-author are a published controlled vocabulary.

**Asymmetric (instance delivery):** the cumulative *instance* set, for both layers.
USDM's instances (the model itself, and a study's data) are cumulative and public.
COSMoS's cumulative BC and DSS instances are public **only in flat form**
(`export/*.csv|xlsx`); the nested form is either **per-package deltas** (public) or the
**gated API** (member-only). So a graph built from the USDM side "reads the published
nested data," but the COSMoS side must be **assembled from the public flat export** —
there is no cumulative nested COSMoS file to read the way `dataStructure.yml` is read.

**The join granularity — the load-bearing finding for the bridge.** USDM
`Activity.biomedicalConceptId` resolves to a **BC** (a C-code). But the measurement
specification — specimen, method, units, LOINC, the CRF-row template — lives at the
**DSS**, not the BC, and the two do not stand in a 1:1 relation:

- One BC fans out to many DSSs. In r17, 76 of 754 BCs carry more than one DSS, with a
  maximum fan-out of **92:1** (`C181398`, allergen-specific IgE — the "IS by target
  antigen" pattern from the behavioural analysis). Immunogenicity and genomics fan out
  similarly.
- The DSS has **no stable machine identifier**. `datasetSpecializationId` is declared
  `identifier: true` in the schema, but its pattern (`^[A-Z][A-Z0-9_]*$`) only enforces
  an uppercase mnemonic (`ALBCREATURIN`, `GLUCSER`) — not a resolvable C-code, and not
  unique across domains. This is the DS_Code identity gap from the repo's key findings.

So the article's "protocol to dataset, no mapping table in between" is exact for
**protocol → BC** — a resolvable-identifier join, both ends carrying a C-code, no
mapping table. It does **not** hold for **protocol → DSS**: that is not an edge but a
path, `protocol → BC → {DSS…}`, and at the fan-out the protocol reference alone cannot
say *which* DSS (which specimen, method, or result scale). That selection is not in
USDM — it is a COSMoS-side choice a study designer makes — and there is no stable DSS
identifier to record the choice against. The DSS-identity open question is therefore
not a COSMoS-internal detail; it is the **precise gap** a USDM-anchored graph exposes
the moment it tries to reach the measurement-specification layer.

Practical guidance for the bridge work: **source COSMoS from the public GitHub
artifacts, never the API** — a member-gated dependency would make the pipeline
non-reproducible for any non-member (the exact wall hit here). Use `export/*.csv` for
the cumulative BC and DSS sets; if a nested shape is needed, un-flatten it from the CSV
(the §2 losses are recoverable). The `biomedicalConceptId` / `bc_id` join key is
present on both sides in the public flat exports, so the protocol → BC edge needs no
API. Build the BC → DSS hop as an explicit, one-to-many edge in the graph, and treat
"which DSS" as a modelled selection, not a lookup — because the standard does not yet
give it a resolvable name.

## 7. Summary

The question was never Excel-vs-YAML as a parsing choice; it was whether the cumulative
nested COSMoS form is reachable. It is not, for a non-member — proven, not inferred.
Keep the Excel/CSV for `cosmos-graph`. Carry three facts into usdm-rdf:

1. COSMoS's **constraints** are public as LinkML for both layers and can be turned into
   SHACL/JSON Schema the same way USDM's are — and the DSS model publishes *more* than
   the BC model (the reification predicates, linking phrases, and Define-XML origin
   terminology as controlled enums). The "constraints as data" story extends, and
   extends further at the DSS.
2. COSMoS's cumulative **instances** (BC and DSS) are public only as flat exports, so
   the COSMoS half of any USDM-anchored graph must be built from `export/*.csv`, not
   the gated API.
3. The **join stops cleanly at the BC**. `protocol → BC` is a resolvable-identifier
   edge with no mapping table; `protocol → DSS` is a one-to-many path with no stable
   identifier on the DSS side. Reaching the measurement-specification layer surfaces
   the DSS-identity gap as the real design problem — not a parsing problem.
