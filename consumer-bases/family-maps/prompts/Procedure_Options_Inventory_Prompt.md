# Procedure-Options Inventory at Repo Level — Prompt Template

Build a repo-level inventory of imaging-procedure option dimensions and their governance status across CDISC SDTM Controlled Terminology and COSMoS DSSs. Output is a portable Excel artefact that consolidates qualifier dimensions across all family maps in the `cdisc-for-ai` repository.

The inventory is architectural, not operational. It records *which qualifier dimensions discriminate the same procedure performed under different acquisition conditions*, *which of those dimensions have governed CDISC CT codelists*, and *which DSSs reachable from each procedure reference those codelists*. It does not assign burden values, durations, or adverse-event ratings — those are downstream concerns and are out of scope here.

The inventory grows monotonically: it is re-run when new family maps introduce new procedures or when CDISC CT publishes new codelists. Family maps cross-reference it rather than re-author option information per family.

---

## Inputs required

- All current `*_Clinical_Knowledge_Reference.xlsx` family maps in `consumer-bases/family-maps/` (initially: MRI of liver, DXA for osteoporosis, hand and foot X-ray for RA structural progression).
- `DSS_View.xlsx` — CDISC COSMoS BC + DSS package projection. Sheets used: `Measurement_Specs` (for DSS-level codelist references on PR-domain procedure DSSs and Findings-domain measurement DSSs).
- SDTM Controlled Terminology (`sdtm-test-codes/downloads/SDTM_Terminology.txt` or the latest equivalent NCI EVS download). Used for codelist authority.
- The X-Ray case-study HTMLs (`XRay_COSMoS_Story.html`, `XRay_PatientBurden_Story.html`) as the architectural worked example. The PatientBurden Story documents what this inventory generalises into a structural artefact.

No sponsor inputs. No internal protocol files. The inventory is fully replicable from public CDISC standards and the family maps already in the repository.

---

## Stage 1 — Procedure canonicalisation

Build the union of unique procedures across all input family maps. The procedure list grows whenever a new family map is added; existing entries should not be silently merged or re-named.

For each canonical procedure, capture:

- **Procedure canonical name** — concise, descriptive, designed to be stable across families. E.g., "Multiphasic contrast-enhanced MRI of liver", "Lumbar spine PA dual-energy x-ray absorptiometry (DXA)", "Hand X-ray (PA)".
- **PROCEDUR codelist anchor (CDISC CT C101858)** — the single PROCEDUR term that identifies this procedure's modality. E.g., `X-RAY` (NCIt C38101), `CT SCAN` (NCIt C17204), `MRI` (NCIt C16809), `MAMMOGRAPHY`, `ULTRASOUND`, `BIOPSY`. Where the procedure's modality is not represented in PROCEDUR (e.g., DXA in current PROCEDUR coverage may need verification), record the gap explicitly — do not fabricate a missing term, and do not silently fold under a generic parent.
- **Anatomical target** — primary anatomical site, anchored on LOC codelist (C74456) where a term exists. Multi-site procedures (whole-body DXA, multi-region MRCP) record the multiplicity explicitly rather than collapsing to a single anatomy.
- **Acquisition technique** — the named technique that distinguishes this procedure from a generic modality+anatomy combination. E.g., "Chemical-shift-encoded MRI", "MR Elastography", "R2-relaxometry (FerriScan method)", "Dual-energy x-ray absorptiometry, lumbar spine PA projection". This is free-text but should be standardised through cross-family review.
- **Family maps where this procedure appears** — comma-separated list of the family map filenames. A procedure that appears in multiple families is a procedure once, not multiple times. The cross-family reuse pattern is itself a finding.
- **Source procedure specification** — the imaging society practice parameter, ACR Appropriateness Criteria entry, RSNA QIBA profile, or equivalent that defines the standardised acquisition protocol. Cite-checked at Stage 3b.

Do not generate procedures speculatively. The inventory is closed to procedures actually referenced by family maps in the repository at the time of the run.

---

## Stage 2 — Option dimension discovery and codelist mapping

Enumerate the qualifier dimensions that discriminate the same canonical procedure performed under different acquisition conditions. Dimensions are *discovered* from procedure-specification literature (Stage 1 sources), from the family-map procedure descriptions, and from the X-ray case study, not pre-listed and applied universally.

For each dimension, capture:

