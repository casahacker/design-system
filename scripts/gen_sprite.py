"""Build · gera assets/sprite.svg combinando ícones repetidos em <symbol>.
Cada ícone vira referenciável via <svg><use href="sprite.svg#name"/></svg>.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Ícones inline canônicos (16×16 viewbox)
ICONS = {
    'h-pixel': '''<g><rect x="0" y="0" width="4" height="4"/><rect x="12" y="0" width="4" height="4"/><rect x="6" y="6" width="4" height="4"/><rect x="0" y="12" width="4" height="4"/><rect x="12" y="12" width="4" height="4"/></g>''',
    'sun':     '<g><circle cx="8" cy="8" r="3"/><g stroke-width="1.5" stroke-linecap="round" stroke="currentColor"><line x1="8" y1="1" x2="8" y2="3"/><line x1="8" y1="13" x2="8" y2="15"/><line x1="1" y1="8" x2="3" y2="8"/><line x1="13" y1="8" x2="15" y2="8"/><line x1="3" y1="3" x2="4.5" y2="4.5"/><line x1="11.5" y1="11.5" x2="13" y2="13"/><line x1="13" y1="3" x2="11.5" y2="4.5"/><line x1="4.5" y1="11.5" x2="3" y2="13"/></g></g>',
    'moon':    '<path d="M14 9.5A6 6 0 0 1 6.5 2a6 6 0 1 0 7.5 7.5z"/>',
    'arrow-up':   '<path d="M8 2 L4 6 L5 7 L7.5 4.5 L7.5 14 L8.5 14 L8.5 4.5 L11 7 L12 6 Z"/>',
    'arrow-down': '<path d="M8 14 L4 10 L5 9 L7.5 11.5 L7.5 2 L8.5 2 L8.5 11.5 L11 9 L12 10 Z"/>',
    'arrow-right':'<path d="M14 8 L10 4 L9 5 L11.5 7.5 L2 7.5 L2 8.5 L11.5 8.5 L9 11 L10 12 Z"/>',
    'arrow-left': '<path d="M2 8 L6 4 L7 5 L4.5 7.5 L14 7.5 L14 8.5 L4.5 8.5 L7 11 L6 12 Z"/>',
    'check':   '<path d="M14 4 L6 12 L2 8 L3 7 L6 10 L13 3 Z"/>',
    'close':   '<path d="M4 4 L12 12 M12 4 L4 12" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    'warning': '<path d="M8 1 L15 14 L1 14 Z M8 6 L8 10 M8 12 L8 13" stroke="currentColor" stroke-width="1.2" fill="none"/>',
    'info':    '<g><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.2" fill="none"/><path d="M8 7 L8 11 M8 5 L8 5.5" stroke="currentColor" stroke-width="1.5"/></g>',
    'plus':    '<path d="M8 3 L8 13 M3 8 L13 8" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    'minus':   '<path d="M3 8 L13 8" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    'search':  '<g><circle cx="7" cy="7" r="4.5" stroke="currentColor" stroke-width="1.2" fill="none"/><path d="M11 11 L14 14" stroke="currentColor" stroke-width="1.5" fill="none"/></g>',
    'menu':    '<g stroke="currentColor" stroke-width="1.5"><line x1="2" y1="4" x2="14" y2="4"/><line x1="2" y1="8" x2="14" y2="8"/><line x1="2" y1="12" x2="14" y2="12"/></g>',
    'github':  '<path d="M8 0.5C3.6.5 0 4.1 0 8.5c0 3.5 2.3 6.5 5.5 7.6.4.1.6-.2.6-.4v-1.5c-2.2.5-2.7-1.1-2.7-1.1-.4-.9-.9-1.2-.9-1.2-.7-.5.1-.5.1-.5.8.1 1.2.8 1.2.8.7 1.2 1.9.9 2.4.7.1-.5.3-.9.5-1.1-1.8-.2-3.7-.9-3.7-4 0-.9.3-1.6.8-2.2-.1-.2-.4-1 .1-2.1 0 0 .7-.2 2.2.8.6-.2 1.3-.3 2-.3.7 0 1.4.1 2 .3 1.5-1 2.2-.8 2.2-.8.4 1.1.2 1.9.1 2.1.5.6.8 1.3.8 2.2 0 3.1-1.9 3.8-3.7 4 .3.3.6.8.6 1.6v2.3c0 .2.2.5.6.4 3.2-1.1 5.5-4.1 5.5-7.6 0-4.4-3.6-8-8-8z"/>',
    'external':'<g stroke="currentColor" stroke-width="1.2" fill="none"><path d="M4 4 L4 12 L12 12 L12 8"/><path d="M10 4 L14 4 L14 8"/><line x1="7" y1="9" x2="14" y2="4"/></g>',
    'copy':    '<g stroke="currentColor" stroke-width="1.2" fill="none"><rect x="4" y="4" width="9" height="11"/><path d="M4 4 L4 1 L11 1 L11 4"/></g>',
    'chevron-down': '<path d="M3 6 L8 11 L13 6" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    'chevron-up':   '<path d="M3 10 L8 5 L13 10" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    'chevron-right':'<path d="M6 3 L11 8 L6 13" stroke="currentColor" stroke-width="1.5" fill="none"/>',
    'chevron-left': '<path d="M10 3 L5 8 L10 13" stroke="currentColor" stroke-width="1.5" fill="none"/>',
}


def build():
    symbols = ''
    for name, body in ICONS.items():
        symbols += f'  <symbol id="{name}" viewBox="0 0 16 16" fill="currentColor">{body}</symbol>\n'
    sprite = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">
{symbols}</svg>
'''
    out = ROOT / 'assets' / 'sprite.svg'
    out.write_text(sprite, encoding='utf-8')
    print(f'written: assets/sprite.svg with {len(ICONS)} symbols ({out.stat().st_size:,} bytes)')


if __name__ == '__main__':
    build()
