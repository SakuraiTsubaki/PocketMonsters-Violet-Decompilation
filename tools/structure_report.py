#!/usr/bin/env python3
"""Summarize a decompilation inventory without redistributing game data."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def load_inventory(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("files"), list):
        raise ValueError("inventory must contain a files list")
    return data


def _extension(path: str) -> str:
    suffix = Path(path).suffix.lower()
    return suffix if suffix else "<none>"


def _top_level(path: str) -> str:
    parts = Path(path).parts
    return parts[0] if parts else "<root>"


def summarize(inventory: dict, largest_limit: int = 25) -> dict:
    sections: dict[str, dict[str, int]] = defaultdict(lambda: {"files": 0, "bytes": 0})
    extensions: dict[str, dict[str, int]] = defaultdict(lambda: {"files": 0, "bytes": 0})
    top_level: dict[str, dict[str, int]] = defaultdict(lambda: {"files": 0, "bytes": 0})

    normalized = []
    for record in inventory["files"]:
        path = str(record["path"])
        size = int(record["size"])
        section = str(record.get("section", "unknown"))

        sections[section]["files"] += 1
        sections[section]["bytes"] += size
        extensions[_extension(path)]["files"] += 1
        extensions[_extension(path)]["bytes"] += size
        top_level[_top_level(path)]["files"] += 1
        top_level[_top_level(path)]["bytes"] += size
        normalized.append({"path": path, "section": section, "size": size, "sha256": record.get("sha256")})

    largest = sorted(normalized, key=lambda r: (-r["size"], r["path"]))[:largest_limit]

    def ordered(mapping: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
        return {key: mapping[key] for key in sorted(mapping)}

    return {
        "schema": "sakurai.structure-report.v1",
        "source_schema": inventory.get("schema"),
        "source_tree_sha256": inventory.get("tree_sha256"),
        "file_count": len(normalized),
        "total_bytes": sum(r["size"] for r in normalized),
        "sections": ordered(sections),
        "extensions": ordered(extensions),
        "top_level": ordered(top_level),
        "largest_files": largest,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize an extracted-tree inventory JSON file.")
    parser.add_argument("inventory", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("structure-report.json"))
    parser.add_argument("--largest", type=int, default=25, help="Number of largest files to retain")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.largest < 0:
        raise SystemExit("error: --largest must be non-negative")
    report = summarize(load_inventory(args.inventory), args.largest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"files: {report['file_count']}")
    print(f"bytes: {report['total_bytes']}")
    print(f"wrote: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
