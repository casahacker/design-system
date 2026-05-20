"""Build · gera search-index.json com títulos + h2/h3 + intro de todas as páginas.

Roda como parte do build. Output: search-index.json no root.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Mapeia label de seção pelos ch-page IDs
SECTION_LABELS = {
    'home': 'home', 'about': 'sobre', 'principles': 'sobre',
    'who-uses': 'sobre', 'ecosystem': 'sobre',
    'g-overview': 'guidelines', 'g-a11y': 'guidelines',
    'g-content': 'guidelines', 'g-ai': 'guidelines',
    'color': 'foundations', 'typography': 'foundations',
    'spacing': 'foundations', 'grid': 'foundations',
    'iconography': 'foundations', 'motion': 'foundations',
    'themes': 'foundations',
}

def get_section(ch_page):
    if ch_page in SECTION_LABELS:
        return SECTION_LABELS[ch_page]
    # heuristics
    if ch_page.startswith('dv-'): return 'data viz'
    if ch_page in ('comp-index', 'accordion','breadcrumb','button','checkbox','code-snippet',
                   'data-table','dropdown','file-uploader','form','inline-notif','link',
                   'loading','modal','notification','number-input','pagination','radio-button',
                   'search','slider','tabs','tag','text-input','tile','toggle','tooltip','ui-shell'):
        return 'components'
    if ch_page.startswith('pat-') or ch_page in ('bit-system','colored-symbol','grafismos',
                                                  'forms-pat','dialogs','empty-states','login',
                                                  'global-header','status'):
        return 'patterns'
    if ch_page == 'sub-index' or ch_page in ('hackerclubes','inclusao-tech','minas-em-tech',
                                              'mao-na-massa','perifa-impacto'):
        return 'submarcas'
    if ch_page == 'imp-index' or ch_page in ('papelaria','eventos','loja'):
        return 'impressos'
    if ch_page.startswith('contrib') or ch_page in ('checklist','pdlc','docs-guide'):
        return 'contributing'
    if ch_page.startswith('help-'):
        return 'help'
    return 'outros'


def parse_html(path):
    text = path.read_text(encoding='utf-8')
    ch_page_m = re.search(r'<meta name="ch-page" content="([^"]+)"', text)
    title_m = re.search(r'<title>([^<]+)</title>', text)
    intro_m = re.search(r'<p class="page-intro">\s*([^<]+(?:<[^>]+>[^<]*)*?)\s*</p>', text)
    h2s = re.findall(r'<section[^>]*\bid="([^"]+)"[^>]*>\s*<div class="section-head"><h2>([^<]+)</h2>', text)

    return {
        'ch_page': ch_page_m.group(1) if ch_page_m else '',
        'title': (title_m.group(1).split('·')[0].strip() if title_m else ''),
        'intro': re.sub(r'<[^>]+>', '', intro_m.group(1)).strip()[:200] if intro_m else '',
        'h2': [{'id': h[0], 'label': h[1]} for h in h2s],
    }


def main():
    pages = list((ROOT / 'pages').rglob('*.html'))
    pages.append(ROOT / 'index.html')
    index = []
    for p in sorted(pages):
        try:
            data = parse_html(p)
            if not data['ch_page']:
                continue
            rel = p.relative_to(ROOT).as_posix()
            data['url'] = rel
            data['section'] = get_section(data['ch_page'])
            index.append(data)
        except Exception as e:
            print(f'WARN: {p.name}: {e}')
    out = ROOT / 'search-index.json'
    out.write_text(json.dumps(index, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print(f'written: search-index.json with {len(index)} pages '
          f'({out.stat().st_size:,} bytes)')


if __name__ == '__main__':
    main()
