# Validity-Sweep — 3 Tools (Bestattungskosten-Rechner, Kostenrechner, Vorsorge-Check)

**Datum:** 2026-05-26 · **Methodik:** Helper-V3 Outcome-Validity (Stufe 0), 3 parallele Reviewer-Tabs, Self-Verify gegen Code-Schwellen via raw.githubusercontent.com
**Status Tools:** Alle LIVE, alle index,follow, alle in Sitemap (Anbeginn der Audit)

## Gesamtverdict: 3 × `VALIDITY_FAIL`

Gleiche Pathologie-Klasse wie der Angebotsprüfer (vgl. `angebotspruefer-validity-fail-2026-05-23.md`):
- **Bezugsgröße** (Linse 1) bei allen 3
- **Anspruch > Datenbasis** (Linse 4) bei allen 3
- **Fehler-Asymmetrie** (Linse 5) bei allen 3 — YMYL/Trauerkontext: False-Beruhigung ist der schädlichere Fehler

Dringlichkeits-Reihenfolge nach erwartetem Real-Schaden: **Vorsorge-Check → Kostenrechner → Bestattungskosten-Rechner**.

---

## 1. Vorsorge-Check (`tools/vorsorge-check/`) — DRINGLICHKEIT 1

### Verdict: `VALIDITY_FAIL` (YMYL-kritisch)

Tool ist zu 100 % anwesenheits-basiert (Häkchen = "besitze ich"). Es gibt keine Frage zu Wirksamkeit, Aktualität, Form, Inhalt, Auffindbarkeit. Das Ergebnis behauptet aber einen Bereitschafts-/Vollständigkeitszustand ("Du hast alle wichtigen Dokumente", "Du bist gut vorbereitet", JS Z. 329/331). Headline-Verzweigung hängt allein an `missing.length === 0`.

| # | Szenario | Inputs | Erwartet | Tatsächlich | Schaden |
|---|---|---|---|---|---|
| a | Mehrdeutiger Input: unbestimmte PV (BGH XII ZB 61/16) | verheiratet, alle 8 Docs OK inkl. unbestimmter PV | Wirksamkeits-Vorbehalt, keine "fertig"-Headline | "Super! Du hast alle wichtigen Dokumente. Du bist gut vorbereitet." | False-Beruhigung HOCH — exakt der Fall, den die PV verhindern soll |
| b | Sonderfall: nichteheliche Lebensgemeinschaft (kein Slot) | single + Testament nicht angekreuzt (oder verheiratet falsch gewählt wegen Sublabel "Mit Partner zusammen") | "dringend" für Testament (Partner erbt sonst nichts, § 1931 BGB greift nicht) | `priorityBy.single='empfohlen'` → gelb "Empfohlen" | Unterwarnung; Widerspruch Tag vs. Begründungstext; Erhebungs-Bias durch Sublabel |
| c | Grenzwert: alles vs nichts | alle 8 angekreuzt (Wirksamkeit offen) | Headline neutral, "8 Dokumente benannt" | "gut vorbereitet"; gegenüberliegende Richtung (nichts) korrekt | False-Beruhigung MAX — Asymmetrie verkehrt: gefährliche Richtung ungeschützt |

### Auslösende Kern-Linsen
- **L1 Bezugsgröße** (primär): Frage misst "Existenz eines gleichnamigen Dokuments", Antwort behauptet "ausreichend vorgesorgt"
- **L4 Anspruch vs. Datenbasis** (primär): Headline-Anspruch (Bereitschaft) übersteigt reine Selbstauskunft
- **L5 Fehler-Asymmetrie**: kein Schutz gegen False-"fertig"; Disclaimer muted/generisch, kontert die Headline nicht
- **L6 Verbotene Wertung** (sek.): "alle wichtigen Dokumente / gut vorbereitet" ist Wirksamkeitsurteil
- **L3 Erhebungs-Bias** (sek.): Sublabel "Mit Partner zusammen" unter verheiratet/verpartnert verschiebt nichteheliche Paare in falsche Kategorie

### Fix-Richtung
1. Headline von `missing.length` entkoppeln. Reframe → "Du hast N von M Dokumenten benannt — angekreuzt heißt nicht rechtswirksam."
2. Pro angekreuztem Doc statt grünem Haken einen Wirksamkeits-Selbstcheck (PV: konkret/aktuell/unterschrieben? Testament: § 2247 BGB? Vollmacht: über den Tod hinaus / im Vorsorgeregister?)
3. Spezifischer Vorbehalt VOR der Headline statt generischem Footer-Disclaimer
4. Taxonomie erweitern: "unverheiratet zusammenlebend", "Wohnsitz/Vermögen im Ausland"
5. "Keines davon" entweder implementieren oder Tipp Z. 112 streichen

