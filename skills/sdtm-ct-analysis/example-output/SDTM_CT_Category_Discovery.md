# SDTM CT Category Discovery — Analysis Report

**Source:** CDISC SDTM Controlled Terminology, NCI EVS
**Release:** 2025-09-26
**Codelist headers analyzed:** 1,181
**Categories discovered:** 25
**Analysis date:** 2026-03-09

---

## Section 1 — Category Definitions

```
Category name: Instrument Test Code
Definition: Codelist of short test identifiers (TESTCDs) for a specific QRS instrument or functional test.
Structural signature: Name ends "Test Code"; submission value ends TC; paired with TN codelist.
Primary discriminator: Codelist Name contains "Test Code"
Count: 409 (Extensible: 56 Yes, 353 No)
```

```
Category name: Instrument Test Name
Definition: Codelist of full-text test names (TESTs) for a specific QRS instrument or functional test.
Structural signature: Name ends "Test Name"; submission value ends TN; paired with TC codelist.
Primary discriminator: Codelist Name contains "Test Name"
Count: 409 (Extensible: 56 Yes, 353 No)
```

```
Category name: Instrument Original Result
Definition: Allowed original result values (ORRES) for specific questions within a QRS or clinical classification instrument.
Structural signature: Name contains "ORRES" or "Clinical Classification ORRES"; SV ends OR; always non-extensible.
Primary discriminator: Submission value suffix OR with instrument-prefix naming
Count: 79 (Extensible: 0 Yes, 79 No)
```

```
Category name: Instrument Standardized Result
Definition: Allowed standardized character result values (STRESC) for specific questions within a QRS or clinical classification instrument.
Structural signature: Name contains "STRESC" or "Clinical Classification STRESC"; SV ends STR; always non-extensible.
Primary discriminator: Submission value suffix STR with instrument-prefix naming
Count: 79 (Extensible: 0 Yes, 79 No)
```

```
Category name: Clinical Classification
Definition: Standalone clinical grading, staging, or classification system not structured as a QRS instrument.
Structural signature: Name contains Grade/Classification/Scale/Class; almost always non-extensible; no TC/TN pairs.
Primary discriminator: Absence of instrument pairing (no TC/TN/OR/STR set) combined with classification naming
Count: 27 (Extensible: 1 Yes, 26 No)
```

```
Category name: Observation Qualifier
Definition: General-purpose codelist that qualifies or describes an observation context, result characteristic, or clinical state.
Structural signature: Heterogeneous names; mostly extensible; definition references "relevant to" a qualifying property.
Primary discriminator: Residual after all specific-role categories; qualifies observations without fitting a narrower role
Count: 27 (Extensible: 22 Yes, 5 No)
```

```
Category name: Trial Design
Definition: Codelist that describes study-level or protocol-level design metadata.
Structural signature: Name references Trial/Study/Protocol/SDTM/Epoch/Domain; mostly extensible.
Primary discriminator: Codelist Name or submission value references trial/study/protocol design constructs
Count: 24 (Extensible: 19 Yes, 5 No)
```

```
Category name: Treatment Qualifier
Definition: Codelist that qualifies an intervention: dosage form, route, frequency, treatment reason, or procedure.
Structural signature: Name references Route/Dosage/Frequency/Treatment/Therapy/Procedure; all extensible.
Primary discriminator: Codelist Name references intervention administration properties
Count: 14 (Extensible: 14 Yes, 0 No)
```

```
Category name: Domain Category
Definition: Codelist used as the --CAT variable for a specific SDTM domain, grouping records within that domain.
Structural signature: Name follows "Category of [Domain]" or "Subcategory for [Domain]" pattern.
Primary discriminator: Codelist Name pattern "Category of/for" or "Subcategory"
Count: 12 (Extensible: 10 Yes, 2 No)
```

```
Category name: Method
Definition: Codelist of analytical, measurement, or collection methods.
Structural signature: Name contains Method or Analytical; always extensible.
Primary discriminator: Codelist Name contains "Method" or "Analytical"
Count: 12 (Extensible: 12 Yes, 0 No)
```

```
Category name: Demographic
Definition: Codelist capturing subject demographic characteristics: race, sex, ethnicity, gender identity, marital status, employment.
Structural signature: Defined set of demographic variable names; mixed extensibility (collected-as variants extensible).
Primary discriminator: Codelist Name matches a known demographic concept (Race, Sex, Ethnic, Gender, Marital, Employment)
Count: 11 (Extensible: 8 Yes, 3 No)
```

```
Category name: Disposition
Definition: Codelist related to subject disposition events, study completion status, or protocol milestones.
Structural signature: Name contains Disposition/Completion/Status; mixed extensibility.
Primary discriminator: Codelist Name contains "Disposition", "Completion", or "Status"
Count: 10 (Extensible: 8 Yes, 2 No)
```

```
Category name: Parameter Name-Code
Definition: Paired codelists defining parameter names and their short codes for PK, device, tobacco, or organism identifier variables.
Structural signature: Name contains "Parameter" with "Name" or "Code"; always extensible; come in PARM/PARMCD pairs.
Primary discriminator: Codelist Name contains "Parameter" and ("Name" or "Code")
Count: 10 (Extensible: 10 Yes, 0 No)
```

```
Category name: Role/Relationship
Definition: Codelist identifying roles (evaluator, contact) or relationships between entities in a study.
Structural signature: Name references Evaluator/Contact/Relationship/Accountable; mostly extensible.
Primary discriminator: Codelist Name references a role or relationship concept
Count: 9 (Extensible: 8 Yes, 1 No)
```

```
Category name: Unit of Measure
Definition: Codelist of measurement units for a specific variable context (general, PK, vital signs, age).
Structural signature: Name contains "Unit" or "Units of Measure"; mostly extensible.
Primary discriminator: Codelist Name contains "Unit" and definition references measurement
Count: 8 (Extensible: 7 Yes, 1 No)
```

```
Category name: Device
Definition: Codelist specific to medical device tracking, properties, or device-related events.
Structural signature: Name contains "Device" or device-component terms (Graft, Lead Abnormality); all extensible.
Primary discriminator: Codelist Name references device concepts
Count: 6 (Extensible: 6 Yes, 0 No)
```

```
Category name: Specimen
Definition: Codelist describing specimen types, conditions, or collection characteristics.
Structural signature: Name contains Specimen/Sample/Culture; all extensible.
Primary discriminator: Codelist Name references specimen or sample concepts
Count: 6 (Extensible: 6 Yes, 0 No)
```

```
Category name: Adverse Event Qualifier
Definition: Codelist qualifying adverse events: action taken, outcome, severity scale.
Structural signature: Defined set: ACN, TPACN, OUT, AESEV, plus "Action Taken" pattern.
Primary discriminator: Codelist submission value is a known AE qualifier variable code
Count: 5 (Extensible: 2 Yes, 3 No)
```

```
Category name: Anatomical Qualifier
Definition: Codelist qualifying anatomical position: location, laterality, directionality, portion.
Structural signature: Name references Location/Laterality/Directionality/Position/Portion; all extensible.
Primary discriminator: Codelist Name references anatomical spatial qualifiers
Count: 5 (Extensible: 5 Yes, 0 No)
```

```
Category name: Microbiology/Immunology
Definition: Codelist specific to microbiology or immunology testing: organisms, test details, susceptibility results.
Structural signature: Name contains Microorganism/Microbiology/Microscopic/Immunogenicity; all extensible.
Primary discriminator: Codelist Name references microbiology or immunology domain concepts
Count: 5 (Extensible: 5 Yes, 0 No)
```

```
Category name: Oncology Assessment
Definition: Codelist specific to oncology response assessment, tumor identification, or lesion properties.
Structural signature: Name contains Oncology/Tumor/Lesion; mostly extensible.
Primary discriminator: Codelist Name references oncology assessment concepts
Count: 4 (Extensible: 3 Yes, 1 No)
```

```
Category name: Dictionary Reference
Definition: Codelist of standardized dictionary-derived terms or dictionary names used for coding.
Structural signature: Name contains "Dictionary" or "Dictionary Derived Term"; all extensible.
Primary discriminator: Codelist Name contains "Dictionary"
Count: 3 (Extensible: 3 Yes, 0 No)
```

```
Category name: ECG Findings
Definition: Codelist specific to ECG domain results, leads, or finding values (not method or instrument items).
Structural signature: Name references ECG Lead/Result/Findings; all extensible; distinct from ECG method codelists.
Primary discriminator: Codelist Name references ECG result/lead/finding concepts (excluding Method)
Count: 3 (Extensible: 3 Yes, 0 No)
```

```
Category name: Genomic
Definition: Codelist specific to genomic findings: test details, inheritability, symbol types.
Structural signature: Name contains Genomic/Genetic; all extensible.
Primary discriminator: Codelist Name references genomic or genetic concepts
Count: 3 (Extensible: 3 Yes, 0 No)
```

```
Category name: Tobacco Product
Definition: Codelist specific to tobacco product categorization (beyond tobacco-specific parameters and completion, which are in other categories).
Structural signature: Name contains "Tobacco Product Category"; extensible.
Primary discriminator: Codelist Name references tobacco product category
Count: 1 (Extensible: 1 Yes, 0 No)
```

---

## Section 2 — Full Assignment Table

