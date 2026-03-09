# SDTM CT Category Profiles

**Source:** Step 1 output — SDTM CT Category Discovery (2025-09-26 release)
**Codelist headers analyzed:** 1,181
**Categories profiled:** 25
**Profile date:** 2026-03-09

---

## Output 1 — Category Profile Table

| Category | Count | Extensibility | SDTM_Variable_Role | NCIt_Relationship | Machine_Actionability | Consumer_Behavior |
|---|---|---|---|---|---|---|
| Instrument Test Code | 409 | Mixed — 56 extensible (domain-level aggregators like LBTESTCD, VSTESTCD) vs 353 non-extensible (instrument-specific fixed lists) | --TESTCD | Direct C-code per concept | Automated variable population via code lookup; extensible codelists require sponsor-term validation, non-extensible allow strict enumeration | Must distinguish domain-level extensible codelists (open to sponsor additions) from instrument-specific fixed codelists (closed enumeration) — same category, fundamentally different validation logic. |
| Instrument Test Name | 409 | Mixed — identical 56/353 split mirroring Test Code | --TEST | Direct C-code per concept | Paired display-name lookup keyed by TESTCD; always consumed with its TC partner | Always resolve via the paired TC codelist — never consume a TN codelist independently; the TC↔TN pairing is implicit (shared SV prefix) and must be reconstructed by the consumer. |
| Instrument Original Result | 79 | Never — all 79 non-extensible | --ORRES (for instrument questions) | Instrument-defined | Strict allowed-value validation per instrument question; values are question-specific, not reusable across instruments | Each codelist constrains a single question's original responses — the codelist-to-question mapping is encoded only in the SV prefix and must be parsed to link to the correct TC/TN pair. |
| Instrument Standardized Result | 79 | Never — all 79 non-extensible | --STRESC (for instrument questions) | Instrument-defined | Identical pattern to Original Result but populates STRESC; enables ORRES→STRESC mapping validation | Co-occurs 1:1 with an Original Result codelist for the same question — a consumer must pair OR↔STR codelists and may need both to validate the original-to-standardized transformation. |
| Clinical Classification | 27 | Mixed — 26 non-extensible, 1 extensible (near-Never) | --ORRES or --STRESC (standalone classification values) | Concept-backed | Allowed-value validation for grading/staging/classification scales; values represent positions on a recognized clinical scale | These are standalone classification value sets, not part of an instrument TC/TN/OR/STR family — do not attempt to resolve paired codelists; treat as independent allowed-value enumerations. |
| Observation Qualifier | 27 | Mixed — 22 extensible, 5 non-extensible (majority-Yes) | Various qualifier variables (--RESCAT, --LOC, --STAT, --REASND, etc.) | Mixed — some concept-backed, some administrative | Each codelist validates a different qualifying property; no uniform consumption pattern across the group | This is a heterogeneous residual category — every codelist qualifies observations differently; a consumer must read the codelist name and inferred variable role individually rather than applying a category-wide rule. |
| Trial Design | 24 | Mixed — 19 extensible, 5 non-extensible | TS domain variables (TSPARMCD values), TA/TE/TV variables | Concept-backed | Study-level metadata population; most codelists map to Trial Summary (TS) parameter values | These populate protocol-level metadata, not observation-level data — they are consumed once per study (or per arm/epoch), not per subject or per record. |
| Treatment Qualifier | 14 | Always — all 14 extensible | --ROUTE, --DOSFRM, --DOSFRQ, --TRTREAS, etc. | Direct C-code per concept | Intervention qualifier validation; extensible so sponsors may add unlisted terms | All codelists in this category are extensible — a consuming system must accept both CT-defined and sponsor-defined terms and handle validation accordingly. |
| Domain Category | 12 | Mixed — 10 extensible, 2 non-extensible | --CAT, --SCAT | Concept-backed | Domain-level record grouping validation; links records within a domain into named categories | These codelists are domain-specific by definition — a consumer must match each codelist to its owning domain (encoded in the Codelist Name "Category of [Domain]" pattern) before applying. |
| Method | 12 | Always — all 12 extensible | --METHOD, --ANMETH, --COLLMETH | Direct C-code per concept | Method term validation; all extensible to accommodate site-specific or sponsor-specific methods | Always extensible — consuming systems should expect unlisted method terms and provide graceful handling rather than hard rejection. |
| Demographic | 11 | Mixed — 8 extensible, 3 non-extensible | DM domain variables: RACE, SEX, ETHNIC, AGEU, etc. | Direct C-code per concept | Subject-level demographic variable population; fixed-choice variables (SEX) are non-extensible, collected-as variants (RACE) are extensible | Non-extensible codelists (e.g., SEX) represent truly closed value sets; extensible ones (e.g., RACE) accommodate regional or regulatory variation — the extensibility flag is the critical dispatch signal. |
| Disposition | 10 | Mixed — 8 extensible, 2 non-extensible | DS domain: DSDECOD, DSTERM, EPOCH-related | Concept-backed | Disposition event validation; some codelists are study-milestone-specific | Codelists in this category serve different disposition contexts (screening, treatment, follow-up) — the codelist name encodes which study phase applies; a consumer cannot treat them interchangeably. |
| Parameter Name-Code | 10 | Always — all 10 extensible | --PARMCD / --PARM (PK, device, tobacco, organism domains) | Direct C-code per concept | Paired name-code lookup identical to TC/TN pattern; always consumed as PARMCD↔PARM pairs | Functionally identical consumption pattern to Instrument Test Code/Name — paired lookup, extensible, but uses PARM/PARMCD naming instead of TC/TN; a consumer applying the TC/TN pattern can reuse the same logic. |
| Role/Relationship | 9 | Mixed — 8 extensible, 1 non-extensible | RELSUB, EVAL, various role variables | Concept-backed | Role or relationship qualifier validation; identifies who or what entity fills a role in a study record | These codelists identify entities (evaluator, contact, accountable party) rather than observations — a consumer uses them for provenance/attribution, not for clinical data validation. |
| Unit of Measure | 8 | Mixed — 7 extensible, 1 non-extensible | --U, --ORRESU, --STRESU, AGEU | Direct C-code per concept | Unit validation and potential unit-conversion support; each codelist is scoped to a variable context (general, PK, VS, age) | Context-scoped — the general UNIT codelist is a superset while domain-specific unit codelists (VSRESU, PKSTRESU) are subsets; a consumer must select the correct scoped codelist per variable, not default to the general one. |
| Device | 6 | Always — all 6 extensible | DO/DI domain variables | Concept-backed | Device property and event validation; extensible to accommodate unlisted device types | All extensible — medical device terminology evolves rapidly; consuming systems must treat these as open value sets that will grow. |
| Specimen | 6 | Always — all 6 extensible | --SPEC, --SPCCND, --SPCUFL | Direct C-code per concept | Specimen type and condition validation; always extensible for site-specific specimen handling | Multiple codelists cover different specimen properties (type, condition, usability) — a consumer must use the correct codelist per variable, not conflate specimen type with specimen condition. |
| Adverse Event Qualifier | 5 | Mixed — 2 extensible, 3 non-extensible (majority-No) | AEACN, AETOXGR, AEOUT, AESEV | Direct C-code per concept | AE-specific qualifier validation; non-extensible codelists (outcome, severity) are truly closed scales | The non-extensible codelists (AEOUT, AESEV) represent fixed regulatory scales — these must never accept sponsor extensions; the extensible ones (ACN, TPACN) allow additional action-taken terms. |
| Anatomical Qualifier | 5 | Always — all 5 extensible | --LOC, --LAT, --DIR, --PORTOT | Direct C-code per concept | Anatomical position validation; extensible to accommodate anatomical specificity beyond the base terms | All extensible — consuming systems should expect sponsors to add more granular anatomical terms; these codelists collectively describe spatial position and should be used in combination for full anatomical qualification. |
| Microbiology/Immunology | 5 | Always — all 5 extensible | MB domain variables: --TSTDTL, --ORGNM, etc. | Direct C-code per concept | Domain-specific observation validation; extensible for organism and test detail additions | Domain-specialized Observation Qualifiers — structurally identical to the generic category but separated by strong naming signal; a consumer can apply the same validation pattern as Observation Qualifier. |
| Oncology Assessment | 4 | Mixed — 3 extensible, 1 non-extensible | RS/TR/TU domain variables | Concept-backed | Oncology response and tumor assessment validation; the non-extensible codelist (tumor identification results) is a closed evaluation set | Domain-specialized Observation Qualifiers for oncology — the non-extensible codelist (TUIDRS) represents a fixed assessment scale and must not accept extensions, unlike the other three. |
| Dictionary Reference | 3 | Always — all 3 extensible | DICTNAM, DECOD | Administrative | Dictionary name validation and dictionary-derived term context; extensible as new dictionaries emerge | These identify which external coding dictionary was used (MedDRA, WHODrug, etc.) — a consumer uses them for traceability to source dictionaries, not for clinical data validation. |
| ECG Findings | 3 | Always — all 3 extensible | EG domain variables: --LEAD, --ORRES (ECG-specific) | Direct C-code per concept | ECG-specific observation validation; extensible for additional lead configurations or finding terms | Domain-specialized Observation Qualifiers for ECG — separated from generic qualifiers by strong "ECG" naming signal; consuming logic is identical to Observation Qualifier within the EG domain scope. |
| Genomic | 3 | Always — all 3 extensible | GF domain variables: --TSTDTL, genomic-specific | Direct C-code per concept | Genomic findings validation; extensible as genomic testing expands rapidly | Domain-specialized Observation Qualifiers for genomics — the most rapidly evolving category; consuming systems should expect frequent additions and avoid hard-coding term lists. |
| Tobacco Product | 1 | Always — 1 extensible | --CAT (tobacco-specific) | Concept-backed | Tobacco product categorization; single extensible codelist | A Domain Category specialization for tobacco — could arguably merge into Domain Category; separated only because the naming pattern is distinctive. Consume identically to Domain Category. |

