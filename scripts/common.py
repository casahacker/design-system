"""Casa Hacker DS — template helpers (build-time only)."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def write(rel, html):
    fp = ROOT / rel
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(html, encoding="utf-8")
    print("written:", rel)


# ----- page skeleton --------------------------------------------------------
def page(page_id, title, breadcrumb, intro, sections, *, depth="../../", tags=None, toc=None, extra_head=""):
    tags = tags or []
    toc = toc or []
    tags_html = (
        '<div class="page-tags">'
        + "".join(f'<span class="tag {t.get("cls","")}">{t["label"]}</span>' for t in tags)
        + "</div>"
    ) if tags else ""
    toc_html = (
        '<aside class="toc"><h5>nesta página</h5><ol>'
        + "".join(f'<li><a href="#{t["id"]}">{t["label"]}</a></li>' for t in toc)
        + "</ol></aside>"
    ) if toc else ""
    desc = (intro or "").replace("<", "&lt;").replace(">", "&gt;")[:160].replace('"', "&quot;")
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="ch-page" content="{page_id}">
<meta name="ch-base" content="{depth}">
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="{depth}favicon.svg">
<title>{title} · Casa Hacker DS</title>
<link rel="stylesheet" href="{depth}styles.css">
{extra_head}
</head>
<body>
<main class="main">

  <header class="page-header">
    <div class="page-breadcrumb">{breadcrumb}</div>
    <h1 class="page-title">{title.lower()}</h1>
    <p class="page-intro">{intro}</p>
    {tags_html}
  </header>

  {toc_html}

  {sections}

</main>
<script src="{depth}shell.js"></script>
<script src="{depth}components.js"></script>
</body>
</html>
"""


# ----- section builders -----------------------------------------------------
def sec(sid, title, meta, body):
    return (
        f'<section class="section" id="{sid}">'
        f'<div class="section-head"><h2>{title}</h2>'
        f'<span class="meta">{meta}</span></div>{body}</section>'
    )


def demo(content, modifier=""):
    return f'<div class="demo {modifier}">{content}</div>'


def anatomy(svg, legend=None):
    legend = legend or []
    legend_html = (
        '<ol class="anatomy-legend">'
        + "".join(f"<li>{l}</li>" for l in legend)
        + "</ol>"
    ) if legend else ""
    return f'<div class="anatomy">{svg}{legend_html}</div>'


def api_table(rows):
    body = "".join(
        f"<tr><td>{r['prop']}</td><td>{r['type']}</td>"
        f"<td>{r.get('def') or '—'}</td><td>{r['desc']}</td></tr>"
        for r in rows
    )
    return (
        '<table class="api-table">'
        "<thead><tr><th>prop</th><th>tipo</th><th>default</th><th>descrição</th></tr></thead>"
        f"<tbody>{body}</tbody></table>"
    )


def do_dont(dos, donts):
    li = lambda lst: "".join(f"<li>{x}</li>" for x in lst)
    return (
        '<div class="do-dont">'
        f'<div class="tile do"><h4>use</h4><ul class="bare">{li(dos)}</ul></div>'
        f'<div class="tile dont"><h4>não use</h4><ul class="bare">{li(donts)}</ul></div>'
        "</div>"
    )


def code(content):
    return f'<div class="code-snippet">{content}</div>'


def checklist(items):
    return '<ul class="checklist">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def related(cards):
    return (
        '<div class="resource-cards">'
        + "".join(
            f'<a class="resource-card" href="{c["href"]}">'
            f'<div class="meta">{c.get("meta","componente")}</div>'
            f'<h4>{c["title"]}</h4>'
            f'<p>{c["desc"]}</p>'
            '<span class="cta">explorar</span></a>'
            for c in cards
        )
        + "</div>"
    )


def table(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="data-table"><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>'


def grid(tiles, cols=3):
    cards = "".join(
        f'<div class="tile tile--bordered"><h4>{t["title"]}</h4><p>{t["desc"]}</p></div>'
        for t in tiles
    )
    return f'<div class="grid-{cols}">{cards}</div>'


# ----- component page template ----------------------------------------------
def component_page(*, page_id, name, intro, demo_html, variants=None, sizes=None, states=None,
                   anatomy_html=None, behaviors=None, modifiers=None, usage=None, a11y=None,
                   code_html=None, related_html=None, extra_tags=None, extra_head=""):
    toc = [{"id": "overview", "label": "Overview"}, {"id": "variants", "label": "Variantes"}]
    if sizes: toc.append({"id": "sizes", "label": "Tamanhos"})
    if states: toc.append({"id": "states", "label": "Estados"})
    if anatomy_html: toc.append({"id": "anatomy", "label": "Anatomia"})
    if behaviors: toc.append({"id": "behaviors", "label": "Comportamentos"})
    if modifiers: toc.append({"id": "modifiers", "label": "Modifiers"})
    toc += [{"id": "usage", "label": "Quando usar"}, {"id": "a11y", "label": "Acessibilidade"}, {"id": "code", "label": "Código"}]
    if related_html: toc.append({"id": "related", "label": "Relacionados"})

    body = sec("overview", "overview", "01", demo_html)
    body += sec("variants", "variantes", "02", variants or '<p class="t-secondary">Variante única.</p>')
    n = 3
    if sizes:        body += sec("sizes", "tamanhos", f"0{n}", sizes); n += 1
    if states:       body += sec("states", "estados", f"0{n}", states); n += 1
    if anatomy_html: body += sec("anatomy", "anatomia", f"0{n}", anatomy_html); n += 1
    if behaviors:    body += sec("behaviors", "comportamentos", f"0{n}", behaviors); n += 1
    if modifiers:    body += sec("modifiers", "modifiers · api", f"0{n}", modifiers); n += 1
    body += sec("usage", "quando usar", f"0{n}", usage or do_dont(["Use em casos comuns"], ["Não use em casos extremos"])); n += 1
    body += sec("a11y", "acessibilidade", f"{n:02d} · wcag aa", a11y or checklist(["Contraste 4.5:1", "Foco visível", "Funciona com teclado"])); n += 1
    body += sec("code", "código", f"{n:02d} · html", code_html or '<p class="t-secondary">Ver exemplo no overview.</p>'); n += 1
    if related_html: body += sec("related", "componentes relacionados", f"{n:02d}", related_html)

    tags = [{"cls": "tag--code", "label": "stable"}] + (extra_tags or [])
    breadcrumb = (
        f'<a href="../../index.html">home</a><span class="sep">/</span>'
        f'<a href="index.html">components</a><span class="sep">/</span>{name}'
    )
    return page(page_id, name, breadcrumb, intro, body, tags=tags, toc=toc, extra_head=extra_head)
