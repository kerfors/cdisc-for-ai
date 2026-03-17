# cdisc-for-ai

Machine-actionable reference files for CDISC clinical data standards — designed for both human review and AI consumption.

## Why

Behind every TESTCD/TEST pair sits an NCIt concept with its own identity, definition, synonyms, and connections to broader biomedical vocabularies. In specimen-based and measurement domains, each Dataset Specialization adds an identifiable measurement specification — specimen, method, units, LOINC. But these linkages are scattered across disconnected sources. The CT file presents test codes as submission strings. Reaching the measurement specification requires navigating across BC and DSS exports. A human must mentally reconstruct the connections.

The move toward structured study definitions (USDM, 360i, OpenStudyBuilder) pushes this specificity upstream — into study design, where it needs to be explicit and machine-readable from the start. Study designers need to *select from* identifiable measurement specifications, not reconstruct them downstream through implicit decisions during test ordering, data collection, and SDTM mapping.

This repository makes the linkages explicit. Each reference file puts related data side by side in rows, with clear keys linking across sheets and tracks — reachable from one place for humans, AI systems, and rule engines alike. The failures this addresses are not knowledge gaps — the concepts exist. They are infrastructure gaps: missing machine-traversable connections between concepts that already exist.

For how the analytical layers fit together — CT discovery, domain classification, and COSMoS behavioural analysis — see [`SDTM_Domain_Overview.md`](SDTM_Domain_Overview.md).

## Tracks

The repository is organized into source tracks, a reference track, and consumer tracks. Source tracks extract and enrich from upstream standards. The reference track provides shared domain metadata. Consumer tracks join source data into structural-type-specific outputs for study design and mapping workflows.

Each reference file is self-describing — with a README sheet documenting columns, provenance, and design decisions.

### Source tracks

| Track | Question | Output | Source |
|---|---|---|---|
| [`sdtm-test-codes/`](sdtm-test-codes/) | What is measured? | `SDTM_Test_Identity.xlsx` — domain-level test codes | NCI EVS, NCIt, UMLS |
| | | `SDTM_Instrument_Identity.xlsx` — instrument-level test codes | |
| [`cosmos-bc-dss/`](cosmos-bc-dss/) | How is it measured? | `COSMoS_BC_DSS.xlsx` — flattened BC/DSS interim file | COSMoS BC/DSS exports |
| | What are the behavioural patterns? | [`COSMoS_Behavioural_Analysis.md`](cosmos-bc-dss/docs/COSMoS_Behavioural_Analysis.md), [`COSMoS_Domain_Pattern_Inventory.xlsx`](cosmos-bc-dss/docs/COSMoS_Domain_Pattern_Inventory.xlsx) | |

### Reference track

| Track | Purpose | Output |
|---|---|---|
| [`sdtm-domain-reference/`](sdtm-domain-reference/) | Domain metadata — structural types, COSMoS coverage flags, specimen/instrument classification | `SDTM_Domain_Metadata.xlsx` (pipeline input) |
| | Structural type + behavioural group classification per domain | `SDTM_Domain_Analysis.xlsx` (analysis) |

### Consumer tracks

| Track | Structural type | Scope | Output |
|---|---|---|---|
| [`sdtm-findings/`](sdtm-findings/) | Specimen-based | Domains with `Specimen_Based=Yes` in Domain_Metadata | `Specimen_Findings.xlsx` |
| | Measurement | VS, MK, CV (EG deferred) | `Measurement_Findings.xlsx` |
| | Instrument-based | QS, FT, RS | `Instrument_Findings.xlsx` *(planned)* |

Consumer files are two-sheet Excel workbooks: **Test_Identity** (one row per TESTCD, enriched with COSMoS summary) and **Measurement_Specs** (one row per Dataset Specialization, scoped to the relevant domains). The link between sheets is TESTCD. This two-step structure matches the mapping workflow: first resolve a term to a concept, then select the specific measurement variant.

## Skills

AI mapping skills that consume the reference files.

| Skill | Purpose | Reference file |
|---|---|---|
| [`specimen-findings-ct-mapping/`](skills/specimen-findings-ct-mapping/) | Map specimen-based terms to SDTM CT — two-level resolution (TESTCD → DS_Code) | `Specimen_Findings.xlsx` |
| [`sdtm-ct-analysis/`](skills/sdtm-ct-analysis/) | Structural analysis of SDTM Controlled Terminology — category discovery and profiling | NCI EVS SDTM CT file |

## Data flow

```mermaid
graph TD
    subgraph Sources
        EVS["NCI EVS SDTM CT"]
        COS["COSMoS exports"]
    end

    subgraph sdtm-test-codes
        TI["SDTM_Test_Identity.xlsx"]
        II["SDTM_Instrument_Identity.xlsx"]
    end

    subgraph cosmos-bc-dss
        BCD["COSMoS_BC_DSS.xlsx"]
        BA["Behavioural_Analysis.md"]
        DPI["Domain_Pattern_Inventory.xlsx"]
    end

    subgraph sdtm-domain-reference
        DM["SDTM_Domain_Metadata.xlsx"]
        DA["SDTM_Domain_Analysis.xlsx"]
    end

    subgraph sdtm-findings
        SF["Specimen_Findings.xlsx"]
        MF["Measurement_Findings.xlsx"]
        IF["Instrument_Findings.xlsx ❋"]
    end

    subgraph skills
        SK["specimen-findings-ct-mapping"]
    end

    EVS --> TI
    EVS --> II
    COS --> BCD
    BCD --> BA
    BCD --> DPI
    EVS --> DM
    BCD --> DA
    DM --> DA

    TI --> SF
    DM --> SF
    BCD --> SF

    TI --> MF
    DM --> MF
    BCD --> MF

    SF --> SK

    DO["SDTM_Domain_Overview.md<br/>repo root"]
```

*❋ = planned*

## Design decisions

**Why flat files?** Excel files with README sheets reach the broadest audience — data managers, statisticians, LLMs, rule engines. The graph exists in COSMoS; we project it into a consumable view. *One Graph — Many Views.*

**Why "machine-actionable" not "AI-friendly"?** Applies to any automated system, not just LLMs. Aligns with FAIR data principles.

**Why interim/?** Downloads are external. Interim files are our own pipeline artifacts — visible because they have value as standalone artifacts, even if not the final product.

**Why COSMoS vocabulary in column names?** The consumer files keep COSMoS source vocabulary (DS_Code, DS_Name, BC_Name, Domain_Class) rather than translating to study-design-friendly alternatives. Consumers are CDISC-literate; traceability to source trumps consumer-friendliness.

**Why three consumer notebooks?** The three Findings structural types (specimen-based, instrument-based, measurement) have fundamentally different data shapes and join logic. Splitting by structural type keeps each notebook focused and its output consumable.

## Status

Early and exploratory. Not a finished product. Built with AI assistance — will evolve through interaction with the CDISC community.

## Author

Kerstin Forsberg — information architect specializing in clinical data standards.
