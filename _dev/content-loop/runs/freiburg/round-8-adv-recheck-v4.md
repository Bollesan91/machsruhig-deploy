Ich lade die drei Dateien und prüfe MUST-FIX-Status.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Hinweis: Das übergebene Adv-v3-Dokument ist 93%, nicht 82% (Briefing-Trigger-Wert weicht ab). Ich prüfe trotzdem die v4 adversarial gegen das C-Briefing und die offenen Punkte aus v3.

Die drei v3-Restpunkte (1) 14./15.4.1914-Datum, (2) Eingangstor-Formulierung, (3) Trauerkultur dünn) wurden in v4 sichtbar adressiert: "im April 1914" mit expliziter Datums-Unsicherheits-Note, "monumentales Hauptportal" statt Triumphbogen, Trauerkultur mit Münster-Hosanna/Wegga/Totenwache angereichert. Jetzt Schwächen-Suche v4:

SCORE: 89/100

FUNDE:

SCHWÄCHE 1 — Schema.org / FAQPage-Drift (Kategorie 10): Die FAQ-Antwort "Was kostet eine Bestattung in Freiburg?" im JSON-LD listet "Grab im Baumfeld 614 €", die sichtbare HTML-FAQ schreibt aber "Urnengrab im Baumfeld 614 €". Außerdem fehlt in der JSON-FAQ-Antwort "Kindergrab" (165 €) und in der HTML-FAQ ebenfalls — aber der Tabellentext führt es als A.4.1.3. Inkonsistenz HTML↔JSON-LD bei FAQ-Antworten ist ein Schema-Warning-Trigger (Google Rich-Results-Test). Fix: FAQ-Antwort-Text in JSON-LD 1:1 mit HTML-Detail synchronisieren oder beide auf identische Kurzliste reduzieren.
SCHWÄCHE 2 — Floskel/Generischer Satz in Trauerkultur (Kategorie 2 & 11): „Freiburg ist eine universitätsgeprägte Stadt mit kosmopolitischer Trauerkultur" — generisches Klischee ohne Beleg, austauschbar mit Heidelberg/Tübingen/Göttingen. Auch „Wandel zur Feuerbestattung und zu pflegeleichten Grabformen … die klassisch-katholische Sargbestattung im Wahlgrab als statistische Norm längst abgelöst" — Behauptung über Statistik ohne Quelle/Zahl (Feuerbestattungsanteil Freiburg %). Fix: Entweder konkrete Zahl vom Eigenbetrieb Friedhöfe (Feuerbestattungsquote Freiburg, z. B. Geschäftsbericht) oder Satz streichen.
SCHWÄCHE 3 — Halluzinations-Verdacht §-Querverweis (Kategorie 12): Behauptung „§ 31 BestattG BW ... identisch mit der Aufzählung in § 21 Abs. 1 Nr. 1 und in § 38 Abs. 1 Nr. 3 der Freiburger Friedhofssatzung". Das wirkt zu spezifisch ohne Quellen-Snippet: § 21 Satzung und § 38 Satzung mit diesen exakten Absatz-/Nummern-Zuordnungen sind nicht in der zitierten Quellenliste verifiziert sichtbar (PDF wird gesamt verlinkt, aber kein Stellenzitat). Wenn das Gebührenverzeichnis penibel mit A.x.y.z verifiziert wurde, sollte der Satzungs-§-Querverweis identisch belegt sein. Risiko Faktenfehler / Audit-Fail im bundesland-recheck.py bei „specific paragraph claims without sentence-level source". Fix: § 21 und § 38 entweder mit Seitenzahl/Wortlaut-Snippet im Quellen-Eintrag verankern oder Querverweis weniger spezifisch formulieren („vgl. Friedhofssatzung").

Zusatz (kein eigener Schwäche-Slot, aber Notiz): Im Footer steht „© 2024–2026 machsruhig.de" — wenn Domain laut Memory erst 2026 produktiv wird, ist 2024 fragwürdig. Niedrig-Prio.

MUST-FIX vor Deploy: ja.

Schwäche 1 (Schema-Inkonsistenz HTML↔JSON-LD) ist ein echter Blocker — Rich-Results-Test wird warnen und FAQ-Snippet im SERP kann ausfallen. Schwäche 3 ist Re-Check-Risk. Schwäche 2 ist kosmetisch, kann mitgehen, sollte aber bei nächstem Pass raus. Score 89 — über 85-Schwelle, aber nicht „sauber Gold" wegen Schema-Drift.