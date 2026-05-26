Claude hat geantwortet: Ich lese beide Dateien.
Orchestrierte Datenbeschaffung aus zwei Quellen für adversariale Audit-Analyse
Orchestrierte Datenbeschaffung aus zwei Quellen für adversariale Audit-Analyse

Ich lese beide Dateien.

Fetching site
Verifizierend §-Referenzen gegen primäre Rechtsquellen prüfen

Jetzt das Quellen-Pack.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/_dev/content-loop/runs/vorsorge-allein-leben/quellen-pack.md
Verifizierte kritische Paragraphen gegen Primärquellen statt Sekundärquellen

Jetzt verifiziere ich die kritischen §§ direkt gegen die Primärquellen — nicht auf Chat B vertrauen.

Fetching site
Verifizierend Erbordnungen und Gesetzesverweise gegen Primärquellen prüfend

§ 1827 ist sauber. Jetzt die Erbordnungen §§ 1928/1929 und § 1931.

Searching the web
Validating Schonvermögen-Spanne gegen Fallrecht-Variabilität

Erbordnungen bestätigt. Jetzt noch Schonvermögen-Betrag und Notarkosten.

Verifizierend Schonvermögen-Spannweite und interne Konsistenz prüfend
Systematisierte Compliance-Prüfung gegen Rechtsnormen und User-Perspektiven

Beide Dateien gelesen, §§ gegen gesetze-im-internet.de / dejure.org selbst geprüft (nicht auf Chat B verlassen). Ergebnis:

