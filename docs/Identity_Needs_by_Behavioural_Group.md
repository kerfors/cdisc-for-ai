# Identity Needs Across COSMoS Behavioural Groups

*Where do DSS-level identifiers add real value? Analysis of 1,127 BCs and 1,123 DSSs across 31 SDTM domains.*

*cdisc-for-ai project -- March 2026*

---

## The question

COSMoS defines two levels: Biomedical Concepts (BCs) for semantic identity and Dataset Specializations (DSSs) for implementation detail. Each DSS carries a DS_Code (COSMoS `vlm_group_id`) -- a mnemonic code designed for human readability (GLUCSER = Glucose in Serum), not a stable machine identifier. DS_Codes are not unique across domains and lack the properties needed to function as persistent, resolvable identifiers.

Several approaches could make DSSs machine-addressable: constructing URIs from domain + DS_Code, assigning NCIt C-codes at the DSS level (paralleling how every BC already has one), or other schemes. The right mechanism is an open question. The prior question -- addressed here -- is *where* DSS-level identifiers add real value.

Five identity patterns emerge across the ten groups.

### A key distinction: collection templates, not medical ontology

COSMoS DSSs are derived from SDTM -- a submission and collection standard. A DSS models how a row looks in the dataset, not which clinically distinct measurements exist. It is, in effect, a template for a CRF row pattern. This is why MH has 11 DSSs (CRF template variants) and SU decomposes Alcohol into Beer/Wine/Spirits (collection form options).

The identity need for DSS-level identifiers arises where the collection template coincides with a genuine clinical distinction -- as in specimen-based domains where glucose in serum and glucose in urine are different CRF rows AND different clinical measurements. Where collection structure and clinical identity diverge, DSS-level identifiers address form design, not measurement identity.

For the full reasoning, see [What COSMoS DSSs Actually Model](COSMoS_Collection_vs_Ontology.md).

---

## 1. DSS-level identifiers justified

Decomposition creates clinically distinct specifications. A BC-level identifier is insufficient for operational use.

### Specimen Findings (LB, MB, MI, CP, BS)

One concept decomposes by specimen and result scale into variants with different LOINC codes, units, and clinical interpretation.

**Glucose Measurement (C105585) -- 1 BC, 8 DSSs in LB:**

| DS_Code | Specimen | Scale | Units | LOINC |
|---|---|---|---|---|
| GLUCSER | SERUM | Quantitative | mg/dL; g/L; mmol/L | Yes |
| GLUCPL | PLASMA | Quantitative | mg/dL; g/L; mmol/L | Yes |
| GLUCBLD | BLOOD | Quantitative | mg/dL; mmol/L | Yes |
| GLUCURIN | URINE | Quantitative | mg/dL; mmol/L; umol/L | Yes |
| GLUCPE | INTERSTITIAL FLUID | Quantitative | mg/dL; g/L; mmol/L | Yes |
| GLUCUA | URINE | Qualitative | -- | Yes |

Glucose in serum is not interchangeable with glucose in urine. Different reference ranges, different clinical significance, different LOINC codes. A mapping system that resolves "glucose" to a single BC cannot tell you which specimen, units, or LOINC code applies. The DS_Code is the operational identifier.

### Immunogenicity Findings (IS)

7 BCs produce 290 DSSs. Axis: target antigen, not specimen.

**Allergen-Induced IgE Antibody -- 1 BC, 92 DSSs (partial):**

| DS_Code | Target (encoded in mnemonic) | Scale |
|---|---|---|
| ARIGEABACA | American Cockroach Antigen | Quantitative |
| ARIGEABALM | Almond | Quantitative |
| ARIGEABCAT | Cat Dander | Quantitative |
| ARIGEABPEA | Peanut | Quantitative |
| ... | (46 allergen targets total) | ... |

IgE against peanut is a different clinical test from IgE against cat dander. The BC is too coarse -- without DSS-level identity, 46 distinct tests collapse into one concept. Problem: target identity is encoded in the DS_Code mnemonic, not a separate filterable column.

### Genomics Findings (GF)

10 BCs, 38 DSSs. All BCs fan out (max 6:1). Primary axis: result scale. Secondary: method. Same logic -- quantitative and qualitative versions of a genomics assessment are distinct specifications.

