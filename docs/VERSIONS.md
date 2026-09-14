# Version Coverage

Use this document as the authoritative inventory of game versions targeted by this decompilation project.

## Research baseline

The project currently has no local retail ROM, decrypted game image, or complete game dump. Version coverage therefore begins from public-source evidence. Japanese release / Japanese-language material is the origin reference for comparison, but this does not imply that Japan necessarily uses a distinct binary or package-internal data set.

## Initial official-source baseline

- **Title:** Pokémon Violet
- **Original release date:** 2022-11-18
- **Platform:** Nintendo Switch; Nintendo Switch 2 compatibility enhancements are provided through the later software update path.
- **Latest software update confirmed in this baseline:** Ver. 4.0.0
- **Japanese official Ver. 4.0.0 notice date:** 2025-06-03
- **Officially listed languages:** Japanese, American English, French, German, Italian, Spanish, Korean, Simplified Chinese, Traditional Chinese
- **DLC family:** The Hidden Treasure of Area Zero; New Uniform Set; Part 1: The Teal Mask; Part 2: The Indigo Disk

These facts are public-source baseline facts, not hash-verified target identities.

## Language / regional comparison inventory

| Status | Baseline role | Region / distribution mapping | Language | Revision / update | Platform / build | Hashes | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Planned | Origin reference | Japan reference | Japanese | Launch through Ver. 4.0.0 | Nintendo Switch / Switch 2 compatibility | unavailable | Official primary | Starting comparison point; package/build identity still to be mapped |
| Planned | Compare to JP | TBD | American English | Launch through Ver. 4.0.0 | Nintendo Switch / Switch 2 compatibility | unavailable | Official primary | Officially supported language |
| Planned | Compare to JP | TBD | French | Launch through Ver. 4.0.0 | Nintendo Switch / Switch 2 compatibility | unavailable | Official primary | Officially supported language |
| Planned | Compare to JP | TBD | German | Launch through Ver. 4.0.0 | Nintendo Switch / Switch 2 compatibility | unavailable | Official primary | Officially supported language |
| Planned | Compare to JP | TBD | Italian | Launch through Ver. 4.0.0 | Nintendo Switch / Switch 2 compatibility | unavailable | Official primary | Officially supported language |
| Planned | Compare to JP | TBD | Spanish | Launch through Ver. 4.0.0 | Nintendo Switch / Switch 2 compatibility | unavailable | Official primary | Officially supported language |
| Planned | Compare to JP | TBD | Korean | Launch through Ver. 4.0.0 | Nintendo Switch / Switch 2 compatibility | unavailable | Official primary | Officially supported language |
| Planned | Compare to JP | TBD | Simplified Chinese | Launch through Ver. 4.0.0 | Nintendo Switch / Switch 2 compatibility | unavailable | Official primary | Officially supported language |
| Planned | Compare to JP | TBD | Traditional Chinese | Launch through Ver. 4.0.0 | Nintendo Switch / Switch 2 compatibility | unavailable | Official primary | Officially supported language |

## Update / DLC milestones currently seeded

| Date | Version / content | Scope | Evidence state | Notes |
| --- | --- | --- | --- | --- |
| 2022-11-18 | Launch | Base game | Official primary | Global release date listed by Nintendo |
| 2023-02-27 | The Hidden Treasure of Area Zero bundle / New Uniform Set | DLC | Official primary | DLC storefront milestone |
| 2023-09-13 | Part 1: The Teal Mask | DLC | Official primary | DLC release milestone |
| 2023-12-14 | Part 2: The Indigo Disk | DLC | Official primary | DLC release milestone |
| 2025-06-03 (JP notice) | Ver. 4.0.0 | Update | Official primary | Japanese notice; includes Nintendo Switch 2 enhancements. Other regional support pages may display 2025-06-02 because of local date/time handling. |

## Primary sources seeded in Phase 0

- Japanese Pokémon Scarlet/Violet update notice (Ver. 4.0.0): https://sv-news.pokemon.co.jp/ja/page/350.html
- Nintendo US Pokémon Violet product page: https://www.nintendo.com/us/store/products/pokemon-violet-switch/
- Nintendo US Scarlet/Violet update history: https://en-americas-support.nintendo.com/app/answers/detail/a_id/60277

## Status vocabulary

- **Planned** — intended for investigation but not yet directly verified against a target build.
- **Verified** — identity and hashes confirmed.
- **Mapped** — executable/data layout documented.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the target.
- **Reference only** — used for comparison but not a reconstruction target.

## Recording rules

1. Record exact revision/update information whenever known.
2. Prefer cryptographic hashes over filenames as identity evidence.
3. Do not commit retail game images or console keys.
4. Record regional or language differences instead of assuming two releases are identical.
5. Start comparisons from the Japanese reference baseline, then enumerate every official language and distribution region discovered.
6. Treat storefront/package region, language resources, executable identity, event availability, and service behavior as separate comparison axes.
7. Preserve local-date differences in official regional update notices rather than normalizing them away without explanation.
8. Link version-specific findings to relevant documentation, manifests, sources, or verification issues.