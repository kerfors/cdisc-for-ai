# Instances

- `GlucoseBloodQuantitative.dds.json` — the sibling BC and its thinned
  GLUCPL recording expressed in base-DDS vocabulary (ReifiedConcept /
  CodeList / ItemGroup fragments). Authored 2026-08-29 against
  cdisc-org and TeMeta schemas; identical to the file shared in chat.
- `GlucoseBloodQuantitative.profiled.dds.json` — same content plus the
  profile's ddsq* extension slots (result scale, broader concept,
  interpretation regimes, per-property data types). Stripping every
  ddsq* key yields a base-valid instance (checked by ../validate_dds.py).
- `HCVRNASiblings.dds.json` / `HCVRNASiblings.profiled.dds.json` — the
  second worked case: the two HCV RNA siblings (quantitative viral
  load vs qualitative detection, same serum/plasma specimen — a scale
  seam within one specimen, complementary to glucose's specimen x
  scale split), their code lists and both thinned MB recordings; the
  profiled variant adds the ddsq* slots. LOINC anchors (fetched
  2026-08-29, cached at ../../cache/loinc_hcvrna_search_cache.json)
  ride on the base coding slot with AliasPredicate: NARROW_SYNONYM for
  the method-pinned leaves, BROAD_SYNONYM for NCIt analyte and LOINC
  order/collation term. HCV RNA is in the engine's
  example study NCT01797120 (pinned to HCRNASERPL via the USDM
  extension attribute). The detection recording carries MBTSTDTL
  DETECTION as `preSpecifiedValue` — the package's encoding of the
  scale split as a test detail.
- `CONC.BiomedicalConcept_55.dds.json` — the 360i engine's OWN glucose
  concept, extracted verbatim from
  cdisc-org/data-definition-engine data/protocols/NCT01797120/NCT01797120-dds-latest.json
  at commit 97acb8a65090ebae2d598983aed490ab40b094ec (2026-08-26).
  It validates against base AND against the profile unchanged — the
  extensions are optional, so the profile sits on top of what the
  engine already produces.

Note: the recordings link to their concept with
`ItemGroup.implementsConcept`. That is the slot the base model intends
("specialization of an abstract concept topic", and it appears again on
`Method`) and the one the engine emits: 13 of the 17 itemGroups in
`NCT01797120-dds-latest.json` carry it, with `Item.conceptProperty` at
variable level. `Governed.wasDerivedFrom` was used in the first draft
and has been aligned.
