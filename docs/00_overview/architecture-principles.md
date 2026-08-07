# Architekturprinzipien

1. **Kontrolliertes Zoomen:** L0/L1 sind die Basis, L2 ist strukturiert, L3 wird am Vertical Slice erprobt, L4 folgt später.
2. **Domänenspezifische Qualität:** Prüfungen sind dezentral und datentypspezifisch; Qualitätsmanagement, Status, Lineage und Reporting sind übergreifend standardisiert.
3. **Data Products:** Verantwortete, versionierte Produkte ersetzen lose Projektdateien.
4. **Immutable Raw Data:** Originale bleiben unverändert; Transformationen erzeugen neue Repräsentationen.
5. **Provenance:** Quellen, Runs, Code, Datasets, Modelle, Pre-/Postprocessing und Zeiten bleiben rückverfolgbar.
6. **Modulare AI Platform:** Fähigkeiten sind kombinierbar und austauschbar.
7. **Batch First:** reproduzierbare Batch-Verarbeitung hat Vorrang; Online Inference bleibt optional.
8. **Technologieoffenheit:** Produkte werden erst durch nachvollziehbare Entscheidungen verbindlich.
