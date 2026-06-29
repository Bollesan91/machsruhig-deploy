#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lint-all.py - alle Deploy-Gates in einem Lauf:
  lint-site.py  +  lint-friedhof.py  +  lint-claims.py
Exit 1, sobald irgendein Gate fehlschlaegt. Vor jedem Deploy ausfuehren.
"""
import subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
GATES = ["lint-site.py", "lint-friedhof.py", "lint-claims.py"]
rc = 0
for g in GATES:
    print(f"\n===== {g} =====")
    r = subprocess.run([sys.executable, os.path.join(HERE, g)])
    if r.returncode != 0:
        rc = 1
print(f"\n===== lint-all: {'ALLE GRUEN' if rc == 0 else 'FEHLER in mindestens einem Gate'} =====")
sys.exit(rc)
