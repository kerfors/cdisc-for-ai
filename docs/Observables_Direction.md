# Direction: observables, more expressive reference files, RDF/OWL

*Written 2026-10-01. Updated as the steps are done; last update 2026-10-31.*

Three steps, in order: find out what identifies an observable in the CDISC standards and whether a conclusion can be drawn; then make the Excel reference files express it; later, move towards RDF/OWL.

## Re-based on the IG (2026-10-31)

SDTMIG v3.4 publishes more of the decomposition than this page first assumed. The IG statements are collected, quoted, in [`SDTMIG_Statements.xlsx`](../sdtm-domain-reference/machine_actionable/SDTMIG_Statements.xlsx): a generic test code with qualifier variables (§4.1.9); the aspects of a lab test associated with a LOINC code, four base and the rest conditional (LB Assumption 8); the analyte as ISTEST with ISBDAGNT; the microbiology test detail; the gene in GFSYM. That published facet model is now the base. The COSMoS fan-out and LOINC are cross-checks beside it.

What the IG does not define is the observable. It leaves the uniqueness of a test to the sponsor's natural key, and a natural key, like a Dataset Specialization, is about SDTM storage and transfer. The observable is a concept: what makes an observation specific. Where the standards are silent or disagree, our position stays in `Variable_Meaning`, each basis citing the IG statements where they exist. See [Phase 1, Reassessment](Observables_Phase1.md#reassessment-2026-10-31).

## Where we stand (COSMoS 2026-07-14, SDTM CT 2026-09-25)

Evidence from COSMoS, a cross-check against the published facet model.

[`domain-behaviour/Domain_Behaviour.ipynb`](../domain-behaviour/notebooks/Domain_Behaviour.ipynb) re-derives, per domain, which variables distinguish the Dataset Specializations (DSSs) of one Biomedical Concept (BC). An axis is counted when the assigned value of the variable differs between the DSSs. Where only the value list differs, it is counted separately. Of 83 BCs that fan out into more than one DSS:

| Axis | Assigned value differs (BCs) | Domains | Only the value list differs (BCs) | Domains |
|---|---|---|---|---|
| specimen | 29 | LB, GF, IS | 0 | |
| scale (some DSSs with units, some without) | 20 | LB, MB, GF, IS | n/a | |
| test detail (TSTDTL) | 18 | GF, MI, MB, IS | n/a | |
| category (CAT/SCAT) | 15 | LB, RS, CM, MH, PR | 3 | SU |
| method | 9 | LB, GF, IS | 0 | |
| binding agent (BDAGNT) | 6 | IS | n/a | |
| location (LOC/LAT/POS) | 4 | PR | 7 | VS, EC, MK, PR |
| evaluator | 0 | | 10 | RS, TR, TU |
| none (no assigned value differs) | 20 | AE, EC, MK, SU, TR, TS, TU, VS | | |

Until 2026-10-06 the two columns were counted together. That made evaluator look like an axis in RS, TR and TU, and location look like one in VS.

Other findings from the same run:
- Only LB fans out primarily by specimen. MB fans out by scale and test detail, MI by test detail, GF by test detail, IS by binding agent.
- Every DSS in LB, MB, MI, IS and GF carries a specimen; in UR only 10% do.
- The March 2026 exclusion reasons for IS ("target only in the DS code") and GF ("scale-driven") no longer described the content; both are restated in the `Consumer_Exclusions` sheet of [`SDTM_Domain_Metadata.xlsx`](../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx) and hold now.

## Working formulation

*The reading of 2026-10-06, before Phase 1, is retired; the positions now held are in `Variable_Meaning` in [`SDTM_Domain_Metadata.xlsx`](../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx), each with its basis.*

The test is the line between Biomedical Concept and Dataset Specialization: does the attribute change the observation itself, or only where and how an unchanged observation is filed?

An observable = a BC plus its observation-changing axes. A COSMoS DSS bundles those with collection choices, and domains differ in which kind dominates. This supports specifying observables on the BC rather than the DSS, as explored for glucose in [`Glucose_Siblings_BC_DSS_Proposal.html`](../cosmos-bc-dss/docs/Glucose_Siblings_BC_DSS_Proposal.html), but it is a reading of the data, not something the data states. The axes above are named after SDTM variables, and a variable does not say what the distinction means. The meaning has to be named separately from the variable that carries it.

