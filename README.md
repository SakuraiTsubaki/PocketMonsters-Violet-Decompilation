# Pocket Monsters Violet — Decompilation

![Status](https://img.shields.io/badge/status-phase_1_active-blue)
![Project](https://img.shields.io/badge/project-decompilation-blue)
![ROMs](https://img.shields.io/badge/ROM_binaries-not_included-success)

Decompilation and source-reconstruction project for **Pokémon Violet**.

## 🚧 Status

**Phase 1 is active:** target identity, update coverage, reproducible extracted-tree inventory, and initial filesystem mapping.

Current working material includes:

- `tools/inventory.py` — deterministic per-file SHA-256 inventory for already-extracted local research trees.
- `tests/test_inventory.py` — regression coverage for sorting, hashing, and tree-digest reproducibility.
- `manifests/version-matrix.json` — historical update targets retained for comparison.
- `docs/DECOMPILATION_BASELINE.md` — first reconstruction phases and evidence rules.

## 🎯 Goals

- Reconstruct game code and data into readable, editable source form.
- Document executable structures, data formats, scripts, assets, and version differences.
- Compare Scarlet and Violet without collapsing version-specific behavior or data.
- Keep analysis, tooling, metadata, and documentation reproducible.

## 📌 Repository policy

Retail game images, raw dumps, update packages, console keys, and redistributed proprietary executables are not committed. Reconstructed source, tooling, schemas, manifests, hashes, documentation, tests, metadata, and appropriate recreated/extracted project assets may be tracked.

## 🧭 Active roadmap

- [x] Establish clean repository baseline
- [x] Add deterministic inventory tooling and tests
- [x] Record update-version matrix
- [ ] Inventory verified local targets
- [ ] Map ExeFS/RomFS structure
- [ ] Build Scarlet/Violet path and subsystem comparisons
- [ ] Begin subsystem source reconstruction
- [ ] Add matched-output verification where practical

See `docs/PROJECT_STATUS.md` and `docs/DECOMPILATION_BASELINE.md` for the active workflow.
