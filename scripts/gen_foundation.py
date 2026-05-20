"""Gera about (3) + guidelines (4) + elements remanescentes (5)."""
from common import page, sec, demo, do_dont, code, checklist, table, grid, related, write, anatomy

# =============================================================================
# ABOUT (3 pages, index já existe)
# =============================================================================
write("pages/about/principles.html", page(
    "principles", "Princípios",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">sobre</a><span class="sep">/</span>princípios',
    "Os 5 princípios que guiam todas as decisões de design no CHDS. Servem de filtro quando o caminho não é óbvio.",
    "".join([
        sec("p1", "acessível por padrão", "01", '<p class="t-body-02 t-secondary prose">Componente que não passa em WCAG 2.1 AA não entra no sistema. Foco visível, contraste mínimo 4.5:1 em texto, alvos de toque 44×44px, navegação por teclado e leitor de tela. Acessibilidade não é feature opcional — é qualidade de base.</p>'),
        sec("p2", "bit-aligned", "02", '<p class="t-body-02 t-secondary prose">O BIT (8px) é a unidade primitiva de tudo: spacing, sizing, ícones, grid, divisores. Múltiplos de 8 (com 4 e 2 como divisores excepcionais) garantem ritmo visual consistente entre interfaces, impressos e merchandise.</p>'),
        sec("p3", "híbrido digital-físico", "03", '<p class="t-body-02 t-secondary prose">Casa Hacker faz hackathons, eventos, oficinas. O sistema atende produto digital E papelaria, sinalização, brindes. Tokens valem nos dois mundos — um adesivo segue a mesma grade que um botão.</p>'),
        sec("p4", "aberto e modificável", "04", '<p class="t-body-02 t-secondary prose">Forkado do Carbon (Apache 2.0) e mantido em GitHub público. Submarcas estendem tokens sem fragmentar o sistema. Qualquer pessoa pode propor melhorias via PR.</p>'),
        sec("p5", "brasileiro de raiz", "05", '<p class="t-body-02 t-secondary prose">Documentação em pt-br. Exemplos refletem a realidade brasileira. Submarcas falam dos contextos atendidos. O sistema não é tradução de Carbon: é Carbon recontextualizado.</p>'),
    ]),
    tags=[{"cls": "tag--code", "label": "foundational"}],
    toc=[{"id":"p1","label":"Acessível por padrão"},{"id":"p2","label":"BIT-aligned"},{"id":"p3","label":"Híbrido digital-físico"},{"id":"p4","label":"Aberto e modificável"},{"id":"p5","label":"Brasileiro de raiz"}],
))

write("pages/about/who-uses.html", page(
    "who-uses", "Quem usa",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">sobre</a><span class="sep">/</span>quem usa',
    "Times internos da Casa Hacker, parceiros externos e a comunidade open-source que constrói pra mesma audiência.",
    "".join([
        sec("internal", "uso interno", "01",
            grid([
                {"title":"portal casa hacker","desc":"Site institucional, blog, materiais didáticos."},
                {"title":"plataforma hackerclubes","desc":"App de gestão dos clubes nas escolas."},
                {"title":"internet segura","desc":"Conteúdo educativo digital + impresso."},
            ])),
        sec("partners", "parceiros e financiadores", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">Organizações que constroem soluções alinhadas com a missão da Casa Hacker podem adotar o CHDS pra acelerar entregas e garantir consistência.</p>' +
            grid([
                {"title":"governo","desc":"Secretarias e órgãos públicos com pautas de tecnologia social."},
                {"title":"ongs","desc":"Terceiro setor focado em educação tech e inclusão digital."},
                {"title":"empresas","desc":"Patrocinadores com programas de impacto social comunitário."},
            ])),
        sec("community", "comunidade open-source", "03",
            '<p class="t-body-02 t-secondary prose">Fork público no GitHub. Devs e designers da comunidade podem usar componentes, propor melhorias e adaptar pra projetos próprios. Licença MIT no código, CC BY-SA no conteúdo de marca.</p>'),
    ]),
    toc=[{"id":"internal","label":"Uso interno"},{"id":"partners","label":"Parceiros"},{"id":"community","label":"Comunidade"}],
))