Fokus-Zwangschecks (10/10 abgearbeitet)
§§ 1928/1929 BGB — ✅ korrekt. § 1928 = 4. Ordnung (Urgroßeltern + Abkömmlinge), § 1929 = fernere Ordnungen. „§§ 1928 f." sauber. Quelltext bestätigt.
§ 74 SGB XII vs. Ordnungsamt — ✅ kein interner Widerspruch mehr. Beide Stellen (Notfallmappe-Hint + Mythos 5) sagen konsistent: ohne Angehörige → Ordnungsamtsbestattung; § 74 nur für bestattungspflichtige Angehörige mit knappen Mitteln. Chat-B-Fix hält. Minor: Bestattungspflicht ist Landesrecht und kann entfernte Verwandte erfassen — das Binär „keine Angehörige = immer Ordnungsamt" ist leicht vereinfacht, aber nicht falsch.
Patientenverfügung Form (§ 1827) — ✅ korrekt. Schriftform i.S.d. § 126 BGB, gedruckt + persönlich unterschrieben zulässig, keine notarielle Beglaubigung, jederzeit formlos widerrufbar, volljährig + einwilligungsfähig. Wortlaut deckt sich.
Eigenhändiges Testament — ⚠️ MEDIUM-Imprecision. Page: „gültig, wenn du es vollständig handschriftlich verfasst, mit Ort und Datum versiehst und unterschreibst." Nach § 2247 BGB sind Ort/Datum Soll-Angaben, keine Wirksamkeitsvoraussetzung — ein undatiertes eigenhändiges Testament ist gültig (nur bei Mehrfach-Testamenten problematisch). Die „gültig, wenn"-Konstruktion suggeriert Konstitutiv-Erfordernis. Zudem: § 2247 wird nirgends zitiert — die einzige nicht belegte erbrechtliche Kernaussage.
Notarkosten — ✅ besser als Quellen-Pack. Page sagt „ab ca. 150 €, steigt mit Geschäftswert (GNotKG)" und lässt die Obergrenze offen. Korrekt: die 500-€-Deckelung des Quellen-Packs ist für mittlere/große Nachlässe schlicht zu niedrig (1,0-Gebühr KV 21200 GNotKG skaliert). Gut, dass nicht gedeckelt. Caveat: 150-€-Untergrenze plausibilisiert, nicht primärquellen-verifiziert (s. Eigen-Kritik).
Schonvermögen 8.700–10.500 € — ✅ vertretbar mit Hedge. Rechtsprechung spannt real weiter (~3.200–11.300 €, Einzelfall); 10.500 € = VG Münster (Erdbestattung). Range etwas eng gefasst, aber durch „in einer Größenordnung von etwa" + „Bewertung im Einzelfall beim Amt" sauber abgesichert.
Vorsorgeregister 15–20 € — ⚠️ plausibel, in diesem Audit nicht primärquellen-verifiziert. Real: Grundgebühr ~13 € (Lastschrift) / ~15,50 € (Überweisung) + Zuschlag pro weiterer Person. „15–20 €" trifft die Größenordnung, kann bei mehreren Bevollmächtigten leicht überschritten werden. Hedge vorhanden.
JSON-LD FAQ vs. HTML-FAQ — ✅ per Sichtprüfung wortgleich, alle 10 Fragen, gleiche Reihenfolge, Antworttexte identisch. Kein Rich-Result-Mismatch erkennbar. Caveat: Auge, kein Byte-Diff.
Pflichtteil — ✅ korrekt (§ 2303/§ 2309 BGB-Logik): Kinder, Ehegatte, Eltern nur ohne Abkömmlinge. Großeltern korrekt nicht genannt. Minor: eingetragene Lebenspartner nicht erwähnt (Randfall). § 2303 ebenfalls nicht zitiert.
Crosslinks — 🔴 NICHT verifizierbar in diesem Audit. Quellen-Pack bestätigt nur /sozialbestattung, /bestattungsarten, /bestattungskosten, /tools/vorsorge-check. Nicht bestätigt: Breadcrumb /vorsorge/, /vorsorge/patientenverfuegung, /vorsorge/testament, /vorsorge/sterbegeldversicherung. Live nicht prüfbar (Seite noch nicht deployed, Domain nicht im Netz-Whitelist). Siehe Show-Stopper.
Perspektive A — Alleinstehender 60+ mit Vorsorge-Druck
Keine kompakte Handlungs-Sequenz oben. [MEDIUM] Die Reihenfolge steckt in FAQ #1 und in den Keyfacts (= Fakten, keine Schritte). Wer „nicht 30 Seiten" will, findet kein „Mach zuerst 1, dann 2, dann 3"-Kästchen. 12 Min Lesezeit + 11 Sektionen ist für die genervte Zielgruppe viel.
Der akuteste Fall der eigenen Zielgruppe wird dünn bedient. [HIGH] „Ich habe WIRKLICH niemanden" → Page sagt Berufsbetreuer/Betreuungsverein „kommen in Betracht", aber nicht wie man sie findet (örtliche Betreuungsbehörde, Betreuungsverein vor Ort) und was sie kosten. Das ist die Kern-Schmerzstelle — und sie bleibt bei „kommt in Betracht" stehen.
Testament-Falle. [HIGH] Page drängt „handschriftlich reicht", schließt aber die Auffindbarkeits-Schleife für das Testament nicht — anders als bei der Vollmacht (Vorsorgeregister). Amtliche Verwahrung beim Nachlassgericht + Zentrales Testamentsregister fehlen komplett. Genau für den Alleinstehenden ist das die #1-Falle: handschriftliches Testament im Schrank → wird nie gefunden → gesetzliche Erbfolge/Fiskus, also exakt das, was er vermeiden wollte.
Perspektive B — Skeptiker (Lead-Funnel-Verdacht)
Neutralität hält. [LOW / positiv] Sterbegeld-Sektion ist auffällig kritisch („Eingezahltes kann Auszahlung übersteigen", „weniger Renditeprodukt"), kein Versicherungs-CTA, kein Affiliate. Einziger CTA = kostenloser Vorsorge-Check ohne Anmeldung. Erkennbar kein Sterbegeld-Verkäufer.
Bestattungsvorsorgevertrag-Repetition + „Bestatter finden". [MEDIUM] Der Vorsorgevertrag wird ~5× als „durchsetzbar"-Lösung wiederholt; in Nav/Footer steht „Bestatter finden / München". Faktisch berechtigt (es ist der Durchsetzungs-Mechanismus), aber die Häufung + der Bestatter-Nav-Link kann als weicher Funnel gelesen werden. „München" ist zudem off-target für eine bundesweite Alleinstehenden-Page.
CTA-Wording. [LOW] „Welche Dokumente brauchst du?" + „Kostenlos · ohne Anmeldung · läuft im Browser" — keine künstliche Dringlichkeit, keine Verknappung, nicht manipulativ. Sauber.
Perspektive C — Fachkundiger (Notar / Sozialarbeiter)
Zwei fehlende §-Anker. [MEDIUM] § 2247 BGB (eigenhändiges Testament) und § 2303 BGB (Pflichtteil) werden inhaltlich behauptet, aber nicht zitiert — die einzigen erbrechtlichen Kernaussagen ohne §. Ein Notar will die sehen. Alle übrigen §§ (1827, 1828, 1924–1926, 1928, 1931, 1936) verifiziert korrekt.
Patientenverfügung-Vagheit = Unwirksamkeit untertrieben. [MEDIUM] Page: pauschale PVs „lassen sich schwerer anwenden". Nach BGH-Rspr (XII ZB 61/16) ist eine zu unbestimmte PV unverbindlich/unwirksam, nicht bloß „schwerer anwendbar". Für die Zielgruppe ohne auslegende Vertrauensperson ist das ein schärferer Hinweis wert.
Empfehlung mit Caveat. Keine falschen Aussagen gefunden — die §§ stimmen, Neutralität gut. Aber als alleinige Grundlage zu lückenhaft (Testaments-Auffindbarkeit, konkreter Betreuer-Weg, § 2247/§ 2303, PV-Unwirksamkeit). → empfehlbar als Einstieg, nicht als Endpunkt.
Killer-Fragen, die die Page NICHT beantwortet
„Ich habe niemanden — wie und wo finde ich konkret einen Berufsbetreuer/Betreuungsverein, und was kostet mich das?"
„Wo bewahre ich mein handschriftliches Testament auf, damit es nach meinem Tod überhaupt gefunden und eröffnet wird?" (amtl. Verwahrung + Testamentsregister)
„Wer kündigt Wohnung/Verträge, versorgt mein Haustier, wenn niemand da ist?" (Notfallmappe listet das, löst aber nicht, wer es verbindlich übernimmt → trans-/postmortale Vollmacht, Testamentsvollstrecker fehlen)
„Was kostet das alles zusammen ungefähr?" (0 € / 15–20 € / Vorsorgevertrag x.xxx € / Notar ab 150 € verstreut — keine Gesamtübersicht)
„Muss meine bevollmächtigte Person das überhaupt machen — und was, wenn sie vorher stirbt oder ablehnt?" (Ersatzbevollmächtigte, keine Annahmepflicht)
Verdict: MIT-CAVEAT

