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

Nine asks. Each is an authoring or subset issue outside this repo.

**To the COSMoS authoring working group.**

1. **TU TUMERGE / TUSPLIT.** `assigned_term_concept_id` points at finding-state concepts (C94525, C96642). Correct TESTCD anchors already exist in SDTM CT: C225437 "Confluent Tumor Masses Assessment" and C225438 "Tumor Fragmentation Assessment".
2. **DM ETHNIC / RACE.** `codelist_concept_id` points at legacy codes (C66790, C74457). Superseded by C128690 ETHNICC and C128689 RACEC.
3. **TUMIDENT carries PRVIR / PRVIRP without TU prefix.** Empirically observed in `cdisc_sdtm_dataset_specializations_latest.xlsx`. Sibling `TUMIDENT_RECIST1_1` correctly carries `TUPRVIR` / `TUPRVIRP`. Both rows have `dec_id = NaN`, `codelist = C66742`. Should align with sibling: `PRVIR` → `TUPRVIR`, `PRVIRP` → `TUPRVIRP`.

**To the CDISC SDTM CT team.**

4. **MBTESTCD / MBTEST subset.** Does not carry C132388 "Treponema pallidum Antibody Measurement" or C171439 "SARS-CoV-2 Antibody Measurement". Both are valid NCIt Laboratory Procedures and are referenced by MB TPLAB and MB SAR2ABDET.
5. **VSRESU (C66770) codelist.** Does not carry C105484 "fraction of 1", needed for OXYSAT.VSSTRESU.
6. **AUTOPSY in `--METHOD` value_lists.** Appears in some `--METHOD` value_lists in the CDISC source xlsx; not present in METHOD codelist (C85492). Confirmed by Linda Lander (CDISC); will be removed in next package release.
7. **PINCH DYNAMOMETRY in `--METHOD` value_lists.** Same pattern as AUTOPSY. Confirmed by Linda Lander (CDISC); will be removed in next package release.
8. **PR PRDECOD value_list carries 5 ungoverned RT modalities.** `RADTHERAPHYBREASTCANCER` PRDECOD value_list contains `INTENSITY MODULATED RADIATION THERAPY`, `RADIOSURGERY`, `STEREOTACTIC BODY RADIATION THERAPY`, `INTRACAVITY BRACHYTHERAPY`, `INTERSTITIAL BRACHYTHERAPY`. None is governed in the PROCEDUR codelist (C101858) at 2026-03-27. Only `3D CONFORMAL RADIATION THERAPY` from the same value_list is governed. All five are valid NCIt concepts. Resolution direction differs from items 6/7 — these are candidates for ADDITION to PROCEDUR rather than removal from the value_list (or, alternatively, for the COSMoS author to remove them from the value_list pending PROCEDUR extension). Surfaced by `consumer-bases/interim/PR_DSS_Reachability.xlsx` (notebook `30_pr_dss_reachability.ipynb`) 2026-05.

**To the NCI EVS Variable Terminology team.**

9. **Root-subset gaps.** Thirty-seven variable codes resolve to compositional forms that have no `--<remainder>` representation in the NCI EVS Variable Terminology Root subset at 2026-03-27. Dominated by the GF* (Genomic Findings) family, `STRESN` across domains, and `ISBDAGNT`. Full list in [`../reports/root_subset_fallback_diagnostic.md`](../reports/root_subset_fallback_diagnostic.md).

Paperwork, not code. Drafts live outside this branch.

## 3. Deferred architectural work

Three items from the 2026-04-23 triage are documented but not built. Each waits on a trigger.

A May 2026 upstream-improvements proposal (separate document, sourced from the family-map / inventory / integration consumer thread) references all three items. Per-item status notes follow.

