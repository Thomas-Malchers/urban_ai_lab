# Beitragen

## Workflow

1. Branch erstellen, etwa `docs/orthophoto-domain`, `architecture/ai-platform`, `adr/domain-specific-quality` oder `fix/broken-links`.
2. Inhalte, Metadaten, Links und Diagramme gemeinsam aktualisieren.
3. `python scripts/validate-yaml.py` und `make docs-build` ausführen.
4. Pull Request mit Review eröffnen.

Bei Architekturänderungen ist zu prüfen: korrekter Dokument- und Architekturstatus, klare Trennung von Current/Transitional/Target, sichtbare Annahmen, klare Ein- und Ausgänge, aktualisierte Diagramme, ADR-Bedarf und gültige Links.

## Definition of Done

Inhalt und Diagramme sind aktualisiert, Metadaten und relevante ADRs gepflegt, Links gültig, der Strict Build erfolgreich und ein Review erfolgt.