| CDISC_Submission_Value | Codelist_Name | Assigned_Category | Confidence | Note |
|---|---|---|---|---|
| TENMW1TC | 10-Meter Walk/Run Functional Test Test Code | Instrument Test Code | HIGH |  |
| TENMW1TN | 10-Meter Walk/Run Functional Test Test Name | Instrument Test Name | HIGH |  |
| A4STR1TC | 4-Stair Ascend Functional Test Test Code | Instrument Test Code | HIGH |  |
| A4STR1TN | 4-Stair Ascend Functional Test Test Name | Instrument Test Name | HIGH |  |
| D4STR1TC | 4-Stair Descend Functional Test Test Code | Instrument Test Code | HIGH |  |
| D4STR1TN | 4-Stair Descend Functional Test Test Name | Instrument Test Name | HIGH |  |
| SIXMW1TC | 6 Minute Walk Functional Test Test Code | Instrument Test Code | HIGH |  |
| SIXMW1TN | 6 Minute Walk Functional Test Test Name | Instrument Test Name | HIGH |  |
| AVL01TC | ADNI Auditory Verbal Learning Functional Test Test Code | Instrument Test Code | HIGH |  |
| AVL01TN | ADNI Auditory Verbal Learning Functional Test Test Name | Instrument Test Name | HIGH |  |
| AJCC1TC | AJCC TNM Staging System 7th Edition Clinical Classification Test  | Instrument Test Code | HIGH |  |
| AJCC1TN | AJCC TNM Staging System 7th Edition Clinical Classification Test  | Instrument Test Name | HIGH |  |
| AJCCGRD | AJCC Tumor Grade Response | Clinical Classification | HIGH |  |
| ASSG01TC | ASSIGN Cardiovascular Disease 10-Year Risk Score Clinical Classif | Instrument Test Code | HIGH |  |
| ASSG01TN | ASSIGN Cardiovascular Disease 10-Year Risk Score Clinical Classif | Instrument Test Name | HIGH |  |
| ATLAS101OR | ATLAS Clinical Classification ORRES for ATLAS101 TN/TC | Instrument Original Result | HIGH |  |
| ATLAS102OR | ATLAS Clinical Classification ORRES for ATLAS102 TN/TC | Instrument Original Result | HIGH |  |
| ATLAS103OR | ATLAS Clinical Classification ORRES for ATLAS103 TN/TC | Instrument Original Result | HIGH |  |
| ATLAS104OR | ATLAS Clinical Classification ORRES for ATLAS104 TN/TC | Instrument Original Result | HIGH |  |
| ATLAS105OR | ATLAS Clinical Classification ORRES for ATLAS105 TN/TC | Instrument Original Result | HIGH |  |
| ATLAS101STR | ATLAS Clinical Classification STRESC for ATLAS101 TN/TC | Instrument Standardized Result | HIGH |  |
| ATLAS102STR | ATLAS Clinical Classification STRESC for ATLAS102 TN/TC | Instrument Standardized Result | HIGH |  |
| ATLAS103STR | ATLAS Clinical Classification STRESC for ATLAS103 TN/TC | Instrument Standardized Result | HIGH |  |
| ATLAS104STR | ATLAS Clinical Classification STRESC for ATLAS104 TN/TC | Instrument Standardized Result | HIGH |  |
| ATLAS105STR | ATLAS Clinical Classification STRESC for ATLAS105 TN/TC | Instrument Standardized Result | HIGH |  |
| ATLAS1TC | ATLAS Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| ATLAS1TN | ATLAS Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| AIMS0101T07OR | Abnormal Involuntary Movement Scale Clinical Classification ORRES | Instrument Original Result | HIGH |  |
| AIMS0108T09OR | Abnormal Involuntary Movement Scale Clinical Classification ORRES | Instrument Original Result | HIGH |  |
| AIMS0110OR | Abnormal Involuntary Movement Scale Clinical Classification ORRES | Instrument Original Result | HIGH |  |
| AIMS0111T12OR | Abnormal Involuntary Movement Scale Clinical Classification ORRES | Instrument Original Result | HIGH |  |
| AIMS0101T07STR | Abnormal Involuntary Movement Scale Clinical Classification STRES | Instrument Standardized Result | HIGH |  |
| AIMS0108T09STR | Abnormal Involuntary Movement Scale Clinical Classification STRES | Instrument Standardized Result | HIGH |  |
| AIMS0110STR | Abnormal Involuntary Movement Scale Clinical Classification STRES | Instrument Standardized Result | HIGH |  |
| AIMS0111T12STR | Abnormal Involuntary Movement Scale Clinical Classification STRES | Instrument Standardized Result | HIGH |  |
| AIMS01TC | Abnormal Involuntary Movement Scale Clinical Classification Test  | Instrument Test Code | HIGH |  |
| AIMS01TN | Abnormal Involuntary Movement Scale Clinical Classification Test  | Instrument Test Name | HIGH |  |
| ACCPARTY | Accountable Party | Role/Relationship | HIGH |  |
| ACN | Action Taken with Study Treatment | Adverse Event Qualifier | HIGH |  |
| TPACN | Action Taken with Tobacco Product | Adverse Event Qualifier | HIGH |  |
| ACSPCAT | Acute Coronary Syndrome Presentation Category | Clinical Classification | HIGH |  |
| APCH101OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH102OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH103OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH104OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH105AOR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH105BOR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH106AOR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH106BOR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH107OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH108OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH109OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH110OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH111OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH114OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH115OR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Original Result | HIGH |  |
| APCH101STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH102STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH103STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH104STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH105ASTR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH105BSTR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH106ASTR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH106BSTR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH107STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH108STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH109STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH110STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH111STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH114STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH115STR | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Standardized Result | HIGH |  |
| APCH1TC | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Test Code | HIGH |  |
| APCH1TN | Acute Physiology and Chronic Health Evaluation II Clinical Classi | Instrument Test Name | HIGH |  |
| ADTNQRS | Administration Technique Response | Observation Qualifier | HIGH |  |
| AGEU | Age Unit | Unit of Measure | HIGH |  |
| AQ01TC | Airway Questionnaire 20 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| AQ01TN | Airway Questionnaire 20 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ADTC01TC | Alcohol Use Disorder Identification Test-Consumption Questions Qu | Instrument Test Code | HIGH |  |
| ADTC01TN | Alcohol Use Disorder Identification Test-Consumption Questions Qu | Instrument Test Name | HIGH |  |
| ADT01TC | Alcohol Use Disorder Identification Test: Self-Report Version Que | Instrument Test Code | HIGH |  |
| ADT01TN | Alcohol Use Disorder Identification Test: Self-Report Version Que | Instrument Test Name | HIGH |  |
| AVPU01TC | Alert Verbal Painful Unresponsive Scale Clinical Classification T | Instrument Test Code | HIGH |  |
| AVPU01TN | Alert Verbal Painful Unresponsive Scale Clinical Classification T | Instrument Test Name | HIGH |  |
| ADCTC | Alzheimer's Disease Assessment Scale - Cognitive CDISC Version Fu | Instrument Test Code | HIGH |  |
| ADCTN | Alzheimer's Disease Assessment Scale - Cognitive CDISC Version Fu | Instrument Test Name | HIGH |  |
| ADC1TC | Alzheimer's Disease Assessment Scale-Cognitive 30JUN2015 Function | Instrument Test Code | HIGH |  |
| ADC1TN | Alzheimer's Disease Assessment Scale-Cognitive 30JUN2015 Function | Instrument Test Name | HIGH |  |
| ADL03TC | Alzheimer's Disease Cooperative Study-Activities of Daily Living  | Instrument Test Code | HIGH |  |
| ADL03TN | Alzheimer's Disease Cooperative Study-Activities of Daily Living  | Instrument Test Name | HIGH |  |
| ADL01TC | Alzheimer's Disease Cooperative Study-Activities of Daily Living  | Instrument Test Code | HIGH |  |
| ADL01TN | Alzheimer's Disease Cooperative Study-Activities of Daily Living  | Instrument Test Name | HIGH |  |
| ADL02TC | Alzheimer's Disease Cooperative Study-Activities of Daily Living  | Instrument Test Code | HIGH |  |
| ADL02TN | Alzheimer's Disease Cooperative Study-Activities of Daily Living  | Instrument Test Name | HIGH |  |
| ACGC01TC | Alzheimer's Disease Cooperative Study-Clinical Global Impression  | Instrument Test Code | HIGH |  |
| ACGC01TN | Alzheimer's Disease Cooperative Study-Clinical Global Impression  | Instrument Test Name | HIGH |  |
| LOC | Anatomical Location | Anatomical Qualifier | HIGH |  |
| AVOUTTRT | Anti-Viral Outcome of Treatment | Treatment Qualifier | HIGH |  |
| APGR01TC | Apgar Score V1 Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| APGR01TN | Apgar Score V1 Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| ASEX01TC | Arizona Sexual Experiences Scale - Female Questionnaire Test Code | Instrument Test Code | HIGH |  |
| ASEX01TN | Arizona Sexual Experiences Scale - Female Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ASEX02TC | Arizona Sexual Experiences Scale - Male Questionnaire Test Code | Instrument Test Code | HIGH |  |
| ASEX02TN | Arizona Sexual Experiences Scale - Male Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ARMNULRS | Arm Null Reason | Trial Design | HIGH |  |
| ADSD01TC | Asthma Daytime Symptom Diary v1.0 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| ADSD01TN | Asthma Daytime Symptom Diary v1.0 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ASFATSCD | Asthma Findings About Test Code | Instrument Test Code | HIGH |  |
| ASFATS | Asthma Findings About Test Name | Instrument Test Name | HIGH |  |
| ANSD01TC | Asthma Nighttime Symptom Diary v1.0 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| ANSD01TN | Asthma Nighttime Symptom Diary v1.0 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ASCVD1TC | Atherosclerotic Cardiovascular Disease 10-Year Risk Estimator Cli | Instrument Test Code | HIGH |  |
| ASCVD1TN | Atherosclerotic Cardiovascular Disease 10-Year Risk Estimator Cli | Instrument Test Name | HIGH |  |
| AUTESTCD | Auricular Findings Test Code | Instrument Test Code | HIGH |  |
| AUTEST | Auricular Findings Test Name | Instrument Test Name | HIGH |  |
| BRDGMOOD | BRIDG Activity Mood | Trial Design | HIGH |  |
| BEBQ01TC | Baby Eating Behaviour Questionnaire Concurrent Version Questionna | Instrument Test Code | HIGH |  |
| BEBQ01TN | Baby Eating Behaviour Questionnaire Concurrent Version Questionna | Instrument Test Name | HIGH |  |
| BEBQ02TC | Baby Eating Behaviour Questionnaire Retrospective Version Questio | Instrument Test Code | HIGH |  |
| BEBQ02TN | Baby Eating Behaviour Questionnaire Retrospective Version Questio | Instrument Test Name | HIGH |  |
| BARS01TC | Barnes Akathisia Rating Scale Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| BARS01TN | Barnes Akathisia Rating Scale Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| BDI01TC | Baseline Dyspnea Index Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| BDI01TN | Baseline Dyspnea Index Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| ISBDAGT | Binding Agent for Immunogenicity Tests | Microbiology/Immunology | HIGH |  |
| BSTESTCD | Biospecimen Characteristics Test Code | Instrument Test Code | HIGH |  |
| BSTEST | Biospecimen Characteristics Test Name | Instrument Test Name | HIGH |  |
| BEDECOD | Biospecimen Events Dictionary Derived Term | Dictionary Reference | HIGH |  |
| BLCS01TC | Bladder Control Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| BLCS01TN | Bladder Control Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| BCR101TC | Borg CR10 Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| BCR101TN | Borg CR10 Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| BWCS01TC | Bowel Control Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| BWCS01TN | Bowel Control Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| BACS1TC | Brief Assessment of Cognition in Schizophrenia Functional Test Te | Instrument Test Code | HIGH |  |
| BACS1TN | Brief Assessment of Cognition in Schizophrenia Functional Test Te | Instrument Test Name | HIGH |  |
| BPI1TC | Brief Pain Inventory Questionnaire Test Code | Instrument Test Code | HIGH |  |
| BPI1TN | Brief Pain Inventory Questionnaire Test Name | Instrument Test Name | HIGH |  |
| BPI2TC | Brief Pain Inventory Short Form Questionnaire Test Code | Instrument Test Code | HIGH |  |
| BPI2TN | Brief Pain Inventory Short Form Questionnaire Test Name | Instrument Test Name | HIGH |  |
| BPRS01TC | Brief Psychiatric Rating Scale 1988 Version Clinical Classificati | Instrument Test Code | HIGH |  |
| BPRS01TN | Brief Psychiatric Rating Scale 1988 Version Clinical Classificati | Instrument Test Name | HIGH |  |
| BPRSA118OR | Brief Psychiatric Rating Scale-Anchored Clinical Classification O | Instrument Original Result | HIGH |  |
| BPRSA1SET1OR | Brief Psychiatric Rating Scale-Anchored Clinical Classification O | Instrument Original Result | HIGH |  |
| BPRSA1SET2OR | Brief Psychiatric Rating Scale-Anchored Clinical Classification O | Instrument Original Result | HIGH |  |
| BPRSA118STR | Brief Psychiatric Rating Scale-Anchored Clinical Classification S | Instrument Standardized Result | HIGH |  |
| BPRSA1SET1STR | Brief Psychiatric Rating Scale-Anchored Clinical Classification S | Instrument Standardized Result | HIGH |  |
| BPRSA1SET2STR | Brief Psychiatric Rating Scale-Anchored Clinical Classification S | Instrument Standardized Result | HIGH |  |
| BPRSA1TC | Brief Psychiatric Rating Scale-Anchored Clinical Classification T | Instrument Test Code | HIGH |  |
| BPRSA1TN | Brief Psychiatric Rating Scale-Anchored Clinical Classification T | Instrument Test Name | HIGH |  |
| BUERS1TC | Brooke Upper Extremity Rating Scale Clinical Classification Test  | Instrument Test Code | HIGH |  |
| BUERS1TN | Brooke Upper Extremity Rating Scale Clinical Classification Test  | Instrument Test Name | HIGH |  |
| CDFATSCD | CDAD Findings About Test Code | Instrument Test Code | HIGH |  |
| CDFATS | CDAD Findings About Test Name | Instrument Test Name | HIGH |  |
| CHIVC1TC | CDC Classification System for HIV-Infected Adults and Adolescents | Instrument Test Code | HIGH |  |
| CHIVC1TN | CDC Classification System for HIV-Infected Adults and Adolescents | Instrument Test Name | HIGH |  |
| CTAUGRS | CDISC Therapeutic Area User Guide Response | Trial Design | HIGH |  |
| CPFATSCD | COPD Findings About Test Code | Instrument Test Code | HIGH |  |
| CPFATS | COPD Findings About Test Name | Instrument Test Name | HIGH |  |
| C19FATCD | COVID-19 Findings About Test Code | Instrument Test Code | HIGH |  |
| C19FAT | COVID-19 Findings About Test Name | Instrument Test Name | HIGH |  |
| CCSGA101OR | Canadian Cardiovascular Society Grading Scale of Angina Pectoris  | Instrument Original Result | HIGH |  |
| CCSGA101STR | Canadian Cardiovascular Society Grading Scale of Angina Pectoris  | Instrument Standardized Result | HIGH |  |
| CCSGA1TC | Canadian Cardiovascular Society Grading of Angina Pectoris Clinic | Instrument Test Code | HIGH |  |
| CCSGA1TN | Canadian Cardiovascular Society Grading of Angina Pectoris Clinic | Instrument Test Name | HIGH |  |
| CVPRCIND | Cardiac Procedure Indication | Treatment Qualifier | HIGH |  |
| CRYDFMAN | Cardiac Rhythm Device Failure Manifestation | Device | HIGH |  |
| CVFARS | Cardiovascular Findings About Results | Observation Qualifier | HIGH |  |
| CVFATSCD | Cardiovascular Findings About Test Code | Instrument Test Code | HIGH |  |
| CVFATS | Cardiovascular Findings About Test Name | Instrument Test Name | HIGH |  |
| CVTESTCD | Cardiovascular Test Code | Instrument Test Code | HIGH |  |
| CVTEST | Cardiovascular Test Name | Instrument Test Name | HIGH |  |
| CASEFIND | Case Finding | Observation Qualifier | HIGH |  |
| CPCAT | Category for Cell Phenotyping | Domain Category | HIGH |  |
| CCCAT | Category of Clinical Classification | Domain Category | HIGH |  |
| DECAT | Category of Device Events | Domain Category | HIGH |  |
| DSCAT | Category of Disposition Event | Domain Category | HIGH |  |
| FTCAT | Category of Functional Test | Domain Category | HIGH |  |
| IECAT | Category of Inclusion/Exclusion | Domain Category | HIGH |  |
| IQCAT | Category of Ingredient Quantities by Component | Domain Category | HIGH |  |
| ONCRSCAT | Category of Oncology Response Assessment | Domain Category | HIGH |  |
| QSCAT | Category of Questionnaire | Domain Category | HIGH |  |
| PTCAT | Category of Tobacco Product Testing | Domain Category | HIGH |  |
| TOCAT | Category of Tobacco Products | Domain Category | HIGH |  |
| CPTESTCD | Cell Phenotyping Test Code | Instrument Test Code | HIGH |  |
| CPTEST | Cell Phenotyping Test Name | Instrument Test Name | HIGH |  |
| CELSTATE | Cell State Response | Observation Qualifier | HIGH |  |
| CPS0101OR | Child-Pugh Classification Clinical Classification ORRES for CPS01 | Instrument Original Result | HIGH |  |
| CPS0102OR | Child-Pugh Classification Clinical Classification ORRES for CPS01 | Instrument Original Result | HIGH |  |
| CPS0103OR | Child-Pugh Classification Clinical Classification ORRES for CPS01 | Instrument Original Result | HIGH |  |
| CPS0104OR | Child-Pugh Classification Clinical Classification ORRES for CPS01 | Instrument Original Result | HIGH |  |
| CPS0105AOR | Child-Pugh Classification Clinical Classification ORRES for CPS01 | Instrument Original Result | HIGH |  |
| CPS0105BOR | Child-Pugh Classification Clinical Classification ORRES for CPS01 | Instrument Original Result | HIGH |  |
| CPS0107OR | Child-Pugh Classification Clinical Classification ORRES for CPS01 | Instrument Original Result | HIGH |  |
| CPS0101STR | Child-Pugh Classification Clinical Classification STRESC for CPS0 | Instrument Standardized Result | HIGH |  |
| CPS0102STR | Child-Pugh Classification Clinical Classification STRESC for CPS0 | Instrument Standardized Result | HIGH |  |
| CPS0103STR | Child-Pugh Classification Clinical Classification STRESC for CPS0 | Instrument Standardized Result | HIGH |  |
| CPS0104STR | Child-Pugh Classification Clinical Classification STRESC for CPS0 | Instrument Standardized Result | HIGH |  |
| CPS0105ASTR | Child-Pugh Classification Clinical Classification STRESC for CPS0 | Instrument Standardized Result | HIGH |  |
| CPS0105BSTR | Child-Pugh Classification Clinical Classification STRESC for CPS0 | Instrument Standardized Result | HIGH |  |
| CPS0107STR | Child-Pugh Classification Clinical Classification STRESC for CPS0 | Instrument Standardized Result | HIGH |  |
| CPS01TC | Child-Pugh Classification Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| CPS01TN | Child-Pugh Classification Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| CDRS1TC | Children's Depression Rating Scale, Revised Clinical Classificati | Instrument Test Code | HIGH |  |
| CDRS1TN | Children's Depression Rating Scale, Revised Clinical Classificati | Instrument Test Name | HIGH |  |
| CRQ01TC | Chronic Respiratory Questionnaire Self-Administered Standardized  | Instrument Test Code | HIGH |  |
| CRQ01TN | Chronic Respiratory Questionnaire Self-Administered Standardized  | Instrument Test Name | HIGH |  |
| CRQ02TC | Chronic Respiratory Questionnaire Self-Administered Standardized  | Instrument Test Code | HIGH |  |
| CRQ02TN | Chronic Respiratory Questionnaire Self-Administered Standardized  | Instrument Test Name | HIGH |  |
| CCQ02TC | Clinical COPD Questionnaire 1 Week Version Questionnaire Test Cod | Instrument Test Code | HIGH |  |
| CCQ02TN | Clinical COPD Questionnaire 1 Week Version Questionnaire Test Nam | Instrument Test Name | HIGH |  |
| CCQ01TC | Clinical COPD Questionnaire 24 Hour Version Questionnaire Test Co | Instrument Test Code | HIGH |  |
| CCQ01TN | Clinical COPD Questionnaire 24 Hour Version Questionnaire Test Na | Instrument Test Name | HIGH |  |
| CDR01TC | Clinical Dementia Rating Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| CDR01TN | Clinical Dementia Rating Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| CGI02TC | Clinical Global Impression Generic Modification Version Questionn | Instrument Test Code | HIGH |  |
| CGI02TN | Clinical Global Impression Generic Modification Version Questionn | Instrument Test Name | HIGH |  |
| COWS1TC | Clinical Opiate Withdrawal Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| COWS1TN | Clinical Opiate Withdrawal Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| CLINSTRS | Clinical Status of Disease Response | Disposition | HIGH |  |
| CAP01TC | Clinician-Administered PTSD Scale (Current) DSM-5 With DSM IV Sco | Instrument Test Code | HIGH |  |
| CAP01TN | Clinician-Administered PTSD Scale (Current) DSM-5 With DSM IV Sco | Instrument Test Name | HIGH |  |
| COLSTYP | Collected Summarized Value Type Response | Observation Qualifier | HIGH |  |
| CSS05TC | Columbia-Suicide Severity Rating Scale Already Enrolled Subjects  | Instrument Test Code | HIGH |  |
| CSS05TN | Columbia-Suicide Severity Rating Scale Already Enrolled Subjects  | Instrument Test Name | HIGH |  |
| CSS01TC | Columbia-Suicide Severity Rating Scale Baseline Questionnaire Tes | Instrument Test Code | HIGH |  |
| CSS01TN | Columbia-Suicide Severity Rating Scale Baseline Questionnaire Tes | Instrument Test Name | HIGH |  |
| CSS03TC | Columbia-Suicide Severity Rating Scale Baseline/Screening Version | Instrument Test Code | HIGH |  |
| CSS03TN | Columbia-Suicide Severity Rating Scale Baseline/Screening Version | Instrument Test Name | HIGH |  |
| CSS04TC | Columbia-Suicide Severity Rating Scale Baseline/Screening Version | Instrument Test Code | HIGH |  |
| CSS04TN | Columbia-Suicide Severity Rating Scale Baseline/Screening Version | Instrument Test Name | HIGH |  |
| CSS06TC | Columbia-Suicide Severity Rating Scale Children's Baseline Questi | Instrument Test Code | HIGH |  |
| CSS06TN | Columbia-Suicide Severity Rating Scale Children's Baseline Questi | Instrument Test Name | HIGH |  |
| CSS07TC | Columbia-Suicide Severity Rating Scale Children's Baseline/Screen | Instrument Test Code | HIGH |  |
| CSS07TN | Columbia-Suicide Severity Rating Scale Children's Baseline/Screen | Instrument Test Name | HIGH |  |
| CSS08TC | Columbia-Suicide Severity Rating Scale Children's Since Last Visi | Instrument Test Code | HIGH |  |
| CSS08TN | Columbia-Suicide Severity Rating Scale Children's Since Last Visi | Instrument Test Name | HIGH |  |
| CSS11TC | Columbia-Suicide Severity Rating Scale Lifetime/Recent Version Qu | Instrument Test Code | HIGH |  |
| CSS11TN | Columbia-Suicide Severity Rating Scale Lifetime/Recent Version Qu | Instrument Test Name | HIGH |  |
| CSS10TC | Columbia-Suicide Severity Rating Scale Pediatric/Cognitively Impa | Instrument Test Code | HIGH |  |
| CSS10TN | Columbia-Suicide Severity Rating Scale Pediatric/Cognitively Impa | Instrument Test Name | HIGH |  |
| CSS09TC | Columbia-Suicide Severity Rating Scale Screening Questionnaire Te | Instrument Test Code | HIGH |  |
| CSS09TN | Columbia-Suicide Severity Rating Scale Screening Questionnaire Te | Instrument Test Name | HIGH |  |
| CSS02TC | Columbia-Suicide Severity Rating Scale Since Last Visit Questionn | Instrument Test Code | HIGH |  |
| CSS02TN | Columbia-Suicide Severity Rating Scale Since Last Visit Questionn | Instrument Test Name | HIGH |  |
| CES0101OR | Combat Exposure Scale Questionnaire ORRES for CES0101 TN/TC | Instrument Original Result | HIGH |  |
| CES0102OR | Combat Exposure Scale Questionnaire ORRES for CES0102 TN/TC | Instrument Original Result | HIGH |  |
| CES0103OR | Combat Exposure Scale Questionnaire ORRES for CES0103 TN/TC | Instrument Original Result | HIGH |  |
| CES0104OR | Combat Exposure Scale Questionnaire ORRES for CES0104 TN/TC | Instrument Original Result | HIGH |  |
| CES0105T07OR | Combat Exposure Scale Questionnaire ORRES for CES0105 Through CES | Instrument Original Result | HIGH |  |
| CES0101STR | Combat Exposure Scale Questionnaire STRESC for CES0101 TN/TC | Instrument Standardized Result | HIGH |  |
| CES0102STR | Combat Exposure Scale Questionnaire STRESC for CES0102 TN/TC | Instrument Standardized Result | HIGH |  |
| CES0103STR | Combat Exposure Scale Questionnaire STRESC for CES0103 TN/TC | Instrument Standardized Result | HIGH |  |
| CES0104STR | Combat Exposure Scale Questionnaire STRESC for CES0104 TN/TC | Instrument Standardized Result | HIGH |  |
| CES0105T07STR | Combat Exposure Scale Questionnaire STRESC for CES0105 Through CE | Instrument Standardized Result | HIGH |  |
| CES01TC | Combat Exposure Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| CES01TN | Combat Exposure Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| CBS01TC | Comfort Behavior Scale Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| CBS01TN | Comfort Behavior Scale Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| CMSPSTAT | Commercial Sponsor Status Response | Observation Qualifier | HIGH |  |
| NCOMPLT | Completion/Reason for Non-Completion | Disposition | HIGH |  |
| CSTATE | Consciousness State | Observation Qualifier | HIGH |  |
| CCINVTYP | Contact Case Investigation Contact Type | Role/Relationship | HIGH |  |
| CONROL | Contact Role for Clinical Study | Role/Relationship | HIGH |  |
| TCNTRL | Control Type Response | Trial Design | HIGH |  |
| COWAT1TC | Controlled Oral Word Association Test Functional Test Test Code | Instrument Test Code | HIGH |  |
| COWAT1TN | Controlled Oral Word Association Test Functional Test Test Name | Instrument Test Name | HIGH |  |
| CADPRSN | Coronary Artery Disease Presentation | Clinical Classification | HIGH |  |
| CADRISK | Coronary Artery Disease Risk | Clinical Classification | HIGH |  |
| CADSYMP | Coronary Artery Disease Symptoms | Clinical Classification | HIGH |  |
| CADG01TC | Coronary Artery Dissection NHLBI Grade Clinical Classification Te | Instrument Test Code | HIGH |  |
| CADG01TN | Coronary Artery Dissection NHLBI Grade Clinical Classification Te | Instrument Test Name | HIGH |  |
| CADGRS | Coronary Artery Dissection NHLBI Grade Responses | Clinical Classification | HIGH |  |
| CARTDOM | Coronary Artery Dominance | Clinical Classification | HIGH |  |
| TIMG01TC | Coronary Thrombus TIMI Grade Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| TIMG01TN | Coronary Thrombus TIMI Grade Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| CTTIMIRS | Coronary Thrombus TIMI Grade Responses | Clinical Classification | HIGH |  |
| CVSLDEXT | Coronary Vessel Disease Extent | Clinical Classification | HIGH |  |
| COVI01TC | Covi Anxiety Scale Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| COVI01TN | Covi Anxiety Scale Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| CHSF1TC | Craig Handicap Assessment and Reporting Technique - Short Form In | Instrument Test Code | HIGH |  |
| CHSF1TN | Craig Handicap Assessment and Reporting Technique - Short Form In | Instrument Test Name | HIGH |  |
| CHSF2TC | Craig Handicap Assessment and Reporting Technique - Short Form Pa | Instrument Test Code | HIGH |  |
| CHSF2TN | Craig Handicap Assessment and Reporting Technique - Short Form Pa | Instrument Test Name | HIGH |  |
| CDAI01TC | Crohn's Disease Activity Index Version 1 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| CDAI01TN | Crohn's Disease Activity Index Version 1 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| CRFATSCD | Crohn's Disease Findings About Test Code | Instrument Test Code | HIGH |  |
| CRFATS | Crohn's Disease Findings About Test Name | Instrument Test Name | HIGH |  |
| CLTMDTYP | Culture Medium Type | Specimen | HIGH |  |
| COMM1TC | Current Opioid Misuse Measure Questionnaire Test Code | Instrument Test Code | HIGH |  |
| COMM1TN | Current Opioid Misuse Measure Questionnaire Test Name | Instrument Test Name | HIGH |  |
| DRRI1TC | Deployment Risk and Resilience Inventory-2 Questionnaire Test Cod | Instrument Test Code | HIGH |  |
| DRRI1TN | Deployment Risk and Resilience Inventory-2 Questionnaire Test Nam | Instrument Test Name | HIGH |  |
| DLQI1TC | Dermatology Life Quality Index Questionnaire Test Code | Instrument Test Code | HIGH |  |
| DLQI1TN | Dermatology Life Quality Index Questionnaire Test Name | Instrument Test Name | HIGH |  |
| DEACNDEV | Device Events Action Taken with Device | Adverse Event Qualifier | HIGH |  |
| DIPARM | Device Identifier Long Name | Device | HIGH |  |
| DIPARMCD | Device Identifier Short Name | Device | HIGH |  |
| DOTESTCD | Device Properties Test Code | Instrument Test Code | HIGH |  |
| DOTEST | Device Properties Test Name | Instrument Test Name | HIGH |  |
| DTDECOD | Device Tracking and Disposition Event Dictionary Derived Term | Disposition | HIGH |  |
| DURS | Device-In-Use Response | Device | HIGH |  |
| DUTESTCD | Device-In-Use Test Code | Instrument Test Code | HIGH |  |
| DUTEST | Device-In-Use Test Name | Instrument Test Name | HIGH |  |
| DDS01TC | Diabetes Distress Scale for Adults with Type 1 Diabetes Questionn | Instrument Test Code | HIGH |  |
| DDS01TN | Diabetes Distress Scale for Adults with Type 1 Diabetes Questionn | Instrument Test Name | HIGH |  |
| DDS02TC | Diabetes Distress Scale for Parents of Teens with Type 1 Diabetes | Instrument Test Code | HIGH |  |
| DDS02TN | Diabetes Distress Scale for Parents of Teens with Type 1 Diabetes | Instrument Test Name | HIGH |  |
| DDS03TC | Diabetes Distress Scale for Partners of Adults with Type 1 Diabet | Instrument Test Code | HIGH |  |
| DDS03TN | Diabetes Distress Scale for Partners of Adults with Type 1 Diabet | Instrument Test Name | HIGH |  |
| DIABTHPY | Diabetes Therapy | Treatment Qualifier | HIGH |  |
| DKFATSCD | Diabetic Kidney Disease Findings About Test Code | Instrument Test Code | HIGH |  |
| DKFATS | Diabetic Kidney Disease Findings About Test Name | Instrument Test Name | HIGH |  |
| DIBC01TC | Diary for Irritable Bowel Syndrome Symptoms-Constipation v1.0 Que | Instrument Test Code | HIGH |  |
| DIBC01TN | Diary for Irritable Bowel Syndrome Symptoms-Constipation v1.0 Que | Instrument Test Name | HIGH |  |
| DICTNAM | Dictionary Name | Dictionary Reference | HIGH |  |
| DIR | Directionality | Anatomical Qualifier | HIGH |  |
| DAD01TC | Disability Assessment for Dementia Questionnaire Test Code | Instrument Test Code | HIGH |  |
| DAD01TN | Disability Assessment for Dementia Questionnaire Test Name | Instrument Test Name | HIGH |  |
| DRS01TC | Disability Rating Scale Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| DRS01TN | Disability Rating Scale Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| DISCHDX | Discharge Disposition | Disposition | HIGH |  |
| DSSOUT | Disease Outcome | Observation Qualifier | HIGH |  |
| DSPRTYP | Disease Presentation Type | Observation Qualifier | HIGH |  |
| DS01TC | Disease Steps Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| DS01TN | Disease Steps Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| FRM | Dosage Form | Treatment Qualifier | HIGH |  |
| DATESTCD | Drug Accountability Test Code | Instrument Test Code | HIGH |  |
| DATEST | Drug Accountability Test Name | Instrument Test Name | HIGH |  |
| DRSTAT | Drug Resistance Status | Treatment Qualifier | HIGH |  |
| DMFATSCD | Duchenne Muscular Dystrophy Findings About Test Code | Instrument Test Code | HIGH |  |
| DMFATS | Duchenne Muscular Dystrophy Findings About Test Name | Instrument Test Name | HIGH |  |
| EGANMET | ECG Analysis Method | Method | HIGH |  |
| EGLEAD | ECG Lead | ECG Findings | HIGH |  |
| EGRDMETH | ECG Read Method Response | Method | HIGH |  |
| EGSTRESC | ECG Result | ECG Findings | HIGH |  |
| TWOFFMTH | ECG T Wave Offset Method Response | Method | HIGH |  |
| EGTESTCD | ECG Test Code | Instrument Test Code | HIGH |  |
| EGMETHOD | ECG Test Method | Method | HIGH |  |
| EGTEST | ECG Test Name | Instrument Test Name | HIGH |  |
| ECOG101OR | Eastern Cooperative Oncology Group Performance Status Clinical Cl | Instrument Original Result | HIGH |  |
| ECOG101STR | Eastern Cooperative Oncology Group Performance Status Clinical Cl | Instrument Standardized Result | HIGH |  |
| ECOG1TC | Eastern Cooperative Oncology Group Performance Status Clinical Cl | Instrument Test Code | HIGH |  |
| ECOG1TN | Eastern Cooperative Oncology Group Performance Status Clinical Cl | Instrument Test Name | HIGH |  |
| EBFATSCD | Ebola Virus Findings About Test Code | Instrument Test Code | HIGH |  |
| EBFATS | Ebola Virus Findings About Test Name | Instrument Test Name | HIGH |  |
| EPDS01TC | Edinburgh Postnatal Depression Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| EPDS01TN | Edinburgh Postnatal Depression Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ETRP01TC | Emory Treatment Resistance Interview for PTSD Clinical Classifica | Instrument Test Code | HIGH |  |
| ETRP01TN | Emory Treatment Resistance Interview for PTSD Clinical Classifica | Instrument Test Name | HIGH |  |
| EMO1TC | Emotion Recognition Functional Test Test Code | Instrument Test Code | HIGH |  |
| EMO1TN | Emotion Recognition Functional Test Test Name | Instrument Test Name | HIGH |  |
| EMPSTAT | Employment Status | Demographic | HIGH |  |
| SETTING | Environmental Setting | Observation Qualifier | HIGH |  |
| ESPARMCD | Environmental Storage Conditions Parameter Code | Parameter Name-Code | HIGH |  |
| ESPARM | Environmental Storage Conditions Parameter Name | Parameter Name-Code | HIGH |  |
| EPOCH | Epoch | Trial Design | HIGH |  |
| ESS01TC | Epworth Sleepiness Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| ESS01TN | Epworth Sleepiness Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ETHNIC | Ethnic Group | Demographic | HIGH |  |
| ETHNICC | Ethnicity As Collected | Demographic | HIGH |  |
| EOR06TC | European Organisation for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR06TN | European Organisation for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR01TC | European Organisation for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR01TN | European Organisation for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR18TC | European Organisation for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR18TN | European Organisation for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR02TC | European Organisation for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR02TN | European Organisation for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR30TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR30TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR03TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR03TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR35TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR35TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR24TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR24TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR29TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR29TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR12TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR12TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR21TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR21TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR36TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR36TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR17TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR17TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR19TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR19TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR28TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR28TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EOR20TC | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Code | HIGH |  |
| EOR20TN | European Organization for the Research and Treatment of Cancer Qu | Instrument Test Name | HIGH |  |
| EQ5D02TC | European Quality of Life Five Dimension Five Level Scale Question | Instrument Test Code | HIGH |  |
| EQ5D02TN | European Quality of Life Five Dimension Five Level Scale Question | Instrument Test Name | HIGH |  |
| EQ5D01TC | European Quality of Life Five Dimension Three Level Scale Questio | Instrument Test Code | HIGH |  |
| EQ5D01TN | European Quality of Life Five Dimension Three Level Scale Questio | Instrument Test Name | HIGH |  |
| EVAL | Evaluator | Role/Relationship | HIGH |  |
| EXACT1TC | Exacerbations of Chronic Pulmonary Disease Tool Patient-Reported  | Instrument Test Code | HIGH |  |
| EXACT1TN | Exacerbations of Chronic Pulmonary Disease Tool Patient-Reported  | Instrument Test Name | HIGH |  |
| ED1TC | Expanded Disability Rating Scale - Postacute Interview Caregiver  | Instrument Test Code | HIGH |  |
| ED1TN | Expanded Disability Rating Scale - Postacute Interview Caregiver  | Instrument Test Name | HIGH |  |
| ED2TC | Expanded Disability Rating Scale - Postacute Interview Survivor V | Instrument Test Code | HIGH |  |
| ED2TN | Expanded Disability Rating Scale - Postacute Interview Survivor V | Instrument Test Name | HIGH |  |
| GOSE1TC | Extended Glasgow Outcome Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| GOSE1TN | Extended Glasgow Outcome Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ESRSA1TC | Extrapyramidal Symptom Rating Scale-Abbreviated Clinical Classifi | Instrument Test Code | HIGH |  |
| ESRSA1TN | Extrapyramidal Symptom Rating Scale-Abbreviated Clinical Classifi | Instrument Test Name | HIGH |  |
| FDATSRS | FDA Technical Specification Response | Trial Design | HIGH |  |
| FPSR1TC | Faces Pain Scale - Revised Questionnaire Test Code | Instrument Test Code | HIGH |  |
| FPSR1TN | Faces Pain Scale - Revised Questionnaire Test Name | Instrument Test Name | HIGH |  |
| FTCD01TC | Fagerstrom Test for Cigarette Dependence Questionnaire Test Code | Instrument Test Code | HIGH |  |
| FTCD01TN | Fagerstrom Test for Cigarette Dependence Questionnaire Test Name | Instrument Test Name | HIGH |  |
| FES01TC | Falls Efficacy Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| FES01TN | Falls Efficacy Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| FSS01TC | Fatigue Severity Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| FSS01TN | Fatigue Severity Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| FATESTCD | Findings About Test Code | Instrument Test Code | HIGH |  |
| FATEST | Findings About Test Name | Instrument Test Name | HIGH |  |
| SKINCLAS | Fitzpatrick Skin Classification Response | Clinical Classification | HIGH |  |
| FCVD1TC | Framingham Heart Study Cardiovascular Disease 10-Year Risk Score  | Instrument Test Code | HIGH |  |
| FCVD1TN | Framingham Heart Study Cardiovascular Disease 10-Year Risk Score  | Instrument Test Name | HIGH |  |
| FREQ | Frequency | Treatment Qualifier | HIGH |  |
| FAQ01TC | Functional Activities Questionnaire Clinical Classification Test  | Instrument Test Code | HIGH |  |
| FAQ01TN | Functional Activities Questionnaire Clinical Classification Test  | Instrument Test Name | HIGH |  |
| FAQNA1TC | Functional Assessment Questionnaire-NACC UDS V2.0 Clinical Classi | Instrument Test Code | HIGH |  |
| FAQNA1TN | Functional Assessment Questionnaire-NACC UDS V2.0 Clinical Classi | Instrument Test Name | HIGH |  |
| FASNA1TC | Functional Assessment Scale-NACC UDS Version 3.0 Clinical Classif | Instrument Test Code | HIGH |  |
| FASNA1TN | Functional Assessment Scale-NACC UDS Version 3.0 Clinical Classif | Instrument Test Name | HIGH |  |
| FAC065TC | Functional Assessment of Anorexia/Cachexia Treatment Version 4 Qu | Instrument Test Code | HIGH |  |
| FAC065TN | Functional Assessment of Anorexia/Cachexia Treatment Version 4 Qu | Instrument Test Name | HIGH |  |
| FAC062TC | Functional Assessment of Cancer Therapy-Biologic Response Modifie | Instrument Test Code | HIGH |  |
| FAC062TN | Functional Assessment of Cancer Therapy-Biologic Response Modifie | Instrument Test Name | HIGH |  |
| FAC006TC | Functional Assessment of Cancer Therapy-Bladder Version 4 Questio | Instrument Test Code | HIGH |  |
| FAC006TN | Functional Assessment of Cancer Therapy-Bladder Version 4 Questio | Instrument Test Name | HIGH |  |
| FAC061TC | Functional Assessment of Cancer Therapy-Bone Marrow Transplant Ve | Instrument Test Code | HIGH |  |
| FAC061TN | Functional Assessment of Cancer Therapy-Bone Marrow Transplant Ve | Instrument Test Name | HIGH |  |
| FAC074TC | Functional Assessment of Cancer Therapy-Bone Pain Version 4 Quest | Instrument Test Code | HIGH |  |
| FAC074TN | Functional Assessment of Cancer Therapy-Bone Pain Version 4 Quest | Instrument Test Name | HIGH |  |
| FAC029TC | Functional Assessment of Cancer Therapy-Brain Symptom Index Quest | Instrument Test Code | HIGH |  |
| FAC029TN | Functional Assessment of Cancer Therapy-Brain Symptom Index Quest | Instrument Test Name | HIGH |  |
| FAC005TC | Functional Assessment of Cancer Therapy-Breast Version 4 Question | Instrument Test Code | HIGH |  |
| FAC005TN | Functional Assessment of Cancer Therapy-Breast Version 4 Question | Instrument Test Name | HIGH |  |
| FAC075TC | Functional Assessment of Cancer Therapy-Cognitive Function Versio | Instrument Test Code | HIGH |  |
| FAC075TN | Functional Assessment of Cancer Therapy-Cognitive Function Versio | Instrument Test Name | HIGH |  |
| FAC008TC | Functional Assessment of Cancer Therapy-Colorectal Version 4 Ques | Instrument Test Code | HIGH |  |
| FAC008TN | Functional Assessment of Cancer Therapy-Colorectal Version 4 Ques | Instrument Test Name | HIGH |  |
| FAC015TC | Functional Assessment of Cancer Therapy-Hepatobiliary Version 4 Q | Instrument Test Code | HIGH |  |
| FAC015TN | Functional Assessment of Cancer Therapy-Hepatobiliary Version 4 Q | Instrument Test Name | HIGH |  |
| FAC039TC | Functional Assessment of Cancer Therapy-Kidney Symptom Index-15 Q | Instrument Test Code | HIGH |  |
| FAC039TN | Functional Assessment of Cancer Therapy-Kidney Symptom Index-15 Q | Instrument Test Name | HIGH |  |
| FAC041TC | Functional Assessment of Cancer Therapy-Kidney Symptom Index-Dise | Instrument Test Code | HIGH |  |
| FAC041TN | Functional Assessment of Cancer Therapy-Kidney Symptom Index-Dise | Instrument Test Name | HIGH |  |
| FAC017TC | Functional Assessment of Cancer Therapy-Leukemia Version 4 Questi | Instrument Test Code | HIGH |  |
| FAC017TN | Functional Assessment of Cancer Therapy-Leukemia Version 4 Questi | Instrument Test Name | HIGH |  |
| FAC043TC | Functional Assessment of Cancer Therapy-Lung Symptom Index Questi | Instrument Test Code | HIGH |  |
| FAC043TN | Functional Assessment of Cancer Therapy-Lung Symptom Index Questi | Instrument Test Name | HIGH |  |
| FAC016TC | Functional Assessment of Cancer Therapy-Lung Version 4 Questionna | Instrument Test Code | HIGH |  |
| FAC016TN | Functional Assessment of Cancer Therapy-Lung Version 4 Questionna | Instrument Test Name | HIGH |  |
| FAC018TC | Functional Assessment of Cancer Therapy-Lymphoma Version 4 Questi | Instrument Test Code | HIGH |  |
| FAC018TN | Functional Assessment of Cancer Therapy-Lymphoma Version 4 Questi | Instrument Test Name | HIGH |  |
| FAC019TC | Functional Assessment of Cancer Therapy-Melanoma Version 4 Questi | Instrument Test Code | HIGH |  |
| FAC019TN | Functional Assessment of Cancer Therapy-Melanoma Version 4 Questi | Instrument Test Name | HIGH |  |
| FAC049TC | Functional Assessment of Cancer Therapy-Ovarian Symptom Index Que | Instrument Test Code | HIGH |  |
| FAC049TN | Functional Assessment of Cancer Therapy-Ovarian Symptom Index Que | Instrument Test Name | HIGH |  |
| FAC063TC | Functional Assessment of Cancer Therapy-Taxane Version 4 Question | Instrument Test Code | HIGH |  |
| FAC063TN | Functional Assessment of Cancer Therapy-Taxane Version 4 Question | Instrument Test Name | HIGH |  |
| FAC102TC | Functional Assessment of Cancer Therapy/Gynecologic Oncology Grou | Instrument Test Code | HIGH |  |
| FAC102TN | Functional Assessment of Cancer Therapy/Gynecologic Oncology Grou | Instrument Test Name | HIGH |  |
| FAC057TC | Functional Assessment of Cancer Therapy/Gynecologic Oncology Grou | Instrument Test Code | HIGH |  |
| FAC057TN | Functional Assessment of Cancer Therapy/Gynecologic Oncology Grou | Instrument Test Name | HIGH |  |
| FAC084TC | Functional Assessment of Chronic Illness Therapy-Dyspnea 10 Item  | Instrument Test Code | HIGH |  |
| FAC084TN | Functional Assessment of Chronic Illness Therapy-Dyspnea 10 Item  | Instrument Test Name | HIGH |  |
| FAC100TC | Functional Assessment of Chronic Illness Therapy-Dyspnea Scale 33 | Instrument Test Code | HIGH |  |
| FAC100TN | Functional Assessment of Chronic Illness Therapy-Dyspnea Scale 33 | Instrument Test Name | HIGH |  |
| FAC070TC | Functional Assessment of Chronic Illness Therapy-Fatigue 13-Item  | Instrument Test Code | HIGH |  |
| FAC070TN | Functional Assessment of Chronic Illness Therapy-Fatigue 13-Item  | Instrument Test Name | HIGH |  |
| FAC071TC | Functional Assessment of Chronic Illness Therapy-Fatigue Version  | Instrument Test Code | HIGH |  |
| FAC071TN | Functional Assessment of Chronic Illness Therapy-Fatigue Version  | Instrument Test Name | HIGH |  |
| FAC101TC | Functional Assessment of Chronic Illness Therapy-Item GP5 Version | Instrument Test Code | HIGH |  |
| FAC101TN | Functional Assessment of Chronic Illness Therapy-Item GP5 Version | Instrument Test Name | HIGH |  |
| FSILTC | Functional Assessment of Chronic Illness Therapy-Searchable Item  | Instrument Test Code | HIGH |  |
| FSILTN | Functional Assessment of Chronic Illness Therapy-Searchable Item  | Instrument Test Name | HIGH |  |
| FSLPTC | Functional Assessment of Chronic Illness Therapy-Searchable Item  | Instrument Test Code | HIGH |  |
| FSLPTN | Functional Assessment of Chronic Illness Therapy-Searchable Item  | Instrument Test Name | HIGH |  |
| FAMS01TC | Functional Assessment of Multiple Sclerosis Version 4 Questionnai | Instrument Test Code | HIGH |  |
| FAMS01TN | Functional Assessment of Multiple Sclerosis Version 4 Questionnai | Instrument Test Name | HIGH |  |
| GASTROCD | Gastrointestinal Test Code | Instrument Test Code | HIGH |  |
| GASTRO | Gastrointestinal Test Name | Instrument Test Name | HIGH |  |
| GENIDENT | Gender Identity Response | Demographic | HIGH |  |
| GCGI01TC | General Clinical Global Impressions Questionnaire Test Code | Instrument Test Code | HIGH |  |
| GCGI01TN | General Clinical Global Impressions Questionnaire Test Name | Instrument Test Name | HIGH |  |
| GAD01TC | Generalized Anxiety Disorder - 7 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| GAD01TN | Generalized Anxiety Disorder - 7 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| GAD02TC | Generalized Anxiety Disorder - 7 Version 2 Questionnaire Test Cod | Instrument Test Code | HIGH |  |
| GAD02TN | Generalized Anxiety Disorder - 7 Version 2 Questionnaire Test Nam | Instrument Test Name | HIGH |  |
| GENSMP | Genetic Sample Type | Specimen | HIGH |  |
| GFANMET | Genomic Findings Analytical Method Calculation Formula | Method | HIGH |  |
| GFTESTCD | Genomic Findings Test Code | Instrument Test Code | HIGH |  |
| GFTSDTL | Genomic Findings Test Detail | Genomic | HIGH |  |
| GFTEST | Genomic Findings Test Name | Instrument Test Name | HIGH |  |
| INHERTGF | Genomic Inheritability Type Response | Genomic | HIGH |  |
| SYMTYPGF | Genomic Symbol Type Response | Genomic | HIGH |  |
| GDS01TC | Geriatric Depression Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| GDS01TN | Geriatric Depression Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| GDS02TC | Geriatric Depression Scale Short Form Questionnaire Test Code | Instrument Test Code | HIGH |  |
| GDS02TN | Geriatric Depression Scale Short Form Questionnaire Test Name | Instrument Test Name | HIGH |  |
| GCS01TC | Glasgow Coma Scale NINDS Version 1.0 Clinical Classification Test | Instrument Test Code | HIGH |  |
| GCS01TN | Glasgow Coma Scale NINDS Version 1.0 Clinical Classification Test | Instrument Test Name | HIGH |  |
| GRAFTTYP | Graft Type | Device | HIGH |  |
| HSB01TC | HAS-BLED Bleeding Risk Score Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| HSB01TN | HAS-BLED Bleeding Risk Score Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| HAMA101T14OR | Hamilton Anxiety Rating Scale Clinical Classification ORRES for H | Instrument Original Result | HIGH |  |
| HAMA101T14STR | Hamilton Anxiety Rating Scale Clinical Classification STRESC for  | Instrument Standardized Result | HIGH |  |
| HAMA1TC | Hamilton Anxiety Rating Scale Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| HAMA1TN | Hamilton Anxiety Rating Scale Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| HAMD1TC | Hamilton Depression Rating Scale - 17 Item Clinical Classificatio | Instrument Test Code | HIGH |  |
| HAMD1TN | Hamilton Depression Rating Scale - 17 Item Clinical Classificatio | Instrument Test Name | HIGH |  |
| HAMD3TC | Hamilton Depression Rating Scale - 24 Item Clinical Classificatio | Instrument Test Code | HIGH |  |
| HAMD3TN | Hamilton Depression Rating Scale - 24 Item Clinical Classificatio | Instrument Test Name | HIGH |  |
| HAMD4TC | Hamilton Depression Rating Scale - 6 Clinician Version Clinical C | Instrument Test Code | HIGH |  |
| HAMD4TN | Hamilton Depression Rating Scale - 6 Clinician Version Clinical C | Instrument Test Name | HIGH |  |
| HAMDS1TC | Hamilton Depression Rating Scale - 6 Self-Report Questionnaire Te | Instrument Test Code | HIGH |  |
| HAMDS1TN | Hamilton Depression Rating Scale - 6 Self-Report Questionnaire Te | Instrument Test Name | HIGH |  |
| HAMD2TC | Hamilton Depression Rating Scale 21-Item Clinical Classification  | Instrument Test Code | HIGH |  |
| HAMD2TN | Hamilton Depression Rating Scale 21-Item Clinical Classification  | Instrument Test Name | HIGH |  |
| HBI0101OR | Harvey-Bradshaw Index Clinical Classification ORRES for HBI0101 T | Instrument Original Result | HIGH |  |
| HBI0102OR | Harvey-Bradshaw Index Clinical Classification ORRES for HBI0102 T | Instrument Original Result | HIGH |  |
| HBI0104OR | Harvey-Bradshaw Index Clinical Classification ORRES for HBI0104 T | Instrument Original Result | HIGH |  |
| HBI0105AT05HOR | Harvey-Bradshaw Index Clinical Classification ORRES for HBI0105A  | Instrument Original Result | HIGH |  |
| HBI0101STR | Harvey-Bradshaw Index Clinical Classification STRESC for HBI0101  | Instrument Standardized Result | HIGH |  |
| HBI0102STR | Harvey-Bradshaw Index Clinical Classification STRESC for HBI0102  | Instrument Standardized Result | HIGH |  |
| HBI0104STR | Harvey-Bradshaw Index Clinical Classification STRESC for HBI0104  | Instrument Standardized Result | HIGH |  |
| HBI0105AT05HSTR | Harvey-Bradshaw Index Clinical Classification STRESC for HBI0105A | Instrument Standardized Result | HIGH |  |
| HBI01TC | Harvey-Bradshaw Index Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| HBI01TN | Harvey-Bradshaw Index Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| HAI01TC | Hauser Ambulation Index Functional Test Test Code | Instrument Test Code | HIGH |  |
| HAI01TN | Hauser Ambulation Index Functional Test Test Name | Instrument Test Name | HIGH |  |
| HAQ01TC | Health Assessment Questionnaire Disability Index With Pain Visual | Instrument Test Code | HIGH |  |
| HAQ01TN | Health Assessment Questionnaire Disability Index With Pain Visual | Instrument Test Name | HIGH |  |
| HAQ02TC | Health Assessment Questionnaire Disability Index Without Pain Vis | Instrument Test Code | HIGH |  |
| HAQ02TN | Health Assessment Questionnaire Disability Index Without Pain Vis | Instrument Test Name | HIGH |  |
| HODECOD | Health Care Encounters Dictionary Derived Term | Dictionary Reference | HIGH |  |
| HEGRDMTH | Holter ECG Read Method Response | Method | HIGH |  |
| HESTRESC | Holter ECG Results | ECG Findings | HIGH |  |
| HETESTCD | Holter ECG Test Code | Instrument Test Code | HIGH |  |
| HETEST | Holter ECG Test Name | Instrument Test Name | HIGH |  |
| HADS01TC | Hospital Anxiety and Depression Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| HADS01TN | Hospital Anxiety and Depression Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| HDCAB1TC | Huntington's Disease Cognitive Assessment Battery Functional Test | Instrument Test Code | HIGH |  |
| HDCAB1TN | Huntington's Disease Cognitive Assessment Battery Functional Test | Instrument Test Name | HIGH |  |
| HCS01TC | Hypoglycemic Confidence Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| HCS01TN | Hypoglycemic Confidence Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ISTESTCD | Immunogenicity Specimen Assessments Test Code | Instrument Test Code | HIGH |  |
| ISTEST | Immunogenicity Specimen Assessments Test Name | Instrument Test Name | HIGH |  |
| ISFTSDTL | Immunogenicity Specimen Test Details | Specimen | HIGH |  |
| IVIS01TC | Impact of Visual Impairment Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| IVIS01TN | Impact of Visual Impairment Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| IGDCMPLX | Ingredient Complexity Response | Observation Qualifier | HIGH |  |
| INTEGUCD | Integumentary System Test Code | Instrument Test Code | HIGH |  |
| INTEGU | Integumentary System Test Name | Instrument Test Name | HIGH |  |
| IIEF01TC | International Index of Erectile Function Questionnaire Test Code | Instrument Test Code | HIGH |  |
| IIEF01TN | International Index of Erectile Function Questionnaire Test Name | Instrument Test Name | HIGH |  |
| IPAQ04TC | International Physical Activity Questionnaire (August 2002) Short | Instrument Test Code | HIGH |  |
| IPAQ04TN | International Physical Activity Questionnaire (August 2002) Short | Instrument Test Name | HIGH |  |
| IPAQ01TC | International Physical Activity Questionnaire (August 2002) Short | Instrument Test Code | HIGH |  |
| IPAQ01TN | International Physical Activity Questionnaire (August 2002) Short | Instrument Test Name | HIGH |  |
| IPAQ02TC | International Physical Activity Questionnaire (November 2002) Lon | Instrument Test Code | HIGH |  |
| IPAQ02TN | International Physical Activity Questionnaire (November 2002) Lon | Instrument Test Name | HIGH |  |
| IPAQ03TC | International Physical Activity Questionnaire (October 2002) Long | Instrument Test Code | HIGH |  |
| IPAQ03TN | International Physical Activity Questionnaire (October 2002) Long | Instrument Test Name | HIGH |  |
| IPS0101T06OR | International Prostate Symptom Score Questionnaire ORRES for IPS0 | Instrument Original Result | HIGH |  |
| IPS0107OR | International Prostate Symptom Score Questionnaire ORRES for IPS0 | Instrument Original Result | HIGH |  |
| IPS0109OR | International Prostate Symptom Score Questionnaire ORRES for IPS0 | Instrument Original Result | HIGH |  |
| IPS0101T06STR | International Prostate Symptom Score Questionnaire STRESC for IPS | Instrument Standardized Result | HIGH |  |
| IPS0107STR | International Prostate Symptom Score Questionnaire STRESC for IPS | Instrument Standardized Result | HIGH |  |
| IPS0109STR | International Prostate Symptom Score Questionnaire STRESC for IPS | Instrument Standardized Result | HIGH |  |
| IPS01TC | International Prostate Symptom Score Questionnaire Test Code | Instrument Test Code | HIGH |  |
| IPS01TN | International Prostate Symptom Score Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ISXDXRS | Intersex Diagnosis Indicator Response | Clinical Classification | HIGH |  |
| INTMODEL | Intervention Model Response | Trial Design | HIGH |  |
| INTTYPE | Intervention Type Response | Trial Design | HIGH |  |
| IDSC1TC | Inventory of Depressive Symptomatology Clinician-Rated Version Cl | Instrument Test Code | HIGH |  |
| IDSC1TN | Inventory of Depressive Symptomatology Clinician-Rated Version Cl | Instrument Test Name | HIGH |  |
| IDSR1TC | Inventory of Depressive Symptomatology Self-Report Version Questi | Instrument Test Code | HIGH |  |
| IDSR1TN | Inventory of Depressive Symptomatology Self-Report Version Questi | Instrument Test Name | HIGH |  |
| CRSR01TC | JFK Coma Recovery Scale-Revised Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| CRSR01TN | JFK Coma Recovery Scale-Revised Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| KPSS0101OR | Karnofsky Performance Status Scale Clinical Classification ORRES  | Instrument Original Result | HIGH |  |
| KPSS0101STR | Karnofsky Performance Status Scale Clinical Classification STRESC | Instrument Standardized Result | HIGH |  |
| KPSS01TC | Karnofsky Performance Status Scale Clinical Classification Test C | Instrument Test Code | HIGH |  |
| KPSS01TN | Karnofsky Performance Status Scale Clinical Classification Test N | Instrument Test Name | HIGH |  |
| KDIGO1TC | Kidney Disease Improving Global Outcomes Staging For Acute Kidney | Instrument Test Code | HIGH |  |
| KDIGO1TN | Kidney Disease Improving Global Outcomes Staging For Acute Kidney | Instrument Test Name | HIGH |  |
| KDQ1TC | Kidney Disease and Quality of Life-36 Version 1 Questionnaire Tes | Instrument Test Code | HIGH |  |
| KDQ1TN | Kidney Disease and Quality of Life-36 Version 1 Questionnaire Tes | Instrument Test Name | HIGH |  |
| KDPI01TC | Kidney Donor Profile Index Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| KDPI01TN | Kidney Donor Profile Index Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| KILLIPC | Killip Class Responses | Clinical Classification | HIGH |  |
| EDSS01TC | Kurtzke Expanded Disability Status Scale Clinical Classification  | Instrument Test Code | HIGH |  |
| EDSS01TN | Kurtzke Expanded Disability Status Scale Clinical Classification  | Instrument Test Name | HIGH |  |
| KFSS101OR | Kurtzke Functional System Scores Clinical Classification ORRES fo | Instrument Original Result | HIGH |  |
| KFSS102OR | Kurtzke Functional System Scores Clinical Classification ORRES fo | Instrument Original Result | HIGH |  |
| KFSS103OR | Kurtzke Functional System Scores Clinical Classification ORRES fo | Instrument Original Result | HIGH |  |
| KFSS104OR | Kurtzke Functional System Scores Clinical Classification ORRES fo | Instrument Original Result | HIGH |  |
| KFSS105OR | Kurtzke Functional System Scores Clinical Classification ORRES fo | Instrument Original Result | HIGH |  |
| KFSS106OR | Kurtzke Functional System Scores Clinical Classification ORRES fo | Instrument Original Result | HIGH |  |
| KFSS107OR | Kurtzke Functional System Scores Clinical Classification ORRES fo | Instrument Original Result | HIGH |  |
| KFSS108OR | Kurtzke Functional System Scores Clinical Classification ORRES fo | Instrument Original Result | HIGH |  |
| KFSS1SET1OR | Kurtzke Functional System Scores Clinical Classification ORRES th | Instrument Original Result | HIGH |  |
| KFSS101STR | Kurtzke Functional System Scores Clinical Classification STRESC f | Instrument Standardized Result | HIGH |  |
| KFSS102STR | Kurtzke Functional System Scores Clinical Classification STRESC f | Instrument Standardized Result | HIGH |  |
| KFSS103STR | Kurtzke Functional System Scores Clinical Classification STRESC f | Instrument Standardized Result | HIGH |  |
| KFSS104STR | Kurtzke Functional System Scores Clinical Classification STRESC f | Instrument Standardized Result | HIGH |  |
| KFSS105STR | Kurtzke Functional System Scores Clinical Classification STRESC f | Instrument Standardized Result | HIGH |  |
| KFSS106STR | Kurtzke Functional System Scores Clinical Classification STRESC f | Instrument Standardized Result | HIGH |  |
| KFSS107STR | Kurtzke Functional System Scores Clinical Classification STRESC f | Instrument Standardized Result | HIGH |  |
| KFSS108STR | Kurtzke Functional System Scores Clinical Classification STRESC f | Instrument Standardized Result | HIGH |  |
| KFSS1SET1STR | Kurtzke Functional System Scores Clinical Classification STRESC t | Instrument Standardized Result | HIGH |  |
| KFSS1TC | Kurtzke Functional Systems Scores Clinical Classification Test Co | Instrument Test Code | HIGH |  |
| KFSS1TN | Kurtzke Functional Systems Scores Clinical Classification Test Na | Instrument Test Name | HIGH |  |
| LBANMET | Laboratory Analytical Method Calculation Formula | Method | HIGH |  |
| LBTESTCD | Laboratory Test Code | Instrument Test Code | HIGH |  |
| LBTEST | Laboratory Test Name | Instrument Test Name | HIGH |  |
| LBSTRESC | Laboratory Test Standard Character Result | Observation Qualifier | HIGH |  |
| LPPSS1TC | Lansky Play-Performance Status Scale Clinical Classification Test | Instrument Test Code | HIGH |  |
| LPPSS1TN | Lansky Play-Performance Status Scale Clinical Classification Test | Instrument Test Name | HIGH |  |
| LAT | Laterality | Anatomical Qualifier | HIGH |  |
| LEADABN | Lead Abnormality | Device | HIGH |  |
| LEADSTAT | Lead Status | Disposition | HIGH |  |
| LVEFMRE | Left Ventricular Ejection Fraction Measurement Result | Observation Qualifier | HIGH |  |
| LSNCMPX | Lesion Complexity | Clinical Classification | HIGH |  |
| LEC01TC | Life Events Checklist for DSM-5 Standard Version Questionnaire Te | Instrument Test Code | HIGH |  |
| LEC01TN | Life Events Checklist for DSM-5 Standard Version Questionnaire Te | Instrument Test Name | HIGH |  |
| GRSTNLOC | Location of Most Severe Stenosis Within a Graft | Oncology Assessment | HIGH |  |
| DPETSCRS | London Deauville Criteria Point Scale 2014 | Clinical Classification | HIGH |  |
| LUFATSCD | Lung Cancer Findings About Test Code | Instrument Test Code | HIGH |  |
| LUFATS | Lung Cancer Findings About Test Name | Instrument Test Name | HIGH |  |
| MRFATSCD | Malaria Findings About Test Code | Instrument Test Code | HIGH |  |
| MRFATS | Malaria Findings About Test Name | Instrument Test Name | HIGH |  |
| MARISTAT | Marital Status Response | Demographic | HIGH |  |
| MPAI1TC | Mayo-Portland Adaptability Inventory-4 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| MPAI1TN | Mayo-Portland Adaptability Inventory-4 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| MCRCSPTM | Mechanical Circulatory Support Placement Timing | Clinical Classification | HIGH |  |
| MEDEVAL | Medical Evaluator Identifier | Role/Relationship | HIGH |  |
| MHEDTTYP | Medical History Event Date Type | Observation Qualifier | HIGH |  |
| MPSTATRS | Menopause Status Response | Disposition | HIGH |  |
| METHOD | Method | Method | HIGH |  |
| MNSI1TC | Michigan Neuropathy Screening Instrument Questionnaire Test Code | Instrument Test Code | HIGH |  |
| MNSI1TN | Michigan Neuropathy Screening Instrument Questionnaire Test Name | Instrument Test Name | HIGH |  |
| MCIDCERT | Microbial Identification Certainty | Clinical Classification | HIGH |  |
| MBFTSDTL | Microbiology Findings Test Details | Microbiology/Immunology | HIGH |  |
| MSTESTCD | Microbiology Susceptibility Test Code | Instrument Test Code | HIGH |  |
| MSTEST | Microbiology Susceptibility Test Name | Instrument Test Name | HIGH |  |
| MSSTRESC | Microbiology Susceptibility Test Standard Character Result | Microbiology/Immunology | HIGH |  |
| MBTESTCD | Microbiology Test Code | Instrument Test Code | HIGH |  |
| MBTEST | Microbiology Test Name | Instrument Test Name | HIGH |  |
| MICROORG | Microorganism | Microbiology/Immunology | HIGH |  |
| MIFTSDTL | Microscopic Findings Test Details | Microbiology/Immunology | HIGH |  |
| MMS2TC | Mini-Mental State Examination 2 Standard Version Functional Test  | Instrument Test Code | HIGH |  |
| MMS2TN | Mini-Mental State Examination 2 Standard Version Functional Test  | Instrument Test Name | HIGH |  |
| MMS1TC | Mini-Mental State Examination Functional Test Test Code | Instrument Test Code | HIGH |  |
| MMS1TN | Mini-Mental State Examination Functional Test Test Name | Instrument Test Name | HIGH |  |
| MTWSR101T15OR | Minnesota Tobacco Withdrawal Scale-Revised Clinical Classificatio | Instrument Original Result | HIGH |  |
| MTWSR101T15STR | Minnesota Tobacco Withdrawal Scale-Revised Clinical Classificatio | Instrument Standardized Result | HIGH |  |
| MTWSR1TC | Minnesota Tobacco Withdrawal Scale-Revised Clinical Classificatio | Instrument Test Code | HIGH |  |
| MTWSR1TN | Minnesota Tobacco Withdrawal Scale-Revised Clinical Classificatio | Instrument Test Name | HIGH |  |
| MODDLV | Mode of Delivery | Treatment Qualifier | HIGH |  |
| MODTRN | Mode of Disease Transmission | Observation Qualifier | HIGH |  |
| CNTMODE | Mode of Subject Contact | Role/Relationship | HIGH |  |
| MELD02TC | Model for End Stage Liver Disease - Serum Na 2008 Clinical Classi | Instrument Test Code | HIGH |  |
| MELD02TN | Model for End Stage Liver Disease - Serum Na 2008 Clinical Classi | Instrument Test Name | HIGH |  |
| MELD01TC | Model for End Stage Liver Disease Clinical Classification Test Co | Instrument Test Code | HIGH |  |
| MELD01TN | Model for End Stage Liver Disease Clinical Classification Test Na | Instrument Test Name | HIGH |  |
| MCEQ01TC | Modified Cigarette Evaluation Questionnaire Test Code | Instrument Test Code | HIGH |  |
| MCEQ01TN | Modified Cigarette Evaluation Questionnaire Test Name | Instrument Test Name | HIGH |  |
| MFIS01TC | Modified Fatigue Impact Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| MFIS01TN | Modified Fatigue Impact Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| MHIS01TC | Modified Hachinski Ischemic Scale-NACC Version Questionnaire Test | Instrument Test Code | HIGH |  |
| MHIS01TN | Modified Hachinski Ischemic Scale-NACC Version Questionnaire Test | Instrument Test Name | HIGH |  |
| MMRC01TC | Modified Medical Research Council Dyspnea Scale Questionnaire Tes | Instrument Test Code | HIGH |  |
| MMRC01TN | Modified Medical Research Council Dyspnea Scale Questionnaire Tes | Instrument Test Name | HIGH |  |
| MRS01TC | Modified Rankin Scale Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| MRS01TN | Modified Rankin Scale Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| MVAI101OR | Modified Van Assche Index Clinical Classification ORRES for MVAI1 | Instrument Original Result | HIGH |  |
| MVAI102OR | Modified Van Assche Index Clinical Classification ORRES for MVAI1 | Instrument Original Result | HIGH |  |
| MVAI103OR | Modified Van Assche Index Clinical Classification ORRES for MVAI1 | Instrument Original Result | HIGH |  |
| MVAI104OR | Modified Van Assche Index Clinical Classification ORRES for MVAI1 | Instrument Original Result | HIGH |  |
| MVAI105OR | Modified Van Assche Index Clinical Classification ORRES for MVAI1 | Instrument Original Result | HIGH |  |
| MVAI101STR | Modified Van Assche Index Clinical Classification STRESC for MVAI | Instrument Standardized Result | HIGH |  |
| MVAI102STR | Modified Van Assche Index Clinical Classification STRESC for MVAI | Instrument Standardized Result | HIGH |  |
| MVAI103STR | Modified Van Assche Index Clinical Classification STRESC for MVAI | Instrument Standardized Result | HIGH |  |
| MVAI104STR | Modified Van Assche Index Clinical Classification STRESC for MVAI | Instrument Standardized Result | HIGH |  |
| MVAI105STR | Modified Van Assche Index Clinical Classification STRESC for MVAI | Instrument Standardized Result | HIGH |  |
| MVAI1TC | Modified Van Assche Index Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| MVAI1TN | Modified Van Assche Index Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| MCHR01TC | Montreal Classification for Crohn's Disease Clinical Classificati | Instrument Test Code | HIGH |  |
| MCHR01TN | Montreal Classification for Crohn's Disease Clinical Classificati | Instrument Test Name | HIGH |  |
| UPD2TC | Movement Disorder Society Unified Parkinson's Disease Rating Scal | Instrument Test Code | HIGH |  |
| UPD2TN | Movement Disorder Society Unified Parkinson's Disease Rating Scal | Instrument Test Name | HIGH |  |
| MSFATSCD | Multiple Sclerosis Findings About Test Code | Instrument Test Code | HIGH |  |
| MSFATS | Multiple Sclerosis Findings About Test Name | Instrument Test Name | HIGH |  |
| MSQL1TC | Multiple Sclerosis Quality of Life-54 Instrument Questionnaire Te | Instrument Test Code | HIGH |  |
| MSQL1TN | Multiple Sclerosis Quality of Life-54 Instrument Questionnaire Te | Instrument Test Name | HIGH |  |
| MUSCTSCD | Musculoskeletal System Finding Test Code | Instrument Test Code | HIGH |  |
| MUSCTS | Musculoskeletal System Finding Test Name | Instrument Test Name | HIGH |  |
| FAC028TC | National Comprehensive Cancer Network/Functional Assessment of Ca | Instrument Test Code | HIGH |  |
| FAC028TN | National Comprehensive Cancer Network/Functional Assessment of Ca | Instrument Test Name | HIGH |  |
| FAC030TC | National Comprehensive Cancer Network/Functional Assessment of Ca | Instrument Test Code | HIGH |  |
| FAC030TN | National Comprehensive Cancer Network/Functional Assessment of Ca | Instrument Test Name | HIGH |  |
| FAC036TC | National Comprehensive Cancer Network/Functional Assessment of Ca | Instrument Test Code | HIGH |  |
| FAC036TN | National Comprehensive Cancer Network/Functional Assessment of Ca | Instrument Test Name | HIGH |  |
| FAC042TC | National Comprehensive Cancer Network/Functional Assessment of Ca | Instrument Test Code | HIGH |  |
| FAC042TN | National Comprehensive Cancer Network/Functional Assessment of Ca | Instrument Test Name | HIGH |  |
| FAC050TC | National Comprehensive Cancer Network/Functional Assessment of Ca | Instrument Test Code | HIGH |  |
| FAC050TN | National Comprehensive Cancer Network/Functional Assessment of Ca | Instrument Test Name | HIGH |  |
| NEWS1TC | National Early Warning Score 2 Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| NEWS1TN | National Early Warning Score 2 Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| VFQ1TC | National Eye Institute Visual Functioning Questionnaire - 25 Vers | Instrument Test Code | HIGH |  |
| VFQ1TN | National Eye Institute Visual Functioning Questionnaire - 25 Vers | Instrument Test Name | HIGH |  |
| VFQ2TC | National Eye Institute Visual Functioning Questionnaire - 25 Vers | Instrument Test Code | HIGH |  |
| VFQ2TN | National Eye Institute Visual Functioning Questionnaire - 25 Vers | Instrument Test Name | HIGH |  |
| NY1TC | National Youth Tobacco Survey 2022 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| NY1TN | National Youth Tobacco Survey 2022 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| NSA01TC | Negative Symptom Assessment-16 Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| NSA01TN | Negative Symptom Assessment-16 Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| NVTESTCD | Nervous System Findings Test Code | Instrument Test Code | HIGH |  |
| NVTEST | Nervous System Findings Test Name | Instrument Test Name | HIGH |  |
| NPS01TC | Neuropathic Pain Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| NPS01TN | Neuropathic Pain Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| NPI1TC | Neuropsychiatric Inventory Questionnaire Test Code | Instrument Test Code | HIGH |  |
| NPI1TN | Neuropsychiatric Inventory Questionnaire Test Name | Instrument Test Name | HIGH |  |
| NCF | Never/Current/Former Classification | Clinical Classification | HIGH |  |
| NYHAC | New York Heart Association Classification | Clinical Classification | HIGH |  |
| NHPT01TC | Nine-Hole Peg Test Functional Test Test Code | Instrument Test Code | HIGH |  |
| NHPT01TN | Nine-Hole Peg Test Functional Test Test Name | Instrument Test Name | HIGH |  |
| NY | No Yes Response | Observation Qualifier | HIGH |  |
| NSCLC1TC | Non-Small Cell Lung Cancer Symptom Assessment Questionnaire v1.0  | Instrument Test Code | HIGH |  |
| NSCLC1TN | Non-Small Cell Lung Cancer Symptom Assessment Questionnaire v1.0  | Instrument Test Name | HIGH |  |
| OIPRM | Non-host Organism Identifier Parameters | Parameter Name-Code | HIGH |  |
| OIPRMCD | Non-host Organism Identifier Parameters Code | Parameter Name-Code | HIGH |  |
| NSYSPCID | Non-system Reason for PCI Delay | Clinical Classification | HIGH |  |
| NORMABNM | Normal Abnormal Response | Clinical Classification | HIGH |  |
| NSAA1TC | North Star Ambulatory Assessment Clinical Classification Test Cod | Instrument Test Code | HIGH |  |
| NSAA1TN | North Star Ambulatory Assessment Clinical Classification Test Nam | Instrument Test Name | HIGH |  |
| ND | Not Done | Observation Qualifier | HIGH |  |
| NOTGRDRS | Nottingham Histologic Grade Response | Clinical Classification | HIGH |  |
| NTFATSCD | Nutrition Findings About Test Code | Instrument Test Code | HIGH |  |
| NTFATS | Nutrition Findings About Test Name | Instrument Test Name | HIGH |  |
| OBSSMO | Observational Study Model | Trial Design | HIGH |  |
| OBSSSM | Observational Study Sampling Method | Trial Design | HIGH |  |
| OBSSTP | Observational Study Time Perspective | Trial Design | HIGH |  |
| OGI01TC | Observer Global Impression Generic Modification Version Questionn | Instrument Test Code | HIGH |  |
| OGI01TN | Observer Global Impression Generic Modification Version Questionn | Instrument Test Name | HIGH |  |
| ONCRSR | Oncology Response Assessment Result | Oncology Assessment | HIGH |  |
| ONCRTSCD | Oncology Response Assessment Test Code | Instrument Test Code | HIGH |  |
| ONCRTS | Oncology Response Assessment Test Name | Instrument Test Name | HIGH |  |
| OETESTCD | Ophthalmic Exam Test Code | Instrument Test Code | HIGH |  |
| OETEST | Ophthalmic Exam Test Name | Instrument Test Name | HIGH |  |
| OEFOCUS | Ophthalmic Focus of Study Specific Interest | Observation Qualifier | HIGH |  |
| OTHEVENT | Other Disposition Event Response | Disposition | HIGH |  |
| OUT | Outcome of Event | Adverse Event Qualifier | HIGH |  |
| PKANMET | PK Analytical Method | Method | HIGH |  |
| PKPARM | PK Parameters | Parameter Name-Code | HIGH |  |
| PKPARMCD | PK Parameters Code | Parameter Name-Code | HIGH |  |
| PKUNIT | PK Units of Measure | Unit of Measure | HIGH |  |
| PKUDMG | PK Units of Measure - Dose mg | Unit of Measure | HIGH |  |
| PKUDUG | PK Units of Measure - Dose ug | Unit of Measure | HIGH |  |
| PKUWG | PK Units of Measure - Weight g | Unit of Measure | HIGH |  |
| PKUWKG | PK Units of Measure - Weight kg | Unit of Measure | HIGH |  |
| PA136TC | PROMIS Item Bank v1.0 - Fatigue - Short Form 7a Questionnaire Tes | Instrument Test Code | HIGH |  |
| PA136TN | PROMIS Item Bank v1.0 - Fatigue - Short Form 7a Questionnaire Tes | Instrument Test Name | HIGH |  |
| PA215TC | PROMIS Item Bank v1.0 - Sleep Disturbance - Short Form 4a Questio | Instrument Test Code | HIGH |  |
| PA215TN | PROMIS Item Bank v1.0 - Sleep Disturbance - Short Form 4a Questio | Instrument Test Name | HIGH |  |
| PA020TC | PROMIS Item Bank v2.0 - Cognitive Function - Abilities Subset - S | Instrument Test Code | HIGH |  |
| PA020TN | PROMIS Item Bank v2.0 - Cognitive Function - Abilities Subset - S | Instrument Test Name | HIGH |  |
| PA016TC | PROMIS Item Bank v2.0 - Cognitive Function - Short Form 6a Questi | Instrument Test Code | HIGH |  |
| PA016TN | PROMIS Item Bank v2.0 - Cognitive Function - Short Form 6a Questi | Instrument Test Name | HIGH |  |
| PA261TC | PROMIS-29 Profile v2.1 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| PA261TN | PROMIS-29 Profile v2.1 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| PASAT1TC | Paced Auditory Serial Addition Test Functional Test Test Code | Instrument Test Code | HIGH |  |
| PASAT1TN | Paced Auditory Serial Addition Test Functional Test Test Name | Instrument Test Name | HIGH |  |
| PTAP1TC | Paced Tapping Functional Test Test Code | Instrument Test Code | HIGH |  |
| PTAP1TN | Paced Tapping Functional Test Test Name | Instrument Test Name | HIGH |  |
| PI01TC | Pain Intensity Questionnaire Test Code | Instrument Test Code | HIGH |  |
| PI01TN | Pain Intensity Questionnaire Test Name | Instrument Test Name | HIGH |  |
| PR01TC | Pain Relief Questionnaire Test Code | Instrument Test Code | HIGH |  |
| PR01TN | Pain Relief Questionnaire Test Name | Instrument Test Name | HIGH |  |
| PAFATSCD | Pancreatic Cancer Findings About Test Code | Instrument Test Code | HIGH |  |
| PAFATS | Pancreatic Cancer Findings About Test Name | Instrument Test Name | HIGH |  |
| PDDS01TC | Patient Determined Disease Steps Questionnaire Test Code | Instrument Test Code | HIGH |  |
| PDDS01TN | Patient Determined Disease Steps Questionnaire Test Name | Instrument Test Name | HIGH |  |
| PGI01TC | Patient Global Impression Generic Modification Version Questionna | Instrument Test Code | HIGH |  |
| PGI01TN | Patient Global Impression Generic Modification Version Questionna | Instrument Test Name | HIGH |  |
| PHQ02TC | Patient Health Questionnaire - 15 Item Questionnaire Test Code | Instrument Test Code | HIGH |  |
| PHQ02TN | Patient Health Questionnaire - 15 Item Questionnaire Test Name | Instrument Test Name | HIGH |  |
| PHQ04TC | Patient Health Questionnaire - 2 Item Questionnaire Test Code | Instrument Test Code | HIGH |  |
| PHQ04TN | Patient Health Questionnaire - 2 Item Questionnaire Test Name | Instrument Test Name | HIGH |  |
| PHQ05TC | Patient Health Questionnaire - 8 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| PHQ05TN | Patient Health Questionnaire - 8 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| PHQ01TC | Patient Health Questionnaire - 9 Item Questionnaire Test Code | Instrument Test Code | HIGH |  |
| PHQ01TN | Patient Health Questionnaire - 9 Item Questionnaire Test Name | Instrument Test Name | HIGH |  |
| PHQ0101T09OR | Patient Health Questionnaire - 9 Questionnaire ORRES for PHQ0101  | Instrument Original Result | HIGH |  |
| PHQ0110OR | Patient Health Questionnaire - 9 Questionnaire ORRES for PHQ0110  | Instrument Original Result | HIGH |  |
| PHQ0101T09STR | Patient Health Questionnaire - 9 Questionnaire STRESC for PHQ0101 | Instrument Standardized Result | HIGH |  |
| PHQ0110STR | Patient Health Questionnaire - 9 Questionnaire STRESC for PHQ0110 | Instrument Standardized Result | HIGH |  |
| PHQ03TC | Patient Health Questionnaire Screener Version Questionnaire Test  | Instrument Test Code | HIGH |  |
| PHQ03TN | Patient Health Questionnaire Screener Version Questionnaire Test  | Instrument Test Name | HIGH |  |
| PT01TC | Patient-Reported Outcomes Version of the Common Terminology Crite | Instrument Test Code | HIGH |  |
| PT01TN | Patient-Reported Outcomes Version of the Common Terminology Crite | Instrument Test Name | HIGH |  |
| PDFATSCD | Pediatric Findings About Test Code | Instrument Test Code | HIGH |  |
| PDFATS | Pediatric Findings About Test Name | Instrument Test Name | HIGH |  |
| FAC099TC | Pediatric Functional Assessment of Chronic Illness Therapy-Fatigu | Instrument Test Code | HIGH |  |
| FAC099TN | Pediatric Functional Assessment of Chronic Illness Therapy-Fatigu | Instrument Test Name | HIGH |  |
| PODCI2TC | Pediatric Outcomes Data Collection Instrument, Adolescent Parent- | Instrument Test Code | HIGH |  |
| PODCI2TN | Pediatric Outcomes Data Collection Instrument, Adolescent Parent- | Instrument Test Name | HIGH |  |
| PODCI3TC | Pediatric Outcomes Data Collection Instrument, Adolescent Self-Re | Instrument Test Code | HIGH |  |
| PODCI3TN | Pediatric Outcomes Data Collection Instrument, Adolescent Self-Re | Instrument Test Name | HIGH |  |
| PODCI1TC | Pediatric Outcomes Data Collection Instrument, Pediatric Parent-R | Instrument Test Code | HIGH |  |
| PODCI1TN | Pediatric Outcomes Data Collection Instrument, Pediatric Parent-R | Instrument Test Name | HIGH |  |
| PQL15TC | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Ch | Instrument Test Code | HIGH |  |
| PQL15TN | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Ch | Instrument Test Name | HIGH |  |
| PQL14TC | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Ch | Instrument Test Code | HIGH |  |
| PQL14TN | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Ch | Instrument Test Name | HIGH |  |
| PQL13TC | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Te | Instrument Test Code | HIGH |  |
| PQL13TN | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Te | Instrument Test Name | HIGH |  |
| PQL12TC | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Te | Instrument Test Code | HIGH |  |
| PQL12TN | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Te | Instrument Test Name | HIGH |  |
| PQL18TC | Pediatric Quality of Life Neuromuscular Module Acute Version 3 To | Instrument Test Code | HIGH |  |
| PQL18TN | Pediatric Quality of Life Neuromuscular Module Acute Version 3 To | Instrument Test Name | HIGH |  |
| PQL11TC | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Yo | Instrument Test Code | HIGH |  |
| PQL11TN | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Yo | Instrument Test Name | HIGH |  |
| PQL10TC | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Yo | Instrument Test Code | HIGH |  |
| PQL10TN | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Yo | Instrument Test Name | HIGH |  |
| PQL17TC | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Yo | Instrument Test Code | HIGH |  |
| PQL17TN | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Yo | Instrument Test Name | HIGH |  |
| PQL16TC | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Yo | Instrument Test Code | HIGH |  |
| PQL16TN | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Yo | Instrument Test Name | HIGH |  |
| PQL06TC | Pediatric Quality of Life Neuromuscular Module Version 3 Child Pa | Instrument Test Code | HIGH |  |
| PQL06TN | Pediatric Quality of Life Neuromuscular Module Version 3 Child Pa | Instrument Test Name | HIGH |  |
| PQL05TC | Pediatric Quality of Life Neuromuscular Module Version 3 Child Qu | Instrument Test Code | HIGH |  |
| PQL05TN | Pediatric Quality of Life Neuromuscular Module Version 3 Child Qu | Instrument Test Name | HIGH |  |
| PQL04TC | Pediatric Quality of Life Neuromuscular Module Version 3 Teen Par | Instrument Test Code | HIGH |  |
| PQL04TN | Pediatric Quality of Life Neuromuscular Module Version 3 Teen Par | Instrument Test Name | HIGH |  |
| PQL03TC | Pediatric Quality of Life Neuromuscular Module Version 3 Teen Que | Instrument Test Code | HIGH |  |
| PQL03TN | Pediatric Quality of Life Neuromuscular Module Version 3 Teen Que | Instrument Test Name | HIGH |  |
| PQL09TC | Pediatric Quality of Life Neuromuscular Module Version 3 Toddler  | Instrument Test Code | HIGH |  |
| PQL09TN | Pediatric Quality of Life Neuromuscular Module Version 3 Toddler  | Instrument Test Name | HIGH |  |
| PQL02TC | Pediatric Quality of Life Neuromuscular Module Version 3 Young Ad | Instrument Test Code | HIGH |  |
| PQL02TN | Pediatric Quality of Life Neuromuscular Module Version 3 Young Ad | Instrument Test Name | HIGH |  |
| PQL01TC | Pediatric Quality of Life Neuromuscular Module Version 3 Young Ad | Instrument Test Code | HIGH |  |
| PQL01TN | Pediatric Quality of Life Neuromuscular Module Version 3 Young Ad | Instrument Test Name | HIGH |  |
| PQL08TC | Pediatric Quality of Life Neuromuscular Module Version 3 Young Ch | Instrument Test Code | HIGH |  |
| PQL08TN | Pediatric Quality of Life Neuromuscular Module Version 3 Young Ch | Instrument Test Name | HIGH |  |
| PQL07TC | Pediatric Quality of Life Neuromuscular Module Version 3 Young Ch | Instrument Test Code | HIGH |  |
| PQL07TN | Pediatric Quality of Life Neuromuscular Module Version 3 Young Ch | Instrument Test Name | HIGH |  |
| PSECD1TC | Penn State Electronic Cigarette Dependence Index Questionnaire Te | Instrument Test Code | HIGH |  |
| PSECD1TN | Penn State Electronic Cigarette Dependence Index Questionnaire Te | Instrument Test Name | HIGH |  |
| PUL01TC | Performance of the Upper Limb Module for DMD Version 1.2 Function | Instrument Test Code | HIGH |  |
| PUL01TN | Performance of the Upper Limb Module for DMD Version 1.2 Function | Instrument Test Name | HIGH |  |
| PUL02TC | Performance of the Upper Limb Module for DMD Version 2.0 Function | Instrument Test Code | HIGH |  |
| PUL02TN | Performance of the Upper Limb Module for DMD Version 2.0 Function | Instrument Test Name | HIGH |  |
| PDAI01TC | Perianal Crohn's Disease Activity Index Questionnaire Test Code | Instrument Test Code | HIGH |  |
| PDAI01TN | Perianal Crohn's Disease Activity Index Questionnaire Test Name | Instrument Test Name | HIGH |  |
| PHSPRPCD | Physical Properties Test Code | Instrument Test Code | HIGH |  |
| PHSPRP | Physical Properties Test Name | Instrument Test Name | HIGH |  |
| PORTOT | Portion/Totality | Anatomical Qualifier | HIGH |  |
| POSITION | Position | Anatomical Qualifier | HIGH |  |
| PANSS1TC | Positive and Negative Syndrome Scale Clinical Classification Test | Instrument Test Code | HIGH |  |
| PANSS1TN | Positive and Negative Syndrome Scale Clinical Classification Test | Instrument Test Name | HIGH |  |
| PRITBCON | Priority of Tuberculosis Contact | Role/Relationship | HIGH |  |
| PROCEDUR | Procedure | Treatment Qualifier | HIGH |  |
| PRURGNCY | Procedure Urgency Status | Disposition | HIGH |  |
| PROTMLST | Protocol Milestone | Trial Design | HIGH |  |
| RSKASMT | Protocol Risk Assessment Response | Trial Design | HIGH |  |
| PASI05TC | Psoriasis Area and Severity Index Version Bozek Clinical Classifi | Instrument Test Code | HIGH |  |
| PASI05TN | Psoriasis Area and Severity Index Version Bozek Clinical Classifi | Instrument Test Name | HIGH |  |
| PASI04TC | Psoriasis Area and Severity Index Version EMA Clinical Classifica | Instrument Test Code | HIGH |  |
| PASI04TN | Psoriasis Area and Severity Index Version EMA Clinical Classifica | Instrument Test Name | HIGH |  |
| PASI02TC | Psoriasis Area and Severity Index Version Feldman Clinical Classi | Instrument Test Code | HIGH |  |
| PASI02TN | Psoriasis Area and Severity Index Version Feldman Clinical Classi | Instrument Test Name | HIGH |  |
| PASI03TC | Psoriasis Area and Severity Index Version Fredriksson Clinical Cl | Instrument Test Code | HIGH |  |
| PASI03TN | Psoriasis Area and Severity Index Version Fredriksson Clinical Cl | Instrument Test Name | HIGH |  |
| PSFATSCD | Psoriasis Findings About Test Code | Instrument Test Code | HIGH |  |
| PSFATS | Psoriasis Findings About Test Name | Instrument Test Name | HIGH |  |
| QRSMTHOD | QRS Method | Method | HIGH |  |
| QLES2TC | Quality Of Life Enjoyment And Satisfaction Questionnaire - Short  | Instrument Test Code | HIGH |  |
| QLES2TN | Quality Of Life Enjoyment And Satisfaction Questionnaire - Short  | Instrument Test Name | HIGH |  |
| QLES1TC | Quality Of Life Enjoyment And Satisfaction Questionnaire Test Cod | Instrument Test Code | HIGH |  |
| QLES1TN | Quality Of Life Enjoyment And Satisfaction Questionnaire Test Nam | Instrument Test Name | HIGH |  |
| IBDQ01TC | Quality of Life in Inflammatory Bowel Disease Questionnaire Test  | Instrument Test Code | HIGH |  |
| IBDQ01TN | Quality of Life in Inflammatory Bowel Disease Questionnaire Test  | Instrument Test Name | HIGH |  |
| QSUB01TC | Questionnaire on Smoking Urges-Brief Test Code | Instrument Test Code | HIGH |  |
| QSUB01TN | Questionnaire on Smoking Urges-Brief Test Name | Instrument Test Name | HIGH |  |
| QIDSC1TC | Quick Inventory of Depressive Symptomatology Clinician-Rated Vers | Instrument Test Code | HIGH |  |
| QIDSC1TN | Quick Inventory of Depressive Symptomatology Clinician-Rated Vers | Instrument Test Name | HIGH |  |
| QIDSR1TC | Quick Inventory of Depressive Symptomatology Self-Report Version  | Instrument Test Code | HIGH |  |
| QIDSR1TN | Quick Inventory of Depressive Symptomatology Self-Report Version  | Instrument Test Name | HIGH |  |
| R3601TC | RAND 36-Item Health Survey 1.0 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| R3601TN | RAND 36-Item Health Survey 1.0 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| RSSS01TC | RAND Social Support Survey Instrument Questionnaire Test Code | Instrument Test Code | HIGH |  |
| RSSS01TN | RAND Social Support Survey Instrument Questionnaire Test Name | Instrument Test Name | HIGH |  |
| RACE | Race | Demographic | HIGH |  |
| RACEC | Race As Collected | Demographic | HIGH |  |
| CSLVLNIM | Reason CS/LV Lead Not Implanted | Clinical Classification | HIGH |  |
| REASTRT | Reason For Treatment | Treatment Qualifier | HIGH |  |
| REASTINT | Reason for Treatment Interruption | Treatment Qualifier | HIGH |  |
| NRIND | Reference Range Indicator | Observation Qualifier | HIGH |  |
| STENRF | Relation to Reference Period | Observation Qualifier | HIGH |  |
| RELTYPE | Relationship Type | Role/Relationship | HIGH |  |
| RELSUB | Relationship to Subject | Role/Relationship | HIGH |  |
| RPTESTCD | Reproductive System Findings Test Code | Instrument Test Code | HIGH |  |
| RPTEST | Reproductive System Findings Test Name | Instrument Test Name | HIGH |  |
| RETESTCD | Respiratory Test Code | Instrument Test Code | HIGH |  |
| RETEST | Respiratory Test Name | Instrument Test Name | HIGH |  |
| RSLSCLRS | Result Scale Response | Observation Qualifier | HIGH |  |
| RESTYPRS | Result Type Response | Observation Qualifier | HIGH |  |
| FIQR01TC | Revised Fibromyalgia Impact Questionnaire Questionnaire Test Code | Instrument Test Code | HIGH |  |
| FIQR01TN | Revised Fibromyalgia Impact Questionnaire Questionnaire Test Name | Instrument Test Name | HIGH |  |
| AVL02TC | Rey Auditory Verbal Learning Test Functional Test Test Code | Instrument Test Code | HIGH |  |
| AVL02TN | Rey Auditory Verbal Learning Test Functional Test Test Name | Instrument Test Name | HIGH |  |
| RCVD01TC | Reynolds Cardiovascular Disease 10-Year Risk Score Clinical Class | Instrument Test Code | HIGH |  |
| RCVD01TN | Reynolds Cardiovascular Disease 10-Year Risk Score Clinical Class | Instrument Test Name | HIGH |  |
| RASS01TC | Richmond Agitation-Sedation Scale Clinical Classification Test Co | Instrument Test Code | HIGH |  |
| RASS01TN | Richmond Agitation-Sedation Scale Clinical Classification Test Na | Instrument Test Name | HIGH |  |
| SAS01TC | Riker Sedation-Agitation Scale Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| SAS01TN | Riker Sedation-Agitation Scale Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| RISEF1TC | Rising From Floor Functional Test Test Code | Instrument Test Code | HIGH |  |
| RISEF1TN | Rising From Floor Functional Test Test Name | Instrument Test Name | HIGH |  |
| RPQ01TC | Rivermead Post Concussion Symptoms Questionnaire Questionnaire Te | Instrument Test Code | HIGH |  |
| RPQ01TN | Rivermead Post Concussion Symptoms Questionnaire Questionnaire Te | Instrument Test Name | HIGH |  |
| ROCK01TC | Rockport One Mile Walk Test Version 1.0 Functional Test Test Code | Instrument Test Code | HIGH |  |
| ROCK01TN | Rockport One Mile Walk Test Version 1.0 Functional Test Test Name | Instrument Test Name | HIGH |  |
| RDQ01TC | Roland Morris Disability Questionnaire Questionnaire Test Code | Instrument Test Code | HIGH |  |
| RDQ01TN | Roland Morris Disability Questionnaire Questionnaire Test Name | Instrument Test Name | HIGH |  |
| ROUTE | Route of Administration Response | Treatment Qualifier | HIGH |  |
| RUTG0101OR | Rutgeerts Score Clinical Classification ORRES for RUTG0101 TN/TC | Instrument Original Result | HIGH |  |
| RUTG0101STR | Rutgeerts Score Clinical Classification STRESC for RUTG0101 TN/TC | Instrument Standardized Result | HIGH |  |
| RUTG01TC | Rutgeerts Score Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| RUTG01TN | Rutgeerts Score Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| DTHDXCD | SDTM Death Diagnosis and Details Test Code | Instrument Test Code | HIGH |  |
| DTHDX | SDTM Death Diagnosis and Details Test Name | Instrument Test Name | HIGH |  |
| DOMAIN | SDTM Domain Abbreviation | Trial Design | HIGH |  |
| MITSCD | SDTM Microscopic Findings Test Code | Instrument Test Code | HIGH |  |
| MITS | SDTM Microscopic Findings Test Name | Instrument Test Name | HIGH |  |
| SDTMVRS | SDTM Version Response | Trial Design | HIGH |  |
| SDTMDVRS | SDTMIG Medical Device Version Response | Trial Design | HIGH |  |
| SDTMIGRS | SDTMIG Version Response | Trial Design | HIGH |  |
| SF6D2TC | SF-6Dv2 Health Utility Survey Acute, English Version 2.0 Question | Instrument Test Code | HIGH |  |
| SF6D2TN | SF-6Dv2 Health Utility Survey Acute, English Version 2.0 Question | Instrument Test Name | HIGH |  |
| SF6D1TC | SF-6Dv2 Health Utility Survey Standard, English Version 2.0 Quest | Instrument Test Code | HIGH |  |
| SF6D1TN | SF-6Dv2 Health Utility Survey Standard, English Version 2.0 Quest | Instrument Test Name | HIGH |  |
| SWLS01TC | Satisfaction With Life Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| SWLS01TN | Satisfaction With Life Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| SZFATSCD | Schizophrenia Findings About Test Code | Instrument Test Code | HIGH |  |
| SZFATS | Schizophrenia Findings About Test Name | Instrument Test Name | HIGH |  |
| SOAPR1TC | Screener and Opioid Assessment for Patients with Pain - Revised Q | Instrument Test Code | HIGH |  |
| SOAPR1TN | Screener and Opioid Assessment for Patients with Pain - Revised Q | Instrument Test Name | HIGH |  |
| SOFA0101OR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Original Result | HIGH |  |
| SOFA0102OR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Original Result | HIGH |  |
| SOFA0103OR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Original Result | HIGH |  |
| SOFA0104OR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Original Result | HIGH |  |
| SOFA0105OR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Original Result | HIGH |  |
| SOFA0106OR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Original Result | HIGH |  |
| SOFA0101STR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Standardized Result | HIGH |  |
| SOFA0102STR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Standardized Result | HIGH |  |
| SOFA0103STR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Standardized Result | HIGH |  |
| SOFA0104STR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Standardized Result | HIGH |  |
| SOFA0105STR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Standardized Result | HIGH |  |
| SOFA0106STR | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Standardized Result | HIGH |  |
| SOFA01TC | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Test Code | HIGH |  |
| SOFA01TN | Sepsis-related Organ Failure Assessment 27MAR2024 Clinical Classi | Instrument Test Name | HIGH |  |
| SEVRS | Severity Response | Observation Qualifier | HIGH |  |
| AESEV | Severity/Intensity Scale for Adverse Events | Adverse Event Qualifier | HIGH |  |
| SEX | Sex | Demographic | HIGH |  |
| SEXABRTH | Sex Assigned At Birth Response | Demographic | HIGH |  |
| SEXPOP | Sex of Participants Response | Trial Design | HIGH |  |
| SEXORIRS | Sexual Orientation Response | Demographic | HIGH |  |
| SDS01TC | Sheehan Disability Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| SDS01TN | Sheehan Disability Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| SF102TC | Short Form 10 Health Survey for Children Acute, US Version 1.0 Qu | Instrument Test Code | HIGH |  |
| SF102TN | Short Form 10 Health Survey for Children Acute, US Version 1.0 Qu | Instrument Test Name | HIGH |  |
| SF101TC | Short Form 10 Health Survey for Children Standard, US Version 1.0 | Instrument Test Code | HIGH |  |
| SF101TN | Short Form 10 Health Survey for Children Standard, US Version 1.0 | Instrument Test Name | HIGH |  |
| SF122TC | Short Form 12 Health Survey Acute, US Version 1.0 Questionnaire T | Instrument Test Code | HIGH |  |
| SF122TN | Short Form 12 Health Survey Acute, US Version 1.0 Questionnaire T | Instrument Test Name | HIGH |  |
| SF124TC | Short Form 12 Health Survey Acute, US Version 2.0 Questionnaire T | Instrument Test Code | HIGH |  |
| SF124TN | Short Form 12 Health Survey Acute, US Version 2.0 Questionnaire T | Instrument Test Name | HIGH |  |
| SF121TC | Short Form 12 Health Survey Standard, US Version 1.0 Questionnair | Instrument Test Code | HIGH |  |
| SF121TN | Short Form 12 Health Survey Standard, US Version 1.0 Questionnair | Instrument Test Name | HIGH |  |
| SF123TC | Short Form 12 Health Survey Standard, US Version 2.0 Questionnair | Instrument Test Code | HIGH |  |
| SF123TN | Short Form 12 Health Survey Standard, US Version 2.0 Questionnair | Instrument Test Name | HIGH |  |
| SF82TC | Short Form 8 Health Survey Acute, US Version 1.0 Questionnaire Te | Instrument Test Code | HIGH |  |
| SF82TN | Short Form 8 Health Survey Acute, US Version 1.0 Questionnaire Te | Instrument Test Name | HIGH |  |
| SF81TC | Short Form 8 Health Survey Standard, US Version 1.0 Questionnaire | Instrument Test Code | HIGH |  |
| SF81TN | Short Form 8 Health Survey Standard, US Version 1.0 Questionnaire | Instrument Test Name | HIGH |  |
| SPPB1TC | Short Physical Performance Battery Version 1.2 Functional Test Te | Instrument Test Code | HIGH |  |
| SPPB1TN | Short Physical Performance Battery Version 1.2 Functional Test Te | Instrument Test Name | HIGH |  |
| SFMP2TC | Short-Form McGill Pain Questionnaire-2 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| SFMP2TN | Short-Form McGill Pain Questionnaire-2 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| SES01TC | Simple Endoscopic Score for Crohn's Disease Version 1 Clinical Cl | Instrument Test Code | HIGH |  |
| SES01TN | Simple Endoscopic Score for Crohn's Disease Version 1 Clinical Cl | Instrument Test Name | HIGH |  |
| SIZE | Size Response | Observation Qualifier | HIGH |  |
| SRTESTCD | Skin Response Test Code | Instrument Test Code | HIGH |  |
| SRTEST | Skin Response Test Name | Instrument Test Name | HIGH |  |
| SKINTYP | Skin Type Response | Observation Qualifier | HIGH |  |
| RISKSOC | Social Risk Factor | Demographic | HIGH |  |
| CLMETH | Specimen Collection Method | Method | HIGH |  |
| SPECCOND | Specimen Condition | Specimen | HIGH |  |
| SPECTYPE | Specimen Type | Specimen | HIGH |  |
| SGRQ01TC | St. George's Respiratory Questionnaire Past 3 Months Version Ques | Instrument Test Code | HIGH |  |
| SGRQ01TN | St. George's Respiratory Questionnaire Past 3 Months Version Ques | Instrument Test Name | HIGH |  |
| SGRQ02TC | St. George's Respiratory Questionnaire Past 4 Weeks Version Quest | Instrument Test Code | HIGH |  |
| SGRQ02TN | St. George's Respiratory Questionnaire Past 4 Weeks Version Quest | Instrument Test Name | HIGH |  |
| SGRQC1TC | St. George's Respiratory Questionnaire for COPD Patients Question | Instrument Test Code | HIGH |  |
| SGRQC1TN | St. George's Respiratory Questionnaire for COPD Patients Question | Instrument Test Name | HIGH |  |
| SSS0101OR | Stanford Sleepiness Scale Questionnaire ORRES for SSS0101 TN/TC | Instrument Original Result | HIGH |  |
| SSS0101STR | Stanford Sleepiness Scale Questionnaire STRESC for SSS0101 TN/TC | Instrument Standardized Result | HIGH |  |
| SSS01TC | Stanford Sleepiness Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| SSS01TN | Stanford Sleepiness Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| STCG01TC | Stent Thrombosis Coronary ARC Grade Clinical Classification Test  | Instrument Test Code | HIGH |  |
| STCG01TN | Stent Thrombosis Coronary ARC Grade Clinical Classification Test  | Instrument Test Name | HIGH |  |
| STCARCRS | Stent Thrombosis, Coronary ARC Grade Responses | Clinical Classification | HIGH |  |
| STCTIMRS | Stent Thrombosis, Coronary, ARC Timing Responses | Clinical Classification | HIGH |  |
| STYPE | Study Type Response | Trial Design | HIGH |  |
| DSSCAT | Subcategory for Disposition Event | Domain Category | HIGH |  |
| SCTESTCD | Subject Characteristic Test Code | Instrument Test Code | HIGH |  |
| SCTEST | Subject Characteristic Test Name | Instrument Test Name | HIGH |  |
| SSTATRS | Subject Status Response | Disposition | HIGH |  |
| SSTESTCD | Subject Status Test Code | Instrument Test Code | HIGH |  |
| SSTEST | Subject Status Test Name | Instrument Test Name | HIGH |  |
| SOWSA1TC | Subjective Opiate Withdrawal Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| SOWSA1TN | Subjective Opiate Withdrawal Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| SDTHSDTP | Sudden Death Syndrome Type | Clinical Classification | HIGH |  |
| SIQ01TC | Suicidal Ideation Questionnaire Test Code | Instrument Test Code | HIGH |  |
| SIQ01TN | Suicidal Ideation Questionnaire Test Name | Instrument Test Name | HIGH |  |
| SIQ02TC | Suicidal Ideation Questionnaire-JR Questionnaire Test Code | Instrument Test Code | HIGH |  |
| SIQ02TN | Suicidal Ideation Questionnaire-JR Questionnaire Test Name | Instrument Test Name | HIGH |  |
| EVDRETRT | Supporting Evidence for Re-Treatment | Treatment Qualifier | HIGH |  |
| SDMT01TC | Symbol Digit Modalities Test Functional Test Test Code | Instrument Test Code | HIGH |  |
| SDMT01TN | Symbol Digit Modalities Test Functional Test Test Name | Instrument Test Name | HIGH |  |
| SIQR01TC | Symptom Impact Questionnaire Questionnaire Test Code | Instrument Test Code | HIGH |  |
| SIQR01TN | Symptom Impact Questionnaire Questionnaire Test Name | Instrument Test Name | HIGH |  |
| SMDDS1TC | Symptoms of Major Depressive Disorder Scale v1.0 Questionnaire Te | Instrument Test Code | HIGH |  |
| SMDDS1TN | Symptoms of Major Depressive Disorder Scale v1.0 Questionnaire Te | Instrument Test Name | HIGH |  |
| TIMIFLRS | TIMI Flow Responses | Clinical Classification | HIGH |  |
| TANN0201OR | Tanner Scale Boy Clinical Classification ORRES for TANN0201 TN/TC | Instrument Original Result | HIGH |  |
| TANN0202OR | Tanner Scale Boy Clinical Classification ORRES for TANN0202 TN/TC | Instrument Original Result | HIGH |  |
| TANN0201STR | Tanner Scale Boy Clinical Classification STRESC for TANN0201 TN/T | Instrument Standardized Result | HIGH |  |
| TANN0202STR | Tanner Scale Boy Clinical Classification STRESC for TANN0202 TN/T | Instrument Standardized Result | HIGH |  |
| TANN02TC | Tanner Scale Boy Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| TANN02TN | Tanner Scale Boy Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| TANN0101OR | Tanner Scale Girl Clinical Classification ORRES for TANN0101 TN/T | Instrument Original Result | HIGH |  |
| TANN0102OR | Tanner Scale Girl Clinical Classification ORRES for TANN0102 TN/T | Instrument Original Result | HIGH |  |
| TANN0101STR | Tanner Scale Girl Clinical Classification STRESC for TANN0101 TN/ | Instrument Standardized Result | HIGH |  |
| TANN0102STR | Tanner Scale Girl Clinical Classification STRESC for TANN0102 TN/ | Instrument Standardized Result | HIGH |  |
| TANN01TC | Tanner Scale Girl Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| TANN01TN | Tanner Scale Girl Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| TESTCOND | Test Condition Response | Observation Qualifier | HIGH |  |
| TSTMTHSN | Test Method Sensitivity | Method | HIGH |  |
| TSTOPOBJ | Test Operational Objective | Trial Design | HIGH |  |
| BODE01TC | The Body-Mass Index, Airflow Obstruction, Dyspnea, and Exercise C | Instrument Test Code | HIGH |  |
| BODE01TN | The Body-Mass Index, Airflow Obstruction, Dyspnea, and Exercise C | Instrument Test Name | HIGH |  |
| EPIC1TC | The Expanded Prostate Cancer Index Composite Short Form Questionn | Instrument Test Code | HIGH |  |
| EPIC1TN | The Expanded Prostate Cancer Index Composite Short Form Questionn | Instrument Test Name | HIGH |  |
| EPIC2TC | The Expanded Prostate Cancer Index Composite for Clinical Practic | Instrument Test Code | HIGH |  |
| EPIC2TN | The Expanded Prostate Cancer Index Composite for Clinical Practic | Instrument Test Name | HIGH |  |
| FAC001TC | The Functional Assessment of Cancer Therapy-General Version 4 Que | Instrument Test Code | HIGH |  |
| FAC001TN | The Functional Assessment of Cancer Therapy-General Version 4 Que | Instrument Test Name | HIGH |  |
| FAC023TC | The Functional Assessment of Cancer Therapy-Prostate Version 4 Qu | Instrument Test Code | HIGH |  |
| FAC023TN | The Functional Assessment of Cancer Therapy-Prostate Version 4 Qu | Instrument Test Name | HIGH |  |
| GMSS01TC | The Glucose Monitoring System Satisfaction Survey Version: Type 1 | Instrument Test Code | HIGH |  |
| GMSS01TN | The Glucose Monitoring System Satisfaction Survey Version: Type 1 | Instrument Test Name | HIGH |  |
| FAC052TC | The National Comprehensive Cancer Network/Functional Assessment o | Instrument Test Code | HIGH |  |
| FAC052TN | The National Comprehensive Cancer Network/Functional Assessment o | Instrument Test Name | HIGH |  |
| ODI01TC | The Oswestry Disability Index Version 2.1a Questionnaire Test Cod | Instrument Test Code | HIGH |  |
| ODI01TN | The Oswestry Disability Index Version 2.1a Questionnaire Test Nam | Instrument Test Name | HIGH |  |
| OABQ01TC | The Overactive Bladder Questionnaire Questionnaire Test Code | Instrument Test Code | HIGH |  |
| OABQ01TN | The Overactive Bladder Questionnaire Questionnaire Test Name | Instrument Test Name | HIGH |  |
| OABQ02TC | The Overactive Bladder Questionnaire Short Form Questionnaire Tes | Instrument Test Code | HIGH |  |
| OABQ02TN | The Overactive Bladder Questionnaire Short Form Questionnaire Tes | Instrument Test Name | HIGH |  |
| PCL01TC | The PTSD Checklist for DSM-5 Questionnaire Test Code | Instrument Test Code | HIGH |  |
| PCL01TN | The PTSD Checklist for DSM-5 Questionnaire Test Name | Instrument Test Name | HIGH |  |
| PROS01TC | The Prostate Cancer Specific Quality of Life Instrument Questionn | Instrument Test Code | HIGH |  |
| PROS01TN | The Prostate Cancer Specific Quality of Life Instrument Questionn | Instrument Test Name | HIGH |  |
| SF362TC | The Short Form 36 Health Survey Acute, US Version 1.0 Questionnai | Instrument Test Code | HIGH |  |
| SF362TN | The Short Form 36 Health Survey Acute, US Version 1.0 Questionnai | Instrument Test Name | HIGH |  |
| SF364TC | The Short Form 36 Health Survey Acute, US Version 2.0 Questionnai | Instrument Test Code | HIGH |  |
| SF364TN | The Short Form 36 Health Survey Acute, US Version 2.0 Questionnai | Instrument Test Name | HIGH |  |
| SF361TC | The Short Form 36 Health Survey Standard, US Version 1.0 Question | Instrument Test Code | HIGH |  |
| SF361TN | The Short Form 36 Health Survey Standard, US Version 1.0 Question | Instrument Test Name | HIGH |  |
| SF363TC | The Short Form 36 Health Survey Standard, US Version 2.0 Question | Instrument Test Code | HIGH |  |
| SF363TN | The Short Form 36 Health Survey Standard, US Version 2.0 Question | Instrument Test Name | HIGH |  |
| WPAI02TC | The Work Productivity and Activity Impairment - General Health Ve | Instrument Test Code | HIGH |  |
| WPAI02TN | The Work Productivity and Activity Impairment - General Health Ve | Instrument Test Name | HIGH |  |
| T25FW1TC | Timed 25-Foot Walk Test Functional Test Test Code | Instrument Test Code | HIGH |  |
| T25FW1TN | Timed 25-Foot Walk Test Functional Test Test Name | Instrument Test Name | HIGH |  |
| TUG01TC | Timed Up and Go Test Functional Test Test Code | Instrument Test Code | HIGH |  |
| TUG01TN | Timed Up and Go Test Functional Test Test Name | Instrument Test Name | HIGH |  |
| TIFATSCD | Tobacco Findings About Test Code | Instrument Test Code | HIGH |  |
| TIFATS | Tobacco Findings About Test Name | Instrument Test Name | HIGH |  |
| TPCATRS | Tobacco Product Category Response | Tobacco Product | HIGH |  |
| PDPARMCD | Tobacco Product Design Parameters Code | Parameter Name-Code | HIGH |  |
| PDPARM | Tobacco Product Design Parameters Name | Parameter Name-Code | HIGH |  |
| SPECPT | Tobacco Product Testing Specimen Type | Specimen | HIGH |  |
| PTTESTCD | Tobacco Product Testing Test Code | Instrument Test Code | HIGH |  |
| PTTEST | Tobacco Product Testing Test Name | Instrument Test Name | HIGH |  |
| TOPARMCD | Tobacco Products Parameter Code | Parameter Name-Code | HIGH |  |
| TOPARM | Tobacco Products Parameter Name | Parameter Name-Code | HIGH |  |
| TNCOMPLT | Tobacco Study Completion/Reason for Non-Completion | Disposition | HIGH |  |
| TMT01TC | Trail Making Test Functional Test Test Code | Instrument Test Code | HIGH |  |
| TMT01TN | Trail Making Test Functional Test Test Name | Instrument Test Name | HIGH |  |
| TDI01TC | Transition Dyspnea Index Clinical Classification Test Code | Instrument Test Code | HIGH |  |
| TDI01TN | Transition Dyspnea Index Clinical Classification Test Name | Instrument Test Name | HIGH |  |
| TSCC01TC | Trauma Symptom Checklist for Children Questionnaire Test Code | Instrument Test Code | HIGH |  |
| TSCC01TN | Trauma Symptom Checklist for Children Questionnaire Test Name | Instrument Test Name | HIGH |  |
| TSCYC1TC | Trauma Symptom Checklist for Young Children Questionnaire Test Co | Instrument Test Code | HIGH |  |
| TSCYC1TN | Trauma Symptom Checklist for Young Children Questionnaire Test Na | Instrument Test Name | HIGH |  |
| TRTINTNT | Treatment Intent | Treatment Qualifier | HIGH |  |
| TSQM01TC | Treatment Satisfaction Questionnaire for Medication Version 1.4 Q | Instrument Test Code | HIGH |  |
| TSQM01TN | Treatment Satisfaction Questionnaire for Medication Version 1.4 Q | Instrument Test Name | HIGH |  |
| TRTSET | Treatment Setting | Treatment Qualifier | HIGH |  |
| TBLIND | Trial Blinding Schema Response | Trial Design | HIGH |  |
| TINDTP | Trial Intent Type Response | Trial Design | HIGH |  |
| TPHASE | Trial Phase Response | Trial Design | HIGH |  |
| TSPARMCD | Trial Summary Parameter Test Code | Instrument Test Code | HIGH |  |
| TSPARM | Trial Summary Parameter Test Name | Instrument Test Name | HIGH |  |
| TTYPE | Trial Type Response | Trial Design | HIGH |  |
| TBFATSCD | Tuberculosis Findings About Test Code | Instrument Test Code | HIGH |  |
| TBFATS | Tuberculosis Findings About Test Name | Instrument Test Name | HIGH |  |
| TUTESTCD | Tumor or Lesion Identification Test Code | Instrument Test Code | HIGH |  |
| TUTEST | Tumor or Lesion Identification Test Name | Instrument Test Name | HIGH |  |
| TUIDRS | Tumor or Lesion Identification Test Results | Oncology Assessment | HIGH |  |
| TRTESTCD | Tumor or Lesion Properties Test Code | Instrument Test Code | HIGH |  |
| TRTEST | Tumor or Lesion Properties Test Name | Instrument Test Name | HIGH |  |
| TRPROPRS | Tumor or Lesion Properties Test Result | Oncology Assessment | HIGH |  |
| D1FATSCD | Type 1 Diabetes Findings About Test Code | Instrument Test Code | HIGH |  |
| D1FATS | Type 1 Diabetes Findings About Test Name | Instrument Test Name | HIGH |  |
| UHDR1TC | Unified Huntington's Disease Rating Scale '99 Clinical Classifica | Instrument Test Code | HIGH |  |
| UHDR1TN | Unified Huntington's Disease Rating Scale '99 Clinical Classifica | Instrument Test Name | HIGH |  |
| UPD1TC | Unified Parkinson's Disease Rating Scale Clinical Classification  | Instrument Test Code | HIGH |  |
| UPD1TN | Unified Parkinson's Disease Rating Scale Clinical Classification  | Instrument Test Name | HIGH |  |
| UNIT | Unit | Unit of Measure | HIGH |  |
| VSRESU | Units for Vital Signs Results | Unit of Measure | HIGH |  |
| UPS01TC | Urgency Perception Scale Questionnaire Test Code | Instrument Test Code | HIGH |  |
| UPS01TN | Urgency Perception Scale Questionnaire Test Name | Instrument Test Name | HIGH |  |
| URNSTSCD | Urinary System Test Code | Instrument Test Code | HIGH |  |
| URNSTS | Urinary System Test Name | Instrument Test Name | HIGH |  |
| VCNEVD | Vaccination Evidence Source | Observation Qualifier | HIGH |  |
| VNFATSCD | Vaccines Findings About Test Code | Instrument Test Code | HIGH |  |
| VNFATS | Vaccines Findings About Test Name | Instrument Test Name | HIGH |  |
| VALG01TC | Veterans Administration Lung Study Group Clinical Classification  | Instrument Test Code | HIGH |  |
| VALG01TN | Veterans Administration Lung Study Group Clinical Classification  | Instrument Test Name | HIGH |  |
| VLERS1TC | Vignos Lower Extremity Rating Scale Clinical Classification Test  | Instrument Test Code | HIGH |  |
| VLERS1TN | Vignos Lower Extremity Rating Scale Clinical Classification Test  | Instrument Test Name | HIGH |  |
| VSTESTCD | Vital Signs Test Code | Instrument Test Code | HIGH |  |
| VSTEST | Vital Signs Test Name | Instrument Test Name | HIGH |  |
| VHI01TC | Voice Handicap Index Questionnaire Test Code | Instrument Test Code | HIGH |  |
| VHI01TN | Voice Handicap Index Questionnaire Test Name | Instrument Test Name | HIGH |  |
| WHIVS1TC | WHO Clinical Staging of HIV/AIDS for Adults and Adolescents Clini | Instrument Test Code | HIGH |  |
| WHIVS1TN | WHO Clinical Staging of HIV/AIDS for Adults and Adolescents Clini | Instrument Test Name | HIGH |  |
| WHIVS2TC | WHO Clinical Staging of HIV/AIDS for Children Clinical Classifica | Instrument Test Code | HIGH |  |
| WHIVS2TN | WHO Clinical Staging of HIV/AIDS for Children Clinical Classifica | Instrument Test Name | HIGH |  |
| HEPENCGR | West Haven Hepatic Encephalopathy Grade | Clinical Classification | HIGH |  |
| WHEG01TC | West Haven Hepatic Encephalopathy Grade Clinical Classification T | Instrument Test Code | HIGH |  |
| WHEG01TN | West Haven Hepatic Encephalopathy Grade Clinical Classification T | Instrument Test Name | HIGH |  |
| WPAI01TC | Work Productivity and Activity Impairment Questionnaire - Specifi | Instrument Test Code | HIGH |  |
| WPAI01TN | Work Productivity and Activity Impairment Questionnaire - Specifi | Instrument Test Name | HIGH |  |
| WD4TC | World Health Organization Disability Assessment Schedule 2.0 - 12 | Instrument Test Code | HIGH |  |
| WD4TN | World Health Organization Disability Assessment Schedule 2.0 - 12 | Instrument Test Name | HIGH |  |
| WD1TC | World Health Organization Disability Assessment Schedule 2.0 - 12 | Instrument Test Code | HIGH |  |
| WD1TN | World Health Organization Disability Assessment Schedule 2.0 - 12 | Instrument Test Name | HIGH |  |
| WD2TC | World Health Organization Disability Assessment Schedule 2.0 - 12 | Instrument Test Code | HIGH |  |
| WD2TN | World Health Organization Disability Assessment Schedule 2.0 - 12 | Instrument Test Name | HIGH |  |
| WD3TC | World Health Organization Disability Assessment Schedule 2.0 - 12 | Instrument Test Code | HIGH |  |
| WD3TN | World Health Organization Disability Assessment Schedule 2.0 - 12 | Instrument Test Name | HIGH |  |
| WD5TC | World Health Organization Disability Assessment Schedule 2.0 - 36 | Instrument Test Code | HIGH |  |
| WD5TN | World Health Organization Disability Assessment Schedule 2.0 - 36 | Instrument Test Name | HIGH |  |
| WD6TC | World Health Organization Disability Assessment Schedule 2.0 - 36 | Instrument Test Code | HIGH |  |
| WD6TN | World Health Organization Disability Assessment Schedule 2.0 - 36 | Instrument Test Name | HIGH |  |
| WD7TC | World Health Organization Disability Assessment Schedule 2.0 - 36 | Instrument Test Code | HIGH |  |
| WD7TN | World Health Organization Disability Assessment Schedule 2.0 - 36 | Instrument Test Name | HIGH |  |

