# L2 – Domain Data Processing

**Status: Conceptual**

```mermaid
flowchart LR
    S["Source"] --> I["Ingestion"] --> R["Raw Asset"]
    R --> V["Validation"] --> P["Domain Processing"]
    P --> Q["Domain Quality"] --> O["Standardized / Published Asset"]
```

Die Pipeline-Struktur kann ähnlich sein; die inhaltliche Quality-Logik ist je Datendomäne unterschiedlich. Konkrete Schwellenwerte sind noch offen.

| Domäne | Qualitätsdimensionen |
|---|---|
| Orthophoto | technische Lesbarkeit, CRS, Auflösung, Abdeckung, NoData, Bildqualität, zeitliche Eignung |
| LiDAR | technische Lesbarkeit, Punktdichte, Ausreißer, Klassifikation, Höhenreferenz, räumliche Abdeckung |
| CityGML | Schema, IDs, geometrische Validität, Topologie, Semantik, Vollständigkeit, Höhenbezug |
