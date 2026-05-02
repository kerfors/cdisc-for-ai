# Family-Map Inventory Integration — Prompt Template

Integrate the repo-level Procedure-Options Inventory into a single Clinical-Knowledge Reference family map. Output is the existing family-map workbook augmented with a cross-reference layer that points each clinical-knowledge pair to the inventory's procedure-level findings, without re-authoring inventory content per family.

The integration is mechanical lookup, not original analysis. The inventory is the source of truth for procedure-option findings; the family map carries cross-references back to it. If a family-map row references a procedure not yet in the inventory, the prompt flags it and stops rather than authoring inventory content inline. Inventory authorship is governed by its own prompt and its own cite-checking discipline.

The integration runs in two modes. Default is a lightweight pointer column suitable for family-map readers who want to know that procedure-option findings exist and where to look. The optional rich mode embeds dimension-level summary cells inline for the COSMoS authoring conversation specifically. The mode is a runtime flag, set at the start of the integration session.

---

## Inputs required

- A target `*_Clinical_Knowledge_Reference.xlsx` family map (one of MRI of liver, DXA for osteoporosis, hand and foot X-ray for RA structural progression, or any future family map that follows the same template).
- `Procedure_Options_Inventory.xlsx` — the repo-level inventory at the version current to the integration session.
- The integration mode flag — `lightweight` (default) or `rich`.

No new clinical-knowledge content is authored. No new inventory content is authored. Stage 1b cite-checking from the family-map and inventory prompts is inherited; this prompt does not add citations.

---

## Stage 1 — Procedure name reconciliation

Build a join between the target family map's Sheet 1 (`Clinical_Knowledge_Pairs`, column `Procedure`) and the inventory's Sheet 1 (`Procedures`, column `Procedure canonical name`). The join is on procedure identity, not free-text equality.

For each family-map row:

- **Find the matching inventory row by canonical procedure name.** The inventory's `Family maps` column carries the family-map filename(s) where each procedure was originally surfaced; this anchors the match. A family-map row whose procedure language drifts from the inventory's canonical name (paraphrasing, abbreviation, ordering of qualifiers) still matches if the underlying procedure is identical.
- **Where the family-map row references a procedure split across two or more canonical inventory entries** (e.g., a single family-map pair that mentions "MRI of liver, multiphase contrast-enhanced or hepatobiliary-agent-enhanced" matching both P12 and P13), record the multi-match explicitly in the cross-reference. Do not collapse to one entry; the inventory's distinction was deliberate.
- **Where the family-map row references a procedure not in the inventory**, halt and report. Do not author the missing procedure inline. The inventory must be re-run with the new procedure added before integration can proceed. The most likely cause is a new family map that introduced procedures the inventory does not yet know about.
- **Where the family-map row is procedure-only with no measurement** (e.g., MRCP for biliary anatomy in the liver map), the cross-reference still applies; the inventory tracks all procedures including procedure-only entries.
- **Where the family-map row is a composite indicator that combines a procedure result with non-procedure inputs** (e.g., FRAX = DXA BMD + clinical risk factor questionnaire; TBS-FRAX = DXA + TBS + risk factors; future indices that combine an imaging result with serum markers, demographics, or PROs), match the cross-reference to the underlying procedure(s) and append the annotation `composite-indicator (X + non-procedure inputs)` to the cross-reference cell. The inventory excludes composite indicators from its procedure list by design (they are derived indices, not procedure variants), but the underlying procedure's findings are clinically relevant to the composite and should be reachable from the family-map row. The annotation preserves the visibility of the inventory's design choice. Multiple-procedure composites (e.g., TBS-FRAX combining DXA femur and DXA lumbar spine TBS) carry a multi-match Proc ID list with the same annotation appended once.

The Stage 1 output is an internal join table: family-map row index → inventory Proc IDs (one or more), with optional composite-indicator annotation. This table is not surfaced in the deliverable but drives Stages 2 and 3.

---

## Stage 2 — Cross-reference column construction (lightweight mode)

For each family-map Sheet 1 row, construct a single new column value with three sub-fields concatenated in a stable format:

- **Procedure ID(s) in inventory** — one or more `Pnn` identifiers from inventory Sheet 1 column A. E.g., `P12` or `P12, P13`.
- **F-tier count and C-tier count** — counts of cells in the inventory matrix for this procedure that resolve to Architectural-observation-flag and Catalog-ahead-of-standards tiers respectively. E.g., `F:2 C:4`. Aligned cells and not-applicable cells are not counted.
- **Pointer to inventory observations** — a stable text reference to the inventory file and Observations sheet, filterable by Proc ID. E.g., `→ Procedure_Options_Inventory.xlsx · Observations · Proc ID=P12`.

