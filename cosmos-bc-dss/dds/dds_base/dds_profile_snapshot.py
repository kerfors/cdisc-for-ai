#!/usr/bin/env python3
"""dds_profile_snapshot.py — DDS profile snapshot resolver.

Implements Section 6 ("Snapshot resolution") of the DDS Profiling
Specification: merges a profile *differential* (a sparse LinkML schema that
imports the DDS base model and redefines only what it constrains or extends)
onto the pinned *base model*, producing a self-contained *snapshot* LinkML
schema suitable for gen-json-schema, gen-pydantic, gen-doc, etc.

Resolution rules implemented (numbering per the specification):

  R1  Version gate         base.version must equal dds.profile.baseVersion
  R2  Element matching     same-name elements are redefinitions; everything
                           else is an addition (extension or subset enum)
  R3  Class merge          slot_usage overlays merged per slot; attributes
                           appended as extensions; class metaslots replace,
                           description appends
  R4  Slot merge           per-metaslot replacement; unstated metaslots keep
                           their base (induced) values
  R5  Tightening check     any loosening is a resolution ERROR
  R6  Root & reachability  tree_root reassignment; unreachable classes and
                           enums dropped from the snapshot
  R7  Provenance stamping  snapshot annotated with profile/base ids, versions,
                           and tool version

The snapshot is deterministic: same inputs -> byte-identical output. Hand
edits to a snapshot are never permitted; regenerate instead.

Dependencies: pyyaml, linkml-runtime (SchemaView is used to induce effective
base slot values for the R4/R5 merge-and-check step).

Usage:
  python dds_profile_snapshot.py --base define.yaml \
      --differential profiles/define-xml/profile.yaml \
      --output profiles/define-xml/snapshot.yaml
"""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass, field

import yaml
from linkml_runtime import SchemaView

TOOL_NAME = "dds-profile-snapshot"
TOOL_VERSION = "0.1.0"

EXTENSION_ANNOTATION = "dds.profile.extension"
REQUIRED_PROFILE_ANNOTATIONS = (
    "dds.profile.baseModel",
    "dds.profile.baseVersion",
    "dds.profile.status",
    "dds.profile.useCase",
)

# Class-level keys a differential may state on a *redefined* class (R3).
REDEF_CLASS_KEYS = {
    "slot_usage", "attributes", "description", "tree_root", "rules",
    "annotations", "comments", "notes", "see_also", "todos",
}

# Slot metaslots whose overlay values the tightening checker knows how to
# verify mechanically (R5). Anything else stated in an overlay is applied
# but reported as a warning ("uncheckable").
CHECKED_METASLOTS = {
    "required", "multivalued", "minimum_cardinality", "maximum_cardinality",
    "range", "any_of", "pattern", "minimum_value", "maximum_value",
    "equals_string", "equals_number", "equals_string_in", "ifabsent",
    "description", "annotations", "inlined", "inlined_as_list",
}

LINKML_TYPES = {
    "string", "integer", "boolean", "float", "double", "decimal", "time",
    "date", "datetime", "date_or_datetime", "uriorcurie", "curie", "uri",
    "ncname", "objectidentifier", "nodeidentifier", "jsonpointer",
    "jsonpath", "sparqlpath",
}


class ResolutionError(Exception):
    """Fatal violation of the resolution rules."""


@dataclass
class Report:
    """Collects the resolution report printed at the end of a run."""
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    info: list[str] = field(default_factory=list)

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def note(self, msg: str) -> None:
        self.info.append(msg)

    def emit(self, stream=sys.stderr) -> None:
        for m in self.info:
            print(f"  [info] {m}", file=stream)
        for m in self.warnings:
            print(f"  [warn] {m}", file=stream)
        for m in self.errors:
            print(f"  [ERROR] {m}", file=stream)


# --------------------------------------------------------------------------
# Loading and small helpers
# --------------------------------------------------------------------------

