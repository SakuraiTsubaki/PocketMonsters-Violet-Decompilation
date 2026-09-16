import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "tools" / "toolchain.lock.json"
BOOTSTRAP = ROOT / "tools" / "bootstrap_gen9_linux.sh"


class ToolchainDefinitionTests(unittest.TestCase):
    def test_lock_manifest_is_consistent(self):
        data = json.loads(LOCK.read_text(encoding="utf-8"))
        self.assertEqual(data["schema"], "sakurai.generation-ix-toolchain.v1")
        self.assertEqual(data["dotnet"]["sdk"], "10.0.401")
        self.assertEqual(data["ghidra"]["version"], "12.1.3")
        self.assertEqual(len(data["ghidra"]["sha256"]), 64)
        self.assertEqual(len(data["pknx"]["commit"]), 40)
        self.assertEqual(len(data["emulator"]["commit"]), 40)
        self.assertIn("prod.keys", data["non_repository_inputs"])
        self.assertIn("console firmware", data["non_repository_inputs"])

    def test_bootstrap_has_valid_bash_syntax(self):
        result = subprocess.run(["bash", "-n", str(BOOTSTRAP)], check=False, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_bootstrap_does_not_fetch_sensitive_inputs(self):
        text = BOOTSTRAP.read_text(encoding="utf-8").lower()
        self.assertNotIn("lockpick", text)
        self.assertNotIn("download firmware", text)
        self.assertNotIn("download keys", text)


if __name__ == "__main__":
    unittest.main()