---

## Output 2 — Machine-Actionability Ranking

Definition: *a system can reliably determine which term applies using only the CT file and standard ontological relationships, without additional human judgment.*

1. **Instrument Test Code** — Closed enumeration (353/409) with deterministic code-to-concept mapping; extensible subset adds minor complexity.
2. **Instrument Test Name** — Identical actionability to Test Code; fully determined once TC is resolved.
3. **Instrument Original Result** — All non-extensible; question-specific allowed values are fully enumerable.
4. **Instrument Standardized Result** — Same as Original Result; closed enumeration per question.
5. **Parameter Name-Code** — All extensible but structurally identical paired-lookup pattern to TC/TN.
6. **Adverse Event Qualifier** — Small, well-defined set with majority non-extensible; regulatory-grade closed lists.
7. **Demographic** — Small, well-known variable set; non-extensible items (SEX) are trivially automatable.
8. **Unit of Measure** — Concept-backed units with C-codes; extensibility requires unit-registry integration.
9. **Anatomical Qualifier** — Concept-backed with direct C-codes; spatial qualifier selection is deterministic once the observation context is known.
10. **Specimen** — Direct C-code mapping; context-specific codelist selection is straightforward.
11. **Treatment Qualifier** — Direct C-codes but all extensible; requires sponsor-term handling.
12. **Method** — All extensible; method selection often requires human judgment about which analytical method was actually used.
13. **Clinical Classification** — Near-closed (26/27 non-extensible) but values represent clinical judgment (grades, stages) that a system cannot assign autonomously.
14. **Domain Category** — Mostly extensible; categorization of records within a domain requires understanding of the study's grouping logic.
15. **Dictionary Reference** — Administratively simple but adds no clinical validation capability; merely traces to external dictionaries.
16. **Disposition** — Context-dependent (which study phase?) and mostly extensible; disposition coding requires protocol knowledge.
17. **Device** — All extensible; device terminology is evolving and domain-specific.
18. **ECG Findings** — Domain-specific and all extensible; lead and finding identification is straightforward but result interpretation is not.
19. **Microbiology/Immunology** — All extensible; organism identification requires microbiological expertise beyond the CT file.
20. **Oncology Assessment** — Mixed extensibility; tumor response assessment requires clinical judgment.
21. **Genomic** — All extensible and rapidly evolving; genomic findings interpretation requires domain expertise.
22. **Role/Relationship** — Mostly extensible; role assignment requires study-specific organizational context.
23. **Trial Design** — Study-level metadata requiring protocol knowledge to select correct values.
24. **Tobacco Product** — Single extensible codelist; trivially simple but minimal standalone value.
25. **Observation Qualifier** — Heterogeneous residual; no uniform automation pattern — each codelist requires individual assessment of its qualifying role.

