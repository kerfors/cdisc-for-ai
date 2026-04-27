# The Instrument Layer in COSMoS

Findings on the instrument-shaped Findings group (QS, FT, RS) and their structural anchor in NCIt. Analysis grounded in the cosmos-graph projection of COSMoS. Companion to `COSMoS_Behavioural_Analysis.md`.

*cdisc-for-ai project, April 2026*

---

## 1. Question

The behavioural analysis classified QS, FT and RS as Instrument Findings: one row per question or item within a standardised instrument, hierarchy as the primary axis, the BC layer doing the grouping work that the DSS layer does in specimen-shaped domains. Two open questions about that layer:

1. Is the COSMoS hierarchy internally complete for instrument BCs, and how does the parent chain relate to the multi-value `bc_categories` field?
2. Where does the COSMoS instrument layer sit relative to NCIt's own structural classification?

Both answered with self-contained probes against the cosmos-graph projection (BC, BC_Parents, BC_Categories sheets) and the cached NCIt FLAT file. No live API dependencies.

---

## 2. Internal hierarchy

The cosmos-graph `BC_Parents` sheet resolves every parent edge to a BC in the same projection — the hierarchy is internally complete, depth 0 to 4, most BCs at depth 1.

`BC_Categories` carries many edges to BCs that are not in the BC's parent chain. These off-chain edges are not defects. Linda confirmed in the BC group LinkedIn thread that the multi-value `bc_categories` field is the COSMoS working group's intended grouping mechanism, distinct from structural ancestry by design.

| Relation | What it encodes | What it answers |
|---|---|---|
| `BC_Parents` | Structural ancestry, single chain to root | "Where does this BC sit in the type tree" |
| `BC_Categories` | Cross-cutting grouping tags, multi-value | "What other groupings does this BC participate in" |

For the instrument layer specifically, `BC_Categories` is where the instrument-family grouping lives. A 6MWT distance question's structural ancestry runs `Clinical or Research Assessment Question → CDISC QRS Instruments Questions → 6MWT Functional Test Question`. Its membership in the "6 Minute Walk Functional Test" instrument family is reachable only through `BC_Categories`.

---

## 3. NCIt structural anchor

Every tested instrument question-container BC has NCIt concept `C211913` ("CDISC QRS Instruments Questions") as its **direct parent**, not merely a distant ancestor. Tested across nine instrument families (6MWT, ADAS-Cog, AIMS, APACHE II, CES, EQ-5D-5L, HAMA, KPS, Tanner Scale-Boy): 9 of 9 with `C211913` as the only direct parent in the NCIt FLAT.

Reversing the relation: 365 NCIt concepts have `C211913` as their direct parent. COSMoS materialises 20 of these as BCs, with byte-identical names. The instrument question-container layer in COSMoS is therefore a verbatim subset of an NCIt structural class — same answer from either side.

The coverage gap is explicit: 345 NCIt concepts under C211913 are not yet materialised as COSMoS BCs. Real instruments with NCIt identity but no COSMoS specification.

---

## 4. SDTM-side grouping

The cosmos-graph pin pivot exposes `CAT_value` (`--CAT`) and `SCAT_value` (`--SCAT`) — the single-value SDTM-side grouping fields published in CDISC controlled terminology. Distribution differs across QS, FT, RS:

| Field | QS | FT | RS |
|---|---|---|---|
| `CAT_value` (`--CAT`) | 0 of 17 | 23 of 23 | 0 of 135 |
| `SCAT_value` (`--SCAT`) | 17 of 17 | 11 of 23 | 135 of 135 |

For QS and RS, `--CAT` is empty and `--SCAT` carries the entire SDTM-side grouping load. For FT, `--CAT` holds the instrument family (e.g. `ADAS-COG`) and `--SCAT` holds a subscale within it.

**What `--SCAT` carries** — three patterns, with subscale encoded two different ways:

- **Instrument family** when `--CAT` empty (RS: `APACHE II`, `BPRS-A`).
- **Subscale within an instrument**, with `--CAT` carrying the family (FT ADAS-Cog: `--CAT = ADAS-COG`, `--SCAT = COMMANDS`). Clean two-level grouping.
- **Subscale within an instrument**, with `--CAT` empty (RS AIMS: `--SCAT = DENTAL STATUS`, `FACIAL AND ORAL MOVEMENTS`; no family in `--CAT`). Same structural decomposition as ADAS-Cog, different encoding — an inconsistency in COSMoS.
- **Classification system**, for cross-instrument response criteria: `RECIST 1.1`, `LUGANO CLASSIFICATION`, `RANO`. Scoring frameworks, not instruments.

**Two CT codelist sub-patterns.** SDTM CT publishes the instrument layer via two organisation patterns:

