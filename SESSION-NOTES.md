# Session-Notizen

## Letzte Session
**Datum:** 27. Mai 2026 (Morgen — Stadt-Polish-Welle Top 5 + Konsistenz-Sweep + Deploy)

## Was wurde gemacht
- **Stadt-Polish-Welle Top 5 (4 Städte, 5. Frankfurt offen):** Helper-V3 Writer parallel auf 2 Tabs pro Welle (Branch-Trick via Artifact-Download + Blob-Download). Constraint: KEINE Recherche-Neu-Welle, nur UI-Re-Arrangement.
  - **Welle 1 (Commit 2621e85):** Berlin (+18k: Bezirks-Matrix 12 Standesämter, Träger-Tabelle 85/118/9/10=222, FAQ-Drift-Lesson respektiert — bestehender FAQ-Accordion unangetastet) + Hamburg (+11k: mr-contact-card Hamburger Friedhöfe AöR Fuhlsbüttler Str. 756, Gebühren-Mini-Tabelle aus Bestandscontent, Standesamt-Sammellink 7 Bezirke).
  - **Welle 2 (Commit 8d20e14):** München (+20k: Akutbox unter H1 mit 3 Sofort-Schritten, mr-contact-card FBM Damenstiftstr. 8 +49 89 23199 01, Quellenblock-Straffung Primärquellen-first) + Köln (+14k: FAQ-Block als sichtbarer HTML-Accordion JSON-LD ≡ HTML wortgleich, Gebührenlink stadt-koeln.de prominent, Inline-Hinweis 'persönliche Vorsprache meist nicht nötig').
- **Helper-V3-Validation per WebFetch (Bolle-Quota-Warnung war Threshold, kleine Outputs gingen durch — User-Korrektur 'Kann nicht sein' bestätigt):**
  - Berlin Polish 6/6 PASS · Hamburg Polish 8/8 PASS · München Polish 8/8 PASS · Köln Polish 9/9 PASS
- **End-Check Konsistenz-Sweep (Commit 3080c37 + 9e5e76d):**
  - JSON-LD-Description Du-Form (Berlin + Hamburg): 'Vergleichen und finden Sie' → 'Finde'
  - Berlin id=akut-todesfall → akutbox-berlin (Pattern-Naming einheitlich Hamburg/München/Köln)
  - Köln id=akutbox-koeln + mr-contact-card Standesamt+Friedhofsamt + Träger-Übersicht-Tabelle (55 städt + 7 konfess + 2 muslimische Grabfelder)
- **Konsistenz-Bilanz alle 4 Stadt-Pages:** H1-Format, akutbox-id, Träger-Info, Robots/Canonical, FAQ-Drift, Du-Anrede, § 74 SGB XII durchgängig OK. Berlin's mr-contact-card 'fehlt' bewusst (12 Bezirks-Standesämter = strukturell andere Verwaltungs-Lösung, Bezirks-Matrix erfüllt Pattern-Funktion).
- **Deploy:** main aus content-loop-pipeline gemerged + Netlify-Build.

## Nächste Schritte (priorisiert)

**Phase A — Stadt-Polish-Welle abschließen:**
1. **Frankfurt** (~3h) — letzte der Top-5 aus Reviews: Trustbox + Akutfall-Box + Verwaltungs-Kontakt Adam-Riese-Str. 25 / Tel 069 212 36480 / Gebührenordnung gültig ab 01.01.2025. Helper-V3 Writer + WebFetch-Validation.

**Phase B — strukturelle Trust-Verdichtung (nach Frankfurt):**
2. Trustbox-Komponente auf allen 48 Stadt-Pages (Autor + Stand + Quellen + Vermittlungs-Disclosure) als wiederverwendbares Pattern
3. Lead-Form-Disclosure-Block einheitlich auf allen 48 Stadt-Pages (analog Standard aus Review 2: Wenn Beauftragung → Vermittlungsvergütung, Auswahl provisionsunabhängig)
4. Schema-Audit: WebPage + Article + BreadcrumbList + FAQPage statt LocalBusiness (machsruhig ist kein Bestattungsunternehmen)
5. Akutfall-Hero-Umbau auf Homepage — dreistufiger Einstieg (Akutfall / Planung / Vorsorge), Soforthilfe in Hero-Section

**Phase C — Stadt-Pages-Welle 2 (nach Phase A+B):**
6. Berlin '116 vs 118 evangelische Friedhöfe' interne Inkonsistenz auflösen (Fact-Check gegen liste_friedhoefe.pdf der Stadt Berlin)
7. weitere Stadt-Pages systematisch durch Polish-Pattern (Akutbox + mr-contact-card + Träger-Tabelle wo sinnvoll)

**Hinter dem Messgate (wenn machsleicht-Indexierung rankt):**
8. Externer Reviewer-Pool real aufbauen (Bestattungsfachkraft / Jurist / Trauerbegleitung) — heute mit Bremen-Fake-Label-Entfernung schon Trust-Schritt gemacht
9. Lead-Funnel + Einwilligung sauber (12–30h)
10. Welle E (Tier-Bestattung, Auswanderer, Patchwork-Familie)

## Offene Fragen
- Keine akuten. Stadt-Polish 4/5 deployed mit konsistentem Pattern; Frankfurt als nächste Welle vorgemerkt.

---

# ───────── ARCHIV: frühere Sessions ─────────

# ───────── ARCHIV: frühere Sessions ─────────

## Session
**Datum:** 26. Mai 2026 (Abend — Angebotsprüfer-Rebuild v2.4 + ASCII-Canonical-Fix LIVE)

## Was wurde gemacht
- **Angebotsprüfer v2.4 LIVE, Validity-PASS:** Internes VALIDITY_FAIL (3/3) durch unabhängigen Helper-V3-Audit (frischer Chrome-Tab gegen Live-URL) bestätigt → 5 Iterationen Rebuild (v2 → v2.4-Polish). v2.4 hat im finalen Fresh-Tab-Audit (Tab 1532777164) bestanden. Kern-Änderungen: SEPARAT_KOSTEN-Logik (Friedhofsgebühren raus aus Range), INFO_POSTEN-Konstante (Grabstein/Grabpflege ohne Range-Abzug), pflicht-Flag aktiviert, Pauschale nicht abgestraft, ROT nur bei kumuliertem Risiko (sumRatio<0.3 AND klärungsRatio>=0.7 AND !userHasExplained), High-Side-ROT bei >=2x, YMYL-Wording ("Lockangebot" raus → neutrale Klärungs-Sprache).
- **P0-Versicherung während Rebuild:** Tool noindex + 16 CTAs (8 Seiten × 2) neutralisiert während v2-Bauphase, nach v2.3-Pass sauberer Rollback.
- **ASCII-Canonical-Fix:** `bestatter/luebeck/` + `bestatter/moenchengladbach/` ASCII-Stubs zeigen jetzt percent-encoded canonical auf Umlaut-Hauptversion (`l%C3%BCbeck` / `m%C3%B6nchengladbach`). Commit `123bb90`.
- **Cluster × v2.4 Konsistenz-Sweep + Page-5-Body-Rewrite + Welle C Sozialbestattung + Welle D Vorsorge-allein-leben** — siehe Git-History für Details.

---

# ───────── (Ältere Archive gekürzt — siehe Git-History) ─────────
