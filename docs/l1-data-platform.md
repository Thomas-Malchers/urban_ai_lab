# L1 – Data Platform

## Wie werden heterogene Quellen zu nutzbaren Datenprodukten?

```mermaid
flowchart LR
    subgraph S["Sources"]
        O["Orthophotos"]
        L["LiDAR"]
        C["CityGML"]
        E["Weitere Daten"]
    end
    RAW["Immutable Source Assets"]
    subgraph P["Domain Processing"]
        OP["Orthophoto<br/>Processing + Quality"]
        LP["LiDAR<br/>Processing + Quality"]
        CP["CityGML<br/>Processing + Quality"]
        EP["Other Domain<br/>Processing"]
    end
    subgraph D["Urban Data Layer"]
        STD["Standardized Data"]
        INT["Integrated Urban Data"]
        DER["Derived Features / Indicators"]
    end
    subgraph A["Access"]
        DS["Data Science"]
        API["APIs"]
        VIS["Visualization"]
        AI["AI / Model Platform"]
    end
    O & L & C & E --> RAW
    RAW --> OP & LP & CP & EP
    OP & LP & CP & EP --> STD
    STD --> INT --> DER
    INT & DER --> DS & API & VIS & AI
```

## Raw / Source Layer

Originaldaten bleiben nachvollziehbar erhalten und werden nicht überschrieben. Transformationen erzeugen neue Repräsentationen.

## Domain Processing

Jede Datenart besitzt eigene Processing- und Quality-Logik. Orthophoto, LiDAR und CityGML werden nicht durch denselben generischen Qualitätsprozess gedrückt.

## Standardized Data

Daten werden für weitere Verarbeitung aufbereitet. Standardisierung bedeutet nicht, dass alle Domänen dasselbe Format erhalten.

## Integrated Urban Data

Gemeinsame urbane Objekte verbinden die Quellen. Gebäude sind zunächst ein wichtiger Integrationsanker; Source IDs und Provenance bleiben erhalten.

## Derived Features

Merkmale werden reproduzierbar abgeleitet. Herkunft, Methode und Version bleiben nachvollziehbar.

## Access

Die Plattform stellt Daten für Data Science, APIs, Visualisierung und die AI / Model Platform bereit.
