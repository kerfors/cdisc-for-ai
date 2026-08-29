# DDS Profiling Specification

**An implementer guide for creating profiles of the CDISC Data Definition Specification (DDS)**

| | |
|---|---|
| Status | Draft |
| Version | 0.1.0 |
| Base model | Data Definition Specification (DDS), LinkML representation (`https://cdisc.org/dds`) |
| Repository | https://github.com/cdisc-org/DataExchange-DDS |

---

## 1. Introduction

### 1.1 Why profiles?

The DDS model is deliberately broad. It acts as a Rosetta Stone across CDISC ODM, USDM, Dataset-JSON, SDMX, FHIR, OMOP, and RDF, and it therefore contains far more classes, slots, and optionality than any single implementation needs. An implementer generating a Define-XML file does not need the SDMX cube classes (`Dimension`, `SeriesKey`, `Dataflow`); an implementer building a raw-to-SDTM transformation pipeline needs `Method`, `SourceItem`, and `Parameter` to be far more constrained than the base model requires; an aCRF generator cares about form rendering metadata that most other consumers can ignore.

A **DDS profile** solves this by carving a use-case-specific, machine-readable slice out of the base model. A profile tightens cardinality, narrows value sets, prunes irrelevant classes, fixes values where the use case demands them, and — where genuinely necessary — adds declared extensions. Implementers then build against the profile, which is smaller, stricter, and unambiguous, rather than against the full DDS model.

The design deliberately parallels HL7 FHIR profiling. Where FHIR profiles individual resources with `StructureDefinition`, DDS profiles the one broad model as a whole. Where a FHIR profile is expressed as a *differential* against a base definition and resolved into a *snapshot*, a DDS profile is expressed as a **differential LinkML schema** and resolved into a **snapshot LinkML schema**, from which JSON Schema and other artifacts are generated.

### 1.2 Scope

This guide specifies how to author, resolve, validate, publish, and claim conformance to a DDS profile. It covers the profile file format (LinkML), the permitted constraint operations, the extension mechanism, the snapshot resolution rules, and JSON Schema generation. It does not define any particular profile; example profiles for Define-XML generation, aCRF generation, and raw-to-SDTM transformation are used throughout for illustration, and Appendix A contains a worked Define-XML example.

### 1.3 Audience and conventions

This document is written for implementers who know LinkML basics (classes, slots, `attributes`, `slot_usage`, imports, enums) and are familiar with the DDS model. The keywords **must**, **must not**, **should**, and **may** are used in their conventional sense, but this is a pragmatic guide: where a rule exists, the reason for it is given, and examples are preferred over prose.

---

## 2. Core concepts

**Base model.** The published DDS LinkML schema for a given release, e.g. `dds` version 1.0. Every profile targets exactly one version of the base model.

**Profile.** A named, versioned, machine-readable set of constraints and declared extensions on the base model, serving one use case. A profile is authored as a LinkML schema.

**Differential.** The profile as authored: a LinkML schema that imports the base model and redefines *only* the classes, slots, and enums it constrains or extends, stating *only* the metaslots that change. This is the source of truth for a profile and the artifact that is reviewed and versioned.

**Snapshot.** The fully resolved LinkML schema produced by merging the differential onto the base model (Section 6). The snapshot is self-contained: every profiled class carries its complete, effective set of slots and constraints. Validation and code/schema generation run against the snapshot, never against the raw differential.

**Extension.** A slot, class, or enum added by a profile that does not exist in the base model. Extensions must be explicitly declared as such (Section 5).

**Conformance rule (subset-plus-extensions).** Any data instance that validates against a profile must, *after removal of the profile's declared extension elements*, also validate against the base DDS model. In other words: profiles only tighten the base model; the single sanctioned way to go beyond it is a declared extension. This keeps every profiled instance interoperable — a generic DDS consumer can always read profile-conformant data by ignoring extensions it does not understand.

### 2.1 Why differential + snapshot, rather than plain imports

