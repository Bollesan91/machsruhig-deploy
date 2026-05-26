# Session-Notizen

## Letzte Session
**Datum:** 26. Mai 2026 (Abend — Angebotsprüfer-Rebuild v2.4 + ASCII-Canonical-Fix LIVE)

## Was wurde gemacht
- **Angebotsprüfer v2.4 LIVE, Validity-PASS:** Internes VALIDITY_FAIL (3/3) durch unabhängigen Helper-V3-Audit (frischer Chrome-Tab gegen Live-URL) bestätigt → 5 Iterationen Rebuild (v2 → v2.4-Polish). v2.4 hat im finalen Fresh-Tab-Audit (Tab 1532777164) bestanden. Kern-Änderungen: SEPARAT_KOSTEN-Logik (Friedhofsgebühren raus aus Range), INFO_POSTEN-Konstante (Grabstein/Grabpflege ohne Range-Abzug), pflicht-Flag aktiviert, Pauschale nicht abgestraft, ROT nur bei kumuliertem Risiko (sumRatio<0.3 AND klärungsRatio>=0.7 AND !userHasExplained), High-Side-ROT bei >=2x, YMYL-Wording ("Lockangebot" raus → neutrale Klärungs-Sprache).
- **P0-Versicherung während Rebuild:** Tool noindex + 16 CTAs (8 Seiten × 2) neutralisiert während v2-Bauphase, nach v2.3-Pass sauberer Rollback.
- **ASCII-Canonical-Fix:** `bestatter/luebeck/` + `bestatter/moenchengladbach/` ASCII-Stubs zeigen jetzt percent-encoded canonical auf Umlaut-Hauptversion (`l%C3%BCbeck` / `m%C3%B6nchengladbach`). Commit `123bb90`.
- **Cluster × v2.4 Konsistenz-Sweep (Helper-V3 Outcome-Validity-Audit):** Reviewer fand 0/8 PASS — alle 8 Cluster-Pages versprachen v1-Tool-Verhalten. 3-Pass-Sweep deployed (`2e77b43`, `01a2ab2`): "Lockangebot"/"Pflicht-Posten"/"vermisste Posten"/"18 Posten"/"10 Fragen"/Friedhof-Red-Flag-Logik konsistent auf v2.4-Wording angeglichen (Klärungspunkte / Kern-Posten / 9–18 / "auffällig niedrig statt Lockangebot"). Plus Seebestattung-Selbstwiderspruch (Intro: "keine Friedhofsgebühren" vs Template-Sektionen mit Friedhof-Bullets) durch See-Pendants ersetzt (Reederei, Begleitfahrt, seetaugliche Urne). Plus Tool-meta-description und Page-1-OG/Article angeglichen. Re-Audit → 2 PASS / 4 TUNE / 1 RE-OPEN, alle Findings gefixt + Final-Verify PASS.
- **Page 5 (`bestatter-rechnung-pruefen`) Body-Rewrite (`2912895` + YMYL-Rollback `9304188`):** Page hatte H1 "Bestatter-Rechnung prüfen" und 90 % Vor-Unterschrift-Body. Neuer Body: TRIAGE (Festpreis vs KV vs kein Angebot), Schritt-für-Schritt-Abgleich, Fremdleistungen/durchlaufende Posten (mit MwSt-Heuristik: Sarg/Urne 19 %, Friedhofsgebühren USt-frei, Floristik 7 %/19 %), Rote Flaggen IN DER RECHNUNG, Was-tun-bei-zu-hoher-Rechnung. FAQ-Erweiterung (HTML + JSON-LD wortgleich): § 649 Abs. 2 BGB Anzeigepflicht, § 280 BGB Schadensersatz-Hebel (konjunktivisch), § 632 BGB ortsüblicher Preis bei fehlendem Angebot, § 195 BGB Verjährung (keine Reklamationsfrist-Hallu). Final WebFetch-Verify: Section-Reihenfolge sauber, 6 §-Refs korrekt.
- **Welle C: Sozialbestattung Pillar LIVE (`9d2e2ff`) — Live-Rescore 87%:** Neue Pillar `/sozialbestattung` (~3000 W, § 74 SGB XII) durch komplette V2-Multi-Chat-Pipeline gebaut. 5 Phasen: Quellen-Pack → v1 Writer (Branch-Trick + Blob-Download) → v1 Score (5/5 PASS, 3 TUNES) → v2 Fix → v2 Adversarial (MIT-CAVEAT ~80%) → v3 Final-Fix → main-Deploy + Sitemap. Page enthält: TRIAGE-Anspruchsreihenfolge (Erben/Bestattungspflichtige/Sozialamt), Zumutbarkeit, Schonvermögen (VG Münster 10.500 €), erforderliche Kosten "einfach/würdig/ortsüblich" (KEINE Pauschal-Begrenzung), Antrag (Sterbeort, nachträglich), Sozial- vs Ordnungsamt, Mythen, BSG-Az. 12.12.2023 B 8 SO 20/22 R, § 1944 BGB 6-Wochen-Frist, § 199 BGB Verjährungsbeginn, Widerspruchspfad. 10 FAQ JSON-LD ≡ HTML-Accordion (verifiziert via Python-Diff). Nachträglicher Live-Rescore (`c1b2b69`): 84% reviewer-stated → 87% nach JSON-LD-Parität-Verify (Python). Soft-Polish offen: BSG-Az + VG-Münster-Az in Quellenliste.
- **Welle D: Vorsorge-allein-leben Pillar LIVE (`6db1d06`) — Score 79→84→~88%:** Neue Pillar `/vorsorge-allein-leben` (~3500 W, 11 §§) für Alleinstehende 50+/60+ ohne nahe Familie. Komplette V2-Pipeline (Quellen-Pack 55557d4 → v1 0b29ea9 → v1-Review 79% → v2 b63811a → v2-Adversarial 84% MIT-CAVEAT → v3 0b0c73b → Deploy 6db1d06). Page-Inhalt: Vorsorgevollmacht, Betreuungsverfügung (mit Berufsbetreuer-Weg über örtliche Betreuungsbehörde + VBVG-Stundensätze), Patientenverfügung (§ 1827 BGB + BGH XII ZB 61/16 Unwirksamkeit), Erbordnungen 1-4+ (§§ 1924-1926, 1928, 1931, 1936 BGB), Testament (§ 2247 BGB Soll-Char, § 2303 BGB Pflichtteil, Zentrales Testamentsregister + amtliche Verwahrung), Bestattungsverfügung, Bestattungsvorsorgevertrag, Sterbegeldversicherung, Notfallmappe + Mythen-Block. 10 FAQ JSON-LD ≡ HTML.
- **Pipeline-Lessons Welle D:** (i) Message-Length-Limit bei ~43k chars → "Weiter"-Button + Duplicate-Cleanup-Regex bei Continuation-Word-Repetition. (ii) Artifact-Browser-Cache-Issue: Download-Button liefert OLD-File trotz neuem Artifact → Re-Output als Code-Block via Follow-up-Request fixt es. (iii) DOM-Virtualisierung bei langen Chats: scrollTop=0 + Wait erzwingt Render von alten <pre>-Elementen.
- **Methodik-Lessons:** (a) Erster Helper-V3-Lauf nutzte fälschlich denselben Tab für iteratives Review → Sycophancy-Risiko. Korrektur: pro Iteration frischer Tab. (b) **YMYL-§-Lesson**: Plan-Reviewer hatte WebSearch gemacht und behauptet, § 650 BGB sei der Kostenanschlag-Paragraph. Re-Audit-Reviewer korrigierte zu § 649 BGB — dejure.org/gesetze-im-internet.de bestätigte: § 649 BGB n.F. = Kostenanschlag, § 650 BGB = Werklieferungsvertrag, § 648 BGB = freie Kündigung (was historisch § 649 a.F. war). Bei §-Aussagen IMMER selbst gegen Primärquelle prüfen, auch wenn Reviewer behauptet, verifiziert zu haben. (c) **HTML-Transport-Lesson**: Cookie/QS-Filter blockiert `pre.innerText.slice()` willkürlich auf großen HTMLs. Lösung: Blob + `<a download>` Click → File via ~/Downloads → cp ins Repo. Branch-Trick (raw-URL auf `content-loop-pipeline`) ist der Pipeline-Backbone. Beides jetzt in `_dev/HELPER-V3.md` Sektion "HTML-Transport" dokumentiert (commit `5ad0e20`).

