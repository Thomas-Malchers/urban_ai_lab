# ADR-005: Batch First

**Status:** Proposed

## Context
Urbane Geodaten werden überwiegend flächen- und bestandsbezogen verarbeitet.
## Decision
Batch Inference wird vor produktivem Online Serving priorisiert.
## Consequences
Reproduzierbarkeit und Betrieb bleiben zunächst überschaubar; niedrige Online-Latenz ist kein frühes Ziel.
## Alternatives Considered
Online-first und gleichzeitiger Aufbau beider Serving-Arten.
## Related Documentation
[Inference](../docs/04_ai-platform/inference.md)
