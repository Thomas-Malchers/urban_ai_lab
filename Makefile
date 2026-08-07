.PHONY: docs-build docs-serve validate

docs-build:
	mkdocs build --strict

docs-serve:
	mkdocs serve

validate:
	python scripts/validate-yaml.py
