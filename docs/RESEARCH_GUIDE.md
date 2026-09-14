# Research Guide

This guide defines how reverse-engineering findings should be recorded so that later contributors can reproduce, compare, and verify them.

## Current research mode

The project owner currently has no local retail ROM, decrypted game image, or complete game dump for the target. Research therefore starts from publicly accessible evidence and must preserve provenance carefully enough that later direct verification remains possible.

Comparative research uses the Japanese release / Japanese-language presentation as the origin reference. This is a research baseline, not a presumption that Japan uses a distinct binary or that every difference is region-specific.

## Evidence first

Record the target version/revision, region, language, evidence source, source URL or stable citation, retrieval date, file or executable name when known, offsets or addresses when meaningful, hashes or identifiers, tools or commands used, and comparison notes.

## Evidence classes

- **Official primary** — first-party Pokémon, Nintendo, platform, service, event, patch, or support material.
- **Public datamine** — publicly released extracted data or structured findings derived from a game build.
- **Reverse engineering** — public format research, parser/editor/decompiler code, technical documentation, or tool behavior.
- **Independent database / wiki** — secondary structured reference material.
- **Community report** — community observation that may be useful but needs stronger corroboration.
- **Unverified claim** — a lead kept for investigation, not established project knowledge.

Evidence class describes provenance. It does **not** replace verification level.

## Verification levels

- **Hypothesis** — plausible but not confirmed.
- **Observed** — directly seen by this project in a specific target build, executable, extracted file, or runtime observation.
- **Reproduced** — recreated with documented steps, inputs, and tooling.
- **Matched** — reconstructed output verified against the intended target using an explicit exact-match criterion.

A public datamine, wiki entry, or third-party reverse-engineering claim does not become **Observed** merely because it reports direct access to a build. Record it under its evidence class until this project can independently establish the stronger verification level.

Do not silently promote hypotheses or imported claims into facts.

## Exhaustive-source workflow

1. Define the exact research question and data category.
2. Start from the Japanese reference baseline and list the regions, languages, revisions, updates, DLC states, event periods, and linked services that could differ.
3. Search first-party Japanese sources and other first-party regional sources.
4. Search public GitHub repositories, source code, tools, parsers, editors, format documents, manifests, and datamine projects.
5. Search independent databases, wikis, archived pages, technical write-ups, and relevant community records.
6. Record each useful source with provenance before merging claims.
7. Separate raw observations/claims from interpretation.
8. Compare Japanese-reference material against every identified official region/language target; do not sample only a few major languages.
9. Cross-check important numbers, structural claims, version differences, and historical changes against independent evidence where practical.
10. Preserve unresolved conflicts rather than forcing a single answer.
11. Commit research outputs, comparison tables, source indexes, manifests, tooling, and status updates to GitHub in small reviewable batches.
12. Update `VERSIONS.md`, `PROJECT_STATUS.md`, `ROADMAP.md`, or verification records when scope or confidence changes.

## Regional / language comparison checklist

For each research category, ask separately whether differences exist in:

- package / storefront / distribution metadata
- supported languages
- localized text
- graphics or UI
- executable or code behavior
- structured game data
- events and distributions
- update timing or revision history
- DLC availability or state
- online/service behavior
- censorship, legal, ratings, or localization changes

Do not treat a localization difference as a binary difference without evidence, and do not treat a shared binary as proof that every region-facing behavior is identical.

## Recording unknowns

Use explicit states such as `TBD`, `unknown`, `not yet verified`, or `conflicting sources`. Never fill gaps by analogy with another generation or another game.

## Repository boundaries

Do not commit retail ROM/game images, decrypted distribution images, console keys, or other redistributable game binaries. Public availability elsewhere does not automatically grant redistribution permission. Reconstructed source, tooling, documentation, manifests, metadata, comparison data, and project-created assets should remain reproducible and reviewable.