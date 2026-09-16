# Nintendo Switch-specific tools

The Generation IX bootstrap also installs Switch-specific reverse-engineering support:

- **hactool** (`SciresM/hactool`, pinned commit) for inspecting/extracting NCA, PFS0, RomFS, ExeFS, NPDM, NSO0 and related Switch formats. Any required keyset is user-supplied and remains outside this repository.
- **Ghidra Switch Loader** (`Adubbz/Ghidra-Switch-Loader`, pinned commit) built against the pinned Ghidra installation and installed into its local Extensions directory.

These are installed by `bash tools/bootstrap_gen9_linux.sh`. Set `GEN9_SKIP_SWITCH_TOOLS=1` only when both components are already managed externally.
