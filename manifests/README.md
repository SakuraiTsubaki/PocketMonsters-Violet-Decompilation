# Manifests

This directory stores machine-readable and reviewable inventories for reconstructed source, extracted/recreated assets, public research sources, version coverage, hashes, and reproducibility metadata.

## Purpose

A manifest should make it possible to answer:

- What is this file, asset, dataset, or research source?
- Which target version, region, language, revision, or build does it belong to or describe?
- Where did it come from?
- How was it extracted, reconstructed, generated, or reported?
- How can its identity or claim be verified?
- Is it shared with another version or stored once to avoid duplication?
- May the underlying material be redistributed, or should the repository retain only metadata, hashes, structure, and links?

## Source registry

`source-registry.json` is the project-wide public-source inventory for the current game repository. It is intentionally cumulative and should include official sources, public datamines, reverse-engineering projects, open-source tools, technical documentation, databases/wikis, archives, and useful community findings.

The source registry is **not** a statement that every listed source is correct or redistributable. Each entry should preserve its evidence class, scope, verification state, and repository-inclusion status.

Because the project currently has no local retail ROM/game dump, the source registry is a core input to reconstruction work. Japanese release / Japanese-language material is the origin reference for regional and language comparison, while all other official regions/languages remain in scope.

## Recommended formats

Use JSON, YAML, CSV, or Markdown tables when appropriate. Prefer formats that are easy to review in Git and straightforward to consume from tooling.

## Recommended fields for reconstructed material

- `id` — stable logical identifier
- `path` — repository path
- `kind` — source, data, graphic, audio, script, map, table, metadata, etc.
- `target` — version, region, language, revision, update, build
- `source` — archive, container, executable, section, table, symbol, index, offset, dataset, or public source
- `size` — byte size when useful
- `hashes` — cryptographic identity hashes
- `generated_by` — tool or command used to produce the committed material
- `verification` — Unverified, Observed, Reproduced, or Matched
- `shared_with` — other targets that use the same byte-identical material
- `notes` — meaningful differences, limitations, or unresolved questions

## Recommended fields for research sources

- `id` — stable source identifier
- `kind` — official product page, patch note, public datamine, reverse-engineering tool, technical documentation, database, etc.
- `evidence_class` — Official primary, Public datamine, Reverse engineering, Independent database/wiki, Community report, or Unverified claim
- `url` — stable public URL when available
- `retrieved_at` — date checked by this project
- `scope` — subjects/data categories covered by the source
- `target_version` — version/build coverage when known
- `languages` / `regions` — coverage when known
- `license` — software/content license when known
- `verification` — what this project has actually established from the source
- `repository_inclusion` — whether material may be copied, reused under license, or should remain metadata/link-only
- `notes` — limitations, maintenance state, conflicts, and follow-up work

## Rules

1. Do not invent unknown metadata; use `null`, `unknown`, or `TBD` explicitly.
2. Prefer cryptographic hashes for identity-sensitive files.
3. Do not deduplicate assets only because they look or sound identical; verify byte identity or hashes when practical.
4. Keep provenance sufficient to trace committed material back to a verified source location or reproducible derivation process.
5. Keep source provenance separate from direct project verification level; a third-party datamine is not automatically `Observed` by this project.
6. Public availability does not automatically establish redistribution permission.
7. Do not place retail ROM images, decrypted game images, console keys, or redistributable game binaries in this directory.
8. Expand the source registry in small reviewable batches and never label a seed inventory as exhaustive until the defined search space has been systematically covered.

See `example.asset-manifest.json` for an asset-manifest starting point, `source-registry.json` for the active public-source inventory, and `../docs/PROJECT_STANDARDS.md` for the broader repository rules.
