# Adversarial Recheck v3 — Aachen

SCORE: 87/100
MUST-FIX vor Deploy: JA

## v2-MUST-FIX Status — alle behoben
- §-Zitation BestG NRW
- Kostenkorridor-Phrasenwüste (4 Tabellen, Stichtag 17.12.2025)
- Ostfriedhof "ausschließlich Urnenbeisetzungen"

## NEUE FUNDE (3 MUST-FIX)

### SCHWÄCHE 1: § 13 Abs. 2 BestG NRW für 24h-Frist wahrscheinlich falsch zugeordnet
NRW-Fassung: 24h-Mindestfrist in § 13 Abs. 1, NICHT Abs. 2. § 13 Abs. 2 = 10-Tage-Frist. § 13 Abs. 3 = Urnenbeisetzung 6 Wochen. v3 verschiebt unzulässig.
Verbesserung: Absatznummern eins-zu-eins am recht.nrw.de gegenchecken; FAQ-Schema-Zuordnung angleichen.

### SCHWÄCHE 2: Quellenlink Gebührensatzung INKONSISTENT
Body: "17. Änderungssatzung vom 17.12.2025". Datei: "16-aenderungssatzung-der-friedhofsgebuehrenordnung.pdf".
Verbesserung: PDF-URL prüfen, Satzungs-Nummer im Text + Linktarget angleichen.

### SCHWÄCHE 3: Heißbergfriedhof UNSURE-Kommentar im HTML-Body
Pipeline-Leakage in Production-HTML. "Interkonfessionell" hängt an Reiseblog.
Verbesserung: Primärquelle (Stadtarchiv Aachen) oder neutrale Formulierung. UNSURE-Kommentare vor Deploy strippen.

## Zusatz (klein)
- "Anzeige des Todes spätestens am dritten Werktag" ohne § (Rechtsgrundlage § 28 PStG)
- Mies van der Rohe Chicago — korrekt aber unbelegt
