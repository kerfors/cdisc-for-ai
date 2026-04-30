# X-Ray Case Study — Follow-ups and Learnings

Branch: `xray-cross-class`. Date: 2026-04-30.

What to pick up after this branch closes.

## Artefacts produced

Three HTML documents in `docs/`:

- `XRay_CaseStudy_Overview.html` — sponsor-facing briefing. NOT linked from `docs/index.html`.
- `XRay_COSMoS_Story.html` — recording view across PR (Interventions) + MK / TR / TU (Findings). Part 3 realigned from legacy `cosmos-bc-dss` flattening to `consumer-bases/DSS_View` joined view. Part 2 → Part 2A; new Part 2B added (TR + TU sibling sections).
- `XRay_PatientBurden_Story.html` — SoA / burden view. Part 2 and footer realigned to graph-fed source. Option 4 refined for method-agnostic BCs. Summary cross-linked to COSMoS Story Part 2B.

No code, no new track. The earlier `sdtm-interventions-graph/Design_Notes.md` memo was deleted as out of scope after scope was pulled back to X-Ray-only.

## Architectural learnings

1. **BC nature drives `--METHOD` value_list breadth on the Findings side.** Named scoring instruments (MK Sharp/Genant, Sharp/Van der Heijde) → narrow value_list (X-RAY;MRI). Method-agnostic measurement / identification concepts (TR Longest Diameter, TU Tumor Identification) → wide value_list (15-method imaging panel). Empirically consistent, traceable to BC's NCIt anchor type.

2. **Cross-class joins via shared NCIt anchors are projected fact, not editorial overlay.** The same NCIt code appears as BC anchor on one side and as `--METHOD` value_list member on the other side, joined via METHOD codelist (C85492). 40 X-Ray-modality (PR DSS, Findings DSS) pairs from `cosmos-graph` alone, no authoring required. The earlier framing of the bridge as "editorial overlay territory" was wrong.

3. **`DSS_View.Measurement_Specs` is a pins-only projection.** Slot value_lists do NOT survive — recovering them requires reading `cosmos-graph/interim/COSMoS_Graph.xlsx` Variables sheet directly. Deliberate semantic contract, but a gap relative to the cross-class bridge use case.

4. **Imaging Findings DSSs model rich qualifier vocabulary** (LOC, LAT, DIR, METHOD, EVAL, EVALID, ORRES, STRESC, STRESN, ORRESU, STRESU, DTC, identifiers). Position is specifically absent — not "all qualifiers". The PatientBurden gap is sharper than "imaging DSSs model nothing".

5. **`--METHOD`-as-qualifier is a 332-DSS pattern across 9 Findings domains** (FA, GF, IS, MB, MK, SR, TR, TU, UR). 290 IS immunoassay DSSs are the bulk. X-Ray's 20 imaging-relevant DSSs are one well-bounded instance of a much larger pattern.

6. **Modality compatibility ≠ clinical pairing.** The cross-class bridge expresses what the standards permit, not typical clinical use. Anatomical co-occurrence (PRLOC vs MKLOC / TULOC etc.) is sponsor- and protocol-level, not COSMoS-level. Any tool consuming the bridge needs to be honest about this.

## Follow-up work items

- **DSS_View enhancement** — separate branch `dss-view-value-lists`. Add `<SLOT>_value_list` and `<SLOT>_value_list_ncit` per slot in `consumer-bases/interim/DSS_View.xlsx` Measurement_Specs sheet. Update notebook `consumer-bases/notebooks/10_dss_view.ipynb` and the ReadMe contract. Makes the cross-class bridge a one-step join from a single artefact and benefits all 332 method-as-qualifier DSSs, not just imaging.

- **332-DSS `--METHOD` pattern** — future case-study material. The 290-DSS IS immunoassay sub-pattern in particular deserves a dedicated analytical note: it is the architectural mass of method-as-qualifier in COSMoS, with its own internal structure (RIA / ELISA / IMMUNOASSAY value_list combinations).

- **Procedure-side beyond imaging** — biopsies, ablations, endoscopies. PR DSSs touched only in passing in this case study. The cross-class bridge framing should generalise; not yet verified empirically.

- **PatientBurden speculative layer decision** — Parts 3 (case specialisations), 4 (four options), Registry-band, ID101/ID102/ID103 placeholders sit in Template/Instance/Profile territory (status SPECULATIVE per `MEMORY.md`). Decision pending: keep speculative / promote / retire.

- **Index inclusion** — all three HTMLs intentionally off `docs/index.html`. Reconsider when promoting case study to public.

- **RELREC modelling** — explicitly out of scope. Case study identifies where the link lives (SDTM data layer + sponsor metadata, not COSMoS) but does not extend the repo to model record-to-record relationships.

## Data hygiene observations

- `TUMIDENT` carries variables `PRVIR` / `PRVIRP` (no `TU` prefix); sibling `TUMIDENT_RECIST1_1` has them correctly as `TUPRVIR` / `TUPRVIRP`. Both flagged `is_nonstandard=False` in COSMoS. Source-data inconsistency, noted inline in COSMoS Story Part 2B (yellow row).

- `AUTOPSY` and `PINCH DYNAMOMETRY` appear in some `--METHOD` value_lists but do not resolve in METHOD codelist (C85492). Surfaced during the early scoping pass; not imaging-relevant for this case study, but worth flagging if the 332-DSS pattern is picked up later.

## Source data and where to read first

- Sponsor entry point: `docs/XRay_CaseStudy_Overview.html`.
- Empirical findings and BC-nature insight: `docs/XRay_COSMoS_Story.html` Part 2B (cross-domain insight box).
- DSS_View pins-only contract: `docs/XRay_COSMoS_Story.html` Part 3 (the "what survives" notes on the SGBESCR row).
- Position-gap analysis: `docs/XRay_PatientBurden_Story.html` Part 2 + Summary.
- Underlying data: `cosmos-graph/interim/COSMoS_Graph.xlsx` (sheets: BC, DSS, Variables, Codelists, BC_Categories, BC_Parents) and `consumer-bases/interim/DSS_View.xlsx` (Test_Identity + Measurement_Specs).
