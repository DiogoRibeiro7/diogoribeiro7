"""Validate data/portfolio.json against its local JSON Schema contract.

The profile repository deliberately avoids a runtime dependency on jsonschema.
This module implements only the Draft 2020-12 keywords used by
data/portfolio.schema.json and adds portfolio-specific uniqueness checks.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "data" / "portfolio.json"
SCHEMA_PATH = ROOT / "data" / "portfolio.schema.json"


class SchemaValidationError(ValueError):
    """Raised when the portfolio manifest violates its schema contract."""


def _resolve_ref(root_schema: dict[str, Any], ref: str) -> dict[str, Any]:
    """Resolve a local JSON Pointer reference."""
    prefix = "#/"
    if not ref.startswith(prefix):
        raise SchemaValidationError(f"Only local schema references are supported: {ref}")

    value: Any = root_schema
    for raw_part in ref[len(prefix) :].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if not isinstance(value, dict) or part not in value:
            raise SchemaValidationError(f"Unresolvable schema reference: {ref}")
        value = value[part]

    if not isinstance(value, dict):
        raise SchemaValidationError(f"Schema reference does not resolve to an object: {ref}")
    return value


def _matches_type(value: Any, expected: str) -> bool:
    """Return whether a Python value matches one JSON Schema primitive type."""
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    raise SchemaValidationError(f"Unsupported schema type: {expected}")


def validate_node(
    value: Any,
    schema: dict[str, Any],
    root_schema: dict[str, Any],
    path: str = "$",
) -> list[str]:
    """Validate one value against the schema subset used by this repository."""
    errors: list[str] = []

    if "$ref" in schema:
        target = _resolve_ref(root_schema, str(schema["$ref"]))
        return validate_node(value, target, root_schema, path)

    expected_type = schema.get("type")
    if expected_type is not None:
        if not isinstance(expected_type, str):
            return [f"{path}: schema type must be a string"]
        if not _matches_type(value, expected_type):
            return [f"{path}: expected {expected_type}, got {type(value).__name__}"]

    enum = schema.get("enum")
    if isinstance(enum, list) and value not in enum:
        errors.append(f"{path}: value {value!r} is not in the allowed enum")

    if isinstance(value, str):
        min_length = schema.get("minLength")
        if isinstance(min_length, int) and len(value) < min_length:
            errors.append(f"{path}: string is shorter than {min_length}")
        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.fullmatch(pattern, value) is None:
            errors.append(f"{path}: value {value!r} does not match {pattern!r}")

    if isinstance(value, list):
        min_items = schema.get("minItems")
        max_items = schema.get("maxItems")
        if isinstance(min_items, int) and len(value) < min_items:
            errors.append(f"{path}: expected at least {min_items} items")
        if isinstance(max_items, int) and len(value) > max_items:
            errors.append(f"{path}: expected at most {max_items} items")

        prefix_items = schema.get("prefixItems")
        if isinstance(prefix_items, list):
            for index, item_schema in enumerate(prefix_items):
                if index >= len(value):
                    break
                if not isinstance(item_schema, dict):
                    errors.append(f"{path}: invalid prefixItems schema at {index}")
                    continue
                errors.extend(
                    validate_node(value[index], item_schema, root_schema, f"{path}[{index}]")
                )

        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                # In Draft 2020-12, prefixItems validates leading tuple positions.
                # Avoid validating them twice when a tuple schema is used.
                if isinstance(prefix_items, list) and index < len(prefix_items):
                    continue
                errors.extend(
                    validate_node(item, item_schema, root_schema, f"{path}[{index}]")
                )

    if isinstance(value, dict):
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        additional = schema.get("additionalProperties", True)

        if isinstance(required, list):
            for key in required:
                if key not in value:
                    errors.append(f"{path}: missing required property {key!r}")

        if isinstance(properties, dict):
            for key, child in value.items():
                child_schema = properties.get(key)
                if child_schema is None:
                    if additional is False:
                        errors.append(f"{path}: unexpected property {key!r}")
                    continue
                if not isinstance(child_schema, dict):
                    errors.append(f"{path}.{key}: invalid child schema")
                    continue
                errors.extend(
                    validate_node(child, child_schema, root_schema, f"{path}.{key}")
                )

    return errors


def validate_uniqueness(manifest: dict[str, Any]) -> list[str]:
    """Validate cross-record uniqueness not expressible cleanly in JSON Schema."""
    errors: list[str] = []

    projects = manifest.get("projects", [])
    if isinstance(projects, list):
        repos = [item.get("repo") for item in projects if isinstance(item, dict)]
        if len(repos) != len(set(repos)):
            errors.append("$.projects: repository names must be unique")

        pypi = [
            item.get("pypi")
            for item in projects
            if isinstance(item, dict) and item.get("pypi")
        ]
        if len(pypi) != len(set(pypi)):
            errors.append("$.projects: PyPI package names must be unique")

    outputs = manifest.get("outputs", [])
    if isinstance(outputs, list):
        keys = [
            (item.get("repo"), item.get("path"), item.get("title"))
            for item in outputs
            if isinstance(item, dict)
        ]
        if len(keys) != len(set(keys)):
            errors.append("$.outputs: (repo, path, title) records must be unique")

    cases = manifest.get("case_studies", [])
    if isinstance(cases, list):
        titles = [item.get("title") for item in cases if isinstance(item, dict)]
        if len(titles) != len(set(titles)):
            errors.append("$.case_studies: titles must be unique")

    return errors


def main() -> int:
    """Validate the canonical portfolio manifest and print actionable errors."""
    schema: object = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    manifest: object = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    if not isinstance(schema, dict):
        raise TypeError("Portfolio schema must be a JSON object.")
    if not isinstance(manifest, dict):
        raise TypeError("Portfolio manifest must be a JSON object.")

    errors = validate_node(manifest, schema, schema)
    errors.extend(validate_uniqueness(manifest))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Portfolio manifest satisfies data/portfolio.schema.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
