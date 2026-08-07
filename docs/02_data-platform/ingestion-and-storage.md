# Ingestion und Storage

```mermaid
flowchart LR
 S[Quelle] --> R[Immutable Raw Zone] --> V[Format- und Metadatenprüfung] --> N[Domänenspezifische Standardisierung] --> Q[Domänenspezifisches Quality Gate] --> P[Versioniertes Data Product]
```

Rohdaten werden nicht überschrieben. Speichertechnologien, Topologie und Orchestrator sind offene Architekturentscheidungen. Fehler erzeugen einen nachvollziehbaren Run-Status und keinen teilweise veröffentlichten Bestand.
