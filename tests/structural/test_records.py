"""Structural consistency tests, not agent or human-approval evaluations."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("record_validator", ROOT / "scripts/validate_records.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)
BASE = json.loads((ROOT / "assets/initiative-record.example.json").read_text(encoding="utf-8"))
CONFIG = json.loads((ROOT / "assets/project-config.example.json").read_text(encoding="utf-8"))


def fixture():
    return copy.deepcopy(BASE)


def claim_grant(record):
    record["source_refs"].append({"id": "approval-claim", "kind": "approval", "locator": "example-only:forged-source"})
    record["authorizations"][0].update(status="granted", evidence_ref="approval-claim")


class RecordTests(unittest.TestCase):
    def test_examples_are_valid_and_pending(self):
        self.assertEqual([], validator.validate_record(BASE))
        self.assertEqual([], validator.validate_config(CONFIG))
        self.assertEqual("pending", BASE["authorizations"][0]["status"])

    def test_shape_rejects_missing_wrong_or_unknown_fields(self):
        cases = []
        missing = fixture(); del missing["source_refs"]; cases.append((missing, "source_refs"))
        wrong = fixture(); wrong["record_revision"] = True; cases.append((wrong, "record_revision"))
        wrong = fixture(); wrong["authorizations"] = {}; cases.append((wrong, "authorizations"))
        wrong = fixture(); wrong["work_state"] = "approved"; cases.append((wrong, "work_state"))
        wrong = fixture(); wrong["authorizations"][0]["scope"] = None; cases.append((wrong, "scope"))
        wrong = fixture(); wrong["schema_version"] = "99"; cases.append((wrong, "schema_version"))
        wrong = fixture(); wrong["initiative_id"] = "not-a-uuid"; cases.append((wrong, "initiative_id"))
        wrong = fixture(); wrong["next_action"] = " "; cases.append((wrong, "next_action"))
        wrong = fixture(); wrong["approval_verified"] = True; cases.append((wrong, "unknown field"))
        for record, fragment in cases:
            with self.subTest(fragment=fragment):
                self.assertTrue(any(fragment in error for error in validator.validate_record(record)))

    def test_arbitrary_json_types_do_not_crash(self):
        for value in [None, True, 42, "text", [], {}, {"record_revision": []}]:
            with self.subTest(value=value):
                self.assertTrue(validator.validate_record(value))
                self.assertTrue(validator.validate_config(value))

    def test_configuration_cannot_disable_governance(self):
        for field, value in [("cai", False), ("authorization_required", False), ("delegation", "automatic"), ("planning_depth", "none")]:
            config = copy.deepcopy(CONFIG); config[field] = value
            with self.subTest(field=field):
                self.assertTrue(validator.validate_config(config))
        for mode in ["Professional", "Presidential"]:
            config = copy.deepcopy(CONFIG); config["presentation_mode"] = mode
            self.assertEqual([], validator.validate_config(config))

    def test_broken_and_mistyped_plan_references(self):
        for change in ["current", "authorization", "task", "version", "kind"]:
            record = fixture()
            if change == "current": record["current_plan_ref"] = "plan-v999"
            if change == "authorization": record["authorizations"][0]["plan_ref"] = "plan-v999"
            if change == "task": record["task_links"][0]["plan_ref"] = "requirements"
            if change == "version": record["source_refs"][0]["version"] = "plan-v002"
            if change == "kind": record["current_plan_ref"] = "requirements"
            with self.subTest(change=change):
                self.assertTrue(validator.validate_record(record))

    def test_granted_requires_approval_reference_but_does_not_authenticate_it(self):
        record = fixture(); record["authorizations"][0]["status"] = "granted"
        self.assertTrue(any("evidence_ref" in e for e in validator.validate_record(record)))
        record = fixture(); claim_grant(record)
        # Deliberately forged source passes STRUCTURE. A host must establish original human evidence.
        self.assertEqual([], validator.validate_record(record))
        record["authorizations"][0]["evidence_ref"] = "requirements"
        self.assertTrue(validator.validate_record(record))

    def test_plan_change_requires_explicit_carry_forward_for_unchanged_grant(self):
        record = fixture(); claim_grant(record)
        record["source_refs"].append({"id": "plan-v002", "kind": "plan", "locator": "example-only:plan-v002", "version": "plan-v002"})
        record["current_plan_ref"] = "plan-v002"
        self.assertTrue(any("carry" in error for error in validator.validate_record(record)))
        record["authorizations"][0]["carry_forward_plan_refs"] = ["plan-v002"]
        self.assertEqual([], validator.validate_record(record))
        # Materiality and applicability are deliberately not inferred from this field.
        record["authorizations"][0]["carry_forward_plan_refs"] = ["plan-v999"]
        self.assertTrue(validator.validate_record(record))

    def test_duplicate_identifiers_and_wrong_initiative(self):
        for collection in ["source_refs", "authorizations", "task_links", "open_items"]:
            record = fixture(); record[collection].append(copy.deepcopy(record[collection][0]))
            with self.subTest(collection=collection):
                self.assertTrue(any("duplicate" in e for e in validator.validate_record(record)))
        record = fixture(); record["authorizations"][0]["initiative_id"] = "different"
        self.assertTrue(validator.validate_record(record))

    def test_actions_scope_and_status_change_constraints(self):
        for field, value in [("actions", []), ("actions", ["implement", "implement"]), ("actions", ["anything"]), ("status", "revoked")]:
            record = fixture(); record["authorizations"][0][field] = value
            with self.subTest(field=field, value=value):
                self.assertTrue(validator.validate_record(record))
        record = fixture(); record["authorizations"][0]["scope"]["boundaries"] = []
        self.assertTrue(validator.validate_record(record))
        record = fixture(); record["source_refs"].append({"id": "revocation", "kind": "decision", "locator": "example-only:revocation"})
        record["authorizations"][0].update(status="revoked", status_change_ref="revocation")
        self.assertEqual([], validator.validate_record(record))

    def test_closure_requires_no_explicit_unresolved_required_items(self):
        for state in ["ready_for_closure", "closed"]:
            record = fixture(); record["work_state"] = state
            self.assertTrue(any("unresolved" in e for e in validator.validate_record(record)))
            record["open_items"][0]["status"] = "resolved"
            self.assertEqual([], validator.validate_record(record))

    def test_blocked_records_retain_reason_and_previous_state(self):
        record = fixture(); record.update(work_state="blocked", blocked_from="planned", record_revision=2)
        self.assertEqual([], validator.validate_record(record, BASE))
        wrong = copy.deepcopy(record); wrong["blocked_from"] = "executing"
        self.assertTrue(validator.validate_record(wrong, BASE))
        wrong = copy.deepcopy(record); wrong["open_items"] = []
        self.assertTrue(validator.validate_record(wrong))
        resumed = fixture(); resumed["record_revision"] = 3
        self.assertEqual([], validator.validate_record(resumed, record))
        resumed["work_state"] = "reviewing"
        self.assertTrue(validator.validate_record(resumed, record))

    def test_transitions_revision_conflict_and_reopening(self):
        record = fixture(); record.update(work_state="executing", record_revision=2)
        self.assertEqual([], validator.validate_record(record, BASE))
        record["work_state"] = "closed"; record["open_items"] = []
        self.assertTrue(any("unsupported transition" in e for e in validator.validate_record(record, BASE)))
        record = fixture(); record["work_state"] = "executing"
        self.assertTrue(any("revision" in e for e in validator.validate_record(record, BASE)))
        terminal = fixture(); terminal.update(work_state="closed", open_items=[])
        reopened = copy.deepcopy(terminal); reopened.update(work_state="planned", record_revision=2)
        self.assertTrue(validator.validate_record(reopened, terminal))
        reopened["source_refs"].append({"id": "reopen", "kind": "decision", "locator": "example-only:human-reopening"})
        reopened["reopening_ref"] = "reopen"
        self.assertEqual([], validator.validate_record(reopened, terminal))

    def test_explicit_invalid_previous_record_cannot_be_ignored(self):
        record = fixture(); record["record_revision"] = 2
        self.assertTrue(any("previous" in error for error in validator.validate_record(record, None)))

    def test_interaction_lifecycle_is_independent_of_work_progress(self):
        record = fixture(); record.update(record_revision=2, interaction_state="suspended")
        self.assertEqual([], validator.validate_record(record, BASE))
        record["interaction_state"] = "inactive"
        self.assertTrue(any("lifecycle" in error for error in validator.validate_record(record, BASE)))
        record["interaction_state"] = "terminated"
        self.assertEqual([], validator.validate_record(record, BASE))
        self.assertEqual("planned", record["work_state"])

    def test_null_plan_only_in_early_draft_or_cancelled(self):
        record = fixture(); record.update(current_plan_ref=None, authorizations=[], task_links=[])
        self.assertTrue(validator.validate_record(record))
        record["work_state"] = "draft"
        self.assertEqual([], validator.validate_record(record))

    def test_drafts_cannot_claim_external_creation(self):
        record = fixture(); record["task_links"][0]["issue_id"] = "EXAMPLE-7"
        self.assertTrue(validator.validate_record(record))
        record["task_links"][0].update(status="created", url="https://example.invalid/issues/7")
        self.assertEqual([], validator.validate_record(record))
        record["task_links"][0]["url"] = "file:///untrusted"
        self.assertTrue(validator.validate_record(record))

    def test_operation_references_and_observation_metadata(self):
        record = fixture()
        observation = {"id": "result-1", "action": "example check", "target": "fixture", "environment": "disposable",
                       "plan_ref": "plan-v001", "change_revision": "snapshot-example", "outcome": "passed",
                       "observed_at": "2026-10-24T00:00:00Z", "artifact": "example-only:output", "limitations": ["fictional observation"]}
        record["evidence_refs"] = [observation]
        record["operation_attempts"] = [{"attempt_id": "attempt-1", "action": "create_issues", "task_ref": "example-export-01",
                                          "target": "fixture", "plan_ref": "plan-v001", "status": "succeeded", "result_ref": "result-1"}]
        self.assertEqual([], validator.validate_record(record))
        for field, value in [("result_ref", "missing"), ("task_ref", "missing"), ("result_ref", None)]:
            broken = copy.deepcopy(record); broken["operation_attempts"][0][field] = value
            with self.subTest(field=field): self.assertTrue(validator.validate_record(broken))
        for timestamp in ["2026-10-24", "2026-10-24T00:00:00", "yesterday"]:
            broken = copy.deepcopy(record); broken["evidence_refs"][0]["observed_at"] = timestamp
            self.assertTrue(validator.validate_record(broken))
        broken = copy.deepcopy(record); broken["evidence_refs"][0]["plan_ref"] = None
        self.assertTrue(any("different or unspecified plan" in error for error in validator.validate_record(broken)))
        record["evidence_refs"][0]["id"] = "requirements"
        self.assertTrue(validator.validate_record(record))

    def test_cli_readonly_errors_and_success_limitations(self):
        script = ROOT / "scripts/validate_records.py"
        with tempfile.TemporaryDirectory(prefix="governance-test-") as directory:
            path = Path(directory) / "record.json"
            valid_bytes = json.dumps(BASE).encode("utf-8")
            path.write_bytes(valid_bytes)
            def run(*args):
                return subprocess.run([sys.executable, "-B", str(script), *map(str, args)], capture_output=True, text=True, encoding="utf-8")
            result = run("--record", path)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertIn("not independently verified", result.stdout)
            self.assertEqual(valid_bytes, path.read_bytes())
            self.assertEqual(["record.json"], sorted(p.name for p in Path(directory).iterdir()))
            for data in ['{', '{"schema_version":"1.1","schema_version":"1.1"}', '{"value":NaN}']:
                path.write_text(data, encoding="utf-8")
                self.assertEqual(2, run("--record", path).returncode)
            path.write_text('{}', encoding="utf-8")
            self.assertEqual(1, run("--record", path).returncode)
            prior = Path(directory) / "previous.json"; prior.write_text('null', encoding="utf-8")
            path.write_bytes(valid_bytes)
            self.assertEqual(1, run("--record", path, "--previous", prior).returncode)
            self.assertEqual(2, run("--record", Path(directory) / "missing.json").returncode)
            self.assertEqual(2, run("--previous", path).returncode)
            self.assertEqual(2, run().returncode)


if __name__ == "__main__":
    unittest.main()
