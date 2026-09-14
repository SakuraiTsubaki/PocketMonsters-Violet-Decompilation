# Public Source Survey

This project currently has no local retail ROM/game dump. Reconstruction therefore begins with an exhaustive survey of publicly accessible evidence.

## Exhaustive means exhaustive

A category is not complete because one representative source was found. Every discoverable relevant page, repository, dataset, tool, archive, version, regional notice, language resource, event, distribution, and technical document must be enumerated or explicitly ruled out.

Japanese release/presentation is the comparison origin. This is a comparison axis, not an assumption that separate region-specific binaries exist.

## Required source families

| Family | Required coverage | Status |
| --- | --- | --- |
| Japanese official Pokémon/Nintendo | product pages, news archives, update notices, DLC, gifts, raids, outbreaks, competitions, regulations, HOME, purchase bonuses | Sweeping |
| Korean official Pokémon/Nintendo | same categories, independently enumerated | Sweeping |
| North American official Pokémon/Nintendo | same categories, independently enumerated | Sweeping |
| European and other official regional sites | every available localization/region and date/wording difference | Sweeping |
| Pokémon HOME | compatibility, transfer rules, app update history, research tasks and game-specific restrictions | Sweeping |
| GitHub reverse-engineering tools | parsers, editors, loaders, viewers, dumpers, hooks, debug tools, format libraries | Sweeping |
| GitHub datamines/datasets | text, personal data, moves, items, encounters, trainers, raids, maps, coordinates, events, distributions | Sweeping |
| File-format research | TRPFS/TRPFD, Trinity, FlatBuffers, text formats, models, animation, textures, shaders, audio, placement and hashes | Sweeping |
| Graphics/model resources | model/animation/import-export tooling and publicly referenced extracted resources; rights reviewed separately | Sweeping |
| Audio resources | banks, identifiers, cries, BGM, SFX, decoder/tool documentation | Sweeping |
| Maps/world | Paldea, Kitakami, Blueberry Academy, placement, raid/outbreak coordinates, fixed encounters and object maps | Sweeping |
| Mechanics | Terastal, raids, outbreaks, sandwiches, TM crafting, picnic, Let's Go, auctions, battle rules, online systems | Sweeping |
| Events/distributions | every Mystery Gift, serial/password distribution, event raid, outbreak, tournament reward and linked promotion | Sweeping |
| Competitive | every regulation, ranked season rule set, official online competition and championship rule variation | Sweeping |
| DLC/postgame | The Teal Mask, The Indigo Disk, epilogue, later updates and all associated events | Sweeping |
| Secondary databases | Bulbapedia, Serebii, Pokémon Database and other structured references, used for discovery/cross-checking | Sweeping |
| Project Pokémon / specialist communities | research threads, event galleries, tools, datamines and archived technical findings | Sweeping |
| Unused/deleted/debug material | documented unused data, leftovers, debug hooks/menus, placeholders and removed content | Sweeping |
| Historical/archived pages | retired official pages, old revisions, mirrors and web archives where legally/publicly accessible | Sweeping |

## Status vocabulary

- **Not started** — no systematic search yet.
- **Sweeping** — active broad search; results are incomplete.
- **Catalogued** — discovered sources are individually registered with provenance.
- **Cross-checked** — major claims have been compared against independent sources.
- **Exhausted** — multiple search strategies, languages, archives and source families have been searched with no remaining known uncatalogued leads. This status must not be used casually.

## Recording rule

Every result goes to GitHub. `manifests/public-source-catalog.csv` is the page/repository-level discovery catalog. `manifests/source-registry.json` contains higher-value source records and policy metadata. Detailed findings belong in `docs/`, structured reconstructed data in `data/`, tooling in `tools/`, and identity/provenance records in `manifests/`.

## Current sweep

The initial broad sweep has already identified official Japanese SV news/Portal/DLC archives; official update and HOME pages; pkNX; gftool; PokeDocs; KM Editor; SV multilingual text dumps; Titan reverse-engineering docs; ProjectSky; Pokémon Switch model/Blender tooling; Tera Raid live/map tooling; event galleries; map and sandwich datasets; runtime debug/Trinity bypass work; and major secondary databases. This is a discovery baseline only and is explicitly **not exhaustive yet**.
