# LEKTIONEN — destilliertes Findings-Gedächtnis (Pflicht-Input für Writer & Reviewer)

> Muster, nicht Einzelfälle. Quelle: Verdichtungs-Loop 10.–12.06.2026 (Ränge 1–13, ~15 Review-Wellen) + frühere Audits. Neue Muster nach jeder Welle nachtragen. Mechanisierbares wandert zusätzlich in `_dev/scripts/lint-site.py` / `_dev/config/lint-verboten.txt`.

## Zahlen & Kosten

1. **Jede mehrfach vorkommende Zahl driftet.** Kostenspannen standen auf einer Seite in bis zu 7 Varianten (Meta, OG, Keyfacts, 2 Tabellen, Fließtext, FAQ, JSON-LD) — und widersprachen sich. Vor dem Schreiben: Stellen-Inventar; beim Ändern: ALLE Stellen in einem Skript-Lauf.
2. **Grep-Fallen:** Beträge stehen auch als „Euro" ausgeschrieben, mit Beugungen, in JS-Strings und in `<meta>`/og — Exakt-€-Greps verfehlen sie. Breiter Muster-Sweep + git-diff-Review sind die Wahrheit.
3. **Kanonische Spannen nur aus `/methodik#kostenmodell`** (Erd 3.700–9.300 ohne / 5.300–14.300 mit Grabpflege; Feuer 3.380/3.400–8.200 bzw. 3.800–9.700; See 2.850–6.200; Baum 3.050–7.000; anonym 1.800–3.350; Direktkremation 1.000–2.200). Lokale Zahlen nur satzungsbelegt; sonst defensiv (Verweis + Modell-Einordnung) statt erfundener Spannen.
4. **Einordnungen müssen rechnerisch möglich sein:** „Typisch ab X" darf nicht unter der Summe der eigenen Mindest-Posten liegen (Hamburg: 4.500 < 2.800+1.945). Untergrenzen gegen eigene Tabellen rechnen.
5. **Quellen-Mischung kennzeichnen:** Amtliche Sätze vs. Markt-Korridore (Bestatter-Auswertungen) nie in einer Tabelle mischen, ohne die Differenz zu erklären — sonst sieht es wie Widerspruch aus (Berlin).

## Recht (YMYL-Kern)

