# Changes — May 2026: making implicit linkages reachable

**Reference versions:** unchanged from Changes_2026-04 (SDTM CT 2026-03-27, COSMoS 2026-Q1, SDTMIG v3.4 / SDTM v2.0). No upstream data refresh. This release is a projection-and-reach pass: previously implicit linkages become explicit traversable rows.

## value_list as identity carrier

The DSS Variables sheet binds variables to codelists in several modes: pinned to a single NCIt concept, pinned via a value_list that enumerates allowed terms, declared as a bare codelist (no per-term pinning), or no codelist at all. Earlier releases treated only the pinned mode as identity; value_list pinning was visible in the graph but not propagated downstream.

This release recognises value_list as a first-class identity carrier throughout. `COSMoS_Graph.xlsx` already projected value_list rows; `DSS_View.xlsx` now carries `value_list` and `value_list_ncit` columns; the three `sdtm-findings-graph/` consumers (Specimen, Measurement, Instrument) read those columns through. A new referential-integrity check in the graph-validation notebook closes the value_list column against the rest of the graph.

## Codelist-forward projections

Two new files make codelist-side reachability explicit, complementing the existing variable-forward and BC-forward views.

`Codelist_Cross_References.xlsx` declares semantic relations between codelists. The seed relation is PROCEDUR ↔ METHOD — clinical abbreviations (MRE, DWI, MRCP) drift between the two codelists, and the Term_Diff sheet provides the canonical lookup from abbreviation to CDISC submission_value. Submission_value is the lookup key, not the abbreviation.

`Codelist_Coverage.xlsx` is a codelist-forward projection of the graph. The wide-format DSS pivot loses bare codelist bindings (a variable scoped to a codelist with no per-term pin); this file preserves them, so codelist-scoped queries are answerable without reconstruction from the variables sheet.

## consumer-bases matures into a multi-view layer

`consumer-bases/` previously held a single denormalised view at one row per DSS. This release adds two complementary projections at different grains.

`DSS_Variables_View.xlsx` is the long-format complement at one-row-per-VLM-row grain. Where `DSS_View.xlsx` is wide and DSS-centric, this view is long and variable-centric — convenient for any consumer that wants to iterate over variables rather than aggregate over DSSs.

`PR_DSS_Reachability.xlsx` is a procedure-forward projection: starts from PR PRDECOD/PRTRT value_lists and traces reachability into Findings DSSs. The five ungoverned RT modalities in PRDECOD (see `cosmos-graph/docs/COSMoS_Open_Work.md` §1 item 8) were surfaced by this view.

`DSS_View.xlsx` now joins `observation_class` from `SDTM_Domain_Metadata.xlsx`, so observation-class scoping is available on every row without a separate lookup.

## Public-repo positioning

The cdisc-for-ai work is sponsor-agnostic, and the May pass strips out remnants of sponsor-specific direction-setting that had accumulated in the public repo. The family-map thread, the `sdtm-narrative/` track, and the `XRay_PatientBurden` and `CaseStudy_Overview` artefacts have been removed; the X-Ray cross-class case study (Procedures plus Findings off the image) remains, and the Glucose case-study pair is kept. The `Top_Level_Summary.md` makes the sponsor-agnostic position explicit.

## Legacy retirement

The pre-graph `sdtm-findings/` consumer track and the single-sheet `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx` flatten that fed it have been retired. The `sdtm-findings-graph/` track has carried all three sub-types since April 2026, and the value_list integration described above closes the last functional gap; parity has been validated downstream. The retirement removes the parallel pipeline.

`cosmos-bc-dss/` narrows from "source-ingest + flatten + analyses" to "source-ingest landing zone + behavioural-analysis docs + NCIt-comparison thread". The `downloads/` folder (read by `cosmos-graph/`) and the behavioural-analysis documentation remain unchanged. The `Flatten`, `Flatten_Diff`, and `Validate` notebooks and their outputs are removed; the `NCIt_Compare`, `NCIt_Source_Probe`, and `Parent_Resolution` notebooks remain. Earlier versions of all removed artefacts remain in git history.

## Housekeeping

Branch hygiene: the eighteen merged feature branches accumulated since the March release have been pruned (four local, fourteen remote). A stale `.gitignore` entry referencing a removed `coa-structure/` track has been cleaned up; `.ipynb_checkpoints/` directories left on disk from notebook editing have been swept. None of the housekeeping affects the machine-actionable outputs.

## Authoritative current state

File-level current state lives in the README sheet of each machine-actionable xlsx, regenerated on every run. Counts, column inventories, and coverage percentages are point-in-time and belong there rather than in this note.

## References

- Behavioural rationale for value_list as identity carrier: [`cosmos-bc-dss/docs/COSMoS_Behavioural_Analysis.md`](../cosmos-bc-dss/docs/COSMoS_Behavioural_Analysis.md)
- COSMoS-side upstream flags raised by the new projections: [`cosmos-graph/docs/COSMoS_Open_Work.md`](../cosmos-graph/docs/COSMoS_Open_Work.md) §1
- Previous release: [`Changes_2026-04.md`](Changes_2026-04.md)
