# cdisc-for-ai

Exploratory work on making CDISC standards machine-actionable for humans and AI.

## Background

CDISC publishes authoritative standards for clinical trial data — controlled terminology, biomedical concepts, dataset specializations, study design definitions. The information is there. But it is scattered across multiple sources with no machine-traversable connections between them, and the flat formats hide the semantic structure that both humans and automated systems need to reason correctly.

This repository documents early explorative work on that problem, with laboratory standards as the focus area.

## Contents

### skills/sdtm-ct-analysis

A two-prompt workflow for structural analysis of the CDISC SDTM Controlled Terminology file — discovering the semantic categories present and generating a machine-actionability archetype table.

The workflow is documented as a Claude Skill: a structured, repeatable process with explicit constraints on how the AI reasons, what it is allowed to claim, and where it must stop. The output is verifiable — anyone with the same public NCI EVS input file can check every assignment.

## Status

Early and exploratory. Not a finished product.

## Author

Kerstin Forsberg — information architect specializing in clinical data standards.
