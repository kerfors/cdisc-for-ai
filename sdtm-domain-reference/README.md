# sdtm-domain-reference

A publicly sourced reference for all SDTMIG v3.4 domains, with a structural analysis layer combining SDTM CT categories and COSMoS content patterns.

## What this is

**Reference data** -- [`SDTM_Domain_Metadata.xlsx`](machine_actionable/SDTM_Domain_Metadata.xlsx) lists the 58 SDTMIG v3.4 domains, plus domains that SDTM CT brings test codes for and that are published in the CT SDTM Domain Abbreviation codelist (C66734), with their observation class and pipeline flags (`Has_Test_Codes`, `Specimen_Based`, `Measurement`, `Immunogenicity`; `Immunogenicity` is checked before `Specimen_Based`, so IS goes to its own consumer). Sourced from public CDISC documentation and SDTM CT. Changes when a new SDTMIG version is published, or when CT adds such a domain -- `sdtm-findings-graph/notebooks/Scope_Check.ipynb` fails a refresh until it is classified. A domain added from CT gets its observation class at once; its consumer flag waits until published COSMoS content shows how it behaves. The five SDTMIG v3.4 datasets that are not domains of observations (RELREC, RELSPEC, RELSUB, SUPPQUAL, OI) are listed apart, in the sheet `Non_Observation_Datasets`, each with the reason. Intended for programmatic use by notebooks in other tracks.

**IG statements** -- [`SDTMIG_Statements.xlsx`](machine_actionable/SDTMIG_Statements.xlsx) quotes what SDTMIG v3.4 says about how a test is described (a generic --TEST plus qualifier variables: §4.1.9, LB Assumption 8, the GF, IS and MB facet variables) and which domain a kind of test goes to (IS, GF, MB and PC routing), verbatim with section, item and page, plus the variable-table rows of the variables they name. Facts with citations only; the selection is hand-kept in the notebook, the text is read from the IG. Built by [`notebooks/SDTMIG_Statements.ipynb`](notebooks/SDTMIG_Statements.ipynb) from the local IG copies (needs `pdfminer.six`).

The March 2026 structural-type and behavioural-group analysis that motivated these flags is archived in [`docs/archive/behavioural-analysis-2026-03/`](../docs/archive/behavioural-analysis-2026-03/).

## Files

```
sdtm-domain-reference/
  README.md                                       <- this file
  downloads/                                      <- gitignored: SDTM_v2.0.csv, SDTMIG_v3.4.csv (CDISC variable tables), Approved-Non-Standard-Variable-Registry_2026-04-03.xlsx (CDISC NSV registry), SDTMIG v3.4-FINAL_2022-07-21.pdf (the IG document); sign-in at cdisc.org
  notebooks/
    SDTMIG_Statements.ipynb                       <- builds SDTMIG_Statements.xlsx from the IG PDF and variable tables
  machine_actionable/
    SDTM_Domain_Metadata.xlsx                     <- reference data (stable, hand-kept)
    SDTMIG_Statements.xlsx                        <- IG statements on test facets and domain routing, quoted
```

## Sources

Domain list, sections, names and classes: the SDTMIG v3.4 variable table and table of contents (local copies in `downloads/`). `sdtm-findings-graph/notebooks/Scope_Check.ipynb` checks the sheet against them.

Domains added from CT: the SDTM Domain Abbreviation codelist (C66734) in the NCI EVS SDTM CT file; see the Notes column.

COSMoS coverage is not carried here; see [`consumer-bases/interim/DSS_View.xlsx`](../consumer-bases/interim/DSS_View.xlsx).

Variable-level metadata is not carried in the xlsx either. The CDISC variable tables for SDTM v2.0 and SDTMIG v3.4 are kept as local copies in `downloads/` (gitignored, downloaded with a cdisc.org sign-in) and read by [`domain-behaviour/`](../domain-behaviour/) for role, qualified variables and CDISC Notes. The CDISC Approved Non-Standard Variable Registry sits there too, for variables not in a domain's SDTMIG table. What is quoted from them is published in `SDTMIG_Statements.xlsx`; the files themselves are not.

## About

Exploratory work built with AI assistance. Not an official CDISC product. Part of [cdisc-for-ai](https://github.com/kerfors/cdisc-for-ai).
