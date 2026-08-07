# ADR-010: dbt for Structured Transformations

**Status:** Proposed

## Context
Strukturierte Tabellen und Views benötigen versionierte, getestete und dokumentierte Transformationslogik.

## Decision
dbt wird als Kandidat für strukturierte Transformationen bewertet, nicht als Engine für Raster-, LiDAR- oder CityGML-Raw-Processing.

## Consequences
Die Grenze zu Python, Spark und Spark SQL sowie unterstützte Datenmodelle müssen definiert werden.

## Related Documentation
[Data Integration & Transformation](../docs/l2-data-integration-transformation.md)
