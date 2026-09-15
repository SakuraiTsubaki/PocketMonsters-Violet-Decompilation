#!/usr/bin/env python3
"""Create a reproducible inventory for an already-extracted game tree.

This tool does not extract, decrypt, or redistribute game content. It scans a
local directory, records relative paths, sizes and SHA-256 digests, and writes a
JSON manifest suitable for version-to-version comparison.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

CHUNK_SIZE = 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def classify(relative_path: Path) -> str:
    if not relative_path.parts:
        return "unknown"
    top = relative_path.parts[0].lower()
    if top in {"exefs", "romfs"}:
        return top
    return "other"


def iter_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*"), key=lambda p: p.as_posix()):
        if path.is_symlink():
            continue
        if path.is_file():
            yield path


def build_inventory(root: Path) -> dict:
    records = []
    tree_digest = hashlib.sha256()
    section_counts: dict[str, int] = {}
    total_bytes = 0

    for path in iter_files(root):
        relative = path.relative_to(root)
        relative_posix = relative.as_posix()
        size = path.stat().st_size
        digest = sha256_file(path)
        section = classify(relative)
        records.append({"path": relative_posix, "section": section, "size": size, "sha256": digest})
        total_bytes += size
        section_counts[section] = section_counts.get(section, 0) + 1
        tree_digest.update(relative_posix.encode("utf-8"))
        tree_digest.update(b"\0")
        tree_digest.update(str(size).encode("ascii"))
        tree_digest.update(b"\0")
        tree_digest.update(digest.encode("ascii"))
        tree_digest.update(b"\n")

    return {
        "schema": "sakurai.extracted-tree-inventory.v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_root_name": root.name,
        "file_count": len(records),
        "total_bytes": total_bytes,
        "section_counts": dict(sorted(section_counts.items())),
        "tree_sha256": tree_digest.hexdigest(),
        "files": records,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inventory an already-extracted game directory.")
    parser.add_argument("root", type=Path, help="Extracted game directory to scan")
    parser.add_argument("-o", "--output", type=Path, default=Path("inventory.json"), help="Output JSON path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"error: not a directory: {root}")
    inventory = build_inventory(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"files: {inventory['file_count']}")
    print(f"bytes: {inventory['total_bytes']}")
    print(f"tree sha256: {inventory['tree_sha256']}")
    print(f"wrote: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
