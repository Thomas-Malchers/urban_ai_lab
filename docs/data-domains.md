# Data Domains

| Aspekt | Orthofoto | LiDAR | CityGML |
|---|---|---|---|
| Datentyp | Raster | Punktwolke | semantisches 3D-Modell |
| zentrale Einheit | Tile / Asset | Tile / Punkte | Gebäude / Flächen |
| typische Verarbeitung | Tiling, Konvertierung, Ausschnitte | räumliche Indizierung, Klassifikation | Parsing, Normalisierung |
| Qualitätsschwerpunkt | Bild, Auflösung, Abdeckung | Punktdichte, Ausreißer, Klassifikation | Geometrie, Topologie, Semantik |
| typische Nutzung | Computer Vision, Mapping | Höhe, Gelände, Vegetation | Gebäudeintegration, 3D |

## Orthofoto

Rasterdaten werden über räumliche Auflösung, Kacheln, Bildqualität, Abdeckung und zeitliche Aktualität beschrieben. Sie bilden eine wichtige Grundlage für Mapping und Computer Vision.

## LiDAR

Punktwolken werden insbesondere anhand von Punktdichte, Klassifikation, Höhenbezug und Abdeckung bewertet. Sie unterstützen Analysen von Gelände, Höhe und Vegetation.

## CityGML

Semantische 3D-Modelle beschreiben Gebäude, Building Parts sowie Dach- und Fassadenflächen. Im Mittelpunkt stehen Geometrie, Topologie, Semantik und Vollständigkeit.

Die konkrete Pipeline- und Qualitätsspezifikation einer Datendomäne wird erst vertieft, wenn diese Domäne aktiv implementiert oder überarbeitet wird.
