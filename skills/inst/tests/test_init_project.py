import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "initializer", ROOT / "scripts/init_project.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class InitializationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = self.root / "프로젝트 공백"
        self.project.mkdir()
        (self.project / "README.md").write_text("실제 요구", encoding="utf-8")
        self.output = self.root / "기록 공백"

    def run_init(self, **kwargs):
        return MODULE.initialize(self.project, self.output, ["README.md"], **kwargs)

    def test_creates_utf8_documents_with_explicit_inputs(self):
        paths = self.run_init(time_budget="90분")
        self.assertEqual({path.name for path in paths},
                         {"QNA.md", "USER_INTENT.md", "SPEC.md", "CHECKLIST.md"})
        content = (self.output / "CHECKLIST.md").read_text(encoding="utf-8")
        self.assertIn(str(self.project.resolve()), content)
        self.assertIn(str((self.project / "README.md").resolve()), content)
        self.assertIn("90분", content)
        self.assertNotIn("INVOCATION_MANIFEST", content)
        self.assertFalse((self.output / "HANDOFF.md").exists())
        self.assertTrue((self.output / "SPEC.md").exists())

    def test_checklist_is_created_as_unconfirmed_work(self):
        self.run_init()
        content = (self.output / "CHECKLIST.md").read_text(encoding="utf-8")
        rows = [line.split("|") for line in content.splitlines()
                if line.startswith(("| P1-", "| P2-", "| P3-", "| P4-", "| H-"))]
        self.assertTrue(rows)
        self.assertTrue(all(row[3].strip() == "대기" for row in rows))

    def test_existing_checklist_alone_blocks_initialization_and_is_preserved(self):
        self.output.mkdir()
        existing = "# 기존 점검\n| P3-01 | 재검토 | 사용자 기준 변경 |\n".encode("utf-8")
        (self.output / "CHECKLIST.md").write_bytes(existing)
        with self.assertRaises(ValueError):
            self.run_init()
        self.assertEqual((self.output / "CHECKLIST.md").read_bytes(), existing)
        self.assertEqual({p.name for p in self.output.iterdir()}, {"CHECKLIST.md"})

    def test_existing_user_answers_remain_byte_identical(self):
        self.output.mkdir()
        answer = "# 내 답\nA를 원함. 이유: 접근성을 우선.\n".encode("utf-8")
        (self.output / "QNA.md").write_bytes(answer)
        with self.assertRaises(ValueError):
            self.run_init()
        self.assertEqual((self.output / "QNA.md").read_bytes(), answer)
        self.assertEqual(len(list(self.output.iterdir())), 1)

    def test_second_invocation_preserves_every_document(self):
        self.run_init()
        before = {path.name: path.read_bytes() for path in self.output.iterdir()}
        with self.assertRaises(ValueError):
            self.run_init(time_budget="10분")
        self.assertEqual(before, {path.name: path.read_bytes() for path in self.output.iterdir()})

    def test_missing_source_does_not_create_output(self):
        with self.assertRaises(ValueError):
            MODULE.initialize(self.project, self.output, ["missing.md"])
        self.assertFalse(self.output.exists())

    def test_missing_project_does_not_create_output(self):
        with self.assertRaises(ValueError):
            MODULE.initialize(self.root / "missing", self.output, ["README.md"])
        self.assertFalse(self.output.exists())

    def test_optional_stakeholder_and_url_are_recorded_not_fetched(self):
        dialogue = self.project / "현업.md"
        dialogue.write_text("질의 기록", encoding="utf-8")
        MODULE.initialize(self.project, self.output, ["https://example.invalid/task"], [str(dialogue)])
        content = (self.output / "CHECKLIST.md").read_text(encoding="utf-8")
        self.assertIn("https://example.invalid/task", content)
        self.assertIn(str(dialogue.resolve()), content)


if __name__ == "__main__":
    unittest.main()