---

## 2. Kostenrechner (`tools/kostenrechner/`) — DRINGLICHKEIT 2

### Verdict: `VALIDITY_FAIL`

Formel: `min/max = round((BASIS x REGION x AUSSTATTUNG + TRAUERFEIER + GRABSTEIN) / 100) x 100`
- BASIS: erd 3500–5500 · feuer 2000–3500 · see 1500–3000 · baum 2000–3500 · anonym 800–1500
- REGION 0,8/1,0/1,3 · AUSSTATTUNG 0,7/1,0/1,4 · TRAUERFEIER 0/500/1200/2500 · GRABSTEIN 0/800/2000/4000
- Kein Floor-Clamp. See/Baum/anonym überspringen Grabstein-Step.

**Kern-Bruch:** Ergebnis-Karte deklariert "Gesamtkosten — was die Familie am Ende wirklich zahlt"; 5-Ebenen-Erklärung listet Friedhofsgebühren als eigene Ebene mit "regional 300–400 %". Im Code: kein Friedhofsgebühren-Term, kein Friedhofs-Input. Regionsfaktor ±30 % kann die 300–400-%-Spreizung strukturell nicht tragen.

| # | Szenario | Inputs | Erwartet | Tatsächlich | Schaden |
|---|---|---|---|---|---|
| a | Mehrdeutiger Input: was zählt rein? | Erd / Mittelstadt / Standard / mittl. Feier / Grabstein Standard | 8.000–12.000 €+ ODER "OHNE Friedhofsgebühr" ausweisen | 6.700–8.700 €, deklariert als "wirklich zahlt" | False-Beruhigung |
| b | Sonderfall: See + Region als Kategoriefehler | See / einfach / keine Feier | Region für See/Baum/anonym inert | Region schwankt Ergebnis um ~75 % allein | beidseitig falsch |
| c | Grenzwert: günstigste Kombi, kein Floor | Anonym / Land / einfach / keine Feier | >=1.200–2.500 € | 400–800 € | False-Beruhigung im sensibelsten Fall |

### Fix-Richtung (minimal-invasiv)
1. **Anspruch ehrlich kappen**: Hero-Label umstellen, Friedhofsgebühr explizit ausweisen
2. **Region für See/Baum/anonym auf 1,0 fixen** (oder Region-Step überspringen)
3. **Floor-Clamp**

---

## 3. Bestattungskosten-Rechner (`tools/bestattungskosten-rechner/`) — DRINGLICHKEIT 3

### Verdict: `VALIDITY_FAIL`

Posten-interne Logik ist sauber. FAIL hängt an der **statischen Vergleichsbox** und an **stillen Default-Annahmen**.

| # | Szenario | Inputs | Erwartet | Tatsächlich | Schaden |
|---|---|---|---|---|---|
| a | Default-Durchklick | Feuer + NRW, keine Extra-Checkbox | klare Anzeige der Defaults | 3.968–10.191 €; Grabpflege + Friedhof 10 J. automatisch | gemischt |
| b | Seebestattung + Sarg-Multiplier | See / MV / Sarg "hochwertig" | Sarg-Feld ausblenden/neutralisieren | Sarg x1,4 -> 546–1.638 € | False-Alarm |
| c | Grenzwert günstig vs. statische Vergleichsbox | anonym / Sachsen-Anhalt | günstiges, plausibles Ergebnis | 1.404–2.613 € + fix "Durchschnitt 6.000–8.000 €" | False-Alarm / verbotene Wertung |

### Fix-Richtung
1. **Vergleichsbox dynamisch/kontextualisiert**
2. **Default-Annahmen sichtbar machen**

---

## Methodische Notizen

- Reviewer haben gegen exakte Code-Schwellen gerechnet (raw.githubusercontent.com)
- **Kein Score-Anchoring**: Prompts ohne Vorbefund; alle 3 unabhängigen Reviewer kamen zu konsistenter Pathologie-Klasse
- **Konsistenz mit Angebotsprüfer-FAIL**: 4/4 Trust-relevanten Tools haben strukturell dieselbe Lücke — die Erhebung erfasst weniger als der Output behauptet
