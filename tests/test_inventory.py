import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "inventory.py"
SPEC = importlib.util.spec_from_file_location("inventory_tool", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
inventory_tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory_tool)

class InventoryTests(unittest.TestCase):
    def test_build_inventory_is_sorted_and_hashes_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "violet"
            (root / "romfs" / "data").mkdir(parents=True)
            (root / "exefs").mkdir(parents=True)
            (root / "romfs" / "data" / "b.bin").write_bytes(b"beta")
            (root / "exefs" / "main").write_bytes(b"alpha")
            result = inventory_tool.build_inventory(root)
            self.assertEqual(result["file_count"], 2)
            self.assertEqual(result["total_bytes"], 9)
            self.assertEqual(result["section_counts"], {"exefs": 1, "romfs": 1})
            self.assertEqual([r["path"] for r in result["files"]], ["exefs/main", "romfs/data/b.bin"])
            self.assertEqual(result["files"][0]["sha256"], hashlib.sha256(b"alpha").hexdigest())
            self.assertEqual(result["files"][1]["sha256"], hashlib.sha256(b"beta").hexdigest())

    def test_tree_digest_ignores_absolute_root_location(self):
        with tempfile.TemporaryDirectory() as tmp_a, tempfile.TemporaryDirectory() as tmp_b:
            root_a = Path(tmp_a) / "a"
            root_b = Path(tmp_b) / "b"
            for root in (root_a, root_b):
                (root / "romfs").mkdir(parents=True)
                (root / "romfs" / "same.bin").write_bytes(b"same-content")
            self.assertEqual(inventory_tool.build_inventory(root_a)["tree_sha256"], inventory_tool.build_inventory(root_b)["tree_sha256"])

if __name__ == "__main__":
    unittest.main()
