# OFFENE-REVIEW-PUNKTE — geklärte False-Positives & bewusste Entscheidungen

> Reviewer-Pflicht: Diese Punkte NICHT erneut als Finding melden (sie sind geprüft). Writer-Pflicht: verworfene Findings hier nachtragen (Datum, Beleg).

## Geprüfte False-Positives

- **berlin.de-PM-Link (pressemitteilung.1292194.php) ist NICHT tot** — HTTP 200, selbst gecurlt 11.06.2026. (Wir verlinken trotzdem die eigene BL-Seite, weil die PM die Reform-Etappe nicht paragraphenscharf belegt — das war der berechtigte Kern.)
- **Senats-Broschüre-PDF (broschuere_fhinberlin.pdf), gesetze.berlin.de, Daten-und-Fakten-Seite**: alle 200 (11.06.2026).
- **CHECK24-Nennung in Korridor-Quellzeilen** (München/Berlin) ist Quellenangabe einer Auswertung, KEIN Affiliate-Link — zulässig. (Affiliate-Links auf check24.de/sterbegeldversicherung sind dagegen aus allen Sozial-Kontexten entfernt.)
- **Footer „Landesgesetze aller 16 BL (Stand Mai 2026)"** ist der Prüfstand der Gesetzes-Datenbasis, nicht das Seiten-Stand-Datum — kein Konsistenz-Finding gegen „Stand: Juni". (18.06. NOCHMAL bestätigt: site-weit auf „Juni" bumpen erzeugt L12-FAILs, weil der Linter Pro-Seite-Uniformität erzwingt; der Mai/Juni-Split QUER über Seiten ist beabsichtigt = je Seite ihr eigenes Pruefdatum. Vor jedem Footer-/Stand-Bump erst diese Zeile + Linter lesen.)
- **Leipzig/Stuttgart: Byline „Stand: 9. Juni 2026" vs. Gebühren-Box „Stand Mai 2026"** ist KEIN Widerspruch — die Byline ist das Seiten-Pruefdatum, die Box-Angabe ist scoped auf die Geltung der jeweiligen kommunalen Gebührensatzung (real Mai-Stand). Nicht „vereinheitlichen" — ein Bump auf Juni würde eine Gebühren-Re-Verifikation behaupten, die nicht stattfand. (18.06.)
- **Berlin 222 Friedhöfe / 182 geöffnet / 85 landeseigene**: quellenkonform mit der Senats-Seite (Reviewer-bestätigt 11.06.).
- **Kostenrechner „Basis 3.700–9.300 unter Default-Summe"**: Scheinwiderspruch — die Einordnung rechnet lokale Posten vor dem Vergleich auf Faktor 1 zurück (NRW-Default ergibt exakt 3.700–9.300); dokumentiert in /methodik#kostenmodell.
- **„Hört zu…" im claude.ai-Editor** ist der Diktiermodus (durch Ctrl+V ausgelöst), kein Seitenfehler — Paste via execCommand('insertText'), nicht Ctrl+V.

## Bewusste Entscheidungen (kein Defekt)

- **Umami-Doppel-Regime (Banner auf ~7 Tool-Seiten vs. Head-Load sonst)**: in Datenschutz §9 als Übergangszustand ehrlich deklariert; Vereinheitlichung ist eigener Arbeitsblock (ROADMAP-PBI). Bis dahin kein Finding.
- **Frankfurt-Kosten defensiv** (keine lokalen Beträge, Gebührenordnungs-Verweis + Modell-Einordnung): bewusste Strategie, solange Satzungswerte nicht primärverifiziert sind.
- **Seebestattungs-Block (Hamburg) vor dem Recht-Block**: bewusst (kostenrelevanter Stadt-USP).
- **/sozialbestattung ohne Trailing-Slash**: flache .html-Dateien der Site haben kein Slash-Muster; funktioniert via Netlify. Stil-Vereinheitlichung = Backlog, kein Defekt.
- **tracking.js-Header erwähnt „Plausible"**: window.plausible ist ein dokumentierter Shim auf Umami (Memory analytics_umami_not_plausible) — kosmetisches Backlog.

## Offen (echte Backlogs — nicht als „neu" melden, aber Status darf geprüft werden)

- Hamburg: jüdisches Sonderfeld auf Ohlsdorf, §-6-BestattG-Zitat (36 h), Altona „geschlossen 1877", Feuerbestattungs-Zeile in der Kostenbox.
- Köln: Intro „vier Friedhofs-Essays" bei zwei gelieferten; „Trauerhalle ca. 198 €" unbelegt; Ruhezeit/Nutzungsdauer-Vermischung; Memorial-50 %/Innungs-Pauschale ohne Quelle; doppeltes Nav-JS.
- Frankfurt: Hauptfriedhof-Doppelung in „Besonderheiten" + „Vorreiter"-Absatz vs. Novelle; Südfriedhof-Bestattetenzahl; Footer-München-Link; loser Textknoten nach der 6-Schritte-Sektion.
- Berlin: Träger-Aufschlüsselung/Ehrenmäler-Abgleich; Erd-Korridor-Untergrenze 1.100 vs. landeseigen 939 erklären.
- Site-weit: Consent-Vereinheitlichung; Fristen-Seite MITTEL 4–6 (§30-III-Testament-Satz, FAQ-Q6-Beweislast, Sicherungsmaßnahmen-Hinweis).

## Triage-FPs Korrektheits-Sweep (15.06.2026)
- **check24 auf /bestattungskosten-nach-bundesland** = Quellen-Citation (Friedhofsgebühren-Datenquelle `check24.de/sterbegeldversicherung/friedhofsgebuehren-deutschland`), KEIN Affiliate-CTA. Presse-Seite ohnehin nicht anfassen.
- **berlin „nicht in allen Bundesländern"** = korrekte Verneinung (kein Pauschale-Fehler).
- **/bestattung-in/ „bundesweit einheitlich sind nur Randbereiche"** = korrekt (kein Bundes-Bestattungsgesetz).
- **checkliste-todesfall „5.000–15.000 €"** = Auslandsüberführungs-Kosten, nicht Bestattung.
- **testament „2.000–5.000 €"** = Notarkosten nach Nachlasswert, nicht Bestattung.
- **beerdigungsplaner JS-Kostenarray** (Grabtyp-Schätzwerte) = tool-intern, plausibel; eigene Tool-Validity-Sache, nicht der Korrektheits-Sweep.

## Externes Review 16.06.2026 — geprüfte FPs
- **Testament „Ohne Testament entscheidet die Gesetze"** = bereits gefixt (Seite sagt „greift die gesetzliche Erbfolge"). Reviewer war auf altem Stand. NICHT erneut melden.
- **Patientenverfügung „schriftlich, handschriftlich unterschrieben"** = substanziell korrekt: § 1827 BGB verlangt Schriftform + eigenhändige Unterschrift; die Seite stellt an anderer Stelle ausdrücklich klar, dass der Text getippt sein darf und nur die Unterschrift handschriftlich erfolgen muss. Kein YMYL-Fehler, höchstens Keyfacts-Klarstellung (Backlog, kein Defekt).
- **ZTR-Gebühr**: Reviewer nannte 12,50/15,50 € — real **18 €** (primärverifiziert 16.06.). Bei künftigen Testament-Reviews die 75 € (Verwahrung) + 18 € (ZTR) als gesetzt behandeln.
- **„Stiftung Warentest 7.000–8.000 €" ist KEIN Fabrikat-Defekt** (15.06. primärverifiziert: real, hannover belegt mit Finanztest 11/2023). NICHT als Finding melden. Offen ist nur die Konsistenz (s. Backlog unten).

