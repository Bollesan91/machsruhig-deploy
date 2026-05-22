"""
NRW §-Verifikation Fixes (deterministic):

Bielefeld: § 14 BestG NRW für sarglose Bestattung ist falsch.
  § 14 BestG NRW = Friedhofszwang, nicht Sarg-Regelung.
  Sarg-/Tuchbestattung ergibt sich aus Friedhofssatzung (§ 4 als Satzungsermächtigung).

Muelheim: "§ 14 und § 15 BestG NRW" für Aschen-Verstreuung präziser machen.
  Verstreuen der Asche steht konkret in § 15 Abs. 6 BestG NRW.
"""
import os
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"


def fix_bielefeld():
    p = BESTATTER / "bielefeld" / "index.html"
    text = p.read_text(encoding="utf-8", errors="replace")
    orig = text

    # FAQ-Schema (JSON-LD)
    text = text.replace(
        "Eine sarglose Bestattung nach religiöser Überzeugung ist nach § 14 BestG NRW im Ausnahmefall möglich",
        "Eine sarglose Bestattung nach religiöser Überzeugung ist nach der Friedhofssatzung der Stadt Bielefeld auf Antrag möglich (Satzungsermächtigung § 4 BestG NRW)",
    )
    # Fließtext-Variante
    text = text.replace(
        "Eine sarglose Bestattung aus religiösen Gründen ist nach <strong>§ 14 BestG NRW</strong> im Ausnahmefall möglich, wenn die Friedhofsverwaltung zustimmt",
        "Eine sarglose Bestattung aus religiösen Gründen ist nach der Friedhofssatzung der Stadt Bielefeld (Satzungsermächtigung § 4 BestG NRW) auf Antrag möglich, wenn die Friedhofsverwaltung zustimmt",
    )

    if text != orig:
        p.write_text(text, encoding="utf-8")
        return "patched"
    return "no-change"


def fix_muelheim():
    p = BESTATTER / "muelheim" / "index.html"
    text = p.read_text(encoding="utf-8", errors="replace")
    orig = text

    # Beide Stellen (FAQ-Schema + Fließtext) sagen "Nach § 14 und § 15 BestG NRW"
    text = text.replace(
        "Nach § 14 und § 15 BestG NRW ist die Verstreuung der Asche grundsätzlich an dafür ausgewiesenen Orten zulässig",
        "Nach § 15 Abs. 6 BestG NRW ist die Verstreuung der Asche an dafür ausgewiesenen Orten zulässig; auf Friedhöfen gilt grundsätzlich der Friedhofszwang (§ 14 BestG NRW)",
    )

    if text != orig:
        p.write_text(text, encoding="utf-8")
        return "patched"
    return "no-change"


for name, fn in [("bielefeld", fix_bielefeld), ("muelheim", fix_muelheim)]:
    print(f"  {name}: {fn()}")
