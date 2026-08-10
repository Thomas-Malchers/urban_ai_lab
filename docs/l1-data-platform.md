# L1 – Data Platform

## How do heterogeneous sources become usable data products?

```mermaid
flowchart LR
    subgraph S["Sources"]
        O["Orthophotos"]
        L["LiDAR"]
        C["CityGML"]
        E["Other data"]
    end
    subgraph R["Raw Asset Store / Source Collections"]
        RO["Raw orthophoto collection"]
        RL["Raw LiDAR collection"]
        RC["Raw CityGML collection"]
        RE["Other raw collections"]
    end
    subgraph P["Domain-specific Processing & Quality"]
        OP["Orthophoto"]
        LP["LiDAR"]
        CP["CityGML"]
        EP["Other domains"]
    end
    subgraph D["Urban Data Layer"]
        STD["Standardized / Optimized Domain Assets<br/>COG · LAZ/COPC · normalized GeoParquet"]
        INT["Integrated Urban Data<br/>Canonical Urban Entities"]
        DER["Observations · Derived Features · Predictions"]
    end
    subgraph A["Access"]
        DS["Data Science"]
        API["APIs"]
        VIS["Visualization"]
        AIM["AI / Model Platform"]
    end

    O --> RO --> OP
    L --> RL --> LP
    C --> RC --> CP
    E --> RE --> EP
    OP & LP & CP & EP --> STD
    STD --> INT --> DER
    INT & DER --> DS & API & VIS & AIM
    AIM -- "Versioned predictions" --> DER
```

## Raw asset store and source collections

Original assets remain traceable and are never overwritten. They may share physical object storage, but remain separate logical collections for orthophotos, LiDAR, CityGML, and other domains.

## Domain-specific processing

Each data type has dedicated processing and quality logic. Orthophotos, LiDAR, and CityGML are not forced through one generic quality process.

## Standardized and optimized domain assets

Standardization produces domain products suited to further processing; it does not force all domains into one homogeneous schema. Examples include COG orthophoto collections, LAZ or COPC LiDAR collections, and normalized GeoParquet city models.

## Integrated urban data

Spatial and semantic linking connects assets and records to canonical urban entities such as buildings, roofs, road segments, parcels, vegetation objects, and grid cells. Buildings are the first likely implementation focus, not the platform boundary. Source identifiers and provenance remain intact.

## Observations, features, and predictions

Reproducibly derived values retain their source, method, status, and pipeline version. Predictions written back by the AI / Model Platform remain distinguishable from observations, imported values, calculated features, imputations, and manual corrections.

## Access

The platform publishes data for Data Science, APIs, visualization, and the AI / Model Platform. Applications can consume Data Platform products without requiring an AI workflow.
