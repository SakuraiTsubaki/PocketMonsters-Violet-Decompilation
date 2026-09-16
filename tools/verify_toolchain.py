#!/usr/bin/env python3
"""Verify the local Generation IX reverse-engineering toolchain.

Uses only the Python standard library. It never reads console keys, firmware,
retail game images, or decrypted game content.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / ".local-tools"
LOCK = ROOT / "tools" / "toolchain.lock.json"


def command_ok(name: str) -> tuple[bool, str]:
    path = shutil.which(name)
    return (path is not None, path or "not found")


def git_head(path: Path) -> str | None:
    if not (path / ".git").exists():
        return None
    try:
        return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-partial", action="store_true", help="report missing tools without failing")
    args = parser.parse_args()
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    checks: list[tuple[str, bool, str]] = []

    for cmd in ["git", "curl", "unzip", "file", "cmake", "ninja", "clang", "llvm-objdump", "aarch64-linux-gnu-objdump", "aarch64-linux-gnu-readelf", "java", "zstd", "lz4"]:
        ok, detail = command_ok(cmd)
        checks.append((f"command:{cmd}", ok, detail))

    dotnet = TOOLS / "dotnet" / "dotnet"
    dotnet_ok = dotnet.is_file()
    detail = str(dotnet)
    if dotnet_ok:
        try:
            sdks = subprocess.check_output([str(dotnet), "--list-sdks"], text=True)
            dotnet_ok = lock["dotnet"]["sdk"] in sdks
            detail = sdks.strip().replace("\n", "; ")
        except (OSError, subprocess.CalledProcessError) as exc:
            dotnet_ok = False
            detail = str(exc)
    checks.append(("dotnet-sdk", dotnet_ok, detail))

    ghidra = TOOLS / "ghidra"
    checks.append(("ghidra", (ghidra / "ghidraRun").is_file() and (ghidra / "support" / "analyzeHeadless").is_file(), str(ghidra)))

    venv_python = TOOLS / "venv" / "bin" / "python"
    py_ok = venv_python.is_file()
    checks.append(("python-venv", py_ok, str(venv_python)))
    if py_ok:
        module_map = {"capstone":"capstone", "lief":"lief", "pyelftools":"elftools", "construct":"construct", "kaitaistruct":"kaitaistruct", "rich":"rich", "xxhash":"xxhash"}
        for label, module in module_map.items():
            code = f"import importlib.util,sys; sys.exit(0 if importlib.util.find_spec('{module}') else 1)"
            result = subprocess.run([str(venv_python), "-c", code], check=False)
            checks.append((f"python:{label}", result.returncode == 0, module))

    pknx = TOOLS / "src" / "pkNX"
    pknx_head = git_head(pknx)
    checks.append(("pkNX-commit", pknx_head == lock["pknx"]["commit"], pknx_head or "not cloned"))

    ryubing = TOOLS / "src" / "Ryubing"
    ryubing_head = git_head(ryubing)
    checks.append(("ryubing-commit", ryubing_head == lock["emulator"]["commit"], ryubing_head or "not cloned"))

    build_dir = TOOLS / "ryubing-build"
    checks.append(("ryubing-build", build_dir.is_dir() and any(build_dir.iterdir()), str(build_dir)))

    width = max(len(name) for name, _, _ in checks)
    failures = 0
    for name, ok, detail in checks:
        status = "OK" if ok else "MISSING"
        print(f"{name:<{width}}  {status:<7}  {detail}")
        failures += int(not ok)
    print(f"\nchecks={len(checks)} failures={failures}")
    return 0 if (not failures or args.allow_partial) else 1


if __name__ == "__main__":
    raise SystemExit(main())
