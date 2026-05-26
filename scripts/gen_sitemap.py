"""Gera sitemap.xml e robots.txt-friendly XML index a partir dos .html no repo.

Roda como último passo do build. Inclui apenas páginas estáticas servidas;
ignora node_modules, .git, fonts/, e arquivos non-HTML.
"""
from datetime import date
from pathlib import Path
from common import SITE_URL

ROOT = Path(__file__).resolve().parent.parent

# Subdirs ignorados (não fazem parte do site público)
IGNORE_DIRS = {".git", ".github", "scripts", "node_modules", "fonts", "__pycache__"}


def discover_pages():
    """Coleta URLs relativas a partir de .html no root e em pages/."""
    out = []
    # Páginas no root (index.html, 404.html)
    for fp in sorted(ROOT.glob("*.html")):
        if fp.name == "404.html":
            continue
        out.append(fp.name)
    # Páginas em pages/
    for fp in sorted((ROOT / "pages").rglob("*.html")):
        rel = fp.relative_to(ROOT).as_posix()
        if any(part in IGNORE_DIRS for part in fp.parts):
            continue
        out.append(rel)
    return out


def build_sitemap(pages):
    today = date.today().isoformat()
    urls = []
    for path in pages:
        loc = f"{SITE_URL}/{path}" if path != "index.html" else f"{SITE_URL}/"
        prio = "1.0" if path == "index.html" else ("0.8" if "/elements/" in path or "/components/" in path else "0.6")
        urls.append(
            f"  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>weekly</changefreq>\n"
            f"    <priority>{prio}</priority>\n"
            f"  </url>"
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )


def main():
    pages = discover_pages()
    sitemap = build_sitemap(pages)
    out = ROOT / "sitemap.xml"
    out.write_text(sitemap, encoding="utf-8")
    print(f"written: sitemap.xml with {len(pages)} urls")


if __name__ == "__main__":
    main()
