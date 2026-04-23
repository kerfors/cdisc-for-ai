# cosmos-graph — COSMoS as a traversable graph

The graph layer. Turns the CDISC COSMoS export into a multi-sheet graph projection at VLM-row grain, enriches bindings with NCI EVS SDTM CT, validates against the LinkML schema, and offers a query cookbook. Successor to the legacy single-sheet flattener in [`../cosmos-bc-dss/`](../cosmos-bc-dss/), which stays in place for existing consumers until they rewire.

**Current outputs:** `interim/COSMoS_Graph.xlsx` (core, lossless-over-source) and `interim/COSMoS_Graph_CT.xlsx` (NCI EVS enrichment). Both regenerable from CDISC source + LinkML schemas + SDTM CT — no hand-authored content in the core file.

## Design records

- [`docs/COSMoS_Graph_As_Authored.md`](docs/COSMoS_Graph_As_Authored.md) — Step 1 close. The inherent graph model in the CDISC COSMoS source, made explicit.
- [`docs/COSMoS_Flattener_Rewrite.md`](docs/COSMoS_Flattener_Rewrite.md) — Step 2 design. SchemaView-driven flatten, core-vs-enrichment file split.
- [`docs/COSMoS_Graph_Upstream_Additions.md`](docs/COSMoS_Graph_Upstream_Additions.md) — current wave. Six upstream additions surfaced from the narrative track, sequenced in §6.
- [`docs/COSMoS_Next_Steps_Brief.md`](docs/COSMoS_Next_Steps_Brief.md) — Step 2 → Step 3 hand-off. Branches A (narrative, executing in `sdtm-narrative/`), B (consumer rewire), C (upstream flags to CDISC).
- [`docs/COSMoS_Step2_Scoping_Brief.md`](docs/COSMoS_Step2_Scoping_Brief.md) — frozen pre-build brief that motivated the Step 2 rework.

## Notebooks

| Notebook | Role | Output |
|---|---|---|
| [`10_flatten_schema_driven.ipynb`](notebooks/10_flatten_schema_driven.ipynb) | Flatten | `interim/COSMoS_Graph.xlsx` |
| [`20_resolve_ct.ipynb`](notebooks/20_resolve_ct.ipynb) | CT resolve | `interim/COSMoS_Graph_CT.xlsx` |
| [`30_validate_graph.ipynb`](notebooks/30_validate_graph.ipynb) | Validate | `reports/graph_validation_report.{md,json}` |
| [`50_query_examples.ipynb`](notebooks/50_query_examples.ipynb) | Query cookbook | no file — eight worked queries pinned to the story-pair DSSs |

**Flatten** is a SchemaView walk over the CDISC xlsx export (`cosmos-bc-dss/downloads/`), using the LinkML schemas under [`reference/cosmos_linkml/`](reference/cosmos_linkml/) as the class/slot bridge. Produces six sheets: `BC`, `DSS`, `Variables` (VLM-row grain with the reification quad inlined), `Relationships` (reified edges, long format), `Codelists`, plus `ReadMe`.

**CT resolve** joins the core graph's codelist and assigned-term concept IDs against the NCI EVS SDTM CT package. Produces `Codelists`, `CodelistTerms`, `AssignedTerms`, `Unresolved`, `Anomalies` sheets. Kept as a separate file so the core stays lossless-over-source.

**Validate** runs eight checks (referential integrity, schema column coverage, CT resolution fails, enumerated-value integrity, anomaly counts). Emits `graph_validation_report.md` + `.json` under [`reports/`](reports/).

**Query cookbook** is read-only — eight worked queries exercising the graph shape against the story-pair DSSs (GLUCPL, SIXMW101, SGBESCR + X-Ray cross-domain).

## Data flow

```
cosmos-bc-dss/downloads/  (CDISC BC + DSS xlsx, SDTM_Terminology.txt)
        │
        │  cosmos-graph/reference/cosmos_linkml/*.yaml  (SchemaView)
        ▼
notebook 10 ──► cosmos-graph/interim/COSMoS_Graph.xlsx       (core)
                      │
notebook 20 ──► cosmos-graph/interim/COSMoS_Graph_CT.xlsx    (NCI EVS enrichment)
                      │
notebook 30 ──► cosmos-graph/reports/graph_validation_report.{md,json}
                      │
notebook 50 ──► query examples (no output file)
```

## Folder conventions

Same as the repo convention in [`../CLAUDE.md`](../CLAUDE.md). One difference from most tracks: this track has **no `downloads/`** — it reads source material from [`../cosmos-bc-dss/downloads/`](../cosmos-bc-dss/downloads/), the extraction track that still owns the CDISC source-ingest concern.

```
cosmos-graph/
├── docs/                   design records (see above)
├── interim/                COSMoS_Graph.xlsx, COSMoS_Graph_CT.xlsx
├── notebooks/              10_flatten, 20_resolve_ct, 30_validate, 50_query_examples
├── reference/cosmos_linkml/    LinkML schemas (BC, SDTM, CRF)
├── reports/                graph_validation_report.{md,json}, flattener_rewrite_audit.md
└── README.md               this file
```

## Downstream

- [`sdtm-narrative/`](../sdtm-narrative/) — Tier 2b paragraphs and Tier 3 DataBooks, assembled from the graph via a template catalogue.
- [`sdtm-findings/`](../sdtm-findings/) — still reads the legacy `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx` as of 2026-04; rewire to the graph is Branch B in the Step 2 hand-off brief.
