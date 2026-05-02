# Clinical-Knowledge Reference Map for a Modality Family — Prompt Template

Build a sponsor-agnostic clinical-knowledge reference map for a single procedure or modality family, with CDISC COSMoS coverage assessment. Output is a portable Excel artefact suitable for the `cdisc-for-ai` repository.

The reference map separates clinical truth from standards coverage. Layer 1 captures the procedure+measurement pairs as they exist in clinical practice and the published evidence base. Layer 2 assesses CDISC COSMoS BC + DSS coverage of those pairs as a separate concern. No sponsor catalog references appear anywhere in the output.

---

## Inputs required

- `DSS_View.xlsx` — CDISC COSMoS BC + DSS package (sheets: ReadMe, Test_Identity, Measurement_Specs). Use the latest publicly available release.
- Modality family scope — single concrete scope, stated explicitly. Examples: "MRI of liver disease", "Hand and foot X-ray for RA structural progression", "DXA for osteoporosis", "PET for amyloid quantification", "Echocardiography for cardiac function".

No sponsor inputs. No internal catalog files. The output must be replicable by any reader with access to the public COSMoS package.

---

## Stage 1 — Clinical-knowledge pair inventory

Build the procedure / measurement pair list for the chosen family from the published evidence base. Anchor each pair on regulatory guidance, consortium standards, and peer-reviewed literature. Do not pre-filter by COSMoS coverage and do not consider any sponsor catalog.

For each pair, capture:

- **Procedure** — including any acquisition modifier that is part of the clinical standard (e.g. "MRI of liver (multiphase contrast-enhanced)", "MR Elastography of liver", "MRI of liver and heart (combined)" for dual-organ acquisitions).
- **Measurement (abbrev)** — the standard name as used in the literature, with abbreviation if commonly used (e.g. "Proton Density Fat Fraction (PDFF)", "Liver Stiffness Measurement (LSM)").
- **Kind** — `QB` quantitative biomarker · `RC` response criterion · `STR` structural finding/score · `CSI` composite score/index · `STG` staging or categorisation system · `SEV` severity grade.
- **Anatomical target** — the tissue or structure measured, with ROI specifics if standard practice (e.g. "Liver parenchyma (whole-organ or segmental ROI)", "Mid-ventricular cardiac septum (single slice)").
- **Clinical question / endpoint use** — the clinical decision the measurement supports. Include consensus thresholds or cutoffs where they exist (e.g. for LSM: "≥3.6 kPa significant fibrosis (≥F2); ≥4.7 kPa advanced fibrosis (≥F3)"). Quantitative cutoffs add substantial value for a reference map.
- **Indications (clinical-truth)** — every disease or condition where the pair has documented use in trials or clinical practice. List exhaustively from clinical literature, not filtered by any portfolio. Use bullet-style separator (`·`) for readability.
- **Status** — evidence maturity in the clinical literature:
  - `REG` regulatory-recognised as trial endpoint (FDA, EMA, PMDA)
  - `CS` consortium standard (RECIST WG, ACR, ISCD, AASLD, EASL, IBSG, etc.) — published consensus
  - `WCT` widespread clinical-trial use, no formal consortium endorsement
  - `SPC` specialty-society consensus (e.g. SCMR for cardiac MRI mapping)
  - `EM` emerging — recently introduced, in regulatory qualification, or vendor-specific
- **Key evidence references** — primary citations supporting the pair's clinical-truth status. Include at minimum: any regulatory guidance that names the measurement, the relevant consortium standard or society guidance, and one or two seminal validation papers. **All references must be cite-checked at this stage** (see Stage 1b below).
- **Notes** — anything worth surfacing that does not fit the structured columns: vendor-specific implementations, regulatory qualification path, methodological notes, alternative methods superseded by this one.

Acknowledge correctly procedure-only entries. Some procedures in a family legitimately produce no structured measurement (e.g. MRI w/o contrast as eligibility check, plain X-ray for fracture screening). Document them as procedure-only; do not force-author a measurement leaf.

### Stage 1b — Cite-check the references

Every reference cited in the inventory must be verified before the deliverable is produced. Treat this as a hard gate — uncited or hallucinated references undermine the credibility of the public artefact and cannot be retrofitted later.

For each reference cited:

