"""Fix · merge duplicate class="..." attributes em todos os arquivos.

Bug introduzido pelo sweep_inline.py quando ordem das regex era errada.
Padrão a corrigir: <tag class="a" class="b"> → <tag class="a b">
Aplica nos HTMLs e nos scripts/gen_*.py.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Match class="X" class="Y" (X, Y são qualquer conteúdo sem aspas)
# Há até 2 ocorrências consecutivas possíveis em alguns lugares — itera até estabilizar
PATTERN = re.compile(r'class="([^"]*)"\s+class="([^"]*)"')


def process(path):
    text = path.read_text(encoding='utf-8')
    orig = text
    iterations = 0
    while True:
        new_text, n = PATTERN.subn(r'class="\1 \2"', text)
        if n == 0:
            break
        text = new_text
        iterations += 1
        if iterations > 10:
            print(f'  WARN: too many iterations on {path}')
            break
    if text != orig:
        path.write_text(text, encoding='utf-8')
        return iterations
    return 0


def main():
    targets = list((ROOT / 'pages').rglob('*.html'))
    targets += [ROOT / 'index.html', ROOT / '404.html']
    targets += list((ROOT / 'scripts').glob('gen_*.py'))
    total_files = 0
    for t in targets:
        if not t.exists():
            continue
        n = process(t)
        if n:
            print(f'{t.relative_to(ROOT)}: merged in {n} pass(es)')
            total_files += 1
    print(f'\n{total_files} files fixed.')


if __name__ == '__main__':
    main()
