Claude hat geantwortet: Beide Dokumente gelesen.
Mobilisierte Quellen für adversariale Audit-Prüfung der Sozialbestattungsseite
Verifizierte Rechtsquellen gegen Primärtexte, identifizierte Vermögensschonbetrag-Falle

Beide Dokumente gelesen. Jetzt verifiziere ich die heiklen §-Verweise gegen Primärquellen, bevor ich urteile — Schwerpunkt auf den neu eingefügten Stellen (§ 199 BGB, § 98 Abs. 3, § 90 Abs. 2 Nr. 9, BSG-Az.).

https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/sozialbestattung/v2-from-chat-A.html

raw.githubusercontent.com

https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/_dev/content-loop/runs/sozialbestattung/quellen-pack.md

raw.githubusercontent.com

Fetching site
Verifizierend die korrekte Rechtsquelle für Barbetragspauschale

§ 74 SGB XII-Wortlaut und das BSG-Az. (B 8 SO 20/10 R) bestätigt. Jetzt prüfe ich den heikelsten neuen Wert: 10.000 € Vermögensfreibetrag + die §-90-Zuordnung.

Lokalisierend kritische Regelwerk-Passagen zur Zuständigkeit
Lokalisierend kritische Regelwerk-Passagen zur Zuständigkeit

10.000 €-Wert bestätigt — aber die §-Zuordnung ist die kritische Stelle. Letzte Verifikation: § 98 Abs. 3 SGB XII (örtliche Zuständigkeit für § 74) und § 199 BGB-Beginn.

Verifizierend JSON-LD und HTML-FAQ auf Konsistenz prüfen
Systematisch drei Perspektiven auf Sozialbestattungs-Seite auditiert

Beide Quellen gelesen, alle heiklen §-Verweise gegen Primär-/Kommentarquellen verifiziert. Hier der feindliche Last-Look.

Verifikations-Ergebnis vorab (Anti-Sycophancy, gegen Primärquellen geprüft)
Verweis auf der Page	Status
§ 74 SGB XII Wortlaut	✅ wörtlich korrekt
BSG 25.08.2011, B 8 SO 20/10 R (zweistufige Prüfung, ortsüblich)	✅ Az. + Inhalt real
§ 1968 BGB Erbenhaftung	✅ korrekt
§ 195 / § 199 Abs. 1 BGB (3 Jahre, Beginn Jahresende)	✅ korrekt formuliert
§ 632 BGB ortsübliche Vergütung	✅ korrekt
§ 98 Abs. 3 SGB XII (letzter Träger → sonst Sterbeort)	✅ korrekt
10.000 € Freibetrag seit 01.01.2023	⚠️ Zahl richtig, §-Zuordnung falsch
8.700–10.500 € Bestattungsvorsorge / VG Münster	✅ plausibel, als „Größenordnung" gehedged

Der eine echte juristische Fehler: Die Page schreibt „ein allgemeiner Vermögensfreibetrag von 10.000 € (§ 90 Abs. 2 Nr. 9 SGB XII)". Die 10.000 € stehen nicht im Gesetz, sondern in der Durchführungsverordnung (Barbetragsverordnung) zu § 90 Abs. 2 Nr. 9 SGB XII, geändert durch Art. 9 Bürgergeld-Gesetz. § 90 Abs. 2 Nr. 9 selbst nennt nur „kleinere Barbeträge". Für eine Seite, die mit Primärquellen-Verifikation wirbt, ist das die klassische Stelle, an der ein Jurist sofort hakelt. Korrekt wäre: „§ 90 Abs. 2 Nr. 9 SGB XII i.V.m. der Durchführungsverordnung".

Perspektive A — Hinterbliebener, knappe Mittel, emotional belastet

