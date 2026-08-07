# Data Products

Ein Data Product besitzt Name, Zweck, Owner, Nutzer, Inputs, Outputs, Schnittstellen, Qualitätsversprechen, Aktualisierungsprozess, Version, Abhängigkeiten, Status und bekannte Einschränkungen. Beispiele sind Orthophoto Collection, LiDAR Collection, City Building Model, Integrated Buildings, Roof Object Predictions und Urban Heat Indicators.

Veröffentlichung ist ein expliziter, auditierbarer Statuswechsel. Projektartefakte werden dadurch nicht automatisch zu Datenprodukten.

## Fehlende und abgeleitete Werte

> Fehlende Werte dürfen nicht stillschweigend durch geschätzte Werte ersetzt werden.

Werte werden als `observed`, `imported`, `calculated`, `predicted`, `imputed`, `manually_validated` oder `manually_corrected` gekennzeichnet. Ergänzend können `method`, `source`, `version`, `quality_status`, `uncertainty`, `valid_time` und `creation_time` geführt werden. Beispiel: Eine berechnete Gebäudehöhe referenziert Quellassets und Algorithmusversion; eine imputierte Höhe bleibt davon unterscheidbar.
