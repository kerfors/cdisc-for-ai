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

The reference files produced by the source and consumer tracks are designed for skill consumption — additional skills for tasks like term mapping, panel decomposition, and LOINC cross-validation are natural next steps.
