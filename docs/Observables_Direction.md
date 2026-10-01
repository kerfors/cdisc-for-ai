# Direction: observables, more expressive reference files, RDF/OWL

*Written 2026-10-01. Updated as the steps are done.*

Three steps, in order: find out what identifies an observable in the CDISC standards and whether a conclusion can be drawn; then make the Excel reference files express it; later, move towards RDF/OWL.

## Where we stand (COSMoS 2026-07-14, SDTM CT 2026-09-25)

[`domain-behaviour/Domain_Behaviour.ipynb`](../domain-behaviour/notebooks/Domain_Behaviour.ipynb) re-derives, per domain, which variables distinguish the Dataset Specializations (DSSs) of one Biomedical Concept (BC). Of 83 BCs that fan out into more than one DSS:

| Axis | BCs | Domains |
|---|---|---|
| specimen | 29 | LB, GF, IS |
| scale (some DSSs with units, some without) | 20 | LB, MB, GF, IS |
| test detail (TSTDTL) | 18 | GF, MI, MB, IS |
| category (CAT/SCAT) | 18 | MH, SU, CM, PR, RS, LB |
| location (LOC/LAT/POS) | 11 | VS, MK, PR, EC |
| evaluator | 10 | RS, TR, TU |
| method | 9 | LB, GF, IS |
| binding agent (BDAGNT) | 6 | IS |
| none (only the DS code differs) | 5 | AE, TS, TU |

Other findings from the same run:
- Only LB fans out primarily by specimen. MB fans out by scale and test detail, MI by test detail, GF by test detail, IS by binding agent.
- Every DSS in LB, MB, MI, IS and GF carries a specimen; in UR only 10% do.
- The March 2026 exclusion reasons for IS ("target only in the DS code") and GF ("scale-driven") no longer described the content; both are restated in the `Consumer_Exclusions` sheet of [`SDTM_Domain_Metadata.xlsx`](../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx) and hold now.

## Reading (not yet tested)

The axes fall into two groups. The test is the line between Biomedical Concept and Dataset Specialization: does the attribute change the observation itself, or only where and how an unchanged observation is filed?

- **Observation-changing:** specimen, binding agent, test detail, method, scale — glucose in serum vs urine, IgE against cockroach vs peanut are different observables. Mostly the specimen-based domains.
- **Collection-context:** category, evaluator — which conditions a form pre-specifies, who assessed a tumour. Mostly events, interventions and response domains (the March analysis's "protocol-driven" group).
- **In between:** location — blood pressure at arm vs ankle is arguably a different observable; a location variant of a procedure is not.

Working formulation: an observable = a BC plus its observation-changing axes. A COSMoS DSS bundles those with collection choices, and domains differ in which kind dominates. This supports specifying observables on the BC rather than the DSS, as explored for glucose in [`Glucose_Siblings_BC_DSS_Proposal.html`](../cosmos-bc-dss/docs/Glucose_Siblings_BC_DSS_Proposal.html), but it is a reading of the data, not something the data states.

## Step 1 — test the observable reading

- Classify each axis as observation-changing or collection-context (location case by case); record the classification as data, not in code.
- Compare the observation-changing axes with LOINC's axes (component, property, system, scale, method) using the observables notebooks in [`cosmos-bc-dss/`](../cosmos-bc-dss/) (`COSMoS_Observable_Derivation`, `COSMoS_Observable_LOINC_Check`) and their LOINC cache.
- Decide what the comparison supports: a conclusion, or where the reading fails.
- Related open question: what the specimen-based Findings consumer is for — "specimen is the decomposition axis" (fits LB only) or "observation made on a specimen" (fits LB, MB, MI, IS, GF). MB and MI stay in it for now.

## Step 2 — make the Excel reference files more expressive

Once observables have a working definition, state it in the files instead of leaving it implicit:
- an observable key per DSS;
- the identifying axes as named columns, not only inside the variable pivots;
- continue the pattern of the October 2026 corrections: identity keyed on NCIt codes rather than mnemonics (the TESTCD + NCIt join fix), reasons stated as data (`Consumer_Exclusions`), classifications read from what CT publishes (instrument class, C66734 domain codes).

## Step 3 — towards RDF/OWL

The long-run aim: publish the reference files as RDF/OWL that expresses the behaviour of the standards, related to established ontologies. By then the files would carry the distinctions that need predicates: link kinds from [`link-semantics/`](../link-semantics/), the observable structure from step 1, and identity on NCIt codes.

## See also

- [Domain behaviour](https://kerfors.github.io/cdisc-for-ai/analyses/domain-behaviour.html) — the analysis page behind the table above, regenerated on each COSMoS release
- [`Changes_2026-10.md`](Changes_2026-10.md) — the corrections that led here
