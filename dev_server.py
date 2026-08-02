"""
Yerel onizleme sunucusu — Natro'da .htaccess devreye alindiginda gecerli
olacak temiz URL davranisini TAKLIT eder (docs/htaccess-taslak.txt ile ayni
mantik): /slug -> cadbim_slug.html, /post/slug -> post/slug.html.
Kaynak: 404.html'deki MAP (tek dogru kaynak).
"""
import http.server
import json
import re
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(ROOT, "404.html"), encoding="utf-8") as f:
    _content = f.read()
_m = re.search(r"var MAP = (\{.*?\});", _content)
MAP = json.loads(_m.group(1))


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean = path.split("?")[0].split("#")[0]
        rel = clean.lstrip("/")

        real = super().translate_path(path)
        if os.path.exists(real) or rel == "":
            return real

        if rel.startswith("post/"):
            candidate = os.path.join(ROOT, rel + ".html")
            if os.path.isfile(candidate):
                return candidate

        slug = rel.rstrip("/")
        if slug in MAP:
            return os.path.join(ROOT, MAP[slug])

        return real  # bulunamadi -> normal 404


if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8420
    os.chdir(ROOT)
    http.server.test(HandlerClass=Handler, port=port)
