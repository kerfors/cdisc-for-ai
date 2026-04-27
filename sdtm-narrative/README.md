# sdtm-narrative — narrative projections of the COSMoS graph

Tier 2b (per-DSS paragraph) and Tier 3 (DataBook) narrative projections, assembled from a template catalogue over the cosmos-graph projection.

> **Status — early exploratory.** This track was built during the early cosmos-graph work and has not yet been fully revisited since the recent consumer-bases / sdtm-findings-graph alignment. Outputs run end-to-end and read from `cosmos-graph/interim/COSMoS_Graph*.xlsx`, but the template catalogue, narrative grain choices, and case coverage are early-stage. To be revisited and brought into closer alignment with the consumer-bases joined-view pattern.

## What this track produces

- **Tier 2b — per-DSS paragraph.** One paragraph per Dataset Specialization, matching the cosmos-graph `DSS` sheet grain.
- **Tier 3 — DataBooks.** One DataBook per case pair (currently Glucose, 6MWT, X-Ray). Matches the case grain of the HTML case studies in [`docs/`](../docs/) at the repo root.

Outputs live in [`machine_actionable/databooks/`](machine_actionable/databooks/).

## Inputs

- [`cosmos-graph/interim/COSMoS_Graph.xlsx`](../cosmos-graph/interim/COSMoS_Graph.xlsx) — multi-sheet graph projection.
- [`cosmos-graph/interim/COSMoS_Graph_CT.xlsx`](../cosmos-graph/interim/COSMoS_Graph_CT.xlsx) — CT enrichment.

The track reads the graph directly — it does **not** read the legacy `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx`. It also does not currently read `consumer-bases/DSS_View.xlsx`; whether to rewire onto the joined view is part of the alignment work to revisit.

## Design records

- [`docs/COSMoS_Narrative_Layer.md`](docs/COSMoS_Narrative_Layer.md) — design decisions for the narrative grain, template catalogue, and build order.
- [`docs/COSMoS_Open_Work.md`](docs/COSMoS_Open_Work.md) — forward-looking items.
- [`docs/archive/`](docs/archive/) — frozen predecessor docs.

## Cross-references

- [`cosmos-graph/`](../cosmos-graph/) — upstream graph track that the narrative reads from.
- [`docs/6MWT_NCIt_Story.html`](../docs/6MWT_NCIt_Story.html), [`docs/6MWT_COSMoS_Story.html`](../docs/6MWT_COSMoS_Story.html), [`docs/Glucose_COSMoS_Story.html`](../docs/Glucose_COSMoS_Story.html) — visual case studies, template ground truth for the DataBook layer.

## Alignment work to revisit

- Whether the Tier 2b grain stays at per-DSS paragraph or shifts to consume `consumer-bases/DSS_View.xlsx` directly.
- Template catalogue revision against the graph-fed consumer column shapes.
- Case coverage beyond Glucose / 6MWT / X-Ray.
- Header colour convention and naming alignment with the cosmos-graph + consumer track conventions.
