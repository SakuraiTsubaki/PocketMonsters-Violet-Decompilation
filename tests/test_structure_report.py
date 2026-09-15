import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "structure_report.py"
SPEC = importlib.util.spec_from_file_location("structure_report_tool", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
structure_report = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(structure_report)


class StructureReportTests(unittest.TestCase):
    def test_summary_groups_section_extension_and_top_level(self):
        inventory = {
            "schema": "sakurai.extracted-tree-inventory.v1",
            "tree_sha256": "tree",
            "files": [
                {"path": "exefs/main", "section": "exefs", "size": 100, "sha256": "a"},
                {"path": "romfs/data/a.bin", "section": "romfs", "size": 40, "sha256": "b"},
                {"path": "romfs/data/b.BIN", "section": "romfs", "size": 60, "sha256": "c"},
                {"path": "romfs/text/readme.txt", "section": "romfs", "size": 10, "sha256": "d"},
            ],
        }

        report = structure_report.summarize(inventory, largest_limit=2)

        self.assertEqual(report["file_count"], 4)
        self.assertEqual(report["total_bytes"], 210)
        self.assertEqual(report["sections"]["exefs"], {"files": 1, "bytes": 100})
        self.assertEqual(report["sections"]["romfs"], {"files": 3, "bytes": 110})
        self.assertEqual(report["extensions"][".bin"], {"files": 2, "bytes": 100})
        self.assertEqual(report["extensions"]["<none>"], {"files": 1, "bytes": 100})
        self.assertEqual(report["top_level"]["romfs"], {"files": 3, "bytes": 110})
        self.assertEqual([x["path"] for x in report["largest_files"]], ["exefs/main", "romfs/data/b.BIN"])


if __name__ == "__main__":
    unittest.main()
