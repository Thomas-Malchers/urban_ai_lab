---
title: Logische Gesamtarchitektur
status: draft
architecture_state: target
owner: Urban AI Lab
last_reviewed: 2026-08-06
---

# Logische Gesamtarchitektur

**Status: Zielbild.** Das Diagramm zeigt Fähigkeiten, keine festgelegten Produkte.

```mermaid
flowchart LR
 subgraph S["1. Datenquellen"]
  O[Orthofotos]
  L[LiDAR]
  C[CityGML / 3D]
  V[Vektor, Tabellen, APIs]
  H[Annotationen & Korrekturen]
 end
 subgraph D["2. Urban Data Platform"]
  I[Ingestion & Raw Data]
  P[Domänenspezifische Pipelines]
  U[Urbane Datenprodukte]
  F[Features & Indikatoren]
 end
 subgraph A["3. AI & Analytics Platform"]
  DS[Data Science & Datasets]
  TR[Training & Registry]
  IN[Inference]
  AL[Monitoring, Review & Active Learning]
 end
 subgraph E["4. Nutzung & Bereitstellung"]
  API[APIs & Datenzugriff]
  VIS[Visualisierung]
  APP[Demonstratoren & Exporte]
 end
 subgraph X["5. Übergreifende Plattformfunktionen"]
  META[Metadaten, Versionen & Lineage]
  GOV[Governance, Security & Observability]
 end
 O & L & C & V --> I
 I --> P --> U --> F
 H --> DS
 U & F --> DS --> TR --> IN --> U
 IN --> AL --> DS
 U & F --> API --> APP
 U --> VIS --> APP
 META --- I
 META --- U
 META --- TR
 GOV --- P
 GOV --- IN
 GOV --- API
```

Qualitätsprüfungen bleiben Teil der jeweiligen Domänenpipeline. Übergreifende Fähigkeiten vereinheitlichen nur Steuerung und Nachweis.