Keine sachlich falschen Rechtsaussagen — alle prüfbaren §§ verifiziert korrekt, Neutralität solide. Abzug ausschließlich für (a) inhaltliche Lücken speziell für die erklärte Zielgruppe (der wirklich personenlose Alleinstehende) und (b) unverifizierte Crosslinks.

Show-Stopper vor Deploy
🔴 Crosslink-Targets verifizieren — /vorsorge/, /vorsorge/patientenverfuegung, /vorsorge/testament, /vorsorge/sterbegeldversicherung. Existieren die nicht, deployst du 404s auf einer YMYL-Seite (UX + SEO-Schaden). Harter Blocker.
🟠 Analytics-Doppelung prüfen — Page lädt Plausible (plausible.io/js/script.js) und /js/tracking.js. Frage: Ist Plausible für machsruhig korrekt, oder sollte das (wie machsleicht) Umami sein? Doppel-Tracking + möglicher Vendor-Mismatch. Config-Blocker, nicht rechtlich.

Inhaltliche Lücken (Testaments-Verwahrung, konkreter Betreuer-Weg, § 2247/§ 2303, PV-Unwirksamkeit) sind Post-Launch-Verbesserungen bzw. schnelle Adds — kein Deploy-Blocker, aber sie sind der Unterschied zwischen „MIT-CAVEAT" und „PASS".

Eigen-Kritik
ZVR-Gebühr (15–20 €) und GNotKG-Untergrenze (150 €) habe ich nur plausibilisiert, nicht gegen Primärquellen (BNotK-Gebührenordnung / GNotKG-KV) gefahren. Beide können im Detail abweichen. Ehrlich gekennzeichnet, nicht abgehakt.
JSON-LD vs. HTML per Auge verglichen, kein Byte-Diff — bei 10 langen Antworten kann eine Wort-/Komma-Abweichung durchrutschen. Ich konnte die Datei nicht lokal ziehen und diffen.
Crosslink-Existenz live nicht prüfbar (Seite nicht deployed, Domain nicht im Whitelist) → bleibt offener Blocker, nicht von mir verifiziert.
Chat-A/B-blind wie gefordert geblieben — Nachteil: ich kann nicht ausschließen, dass eine von mir als „Lücke" markierte Sache (z. B. amtliche Testamentsverwahrung) bewusst in eine verlinkte Detailseite /vorsorge/testament ausgelagert wurde. Falls die Zielseiten das abdecken, sinkt die Severity der Findings A-3 und C-1.