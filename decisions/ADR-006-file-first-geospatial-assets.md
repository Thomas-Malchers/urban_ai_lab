# ADR-006: File-first for Large Geospatial Assets

**Status:** Proposed

## Context
Große Raster-, Punktwolken- und 3D-Bestände sind teuer zu duplizieren und nicht für jeden Zugriff vollständig in einer Datenbank erforderlich.

## Decision
Große Geo-Assets sollen primär file-basiert in offenen, partiell lesbaren Formaten gespeichert werden. Datenbanken sind nicht automatisch Primärspeicher für alle Roh- und Analysebestände.

## Consequences
Storage und Compute bleiben getrennt; Katalogisierung, Versionierung und Lifecycle-Management werden notwendig.

## Related Documentation
[Storage & Access](../docs/l2-storage-access.md)
