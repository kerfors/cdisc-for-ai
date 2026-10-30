# sdtm-test-codes — What is measured?

The green layer. Identity for every CDISC SDTM test code: what is it called, what concept does it represent, how does it connect to external terminologies.

**Reference file:** [`machine_actionable/SDTM_Test_Identity.xlsx`](machine_actionable/SDTM_Test_Identity.xlsx)

## Notebooks

| Notebook | Role | Output |
|---|---|---|
| [`SDTM_CT_Extract`](notebooks/SDTM_CT_Extract.ipynb) | Extract | [`interim/SDTM_CT_Extract.csv`](interim/SDTM_CT_Extract.csv) |
| [`SDTM_CT_NCIt_Enrich`](notebooks/SDTM_CT_NCIt_Enrich.ipynb) | Enrich | [`machine_actionable/SDTM_Test_Identity.xlsx`](machine_actionable/SDTM_Test_Identity.xlsx) |
| [`SDTM_CT_Term_NCIt_Synonyms`](notebooks/SDTM_CT_Term_NCIt_Synonyms.ipynb) | Enrich | [`interim/SDTM_CT_Term_NCIt_Synonyms.csv`](interim/SDTM_CT_Term_NCIt_Synonyms.csv) |

**Extract** auto-discovers all extensible Test Code / Test Name codelist pairs from the NCI EVS SDTM Terminology file, covering both the `*TESTCD` convention (e.g. LBTESTCD) and the `*CD` convention used by TA-specific and body-system codelists (e.g. CVFATSCD, MUSCTSCD). Captures cross-domain membership. Excludes Parameter Name-Code pairs (TSPARMCD/TSPARM) — study-level metadata, not observation test codes.

**Enrich** adds NCIt preferred terms, definitions, synonyms, and UMLS cross-references (CUI mappings to SNOMED, MeSH, RxNorm). The reference file includes a ReadMe sheet with full column documentation.

**Term NCIt synonyms** lists the NCIt synonyms of every SDTM CT term (all codelists, not only test codes) from the NCIt FLAT file. The Findings consumers read it for the `term_ncit_synonyms` column of their Codelists sheet. It checks the `NCIt` pin in `Reference_Versions.json` against the FLAT build date. NCIt synonyms in this track are separated by `|`, the FLAT file's own separator (since 2026-10-30; `NCIt_Synonyms` used `; ` before).

Each notebook documents its own logic, sources, and design decisions in detail.

## Data flow

```
NCI EVS SDTM Terminology Excel
        │
    Extract
        │
  interim/SDTM_CT_Extract.csv
        │
    Enrich  ← NCIt FLAT file + CUI map + SDTM Terminology TXT
        │
  machine_actionable/SDTM_Test_Identity.xlsx
```

All source files are downloaded automatically and cached in [`downloads/`](downloads/).

## Dependencies

This track is independent — reads only from NCI EVS public sources.

The interim CSV is consumed by [`cosmos-bc-dss/`](../cosmos-bc-dss/) for codelist lookups.
