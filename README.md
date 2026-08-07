# Urban AI Lab – Data Architecture

Dieses Repository dokumentiert das Architektur-Zielbild für eine gemeinsame Datenbasis aus Orthofotos, LiDAR, CityGML und weiteren urbanen Daten.

**Current focus: L0 / L1 / selected L2 Urban Data & AI Architecture**

Die sichtbare Dokumentation beschreibt die Gesamtarchitektur, Data Platform, AI / Model Platform und ausgewählte L2-Patterns. Konkrete Implementierung, Deployment und Toolkonfiguration bleiben einer späteren L3-Ebene vorbehalten.

## Lokal verwenden

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Den produktionsnahen Build prüfen:

```bash
mkdocs build --strict
```

## Repository-Struktur

- `docs/` – sichtbare L0-/L1-/L2-Dokumentation und bestehende Detailseiten
- `decisions/` – Architecture Decision Records
- `contracts/` – vorbereitete Vertragsstrukturen
- `diagrams/` – Diagrammquellen und Exporte
- `scripts/` – Hilfs- und Prüfskripte

L3-/L4-Inhalte werden erst vertieft, wenn konkrete Pipelines oder Implementierungen bearbeitet werden. Hinweise zur Mitarbeit stehen in [CONTRIBUTING.md](CONTRIBUTING.md).