The full column value, stable format: `P12 · F:2 C:4 → Procedure_Options_Inventory.xlsx · Observations · Proc ID=P12`.

For multi-match rows, the format is comma-separated at the Proc ID and combined at the counts:
`P12, P13 · F:2+5 C:4+4 → Procedure_Options_Inventory.xlsx · Observations · Proc ID in (P12, P13)`.

For composite-indicator rows (per Stage 1), the annotation `· composite-indicator (X + non-procedure inputs)` is inserted between the count field and the pointer:
`P08 · F:4 C:2 · composite-indicator (DXA + non-procedure inputs) → Procedure_Options_Inventory.xlsx · Observations · Proc ID=P08`.
For composite indicators that span multiple procedures, the multi-match format and the composite annotation combine:
`P07, P08 · F:4+4 C:3+2 · composite-indicator (DXA + non-procedure inputs) → Procedure_Options_Inventory.xlsx · Observations · Proc ID in (P07, P08)`.

Add the column to family-map Sheet 1 with header `Procedure-option findings (inventory cross-ref)`. Place it as the rightmost column. Do not modify any existing column content. Do not modify Sheet 2 (`COSMoS_Coverage`) or Sheet 3 (`Notes_Legend`).

---

## Stage 3 — Rich-mode augmentation (rich mode only; skip in lightweight)

In rich mode, in addition to the lightweight cross-reference column, add an additional column or columns that carry dimension-level summary content inline. Two sub-options exist; the rich-mode runtime flag should specify which:

- **Rich-mode-tier-summary** — one new column per dimension (D01 through D13 in the current inventory; the dimension count grows monotonically as families are added). Each cell carries the tier letter (`A`, `F`, `C`, or `—`) for that procedure × dimension intersection. The reader sees the tier matrix inline next to each clinical-knowledge pair. Familiar from the inventory's Sheet 3 but joined into the family map for one-stop reading.

- **Rich-mode-observation-inline** — one new column carrying a concatenated string of all non-Aligned, non-em-dash observations for the procedure. Reproduces the per-cell architectural-observation text from inventory Sheet 4 alongside the family-map row. Verbose. Recommended only for COSMoS-authoring discussion documents where the reader's primary interest is the architectural observations themselves.

Both rich sub-options are derived from the inventory; nothing is re-authored. If the inventory updates, the family map is re-run from this prompt to refresh.

The rich-mode default if the user does not specify a sub-option is `tier-summary`. The observation-inline mode should only be selected explicitly when the family map will be used as standalone briefing material without the inventory present.

---

## Stage 4 — Notes update

In the family map's Notes_Legend (Sheet 3), add a new section titled `Procedure-option findings (inventory cross-reference)` with three short paragraphs:

- **What this column carries.** Single-paragraph explanation of the Proc ID pointer, the F-tier and C-tier counts, and the link to the inventory file. Notes that the inventory is the source of truth for procedure-option findings and that the family map carries cross-references only.
- **What the integration mode is.** One sentence stating which mode (lightweight or rich) was used and, if rich, which sub-mode.
- **When the cross-reference was last refreshed.** The integration date and the inventory file version (its Generated date from inventory Notes_Legend Provenance). Re-running the integration produces a delta unless inventory or family map have changed; record the version pair for traceability.

This is the only modification to Sheet 3. Existing Notes_Legend sections (Architecture, Status codes, Kind codes, Coverage tiers, Key findings, Methodology, Provenance, Verified references) are untouched.

---

## Stage 5 — Deliverable

The target family map workbook, with the new column appended to Sheet 1 and the new section appended to Sheet 3. File name unchanged. Generated-date in Provenance updated to the integration run date.

The integration is non-destructive. Existing Sheet 1 columns, Sheet 2 entirely, and existing Sheet 3 sections are preserved byte-for-byte where possible. Color coding on Sheet 1 status column is preserved; the new column inherits the row colour but does not introduce new colour rules.

If the family map was generated before the standardised audit-trail-section convention was established (e.g., the original MRI of liver map), the integration does not retrofit the audit trail. That is a separate clean-up task.

---

## Stage 6 — Repository integration

The integrated family map replaces the previous version in the repo. The Procedure-Options Inventory does not change as a result of this run. The integration date is recorded in the family map's Provenance.

