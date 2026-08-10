# Decisions & Open Questions

The following questions remain open unless an accepted ADR explicitly resolves them. Candidate technologies support architecture decisions; they do not define the architecture by themselves.

## Immediate architecture questions

1. **Object storage:** Which S3-compatible implementation and bucket/prefix structure do we use?
2. **Asset catalog:** Do we adopt STAC for COG/LiDAR, and how is it hosted or indexed?
3. **Orthophoto standard:** Do we accept COG plus dynamic window access as the standard pattern?
4. **LiDAR standard:** Is COPC useful enough to become the Standardized Asset for partial access?
5. **CityGML representation:** Do we choose file-first GeoParquet/Sedona, 3DCityDB/PostGIS, or a justified hybrid?
6. **CityGML parser:** Which component/library performs robust CityGML parsing and semantic normalization?
7. **Spark threshold:** When does PySpark/Sedona add measurable value over local Python?
8. **Table publication:** Do we use Databricks/Unity Catalog external tables over standardized GeoParquet?
9. **Structured transformations:** Do we adopt dbt for integrated/published SQL models and Data Product Quality tests?
10. **PostGIS:** Which concrete requirements, if any, require a separate PostGIS serving/integration layer?

## Cross-cutting model questions

- Which canonical entities come first: buildings, roofs, road segments, parcels, vegetation objects, or grid cells?
- How do we define stable internal IDs, retain source IDs, represent time, and perform cross-source matching?
- Which metadata is mandatory for observed, imported, calculated, imputed, predicted, and manually corrected values?
- How are conflicts, missing values, lineage, Source Snapshots, and Published Data Product versions exposed to consumers?
- What review gates apply before predictions become Published Data Products?

## AI / Model Platform

These questions remain deliberately open unless an ADR resolves them.

### Training and experimentation

1. Which platform provides GPU training, and must any part run on-premises?
2. Is Databricks the central ML platform or is training operated separately?
3. Do we adopt MLflow as the standard experiment tracker and model registry?
4. How are training environments and dependencies reproduced?

### Datasets and annotation

5. Which annotation platform is used: CVAT, Roboflow, or another system?
6. What is the canonical export and storage format for annotations?
7. How are dataset and label versions represented?
8. Which chips are materialized and which are read dynamically from COGs?

### Production inference

9. Does batch inference run in Databricks, on dedicated GPU servers, Kubernetes, or another platform?
10. At what scale does Spark-based workload distribution become useful?
11. How are inference manifests generated, versioned, and tracked?

### Geospatial postprocessing

12. Which component owns georeferencing and geometry construction?
13. What is the default assignment method: maximum overlap, centroid, topology, or another strategy?
14. Which postprocessing steps are model-specific and which are reusable platform capabilities?
15. How are postprocessing versions represented?

### Prediction storage

16. What is the canonical prediction table schema?
17. Are bbox polygons, segmentation polygons, or both retained?
18. Are raw and postprocessed predictions stored in separate tables?
19. How long are raw model predictions retained?

### Monitoring and quality

20. Which system, input, prediction, and geospatial metrics are mandatory?
21. Which quality thresholds block publication and which only warn?
22. Which conditions automatically add samples to review or Active Learning queues?

### Active Learning

23. Which selection strategies are initially supported?
24. How are selections versioned and made reproducible?
25. How do reviewed production predictions become new governed training labels?

### Platform choice

26. Do we choose a Databricks-centric or self-hosted/open ML stack?
27. Which capabilities must be runnable on-premises?
28. Which components may be cloud-only?

Technical choices continue to be documented as ADRs in this repository. Existing Proposed ADRs are not Accepted decisions.