- **Dimension name** — concise, e.g., "Patient position", "Acquisition view", "Contrast agent class", "Field strength", "Sedation requirement", "Fasting state", "Bowel preparation", "Acquisition technique sub-mode".
- **Definition** — short clinical definition. What is varied; why it matters clinically; whether it changes the acquisition protocol, the burden profile, the data interpretation, or all three.
- **CDISC CT codelist anchor** — codelist code (e.g., POSITION C71148) and codelist short name. If multiple codelists are candidates, list them and note which is most commonly referenced. If no governed CDISC CT codelist exists, record the gap explicitly with a `—` and note where governance currently sits (sponsor-defined; protocol-local; vendor-specific).
- **Governed terms (if codelist exists)** — count of terms in the codelist plus a representative subset (3-5 terms). Full enumeration goes in a separate sheet if useful but is not required at the dimension level.
- **DSSs that reference the codelist** — count of DSSs across COSMoS that reference this codelist, broken down by domain class (e.g., POSITION C71148 referenced by 31 EGPOS rows in EG and 9 VSPOS rows in VS DSSs, zero rows in PR/MK/TR/TU/IS imaging DSSs). The X-ray case study established this pattern; this column makes the asymmetry systematic.
- **Source authority for the dimension's clinical relevance** — imaging society practice parameter or equivalent. Cite-checked at Stage 3b.

A starting set of dimensions, drawn from the X-ray case study and the three existing family maps, that the inventory should at minimum evaluate:

- Patient position (POSITION C71148)
- Acquisition view / projection (no governed CDISC CT codelist as of last review)
- Anatomical laterality (LAT C99073)
- Anatomical direction (DIR — multiple codelists)
- Anatomical region / location (LOC C74456)
- Contrast agent class (partially modelled; varies by domain)
- Acquisition method / technique sub-mode (METHOD C85492 within Findings DSSs)
- Evaluator type (EVAL within Findings DSSs)
- Field strength / scanner generation (typically no governed codelist)
- Sedation requirement (no governed codelist; clinically discriminating in paediatric, claustrophobic, or critically ill populations)
- Fasting / preparation state (FAST codelist where it exists; coverage uneven)
- Setting (inpatient suite vs portable bedside vs outpatient — typically no governed codelist)

This list is not exhaustive. New families surface new dimensions; the inventory absorbs them.

---

## Stage 3 — Procedure × Dimension coverage matrix

For each (procedure, dimension) cell, assign a coverage status:

- **Applicable + Codelist exists + Referenced in DSS** — `Aligned`. The dimension applies clinically to this procedure, governed CDISC CT terms exist, and at least one DSS reachable from this procedure references the codelist.
- **Applicable + Codelist exists + Not referenced in DSS** — `Architectural observation flag`. The dimension applies clinically and governed terms exist, but no DSS reachable from this procedure binds them. The clearest example: patient position for chest X-ray. POSITION (C71148) has 17 governed terms; XRAYCHEST has no `--POS` slot; standing-PA vs supine-portable is unreachable from the DSS layer.
- **Applicable + No governed codelist** — `Catalog ahead of standards`. The dimension applies clinically but CDISC CT has not published a governed vocabulary. The clearest example: acquisition view (PA, AP, lateral) for chest X-ray.
- **Not applicable to this procedure** — `—` (em-dash). The dimension is not a clinical discriminator for this procedure (e.g., field strength is not applicable to X-ray; contrast agent class is not applicable to non-contrast DXA).

The matrix is the central artefact of the inventory. Counts of cells in each tier, broken down by procedure and by dimension, give an at-a-glance picture of where the standards are silent.

For each `Architectural observation flag` and `Catalog ahead of standards` cell, write a short architectural observation in a separate column. These observations are the productive material for any conversation with the COSMoS authoring community and (where relevant) with the CDISC CT governance process.

---

## Stage 3b — Cite-check the references (hard gate)

Every reference cited in the inventory must be verified before the deliverable is produced. The cite-checking discipline is the same as for the family maps but the source corpus is different.

For procedure specifications (Stage 1):
- ACR Practice Parameters and Appropriateness Criteria (`acr.org`)
- RSNA QIBA Profiles (`qibawiki.rsna.org`)
- ESGAR / SAR / EASR / society practice guidelines for the relevant body system
- AIUM / ARDMS for ultrasound
- ISCD Official Positions for DXA
- Vendor protocol publications only where they are the de facto standard for a vendor-specific technique (e.g., FerriScan St Pierre method, LiverMultiScan cT1)

For dimension definitions and clinical relevance (Stage 2):
- Same as procedure specifications, plus peer-reviewed primary literature for dimensions whose clinical role is established but whose acquisition specification is still evolving.

For codelist verification (Stage 2):
- CDISC CT Browser (`evs.nci.nih.gov`) and the SDTM Terminology download for codelist code, name, term count, and individual term verification
- NCIt EVS for term-level concept code verification

