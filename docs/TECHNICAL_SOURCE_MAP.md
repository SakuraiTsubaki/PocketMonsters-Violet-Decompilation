# Technical Source Map

This document maps high-value public technical sources for Pokémon Violet. It is a public-source reconstruction aid, not a substitute for direct target-build observation.

## Evidence boundary

The project currently has no local retail ROM/game dump. Findings below are derived from public source code, documentation, datamines, and reverse-engineering tools. They remain public-source evidence unless independently reproduced against a verified target later.

## Save-data structure — PKHeX

Canonical source: `kwsch/PKHeX`.

`PKHeX.Core/Saves/Access/SaveBlockAccessor9SV.cs` exposes a dedicated `SAV9SV` block accessor shared by Scarlet/Violet family save handling. Public source currently identifies, among many others:

- box and party data
- items, trainer status, play time, Pokédex and configuration
- player fashion and appearance
- Paldea, Kitakami and Blueberry raid spawn lists
- seven-star raid capture/defeat history
- Blueberry Quest records and Club Room data
- money, League Points and Blueberry Points
- hidden-item status blocks for Paldea, Area Zero and Kitakami
- Mystery Gift and DLC gift blocks
- sandwich records
- field items and defeated-trainer history
- BCAT Tera Raid fixed rewards, lottery rewards, enemy data, priority data and version identifier
- BCAT mass-outbreak zones for Paldea, Kitakami and Blueberry plus outbreak Pokémon data
- player coordinates, rotation, field ID and current location ID
- fashion unlock blocks, profile pictures and trainer icons

Important revision evidence in the public source includes the seven-star raid defeat-history split introduced after 2.0.1 and an expanded defeated-trainer history block noted for 2.0.2+.

Do not treat block names, offsets or behavior as project `Observed` until verified against an identified target build.

## Tera Raid / Mass Outbreak research lineage

### Tera Finder — `Manu098vm/Tera-Finder`

PKHeX.Core-based Scarlet/Violet tool supporting raid/outbreak viewing and editing, Poké Portal News imports, RNG/reward calculations, legality seed reversal, progress/caught flags, and remote-device access.

Its credits link PKHeX, pkNX, SysBot.NET, RaidCrawler, sv-live-map, reward research, event group-ID research and disassembled-game pointer work.

### RaidCrawler — `LegoFigure11/RaidCrawler`

Public Scarlet/Violet sys-botbase raid viewer and an upstream source for RAM access, reward structures, search logic, coordinates and map-display research subsequently reused by other projects.

### Event Raid Injector — `Insektaure/Event-Raid-Injector`

Public tool targeting Scarlet/Violet 4.0.0 that preserves/imports historical Poké Portal raid-event and mass-outbreak data into saves. Useful for reconstructing event save/BCAT structures and seven-star capture flags, subject to official/independent cross-checking.

### pkTeraRaid / sv-live-map

Additional raid map coordinates, Paldea/Kitakami/Blueberry map presentation and save/RAM leads. Shared upstream coordinate dumps must not be counted as independent confirmations.

## FlatBuffers and resource metadata — PokeDocs

Canonical source: `pkZukan/PokeDocs`.

The dedicated `SV/` tree contains `Flatbuffers/` and `Hashlists/`. FlatBuffers is split into at least:

- `animation/`
- `customization/`
- `field/`
- `filesystem/`
- `model/`
- `pml/`
- `render/`
- `resources/`
- `scene/`

Each subtree must later be enumerated file-by-file.

## Trinity/container/tooling lineage

- `pkZukan/gftool` — TRPFS/TRPFD and Trinity serializers/viewers.
- `ChicoEevee/Pokemon-Switch-Model-Importer-Blender` — model/animation pipeline.
- `ChicoEevee/PokeModding-PLA-SV-Blender` — exporters and PokeDocs schema usage.
- `AncientDbri/Pokemon-Switch-Model-Importer-Plus` — derivative importer/exporter; only divergent work counts separately.
- `KillzXGaming/Switch-Toolbox` — archived historical format inspection tool.

## Text and structured game data

- `Pokemon-Project-com/sv-text` — multilingual common/script text.
- `kwsch/pkNX` — parsers/dumpers used by downstream legality/raid projects.
- `KotMatrosk1n/KM-Editor` — Pokémon/moves/items/trainers/encounters/gifts/trades/raids/shops/placement/models/audio models.
- `svfeplvce/ProjectSky` — personal/evolution/learnset/trainer editing lineage; deduplicate forks unless materially divergent.

## Next technical enumeration targets

Status remains **Sweeping**.

- enumerate every file under `PokeDocs/SV/Flatbuffers` and `SV/Hashlists`
- inventory PKHeX Gen9/SV save substructures and revision-specific block changes
- trace shared raid coordinate/reward/event data provenance
- enumerate Poké Portal/BCAT raid and outbreak structures and historical archives
- enumerate model, animation, texture, shader, audio and placement formats
- map tool/source support by revision