---

## Output 3 — Gap Analysis

| Category | Gap (max 10 words) | Who would need to act |
|---|---|---|
| Instrument Test Code | No explicit instrument-family grouping in flat file | CDISC (add instrument identifier or grouping metadata) |
| Instrument Test Name | TC↔TN pairing is implicit, not declared | CDISC (add explicit codelist pairing relationship) |
| Instrument Original Result | OR codelist-to-question mapping requires SV prefix parsing | CDISC (add explicit question-level linkage metadata) |
| Instrument Standardized Result | OR↔STR pairing undeclared; same gap as Original Result | CDISC (add explicit OR↔STR codelist pairing) |
| Clinical Classification | Boundary with Observation Qualifier is judgment-based | CDISC (define structural criterion for classification vs qualifier) |
| Observation Qualifier | No shared structural signature; residual category | CDISC (sub-classify by SDTM variable role) |
| Trial Design | Nothing — already self-describing | — |
| Treatment Qualifier | Nothing — already self-describing | — |
| Domain Category | Domain ownership is inferred from name, not declared | CDISC (add domain-linkage metadata to codelist header) |
| Method | Nothing — already self-describing | — |
| Demographic | Nothing — already self-describing | — |
| Disposition | Study-phase context inferred from name only | CDISC (add epoch/phase linkage) |
| Parameter Name-Code | PARMCD↔PARM pairing is implicit, same as TC↔TN | CDISC (same fix as TC↔TN — explicit pairing) |
| Role/Relationship | Nothing — already self-describing | — |
| Unit of Measure | Scope relationship (general vs domain-specific) undeclared | CDISC (declare subset/superset relationships) |
| Device | Nothing — already self-describing | — |
| Specimen | Nothing — already self-describing | — |
| Adverse Event Qualifier | Nothing — already self-describing | — |
| Anatomical Qualifier | Nothing — already self-describing | — |
| Microbiology/Immunology | Category is domain-specialized Observation Qualifier — distinction is naming-based only | CDISC (if domain specialization is intentional, declare it) |
| Oncology Assessment | Same as Microbiology/Immunology | CDISC (same action) |
| Dictionary Reference | Nothing — already self-describing | — |
| ECG Findings | Same as Microbiology/Immunology | CDISC (same action) |
| Genomic | Same as Microbiology/Immunology | CDISC (same action) |
| Tobacco Product | Single codelist — could merge into Domain Category | CDISC (consider whether standalone category is warranted) |

---

## Output 4 — Prompt 1 Sanity Check

- **No material miscategorizations detected.** All 1,181 assignments are HIGH confidence and the category boundaries are internally consistent with the structural signatures documented in Section 1.
- **One architectural observation:** Five categories (ECG Findings, Microbiology/Immunology, Genomic, Oncology Assessment, Tobacco Product — 16 codelists total) are acknowledged in Section 3.7 as domain specializations of Observation Qualifier. This is not an error — the Step 1 analysis correctly separated them because their naming patterns are strongly distinctive — but a consumer building category-level logic should know that these 5 + Observation Qualifier share a common consumption pattern and could be collapsed to a single "Qualifier" super-category if domain specificity is not needed.
- **The Tobacco Product category (1 codelist)** is the only singleton. It could reasonably be reclassified as Domain Category (it populates --CAT for tobacco). Its separation is defensible on naming grounds but fragile — if future releases add no further tobacco-specific codelists, merging would simplify the taxonomy.
