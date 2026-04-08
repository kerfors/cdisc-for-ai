# The Instrument Layer in COSMoS

Insights from `COSMoS_BC_Parent_Resolution.ipynb` and `COSMoS_BC_NCIt_Source_Probe.ipynb`. Companion to `COSMoS_Behavioural_Analysis.md`, focused on the instrument-shaped Findings group (QS, FT, RS) and their structural anchor in NCIt.

*cdisc-for-ai project, April 2026*

---

## 1. Question

The behavioural analysis classified QS, FT and RS as Instrument Findings: one row per question or item within a standardised instrument, hierarchy as the primary axis, the BC layer doing the grouping work that the DSS layer does in specimen-shaped domains. This document closes two open questions about that layer:

1. Is the COSMoS hierarchy internally complete for instrument BCs, and how does the direct parent relate to the multi-value `Categories` field?
2. Where does the COSMoS instrument layer sit relative to NCIt's own structural classification?

Both questions are answered with self-contained probes against published data: COSMoS BC_DSS for the first, the cached NCIt FLAT file for the second. No live API dependencies.

---

## 2. Internal hierarchy

`Parent_Label` resolves to a `BC_Name` in the same file for every BC that has one set. The hierarchy is internally complete, with no orphaned references. Depth ranges from root nodes to four levels, with the bulk of BCs at depth one.

`Categories` carries a substantial number of edges to BCs that are not in the BC's direct parent chain. These off-chain edges are not defects. Linda confirmed in the BC group LinkedIn thread that the multi-value `Categories` field is the COSMoS working group's intended grouping mechanism, distinct from structural ancestry by design.

The two relations carry different information:

| Relation | What it encodes | What it answers |
|---|---|---|
| `Parent_Label` / `Hierarchy_Path` | Structural ancestry, single chain to root | "Where does this BC sit in the type tree" |
| `Categories` | Cross-cutting grouping tags, multi-value | "What other groupings does this BC participate in" |

For the instrument layer specifically, `Categories` is where the instrument-family grouping lives. A 6MWT distance question's structural ancestry is "Clinical or Research Assessment Question, CDISC QRS Instruments Questions, 6MWT Functional Test Question". Its membership in the "6 Minute Walk Functional Test" instrument family is reachable only through `Categories`.

---

## 3. NCIt structural anchor

Every tested instrument question-container BC has NCIt concept `C211913` ("CDISC QRS Instruments Questions") as its **direct parent**, not merely a distant ancestor. Tested across nine instrument families covering functional tests, questionnaires and clinical classifications: 6MWT, ADAS-Cog, AIMS, APACHE II, CES, EQ-5D-5L, HAMA, KPS, Tanner Scale-Boy. Result: 9 of 9 with `Under_C211913 = True` and `C211913` as the only direct parent in the NCIt FLAT.

Reversing the relation in NCIt: 365 concepts have `C211913` as their direct parent. COSMoS materializes 20 of these 365 as BCs. The 20 BC names are byte-identical to the corresponding NCIt preferred terms; no COSMoS renaming.

The instrument question-container layer in COSMoS is therefore a verbatim subset of an existing NCIt structural class. Two consequences:

1. **No interpretive distance.** Asking "is this NCIt concept a CDISC QRS instrument question container" can be answered from NCIt alone (parent = C211913) or from COSMoS (BC name match), and the two answers agree.
2. **The coverage gap is explicit.** 345 NCIt concepts under C211913 are not yet materialized as COSMoS BCs. These are real instruments with NCIt identity but no COSMoS specification.

---

## 4. SDTM-side grouping

Alongside the multi-value `Categories` field, BC_DSS carries two single-value fields that map to SDTM submission values: `COSMoS_Category` for `--CAT` and `COSMoS_Subcategory` for `--SCAT`. These are the values that go into the SDTM dataset columns; they are not the COSMoS-side grouping mechanism described in sections 2 and 5, but a parallel SDTM-side mechanism rooted in published controlled terminology.

**Distribution across instrument domains.** The two fields are populated very differently across QS, FT and RS:

| Field | QS | FT | RS |
|---|---|---|---|
| `COSMoS_Category` (`--CAT`) | 0 of 17 | 23 of 23 | 0 of 135 |
| `COSMoS_Subcategory` (`--SCAT`) | 17 of 17 | 11 of 23 | 135 of 135 |

