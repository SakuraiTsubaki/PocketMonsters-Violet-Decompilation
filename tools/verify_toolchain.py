#!/usr/bin/env python3
"""Verify the local Generation IX reverse-engineering toolchain."""
from __future__ import annotations
import argparse, json, shutil, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / ".local-tools"
LOCK = ROOT / "tools" / "toolchain.lock.json"

def git_head(path: Path) -> str | None:
    if not (path / ".git").exists(): return None
    try: return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError): return None

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("--allow-partial", action="store_true"); args=p.parse_args()
    lock=json.loads(LOCK.read_text(encoding="utf-8")); checks=[]
    for cmd in ["git","curl","unzip","file","make","cmake","ninja","clang","llvm-objdump","aarch64-linux-gnu-objdump","aarch64-linux-gnu-readelf","java","zstd","lz4"]:
        path=shutil.which(cmd); checks.append((f"command:{cmd}",bool(path),path or "not found"))
    dotnet=TOOLS/"dotnet"/"dotnet"; ok=dotnet.is_file(); detail=str(dotnet)
    if ok:
        try:
            sdks=subprocess.check_output([str(dotnet),"--list-sdks"],text=True); ok=lock["dotnet"]["sdk"] in sdks; detail=sdks.strip().replace("\n","; ")
        except (OSError,subprocess.CalledProcessError) as exc: ok=False; detail=str(exc)
    checks.append(("dotnet-sdk",ok,detail))
    ghidra=TOOLS/"ghidra"; checks.append(("ghidra",(ghidra/"ghidraRun").is_file() and (ghidra/"support"/"analyzeHeadless").is_file(),str(ghidra)))
    hactool=TOOLS/"bin"/"hactool"; checks.append(("hactool",hactool.is_file(),str(hactool)))
    loader=TOOLS/"src"/"Ghidra-Switch-Loader"; head=git_head(loader); checks.append(("switch-loader-commit",head==lock["switch_loader"]["commit"],head or "not cloned"))
    ext=ghidra/"Ghidra"/"Extensions"; checks.append(("switch-loader-installed",ext.is_dir() and any("switch" in x.name.lower() for x in ext.iterdir()),str(ext)))
    py=TOOLS/"venv"/"bin"/"python"; checks.append(("python-venv",py.is_file(),str(py)))
    if py.is_file():
        for label,module in {"capstone":"capstone","lief":"lief","pyelftools":"elftools","construct":"construct","kaitaistruct":"kaitaistruct","rich":"rich","xxhash":"xxhash"}.items():
            rc=subprocess.run([str(py),"-c",f"import {module}"],check=False,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode; checks.append((f"python:{label}",rc==0,module))
    for label,key,folder in [("hactool-commit","hactool","hactool"),("pkNX-commit","pknx","pkNX"),("ryubing-commit","emulator","Ryubing")]:
        head=git_head(TOOLS/"src"/folder); checks.append((label,head==lock[key]["commit"],head or "not cloned"))
    build=TOOLS/"ryubing-build"; checks.append(("ryubing-build",build.is_dir() and any(build.iterdir()),str(build)))
    width=max(len(n) for n,_,_ in checks); failures=0
    for name,ok,detail in checks: print(f"{name:<{width}}  {'OK' if ok else 'MISSING':<7}  {detail}"); failures+=int(not ok)
    print(f"\nchecks={len(checks)} failures={failures}"); return 0 if failures==0 or args.allow_partial else 1
if __name__=="__main__": raise SystemExit(main())
