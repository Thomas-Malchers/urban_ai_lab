# Vertical Slice

Der Slice beginnt mit einem unveränderten Orthofoto-Asset und endet an einer veröffentlichten Schnittstelle. Orthofotoqualität ist nicht Prediction Quality; Modelloutput bleibt Prediction. Gebäudezuordnung ist ein eigener Integrationsschritt. Pre- und Postprocessing sind versioniert, Korrekturen überschreiben nie das Modellresultat.

```mermaid
flowchart TD
 O[Orthofoto Source] --> I[Ingestion] --> QO[Orthofoto Quality] --> C[Published Collection]
 C --> CH[Reproduzierbare Chips] --> DM[Dataset / Inference Manifest] --> PRE[Preprocessing] --> M[Object Detection Model]
 M --> POST[Postprocessing] --> G[Georeferenzierung & Merging] --> QP[Prediction Quality]
 QP --> B[Building / Roof Assignment] --> R[Review Queue] --> VP[Versionierte Predictions]
 VP --> F[Freigegebene urbane Merkmale] --> X[API / Demonstrator]
```