For QS and RS, `--CAT` is empty and `--SCAT` carries the entire SDTM-side grouping load. For FT, `--CAT` holds the instrument family (e.g. `ADAS-COG`) and `--SCAT` holds a subscale within it (e.g. `COMMANDS`, `CONSTRUCTIONAL PRAXIS`). Across the full instrument scope, `--SCAT` is populated for 163 of 175 DSS rows (93%).

**What --SCAT carries.** Three patterns visible in the populated rows, with the subscale pattern encoded two different ways:

- **Instrument family**, when `--CAT` is empty. Examples from RS: `APACHE II`, `ATLAS`, `BPRS-A`. The instrument family identity migrates into `--SCAT` because there is no `--CAT` slot to put it in.
- **Subscale within an instrument, with `--CAT` carrying the family.** Example from FT: `--CAT = ADAS-COG`, `--SCAT = COMMANDS` or `CONSTRUCTIONAL PRAXIS` or `WORD RECALL TASK`. The instrument family is the `--CAT` value; the subscale is the `--SCAT` value. Clean two-level grouping.
- **Subscale within an instrument, with `--CAT` empty.** Example from RS: AIMS subscales `DENTAL STATUS`, `FACIAL AND ORAL MOVEMENTS`, `EXTREMITY MOVEMENTS`, `TRUNK MOVEMENTS`, `GLOBAL JUDGMENTS`. The subscale is in `--SCAT`, but there is no `--CAT` value carrying the AIMS instrument family. Same structural decomposition as ADAS-Cog, different SDTM-side encoding. This is an inconsistency in COSMoS: both instruments fan out by subscale, but only one uses the `--CAT` slot to record the family identity.
- **Classification system**, for cross-instrument response criteria. Examples: `RECIST 1.1`, `LUGANO CLASSIFICATION`, `RANO`. These are not instruments in the questionnaire sense; they are scoring frameworks applied to imaging or clinical assessment data.

**Two CT codelist sub-patterns.** SDTM CT publishes the instrument layer via two different codelist organisation patterns, and the COSMoS BC_DSS straddles both:

- **Per-instrument codelists.** Each instrument has its own non-extensible CT codelist (`ADCTC` for ADAS-Cog, `AIMSTC` for AIMS, `CESTC` for CES, etc.). Each TESTCD in such a codelist is one specific question in one specific instrument. 150 of the 175 instrument-scope DSS rows belong here, and they map 1:1 between TESTCD and Dataset Specialization. Most of QS, all of FT, and most of RS.
- **Extensible domain-level RSTESTCD codelist plus classification framework.** Some instrument-shaped data is published in the extensible `RSTESTCD` codelist instead, with the classification framework (RECIST 1.1, LUGANO CLASSIFICATION, RANO) recorded in `--SCAT` rather than in the codelist identity. 21 of the 175 instrument-scope DSS rows belong here. The same TESTCD (e.g. `OVRLRESP` for "Overall Response") can appear in multiple Dataset Specializations, one per criteria framework.

The remaining 4 of 175 rows (TTS Acceptability Survey question containers tied to the LZZT example study) have TESTCDs that are not in any published SDTM CT codelist. These appear to be example-study artifacts in the COSMoS export and are flagged as a separate COSMoS data quality observation.

**Classification framework as a fan-out axis.** In the domain-level RSTESTCD sub-pattern, the same BC and TESTCD can fan out into multiple Dataset Specializations distinguished only by the criteria framework. `OVRLRESP` ("Overall Response") is one BC with three DSSs: one each for RECIST 1.1, LUGANO CLASSIFICATION, and RANO. `TRGRESP`, `NEWLIND`, and `NTRGRESP` show the same multi-framework pattern. Same conceptual measurement, multiple operational specifications, the framework field disambiguates which one applies in a given study. This is a fan-out axis structurally parallel to the specimen, method, and result-scale axes named in `COSMoS_Behavioural_Analysis.md`, but specific to the RS classification-framework sub-pattern.

**Two parallel structural anchors.** Section 3 established NCIt's `C211913` as the structural anchor for the COSMoS instrument layer. This section establishes SDTM `--SCAT` as a parallel anchor for the same grouping work, rooted in CDISC controlled terminology rather than NCIt class hierarchy. Neither anchor is sufficient on its own: NCIt covers the question-container concepts but not the subscale decomposition; SDTM CT covers the subscale grouping but not the BC-level identity. They cover complementary aspects of the same instrument structure.

