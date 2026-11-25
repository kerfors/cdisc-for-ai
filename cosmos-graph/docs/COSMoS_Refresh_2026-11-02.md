# Graph refresh — COSMoS package 2026-11-02 (Package 19)

**Reference versions:** COSMoS BC/DSS bumped **2026-07-14 → 2026-11-02**. SDTM CT (NCI EVS
2026-09-25), NCIt FLAT 2026-09-29 and SDTMIG v3.4 / SDTM v2.0 unchanged. CRF Specializations
held out of scope, as before. Source: the public export (cdisc-org.github.io/COSMoS/export),
identical to `export/` in the COSMoS repository at the Package 19 release commit.

## What moved in the source

**The export has the same structure.** Same sheets, same columns in the same order, ReadMe
sheets identical apart from the date and count line. The BC and SDTM LinkML schemas are
unchanged; only the CRF schema changed, and it is not read here. One new value:
`sdtmig_start_version = 4-0`, on the first Dataset Specializations that start in SDTMIG 4.0
(GI and HM).

**BC — 113 new concepts, no removals.** The additions follow the DSS additions below. Churn on
surviving BCs is small: Age at Death (C135383) loses its parent, plus a few category, synonym
and result-scale edits.

**DSS — +166 groups, no removals.** For the first time COSMoS has Dataset Specializations in
CE, HO, ML, AG, DA, CV, GI, HM and MS. The clusters:

- Hypoglycaemia: the event and its symptoms (CE), precipitating factors (FA), treatment as
  medication, food or drink and prior anti-hyperglycaemic therapy (CM), last dose prior (EX)
  and meals (ML). They use the SDTM disease milestone timing variables MIDS, RELMIDS and
  MIDSDTC, which have no domain prefix.
- Meal and glucose tolerance tests: the procedure agents (AG) and the glucose, insulin and
  C-peptide measurements (LB); the glomerular filtration rate family and other lab tests (LB).
- Healthcare encounters (HO): visits and stays by setting.
- Drug accountability amounts (DA); minimum inhibitory concentration (MS).
- Medical history of kidney and diabetic conditions (MH).
- Procedures (PR): kidney and liver procedures, transplantation, biopsy, mastectomy,
  ultrasound, gastrostomy. Gastrostomy has no location variable.
- Breast cancer pathology (MI).
- Organ measurements: depth, length, width and volume of liver (GI), spleen (HM) and kidney (UR).
- Heart mass, two Dataset Specializations told apart by location (CV).

**Edits on surviving groups.** 64 groups changed, most in RS, DD, LB, MI and VS: data type,
length, origin and value lists. Two exposure groups (EXPOSCOLL, EXPOSCOLL_XANOMELINEPLACEBO)
move to another BC (C117466 → C177924). EDLVRDTC and EGESTAGE, which moved from RP to SC in
2026-07-14, are now in both: the SC groups keep their `vlm_group_id` and get an `SC_` prefix in
their short names, and RP gets new groups `EDLVRDTC_RP` and `EGESTAGE_RP` (short names with
`RP_`) on the same BCs. The domain now shows in the mnemonic itself. PRLNTX leaves RADIATIONCANCER, and the MIRESCAT value list leaves HER2STAININGINT.

## Rebuild results

The graph track rebuilt cleanly. Three steps further on stopped on content the code did not
expect; each was fixed or decided, not worked around.

- **`30_pr_dss_reachability`** assumed one PRLOC row per PR Dataset Specialization. GASTROSTOMY
  has none. The notebook now allows none and keeps that apart from a location present without
  value.
- **`Domain_Behaviour`** assumed a two-letter domain prefix on every variable. MIDS and RELMIDS
  have none. It now strips the prefix only where it is there, as `10_dss_view` already did.
- **`Domain_Behaviour`** found four Variable_Meaning rows that said COSMoS does not use a
  variable it now uses (LBANMETH, LBTPT, CVMETHOD, CVLOC). The rows were updated in
  `SDTM_Domain_Metadata.xlsx`; CVLOC now takes the position system.
- **`COSMoS_Observable_LOINC_Check`** fetched nine new LOINC codes into the service cache. Three of
  them (on CPEPTIDESERPL, CPEPTIDEURIN, INSULINSERPL) are LOINC grouper codes (class
  LABORDERS.ONTOLOGY), not observation codes.

**Validation (notebook 30).** `schema_column_coverage` is unchanged. Against SDTM CT
2026-09-25:

- `ct_unresolved_concept_ids` grows: new procedure, breast pathology and vital signs terms are
  NCIt concepts not yet in CT; two of them are not in NCIt FLAT 2026-09-29 either.
- `pinned_term_not_in_bound_codelist`, empty until now, fails: the organ measurement tests are
  CT terms, but not in GASTROCD, HMTESTCD or URNSTSCD; two lymph node tests are not in MITSCD;
  ULTRASOUND IMAGING and ULTRASONOGRAPHIC ELASTOGRAPHY are not in PROCEDUR.
- Unresolved value-list members change: ABDOMEN in an ultrasound PRLOC value list is not a LOC
  term; three mastectomy and dissection members are not in PROCEDUR.

The package post-dates the CT release it will be aligned with; the next SDTM CT release is
expected in late December. Listed in `COSMoS_Open_Work.md` §1.

**Instrument category resolution (notebook 50).** No status transitions.

**Instrument parent chains (notebook 51).** Unchanged. C222259 and C222260 are still roots.
CDISC has stated the convention that `parent_bc_id` is the NCIt direct parent; the parent of
both is C20993, which is not a BC. The watch item in `COSMoS_Instrument_Layer.md` §8 is closed
on that basis.

**Downstream.** `consumer-bases` and the four `sdtm-findings-graph` consumers rebuilt on the new
graph. The specimen consumer picks up the new LB and MI groups; the measurement consumer its
first CV groups; the instrument consumer follows the RS edits; the immunogenicity consumer is
unchanged apart from its version line. GI and HM have content now and no consumer class;
`Scope_Check` reports them, as it reports the other domains without one. Row counts are
point-in-time and live in each file's ReadMe sheet.

## Still pending after this note

- Whether GI and HM get a consumer class (`SDTM_Domain_Metadata.xlsx`).
- Key_Compare counts location and system as different, also where location is the system
  (`COSMoS_Open_Work.md` §2).
- `sdtm-test-codes` and `sdtm-domain-reference` were not re-run: SDTM CT did not move.
- The per-DSS instance YAML under `cosmos-bc-dss/downloads/cosmos_yaml/` is not on the refresh
  path and was not refreshed.
