"""Sweep · substitui inline styles comuns por classes utilitárias.

Roda nos arquivos HTML em pages/, no index.html, no 404.html
e nos scripts/gen_*.py pra manter sincronia.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Substituições (regex → replacement)
# Cada tupla: (pattern, repl, descrição)
# IMPORTANTE: regras de MERGE vêm primeiro pra não criar class="x" class="y" duplicado.
RULES = [
    # Merge: class+style 720px → class "... prose"
    (r'class="([^"]+)"\s+style="max-width:\s*720px;?"', r'class="\1 prose"', 'merge class+style 720'),
    (r'class="([^"]+)"\s+style="max-width:\s*480px;?"', r'class="\1 max-w-xs"', 'merge class+style 480'),
    (r'class="([^"]+)"\s+style="max-width:\s*600px;?"', r'class="\1 max-w-sm"', 'merge class+style 600'),
    (r'class="([^"]+)"\s+style="max-width:\s*320px;?"', r'class="\1 max-w-card"', 'merge class+style 320'),
    # Standalone (sem class existente)
    (r'style="max-width:\s*720px;?"', 'class="prose"', 'standalone 720 → .prose'),
    (r'style="max-width:\s*480px;?"', 'class="max-w-xs"', 'standalone 480 → .max-w-xs'),
    (r'style="max-width:\s*600px;?"', 'class="max-w-sm"', 'standalone 600 → .max-w-sm'),
    (r'style="max-width:\s*320px;?"', 'class="max-w-card"', 'standalone 320 → .max-w-card'),
]


def process_file(path):
    text = path.read_text(encoding='utf-8')
    orig = text
    changes = []
    for pattern, repl, desc in RULES:
        new_text, n = re.subn(pattern, repl, text)
        if n:
            text = new_text
            changes.append(f'  {desc}: {n}x')
    if text != orig:
        path.write_text(text, encoding='utf-8')
        return changes
    return None


def main():
    # HTML pages
    targets = list((ROOT / 'pages').rglob('*.html'))
    targets += [ROOT / 'index.html', ROOT / '404.html']
    # Also: generators (pra manter sincronizado)
    targets += list((ROOT / 'scripts').glob('gen_*.py'))

    total = 0
    for t in targets:
        if not t.exists():
            continue
        result = process_file(t)
        if result:
            rel = t.relative_to(ROOT)
            print(f'{rel}:')
            for c in result:
                print(c)
            total += 1
    print(f'\n{total} files modified.')


if __name__ == '__main__':
    main()
