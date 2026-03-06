# SDTM CT Archetype Table — Step 2 Output

**Input:** `SDTM_CT_Category_Discovery.md` (12 categories, 1,181 codelists)
**Analysis date:** 2026-03-06

---

## Output 1 — Archetype Table

| Category | Codelist_Count | Extensibility | SDTM_Variable_Role | NCIt_Relationship | Machine_Actionability | Archetype_Behavior |
|---|---|---|---|---|---|---|
| INSTRUMENT_TC_TN | 706 | Never — instrument-defined term sets are fixed at validation time; extension would invalidate scored totals | QSTESTCD / QSTEST, FTTESTCD / FTTEST, and domain-specific instrument variables | Instrument-defined — NCIt C-codes present but the authoritative source is the instrument scoring manual, not NCIt | Exact string lookup by instrument + domain identity; no semantic inference needed | TC and TN codelists are always co-dependent pairs; a consumer must process them as a unit, never independently, or pairing breaks. |
| INSTRUMENT_ITEM_RESPONSE | 158 | Never — item response sets are closed by instrument design | QSORRES / QSSTRESC, FTORRES / FTSTRESC | Instrument-defined — allowed values are instrument-specific, NCIt C-codes are present but do not carry cross-instrument semantic equivalence | Exact match against instrument-item-specific value set; no cross-instrument comparison is valid | These are allowed-value sets for a single instrument item; applying them to any other instrument item — even one with the same text label — is a category error. |
| MEASUREMENT_TEST_CODE | 140 | Always — open extension expected; domain growth is continuous | LBTESTCD / LBTEST, VSTESTCD / VSTEST, FATESTCD / FATEST, PCTESTCD / PCTEST, and all domain-specific TC/TN pairs | Direct C-code per concept — terms are independently meaningful NCIt concepts; NCIt hierarchy traversal is valid | Semantic concept matching via NCIt; extensibility means a consumer must handle unknown terms gracefully, not treat "not in CT" as invalid | Extensible = Yes is not a defect — it is a design intent; reject-if-not-in-CT logic is incorrect for this category. |
| RESULT_VALUE_SET | 109 | Mixed — fixed for closed grading scales (AJCCGRD, TOXGR), extensible for open-ended response enumerations; the flag itself is the discriminator | LBORRES / LBSTRESC, QSORRES (selected), RSSTRESC, TSPARMCD values | Concept-backed for closed sets; Direct C-code per concept for extensible sets | Closed sets: exact term validation; open sets: semantic matching + graceful unknown handling; extensibility flag must be read before applying validation logic | The extensibility flag partitions this category into two behaviorally incompatible subsets; consuming logic must branch on `Codelist Extensible` before applying any validation. |
| ADMINISTRATION_LOGISTICS | 21 | Mixed — routes and dosage forms extensible (new delivery mechanisms emerge); completion status and contact roles closed | ROUTE, DOSFRM, FREQ, EPOCH, NCOMPLT, ACNOTH | Concept-backed — terms have NCIt backing but administrative context defines their applicability | Qualifier slot-filling; terms populate metadata and process variables rather than test identifiers or results | These codelists describe study conduct logistics, not observations; applying measurement-domain matching logic to them will produce spurious matches. |
| REFERENCE_VOCABULARY | 13 | Always — open by design; reference to external scientific nomenclature is inherently incomplete | LBSPEC, LBSPCCND, LOC, MICROORG, TUMIDENT | Direct C-code per concept with external nomenclature backing (MeSH, NCBI Taxonomy, SNOMED adjacency) | External vocabulary alignment; consuming systems should treat these as reference lookups against an external source, not as closed enumerations | These are large open enumerations backed by external nomenclatures; a consuming system that treats them as CT-complete will reject valid external terms that are simply not yet in the CT file. |
| DOMAIN_GROUPING | 11 | Mixed — QSCAT extensible (new instruments add categories); DSCAT closed | QSCAT, QSSCAT, FTCAT, DSCAT, SUPPDS category variables | Concept-backed at the domain level; individual terms often study-design-specific | Hierarchical grouping slot-filling; values organize observations into analysis-ready subsets, not identify individual observations | Category codelists exist to group observations for analysis — they are not test identifiers; a consumer must not attempt concept matching at the level of individual terms. |
| UNIT | 7 | Always — new assay technologies and PK-normalized variants require new units continuously | VSRESU, LBORRESU / LBSTRESU, AGEU, PK units | Direct C-code per concept; UCUM alignment expected but not encoded in the CT file itself | Unit normalization via external UCUM mapping; semantic equivalence across unit variants requires UCUM, not CT-internal comparison | Unit equivalence (mg vs. milligrams vs. 10⁻³g) cannot be resolved from the CT file alone; consuming systems need UCUM mapping, not just CT lookup. |
| SUBJECT_CHARACTERISTIC | 6 | Never — closed by regulatory and reporting requirements | DM.SEX, DM.RACE, DM.ETHNIC, and related demographic variables | Concept-backed — terms have NCIt backing and map to regulatory submission requirements | Exact term validation against closed regulatory enumeration; no extension expected or supported | These codelists are closed by regulatory mandate, not by convention; any term not present is genuinely invalid for submission purposes, not merely unrecognized. |
| TRIAL_DESIGN | 5 | Mixed — SDTM version identifiers closed; trial type and phase codelists extensible as regulatory categories evolve | TS.TSPARMCD values, EPOCH, INTMODEL, PHASE | Administrative — terms describe study metadata, not observations; NCIt backing present but semantic matching to observations is not applicable | Administrative lookup — populate protocol and regulatory metadata fields; no clinical reasoning applies | Trial design codelists describe the study, not observations in it; applying observation-domain logic (test matching, result validation) to these codelists is a category error. |
| ASSAY_AND_PROCESS_METADATA | 4 | Mixed — device identifier parameters extensible; test operational objectives closed | Device and assay configuration variables; METHOD, QRSMTHOD | Concept-backed; terms describe operational context, not clinical findings | Process metadata slot-filling; terms configure assay interpretation rather than identify observations | These codelists configure assay-level interpretation metadata; they should be consumed at the protocol or assay configuration level, not at the individual observation level. |
| GENERAL_FLAG | 1 | Never — binary/near-binary cross-domain utilities are stable by design | NY (No/Yes), NRIND (normal/abnormal), ND (not done), used across all domains | Concept-backed; terms are simple domain-independent Boolean or ternary values | Cross-domain Boolean lookup; identical matching logic applies regardless of which domain variable carries the flag | A single codelist, used everywhere — any change to this codelist has system-wide impact across all SDTM domains simultaneously. |

