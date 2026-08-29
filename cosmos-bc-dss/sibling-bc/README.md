# sibling-bc — loadable form of the Glucose Siblings sketch

The single-file sketch (`../docs/Glucose_Siblings_LinkML_Sketch.yaml`,
2026-08-24) is readable but not loadable: no LinkML tool can open a yaml
with `schema:`/`data:` keys, and its bare-name imports resolve only by
accident. This folder is the split that tools can run.

## Files

- `sibling_bc.schema.yaml` — the schema: QualifiedBiomedicalConcept
  (sibling), ExternalMapping, SemanticValueSetTerm,
  InterpretationRegimeAssertion, Recording, plus the
  SiblingBcSketchData container. The six boundary rules are stated in
  the file header.
- `sibling_bc.instances.yaml` — FOUR glucose siblings (the proposal's
  count; GlucoseUrineQuantitative/GLUCURIN added relative to the
  sketch) and six recordings. GLUCBLD stays parked.
- `sibling_bc.schema.json` — generated JSON Schema (`gen-json-schema`),
  committed for JSON-side consumers.
- `cosmos_linkml_v1.0/` — pinned, unmodified copies of the published
  COSMoS v1.0 LinkML schemas the imports resolve against.
- `validate.sh` — regenerates the JSON Schema and validates the
  instances (`linkml-validate`, target class SiblingBcSketchData).

## Verified against

COSMoS package 2026-07-14; LOINC 2.82 via `../cache/loinc_service_cache.json`
(all cited LOINC parts read from the cache, none asserted from memory);
COSMoS LinkML v1.0 (pinned copies); linkml 1.11.1.

## Decisions vs the sketch (2026-08-29)

- **Own class, not is_a.** `QualifiedBiomedicalConcept` is deliberately
  not a subclass of `cosmos_bc:BiomedicalConcept`: that class's
  identifier slot is pattern-locked to `C[0-9]+|NEW_...` and LinkML
  allows one identifier per class, so subclassing would force either
  pattern abuse or NEW_ identity. The relationship is machine-readable
  instead: class-level `broad_mappings` + instance-level
  `broaderConceptId`. Promotion to `is_a` later is mechanical; the
  reverse is not.
- **admissibleSpecimens** ranges over a BC-side `ConceptTerm`
  (NCIt concept + preferred term), not `cosmos_sdtm:AssignedTerm`;
  the recording's `specimen` keeps the SDTM AssignedTerm.
- **One convention for "not yet governed":** `sourceAnchor` starting
  `[VERIFY]` — used by the urine semantic value set AND by every
  invented `sbc:regime/...` URI and the `stateValue: "*"` assertion.
- **Import order is load-bearing** (documented in the schema): both
  published schemas define a `dataType` slot with different enums;
  LinkML merges imports last-wins, so `cosmos_bc_model` is imported
  last. This schema instantiates no SDTM element that uses the sdtm
  `dataType` slot.

The validator is not vacuous: with the wrong import order it rejects
`dataType: string/boolean` on the DECs — that failure is how the
last-wins collision was found.
