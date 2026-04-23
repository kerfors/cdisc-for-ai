# cosmos-graph — COSMoS as a traversable graph

The graph layer. Turns the CDISC COSMoS export into a multi-sheet graph projection at VLM-row grain, enriches bindings with NCI EVS SDTM CT, and validates against the LinkML schema. Successor to the legacy single-sheet flattener in [`../cosmos-bc-dss/`](../cosmos-bc-dss/), which stays in place for existing consumers until they rewire.

**Current outputs:** `interim/COSMoS_Graph.xlsx` (core, lossless-over-source) and `interim/COSMoS_Graph_CT.xlsx` (NCI EVS enrichment). Both regenerable from CDISC source + LinkML schemas + SDTM CT — no hand-authored content in the core file.

## Design records

- [`docs/COSMoS_Graph.md`](docs/COSMoS_Graph.md) — track reference: what the graph carries, how it is built, the xlsx ↔ LinkML rename table, core vs. overlay pattern.
- [`docs/COSMoS_Open_Work.md`](docs/COSMoS_Open_Work.md) — forward-looking: Branch B consumer rewire, upstream flags, narrative-layer follow-ups, deferred architectural work.
- [`docs/archive/`](docs/archive/) — frozen predecessor docs (Step 1 close, Step 2 scoping, Step 2 as-built, Step 2 → 3 hand-off, 2026-04-23 triage).

## Notebooks

| Notebook | Role | Output |
|---|---|---|
| [`10_flatten_schema_driven.ipynb`](notebooks/10_flatten_schema_driven.ipynb) | Flatten | `interim/COSMoS_Graph.xlsx` |
| [`20_resolve_ct.ipynb`](notebooks/20_resolve_ct.ipynb) | CT resolve | `interim/COSMoS_Graph_CT.xlsx` |
| [`30_validate_graph.ipynb`](notebooks/30_validate_graph.ipynb) | Validate | `reports/graph_validation_report.{md,json}` |

**Flatten** is a SchemaView walk over the CDISC xlsx export (`cosmos-bc-dss/downloads/`), using the LinkML schemas under [`reference/cosmos_linkml/`](reference/cosmos_linkml/) as the class/slot bridge. Produces six sheets: `BC`, `DSS`, `Variables` (VLM-row grain with the reification quad inlined), `Relationships` (reified edges, long format), `Codelists`, plus `ReadMe`.

**CT resolve** joins the core graph's codelist and assigned-term concept IDs against the NCI EVS SDTM CT package. Produces `Codelists`, `CodelistTerms`, `AssignedTerms`, `Unresolved`, `Anomalies` sheets. Kept as a separate file so the core stays lossless-over-source.

**Validate** runs eight checks (referential integrity, schema column coverage, CT resolution fails, enumerated-value integrity, anomaly counts). Emits `graph_validation_report.md` + `.json` under [`reports/`](reports/).

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
```

## Folder conventions

Same as the repo convention in [`../CLAUDE.md`](../CLAUDE.md). One difference from most tracks: this track has **no `downloads/`** — it reads source material from [`../cosmos-bc-dss/downloads/`](../cosmos-bc-dss/downloads/), the extraction track that still owns the CDISC source-ingest concern.

```
cosmos-graph/
├── docs/                   design records (see above)
├── interim/                COSMoS_Graph.xlsx, COSMoS_Graph_CT.xlsx
├── notebooks/              10_flatten, 20_resolve_ct, 30_validate
├── reference/cosmos_linkml/    LinkML schemas (BC, SDTM, CRF)
├── reports/                graph_validation_report.{md,json}, root_subset_fallback_diagnostic.{md,csv}, evs_root_gap_coverage.{md,csv}
└── README.md               this file
```

## Downstream

- [`sdtm-narrative/`](../sdtm-narrative/) — Tier 2b paragraphs and Tier 3 DataBooks, assembled from the graph via a template catalogue.
- [`sdtm-findings/`](../sdtm-findings/) — still reads the legacy `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx` as of 2026-04; rewire to the graph is Branch B in the Step 2 hand-off brief.