---

## 2. BC-level identifiers sufficient

1:1 or near-1:1 BC-to-DSS ratios. The DSS adds implementation detail but not a new identity.

### Measurement Findings (VS, MK, CV)

Systolic blood pressure is systolic blood pressure. No "serum variant" and "urine variant".

VS: 12 BCs, 16 DSSs. The 4 BCs with fan-out (SYSBP, DIABP, PULSE, HR) add location variants (7 arteries) and laterality (LEFT/RIGHT). But the measurement is still blood pressure in mmHg. Location and laterality are contextual attributes, not identity axes.

MK: 49 BCs, 50 DSSs -- essentially 1:1. CV: 6 BCs, 6 DSSs -- perfectly flat.

### Domain-specific Findings (DD, RP, SC, SR, UR)

Flat 1:1. No decomposition. RP: 96/96. DD: 13/13. UR: 10/10 (classified as Specimen-based in SDTM IG but behaviourally flat). The DS_Code adds no information beyond the BC's NCIt code.

### Instrument Findings (QS, FT, RS)

Identity sits at the instrument level, not the item level. QS: 17/17. FT: 23/23. RS: 129 BCs, 135 DSSs -- the 4 BCs that fan out do so by response criteria system (RECIST 1.1 / Lugano / RANO), arguably a distinct specification rather than a hierarchy position.

---

## 3. Protocol-driven identity

Fan-out encodes study design decisions, not measurement variants.

### Events (AE, DS, MH, BE)

**Medical History -- 1 BC, 11 DSSs:**

| DS_Code pattern | Represents |
|---|---|
| Free text | Open-ended collection |
| Prespecified | Structured form |
| Alzheimer's Disease | Protocol pre-populates this condition |
| Essential Tremor | Protocol pre-populates this condition |
| Visual Hallucinations | Protocol pre-populates this condition |
| ... | (9 disease-specific conditions total) |

Not 11 ways to measure medical history -- 11 protocol decisions about which conditions matter. AE: 1 BC, 2 DSSs. DS and BE: flat 1:1.

### Interventions (CM, EX, PR, SU)

**Substance Use -- 3 BCs, 12 DSSs:**

| BC | DSSs |
|---|---|
| Alcohol | Beer, Wine, Spirits |
| Caffeine | Coffee, Cola, Tea |
| Tobacco | Cigarette, Cigar, Pipe |

Beer is not a different way to measure alcohol -- it is a subtype. The protocol decides which subtypes to collect. Same for PR: CT Scan → Chest CT, MRI → Brain MRI, X-Ray → Chest X-Ray.

---

## 4. Relational identity

### Clinical Assessment (FA, TR, TU, IE)

TR: 4 BCs, 9 DSSs with fan-out by method and anatomical context. But a tumor measurement is meaningless without knowing which tumor, which visit, which parent record. Identity is relational (RELREC), not standalone. FA and IE: flat 1:1.

---

## 5. Not applicable

### Trial Design (TS)

128 BCs, 129 DSSs. Study-level parameters. BC_Scope = Study. Outside subject-level identity scope.

---

## Summary

| Identity pattern | Groups | Domains |
|---|---|---|
| **DSS-level justified** | Specimen, Immunogenicity, Genomics | LB, MB, MI, CP, BS, IS, GF |
| **BC-level sufficient** | Measurement, Domain-specific, Instrument | VS, MK, CV, EG, DD, RP, SC, SR, UR, QS, FT, RS |
| **Protocol-driven** | Events, Interventions | AE, DS, MH, BE, CM, EX, EC, PR, SU |
| **Relational** | Clinical Assessment | FA, TR, TU, IE |
| **Not applicable** | Trial Design | TS |

Making DSSs addressable and linkable -- by whatever mechanism -- is most urgent for the first group. These are the domains where "glucose" is not enough and you need "glucose in serum, quantitative, in mg/dL."

---

*Sources: COSMoS public BC/DSS exports, SDTM IG v3.4, NCI EVS. All examples from actual published content. Not an official CDISC product. Part of [cdisc-for-ai](https://github.com/kerfors/cdisc-for-ai).*
