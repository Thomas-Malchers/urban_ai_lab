# ADR-008: CityGML Analytical Representation

**Status:** Proposed

## Context
CityGML ist eine wichtige Source-Repräsentation, aber hierarchische XML-/GML-Strukturen sind für analytische Tabellenverarbeitung nur eingeschränkt geeignet.

## Decision
Normalisierte CityGML-Objekte sollen als GeoParquet nutzbar gemacht werden. Raw CityGML, Source IDs und Semantik bleiben erhalten.

## Consequences
Parsing, semantische Normalisierung und Geometriekonvertierung müssen explizit definiert werden.

## Related Documentation
[Storage & Access](../docs/l2-storage-access.md)
