# Graph refresh — COSMoS package 2026-05-26

**Reference versions:** COSMoS BC/DSS bumped **2026-03-31 → 2026-05-26**. SDTM CT (NCI EVS
2026-03-27) and SDTMIG v3.4 / SDTM v2.0 unchanged. CRF Specializations draft held out of
scope this pass. This is an upstream data refresh, not a projection change — the flatten
and downstream notebooks are unchanged; only their inputs moved.

## What moved in the source

**BC — five new concepts, no removals.** Two QRS / Functional Assessment containers
(Cognitive Assessment Tool, Clinical or Research Functional Assessment Tool), two
Tumor/Lesion Identification assessments under RECIST 1.1 (Confluent Tumor Masses,
Tumor Fragmentation), and a Tumor Examination under Medical Examination. Only the two
RECIST tumor assessments carry a Dataset Specialization; the QRS pair and Tumor
Examination are BC-only so far. Categories and the BC hierarchy grew to match.

**DSS — no new or removed specialization groups; the change is a metadata backfill.**
The group set is identical across the bump. What changed is that previously-empty
provenance and typing fields are now populated across thousands of variable rows:
`origin_type` and `origin_source` move from blank to Assigned / Derived / Collected and
Sponsor / Vendor / Investigator; `data_type` and `length` fill in where they were blank.
Smaller touches land on `value_list`, `dec_id`, `assigned_term` / `assigned_value`,
`significant_digits`, and `format`.

The `consumer-bases` and `sdtm-findings-graph` consumers do not project `origin_type` or
`origin_source`, so that part of the backfill stops at the graph. What reaches downstream
is the `value_list` / assigned-term movement — concentrated in the unit slots (`STRESU`,
`ORRESU` value-lists and codelists) and a few `result_scales` — surfaced on the rebuild
below, even though no DSS group was added or dropped.

## Instrument category-token resolution, re-run on the new package

The instrument-family grouping tokens in `BC_Categories` are labels, not identifiers; the
resolver (`notebooks/50_instrument_category_resolution.ipynb`, output
`reports/Instrument_Category_Resolution.xlsx`) recovers BC identity where a label matches a
`bc_short_name` or a unique `bc_synonyms` entry. See `COSMoS_Instrument_Layer.md` §5 for the
underlying identifier asymmetry. The token population is stable across the bump; two
qualitative shifts are worth recording.

**Upstream registered synonyms that previously had no home.** Abbreviation tokens that were
unresolved against the March package — among them ECOG and KFSS — now resolve, because the
May BC export carries them as `bc_synonyms`. This is the synonym layer doing exactly the
recovery work it was meant to, and evidence the COSMoS group is closing abbreviation gaps
from the source side.

**A BC rename broke a long-form label link — a live instance of the §5 fragility.** The
6 Minute Walk container BC (C115789) was renamed to append "2008 Version", but the
`BC_Categories` token kept the original text and the long form is not among the BC's
synonyms. The exact-name link therefore silently broke: a token that resolved by name in
March is unresolved in May. This is precisely the renaming / versioning fragility §5 warned
about, and it landed on the repo's flagship 6MWT instrument. It argues again for a
persistent identifier on the grouping itself rather than label-text matching.

Per-token counts are version-bound and live in the report, not here.

## Downstream rebuild

`consumer-bases` (DSS_View, DSS_Variables_View, PR_DSS_Reachability) and the three
`sdtm-findings-graph` consumers (Specimen, Measurement, Instrument) were rebuilt on the new
graph. Row counts are stable (DSS 1326, Measurement 128, Instrument 175 instrument rows);
the cell movement is modest and sits where the source backfill landed — unit value-lists
and codelists (`STRESU`, `ORRESU`) and a few `result_scales`.

Two structural changes propagated and are worth recording:

- **6MWT rename and a new parent.** The renamed 6MWT container (C115789, now
  "…2008 Version") carries through every sheet it appears in. It also gained a new parent,
  **C222260 "Clinical or Research Functional Assessment Tool"** — one of the five new May
  BCs — so a new concept entered the hierarchy directly above 6MWT. In `BC_Categories` the
  same row now pairs the new `bc_short_name` with the unchanged old category text
  ("6 Minute Walk Functional Test"), a literal view of the §5 label-vs-identifier split.
- **LOINC coding-system URI normalised.** The May package consolidated the LOINC system URI
  from `https://loinc.org` to `http://loinc.org/`. In `DSS_View` this shows as a dropped
  `Coding_https://loinc.org` column, its content folded into `Coding_http://loinc.org/`.
  Cosmetic upstream cleanup, not a content loss.

## Still pending after this note

CRF Specializations deferred (see `COSMoS_Open_Work.md`). `sdtm-test-codes` and
`sdtm-domain-reference` were not re-run — they are CT/NCIt-driven and hand-maintained
respectively, and SDTM CT (2026-03-27) did not move this pass. The per-DSS instance YAML
under `cosmos-bc-dss/downloads/cosmos_yaml/` was not refreshed; it feeds only the archived
"as authored" analysis, not the flatten, so it is not on the refresh path.
