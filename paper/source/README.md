# The Quiet Calculus — scientific manuscript

Prepared locally for Christopher Michael Baird on October 25, 2026.

Version 4.0 adds targeted semantic and adaptive-memory revisions, evaluated on newly held-out cases and simulation paths, while preserving the version 3 computational campaign and the original 92-principle extraction and 12-card research program. Results distinguish software checks, synthetic language-model evaluation, simulated predictive performance, and conditional physical-model calculations. There is no new human or laboratory evidence, physical field detection, or completed unified theory.

Version 3 results (unchanged): the adaptive-memory comparison gives a small average loss improvement but fails its frozen minimum-effect and worst-scenario robustness requirements. The spectral suite reproduces its historical outputs and passes additional numerical-route checks. Portal stress-test warnings are retained, with exploratory follow-up diagnosing the unreliable adaptive reference and quantifying both quadratures. The fresh local inference run yields 10/12 label matches for both single-pass and three-role systems, with the same two semantic errors; three roles use 3.28 times the tokens. All results and limitations are reported in the manuscript and companion evidence bundle.

Version 4 results: the revised memory gate lowers Brier loss relative to the original adaptive policy on 1,100 new held-out paths and passes both its frozen repair criterion and the unchanged version 3 criterion; five known-family givebacks are retained, and fixed memory remains better on two exploratory transfer families. The first semantic revision, a structured certificate, fails its frozen gate on 36 new cases (21/36 versus 26/36 label matches). The one permitted follow-up, a five-field representation with two abstention guards, also fails on 24 further cases: it removes the same-model baseline's three false refutations of undecidable claims and makes fewer incorrect definite judgments (2 versus 5), but matches 18/24 versus 19/24 labels with four unnecessary abstentions. The unchanged baseline on a larger installed model matched 21/24 as a descriptive model control. Both semantic candidates are recorded as rejected repairs; no further retuning was performed.

## Read or edit

- `main.pdf`: compiled manuscript.
- `main.tex`: main LaTeX document.
- `sections/`: editable manuscript and appendices.
- `references.tex`: bibliography used by the manuscript.
- `references.bib`: equivalent BibTeX records for journal-format conversion; not used by the present build.
- `data/principles.psv` and `data/principles.json`: full 92-item inventory with physical PDF page references.
- `data/source_provenance.json`: original-file SHA-256, metadata, and page-by-page extraction audit (no copied full source text).
- `data/toy_results.json`: all synthetic numerical results and checks.
- `data/reference_audit.json`: citation identities and verification scope. `reference_metadata.json` retains the limited Crossref responses, including rate-limit failures; it is not the sole citation-verification source.
- `data/research_sources.json`: 24 source paths, hashes and evidence locators.
- `data/prediction_registry.json`: 12 target cards, with version 3 execution coverage and remaining gaps.
- `data/prediction_checks.json`: new deterministic kernel and information calculations.
- `figures/portal_shape.pdf`: vector separation-response illustration.
- `figures/fresh_memory_results.pdf`: fresh simulation effects, including benefits and harms.
- `data/fresh_memory_summary.json`: compact audited seed-cluster contrasts.
- `data/fresh_run_manifest.json`: local experiment paths, freeze/result hashes and execution scope.
- `sections/15_revisions.tex`: version 4 targeted revisions and their fresh held-out evaluations.
- `figures/revision_memory_results.pdf`: revised versus original memory policy on new held-out paths.
- `data/revision_memory_summary.json`, `data/revision_semantic_summary.json`, `data/revision_semantic_followup_summary.json`: compact version 4 result records.
- `data/revision_run_manifest.json`: version 4 revision paths, freeze/result hashes, scope and prediction-card coverage.
- `verification/`: compiler logs, build report, artifact audit, and review record.

## Overleaf

Upload the provided ZIP as a new project, choose `main.tex` as the main document, and use **pdfLaTeX**. All assets required to compile are included. No shell escape, Python execution, external source PDF, special fonts, BibTeX pass, or network request is needed for compilation. Overleaf itself was not accessed or tested. Version 4 sources were verified locally with three-pass pdfLaTeX and a clean rebuild from the extracted ZIP; the Codex desktop compiler, used for version 3, was not used for version 4.

## Reproduce locally

From the project directory:

