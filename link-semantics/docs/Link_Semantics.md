# Link semantics — what the links in CDISC CT and COSMoS actually say

**Scope.** What the published content exhibits, measured. No proposals and no
decisions: predicates are chosen in the RDF repositories, with this document as
evidence.

**Evidence.** [`Link_Kind_Audit.ipynb`](../notebooks/Link_Kind_Audit.ipynb) and
[`Code_Collision_Check.ipynb`](../notebooks/Code_Collision_Check.ipynb), with
their workbooks in [`../interim/`](../interim/). Every number in this document
has a cell in one of the two notebooks.

**How to read it.** Part A is the narrative and does not depend on a package
version. Part B is a dated snapshot with the counts. The counts are
package-bound: a change at the next COSMoS or CT package is a finding, not an
error. Section numbers are the same in both parts.

---

# Part A — Findings

## 1. Background

A framework from 2014 (Hussain et al., MIE2014 / CIM2014 workshop; EHR4CR, Open
PHACTS, SALUS and W3C HCLS) argued three things about terminology mappings:

1. A mapping needs a **justification** — why does the equivalence hold?
2. **Inferred mappings can be erroneous** — especially via a hub terminology.
3. **Context matters** — a code can be equivalent in one usage and not in another.

Where this stands today:

- Justification is mainstream. **SSSOM** makes `mapping_justification` a
  required field, with the **SEMAPV** vocabulary (ManualMappingCuration,
  LexicalMatching, MappingChaining, LogicalReasoning, MappingReview, ...). The
  SSSOM paper cites the Open PHACTS justification work as prior art.
- Validation of inferred mappings exists in tooling, not in the standard — for
  example **Boomer**, which searches for a coherent merged ontology and flags
  new equivalences *within* a namespace.
- Context is still open. SSSOM decided that mappings must be universally
  applicable, not context-dependent, because context would make merging much
  harder. For clinical data this means that **context must live in the concept
  you map to, not on the mapping**.

The last point bears on COSMoS: a Dataset Specialization *is* the context. A
code given at DSS level therefore needs no context annotation.

Before any of this can be applied, a simpler question has to be answered: which
of the links in the CDISC content are mappings at all?

## 2. Core finding — one predicate hides eight statements

`skos:exactMatch` is the natural default for "this thing relates to that NCIt
concept". The content in this repository makes at least eight different
statements:

| Link kind | Statement | Mapping? |
|---|---|---|
| `identity` | this thing **is** that NCIt concept (the C-code is its identifier) | no |
| `membership` | this concept is a permissible value in that codelist | no |
| `binding` | this variable draws its values from that codelist | no |
| `denotation` | this model element **means** that concept | no |
| `pinned_value` | this variable is fixed to that value in this specialization | no |
| `value_list` | this variable is restricted to these values in this specialization | no |
| `category_tag` | this BC carries that category token - the object end is a label | no |
| `mapping` | this concept corresponds to a concept in another terminology | yes |

Two of them, `value_list` and `category_tag`, were missed in the first audit
(sections 8 and 6).

There are three provenance classes:

| Class | Meaning | Needs a justification? |
|---|---|---|
| `published` | CDISC / NCI EVS asserts it in a release | no — record the release |
| `derived` | computed by a rule from published inputs | record the rule + inputs |
| `curated` | a judgement | yes |

None of this is declared in the CDISC models. The link kind is inferred from
how each source column behaves. The assignment of kind and class to each column
is authored, in one `INVENTORY` list in the audit notebook. That list is the
part to review; the counts are measured.

Mappings are a very small share of all links. Everything else is identity,
membership, binding, denotation, pinned values, value lists or category tags.
None of these should carry a transitive predicate, and none of them needs a
justification.

## 3. Collision check — where a transitive predicate would bite

The collision check collects every NCIt C-code by the **role** it is used in (BC
identity, DEC identity, TESTCD identity, codelist identity, codelist term,
pinned value, instrument and container anchors, USDM anchor) and looks for
codes used more than once.

**Within a role, identity is clean.** No C-code identifies two different BCs,
two TESTCDs, two DECs or two codelists. Repeats exist in two roles only, and
both are correct by design: a term can sit in several codelists, and a value
can be pinned in many specializations.

The inverse case exists in one role only. No BC, DEC or codelist carries more
than one code, but some TESTCD strings carry two different NCIt codes in
different domains — ALA is Alanine in LB and Acinetobacter lactucae in MB. The
code is a clean identifier; the string a consumer joins on is not.

