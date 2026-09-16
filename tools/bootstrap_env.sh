#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLS_DIR="$ROOT_DIR/.tools"; BIN_DIR="$TOOLS_DIR/bin"; SRC_DIR="$TOOLS_DIR/src"; EMU_DIR="$TOOLS_DIR/emulators"
mkdir -p "$BIN_DIR" "$SRC_DIR" "$EMU_DIR"
if [[ -d "$ROOT_DIR/.git" ]]; then touch "$ROOT_DIR/.git/info/exclude"; grep -qxF '.tools/' "$ROOT_DIR/.git/info/exclude" || echo '.tools/' >> "$ROOT_DIR/.git/info/exclude"; fi
if [[ "$(id -u)" -eq 0 ]]; then SUDO=(); elif command -v sudo >/dev/null 2>&1; then SUDO=(sudo); else SUDO=(); fi
if command -v apt-get >/dev/null 2>&1; then "${SUDO[@]}" apt-get update || true; DEBIAN_FRONTEND=noninteractive "${SUDO[@]}" apt-get install -y --no-install-recommends ca-certificates curl git make cmake ninja-build python3 build-essential llvm clang lld || true; fi
if [[ ! -x "$BIN_DIR/hactool" ]]; then rm -rf "$SRC_DIR/hactool"; git clone --depth 1 https://github.com/SciresM/hactool.git "$SRC_DIR/hactool"; make -C "$SRC_DIR/hactool" -j"$(getconf _NPROCESSORS_ONLN 2>/dev/null || echo 2)"; ln -sfn "$SRC_DIR/hactool/hactool" "$BIN_DIR/hactool"; fi
JSON_FILE="$(mktemp)"; trap 'rm -f "$JSON_FILE"' EXIT
if curl -fsSL https://nightly.eden-emu.dev/latest/release.json -o "$JSON_FILE"; then URL="$(python3 - "$JSON_FILE" <<'PY'
import json,sys
stack=[json.load(open(sys.argv[1],encoding='utf-8'))]
while stack:
 x=stack.pop()
 if isinstance(x,dict): stack.extend(x.values())
 elif isinstance(x,list): stack.extend(x)
 elif isinstance(x,str):
  s=x.lower()
  if x.startswith('http') and s.endswith('.appimage') and ('amd64' in s or 'x86_64' in s) and 'pgo' in s:
   print(x); break
PY
)"; if [[ -n "$URL" && ! -x "$EMU_DIR/Eden.AppImage" ]]; then curl -fL --retry 3 "$URL" -o "$EMU_DIR/Eden.AppImage" && chmod +x "$EMU_DIR/Eden.AppImage"; fi; fi
printf 'export PATH="%s:$PATH"\n' "$BIN_DIR" > "$TOOLS_DIR/activate.sh"
printf '%s\n' 'Toolchain ready. Use only your own legally dumped game data, firmware, and keys.'
