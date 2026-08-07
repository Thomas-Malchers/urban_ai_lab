# Urban AI Lab – Data Architecture

Dieses Repository dokumentiert das Architektur-Zielbild für eine gemeinsame Datenbasis aus Orthofotos, LiDAR, CityGML und weiteren urbanen Daten.

**Current focus: L0 / L1 Urban Data Architecture**

Die sichtbare Dokumentation beschreibt das Zielbild, den logischen Datenfluss, die drei zentralen Datendomänen und offene Architekturfragen. Detailliertere Plattform-, Pipeline- und AI-Inhalte bleiben als Wissensbestand erhalten, stehen derzeit aber nicht im Vordergrund.

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

- `docs/` – sichtbare L0-/L1-Dokumentation und bestehende Detailseiten
- `decisions/` – Architecture Decision Records
- `contracts/` – vorbereitete Vertragsstrukturen
- `diagrams/` – Diagrammquellen und Exporte
- `scripts/` – Hilfs- und Prüfskripte

L2–L4-Inhalte werden erst vertieft, wenn konkrete Domänen, Pipelines oder Implementierungen bearbeitet werden. Hinweise zur Mitarbeit stehen in [CONTRIBUTING.md](CONTRIBUTING.md).
