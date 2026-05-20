#!/usr/bin/env python
"""Casa Hacker DS · Rename helper for submarca SVGs.

Renomeia arquivos `*_Artboard NN.svg` em assets/submarcas/* para nomes
descritivos baseados na paleta de cores presente no SVG.

Convenção:
    {slug}-{lockup}-{colorway}.svg

Auto-detecta colorway pelos hex codes:
    code+dos  → "primary" (full color Casa Hacker)
    code+css  → "inverse" (pra fundo escuro)
    pink+dos  → "pink" (signature minas-em-tech)
    purple+dos → "purple" (signature perifa-impacto)
    sec-blue+css → "blue-light" (variação hackerclubes)
    + outras

Lockup inferido por viewBox aspect ratio:
    > 5:1  → "horizontal"
    1:1±0.3 → "symbol"
    outros → "vertical"

Uso:
    py scripts/rename_submarcas.py --dry-run   # mostra plano
    py scripts/rename_submarcas.py --apply     # renomeia de fato
    py scripts/rename_submarcas.py --submarca perifa-impacto --apply

Mantém PRIMARY_LOGO map em gen_brand.py atualizado opcionalmente.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "submarcas"

# Mapeamento cor → nome semântico
COLOR_TO_NAME = {
    frozenset({"#32fa96","#3c433c"}): "primary",       # Code + Dos
    frozenset({"#32fa96","#f8fcf8"}): "inverse",       # Code + CSS (pra fundo escuro)
    frozenset({"#3c433c","#ff9ecf"}): "pink",          # Dos + Pink (Minas)
    frozenset({"#3c433c","#aa78e6"}): "purple",        # Dos + Purple (Perifa)
    frozenset({"#f8fcf8","#ff9ecf"}): "pink-light",
    frozenset({"#aa78e6","#ffdfef"}): "purple-pink",
    frozenset({"#b3d9fe","#f8fcf8"}): "blue-light",
    frozenset({"#32fa96","#91938c"}): "code-gray",
    frozenset({"#3c433c"}): "dos-mono",
    frozenset({"#32fa96"}): "code-mono",
    frozenset({"#f8fcf8"}): "css-mono",
    frozenset({"#b3d9fe"}): "blue-mono",
    frozenset({"#ff9ecf"}): "pink-mono",
    frozenset({"#e1ffde"}): "green-mono",
}

VIEWBOX_RE = re.compile(r'viewBox="([0-9.\s]+)"')
HEX_RE = re.compile(r'#[0-9A-Fa-f]{6}')


def get_lockup(svg_text):
    m = VIEWBOX_RE.search(svg_text)
    if not m:
        return "lockup"
    parts = m.group(1).split()
    if len(parts) < 4:
        return "lockup"
    w, h = float(parts[2]), float(parts[3])
    if h == 0:
        return "lockup"
    ratio = w / h
    if ratio > 5:
        return "horizontal"
    if 0.7 < ratio < 1.4:
        return "symbol"
    if ratio > 2:
        return "horizontal"
    return "vertical"


def get_colorway(svg_text):
    colors = frozenset(c.lower() for c in HEX_RE.findall(svg_text))
    if colors in COLOR_TO_NAME:
        return COLOR_TO_NAME[colors]
    # fallback: hash dos hex
    return "color-" + "-".join(sorted(colors)).replace("#", "")[:12]


def plan_rename(slug_dir):
    slug = slug_dir.name
    plans = []
    seen_names = set()
    for f in sorted(slug_dir.iterdir()):
        if not f.is_file() or not f.suffix.lower() == ".svg":
            continue
        if not f.name.endswith(".svg") or "_Artboard" not in f.name:
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        lockup = get_lockup(text)
        colorway = get_colorway(text)
        base = f"{slug}-{lockup}-{colorway}"
        new_name = f"{base}.svg"
        # Disambiguar duplicatas
        n = 2
        while new_name in seen_names:
            new_name = f"{base}-{n}.svg"
            n += 1
        seen_names.add(new_name)
        plans.append((f, slug_dir / new_name))
    return plans


def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    target = None
    if "--submarca" in args:
        idx = args.index("--submarca")
        target = args[idx + 1] if idx + 1 < len(args) else None

    dirs = sorted(ASSETS.iterdir()) if ASSETS.exists() else []
    if target:
        dirs = [d for d in dirs if d.name == target]

    total = 0
    for slug_dir in dirs:
        if not slug_dir.is_dir():
            continue
        plans = plan_rename(slug_dir)
        if not plans:
            continue
        print(f"\n=== {slug_dir.name} ({len(plans)} files) ===")
        for src, dst in plans:
            arrow = "→" if apply else "?"
            print(f"  {src.name}  {arrow}  {dst.name}")
            if apply:
                src.rename(dst)
        total += len(plans)
    mode = "renamed" if apply else "would rename"
    print(f"\n{total} files {mode}")
    if not apply and total > 0:
        print("(use --apply pra aplicar de fato)")


if __name__ == "__main__":
    main()
