#!/usr/bin/env python3
"""Validation matrix for the qualified-BC DDS profile.

Instances are fragments (a concept, code lists, one recording), so each
part is validated against its class definition in the generated JSON
Schemas ($defs), not against a whole MetaDataVersion document — how a
reusable concept library is contained/transported is an open base-model
question the profile deliberately does not solve.

Run from this directory. Requires: pip install jsonschema
Regenerate inputs first if schemas changed:
  python3 dds_base/dds_profile_snapshot.py --base dds_base/dds.yaml \
      --differential dds-profile-qualified-bc/profile.yaml \
      --output dds-profile-qualified-bc/snapshot.yaml --allow-unversioned-base
  gen-json-schema --closed --top-class MetaDataVersion \
      dds-profile-qualified-bc/snapshot.yaml > dds-profile-qualified-bc/qualified-bc.schema.json
  gen-json-schema --closed --top-class MetaDataVersion \
      dds_base/dds.yaml > dds_base/dds.schema.json
"""
import copy
import json
import sys

from jsonschema import Draft7Validator

BASE = json.load(open('dds_base/dds.schema.json'))
PROF = json.load(open('dds-profile-qualified-bc/qualified-bc.schema.json'))


def check(label, schema, class_name, obj, expect_valid=True):
    v = Draft7Validator(
        {'$ref': f'#/$defs/{class_name}', '$defs': schema['$defs']})
    errors = sorted(v.iter_errors(obj), key=lambda e: list(e.absolute_path))
    ok = (not errors) if expect_valid else bool(errors)
    print(f"{'PASS' if ok else 'FAIL'}  {label}")
    if not ok or not expect_valid:
        for e in errors[:6]:
            path = '/'.join(str(x) for x in e.absolute_path) or '<root>'
            print(f"        {path}: {e.message[:110]}")
    return ok


def strip_extensions(obj):
    """Remove every ddsq* slot, recursively (spec §5 conformance rule)."""
    if isinstance(obj, dict):
        return {k: strip_extensions(v) for k, v in obj.items()
                if not k.startswith('ddsq')}
    if isinstance(obj, list):
        return [strip_extensions(v) for v in obj]
    return obj


results = []

own = json.load(open('instances/GlucoseBloodQuantitative.dds.json'))
prof = json.load(open('instances/GlucoseBloodQuantitative.profiled.dds.json'))
engine = json.load(open('instances/CONC.BiomedicalConcept_55.dds.json'))

# 1. own concept, base variant, against base model
results.append(check('own concept (base variant)      vs BASE    ReifiedConcept',
                     BASE, 'ReifiedConcept', own['concept']))
# 2. code lists and recording against base model
for cl in own['codeLists']:
    results.append(check(f"own codeList {cl['OID'][:40]:<40} vs BASE    CodeList",
                         BASE, 'CodeList', cl))
results.append(check('own recording GLUCPL             vs BASE    ItemGroup',
                     BASE, 'ItemGroup', own['recording_GLUCPL']))
# 3. profiled concept against the profile snapshot
results.append(check('own concept (profiled variant)   vs PROFILE ReifiedConcept',
                     PROF, 'ReifiedConcept', prof['concept']))
# 4. spec §5 conformance rule: profiled minus extensions must pass base
results.append(check('profiled variant stripped of ddsq* vs BASE  ReifiedConcept',
                     BASE, 'ReifiedConcept', strip_extensions(prof['concept'])))
# 5. the engine's own output (360i, NCT01797120) against base and profile
results.append(check('engine CONC.BiomedicalConcept_55 vs BASE    ReifiedConcept',
                     BASE, 'ReifiedConcept', engine))
results.append(check('engine CONC.BiomedicalConcept_55 vs PROFILE ReifiedConcept',
                     PROF, 'ReifiedConcept', engine))
# 6. negative controls: the profile must actually tighten
no_oid = copy.deepcopy(prof['concept']); no_oid.pop('OID')
results.append(check('negative: concept without OID    vs PROFILE (must fail)',
                     PROF, 'ReifiedConcept', no_oid, expect_valid=False))
no_coding = copy.deepcopy(prof['concept']); no_coding.pop('coding')
results.append(check('negative: concept without coding vs PROFILE (must fail)',
                     PROF, 'ReifiedConcept', no_coding, expect_valid=False))
bad_scale = copy.deepcopy(prof['concept']); bad_scale['ddsqResultScale'] = 'Coded'
results.append(check('negative: ddsqResultScale=Coded  vs PROFILE (must fail)',
                     PROF, 'ReifiedConcept', bad_scale, expect_valid=False))

print()
if all(results):
    print(f'ALL {len(results)} CHECKS PASS')
else:
    print(f'{results.count(False)} of {len(results)} checks FAILED')
    sys.exit(1)
