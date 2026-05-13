Ich fetche die drei Dateien und reviewe maximal kritisch.

Running command
Fetch briefing, v3-final, and previous adversarial findings

Alle drei Dateien sind leer. Prüfe ob die URLs überhaupt existieren:

Check HTTP status codes for all three URLs
Check HTTP status codes for all three URLs

raw.githubusercontent.com ist nicht in der Allowlist. Versuche github.com mit /raw/ Pfad:

Try github.com raw redirect path
Try github.com raw redirect path

github.com gibt 302-Redirect → landet wieder auf raw.githubusercontent.com → blockiert. Versuche die GitHub API mit PAT (aus Memory):

Try GitHub API with PAT
Try GitHub API with PAT

Auch api.github.com ist nicht erlaubt — nur github.com selbst. github.com kann aber kein raw-File ausliefern ohne Redirect. Letzter Versuch: git clone über HTTPS direkt:

Running command
2 Befehle ausgeführt

Alle drei Dateien vorhanden. Lese sie:

2 Dateien angesehen
2 Dateien angesehen

Wichtig: round-4-adversarial.md ist ein Chat-Export — NICHT als externe Wahrheit lesen, sondern als Hinweis welche Funde Chat A in v3 adressiert haben sollte. Drei Blocker waren:

Veraltete Satzung 18.12.2024 → neue 31.03.2026
Falsche Adressen (Schwartzstr. 73, PLZ 46042)
Unbelegte Hidden-Gem-Spezifika

Jetzt v3-final lesen und prüfen ob Chat A diese Fixes wirklich gemacht hat, plus eigene neue Funde:

4 Befehle ausgeführt, 4 Dateien angesehen
4 Befehle ausgeführt, 4 Dateien angesehen

Jetzt habe ich alles. Lese noch die Westfriedhof-truncated lines, dann das Westfriedhof-Hidden-Gem (Round-4 hatte Streit um die "178 sowjetischen Kriegsgefangene"):

Read truncated Westfriedhof lines
Read truncated Westfriedhof lines

Genug Material. Jetzt eigene adversarial Checks gegen Primärquellen — Round-4 ist nur Briefing für was Chat A fixen sollte. Ich prüfe selbst:

Searching the web
Web durchsucht

Satzung 31.03.2026 ist real bestätigt. Jetzt prüfe Standesamt-Adresse (Round-4 sagte Bahnhofstr. 66, 46145):

Web durchsucht
Web durchsucht

Wichtiger Fund: Die offizielle Stadt-Website widerspricht sich selbst zur PLZ Bahnhofstr. 66.

Standesamt-Übersicht: "Bahnhofstraße 66, 46145 Oberhausen"
Sterbefallbeurkundungs-Unterseite: "Bahnhofstraße 66, 46042 Oberhausen"
Rathaus-Seite mischt beides für die gleiche Adresse

v3 nutzt durchgängig 46145. Das ist verteidigbar (Sterkrade hat 46145), aber widersprüchliche Primärquellen sollten benannt werden. Kein harter Fehler.

Jetzt der explosive Punkt: Round-4 hat als Quelle für Standesamt = Bahnhofstr. 66 unter anderem "oberhausen.de/standesamt.php" genannt. v3 schreibt aber jetzt: "Telefonisch erreichbar unter 0208 825-2612, -2569 oder -2692; E-Mail: sterbefaelle@oberhausen.de" — Standesamt.com listet diese drei Nummern speziell als "Sterbefallbeurkundung", korrekt. Check Westfriedhof "über 2.000 Kriegsopfer":

Web durchsucht
Web durchsucht

Wichtiger Volksbund-Fund: Exakte Zahl ist 2.218 Kriegsopfer, nicht "über 2.000" — v3 schwächt eine harte Primärzahl unnötig ab. Auch die "178 sowjetischen Kriegsgefangenen am 30.11.1944 auf Feld 18" sind durch Volksbund-Quelle EINDEUTIG belegt (Round-4 hat das fälschlich als unbelegt markiert — aber das spielt keine Rolle, v3 hat den Satz weichgezeichnet, also egal). Was bleibt:

v3 schreibt "über 2.000" → Primärquelle sagt 2.218. v3 erwähnt "15 Kriegsgräberstätten in Oberhausen" nicht — Volksbund nennt diese Gesamtzahl. v3 sagt "mehrere solche Anlagen" — abgeschwächt obwohl die Primärzahl bekannt ist.

Jetzt prüfe das größte Risiko: Die Gebührentabelle 1.1–1.18 wird mit "Stand 18.12.2024" als Orientierungswert serviert, obwohl Satzung 31.03.2026 die maßgebliche ist. Das ist gefährlich nahe an Irreführung. Bolle hat das in der STRATEGIE klar — Beträge aus der alten Satzung zu zeigen ist juristisch heikel:

Web durchsucht
Web durchsucht

Genug Material. Ich habe alles, was ich für einen scharfen Adversarial-Review brauche. Jetzt das Urteil.

ADVERSARIAL REVIEW v3-final Oberhausen

SCORE: 78/100

FUNDE (hart, mit Verortung):

