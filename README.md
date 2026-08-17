# Urban AI Lab – Data Architecture

This repository documents the target architecture for a shared data foundation spanning orthophotos, LiDAR, CityGML, and other urban data.

**Current focus: L0 / L1 / selected L2 Urban Data & AI Architecture**

The published documentation covers the overall architecture, Data Platform, AI / Model Platform, and selected L2 patterns. Concrete implementation, deployment, and tool configuration are deferred to a later L3 level.

## Local usage

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Run a production-like validation build with:

```bash
mkdocs build --strict
```

## Repository structure

- `docs/` – published L0/L1/L2 documentation and existing detailed pages
- `decisions/` – Architecture Decision Records
- `contracts/` – prepared contract structures
- `diagrams/` – diagram sources and exports
- `scripts/` – helper and validation scripts

L3/L4 content will be expanded when concrete pipelines or implementations are developed. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance.

17.08.2026