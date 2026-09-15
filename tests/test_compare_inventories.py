import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "compare_inventories.py"
SPEC = importlib.util.spec_from_file_location("compare_tool", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
compare_tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(compare_tool)


def manifest(entries, tree="tree"):
    return {"schema": "sakurai.extracted-tree-inventory.v1", "tree_sha256": tree, "files": entries}


def entry(path, payload_hash, size=1, section="romfs"):
    return {"path": path, "sha256": payload_hash, "size": size, "section": section}


class CompareInventoryTests(unittest.TestCase):
    def test_added_removed_changed_and_unchanged(self):
        left = manifest([
            entry("romfs/same.bin", "same"),
            entry("romfs/change.bin", "old", 2),
            entry("romfs/remove.bin", "gone"),
        ], "left")
        right = manifest([
            entry("romfs/same.bin", "same"),
            entry("romfs/change.bin", "new", 3),
            entry("romfs/add.bin", "added"),
        ], "right")
        result = compare_tool.compare_manifests(left, right)
        self.assertEqual(result["summary"], {"added": 1, "removed": 1, "changed": 1, "unchanged": 1})
        self.assertEqual(result["added"][0]["path"], "romfs/add.bin")
        self.assertEqual(result["removed"][0]["path"], "romfs/remove.bin")
        self.assertEqual(result["changed"][0]["path"], "romfs/change.bin")
        self.assertEqual(result["unchanged"], ["romfs/same.bin"])

    def test_output_is_path_sorted(self):
        left = manifest([])
        right = manifest([entry("romfs/z.bin", "z"), entry("exefs/a", "a", section="exefs")])
        result = compare_tool.compare_manifests(left, right)
        self.assertEqual([item["path"] for item in result["added"]], ["exefs/a", "romfs/z.bin"])


if __name__ == "__main__":
    unittest.main()
