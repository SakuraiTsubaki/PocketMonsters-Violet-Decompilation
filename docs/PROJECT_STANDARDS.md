# Project Standards

This document defines shared repository conventions for source reconstruction, research data, manifests, and project assets. Platform-specific rules may extend these standards once the target architecture is verified.

## Operating baseline

- This project currently assumes that no local retail ROM, decrypted game image, or complete game dump is available to the project owner.
- Research therefore begins from publicly accessible material: official documentation, public reverse-engineering work, public datamines, open-source tooling, technical write-ups, databases, archives, and independently checkable community findings.
- The Japanese release / Japanese-language presentation is the origin reference for comparative research. This is a comparison baseline, not an assumption that Japan necessarily has a separate binary, earlier build, or unique file set.
- All officially released regions, languages, revisions, updates, DLC, distributions, online events, and linked-service behavior are in scope. Do not assume that two regional or language releases are identical until evidence supports that conclusion.
- Research results, source indexes, comparison tables, manifests, tooling, and verification records produced by this project should be committed to GitHub in reviewable form whenever they belong within repository boundaries.

## Naming conventions

- Prefer stable, descriptive, ASCII-safe file and directory names unless the original format requires otherwise.
- Use lowercase names for new generic directories and tooling paths unless a verified upstream convention requires different casing.
- Avoid spaces in machine-consumed paths when a clear hyphen or underscore is sufficient.
- Preserve verified original identifiers when they carry technical meaning; document aliases instead of silently renaming them.
- Include version, language, revision, or region identifiers in paths or metadata when material differs between targets.

## Source and generated data

- Prefer editable source, metadata, and reproducible conversion steps over opaque generated output.
- Generated files should identify their source inputs and generation method when practical.
- Do not treat generated output as authoritative when an editable source representation exists.
- Keep tools and scripts required to reproduce committed derived data in the repository whenever practical.

## Asset policy

- Human-viewable assets such as PNG previews may be committed when they help inspection, review, or verification.
- Preserve the corresponding reconstructed source data or documented extraction/conversion path where practical.
- Byte-identical assets shared by versions, revisions, regions, or languages should normally be stored once and referenced through metadata, manifests, or version maps instead of duplicated.
- Do not deduplicate files merely because they look visually or audibly identical; confirm identity using hashes or byte comparison when practical.
- Record meaningful differences between regional, language, revision, and update variants.

## Manifest policy

Manifests should use a structured, reviewable format such as JSON, YAML, CSV, or Markdown tables as appropriate. Entries should record enough information to identify, compare, and reproduce the material they describe.

Recommended fields include:

- logical identifier or asset name
- repository path
- target version / region / language / revision
- Japanese-baseline relationship when relevant
- source type and source URL or stable citation
- retrieval or observation date
- source container, archive, section, table, executable, or public dataset identifier
- source offset, index, symbol, or record identifier when known
- file size where useful
- cryptographic hash for identity-sensitive material
- extraction or generation tool / command
- evidence class
- verification level
- redistribution / repository-inclusion status
- notes and known differences

Do not invent unknown metadata. Use an explicit `unknown`, `TBD`, `null`, or equivalent state when information has not been verified.

## Evidence and provenance

Keep **source provenance** separate from **verification level**.

Recommended evidence classes are:

- **Official primary** — first-party Pokémon, Nintendo, platform, service, event, patch, or support material.
- **Public datamine** — publicly released extracted data or structured findings derived from a game build.
- **Reverse engineering** — public technical analysis, format documentation, parser, editor, decompiler, or related source code.
- **Independent database / wiki** — secondary structured reference material.
- **Community report** — reproducible or potentially useful community observation that still needs stronger corroboration.
- **Unverified claim** — a claim recorded for investigation but not yet supported strongly enough for project use.

Evidence class does not automatically grant a verification level. In particular, material imported from a public datamine or another reverse-engineering project must not be labeled **Observed** by this project merely because someone else observed it.

- Separate confirmed observations from hypotheses.
- Record the target build or version associated with technical claims whenever known.
- Prefer hashes and stable identifiers over filenames alone for identity checks.
- Keep enough provenance to trace reconstructed data back to its public source, verified source location, or derivation process.
- Cross-check important claims against independent sources where practical.
- Update `VERSIONS.md`, `PROJECT_STATUS.md`, and verification records when newly confirmed information changes project scope.

## Regional and language comparison policy

1. Start comparative inventories from the Japanese reference baseline.
2. Enumerate every officially supported region and language rather than sampling only major releases.
3. Distinguish packaging/store/distribution differences from actual executable, resource, text, event, or data differences.
4. Preserve historical differences that existed in earlier updates even if later versions converged.
5. When two targets appear identical, record the evidence used to establish identity; do not collapse them by assumption.
6. When evidence conflicts, preserve the conflicting claims and their provenance until the discrepancy is resolved.

## Repository boundaries

- Do not commit retail ROM images, decrypted game images, console keys, or other redistributable game binaries.
- Reconstructed source, project data, analysis, manifests, tooling, documentation, and reviewable extracted/recreated assets may belong in the repository when they serve the decompilation project and their inclusion is appropriate.
- Public availability elsewhere does not by itself establish redistribution permission. Record provenance and repository-inclusion status separately.
- Temporary dumps, local caches, and disposable build output should remain outside version control unless they are intentionally promoted into documented project material.

## Platform-specific extensions

Do not force conventions from another generation or platform onto this project. Once executable, archive, resource, and build layouts are verified, add platform-specific naming, directory, manifest, and verification rules that reflect the actual target architecture.