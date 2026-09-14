# Project Status

**Current stage:** Phase 0 — Public-source baseline inventory

This document tracks decompilation progress, target-version coverage, validation level, and the next major milestones.

## Operating conditions

- No local retail ROM, decrypted game image, or complete game dump is currently available to the project owner.
- Research is therefore proceeding from publicly accessible official sources, reverse-engineering projects, datamines, tools, technical documentation, databases, archives, and cross-checkable community findings.
- Japanese release / Japanese-language material is the origin reference for all regional and language comparisons.
- All project research results are intended to be recorded in this GitHub repository in reviewable form.

## Version inventory

| Target | Region / role | Language coverage | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Pokémon Violet | Japan origin reference | Japanese baseline | Launch → Ver. 4.0.0 currently seeded | Public-source evidence only | No local build/hash verification yet |
| Pokémon Violet | Global comparison set | 9 official languages currently enumerated | Launch → Ver. 4.0.0 currently seeded | Public-source evidence only | Region/package mapping still incomplete |

See `VERSIONS.md` for the authoritative language, update, DLC, and source baseline.

## Progress

- [x] Establish repository standards and verification vocabulary
- [x] Record the no-local-ROM public-source research condition
- [x] Define Japanese-origin comparative research policy
- [x] Seed official release date, supported-language list, DLC milestones, and latest-update baseline
- [ ] Exhaust first-party Japanese source inventory
- [ ] Exhaust first-party sources for every other official region/language
- [ ] Build the public GitHub / reverse-engineering / tooling source registry
- [ ] Build the public datamine / structured-data source registry
- [ ] Map storefront, package, region, language, revision, and update relationships
- [ ] Build complete historical update and DLC timeline
- [ ] Document executable and section layout from public technical evidence
- [ ] Map symbols, functions, and major subsystems where public evidence permits
- [ ] Document game-data formats and resource containers
- [ ] Reconstruct scripts, events, data, and behavior from attributable public evidence
- [ ] Reconstruct asset pipelines and metadata
- [ ] Add reproducible extraction/repacking tooling where inputs can be legally supplied by the user later
- [ ] Add automated verification where practical

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly by this project in a target build or extracted data.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is verified against the intended target.

Imported public datamines and third-party reverse-engineering claims retain their provenance and do not automatically count as **Observed**.

## Current limitations

Because no local target build is available, exact binary hashes, direct file identity, byte-exact matching, and runtime observations cannot currently be claimed by this project. Public sources can still be catalogued, compared, normalized, and used to reconstruct documented structures while those stronger verification levels remain pending.

## Next milestones

1. Build a source registry beginning with Japanese official material, then all other regional official material.
2. Enumerate public Scarlet/Violet reverse-engineering repositories, parsers, editors, format research, datamines, and structured datasets.
3. Expand `VERSIONS.md` from language coverage into concrete region/package/store/update identities.
4. Record every source with provenance, retrieval date, scope, confidence, and repository-inclusion status.
5. Select the first technical subsystem only after the source inventory shows where public evidence is strongest.

Update this file whenever the project reaches a meaningful milestone or adds a new supported target.