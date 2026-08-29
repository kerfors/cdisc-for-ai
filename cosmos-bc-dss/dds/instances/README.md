# Instances

- `GlucoseBloodQuantitative.dds.json` — the sibling BC and its thinned
  GLUCPL recording expressed in base-DDS vocabulary (ReifiedConcept /
  CodeList / ItemGroup fragments). Authored 2026-08-29 against
  cdisc-org and TeMeta schemas; identical to the file shared in chat.
- `GlucoseBloodQuantitative.profiled.dds.json` — same content plus the
  profile's ddsq* extension slots (result scale, broader concept,
  interpretation regimes, per-property data types). Stripping every
  ddsq* key yields a base-valid instance (checked by ../validate_dds.py).
- `CONC.BiomedicalConcept_55.dds.json` — the 360i engine's OWN glucose
  concept, extracted verbatim from
  cdisc-org/data-definition-engine data/protocols/NCT01797120/NCT01797120-dds-latest.json
  at commit 97acb8a65090ebae2d598983aed490ab40b094ec (2026-08-26).
  It validates against base AND against the profile unchanged — the
  extensions are optional, so the profile sits on top of what the
  engine already produces.

Note: the recording uses `wasDerivedFrom` for the sibling link; base
DDS also offers `ItemGroup.implementsConcept` ("specialization of an
abstract concept topic"), which is arguably the semantically precise
slot — kept as-is pending discussion.
