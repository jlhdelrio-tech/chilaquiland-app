"""Genera la versión de Claude (artifact) a partir de index.html: quita <head>/<body> y los scripts de Firebase."""
import re, sys
s = open("index.html", encoding="utf-8").read()
body = s.split("<body>", 1)[1].rsplit("</body>", 1)[0]
open(sys.argv[1] if len(sys.argv) > 1 else "artifact.html", "w", encoding="utf-8").write(body.strip() + "\n")
