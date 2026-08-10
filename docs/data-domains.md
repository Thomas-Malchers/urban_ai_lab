# Data Domains

| Aspect | Orthophoto | LiDAR | CityGML |
|---|---|---|---|
| Data type | Raster | Point cloud | Semantic 3D model |
| Primary raw representation | GeoTIFF / source raster | LAS / LAZ | GML / XML |
| Possible standardized representation | COG | LAZ / COPC candidate | GeoParquet |
| Central unit | Tile / asset / window | Tile / points | Building / surfaces |
| Processing | Windowing, resampling, raster processing | Filtering, classification, spatial processing | Parsing, normalization, spatial processing |
| Quality | Image, resolution, coverage | Point density, outliers, classification | Geometry, topology, semantics |
| Possible compute engine | GDAL / Rasterio / Python | PDAL / Python / possibly Spark | Python / PySpark + Sedona |
| Typical use | Computer vision, mapping | Height, terrain, vegetation | Building integration, 3D |

These formats and tools are proposed patterns or candidates, not final implementation decisions. Domain-specific processing and quality logic will be refined when implementation starts.
