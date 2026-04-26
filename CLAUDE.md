# CLAUDE.md — Project instructions for Claude

This file is read automatically at the start of every Claude session (Cowork or Claude Code).

## Project

**cdisc-for-ai** — Machine-actionable reference files for CDISC clinical data standards.

Makes explicit the linkages between SDTM Controlled Terminology, NCIt concepts, COSMoS Biomedical Concepts, and Dataset Specializations. Outputs are flat Excel files designed for both human review and AI/tool consumption. The long-term goal is a traversable graph; flat files are today's delivery format.

Owner: Kerstin Forsberg — information architect, 25 years in clinical data/metadata, deep CDISC domain expertise, architectural thinker but not a developer.

Repository: https://github.com/kerfors/cdisc-for-ai

## Reference versions

- SDTM CT: NCI EVS package **2026-03-27**
- COSMoS BC/DSS: package **2026-Q1**
- SDTMIG: **v3.4** / SDTM v2.0

## Architecture — how tracks relate

The repo has five track types. The domain code is the join key across all tracks.

**Source tracks** extract and enrich from upstream standards:
- `sdtm-test-codes/` — "What is measured?" Extracts TESTCD/TEST from NCI EVS, enriches with NCIt identity (definitions, synonyms, C-codes, UMLS/LOINC mappings). Outputs: `SDTM_Test_Identity.xlsx` (domain-level test codes), `SDTM_Instrument_Test_Identity.xlsx` (test codes within an instrument codelist), `SDTM_Instrument_Identity.xlsx` (one row per instrument codelist, dual NCIt anchors from C20993 + C211913).
- `cosmos-bc-dss/` — "How is it measured? (extraction)" Owns the COSMoS source-ingest and legacy single-sheet flatten. Output: `COSMoS_BC_DSS.xlsx` (interim). Also carries the early behavioural/content analyses.

**Graph track** provides the traversable COSMoS projection:
- `cosmos-graph/` — SchemaView-driven multi-sheet graph over the CDISC COSMoS export, plus NCI EVS SDTM CT enrichment. Outputs: `interim/COSMoS_Graph.xlsx` (core, lossless-over-source), `interim/COSMoS_Graph_CT.xlsx` (CT enrichment). Reads source material from `cosmos-bc-dss/downloads/`. LinkML schemas live here at `reference/cosmos_linkml/`.

**View track** provides denormalised joined projections over the graph for consumer use:
- `consumer-bases/` — Joined views over `cosmos-graph/` and repo reference metadata, shaped for consumer use but not yet final consumer shape. Output: `interim/DSS_View.xlsx` (Test_Identity + Measurement_Specs sheets, graph-wide across all 32 domains). Consumers apply observation-class scoping, sub-typing, behavioural classification, and narrative framing themselves.

**Reference track** provides shared domain metadata:
- `sdtm-domain-reference/` — Domain-level classification: structural types, COSMoS coverage flags, specimen/instrument classification. Output: `SDTM_Domain_Metadata.xlsx`. Pipeline input to consumer tracks.

**Consumer tracks** join source/graph data into structural-type-specific outputs:
- `sdtm-findings/` — Three sub-types: Specimen-based (LB, MB, MI, CP, BS, MS, PC, PP), Measurement (VS, MK, CV), Instrument (QS, FT, RS). Each output is a two-sheet workbook: Test_Identity (one row per TESTCD) + Measurement_Specs (one row per DSS). Join key between sheets: TESTCD. Still reads the legacy `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx` as of 2026-04; superseded by `sdtm-findings-graph/` (parallel during transition).
- `sdtm-findings-graph/` — Graph-fed successor to `sdtm-findings/`. All three sub-types built. Specimen and measurement use the two-sheet pattern (Test_Identity + Measurement_Specs); instrument adds two more sheets (BC_Categories + BC_Parents) to handle the parallel BC chains and the search-tag mechanism. Fresh column shape designed against `consumer-bases/DSS_View.xlsx`. Runs parallel to the legacy until retirement.
- `sdtm-narrative/` — Tier 2b (per-DSS paragraph) and Tier 3 (DataBook) narrative projections of the graph, assembled from a template catalogue over `cosmos-graph/interim/COSMoS_Graph*.xlsx`.

See `SDTM_Domain_Overview.md` (repo root) for the full three-layer analytical model. See `docs/Changes_2026-03.md` for what changed in the latest release.

