# ADR-004: Immutable Raw Data

**Status:** Proposed

## Context
Überschriebene Quellen verhindern Reproduktion und Audit.
## Decision
Rohdaten werden nicht überschrieben; Transformationen erzeugen neue Repräsentationen und Versionen.
## Consequences
Lineage bleibt erhalten, Speicher- und Lifecycle-Management werden notwendig.
## Alternatives Considered
In-place-Bereinigung und nur aktuelle Snapshots.
## Related Documentation
[Ingestion und Storage](../docs/02_data-platform/ingestion-and-storage.md)