6. **Fundstellen nur primärverifiziert.** Reviewer-Normwissen ist bei novellierten Gesetzen systematisch veraltet — in BEIDE Richtungen (SH-Frist: Reviewer korrekt 9 Tage; PM-Link: Reviewer fälschlich „tot"). Jedes Az./§ vor Einbau selbst prüfen.
7. **Landesrecht ≠ Bundesrecht** („bundesrechtlich … Art. 10 BestG" = Kategorienfehler). Verkündungs-Details (GVBl-Nr./Datum) nur wenn selbst verifiziert — sonst weglassen, „Novelle JJJJ, in Kraft seit TT.MM." reicht.
8. **Pauschalen über 16 Bundesländer sind fast immer falsch** („in allen Bundesländern 48 h", „4–10 Tage überall", „nur Nord-/Ostsee"). Nur belegte Beispiele nennen + „einige Länder regeln keine …".
9. **Site-Linie Sozialbestattung (BSG-fest):** § 74 SGB XII = Zumutbarkeit der Kostentragungspflichtigen (nie „Erben zu arm"); Antrag AUCH nachträglich möglich (B 8 SO 20/22 R); einfacher freier Trauerredner gehört zu den erforderlichen Kosten; SGB II = SGB XII gleichrangig (regelmäßig unzumutbar); Schonvermögen je nach Gericht ~7.000 (OVG NRW 12 A 2454/18) bis ~10.500 € (VG Münster 6 K 4230/17). Jede Seite, die §74 erwähnt, gegen diese Linie prüfen.

## Logik-Checks, die Reviewer-Gold waren

10. **Zeitliche Unmöglichkeiten:** Person †1816 „beigesetzt auf" Friedhof eröffnet 1877 → nur per Umbettung möglich; im Zweifel Namen streichen statt raten. Gleiche Klasse: Gründungsjahre, „40 Jahre vor X" nachrechnen.
11. **Superlative & Tourismus-Ton sind HOCH-Findings** auf YMYL-Seiten — besonders in FAQ/JSON-LD (SERP-sichtbar neben Trauerfällen): „Ein Muss für Hamburg!", „UNESCO-Kulturdenkmal" (erfunden), „außergewöhnlich viel Wahlfreiheit" (ignoriert Friedhofszwang).
12. **Meta/OG sind Versprechen:** „Kostenspanne, recherchiert" in der Description, die die Seite bewusst nicht liefert = Widerspruch im Share-Snippet. Meta immer gegen Seiteninhalt prüfen.
13. **Schema lügt leicht:** containsPlace/@id-Referenzen auf nicht existierende Anker; Service-Schema, das machsruhig als Bestattungs-Provider auswies; FAQPage-Antworten mit unbelegtem Zahlenwerk. JSON-LD ist Inhalt, kein Dekor — gleiche Prüftiefe.

## Technik-Muster (Standalone-Seiten & Fixes)

14. **Standalone-Seiten ohne site.css:** `var(--mr-*)` braucht IMMER Fallback (`var(--mr-text,#2D2319)`); :root-Werte siehe assets/css/site.css. Sichtbarkeits-Test ≠ Farb-Rendering-Test — computed styles prüfen.
15. **Kein @media in @media** — beim Ersetzen von Regeln den umgebenden Block prüfen (Desktop-Basisregel gehört VOR den Mobile-Block).
16. **tracking.js selektiert exakt `[data-track="cta"]`** (+ feste Klassen) — eigene data-track-Namen feuern nie; Unterscheidung liefert das Event über href+page. Umami genau 1× pro Seite (Doppel-Einbindung = doppelte Pageviews).
17. **Fix-induzierte Fehler sind die häufigste spätere MAJOR-Quelle.** Bei Block-Splices: Tag-Balance + Soll-Reihenfolge + JSON-LD-Parse als Asserts VOR dem einzigen Write am Ende. Nach jedem Fix: Linter + Diff-Re-Check, keine ungeprüfte Vollrunde.
18. **Stale Kommentare lügen** („echter Loader: consent.js → Opt-In" über einem Head-Load). Kommentare beim Anfassen der Stelle mitprüfen/entfernen.
19. **„Als erledigt gemeldet" ≠ erledigt** — gilt für Reviewer UND für uns (Tracking-Auflage R12). Erfolgsmeldungen immer mit Beleg (Grep/Curl/Screenshot-Äquivalent).

## Funnel & Struktur (Stadt-/Funnel-Seiten)

20. **Soll-Reihenfolge:** Schnelle Hilfe → Fakten/Behörden → Akut-Schritte → (Recht kompakt) → Kosten (+ Gesamtbudget-Einordnung) → Sozialbestattung → Bestatter-Wahl → Formular → Historie/Kultur/Umland → FAQ → Exit-Links → Quellen. **Exit-Blöcke und Promi-Essays nie vor dem Formular.**
21. **Check24-Sterbegeld-Affiliate nie im Sozialbestattungs-Kontext** (monetarisiert Zahlungsunfähige mit nutzlosem Produkt). Nur Vorsorge-Kontext.
22. **Lead-Formulare:** mindestens ein Pflicht-Rückkanal (Email required); CTA-Texte konsistent; Datenschutz-Checkbox required.
23. **Stand-Daten:** sichtbarer „Stand", JSON-LD dateModified und Quellen-Stand müssen zusammenpassen; Footer-„Landesgesetze Stand X" ist davon getrennt (Prüfstand der Gesetze).

## Nachtrag 12.06.2026 (V4.1-Dogfood + externe Bewertung)

24. **FAQPage-Schema auf JS-gerenderten Tool-Seiten** (Babel/JSX, FAQ im `<script>`-Template): statischer Linter kann Parität NICHT prüfen → Browser-Smoke nötig. Gefunden: 2 Tool-Seiten (abschiedsbrief, fristen-radar) hatten FAQPage-Schema für FAQ, die **gar nicht rendert** = echter Strukturdaten-Verstoß; danksagung rendert, hatte aber Wortdrift. Regel: FAQPage nur, wenn die FAQ auch (statisch oder gerendert) sichtbar ist.
25. **Stand-Datum-Konsistenz pro Seite** ist mechanisierbar (Linter L12) — „Stand: <Monat 2026>" darf je Seite nur EINEN Monat haben; „Stand seit <Datum>" (Rechts-Gültigkeit, z. B. Vermögensfreibetrag 01.01.2023) ist ausgenommen. L12 fand sofort 3 weitere Seiten (kassel, angebotspruefer, was-tun) neben dem Eval-Fund (sozialbestattung).
26. **Sichtbare Grammatik-/Rechtsfehler in Lead-Sätzen sind die teuersten Vertrauensbrecher** (Eval-Fund): „Ohne Testament entscheidet die Gesetze" (YMYL-Recht-Seite). Lead-Sätze von Recht-Seiten besonders scharf prüfen.
27. **Vormundschaft: das Familiengericht entscheidet/bestellt den Vormund (§ 1774 BGB), das Jugendamt wird beteiligt und kann selbst Vormund werden** — NICHT „das Jugendamt entscheidet". (Primärverifiziert 12.06.)
28. **Gemeinfreiheit-Überclaims:** „Bibelverse immer frei verwendbar" ist falsch — moderne Übersetzungen (Lutherbibel 2017, Einheitsübersetzung) sind urheberrechtlich geschützt. Bei „Public Domain"/„gemeinfrei"-Aussagen Übersetzung/Ausgabe qualifizieren.
29. **JSX-Leak `className=` im ausgelieferten HTML**: bei den Babel-in-Browser-AI-Tools (trauerrede/danksagung/abschiedsbrief) by design; auf JEDER anderen Seite ein Bug (Browser ignoriert das Attribut → CSS-Klasse wirkungslos). Linter L11.
