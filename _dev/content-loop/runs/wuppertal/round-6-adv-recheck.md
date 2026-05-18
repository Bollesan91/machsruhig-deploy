Ich lese die drei Dateien.

Fetching site
Web durchsucht

Adversarial-Mindset an. Annahme: v3 hat mindestens 3 Schwächen. Ich gehe systematisch v2-Befunde durch und suche neue.

v2-Befunde Check (was wurde gefixt?):

❌ Foerster-Halluzination → gestrichen, jetzt nur "Vertreter der Wuppertaler Stadtgeschichte" + Verweis auf Stadtarchiv. ✓ Sauber gelöst.
❌ Eurosätze-Suggestion → Tabellen-Header heißt jetzt "Spanne NRW-Großstädte (Orientierung)" + Disclaimer. ✓ Sauber gelöst.
❌ 25-Jahre ohne Direktlink → Link auf Microsite, aber nicht auf die Satzung selbst. Teilweise gefixt.
FAQ-Schema Ratingen → entfernt. ✓
Copyright 2024 → jetzt "2025–2026". ✓

Jetzt neue adversariale Suche:

Befund A — Halluzinations-Verdacht Krummacher-Genealogie: Der Text sagt: „Der Name verweist auf die theologische Familie Krummacher... Friedrich Wilhelm Krummacher (1796–1868) wirkte als Pfarrer an der Elberfelder Niederländisch-Reformierten Gemeinde." — Faktencheck: F.W. Krummacher (1796–1868) war Pfarrer in Barmen-Gemarke, später Elberfeld, dann Potsdam. Aber: der Friedhof heißt Krummacherstraße, und ob die Straße tatsächlich nach diesem Krummacher benannt ist oder nach seinem Vater Friedrich Adolf Krummacher (1767–1845) oder seinem Onkel Gottfried Daniel Krummacher (1774–1837, der die reformierte Elberfelder Gemeinde prägte), ist nicht zitiert. Der Text verknüpft die Straßenbenennung mit einer konkreten Person ohne Beleg — und G.D. Krummacher wäre der historisch korrektere Bezug für „Elberfelder Niederländisch-Reformierte Gemeinde". Halluzinations-Verdacht in Kategorie 12.

Befund B — Quellen-Lücke beim harten Faktum „Ruhezeit 25 Jahre": Der v2-Befund 3 ist nicht voll behoben. Die Aussage „Ruhezeit für Erwachsenengräber beträgt in Wuppertal nach Auskunft der städtischen Friedhofsverwaltung 25 Jahre, für Kindergräber bis zur Vollendung des fünften Lebensjahres 20 Jahre" ist eine harte Zahlen-Tatsachenbehauptung. Verlinkt wird die Microsite, nicht die Friedhofssatzung mit der konkreten §-Fundstelle. Zusätzliches Risiko: „20 Jahre für Kindergräber bis Vollendung 5. Lebensjahr" ist eine sehr spezifische Zweitzahl — wenn der Re-Check-Script greift, ist das genau der Typ Aussage, der einen Primärquellen-Direktlink braucht. Auch der „nach Auskunft der städtischen Friedhofsverwaltung"-Hedge ist schwach: telefonische Auskunft ≠ verlinkbare Primärquelle.

Befund C — Generischer Satz + Quellen-Lücke „spezifisch bergische Trauerkultur": Im Krummacher-Absatz steht: „Der Friedhof ist ein Beispiel für die spezifisch bergische Trauerkultur: schlicht in der Formensprache, geprägt von reformiert-protestantischer Zurückhaltung, mit Familiengrabstätten in geschlossenen Geviertanordnungen..." — Das ist eine kulturwissenschaftliche Behauptung ohne jede Quelle. „Geschlossene Geviertanordnungen" als wuppertaler Spezifikum, der Vergleich mit Melaten/Düsseldorfer Nordfriedhof als „repräsentativer" — alles unbelegt. Kategorie 1 (Quellen-Lücke) + Kategorie 12 (Halluzinations-Verdacht). Auf einer YMYL-Page mit Author-Schema ist das die schwächste Stelle der Seite, weil sie literarisch ist statt überprüfbar.