## Nächste Schritte (priorisiert, Messgate-Logik)
**Soft-Polish (klein, schnell):**
1. Sozialbestattung: BSG-Az (B 8 SO 20/22 R, B 8 SO 20/10 R) + VG-Münster-Az in Quellenliste verlinken (~10 Min).
2. Vorsorge-allein-leben: VG-Münster-Az + BSG-Az im Body als Trust-Anker prüfen.

**Hinter dem Messgate (erst wenn machsleicht-Indexierung beweist, dass Content rankt):**
3. Lead-Funnel + Einwilligung sauber (12–30h).
4. Autoren-/Redaktionsprofil + Trust (8–20h).
5. Welle E (Tier-Bestattung, Auswanderer, Patchwork-Familie) aus 90-Tage-Roadmap.

## Offene Fragen
- Keine akuten. Trust-Risiko Angebotsprüfer entschärft, Cluster-Konsistenz hergestellt, Page-5-Body-Intent gelöst inkl. YMYL-§-Korrektur, Welle C Sozialbestattung-Pillar live, SEO-Hygiene-Mini-Rest erledigt.

---

# ───────── ARCHIV: frühere Sessions ─────────

## Session
**Datum:** 26. Mai 2026 (Vormittag — Repo-Reality-Check gegen externes Marktreife-Beraterpapier — Doppelsession ruhig+leicht, NUR Analyse, kein Code/Content geändert)

