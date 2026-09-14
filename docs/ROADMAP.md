# Roadmap

This roadmap defines the recommended order for turning this repository from a public-source research scaffold into a reproducible decompilation and source-reconstruction project.

## Phase 0 — Public-source target definition

### 0A — Operating baseline
- [x] Record that no local retail ROM, decrypted game image, or complete game dump is currently available.
- [x] Define Japanese release / Japanese-language material as the origin reference for comparison.
- [x] Separate source provenance from direct project verification levels.
- [x] Require project research outputs to be committed to GitHub in reviewable form.

### 0B — First-party source inventory
- [ ] Exhaust official Japanese product, support, patch, DLC, event, distribution, service, and archival material.
- [ ] Repeat the official-source inventory for every other supported region and language.
- [ ] Record local-date, wording, storefront, packaging, ratings, distribution, and service differences.

### 0C — Public technical-source inventory
- [ ] Enumerate public GitHub reverse-engineering repositories, parsers, editors, decompilers, format research, and tooling.
- [ ] Enumerate public datamines, structured datasets, text dumps, manifests, and technical write-ups.
- [ ] Record licenses, redistribution constraints, source scope, target versions, and maintenance status.

### 0D — Version / region / language matrix
- [ ] Expand `VERSIONS.md` into all known regions, languages, revisions, updates, DLC states, and distribution variants.
- [ ] Distinguish language differences from package/store region and binary/resource differences.
- [ ] Identify authoritative target identities and hashes whenever public evidence makes them available.
- [ ] Preserve unresolved conflicts instead of normalizing them away.

## Phase 1 — Binary, container, and resource mapping from public evidence
- [ ] Document executable layout, sections, overlays, archives, and resource containers where public technical evidence permits.
- [ ] Build file/path/format manifests from attributable public sources.
- [ ] Record known compression, packing, hashing, serialization, and resource-index formats.
- [ ] Mark claims that still require direct target verification.

## Phase 2 — Symbol and subsystem mapping
- [ ] Name functions, symbols, tables, and major data structures only when evidence supports the mapping.
- [ ] Identify engine subsystems and dependencies.
- [ ] Track source provenance, confidence, target version, and unresolved alternatives for each finding.

## Phase 3 — Source and data reconstruction
- [ ] Reconstruct code into readable, maintainable source where sufficient public evidence exists.
- [ ] Reconstruct scripts, data tables, text structures, event structures, and asset metadata.
- [ ] Add conversion, analysis, validation, and repacking tools where needed.
- [ ] Keep public-source reconstruction claims separate from later exact target matching.

## Phase 4 — Verification
- [ ] Add repeatable tests and comparison workflows that do not require redistributing retail game binaries.
- [ ] Track behaviorally reproduced, structurally reproduced, and exactly matched results separately.
- [ ] When a legally supplied local target becomes available in the future, use it to promote eligible findings from external evidence to Observed/Reproduced/Matched status.
- [ ] Document remaining mismatches and unknowns.

## Phase 5 — Reproducible project workflow
- [ ] Provide documented setup and reconstruction/repack steps.
- [ ] Add CI or automated verification where practical.
- [ ] Keep generated outputs reproducible from repository sources and tooling.
- [ ] Maintain a complete provenance trail from Japanese-origin comparison through every regional/language/version variant.