## Backlog: site-weite Kosten-Konsolidierung (Bolle-Entscheid nötig)
- **Problem:** Kosten-Spannen driften über die Seiten — „7.000–8.000 €" (Legacy ~16 BL + mainz/dresden/muenster/karlsruhe/bielefeld/bremen/hannover/leipzig/stuttgart/wuppertal/bonn/saarland), „6.000–8.000 € (Stand 2026)" (neuere Seiten), per-Art-Varianten („Erd typisch 4.500–9.500" vs. kanonisch 3.700–9.300). Quellen gemischt (SW unbelegt / SW Finanztest 11/2023 / SW+Aeternitas / SW+Verbraucherzentrale).
- **Entscheid offen (Bolle, redaktionell, YMYL):** Welche EINE Darstellung wird Standard? (a) eigenes Kostenmodell `/methodik#kostenmodell` als Single Source (LEKTIONEN #3) mit optionaler SW-Korroboration, oder (b) SW-Zahl als Headline mit working-Link, oder (c) beide klar getrennt. Exakte aktuelle SW-Zahl ist paywall-bedingt nicht voll primärverifizierbar → eigenes Modell ist die sicherere Single Source.
- **Ein-Klick-fertig vorbereitet:** sobald Variante gewählt, deterministisches Skript (`_dev/audit/`) über alle ~53 Fundstellen (Body + faq-answer + JSON-LD, Parität-erhaltend), Asserts vor Write, Linter + Diff-Re-Check.

## 02.07.2026 (Quick-Win-Review, Fable-5-Tab)
- **False Positive: "Deploy haengt / live noch alter Stand (Hagen zeigt Iserlohn)"** — Reviewer-Fetch war indirekt/cached (machsruhig.de nicht in seiner Container-Whitelist); eigener curl-Verify zeigte die Aenderungen live VOR seiner Antwort. Kein Deploy-Problem.
- **Bewusst nicht gefixt: lowercase-Percent-Umlaut-Redirects (%c3%b6 etc.) fehlen fuer moenchengladbach/baden-wuerttemberg/thueringen** (nur luebeck hat sie). Praktisch irrelevant (Clients normalisieren uppercase); bei Bedarf 6 Zeilen in _redirects.
- **Bewusst offen: Checkliste-Breadcrumb verlinkt sich selbst** (Mittel-Glied) — kosmetisch, Bestandsverhalten, kein 404.
- **Bewusst offen: Beerdigungsplaner sendet ggf. localStorage-Antworten aelterer Session mit** — durch neuen DS-Hinweis abgedeckt ("deine Plan-Antworten"); echte Loesung waere Session-Flag.
- **02.07. (Daten-Review): False Positive "Kasten fehlt auf hamburg/muenchen/chemnitz"** — Reviewer-Fetch-Cache (2. Vorfall); plain-URLs + Cf-Cache-Status DYNAMIC bewiesen live. Zahlen-Nachrechnung des Reviews dagegen wertvoll: 12/12 bestaetigt, 0 falsche Zahlen.
- **Bewusst offen: Koeln 25-vs-30-Jahre-Variante** (gleiche 1.945 EUR kaufen auf § 11-Friedhoefen 30 J.) — Kasten nennt 25 (Untergrenze, konservativ). Bei Detail-Ausbau ergaenzen.
- **Bewusst offen: chemnitz.de-Satzungs-PDF liefert curl-403** (WAF/Bot-Schutz, kein toter Link — bei Erhebung maschinell lesbar). Beobachten.
- **Bewusst offen: zwei Pruefdaten je Seite** (Kopf vs. Kasten) — kosmetisch.
- **02.07. (Loop-Welle) F7 UNSICHER: sozialbestattung.html "uebernommene Kosten oft 1.500-3.500 €"** — Sozialamts-Empirie ohne Quelle am Satz (zufaellig = alte Anonym-Spanne). Nicht angefasst; bei naechster Sozialbestattungs-Ueberarbeitung Quelle finden oder Formulierung entschaerfen.
- **F11 Info: FAQPage-Rich-Results zeigt Google seit 08/2023 fast nur noch Behoerden/Gesundheit** — unsere FAQ-Bloecke zielen auf Content/AI-Answer-Extraktion, nicht SERP-Sterne. Erwartung entsprechend.
- **Bewusst offen: Satelliten-Links ohne Trailing-Slash neben Bestands-Links mit Slash** — funktional egal (Netlify), nur Stil.
- **02.07. (Grabpflege-Welle) False Positives F17/F18:** "/bestattungskosten sagt 10-50 Euro/Jahr Grabpflege" und "Steuer-FAQ pauschal 'nicht absetzbar'" — beide Saetze existieren weder im Repo noch live (0 Treffer mit+ohne Cache-Buster); Live-FAQ hat die korrekte Par.-33-EStG-Antwort. Reviewer-Fetcher-Snapshot. NICHT fixen.
- **Bewusst offen (Grabpflege): Eigenleistung unbeziffert, Sozialbestattung-deckt-keine-Grabpflege-Satz fehlt** — Reviewer-Anregungen ohne Score-Relevanz; bei naechster Ueberarbeitung.

## Welle Daten-Spende 03.07.2026 (Score 58) — verworfene/eingeordnete Findings
- **M4 "DSE ist live noch Alt-Stand, 6a fehlt" = FALSE POSITIVE Nr. 4 (Fetcher-Cache).** Zur Review-Zeit selbst
  verifiziert: `curl datenschutz?cb=<rand> | grep` fand "6a. Freiwillige anonyme Daten-Spende" + "drei Ausnahmen"
  (2 Treffer). Feature + DSE gingen im SELBEN Commit (a3a323e) live, ein Fenster gab es nie. Der wahre Kern des
  Findings war M5 (Par.2 + Methodik-Box uebersehen) — der wurde gefixt. Regel bleibt: Live-Behauptungen von
  Reviewern IMMER selbst mit Cache-Buster pruefen.
- **M9 (Button "anonym spenden" vs. Hedge)**: akzeptiert nach M1-Fix — mit 30-Tage-Trennprozess ist "anonym"
  fuer die Dauer-Phase korrekt; Karte+DSE erklaeren die Phasen.
- **M11 (25er-Schwelle, Differenzangriffe)**: berechtigt fuer PUBLIKATIONEN — als Redaktionsregel in
  DATEN-SPENDE.md aufgenommen (nicht-ueberlappende Zellen, Median, Rundung). Kein Site-Text-Fix noetig.
- **M12 (Fake-Submissions)**: berechtigt — Plausibilitaetsfenster + IP-Zweckbindung (Missbrauchs-Abwehr) in
  DATEN-SPENDE.md; Methodik-Transparenzsatz kommt mit der ersten Publikation.