So there is no hub risk *inside* a role today. It also means that a
non-transitive annotation property costs nothing: no inference that the sources
actually assert would be lost.

**Across roles, reuse is large.** Thousands of codes are used in more than one
role. The largest pair is codelist term and TESTCD identity, which is by design:
a test code is a term in its TESTCD codelist. With one transitive predicate for
all roles, every such pair becomes a statement of equivalence between two
different kinds of subject.

Three cases deserve attention.

**(a) A BC and a Data Element Concept share a C-code.** A small group of codes
is used both as a BC and as a DEC, in most cases with identical labels —
"Race", "Sex", "Adverse Event Yes No Indicator". With one predicate on both, a
BC and its data element concept collapse into one node.

`cosmos-rdf` has met the same group of codes and has taken a position. There
the C-code is the identifier of the node itself, so a code used at two layers
resolves to one node carrying both types. The decision is to accept that merge
and to report the population, not to model around it. For Race, Sex and Ethnic
Group the merge is correct: each is a BC with one DSS in DM and a DEC on one DM
variable, so the concept is the whole content of the observation and there is
nothing for the two roles to be distinct from. The remaining codes are treated
as a curation observation for CDISC, not as a modelling problem: most of them
have no DSS of their own as a BC. The reasoning is in the `cosmos-rdf`
[decision log](https://github.com/kerfors/cosmos-rdf/blob/main/docs/decisions.md)
under "Concepts used at two layers", and the population is listed in its
[known gaps](https://github.com/kerfors/cosmos-rdf/blob/main/docs/known-gaps.md).
This section adds the measurement from the `cdisc-for-ai` side, nothing more.

**(b) Some BCs are NCIt question containers** — section 5.

**(c) USDM and COSMoS share codes.** The same C-code anchors a class or a
property in `usdm_v4.ttl` and is a BC, a test code, a codelist term or a pinned
value on the COSMoS side. Section 4 looks at the pinned values.

Method note: a naive pandas merge matches NaN to NaN and invents pairs for the
BCs and DECs that have no code. Drop nulls on both sides first.

## 4. The TS parameter bridge

Every USDM-anchored code that COSMoS pins as a value is a Trial Summary
parameter. For all but one, the same concept is a **property** in the
study-definition model and a **parameter name pinned as a value** in the
submission model. The exception is Trial Title, which is a **class** on the
USDM side.

This is not a data problem. It is the real join between USDM study design and
SDTM Trial Summary. It is also the clearest case where one predicate cannot
serve both roles: an `owl:ObjectProperty` and a pinned string value would
become the same node.

## 5. Instrument grouping — answered upstream

The BCs whose C-code is also an NCIt question container (under C211913) behave
as a distinct class: no Dataset Specializations, no DECs, all in the category
"QRS Instrument Questions", and all of them parents of item BCs. In none of
them is the instrument concept the parent of the BC. The chain always runs to
the container branch, even though the instrument concept usually exists as a BC
as well.

**This is intentional and documented.**
[`COSMoS_Instrument_Layer.md`](../../cosmos-graph/docs/COSMoS_Instrument_Layer.md)
§8 cites the CDISC Knowledge Base article
[*Searching CDISC Biomedical Concepts*](https://www.cdisc.org/kb/articles/cdisc-published/searching-cdisc-biomedical-concepts).
It states that the NCIt hierarchy is not sufficient for finding all BCs of a
QRS instrument, because NCIt groups the questions under one container and does
not link the instrument to them, and that the `categories` attribute is the
intended retrieval path. Grouping is `categories`; `synonyms` is a search aid
only.

So the link is not missing. What is left is what follows from a label-based
mechanism (section 6). The watch items are already recorded in §8 of that
document.

## 6. Link kind: `category_tag`

`BC_Categories` is a published link whose object end has **no identifier**.
Every category token is a string. Whether a token can be tied to a BC is a
derived question. It is answered here with the mechanism of
`cosmos-graph/notebooks/50_instrument_category_resolution.ipynb` (exact
`bc_short_name`, then a unique `bc_synonyms` match), applied to all tokens and
not only to the instrument scope.

Less than half of the tokens resolve. The most used unresolved tokens are
grouping buckets such as QRS, Trial Summary and Laboratory Tests. They are not
broken links. They name groups that have no identifier anywhere.

This is the CDISC-sanctioned grouping mechanism for QRS instruments, and the
tokens that carry most of the grouping are the ones with nothing to resolve to.
For RDF it forces a choice: mint IRIs for the labels, or keep them as literals
and lose traversal.

## 7. LOINC at two grains

LOINC codes appear at two grains: on the BC (`Coding`) and on the `--LOINC`
variable of a Dataset Specialization. On the DSS, the variable has either one
assigned value, a value list of several codes, or no value. The first audit
counted only the assigned values and missed the specializations that carry
their LOINC codes as a value list. With them included, the figures agree with
the observable LOINC check in `cosmos-bc-dss`.

Glucose shows the pattern. The BC "Glucose Measurement" has no BC-level LOINC.
Some of its specializations pin one code, some list two, and some have a LOINC
variable with no value. One of the pinned codes also sits at BC level on a
different BC, "Urine Glucose Test Strip Measurement" — a BC that is already
specific.

Reading: the **DSS pin is context-bound by construction** — the DSS is the
context, so no mapping annotation is needed — and a **BC-level LOINC appears to
work where the BC itself is specific**. This is not verified across all BCs
with a BC-level LOINC.

What a list of several LOINC codes on one DSS asserts is already measured in
[`COSMoS_Observable_LOINC_Check.xlsx`](../../cosmos-bc-dss/reports/COSMoS_Observable_LOINC_Check.xlsx)
(`Multi_Code_DSS`): all lists stay within one LOINC system and one scale, and
in nearly all of them the codes differ on the LOINC property only, for example
mass against substance concentration. The list reads as one observable at two
LOINC property values, not as two alternative observables.

Only one external system appears in `Coding` in this build: LOINC, all under
`http://loinc.org/`.

## 8. Link kind: `value_list`

A DSS variable can carry a `;`-separated `value_list`. It is a published link
with its own statement — the variable is restricted to these values in this
specialization — between `binding` (the whole codelist) and `pinned_value` (one
value). It never occurs together with an assigned value.

Some of the lists also carry a `subset_codelist` name, for example `NY_NY`.
That is a label on the list, not a separate link.

The object end differs by scope, and this matters for RDF:

- **With a bound codelist**, the values are submission values. They can be
  checked against that codelist and through it reach NCIt concepts. This is not
  measured here; [`COSMoS_Open_Work.md`](../../cosmos-graph/docs/COSMoS_Open_Work.md)
  item 8 records one list with values that the codelist does not govern.
- **Without a codelist**, the values are strings with nothing to resolve to.
- **On a `--LOINC` variable**, they are external codes (section 7).

A variable with a bound codelist is therefore in one of three states:
`assigned` (one value fixed), `value_list` (restricted to a list) or `open`
(the whole codelist). The schema says none of this; every one of these is the
same `SDTMVariable` slot. The assigned rate alone hides the second state.
`--SPEC` is often assigned, but in even more cases the specialization restricts
it to a value list, and it is almost never open. `--FAST` is never assigned and
always carries a value list. This is measured only; no reading is attached to
the states here.

---

# Part B — Snapshot 2026-09-21

**Pins.** `cdisc-for-ai` main at 4f81232, COSMoS package 2026-07-14, SDTM CT
2026-03-27; `usdm-rdf` main at 6334ef2, `usdm_v4.ttl` `owl:versionInfo` v0.7.0.
The SDTM CT release date is not recorded in any input file. It is taken from
the repo README, not from data.

## B2. Link kinds — measured distribution

| Link kind | Provenance | Rows |
|---|---|---|
| identity | published | 13,686 |
| membership | published | 17,607 |
| binding | published | 7,438 |
| denotation | published | 10,791 |
| pinned_value | published | 4,398 |
| value_list | published | 3,000 |
| category_tag | published | 4,382 |
| mapping | published | 105 |
| mapping | derived | 354 |
| mapping | curated | 259 |
| membership | derived | 673 |

**Mappings are 1.1% of all links** (718 of 62,693).

## B3. Collision check

Within-role repeats:

- `codelist_term` — 4,661 codes sit in several codelists (max 12)
- `pinned_value` — 1,146 codes are pinned in many places (C181398 in 256 DSS
  variables)

**17 TESTCD strings carry two different NCIt codes** in different domains: ALA,
APPEAR, COLOR, DCA, DMG, DNA, LYS, MCH, MPV, NNAL, PBG, SE, TEMP, TLC, TLS,
ULCER, UPA.

**5,233 distinct codes are used in more than one role.** Largest pairs:

| Role A | Role B | Shared codes |
|---|---|---|
| codelist_term | testcd_identity | 4,145 |
| codelist_term | pinned_value | 1,305 |
| bc_identity | codelist_term | 1,141 |
| bc_identity | pinned_value | 1,003 |
| bc_identity | testcd_identity | 681 |
| codelist_term | instrument_anchor | 256 |
| bc_identity | container_anchor | 22 |
| bc_identity | usdm_anchor | 22 |
| bc_identity | dec_identity | 19 |

(a) BC and DEC: 19 codes, 12 of them within the same BC. The labels are
identical in 84 of 99 rows.

(c) USDM × COSMoS overlap: 28 codes. By what they anchor in `usdm_v4.ttl`: 14
`owl:Class`, 9 `owl:ObjectProperty`, 5 `owl:DatatypeProperty`. Worked example,
C112038:

| Role | Subject |
|---|---|
| usdm_anchor | `Indication-description` (DatatypeProperty) |
| bc_identity | BC C112038 |
| testcd_identity | INDC |
| codelist_term | TSPARMCD, TSPARM |
| pinned_value | INDIC.TSPARMCD, INDIC.TSPARM |

The NaN-to-NaN merge in the method note concerns the 6 BCs and 2 DECs without a
code.

## B4. The TS parameter bridge — 13 codes

| Code | USDM anchor | USDM type | COSMoS pin (TSPARMCD / TSPARM) |
|---|---|---|---|
| C38114 | Administration-route | ObjectProperty | ROUTE — Route of Administration |
| C49658 | InterventionalStudyDesign-blindingSchema | ObjectProperty | TBLIND — Trial Blinding Schema |
| C49652 | InterventionalStudyDesign-intentTypes | ObjectProperty | TINDTP — Trial Intent Type |
| C49660 | InterventionalStudyDesign-subTypes | ObjectProperty | TTYPE — Trial Type |
| C98746 | InterventionalStudyDesign-model | ObjectProperty | INTMODEL — Intervention Model |
| C98747 | StudyIntervention-type | ObjectProperty | INTTYPE — Intervention Type |
| C112038 | Indication-description | DatatypeProperty | INDIC — Trial Disease/Condition Indication |
| C126065 | ObservationalStudyDesign-timePerspective | ObjectProperty | OBSTIMP |
| C126067 | ObservationalStudyDesign-samplingMethod | ObjectProperty | OBSTSMM |
| C127777 | BiospecimenRetention-includesDNA | DatatypeProperty | BRDNAIND |
| C164620 | BiospecimenRetention-isRetained | DatatypeProperty | BRIND |
| C89081 | Administration-frequency | ObjectProperty | DOSFRQ — Dosing Frequency |
| C49802 | StudyTitle | Class | TITLE — Trial Title |

12 of the 13 are properties on the USDM side (9 `owl:ObjectProperty`, 3
`owl:DatatypeProperty`). The 13th, C49802, is a class. Each code is pinned
twice per parameter (TSPARMCD and TSPARM).

## B5. Question-container BCs — 22

| Property | The 22 | Other BCs |
|---|---|---|
| `bc_type` | all `full_no_ds` | 1,008 `full`, 445 other `full_no_ds` |
| DSS rows | 0 | — |
| DECs | none | — |
| Category | all "QRS Instrument Questions" | — |
| Children | 271 item BCs | — |
| Parent | 21 under C211913, 1 under C91102 | — |

19 of the 22 have a C20993 instrument anchor from the instrument track
(C115409 → C115789, exact). **3 have none**: instrument codelists ADCTC,
AJCC1TC, PASI03TC. For all 19 the instrument concept is itself a BC (C115789 "6
Minute Walk Functional Test 2008 Version", `full_no_ds`).

## B6. Category tokens

| Measure | Count |
|---|---|
| Raw token uses in `BC.bc_categories` | 4,389 |
| Distinct (BC, token) rows in `BC_Categories` | 4,382 |
| BCs with at least one category | 1,475 of 1,475 |
| Distinct category tokens | 408 |
| (instrument scope, per COSMoS_Instrument_Layer.md) | 99 tokens: 40 resolve, 59 pure labels |

The 7 rows of difference are tokens repeated inside one BC's own string.

Resolution of the 408 tokens:

| Status | Tokens | Uses |
|---|---|---|
| `exact_name` | 125 | 1,403 |
| `synonym` | 58 | 474 |
| `synonym_ambiguous` | 3 | 18 |
| `unresolved` | 222 | 2,487 |

Most used unresolved tokens: QRS (290 uses), Trial Summary (192), Laboratory
Tests (186).

## B7. LOINC at two grains

| Measure | Count |
|---|---|
| BCs with a BC-level LOINC (`Coding`) | 105 |
| `--LOINC` variables in DSSs | 151 |
| ... with one assigned value | 98 |
| ... with a value list of several codes | 42 |
| ... with no value | 11 |
| DSSs carrying at least one LOINC | 140 |
| DSS × LOINC pairs | 183 |
| Distinct LOINC codes at DSS level | 180 |
| DSSs with a LOINC whose BC also has a BC-level LOINC | 11 |
| ... of those, BC-level code is among the DSS codes | 11 |
| BCs whose DSSs carry more than one distinct LOINC | 51 |

The first audit saw 98 DSSs and 21 BCs. With the 42 value-list DSSs the figures
agree with the observable LOINC check (140 DSSs, 183 pairs, 42 multi-code
DSSs). In 39 of the 42 lists the codes differ on the LOINC property only (e.g.
ALBSERPL 1751-7;54347-0).

Glucose: BC C105585 has 8 DSSs. GLUCUA pins 25428-4 and GLUCURINPRES pins
2349-9; GLUCBLD, GLUCPE, GLUCSERPL and GLUCURIN each list two codes; GLUCPL and
GLUCSER have a LOINC variable with no value. The same 2349-9 sits at BC level
on NEW_1 "Urine Glucose Test Strip Measurement".

## B8. Value lists and assignment states

3,000 variables carry a value list.

| Scope | Variables | DSSs | Values listed | Distinct values |
|---|---|---|---|---|
| Bound codelist | 2,310 | 896 | 6,686 | 674 |
| No codelist | 648 | 241 | 5,016 | 588 |
| `--LOINC` variable | 42 | 42 | 85 | 83 |

296 of the codelist-bound lists also carry a `subset_codelist` name.

Assignment states, measured on the `Variables` sheet of `COSMoS_Graph.xlsx`
(13,922 rows, 1,475 specializations). 7,438 variables are CT-bound: 4,301
assigned, 2,310 value_list, 827 open. By variable suffix, for the 27 suffixes
with at least 30 CT-bound rows (7,163 of the 7,438; all 68 suffixes are in the
`Assignment_States` sheet):

| Variable suffix | CT-bound | assigned | value_list | open | Assigned rate |
|---|---|---|---|---|---|
| `--TESTCD` | 1,257 | 1,257 | 0 | 0 | 1.00 |
| `--TEST` | 1,257 | 1,257 | 0 | 0 | 1.00 |
| `--BDAGNT` | 326 | 326 | 0 | 0 | 1.00 |
| `--CAT` | 218 | 218 | 0 | 0 | 1.00 |
| `--PARMCD` | 129 | 129 | 0 | 0 | 1.00 |
| `--PARM` | 129 | 129 | 0 | 0 | 1.00 |
| `--TSTDTL` | 168 | 164 | 0 | 4 | 0.98 |
| `--DECOD` | 42 | 36 | 4 | 2 | 0.86 |
| `--SYMTYP` | 33 | 23 | 0 | 10 | 0.70 |
| `--SPEC` | 541 | 239 | 295 | 7 | 0.44 |
| `--STRESU` | 557 | 238 | 311 | 8 | 0.43 |
| `--ORRESU` | 576 | 123 | 452 | 1 | 0.21 |
| `--METHOD` | 485 | 87 | 332 | 66 | 0.18 |
| `--EVAL` | 109 | 19 | 90 | 0 | 0.17 |
| `--LOC` | 133 | 19 | 30 | 84 | 0.14 |
| `--STRESC` | 260 | 4 | 103 | 153 | 0.02 |
| `--ORRES` | 246 | 4 | 90 | 152 | 0.02 |
| `--FAST` | 131 | 0 | 131 | 0 | 0.00 |
| `--LAT` | 108 | 0 | 79 | 29 | 0.00 |
| `--STRESN` | 103 | 0 | 8 | 95 | 0.00 |
| `--VCDREF` | 69 | 0 | 0 | 69 | 0.00 |
| `--TSTOPO` | 64 | 0 | 64 | 0 | 0.00 |
| `--VAL` | 56 | 0 | 29 | 27 | 0.00 |
| `--PRESP` | 43 | 0 | 38 | 5 | 0.00 |
| `--EVALID` | 42 | 0 | 42 | 0 | 0.00 |
| `--OCCUR` | 41 | 0 | 36 | 5 | 0.00 |
| `--POS` | 40 | 0 | 9 | 31 | 0.00 |
