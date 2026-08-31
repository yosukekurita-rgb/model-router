#!/usr/bin/env python3
"""Static package, link, YAML, route-contract, and guard validation."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Install requirements-dev.txt and retry.")


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
REQUIRED_GUARDS = {
    "model-after-capabilities",
    "deterministic-core",
    "available-tests",
    "coupled-bottleneck",
    "independent-breadth",
    "fixed-quality-target",
    "approval-boundary",
    "availability-not-permission",
}


def error(message: str) -> None:
    ERRORS.append(message)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        error(f"{path.relative_to(ROOT)}: cannot read: {exc}")
        return ""


def load_yaml_text(text: str, label: str) -> Any:
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as exc:
        error(f"{label}: invalid YAML: {exc}")
        return None


def validate_required_files() -> None:
    required = [
        "SKILL.md",
        "README.md",
        "LICENSE",
        "agents/openai.yaml",
        "evals/routing-cases.yaml",
        "evals/trigger-cases.md",
        "scripts/validate_repository.py",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            error(f"{relative}: required file is missing")


def validate_skill_frontmatter() -> dict[str, Any]:
    text = read(ROOT / "SKILL.md")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        error("SKILL.md: missing YAML frontmatter")
        return {}
    data = load_yaml_text(match.group(1), "SKILL.md frontmatter")
    if not isinstance(data, dict):
        error("SKILL.md: frontmatter must be a mapping")
        return {}
    if data.get("name") != "model-router":
        error("SKILL.md: name must be model-router")
    if not isinstance(data.get("description"), str) or not data["description"].strip():
        error("SKILL.md: description must be a non-empty string")
    if data.get("license") != "MIT":
        error("SKILL.md: license must be MIT for this package")
    metadata = data.get("metadata")
    if not isinstance(metadata, dict) or metadata.get("version") != "0.1.0":
        error('SKILL.md: metadata.version must be "0.1.0"')
    return data


def validate_all_yaml() -> dict[Path, Any]:
    documents: dict[Path, Any] = {}
    for path in sorted(ROOT.rglob("*.yaml")) + sorted(ROOT.rglob("*.yml")):
        if ".git" in path.parts or ".codex" in path.parts:
            continue
        documents[path] = load_yaml_text(read(path), str(path.relative_to(ROOT)))
    return documents


def validate_markdown_links() -> None:
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts or ".codex" in path.parts:
            continue
        for raw_target in pattern.findall(read(path)):
            parts = raw_target.strip().strip("<>").split()
            if not parts:
                error(f"{path.relative_to(ROOT)}: empty Markdown link target")
                continue
            target = parts[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if local_part and not (path.parent / local_part).exists():
                error(f"{path.relative_to(ROOT)}: broken relative link: {raw_target}")


def validate_yaml_references(documents: dict[Path, Any]) -> None:
    def walk(value: Any, source: Path) -> None:
        if isinstance(value, dict):
            for child in value.values():
                walk(child, source)
        elif isinstance(value, list):
            for child in value:
                walk(child, source)
        elif isinstance(value, str) and value.startswith(("./", "../")):
            if not (source.parent / value).resolve().exists():
                error(f"{source.relative_to(ROOT)}: missing referenced file: {value}")

    for path, document in documents.items():
        walk(document, path)


def canonical_route_spec() -> dict[str, Any]:
    text = read(ROOT / "SKILL.md")
    match = re.search(r"## Route outcome.*?```yaml\s*\n(.*?)```", text, re.DOTALL)
    if not match:
        error("SKILL.md: canonical route-outcome YAML block is missing")
        return {}
    spec = load_yaml_text(match.group(1), "SKILL.md route outcome")
    if not isinstance(spec, dict):
        error("SKILL.md: canonical route outcome must be a mapping")
        return {}
    return spec


def validate_against_spec(value: Any, spec: Any, label: str) -> None:
    if isinstance(spec, dict):
        if not isinstance(value, dict):
            error(f"{label}: expected mapping")
            return
        expected_keys = set(spec)
        actual_keys = set(value)
        if actual_keys != expected_keys:
            missing = sorted(expected_keys - actual_keys)
            extra = sorted(actual_keys - expected_keys)
            error(f"{label}: schema keys differ; missing={missing}, extra={extra}")
        for key in expected_keys & actual_keys:
            validate_against_spec(value[key], spec[key], f"{label}.{key}")
        return
    if isinstance(spec, list):
        if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
            error(f"{label}: expected a list of strings")
        return
    if not isinstance(spec, str):
        error(f"{label}: unsupported canonical schema token {spec!r}")
        return
    if spec == "string":
        if not isinstance(value, str) or not value.strip():
            error(f"{label}: expected a non-empty string")
        return
    tokens = spec.split("|")

    def matches(token: str) -> bool:
        if token == "true":
            return value is True
        if token == "false":
            return value is False
        if token == "null":
            return value is None
        if token == "string":
            return isinstance(value, str) and bool(value.strip())
        return isinstance(value, str) and value == token

    if not any(matches(token) for token in tokens):
        error(f"{label}: expected {spec}, got {value!r}")


def route_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(route_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(route_keys(child))
    return keys


def validate_guard(guard: str, route: dict[str, Any], label: str) -> None:
    if guard == "model-after-capabilities":
        forbidden = {"model", "provider", "model_id", "provider_id", "approval_granted"}
        found = sorted(forbidden & route_keys(route))
        if found:
            error(f"{label}: concrete resolution or granted-approval keys are forbidden: {found}")
    elif guard == "deterministic-core":
        if route.get("deterministic_first") is not True:
            error(f"{label}: deterministic core must set deterministic_first: true")
    elif guard == "available-tests":
        if route.get("verification") != "deterministic" or route.get("independent_review") is not False:
            error(f"{label}: available tests must remain the deterministic verifier")
    elif guard == "coupled-bottleneck":
        if route.get("topology") == "bounded-parallel":
            error(f"{label}: a coupled bottleneck cannot use bounded-parallel topology")
    elif guard == "independent-breadth":
        if route.get("limiting_shape") != "breadth" or route.get("topology") != "bounded-parallel":
            error(f"{label}: independent breadth must be explicit before bounded parallelism")
    elif guard == "fixed-quality-target":
        if route.get("runtime_resolution", {}).get("status") not in {"degraded", "blocked"}:
            error(f"{label}: failed resolution must be degraded or blocked without lowering quality")
        if not isinstance(route.get("human_decision_required"), str):
            error(f"{label}: a failed route with fixed quality must expose the decision")
    elif guard == "approval-boundary":
        if route.get("human_escalation") != "required":
            error(f"{label}: approval boundary must require human escalation")
        if route.get("runtime_resolution", {}).get("status") == "resolved":
            error(f"{label}: requested approval cannot be encoded as resolved execution")
    elif guard == "availability-not-permission":
        constraints = " ".join(route.get("eligibility_constraints", [])).lower()
        if not any(term in constraints for term in ("permission", "policy", "eligible", "authorized")):
            error(f"{label}: availability must be separated from permission or eligibility")
    else:
        error(f"{label}: unknown guard {guard!r}")


def validate_evals(spec: dict[str, Any], document: Any) -> None:
    if not isinstance(document, dict):
        error("evals/routing-cases.yaml: expected mapping")
        return
    cases = document.get("cases")
    if document.get("version") != 2 or not isinstance(cases, list):
        error("evals/routing-cases.yaml: expected version 2 and a cases list")
        return
    if len(cases) != 20:
        error(f"evals/routing-cases.yaml: expected 20 cases, found {len(cases)}")
    ids: list[str] = []
    observed_guards = {"model-after-capabilities"}
    for index, case in enumerate(cases):
        label = f"evals/routing-cases.yaml case {index + 1}"
        if not isinstance(case, dict):
            error(f"{label}: expected mapping")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            error(f"{label}: id must be a non-empty string")
            case_id = str(index + 1)
        ids.append(case_id)
        route = case.get("expected")
        validate_against_spec(route, spec, f"{label} ({case_id}).expected")
        if not isinstance(route, dict):
            continue
        validate_guard("model-after-capabilities", route, label)
        guards = case.get("guards", [])
        if not isinstance(guards, list) or any(not isinstance(item, str) for item in guards):
            error(f"{label}: guards must be a list of strings")
            continue
        for guard in guards:
            observed_guards.add(guard)
            validate_guard(guard, route, label)
        if route.get("topology") == "bounded-parallel" and route.get("limiting_shape") != "breadth":
            error(f"{label}: bounded-parallel requires limiting_shape: breadth")
    if len(ids) != len(set(ids)):
        error("evals/routing-cases.yaml: case ids must be unique")
    missing_guards = sorted(REQUIRED_GUARDS - observed_guards)
    if missing_guards:
        error(f"evals/routing-cases.yaml: prohibited-behavior coverage missing {missing_guards}")


def validate_examples(spec: dict[str, Any]) -> None:
    examples = sorted((ROOT / "examples").glob("*.md"))
    if not examples:
        error("examples: no Markdown examples found")
    for path in examples:
        match = re.search(r"## Route\s*\n\s*```yaml\s*\n(.*?)```", read(path), re.DOTALL)
        if not match:
            error(f"{path.relative_to(ROOT)}: missing ## Route YAML block")
            continue
        route = load_yaml_text(match.group(1), f"{path.relative_to(ROOT)} route")
        validate_against_spec(route, spec, f"{path.relative_to(ROOT)} route")
        if isinstance(route, dict):
            validate_guard("model-after-capabilities", route, str(path.relative_to(ROOT)))
            if route.get("topology") == "bounded-parallel" and route.get("limiting_shape") != "breadth":
                error(f"{path.relative_to(ROOT)}: bounded-parallel requires limiting_shape: breadth")


def main() -> int:
    validate_required_files()
    validate_skill_frontmatter()
    documents = validate_all_yaml()
    validate_markdown_links()
    validate_yaml_references(documents)
    spec = canonical_route_spec()
    validate_evals(spec, documents.get(ROOT / "evals/routing-cases.yaml"))
    validate_examples(spec)
    if ERRORS:
        for message in ERRORS:
            print(f"ERROR: {message}", file=sys.stderr)
        print(f"Validation failed with {len(ERRORS)} error(s).", file=sys.stderr)
        return 1
    print("Validation OK: package, YAML, links, references, 20 eval routes, examples, and guards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
