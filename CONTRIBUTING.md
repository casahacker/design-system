# Contribuindo com o Casa Hacker Design System

Obrigado pelo interesse em contribuir! Este documento cobre o básico — pra detalhes profundos, veja a [seção Contributing no site](https://casahacker.github.io/design-system/pages/contributing/index.html).

## Decisões arquiteturais (não negociáveis)

1. **Zero-build** — HTML, CSS, JS vanilla. Sem npm, bundler, Sass, framework. Editar = salvar = funciona.
2. **Tokens semânticos** — toda cor/spacing/tipografia via `var(--token)`, nunca hex cru.
3. **WCAG 2.1 AA** — acessibilidade não é opcional.
4. **BIT-aligned** — múltiplos de 8px em tudo.
5. **pt-br caixa baixa** — UI em pt-br, títulos e labels em caixa baixa.

## Fluxo

```bash
# 1. Fork no GitHub
# 2. Clone seu fork
git clone https://github.com/SEU_USUARIO/design-system.git
cd design-system

# 3. Cria branch
git checkout -b feat/sua-feature

# 4. Preview local
py -m http.server 8000
# abre http://localhost:8000

# 5. Faz mudanças. Se for página gerada (em pages/), edita o
# script correspondente em scripts/ e roda:
py scripts/gen_<nome>.py

# 6. Commit + push
git add .
git commit -m "feat: descrição clara"
git push origin feat/sua-feature

# 7. Abre PR
```

## Onde mexer

| Quer mudar | Edite |
|---|---|
| Token de cor / spacing | `styles.css` (seção 02 · DESIGN TOKENS) |
| Componente CSS | `styles.css` (seção 07 · COMPONENTS) |
| Componente JS interativo | `components.js` |
| Header / sidebar / theme | `shell.js` |
| Conteúdo de página | regenera via `scripts/gen_*.py` ou edita HTML direto |
| Nova página | `scripts/gen_*.py` + `navConfig` em `shell.js` |
| Adicionar componente | `styles.css` + `components.js` (se interativo) + `scripts/gen_components_*.py` + `navConfig` em `shell.js` + listar em `pages/components/index.html` |

## Checklist de PR

Antes de abrir PR, confirme:

- [ ] Funciona em light + dark
- [ ] Funciona em mobile (≤600px) e desktop (≥1024px)
- [ ] Zero `<style>` ou `style="..."` em página (sempre via classe)
- [ ] Tokens semânticos usados (sem `#XXXXXX` cru)
- [ ] Foco visível, navegação por teclado
- [ ] Tem doc na página correspondente
- [ ] Spacing em múltiplos de 8px

## Tom de voz

Veja [content & voice](https://casahacker.github.io/design-system/pages/guidelines/content.html).

Resumo:
- Direto, ativo, brasileiro
- Caixa baixa em títulos e labels
- Verbos no infinitivo em botões ("salvar", não "salvar alterações")
- Sem jargão desnecessário

## Reportando bugs

Use o template de [bug report](https://github.com/casahacker/design-system/issues/new?template=bug.yml).

## Propondo componente

Use o template de [component proposal](https://github.com/casahacker/design-system/issues/new?template=component-proposal.yml). Discuta antes de codar.

## Código de conduta

Ver [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md). Resumo: respeito mútuo, foco no problema, sem ataques pessoais.

## Licença

Ao contribuir, você concorda em licenciar sua contribuição sob:
- MIT pro código
- Creative Commons BY-SA 4.0 pro conteúdo de marca
