# PR

## O que muda

<!-- Descrição curta. Link pra issue se aplicável: Closes #X -->

## Tipo

- [ ] 🐛 Bugfix
- [ ] ✨ Feature nova
- [ ] 🧩 Componente novo
- [ ] 📝 Docs
- [ ] ♻️ Refactor
- [ ] 🎨 Visual / identidade
- [ ] ⚡ Performance
- [ ] ♿ Acessibilidade

## Checklist

### Código
- [ ] CSS no `styles.css` (sem `<style>` em página, sem `style="..."` inline)
- [ ] JS no `components.js` ou `shell.js` (sem `<script>` inline)
- [ ] Sem dependências externas (zero-build mantido)
- [ ] Tokens semânticos usados (não hex cru)

### Design
- [ ] Funciona em light + dark
- [ ] Funciona em mobile (≤600px) e desktop (≥1024px)
- [ ] Spacing em múltiplos do BIT (8px)
- [ ] Identidade Casa Hacker preservada

### Acessibilidade (se componente)
- [ ] Operável só com teclado
- [ ] Foco visível 2px
- [ ] Contraste ≥ 4.5:1 em texto
- [ ] ARIA APG aplicado
- [ ] `prefers-reduced-motion` respeitado

### Docs
- [ ] Página de doc criada/atualizada
- [ ] TOC + 10 seções padrão (overview, variants, sizes, states, anatomy, behaviors, modifiers, usage, a11y, code) se componente
- [ ] Listado em `pages/components/index.html` (se componente)
- [ ] Adicionado ao `navConfig` do `shell.js` (se página nova)

### Screenshots (se UI)

<!-- Antes / depois, light + dark -->
