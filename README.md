# Urban AI Lab Architecture

Dieses Repository ist die versionierte technische Quelle der Wahrheit für die Zielarchitektur des Urban AI Lab. Es beschreibt, wie heterogene urbane Daten nachvollziehbar in qualitätsgesicherte Datenprodukte, Analysen und KI-Ergebnisse überführt werden. Der Inhalt ist ein Architekturentwurf; er implementiert keine produktive Plattform.

## Dokumentation

Die Inhalte folgen den Zoomstufen Vision (L0), Gesamtarchitektur (L1), Plattform und Domänen (L2), Vertical Slice (L3) sowie späteren Implementierungsdetails (L4). Die veröffentlichte Website liegt künftig unter `https://example.org/urban-ai-lab-architecture/`.

Confluence kann als Landingpage und für Zusammenarbeit dienen. Architektur, ADRs, Verträge und Diagrammquellen werden ausschließlich hier gepflegt.

## Lokal starten

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
make docs-serve
```

Unter Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements-docs.txt
mkdocs serve
```

Mit `make docs-build` wird die Website im Strict Mode gebaut. Änderungen erfolgen über thematische Branches und Pull Requests; Details stehen in [CONTRIBUTING.md](CONTRIBUTING.md).
