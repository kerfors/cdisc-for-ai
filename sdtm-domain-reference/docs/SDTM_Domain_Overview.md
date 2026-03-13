# SDTM Domain Reference — What We Learned

*Findings from a structural analysis of all SDTMIG v3.4 domains, categorized by how their data is structured and consumed, annotated with COSMoS coverage.*

| | |
|---|---|
| **Date** | March 2026 |
| **SDTMIG** | v3.4 / SDTM v2.0 |
| **CT analysis** | [`skills/sdtm-ct-analysis/`](../../skills/sdtm-ct-analysis/) — 1,181 codelists → 25 categories |
| **COSMoS analysis** | [`cosmos-bc-dss/`](../../cosmos-bc-dss/) — 1,127 BCs, 1,123 DSSs across 31 domains |
| **Reference file** | [`machine_actionable/SDTM_Domain_Metadata.xlsx`](../machine_actionable/SDTM_Domain_Metadata.xlsx) |
| **Analysis file** | [`reports/SDTM_Domain_Analysis.xlsx`](../reports/SDTM_Domain_Analysis.xlsx) |

---

## Summary

SDTM classifies its 56 domains by observation class — Findings, Events, Interventions, Special-Purpose, Trial Design. This tells you *what kind of observation* a domain holds. It does not tell you *how the data within that class is architecturally structured*.

That structural view matters for automated systems. A mapping tool, study design selector, or validation engine needs to know whether test codes decompose by specimen, whether a domain carries instrument-level hierarchies, or whether a Biomedical Concept produces one or many Dataset Specializations. The observation class alone is too coarse for this.

We identified 10 structural types by analysing two things: the 25 CT categories discovered from 1,181 SDTM codelists, and the content patterns in the COSMoS flattened BC/DSS file. These structural types cross-cut observation class with usage patterns.

---

## Key findings

### Specimen-based Findings are where the two-level model works

11 domains (LB, IS, GF, MB, MI, MS, BS, CP, PC, PP, UR) are specimen-based. This is the only structural type where the COSMoS two-level model — Biomedical Concept → Dataset Specialization — does real decomposition work. One BC (Glucose Measurement, C105585) produces 8 DSSs, each differing by specimen (SERUM, PLASMA, BLOOD, URINE, INTERSTITIAL FLUID), method (TEST STRIP vs none), and result scale (Quantitative vs Qualitative).

The SDTMIG v3.4 explicitly groups these domains in Section 6.3.5 and provides a generic specification for them. This is also where LOINC cross-referencing is meaningful and where the SDTM postcoordinated model (TESTCD × specimen × method × scale × units) contrasts with LOINC's precoordinated approach.

### Instrument Findings use the BC hierarchy differently

3 domains (QS, FT, RS) carry instrument-based findings. 976 of 1,181 CT codelists (83%) serve these domains — but the architecture is fundamentally different from specimen-based domains.

Each BC is a single question: "PHQ-9 Question 1", "6MWT Distance at 1 Minute." The DS_Code equals the TESTCD. There is no specimen, no method, no unit decomposition. BC→DSS is 1:1 — the DSS restates the BC in domain terms without adding specification value.

What COSMoS *does* add for instruments is the **BC hierarchy** — Categories and Hierarchy_Path group individual questions into their parent instrument and subscale. This provides the instrument→subscale→question grouping that SDTM CT does not declare. The CT file has 353 non-extensible instrument test code codelists with no explicit instrument-to-question linkage; the BC hierarchy makes that linkage machine-traversable.

### The "other" Findings domains are diverse

Beyond specimen-based and instrument-based, there are 11 more Findings domains. They cluster into two groups:

**Measurement Findings** (VS, EG, MK, CV) — subject-level measurements without specimen decomposition. VS has units but no specimen variable. EG findings are qualitative. BC→DSS is mostly 1:1, with mild decomposition in VS (12 BCs → 16 DSSs, likely by location/position).

**Domain-specific and Clinical Assessment Findings** (RP, DD, SR, SC, SS, DA, FA, TR, TU, IE) — each has its own observation pattern. RP (Reproductive System) is the largest with 96 DSSs, all 1:1 with BCs. FA records findings about events or interventions and depends on RELREC linkage. TR/TU are oncology domains for tumor measurement and identification.

### Events and Interventions are structurally simple

Events (AE, DS, MH, CE, BE, DV, HO) and Interventions (CM, EX, EC, PR, SU, ML, AG) don't use test codes. Each record represents one occurrence or one treatment. COSMoS models some of these, but the BC→DSS pattern adds limited value — the DSS is a 1:1 restatement of the BC.

### Trial Summary stretches the BC concept

TS (Trial Summary) has 129 DSSs — the third-largest domain in COSMoS. But these are study-level metadata parameters (SPONSOR, ACTSUB, SENDTC), not subject-level observations. No specimen, no method, no units. The `sdtm-test-codes` track deliberately excluded TSPARMCD/TSPARM as "study-level metadata, not observation test codes." COSMoS made a different choice — include them, so every SDTM domain gets machine-readable specification.

The `BC_Scope` column (Subject/Study) distinguishes them. For study design use cases, filtering on `BC_Scope=Subject` removes TS parameters from measurement selection lists.

---

## COSMoS coverage landscape

31 of 56 SDTMIG v3.4 domains have COSMoS BCs. Coverage is deepest in specimen-based Findings (494 DSSs across 6 of 11 domains) and instrument Findings (175 DSSs across all 3 domains).

Notable gaps among specimen-based domains: BS, CP, MS, PC, PP have no COSMoS coverage yet. CP and BS are new in v3.4; PC/PP use the PARMCD/PARM pattern rather than TESTCD/TEST.

Among non-Findings domains, coverage is sparse — selected events (AE, DS, MH, BE), interventions (CM, EC, EX, PR, SU), and DM. The remaining Events, Interventions, Special-Purpose, Trial Design (except TS), and Relationship domains are not yet modeled.

COSMoS is actively evolving. These gaps reflect the March 2026 snapshot, not permanent boundaries.

---

## Why this matters for the cdisc-for-ai repository

The structural type categorization explains why the different tracks in this repository have different scopes:

- **sdtm-test-codes** extracted all 5,781 test codes across 55 domains — broad scope, because the NCIt enrichment (definitions, synonyms, CUIs) adds value regardless of structural type.
- **cosmos-bc-dss** flattened all 1,127 BCs across 31 domains — broad scope, because the structural analysis itself required seeing the full picture.
- **specimen-findings mapping skill** scoped to LB, CP, MB, IS, MS, BS — narrow scope, because the two-level resolution (TESTCD → DS_Code) only makes sense where specimen decomposition exists.

The structural types make these scoping decisions explicit and principled rather than ad-hoc.

---

## Sources

**Domain list and observation classes:** SDTMIG v3.4 public documentation — CDISC website, CDISC Wiki table of contents (Section 5–8 structure), published conference papers (PharmaSUG, PHUSE).

**Structural type categorization:** Our analysis, based on SDTM CT Category Discovery (25 categories from 1,181 codelists), COSMoS BC/DSS content analysis, and SDTMIG v3.4 Section 6.3.5 grouping of specimen-based domains.

**COSMoS coverage counts:** From the `cosmos-bc-dss` track interim file.

**Not included:** SDTM v2.0 variable-level metadata (requires CDISC membership). SDTM v3.0 (under review, not yet published).

## About

Exploratory work built with AI assistance. Not an official CDISC product. Part of [cdisc-for-ai](https://github.com/kerfors/cdisc-for-ai).
