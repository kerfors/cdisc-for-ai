# cosmos-bc-dss — How is it measured?

The yellow layer. COSMoS defines measurements at two levels: Biomedical Concepts describe *what* is measured (e.g. Glucose), and Dataset Specializations describe *how* it maps to SDTM variables (specimen, method, units, result type). This track combines both levels into a single flat file — so that anyone implementing SDTM mappings can look up a measurement and see everything needed in one row. Covers all SDTM domains, not just Laboratory.

**Current output:** [`interim/COSMoS_BC_DSS.xlsx`](interim/COSMoS_BC_DSS.xlsx) — structurally complete, validated, but column naming not yet finalized.

**Planned reference file:** `machine_actionable/Measurement_Specifications.xlsx` — pending column naming decisions (see below).

For a walkthrough of what the interim file contains and the QC findings, see [`docs/COSMoS_Content_and_QC.md`](docs/COSMoS_Content_and_QC.md). For open questions on column naming and measurement identifiers, see [`docs/COSMoS_Study_Design_Questions.md`](docs/COSMoS_Study_Design_Questions.md).

## Notebooks

| Notebook | Role | Output |
|---|---|---|
| [`COSMoS_BC_DSS_Flatten`](notebooks/COSMoS_BC_DSS_Flatten.ipynb) | Flatten | [`interim/COSMoS_BC_DSS.xlsx`](interim/COSMoS_BC_DSS.xlsx) |
| [`COSMoS_BC_DSS_Validate`](notebooks/COSMoS_BC_DSS_Validate.ipynb) | Validate | [`reports/COSMoS_BC_DSS_QC.xlsx`](reports/COSMoS_BC_DSS_QC.xlsx) |

**Flatten** downloads COSMoS BC and DSS exports, resolves SDTM CT submission values for specimen/method/unit, classifies BCs by type, and builds hierarchy paths. Extracts DSS dimensions generically by variable role — no hardcoded domain logic.

**Validate** runs 13 quality checks (QC-01 to QC-13) on the interim file — structural integrity checks plus validation against the [BC Curation Principles and Completion Guidelines](https://cdisc-org.github.io/COSMoS/bc_starter_package/doc/BC%20Curation%20Principles%20and%20Completion%20GLs.xlsx). Reads only from the interim file — no source re-download needed.

Each notebook documents its own logic, sources, and design decisions in detail.

## Data flow

```
COSMoS BC + DSS exports       SDTM CT codelists (NCI EVS)
        │                              │
        └──────────┬───────────────────┘
                   │
               Flatten
                   │
     interim/COSMoS_BC_DSS.xlsx
                   │
               Validate
                   │
     reports/COSMoS_BC_DSS_QC.xlsx
```

All source files are downloaded automatically and cached in [`downloads/`](downloads/).

## Key design choices

**Column naming — work in progress:** COSMoS uses implementation-oriented field names optimized for SDTM variable assignment. The [Flatten notebook](notebooks/COSMoS_BC_DSS_Flatten.ipynb) translates them to semantically transparent names — but the current naming is a first pass, not a final answer. For [`sdtm-test-codes/`](../sdtm-test-codes/), we believe the column names have landed in a good place. This track needs the same careful iteration, ideally informed by discussion with the CDISC community, before producing a final reference file. The mapping from COSMoS source fields to current output columns is documented in the Flatten notebook.

**All domains:** Generic extraction by variable role handles Findings, Events, and Interventions uniformly. Domain observation class is annotated for each entry.

**Categories vs. hierarchy:** Two independent classification axes in COSMoS, kept separate. Categories are multi-valued (from `categories` field). Hierarchy is single-valued (from `parent_bc_id`).

**CT unmapped log:** Serialized in the interim file so Validate can run independently from source downloads.

## Dependencies

Reads SDTM CT codelists from NCI EVS for submission value resolution. Does not depend on [`sdtm-test-codes/`](../sdtm-test-codes/) output, but reads the same NCI EVS source file.