---

## Section 3 — Structural Observations

1. **Which categories were easiest to identify and why?** Instrument Test Code and Test Name (818 of 1,181 codelists) are trivially identified by their naming convention — "Test Code" / "Test Name" in the Codelist Name, with matching TC/TN submission value suffixes.

2. **Which codelists were hardest to assign — what caused the ambiguity?** The ~27 Observation Qualifier codelists were hardest because they lack a shared naming pattern — each qualifies observations in a different way (reference range indicator, consciousness state, disease outcome, result scale), and their only unifying property is that they *qualify* rather than *identify* or *classify*.

3. **Did any codelists appear to belong to two categories?** Several codelists with "Response" in their name and RS-suffix submission values straddle Clinical Classification and Observation Qualifier — e.g., SKINCLAS (Fitzpatrick Skin Classification Response) functions as both a classification and a response value set; AJCCGRD (AJCC Tumor Grade Response) likewise; these were assigned to Clinical Classification because the classification identity dominates their machine-consumption role.

4. **What structure is present but invisible in the flat format?** The instrument family grouping — a single QRS instrument produces 2–4 coordinated codelists (TC, TN, and per-question OR/STR pairs) — is completely implicit; a consumer must parse submission value prefixes to reconstruct which codelists belong to the same instrument.

5. **Are there codelists whose machine-actionability differs fundamentally from others in the same category?** Within Instrument Test Code, 56 codelists are extensible and 353 are not — the extensible ones (e.g., EGTEST, LBTESTCD, VSTESTCD) are domain-level test code codelists that aggregate across multiple instruments, while the non-extensible ones are instrument-specific; a consuming system must handle them differently (the former grows, the latter is fixed).

