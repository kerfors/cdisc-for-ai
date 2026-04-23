# Chest X-Ray — COSMoS DataBook

*BC `C38101` — X-Ray Imaging.*
*Generated from `COSMoS_Graph.xlsx` via the template catalogue.*

---

## BC opener

**X-Ray Imaging** (C38101) binds 2 DSSs in the current graph, all in domain `PR`.

*Definition.* A radiographic procedure using the emission of x-rays to form an image of the structure penetrated by the radiation.

*Categories.* Diagnostic Imaging;Medical Imaging

---

## Data-integrity note

`docs/XRay_COSMoS_Story.html` argues a cross-Domain_Class composition where the same BC binds both a PR DSS (procedure performed) and an MK DSS (finding read from the image). The current graph carries only PR-domain DSSs for `C38101`. Template 03's cross-class band (Band 3c and Band 5 cross-domain registry-need) is therefore published here as a *gap argument*, not as a rendered binding.


## DSS `XRAY` — X-Ray

The **X-Ray** specialisation (`XRAY`) realises the **X-Ray Imaging** biomedical concept as a PR-domain row template. It pins `PRTESTCD = —`. Added to SDTMIG in 3-4.

### Variables

| Variable | Natural name | Role | Pinned value | Codelist | Value list |
|---|---|---|---|---|---|
| `PRTRT` | Reported Name of Procedure | Topic |  |  |  |
| `PRDECOD` | Standardized Name of Procedure | Qualifier | X-RAY | PROCEDUR |  |
| `PRCAT` | Procedure Category | Qualifier |  |  |  |
| `PRSCAT` | Procedure Subcategory | Qualifier |  |  |  |
| `PRPRESP` | Procedure Pre-specified | Qualifier |  | NY | Y |
| `PROCCUR` | Procedure Occurrence | Qualifier |  | NY | N;Y |
| `PRLOC` | Procedure Location | Qualifier |  | LOC | CHEST, HEAD, ABDOMINAL REGION, CERVICAL SPINE, THORACIC SPINE, LUMBAR SPINE |
| `PRSTDTC` | Start Date and Time of Procedure | Timing |  |  |  |
| `PRENDTC` | End Date and Time of Procedure | Timing |  |  |  |

### Attributes

| Attribute | Value |
|---|---|
| Category | open |
| Sub Category | open |
| Location | open, constrained to `CHEST, HEAD, ABDOMINAL REGION, CERVICAL SPINE, THORACIC SPINE, LUMBAR SPINE` |
| Decod | **X-RAY** *(pinned)* |

### Flattened row (band 4 stub)

*Flattened row (band 4) — stub rendering from graph; the
`COSMoS_Graph_Flat.xlsx` round-trip file is not yet produced.*

| Field | Value |
|---|---|
| BC_ID | C38101 |
| BC_short_name | X-Ray Imaging |
| BC_definition | A radiographic procedure using the emission of x-rays to form an image of the structure penetrated by the radiation. |
| BC_categories | Diagnostic Imaging;Medical Imaging |
| BC_type | full |
| result_scales | Nominal |
| DS_Code | XRAY |
| DS_short_name | X-Ray |
| Domain | PR |
| sdtmig_since | 3-4 |

## DSS `XRAYCHEST` — Chest X-Ray

The **Chest X-Ray** specialisation (`XRAYCHEST`) realises the **X-Ray Imaging** biomedical concept as a PR-domain row template. It pins `PRTESTCD = —`. Added to SDTMIG in 3-4.

### Variables

| Variable | Natural name | Role | Pinned value | Codelist | Value list |
|---|---|---|---|---|---|
| `PRTRT` | Reported Name of Procedure | Topic |  |  |  |
| `PRDECOD` | Standardized Name of Procedure | Qualifier | X-RAY | PROCEDUR |  |
| `PRCAT` | Procedure Category | Qualifier |  |  |  |
| `PRSCAT` | Procedure Subcategory | Qualifier |  |  |  |
| `PRPRESP` | Procedure Pre-specified | Qualifier |  | NY | Y |
| `PROCCUR` | Procedure Occurrence | Qualifier |  | NY | N;Y |
| `PRLOC` | Procedure Location | Qualifier | CHEST | LOC |  |
| `PRSTDTC` | Start Date and Time of Procedure | Timing |  |  |  |
| `PRENDTC` | End Date and Time of Procedure | Timing |  |  |  |

### Attributes

| Attribute | Value |
|---|---|
| Category | open |
| Sub Category | open |
| Location | **CHEST** *(pinned)* |
| Decod | **X-RAY** *(pinned)* |

### Case specialisations refining this DSS (Template 04)

#### Case specialisation — ID101: Standing PA Chest X-Ray

Parent DSS: `XRAYCHEST`  
Case type: recording-child + SoA-activity  

*No additional inside-DSS pinning — case inherits parent pins only.*

Rationale: Standard diagnostic standing PA; inherits XRAYCHEST pins (PRDECOD=X-RAY, PRLOC=CHEST).

*Source: `docs/XRay_PatientBurden_Story.html`*

#### Case specialisation — ID102: Supine Portable Chest X-Ray

Parent DSS: `XRAYCHEST`  
Case type: recording-child + SoA-activity  

*No additional inside-DSS pinning — case inherits parent pins only.*

Rationale: Portable supine; inherits XRAYCHEST pins; no additional slot available.

*Source: `docs/XRay_PatientBurden_Story.html`*

#### Case specialisation — ID103: Semi-Recumbent Chest X-Ray (Post-Op Follow-Up)

Parent DSS: `XRAYCHEST`  
Case type: recording-child + SoA-activity  
Composes with: Post-operative assessment event (SoA-scheduling parent, study-design object)  

*No additional inside-DSS pinning — case inherits parent pins only.*

Rationale: Post-operative follow-up positioning; inherits XRAYCHEST pins.

*Source: `docs/XRay_PatientBurden_Story.html`*

### Flattened row (band 4 stub)

*Flattened row (band 4) — stub rendering from graph; the
`COSMoS_Graph_Flat.xlsx` round-trip file is not yet produced.*

| Field | Value |
|---|---|
| BC_ID | C38101 |
| BC_short_name | X-Ray Imaging |
| BC_definition | A radiographic procedure using the emission of x-rays to form an image of the structure penetrated by the radiation. |
| BC_categories | Diagnostic Imaging;Medical Imaging |
| BC_type | full |
| result_scales | Nominal |
| DS_Code | XRAYCHEST |
| DS_short_name | Chest X-Ray |
| Domain | PR |
| sdtmig_since | 3-4 |

---

## Cross-Domain_Class framing

The reference story posits an MK-domain partner DSS (morphological finding). In the current graph both DSSs are PR-domain. The cross-class proposition the BC should realise is:

> *A chest X-ray, as a clinical event, is simultaneously a procedure executed (PR-domain) and a morphological observation read from the resulting image (MK-domain). Both rows belong together under this BC.*

> ### Registry gap — cross-domain composition
>
> The **X-Ray Imaging** BC binds DSSs in the PR domain (`XRAY`,
> `XRAYCHEST`). The MK-domain framing argued for in
> `docs/XRay_COSMoS_Story.html` (the finding read from the image)
> is prospective — it is not present in the current graph. A
> cross-domain-class registry would name which Domain_Class
> bindings are expected for which clinical events.

> ### Registry gap — case specialisations
>
> The cases above are encoded inline in this notebook from the
> reference HTML stories. A registry of shape
> *(case_spec_id, parent_dss, case_type, composes_with, rationale,
> ext_ref)* would lift these from story prose into machine-
> actionable first-class content.
