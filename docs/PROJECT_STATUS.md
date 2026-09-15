# Project Status

**Current stage:** Phase 1 — target identity and filesystem inventory

Pokémon Violet decompilation is active. The repository now has a deterministic extracted-tree inventory tool, tests, a version matrix, and a frozen baseline document.

## Progress

- [x] Establish repository policy and ignore rules
- [x] Record official update-version coverage
- [x] Add extracted-tree inventory tooling
- [x] Add deterministic inventory tests
- [ ] Run inventory against verified local Violet targets
- [ ] Map executable and section layout
- [ ] Map major RomFS directory families and containers
- [ ] Compare Scarlet/Violet common and version-specific paths
- [ ] Select and reconstruct the first subsystem

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a target build or extracted data.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Mapped** — structure and role are documented sufficiently for reconstruction.
- **Matched** — reconstructed output is verified against the intended target.

## Next milestone

Generate inventories from verified local targets, then build the first ExeFS/RomFS structural map and Scarlet/Violet cross-version path comparison.