LinkML resolves name collisions between an importing schema and an imported schema by letting the local definition *shadow* the imported one wholesale — it does not deep-merge a sparse local `Item` into the imported `Item`. If profiles were consumed directly as import-and-redefine schemas, every profiled class would have to restate all of its inherited attributes, which is verbose, error-prone, and drifts silently when the base model changes.

The differential/snapshot split resolves this, exactly as FHIR's `differential`/`snapshot` elements do. Authors write the sparse, readable differential; a deterministic merge step (Section 6) produces the complete snapshot; generators and validators consume the snapshot. The differential stays small and reviewable, and regenerating the snapshot against a new base release immediately surfaces any incompatibility.

---

## 3. Profile file structure

A profile differential is a single LinkML schema file. The skeleton:

```yaml
id: https://cdisc.org/dds/profiles/define-xml       # canonical profile URI
name: dds-profile-define-xml                        # lowercase, dds-profile- prefix
title: DDS Profile - Define-XML Generation
description: >-
  Constrains the DDS model to the elements and cardinalities required to
  generate a Define-XML v2.1 document from a DDS instance.
version: 1.0.0                                      # profile's own semver
license: MIT

prefixes:
  dds: https://cdisc.org/dds
  ddsp: https://cdisc.org/dds/profiles/define-xml/  # the profile's OWN namespace
  linkml: https://w3id.org/linkml/

default_prefix: ddsp
default_range: string

imports:
  - linkml:types
  - dds                                             # the base DDS model

annotations:
  dds.profile.baseModel: https://cdisc.org/dds
  dds.profile.baseVersion: "1.0.0"                  # pinned base release
  dds.profile.status: draft                         # draft | trial-use | stable | retired
  dds.profile.useCase: >-
    Generation of Define-XML v2.1 for regulatory submission.

classes:
  # differential class redefinitions go here (Section 4)

enums:
  # narrowed or extension enums go here

slots:
  # reusable extension slots, if any
```

Requirements on the header:

1. `id` **must** be a resolvable canonical URI under the profile registry namespace (`https://cdisc.org/dds/profiles/...` for CDISC-published profiles; implementers publishing their own profiles use their own namespace). This URI is what instances reference when claiming conformance (Section 9).
2. `name` **must** begin with `dds-profile-`.
3. The four `dds.profile.*` annotations shown above are **mandatory**. `dds.profile.baseVersion` pins the exact base release the profile was authored against; snapshot resolution fails if the available base model version does not match.
4. The profile **must** declare its own prefix (here `ddsp`) and use it as `default_prefix`. All extension elements get URIs in this namespace, which is what keeps them distinguishable from base-model elements in generated RDF, JSON-LD contexts, and documentation.

---

## 4. Constraint operations

Inside the differential, a profile redefines a base class by declaring a class of the *same name* and listing only what changes. The merge rules in Section 6 overlay these deltas onto the base definition. This section catalogs the permitted operations, all of which are "tightening" moves — each one shrinks or preserves the set of valid instances, never grows it.

### 4.1 Cardinality

| Operation | Base | Profile | Allowed? |
|---|---|---|---|
| Make optional slot required | `required: false` (or unset) | `required: true` | Yes |
| Make required slot optional | `required: true` | `required: false` | **No** — loosening |
| Restrict multivalued to single | `multivalued: true` | `multivalued: false` | Yes |
| Allow multiple where base allows one | `multivalued: false` | `multivalued: true` | **No** — loosening |
| Bound a list | `multivalued: true` | add `minimum_cardinality` / `maximum_cardinality` | Yes (min may only rise, max may only fall) |
| Prohibit a slot | any optional slot | `maximum_cardinality: 0` | Yes |

Prohibition (`maximum_cardinality: 0`) is the profile's pruning tool at slot level: it tells implementers "this element plays no role in this use case, and conformant instances must not populate it." Use it sparingly — an unmentioned optional slot is merely *ignored* by the profile, which is usually enough. Reserve prohibition for slots whose presence would actively confuse the use case (for example, a Define-XML profile prohibiting the SDMX `DataStructureDefinition` reference slots on `ItemGroup`).

