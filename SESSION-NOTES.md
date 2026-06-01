# Session-Notizen

## Letzte Session
**Datum:** 2026-06-01

## Was wurde gemacht

### Iter-32: SEO-Welle (siehe Vorgänger-Notes — alle 4 Pillars ≥85 BEHALTEN)

### Iter-33: KI-Helper Master-Architektur (Phase 1: Trauerrede)

**Problem-Diagnose**: Trauerrede-Generator war Template-Slot-Filler, übernahm User-Tippfehler 1:1. Helper-V3-Audit (SEO/YMYL) hatte Tool-Validity nicht geprüft → 85+ Score trotz unbrauchbarer Output.

**Lösung**: Groq + Llama 3.3 70B via Netlify Function. Free-API (14.400 req/Tag), 2-5s Latenz, deutsche Qualität sehr gut.

**Master-Stack (wiederverwendbar für Danksagung + Abschiedsbrief):**
- `netlify/functions/ai-rede.js`: Backend-Proxy, type-basiert (`trauerrede`/`danksagung`/`abschiedsbrief`)
  - Rate-Limit per IP (10/min, 100/day)
  - Input-Size-Guard (8000 chars max)
  - Type-spezifische System-Prompts (Tonalität, Länge, Stil-Regeln)
- `assets/js/mr-ai.js`: Frontend-Helper
  - Consent-Mgmt via localStorage (`mr-ai-consent-v1`)
  - `window.mrAI.generate({type, data})` → Promise<text>
  - Loading/Success/Error Events

**Trauerrede-Tool (Master für Phase 2/3):**
- Lesemodus (Default): zusammenhängender `<article>` Fließtext (Fraunces 17px, line-height 1.85)
- Bearbeiten-Modus: original Section-by-Section Editor
- "✨ Mit KI verfeinern" Button → Consent-Modal → Groq-Call → KI-Result
- Copy/Print priorisiert KI-Result
- Reset löscht KI-Result + zurück zum Lesemodus

**Privacy-Modell**: Opt-in Pflicht (Modal mit Groq-Inc.-Hinweis "USA, kein KI-Training"), localStorage `mr-ai-consent-v1`. Fallback: KI-Fehler → User sieht Vorlage-Variante.

**ENV-Setup (in Netlify-Site-Settings):**
- `GROQ_API_KEY` als Secret-Variable, alle Scopes

**Strukturelle Erkenntnis Iter-33:**
- Helper-V3-YMYL-Audit misst SEO-Hülle, NICHT Tool-Output-Qualität
- Tools brauchen separaten "Validity-Audit" (Eingabe→Output mit Tippfehler-Test)
- LLM-API > Template-Slot-Filler bei jedem Content-Generation-Tool

## Nächste Schritte
- Phase 2: Danksagung-Tool (Score 86) mit gleichem Stack — ~1h Aufwand
- Phase 3 optional: Abschiedsbrief "✨ Mit KI polieren"-Button (Rechtschreibung/Stil)
- Post-Deploy-Live-Test Trauerrede-KI-Flow

## Tool-Klassifikation (aus Iter-33-Analyse)

| Tool | Typ | KI-Bedarf |
|------|-----|-----------|
| trauerrede | Generator | ✅ Phase 1 (DEPLOYED Iter-33) |
| danksagung | Generator | ✅ Phase 2 (Master-Pattern wiederverwendbar) |
| abschiedsbrief | Editor (User schreibt) | optional (Polish-Button) |
| beerdigungsplaner, bestattungskosten-rechner, kostenrechner, fristen-radar, notfallkarte, checkliste-todesfall, angebotspruefer, vorsorge-check | Rechner/Quiz/Formular | nein |

## Strukturelle Erkenntnisse Iter-1–33 dieser Sessions-Reihe
- Reviewer-Noise ±5-10 Punkte → Median über 3-5 Cycles ist echter Schätzwert
- Strukturelle Defekte (Babel-Self-Host, YMYL-Faktenfehler, Footer-Missing, unstyled-CSS) bringen +5-15 Punkte
- Helper-V3 Multi-Tab-Pipeline mit Branch-Trick ist robuster als Single-Audit-Loop
- raw.githubusercontent.com Edge-Cache verfälscht Audits — Live-File-Verification + Cache-Bust-Branches als Standard
- **NEU Iter-33**: Helper-V3-Audit misst SEO, nicht Tool-Output-Qualität. Tool-Validity braucht separaten Test.
