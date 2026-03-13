# sdtm-domain-reference

A publicly sourced reference for all SDTMIG v3.4 domains, with a structural analysis layer combining SDTM CT categories and COSMoS content patterns.

## What this is

Two files with distinct purposes:

**Reference data** — [`SDTM_Domain_Metadata.xlsx`](machine_actionable/SDTM_Domain_Metadata.xlsx) lists all 56 SDTMIG v3.4 domains with their observation class and factual properties. Sourced from public CDISC documentation. Stable — changes only when a new SDTMIG version is published. Intended for programmatic use by notebooks in other tracks.

**Analysis output** — [`SDTM_Domain_Analysis.xlsx`](reports/SDTM_Domain_Analysis.xlsx) adds our Structural Type categorization and COSMoS coverage counts. Evolves as we refine the categorization or COSMoS updates. Joins to the metadata file on `Domain`.

## Files

```
sdtm-domain-reference/
  README.md                                       ← this file
  docs/
    SDTM_Domain_Overview.md                       ← what we learned (narrative)
  machine_actionable/
    SDTM_Domain_Metadata.xlsx                     ← reference data (stable)
  reports/
    SDTM_Domain_Analysis.xlsx                     ← structural types + COSMoS (evolving)
```

## Structural types (our contribution)

SDTM classifies domains by observation class (Findings, Events, Interventions, etc.). We add a Structural Type layer that describes *how the data within each class is architecturally structured*:

| Structural Type | Domains | What distinguishes it |
|---|---|---|
| Specimen-based Findings | 11 | BC→DSS decomposition by specimen/method/scale |
| Instrument Findings | 3 | QRS instruments; BC hierarchy = form→question grouping |
| Measurement Findings | 4 | Quantitative measurements without specimen |
| Domain-specific Findings | 6 | Domain-specific observation patterns |
| Clinical Assessment Findings | 4 | Findings about events/interventions, tumor assessments |
| Events | 7 | Clinical occurrences |
| Interventions | 7 | Treatments, procedures, exposures |
| Special-Purpose | 5 | Demographics and subject-level metadata |
| Trial Design | 7 | Study-level protocol metadata |
| Relationship | 2 | Record linkage datasets |

## Sources

Domain list and observation classes: SDTMIG v3.4 public documentation.

Structural type categorization: our analysis — see [`docs/SDTM_Domain_Overview.md`](docs/SDTM_Domain_Overview.md).

COSMoS coverage: point-in-time snapshot from the [`cosmos-bc-dss`](../cosmos-bc-dss/) interim file.

## About

Exploratory work built with AI assistance. Not an official CDISC product. Part of [cdisc-for-ai](https://github.com/kerfors/cdisc-for-ai).