- **Per-instrument codelists.** Each instrument has its own non-extensible codelist (`ADCTC`, `AIMSTC`, `CESTC`). 1:1 between TESTCD and Dataset Specialization. 150 of 175 instrument-scope DSS rows. Most of QS, all of FT, most of RS.
- **Extensible domain-level `RSTESTCD` codelist plus classification framework.** Some instrument-shaped data uses the extensible `RSTESTCD` codelist with the framework recorded in `--SCAT`. 21 of 175 rows. The same TESTCD (e.g. `OVRLRESP`) can appear in multiple Dataset Specializations, one per criteria framework.

The remaining 4 of 175 rows (TTS Acceptability Survey, LZZT example study) have TESTCDs not in any published SDTM CT codelist — example-study artefacts.

**Two parallel structural anchors.** NCIt's `C211913` is the structural anchor for the COSMoS instrument layer (section 3). SDTM `--SCAT` is a parallel anchor for the same grouping work, rooted in CDISC controlled terminology. NCIt covers the question-container concepts but not the subscale decomposition; SDTM CT covers the subscale grouping but not the BC-level identity. Complementary, not redundant.

---

## 5. The identifier asymmetry

`BC_Categories` is the working group's confirmed grouping mechanism, but the tokens it carries are labels, not addressable identifiers. Some labels coincide with `bc_short_name` values and resolve to a COSMoS BC ID and NCIt code; most do not.

Instrument-scope DSS rows use 99 distinct category tokens. 40 are also `bc_short_name` values (resolve to identifiers). The remaining 59 are pure labels with no identifier anywhere. Every one of the 175 instrument DSS rows uses at least one pure-label category in its grouping set.

Long-form names tend to be the identifier-bearing tokens. `6 Minute Walk Functional Test` is a BC with an NCIt code; `6MWT` is a label. `Alzheimer's Disease Assessment Scale - Cognitive` resolves to a BC; `ADAS-Cog`, `ADC`, and the codelist short name `ADCTC` do not. Multiple tokens reach the same instrument family, of which typically only the long form carries identity.

A query like "all questions in the ADAS-Cog instrument" must choose between `category = 'ADAS-Cog'` (label, no identifier) and `category = 'ADAS-Cog CDISC Version Functional Test Question'` (BC, identifier). Both reach the same set in current data, but the label path is fragile against renaming, abbreviation drift, and CDISC versioning. No machine-readable signal that the two are equivalent or which is canonical.

A persistent identifier on the grouping itself, not just the BCs that participate in it, would resolve this. Same architectural request as resolvable `DS_Code` URIs, applied one layer up.

---

## 6. Operationalised in

The findings above are now operationalised in:

- [`cosmos-graph/`](../../cosmos-graph/) — multi-sheet projection of COSMoS into BC, BC_Parents, BC_Categories, DSS, Variables, Codelists. The structural facts in sections 2–4 are queryable directly against this projection.
- [`sdtm-findings-graph/Instrument_Findings.xlsx`](../../sdtm-findings-graph/machine_actionable/Instrument_Findings.xlsx) — instrument-based Findings consumer, four-sheet design (Test_Identity, Measurement_Specs, BC_Categories, BC_Parents). Carries the chocolate C20993 and copper C211913 anchors per row plus the `--SCAT` framework split for the `RSTESTCD` sub-pattern.
- [`docs/6MWT_NCIt_Story.html`](../../docs/6MWT_NCIt_Story.html) and [`docs/6MWT_COSMoS_Story.html`](../../docs/6MWT_COSMoS_Story.html) — visual case studies.

The identifier asymmetry described in section 5 remains an open architectural thread.

---

## 7. Fact box

Numbers reflect the data current at time of analysis.

| Fact | Value |
|---|---|
| Tested instrument question containers | 9 (all with C211913 as direct parent) |
| NCIt direct children of C211913 | 365 |
| C211913 children materialised as COSMoS BCs | 20 (byte-identical names) |
| `--CAT` populated, FT | 23 of 23 |
| `--CAT` populated, QS and RS | 0 of 152 |
| `--SCAT` populated, instrument scope | 163 of 175 (93%) |
| DSS rows in per-instrument codelists | 150 of 175 |
| DSS rows in domain-level `RSTESTCD` codelist | 21 of 175 |
| DSS rows in LZZT example study (no published CT) | 4 of 175 |
| Multi-framework TESTCDs (RSTESTCD sub-pattern) | 4 (NEWLIND, NTRGRESP, OVRLRESP, TRGRESP) |
| Distinct criteria frameworks in RS `--SCAT` | 3 (RECIST 1.1, LUGANO CLASSIFICATION, RANO) |
| Distinct category tokens (instrument scope) | 99 |
| Tokens that are also `bc_short_name` values (have ID) | 40 |
| Pure-label tokens (no identifier) | 59 |
| Instrument DSS rows using ≥1 pure-label category | 175 of 175 |
