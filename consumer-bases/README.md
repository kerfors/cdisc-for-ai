# consumer-bases — Joined views over the graph for consumer tracks

`consumer-bases/` carries joined, denormalised projections over `cosmos-graph/` and
repo reference metadata, shaped for consumer use but not yet the final consumer
shape. Final shaping — sub-typing, behavioural classification, narrative framing —
stays in consumer tracks (`sdtm-findings/`, `sdtm-narrative/`, future tracks).

## Scope discipline

**In scope.** Join, filter, denormalise the graph (`cosmos-graph/interim/COSMoS_Graph*.xlsx`).
Join with repo reference metadata: `SDTM_Domain_Metadata.xlsx`,
`SDTM_Test_Identity.xlsx`, `SDTM_Instrument_Identity.xlsx`,
`SDTM_Instrument_Test_Identity.xlsx`.

**Out of scope.** Interpretive overlays — sub-typing decisions (specimen-based vs
measurement vs instrument), behavioural classifications (decomposition-axis
triage, scope exclusions), narrative framing.

**Why.** Content that requires editorial judgment belongs to the consumer that
owns the judgment, not to a shared upstream view. The same view feeds all
consumers; each consumer applies its own editorial pass.

## Architecture — where this fits

```
cosmos-graph/ ─────────┐
                       │
sdtm-test-codes/ ──────┼──→ consumer-bases/ ──→ sdtm-findings/
sdtm-domain-reference/ ┘                    └─→ (future consumers)
```

`cosmos-graph/` provides the lossless COSMoS projection. The reference tracks
provide shared SDTM identity (TESTCDs, instrument codelist anchors, domain
metadata). consumer-bases joins them into views shaped for consumer use.
Consumer tracks add the final shaping.

## Views

| File | Sheets | Grain | Built by |
|---|---|---|---|
| `DSS_View.xlsx` | `Test_Identity`, `Measurement_Specs`, `ReadMe` | TESTCD / DSS | `notebooks/10_dss_view.ipynb` |

`DSS_View.xlsx` is graph-wide — every COSMoS DSS across all 32 domains (not
only Findings). Observation-class scoping (Findings vs Events vs Interventions
vs Special-Purpose) is applied by each consumer track. The first consumer is
`sdtm-findings/`, which filters on `SDTM_Domain_Metadata.Observation_Class`.

## Folder conventions

- `notebooks/` — Jupyter notebooks that build the views.
- `interim/` — view xlsx files. Named `interim/` rather than `machine_actionable/`
  because the views are joined projections, not final consumer shape; consumer
  tracks still own the final form. Same precedent as `cosmos-graph/interim/`.
- `docs/` — track documentation as it accrues.
- `reports/` — per-view validation reports.

Folders not present:

- `downloads/` — not applicable. Reads only repo artefacts.
- `machine_actionable/` — replaced by `interim/` (see above).
- `pre-2026-03/`, `diffs/` — added when the first release boundary is taken.

## Cross-references

- `cosmos-graph/docs/COSMoS_Graph.md` — graph reference.
- `cosmos-graph/docs/COSMoS_Open_Work.md` — open work, including the deferred
  `DSS_Attributes` long-format sheet (§3) which would live here when its trigger
  fires.
- `sdtm-findings/` — first consumer of `DSS_View.xlsx` (rewire is separate
  work; legacy `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx` still feeds it as of
  2026-04).
- Repo-root `CLAUDE.md` — repo conventions.