def load_yaml(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    if not isinstance(doc, dict):
        raise ResolutionError(f"{path}: not a YAML mapping / LinkML schema")
    return doc


def get_annotation(node: dict, key: str):
    """Read an annotation value from a raw YAML element definition.

    Accepts both shorthand (``annotations: {k: v}``) and expanded
    (``annotations: {k: {tag: k, value: v}}``) LinkML annotation forms.
    """
    ann = (node or {}).get("annotations") or {}
    if key not in ann:
        return None
    val = ann[key]
    if isinstance(val, dict) and "value" in val:
        return val["value"]
    return val


def is_extension(node: dict) -> bool:
    val = get_annotation(node, EXTENSION_ANNOTATION)
    return str(val).lower() == "true" or val is True


def slot_ranges(slot_def: dict) -> list[str]:
    """All ranges a raw slot definition can take (range + any_of ranges)."""
    ranges: list[str] = []
    if slot_def.get("range"):
        ranges.append(slot_def["range"])
    for alt in slot_def.get("any_of") or []:
        if isinstance(alt, dict) and alt.get("range"):
            ranges.append(alt["range"])
    return ranges


# --------------------------------------------------------------------------
# R5 — tightening checks
# --------------------------------------------------------------------------

class TighteningChecker:
    """Verifies that every overlay metaslot only tightens the base value."""

    def __init__(self, sv: SchemaView, base: dict, diff: dict, report: Report):
        self.sv = sv
        self.base = base
        self.diff = diff
        self.report = report

    # -- range narrowing helpers ------------------------------------------

    def _is_subclass(self, child: str, parent: str) -> bool:
        try:
            return parent in self.sv.class_ancestors(child)
        except Exception:
            return False

    def _is_subset_enum(self, new_enum: str, base_enum: str) -> bool:
        """new_enum (defined in the differential) ⊆ base_enum, meanings kept."""
        new_def = (self.diff.get("enums") or {}).get(new_enum)
        base_def = (self.base.get("enums") or {}).get(base_enum)
        if not new_def or not base_def:
            return False
        base_pv = base_def.get("permissible_values") or {}
        for value, vdef in (new_def.get("permissible_values") or {}).items():
            if value not in base_pv:
                return False
            base_meaning = (base_pv[value] or {}).get("meaning")
            new_meaning = (vdef or {}).get("meaning")
            if base_meaning and new_meaning != base_meaning:
                return False
        return True

    def _narrows(self, new_range: str, old_range: str) -> bool:
        if new_range == old_range:
            return True
        if self._is_subclass(new_range, old_range):
            return True
        if old_range in (self.base.get("enums") or {}):
            return self._is_subset_enum(new_range, old_range)
        return False

    # -- the per-metaslot rules -------------------------------------------

    def check(self, where: str, meta: str, new, base_slot) -> None:
        """Check one overlay metaslot against the induced base slot.

        ``base_slot`` is a linkml_runtime SlotDefinition (induced), so its
        attribute values reflect inheritance and base slot_usage.
        """
        err = self.report.error
        warn = self.report.warn

        if meta == "required":
            if bool(getattr(base_slot, "required", False)) and new is False:
                err(f"{where}: required may not be loosened true->false")
        elif meta == "multivalued":
            if not bool(getattr(base_slot, "multivalued", False)) and new is True:
                err(f"{where}: multivalued may not be loosened false->true")
        elif meta == "minimum_cardinality":
            old = getattr(base_slot, "minimum_cardinality", None)
            if old is not None and new is not None and new < old:
                err(f"{where}: minimum_cardinality may only rise ({old}->{new})")
        elif meta == "maximum_cardinality":
            old = getattr(base_slot, "maximum_cardinality", None)
            if old is not None and new is not None and new > old:
                err(f"{where}: maximum_cardinality may only fall ({old}->{new})")
            if new == 0 and bool(getattr(base_slot, "required", False)):
                err(f"{where}: cannot prohibit a slot the base requires")
        elif meta == "range":
            old = getattr(base_slot, "range", None)
            base_any_of = list(getattr(base_slot, "any_of", []) or [])
            if base_any_of:
                alts = [getattr(a, "range", None) for a in base_any_of]
                if not any(a and self._narrows(new, a) for a in alts):
                    err(f"{where}: range '{new}' is not among (or a narrowing "
                        f"of) the base any_of alternatives {alts}")
            elif old and not self._narrows(new, old):
                err(f"{where}: range '{new}' does not narrow base range '{old}'")
        elif meta == "any_of":
            base_any_of = list(getattr(base_slot, "any_of", []) or [])
            alts = {getattr(a, "range", None) for a in base_any_of}
            for alt in new or []:
                r = (alt or {}).get("range")
                if alts:
                    if not any(a and self._narrows(r, a) for a in alts):
                        err(f"{where}: any_of alternative '{r}' is not a "
                            f"narrowing of any base alternative {sorted(a for a in alts if a)}")
                else:
                    old = getattr(base_slot, "range", None)
                    if old and not self._narrows(r, old):
                        err(f"{where}: any_of alternative '{r}' does not "
                            f"narrow base range '{old}'")
        elif meta == "pattern":
            old = getattr(base_slot, "pattern", None)
            if old and old != new:
                warn(f"{where}: pattern changed from base ('{old}' -> '{new}'); "
                     "regex subset relations are not machine-checkable — "
                     "verify manually that the profile pattern only accepts "
                     "strings the base pattern accepts")
        elif meta == "minimum_value":
            old = getattr(base_slot, "minimum_value", None)
            if old is not None and new is not None and new < old:
                err(f"{where}: minimum_value may only rise ({old}->{new})")
        elif meta == "maximum_value":
            old = getattr(base_slot, "maximum_value", None)
            if old is not None and new is not None and new > old:
                err(f"{where}: maximum_value may only fall ({old}->{new})")
        elif meta in ("inlined", "inlined_as_list"):
            warn(f"{where}: serialization metaslot '{meta}' changed — this "
                 "alters the physical JSON shape (spec §4.5); ensure the "
                 "profile documentation calls it out")
        elif meta in ("equals_string", "equals_number", "equals_string_in",
                      "ifabsent", "description", "annotations"):
            pass  # always-permitted additions / documentation
        else:
            warn(f"{where}: metaslot '{meta}' applied but not mechanically "
                 "checkable; verify tightening manually")

# --------------------------------------------------------------------------
# The resolver
# --------------------------------------------------------------------------

class SnapshotResolver:
    def __init__(self, base_path: str, diff_path: str,
                 allow_unversioned_base: bool = False,
                 prune: bool = True):
        self.base_path = base_path
        self.diff_path = diff_path
        self.allow_unversioned_base = allow_unversioned_base
        self.prune = prune
        self.report = Report()
        self.base = load_yaml(base_path)
        self.diff = load_yaml(diff_path)
        self.sv = SchemaView(base_path)  # induced views over the base model
        self.checker = TighteningChecker(self.sv, self.base, self.diff, self.report)
        # Filled during resolution:
        self.snapshot: dict = {}
        self.extension_classes: dict = {}
        self.subset_enums: dict = {}
        self.extension_enums: dict = {}
        self.range_overrides: dict[tuple[str, str], dict] = {}

    # -- R1 ----------------------------------------------------------------

    def check_version_gate(self) -> None:
        for key in REQUIRED_PROFILE_ANNOTATIONS:
            if get_annotation(self.diff, key) is None:
                self.report.error(f"differential: mandatory annotation '{key}' missing")
        pinned = get_annotation(self.diff, "dds.profile.baseVersion")
        base_version = self.base.get("version")
        if base_version is None:
            msg = (f"base model '{self.base.get('id')}' declares no 'version'; "
                   f"differential pins baseVersion={pinned!r}")
            if self.allow_unversioned_base:
                self.report.warn(msg + " — proceeding (--allow-unversioned-base)")
            else:
                self.report.error(msg + " — pass --allow-unversioned-base to override")
        elif pinned is not None and str(base_version) != str(pinned):
            self.report.error(
                f"R1 version gate: base version '{base_version}' != pinned "
                f"dds.profile.baseVersion '{pinned}'")
        base_id = get_annotation(self.diff, "dds.profile.baseModel")
        if base_id and base_id != self.base.get("id"):
            self.report.error(
                f"R1: differential targets base '{base_id}' but the supplied "
                f"base model has id '{self.base.get('id')}'")

    # -- R2 ----------------------------------------------------------------

    def classify_elements(self) -> None:
        base_classes = self.base.get("classes") or {}
        base_enums = self.base.get("enums") or {}

        for name, cdef in (self.diff.get("classes") or {}).items():
            cdef = cdef or {}
            if name in base_classes:
                continue  # redefinition, handled in merge_classes
            if not is_extension(cdef):
                self.report.error(
                    f"class '{name}': additions must be declared extensions "
                    f"(annotate with {EXTENSION_ANNOTATION}: true)")
            self.extension_classes[name] = cdef

        for name, edef in (self.diff.get("enums") or {}).items():
            edef = edef or {}
            if name in base_enums:
                self.report.error(
                    f"enum '{name}': base enums may not be redefined; define "
                    "a subset enum under a new name and narrow the slot range")
                continue
            if is_extension(edef):
                self.extension_enums[name] = edef
            else:
                # Must be a subset of at least one base enum (meanings kept)
                parents = [b for b in base_enums
                           if self.checker._is_subset_enum(name, b)]
                if not parents:
                    self.report.error(
                        f"enum '{name}': not a subset (with preserved "
                        "meanings) of any base enum, and not declared an "
                        "extension")
                else:
                    self.report.note(
                        f"subset enum '{name}' narrows base enum(s): "
                        f"{', '.join(parents)}")
                self.subset_enums[name] = edef

        for name, sdef in (self.diff.get("slots") or {}).items():
            if not is_extension(sdef or {}):
                self.report.error(
                    f"top-level slot '{name}': additions must be declared "
                    f"extensions ({EXTENSION_ANNOTATION}: true)")

    # -- R3 / R4 / R5 ------------------------------------------------------

    def merge_classes(self) -> dict:
        merged = copy.deepcopy(self.base.get("classes") or {})
        diff_classes = self.diff.get("classes") or {}
        diff_root_set = any((c or {}).get("tree_root") for c in diff_classes.values())

        for name, cdef in diff_classes.items():
            cdef = cdef or {}
            if name not in merged:
                continue  # addition; appended later
            target = merged[name] = merged[name] or {}

            unknown = set(cdef) - REDEF_CLASS_KEYS
            if unknown:
                self.report.error(
                    f"class '{name}': keys {sorted(unknown)} may not be "
                    "restated on a redefinition (structural keys such as "
                    "is_a/mixins come from the base)")

            # class-level metaslots (replace; description appends)
            if "description" in cdef:
                base_desc = (target.get("description") or "").rstrip()
                target["description"] = (
                    f"{base_desc}\n[profile] {cdef['description']}".strip())
            if cdef.get("tree_root"):
                target["tree_root"] = True
            for key in ("annotations", "comments", "notes", "see_also", "todos"):
                if key in cdef:
                    if isinstance(cdef[key], list):
                        target[key] = (target.get(key) or []) + cdef[key]
                    else:
                        merged_ann = dict(target.get(key) or {})
                        merged_ann.update(cdef[key])
                        target[key] = merged_ann
            if "rules" in cdef:
                target["rules"] = (target.get("rules") or []) + cdef["rules"]

            # R6 pre-step: differential tree_root clears the base flag elsewhere
            if diff_root_set and not cdef.get("tree_root"):
                target.pop("tree_root", None)

            # slot_usage overlays (R4 + R5)
            induced = {s.name: s for s in self.sv.class_induced_slots(name)}
            usage_target = target.setdefault("slot_usage", {})
            for sname, overlay in (cdef.get("slot_usage") or {}).items():
                overlay = overlay or {}
                if sname not in induced:
                    self.report.error(
                        f"{name}.{sname}: slot_usage targets a slot the base "
                        "class does not have (extensions belong under "
                        "'attributes')")
                    continue
                where = f"{name}.{sname}"
                for meta, value in overlay.items():
                    self.checker.check(where, meta, value, induced[sname])
                slot_target = usage_target.setdefault(sname, {})
                for meta, value in overlay.items():   # R4: stated values replace
                    slot_target[meta] = copy.deepcopy(value)
                if "range" in overlay or "any_of" in overlay:
                    self.range_overrides[(name, sname)] = overlay

            # extension attributes (R3)
            for aname, adef in (cdef.get("attributes") or {}).items():
                adef = adef or {}
                where = f"{name}.{aname}"
                if aname in induced:
                    self.report.error(
                        f"{where}: extension attribute collides with an "
                        "existing base slot (use slot_usage to constrain it)")
                    continue
                if not is_extension(adef):
                    self.report.error(
                        f"{where}: added attribute must be declared an "
                        f"extension ({EXTENSION_ANNOTATION}: true)")
                if bool(adef.get("required")):
                    self.report.error(
                        f"{where}: extension slots must not be required "
                        "(instances stripped of extensions must remain "
                        "base-conformant, spec §5)")
                uri = adef.get("slot_uri", "")
                if uri.startswith("dds:"):
                    self.report.error(
                        f"{where}: extension slot_uri must live in the "
                        "profile's namespace, not 'dds:'")
                elif not uri:
                    self.report.warn(
                        f"{where}: extension slot has no slot_uri; add one in "
                        "the profile namespace (spec §5 rule 2)")
                target.setdefault("attributes", {})[aname] = copy.deepcopy(adef)

        return merged

    # -- R6 ----------------------------------------------------------------

    def find_root(self, merged_classes: dict) -> str:
        roots = [c for c, d in merged_classes.items() if (d or {}).get("tree_root")]
        if len(roots) != 1:
            raise ResolutionError(
                f"R6: expected exactly one tree_root after merge, found {roots}")
        return roots[0]

    def _inherited_usage(self, cname: str, slot_name: str):
        """The differential slot_usage overlay in effect for (class, slot).

        LinkML slot_usage propagates down is_a and mixin hierarchies, so an
        overlay placed on a mixin (e.g. Governed.wasDerivedFrom) governs every
        class that mixes it in. Most-specific class wins.
        """
        diff_classes = self.diff.get("classes") or {}
        try:
            lineage = self.sv.class_ancestors(cname, mixins=True)
        except Exception:
            lineage = [cname]
        for anc in lineage:  # ordered most-specific first
            usage = ((diff_classes.get(anc) or {}).get("slot_usage") or {}
                     ).get(slot_name)
            if usage:
                return usage
        return None

    def _effective_slot_view(self, cname: str) -> list[tuple[str, dict]]:
        """(slot_name, effective raw view) pairs for reachability purposes."""
        out = []
        for slot in self.sv.class_induced_slots(cname):
            raw = {"range": getattr(slot, "range", None),
                   "any_of": [{"range": getattr(a, "range", None)}
                              for a in (getattr(slot, "any_of", []) or [])],
                   "maximum_cardinality": getattr(slot, "maximum_cardinality", None)}
            usage = self._inherited_usage(cname, slot.name)
            if usage and usage.get("maximum_cardinality") == 0:
                continue  # prohibited slots contribute nothing to reachability
            override = usage if usage and (
                "range" in usage or "any_of" in usage) else None
            if override:
                if "range" in override:
                    raw["range"], raw["any_of"] = override["range"], []
                if "any_of" in override:
                    raw["any_of"] = override["any_of"]
                    raw["range"] = None
            out.append((slot.name, raw))
        return out

    def compute_closure(self, merged_classes: dict, root: str
                        ) -> tuple[set, set]:
        base_enums = self.base.get("enums") or {}
        keep_classes: set[str] = set()
        keep_enums: set[str] = set()
        stack = [root]
        while stack:
            cname = stack.pop()
            if cname in keep_classes:
                continue
            if cname in merged_classes:
                keep_classes.add(cname)
                # structural parents: is_a + mixins closure
                for anc in self.sv.class_ancestors(cname, mixins=True):
                    if anc != cname and anc not in keep_classes:
                        stack.append(anc)
                for _, raw in self._effective_slot_view(cname):
                    for r in slot_ranges(raw):
                        self._push_range(r, base_enums, keep_enums, stack)
                # extension attributes on this class
                ext = ((self.diff.get("classes") or {}).get(cname) or {}
                       ).get("attributes") or {}
                for adef in ext.values():
                    for r in slot_ranges(adef or {}):
                        self._push_range(r, base_enums, keep_enums, stack)
            elif cname in self.extension_classes:
                keep_classes.add(cname)
                for adef in (self.extension_classes[cname].get("attributes")
                             or {}).values():
                    for r in slot_ranges(adef or {}):
                        self._push_range(r, base_enums, keep_enums, stack)

    # ranges may point at classes, enums, or builtin types
        return keep_classes, keep_enums

    def _push_range(self, r: str, base_enums: dict, keep_enums: set,
                    stack: list) -> None:
        if not r or r in LINKML_TYPES:
            return
        if (r in base_enums or r in self.subset_enums
                or r in self.extension_enums):
            keep_enums.add(r)
        else:
            stack.append(r)

    # -- assembly (incl. R7) ----------------------------------------------

    def assemble(self, merged_classes: dict, keep_classes: set,
                 keep_enums: set) -> dict:
        base_enums = self.base.get("enums") or {}
        prefixes = dict(self.base.get("prefixes") or {})
        for pfx, uri in (self.diff.get("prefixes") or {}).items():
            if pfx in prefixes and prefixes[pfx] != uri:
                self.report.error(
                    f"prefix '{pfx}' conflicts: base '{prefixes[pfx]}' vs "
                    f"differential '{uri}'")
            prefixes[pfx] = uri

        annotations = dict(self.diff.get("annotations") or {})
        annotations.update({
            "dds.profile.snapshot": "true",                       # R7
            "dds.profile.snapshot.profileId": self.diff.get("id"),
            "dds.profile.snapshot.profileVersion": self.diff.get("version"),
            "dds.profile.snapshot.baseId": self.base.get("id"),
            "dds.profile.snapshot.baseVersion":
                self.base.get("version") or "(unversioned)",
            "dds.profile.snapshot.tool": f"{TOOL_NAME}/{TOOL_VERSION}",
        })

        snap_classes = {c: merged_classes[c] for c in merged_classes
                        if c in keep_classes}
        for name in self.extension_classes:
            if name in keep_classes:
                snap_classes[name] = copy.deepcopy(self.extension_classes[name])

        snap_enums = {e: copy.deepcopy(base_enums[e]) for e in base_enums
                      if e in keep_enums}
        for coll in (self.subset_enums, self.extension_enums):
            for name, edef in coll.items():
                if name in keep_enums:
                    snap_enums[name] = copy.deepcopy(edef)
                else:
                    self.report.warn(
                        f"enum '{name}' defined in differential but "
                        "unreferenced after resolution")

        snapshot = {
            "id": self.diff.get("id"),
            "name": f"{self.diff.get('name')}-snapshot",
            "title": (self.diff.get("title") or self.diff.get("name") or "")
                     + " (snapshot)",
            "description": self.diff.get("description"),
            "version": self.diff.get("version"),
            "license": self.diff.get("license") or self.base.get("license"),
            "prefixes": prefixes,
            "default_prefix": self.diff.get("default_prefix")
                              or self.base.get("default_prefix"),
            "default_range": self.base.get("default_range", "string"),
            "imports": ["linkml:types"],          # self-contained: no dds import
            "annotations": annotations,
            "classes": snap_classes,
            "enums": snap_enums,
        }
        if self.diff.get("slots"):
            snapshot["slots"] = copy.deepcopy(self.diff["slots"])
        return {k: v for k, v in snapshot.items() if v is not None}

    # -- driver ------------------------------------------------------------

    def resolve(self) -> dict:
        self.check_version_gate()
        self.classify_elements()
        merged = self.merge_classes()
        root = self.find_root(merged)
        self.report.note(f"profile root class: {root}")
        if self.prune:
            keep_classes, keep_enums = self.compute_closure(merged, root)
            dropped = len(merged) - len(keep_classes & set(merged))
            self.report.note(
                f"reachability closure: {len(keep_classes)} classes, "
                f"{len(keep_enums)} enums kept; {dropped} base classes dropped")
        else:
            keep_classes = set(merged) | set(self.extension_classes)
            keep_enums = (set(self.base.get('enums') or {})
                          | set(self.subset_enums) | set(self.extension_enums))
        self.snapshot = self.assemble(merged, keep_classes, keep_enums)
        if self.report.errors:
            raise ResolutionError(
                f"{len(self.report.errors)} resolution error(s); "
                "snapshot not written")
        return self.snapshot


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog=TOOL_NAME,
        description="Resolve a DDS profile differential into a snapshot "
                    "(DDS Profiling Specification, Section 6).")
    ap.add_argument("--base", required=True,
                    help="path to the base DDS LinkML schema (e.g. define.yaml)")
    ap.add_argument("--differential", "-d", required=True,
                    help="path to the profile differential schema")
    ap.add_argument("--output", "-o", required=True,
                    help="path to write the resolved snapshot schema")
    ap.add_argument("--no-prune", action="store_true",
                    help="keep unreachable classes/enums (skip R6 pruning)")
    ap.add_argument("--allow-unversioned-base", action="store_true",
                    help="permit a base model without a 'version' field "
                         "(R1 gate downgraded to a warning)")
    args = ap.parse_args(argv)

    try:
        resolver = SnapshotResolver(
            args.base, args.differential,
            allow_unversioned_base=args.allow_unversioned_base,
            prune=not args.no_prune)
        snapshot = resolver.resolve()
    except ResolutionError as exc:
        if 'resolver' in dir() and resolver.report:
            resolver.report.emit()
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1

    with open(args.output, "w", encoding="utf-8") as fh:
        fh.write(f"# GENERATED by {TOOL_NAME} {TOOL_VERSION} — do not edit.\n"
                 f"# Regenerate from the differential; hand edits to a "
                 f"snapshot are never permitted.\n")
        yaml.safe_dump(snapshot, fh, sort_keys=False, allow_unicode=True,
                       default_flow_style=False, width=100)
    resolver.report.emit()
    print(f"snapshot written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