write("pages/about/ecosystem.html", page(
    "ecosystem", "Ecossistema",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">sobre</a><span class="sep">/</span>ecossistema',
    "Mapa de como o CHDS se conecta com Carbon, com os produtos da Casa Hacker e com a comunidade externa.",
    "".join([
        sec("carbon", "relação com ibm carbon", "01",
            '<p class="t-body-02 t-secondary mb-05 prose">CHDS adota a <strong>estrutura</strong> do Carbon — tokens semânticos, escala de spacing, sistema de grid, princípios de a11y — e <strong>reskinna</strong> com a paleta, tipografia e linguagem visual Casa Hacker.</p>' +
            table(["Carbon","CHDS"], [
                ["Blue 60 (#0F62FE) primary","Code Green (#32FA96)"],
                ["IBM Plex Sans","Roboto Flex + IBM Plex Mono"],
                ["8px base unit","BIT (8px) — mesmo conceito, naming próprio"],
                ["Carbon Icons","Iconography BIT-aligned (em construção)"],
                ["Gray 10 / Gray 100 themes","Console / Dos themes"],
            ])),
        sec("submarcas", "submarcas", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">5 marcas-filha que herdam o sistema e estendem com tokens próprios. Ver a seção <a class="link" href="../submarcas/index.html">submarcas</a>.</p>'),
        sec("community", "aberto à comunidade", "03",
            '<p class="t-body-02 t-secondary prose">Repositório público em <a class="link" href="https://github.com/casahacker/design-system" target="_blank" rel="noopener">github.com/casahacker/design-system</a>. Issues, PRs e discussões são bem-vindos.</p>'),
    ]),
    toc=[{"id":"carbon","label":"Relação com Carbon"},{"id":"submarcas","label":"Submarcas"},{"id":"community","label":"Aberto à comunidade"}],
))

# =============================================================================
# GUIDELINES (4 pages)
# =============================================================================
write("pages/guidelines/index.html", page(
    "g-overview", "Guidelines",
    '<a href="../../index.html">home</a><span class="sep">/</span>guidelines',
    "Diretrizes transversais que valem pra todos os componentes e padrões: acessibilidade, conteúdo & voz e uso responsável de IA.",
    "".join([
        sec("a11y", "accessibility", "01",
            '<p class="t-body-02 t-secondary mb-05 prose">Critérios WCAG 2.1 AA em todo componente, com auditoria contínua. Cobre contraste, foco, teclado, ARIA, motion e densidade.</p>' +
            '<a class="link link--standalone" href="accessibility.html">ler guidelines de a11y</a>'),
        sec("content", "content & voice", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">Tom Casa Hacker: direto, ativo, brasileiro, sem firula. UI fala pt-br em caixa baixa, microcopy curto, sem jargão desnecessário.</p>' +
            '<a class="link link--standalone" href="content.html">ler guidelines de conteúdo</a>'),
        sec("ai", "casa hacker for ai", "03",
            '<p class="t-body-02 t-secondary mb-05 prose">Princípios pra usar IA generativa em produtos: transparência, divulgação, opt-in, fontes citáveis, controle do usuário.</p>' +
            '<a class="link link--standalone" href="ai.html">ler guidelines de ia</a>'),
    ]),
    toc=[{"id":"a11y","label":"Accessibility"},{"id":"content","label":"Content & voice"},{"id":"ai","label":"Casa Hacker for AI"}],
))

write("pages/guidelines/accessibility.html", page(
    "g-a11y", "Accessibility",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">guidelines</a><span class="sep">/</span>accessibility',
    "CHDS é WCAG 2.1 AA por padrão. Esta página documenta os critérios, padrões de teclado e ARIA aplicados em todos os componentes.",
    "".join([
        sec("a11y-bar", "barra de acessibilidade — obrigatória", "00 · base",
            '<p class="t-body-02 t-secondary mb-05 prose">Todo produto Casa Hacker <strong>deve incluir</strong> a barra de acessibilidade oficial (<a class="link" href="https://github.com/casahacker/barra-acessibilidade" target="_blank" rel="noopener">github.com/casahacker/barra-acessibilidade ↗</a>), que cobre 12 features WCAG-aligned + integração VLibras. Detalhes de integração na página <a class="link" href="../patterns/global-header.html">global header</a>.</p>' +
            checklist([
                "Tema (claro/escuro/alto contraste) + 3 tamanhos de fonte (14/16/18)",
                "Fonte Atkinson Hyperlegible pra dislexia",
                "Régua de leitura, modo foco, cursor ampliado",
                "VLibras (Língua Brasileira de Sinais) oficial do governo",
                "Pausa de animação (WCAG 2.3.3), foco realçado (2.4.7), alvos ampliados (2.5.8)",
                "Carrega via CDN jsDelivr — peso ~30KB minificado",
                "Este design system já inclui automaticamente em todas as páginas",
            ])),
        sec("contrast", "contraste", "01 · 1.4.3",
            '<p class="t-body-02 t-secondary mb-05 prose">Texto normal exige razão 4.5:1 contra o fundo. Texto grande (18pt+ regular, 14pt+ bold) exige 3:1. Bordas e ícones também 3:1.</p>' +
            table(["par","razão","aa text","aa large"], [
                ["text-primary / background (light)","11.7:1","✓","✓"],
                ["text-secondary / background (light)","7.2:1","✓","✓"],
                ["text-on-color / background-brand","11.5:1","✓","✓"],
                ["text-primary / background (dark)","13.4:1","✓","✓"],
                ["text-secondary / background (dark)","9.1:1","✓","✓"],
                ["support-error / background (light)","5.2:1","✓","✓"],
            ])),
        sec("keyboard", "navegação por teclado", "02 · 2.1.1",
            '<p class="t-body-02 t-secondary mb-05 prose">Todo elemento interativo é acessível via Tab. Componentes complexos seguem ARIA Authoring Practices.</p>' +
            table(["componente","tecla","ação"], [
                ["Tabs","← / →","move foco entre tabs"],
                ["Tabs","Home / End","primeiro / último tab"],
                ["Dropdown","↓ / ↑","navega opções"],
                ["Dropdown","Enter / Space","abre / seleciona"],
                ["Modal","Esc","fecha"],
                ["Modal","Tab","cycla com focus trap"],
                ["Accordion","Enter / Space","expande / colapsa"],
                ["Sidebar nav","/","foca busca"],
            ])),
        sec("focus", "foco visível", "03 · 2.4.7",
            '<p class="t-body-02 t-secondary mb-05 prose">Todo elemento focado tem indicação visual evidente. <code class="code-inline">outline: 2px solid var(--focus)</code> ou <code class="code-inline">box-shadow: inset 0 0 0 2px var(--focus)</code>. Nunca <code class="code-inline">outline: none</code> sem fallback.</p>' +
            demo('<div class="row"><button class="btn btn--primary" style="outline: 2px solid var(--focus); outline-offset: 2px;">botão com foco</button><a class="link" style="outline: 2px solid var(--focus); outline-offset: 2px;" href="#">link com foco</a></div>')),
        sec("aria", "aria & semântica", "04 · 4.1.2",
            checklist([
                "HTML semântico antes de ARIA — usar &lt;button&gt;, &lt;nav&gt;, &lt;main&gt;, &lt;article&gt; em vez de divs",
                "aria-label em controles sem texto visível",
                "aria-expanded em toggles (accordion, dropdown)",
                'aria-current="page" no link ativo da nav',
                'aria-live="polite" em toasts/notificações dinâmicas',
                'role="dialog" + aria-modal="true" em modais',
                'role="tablist", role="tab", role="tabpanel" em tabs',
            ])),
        sec("motion", "motion & reduced motion", "05 · 2.3.3",
            '<p class="t-body-02 t-secondary prose">Animações longas (>200ms) e parallax são respeitados via <code class="code-inline">prefers-reduced-motion</code>. Durações Carbon: fast-01 (70ms) até slow-02 (700ms).</p>'),
        sec("targets", "áreas de toque", "06 · 2.5.5",
            '<p class="t-body-02 t-secondary prose">Alvos interativos têm no mínimo 44×44px (botões padrão são 48px de altura). Tamanhos menores (small) só em toolbars internas com espaçamento extra.</p>'),
        sec("forms", "formulários", "07 · 3.3.x",
            checklist([
                "Todo input tem &lt;label&gt; associado (for + id)",
                "Mensagens de erro são programaticamente associadas (aria-describedby)",
                "Campos obrigatórios marcados visualmente E semanticamente (required)",
                "Erros não são apenas cor — incluem ícone e texto",
                "Helper text antes do erro, não substituído por ele",
            ])),
        sec("checklist", "checklist por componente", "08",
            '<p class="t-body-02 t-secondary mb-05 prose">Antes de qualquer componente entrar no sistema, passa por este checklist.</p>' +
            checklist([
                "Operável só com teclado (sem mouse, sem touch)",
                "Visível ao zoom 200% sem perda de função",
                "Funciona em leitor de tela (NVDA, VoiceOver)",
                "Estado focado é evidente visualmente",
                "Contraste verificado em ambos os temas (light e dark)",
                "prefers-reduced-motion respeitado",
                "Padrão ARIA aplicado conforme APG",
            ])),
    ]),
    tags=[{"cls":"tag--blue","label":"wcag 2.1 aa"}],
    toc=[{"id":"a11y-bar","label":"Barra de acessibilidade (obrigatória)"},{"id":"contrast","label":"Contraste"},{"id":"keyboard","label":"Teclado"},{"id":"focus","label":"Foco visível"},{"id":"aria","label":"ARIA & semântica"},{"id":"motion","label":"Motion & reduced motion"},{"id":"targets","label":"Áreas de toque"},{"id":"forms","label":"Formulários"},{"id":"checklist","label":"Checklist por componente"}],
))

write("pages/guidelines/content.html", page(
    "g-content", "Content & voice",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">guidelines</a><span class="sep">/</span>content & voice',
    "Como a Casa Hacker fala em interfaces: direta, ativa, em pt-br, sem jargão. Microcopy curto, comandos em verbo, erros úteis.",
    "".join([
        sec("tone", "tom de voz", "01",
            '<div class="grid-2"><div class="tile tile--bordered"><h4>somos</h4><ul class="checklist"><li>diretos · sem rodeio</li><li>ativos · "salvar" em vez de "as alterações foram salvas"</li><li>brasileiros · pt-br informal mas profissional</li><li>técnicos sem jargão · "json" sim, "monetização programática" não</li></ul></div><div class="tile tile--bordered"><h4>não somos</h4><ul class="checklist"><li>solenes · "prezado usuário" → "olá"</li><li>passivos · "houve um erro" → "deu ruim, tenta de novo"</li><li>genéricos · "operação concluída" → "post publicado"</li><li>infantis · "ops!" exagerado fica antipático</li></ul></div></div>'),
        sec("case", "caixa baixa", "02",
            '<p class="t-body-02 t-secondary prose">Títulos, labels e botões em caixa baixa. CAIXA ALTA só pra labels técnicos (// CODE, // META). Nomes próprios mantêm capitalização: Casa Hacker, PerifaImpacto, IBM Carbon.</p>'),
        sec("verbs", "verbos em ação", "03",
            table(["contexto","evita","prefere"], [
                ["botão de salvar","salvar alterações","salvar"],
                ["botão de envio","enviar formulário","enviar"],
                ["confirmação","operação foi concluída","tudo certo · enviado"],
                ["cancelar","cancelar e voltar","cancelar"],
                ["próxima etapa","ir pra próxima etapa","próximo"],
            ])),
        sec("errors", "erros úteis", "04",
            '<p class="t-body-02 t-secondary mb-05 prose">Erro diz (1) o que aconteceu, (2) por que aconteceu se ajudar, (3) o que fazer agora.</p>' +
            demo('<div class="notification notification--error max-w-xs"><div class="notification-icon">⚠</div><div class="notification-body"><strong>não rolou enviar</strong><p>o servidor demorou pra responder. tenta de novo em alguns segundos.</p></div></div>')),
        sec("examples", "exemplos comparados", "05",
            do_dont(
                ['"salvar" como label de botão primary','"cancelar" simples, sem "voltar e cancelar"','"deu ruim, tenta de novo" em erro de rede','"publicar post" deixa claro o que será publicado'],
                ['"submeter formulário" — usar "enviar"','"prezado usuário" — usar "olá" ou nada','"erro 500 internal server error" — texto técnico cru','"clique aqui" — usa o verbo da ação'],
            )),
    ]),
    toc=[{"id":"tone","label":"Tom de voz"},{"id":"case","label":"Caixa baixa"},{"id":"verbs","label":"Verbos em ação"},{"id":"errors","label":"Erros úteis"},{"id":"examples","label":"Exemplos comparados"}],
))

write("pages/guidelines/ai.html", page(
    "g-ai", "Casa Hacker for AI",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">guidelines</a><span class="sep">/</span>casa hacker for ai',
    "Princípios pra integrar IA generativa em produtos Casa Hacker de forma transparente, responsável e útil.",
    "".join([
        sec("principles", "princípios", "01",
            '<div class="grid-2"><div class="tile tile--bordered"><h4>1. transparência</h4><p>Usuário sempre sabe quando está interagindo com IA. Indicador visual + texto explícito.</p></div><div class="tile tile--bordered"><h4>2. opt-in</h4><p>Funcionalidades de IA são opcionais. Usuário ativa, não vem ligado por padrão.</p></div><div class="tile tile--bordered"><h4>3. fontes citáveis</h4><p>Quando a IA cita fato, mostra a fonte. Resposta sem fonte é especulação.</p></div><div class="tile tile--bordered"><h4>4. correção pelo humano</h4><p>Usuário pode editar, refazer, desfazer. IA propõe — usuário decide.</p></div></div>'),
        sec("disclosure", "divulgação", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">Conteúdo gerado por IA recebe marcação visual: tag com ícone, ou borda colorida característica.</p>' +
            demo('<div class="row"><span class="tag tag--purple-ai">gerado por ia</span><span class="tag tag--purple-ai">resumido por ia</span><span class="tag tag--purple-ai">traduzido por ia</span></div>')),
        sec("control", "controle do usuário", "03",
            checklist([
                'Sempre oferecer "regenerar" e "editar"',
                'Mostrar "rascunho" antes de aplicar — nada gerado é aplicado sem confirmação',
                'Histórico de versões pra reverter',
                'Botão de "explicar essa sugestão" quando faz sentido',
            ])),
        sec("patterns", "padrões visuais", "04",
            '<p class="t-body-02 t-secondary prose">Cor de destaque pra IA: <strong>--ch-purple</strong> (#AA78E6). Mesma cor do PerifaImpacto — porque tecnologia de ponta na periferia. Borda gradiente verde→roxo opcional pra destacar áreas de IA.</p>'),
    ]),
    tags=[{"cls":"tag--purple","label":"novo"}],
    toc=[{"id":"principles","label":"Princípios"},{"id":"disclosure","label":"Divulgação"},{"id":"control","label":"Controle do usuário"},{"id":"patterns","label":"Padrões visuais"}],
))

# =============================================================================
# FOUNDATIONS (5 pages: spacing, grid, iconography, motion, themes)
# =============================================================================
write("pages/elements/spacing.html", page(
    "spacing", "Spacing · BIT",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="../about/index.html">foundations</a><span class="sep">/</span>spacing',
    "O BIT (8px) é a unidade primitiva. Toda a escala de spacing são múltiplos ou frações dele, garantindo ritmo visual consistente em digital e físico.",
    "".join([
        sec("scale", "escala", "01 · 13 tokens",
            '<p class="t-body-02 t-secondary mb-05 prose">Spacing-01 a spacing-13. Os primeiros 2 são frações do BIT (2px, 4px); os demais são múltiplos.</p>' +
            table(["token","valor","múltiplo do BIT","uso típico"], [
                ["--spacing-01","2px","¼ BIT","ajuste fino · ícones inline"],
                ["--spacing-02","4px","½ BIT","gap mínimo entre elementos"],
                ["--spacing-03","8px","1 BIT","padding compacto · gap default"],
                ["--spacing-04","12px","1.5","padding interno de form"],
                ["--spacing-05","16px","2","padding standard"],
                ["--spacing-06","24px","3","gap entre componentes"],
                ["--spacing-07","32px","4","gap entre seções"],
                ["--spacing-08","40px","5","padding generoso"],
                ["--spacing-09","48px","6","margin de seção"],
                ["--spacing-10","64px","8","main padding"],
                ["--spacing-11","80px","10","hero spacing"],
                ["--spacing-12","96px","12","margin entre macro-seções"],
                ["--spacing-13","160px","20","display spacing"],
            ])),
        sec("bit", "o bit", "02 · unidade primitiva",
            '<p class="t-body-02 t-secondary mb-05 prose">BIT = 8px. Por que 8? É divisível por 2 e 4, encaixa em telas retina (×2, ×3), e cria um grid invisível que conecta padding, sizing, ícones e linha-altura.</p>' +
            demo('<div style="display:grid;grid-template-columns:repeat(8,32px);gap:1px;background:var(--ch-code);padding:1px;width:fit-content;"><div style="background:var(--layer-01);height:32px"></div>'.join([""]*9) + '</div><p class="t-helper mt-04">8 BITs no horizontal · 32px cada · grid de 264px</p>')),
        sec("density", "modos de densidade", "03",
            '<p class="t-body-02 t-secondary mb-05 prose">Componentes podem assumir 3 densidades. Para usar, troque os tokens base por seus equivalentes denser.</p>' +
            table(["modo","altura input","altura btn","uso"], [
                ["compact","32px","32px","tabelas densas, toolbars"],
                ["default","40px","48px","produto padrão"],
                ["expressive","56px","64px","landings, formulários longos"],
            ])),
        sec("usage", "quando usar cada valor", "04",
            do_dont(
                ["Múltiplos do BIT — mesmo se for valor pequeno (8px sim, 7px não)","spacing-03 (8px) como gap default entre rows","spacing-09 (48px) como margin de section em desktop","spacing-05 (16px) como padding interno padrão"],
                ["Valores arbitrários (13px, 17px) — quebra o ritmo","spacing-01 / 02 em layouts macro","spacing-13 (160px) em mobile — quebra responsividade","spacings diferentes pra coisas iguais — gera inconsistência"],
            )),
        sec("code", "código", "05 · css",
            code('<span class="c">/* uso de spacing tokens */</span>\n<span class="k">.my-card</span> {\n  padding: <span class="k">var</span>(--spacing-05) <span class="k">var</span>(--spacing-06);\n  margin-bottom: <span class="k">var</span>(--spacing-07);\n  gap: <span class="k">var</span>(--spacing-04);\n}\n\n<span class="c">/* responsivo */</span>\n<span class="k">@media</span> (max-width: <span class="v">600px</span>) {\n  <span class="k">.my-card</span> { padding: <span class="k">var</span>(--spacing-04); }\n}')),
    ]),
    toc=[{"id":"scale","label":"Escala"},{"id":"bit","label":"O BIT"},{"id":"density","label":"Modos de densidade"},{"id":"usage","label":"Quando usar cada valor"},{"id":"code","label":"Código"}],
))

write("pages/elements/grid.html", page(
    "grid", "2x Grid",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="../about/index.html">foundations</a><span class="sep">/</span>2x grid',
    "Sistema de grid responsivo com colunas fluidas e gutters fixos. Baseado no 2x Grid do Carbon, alinhado ao BIT.",
    "".join([
        sec("breakpoints", "breakpoints", "01",
            table(["nome","largura","colunas","gutter","margin"], [
                ["sm","640px","4","16px","16px"],
                ["md","800px","8","16px","24px"],
                ["lg","1024px","12","16px","24px"],
                ["xl","1280px","12","24px","32px"],
                ["2xl","1440px+","12","24px","32px"],
            ])),
        sec("columns", "colunas", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">12 colunas em desktop, 8 em tablet, 4 em mobile. Gutter é constante; o que muda é a largura das colunas.</p>' +
            demo('<div style="display:grid;grid-template-columns:repeat(12,1fr);gap:16px;background:rgba(50,250,150,.1);padding:16px;">' + ''.join(f'<div style="background:var(--ch-code);height:48px;display:flex;align-items:center;justify-content:center;font:var(--code-01);color:var(--ch-dos)">{i+1}</div>' for i in range(12)) + '</div>')),
        sec("containers", "containers", "03",
            '<p class="t-body-02 t-secondary mb-05 prose">Largura máxima do conteúdo principal por breakpoint.</p>' +
            table(["token","valor"], [
                ["--container-sm","640px"],
                ["--container-md","800px"],
                ["--container-lg","1024px"],
                ["--container-xl","1280px"],
                ["--container-2xl","1440px"],
            ])),
        sec("usage", "quando usar", "04",
            do_dont(
                ["Layouts macro — sempre encaixar em colunas do grid","Componentes ocupando spans inteiros (col 1-6, col 7-12)","Container max-width pra evitar linhas de texto longas demais"],
                ["Posicionamento absoluto pra alinhar — usa grid","Larguras fixas em px arbitrários — usa fr ou span"],
            )),
        sec("code", "código", "05",
            code('<span class="c">/* usar grid-12 com tokens */</span>\n<span class="k">.layout</span> {\n  display: grid;\n  grid-template-columns: repeat(<span class="v">12</span>, <span class="v">1fr</span>);\n  gap: <span class="k">var</span>(--spacing-05);\n  max-width: <span class="k">var</span>(--container-xl);\n  margin: 0 auto;\n  padding: 0 <span class="k">var</span>(--spacing-06);\n}')),
    ]),
    toc=[{"id":"breakpoints","label":"Breakpoints"},{"id":"columns","label":"Colunas"},{"id":"containers","label":"Containers"},{"id":"usage","label":"Quando usar"},{"id":"code","label":"Código"}],
))

# --- Biblioteca real de 55 ícones disponíveis em assets/icons/sprite.svg
ICON_GROUPS = [
    ("Navigation", ["chevron-up","chevron-down","chevron-left","chevron-right","arrow-up","arrow-down","arrow-left","arrow-right","external"]),
    ("UI Controls", ["close","menu","more-horizontal","more-vertical","plus","minus","check","search","settings","filter"]),
    ("State & Feedback", ["info","warning","error","check-circle","help","loading"]),
    ("Content", ["document","folder","image","code","terminal","copy","link","download","upload","share"]),
    ("People & Communication", ["user","users","mail","phone","chat","bell"]),
    ("Privacy & Security", ["eye","eye-off","lock","unlock","shield"]),
    ("Time & Location", ["calendar","clock","location","globe"]),
    ("Actions", ["edit","trash","star","bookmark","github"]),
]
def _icon_cell(name):
    return (
        f'<div class="icon-cell" data-icon-name="{name}" title="clique pra copiar &quot;{name}&quot;">'
        f'<svg class="ico ico--24" aria-hidden="true"><use href="../../assets/icons/sprite.svg#{name}"/></svg>'
        f'<span class="icon-name">{name}</span>'
        f'</div>'
    )
def _icon_group(label, names):
    cells = "".join(_icon_cell(n) for n in names)
    return (
        f'<div style="margin-bottom:var(--spacing-07)">'
        f'<h3 class="t-h02" style="margin-bottom:var(--spacing-04)">{label} <span style="font:var(--code-01);color:var(--text-helper);margin-left:var(--spacing-03);text-transform:none">{len(names)}</span></h3>'
        f'<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:var(--spacing-03)">{cells}</div>'
        f'</div>'
    )
icons_html = "".join(_icon_group(lbl, names) for lbl, names in ICON_GROUPS)
total_icons = sum(len(names) for _, names in ICON_GROUPS)

write("pages/elements/iconography.html", page(
    "iconography", "Iconography",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="../about/index.html">foundations</a><span class="sep">/</span>iconography',
    f"Biblioteca de {total_icons} ícones BIT-aligned em SVG sprite. Grid 16×16px, traço 1.5px, currentColor por padrão. Zero icon font, zero dependência externa.",
    "".join([
        sec("library", f"biblioteca · {total_icons} ícones", "01 · sprite svg",
            '<p class="t-body-02 t-secondary mb-05 prose">Todos os ícones do sistema. Clique pra copiar o nome. Uso via <code class="code-inline">&lt;use href="../../assets/icons/sprite.svg#name"&gt;</code>.</p>' +
            icons_html),
        sec("sizes", "tamanhos", "02 · classes utility",
            '<p class="t-body-02 t-secondary mb-05 prose">Cinco tamanhos canônicos via classes. Ícones desenhados em grid de 16px com traço 1.5px otimizado para 16/20/24px.</p>' +
            demo(
                '<div class="row" style="gap: var(--spacing-06); align-items: center;">'
                '<div style="text-align:center"><svg class="ico ico--12" aria-hidden="true"><use href="../../assets/icons/sprite.svg#info"/></svg><div style="font:var(--code-01);color:var(--text-helper);margin-top:var(--spacing-02)">12</div></div>'
                '<div style="text-align:center"><svg class="ico" aria-hidden="true"><use href="../../assets/icons/sprite.svg#info"/></svg><div style="font:var(--code-01);color:var(--text-helper);margin-top:var(--spacing-02)">16 · default</div></div>'
                '<div style="text-align:center"><svg class="ico ico--20" aria-hidden="true"><use href="../../assets/icons/sprite.svg#info"/></svg><div style="font:var(--code-01);color:var(--text-helper);margin-top:var(--spacing-02)">20</div></div>'
                '<div style="text-align:center"><svg class="ico ico--24" aria-hidden="true"><use href="../../assets/icons/sprite.svg#info"/></svg><div style="font:var(--code-01);color:var(--text-helper);margin-top:var(--spacing-02)">24</div></div>'
                '<div style="text-align:center"><svg class="ico ico--32" aria-hidden="true"><use href="../../assets/icons/sprite.svg#info"/></svg><div style="font:var(--code-01);color:var(--text-helper);margin-top:var(--spacing-02)">32</div></div>'
                '</div>'
            ) +
            table(["classe","px","uso"], [
                [".ico--12","12px","inline em label-01"],
                [".ico (default)","16px","inline em texto body, botões small"],
                [".ico--20","20px","botões standard, form fields"],
                [".ico--24","24px","menus, nav items, headers"],
                [".ico--32","32px","header brand, ações destacadas"],
            ])),
        sec("color", "cor · currentColor", "03",
            '<p class="t-body-02 t-secondary mb-05 prose">Ícones herdam a cor do contexto via <code class="code-inline">currentColor</code>. Helpers para cores específicas.</p>' +
            demo(
                '<div class="row" style="gap: var(--spacing-06); align-items: center;">'
                '<div style="text-align:center;color:var(--text-primary)"><svg class="ico ico--24" aria-hidden="true"><use href="../../assets/icons/sprite.svg#star"/></svg><div style="font:var(--code-01);color:var(--text-helper);margin-top:var(--spacing-02)">currentColor</div></div>'
                '<div style="text-align:center"><svg class="ico ico--24 ico--code" aria-hidden="true"><use href="../../assets/icons/sprite.svg#star"/></svg><div style="font:var(--code-01);color:var(--text-helper);margin-top:var(--spacing-02)">.ico--code</div></div>'
                '<div style="text-align:center"><svg class="ico ico--24 ico--muted" aria-hidden="true"><use href="../../assets/icons/sprite.svg#star"/></svg><div style="font:var(--code-01);color:var(--text-helper);margin-top:var(--spacing-02)">.ico--muted</div></div>'
                '<div style="text-align:center;color:var(--support-error)"><svg class="ico ico--24" aria-hidden="true"><use href="../../assets/icons/sprite.svg#error"/></svg><div style="font:var(--code-01);color:var(--text-helper);margin-top:var(--spacing-02)">inherited</div></div>'
                '</div>'
            )),
        sec("h-symbol", "h símbolo · marca casa hacker", "04",
            '<p class="t-body-02 t-secondary mb-05 prose">O H estilizado é o ícone-assinatura da marca. Sempre num grid 3×3 de quadrados, com 5 quadrados ativos no padrão H. Modificadores opcionais com animações CSS (todos respeitam prefers-reduced-motion).</p>' +
            demo('<div class="row" style="gap: var(--spacing-07);"><div class="h-symbol h-symbol--dark" style="width:32px;height:32px"><span class="on"></span><span></span><span class="on"></span><span></span><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span class="on"></span></div><div class="h-symbol h-symbol--dark" style="width:64px;height:64px"><span class="on"></span><span></span><span class="on"></span><span></span><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span class="on"></span></div><div class="h-symbol h-symbol--dark" style="width:128px;height:128px"><span class="on"></span><span></span><span class="on"></span><span></span><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span class="on"></span></div></div>')),
        sec("h-symbol-variants", "variações animadas", "05",
            demo('<div class="grid-3"><div style="text-align:center"><div class="h-symbol h-symbol--dark h-symbol--loading" style="width:64px;height:64px;margin:0 auto var(--spacing-04)"><span class="on"></span><span></span><span class="on"></span><span></span><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span class="on"></span></div><div class="t-helper">--loading</div></div><div style="text-align:center"><div class="h-symbol h-symbol--dark h-symbol--breathing" style="width:64px;height:64px;margin:0 auto var(--spacing-04)"><span class="on"></span><span></span><span class="on"></span><span></span><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span class="on"></span></div><div class="t-helper">--breathing</div></div><div style="text-align:center"><div class="h-symbol h-symbol--dark h-symbol--hover" style="width:64px;height:64px;margin:0 auto var(--spacing-04);cursor:pointer"><span class="on"></span><span></span><span class="on"></span><span></span><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span class="on"></span></div><div class="t-helper">--hover (passa mouse)</div></div></div>')),
        sec("usage", "quando usar", "06",
            do_dont(
                ["Ícones reforçam significado de texto, não substituem","Múltiplos de 8px (16, 24, 32, 40, 48)","Cor herdada do contexto (currentColor) sempre que possível","Traço consistente · usa o sprite oficial","Tap-target mínimo 44×44px em mobile"],
                ["Ícone sozinho pra ação crítica — sempre acompanhe de label/aria-label","Tamanhos arbitrários (19px, 21px)","Misturar estilos diferentes (filled + outlined) sem critério","Cores cruas em ícones — usa currentColor ou tokens","Misturar ícones de bibliotecas diferentes"],
            )),
        sec("code", "código", "07",
            code('<span class="c">&lt;!-- 1. usando o sprite (recomendado) --&gt;</span>\n&lt;<span class="k">svg</span> <span class="v">class</span>=<span class="s">"ico ico--24"</span> <span class="v">aria-hidden</span>=<span class="s">"true"</span>&gt;\n  &lt;<span class="k">use</span> <span class="v">href</span>=<span class="s">"/assets/icons/sprite.svg#search"</span>/&gt;\n&lt;/<span class="k">svg</span>&gt;\n\n<span class="c">&lt;!-- 2. com label acessível --&gt;</span>\n&lt;<span class="k">button</span> <span class="v">aria-label</span>=<span class="s">"buscar"</span>&gt;\n  &lt;<span class="k">svg</span> <span class="v">class</span>=<span class="s">"ico"</span> <span class="v">aria-hidden</span>=<span class="s">"true"</span>&gt;\n    &lt;<span class="k">use</span> <span class="v">href</span>=<span class="s">"#search"</span>/&gt;\n  &lt;/<span class="k">svg</span>&gt;\n&lt;/<span class="k">button</span>&gt;\n\n<span class="c">/* CSS: herda cor do parent */</span>\n<span class="k">.btn</span> {\n  color: <span class="k">var</span>(--text-primary);\n}\n<span class="k">.btn</span> <span class="k">.ico</span> {\n  <span class="c">/* já é currentColor por default */</span>\n}')),
    ]),
    toc=[{"id":"library","label":"Biblioteca"},{"id":"sizes","label":"Tamanhos"},{"id":"color","label":"Cor"},{"id":"h-symbol","label":"H símbolo"},{"id":"h-symbol-variants","label":"Variações"},{"id":"usage","label":"Quando usar"},{"id":"code","label":"Código"}],
))

# --- Motion demo: bloco que anima ao clicar/hover, mostrando cada token visualmente
def _motion_demo(label, var_name, duration_or_ease, kind):
    # kind = 'duration' ou 'ease'
    if kind == 'duration':
        anim = f'transition: transform {duration_or_ease} var(--ease-productive)'
    else:
        anim = f'transition: transform 600ms {duration_or_ease}'
    return (
        f'<div class="motion-demo">'
        f'<div class="motion-demo-label">{label}</div>'
        f'<div class="motion-demo-var">{var_name}</div>'
        f'<button type="button" data-motion-play class="motion-demo-stage">'
        f'<span data-motion-box class="motion-demo-box" style="{anim}"></span>'
        f'<span class="motion-demo-play">▶ play</span>'
        f'</button>'
        f'</div>'
    )

motion_durations_demo = '<div class="grid-3" style="gap:var(--spacing-04)">' + ''.join([
    _motion_demo('Fast 01', '--duration-fast-01', '70ms', 'duration'),
    _motion_demo('Fast 02', '--duration-fast-02', '110ms', 'duration'),
    _motion_demo('Moderate 01', '--duration-moderate-01', '150ms', 'duration'),
    _motion_demo('Moderate 02', '--duration-moderate-02', '240ms', 'duration'),
    _motion_demo('Slow 01', '--duration-slow-01', '400ms', 'duration'),
    _motion_demo('Slow 02', '--duration-slow-02', '700ms', 'duration'),
]) + '</div>'

motion_easings_demo = '<div class="grid-3" style="gap:var(--spacing-04)">' + ''.join([
    _motion_demo('Productive', '--ease-productive', 'cubic-bezier(0.2,0,0.38,0.9)', 'ease'),
    _motion_demo('Expressive', '--ease-expressive', 'cubic-bezier(0.4,0.14,0.3,1)', 'ease'),
    _motion_demo('Entrance', '--ease-entrance', 'cubic-bezier(0,0,0.38,0.9)', 'ease'),
    _motion_demo('Exit', '--ease-exit', 'cubic-bezier(0.2,0,1,0.9)', 'ease'),
    _motion_demo('Standard', '--ease-standard', 'cubic-bezier(0.5,0,0.1,1)', 'ease'),
]) + '</div>'

write("pages/elements/motion.html", page(
    "motion", "Motion",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="../about/index.html">foundations</a><span class="sep">/</span>motion',
    "Animações com propósito: curtas, com easing certo, e sempre respeitando prefers-reduced-motion. Tokens Carbon de duration e easing — demonstrados aqui com animações ao vivo (clique nos blocos pra ver).",
    "".join([
        sec("durations", "durations · live", "01 · 6 tokens",
            '<p class="t-body-02 t-secondary mb-05 prose">Clique em cada bloco pra ver a duração em ação. O quadrado verde anima 200px à direita.</p>' +
            demo(motion_durations_demo) +
            table(["token","valor","uso"], [
                ["--duration-fast-01","70ms","micro-interações (button press)"],
                ["--duration-fast-02","110ms","hover transitions"],
                ["--duration-moderate-01","150ms","tabs, dropdowns"],
                ["--duration-moderate-02","240ms","modal slide-in"],
                ["--duration-slow-01","400ms","page transitions"],
                ["--duration-slow-02","700ms","animações narrativas"],
            ])),
        sec("easings", "easings · live", "02 · 5 curvas",
            '<p class="t-body-02 t-secondary mb-05 prose">Curvas com duração fixa de 600ms pra exagerar a diferença das curvas.</p>' +
            demo(motion_easings_demo) +
            table(["token","curva","uso"], [
                ["--ease-productive","cubic-bezier(0.2,0,0.38,0.9)","UI default"],
                ["--ease-expressive","cubic-bezier(0.4,0.14,0.3,1)","entradas chamativas"],
                ["--ease-entrance","cubic-bezier(0,0,0.38,0.9)","elemento entrando"],
                ["--ease-exit","cubic-bezier(0.2,0,1,0.9)","elemento saindo"],
                ["--ease-standard","cubic-bezier(0.5,0,0.1,1)","easing genérico"],
            ])),
        sec("reduced", "reduced motion", "03",
            '<p class="t-body-02 t-secondary mb-05 prose">Usuários com <code class="code-inline">prefers-reduced-motion: reduce</code> têm todas as animações reduzidas a ~0ms. Implementado globalmente no CSS — sem precisar tratar em cada componente.</p>' +
            code('<span class="k">@media</span> (<span class="v">prefers-reduced-motion</span>: <span class="v">reduce</span>) {\n  *, *::before, *::after {\n    animation-duration: <span class="v">0.01ms</span> !important;\n    transition-duration: <span class="v">0.01ms</span> !important;\n  }\n}')),
        sec("usage", "quando animar", "04",
            do_dont(
                ["Feedback de interação (button press, focus ring)","Mudança de estado (modal abrindo, drawer)","Entrada de elementos recém-carregados","Indicação de loading (spinner, skeleton)"],
                ["Decoração pura sem propósito","Animações longas (>500ms) em UI funcional","Parallax em conteúdo de leitura","Auto-play em elementos sem controle de pause"],
            )),
        sec("code", "código", "05",
            code('<span class="c">/* transição padrão */</span>\n<span class="k">.btn</span> {\n  transition: all <span class="k">var</span>(--duration-fast-02) <span class="k">var</span>(--ease-productive);\n}\n\n<span class="c">/* animação keyframe */</span>\n<span class="k">@keyframes</span> ch-slide-up {\n  <span class="v">from</span> { opacity: <span class="v">0</span>; transform: translateY(<span class="v">16px</span>); }\n  <span class="v">to</span>   { opacity: <span class="v">1</span>; transform: translateY(<span class="v">0</span>); }\n}\n\n<span class="k">.modal</span> {\n  animation: ch-slide-up <span class="k">var</span>(--duration-moderate-02) <span class="k">var</span>(--ease-entrance);\n}')),
    ]),
    toc=[{"id":"durations","label":"Durations"},{"id":"easings","label":"Easings"},{"id":"reduced","label":"Reduced motion"},{"id":"usage","label":"Quando animar"},{"id":"code","label":"Código"}],
))

write("pages/elements/themes.html", page(
    "themes", "Themes",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="../about/index.html">foundations</a><span class="sep">/</span>themes',
    "Light e dark theme controlados por atributo data-theme no html. Tokens semânticos garantem que componentes nunca precisam saber qual tema está ativo.",
    "".join([
        sec("active", "temas ativos", "01",
            '<p class="t-body-02 t-secondary mb-05 prose">Dois temas em produção, ambos cobrindo a paleta completa. Dark theme segue <code class="code-inline">prefers-color-scheme</code> como default.</p>' +
            '<div class="grid-2"><div class="demo" style="background:#F8FCF8;color:#3C433C;padding:var(--spacing-07)"><div class="t-label-01 mb-04" style="color:#91938C">// light · default</div><h4 class="t-h03 mb-04" style="color:#3C433C">claro</h4><p style="color:#5C625C">background CSS, texto Dos, destaques Code.</p></div><div class="demo" style="background:#3C433C;color:#F8FCF8;padding:var(--spacing-07)"><div class="t-label-01 mb-04" style="color:#ADB1A9">// dark</div><h4 class="t-h03 mb-04" style="color:#F8FCF8">escuro</h4><p style="color:#D7DCD7">background Dos, texto CSS, mesmo Code.</p></div></div>'),
        sec("switching", "trocando de tema", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">Tema é controlado por atributo no &lt;html&gt;. Persistido em localStorage. Inicial respeita prefers-color-scheme.</p>' +
            code('<span class="c">/* CSS: tokens redeclarados */</span>\n<span class="k">html</span>[<span class="v">data-theme</span>=<span class="s">"dark"</span>] {\n  --background: <span class="k">var</span>(--ch-dos);\n  --text-primary: <span class="k">var</span>(--ch-css);\n  <span class="c">/* etc */</span>\n}\n\n<span class="c">// JS</span>\ndocument.documentElement.setAttribute(<span class="s">"data-theme"</span>, <span class="s">"dark"</span>);')),
        sec("philosophy", "filosofia", "03",
            '<p class="t-body-02 t-secondary prose">Componentes não conhecem o tema. Eles consomem tokens semânticos (<code class="code-inline">--text-primary</code>, <code class="code-inline">--layer-01</code>) que mudam de valor conforme o atributo. Trocar de tema = trocar tokens, zero refactor de componente.</p>'),
        sec("usage", "quando usar cada tema", "04",
            do_dont(
                ["Light por padrão em produtos de produtividade e leitura","Dark por padrão em IDEs, dashboards de monitoramento, conteúdo notural","Sempre permitir o usuário trocar","Respeitar prefers-color-scheme do SO"],
                ["Forçar um tema sem opção de troca","Cores fixas (cruas) que não respondem ao tema","Mensagens que pressupõem qual tema está ativo (\"clica no botão escuro\")"],
            )),
        sec("code", "código", "05",
            code('<span class="c">/* alternar tema via JS */</span>\n<span class="k">const</span> cur = document.documentElement.getAttribute(<span class="s">"data-theme"</span>);\n<span class="k">if</span> (cur === <span class="s">"dark"</span>) {\n  document.documentElement.removeAttribute(<span class="s">"data-theme"</span>);\n  localStorage.setItem(<span class="s">"chds-theme"</span>, <span class="s">"light"</span>);\n} <span class="k">else</span> {\n  document.documentElement.setAttribute(<span class="s">"data-theme"</span>, <span class="s">"dark"</span>);\n  localStorage.setItem(<span class="s">"chds-theme"</span>, <span class="s">"dark"</span>);\n}')),
    ]),
    toc=[{"id":"active","label":"Temas ativos"},{"id":"switching","label":"Trocando de tema"},{"id":"philosophy","label":"Filosofia"},{"id":"usage","label":"Quando usar cada tema"},{"id":"code","label":"Código"}],
))

print("done · foundations")
