# Case-study walkthroughs — archived April 2026 snapshots

Two case pairs, written 2026-04-13/14 and reframed 2026-04-26, against NCI EVS SDTM CT 2026-03-27 and the COSMoS 2026-Q1 export (DSS package_date 2025-12-16). Archived 2026-10. They are not maintained. The current reference set is listed at [kerfors.github.io/cdisc-for-ai](https://kerfors.github.io/cdisc-for-ai/).

- **Glucose** (Findings; LB) — `Glucose_COSMoS_Story.html`, `Glucose_StudyIntent_Story.html`
- **6MWT** (COA; QS / FT / RS) — `6MWT_NCIt_Story.html`, `6MWT_COSMoS_Story.html`

The pages are kept as written. A check on 2026-10-01 against SDTM CT 2026-09-25, the COSMoS 2026-07-14 graph and NCIt 26.09d found the points below.

## Not correct when written

- **6MWT NCIt Story — node labels.** C20993 is *Research or Clinical Assessment Tool*, not "Clinical or Research Assessment Instrument". C211913 is *CDISC QRS Instruments Questions*; "Clinical or Research Assessment Question" is its parent, C91102.
- **6MWT NCIt Story — C213028.** Shown as an intermediate QRS grouping node. C213028 is *IGHE wt Allele*. C115409's parent is C211913 directly.
- **6MWT NCIt Story — instrument to question link.** NCIt has no association from C115789 to C115800–C115805; C115789 carries only Concept_In_Subset associations. The instrument-to-question link in this repo comes from codelist name matching (`Instrument_Match_Method`), not from NCIt.
- **6MWT COSMoS Story — LOINC.** SIXMW106 (C115805) has LOINC 64098-7; the page says none mapped for all six.
- **6MWT COSMoS Story — decimal places.** "Decimal Places 5" has no source in the COSMoS graph.
- **6MWT COSMoS Story — "Functional Assessment".** Called a COSMoS-original tag that exists nowhere in NCIt. It is the preferred term of NCIt C81250.
- **Glucose pair — "Qualitative".** Used as result scale for GLUCUA and GLUCURINPRES. It is not a COSMoS result-scale value (Nominal, Ordinal, Quantitative, Temporal, Narrative).
- **Glucose Study-Intent Story — LOINC.** Says LOINC is listed at DSS metadata level, not in the variable spec. LOINC is carried on the LBLOINC variable (assigned value or value list).
- **Glucose Study-Intent Story — open slots.** LBTPTREF, LBELTM, LBTPT and LBVISIT are listed as GLUCPL open slots. GLUCPL has 12 variables and none of these; Part 1 of the same page correctly places them outside the DSS.

## Changed since

- **COSMoS 2026-05-26:** instrument BC C115789 renamed *6 Minute Walk Functional Test 2008 Version* and re-parented from C81250 to C222260 (*Clinical or Research Functional Assessment Tool*), which has no parent BC.
- **COSMoS 2026-05-26:** variable origins changed. STRESC/STRESN are now Derived (GLUCPL: was Collected; SIXMW101: was Assigned). TESTCD/TEST carry origin Assigned/Sponsor. Unit variables carry data type `text`.
- **package_date** is now 2026-05-26.
- **6MWT NCIt Story, Part 2 counts** (SDTM CT 2026-09-25): 363 instrument codelists (was 359); instrument match 260 (258); container match 359 (354); both 256 (254); container only 103 (100); instrument only 4 (4); neither 0 (1). C20993 tree 2,559 concepts (2,208); C211913 tree 370 (365). The "1,220 mapped / 988 classification-only" split cannot be reproduced from files in this repo.
