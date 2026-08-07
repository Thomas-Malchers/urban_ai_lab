# End-to-End-Datenfluss

```mermaid
flowchart LR
 A[Source Asset] --> B[Standardized Asset] --> C[Curated Object] --> D[Derived Feature] --> E[Model Prediction] --> F[Reviewed Result] --> G[Published Data Product]
```

Jeder Übergang erzeugt eine neue, versionierte Repräsentation. Freigabe, Review und Fehlerbehandlung sind explizite Gates; Rückmeldungen verändern niemals stillschweigend das Original.