```yaml
classes:
  Item:
    slot_usage:
      length:
        required: true          # Define-XML needs Length for most datatypes
      rangeChecks:
        maximum_cardinality: 0  # out of scope for this profile
```

> **Note — `attributes` vs `slot_usage` in a differential.** In the base DDS model most slots are declared inline as `attributes`. In a differential, express constraint deltas on existing slots using `slot_usage`, and reserve `attributes` for *extension* slots that are new in the profile. The merge step (Section 6) treats them accordingly. This convention makes a differential self-documenting: everything under `slot_usage` is a tightening of something that already exists; everything under `attributes` is new.

### 4.2 Range narrowing

A profile may replace a slot's range with a narrower one:

- A class range may be narrowed to a subclass defined in the base model.
- An enum range may be narrowed to a **subset enum**: a new enum, defined in the profile, whose permissible values are a strict subset of the base enum's values, preserving each value's `meaning` URI. Preserving `meaning` is what makes the subset relationship machine-checkable.
- A slot with an `any_of` union range may be narrowed to a subset of the alternatives (including collapsing to a single `range`).
- A string range may gain a `pattern`, or a tighter `pattern` than the base (the profile pattern must accept only strings the base pattern accepts, where the base has one).
- Numeric ranges may gain or tighten `minimum_value` / `maximum_value`.

```yaml
classes:
  Origin:
    slot_usage:
      type:
        required: true
        range: DefineOriginType     # subset enum, defined below
      source:
        required: true

enums:
  DefineOriginType:
    description: Origin types permitted in Define-XML v2.1 submissions.
    permissible_values:
      Assigned:
        meaning: NCIT:C170547       # meanings copied verbatim from base OriginType
      Collected:
        meaning: NCIT:C170548
      Derived:
        meaning: NCIT:C170549
      Protocol:
        meaning: NCIT:C170550
      Predecessor:
        meaning: NCIT:C170551
```

Narrowing an `any_of` union is particularly useful with DDS's flexible slots such as `Governed.purpose` (`string` or `TranslatedText`) and `Governed.owner` (`User`, `Organization`, or `string`) — a profile aimed at regulated submissions will typically pin these to a single alternative so that all producers serialize them the same way:

```yaml
classes:
  Item:
    slot_usage:
      purpose:
        range: TranslatedText       # collapses the any_of union
```

### 4.3 Fixed and default values

A profile may fix a slot to a constant using `equals_string`, `equals_number`, or (for multivalued slots) `equals_string_in`, and may supply defaults with `ifabsent`. Fixing values is how a profile encodes use-case invariants — for example, an SDTM-oriented profile fixing `ItemGroup.type` to the tabulation dataset kind, or a profile fixing `ODMFileMetadata.fileType` for its exchange scenario.

```yaml
classes:
  ItemGroup:
    slot_usage:
      isReferenceData:
        ifabsent: "boolean(false)"
```

### 4.4 Identifier and pattern conventions

Profiles frequently need to enforce identifier conventions that the base model deliberately leaves open. The base `Identifiable.OID` slot says "use CDISC OID format for regulatory submissions, or simple strings for internal use" — a submission-oriented profile closes that choice:

```yaml
classes:
  Item:
    slot_usage:
      OID:
        required: true
        pattern: "^IT\\..+"
  Governed:
    slot_usage:
      wasDerivedFrom:
        # Narrow the provenance union to the element kinds this use case
        # derives from (value-list slices derive from Items; groups and code
        # lists may derive from their standard counterparts). Narrowing here,
        # on the mixin, propagates to every class that mixes Governed in and
        # severs reachability into the SDMX/data-product subtrees.
        any_of:
          - range: Item
          - range: ItemGroup
          - range: CodeList

  RangeCheck:
    slot_usage:
      item:
        range: Item                   # collapse the Item/Dimension/Measure/
                                      # DataAttribute union: checks target Items

  Parameter:
    slot_usage:
      items:
        range: Item                   # method parameters bind to Items here

  ItemGroup:
    slot_usage:
      OID:
        required: true
        pattern: "^IG\\..+"
```

