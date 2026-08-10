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

Technical choices continue to be documented as ADRs in this repository. Existing Proposed ADRs are not Accepted decisions.