1. **Verify the citation exists** by web search against an authoritative source. PubMed for journal articles. The publishing body's website for guidance documents (FDA at fda.gov, EMA at ema.europa.eu, ACR at acr.org, AASLD at aasldpubs.onlinelibrary.wiley.com, EASL at journal-of-hepatology.eu, RECIST WG / EORTC, QIBA at qibawiki.rsna.org). Society guidelines on the society site or the journal of record.
2. **Verify the year and authorship** match what is cited. Common failure modes: citing a guideline by an older year when only the newer version is accessible; conflating a working-group statement with a journal publication; citing a first author when later versions have different first authors.
3. **Verify the cited claim** is actually supported by the document at the level needed. A guideline that mentions a measurement in passing is not the same as a guideline that recommends it as an endpoint. Be precise about what the citation supports.
4. **Replace, correct, or remove** any reference that fails verification. If the underlying claim is correct but the original citation is wrong, find the correct citation. If the underlying claim cannot be supported by any verifiable reference, remove it from the map and note the gap.
5. **Capture the verification trail** — for each reference, note the source URL or database identifier (PubMed ID, DOI, official URL) so that a reader can re-verify. This goes in the provenance, not in the per-pair Notes column, but it must exist before the deliverable is finalised.

Do not skip this stage even for "well-known" references. Familiar names produce more hallucinations, not fewer, because the LLM will pattern-match to a plausible-sounding citation that does not exist.

Sources to prefer: PubMed (`https://pubmed.ncbi.nlm.nih.gov/`), DOI resolution (`https://doi.org/`), publishing body official sites, the journal of record. Avoid relying on aggregator summaries, lecture slides, or non-primary sources for citation verification.

---

## Stage 2 — CDISC COSMoS coverage assessment

For each pair from Stage 1, look up `DSS_View.xlsx`. Anchor on the measurement first, the procedure second.

For each pair, capture:

- **COSMoS DSS** — `ds_id` if present, "absent" if no DSS exists for the measurement-anatomy combination. If a DSS exists but with anatomy-agnostic pinning (e.g. TR/TU LDIAM with MRI in the METHOD value_list), state this explicitly — it is not the same as a hepatic-pinned DSS.
- **DSS short name** — the `ds_short_name` value from COSMoS, copied verbatim.
- **Domain** — the SDTM domain placement (`UR`, `MK`, `LB`, etc.) with the human-readable expansion in parentheses.
- **TESTCD · NCIt · METHOD** — the published TESTCD, the NCIt code from `bc_id`, and the METHOD value or value_list. Where METHOD is a list, capture all values.
- **Coverage tier** — categorisation:
  - **Aligned** — DSS exists; pair maps end-to-end.
  - **Catalog ahead of standards** — DSS absent despite mature clinical evidence (REG or CS status). Notable gap.
  - **Greenfield** — DSS absent and clinical evidence is emerging or specialised. Lower-priority gap.
  - **Architectural observation flag** — DSS exists but with a modelling decision worth surfacing (e.g. domain placement does not match clinical use).
- **Architectural observations** — modelling decisions that deserve explicit surfacing. Domain placements that differ from clinical use. METHOD value_list patterns that group acquisitions across modalities. Anatomy-agnostic vs anatomy-pinned modelling differences. Dual-organ or composite-acquisition patterns. These observations are a primary output of the map, not a side note. They are the productive material for any conversation with the COSMoS authoring community.

---

## Stage 3 — Architectural observations summary

After Stage 2, draft a short summary of architectural observations across the family. Common patterns worth capturing:

- **Domain placements that do not match clinical use.** Surfaced as flags (e.g. PDFF in UR domain for a hepatic biomarker).
- **REG-status pairs without DSS coverage.** Strongest candidates for COSMoS authoring proposal because the regulatory status indicates clinical maturity.
- **CS-status published-consensus pairs without DSS coverage.** Strong candidates because the structure is already standardised externally.
- **Dual-organ or composite-acquisition patterns.** Raise modelling questions for COSMoS that go beyond "author another DSS" — for example, whether a single DSS with two anatomy values or two paired DSSs with linkage is the right structure.
- **Anatomy-agnostic DSSs that could be subtyped.** Where COSMoS has a generic DSS with METHOD value_list spanning many imaging modalities, ask whether modality-specific or anatomy-specific subtypes would carry more information.

Three to seven observations is the right range for a single family. Fewer signals an undercooked assessment; more starts to dilute.

---

## Stage 4 — Deliverable

`{ModalityFamily}_Clinical_Knowledge_Reference.xlsx` with three sheets:

### Sheet 1 — Clinical_Knowledge_Pairs (primary)

One row per pair. Columns: Procedure · Measurement (abbrev) · Kind · Anatomical target · Clinical question / endpoint use · Indications (clinical-truth) · Status · Key evidence references · Notes.