### 4.5 Serialization form

`inlined` / `inlined_as_list` on a slot may be changed by a profile **only** in the tightening direction for its purpose: converting a by-reference slot to inlined (or vice versa) changes the physical JSON shape, so a profile that does this must call it out prominently in its documentation, and the change is exempt from the "instances must validate against base" check only in physical form — the *logical* content must still be expressible in the base model. When in doubt, leave serialization metaslots alone; they are rarely what a use case actually needs to constrain.

### 4.6 Class pruning and the profile boundary

A profile does not need to prohibit every base class it ignores. The **profile boundary** is defined implicitly:

1. The profile designates a **root class** for its instance documents. If the base model's `tree_root` (currently `MetaDataVersion`) is the right root, nothing needs to be said; otherwise the differential sets `tree_root: true` on its chosen root class (the merge step clears the base flag).
2. Every class reachable from the root through non-prohibited slots in the snapshot is *in scope*.
3. Everything else is *out of scope* and is dropped from generated JSON Schema (Section 8). Out-of-scope classes need no mention in the differential.

This means a Define-XML profile that never references `Dataflow`, `SeriesKey`, or `DataProduct` simply excludes them by reachability — no prohibition boilerplate required.

### 4.7 Operations that are never allowed

For clarity, a profile **must not**:

- Remove or rename a base slot or class (prohibit with `maximum_cardinality: 0` instead).
- Loosen any constraint: required→optional, single→multivalued, widen a range, relax a pattern, raise a `maximum_cardinality`, remove an enum value's `meaning`.
- Change the semantics of a base element — `description` may be *appended to* (to add use-case guidance) but must not contradict the base meaning, and semantic mapping metaslots (`exact_mappings`, `close_mappings`, `narrow_mappings`, etc.) on base elements must not be altered.
- Redefine a base element as something structurally different (e.g., turning a class into an enum).

Automated compatibility checking (Section 7) enforces the mechanically checkable subset of these rules.

---

## 5. Extensions

Constraints cover most use cases, but some profiles genuinely need data the base model does not carry — an aCRF profile, for example, may need per-item rendering hints that have no home in DDS. Extensions are the sanctioned mechanism for this, and they come with three rules that keep the subset-plus-extensions conformance model intact:

**Rule 1 — declare it.** Every extension element (slot, class, or enum) must carry the annotation `dds.profile.extension: true`. This is what tooling uses to identify, document, and strip extensions.

**Rule 2 — namespace it.** Every extension element must have its URI (`slot_uri` / `class_uri` / `enum_uri`) in the profile's own namespace, never in the `dds:` namespace. Extension slot *names* should additionally carry a short profile-specific prefix in the name itself (e.g., `acrfRenderingHint` rather than `renderingHint`) to minimize the chance of colliding with a slot added to DDS in a future release.

**Rule 3 — keep the base reachable.** An instance with all extension slots removed must validate against the base model. Consequences: extension slots must be optional or have profile-supplied semantics that a stripping tool can remove wholesale; extension classes may appear only as the range of extension slots (or as subclasses used behind extension slots); an extension must never be the only way to satisfy a base-model constraint.

```yaml
classes:
  Item:
    slot_usage:
      # ... constraints as usual ...
    attributes:                          # attributes block = extensions
      acrfRenderingHint:
        description: >-
          Hint to the aCRF renderer for how to display this item's
          annotation (e.g., placement, grouping, abbreviation).
        slot_uri: ddsp:acrfRenderingHint
        range: AcrfRenderingHint
        annotations:
          dds.profile.extension: true

  AcrfRenderingHint:
    class_uri: ddsp:AcrfRenderingHint
    annotations:
      dds.profile.extension: true
    attributes:
      placement:
        range: string
      abbreviatedLabel:
        range: string
```

Extensions are exempt from the base-conformance check but not from review: a recurring extension across several profiles is a signal that the base DDS model should grow to absorb it. Profile maintainers should raise such cases against the DataExchange-DDS repository rather than letting parallel extensions diverge.

