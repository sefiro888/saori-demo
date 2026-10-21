# -*- coding: utf-8 -*-
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
p = os.path.join(ROOT, "src", "build.py")
b = open(p, encoding="utf-8").read()
if "viewer.css" not in b:
    b = b.replace('<link rel="stylesheet" href="{prefix}premium.css">', '<link rel="stylesheet" href="{prefix}premium.css">\n<link rel="stylesheet" href="{prefix}viewer.css">')
    b = b.replace('<link rel="stylesheet" href="premium.css">', '<link rel="stylesheet" href="premium.css"><link rel="stylesheet" href="viewer.css">')
    b = b.replace('<script src="{prefix}premium.js"></script>', '<script src="{prefix}premium.js"></script>\n<script src="{prefix}viewer.js"></script>')
    open(p, "w", encoding="utf-8").write(b)
j = os.path.join(ROOT, "premium.js")
t = open(j, encoding="utf-8").read()
t = t.replace("  $$('.reel-shield').forEach(b => b.addEventListener('click', () => b.closest('.reel').classList.add('live')));\n", "")
open(j, "w", encoding="utf-8").write(t)
print("ok")
