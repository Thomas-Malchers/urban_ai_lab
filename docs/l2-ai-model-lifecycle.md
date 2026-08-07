# L2 – AI Model Lifecycle

**Status: Conceptual**

```mermaid
flowchart LR
    D["Published Data"] --> M["Dataset Manifest"]
    M --> A["Annotation / Review"] --> T["Training"] --> E["Evaluation"]
    E --> MV["Model Version"] --> I["Batch Inference"]
    I --> P["Prediction Version"] --> R["Quality / Human Review"]
    R --> O["Published Result"]
    R --> A
```

- Eine Dataset-Version ist nicht gleichbedeutend mit einem Ordner duplizierter Dateien. Manifests können bestehende Source Assets referenzieren.
- Preprocessing und Postprocessing werden versioniert.
- Modelloutput ist eine Prediction, keine Ground Truth; Predictions besitzen eigene Versionen.
- Human Review überschreibt ursprüngliche Predictions nicht stillschweigend.
- Batch Inference ist zunächst der primäre Modus.
- Active Learning bezeichnet den gesamten Feedback-Loop aus Prediction, Review, Auswahl und erneuter Annotation – keinen einzelnen Algorithmus.
