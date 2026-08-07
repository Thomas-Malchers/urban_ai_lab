# Entscheidungen & offene Fragen

## Als Nächstes zu entscheiden

1. Welche Raw- und Standardformate verwenden wir verbindlich je Datendomäne?
2. Ist COG das Standardformat für aufbereitete Orthofotos?
3. Ist GeoParquet das Standardformat für normalisierte CityGML-Daten?
4. Ab welcher Datengröße oder welchem Workflow setzen wir Spark + Sedona ein?
5. Welche Rolle übernimmt PostGIS gegenüber dem file-basierten Data Layer?
6. Welche strukturierten Transformationen sollen mit dbt umgesetzt werden?

## Storage

- Object Storage oder Filesystem?
- Wie partitionieren und versionieren wir Assets?
- Welche Retention- und Cache-Strategien gelten?

## Raster

- Wie erzeugen und prüfen wir COGs?
- Wie entstehen dynamische Chips und Dataset Manifests?
- Welche Exporte benötigt der Annotation-Prozess?

## CityGML

- Welcher Parser und welches normalisierte Semantikmodell werden verwendet?
- Wie werden GML-Geometrien konvertiert und GeoParquet-Schemas gestaltet?
- Wo liegt die Schwelle für Spark / Sedona?

## Integration

- Wie definieren wir `building_id`, erhalten Source IDs und behandeln Zeit?
- Wie erfolgt Cross-Source-Matching?

## Serving

- Welche Daten werden in PostGIS veröffentlicht, welche bleiben file-basiert?
- Welche APIs werden tatsächlich benötigt?

## Transformation

- Nutzen wir dbt; wenn ja, für welche Modelle?
- Wo verläuft die Grenze zwischen Spark SQL und dbt?
- Welche Tests gehören auf welchen Layer?

Technische Entscheidungen werden weiterhin als ADR im Repository dokumentiert.