6. **Which categories share a machine-consumption profile despite different naming signatures?** Parameter Name-Code and Instrument Test Code/Test Name share the same consumption pattern (name-code pair lookup for variable population) despite completely different naming conventions; similarly, Observation Qualifier and Clinical Classification both provide allowed-value validation but are distinguished only by whether the values form a recognized clinical scale.

7. **Do any categories appear to be specializations or subsets of another category rather than peers?** Instrument Original Result and Instrument Standardized Result are specializations of a broader "Instrument Response Value" concept — they always co-occur and differ only in which SDTM variable they populate (--ORRES vs --STRESC); ECG Findings, Microbiology/Immunology, Genomic, Oncology Assessment, and Tobacco Product are all domain-specific specializations of Observation Qualifier — they were separated because their naming patterns are strongly distinctive, but structurally they serve the same qualifying role.

---

## Section 4 — What would refine this

- **CDISC Library API codelist-to-variable mappings** would resolve which SDTM variable each codelist populates, converting inferred roles ("this looks like a --CAT codelist") into confirmed assignments.
- **NCIt hierarchy relationships** (parent/child C-codes) would reveal the instrument family groupings that are invisible in the flat file and would confirm which Clinical Classifications are truly standalone vs. instrument-derived.
- **SDTMIG domain model metadata** (which variables are Required/Expected/Permissible per domain) would ground the Observation Qualifier category — items could be sub-classified by their variable role (qualifier, timing, identifier).