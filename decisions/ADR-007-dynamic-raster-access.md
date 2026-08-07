# ADR-007: Dynamic Raster Access

**Status:** Proposed

## Context
Persistente Chip-Bestände duplizieren große Orthofoto-Datenmengen und erschweren reproduzierbare Dataset-Versionen.

## Decision
Orthophoto-Chips werden standardmäßig dynamisch aus COG-basierten Assets gelesen. Manifests versionieren Referenzen und Generierungsparameter.

## Consequences
Einzeldateien entstehen nur für begründete Exporte oder Caches; Zugriff und Cache-Strategien müssen definiert werden.

## Related Documentation
[Storage & Access](../docs/l2-storage-access.md)
