Ich lade die drei Dateien und prüfe v3.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

BRIEFING_OK.

Ich zerlege v3 mit Fokus auf MUST-FIX-Behebung aus Runde 4 (76%) und neue Schwächen.

Check Runde-4-MUST-FIX:

FAQ-Schema vs. Fließtext (Konjunktiv vs. Indikativ Novelle) → ✅ Behoben. FAQ-Schema, Fließtext und Keyfacts sind jetzt konsistent im Konjunktiv („verlängert werden soll", „zum Redaktionsstand nicht zweifelsfrei belegt"). Saubere Fix.
§ 18 vs. § 19 FBG (sarglose Bestattung) → ✅ Behoben. Steht jetzt korrekt als „§ 19 FBG Hessen, Bestattungsart und Sarg".
Kostentabelle mit nicht primärquellen-belegten Cent-Beträgen → ✅ Behoben. Konkrete Eurobeträge wurden durch „mittlerer dreistelliger", „niedriger vierstelliger Bereich" ersetzt + transparenter Disclaimer.
Mindestruhezeit 15 Jahre / 60 Jahre Grüfte ohne § → ✅ Behoben via <!-- UNSURE -->-Kommentar; konkrete Werte weggelassen.
bensheimer-bestatter.de als Wettbewerber-Link → ✅ Behoben. Nicht mehr in der Page.
Heinrich Felsing „Vereinsgründer TSG Darmstadt" → ✅ Behoben. Steht jetzt nur noch „Kupferdrucker".
Dolivo-Dobrowolsky → ✅ Entfernt (nicht mehr in der Liste).

Sieben von sieben Funden adressiert. Aber: jetzt strenge Suche nach neuen Schwächen.

SCHWÄCHE 1: Sektion „Bestatter-Wahl" — generischer Boilerplate ohne Darmstadt-Bezug

Die Sektion „Bestatter-Wahl in Darmstadt" ist faktisch Generic-Content, der auf jeder Stadt-Page kopierbar wäre. Inhaltlich enthält sie: IHK-Bestattungsfachkraft, BDB/BVB, Kostenvoranschlag-Aufschlüsselung, Vergleichsangebote, Treuhandstelle Deutscher Bestatter. Kein einziger Darmstadt-spezifischer Inhalt — kein lokaler Verband, keine Darmstädter Innung, keine konkret zu prüfenden Darmstädter Anbieter-Eigenheiten, keine Erwähnung der lokalen IHK Darmstadt Rhein Main Neckar, keine Verweise auf einen lokalen Beschwerdeweg. Die Eingangsformulierung „In Darmstadt sind etwa zwei Dutzend Bestattungsunternehmen tätig" ist eine vage Schätzung ohne Quelle und der einzige geo-spezifische Satz. Kategorie 2 (generischer Satz) + Kategorie 9 (fehlender Cross-Link bzw. lokaler Verweis). Verbesserung: Entweder die Sektion auf eine Generic-Seite /bestattung/bestatter-waehlen/ auslagern und hier nur 2-3 Sätze + Cross-Link, oder echte Darmstadt-Spezifika einbauen (IHK Darmstadt Rhein Main Neckar als Verbraucher-Anlaufstelle bei Streit, Hinweis auf Verbraucherzentrale Hessen mit Beratungsstelle Darmstadt, ggf. Bestatter-Innung Südhessen).

SCHWÄCHE 2: Schema.org FAQPage enthält 7 Fragen, sichtbare FAQ-Sektion enthält 7 Fragen — aber sie sind nicht identisch

Schema-FAQ Frage 6 lautet: „Welche Bestattungsformen sind in Darmstadt möglich?" — diese Frage existiert in der sichtbaren FAQ-Sektion nicht. Stattdessen heißt die sichtbare Frage 6: „Sind Baumbestattungen in Darmstadt möglich?" Die Antworten sind ebenfalls inhaltlich unterschiedlich (Schema spricht von Erd-/Urne/Rasen/Wiese/anonym/Baum + FriedWälder; sichtbare FAQ-Antwort fokussiert allein Friedpark/Baumbestattung mit der Trauerwald-Stopp-Info). Das ist ein Google-Rich-Result-Risiko: Schema-FAQ-Antworten, die auf der sichtbaren Seite so nicht auftauchen, sind ein dokumentierter Verstoß gegen die Google Structured Data Guidelines („the content of the FAQ must be visible to the user on the source page"). Kategorie 10 (Schema.org-Inkonsistenz). Verbesserung: Schema-FAQ Frage 6 entweder ändern auf „Sind Baumbestattungen…" mit der sichtbaren Antwort, oder die sichtbare FAQ-Sektion um die Frage „Welche Bestattungsformen sind in Darmstadt möglich?" mit der Schema-Antwort ergänzen. Eins von beiden — sonst riskiert man eine manuelle Maßnahme.

SCHWÄCHE 3: Hero-Statistik „rund 160.000 Einwohner" — Vier-Friedhöfe-Behauptung im Lead widerspricht Kernfakten und FAQ

Der Hero-Lead behauptet: „Vier Anlagen prägen das Friedhofsbild der Stadt — der klassizistische Alte Friedhof […], der hufeisenförmige Waldfriedhof […], der park-artige Bessunger Friedhof […] und der Jüdische Friedhof". Die Keyfacts und FAQ sagen aber konsistent: „6 kommunale Friedhöfe plus Jüdischer Friedhof" (also 7 Anlagen insgesamt). Auch die Sektion „Friedhöfe in Darmstadt" beginnt mit „Vier Friedhöfe prägen das Gesicht der Stadt" — Stadtteilfriedhöfe Eberstadt/Arheilgen/Wixhausen werden als Anhängsel mitgenommen, obwohl Eberstadt laut Stadtteilfriedhof-Absatz „der größte unter den Stadtteilfriedhöfen" ist und faktisch ein Hauptfriedhof eines 25.000-Einwohner-Stadtteils. Das ist nicht falsch im engeren Sinne, aber redaktionell inkonsistent und für Nutzer aus Eberstadt/Arheilgen irritierend („mein Friedhof gehört zu den 6, aber nur 4 sind genannt"). Kategorie 4 (schwacher Übergang/Logikbrücke). Außerdem: Die Hero-Aussage „rund 160.000 Einwohner" hat in v3 die fragwürdige Stichtags-Quellenangabe entfernt — gut. Aber: Wer als kritischer Reviewer prüft, würde inzwischen den aktuellen HSL-Wert (Stand 2024/25: ~159.700) erwarten. Das ist ein kleinerer Nebenfund, kein Hauptproblem. Verbesserung: Hero-Lead umformulieren auf „sechs kommunale Friedhöfe sowie der Jüdische Friedhof" und im selben Satz die vier Hauptanlagen als „prägende vier" einleiten, dann am Ende auf die Stadtteilfriedhöfe verweisen mit Anker-Link. Macht die Information-Architektur sauber.

