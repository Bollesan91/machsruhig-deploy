Reviewer-Output Bremen v1
Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Web durchsucht

BRIEFING_OK

SCORE: 74/100

FUNDE (Quellenanker / Faktenfehler / Struktur-Lücken / Marketing):

Quellenanker / §-Präzision:

§ 4 Abs. 1a Bremer Friedhofs- und Bestattungsgesetz wird zweimal zitiert (Fließtext + FAQ), aber NIE direkt zur Gesetzes-URL verlinkt. Der Quellenblock führt das Gesetz auf, aber im Fließtext fehlt der inline-Anker direkt am §-Zitat. Das ist der wichtigste Paragraph der ganzen Seite.
Die Novelle 2015 wird im Hero-Lead und im Fließtext als Stichdatum für die Asche-Ausnahme genannt, aber ohne Drucksache, Gesetzblatt-Fundstelle oder Beleg. Bei einem so zentralen Bremer Alleinstellungsmerkmal muss eine konkrete Fundstelle stehen.
Die "Aschestreuwiesen Osterholz und Blumenthal" sind eine sehr konkrete Behauptung ohne verlinkte UBB-Quelle direkt am Satz.
Bestattungsfrist und Sargpflicht-Paragraphen werden komplett auf die Bundeslandseite weggeschoben ("dort dokumentiert"). Eine Stadt-Seite, die das Standes-Wording "Stadt-Leitfaden" trägt, muss mindestens die einschlägigen §§ namentlich nennen, nicht nur verlinken.
§ 28 PStG ist korrekt verlinkt — einer der wenigen sauber gesetzten §-Anker. Maßstab für den Rest.

Faktenfehler / Belege wackelig:

"Osterholzer Friedhof, dem mit 79,5 Hektar größten Friedhof Norddeutschlands" im Lead — der Ohlsdorfer Friedhof Hamburg (~389 ha) ist deutlich größer und liegt nachweislich in Norddeutschland. Das ist sachlich falsch und auf einer Bremen-Seite, die Hamburg-Cross-Links zu Nachbar-Bundesländern hat, ein vermeidbarer Patzer. In der Sektion selbst korrekter formuliert ("einer der größten Norddeutschlands") — der Lead-Satz widerspricht der späteren Aussage.
"Heinrich Wilhelm Matthias Olbers" steht doppelt: einmal in Riensberg (Feld C Grab 7), einmal in Osterholz. Eines der beiden ist falsch — Olbers liegt nach Quellenlage auf Riensberg (Überführung), in Osterholz hat er nichts zu suchen, denn Olbers † 1840 und Osterholz eröffnet erst 1920. Das ist ein blamabler innerer Widerspruch.
"13 Friedhöfe — vom 1875 angelegten Riensberger" im Lead, aber Hastedt seit 1796 belegt — die "ältester durchgängiger Friedhof Bremens"-Aussage in der Hastedt-Sektion widerspricht der Lead-Framing-Logik. Lead-Satz präzisieren.
Krematorium Bremen "auf dem Friedhof Huckelriede" — im FAQ-Schema und in Sektion "Was zu tun ist". Die Keyfacts sagen "Krematorium: Huckelriede, ca. 5.000 Einäscherungen/Jahr". Faktisch wird Huckelriede vom UBB betrieben, aber an keiner Stelle wird Huckelriede als eigenständiger Friedhof in der Friedhofs-Sektion vorgestellt — er erscheint nur als "Hier wird verbrannt"-Standort. Das ist eine strukturelle Lücke, kein reiner Faktenfehler.
"1907 von Architekt Heinrich Wilhelm Behrens" für das Riensberg-Krematorium: zu prüfen — gängige Bremer Quellen nennen für das Krematorium Riensberg meist Hugo Wagner als Architekten, nicht Behrens. UNSURE-Kommentar fehlt.
"Carl F. W. Borgward (1890–1963)" — Geburtsjahr 1890 ist korrekt, aber Sterbejahr 1963 stimmt. "zeitweise größter Bremer Arbeitgeber" — ok, aber unbelegt.
"ewiges Ruherecht" für 6.192 Kriegstote — die Formulierung ist korrekt im Sinne der Kriegsgräberstätten-Regelung, aber ohne § oder Gräbergesetz-Verweis bleibt sie behauptet.

Struktur-Lücken:

Huckelriede fehlt als eigener Friedhof-Eintrag. Auf einer Bremen-Stadt-Seite, die das Krematorium dort 4-mal erwähnt, muss Huckelriede entweder eigener H3-Abschnitt oder mindestens explizit in der Friedhofs-Auswahl benannt werden. Aktuell: 4 Friedhöfe vorgestellt (Riensberg, Osterholz, Walle, Hastedt) — Huckelriede sollte der 5. sein, oder die Auswahl-Logik muss begründet werden.
Bremerhaven-Schnittstelle wird angerissen, dann fallengelassen. Lead und §-Sektion sagen "Stadtgemeinde Bremerhaven über den Magistrat" — danach kommt zu Bremerhaven kein Wort mehr. Entweder die Seite ist klar Stadtgemeinde Bremen only (dann Bremerhaven-Erwähnung streichen oder als Abgrenzung kennzeichnen), oder es braucht einen Cross-Link/Mini-Abschnitt zu Bremerhaven.
Keine Cross-Links zu weiteren Bremer Stadtteilen / Nachbar-Bundesländern. Andere fertige Bundesland-/Stadt-Seiten haben Cross-Links (z.B. Niedersachsen, Hamburg). Hier: null Cross-Link zu Nachbar-Städten oder anderen machsruhig-Stadtseiten.
Kostentabelle ist dünn. 5 Zeilen, davon eine "auf Anfrage". Keine Spalte für Ruhezeit, keine Nutzungsdauer-Spalte, keine Differenzierung Reihen-/Wahlgrab-Begründung. Im Vergleich zu vorhandenen Gold-Seiten zu wenig.
UNSURE-HTML-Kommentar ist im Live-HTML enthalten (<!-- UNSURE: Exakte UBB-Tarife... -->). Das gehört vor Go-Live raus oder in eine sichtbare Quellenfußnote. Im Quelltext beim Endnutzer findbar, wirkt unfertig.
OG-Image verweist auf generisches /assets/og-image.png — kein bremen-spezifisches OG-Image. Bekannter site-weiter Deploy-Blocker laut Audit, hier nicht gefixt.
Schema.org: Article-Datum "2026-05-12", aber im sichtbaren Text "Stand: 12. Mai 2026" — konsistent, ok. Aber: datePublished = dateModified deutet auf Erst-Veröffentlichung; das ist ok für v1, aber bei späteren v-Iterationen muss dateModified getrennt geführt werden.
Trust-Box am Ende ist ein Pflichtelement, vorhanden — ok. Aber "machsruhig Redaktion" als Autor ohne Fachpool-Reviewer-Nennung widerspricht dem festgelegten Autorenmodell ("machsruhig Redaktion + Fachpool-Reviewer").

