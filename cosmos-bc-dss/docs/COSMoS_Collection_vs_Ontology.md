# What COSMoS DSSs Actually Model

*Understanding Dataset Specializations as collection templates, not medical ontology.*

*cdisc-for-ai project -- March 2026*

---

## The two layers

COSMoS defines two levels. The BC (Biomedical Concept) level carries semantic identity: an NCIt concept code, a definition, synonyms. This is the closest COSMoS comes to medical ontology -- "Glucose Measurement" (C105585) names a concept that exists independently of any data collection system.

The DSS (Dataset Specialization) level sits below. It specifies how that concept appears as a row in an SDTM dataset: which specimen, which method, which result scale, which units. A DSS is identified by a DS_Code (COSMoS `vlm_group_id`) -- a mnemonic code like GLUCSER (Glucose in Serum) designed for human readability.

## DSSs model collection structure, not clinical concepts

The critical insight: DSSs are derived from SDTM, which is a submission and collection standard. A DSS models "how does a row look in the dataset?" -- not "which clinically distinct measurements exist?". It is, in effect, a template for a specific CRF row pattern.

This origin shapes everything about how DSSs decompose:

**Medical History** has 1 BC and 11 DSSs. Not because medical history has 11 clinically distinct measurement types, but because there are 11 CRF template variants: free text collection, prespecified structured form, and 9 disease-specific forms (Alzheimer's Disease, Essential Tremor, Visual Hallucinations...). An Alzheimer's trial pre-populates different conditions than an oncology trial. The DSSs encode protocol design decisions.

**Substance Use** decomposes Alcohol into Beer, Wine, and Spirits. Not because these are medically distinct concepts requiring separate identifiers, but because a CRF may ask about consumption by beverage type. The DSS models the form, not the pharmacology.

**Procedures** decomposes CT Scan into CT Scan (general) and Chest CT. The specialisation is a protocol decision -- this oncology study cares about chest imaging -- not a fundamentally different medical procedure.

## Where collection template meets clinical reality

In some domains, the CRF row pattern happens to coincide with a genuine clinical distinction. This is where the DSS level carries real semantic weight.

**Laboratory (LB):** Glucose in serum and glucose in urine are different CRF rows AND different clinical measurements. They have different LOINC codes, different reference ranges, different clinical interpretation. The specimen decomposition axis creates DSSs that are simultaneously collection templates and clinically meaningful measurement specifications.

**Immunogenicity (IS):** IgE against peanut and IgE against cat dander are different CRF rows AND different clinical tests. The target-antigen decomposition creates DSSs with genuine diagnostic identity.

**Genomics (GF):** Quantitative and qualitative versions of a genomics assessment are different CRF rows AND different result types with different downstream use.

In these domains, the DSS is more than a form layout -- it is an identifiable measurement specification.

## Why this matters

The COSMoS model is intentionally generic: one BC schema and one DSS schema serve all 31 domains. This generality is a design feature, not a flaw. But it means the same structural relationship (BC→DSS) carries fundamentally different meaning depending on where you are:

| Domain type | What a DSS represents | Example |
|---|---|---|
| Specimen/IS/GF | A clinically distinct measurement specification | GLUCSER = glucose in serum (own LOINC, own reference range) |
| Events/Interventions | A protocol-driven collection template | MH Alzheimer's = CRF pre-populates this condition |
| Instruments | A position in a question hierarchy | EQ-5D Mobility = one item within the EQ-5D-5L instrument |
| Domain-specific | A 1:1 mirror of the BC | DD Cause of Death = same information at both levels |

A consumer who treats all DSSs the same -- as if every DS_Code identifies a distinct clinical entity -- will overweight form design choices and underweight genuine measurement distinctions. The behavioural group classification exists precisely to make this difference visible.

## The study design perspective

The collection-template nature of DSSs is not confined to COSMoS. It runs through the entire chain. USDM (Unified Study Definitions Model) includes BCs as part of the study definition, and structured study design tools like OpenStudyBuilder and 360i push specificity upstream into protocol design. But these systems also inherit the CRF focus: they define what will be *collected*, not what *exists* in medicine.

This creates a practical tension for study designers. When building the laboratory section of a protocol, a designer needs to select specific things: sometimes a panel ("Comprehensive Metabolic Panel"), sometimes an individual precise test ("Glucose in Serum, quantitative"). The thing being selected needs to be unambiguously identifiable. The BC level -- "Glucose Measurement" -- is not specific enough. The designer needs to point at the DSS level: GLUCSER, GLUCBLD, GLUCURIN.

From a study design perspective, these mnemonic codes are exactly the identifiable things a designer needs to point at. But they are mnemonic codes, not persistent identifiers. They lack the properties that study design tooling and automation require: resolvability, stability across releases, uniqueness without domain context.

The need is clearest in the specimen-based, immunogenicity, and genomics domains -- where the DSS level coincides with a clinically distinct measurement specification that a study designer genuinely needs to select between. In events and interventions, the designer makes protocol-level choices (which conditions to pre-populate, which substance subtypes to collect) that are study-specific rather than measurement-specific.

## Implications for identifiers

The argument for making DSSs machine-addressable (through URIs, NCIt codes at the DSS level, or other mechanisms) has different weight depending on which behavioural group a domain belongs to. Where collection template and clinical reality coincide, a DSS-level identifier carries real semantic value. Where they diverge, it identifies a form variant.

See [Identity Needs Across COSMoS Behavioural Groups](Identity_Needs_by_Behavioural_Group.md) for the detailed analysis by group.

---

*Sources: COSMoS public BC/DSS exports, SDTM IG v3.4, NCI EVS. All examples from actual published content. Not an official CDISC product. Part of [cdisc-for-ai](https://github.com/kerfors/cdisc-for-ai).*