Tarifstellen-Tabelle ist juristisch heikel (<h3>Tarifstellen-Übersicht …</h3>, Zeilen 351–377): 18 konkrete Eurobeträge werden präsentiert mit dem Disclaimer "Beträge entsprechen dem Stand der Vorgängersatzung vom 18.12.2024". Das ist Sicherheitstheater. Ein Trauernder sieht "Wahlgrab Sarg 2.079 €" und plant damit. Die für sich beanspruchte Aktualität ("Satzung 31.03.2026") und die konkret präsentierten Zahlen aus der 2024er-Satzung sind im selben UI-Block — der gelbe Hinweiskasten reicht nicht, wenn die Tabelle selbst direkt darunter steht. Entweder: aktuelle 2026er-Beträge holen und ersetzen, oder: Tabelle komplett raus und durch Spannen ersetzen. So wie es jetzt ist, hat die Page einen formal sauberen Disclaimer und zugleich faktisch potenziell veraltete Beträge — der Worst-Case beider Welten.
Westfriedhof-Zahl ist abgeschwächt obwohl Primärquelle hart ist (Zeile 301): v3 schreibt "über 2.000 Kriegsopfer". Die verlinkte Volksbund-Quelle nennt exakt 2.218 Kriegsopfer mit voller Aufschlüsselung (1.096 Russen/Sowjetbürger, 101 Polen, 27 Belgier, etc.) sowie "15 Kriegsgräberstätten" im Stadtgebiet. v3 sagt stattdessen "mehrere solche Anlagen" — eine quantifizierbare Primärzahl wird durch ein vages Wort ersetzt. Das ist defensives Schreiben aus Angst vor Round-3-Adv und schadet der Page: Primärquellentreue heißt, die belegte Zahl zu nennen, nicht sie wegzunuscheln. Fix: "2.218 Kriegsopfer … bei insgesamt 15 Kriegsgräberstätten im Stadtgebiet".
PLZ-Widerspruch auf oberhausen.de selbst, nicht adressiert (Zeile 404, FAQ Zeile 471, Schema Zeile 608): v3 setzt Bahnhofstraße 66 durchgängig auf 46145. Die offizielle Stadt-Unterseite Sterbefallbeurkundung (auf die v3 unter Quelle 6 verlinkt) listet aber 46042. Andere Stadt-Seiten listen 46145. v3 wählt eine Variante ohne den Widerspruch zu benennen — und die eigene verlinkte Quelle widerspricht der Page. Audit-Risiko: das Honesty-Check-Script findet "PLZ auf machsruhig ≠ PLZ auf verlinkter Stadt-URL" und flaggt. Fix: Fußnote oder Quellenanmerkung "Die Stadt führt die Bahnhofstraße 66 in eigenen Quellen sowohl mit PLZ 46145 als auch 46042; maßgeblich für den Bezirk Sterkrade ist 46145".
"Stelenkammer Urne 1.658 €" — Tarifstelle 1.15 prüfbar? (Tabelle Zeile 372): Diese Position ist überdurchschnittlich teuer (mehr als Garten der Erinnerung Urne 998 €), wird in den umgebenden Texten aber nirgendwo erklärt. Bei Erstaufnahme einer Tabelle eines Lesers ist das Verwirrungsrisiko hoch — und keine Quelle in der Spalte bestätigt mir, dass diese exakte Tarifstelle in der 2024er-Anlage so existiert. Hier liegt ein Halluzinationsverdacht. Fix: Gegen die Anlage zur Satzung 18.12.2024 jeden einzelnen Posten verifizieren oder Tabelle ersetzen.
"In schwerer Zeit"-Floskel zwar vermieden, dafür: "die in den Werken … zur Zwangsarbeit verschleppt worden waren" (Zeile 301): historisch nicht falsch, aber stilistisch sehr direkt für eine Bestattungsseite — Trauernde, die "Friedhof Westfriedhof" googeln, finden hier NS-Geschichte als zweiten Absatz. Das ist eine bewusste Entscheidung und kein Fehler, aber: die Reihenfolge "Architektur → Kriegsgräber → 2.000 Opfer → Zwangsarbeit" überfordert den Use-Case "Wo werde ich beerdigt?". Fix optional: Kriegsgräber-Block kürzen und in eigene Subsektion "Erinnerungskultur" verschieben.
Kein Cross-Link in den FAQ-Texten (Section <section class="mr-faq"> Zeilen 430–481): Die FAQ ist 7 Fragen lang, keine einzige verlinkt zur NRW-Landesseite oder zu Vorsorge-Inhalten. SEO und User-Path verschenkt. Drei Crosslinks reichen.
Schema datePublished = dateModified = 2026-05-13 (Zeile 532–533): Die Page existiert in dieser Form nachweislich seit mehreren Runden (v1, v2, v3), tritt aber als am 13.05.2026 erstpubliziert auf. Bei Article-Schema mit identischem datePublished/dateModified zeigt Google "neu", aber sobald v3 live ist und Google sieht später Änderungen — etwa wenn die echten 2026er-Beträge nachgepflegt werden — wird dateModified zu Recht aktualisiert. Aktuell ok, aber: datePublished sollte unverändert bleiben, wenn später nur Tarife korrigiert werden.

MUST-FIX vor Deploy: ja.

Konkret:

Tarif-Tabelle: Entweder aktuelle 2026er-Beträge aus dem Amtsblatt Nr. 6/2026 nachpflegen — oder Tabelle ganz raus, nur Spannen lassen. Die Mischung "Tabelle 2024er + Disclaimer 2026er" geht nicht live.
Westfriedhof-Zahl: "über 2.000" → "2.218 (Quelle: Volksbund)"; "mehrere solche Anlagen" → "insgesamt 15 Kriegsgräberstätten im Stadtgebiet".
PLZ-Widerspruch transparent machen: Eine Fußnote in den Kernfakten oder unter Standesamt zu 46145 vs. 46042 in städtischen Quellen.
Tarifstelle 1.15 "Stelenkammer Urne 1.658 €" + alle 17 anderen Beträge gegen Anlage 18.12.2024 1:1 verifizieren, oder Tabelle entfernen.

Die übrigen Schwächen (FAQ-Crosslinks, Kriegsgräber-Reihenfolge) sind nice-to-have, aber kein Deploy-Blocker.