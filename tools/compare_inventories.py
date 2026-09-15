#!/usr/bin/env python3
"""Compare two extracted-tree inventory manifests.

Inputs are JSON files produced by tools/inventory.py. The comparator never reads
retail game data; it compares only paths, sizes, hashes, and section labels.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_manifest(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "sakurai.extracted-tree-inventory.v1":
        raise ValueError(f"unsupported inventory schema: {data.get('schema')!r}")
    return data


def index_files(manifest: dict) -> dict[str, dict]:
    return {entry["path"]: entry for entry in manifest.get("files", [])}


def compare_manifests(left: dict, right: dict) -> dict:
    a = index_files(left)
    b = index_files(right)
    paths = sorted(set(a) | set(b))
    added, removed, changed, unchanged = [], [], [], []

    for path in paths:
        if path not in a:
            added.append(b[path])
        elif path not in b:
            removed.append(a[path])
        else:
            before, after = a[path], b[path]
            if before.get("sha256") == after.get("sha256") and before.get("size") == after.get("size"):
                unchanged.append(path)
            else:
                changed.append({
                    "path": path,
                    "before": {"section": before.get("section"), "size": before.get("size"), "sha256": before.get("sha256")},
                    "after": {"section": after.get("section"), "size": after.get("size"), "sha256": after.get("sha256")},
                })

    return {
        "schema": "sakurai.inventory-diff.v1",
        "left_tree_sha256": left.get("tree_sha256"),
        "right_tree_sha256": right.get("tree_sha256"),
        "summary": {"added": len(added), "removed": len(removed), "changed": len(changed), "unchanged": len(unchanged)},
        "added": added,
        "removed": removed,
        "changed": changed,
        "unchanged": unchanged,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare two extracted-tree inventories")
    parser.add_argument("left", type=Path)
    parser.add_argument("right", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("inventory-diff.json"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = compare_manifests(load_manifest(args.left), load_manifest(args.right))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = result["summary"]
    print(f"added={summary['added']} removed={summary['removed']} changed={summary['changed']} unchanged={summary['unchanged']}")
    print(f"wrote: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