## Was wurde gemacht
Externes Beraterpapier ("Aufwand bis Marktreife, 260–480h") gegen den echten Repo-Stand geprüft (frischer Clone, Dateien einzeln gelesen, kein Pauschalurteil). Kernergebnis: **Das Papier ist featurelastig und unterschätzt den Ist-Stand massiv. machsruhig hat KEIN Contentproblem — es hat ein Trust-Tool-Problem und ein SEO-Hygiene-Detail.**

Verifizierte Befunde machsruhig:
- **Stadtseiten faktisch fertig:** 52 Seiten unter `bestatter/`, davon 50 mit 4.500–7.000 Wörtern (Friedhöfe, Gebühren, Sozialbestattung, Quellenbox, Schema). Plus 16 Bundesland-Seiten (2.500–3.350 W). Berater-Schätzung "Top 5–10 Städte auf Gold: 35–70h" ist gegenstandslos.
- **Angebotsprüfer = akutes Trust-Risiko, NICHT "starker Kernhebel":** Tool ist LIVE, `<meta robots: index,follow>`, eigener Canonical, und von **8 Seiten per CTA verlinkt**. Trägt den dokumentierten VALIDITY_FAIL 3/3 (siehe `_dev/audit/angebotspruefer-validity-fail-2026-05-23.md`): schlägt seriöse Angebote ROT, Wording Richtung "Lockangebot". Risiko ist latent (≈0 Traffic), wird real sobald Distribution greift.
- **Doppel-Slug-FALSCHALARM aufgelöst:** `moenchengladbach`/`luebeck` sind bereits `noindex,follow` UND nicht in der Sitemap (98 saubere URLs). Bewusste Entscheidung lt. Inline-Kommentar ("noindex bis Gold-Template-Upgrade"). KEIN 4–12h-Task. Einziger Mini-Rest: ASCII-Stub-Canonical zeigt aktuell self (ASCII) — sollte auf die Umlaut-Version zeigen, ~10 Min.

