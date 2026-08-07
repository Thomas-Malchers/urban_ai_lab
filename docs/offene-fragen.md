# Entscheidungen & offene Fragen

Diese Arbeitsliste macht bewusst sichtbar, welche Architekturfragen noch nicht entschieden sind.

## Storage und Dateiformate

- Welche Rohdaten bleiben dateibasiert?
- Welche standardisierten Formate verwenden wir?
- Welche Daten gehören in Object Storage, welche in eine räumliche Datenbank?
- Was wird materialisiert und was on demand erzeugt?

## Integration

- Was ist die stabile interne Gebäude-ID und welche weiteren Objekte benötigen stabile IDs?
- Wie bleiben Source IDs erhalten?
- Wie behandeln wir unterschiedliche Aufnahmezeitpunkte?
- Wie machen wir Cross-Source-Konflikte sichtbar?

## Versionierung und Lineage

- Welche Granularität benötigen Datenversionen?
- Wie referenzieren abgeleitete Werte ihre Quellen?
- Wie dokumentieren wir Pipeline-Versionen und Änderungen?

## Zugriff

- Wie erhalten Data Scientists Daten: SQL, Files, GeoParquet, Python API, STAC oder eine Kombination?

## Qualität

- Welche Qualitätsdimensionen sind je Datendomäne relevant?
- Welche Checks blockieren eine Veröffentlichung, welche erzeugen Warnungen?
- Welche Qualitätsinformationen müssen beim Datenzugriff sichtbar sein?

## Zukunft

- Wie dockt später die AI-/ML-Plattform an?
- Welche Datenprodukte werden zuerst benötigt?
- Welche Use Cases bestimmen die Priorität der Architekturentscheidungen?

Technische Entscheidungen werden bei Bedarf weiterhin als ADR im Repository dokumentiert.
