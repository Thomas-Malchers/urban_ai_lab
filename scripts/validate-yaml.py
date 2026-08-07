#!/usr/bin/env python3
"""Validate YAML files while ignoring generated and environment directories."""

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".venv", "venv", "site", "node_modules", "__pycache__"}


def yaml_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".yaml", ".yml"}:
            if not any(part in IGNORED for part in path.relative_to(ROOT).parts):
                yield path


def main() -> int:
    errors = 0
    for path in yaml_files():
        try:
            with path.open(encoding="utf-8") as stream:
                # BaseLoader validates YAML syntax while accepting MkDocs'
                # trusted Python-name tag used by the Mermaid superfence.
                yaml.load(stream, Loader=yaml.BaseLoader)
            print(f"OK: {path.relative_to(ROOT)}")
        except (OSError, yaml.YAMLError) as exc:
            errors += 1
            print(f"ERROR: {path.relative_to(ROOT)}: {exc}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