- **`DSS_Attributes` derived sheet.** Long-format projection over `Variables` (specimen, method, units, LOINC, decimal_places). Projection fits in ~20 lines of consumer code; single consumer today. **Trigger:** a second consumer appears and the projection becomes worth materialising. **Status (2026-05): superseded.** Trigger fired (three consumers — family-map prompt, Procedure-Options Inventory, integration prompt) and resolved by `consumer-bases/interim/DSS_Variables_View.xlsx` (notebook `20_dss_variables_view.ipynb`), which projects every Variables row at the consumer-bases layer with AssignedTerms enrichment, observation_class, and the four binding modes (pinned / value_list / bare / no codelist). Any consumer that wanted `DSS_Attributes` can derive it by filtering this view on the relevant variable suffixes. No further upstream action.
- **`BC` cross-domain flags.** An `is_cross_domain_class` flag on the `BC` sheet. Zero BCs are cross-Observation_Class at 2026-Q1 — the flag would be uniformly `False`. **Trigger:** overlay content introduces a cross-class pairing (see below). **Status (2026-05):** Still contingent. The May 2026 proposal does not introduce overlay content; the flag would remain uniformly `False`.
- **`COSMoS_Graph_Overlay.xlsx` file.** Parallel file for schema-identical but not-CDISC-authored content (track-authored extrapolations, sponsor-scope case specialisations). Pattern documented in [`COSMoS_Graph.md`](COSMoS_Graph.md) §4. **Trigger:** a first overlay row is authored. Current candidates are the X-Ray MK-side DSSs (genuine cross-domain-class extrapolation, absent from source) and DSS rows under the 6MWT BC (which has `bc_type = full_no_ds`). Both candidates stay out of scope until authored. **Status (2026-05):** Pattern unchanged. The May 2026 proposal does not author overlay content; the file remains a documented architectural pattern.
- **`ds_id` → `ds_code` rename (track-wide).** The values in `ds_id` are CDISC mnemonics, not identifiers — empirically unique at 2026-Q1, but cross-domain uniqueness is incidental, not guaranteed (per `CLAUDE.md` "DS_Codes are mnemonics, not identifiers"). The cosmos-graph stack currently standardises on `ds_id` (DSS sheet, Variables sheet, `DSS_View.Measurement_Specs`, `DSS_Variables_View.Variables`). **Trigger:** dedicated rename branch with coordinated diffs across `cosmos-graph/notebooks/10_flatten_schema_driven.ipynb`, `consumer-bases/notebooks/10_dss_view.ipynb`, `consumer-bases/notebooks/20_dss_variables_view.ipynb`, and any docs/READMEs that name the column. Held off the May 2026 upstream-improvements branch to keep that work consistency-preserving.

## 4. What's closed

For context, so the items above read as what remains.

- **Branch A — Step 3 NCIt narrative layer.** Delivered in `sdtm-narrative/` (Tier 2b per-DSS paragraphs + Tier 3 per-case DataBooks).
- **Narrative-layer follow-ups.** `var_nn` compositional-fallback strip and `Instrument_NCIt_Code` column-name fix delivered in sdtm-narrative (commit `0ba8791`).
- **Root-subset fallback diagnostic** (archive/`COSMoS_Graph_Upstream_Additions.md` §3.5). Closed 2026-04-23. Output in [`../reports/root_subset_fallback_diagnostic.{md,csv}`](../reports/root_subset_fallback_diagnostic.md).
- **Step 2 flattener rewrite.** Delivered and merged. Close-out in [`archive/flattener_rewrite_audit.md`](archive/flattener_rewrite_audit.md).
- **BC-side validation in `30_validate_graph.ipynb`.** Six hard referential-integrity checks promoted from inline prints in notebook 10 — `BC_Parents.bc_id` and `.parent_bc_id` close against `BC`; `BC_Categories.bc_id` closes against `BC` and `.category` against the `Categories` vocabulary; `Coding.bc_id` and `DataElementConcepts.bc_id` close against `BC`. Trigger: `consumer-bases/` consumes `Coding` directly. All checks PASS at the current package.
- **METHOD codelist false-positive review.** Earlier QC pass flagged `C179788` as missing from METHOD codelist (C85492). Linda Lander (CDISC) confirmed C179788 is correctly assigned to QRSMTHOD codelist; the dataset specialization assigns it correctly. No action.
