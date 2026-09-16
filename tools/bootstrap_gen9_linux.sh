#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLS_DIR="$ROOT/.local-tools"
SRC_DIR="$TOOLS_DIR/src"
BIN_DIR="$TOOLS_DIR/bin"
DOTNET_DIR="$TOOLS_DIR/dotnet"
VENV_DIR="$TOOLS_DIR/venv"
GHIDRA_DIR="$TOOLS_DIR/ghidra"
RYUBING_BUILD="$TOOLS_DIR/ryubing-build"

DOTNET_VERSION="10.0.401"
GHIDRA_ARCHIVE="ghidra_12.1.3_PUBLIC_20260817.zip"
GHIDRA_SHA256="93a5d11a9ad510622acaaf908c556a7b9b764d338e78a7567f3689bf5081fd54"
GHIDRA_URL="https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_12.1.3_build/$GHIDRA_ARCHIVE"
PKNX_REPO="https://github.com/kwsch/pkNX.git"
PKNX_COMMIT="d191cd0e5c05f2af81d9a41c1f1d82e6621b351a"
HACTOOL_REPO="https://github.com/SciresM/hactool.git"
HACTOOL_COMMIT="1d64a83450e025622f3468c28fc4164dad2c5ef6"
SWITCH_LOADER_REPO="https://github.com/Adubbz/Ghidra-Switch-Loader.git"
SWITCH_LOADER_COMMIT="1f479fc8eb24479f0e5f74ccd4dd4103a10ac24d"
RYUBING_REPO="https://github.com/Leuconoe/Ryubing.git"
RYUBING_COMMIT="793ca017ff4f6e48b798a62d2486405bfc42ef39"

mkdir -p "$TOOLS_DIR" "$SRC_DIR" "$BIN_DIR"
run_root() { if [ "$(id -u)" -eq 0 ]; then "$@"; elif command -v sudo >/dev/null 2>&1; then sudo "$@"; else echo "error: root or sudo required" >&2; exit 1; fi; }

if [ "${GEN9_SKIP_SYSTEM:-0}" != "1" ]; then
  if command -v apt-get >/dev/null 2>&1; then
    run_root apt-get update
    run_root apt-get install -y git curl ca-certificates unzip jq file xxd build-essential make cmake ninja-build python3 python3-venv python3-pip clang llvm lld gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu openjdk-21-jdk zstd lz4 libvulkan1 mesa-vulkan-drivers libsdl2-2.0-0 libsdl2-dev libopenal1
  else echo "error: automatic system-package installation currently supports Debian/Ubuntu apt-get" >&2; exit 1; fi
fi

if [ "${GEN9_SKIP_DOTNET:-0}" != "1" ]; then
  if [ ! -x "$DOTNET_DIR/dotnet" ] || ! "$DOTNET_DIR/dotnet" --list-sdks 2>/dev/null | grep -q "^${DOTNET_VERSION}"; then
    tmp_install="$(mktemp)"; curl -fsSL https://dot.net/v1/dotnet-install.sh -o "$tmp_install"; bash "$tmp_install" --version "$DOTNET_VERSION" --install-dir "$DOTNET_DIR"; rm -f "$tmp_install"
  fi
fi
export DOTNET_ROOT="$DOTNET_DIR"; export PATH="$BIN_DIR:$DOTNET_DIR:$PATH"
python3 -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install --upgrade pip wheel
"$VENV_DIR/bin/python" -m pip install capstone lief pyelftools construct kaitaistruct rich xxhash

if [ "${GEN9_SKIP_GHIDRA:-0}" != "1" ] && [ ! -x "$GHIDRA_DIR/ghidraRun" ]; then
  tmp_dir="$(mktemp -d)"; curl -fL "$GHIDRA_URL" -o "$tmp_dir/$GHIDRA_ARCHIVE"; echo "$GHIDRA_SHA256  $tmp_dir/$GHIDRA_ARCHIVE" | sha256sum -c -; unzip -q "$tmp_dir/$GHIDRA_ARCHIVE" -d "$tmp_dir/unpacked"
  extracted="$(find "$tmp_dir/unpacked" -maxdepth 1 -mindepth 1 -type d -name 'ghidra_*_PUBLIC' | head -n1)"; test -n "$extracted"; rm -rf "$GHIDRA_DIR"; mv "$extracted" "$GHIDRA_DIR"; rm -rf "$tmp_dir"
