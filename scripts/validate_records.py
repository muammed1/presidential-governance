#!/usr/bin/env python3
"""Read-only structure/internal-consistency validation; never authenticates approval."""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from uuid import UUID

VERSION = "1.1"
NO_PREVIOUS = object()
LIMITATION = (
    "Authorization evidence, plan contents, external facts and actual operations "
    "were not independently verified."
)
ACTIONS = {
    "confirm_requirements", "approve_plan", "write_records", "modify_docs",
    "select_branch", "create_branch", "create_issues", "update_issues", "run_tests",
    "implement", "delegate", "commit", "push", "create_pr", "merge", "migrate",
    "change_environment", "deploy", "close_issue",
}
UNFINISHED = {"draft", "planned", "executing", "reviewing", "ready_for_closure"}
WORK_STATES = UNFINISHED | {"blocked", "closed", "cancelled"}
STATUSES = {"pending", "granted", "denied", "revoked", "superseded", "expired", "needs_reconfirmation"}


def enum(*values):
    return ("enum", set(values))


def nullable(spec):
    return ("nullable", spec)


CONFIG = {
    "schema_version": enum(VERSION),
    "presentation_mode": enum("Professional", "Presidential"),
    "roles": {"user": "str", "advisor": "str"},
    "language": "str", "formality": "str",
    "planning_depth": enum("proportional"),
    "documentation_layout": enum("discover"),
    "issue_tracker": enum("detect", "none", "Linear"),
    "execution": enum("primary"), "delegation": enum("explicit_authorization"),
    "storage": enum("approved_existing_or_conversation"),
    "shared_record_editing": enum("single_writer"),
}
SOURCE = {"id": "str", "kind": enum("plan", "requirement", "decision", "approval", "artifact"),
          "locator": "str", "version?": "str"}
AUTH = {
    "authorization_id": "str", "initiative_id": "str", "actions": [("enum", ACTIONS)],
    "plan_ref": "str", "scope": {"target": "str", "environment": "str", "boundaries": ["str"], "executor?": "str"},
    "preconditions": ["str"], "exclusions": ["str"], "duration": "str",
    "evidence_ref": nullable("str"), "status": ("enum", STATUSES),
    "status_change_ref": nullable("str"), "carry_forward_plan_refs": ["str"],
}
EVIDENCE = {
    "id": "str", "action": "str", "target": "str", "environment": "str",
    "plan_ref": nullable("str"), "change_revision": "str",
    "outcome": enum("passed", "failed", "partial", "unknown"),
    "observed_at": "str", "artifact": "str", "limitations": ["str"],
}
TASK = {"task_ref": "str", "plan_ref": "str", "status": enum("draft", "created", "unknown"),
        "issue_id": nullable("str"), "url": nullable("str")}
ATTEMPT = {
    "attempt_id": "str", "action": ("enum", ACTIONS), "task_ref": nullable("str"),
    "target": "str", "plan_ref": "str", "status": enum("intended", "succeeded", "failed", "unknown"),
    "result_ref": nullable("str"),
}
OPEN = {"id": "str", "kind": enum("question", "gate", "risk"), "required": "bool",
        "status": enum("open", "resolved"), "reference": "str"}
RECORD = {
    "schema_version": enum(VERSION), "initiative_id": "str", "title": "str",
    "record_revision": "positive_int", "interaction_state": enum("inactive", "active", "suspended", "terminated"),
    "work_state": ("enum", WORK_STATES), "blocked_from?": ("enum", UNFINISHED),
    "current_plan_ref": nullable("str"), "source_refs": [SOURCE], "authorizations": [AUTH],
    "task_links": [TASK], "operation_attempts": [ATTEMPT], "evidence_refs": [EVIDENCE],
    "open_items": [OPEN], "next_action": "str", "reopening_ref?": "str",
}


def check_shape(value, spec, path, errors):
    """Validate a deliberately small, dependency-free schema vocabulary."""
    if isinstance(spec, tuple):
        kind, argument = spec
        if kind == "nullable":
            if value is not None:
                check_shape(value, argument, path, errors)
        elif not isinstance(value, str) or value not in argument:
            errors.append(f"{path}: expected one of {', '.join(sorted(argument))}")
    elif isinstance(spec, dict):
        if not isinstance(value, dict):
            errors.append(f"{path}: expected object")
            return
        allowed = {key.rstrip("?") for key in spec}
        for key in value.keys() - allowed:
            errors.append(f"{path}.{key}: unknown field")
        for field, child in spec.items():
            key = field.rstrip("?")
            if key not in value:
                if not field.endswith("?"):
                    errors.append(f"{path}.{key}: required field missing")
            else:
                check_shape(value[key], child, f"{path}.{key}", errors)
    elif isinstance(spec, list):
        if not isinstance(value, list):
            errors.append(f"{path}: expected array")
        else:
            for index, child in enumerate(value):
                check_shape(child, spec[0], f"{path}[{index}]", errors)
    elif spec == "str":
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path}: expected non-empty string")
    elif spec == "bool":
        if type(value) is not bool:
            errors.append(f"{path}: expected boolean")
    elif spec == "positive_int":
        if type(value) is not int or value < 1:
            errors.append(f"{path}: expected integer >= 1")


