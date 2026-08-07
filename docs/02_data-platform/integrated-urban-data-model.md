---
title: Integriertes urbanes Objektmodell
status: draft
architecture_state: conceptual
owner: Urban AI Lab
last_reviewed: 2026-08-06
---

# Integriertes urbanes Objektmodell

**Status: Conceptual Draft** — kein physisches Datenbankschema.

```mermaid
classDiagram
 Area "1" o-- "*" Parcel
 Parcel "1" o-- "*" Building
 Building "1" o-- "*" BuildingPart
 BuildingPart "1" o-- "*" RoofSurface
 BuildingPart "1" o-- "*" FacadeSurface
 FacadeSurface "1" o-- "*" Opening
 RoofSurface "1" o-- "*" RoofObject
 Area "1" o-- "*" Road
 Area "1" o-- "*" VegetationObject
 Building "1" o-- "*" Observation
 Building "1" o-- "*" DerivedFeature
 Building "1" o-- "*" Prediction
 Prediction "1" o-- "*" Annotation
 Prediction "1" o-- "*" ReviewDecision
 SourceDataset "1" o-- "*" SourceAsset
 SourceAsset "*" --> "*" Observation
 PipelineRun "1" --> "*" DerivedFeature
 PipelineRun "1" --> "*" Prediction
 ModelVersion "1" --> "*" Prediction
 QualityResult "*" --> "1" SourceAsset
```

Quellprodukte bleiben eigenständig. Interne stabile IDs verbinden urbane Objekte; Quell-IDs bleiben Referenzen. Beobachtungen, Features und Predictions sind getrennte, versionierte Entitäten mit Provenance.
