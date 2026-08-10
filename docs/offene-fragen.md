# Decisions & Open Questions

## Architecture decisions to make next

1. What storage pattern applies to each data class?
2. How do we version and catalog data, assets, and their lineage?
3. What are our canonical urban entities and stable identifier rules?
4. How do we distinguish source data, observations, features, imputations, predictions, and manual corrections?
5. Where does each kind of compute run?
6. How are data products published and consumed?

Tools support these decisions; they do not define the architecture. Current candidates include COG, GeoParquet, and COPC for storage patterns; STAC for asset catalogs; local Python or Spark / Sedona for compute; dbt for managing suitable SQL transformations; and PostGIS for curated entities, relations, and serving.

## Storage and catalog

- Object storage or filesystem?
- Which raw and standardized formats apply to each domain?
- Is COG the standard for processed orthophotos, GeoParquet for normalized CityGML projections, and COPC useful for LiDAR?
- How are assets partitioned, versioned, retained, cached, and cataloged through STAC?

## Canonical entities and integration

- Which entities do we introduce first: buildings, roofs, road segments, parcels, vegetation objects, or grid cells?
- How do we define stable internal IDs, retain source IDs, represent time, and perform cross-source matching?
- How do normalized CityGML projections preserve hierarchy, semantics, and provenance?

## Value provenance

- Which metadata is mandatory for observed, imported, calculated, imputed, predicted, and manually corrected values?
- How are conflicts and missing values exposed to consumers?

## Compute and transformation

- When is local Python sufficient, and when does Spark / Sedona provide measurable value?
- Which transformations run on Spark / Sedona and which on PostGIS?
- For which SQL transformations do we use dbt for modeling, versioning, testing, and materialization?

## Publication and consumption

- Which curated entities and relations belong in PostGIS, and which large assets remain file-based?
- Which products are consumed by Data Science, APIs, visualization, and AI workflows?
- What review gates apply before predictions are written back as Data Platform products?

Technical choices continue to be documented as ADRs in this repository.