**Contrast with section 6.** Unlike `Categories` tokens, `--SCAT` values are SDTM CT submission values with provenance and stability through the published codelist. They have NCIt codes via the SDTM CT to NCIt mapping. Where COSMoS `Categories` is a label-based grouping that lacks addressable identity for the grouping itself, SDTM `--SCAT` provides exactly that addressability for a subset of the same grouping concepts. This is a partial structural answer to the identifier asymmetry, available now and underused.

---

## 5. Implications for an instrument consumer file

The two notebooks establish structural facts. Translating those facts into a consumer file requires four design choices.

### 5.1 Scope boundary

Two candidate scopes exist:

- **C211913 children only.** Strictly the question-container layer under "CDISC QRS Instruments Questions". 20 materialized BCs as starting set. Tight, defensible, anchored in NCIt structure.
- **All instrument-shaped Findings.** The full QS, FT, RS group as classified in the behavioural analysis. Larger, more inclusive, but requires the consumer to understand the behavioural classification.

Recommendation: scope to the QS, FT, RS domains as classified in the Domain Pattern Inventory, and within that, surface C211913 ancestry as a column. The behavioural classification is the consumer-facing scope; the NCIt anchor is metadata that lets sponsors verify alignment.

**Note on RS heterogeneity.** As section 4 establishes, RS is structurally heterogeneous. Some instrument-shaped RS data lives in per-instrument codelists (AIMS, BPRS-A, KFSS and others), and some lives in the extensible `RSTESTCD` codelist with the criteria framework recorded in `--SCAT` (RECIST 1.1, LUGANO CLASSIFICATION, RANO). The consumer file scope covers both. This means the green-side input is not just `SDTM_Instrument_Identity.xlsx` but also the RS subset of `SDTM_Test_Identity.xlsx` for the classification-framework rows.

### 5.2 Row grain

For most of the instrument layer (per-instrument codelists), each BC has one Dataset Specialization with `DS_Code = TESTCD`. For the classification-framework sub-pattern in RS (section 4), a single TESTCD can fan out into multiple Dataset Specializations, one per criteria framework. The row grain choice has to handle both cases.

**Recommendation: one row per Dataset Specialization, parallel to `Specimen_Findings.ipynb`.** For per-instrument codelist rows, this is one row per question (TESTCD = DSS 1:1). For the classification-framework sub-pattern, a single TESTCD can produce multiple rows: `OVRLRESP` produces three rows, one each for RECIST 1.1, LUGANO CLASSIFICATION, and RANO.

This preserves the framework distinction at row grain and avoids the silent flattening that would occur if multi-framework DSSs were aggregated. It matches the established consumer-track pattern in `Specimen_Findings.ipynb`, where the row grain is one per Dataset Specialization regardless of how many DSSs share a TESTCD. An instrument-first or framework-first summary view can be provided as an additional sheet later without restructuring the primary data.

### 5.3 Coverage representation

Whether to include the 345 NCIt-only C211913 children as reference rows alongside the 20 materialized BCs.

Recommendation: include them. Same pattern as the lab coverage gap framing already in the project README. Surfacing the gap is exactly the value-add for sponsors with internal instrument catalogues, who can bridge the gap themselves. The rows would carry NCIt code, NCIt label, and a flag distinguishing materialized from reference-only.

### 5.4 Grouping exposure

`Categories` carries the instrument-family edges. Three options for the consumer file:

- **Multi-value column.** Single column with semicolon-separated values. Compact, queryable with substring or membership tests, matches the source format.
- **Separate sheet.** A two-column edge list (BC_Name, Category). Normalised, easier to filter and join.
- **Both.** Multi-value column on the primary sheet, edge list on a secondary sheet for those who need normalised access.

Recommendation: both. The multi-value column on the question rows preserves locality and matches what consumers already see in BC_DSS. The edge list makes the grouping queryable without parsing. Same trade-off the SDTM CT extract already makes between the wide and long forms.

---

## 6. The identifier asymmetry

`Categories` is the working group's confirmed grouping mechanism, but the tokens it carries are labels, not addressable identifiers. Some of those labels coincide with `BC_Name` values and so carry an identifier indirectly; most do not.

**Numbers from the current data.** Instrument-scope DSS rows use 99 distinct `Categories` tokens. 40 of the 99 are also `BC_Name` values, so they resolve to a COSMoS BC ID and an NCIt code. The remaining 59 are pure labels with no identifier anywhere. Every one of the 175 instrument DSS rows uses at least one pure-label Category in its grouping set.