Note the relationship to the base model's `IsProfile.profile` slot: that slot is for *instances* to claim conformance to profiles (Section 9). It is not itself an extension mechanism, and profiles must not repurpose it.

---

## 6. Snapshot resolution

The snapshot is produced by a deterministic merge of the differential onto the pinned base model. Tooling implements the following rules; profile authors need to know them mainly to predict what their differential means.

**R1 — version gate.** Resolution fails unless the base model's `version` equals `dds.profile.baseVersion` in the differential.

**R2 — element matching.** A class, slot, or enum in the differential whose name equals a base element's name is a *redefinition* of that element. All other elements in the differential are *additions* and must satisfy the extension rules of Section 5 (subset enums under Section 4.2, which replace nothing and are referenced only via narrowed ranges, are also additions but are not extensions and do not need the extension annotation — they constrain, rather than exceed, the base model).

**R3 — class merge.** For a redefined class: start from the fully induced base class (with all inherited and mixin slots materialized); apply each entry in the differential's `slot_usage` as a per-metaslot overlay on the matching slot; append `attributes` entries as new slots; class-level metaslots stated in the differential (e.g., `tree_root`, `description`) replace the base values, except `description`, which is appended with a separator.

**R4 — slot merge.** Within a `slot_usage` overlay, only the metaslots explicitly stated in the differential change; every unstated metaslot keeps its base value. Stated values replace base values (no deep merge within a metaslot).

**R5 — tightening check.** After merging, every changed metaslot is checked against the tightening rules of Section 4. Any loosening is a resolution error, not a warning.

**R6 — root and reachability.** If the differential set `tree_root: true` on a class, the flag is cleared elsewhere. The reachability closure from the root through non-prohibited slots is computed; classes and enums outside the closure are dropped from the snapshot.

**R7 — provenance stamping.** The snapshot records, as schema-level annotations, the profile id and version, the base id and version, and the resolution tool version, so any generated artifact is traceable to exact inputs.

The snapshot is a generated artifact. It is committed alongside the differential for reviewability (a snapshot diff makes the effect of a differential change obvious), but hand edits to a snapshot are never permitted.

A reference implementation of this resolution algorithm, `dds_profile_snapshot.py`, accompanies this specification. It implements R1–R7 (including the tightening checks of R5, with warnings where a rule is not mechanically checkable, such as regex-subset relations), produces deterministic byte-identical output for identical inputs, and is exercised in CI as: `python dds_profile_snapshot.py --base define.yaml --differential profiles/<name>/profile.yaml --output profiles/<name>/snapshot.yaml`.

---

## 7. Validation and compatibility checking

A profile is subject to three layers of checking, all automatable in CI:

**Schema validity.** The differential and the resolved snapshot must each be valid LinkML (e.g., `linkml lint` / schema loading must succeed).

**Profile compatibility.** A profile-aware checker compares snapshot against base and asserts, class by class and slot by slot, that only tightening operations occurred (Section 4.7), that every added element is either a declared extension or a subset enum, that subset enums preserve `meaning` URIs, and that extension URIs live outside the `dds:` namespace. This is the machine-readable enforcement of the subset-plus-extensions rule.

**Instance validation.** A data instance conforms to a profile if it validates against the snapshot (via `linkml-validate` or the generated JSON Schema). The conformance rule additionally requires that the instance, stripped of extension slots, validates against the base model; because the compatibility check already guarantees this holds for any snapshot-valid instance, base revalidation is a belt-and-braces check rather than a routine step.

---

## 8. Generating JSON Schema (and other artifacts)

JSON Schema is generated from the **snapshot**, rooted at the profile's root class:

```bash
gen-json-schema --closed --top-class MetaDataVersion \
    profiles/define-xml/snapshot.yaml \
    > profiles/define-xml/define-xml.schema.json
```