For DSS coverage (Stage 2 and Stage 3):
- `DSS_View.xlsx` Measurement_Specs sheet, queried programmatically. The supporting `cosmos-graph/interim/COSMoS_Graph.xlsx` Variables sheet should be consulted directly when value_list breadth or per-row codelist references are needed (the joined view does not carry slot value_lists, only assigned values — established in the X-ray case study).

Each verified reference must carry a stable identifier (DOI, PubMed ID, or persistent URL). Replace, correct, or remove any reference that fails verification. Familiar names produce more hallucinations, not fewer.

---

## Stage 4 — Architectural observations summary

Synthesise observations across the matrix. Three to seven observations is the right range for the repo-level inventory; if more emerge, group them into themes.

Patterns worth surfacing explicitly, drawing on what the family maps have already shown:

- **Codelist-DSS-binding asymmetry.** Where SDTM CT publishes a governed vocabulary (POSITION, LAT, LOC, DIR) but the DSSs reachable from imaging procedures do not bind it. The X-ray story documented this for POSITION; the inventory should make it systematic across dimensions.
- **PR-side modality × anatomy authoring gap.** The procedure-side DSS proliferation (XRAYCHEST, CTSCANCHEST, MRIBRAIN) has been uneven across modalities. The inventory should make explicit which modality × anatomy combinations have a PR DSS and which do not.
- **Method-conditional discrimination required but not modelled.** Where a single Findings DSS accepts multiple modalities (e.g., Sharp/Genant DSSs accepting X-RAY;MRI), the methodological choice "x-ray Sharp scoring vs MRI RAMRIS scoring" is unreachable from the DSS without sponsor-side discipline. This is closely related to but distinct from the value_list pattern itself.
- **Dimensions with no governed codelist.** Where the clinical literature treats a dimension as discriminating but CDISC CT has no codelist (acquisition view, field strength, setting). These are CDISC CT governance items, not COSMoS DSS authoring items, and should be flagged separately for that reason.
- **Cross-family procedure reuse.** Procedures that appear in multiple family maps (multiphasic contrast-enhanced MRI shows up in liver, kidney, prostate, cardiac contexts) should be flagged. The reuse means a single PR DSS extension benefits multiple family maps simultaneously.

---

## Stage 5 — Deliverable

`Procedure_Options_Inventory.xlsx` with five sheets.

### Sheet 1 — Procedures

One row per canonical procedure. Columns: Procedure canonical name · PROCEDUR anchor (term + NCIt code) · Anatomical target (LOC anchor where applicable) · Acquisition technique · Family maps where it appears · PR-domain DSS reachable (ds_id or absent) · Source procedure specification.

Color-coded by PR-domain DSS coverage: green if a PR DSS exists and matches the procedure (e.g., XRAYCHEST for chest x-ray); peach if a PR DSS exists at parent level but not for this anatomy (e.g., MRI exists but no MRILIVER for liver MRI procedures); pink if no PR DSS.

### Sheet 2 — Option_Dimensions

One row per qualifier dimension. Columns: Dimension name · Definition · CDISC CT codelist anchor (codelist code + name + governed term count) · DSSs that reference the codelist (count, with domain breakdown) · Source authority for clinical relevance.

Color-coded by codelist availability: green if a CDISC CT codelist exists; pink if no governed codelist exists.

### Sheet 3 — Procedure_Option_Coverage_Matrix

The tier matrix. Rows are procedures (ordered as Sheet 1); columns are dimensions (ordered as Sheet 2). Each cell carries a single tier value: `Aligned`, `Architectural observation flag`, `Catalog ahead of standards`, or `—` (not applicable). No observation text in this sheet — it is intentionally compact and visually scannable.

Color-coded: green for Aligned; peach for Architectural observation flag; yellow for Catalog ahead of standards; grey for not applicable.

### Sheet 4 — Procedure_Option_Observations

One row per non-Aligned, non-`—` cell from Sheet 3. Columns: Procedure · Dimension · Tier · Observation · Reference. The Observation column carries one to three sentences of architectural commentary on that specific (procedure, dimension) cell — the productive material that the matrix surfaces but cannot itself contain. The Reference column carries the stable identifier (DOI, PubMed ID, CDISC CT codelist code, or persistent URL) supporting the observation.

This sheet is the queryable artefact for the COSMoS authoring conversation. Filtering by Tier surfaces the strongest authoring candidates (Catalog ahead of standards) or the strongest CT-governance flags (Architectural observation flag). Filtering by Dimension surfaces dimensions that are systematically unreachable across many procedures.

Color-coded by Tier in column C, matching Sheet 3.

### Sheet 5 — Notes_Legend

Sections:

