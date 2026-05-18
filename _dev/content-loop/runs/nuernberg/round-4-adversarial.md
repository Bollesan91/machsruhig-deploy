Ich lese die drei Dateien.

Fetching site
Web durchsucht

Jetzt habe ich alle drei Dokumente. Adversarial Mode an. Ich gehe die v2 systematisch durch und suche substantielle Schwächen — nicht die offensichtlichen aus Round 2, sondern was Chat A in v2 übersehen oder neu eingeführt hat.

Was mir beim Lesen ins Auge fällt:

Schema-Inkonsistenz BestG-Artikel: Der Fließtext sagt "Art. 16 BestG (Bestattungsfristen, frühestens 48 Stunden, spätestens nach 96 Stunden)" und "Art. 19 BestG i.V.m. § 18 BestV (zweite Leichenschau)". Aber: Das Bayerische Bestattungsgesetz hat eine andere Artikel-Struktur — Art. 16 BestG regelt nicht die Bestattungsfristen (das ist § 19 BestV) und Art. 19 BestG ist nicht die Leichenschau-Norm. Das ist ein potenzieller Halluzinations-Verdacht — Round 2 hat genau das "MUST-FIX" gefordert, Chat A hat Nummern eingesetzt, die plausibel klingen, aber falsch sein können. Das prüfe ich schnell.

Searching the web
Web durchsucht

Bestätigt — und das ist ein schwerer Befund:

Die 96-Stunden-Frist ist seit 01.04.2021 abgeschafft und auf acht Tage verlängert. Die Page schreibt aber: "frühestens 48 Stunden, spätestens nach 96 Stunden". Das ist seit 5 Jahren falsch.
Die Bestattungsfrist steht in § 19 Abs. 1 BestV — nicht in Art. 16 BestG. Art. 16 BestG ist die Verordnungsermächtigung.
Die zweite Leichenschau ist nicht "Art. 19 BestG i.V.m. § 18 BestV", sondern wurde durch die Reform 2021 in der BestV neu geregelt und gilt seit 01.01.2023. Art. 19 BestG existiert in der zitierten Form nicht als Leichenschau-Norm.

Das sind harte Halluzinations-Treffer auf YMYL-Niveau. Die Page steht außerdem an drei Stellen prominent mit diesen Falsch-Zitaten (Fließtext, FAQ, Schema.org). Genau das, was Round 2 angemahnt hat ("§-Anker einbauen") — Chat A hat geliefert, aber falsch.

BRIEFING_OK

SCORE: 64/100

FUNDE:

SCHWÄCHE 1 (kritisch, Halluzination + veraltete Daten): Falsche §-Verweise und veraltete Bestattungsfrist im Rechtsteil Die Page schreibt im Abschnitt "Rechtlicher Rahmen": "Art. 16 BestG (Bestattungsfristen, frühestens 48 Stunden, spätestens nach 96 Stunden nach Feststellung des Todes), Art. 19 BestG in Verbindung mit § 18 BestV (zweite Leichenschau)". Drei Fehler übereinander: (a) Die 96-Stunden-Frist gilt nicht mehr — seit 01.04.2021 sind es acht Tage (§ 19 Abs. 1 BestV). Die Page zitiert einen Rechtsstand, der seit fünf Jahren überholt ist. (b) Die Bestattungsfrist steht in § 19 BestV, nicht in Art. 16 BestG. Art. 16 BestG ist die Verordnungsermächtigung an das Ministerium. (c) Die zweite Leichenschau ist kein Inhalt von Art. 19 BestG — sie wurde 2021 in die BestV eingeführt und gilt seit 01.01.2023 (vgl. Reform 2021). Dieselbe Falsch-Information steht zusätzlich in den Key-Facts ("BestG Bayern (Art. 16, 19) + BestV (§ 18)"), in der FAQ-Antwort "Welches Recht gilt" und in der FAQ "Wo wird eingeäschert" → vier Wiederholungen einer falschen Norm-Zitierung. Auf einer YMYL-Stadtseite ist das ein Deploy-Blocker. Fix: Bestattungsfrist nach § 19 Abs. 1 BestV (acht Tage), zweite Leichenschau nach den 2021/2023 reformierten BestV-Vorschriften, Art. 16 BestG nur als Verordnungsermächtigung erwähnen. Quelle: GVBl. 2021 S. 138.

