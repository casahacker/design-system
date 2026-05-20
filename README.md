# Casa Hacker Design System

Sistema de design da Casa Hacker, forked do [IBM Carbon Design System](https://carbondesignsystem.com/) e reskinned com a identidade visual da Casa Hacker.

**Versão:** v1.0 · **Status:** stable · **Stack:** zero-build (HTML + CSS + JS vanilla)

---

## Estrutura

```
design-system/
├── index.html              # Landing
├── 404.html                # Error page
├── favicon.svg             # Brand favicon (H pixelado)
├── robots.txt              # SEO
├── .nojekyll               # Bypass Jekyll no GitHub Pages
├── styles.css              # Tokens + base + componentes + utils + responsive
├── shell.js                # Header + sidebar + theme + auto-TOC + copy
├── components.js           # Modal, Tabs, Accordion, Dropdown, Notification
├── DISCOVERY.md            # Documento de discovery e proposal
├── README.md               # Este arquivo
│
├── .github/workflows/
│   └── pages.yml           # GitHub Action de deploy
│
├── fonts/                  # IBM Plex Mono, Roboto Flex, VT323 (WOFF2)
│
├── assets/
│   ├── logos/              # Logos casa-hacker em variações
│   ├── symbols/            # H pixelado (dark + colored)
│   ├── patterns/           # Patterns demonstrativos
│   ├── bit/                # Cubos 3D do BIT
│   ├── bit-library/        # 9 SVGs da biblioteca BIT
│   ├── colored-symbols/    # Variantes coloridas do H
│   ├── grafismos/          # 67+ patterns geométricos
│   ├── submarcas/          # Logos de cada submarca
│   │   ├── hackerclubes/
│   │   ├── inclusao-tech/
│   │   ├── minas-em-tech/
│   │   ├── mao-na-massa/
│   │   └── perifa-impacto/
│   └── impressos/          # Templates de papelaria, eventos, loja
│
├── pages/
│   ├── about/              # Visão geral, princípios, quem usa, ecossistema (4)
│   ├── guidelines/         # Accessibility, content & voice, AI (4)
│   ├── elements/           # Color, typography, spacing/BIT, grid, iconography, motion, themes (7)
│   ├── components/         # 22 componentes Carbon-complete
│   ├── patterns/           # BIT modular, colored symbol, grafismos, login, dialogs... (10)
│   ├── dataviz/            # Anatomy, types, color palettes (4)
│   ├── submarcas/          # Overview + 5 submarcas (6)
│   ├── impressos/          # Papelaria, eventos, loja (4)
│   ├── contributing/       # Get started, checklist, PDLC, docs guide (4)
│   └── help/               # Contato, FAQ (2)
│
└── scripts/                # Geradores Python (build-time)
    ├── common.py           # Templates de página
    ├── gen_foundation.py   # about + guidelines + foundations
    ├── gen_components_a.py # 10 componentes
    ├── gen_components_b.py # 11 componentes
    ├── gen_patterns.py     # patterns + dataviz
    └── gen_brand.py        # submarcas + impressos + contributing + help
```

**Total: 67 páginas HTML, ~120 SVGs de marca, 3 fontes self-hosted.**

---

## Quickstart

### Preview local

```bash
cd design-system
py -m http.server 8000
# abre http://localhost:8000
```

### Deploy GitHub Pages

#### Opção A — GitHub Actions (recomendado, já configurado)

```bash
git init
git add .
git commit -m "Initial commit · CHDS v1.0"
git remote add origin git@github.com:casahacker/design-system.git
git branch -M main
git push -u origin main
```

No GitHub: **Settings → Pages → Source: GitHub Actions**. O workflow `.github/workflows/pages.yml` faz deploy automático em cada push pra `main`.

#### Opção B — Deploy from branch

**Settings → Pages → Source: Deploy from a branch → main / (root)**

Em ~1 minuto: `https://casahacker.github.io/design-system/`

#### Custom domain

1. DNS: CNAME apontando pra `casahacker.github.io`
2. Settings → Pages → Custom domain → seu domínio
3. ✓ Enforce HTTPS

---

## Páginas (v1.0)

### Sobre o sistema (4)
- Visão geral · Princípios · Quem usa · Ecossistema

### Guidelines (4)
- Overview · Accessibility (WCAG 2.1 AA) · Content & voice · Casa Hacker for AI

### Foundations (7)
- Color · Typography · Spacing · BIT · 2x Grid · Iconography · Motion · Themes

### Components (22 — Carbon-complete)
Accordion · Breadcrumb · Button · Checkbox · Code snippet · Data table · Dropdown · Form · Link · Loading · Modal · Notification · Pagination · Radio button · Search · Tabs · Tag · Text input · Tile · Tooltip · UI shell

### Patterns (10)
Overview · BIT modular · Colored symbol · Grafismos · Forms · Dialogs · Empty states · Login · Global header · Status indicators

### Data Visualization (4)
Overview · Chart anatomy · Chart types · Color palettes

### Submarcas (6)
Overview · Hackerclubes · Inclusão Tech · Minas em Tech · Mão na Massa · Perifa Impacto

### Impressos (4)
Overview · Papelaria · Eventos · Loja & merch

### Contributing (4)
Get started · Component checklist · Lifecycle (PDLC) · Documentation guide

### Help (2)
Contato · FAQ

---

## Como adicionar uma página

Cada página segue este template:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="ch-page" content="ID-DA-PAGINA">
  <meta name="ch-base" content="../../">
  <link rel="icon" type="image/svg+xml" href="../../favicon.svg">
  <title>Nome · Casa Hacker DS</title>
  <link rel="stylesheet" href="../../styles.css">
</head>
<body>
<main class="main">
  <!-- conteúdo -->
</main>
<script src="../../shell.js"></script>
<script src="../../components.js"></script>
</body>
</html>
```

Depois, em `shell.js`, adicione o item no `navConfig`. A sidebar atualiza automaticamente em todas as páginas.

Para geração em batch, use os scripts em `scripts/` (rodar com `py scripts/gen_<seção>.py`).

---

## Stack técnico

| Camada | Tech |
|---|---|
| HTML | Semântico, vanilla |
| CSS | Custom properties (sem Sass/PostCSS) |
| JS | Vanilla, modular (shell.js + components.js) |
| Fontes | WOFF2 self-hosted (IBM Plex Mono, Roboto Flex variable, VT323) |
| Ícones | SVG inline (sem icon fonts) |
| Build | **Zero** — funciona em qualquer servidor estático |
| Deploy | GitHub Pages (workflow incluso) |
| Acessibilidade | WCAG 2.1 AA, ARIA APG |

---

## Performance

- **Bundle total:** ~2 MB (incluindo as 3 famílias de fontes self-hosted)
- **HTML por página:** 5-25 KB
- **CSS:** 1 arquivo único (~50 KB) — bem cacheável
- **JS:** 2 arquivos (~15 KB) — bem cacheável
- **Fontes WOFF2:** 996 KB (62% menores que TTF)
- **Sem build step:** edita → salva → recarrega

---

## Componentes JS interativos

`components.js` registra automaticamente:

| Componente | API |
|---|---|
| Accordion | `<div class="accordion" data-mode="single\|multi">` |
| Tabs | `<div role="tablist">` + `<button role="tab">` |
| Modal | `<button data-modal-open="id">` + `<div class="modal-backdrop" id="...">` |
| Dropdown | `<div class="dropdown">` + `.dropdown-trigger` + `.dropdown-menu` |
| Notification | `<div class="notification">` (auto-dismiss) |
| Toast (programático) | `window.CHDS.toast({title, message, kind, timeout})` |
| Copy code | Botão `copy` automático em todo `.code-snippet` |

---

## Theme

Toggle via botão flutuante (canto inferior direito). Inicial respeita `prefers-color-scheme` do SO. Persistido em `localStorage`.

```js
// Trocar via código:
document.documentElement.setAttribute('data-theme', 'dark');
```

---

## Acessibilidade

- ✓ WCAG 2.1 AA em todos os componentes
- ✓ ARIA APG aplicado (tabs, dialogs, listbox, accordion)
- ✓ Foco visível 2px em todos os interativos
- ✓ Skip-link "pular pra conteúdo"
- ✓ `prefers-reduced-motion` respeitado globalmente
- ✓ Contraste mínimo 4.5:1 em todos os pares texto/fundo
- ✓ Navegação 100% por teclado (Tab, setas, Esc, Enter, atalho `/`)
- ✓ Áreas de toque ≥ 44×44px

---

## Licença

- **Código:** MIT
- **Conteúdo de marca:** CC BY-SA 4.0

---

## Links

- **Site:** https://casahacker.github.io/design-system/
- **Repo:** https://github.com/casahacker/design-system
- **Issues:** https://github.com/casahacker/design-system/issues
- **Carbon (upstream):** https://carbondesignsystem.com/

---

made with ◆ in br
