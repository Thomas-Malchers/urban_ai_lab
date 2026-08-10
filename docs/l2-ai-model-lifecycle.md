# L2 – AI Model Lifecycle

**Status: Conceptual**

```mermaid
flowchart LR
    D["Data Platform<br/>Published Data"] --> M["Dataset Manifest"]
    M --> A["Annotation / Review"] --> T["Training"] --> E["Evaluation"]
    E --> MV["Model Version"] --> I["Batch Inference"]
    I --> P["Prediction Version"] --> R["Quality / Human Review"]
    R --> PDP["Prediction Data Product"] --> D
    PDP --> APP["API · Map · Demonstrator"]
    R --> A
```

- A dataset version is not necessarily a folder of duplicated files. Manifests can reference existing source assets.
- Preprocessing and postprocessing are versioned.
- Model output is a prediction, not ground truth; predictions have independent versions.
- Human review never silently overwrites the original prediction.
- Batch inference is initially the primary mode.
- Active learning is the complete feedback loop of prediction, review, selection, and renewed annotation—not one algorithm.
- Reviewed predictions return to the Data Platform as governed data products before publication or reuse in another dataset version.
