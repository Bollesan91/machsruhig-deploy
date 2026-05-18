In Arbeit
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/mannheim/index.html

Systematische Prüfung Mannheim:

Inhaltscheck:

Hauptfriedhof Wohlgelegen 14.7.1842, 34,4 ha — Wikipedia bestätigt
Jüdischer Friedhof 1842, 2,8 ha, größter in BW — konsistent
Käfertal "älterer als Hauptfriedhof, um 1830" — konsistent in Lead, Keyfacts, FAQ, Body
§§ BestattG BW (31, 32, 37, 39, 9) — Reihenfolge der Bestattungspflichtigen entspricht § 31 BestattG BW
Ruhezeiten 15/10/30 — durchgehend konsistent zwischen Tabelle, FAQ, Schema
Gebührentabelle: 910 € / 1.247 € / 1.266 € / 424 € — in FAQ, Tabelle und Schema identisch

Selbstwidersprüche: Keine entdeckt — Daten zwischen Lead, Keyfacts, Tabellen, FAQ und Schema sind durchgehend kongruent.

Strukturcheck: Alle Sektionen vorhanden (Recht, Ruhezeiten, 10 Friedhöfe, Hauptfriedhof, Jüdischer Friedhof, Käfertal, Kosten, Todesfall-Schritte, Bestatter-Wahl, FAQ, Quellen). Keine Duplikate.

SEO/Schema:

❌ Article-Knoten hat KEIN image und Publisher KEIN logo — exakt derselbe Fix wie bei Bochum nötig
❌ OG-Image ist generisch og-image.png statt stadtspezifisch og-mannheim.png — Pipeline-Leakage (Bochum hatte og-bochum.png)
❌ og:image:alt Tag fehlt komplett (Bochum hatte ihn)

UI/UX:

❌ Nav-Link "Bestatter finden" → /bestatter/muenchen/ und Footer-Link "Bestatter" → /bestatter/muenchen/ — beides dead cross-link (selber Bug wie Bochum v6, wurde dort gefixt, hier nicht)

Pipeline-Leakage: Keine <!-- UNSURE --> Marker, aber generisches OG-Image ist klares Leakage-Signal.

STADT: MANNHEIM VERDICT: MAJOR-FIX

1) Schema.org Article: image + Publisher-Logo fehlen

Was: Im JSON-LD @graph hat das Article-Objekt kein image-Property; publisher ist nur {name} ohne logo als ImageObject. Google-required für Article-Rich-Results → Rich Results Test wirft Error, Article-Karte wird unterdrückt. Identischer Bug wie auf der Bochum-v6.
Wo: <script type="application/ld+json"> → Article-Knoten im @graph
Fix: "image":"https://machsruhig.de/assets/og-mannheim.png" ergänzen und publisher zu {"@type":"Organization","name":"machsruhig.de","logo":{"@type":"ImageObject","url":"https://machsruhig.de/assets/logo.png"}} erweitern.

2) Pipeline-Leakage: generisches OG-Image + fehlender Alt-Tag

Was: og:image zeigt auf og-image.png (generischer Default), nicht auf eine stadtspezifische Variante. og:image:alt fehlt komplett. Auf Social-Previews erscheint kein Mannheim-Bezug, Accessibility-Tag fehlt. Bochum-Page hatte korrekt og-bochum.png plus alt-Tag — Pipeline-Drift sichtbar.
Wo: <head> → <meta property="og:image"> + og:image:secure_url
Fix: Auf https://machsruhig.de/assets/og-mannheim.png umstellen (oder Asset erstellen) und <meta property="og:image:alt" content="Hauptfriedhof Mannheim Wohlgelegen — Bestattung in Mannheim"> ergänzen. Auch im JSON-LD WebPage.primaryImageOfPage und Article.image mitziehen.

3) Dead Cross-Links zu München in Nav UND Footer

Was: Nav-Link „Bestatter finden" zeigt auf /bestatter/muenchen/; Footer-Link „Bestatter" ebenfalls. Auf einer Mannheim-Seite verweist die Hauptnavigation den User nach München — Topical-Inconsistency, UX-Bruch und SEO-Signal-Streuung. Wurde auf Bochum-v7 bereits gefixt, hier nicht propagiert.
Wo: <nav class="mr-nav"> letzter Link + <footer> Tools-Spalte
Fix: Beide auf /bestatter/ umstellen (Stadt-Hub).
Abrufen von raw.githubusercontent.com