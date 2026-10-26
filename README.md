# The Quiet Calculus

**Inference, Adaptive Memory, and Conditional Physics in ZoraASI and Theory of Everything Research**
Christopher Michael Baird · version 4.0 · October 25, 2026

> **Status:** preprint, not peer reviewed. The evidence is computational: software checks, a local language model's behavior on AI-written fictional test cases, and simulations. There is no laboratory or human-subject data, and nothing here is a physical validation of a Theory of Everything.

## What this is

The paper starts from a Dune campaign novelization, *The Quiet Calculus, Book I: First Cohort*, and pulls out 92 page-referenced principles. It connects them to versioned ZoraASI and Theory of Everything research and states twelve predictions, each with what would count against it. It then tests the parts a local computer can test, under rules fixed before each run, with fresh test material and all failures reported.

## Main results

**Version 3 (local test campaign)**
- *Evidence judgment:* on 12 fictional cases, a single-pass reviewer and a three-role team each matched 10 of 12 provisional labels and made the same two errors. One error was treating silence as proof something was false; the other was picking a side when equally credible sources disagreed.
- *Adaptive memory:* on 1,100 simulated paths it beat a fixed baseline on average, but failed its pre-set minimum-benefit and worst-case-harm criteria.
- *Conditional physics checks:* the exact spectral suite reproduced its 126 historical checks, and two independent dephasing calculations agree on 960 configurations. These are checks of stated equations, not of nature.

**Version 4 (targeted repairs, tested on new held-out material)**
- *Adaptive-memory repair: passed.* On 1,100 new simulated paths, a gated memory lowered average forecast error by about 0.4% versus the original and passed both its repair criterion and the version 3 criterion. Fixed memory still wins on two untuned transfer scenarios.
- *Evidence-judgment repairs: both failed* their pre-set tests.
  - The first scored 21/36 against the original's 26/36.
  - The second removed the targeted error on its test set: it never called an undecidable claim false. But it over-abstained and misread negatively worded claims, scoring 18/24 against 19/24.

The version 3 results section of the paper is byte-identical to its version 3 form. Earlier versions are kept in `versions/`.

## Contents

| Path | What it is |
|---|---|
| `paper/Quiet_Calculus_Scientific_Paper_v4.0.pdf` | The paper, version 4.0 (58 pages) |
| `paper/source/` | Full LaTeX source, data, figures, scripts and verification records. Compiles with pdfLaTeX, e.g. on Overleaf. |
| `evidence/Quiet_Calculus_Revision_Test_Bundle.zip` | Version 4 evidence: frozen protocols, held-out cases, raw model calls, audits and post-run error reviews |
| `evidence/Quiet_Calculus_Local_Test_Bundle.zip` | Version 3 evidence (unchanged) |
| `evidence/Quiet_Calculus_Overleaf.zip` | The delivered source archive |
| `evidence/Quiet_Calculus_v4_Delivery.json` | Delivery record with checksums and verification flags |
| `versions/` | Versions 1.0 to 3.0 of the paper |
| `CHECKSUMS.sha256` | SHA-256 of every top-level artifact |

## Verify and reproduce

- `sha256sum -c CHECKSUMS.sha256` checks the files. The hashes match the original delivery records.
- `paper/source/README.md` explains how to rebuild the PDF and rerun the deterministic calculations.
- Each evidence bundle has its own README, frozen protocols, audits and `reproduce_to.py` scripts.
  - Model runs need the exact local Ollama model digests recorded in the bundles.
  - A replay re-exposes cases that are already public; it is not a fresh test.
- Some provenance records contain absolute file paths from the author's computer. They are kept unchanged so the checksums still verify.

## AI assistance and provenance

Christopher Michael Baird is the author. Versions 1 to 4 were prepared with Zora, the author's name for his AI research assistant, working through ChatGPT Codex. When the Codex session reached its usage limit, Claude (Anthropic) completed the final version 4 steps: the held-out semantic run, integration, compilation and packaging, documented in the evidence bundle. All test cases and labels were written by AI assistants. There has been no independent human adjudication or external replication.

## Related work

- **Updating Without Runaway: Truth-Constrained, Multi-Timescale Alignment for Autonomous Adaptive AI.** A follow-up engineering note that builds on these results. Repository: <https://github.com/Cbaird26/updating-without-runaway>
- **A Theory of Everything** (C. M. Baird), Zenodo concept DOI [10.5281/zenodo.14019809](https://doi.org/10.5281/zenodo.14019809)

## Citation

See `CITATION.cff`. Each GitHub release of this repository is archived on Zenodo with a DOI.

## License

The paper, figures and data are licensed CC BY 4.0, and the code MIT; see `LICENSE.md`. The Dune setting and the analyzed fan novelization are not covered and are not included.
