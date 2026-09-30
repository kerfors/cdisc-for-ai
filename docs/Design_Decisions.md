# Design decisions

*Moved from the root README, 2026-09-30.*

**Why flat files?** Excel files with README sheets reach the broadest audience today: data managers, statisticians, LLMs, rule engines. The underlying relationships are graph-shaped, but flat projections are the most accessible delivery format until the standards are published as a traversable graph.

**Why "machine-actionable" not "AI-friendly"?** Applies to any automated system, not just LLMs. Aligns with FAIR data principles.

**Why interim/?** Downloads are external. Interim files are our own pipeline artifacts, visible because they have value as standalone artifacts, even if not the final product.

**Why renamed columns?** COSMoS source field names are implementation-oriented (vlm_group_id, specimenIdentity, resultScale). The consumer files translate these to more transparent names (DS_Code, Specimen, Result_Scale) while documenting the mapping in the Flatten notebook for traceability.

**Why three consumer notebooks?** The three Findings structural types (specimen-based, instrument-based, measurement) have fundamentally different data shapes and join logic. Splitting by structural type keeps each notebook focused and its output consumable.
