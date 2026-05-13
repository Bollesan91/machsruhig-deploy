Ich lade die drei Dateien und prüfe.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

BRIEFING_OK. Adversarial Review v5-Final Osnabrück:

SCORE: 88/100

FUNDE:

v4 MUST-FIX-Punkte — Status:

Heger ältere Kapelle datieren → SAUBER GELÖST. v5 schreibt jetzt klar: "Die ältere, kleinere Kapelle ist jene Trauerhalle, die 1927 nach dem Scheitern des ersten Großentwurfs als bescheidener Vorgängerbau errichtet wurde". Datum 1927 explizit benannt, konsistent mit Quelle 11 (Wikipedia). Kein "Anfangsjahre"-Geschwurbel mehr. ✓
Krematoriumsinschrift → SAUBER GELÖST durch Streichung. Der inhaltsleere "Geist-der-Feuerbestattungsbewegung"-Satz aus v4 ist komplett raus. v5 beschreibt im Krematoriums-Block stattdessen die konkrete Technik (Ruppmann-Etagenöfen, waagerechter Sargentzug). Faktisch, ohne halluzinierte Inschrift. ✓
§ 8 Abs. 3 BestattG-Reihenfolge → DEFENSIV ENTSCHÄRFT. v5 zitiert die Reihenfolge nicht mehr wörtlich im Fließtext. Statt der Ziffernliste 1-6 jetzt: "vorrangig Ehegatten und Lebenspartner, danach volljährige Kinder, Eltern und weitere Verwandte in der gesetzlich festgelegten Abstufung – auch über die Kostenträgerschaft entscheidet. Die genaue Reihenfolge ist in der Bundesland-Seite Niedersachsen aufgeführt." Cross-Link statt riskantes Wörtlich-Zitat. Pragmatisch gelöst, Compliance-Killshot-Risiko entfernt. ✓
Hasefriedhof Flächenangabe → SAUBER GELÖST. v5 schreibt "rund 10 ha" im Meta-Block. Die überspezifischen 105.000 m² sind weg. ✓
Treuhandstiftung Gründungsjahr → SAUBER GELÖST durch Streichung. v5 schreibt nur noch "Eine Treuhandstiftung der Stadt Osnabrück kümmert sich um den Erhalt der wertvollen Grabmale". Kein Jahr mehr, keine Halluzinations-Falle. ✓

Drei neue Schwächen (Adversarial-Auftrag: ich finde 3, auch wenn die Page jetzt gut ist):

Quellen-Lücke Krematoriums-Detail Ruppmann/Stuttgart. Die Detailtiefe im Krematoriumskasten ist auffällig — "zwei gasbetriebene Etagenöfen der Firma Ruppmann (Stuttgart)", "waagerechter Sargentzug durch ein Tor, hinter dem der Sarg in einem künstlich beleuchteten Raum versenkt wurde". Quelle 11 (Wikipedia Heger Friedhof) ist die einzige plausible Quelle, aber das ist eine Sekundärquelle für eine sehr spezifische technische Aussage. Wenn ein Auditor die Wikipedia-Version checkt und Ruppmann/Stuttgart dort nicht genau so steht, ist das ein Halluzinations-Verdacht. Fix: Quelle 11 direkt am Krematoriums-Absatz inline verlinken, oder „Ruppmann"-Detail entschärfen zu „Etagenöfen einer süddeutschen Spezialfirma".
„adventure-hasefriedhof.de" Halluzinations-Verdacht. Im Hidden-Gem-Kasten Hasefriedhof: "Für jüngere Besucher gibt es unter adventure-hasefriedhof.de eine digitale Schnitzeljagd mit QR-Codes an einzelnen Gräbern (Stand 2025/2026 in Testphase, eine App ist in Vorbereitung)." Eine konkrete URL mit Statusangabe „2025/2026 in Testphase" — das ist die genaue Form, in der Halluzinationen auftauchen. Die Domain wird in keiner der 16 Quellen erwähnt. Wenn die Domain nicht existiert oder das Projekt nie startete, ist das peinlich und ein Faktencheck-Killshot. Fix: URL streichen oder verifizieren — wenn nicht verifizierbar, ganzen Halbsatz raus.
Floskel in Bestatter-Wahl-Sektion. „Eine pauschale Empfehlung wäre unredlich; sinnvoll ist ein systematischer Vergleich anhand objektiver Kriterien." — der erste Halbsatz ist die klassische Meta-Geste („wir sind seriös"), die Reviewer als Floskel-Marker werten. Auch „Wer auf konkrete Preisfragen ausweichend reagiert, ist mit Vorsicht zu betrachten" ist Allgemeinplatz ohne Osnabrück-Bezug. Die ganze Sektion ist die schwächste der Page — hier fehlt Osnabrück-Spezifik (Anzahl Bestatter in Osnabrück, BDB-Mitgliederliste konkret, Hinweise auf das städtische Online-Portal für Bestatter). Fix: Mindestens eine konkret Osnabrück-bezogene Zahl/Fakt einbauen (z. B. „in Osnabrück operieren rund X BDB-Mitglieder…") oder Sektion straffen.

MUST-FIX vor Deploy: ja — Punkte 6 und 7 sind Halluzinations-Risiken, die in der jetzigen Form ein einzelner Faktencheck killen kann. Punkt 7 (adventure-hasefriedhof.de) ist das gefährlichste, weil verifizierbar in 30 Sekunden. Punkt 8 (Floskel-Sektion) ist Score-Drücker, kein Blocker.

v4 → v5 ist ein klarer Sprung: alle fünf v4-MUST-FIX-Punkte sauber adressiert (3× gelöst, 2× durch Streichung entschärft). 88 ehrlich, kein 90+, weil mit Ruppmann-Detail und adventure-URL zwei neue Spezifik-Risiken eingebaut wurden, die in v4 nicht da waren — gleiches Pattern wie immer: lösen alte Probleme, generieren neue durch Übereifer in Details.