# Violet — Exhaustive Defect Eradication

## Target

- Game: Pocket Monsters Violet
- Generation: IX
- Latest official upstream software version checked: 4.0.0 (2025-06-02)
- Local ROM/package identity: **not yet selected in `config/target.json`**
- Completion claim: **not permitted until the local target hash/build is recorded and verified**

## Policy

Use the common workflow in `SakuraiTsubaki/Decompilation/docs/bug-eradication.md`.

The initial cross-target defect inventory is maintained in:

- `SakuraiTsubaki/Decompilation/manifests/generation-ix-known-defects.csv`

For Violet, include every row targeting `Violet` or `Scarlet|Violet`, plus every newly discovered Violet-only defect.

## Mandatory Violet coverage

- base game and every retained update delta
- The Teal Mask
- The Indigo Disk
- Mochi Mayhem / epilogue content
- Poké Portal News and historical event payloads
- Tera Raid Battle state/rewards/network behavior
- Battle Stadium / ranked / official competition behavior
- Pokémon HOME transfer/import interactions
- Violet-only encounter/data/event differences
- Miraidon-specific field/battle/model behavior
- Uva Academy-specific content and text
- Nintendo Switch and 4.0.0 Switch 2 behavior differences
- long-session performance/resource behavior

## First execution gate

Before binary-derived fixes:

1. Identify the exact local Violet input build and update/DLC combination.
2. Record hashes in `config/target.json` or a linked target manifest.
3. Inventory executable/data containers and extracted file hashes.
4. Re-test every applicable `REPRODUCTION_NEEDED_ON_LATEST` row.
5. Diff official update generations for every `DIFF_REQUIRED` row.
6. Create one regression test per confirmed bug before closure.

## Zero-known-defect rule

No confirmed bug, glitch, exploit, data error, crash, softlock, progression failure, performance defect, collision fault, visual/audio/UI error, networking desync, event-data defect, or version-integration error may be excluded merely because it is minor or historical.

Historical defects stay documented; the reconstructed/latest project behavior must not reproduce them unless the behavior is separately proven intentional.

## Primary public baselines

- Nintendo Support: Pokémon Scarlet / Violet update history
- Bulbapedia: List of glitches in Generation IX

Public reports are leads. Local target reproduction and binary/data evidence decide the final status.
