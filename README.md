# cdisc-for-ai

Machine-actionable reference files for CDISC clinical data standards — designed for both human review and AI consumption.

## Why

CDISC standards are published as PDFs, spreadsheets, and APIs. They can be used by automated systems, but AI puts new focus on making them work at the language level — for both human and artificial intelligence. The information is there. But it is scattered across multiple sources with no machine-traversable connections between them, and the flat formats hide the semantic structure that both humans and automated systems need to reason correctly.

A significant share of automated protocol-to-CDISC translation failures are not caused by missing vocabulary — the concepts exist. They fail because the standards lack the machine-traversable connections needed for automated systems to resolve them. These are infrastructure gaps, not knowledge gaps.

This repository builds flat, self-describing reference files that make existing CDISC standards machine-actionable — following FAIR data principles. Laboratory and measurement standards are the focus area.

## Context

The Unified Study Definitions Model (USDM), CDISC's 360i initiative, and the broader move toward structured, machine-readable protocols are creating demand for standards that work as computable building blocks — not just documentation. When study designs are expressed as data, the standards they reference must also be data.

## Tracks

Each track produces one machine-actionable reference file. Each reference file is self-describing — with a README sheet documenting columns, provenance, and design decisions.

| Track | Question | Reference file | Source |
|---|---|---|---|
| [`sdtm-test-codes/`](sdtm-test-codes/) | What is measured? | [`SDTM_Test_Identity.xlsx`](sdtm-test-codes/machine_actionable/SDTM_Test_Identity.xlsx) | NCI EVS, NCIt, UMLS |
| [`cosmos-bc-dss/`](cosmos-bc-dss/) | How is it measured? | `Measurement_Specifications.xlsx` *(planned)* | COSMoS BC/DSS, SDTM CT |

The [`sdtm-test-codes/`](sdtm-test-codes/) track has a complete pipeline from source to reference file. The [`cosmos-bc-dss/`](cosmos-bc-dss/) track produces a validated [interim file](cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx) — column naming and final reference file generation are pending discussion with the CDISC community.

An exploratory [merged interim file](cosmos-bc-dss/interim/Study_Design_Merge.xlsx) joins both tracks into a single two-sheet reference — test identity (green) enriched with measurement specifications (yellow). This serves as the reference file for the [`specimen-findings-ct-mapping`](skills/specimen-findings-ct-mapping/) skill.

The progression tells a story: first you establish *what* is measured (test identity), then *how* it is measured (measurement specifications), then you use both to *resolve* protocol terms to CDISC standards.

## Pipeline pattern

Each track follows the same data flow:

```
downloads/  →  interim/  →  machine_actionable/
                              reports/
```

- **downloads/** — cached source files, downloaded by notebooks, not committed to git
- **interim/** — structurally complete pipeline artifacts, not yet enriched to reference quality
- **machine_actionable/** — the reference files, one per track
- **reports/** — QC and validation output, separate from reference files

Each notebook does one thing: **Extract/Flatten**, **Validate**, **Compare**, **Enrich**, or **Merge**. Validation and comparison are separated from production so QC can re-run independently when sources update. Details are documented in the notebooks themselves.

## Repository structure

```
cdisc-for-ai/
├── sdtm-test-codes/       ← independent, reads from NCI EVS
│   ├── notebooks/
│   ├── downloads/
│   ├── interim/
│   ├── machine_actionable/
│   ├── reports/
│   └── README.md
├── cosmos-bc-dss/          ← reads SDTM CT for codelist lookups
│   ├── notebooks/
│   ├── downloads/
│   ├── interim/
│   ├── machine_actionable/
│   ├── reports/
│   ├── docs/
│   └── README.md
├── skills/
│   ├── sdtm-ct-analysis/
│   └── specimen-findings-ct-mapping/
└── README.md
```

## Design decisions

**Why flat files?** Excel files with README sheets reach the broadest audience — data managers, statisticians, LLMs, rule engines. The graph exists in COSMoS; we project it into a consumable view. *One Graph — Many Views.*

**Why "machine-actionable" not "AI-friendly"?** Applies to any automated system, not just LLMs. Aligns with FAIR data principles.

**Why interim/?** Downloads are external. Interim files are our own pipeline artifacts — visible because they have value as standalone artifacts, even if not the final product.

## Status

Early and exploratory. Not a finished product. Built with AI assistance — will evolve through interaction with the CDISC community.

## Author

Kerstin Forsberg — information architect specializing in clinical data standards.
