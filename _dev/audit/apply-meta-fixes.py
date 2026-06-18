# -*- coding: utf-8 -*-
"""Kuerzt zu lange meta-description (<=160). Nur Laenge getrimmt, keine neuen
Sachaussagen; §§ bei fristen wortgleich erhalten. Presse-Seite nicht enthalten."""
import re
from pathlib import Path
ROOT = Path(".")

METAS = {
 "abschiedsbrief-schreiben.html": "Abschiedsbrief schreiben — ehrlicher Leitfaden: Was gehört hinein, wann der richtige Zeitpunkt, an wen, wo sicher aufbewahren? Mit drei echten Vorlagen.",
 "bestatter-angebot-pruefen.html": "Bestatter-Angebot prüfen: Welche Posten gehören rein, welche Pauschalen schwer vergleichbar sind, wann ein zweites Angebot lohnt. Kostenlos in 3 Minuten.",
 "danksagung-nach-beerdigung.html": "Danksagung nach Beerdigung schreiben: Was gehört hinein, wann verschicken, wer bekommt eine? Aufbau, Formate und ein kostenloser Generator im Browser.",
 "fristen-nach-todesfall.html": "Fristen nach Todesfall: Standesamt (§ 28 PStG), Erbausschlagung (§ 1944 BGB), Erbschaftsteuer (§ 30 ErbStG), Mietvertrag. Mit Timelines und Fristen-Radar.",
 "fuer-bestatter.html": "machsruhig.de sucht in ausgewählten Städten Bestatter als Pilotpartner für unverbindliche, qualifizierte Anfragen — redaktionelles Portal, kein Lead-Portal.",
 "kindern-tod-erklaeren.html": "Wie erkläre ich meinem Kind den Tod? Gesprächsleitfaden nach Alter (3–5, 6–9, 10–13, 14+): konkrete Formulierungen, häufige Fehler, wann Hilfe sinnvoll ist.",
 "kondolenzschreiben.html": "Wie schreibe ich ein Kondolenzschreiben? Anleitung Schritt für Schritt: Struktur, Dos und Don'ts, Vorlagen für viele Situationen. Respektvoll und einfach.",
 "notfallkarte.html": "Notfallkarte erstellen Schritt für Schritt: Welche Felder draufgehören, wie sie das NFDM der eGK ergänzt, Layouts für Kranke, Senioren & Reisende. Kostenlos.",
 "trauerrede-schreiben.html": "Trauerrede schreiben Schritt für Schritt: Aufbau, Tipps, Beispiele für Vater, Mutter, Oma, Opa. Plus kostenloser Generator — komplett in deinem Browser.",
 "trauersprueche.html": "Über 200 Trauersprüche: tröstliche Sprüche, Bibelverse und Zitate für Trauerkarten, Grabsteine und Reden. Überwiegend gemeinfrei, authentisch und kostenlos.",
 "was-tun-nach-todesfall.html": "Was tun nach Todesfall? Die ersten Schritte Stunde für Stunde: Arzt, Bestatter, Sterbeurkunde, Versicherungen, Erbe. Mit kostenloser Checkliste.",
 "tools/bestattungskosten-rechner/index.html": "Kostenloser Bestattungskosten-Rechner: realistische Kosten in wenigen Schritten — nach Bestattungsart, Region und Extras. Ohne Anmeldung, 100% privat.",
 "tools/trauerrede/index.html": "Trauerrede schreiben leicht gemacht: Schritt-für-Schritt-Assistent mit Vorlagen, Zitatbibliothek und optionalem KI-Helfer für 7 Tonarten. Kostenlos im Browser.",
 "vorsorge/testament/index.html": "Testament einfach erklärt: handschriftlich & notariell, Anforderungen, Berliner Testament, Pflichtteil, häufige Fehler. Kostenlos informiert zur Vorsorge.",
 "bestatter/frankfurt/index.html": "Hauptfriedhof Frankfurt (Schopenhauer, Adorno), Alter Jüdischer Friedhof Battonnstraße, Hessen-Recht nach Novelle 2025, Kosten und Bestatter-Wahl.",
}

changed, warn, skip = 0, [], []
for rel, new in METAS.items():
    f = ROOT / rel
    if not f.exists(): skip.append(rel); continue
    if len(new) > 160: warn.append((rel, len(new)))
    t = f.read_text(encoding="utf-8")
    pat = r'(<meta[^>]*name="description"[^>]*content=")[^"]*(")'
    nt, n = re.subn(pat, lambda m: m.group(1) + new + m.group(2), t, count=1, flags=re.I)
    if n == 1 and nt != t: f.write_text(nt, encoding="utf-8"); changed += 1
    elif n == 0: skip.append(rel + " (kein meta-desc)")

print(f"Metas gesetzt: {changed} | übersprungen: {len(skip)} | >160: {len(warn)}")
for r, l in warn: print(f"  WARN >160 ({l}): {r}")
for s in skip: print(f"  SKIP: {s}")
print("\nLängen (Kontrolle):")
for rel, new in sorted(METAS.items(), key=lambda x: -len(x[1])):
    print(f"  {len(new):>3}  {rel}")