`--closed` is the recommended default for profiles: it sets `additionalProperties: false`, so instance documents containing slots outside the profile (including base-model slots the profile ignores) are rejected. This is usually what a profile implementer wants — the whole point of the profile is a closed contract. A profile that must tolerate unprofiled base-model content (for example, a validation profile applied over full DDS documents) may generate open schemas instead; it should say so in its documentation, and its `dds.profile.useCase` annotation should make the reading-vs-authoring intent clear.

Because the snapshot is an ordinary LinkML schema, every other LinkML generator works on it unchanged: `gen-pydantic` for Python datamodels, `gen-typescript`, `gen-owl`, `gen-doc` for the profile's rendered documentation, and `gen-jsonld-context` (where extension slots resolve to the profile namespace, exactly as Rule 2 of Section 5 intends).

---

## 9. Instance conformance claims

Instances should say what they conform to. The base model already provides the hook: classes carrying the `IsProfile` mixin (notably `ItemGroup`, and the dataset/data-product classes) have a multivalued `profile` slot, described as "profiles this resource claims to conform to." A conformant producer populates it with the profile's canonical URI, optionally version-qualified:

```yaml
itemGroups:
  - OID: IG.ADSL
    profile:
      - https://cdisc.org/dds/profiles/define-xml/1.0
```

For whole-document claims where the root class does not mix in `IsProfile`, the claim is carried out of band (e.g., in the exchange envelope or API content negotiation) — profiles should document which mechanism they expect. Consumers must treat conformance claims as claims, not proof; validation (Section 7) is what establishes conformance.

---

## 10. Publication, naming, and versioning

