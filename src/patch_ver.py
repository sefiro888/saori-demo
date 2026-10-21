# -*- coding: utf-8 -*-
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
p = os.path.join(ROOT, "src", "build.py")
b = open(p, encoding="utf-8").read()
if "def bust(" not in b:
    helper = '''import re, time
VER = str(int(time.time()))
def bust(html_text):
    """Añade ?v=<versión> a los CSS/JS locales para que el navegador no use copias antiguas."""
    return re.sub(r'(href|src)="((?:[a-z0-9\\-]+)\\.(?:css|js))"', lambda m: f'{m.group(1)}="{m.group(2)}?v={VER}"', html_text)

'''
    b = b.replace("def build():", helper + "def build():", 1)
    b = b.replace('f.write(service_page(sv))', 'f.write(bust(service_page(sv)))')
    b = b.replace('        f.write(tpl)', '        f.write(bust(tpl))')
    open(p, "w", encoding="utf-8").write(b)
print("bust(" in b)
