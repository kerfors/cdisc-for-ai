# COSMoS Graph — open work

*Forward-looking brief. Supersedes `COSMoS_Next_Steps_Brief.md` and the §3 proposals in `COSMoS_Graph_Upstream_Additions.md` (both retained under [`archive/`](archive/)). State as of the 2026-04-23 triage.*

*cdisc-for-ai, 2026-04.*

---

## 1. Branch B — consumer-track rewiring

Still open. Rewire `sdtm-findings/` (and, downstream of it, `sdtm-domain-reference/` where it depends on COSMoS coverage) to read `COSMoS_Graph*.xlsx` instead of the legacy `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx`.

**Starting state.** The legacy flattener still builds and still feeds the existing consumers — nothing is broken. The `Identity` back-compat sheet was not built (see [`archive/COSMoS_Flattener_Rewrite.md`](archive/COSMoS_Flattener_Rewrite.md) §3); consumer tracks cannot switch files with a column-rename.

**Decisions to make up front.**

- Rewire one structural-type consumer first (specimen-based, measurement, or instrument) vs. all three in one pass. Specimen-based has the richest coverage; instrument has the cleanest joins.
- Retire the legacy pipeline at the end of the rewire, or leave both in place. If retiring, the `cosmos-bc-dss/notebooks/COSMoS_BC_DSS_Flatten*.ipynb` notebooks also go.

The two-sheet consumer output shape (`Test_Identity` + `Measurement_Specs`) should be preserved — downstream readers rely on it.

## 2. Upstream flags — paperwork to CDISC and NCI EVS

Five asks. Each is an authoring or subset issue outside this repo.

**To the COSMoS authoring working group.**

1. **TU TUMERGE / TUSPLIT.** `assigned_term_concept_id` points at finding-state concepts (C94525, C96642). Correct TESTCD anchors already exist in SDTM CT: C225437 "Confluent Tumor Masses Assessment" and C225438 "Tumor Fragmentation Assessment".
2. **DM ETHNIC / RACE.** `codelist_concept_id` points at legacy codes (C66790, C74457). Superseded by C128690 ETHNICC and C128689 RACEC.

**To the CDISC SDTM CT team.**

3. **MBTESTCD / MBTEST subset.** Does not carry C132388 "Treponema pallidum Antibody Measurement" or C171439 "SARS-CoV-2 Antibody Measurement". Both are valid NCIt Laboratory Procedures and are referenced by MB TPLAB and MB SAR2ABDET.
4. **VSRESU (C66770) codelist.** Does not carry C105484 "fraction of 1", needed for OXYSAT.VSSTRESU.

**To the NCI EVS Variable Terminology team.**

5. **Root-subset gaps.** Thirty-seven variable codes resolve to compositional forms that have no `--<remainder>` representation in the NCI EVS Variable Terminology Root subset at 2026-03-27. Dominated by the GF* (Genomic Findings) family, `STRESN` across domains, and `ISBDAGNT`. Full list in [`../reports/root_subset_fallback_diagnostic.md`](../reports/root_subset_fallback_diagnostic.md).

Paperwork, not code. Drafts live outside this branch.

## 3. Deferred architectural work

Three items from the 2026-04-23 triage are documented but not built. Each waits on a trigger.

- **`DSS_Attributes` derived sheet.** Long-format projection over `Variables` (specimen, method, units, LOINC, decimal_places). Projection fits in ~20 lines of consumer code; single consumer today. **Trigger:** a second consumer appears and the projection becomes worth materialising.
- **`BC` cross-domain flags.** An `is_cross_domain_class` flag on the `BC` sheet. Zero BCs are cross-Observation_Class at 2026-Q1 — the flag would be uniformly `False`. **Trigger:** overlay content introduces a cross-class pairing (see below).
- **`COSMoS_Graph_Overlay.xlsx` file.** Parallel file for schema-identical but not-CDISC-authored content (track-authored extrapolations, sponsor-scope case specialisations). Pattern documented in [`COSMoS_Graph.md`](COSMoS_Graph.md) §4. **Trigger:** a first overlay row is authored. Current candidates are the X-Ray MK-side DSSs (genuine cross-domain-class extrapolation, absent from source) and DSS rows under the 6MWT BC (which has `bc_type = full_no_ds`). Both candidates stay out of scope until authored.

## 4. What's closed

For context, so the items above read as what remains.

- **Branch A — Step 3 NCIt narrative layer.** Delivered in `sdtm-narrative/` (Tier 2b per-DSS paragraphs + Tier 3 per-case DataBooks).
- **Narrative-layer follow-ups.** `var_nn` compositional-fallback strip and `Instrument_NCIt_Code` column-name fix delivered in sdtm-narrative (commit `0ba8791`).
- **Root-subset fallback diagnostic** (archive/`COSMoS_Graph_Upstream_Additions.md` §3.5). Closed 2026-04-23. Output in [`../reports/root_subset_fallback_diagnostic.{md,csv}`](../reports/root_subset_fallback_diagnostic.md).
- **Step 2 flattener rewrite.** Delivered and merged. Close-out in [`archive/flattener_rewrite_audit.md`](archive/flattener_rewrite_audit.md).
