# Session-Notizen

## Letzte Session
**Datum:** 2026-06-01

## Was wurde gemacht

### Iter-32: SEO-Welle (alle 4 Pillars ≥85 BEHALTEN) — siehe Vorgänger-Notes

### Iter-33: KI-Helper Master-Architektur (Phase 1 + 1.5 + 1.6 + 2)

#### Phase 1 (initial Deploy)
**Problem-Diagnose**: Trauerrede-Generator war Template-Slot-Filler, übernahm User-Tippfehler 1:1. Helper-V3-Audit (SEO/YMYL) hatte Tool-Validity nicht geprüft → 85+ Score trotz unbrauchbarem Output.

**Lösung**: Groq + Llama 3.3 70B via Netlify Function. Free-API (14.400 req/Tag), 2-5s Latenz, deutsche Qualität sehr gut.

**Master-Stack (wiederverwendbar für Danksagung + Abschiedsbrief):**
- `netlify/functions/ai-rede.js`: Backend-Proxy, type-basiert (trauerrede/danksagung/abschiedsbrief)
- `assets/js/mr-ai.js`: Frontend-Helper mit Consent-Mgmt
- Trauerrede-Tool: Lesemodus + KI-Button + Consent-Modal

#### Phase 1.5 (Section-Regenerate)
- 7 Section-Buttons "🔄 Diesen Abschnitt mit KI neu" (opening/character/hobbies/memory/meaning/reflection/closing)
- Backend: section-Parameter mit spezifischen System-Prompts, max_tokens 500
- Verbesserter Haupt-Prompt: Few-Shot-Beispiel (Tomaten-Garten), Anti-Floskel-Liste

#### Phase 1.6 (Style-Picker + 7 Tonarten)
- 4 neue Stile: melancholisch, hoffnungsvoll, poetisch + bestehende (persönlich, würdevoll, lebensbejahend, humorvoll)
- Style-Pills im Output-Bereich (ohne zurück zum Wizard)
- Child-Guard: humorvoll bei Kindern/Jugendlichen disabled
- Hinweis-Box ehrlich umformuliert (KI-Variante erklärt)

#### Phase 2 (Hotfixes nach Doppel-Audit)
**Helper-V3-Doppel-Audit der Live-Site** ergab:
- SEO-Audit: **68/100** (mit Verifizierbarkeits-Abschlag — Reviewer sah nur Static Shell)
- Tool-Validity-Audit (neu, parallel): **83/100** (knapp drunter)

**3 Hotfixes deployed (SHA 597468b):**
1. **🔒 Security**: CORS-Wildcard `*` → strikte Allowlist (machsruhig.de + www + Netlify-Preview-Regex). Verhindert dass fremde Sites GROQ_API_KEY als Gratis-Llama-Relay missbrauchen.
2. **🔧 KI-Integration**: lebensbejahend-Tone war Frontend-Liste aber NICHT im Backend-System-Prompt → vollständige Tone-Beschreibung ergänzt
3. **📝 SEO**: Meta-Description war abgeschnitten ("…im Browser, ohne.") → vollständig mit KI-Helfer + 7 Tonarten

### NEUE Memory-Erkenntnis (Iter-33 Strukturell)

**Helper-V3-SEO-Audit misst nur die Hülle, NICHT die Tool-Substanz.**
→ Pflicht-Doppel-Audit bei allen Tool-Sessions (siehe Memory `tool_validity_audit.md`):
- Tab 1: SEO-Standard (6 YMYL-Linsen)
- Tab 2: Tool-Validity (5 Tool-Linsen: Konzept-Klarheit, UX-Flow, Privacy & Trust, KI-/Backend-Code-Qualität, Accessibility)

Tool-Validity-Reviewer fand 2 echte Defekte die SEO-Reviewer übersehen hatte (CORS-Wildcard + Frontend-Backend-Lücke).

### Deploy
- **Phase 1** main SHA d308632 — KI-Button + Lesemodus
- **Phase 1.5+1.6** main SHA 5f7616a — Section-Regen + 7 Tonarten + Style-Picker
- **Phase 2 Hotfixes** main SHA 597468b — CORS + lebensbejahend + Meta-Description
- **ENV**: GROQ_API_KEY in Netlify-Site-Settings (Bolle hat eingetragen)

## Tool-Klassifikation (Iter-33 Analyse aller 11 Tools)

| Tool | Typ | KI-Bedarf | Status |
|------|-----|-----------|--------|
| trauerrede | Generator | ✅ JA | **DEPLOYED Iter-33** |
| danksagung | Generator | ✅ JA | Phase 2 (Master-Pattern wiederverwendbar) |
| abschiedsbrief | Editor (User schreibt) | optional | Phase 3 (Polish-Button) |
| beerdigungsplaner, bestattungskosten-rechner, kostenrechner, fristen-radar, notfallkarte, checkliste-todesfall, angebotspruefer, vorsorge-check | Rechner/Quiz/Formular | nein | ✓ OK |

## Nächste Schritte

- **Phase 3 Trauerrede Re-Audit** (optional): 2-Tab-Audit nach Hotfix-Deploy verifizieren — Tool-Validity sollte 85+ erreichen
- **Phase 2 Danksagung**: gleicher Stack, ~1h Aufwand
- **Phase 3 Abschiedsbrief**: Polish-Button, ~30 Min
- **Cool-Down**: 4 Iter-Phasen + 5 Iterations-Cycles + Doppel-Audit + Hotfixes in dieser Session

## Strukturelle Erkenntnisse Iter-1–33 dieser Sessions-Reihe
- Reviewer-Noise ±5-10 Punkte → Median über 3-5 Cycles ist echter Schätzwert
- Strukturelle Defekte (Babel-Self-Host, YMYL-Faktenfehler, Footer-Missing, unstyled-CSS) bringen +5-15 Punkte
- Helper-V3 Multi-Tab-Pipeline mit Branch-Trick ist robuster als Single-Audit-Loop
- raw.githubusercontent.com Edge-Cache verfälscht Audits — Live-File-Verification + Cache-Bust-Branches als Standard
- **NEU Iter-33**: Helper-V3-SEO-Audit misst Hülle, NICHT Tool-Output-Qualität. Tools brauchen Doppel-Audit (SEO + Tool-Validity).
- **NEU Iter-33**: Bei CSR-Tools (React-Hybrid) kann SEO-Reviewer den Wizard nicht sehen → konservativer Score. Tool-Validity-Reviewer darf Repo-Code direkt ziehen.