**Repository layout.** Profiles live in the DataExchange-DDS repository (or an implementer's own repository for private profiles) under a `profiles/` directory:

```
profiles/
  define-xml/
    profile.yaml        # the differential (source of truth)
    snapshot.yaml       # generated; regenerated in CI, never hand-edited
    define-xml.schema.json
    README.md           # use case, scope, examples, serialization notes
  acrf/
    ...
  raw-to-sdtm/
    ...
```

**Naming.** Directory and schema `name` use a short kebab-case use-case token; the schema `name` is `dds-profile-<token>`. The canonical `id` is `https://cdisc.org/dds/profiles/<token>` with a major-version segment appearing in conformance-claim URIs (`.../define-xml/1.0`).

**Versioning.** Profiles use semantic versioning, independent of the base model's version. Adding a constraint is a *major* change from a data producer's perspective (previously valid data may become invalid), so treat any tightening as major unless the profile is still `draft`. Loosening never happens by definition — relaxing a constraint means the constraint moves out of the profile, which is likewise major for consumers relying on it. Rebasing a profile onto a new base model release is at minimum a minor version bump and requires rerunning the compatibility check and regenerating all artifacts.

**Lifecycle.** `dds.profile.status` moves `draft → trial-use → stable → retired`. Breaking changes to a `stable` profile require a new major version published alongside the old one; retired profiles remain resolvable at their canonical URIs.

---

## 11. Authoring checklist

Before publishing a profile, confirm:

1. Header carries canonical `id`, `dds-profile-` name, semver `version`, and all four `dds.profile.*` annotations, with `baseVersion` pinned.
2. Every redefinition only tightens (Section 4); the compatibility check passes.
3. Every addition is either a subset enum (meanings preserved) or a declared, namespaced extension (Section 5).
4. The root class is correct and the reachability closure contains everything the use case needs — generate the JSON Schema and eyeball it.
5. Snapshot and JSON Schema are regenerated from the committed differential in CI, and at least one valid and one deliberately invalid example instance are committed and exercised as tests.
6. README states the use case, the intended direction (authoring contract vs. validation overlay), open/closed schema choice, and any serialization-form changes (Section 4.5).

---

## Appendix A — Worked example: a Define-XML generation profile (excerpt)

This appendix is grounded in a reference instance: a DDS document for the CDISC pilot LZZT study (SDTMIG 3.4, CDISC/NCI CT 2024-09-27) that was used to generate a Define-XML v2.1 document. The instance contains 21 tabulation `itemGroups` with 311 items, 60 code lists, 164 conditions, and 202 where-clauses; it is authored as a *template*, with `__PLACEHOLDER__` markers standing in for metadata to be supplied by a later substitution step (see the workflow notes at the end of this appendix). Two of its structural choices shape the profile below:

- **Value-level metadata is expressed through `ItemGroup.slices`.** Each dataset-level `ItemGroup` (OID prefix `IG.`) may carry slice `ItemGroup`s of `type: ValueList` (OID prefix `VL.`, linked back to the parent variable via `wasDerivedFrom`), whose items carry `applicableWhen` references to `whereClauses`. Because slices are themselves `ItemGroup`s, any constraint the profile places on `ItemGroup` must hold for both dataset definitions and value lists — which is why the OID pattern below admits both prefixes, and why `domain`, `standard`, and `structure` stay optional (value-list slices legitimately omit them).
- **Item-level provenance carries the Define-XML `def:Origin` content.** `Origin.type` and `Origin.source` do the work, so the profile makes both required and binds `type` to the Define-XML v2.1 subset.

```yaml
id: https://cdisc.org/dds/profiles/define-xml
name: dds-profile-define-xml
title: DDS Profile - Define-XML Generation
description: >-
  Constrains DDS to the content required to generate Define-XML v2.1.
version: 1.0.0
license: MIT

prefixes:
  dds: https://cdisc.org/dds
  ddsp: https://cdisc.org/dds/profiles/define-xml/
  linkml: https://w3id.org/linkml/
  NCIT: http://purl.obolibrary.org/obo/NCIT_
default_prefix: ddsp
default_range: string

imports:
  - linkml:types
  - dds

annotations:
  dds.profile.baseModel: https://cdisc.org/dds
  dds.profile.baseVersion: "1.0.0"
  dds.profile.status: draft
  dds.profile.useCase: Generation of Define-XML v2.1 documents.

classes:

  MetaDataVersion:            # base tree_root retained as profile root
    slot_usage:
      OID:
        required: true
      name:
        required: true
      defineVersion:
        required: true
        pattern: "^2\\.1(\\.\\d+)?$"
      fileOID:
        required: true
      studyOID:
        required: true
      studyName:
        required: true
      standards:
        required: true
        minimum_cardinality: 1        # the IG and CT standards referenced by content
      itemGroups:
        required: true
        minimum_cardinality: 1
      # Document-level subtrees out of scope for Define-XML generation.
      # Prohibiting them here is what lets R6 reachability drop the SDMX
      # cube, data-product, and display classes from the snapshot (spec 4.6).
      analyses:
        maximum_cardinality: 0
      dataProducts:
        maximum_cardinality: 0
      displays:
        maximum_cardinality: 0
      dictionaries:
        maximum_cardinality: 0
      resources:
        maximum_cardinality: 0

  ItemGroup:
    slot_usage:
      OID:
        required: true
        pattern: "^(IG|VL)\\..+"      # dataset-level definitions and value-list slices
      name:
        required: true
      purpose:
        range: string                 # collapse the any_of; the use case emits plain text
      structure:
        range: string
      # purpose, domain, standard, observationClass, keySequence, slices: required
      # for dataset-level groups but legitimately absent on value-list slices, so
      # the profile leaves them optional and defers dataset-vs-slice rules to its
      # documentation (LinkML rules could express them; see the Item length rule).

  Item:
    slot_usage:
      OID:
        required: true
        pattern: "^IT\\..+"
      name:
        required: true
      mandatory:
        required: true                # feeds ItemRef/@Mandatory
      # role feeds ItemRef/@Role on dataset variables but is legitimately absent
      # on value-level items, so it stays optional here.
      dataType:
        range: DefineDataType         # subset enum
      rangeChecks:
        maximum_cardinality: 0        # edit checks live on Condition in this use case
    rules:
      - description: >-
          Define-XML v2.1 requires Length for text, integer, and float items.
          (Rule support varies by generator/validator; treat as a documented
          check where the toolchain cannot enforce it.)
        preconditions:
          slot_conditions:
            dataType:
              any_of:
                - equals_string: text
                - equals_string: integer
                - equals_string: float
        postconditions:
          slot_conditions:
            length:
              required: true

  Origin:
    slot_usage:
      type:
        required: true
        range: DefineOriginType       # subset enum
      source:
        required: true

  WhereClause:
    slot_usage:
      conditions:
        required: true
        minimum_cardinality: 1

enums:

  DefineDataType:
    description: >-
      ODM data types permitted in Define-XML v2.1 that exist in the base
      DataType enum. (Define-XML also permits partialDate, partialTime, and
      partialDatetime, which the base enum currently lacks; a profile cannot
      add enum values — that gap must be raised against the base model.)
    permissible_values:
      text: {}
      integer: {}
      float: {}
      date: {}
      time: {}
      datetime: {}
      durationDatetime: {}

  DefineOriginType:
    description: Origin types permitted in Define-XML v2.1.
    permissible_values:
      Assigned:    { meaning: NCIT:C170547 }
      Collected:   { meaning: NCIT:C170548 }
      Derived:     { meaning: NCIT:C170549 }
      Predecessor: { meaning: NCIT:C170550 }
      Protocol:    { meaning: NCIT:C170551 }
```

What the resolution step does with this: `Item` in the snapshot keeps every base attribute and mixin slot (`description`, `codeList` — used as a string OID reference, since the slot is not inlined — `method`, `applicableWhen`, the `Formatted` slots `displayFormat` and `significantDigits` that the reference instance uses on value-level items, and so on) with only the slots named above altered; `ItemGroup.slices` recursion means value lists are profiled by the same `ItemGroup` constraints as datasets; the SDMX cube, data-product, and display classes disappear from the snapshot once the document-level slots that reach them are prohibited (reachability alone would keep them, since `MetaDataVersion` references them directly); and `gen-json-schema --closed --top-class MetaDataVersion` yields the closed contract a Define-XML generator implements against.

Two workflow notes from the reference instance are worth generalizing:

**Templates and placeholder substitution.** The reference instance is deliberately a *template*: where metadata was not yet available, the generator emitted the literal marker `__PLACEHOLDER__` (in `Origin.type`, `Origin.source`, and `keySequence`), to be swapped for real values by a downstream substitution step. Profile validation applies to the *resolved* document, after substitution — a template will (and should) fail enum bindings and reference-range checks on its markers, and that failure is meaningless before substitution runs. Pipelines using this pattern should therefore run profile validation as a post-substitution gate, and may additionally run a template-stage check that ignores marker-valued slots. A profile itself must not be relaxed to admit markers: adding `__PLACEHOLDER__` to a subset enum or loosening a reference range would violate Section 4.7, and would let unresolved templates masquerade as finished documents.

**Serialization shape is part of the contract.** `Item.origin` is declared `multivalued: true, inlined_as_list: true`, so conformant JSON is `"origin": [ { ... } ]` even when there is exactly one origin. A producer emitting a bare object is a bug to fix in the producer, not a shape for the profile to canonize by tightening to `multivalued: false` — the list form keeps every profiled instance directly valid against the base model, per the subset rule. The same reasoning covers `null` versus absence (`length: null` is a type violation; omit the key instead) and unknown document-level keys (`annotatedCRF` for the base slot `annotatedCRFs`, or `conceptProperties`, which is not a base slot), both rejected by the closed schema. A profile does not paper over such divergences by loosening — under Section 4.7 it cannot — which is precisely what makes profile validation a useful quality gate for generator output.

For contrast, the aCRF profile would follow the identical pattern but constrain rendering-relevant slots (`Formatted`, `crfCompletionInstructions`), require `Collected`-centric origins, and add the `acrfRenderingHint` extension from Section 5; the raw-to-SDTM transformation profile would center on `Method`, `FormalExpression`, `SourceItem`, `Parameter`, and `ReturnValue`, requiring `Item.method` for derived variables and fixing `FormalExpression` context values to the transformation engine's identifier.
