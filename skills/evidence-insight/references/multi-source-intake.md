# Multi Source Intake

Required loading condition: At source intake for every evidence task, before interpreting any input. Apply format-specific subsections only to supplied formats.

Section identifiers are stable rule identifiers, not release versions.

# 2A. MULTI-SOURCE EVIDENCE INTAKE — Identify What the User Actually Supplied

This layer is intentionally lightweight. It is not a new scoring system and not a large router.

Before interpretation, classify the supplied material by source role.

## 2A.1 Source types

### IMAGE
Examples:
- screenshot
- chart
- research figure
- map
- infographic

### URL
Examples:
- article
- official data page
- research paper page
- interactive chart
- institutional rule page

### DATA
Examples:
- CSV
- TSV
- JSON
- XLSX
- spreadsheet export

### ARCHIVE
Examples:
- ZIP containing CSV, JSON, README, metadata, charts or codebooks

### DOCUMENT
Examples:
- PDF
- Markdown
- TXT
- report
- working paper
- methodology note

### MIXED
Any task combining two or more source types.

The purpose is not to assign a workflow label for its own sake.
The purpose is to decide which supplied source should answer which question.

---

## 2A.2 Source-role hierarchy

When multiple representations of the same evidence are available, prefer the most informative representation for the claim being tested.

Typical hierarchy:

1. machine-readable underlying data for exact calculations;
2. metadata / README / methodology for definitions, units, revisions and scope;
3. original paper / official source for interpretation and provenance;
4. chart / image for visual framing and what caught the user's attention;
5. secondary article for context;
6. repost / summary only when better sources are unavailable.

Do not infer exact values from pixels when an attached machine-readable dataset contains the value.

Do not treat a chart as the methodology document when a README, metadata file or source note is available.

Do not treat three reposts of one press release as three independent sources.

---

## 2A.3 Archive handling

For ZIP / archive inputs:

1. inspect the file list first;
2. identify likely roles:
   - data;
   - metadata / README / codebook;
   - chart / visualization;
   - methodology;
   - source notes;
3. open the smallest set of files needed to understand:
   - variables;
   - units;
   - date coverage;
   - geography / population;
   - missing values;
   - revision or version information;
4. prefer machine-readable data for calculations;
5. use metadata / README to interpret column meaning;
6. never assume a column definition from its name alone when supporting documentation exists.

If the archive cannot be read, say so explicitly and do not pretend that archive contents were analyzed.

---

## 2A.4 URL handling

For URL inputs:

- identify whether the URL is:
  - the original source;
  - a secondary article;
  - an interactive visualization;
  - a landing page;
  - a PDF / dataset link;
- follow primary-source links when the user's question depends on the original evidence;
- if an interactive chart exposes underlying data or metadata, prefer those for exact values;
- distinguish:
  - publication date;
  - data period;
  - latest revision date.

Do not quote a news article as the primary evidence when the linked original paper or official dataset is available and central to the claim.

---

## 2A.5 Dataset handling

Before analyzing a dataset, determine:

- unit of observation;
- variable definitions;
- units;
- time range;
- geography / population;
- missing-value conventions;
- whether values are observed, modeled, imputed, revised or forecast;
- whether multiple files are comparable.

For exact numerical claims:
- compute from the dataset when practical;
- do not estimate from the chart if the dataset is available.

For derived metrics:
- verify the calculation logic;
- distinguish direct source values from model-derived calculations.

---

## 2A.6 Mixed-source division of labor

When the user supplies multiple sources, assign each source a role.

Default pattern:

### Image
Use for:
- framing;
- visible relationships;
- what needs explanation;
- visual anomalies.

### Dataset
Use for:
- exact values;
- thresholds;
- rankings;
- rates of change;
- cross-country / cross-group comparisons;
- reproducible calculations.

### Metadata / methodology
Use for:
- definitions;
- scope;
- comparability;
- model / estimate status;
- revisions.

### External web research
Use for:
- causal mechanisms;
- institutional context;
- original-source verification;
- counterevidence;
- updated context not contained in the supplied material.

The final synthesis may combine these roles, but do not blur them.

---

## 2A.7 Conflict handling

If supplied sources disagree, do not silently choose one.

Check:
- revision date;
- definition;
- population;
- geography;
- denominator;
- unit;
- time coverage;
- modeled vs observed status.

Then:
- reconcile when possible;
- otherwise state the conflict;
- preserve the stronger source for the narrower supported claim.

---

## 2A.8 Source intake stopping rule

Do not inspect every file merely because it exists.

Stop intake when:
- the relevant variable definitions are clear;
- the necessary data are located;
- provenance is known;
- additional files are unlikely to change the interpretation.

This prevents archive or document tasks from becoming exhaustive file-dump analysis.

# 3. READ — Identify What the Supplied Evidence Already Tells the User

For images, classify the visual evidence:
- official statistic
- direct observation
- historical series
- reconstruction
- model simulation
- forecast
- hypothesis diagram
- correlation plot
- causal estimate
- map
- survey
- media summary
- secondary infographic
- unknown

For multiple images or mixed sources, determine their relation:
- overview → detail
- distribution → transmission
- hypothesis → evidence
- before → after
- level → slope
- claim → qualification
- independent evidence

Extract the already-supplied known information. For images this includes:
- title
- headline
- main numbers
- axes
- legend
- labels
- annotations
- footnotes
- methodology notes
- source names
- obvious trends

All of this becomes KNOWN information. For documents, URLs and datasets, information explicitly supplied by the source is also KNOWN once read.

---