Cross-family runs of this prompt are independent. Running the integration for the DXA family map does not alter the MRI-of-liver or RA-X-ray maps. Each family map carries its own cross-reference to the same inventory.

When the inventory is re-run (because a new family added new procedures or new dimensions), each family map should be re-integrated to refresh tier counts and observation pointers. The integration is fast and mechanical; running it across all current family maps in sequence is reasonable maintenance.

---

## Failure modes and what to do

- **Family-map procedure not in inventory.** Halt; report the procedure to the user; advise re-running the inventory prompt with the new procedure added. Do not proceed.
- **Inventory contains procedures not in any family map.** This is normal — the inventory is repo-level and its current procedure list is the union from earlier families. No action required during this prompt's run.
- **Family-map procedure description ambiguous between two inventory entries.** Halt; report the ambiguity; ask the user which entry the family-map row maps to. Do not silently choose. The ambiguity is itself useful information about whether the inventory's canonicalisation needs refinement.
- **Inventory schema has changed since the family map was last integrated.** Detect by comparing inventory column names to the prompt's expected set. If the schema has changed, halt and report; the prompt may need updating before it can produce a faithful integration.
- **Family-map row is a composite indicator combining a procedure result with non-procedure inputs** (FRAX, TBS-FRAX, similar derived indices in future families). This is a deliberate non-failure case. Match to the underlying procedure(s) per Stage 1, append the `composite-indicator (X + non-procedure inputs)` annotation to the cross-reference cell per Stage 2, and proceed. Do not halt. The inventory's exclusion of composite indicators is a design choice; the integration's role is to make the underlying procedure findings reachable while preserving visibility of the design choice via the annotation. Track the count of composite-indicator rows processed in the Stage 4 Notes_Legend refresh-provenance entry.
- **Rich-mode dimension count exceeds reasonable column-width budget.** With the current 13 dimensions, rich-mode-tier-summary adds 13 columns to Sheet 1; this is workable but cramped. If the inventory grows past ~20 dimensions, rich-mode-tier-summary should be split across two sheets (one Sheet 1 keeping the original family-map content, one new sheet carrying the tier matrix). Default to lightweight in that scenario unless the user has a specific reason for rich.

---

## Methodological commitments

- **No content authoring at integration.** The integration prompt does not author clinical-knowledge content, does not author inventory content, does not add citations. It is mechanical lookup and surfacing. Authorship lives in the family-map prompt and the inventory prompt; this prompt is the join.
- **Non-destructive on inputs.** The family map is augmented, not rewritten. The inventory is read, not modified. Both files are preserved at their current versions.
- **Inventory is single source of truth for procedure-options findings.** Every procedure-option observation referenced from a family map traces to a specific row in inventory Sheet 4. The cross-reference is queryable, not paraphrased.
- **Lightweight default.** The lightweight mode is the default because most family-map readers want to know that procedure-option findings exist and where to find them, not to read them inline. Rich mode is opt-in for specific use cases.
- **Re-run cadence is event-driven.** Re-integrate when (a) the inventory is updated, (b) the family map is updated with new pairs, or (c) a procedure is renamed in either source. Otherwise the integration is stable.
- **Procedure-identity convention is borrowed, not re-derived.** The PROCEDUR-anchor + anatomy + technique convention from the inventory is the canonical naming; the family map's free-text procedure description is the matching key only.

---

## Provenance fields to capture in each integration run

- Source family map — file name and Generated date
- Source inventory — file name and Generated date
- Integration mode — `lightweight` or `rich-tier-summary` or `rich-observation-inline`
- Integration date
- Analysis tool (Claude model used)
- Repository home — `https://github.com/kerfors/cdisc-for-ai`

---

## Notes on the integration's scope and stability

The integration prompt deliberately does not add Stage-4-style architectural-observations summaries to the family map. The inventory's findings are repo-level findings, not per-family findings; reproducing them inline in each family map would duplicate the architectural summary across artefacts and create a maintenance burden when the inventory is updated. The cross-reference pointer is enough — readers who want the synthesis read the inventory's Notes_Legend Key findings; readers who want per-cell detail filter inventory Sheet 4 by Proc ID.

If, after running this integration across the three current family maps, it becomes clear that some patterns recur strongly enough that they warrant per-family summary, the prompt can be extended later with a Stage 4 summary section. For now, the discipline is: inventory carries findings; family maps carry pointers.
