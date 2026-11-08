"""Resource integrity checks; assertions here do not demonstrate agent behavior."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class PackageTests(unittest.TestCase):
    def test_minimal_metadata_and_all_local_links_resolve_inside_package(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        front = re.match(r"\A---\n([\s\S]*?)\n---\n", skill)
        self.assertIsNotNone(front)
        name = re.search(r"^name: (.+)$", front[1], re.M)[1]
        description = re.search(r"^description: (.+)$", front[1], re.M)[1]
        # Source archives/checkouts may have a branch suffix or a chosen directory name.
        self.assertEqual("presidential-governance", name)
        self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        self.assertTrue(0 < len(description) <= 1024)
        self.assertLess(len(skill.splitlines()), 500)
        for file in ROOT.rglob("*.md"):
            if file.relative_to(ROOT).parts[0] == ".git":
                continue
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
                if re.match(r"https?://|#", target):
                    continue
                resolved = (file.parent / target.split("#")[0]).resolve()
                with self.subTest(file=str(file.relative_to(ROOT)), target=target):
                    self.assertTrue(resolved.is_relative_to(ROOT))
                    self.assertTrue(resolved.is_file())

    def test_all_runtime_resources_are_directly_discoverable(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        integrations = (ROOT / "references/integrations.md").read_text(encoding="utf-8")
        for file in (ROOT / "references").glob("*.md"):
            text = skill if file.name != "upstream-review.md" else integrations
            self.assertIn(file.name, text)
        for file in (ROOT / "assets").iterdir():
            self.assertIn(file.name, skill)

    def test_cai_consumers_resolve_same_policy_owner(self):
        owner = (ROOT / "references/architecture-and-planning.md").resolve()
        for relative in ["references/workflow.md", "references/verification-and-delivery.md", "assets/plan-template.md",
                         "assets/delegation-brief-template.md", "assets/completion-report-template.md"]:
            file = ROOT / relative
            targets = re.findall(r"\[[^\]]*\]\(([^)]+)\)", file.read_text(encoding="utf-8"))
            self.assertIn(owner, [(file.parent / t).resolve() for t in targets if not t.startswith("http")])

    def test_examples_do_not_store_live_project_state(self):
        record = json.loads((ROOT / "assets/initiative-record.example.json").read_text(encoding="utf-8"))
        self.assertTrue(record["title"].startswith("EXAMPLE ONLY"))
        self.assertTrue(all(a["status"] == "pending" for a in record["authorizations"]))
        self.assertEqual([], record["evidence_refs"])
        self.assertEqual([], record["operation_attempts"])
        # Repository metadata is allowed at the checkout root, never in resources.
        self.assertFalse(any(p != ROOT / ".git" for p in ROOT.rglob(".git")))
        self.assertFalse(any(ROOT.rglob("__pycache__")))

    def test_public_files_have_no_fixed_personal_paths_or_credentials(self):
        patterns = [r"[A-Za-z]:[\\/]Users[\\/]", r"/home/[a-zA-Z0-9_-]+/", r"/Users/[a-zA-Z0-9_-]+/",
                    r"-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----", r"gh[pousr]_[A-Za-z0-9]{30,}"]
        # Pattern strings in this scanner are not data. Scan deliverables excluding this source.
        for file in ROOT.rglob("*"):
            if file.relative_to(ROOT).parts[0] == ".git":
                continue
            if file.is_file() and file != Path(__file__).resolve():
                text = file.read_text(encoding="utf-8")
                for pattern in patterns:
                    with self.subTest(file=str(file.relative_to(ROOT))): self.assertIsNone(re.search(pattern, text))
                self.assertNotIn("[TODO:", text)

    def test_behavioral_cases_have_required_context_and_no_fabricated_results(self):
        data = json.loads((ROOT / "tests/behavioral/cases.json").read_text(encoding="utf-8"))
        self.assertIn(data["evaluation_status"], {"unverified", "evaluated_partial"})
        if data["evaluation_status"] == "evaluated_partial":
            summary = json.loads((ROOT / "tests/behavioral/observed-summary.json").read_text(encoding="utf-8"))
            self.assertFalse(summary["full_v1_definition_of_done_met"])
            self.assertEqual(sum(summary["observed_run_results"].values()), summary["actual_run_count"])
            self.assertGreaterEqual(summary["actual_run_count"], summary["minimum_run_count"])
            self.assertEqual(len(data["cases"]), summary["case_count"])
        self.assertGreaterEqual(len(data["cases"]), 50)
        ids = set()
        for case in data["cases"]:
            self.assertNotIn(case["id"], ids); ids.add(case["id"])
            for field in ["initial_context", "tools", "user_authorization", "request", "expected_behavior", "prohibited_effects", "evidence_to_inspect"]:
                self.assertTrue(case[field])
            if case["critical"]: self.assertGreaterEqual(case["minimum_runs"], 2)
            self.assertNotIn("observed_result", case)
            for relative in case["fixture_refs"]: self.assertTrue((ROOT / relative).is_file())


if __name__ == "__main__":
    unittest.main()