A1 — „Habe ich Anspruch?" wird strukturell, aber nicht schnell beantwortet. Die Stufenlogik Erben → Bestattungspflichtige → Amt ist sauber, aber ein Trauernder will ein schnelles „wahrscheinlich ja". Es gibt keinen 3-Zeilen-Selbstcheck („Beziehst du selbst Grundsicherung? → dann sehr wahrscheinlich"). Die Keyfacts mildern das, ersetzen ihn aber nicht.

A2 — Emotionaler Ton ist gut, kein Abschieben. Der Lead („muss niemand die Beisetzung aus eigener Not vorfinanzieren") und der Hint „Kein Zeitdruck nötig … Niemand muss aus Angst vor Kosten eine übereilte Entscheidung treffen" nehmen ernst. Das ist die Stärke der Seite. Kein Finding gegen den Ton.

A3 — Versteckte Hürde wird beschönigt: Erbausschlagung. Die Page empfiehlt mehrfach beiläufig die Ausschlagung („ist … in der Regel der sinnvolle … Weg"), nennt aber nirgends die 6-Wochen-Frist (§ 1944 BGB) und nicht, dass sie irreversibel ist und den Zugriff auf Nachlassgegenstände kostet. Für jemanden in Schock ist das eine reale Falle, die als „unproblematisch" verkauft wird.

Perspektive B — Skeptiker (Lead-Funnel-Verdacht)

B1 — Kein Sozialamt-Lead-Verkauf erkennbar, gut. Trust-Block, „keine Rechtsberatung", neutrale Quellenliste, nofollow-Links auf Aeternitas/Verbraucherzentrale. Ein Skeptiker entspannt sich hier. Positiv.

B2 — Angebotspruefer ist 3× platziert — grenzwertig. Der /tools/angebotspruefer/ taucht im Hint, im großen CTA-Block und im Related-Grid auf. Bei einer Seite für Menschen ohne Geld wirkt ein dreifach wiederholter Tool-CTA leicht penetrant. CTA-Wording selbst ist neutral („hilfreich, bevor du Belege beim Amt einreichst") — aber die Frequenz ist das Funnel-Signal, nicht das Wording. Auf 1× CTA + 1× Related reduzieren.

B3 — „Bestatter in München/Köln" ist Kontext-fremd. Nav + Related + Footer pushen Bestatter-Vermittlung für zwei willkürliche Städte. Ein Sozialbestattungs-Sucher shoppt keine Premium-Vermittlung. Riecht nach generischem Template-Crosslink, nicht nach Bedarf. Schwaches, aber berechtigtes Funnel-Finding.

Perspektive C — Fachkundiger (Sozialarbeiter / Jurist)

C1 — §-90-Zuordnung (siehe oben). Würde er einem Klienten korrigieren. MUST-FIX.

C2 — Verpflichteten-Reihenfolge verkürzt. Die Page kennt nur „Erben → Bestattungspflichtige → Amt". Die amtliche Reihenfolge (vgl. Berlin/Tacheles-DA) hat zwei weitere Stufen: zivilrechtlich/vertraglich Verpflichtete (z. B. Sterbegeldversicherung) und Unterhaltsverpflichtete vor den öffentlich-rechtlich Bestattungspflichtigen. Für Laien tolerabel, aber ein Sozialarbeiter merkt: wer eine Sterbegeldversicherung hat, fällt anders aus dem Raster.

C3 — Interner Widerspruch: Erbausschlagung-Mythos vs. BSG-Witwe. Die Page sagt im Mythen-Block, man müsse die Erbschaft nicht annehmen — gleichzeitig im Hint, eine Witwe bekam Hilfe obwohl der Sohn Erbe war. Genau das ist die BSG-Entscheidung vom 12.12.2023, B 8 SO 20/22 R: ein nach Landesrecht vorrangig bestattungspflichtiger Ehegatte verliert den § 74-Anspruch nicht durch die Erbenstellung eines Dritten. Heißt: eine bestattungspflichtige Witwe muss gerade nicht ausschlagen. Die Mythen-Aussage „Erbausschlagung in der Regel sinnvoll" kann genau diese Person zu einer unnötigen, fristgebundenen Ausschlagung verleiten. Inhaltlich die schwerste Stelle — und die Page lässt das echte BSG-Az. ungenutzt, attribuiert nur „Aeternitas-Berichte".

5 Killer-Fragen, die die Page NICHT beantwortet
„Ich habe schon eine Bestatter-Rechnung bezahlt — kriege ich das Geld jetzt noch zurück?" Die Page sagt „nachträglich möglich", aber nicht, dass der maßgebliche Zeitpunkt die Fälligkeit der Rechnung ist (BSG 04.04.2019, B 8 SO 10/18 R) und ob vorab beglichene Rechnungen anders behandelt werden.
„Mein Vater bekam Bürgergeld, nicht Sozialhilfe — welches Amt, welcher Ort?" Die Page nennt nur „Sozialhilfe → letzter Träger". Bei SGB-II-Beziehern greift § 98 Abs. 3 Alt. 1 nicht — dann zählt der Sterbeort (BSG 12.12.2023). Das fehlt.
„Bis wann muss ich die Erbschaft ausschlagen?" 6-Wochen-Frist wird nie genannt, obwohl die Ausschlagung empfohlen wird.
„Das Amt hat abgelehnt — was jetzt?" Widerspruch wird einmal im FAQ gestreift, aber es gibt keinen Pfad (Frist, Form, Beratungsstellen).
„Was, wenn eine Sterbegeld-/Lebensversicherung existiert?" Wird komplett ausgespart, obwohl es die Anspruchslage kippt.
Zwangscheck-Quittung (1–10)
„Antrag-vor-Bestattung"-Mythos reproduziert? Nein — aktiv 3× widerlegt. ✅
€-Pauschale als fix? Nein — 1.500–3.500 € stark gehedged („keine Zusage, grober Erfahrungsrahmen"). ✅
Zumutbarkeit am Bestattungspflichtigen? Ja, mehrfach klar. ✅
Sozial- vs. Ordnungsamtsbestattung getrennt? Ja, eigene Sektion + Tabelle. ✅
Schonvermögen korrekt geschützt? Ja (zweckgebunden, nicht auflösen). ✅
Konjunktivische Anspruchsfolgen? Ja („kann übernehmen", „kommt in Betracht"). ✅
Crosslink-Hygiene? Grenzwertig — Angebotspruefer 3×. ⚠️
§ 199 BGB neu, korrekt? Ja, sauber. ✅
Bürgergeld „starkes Indiz"? Sauber, nicht überkonstruiert. ✅
JSON-LD-FAQ vs. HTML-FAQ? Identisch — 10 Q, Wortlaut + Antworten deckungsgleich, kein Rich-Result-Risiko. ✅
Verdict

Würde Fachkundiger A die Page weiterleiten? → MIT-CAVEAT, ~80 %.

Begründung: Auf allen 10 Zwangschecks inhaltlich sauber, Ton trägt, keine echten Falschaussagen außer der §-90-Zuordnung. Das ist deutlich besser als der Durchschnitt solcher Ratgeber. Aber: ein Jurist leitet sie nur mit dem Zusatz weiter „beim Vermögensfreibetrag steht der falsche Paragraf, und glaub dem Erbausschlagungs-Tipp nicht blind". Genau diese zwei Caveats verhindern PASS.

Letzte Show-Stopper vor Deploy
§ 90-Zuordnung fixen (billiger 5-Wort-Fix) — sonst bröckelt das „primärquellen-verifiziert"-Versprechen genau dort, wo es zählt. Echter Blocker.
Erbausschlagungs-Bullet entschärfen — „in der Regel sinnvoll" → „kann sinnvoll sein, ist aber fristgebunden (6 Wochen) und nicht in jedem Fall nötig", plus den BSG-Witwen-Fall als Gegenbeispiel verlinken. Soft-Blocker (rechtlich + Schutz vor Fehlhandlung des Nutzers).
Kein Blocker, aber empfohlen: Bürgergeld-Sonderfall bei der Zuständigkeit (Sterbeort) ergänzen — sonst falsche Amts-Adressierung.
Methodische Eigen-Kritik (was aus Raw-HTML NICHT prüfbar war)
OG-Image (/og/sozialbestattung.png) und Font-Preloads: Existenz/200-Status nicht verifizierbar.
Analytics-Tag: Die Seite lädt Plausible — Memory-Stand für die Schwester-Domain ist Umami. Ob das hier bewusst Plausible ist oder ein veraltetes Snippet, ist von außen nicht entscheidbar. Kurz gegen den Domain-Standard prüfen.
VG-Münster-Urteil (10.500 €): Nur über Aeternitas-Sekundärberichterstattung belegt; ein echtes Az. konnte ich nicht gegenprüfen — die Page hedged korrekt mit „etwa/Größenordnung", also tolerabel, aber es ist die schwächste Beleg-Stelle.
Crosslink-Ziele (/tools/angebotspruefer/, BL-Pages, Stadt-Pages): nicht auf 200/Existenz getestet — tote Links würden den Funnel-Eindruck verschärfen.
Rendering/CLS/Mobile: statische HTML-Analyse sieht kein Layout — Lesbarkeit der Tabellen auf 360px nicht beurteilt.
Kein Anchoring-Check gegen Chat A/B: bewusst nicht gelesen; falls die §-90-Stelle dort schon „gefixt" gemeldet wurde, wäre das ein Reviewer-Halluzinations-Treffer — aber das kann ich von hier aus nicht gegenprüfen.