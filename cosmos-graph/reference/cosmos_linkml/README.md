# COSMoS LinkML snapshot

Three schema files fetched 2026-04-22 from https://github.com/cdisc-org/COSMoS/tree/main/model.

| File | Source path | Purpose |
|---|---|---|
| `cosmos_bc_model.yaml` | `model/cosmos_bc_model.yaml` | LinkML schema for Biomedical Concepts |
| `cosmos_sdtm_model.yaml` | `model/cosmos_sdtm_model.yaml` | LinkML schema for SDTM Dataset Specializations |
| `cosmos_crf_model.yaml` | `model/cosmos_crf_model.yaml` | LinkML schema for CRF Specializations |

Cached locally because `raw.githubusercontent.com` and `api.github.com` are outside the sandbox network-egress allowlist. Tracked in git as part of the `cosmos-graph/` track — the schemas drive the flattener, so they are first-class inputs, not transient reference material.

Read by `cosmos-graph/notebooks/10_flatten_schema_driven.ipynb` (SchemaView
driver) and `cosmos-graph/notebooks/30_validate_graph.ipynb` (schema
column coverage check). Also cited as provenance in
`cosmos-graph/docs/COSMoS_Graph_As_Authored.md`.
