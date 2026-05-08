# Round 6 — Eskalation (in Chat A, Versuch 3)

---

Du hast jetzt drei Versuche gemacht. Die Tools sind immer noch nicht zufrieden:

**Aktuelle Tool-Ausgabe:**
```
[PASTE-CURRENT-TOOL-OUTPUT]
```

**Verlauf der letzten Scores:**
- Versuch 1 (nach Round 5): Audit NN, Recheck-Blocker M
- Versuch 2 (nach Tool-Fix 1): Audit NN, Recheck-Blocker M
- Versuch 3 (jetzt nach Tool-Fix 2): Audit NN, Recheck-Blocker M

---

**Stop. Bevor du noch einen Symptom-Fix versuchst:**

Was ist das **fundamentale Problem**, das du nicht löst? 

Oberflächliche Fixes haben nicht funktioniert. Das heißt: das Problem liegt **eine Ebene tiefer** als du es bisher angegangen bist.

**Schreib zuerst eine Diagnose** (nicht den Fix):

```
DIAGNOSE:
- Was ist die echte Ursache der wiederkehrenden Tool-Findings?
- Liegt es an fehlender Information (dann: was fehlt konkret?)
- Liegt es an Struktur (dann: welche Sektion muss anders aufgebaut werden?)
- Liegt es an meinem Verständnis des Audit-Scoring (dann: was misinterpretiere ich?)
```

**Danach** schreib die nächste Version, basierend auf der Diagnose.

**Wenn die Diagnose ergibt, dass dir Recherche-Daten fehlen, die du nicht kompensieren kannst:** Schreib statt der Page nur:

```
NEEDS_USER_INPUT:
- [Was genau müsste der User recherchieren oder mitgeben?]
```

Liefere jetzt entweder DIAGNOSE+Page oder NEEDS_USER_INPUT.
