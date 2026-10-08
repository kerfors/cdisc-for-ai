# Observables, Phase 1: what the standards publish

*Written 2026-10-08. COSMoS 2026-07-14, SDTM CT 2026-09-25, LOINC 2.82. One pass, Findings domains only.*

Phase 1 of the [observables direction](Observables_Direction.md): read and record what the standards publish about what identifies an observable, and say where they agree, disagree and are silent. The standards have been developed over many years by different groups, so they are read as evidence, not as a specification that is right. Nothing on this page is classified by us; where we would have to decide, it is listed as open. The decisions come after this page (see [What comes next](#what-comes-next)).

Every number on this page comes from a cell in [`Domain_Behaviour.ipynb`](../domain-behaviour/notebooks/Domain_Behaviour.ipynb), sections 4b to 4e, and the sheets of [`Domain_Behaviour.xlsx`](../domain-behaviour/interim/Domain_Behaviour.xlsx).

## Sources read

| Source | What is read | Sheet |
|---|---|---|
| COSMoS (public export) | Which variables separate the Dataset Specializations (DSSs) of one Biomedical Concept (BC); predicate term, linking phrase, data element concept per variable; `--EVAL` values | `Fanout_Axes`, `Variable_Evidence`, `Rater_COSMoS_EVAL` |
| `COSMoS_Observable_Derivation` | The observable key per DSS: `bc_id \| component \| system \| scale \| method` | `Key_Compare` |
| SDTM CT | Codelist names and definitions; instrument class (QS, FT, RS); the Evaluator codelist | `Variable_Evidence`, `Rater_Evidence`, `Rater_Class_Moves` |
| LOINC | LOINC's own axes for each code a DSS pins (via `COSMoS_Observable_LOINC_Check`) | `LOINC_Compare`, `LBCAT_LOINC_Class` |
| NCIt | Instrument definitions; the clinical outcome assessment types | `Rater_Evidence` |

Scope: the Findings domains, by `Observation_Class` in [`SDTM_Domain_Metadata.xlsx`](../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx). Of 74 variable × domain pairs that differ between the DSSs of one BC, 27 are in Findings. The Events and Interventions rows stay in the sheet for a later pass.

## Where the standards agree

**A core of three axes.** For the 70 BCs that fan out and are in the scope of the observable key, the fan-out axes and the key agree without exception on:

| Axis (fan-out) | Key part | BCs, both |
|---|---|---|
| specimen | system | 29 |
| test detail | component | 18 |
| binding agent | component | 6 |

Method agrees in 8 BCs (one difference, below).

**COSMoS publishes these variables consistently.** `--SPEC`, `--METHOD`, `--TSTDTL` and `--BDAGNT` each have a COSMoS predicate, a linking phrase and an SDTM CT codelist, and they are published the same way in every Findings domain where they occur. In the Findings rows, only 4 variables are published differently from the same generic variable in another domain: `LBCAT`, `RSCAT`, `MKLOC`, `TRGRPID` — grouping and context variables, not the core.

**LOINC confirms the specimen axis.** For 30 LB BCs that fan out and have DSSs with a LOINC code, COSMoS specimen and LOINC system agree in 26 BCs. The two exceptions are COSMoS pin errors already reported by the LOINC check: both nicotine DSSs pin the same serum/plasma codes, and `HGBBLDDIP` pins a urine code.

So the standards together give a component (test code, test detail, binding agent), a system (specimen) and a method. This is close to LOINC's own decomposition.

## Where the standards disagree

**Method.** One BC: Transcription (C17208). Its DSSs differ in `GFANMETH` (method of secondary analysis), not in `GFMETHOD`; the key reads `--METHOD` only. LOINC adds method differences in 3 BCs where COSMoS has none (Prothrombin Time, Macrocyte Count, Microcyte Count); there, LOINC method follows from which codes are pinned, not from a COSMoS `--METHOD` value.

**Scale.** The fan-out and the key read different proxies: units present or absent, against the `--ORRES` data type. They agree in 17 BCs; 3 are fan-out only, 7 key only. COSMoS publishes result scale per BC, not per DSS, so no published value settles which proxy is right. LOINC scale agrees with the fan-out in 8 BCs and adds 1.

**Test code within one BC.** Glucose (C105585) carries two test codes, `GLUC` and `GLUCPE`. The key separates them; the fan-out does not count test code as an axis.

**LOINC distinguishes more.** Between sibling DSSs, LOINC property differs in 13 BCs, class in 11, component in 2 (for example Occult Blood: hemoglobin in stool, blood and erythrocytes in urine). COSMoS has no axis for property or class.

**Category and LOINC class are different groupings.** LB DSSs with a LOINC code, by assigned `LBCAT` and LOINC class: CHEMISTRY is mostly CHEM but also DRUG/TOX, COAG and UA; HEMATOLOGY is mostly HEM/BC but also COAG and CHEM; URINALYSIS is mostly UA but also 9 CHEM. LOINC does not settle what `LBCAT` means.

## Where the standards are silent

**Whether a distinction changes the observation.** No source says it. The COSMoS predicates say how a variable relates to the result, not whether two DSSs that differ on it are two observables. Only two predicates name a kind of thing: `IS_SPECIMEN_TESTED_IN` and `IS_SUBJECT_STATE_FOR`. `SPECIFIES` covers method, test detail, location, status and reasons alike.

**Category.** `LBCAT` and `RSCAT` have the same predicate and phrase (`GROUPS`, "groups values in"). Only SDTM CT tells them apart: `RSCAT` has the codelist ONCRSCAT, defined as the named response criteria; `LBCAT` has no codelist and its values carry no NCIt code. 12 BCs fan out by category (8 LB, 4 RS); category is not in the key, so the four RS BCs collapse to one key each.

**Variables that separate DSSs without a stated meaning in our axes.** `GFSYMTYP` and `GFINHERT` (1 BC each, both with predicate and codelist) and `TRGRPID` (2 BCs, no predicate, no codelist — in TR the only assigned value that separates the DSSs besides the DS code). These are outside the seven axes we chose; the gap is in our analysis, not in the standards.

**Evaluator in oncology.** In RS, TR and TU only value lists differ (`--EVALID`, `TREVAL`, and in TR `TRSTAT`, `TRREASND`, `TRREASNE`). Where `TUEVAL` = INVESTIGATOR is assigned, it is the same on both siblings.

**Subject state.** COSMoS states that position is subject state (`VSPOS`, `IS_SUBJECT_STATE_FOR`), and only its value list differs. Fasting is a value list on most LB DSSs and never separates sibling DSSs, so it cannot show up as an axis. The local LOINC cache has no fasting entries; LOINC is not read on this point.

## Who rates

The standards record who completes or rates an instrument in places that are not connected:

| Where | What is published |
|---|---|
| SDTM CT class (QS, FT, RS, CC) | Stated only for Clinical Classification: the CC domain definition (C228234) says clinical classifications "are based on a trained healthcare professional's observation and clinical judgement". The QS definition describes structure and scoring, FT task-based evaluations, RS response to therapy; none names a rater. The class category codelists QSCAT, FTCAT, CCCAT are defined only as "A grouping of observations within the … domain". |
| SDTM CT Evaluator (EVAL, C78735) | 65 roles, from STUDY SUBJECT and PARENT to INVESTIGATOR and RATER. COSMoS assigns `QSEVAL` = CAREGIVER on 4 DSSs and `RSEVAL` = INVESTIGATOR on 8; elsewhere only value lists. |
| NCIt instrument definitions | Prose. 85 of 253 QS and 11 of 83 RS definitions use a phrase that names a rater; FT none. |
| NCIt clinical outcome assessment types | ClinRO, ObsRO, PerfO and Proxy-reported exist under C142378. No instrument has one as its parent. |

Where an NCIt definition names a rater, the class follows it: QS definitions name self-report, self-administered, parent-report or the patient; RS definitions name a clinician. One QS instrument names only a clinician (Clinical Opiate Withdrawal Scale); three QS instruments name the patient together with a clinician, physician or health professional.

Four instruments changed class between SDTM CT 2026-03-27 and 2026-09-25. Each move matches the rater where NCIt states one:

| NCIt | Instrument | From | To | NCIt definition says |
|---|---|---|---|---|
| C138333 | LPPS SCALE (Lansky) | RS | QS | parent-rated |
| C103515 | ADCS-CGIC | QS | RS | by a clinician; caregiver; clinician rates |
| C135738 | CGI | QS | RS | clinician-determined |
| C105169 | GCGI | QS | RS | (no rater stated) |

The rater phrases are matched with a phrase list of our own and quoted as found; they are not mapped to rater categories. A shared classification from a published ontology is for later.

## Corrections to earlier statements

- [`Observables_Direction.md`](Observables_Direction.md) said that in RS, TR and TU no evaluator value is assigned on any DSS. For TU this is wrong: `TUEVAL` = INVESTIGATOR is assigned on four DSSs, the same on both siblings, so it is still not an axis.
- The same page said who rates is "not a variable at all". It is: SDTM CT has the Evaluator codelist and COSMoS assigns `QSEVAL` and `RSEVAL` on some DSSs. What is missing is the rater as a property of the instrument.
- [Who rates?](examples/who-rates.html) placed the four class moves in SDTM CT 2026-09-25. The repository holds no CT between 2026-03-27 and 2026-09-25, so they are moves since March.

## What comes next

This page is the input to a decision, not the decision. Our own position, separate from what is published, is recorded for the rows that bear on the observable question in a hand-kept sheet, `Variable_Meaning` in [`SDTM_Domain_Metadata.xlsx`](../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx), checked by the notebook (section 4f). Each position states its basis:

- **sources agree** — specimen/system, test detail, binding agent, test method (`--METHOD`); where only COSMoS is read, the basis says so;
- **sources disagree, decided by a stated rule** — scale, test code within one BC;
- **standards silent, open** — category, the analysis method `GFANMETH`, the GF and TR variables above, rater (`QSEVAL`, `RSEVAL`), subject state (`VSPOS`).

The positions are proposed, not yet accepted. Fasting has no row: it never separates sibling DSSs, so no sheet carries it.

The silent rows are where the work will have to go beyond what the data standards say. Bridging study design and data standards needs distinctions — who rates, the subject's state, which response criteria — that the standards carry only in places that are not connected, or not at all.

Phase 2 (more expressive reference files) starts when the positions hold. Events and Interventions get the same pass after the next COSMoS release.
