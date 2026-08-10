# L0 – Overall Architecture

## What is the long-term target system of the Urban AI Lab?

```mermaid
flowchart LR
    S["Urban Sources<br/>Orthophotos · LiDAR · CityGML · other data"]
    D["Data Platform<br/>Ingest · Quality · Integrate · Publish"]
    AI["AI / Model Platform<br/>Train · Infer · Monitor · Improve"]
    C["Exposure & Applications<br/>Data Science · APIs · Maps · 3D · Demonstrators"]

    S --> D
    D -- "Published data products" --> AI
    AI -- "Versioned prediction data products" --> D
    D --> C
    AI --> C
```

1. Urban source data is ingested and prepared through a shared Data Platform.
2. Each data domain retains its own processing and quality logic.
3. The AI / Model Platform is both a consumer and a producer of the Data Platform: it consumes published data products and writes reviewed, versioned predictions back as data products.
4. Applications may consume data products directly, AI results directly, or both. They do not have to pass through the AI platform.