fi

checkout_pinned() { local repo="$1" commit="$2" dest="$3"; if [ ! -d "$dest/.git" ]; then git clone "$repo" "$dest"; fi; git -C "$dest" fetch origin "$commit" --depth=1 || git -C "$dest" fetch origin; git -C "$dest" checkout --detach "$commit"; }

if [ "${GEN9_SKIP_SWITCH_TOOLS:-0}" != "1" ]; then
  checkout_pinned "$HACTOOL_REPO" "$HACTOOL_COMMIT" "$SRC_DIR/hactool"
  cp "$SRC_DIR/hactool/config.mk.template" "$SRC_DIR/hactool/config.mk"; make -C "$SRC_DIR/hactool"; install -m 0755 "$SRC_DIR/hactool/hactool" "$BIN_DIR/hactool"
  if [ -x "$GHIDRA_DIR/ghidraRun" ]; then
    checkout_pinned "$SWITCH_LOADER_REPO" "$SWITCH_LOADER_COMMIT" "$SRC_DIR/Ghidra-Switch-Loader"
    java_bin="$(readlink -f "$(command -v javac)")"; export JAVA_HOME="$(dirname "$(dirname "$java_bin")")"
    (cd "$SRC_DIR/Ghidra-Switch-Loader" && GHIDRA_INSTALL_DIR="$GHIDRA_DIR" ./gradlew -PGHIDRA_INSTALL_DIR="$GHIDRA_DIR")
    ext_zip="$(find "$SRC_DIR/Ghidra-Switch-Loader/dist" -maxdepth 1 -type f -name '*.zip' | head -n1)"; test -n "$ext_zip"; mkdir -p "$GHIDRA_DIR/Ghidra/Extensions"
    first_entry="$(unzip -Z1 "$ext_zip" | head -n1)"; if [[ "$first_entry" == Ghidra/Extensions/* ]]; then unzip -q -o "$ext_zip" -d "$GHIDRA_DIR"; else unzip -q -o "$ext_zip" -d "$GHIDRA_DIR/Ghidra/Extensions"; fi
  fi
fi

if [ "${GEN9_SKIP_PKNX:-0}" != "1" ]; then checkout_pinned "$PKNX_REPO" "$PKNX_COMMIT" "$SRC_DIR/pkNX"; fi
if [ "${GEN9_SKIP_EMULATOR:-0}" != "1" ]; then checkout_pinned "$RYUBING_REPO" "$RYUBING_COMMIT" "$SRC_DIR/Ryubing"; git -C "$SRC_DIR/Ryubing" submodule update --init --recursive; rm -rf "$RYUBING_BUILD"; "$DOTNET_DIR/dotnet" build "$SRC_DIR/Ryubing" -c Release -o "$RYUBING_BUILD"; fi

cat > "$TOOLS_DIR/env.sh" <<EOF
export GEN9_TOOLS="$TOOLS_DIR"
export DOTNET_ROOT="$DOTNET_DIR"
export GHIDRA_HOME="$GHIDRA_DIR"
export PATH="$VENV_DIR/bin:$BIN_DIR:$DOTNET_DIR:$GHIDRA_DIR:\$PATH"
EOF

cat <<EOF
Generation IX toolchain ready.
  Ghidra:         $GHIDRA_DIR
  Switch loader:  $SRC_DIR/Ghidra-Switch-Loader
  hactool:        $BIN_DIR/hactool
  pkNX:           $SRC_DIR/pkNX
  Ryubing:        $RYUBING_BUILD
Activate: source .local-tools/env.sh
Verify:   python tools/verify_toolchain.py
No console keys, firmware, retail game images, updates/DLC, or decrypted game dumps were downloaded by this script.
EOF
