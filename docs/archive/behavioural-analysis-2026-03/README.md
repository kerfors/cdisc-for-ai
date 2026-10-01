# Behavioural analysis — archived March 2026 snapshots

The analysis behind the repository's early design: how the BC-to-DSS relationship behaves across SDTM domains, the behavioural groups and identity patterns, and the three analytical layers. Written in March 2026 against the COSMoS package of that month; the domain overview against NCI EVS SDTM CT 2025-09-26. Archived 2026-10. They are not maintained. The current domain classification lives in [`sdtm-domain-reference/SDTM_Domain_Metadata.xlsx`](../../../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx); the Findings consumers take their scope from it.

- `SDTM_Domain_Overview.md` — three analytical layers, structural types (was at the repository root)
- `COSMoS_Behavioural_Analysis.md` — ten behavioural groups, six decomposition axes (was in `cosmos-bc-dss/docs/`)
- `COSMoS_Domain_Pattern_Inventory.xlsx` — domain-by-domain behavioural-group classification, built by hand (was in `cosmos-bc-dss/docs/`)
- `Identity_Needs_by_Behavioural_Group.md` — where DSS-level identifiers add value (was in `docs/`)
- `COSMoS_Collection_vs_Ontology.md` — DSSs as collection templates, not medical ontology (was in `cosmos-bc-dss/docs/`)

The documents are kept as written. Links inside them point to their original locations. A check on 2026-10-01 against COSMoS 2026-07-14 and SDTM CT 2026-09-25 found the points below.

## Not consistent when written

- **Population.** The Behavioural Analysis counts 1,345 BCs and 1,326 DSSs over 32 domains; Identity Needs counts 1,127 BCs and 1,123 DSSs over 31 domains. The two do not describe the same population.
- **Measurement scope.** The Behavioural Analysis gives the measurement consumer as "two sheets (VS, MK, RE, CV)". The consumer notebook never included RE; it did from 2026-10-01.

## Changed since

- **Population:** 1,475 BCs and 1,475 DSSs over 32 domains.
- **Result-scale vocabulary:** "Qualitative" no longer appears in COSMoS. The values are Nominal, Ordinal, Quantitative, Temporal and Narrative. Counts such as "16 qualitative" (QS) or "132 qualitative" (RS) use the old term.
- **EG:** still 33 BCs, all 1:1, but no longer all Qualitative — 18 Quantitative, all with units, and 15 Nominal, none with units (republished in the 2026-05-26 package). EG is in the measurement consumer from 2026-10-01.
- **IS:** 7 BCs, 326 DSSs (was 290). The largest fan-out under one BC is 128:1 (was 92:1).
- **MH:** 1 BC, 13 DSSs (was 11).
- **LB** 98 BCs / 147 DSSs (was 97 / 146); **MB** 10 / 14 (6 / 7); **MI** 4 / 8 (3 / 7); **RS** 151 / 157 (129 / 135).
- **FT:** 23 BCs — 16 Ordinal, 6 Quantitative, 1 Temporal (was "all quantitative").
- **Domain overview:** SDTM CT 2025-09-26 and 56 domains. The domain reference now carries 67 domains at SDTM CT 2026-09-25, ten of them added from the CT SDTM Domain Abbreviation codelist (C66734).

## Still holds

- The BC-to-DSS relationship means different things in different domains, and the per-group patterns are unchanged: IS fans out by target antigen; GF has all 10 BCs fanning out (38 DSSs, at most 6:1); UR has 10 BCs, all 1:1; VS has 74 BCs and 78 DSSs with 4 fanning out; MK has 49 BCs and 50 DSSs with 1 fanning out; LB still has 30 BCs fanning out; RE is flat, 135 BCs to 135 DSSs; QS (17) and FT (23) are all 1:1; RS still has 4 BCs fanning out by response criteria.
- MH and SU still decompose by form variant — prespecified conditions for MH; beer, wine and distilled spirits for SU.
