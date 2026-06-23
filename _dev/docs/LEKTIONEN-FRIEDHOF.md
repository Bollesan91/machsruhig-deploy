# LEKTIONEN — FRIEDHOF (Findings-Gedächtnis für Friedl)

> Pflichtteil jedes Bau-/Review-Prompts für Friedhofseiten (`_dev/FRIEDL.md`). False Positives → `OFFENE-REVIEW-PUNKTE-FRIEDHOF.md`.

## Nachtrag 23.06.2026 (Erstlauf Hamburg AöR — Ohlsdorf Goldstandard)

1. **Träger bündelt — eine Satzung deckt mehrere Friedhöfe.** Hamburger Friedhöfe -AöR-: EINE Gebührenübersicht 2025 für Ohlsdorf/Öjendorf/Volksdorf/Wohldorf. Gebühren-Record pro **Träger** anlegen, Friedhöfe referenzieren ihn — nicht pro Friedhof neu ziehen.
2. **GBO-PDF in WebFetch „garbled" ≠ unlesbar.** Die WebFetch-Konvertierung meldete die Gebührenübersicht-PDF als unlesbar (komprimierter Fontstream); lokal mit `pdfplumber`/`pdftotext` kam sauberer Volltext (Umlaute korrekt). → Eine vom Tool als unlesbar gemeldete PDF erst lokal extrahieren, bevor man die Quelle aufgibt (vgl. #52).
3. **Friedl-Linter fing zwei echte Fehler, die ich übersah:** (a) toter Breadcrumb-Link auf den noch nicht gebauten Aggregations-Hub → Standalone-Friedhof braucht seinen Hub gleich mit; (b) FAQ-JSON-LD-Parität: sichtbare Summary nutzte ASCII-`"` als typografisches Anführungszeichen, JSON-LD das deutsche `“` → Mismatch. **Regel: in JSON-LD und sichtbarem Text dieselben deutschen Anführungszeichen `„ “` (U+201E/U+201C) verwenden — nie ASCII `"` (bricht JSON, Lektion vom Angebotsstandard).**
4. **Gebühren-Einheit-Falle: Block-Überschrift auf JEDE Unterzeile anwenden.** „102 Urnenwahlgrabstätten, **je Jahr**" gilt auch für 1026 Kolumbarium (188) und 1029 Urnenwand (183) — die sind je Urne **und Jahr**, nicht einmalig. Review-Fund (MINOR). Bei Satzungs-Tabellen die je-Jahr/je-Ruhezeit-Überschrift jeder Tarifzeile mitgeben, sonst liest es sich als Einmalbetrag.
5. **Ruhezeit steht NICHT in der Gebührenübersicht.** Sie kommt aus Friedhofssatzung/Landes-BestattG — separat belegen + attribuieren („Ruhezeit 25 Jahre, Hamburger Friedhofssatzung"). Der target-blinde Reviewer kann sie aus dem GBO-Auszug nicht prüfen → seine UNSICHER-Markierung ist erwartbar, kein Fehler; Stufe-3-Beleg liefert die separate Quelle.
6. **Datensatz-Review (Stufe 2) funktioniert:** Reviewer bekam Satzungs-Auszug + Webangaben, bestätigte alle 12 Beträge + beide Summen (Zitatpflicht, „rechne nach"). 0 MAJOR. Der Modus skaliert (Record statt Seite).
