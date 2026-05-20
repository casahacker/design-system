"""Cria as issues de melhoria no GitHub via gh CLI."""
import subprocess, json, os

GH = r'C:\Program Files\GitHub CLI\gh.exe'
REPO = 'casahacker/design-system'

ISSUES = [
    # ========== P0 — alta prioridade ==========
    {
        "title": "Extrair estilos inline pra classes utilitárias",
        "labels": ["enhancement", "ui", "dx", "P0-high"],
        "body": """## Problema
51 de 67 páginas têm atributos `style="..."` inline (~76%). Algumas têm também blocos `<style>` page-specific (color, typography). Isso:
- Dificulta manutenção (mudança de token precisa varrer 51 arquivos)
- Quebra responsividade (`max-width:720px` hardcoded ignora breakpoints)
- Polui o HTML
- Impede CSP strict (`style-src 'self'` sem `unsafe-inline`)

## Solução proposta
1. Auditar `style="..."` mais comuns:
   - `max-width: 720px` → `.prose-max`
   - `margin-bottom: var(--spacing-XX)` → `.mb-XX` (já temos algumas)
   - `style="gap: var(--spacing-06)"` em rows → utility class
   - `style="padding: var(--spacing-07)"` em demos → modifier
2. Criar classes utilitárias em `styles.css` (seção "10 · UTILITIES")
3. Migrar páginas pra usar as classes
4. Atualizar `gen_*.py` pra usar as classes nos geradores
5. Lint regra: zero `style="` em pages/

## Critério de aceite
- [ ] `grep -r 'style="' pages/` retorna 0 resultados
- [ ] Páginas idênticas visualmente (regressão zero)
- [ ] Documentar utilities novas em /pages/elements/spacing ou page nova
"""
    },
    {
        "title": "Auditoria a11y automatizada (Lighthouse CI + Pa11y)",
        "labels": ["a11y", "dx", "P0-high"],
        "body": """## Problema
Acessibilidade hoje é validada manualmente. Sem CI, regressão é fácil.

## Solução proposta
GitHub Action que roda em cada PR:
1. **Lighthouse CI** com budget mínimo (a11y 95+, perf 90+)
2. **Pa11y** validando WCAG 2.1 AA em todas as 67 páginas
3. **axe-core** via Playwright pra componentes interativos
4. Comentar no PR com diff de score

## Arquivos
- `.github/workflows/a11y-audit.yml`
- `lighthouserc.json`
- `.pa11yci.json`

## Critério
- [ ] Workflow roda em push + PR
- [ ] Bloqueia merge se score < threshold
- [ ] Relatório anexado ao run
"""
    },
    {
        "title": "Adicionar componentes faltantes (Toggle, Slider, Date picker, File uploader, Number input)",
        "labels": ["component", "enhancement", "P0-high"],
        "body": """## Problema
Vs IBM Carbon, faltam componentes comuns em forms e configurações.

## Componentes a adicionar (com 10 seções Carbon-complete cada)

### Toggle (switch)
- Use case: settings binárias
- Variantes: small / medium
- ARIA: role="switch", aria-checked

### Slider
- Use case: ranges contínuos (volume, brilho, valores)
- Variantes: single value / range / com input numérico
- Keyboard: ←/→/Home/End/PageUp/Down

### Date picker / Time picker / Date-time picker
- Use case: forms com datas
- Considerar integração com biblioteca leve (sem framework)
- Acessível via teclado + leitor de tela

### File uploader
- Drag-and-drop area
- Progress + cancel
- Multi-file
- Validation (size, type)

### Number input
- Stepper +/-
- Validation (min/max/step)
- Sem dependência de Slider

### Inline notification (vs toast)
- Banner permanente in-page
- Já temos toast/notification mas não banner

## Critério
- [ ] 6 páginas novas em `pages/components/`
- [ ] Adicionados no navConfig do shell.js
- [ ] CSS no styles.css
- [ ] JS no components.js (auto-init)
- [ ] Listed in components/index.html
"""
    },
    {
        "title": "Search full-text + command palette (Cmd/Ctrl+K)",
        "labels": ["ux", "enhancement", "P0-high"],
        "body": """## Problema
Atalho `/` foca a busca, mas ela só filtra a sidebar (não busca conteúdo). Não há command palette pra navegação rápida.

## Solução proposta
1. **Build-time:** script Python que extrai títulos+h2+h3 de todas as páginas e gera `search-index.json` (~50KB)
2. **Runtime:** componente Cmd+K (modal flutuante)
   - Carrega o índice via fetch (lazy)
   - Fuzzy match (algoritmo similar ao Sublime/VSCode)
   - Agrupa por seção (Foundations, Components, Patterns...)
   - Atalhos: Cmd/Ctrl+K abre, ↑↓ navega, Enter abre, Esc fecha
3. **Integração** com a busca atual da sidebar (mesmo input, mais resultados)

## Critério
- [ ] Cmd+K abre overlay
- [ ] Resultados em <100ms
- [ ] Funciona offline (índice cacheado)
- [ ] Documentado em ui-shell.html
"""
    },
    {
        "title": "Refatorar generators Python — reduzir duplicação e melhorar manutenção",
        "labels": ["dx", "enhancement", "P0-high"],
        "body": """## Problema
- `gen_components_a.py` + `gen_components_b.py` têm ~300 linhas duplicando estrutura
- Cada componente repete `s.demo()`, `s.code()`, `s.api_table()` com formato similar
- Dificulta adicionar componente novo (copy/paste extenso)

## Solução proposta
1. Centralizar configuração de componentes num único `components_data.py` (estrutura declarativa)
2. `common.py` cresce com helpers mais ricos (ex: `code_html_block`, `state_grid`, `playground`)
3. Um único `gen_components.py` itera sobre os dados
4. Adicionar componente vira só editar o dict

## Refactor de exemplo
```python
COMPONENTS = {
    "button": {
        "intro": "...",
        "variants": [("primary", "Ação mais importante..."), ...],
        "sizes": [("sm", "32px"), ...],
        "api": [...],
        "do": [...], "dont": [...],
        "code_html": "...",
    }
}
```

## Critério
- [ ] -40% linhas nos generators de components
- [ ] Adicionar componente novo: editar 1 lugar
- [ ] Páginas geradas idênticas ao output atual
"""
    },

    # ========== P1 — média ==========
    {
        "title": "Auto-TOC scrollspy + botão voltar-ao-topo em páginas longas",
        "labels": ["ux", "enhancement", "P1-medium"],
        "body": """## Problema
- TOC fica estática — não indica seção atual conforme usuário rola
- Páginas longas (color, typography, accessibility, global-header) não têm "back to top"

## Solução
1. **Scrollspy:** IntersectionObserver no `shell.js` que adiciona `.active` ao link da TOC conforme a seção entra na viewport
2. **TOC sticky desktop:** em telas >1280px, TOC vira lateral fixa à direita (Carbon-style)
3. **Back-to-top:** botão flutuante (visível ao scrollar >800px)

## Critério
- [ ] TOC ativo segue scroll suavemente
- [ ] Versão sticky lateral em desktop wide
- [ ] Back-to-top com animação smooth
- [ ] Funciona com prefers-reduced-motion (sem smooth)
"""
    },
    {
        "title": "Navegação prev/next no rodapé das páginas",
        "labels": ["ux", "enhancement", "P1-medium"],
        "body": """## Problema
Ao terminar de ler uma página, usuário precisa voltar ao sidebar pra ir à próxima.

## Solução
Adicionar no shell.js footer um par de links "← anterior · próximo →" baseado na ordem do `navConfig`. Inteligente:
- Pula seções (último item de Foundations vai pro primeiro de Components)
- Mostra nome legível do destino
- Atalhos: `J` próximo, `K` anterior (vim-style)

## Critério
- [ ] Footer mostra prev/next em todas as páginas
- [ ] Atalhos J/K funcionam
- [ ] Texto descritivo (não só seta)
"""
    },
    {
        "title": "Service Worker pra offline + PWA manifest",
        "labels": ["performance", "enhancement", "P1-medium"],
        "body": """## Problema
Site não funciona offline. Sem PWA install.

## Solução
1. **Manifest** (`manifest.webmanifest`) com ícones, theme color, display standalone
2. **Service worker** com cache-first pra:
   - styles.css, shell.js, components.js
   - todas as fontes
   - todos os assets svg
   - HTML em network-first com fallback offline
3. Adicionar `<link rel="manifest">` no shell.js head injection
4. Página offline.html

## Critério
- [ ] Lighthouse PWA score ≥ 90
- [ ] Funciona sem rede após primeira visita
- [ ] Install prompt funcional
"""
    },
    {
        "title": "Dark mode toggle persistente no header (não só botão flutuante)",
        "labels": ["ux", "ui", "P1-medium"],
        "body": """## Problema
Theme toggle é um botão flutuante no canto inferior direito. Descoberta ruim e cobre conteúdo em mobile.

## Solução
1. Mover toggle pro header (`shell-actions`), entre `sobre` e `github`
2. Ícone SVG inline (sol/lua) em vez de "◑ theme"
3. Manter atalho keyboard (talvez `T`)
4. Remover botão flutuante

## Critério
- [ ] Toggle visível no header desktop
- [ ] Funcional em mobile (não sumir)
- [ ] Acessível via teclado
- [ ] aria-pressed reflete estado
"""
    },
    {
        "title": "Issue templates + PR template + CONTRIBUTING.md + CODE_OF_CONDUCT.md",
        "labels": ["dx", "documentation", "P1-medium"],
        "body": """## Problema
Repositório sem templates de issue/PR — contribuições não-estruturadas.

## Arquivos a criar
```
.github/
  ISSUE_TEMPLATE/
    bug.yml          (formulário de bug)
    component-proposal.yml
    docs-fix.yml
    feature.yml
  pull_request_template.md
CONTRIBUTING.md       (já existe a page, falta o arquivo raiz)
CODE_OF_CONDUCT.md    (Contributor Covenant adaptado)
SECURITY.md           (como reportar vulnerabilidades)
```

## Critério
- [ ] Issue nova mostra dropdown de tipos
- [ ] PR mostra checklist (a11y, docs, code style)
- [ ] CoC em pt-br + linka da home/sobre
"""
    },
    {
        "title": "Adicionar interactive props playground em todos os componentes",
        "labels": ["component", "ux", "P1-medium"],
        "body": """## Problema
Só 4 de 22 componentes têm comportamento interativo nos demos (accordion, dropdown, modal, tabs). O resto é estático.

## Solução
Cada página de componente ganha uma seção "Playground" com:
- Controles pra cada modifier (variant, size, state, disabled)
- Preview ao vivo
- Snippet de código que atualiza conforme controles
- Botão "copy with these settings"

## Exemplo (Button)
```
[Variant: primary ▼]
[Size: medium ▼]
[Disabled: ☐]
[Icon: ◯ none / ◉ leading / ◯ trailing]

→ Preview: <button class="btn btn--primary">label</button>
→ Code: <button class="btn btn--primary">label</button>
```

## Critério
- [ ] 22 páginas com playground
- [ ] Helper reutilizável `.playground` em styles.css
- [ ] Snippet de código atualiza em tempo real
"""
    },
    {
        "title": "Variantes expandidas dos componentes existentes",
        "labels": ["component", "enhancement", "P1-medium"],
        "body": """## Problema
Vários componentes têm apenas a variante base, faltando casos comuns do Carbon.

## Variantes a adicionar

### Modal
- [ ] Alert dialog (1 ação, crítico)
- [ ] Passive modal (sem footer)
- [ ] Transactional (com loading state no submit)
- [ ] Full-screen mobile

### Button
- [ ] `btn--icon-leading` (ícone antes do label)
- [ ] `btn--icon-trailing` (ícone depois)
- [ ] `btn--loading` (spinner inline durante async action)
- [ ] `btn--block` (largura 100%)

### Tag
- [ ] Filter applied (com checkmark + close)
- [ ] Selectable (clicável, vira filter)
- [ ] Com ícone leading

### Notification
- [ ] Inline (vs toast) — banner persistente na página
- [ ] Action button no rodapé
- [ ] Ícone customizável

### Data table
- [ ] Sortable columns (clique no header)
- [ ] Filter row
- [ ] Select all checkbox
- [ ] Row expansion (drilldown)
- [ ] Pagination integrada

### Tabs
- [ ] Vertical layout
- [ ] Contained vs line (atual é line)
- [ ] Com counter/badge

## Critério
- [ ] Variantes documentadas em cada página
- [ ] CSS no styles.css
- [ ] Demos funcionais
"""
    },

    # ========== P2 — refinamento ==========
    {
        "title": "Usar a biblioteca de 67+ grafismos in-context (não só catálogo)",
        "labels": ["identity", "ui", "P2-low"],
        "body": """## Problema
Temos 67 SVGs em `assets/grafismos/` mas não aparecem em lugar nenhum exceto a página de catálogo.

## Solução
- Hero das páginas de submarcas com grafismo de fundo (cada submarca tem 1 grafismo signature)
- Empty states com grafismo decorativo
- Section dividers usando padrões modulares
- Hero da home com grafismo isométrico animado (subtle)
- 404 page com grafismo "glitched"

## Critério
- [ ] Mínimo 10 grafismos usados além do catálogo
- [ ] Sempre com `aria-hidden="true"` (decorativos)
- [ ] Respeitar prefers-reduced-motion (sem parallax)
"""
    },
    {
        "title": "Personalidade hacker — easter eggs e momentos lúdicos (VT323)",
        "labels": ["identity", "ux", "P2-low"],
        "body": """## Problema
A fonte VT323 (pixel terminal) está self-hosted e disponível mas quase não é usada. O sistema é técnico mas falta a "alma" hacker da marca.

## Ideias

### Easter eggs
- Konami code (↑↑↓↓←→←→BA) → modo terminal verde-no-preto temporário
- Digitar "hack" em qualquer lugar → animação no H da brand
- `?cheat` na URL → mostra atalhos disponíveis
- Console: ASCII art da Casa Hacker ao abrir DevTools

### Momentos VT323
- Loading inicial: terminal "booting design system v1.0..."
- 404 com aesthetic terminal: "command not found: /typo/aqui"
- Footer com timestamp tipo `[2026-05-19 22:08:00] system ready`
- Badges de status com fonte pixel ("◆ live", "⚠ beta")

### Reveal sutil
- H do logo "carrega" quadrado por quadrado no primeiro paint
- Cursor piscante (▎) em headlines
- Glitch effect raro (1% load) no logo header

## Critério
- [ ] Mínimo 3 momentos VT323/lúdicos
- [ ] Tudo opt-in ou skip-able (não atrapalha quem não quer)
- [ ] Respeita prefers-reduced-motion
- [ ] Sem prejudicar acessibilidade
"""
    },
    {
        "title": "Substituir SVGs avulsos por sprite + lazy-loading de imagens",
        "labels": ["performance", "enhancement", "P2-low"],
        "body": """## Problema
- 209 arquivos em `assets/` servidos como GETs separados
- Ícones inline duplicados em vários HTMLs
- Submarca logos sempre baixados na navegação (mesmo se não vai aparecer)

## Solução
1. Script Python que gera `assets/sprite.svg` com `<symbol id="...">` pra ícones comuns
2. Usar via `<svg><use href="/assets/sprite.svg#h-symbol"/></svg>`
3. `loading="lazy"` + `decoding="async"` em todas as `<img>` de submarcas
4. Preload do sprite no head crítico

## Critério
- [ ] Sprite gerado automaticamente
- [ ] -50% requests HTTP em primeira visita
- [ ] Lighthouse performance score >95
"""
    },
    {
        "title": "Auditar e remover cores hardcoded em prol de tokens",
        "labels": ["identity", "ui", "P2-low"],
        "body": """## Problema
Várias páginas têm cores literais (#XXXXXX) em vez de `var(--token)`. Quebra dark mode em pontos específicos.

## Auditoria
```bash
grep -rE '#[0-9A-Fa-f]{3,6}' pages/ --include='*.html' | wc -l
```

## Solução
1. Listar todos os hex literais
2. Decidir: virá token (se reutilizável) ou troca pra token existente
3. Páginas mais afetadas: color.html (intencional, é o catálogo de cores), submarcas/* (cores de marca-filha), impressos/* (CMYK references)
4. Documentar exceções (quando hardcoded é OK: catálogos visuais)

## Critério
- [ ] Páginas que não são catálogo → 0 hex literals
- [ ] Cor de identidade de submarca → token (--ch-sub-{nome})
- [ ] Dark mode 100% sem fallback de hex
"""
    },
    {
        "title": "Variações do H-symbol (loading, glitch, hover)",
        "labels": ["identity", "ui", "P2-low"],
        "body": """## Problema
O H da marca é estático em todo lugar. É o símbolo principal e poderia ter mais expressividade.

## Variações propostas
1. **H loading** — quadrados acendem em sequência (animação pixelada)
2. **H hover no header** — pequena animação ao passar mouse
3. **H glitch** — efeito raro/easter egg
4. **H breathing** — pulsa suavemente quando há carregamento na página
5. **H typed** — desenha-se quadrado por quadrado no primeiro paint

## Implementação
- Componente `<div class="h-symbol h-symbol--{variant}">`
- CSS animations puras (zero JS)
- Documentar em `pages/elements/iconography.html`
- Showcasing em `pages/patterns/bit-system.html`

## Critério
- [ ] 3+ variações implementadas
- [ ] Todas respeitam prefers-reduced-motion
- [ ] Documentadas na iconography
"""
    },
    {
        "title": "Propor CSS variables upstream em casahacker/barra-acessibilidade",
        "labels": ["a11y", "identity", "dx", "P2-low"],
        "body": """## Problema
A barra de acessibilidade usa cores hardcoded (#21272a, #0F62FE). No CHDS fazemos override com `!important`, o que é frágil.

## Solução
PR no repo upstream (`casahacker/barra-acessibilidade`) expondo CSS variables:

```css
.ch-a11y-bar {
  --ch-a11y-bg: #21272a;
  --ch-a11y-fg: #fff;
  --ch-a11y-active-bg: #0f62fe;
  --ch-a11y-active-fg: #fff;
  --ch-a11y-ruler-color: #f4a100;
  --ch-a11y-font: system-ui, sans-serif;

  background: var(--ch-a11y-bg);
  color: var(--ch-a11y-fg);
  font-family: var(--ch-a11y-font);
}
```

Aí no CHDS troca o override `!important` por:
```css
.ch-a11y-bar {
  --ch-a11y-bg: var(--ch-dos);
  --ch-a11y-active-bg: var(--ch-code);
  --ch-a11y-active-fg: var(--ch-dos);
  --ch-a11y-font: var(--font-mono);
}
```

## Critério
- [ ] PR aberto no upstream
- [ ] Variables definidas, valores atuais preservados como default
- [ ] Após merge, remover !important do styles.css local
"""
    },
]


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')


def create_issue(issue):
    cmd = [GH, 'issue', 'create',
           '--repo', REPO,
           '--title', issue['title'],
           '--body', issue['body']]
    for label in issue['labels']:
        cmd.extend(['--label', label])
    result = run(cmd)
    if result.returncode == 0:
        url = result.stdout.strip().split('\n')[-1]
        print(f"  [ok] {issue['title'][:60]}")
        print(f"    {url}")
        return url
    else:
        print(f"  [FAIL] {issue['title'][:60]}")
        print(f"    {result.stderr.strip()[:200]}")
        return None


print(f"Creating {len(ISSUES)} issues in {REPO}...\n")
urls = []
for i, issue in enumerate(ISSUES, 1):
    print(f"[{i}/{len(ISSUES)}]", issue['title'][:80])
    url = create_issue(issue)
    if url:
        urls.append(url)

print(f"\n{'='*60}\nCreated {len(urls)}/{len(ISSUES)} issues")
for u in urls:
    print(u)