## Nächste Schritte (priorisiert, Messgate-Logik)
**Pflicht VOR Traffic:**
1. **Angebotsprüfer-Versicherung (P0, ~20–30 Min):** Tool auf `noindex` + die 8 CTAs ziehen/neutralisieren — ODER schneller Wording-Defuse (2–6h): "Lockangebot" raus, Preis nie allein ROT, Pauschale nie allein ROT, Default GELB statt ROT, "Pflicht"→"Klären", Ergebnis von Urteil auf Rückfragen.

**HINTER dem Messgate (erst wenn machsleicht-Indexierung beweist, dass Content rankt — gemeinsamer Strategie-Anker beider Projekte):**
2. Angebotsprüfer-Logik sauber rebuilden (15–40h, über Content-Loop, asynchron): severity pro Posten (critical/medium/info), Preisabweichung nur Signal, Pauschale = "unklar" nicht Fehler, ROT nur bei kumuliertem Risiko, Regressionstest mit 5–10 echten Angeboten.
3. ASCII-Canonical-Fix (~10 Min).
4. Lead-Funnel + Einwilligung sauber (12–30h); Autoren-/Redaktionsprofil + Trust (8–20h).

## Offene Fragen
- Angebotsprüfer: harte Versicherung (noindex+CTA raus) ODER Wording-Defuse als Sofortschritt? (Empfehlung: noindex, billigste sichere Variante, Rebuild ohne Zeitdruck dahinter.)

---

# ───────── ARCHIV: frühere Sessions ─────────


## Letzte Session
**Datum:** 23. Mai 2026 (Helper-V3-Methodik-Erweiterung + erster Validity-Run)

## Was wurde gemacht
- **HELPER-V3.md erweitert** (_dev/HELPER-V3.md, 12,5 KB → 21,5 KB): Neue **Stufe 0 — Artefakt-Typ bestimmt den Review-Fokus** (5 Typen: Content-Page / Tool / Funnel / Posting / Strategie). Pro Nicht-Content-Typ eine Validity-Linse:
  - Tool → Outcome-Validity (Tool adversarial *bedienen*, 6 Kern-Fragen, 3 Fehl-Input-Durchläufe)
  - Funnel → Promise-Delivery + Dark-Pattern
  - Posting → Claim + Pietät/Brand + Plattform-Policy
  - Strategie → Prämissen-Audit + Pre-Mortem (gefährlichster Typ, Sycophancy-Risiko)
  - Prinzip: Validity-Linse ist Pflicht, Dispatch-Loop skaliert mit Aufwand. Anti-Score-Anchoring gilt überall.
- **Erster echter Validity-Run** über tools/angebotspruefer/ → **VALIDITY_FAIL (3/3)**. Befund dokumentiert in `_dev/audit/angebotspruefer-validity-fail-2026-05-23.md`.

## Nächste Schritte
- **Angebotsprüfer Writer-Pass** (Tool ist LIVE mit dem FAIL): Preis nie allein ROT (Vollständigkeit = Anker, Preis max. GELB); Summen-Bezugsgröße definieren; Posten-Check als Klärungs- statt Vollständigkeits-Audit; Pauschale nicht abstrafen. KEIN Stadt/Friedhof-Ausbau.
- Optional: Validity-Run in separatem Tab gegen Live-URL gegenchecken (wasserdichter Sycophancy-Schutz).
- HELPER-V3 "Adversarial-Fundtypen"-Sektion um Tool/Funnel/Posting/Strategie-Fälle ergänzen, sobald echte Fälle da sind.

## Offene Fragen
- Soll der Funnel-Conversion-Check ausformuliert werden (aktuell nur Linse skizziert)?
