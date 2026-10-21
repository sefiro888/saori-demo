# -*- coding: utf-8 -*-
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
p = os.path.join(ROOT, "src", "build.py")
b = open(p, encoding="utf-8").read()
if "reelstyle.css" not in b:
    b = b.replace('<link rel="stylesheet" href="{prefix}viewer.css">', '<link rel="stylesheet" href="{prefix}viewer.css">\n<link rel="stylesheet" href="{prefix}reelstyle.css">')
    b = b.replace('<link rel="stylesheet" href="viewer.css">', '<link rel="stylesheet" href="viewer.css"><link rel="stylesheet" href="reelstyle.css">')
    open(p, "w", encoding="utf-8").write(b)
print("reelstyle.css" in b)
