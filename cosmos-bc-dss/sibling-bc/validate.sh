#!/usr/bin/env bash
# Validation for the sibling BC sketch split (run from anywhere).
# Requires: pip install linkml   (tested with linkml 1.11.1)
set -euo pipefail
cd "$(dirname "$0")"
gen-json-schema sibling_bc.schema.yaml > sibling_bc.schema.json
linkml-validate --schema sibling_bc.schema.yaml --target-class SiblingBcSketchData sibling_bc.instances.yaml
echo "OK: schema generates + instances validate"
