# ADR-009: Spark / Sedona for Scalable Geospatial Processing

**Status:** Proposed

## Context
Große räumliche Bestände und Spatial Joins können verteilte Batch-Verarbeitung benötigen; lokale Workloads rechtfertigen diese Komplexität nicht immer.

## Decision
PySpark mit Apache Sedona wird als Kandidat für skalierbare geospatial Batch-Verarbeitung bewertet. Es ist kein verpflichtender Pfad für kleine lokale Workloads.

## Consequences
Skalierungsschwellen und kompatible lokale Ausführungswege müssen festgelegt werden. CityGML-Parsing bleibt ein vorgelagerter Schritt.

## Related Documentation
[Storage & Access](../docs/l2-storage-access.md)