Color-coded by status:
- Green (REG)
- Yellow (CS)
- Pink (WCT, EM)

### Sheet 2 — COSMoS_Coverage

One row per pair, in the same order as Sheet 1. Columns: Pair (procedure + measurement) · Status · COSMoS DSS · DSS short name · Domain · TESTCD · NCIt · METHOD · Coverage tier · Architectural observations.

Color-coded by coverage tier:
- Green (Aligned)
- Yellow (Catalog ahead of standards)
- Pink (Greenfield)
- Peach (Architectural observation flag)

### Sheet 3 — Notes_Legend

Sections:

- **Architecture** — short paragraph stating the two-layer separation and the sponsor-agnostic design.
- **Status codes** — definitions for REG, CS, WCT, SPC, EM, PRO.
- **Kind codes** — definitions for QB, RC, STR, CSI, STG, SEV.
- **COSMoS coverage tiers** — color key with definitions.
- **Key findings** — three to seven numbered findings synthesising the architectural observations from Stage 3.
- **Methodology** — six numbered steps describing how to extend or replicate the map.
- **Provenance** — clinical-knowledge sources (regulatory guidance and consortium standards used, with a citation list), COSMoS source (DSS_View.xlsx package version), SDTM CT version, NCIt Thesaurus version, SDTMIG version, generated date, analysis tool, repository home (`https://github.com/kerfors/cdisc-for-ai`).

---

## Stage 5 — Repository integration

The reference map is one artefact. Surrounding it in the repository:

- **README per family.** A one-page narrative summarising the family, the architectural observations from Stage 3, and pointers to the Excel artefact and any supporting case-study HTML. Mirrors the format of the existing Glucose lab and 6MWT instrument cases.
- **Methodology preface.** A repo-level document (one for the whole repo, not per family) explaining the two-layer architecture and why it is sponsor-agnostic. Reusable across families.
- **Citation list export.** Optionally, a flat `.bib` or `.csv` file enumerating every reference cited across all families in the repository, to support reuse and cross-checking.

---

## Suggested first family on the public machine

**MRI of liver disease.** Content already validated through prior work. Worked example for the methodology because COSMoS coverage is genuinely thin (PDFF only) and the architectural observation (PDFF in UR domain) is a strong demonstrator of the kind of surfacing the map produces.

After MRI of liver, two natural follow-ons that demonstrate the method in different conditions:

- **Hand and foot X-ray for RA structural progression.** COSMoS-aligned anchor (five Sharp/Genant and Sharp/van der Heijde DSSs in MK with `METHOD=X-RAY;MRI`). Clinical-knowledge layer extends with mTSS, RAMRIS variants, Larsen. Single TA in clinical use, structurally clean.
- **DXA for osteoporosis.** Multiple anatomical sites (lumbar spine, femoral neck, total hip, distal radius), multiple measurement variants (BMD, T-score, Z-score, TBS, VFA). Strong for showing how the map handles anatomical multiplicity within a single family.

Running three families before declaring the methodology stable is sensible. Each surfaces different shapes of clinical-knowledge / COSMoS-coverage relationship and stress-tests the template differently.

---

## Methodological commitments

- **Public sources only.** Every claim in the map traces to a publicly verifiable reference. No internal documents, no paywalled material that cannot be cited by DOI or stable URL.
- **Cite-check is a hard gate.** Stage 1b is not optional. Hallucinated citations destroy the artefact's value as a public reference.
- **Indications are clinical-truth, not portfolio-filtered.** A biomarker used in thalassemia, sickle cell disease, and hemochromatosis is recorded as such regardless of any sponsor's TA list.
- **Architectural observations are first-class output.** They are the most reusable part of the map for the CDISC community. Surface them explicitly in Sheet 2 and synthesise them in the Sheet 3 key findings.
- **One family per session.** Keeps the deliverable focused, the cite-checking tractable, and the architectural observations sharp.
- **Re-run periodically.** COSMoS coverage evolves. A pair that is Greenfield this quarter may be Aligned next quarter. The clinical-knowledge layer is much more stable but should be reviewed annually for new consortium guidance or regulatory qualifications.

---

## Provenance fields to capture in each deliverable

- Clinical-knowledge sources — bulleted list of guidance and standards documents cited
- COSMoS source — `DSS_View.xlsx` package version
- SDTM CT version
- NCIt Thesaurus version
- SDTMIG version
- Generated date
- Analysis tool (Claude model used)
- Repository home — `https://github.com/kerfors/cdisc-for-ai`
