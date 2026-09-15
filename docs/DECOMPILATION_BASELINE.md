# Decompilation Baseline

This document freezes the first working baseline for the Pokémon Violet decompilation effort.

## Scope

Reconstruct Pokémon Violet code, data structures, scripts, resources, and behavior from independently obtained local research material. Retail game images, update packages, console keys, and redistributed proprietary binaries are not committed.

Historical revisions are retained as comparison targets rather than overwritten.

## Phase 1 — inventory and identity

- [x] Establish repository policy and ignore rules.
- [x] Record the official update matrix.
- [x] Add a deterministic local extracted-tree inventory tool.
- [ ] Run the inventory against verified Violet targets.
- [ ] Record file counts, total size, tree SHA-256, and per-file hashes.
- [ ] Identify executable-side files without speculative semantics.
- [ ] Identify major resource/data containers.

## Phase 2 — structural mapping

- map executable modules and sections;
- map major RomFS directory families and containers;
- record archive/compression/container signatures;
- compare Scarlet/Violet common and version-specific paths;
- select the first subsystem for source reconstruction.

## Phase 3 — source reconstruction

Priority: executable/module map → core readers → game-parameter tables → scripts/events → world/map data → graphics/UI/audio metadata → update/online/event-specific data.

## Repository boundary

Committed: source, scripts, schemas, manifests, hashes, metadata, documentation, recreated assets where appropriate, tests, and verification outputs.

Not committed: retail game images, update packages, console keys, decrypted proprietary executables copied verbatim, or raw local dumps.