Zusatzbefund (nicht Top-3, aber notiert): Im Schema.org JSON-LD steht beim Place-Eintrag Hauptfriedhof Elberfeld die Beschreibung „eröffnet 1898" — der Hauptfriedhof Elberfeld wurde laut Stadtwiki und Stadt Wuppertal tatsächlich 1898 eröffnet, das passt. Aber der Eröffnungsjahr-Hinweis sollte verifizierbar sein — Quelle fehlt sowohl im Schema als auch im Body. Sekundär.

SCORE: 83/100

FUNDE:

SCHWÄCHE 1 (Friedhof Krummacherstraße, Krummacher-Genealogie): Friedrich Wilhelm Krummacher (1796–1868) wird als prägende Figur der Elberfelder reformierten Gemeinde genannt — historisch ist aber Gottfried Daniel Krummacher (1774–1837) der eigentliche Elberfeld-Reformierten-Pfarrer; F.W. Krummacher wirkte primär in Barmen-Gemarke und später in Potsdam. Zudem keine Quelle für die Verknüpfung Straßenname↔Person. Halluzinations-Verdacht. Verbesserung: Verifizierung über Stadtarchiv/Stadtwiki Wuppertal — entweder G.D. Krummacher als korrekten Bezug einsetzen oder Familien-Bezug allgemeiner halten („Theologen-Familie Krummacher, im 19. Jahrhundert in Elberfeld und Barmen wirkend") ohne konkrete Personenzuordnung ohne Beleg.
SCHWÄCHE 2 (Ruhezeit 25/20 Jahre, harte Tatsachenbehauptung ohne Primärquellen-Direktlink): „Ruhezeit Erwachsene 25 Jahre, Kindergräber bis 5. Lebensjahr 20 Jahre nach Auskunft der städtischen Friedhofsverwaltung" — verlinkt wird nur die Microsite, nicht die Friedhofssatzung mit §-Fundstelle. „Nach Auskunft" ist als Quellenangabe für eine YMYL-Zahlenaussage zu weich. Verbesserung: Direkter Link zur Friedhofssatzung-PDF auf wuppertal.de + §-Angabe in der Satzung; falls PDF-Pfad nicht verifizierbar, „laut § X der Friedhofssatzung der Stadt Wuppertal, abrufbar unter [Microsite]" mit konkretem Paragraphen.
SCHWÄCHE 3 (Krummacher-Absatz, unbelegte kulturwissenschaftliche Behauptung): „Spezifisch bergische Trauerkultur: schlicht in der Formensprache, geprägt von reformiert-protestantischer Zurückhaltung, mit Familiengrabstätten in geschlossenen Geviertanordnungen" + Vergleich „Düsseldorfer Nordfriedhof oder Kölner Melaten" als „repräsentativer" — komplett ohne Quelle. Auf einer YMYL-Page mit Article-Schema und Autor-Auszeichnung sind solche kulturhistorischen Wertungen ohne Beleg ein E-E-A-T-Audit-Befund. Verbesserung: Entweder Beleg (Denkmalpflege NRW, Stadtarchiv Wuppertal, Bergisches Geschichtswerk) ergänzen oder Passage entschärfen zu einer beschreibenden Aussage ohne Vergleichswertung („Die Anlage zeigt die für reformiert-protestantische Friedhöfe des 19. Jahrhunderts typische Zurückhaltung in der Grabgestaltung.").

MUST-FIX vor Deploy: ja.

Begründung: v3 ist gegenüber v2 deutlich verbessert — Foerster ist sauber raus, Eurosätze-Header ist klargestellt, FAQ-Schema-Inkonsistenzen behoben. Aber Schwäche 1 ist ein neuer Halluzinations-Verdacht (konkrete historische Person ohne Quelle), und Schwächen 2+3 sind beides Quellen-Lücken auf YMYL-tauglichem Niveau. Für eine Gold-Standard-Page mit Author-Schema und Stand 15.05.2026 sind „nach Auskunft" und unbelegte Kultur-Vergleiche genau die Stellen, an denen ein Re-Check-Script anschlagen würde. 83/100: über 80, weil die Page substanziell solide ist und v2-Befunde sauber adressiert wurden; unter 85, weil drei Belegrisiken offen sind, davon eines (Schwäche 1) ein Faktenrisiko.