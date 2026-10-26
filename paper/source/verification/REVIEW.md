# Version 4.0 local verification — October 25, 2026

- Manuscript: 58 pages; 92 catalogue entries; 12 prediction cards; 33 references; 24 hashed research-source records.
- pdfLaTeX (pdfTeX 3.141592653-2.6-1.40.27 (TeX Live 2025)): three passes with shell escape disabled; zero warnings, unresolved references, missing characters, overfull or underfull boxes (`build_report.json`).
- Clean rebuild: the delivered Overleaf ZIP contents were extracted to a fresh folder and compiled from scratch. Page count and extracted text match the working PDF, and compile-input hashes match the delivered ZIP (`archive_rebuild.json`). The Codex desktop compiler was not used for version 4 (`desktop_compile.json`).
- Structural PDF audit: all catalogue and prediction identifiers and all citations are present. There are no empty pages, replacement characters, or off-page text. The original narrative and all 24 research-source hashes are unchanged (`artifact_audit.json`).
- Preservation: the version 3 results section (Section 12) is byte-identical. All 257 version 3 experiment files and the three version 3 deliverables match their recorded hashes (`preservation_audit.json` in the revision bundle). Version 1-3 PDFs and ZIPs remain in adjacent archives.
- Revision experiments: the memory audit covers 51 software checks, the replayed validation selection and traces, and independent seed-cluster arithmetic. The first semantic stage audit has 668 assertions and the semantic follow-up audit 671. These verify the saved runs, not label correctness. Both semantic repairs fail their frozen gates, and that is reported as such.
- Visual QA: all rendered pages of the final build were reviewed as contact sheets, with expanded inspection of the new Section 13 tables and the revision-memory figure.
- Execution: Codex prepared most of version 4. Claude (Anthropic) completed the semantic follow-up execution, the manuscript integration, compilation and packaging after the Codex session ended (`semantic_followup/OPERATOR_HANDOFF.json`). Neither is independent human review. No human or laboratory study, public upload, or submission was performed.

Compilation and hashes establish artifact integrity, not empirical validation of ZoraASI or a Theory of Everything. The version 3 review record is preserved inside the version 3 archive.