## Data flow and joins

```
sdtm-test-codes/SDTM_Test_Identity.xlsx ─────────┐
sdtm-domain-reference/SDTM_Domain_Metadata.xlsx ─┤
cosmos-graph/interim/COSMoS_Graph*.xlsx ─────────┤
                                       │         │
                                       │         ▼
                                       │   consumer-bases/interim/DSS_View.xlsx
                                       │                 │
                                       │                 └──→ sdtm-findings-graph
                                       │
                                       └──→ sdtm-narrative
```

The legacy `sdtm-findings/` consumer reads `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx`
instead of the graph projection; it runs in parallel with `sdtm-findings-graph/`
until the latter has all three sub-types.

## Folder conventions

Each track follows a consistent structure:
- `downloads/` — External source files. Re-downloadable by notebooks. **Gitignored.** Never modify.
- `interim/` — Pipeline artifacts. Generated by notebooks. Visible because useful standalone.
- `machine_actionable/` — Final outputs. The deliverables.
- `notebooks/` — Jupyter notebooks that produce interim and final outputs. The processing logic.
- `reports/` — QC and analysis reports. Generated by notebooks.
- `docs/` — Human-readable analysis and documentation.
- `pre-2026-03/` — Baseline snapshots from before the March 2026 update.
- `diffs/` — CSV diffs between pre-2026-03 and current versions.

## Workflow rules

1. **Never modify `downloads/` files.** They are external source data, re-downloaded by notebooks.
2. **Never modify `pre-2026-03/` files.** They are frozen baselines.
3. **Notebooks are the processing logic.** Changes to output files should come from notebook changes, not direct edits to xlsx/csv.
4. **Diff before committing.** When updating outputs, generate diff CSVs so changes are reviewable.
5. **README sheets.** Every machine_actionable xlsx has a README sheet documenting columns, provenance, and design decisions. Keep it current.

## Data integrity — critical

- **NEVER fabricate, simulate, or generate example data.** All data comes from actual CT, COSMoS, NCIt, or EVS content.
- **If real data is unavailable, state clearly and stop.** Do not produce plausible examples.
- **Flag ambiguities** rather than making assumptions about classification or mapping.
- **Preserve hierarchical relationships** exactly as they exist in the source standards.

## Code conventions

- Python / Pandas preferred
- 4-space indentation, always
- Complete, copy/paste-ready code — no placeholders
- Clean, assumptive code — fail fast with clear errors
- No defensive programming or silent auto-fixes

## Notebook conventions

- Notebooks are `.ipynb` files, opened and run in VSCode
- Always generate using Python's `json` module (never raw JSON text)
- Build cells as Python dicts with helper functions for `markdown_cell()` and `code_cell()`
- Use `json.dump(notebook, file, indent=1, ensure_ascii=False)`
- Each cell's `"source"` field must be a list of strings ending with `\n`
- Include clear markdown documentation cells explaining purpose and decisions
- Test that generated notebooks open in Jupyter immediately after creation

## Code modification rules

- When asked to fix/change ONE thing, modify ONLY that thing
- NEVER rewrite entire functions unless explicitly told to
- NEVER "clean up", "simplify", or "improve" unrequested code
- Show unified diff before making changes, wait for approval
- After changes, verify critical features still exist

## Reference materials

The `reference/` folder (gitignored) contains articles, specs, and background documents used in development. These are local-only — not in git. When working on design decisions or writing docs, check `reference/` for relevant background.

## Skills

Custom AI skills live in `skills/` (tracked in git):
- `sdtm-ct-analysis/` — Structural analysis of SDTM CT: category discovery and profiling.

## Key architectural insights

These emerged from the analytical work and inform design decisions:

- **BCs model collection templates, not medical ontology.** COSMoS DSSs are CRF row templates. DSS-level identity matters only where collection differences reflect clinical differences (specimen-based domains).
- **Specimen-based Findings is not one pattern.** The IG groups 11 domains under this label, but at least three distinct decomposition logics exist (by specimen, by target antigen, by result scale).
- **DS_Codes are mnemonics, not identifiers.** Not unique across domains. Machine-addressability is an open question.
- **Identity layer is complete; measurement spec layer is not.** 4,183 TESTCDs have NCIt identity; only 104 have COSMoS measurement specifications.