## Step 1 — test the observable reading

Read and record what the standards publish. No classification by our own judgement. Where the published sources do not settle whether a distinction changes the observation, record it as undecided, with both readings.

Done 2026-10-08 ([Observables, Phase 1](Observables_Phase1.md)); reassessed 2026-10-31 against the IG statements ([Reassessment](Observables_Phase1.md#reassessment-2026-10-31)).

- Related open question: what the specimen-based Findings consumer is for — "specimen is the decomposition axis" (fits LB only) or "observation made on a specimen" (fits LB, MB, MI, IS, GF). MB and MI stay in it for now.

## Step 2 — make the Excel reference files more expressive

Once observables have a working definition, state it in the files instead of leaving it implicit:
- an observable key per DSS;
- the identifying axes as named columns, not only inside the variable pivots;
- continue the pattern of the October 2026 corrections: identity keyed on NCIt codes rather than mnemonics (the TESTCD + NCIt join fix), reasons stated as data (`Consumer_Exclusions`), classifications read from what CT publishes (instrument class, C66734 domain codes).

**Done so far (2026-10-08).** Phase 1 settles the core axes at the level of the variable: test code, test detail and binding agent as component, specimen as system, `--METHOD` as method. For LB, LB Assumption 8 states these (reassessment 2026-10-31). It does not yet settle a key per DSS:
- the per-DSS reading of scale is open (units present, or the `--ORRES` data type; neither is right throughout);
- a key would carry the assignment errors in COSMoS as they are, such as the two found by the LOINC check (nicotine, `HGBBLDDIP`);
- Phase 1 read the BCs that fan out; for BCs with one DSS the key would come from a rule not tested against them.

So Step 2 started at the variable level. The three Findings consumer files in [`sdtm-findings-graph/`](../sdtm-findings-graph/) now have an `Axis_Meaning` sheet: the rows of `Variable_Meaning` that apply to the file (Position, Basis, Status) and the `Measurement_Specs` columns each row refers to. It says which columns identify the observable, which are open, and on what basis. It is our position, not a published fact, and carries the basis note with each position (since 2026-10-31; `Immunogenicity_Findings` has one too).

Then a key per DSS for LB, MB and MI only, in `Specimen_Findings`: `bc_id | component | system | scale | method`, built from the `Axis_Meaning` rows. Scale is in the key, by the accepted rule, read as units present or absent. That is the reading the file supports; it stays marked as open. Without scale, concentration and presence in urine (glucose, protein and others) would share a key. In MB and MI the key holds test code and test detail only, because `Variable_Meaning` has no rows for their specimen and method (they never separate sibling DSSs, so the grouping is the same either way).

Parked: reading what is published for the identifying variables that never separate sibling DSSs (`MBSPEC`, `MISPEC` and others), so they can get rows with a basis. Needed when the key is extended beyond LB, MB and MI.

Phase 2 closed on 2026-10-08 with this scope; see [Observables, Phase 2](Observables_Phase2.md). The 2026-10-31 reassessment adds one open point: the key has no property part, which LOINC uses and CDISC carries in the units (and, by one reading, in test detail).

## Step 3 — towards RDF/OWL

The long-run aim: publish the reference files as RDF/OWL that expresses the behaviour of the standards, related to established ontologies. By then the files would carry the distinctions that need predicates: link kinds from [`link-semantics/`](../link-semantics/), the observable structure from step 1, and identity on NCIt codes.

## See also

- [`SDTMIG_Statements.xlsx`](../sdtm-domain-reference/machine_actionable/SDTMIG_Statements.xlsx) — what SDTMIG v3.4 says about test facets and domain routing, quoted (2026-10-31)
- [Interpretation context](Interpretation_Context.md) — what the record carries beside a value so it can be read, and how COSMoS uses it (2026-10-12)
- [Who rates?](https://kerfors.github.io/cdisc-for-ai/examples/who-rates.html) — worked example (early, exploratory): the instrument reclassifications in SDTM CT 2026-09-25, today's representation against an explicit graph
- [Domain behaviour](https://kerfors.github.io/cdisc-for-ai/analyses/domain-behaviour.html) — the analysis page behind the table above, regenerated on each COSMoS release
- [`Changes_2026-10.md`](Changes_2026-10.md) — the corrections that led here
