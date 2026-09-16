# Generation IX Decompilation Toolchain

This repository uses a pinned local toolchain for Pokémon Violet reverse engineering and runtime validation. Tool binaries and emulator builds live under `.local-tools/` and are not committed.

## One-command bootstrap

```bash
bash tools/bootstrap_gen9_linux.sh
source .local-tools/env.sh
python tools/verify_toolchain.py
```

The bootstrap installs/prepares **Ghidra 12.1.3**, LLVM/Clang, AArch64 GNU binutils, Python Capstone/LIEF/pyelftools/Construct/Kaitai tooling, **.NET SDK 10.0.401**, pinned **pkNX**, pinned **Ryubing/Ryujinx**, zstd/lz4, CMake and Ninja. Exact versions and commits are recorded in `tools/toolchain.lock.json`.

pkNX is a secondary Generation IX format/data research reference; its names and assumptions are independently verified against the target before adoption.

## Emulator boundary

The bootstrap builds emulator software only. It never downloads Nintendo Switch keys, firmware, retail games, updates, DLC, NSP/XCI/NCA files or decrypted game dumps. User-owned research inputs remain outside Git. Runtime validation requires a suitable local GPU/Vulkan environment; CI does not boot retail games.

## Optional bootstrap switches

`GEN9_SKIP_SYSTEM=1`, `GEN9_SKIP_DOTNET=1`, `GEN9_SKIP_GHIDRA=1`, `GEN9_SKIP_PKNX=1`, and `GEN9_SKIP_EMULATOR=1` skip components already managed elsewhere.

All generated tools live under `.local-tools/` and can be recreated at any time.
