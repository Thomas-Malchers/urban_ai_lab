# Data Domains

| Aspekt | Orthophoto | LiDAR | CityGML |
|---|---|---|---|
| Datentyp | Raster | Punktwolke | semantisches 3D-Modell |
| primäre Raw-Repräsentation | GeoTIFF / Source Raster | LAS / LAZ | GML / XML |
| mögliche standardisierte Repräsentation | COG | LAZ / COPC-Kandidat | GeoParquet |
| zentrale Einheit | Tile / Asset / Window | Tile / Punkte | Gebäude / Flächen |
| Processing | Windowing, Resampling, Raster Processing | Filterung, Klassifikation, Spatial Processing | Parsing, Normalisierung, Spatial Processing |
| Quality | Bild, Auflösung, Abdeckung | Punktdichte, Ausreißer, Klassifikation | Geometrie, Topologie, Semantik |
| mögliche Compute-Engine | GDAL / Rasterio / Python | PDAL / Python / ggf. Spark | Python / PySpark + Sedona |
| typische Nutzung | CV, Mapping | Höhe, Gelände, Vegetation | Gebäudeintegration, 3D |

Die genannten Formate und Werkzeuge sind Proposed Patterns beziehungsweise Kandidaten, keine abschließend beschlossene Implementierung. Domänenspezifische Processing- und Quality-Logik wird bei aktiver Umsetzung vertieft.
