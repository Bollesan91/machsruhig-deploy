"""
Build per-city dispatch JS files for FAQ-Review.
Outputs: dispatch-faq-{CITY}-{LETTER}.js
Each file: installerJS + window.__mcp.run(prompt, label) call.
"""

import os
import json
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
INSTALLER = (_HERE.parent / "helper-v3-installer.js").read_text(encoding="utf-8")
PROMPT_TPL = (_HERE / "faq-review-prompt.txt").read_text(encoding="utf-8")

# Extract only the IIFE (skip comments)
installer_lines = [ln for ln in INSTALLER.splitlines() if not ln.strip().startswith("//") and ln.strip()]
INSTALLER_JS = "\n".join(installer_lines)

ASSIGN = [
    ("augsburg", "A"),
    ("berlin", "B"),
    ("bremen", "C"),
    ("chemnitz", "A"),
    ("darmstadt", "B"),
    ("essen", "C"),
    ("hamburg", "A"),
    ("muelheim", "B"),
    ("muenster", "C"),
    ("rostock", "A"),
]

for city, letter in ASSIGN:
    prompt = PROMPT_TPL.replace("__CITY__", city).replace("__LETTER__", letter)
    label = f"faq-review-{city}"
    js = INSTALLER_JS + ";\n" + (
        f"window.__mcp.run({json.dumps(prompt, ensure_ascii=False)}, {json.dumps(label)});"
    )
    out = _HERE / f"dispatch-faq-{city}-{letter}.js"
    out.write_text(js, encoding="utf-8")
    print(f"  {out.name}  prompt={len(prompt)}c  total={len(js)}c")