---

## Output 2 — Machine-Actionability Ranking

Most to least actionable (system can reliably determine correct term without additional human judgment):

1. **GENERAL_FLAG** — 2–4 closed terms, cross-domain, no ambiguity; exact match is always correct.
2. **SUBJECT_CHARACTERISTIC** — closed, regulatory-mandated, small; exact validation is both sufficient and required.
3. **INSTRUMENT_TC_TN** — naming convention fully systematic; pairing reconstructable from suffix rules alone, no semantic reasoning needed.
4. **INSTRUMENT_ITEM_RESPONSE** — same systematic naming as TC/TN; closed value sets, exact match, no inference required.
5. **TRIAL_DESIGN** — small closed codelists with administrative semantics; exact lookup sufficient for closed members; extensible members require protocol context.
6. **MEASUREMENT_TEST_CODE** — NCIt C-codes enable semantic matching; extensibility flag signals graceful-unknown handling required; large codelists (LBTESTCD 2,475 terms) increase collision risk.
7. **RESULT_VALUE_SET** — machine-actionable within each subset, but extensibility flag must be read first to select the correct validation strategy; bifurcated behavior reduces reliability without that branch.
8. **ADMINISTRATION_LOGISTICS** — concept-backed but administrative context determines applicability; automated routing to correct domain variable requires protocol context not in CT.
9. **DOMAIN_GROUPING** — grouping semantics are study-design-dependent; category values often require protocol knowledge to assign correctly.
10. **REFERENCE_VOCABULARY** — large, open, externally backed; CT coverage is incomplete by design; reliable matching requires external nomenclature systems (NCBI Taxonomy, MeSH).
11. **ASSAY_AND_PROCESS_METADATA** — small category, mixed extensibility, assay-configuration context required; not resolvable from CT alone.
12. **UNIT** — unit equivalence requires UCUM mapping external to CT; CT-only lookup cannot resolve normalization reliably.

---

## Output 3 — Gap Analysis

| Category | Gap | Who would need to act |
|---|---|---|
| INSTRUMENT_TC_TN | TC/TN pairing not encoded — inferred from naming convention only | CDISC + NCI EVS: add `Paired_Codelist_Code` column to CT file |
| INSTRUMENT_ITEM_RESPONSE | Item-to-instrument binding not encoded — inferred from name parsing | CDISC + NCI EVS: add `Parent_Instrument_Code` column |
| MEASUREMENT_TEST_CODE | NCIt hierarchy (parent domain → child domain codelists) not encoded | NCI EVS: publish C-code parent-child hierarchy alongside CT file |
| RESULT_VALUE_SET | Extensibility behavioral branch invisible — no column signals which validation strategy applies | CDISC: document extensibility-driven validation rules per category in SDTM IG |
| ADMINISTRATION_LOGISTICS | Variable binding not encoded — which SDTM variable each codelist populates requires SDTM IG lookup | CDISC: publish variable-codelist binding table as machine-readable artifact |
| REFERENCE_VOCABULARY | External nomenclature source not identified in CT file | NCI EVS: add `External_Source` column (MeSH, NCBI Taxonomy, SNOMED, etc.) |
| DOMAIN_GROUPING | Study-design-specific category values not flagged as such | CDISC: distinguish CT-canonical vs. study-defined values within extensible category codelists |
| UNIT | UCUM equivalence not encoded | CDISC + NCI EVS: add `UCUM_Code` column per unit term |
| SUBJECT_CHARACTERISTIC | Nothing — already self-describing | — |
| TRIAL_DESIGN | Nothing — already self-describing | — |
| ASSAY_AND_PROCESS_METADATA | Assay configuration context (which assay platform drives the codelist) not encoded | CDISC Therapeutic Area teams: document assay-platform bindings in TA IGs |
| GENERAL_FLAG | Nothing — already self-describing | — |

---

## Output 4 — Prompt 1 Sanity Check

No material miscategorizations detected. One boundary worth noting:

**LBSTRESC / EGSTRESC / HESTRESC / ONCRSR** (flagged MEDIUM confidence in Step 1): Step 1 placement in RESULT_VALUE_SET is defensible — their semantic role is allowed result values, not test identifiers. Output 1 makes explicit that RESULT_VALUE_SET has two behaviorally distinct subsets (closed vs. extensible), and these codelists fall in the extensible subset. The MEDIUM confidence flag is appropriate and should be preserved in the assignments CSV — these codelists are the primary evidence that RESULT_VALUE_SET may eventually warrant a formal split into two categories if downstream tooling requires it.