- **Architecture** — short paragraph stating the inventory's purpose: which qualifier dimensions discriminate procedures, which have governed CDISC CT codelists, which DSSs reference them. Explicit note that the inventory is architectural, not operational; burden values are out of scope.
- **Status codes** — Aligned · Architectural observation flag · Catalog ahead of standards · Not applicable. Definitions and color key.
- **Procedure-identity convention** — short paragraph explaining the PROCEDUR anchor + anatomy + technique convention; how procedures missing from PROCEDUR are handled; how the inventory grows monotonically as new families are added.
- **Dimension-discovery convention** — short paragraph explaining that dimensions are discovered from procedure-specification literature and family maps, not pre-listed; the starting dimension set; the rule that a new family may surface new dimensions.
- **Key findings** — three to seven numbered findings synthesising Stage 4.
- **Methodology** — six numbered steps describing how to extend or replicate the inventory.
- **Provenance** — clinical-knowledge sources (procedure-specification authorities, with full citation list); CDISC CT version; NCIt Thesaurus version; SDTMIG version; family maps consumed (with their generation dates); generated date; analysis tool; repository home.
- **Verified references (cite-check audit trail)** — single audit trail of all references cited across the inventory, each with stable identifier (DOI, PubMed ID, persistent URL). Modelled on the audit-trail section in the DXA family map.

---

## Stage 6 — Repository integration

The inventory is repo-level. Surrounding it:

- **Repo-level README addition.** The repository README should reference the inventory as a cross-family architectural artefact, alongside the family maps. The relationship between the two artefact types should be stated explicitly: family maps catalogue clinical-knowledge pairs and COSMoS coverage *per modality family*; the inventory catalogues procedure-option dimensions and CDISC CT governance status *across modality families*.
- **Family-map cross-reference column.** Each family map's Sheet 1 may carry a column "Discriminating procedure-option dimensions" pointing back to the inventory by procedure canonical name. This is a future enhancement to the family-map prompt template, not a retrofit; existing family maps continue to work without it.
- **Re-run cadence.** The inventory is re-run when (a) a new family map is added that introduces a new procedure or (b) CDISC CT publishes a new codelist that is relevant to a dimension already in the inventory. New families do not trigger a full re-authoring; they trigger a delta. Document the delta in Notes_Legend Provenance.

---

## Methodological commitments

- **Architectural, not operational.** The inventory documents what the standards capture and what they don't. It does not assign burden values, durations, contrast adverse-event rates, or radiation dose estimates. Those are downstream artefacts that may be authored separately if needed; they have a different audience and a different cite-checking discipline.
- **Public sources only.** Every claim in the inventory traces to a publicly verifiable reference. CDISC CT, NCIt, ACR, RSNA QIBA, peer-reviewed literature.
- **Cite-check is a hard gate.** Stage 3b is not optional. The audit-trail section in Sheet 4 must enumerate every reference with a stable identifier.
- **PROCEDUR codelist anchoring.** Procedures are anchored on PROCEDUR (CDISC CT C101858) where a term exists. Where no term exists, the gap is documented explicitly. No fabricated terms; no silent merging under a generic parent.
- **Dimensions discovered, not assumed.** The dimension catalog grows from the procedure-specification literature and the family maps. New families may surface new dimensions; the inventory absorbs them.
- **Architectural observations are first-class output.** They are the most reusable part of the inventory for the CDISC community. Surface them per cell in Sheet 3 and synthesise them in Sheet 4 key findings.
- **Cross-family reuse is a finding, not an inconvenience.** Procedures that appear in multiple families compound the value of single CDISC CT or COSMoS authoring decisions and should be flagged explicitly.

---

## Provenance fields to capture in the deliverable

- Family maps consumed — list with file names and generation dates
- COSMoS source — `DSS_View.xlsx` package version
- SDTM CT version
- NCIt Thesaurus version
- SDTMIG version
- Generated date
- Analysis tool (Claude model used)
- Repository home — `https://github.com/kerfors/cdisc-for-ai`
- Companion artefacts — link to the X-Ray case-study HTMLs as the architectural worked example

---

## Worked example anchor

The inventory generalises what the `XRay_PatientBurden_Story.html` case study did manually for one procedure (chest X-ray) into a structural artefact that covers all procedures across all family maps. The architectural finding the case study documented — that POSITION (C71148) has 17 governed terms, is referenced by 31 EGPOS rows in EG DSSs and 9 VSPOS rows in VS DSSs, and is referenced by zero rows in any PR, MK, TR, or TU imaging DSS — is the kind of cell-level observation the inventory's Sheet 3 produces systematically.

The case study and the inventory are not redundant. The case study tells the architectural story for a single procedure in narrative form; the inventory makes the underlying pattern queryable across the repository. They cite each other.