def validate_config(config):
    errors = []
    check_shape(config, CONFIG, "config", errors)
    return errors


def index_entries(entries, key, path, errors):
    result = {}
    for index, entry in enumerate(entries):
        value = entry[key]
        if value in result:
            errors.append(f"{path}[{index}].{key}: duplicate identifier")
        result[value] = entry
    return result


def validate_record(record, previous=NO_PREVIOUS):
    errors = []
    check_shape(record, RECORD, "record", errors)
    if errors:
        return errors
    try:
        UUID(record["initiative_id"])
    except ValueError:
        errors.append("record.initiative_id: expected UUID")
    sources = index_entries(record["source_refs"], "id", "record.source_refs", errors)
    observations = index_entries(record["evidence_refs"], "id", "record.evidence_refs", errors)
    index_entries(record["authorizations"], "authorization_id", "record.authorizations", errors)
    tasks = index_entries(record["task_links"], "task_ref", "record.task_links", errors)
    index_entries(record["operation_attempts"], "attempt_id", "record.operation_attempts", errors)
    index_entries(record["open_items"], "id", "record.open_items", errors)
    if sources.keys() & observations.keys():
        errors.append("record: source_refs and evidence_refs must have disjoint identifiers")
    plans = {key: ref for key, ref in sources.items() if ref["kind"] == "plan"}
    for index, ref in enumerate(record["source_refs"]):
        if ref["kind"] == "plan":
            if not re.fullmatch(r"plan-v[0-9]{3,}", ref["id"]) or ref.get("version") != ref["id"]:
                errors.append(f"record.source_refs[{index}]: plan requires matching plan-vNNN id and version")
        elif "version" in ref:
            errors.append(f"record.source_refs[{index}].version: only plan sources have a version")

    def plan_ref(value, path, allow_null=False):
        if value is None and allow_null:
            return
        if value not in plans:
            errors.append(f"{path}: missing plan source reference")

    def source_ref(value, path, kind=None, required=False):
        if value is None:
            if required:
                errors.append(f"{path}: source reference required")
            return
        if value not in sources or (kind is not None and sources[value]["kind"] != kind):
            errors.append(f"{path}: missing or incompatible source reference")

    current = record["current_plan_ref"]
    state = record["work_state"]
    effective_state = record.get("blocked_from") if state == "blocked" else state
    plan_ref(current, "record.current_plan_ref", allow_null=effective_state in {"draft", "cancelled"})
    if state == "blocked":
        if "blocked_from" not in record:
            errors.append("record.blocked_from: required while blocked")
        if not any(item["required"] and item["status"] == "open" for item in record["open_items"]):
            errors.append("record.open_items: blocked requires an open required reason")
    elif "blocked_from" in record:
        errors.append("record.blocked_from: only permitted while blocked")
    if state in {"ready_for_closure", "closed"}:
        if any(item["required"] and item["status"] == "open" for item in record["open_items"]):
            errors.append("record.open_items: closure has unresolved required items")
    if "reopening_ref" in record:
        source_ref(record["reopening_ref"], "record.reopening_ref", "decision")

    for index, auth in enumerate(record["authorizations"]):
        path = f"record.authorizations[{index}]"
        if auth["initiative_id"] != record["initiative_id"]:
            errors.append(f"{path}.initiative_id: initiative mismatch")
        if not auth["actions"] or len(set(auth["actions"])) != len(auth["actions"]):
            errors.append(f"{path}.actions: expected non-empty unique actions")
        if not auth["scope"]["boundaries"]:
            errors.append(f"{path}.scope.boundaries: at least one boundary required")
        plan_ref(auth["plan_ref"], f"{path}.plan_ref")
        carries = auth["carry_forward_plan_refs"]
        if len(set(carries)) != len(carries):
            errors.append(f"{path}.carry_forward_plan_refs: duplicate plan reference")
        for carry in carries:
            plan_ref(carry, f"{path}.carry_forward_plan_refs")
        source_ref(auth["evidence_ref"], f"{path}.evidence_ref", "approval", auth["status"] == "granted")
        changed = auth["status"] in {"revoked", "superseded", "expired", "denied", "needs_reconfirmation"}
        source_ref(auth["status_change_ref"], f"{path}.status_change_ref", required=changed)
        if auth["status"] == "granted" and (current is None or (auth["plan_ref"] != current and current not in carries)):
            errors.append(f"{path}: granted scope does not reference or explicitly carry to the current plan")

    for index, task in enumerate(record["task_links"]):
        path = f"record.task_links[{index}]"
        plan_ref(task["plan_ref"], f"{path}.plan_ref")
        if task["status"] == "created":
            if task["issue_id"] is None or task["url"] is None or not re.fullmatch(r"https://[^/\s]+(?:/[^\s]*)?", task["url"]):
                errors.append(f"{path}: created requires actual ID and HTTPS URL (authenticity unverified)")
        elif task["issue_id"] is not None or task["url"] is not None:
            errors.append(f"{path}: draft/unknown must not claim external ID or URL")

    known_results = sources.keys() | observations.keys()
    for index, attempt in enumerate(record["operation_attempts"]):
        path = f"record.operation_attempts[{index}]"
        plan_ref(attempt["plan_ref"], f"{path}.plan_ref")
        task_id = attempt["task_ref"]
        if task_id is not None and task_id not in tasks:
            errors.append(f"{path}.task_ref: unknown task")
        elif task_id is not None and tasks[task_id]["plan_ref"] != attempt["plan_ref"]:
            errors.append(f"{path}.plan_ref: differs from referenced task plan")
        result = attempt["result_ref"]
        if result is not None and result not in known_results:
            errors.append(f"{path}.result_ref: unknown result reference")
        if result in observations and observations[result]["plan_ref"] != attempt["plan_ref"]:
            errors.append(f"{path}.result_ref: observation belongs to a different or unspecified plan")
        if attempt["status"] == "succeeded" and result is None:
            errors.append(f"{path}.result_ref: succeeded requires result reference")

    for index, observation in enumerate(record["evidence_refs"]):
        path = f"record.evidence_refs[{index}]"
        plan_ref(observation["plan_ref"], f"{path}.plan_ref", allow_null=True)
        try:
            when = datetime.fromisoformat(observation["observed_at"].replace("Z", "+00:00"))
            if when.utcoffset() is None:
                raise ValueError
        except ValueError:
            errors.append(f"{path}.observed_at: expected ISO 8601 datetime with timezone")

    if previous is not NO_PREVIOUS:
        prior_errors = validate_record(previous)
        if prior_errors:
            errors.extend("previous: " + error for error in prior_errors)
            return errors
        if previous["initiative_id"] != record["initiative_id"]:
            errors.append("record.initiative_id: differs from previous record")
        if record["record_revision"] != previous["record_revision"] + 1:
            errors.append("record.record_revision: expected previous revision + 1; reconcile conflicts")
        interaction = {
            "inactive": {"inactive", "active"},
            "active": {"active", "suspended", "terminated"},
            "suspended": {"suspended", "active", "terminated"},
            "terminated": {"terminated", "active"},
        }
        if record["interaction_state"] not in interaction[previous["interaction_state"]]:
            errors.append("record.interaction_state: unsupported lifecycle transition")
        before = previous["work_state"]
        normal = {
            "draft": {"planned"}, "planned": {"draft", "executing"},
            "executing": {"reviewing"}, "reviewing": {"executing", "ready_for_closure"},
            "ready_for_closure": {"reviewing", "closed"},
        }
        allowed = {before} | normal.get(before, set())
        if before in UNFINISHED:
            allowed |= {"blocked", "cancelled"}
        elif before == "blocked":
            allowed |= {previous["blocked_from"], "cancelled"}
        elif state != before:
            if state not in {"draft", "planned"} or "reopening_ref" not in record:
                errors.append("record.reopening_ref: terminal reopening requires explicit decision reference and draft/planned state")
            else:
                allowed.add(state)
        if state not in allowed:
            errors.append(f"record.work_state: unsupported transition {before} -> {state}")
        if state == "blocked":
            expected = previous.get("blocked_from") if before == "blocked" else before
            if record.get("blocked_from") != expected:
                errors.append("record.blocked_from: must retain prior unfinished state")
    return errors


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON field: {key}")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError(f"non-JSON constant: {value}")


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object, parse_constant=reject_constant)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record")
    parser.add_argument("--config")
    parser.add_argument("--previous", help="prior record; requires --record")
    args = parser.parse_args(argv)
    if not (args.record or args.config) or (args.previous and not args.record):
        parser.error("supply --record and/or --config; --previous requires --record")
    try:
        errors = []
        if args.config:
            errors.extend(validate_config(read_json(args.config)))
        if args.record:
            previous = read_json(args.previous) if args.previous else NO_PREVIOUS
            errors.extend(validate_record(read_json(args.record), previous))
    except (OSError, ValueError, RecursionError) as error:
        print(f"INPUT ERROR: {error}", file=sys.stderr)
        print(LIMITATION, file=sys.stderr)
        return 2
    if errors:
        for error in sorted(errors):
            print("ERROR: " + error, file=sys.stderr)
        print(LIMITATION, file=sys.stderr)
        return 1
    print("Record structure and internal consistency passed. " + LIMITATION)
    return 0


if __name__ == "__main__":
    sys.exit(main())