```sh
python3 scripts/build.py
python3 scripts/reproduce.py
python3 scripts/generate_catalogue.py
python3 scripts/build.py
```

The original numerical calculations and catalogue generation use Python's standard library. The new physics illustrations require NumPy; ReportLab is additionally needed to regenerate their figure:

```sh
python3 scripts/prediction_checks.py --figures
```

To regenerate the original toy-results figure, install ReportLab and run:

```sh
python3 scripts/reproduce.py --figures
```

To re-audit the original source, install pypdf and run:

```sh
python3 scripts/audit_source.py /absolute/path/to/Dune_The_Quiet_Calculus_Book_I_First_Cohort.pdf
```

The script requires the exact SHA-256 analyzed in version 1.0. The original file is not included in this package and was not modified. All page locators are physical PDF pages; printed folios are one lower after the cover.

## Validation and scientific status

A clean build establishes that this artifact compiles and has resolved references. The included deterministic calculations establish outputs under their explicitly stated synthetic assumptions. Neither is physical evidence. Synthetic model behavior and simulation outcomes provide bounded computational performance evidence, with the paper reporting failures as well as successes. Feasible local test subsets were executed under timestamped internal protocols. The paper distinguishes them from historical results and from still-unperformed human/laboratory studies. No external public registration is claimed. This manuscript has not been published or externally peer reviewed.

Authorship, funding, conflicts of interest, intended venue, and any human-study protocol require the author's substantive review before a submission. Zora is the name used for the AI research assistant, not an additional human author. No external Grok, Claude, or Gemini review was performed. After the Codex session that prepared most of version 4 reached its usage limit, Claude (Anthropic) executed the remaining frozen semantic follow-up steps and completed the manuscript integration, compilation and packaging at the author's request. That is continuation of the same internal workflow, not independent review.

## Version preservation

Version 1, version 2 and version 3 PDFs and ZIPs are preserved beside this project in `../quiet-calculus-version-1-archive/`, `../quiet-calculus-version-2-archive/` and `../quiet-calculus-version-3-archive/`. The version 3 evidence ZIP is preserved there too. Version 4 updates the working manuscript in place; section 12 (the original version 3 results) remains byte-identical in its LaTeX source. Original narrative and synced research sources were not changed. The Overleaf archive contains the complete manuscript and new illustrative code, not the full upstream research corpora. Source-integrity auditing requires the original local files; compilation and the new numerical examples do not.

## Fresh local evidence bundle

`Quiet_Calculus_Local_Test_Bundle.zip`, delivered alongside the manuscript and Overleaf ZIP, contains the isolated inference, memory, portal, and spectral workstreams: frozen protocols, source copies, raw outputs, scripts, environments, commands, logs and audits. The manuscript project contains compact result records; the evidence ZIP contains the fuller execution record. Both are local artifacts, with no public upload performed.

The inference run needs the recorded local Ollama model digest; it is not reproduced by merely compiling the paper. The memory scripts use the copied pinned dependency. Spectral and portal reproduction need the recorded NumPy/SciPy/mpmath environment. Follow each workstream's README/protocol and write new outputs to a separate directory to preserve the delivered evidence.

To regenerate the new memory figure from its saved results (ReportLab required):

```sh
python3 scripts/plot_fresh_memory.py
python3 scripts/plot_revision_memory.py
```

The second command regenerates the version 4 revision figure from `data/revision_memory_summary.json`.

The internal protocol freeze was informed by earlier outcomes. The portal follow-up was designed after initial numerical warnings and is explicitly exploratory. No failed result was removed or retuned into a confirmatory success.

## Revision implementation and evidence

`Quiet_Calculus_Revision_Test_Bundle.zip` is a separate additive revision package. It contains the semantic implementation and preserved development variants, separately authored frozen holdout, paired raw model calls, the second-stage five-field follow-up (development model selection, separately authored 24-case holdout, three-arm raw calls, audit and post-run error review), memory gate and frozen candidate selection, fresh test paths, and audits. `semantic_followup/OPERATOR_HANDOFF.json` records the hand-off from the Codex session to Claude before the follow-up was sealed and run. The earlier `Quiet_Calculus_Local_Test_Bundle.zip` remains the unchanged version 3 campaign. The paper’s `data/revision_run_manifest.json` links the new records to their hashes. No installed model weights or production workflow were changed.