**Pattern in the gap.** Long-form instrument names tend to be the identifier-bearing tokens. `6 Minute Walk Functional Test` is a BC with an NCIt code; `6MWT` is a label. `Alzheimer's Disease Assessment Scale - Cognitive` resolves to a BC; `ADAS-Cog`, `ADC`, and the codelist short name `ADCTC` do not. The same conceptual instrument family is reachable via multiple Category tokens, of which typically only the long form carries identity.

**Why this matters.** A sponsor or AI system querying "all questions in the ADAS-Cog instrument" must choose between `Category = 'ADAS-Cog'` (label, no identifier, no provenance) and `Category = 'ADAS-Cog CDISC Version Functional Test Question'` (BC, identifier, provenance). The two reach the same set in the current data, but the label path is fragile against renaming, abbreviation drift, and CDISC versioning. There is no machine-readable signal that the two are equivalent or which is canonical.

**What a fix would look like.** A persistent identifier on the grouping itself, not just the BCs that participate in it. This is the same architectural request as resolvable `DS_Code` URIs but applied one layer up: groupings as first-class citizens with addressable identity, not labels assembled from string conventions. With identifiers, the multiple tokens for one instrument family become aliases of a single thing rather than independent strings that happen to converge.

---

## 7. Open thread

The C211913 ancestry discriminator is empirically confirmed without API calls. The complementary P322 ("Contributing_Source = CDISC") discriminator is deferred. P322 is not in the cached NCIt FLAT file. Recovery options: an EVS REST recovery from current degradation, a property-specific extract on the NCI FTP, or OWL parsing. Not blocking for the consumer file since C211913 ancestry is sufficient for the structural layer claim.

The identifier asymmetry described in section 6 is the second standing dialogue topic for the upcoming community call, alongside the broader request for resolvable `DS_Code` URIs. Both are about making addressable identity a first-class property of COSMoS rather than a coincidence of naming.

---

## 8. Fact box

Numbers below reflect the data current at time of analysis. The notebooks are the authoritative source for current counts.

| Fact | Value |
|---|---|
| BCs in COSMoS_BC_DSS | 1,127 |
| BCs with `Parent_Label` set | 888 |
| `Parent_Label` resolution rate | 100% |
| Hierarchy depth range | 0 to 4 |
| BCs with off-chain `Categories` to BCs | 426 |
| Total off-chain Category-to-BC edges | 730 |
| Tested instrument question containers | 9 |
| Containers with C211913 as direct parent | 9 of 9 |
| NCIt direct children of C211913 | 365 |
| C211913 children materialized as COSMoS BCs | 20 |
| BC names matching NCIt label exactly | 20 of 20 |
| `COSMoS_Category` (`--CAT`) populated, FT | 23 of 23 |
| `COSMoS_Category` (`--CAT`) populated, QS and RS | 0 of 152 |
| `COSMoS_Subcategory` (`--SCAT`) populated, QS and RS | 152 of 152 |
| `COSMoS_Subcategory` (`--SCAT`) populated, instrument scope total | 163 of 175 |
| Yellow instrument DSS rows in per-instrument SDTM CT codelists | 150 of 175 |
| Yellow instrument DSS rows in domain-level `RSTESTCD` codelist | 21 of 175 |
| Yellow instrument DSS rows not in published SDTM CT (LZZT example) | 4 of 175 |
| Multi-framework TESTCDs in `RSTESTCD` sub-pattern | 4 (NEWLIND, NTRGRESP, OVRLRESP, TRGRESP) |
| Distinct criteria frameworks in RS `--SCAT` | 3 (RECIST 1.1, LUGANO CLASSIFICATION, RANO) |
| Distinct Category tokens (instrument scope) | 99 |
| Tokens that are also `BC_Name` values (have ID) | 40 |
| Pure-label tokens (no identifier) | 59 |
| Instrument DSS rows using ≥1 pure-label Category | 175 of 175 |

---

## 9. Files

- `notebooks/COSMoS_BC_Parent_Resolution.ipynb`: parent self-join, depth profiling, off-chain Category edge inventory.
- `notebooks/COSMoS_BC_NCIt_Source_Probe.ipynb`: C211913 ancestry probe and materialization gap, FLAT-based, no API calls.
- `COSMoS_BC_Parent_Resolution.md`: companion notes on the parent / Categories distinction.
