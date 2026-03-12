# Skills

Reusable AI workflows for working with CDISC standards.

## What is a Skill?

A Skill is a structured instruction set that tells an AI assistant how to approach a specific task — what to reason from, what constraints apply, what outputs to produce, and in what order. It makes a workflow repeatable and inspectable rather than dependent on how you happened to phrase the question on a given day.

Each skill is a folder containing a `SKILL.md` (the workflow definition) and any supporting prompt files it references. The prompts are the working instructions; the SKILL.md is the orchestration.

## Why Skills?

In regulated environments, "I asked AI and it gave a good answer" is not defensible. A documented, constrained workflow — with explicit inputs, reasoning boundaries, and verifiable outputs — is. Skills are a simple way to capture that discipline: plain markdown files, readable by both humans and LLMs, portable across environments.

## Available Skills

| Skill | Purpose | Input |
|---|---|---|
| [`sdtm-ct-analysis/`](sdtm-ct-analysis/) | Structural categorization of SDTM Controlled Terminology | NCI EVS SDTM Terminology file |
| [`specimen-findings-ct-mapping/`](specimen-findings-ct-mapping/) | Map specimen-based measurement terms to CDISC CT and COSMoS specifications | [`Study_Design_Merge.xlsx`](../cosmos-bc-dss/interim/Study_Design_Merge.xlsx) |

`sdtm-ct-analysis` is a two-step inductive analysis workflow — category discovery followed by profile generation. Produces structural understanding of SDTM CT, not operational mappings.

`specimen-findings-ct-mapping` *(exploratory)* resolves measurement terms (from SoA tables, lab catalogs, or similar sources) to SDTM TESTCDs and, where COSMoS coverage exists, to dataset specialization level (specimen, method, scale, units, LOINC). Uses semantic clinical reasoning, not string matching. Produces candidate mappings for SME review. Evolving from an earlier CT-only mapping prompt — now uses the merged green+yellow reference file for two-level resolution.

## Planned

Additional skills using the reference files for practical tasks — panel decomposition, unit harmonization, LOINC cross-validation.
