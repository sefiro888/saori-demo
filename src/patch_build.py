# -*- coding: utf-8 -*-
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
p = os.path.join(ROOT, "src", "build.py")
b = open(p, encoding="utf-8").read()
if "extra.css" not in b:
    b = b.replace('<link rel="stylesheet" href="{prefix}site.css">', '<link rel="stylesheet" href="{prefix}site.css">\n<link rel="stylesheet" href="{prefix}extra.css">')
    b = b.replace('<link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="site.css">', '<link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="site.css"><link rel="stylesheet" href="extra.css">')
    b = b.replace('.replace("{{FOOTER}}", footer())', '.replace("{{FOOTER}}", footer() + \'\\n<script src="splash.js"></script>\')')
    open(p, "w", encoding="utf-8").write(b)
print("ok")