Weitere Stichproben (nicht Top-3):

Sektion „Bestattungsrecht": Der HTML-Kommentar <!-- UNSURE: ... --> mit dem Satz „die im v1/v2 genannten Werte (15 Jahre, 25/30 Jahre…) waren in v3 ohne stabile Primär-URL nicht zu verifizieren" ist interner Pipeline-Slang im ausgelieferten HTML. Das ist ein Deploy-Blocker — auch wenn nicht sichtbar, sieht jede:r Reviewer im View-Source „v1/v2" und „Pipeline-Spur". Muss vor Deploy raus.
Quellen-Sektion: Drei Wikipedia-Links (Alter Friedhof, Waldfriedhof, Bessunger Friedhof) als Fundstellen für „Hidden-Gem-Hintergrund". Wikipedia in Quellen einer juristisch-sensiblen Seite ist E-E-A-T-Schwäche, auch wenn explizit als „keine Rechtsaussage" gekennzeichnet. Saarland/Vorgänger haben das vermutlich vermieden.
Hidden-Gem Alter Friedhof: Friedrich von Flotow „starb am 24. Januar 1883 in Darmstadt" — Quellen sagen mehrheitlich, Flotow starb am 24. Januar 1883 in Darmstadt, das ist korrekt. „Denkmal des Bildhauers Benedikt König" für Flotow ist eine konkret prüfbare Behauptung ohne Quelle in der Page.
Schema.org Place-Objekte für die vier Friedhöfe haben keine geo-Koordinaten und keine url zu einer offiziellen Stadtseite — schwächere Strukturdaten-Implementierung.
FAQ-Antwort „erste Sterbeurkunde 12 €" wiederholt sich an drei Stellen (FAQ-Schema, sichtbare FAQ, Kostentabelle, Sektion „Nach Todesfall"). Inhaltlich konsistent, aber DRY-Verstoß; falls Gebühr sich ändert, vier Stellen anzupassen.

SCORE: 84/100

FUNDE:

HTML-Kommentar <!-- UNSURE: ... v1/v2 ... --> mit interner Pipeline-Sprache im Production-HTML — muss raus
Schema-FAQ Frage 6 (Bestattungsformen) ist nicht 1:1 in sichtbarer FAQ-Sektion vorhanden — Google-Guidelines-Verstoß für FAQ-Rich-Result
Sektion „Bestatter-Wahl in Darmstadt" ist generischer Boilerplate ohne Darmstadt-Spezifika außer „etwa zwei Dutzend Anbieter"
Hero/Sektions-Lead spricht von „vier Friedhöfen prägen die Stadt", Keyfacts und FAQ sagen „sechs kommunale plus Jüdischer" — informationsarchitektonische Inkonsistenz, die Eberstadt/Arheilgen/Wixhausen marginalisiert
Drei Wikipedia-Links in Quellen-Sektion (Alter, Wald-, Bessunger Friedhof) — E-E-A-T-Schwäche auf juristisch-sensibler Seite
Schema.org Place-Objekte ohne geo-Koordinaten, ohne url-Verweis zur städtischen Friedhofs-Detailseite
Benedikt König als Bildhauer des Flotow-Denkmals — konkrete Personenzuschreibung ohne Quelle
Hero-Aussage „rund 160.000 Einwohner" ohne Stichtag (war in Runde 4 mit Stichtag noch fragwürdig; jetzt ohne Stichtag harmlos, aber HSL-Aktualwert ~159.700 wäre präziser)

MUST-FIX vor Deploy: ja.

Begründung: Zwei harte Blocker — (1) der <!-- UNSURE: v1/v2 -->-Kommentar im Production-HTML ist Pipeline-Leakage, das schaut bei jedem View-Source und bei jedem GitHub-Reviewer peinlich aus und untergräbt das Redaktionsversprechen oben. (2) Die Schema-FAQ/sichtbare-FAQ-Diskrepanz bei Frage 6 verstößt gegen die Google Rich-Result-Guidelines („FAQ content must be visible on the page"). Beides sind 5-Minuten-Fixes, aber bis dahin nicht live. Die anderen Funde sind Nice-to-Have für 90+, aber nicht Deploy-blockierend.

Positive Notiz (gegen das Briefing, daher knapp): Die sieben Adv-Runde-4-Funde wurden alle adressiert, das ist solide Reviewer-Arbeit zwischen Runde 4 und v3.