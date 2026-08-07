---
title: Systemkontext
status: draft
architecture_state: target
owner: Urban AI Lab
last_reviewed: 2026-08-06
---

# Systemkontext

Das Urban AI Lab übernimmt Daten von öffentlichen, institutionellen und manuellen Quellen. Data Scientists, Entwickler, Fachanwender und die Öffentlichkeit nutzen ausschließlich freigegebene Datenprodukte über passende Zugriffspfade. Daten- und Modellverantwortliche prüfen Qualität, Versionen und Freigaben.

```mermaid
flowchart LR
  Q[Urbane Datenquellen] --> U[Urban AI Lab]
  T[Data & Model Stewards] <--> U
  U --> DS[Data Scientists]
  U --> DEV[Entwickler]
  U --> F[Fachanwender]
  U --> O[Öffentlichkeit]
```