Marketing / Floskel-Check:

"Hanseatische Tradition" im Title, Lead und H1 — wirkt als Marketing-Klammer, aber inhaltlich wird "hanseatisch" nur 4× als Adjektiv eingestreut ("hanseatisch-bürgerliche Tradition", "hanseatisch-russisch", "hanseatisch-jüdisch", "hanseatischer Bürgergräber"). Konkrete hanseatische Bestattungstradition (z.B. Bremer Senatsbeschlüsse zu Friedhofsverlegung 1875, Schnoor-Rolle, hanseatische Familienpatronate) wird angedeutet, nicht ausgeführt. Entweder ausführen oder aus dem Titel/Lead nehmen.
"Eine Bremer Besonderheit" — ok, aber "bundesweit selten" wird 2× verwendet ohne Aufzählung der wenigen anderen Bundesländer (NRW, Berlin-Friedhof außerhalb). Konkretisieren oder weglassen.
"norddeutsche Begräbnisspur amerikanischer Showgeschichte" (Buffalo-Bill-Sioux) — ist eine schöne Hidden-Gem-Anekdote, aber die Story ohne Belege/Wikipedia-Anker bleibt anekdotisch. Wenn drin, dann mit Quelle.
Keine der verbotenen Phrasen aus dem Briefing ("solide", "weitgehend" etc.) gefunden. Sauber.
Lead-Lesezeit "ca. 10 Minuten" — Wortzahl Fließtext ~2100 Wörter, das passt zur Audit-Korridor 2000–2500. Ok.

Sonstiges:

Header-Nav: Link "Bestatter finden" zeigt auf /bestatter/muenchen/ — auf einer Bremen-Seite. Footer ebenfalls. Vermutlich global so, aber auf Bremen-Seite irritierend. Sollte auf /bestatter/ zeigen.
Footer Copyright "2024–2026" — ok.

MUST-FIX vor v2:

Olbers-Doppelung auflösen: Olbers gehört auf Riensberg (Verifizierung an UBB-Quelle), Streichen aus Osterholz-Persönlichkeiten. Innerer Widerspruch ist disqualifizierend.
"Größter Friedhof Norddeutschlands" im Lead korrigieren → "einer der größten Norddeutschlands" oder "der zweitgrößte". Ohlsdorf bleibt unangefochten Nr. 1.
§ 4 Abs. 1a Bremer Bestattungsgesetz inline verlinken direkt am Zitat — nicht nur im Quellenblock. Plus Drucksachen-/Novelle-Beleg 2015.
UNSURE-HTML-Kommentar entfernen oder in sichtbare Quellenfußnote umwandeln.
Huckelriede als 5. Friedhof-Eintrag ergänzen (H3 mit Krematorium-Geschichte, Gräberfeldern, Eröffnung) — oder die Auswahl der 4 Friedhöfe in einem Satz begründen ("Wir stellen exemplarisch die vier prägendsten vor; alle 13 städtischen Friedhöfe siehe UBB-Übersicht").
Bremerhaven-Erwähnung im §-Block entweder mit Cross-Link zu separater Seite oder als klare Abgrenzung markieren ("Diese Stadtseite behandelt ausschließlich die Stadtgemeinde Bremen; für Bremerhaven siehe X").
Architekt Riensberg-Krematorium prüfen: Behrens vs. Wagner — Quelle nennen oder als UNSURE im Backend kennzeichnen, nicht im Live-HTML.
Hidden-Gem Buffalo-Bill-Sioux mit Quelle belegen (Spurensuche Bremen oder Weser-Kurier) oder weglassen.
Cross-Links setzen: Mindestens 1× Niedersachsen, 1× Hamburg, 1× Bremerhaven (falls separate Seite), 1× Bundeslandseite Bremen prominent.
Kostentabelle erweitern: Spalte "Nutzungsdauer/Ruhezeit" ergänzen, Kolumbarium konkretisieren oder weglassen.
OG-Image Bremen-spezifisch ersetzen (oder Site-weiter Deploy-Blocker hier dokumentieren, dass es im Sweep gefixt wird).
Nav-Link "Bestatter finden" auf /bestatter/ statt /bestatter/muenchen/ korrigieren.
Autor-Block: "machsruhig Redaktion · Fachlich geprüft: [Name Fachpool-Reviewer]" gemäß festgelegtem Autorenmodell ergänzen — oder bewusst auf v2-Phase verschieben mit Notiz im Loop-Log.