SCHWÄCHE 2 (Quellenanker fehlt weiterhin trotz Round-2-MUST-FIX): Friedhofssatzung Nürnberg & SUN-Gebührensatzung nicht direkt verlinkt Round 2 hat exakt das als MUST-FIX angemahnt: "Friedhofssatzung Stadt Nürnberg und SUN-Gebührensatzung mit direkten URLs verlinken … nicht nur generisch nuernberg.de". Chat A verlinkt in v2 zwar friedhof.nuernberg.de und sun.nuernberg.de als Portal-Seiten — aber nicht die Satzungs-PDFs selbst. Die Friedhofs- und Bestattungssatzung wird viermal genannt (Rechtsteil, Kosten, FAQ Ruhezeit, FAQ Recht), jedes Mal ohne direkten Anker auf das Satzungsdokument. Gleiches gilt für die Gebührensatzung. Das ist exakt der Round-2-Befund, unverändert. Fix: Konkretes Satzungs-PDF (oder Unterseite der Stadtportals, die zur Satzung führt) als Deeplink statt Portal-Startseite.

SCHWÄCHE 3 (Generische Kostenkomponenten ohne Nürnberg-Anker): Bestattungskosten-Sektion ist deutschlandweite Boilerplate, nicht Nürnberg-spezifisch Die Kosten-Aufschlüsselung ("Bestatterleistungen 2.500–4.500 €, Friedhofsgebühren wenige hundert bis 3.000 €, Grabstein 1.500–4.000 €, Trauerfeier 500–1.500 €") enthält kein einziges Nürnberg-spezifisches Datum. Keine konkrete Gebührenposition aus der SUN-Satzung (z.B. "Wahlgrab Westfriedhof 30 Jahre: X €", "Urnenwand Südfriedhof: Y €"), kein Vergleich West/Süd vs. St. Johannis/Rochus (obwohl im Text behauptet wird, dass die historischen Friedhöfe "in der Regel höher liegen" — ohne Zahl), keine kommunale Bestattungspflicht-Kostenangabe für Sozialbestattungen. Die Sektion könnte 1:1 auf jeder bayerischen Stadtseite stehen. Das ist die "generischer Satz"-Kategorie aus dem Briefing: Lokal verankerte Aussage fehlt. Fix: Mindestens 2–3 konkrete Zahlen aus der aktuellen SUN-Gebührensatzung (mit Stichtag) oder explizit "konkrete Tarife siehe [Deeplink Gebührensatzung]" + ein realer Stadt-Anker (z.B. Anteil Urnenbestattungen Nürnberg, durchschnittliche Bestattungskosten laut Stadtarchiv-Statistik oder ähnliches).

Weitere bemerkenswerte Schwächen (nicht in den Top-3, aber zur Vollständigkeit):

Floskel "erfahrungsgemäß" zweimal beim Kostenkorridor — schwache Quelle, kein Beleg. Round 2 hatte "Stiftung Warentest-Zuschreibung oder streichen" gefordert. Chat A hat die Zuschreibung gestrichen, aber durch "erfahrungsgemäß" ersetzt = ungenannter Erfahrungswert = im Briefing-Sinne Floskel.
Anselm-Feuerbach-Kontext (laut Round 2 MUST-FIX) ist eingebaut ✓ — gut.
Cross-Links zu bayerischen Städten ergänzt ✓ — gut.
Geo-Koordinaten im Schema.org ergänzt ✓ — gut.
Hans Sachs / Veit Stoß als "vermutet" kennzeichnet ✓ — gut.
UNSURE-Kommentare in HTML sind im Code sichtbar (5 Stück) — das ist Pipeline-intern okay, sollten aber vor Deploy raus (<!-- UNSURE: ... -->). Wenn das HTML 1:1 deployed wird, stehen die Hinweise im Quelltext öffentlich.
Wortzahl jetzt ~2.200 ✓ (Round-2-Vorgabe erfüllt).
Tradition-Sektion ✓ eingebaut.
Muslimisch/jüdisch-Sektion ✓ eingebaut, aber ohne konkrete Adressen (Islamische Gemeinde Nürnberg: welche? Es gibt mehrere. IKG Nürnberg: Adresse?). Round 2 hatte "konkrete Adressen" explizit gefordert — teilerfüllt.

MUST-FIX vor Deploy: ja.

Schwäche 1 (falsche/veraltete §-Zitate) ist allein schon Deploy-Blocker für eine YMYL-Seite. Bestattungsfrist seit 2021 acht Tage, nicht 96 Stunden — diese Information wird Nutzer in der akuten Trauerphase aktiv falsch informieren ("ich habe nur 4 Tage"). Das ist genau das Risiko, das die Re-Check-Pipeline verhindern soll. Schwäche 2 und 3 sind nicht so kritisch, aber Schwäche 2 ist ein wiederholter Round-2-MUST-FIX, der nicht erledigt wurde — das ist ein Pipeline-Trust-Problem.

EHRLICHE %-ZAHL: 64%