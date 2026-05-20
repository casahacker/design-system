"""Components batch B: notification, pagination, radio-button, search, tabs, tag,
text-input, tile, tooltip, ui-shell."""
from common import sec, demo, do_dont, code, checklist, table, related, write, anatomy, component_page, api_table

# ----- NOTIFICATION ---------------------------------------------------------
write("pages/components/notification.html", component_page(
    page_id="notification",
    name="notification",
    intro="Feedback inline ou toast pra resultado de ações: sucesso, erro, aviso, info. Pode ser dispensável.",
    demo_html=demo('<div class="stack" style="max-width: 480px;">' +
        '<div class="notification notification--success"><div class="notification-icon">◆</div><div class="notification-body"><strong>tudo certo</strong><p>post publicado com sucesso.</p></div><button class="notification-close" aria-label="fechar">×</button></div>' +
        '<div class="notification notification--error"><div class="notification-icon">⚠</div><div class="notification-body"><strong>deu ruim</strong><p>não foi possível enviar. tenta de novo em alguns segundos.</p></div><button class="notification-close" aria-label="fechar">×</button></div>' +
        '<div class="notification notification--warning"><div class="notification-icon">⚠</div><div class="notification-body"><strong>atenção</strong><p>essa ação tem consequências.</p></div></div>' +
        '<div class="notification notification--info"><div class="notification-icon">i</div><div class="notification-body"><strong>fyi</strong><p>nova versão disponível.</p></div></div>' +
        '</div>'),
    variants='<p class="t-secondary mb-04">Inline (default) e Toast (programático via <code class="code-inline">window.CHDS.toast()</code>).</p>' +
        demo('<button class="btn btn--primary" onclick="window.CHDS && window.CHDS.toast({title:\'toast disparado\',message:\'demo de toast programático\',kind:\'success\'})">disparar toast</button>'),
    states=demo('<div class="stack" style="max-width: 480px"><div class="notification notification--success"><div class="notification-icon">◆</div><div class="notification-body"><strong>com ação</strong><p>tem botão de fechar.</p></div><button class="notification-close">×</button></div><div class="notification notification--info"><div class="notification-icon">i</div><div class="notification-body"><strong>sem ação</strong><p>não pode ser dispensada.</p></div></div></div>'),
    modifiers=api_table([
        {"prop":".notification--success","type":"class","desc":"verde"},
        {"prop":".notification--error","type":"class","desc":"vermelho"},
        {"prop":".notification--warning","type":"class","desc":"amarelo"},
        {"prop":".notification--info","type":"class","desc":"neutro"},
        {"prop":".notification-close","type":"class","desc":"botão dispensar"},
        {"prop":"CHDS.toast()","type":"function","desc":"toast programático {title, message, kind, timeout}"},
    ]),
    behaviors=checklist([
        "Click no × dispara animação de saída (200ms) e remove do DOM",
        "Toast desaparece sozinho após 4.5s (configurável)",
        "Toast novo empilha em cima dos anteriores (.toast-stack)",
        "Toast stack tem aria-live='polite' pra anunciar",
    ]),
    usage=do_dont(
        ["Feedback de ação do usuário","Erro recuperável","Confirmação de operação assíncrona"],
        ["Conteúdo persistente — usa tile/banner","Erro crítico bloqueante — usa modal","Empilhar 5+ notifications — vira ruído"],
    ),
    a11y=checklist([
        'role="alert" pra erros críticos (interrompe SR)',
        'role="status" pra info/success (não-interruptivo)',
        'aria-live="polite" pra updates dinâmicos',
        "Botão close com aria-label",
        "Tempo suficiente pra ler (mínimo 5s pra texto curto)",
    ]),
    code_html=code('<span class="c">&lt;!-- inline --&gt;</span>\n&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"notification notification--success"</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"notification-icon"</span>&gt;◆&lt;/<span class="k">div</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"notification-body"</span>&gt;\n    &lt;<span class="k">strong</span>&gt;tudo certo&lt;/<span class="k">strong</span>&gt;\n    &lt;<span class="k">p</span>&gt;post publicado.&lt;/<span class="k">p</span>&gt;\n  &lt;/<span class="k">div</span>&gt;\n  &lt;<span class="k">button</span> <span class="v">class</span>=<span class="s">"notification-close"</span>&gt;×&lt;/<span class="k">button</span>&gt;\n&lt;/<span class="k">div</span>&gt;\n\n<span class="c">// programático</span>\nCHDS.toast({\n  title: <span class="s">"enviado"</span>,\n  message: <span class="s">"obrigado!"</span>,\n  kind: <span class="s">"success"</span>\n});'),
))

# ----- PAGINATION -----------------------------------------------------------
write("pages/components/pagination.html", component_page(
    page_id="pagination",
    name="pagination",
    intro="Navegação entre páginas de resultado em listas e tabelas longas. Mostra qual página está ativa e total.",
    demo_html=demo('<div class="pagination"><div>mostrando 1-10 de 247</div><div class="pagination-items"><button disabled>← anterior</button><span>página 1 de 25</span><button>próximo →</button></div></div>'),
    states=demo('<div class="stack" style="max-width: 720px"><div class="pagination"><div>10 / 100</div><div class="pagination-items"><button disabled>← anterior</button><span>página 1</span><button>próximo →</button></div></div><div class="pagination"><div>50 / 100</div><div class="pagination-items"><button>← anterior</button><span>página 5</span><button>próximo →</button></div></div><div class="pagination"><div>100 / 100</div><div class="pagination-items"><button>← anterior</button><span>página 10</span><button disabled>próximo →</button></div></div></div>'),
    modifiers=api_table([
        {"prop":".pagination","type":"class","desc":"container"},
        {"prop":".pagination-items","type":"class","desc":"grupo de controles"},
        {"prop":"button[disabled]","type":"attr","desc":"estado boundary"},
    ]),
    usage=do_dont(
        ["Listas com 50+ itens","Tabelas paginadas no servidor","Quando paginação é mais clara que scroll infinito"],
        ["Listas com <30 itens — mostra tudo","Conteúdo de feed (rede social) — usa scroll infinito","Esconder o total — usuário precisa saber onde está"],
    ),
    a11y=checklist([
        '&lt;nav aria-label="pagination"&gt;',
        'aria-current="page" no número da página atual',
        "Boundary buttons disabled (não só visualmente)",
        "Foco visível em todos os controles",
    ]),
    code_html=code('&lt;<span class="k">nav</span> <span class="v">class</span>=<span class="s">"pagination"</span> <span class="v">aria-label</span>=<span class="s">"pagination"</span>&gt;\n  &lt;<span class="k">div</span>&gt;1-10 de 247&lt;/<span class="k">div</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"pagination-items"</span>&gt;\n    &lt;<span class="k">button</span>&gt;← anterior&lt;/<span class="k">button</span>&gt;\n    &lt;<span class="k">span</span>&gt;página 5 de 25&lt;/<span class="k">span</span>&gt;\n    &lt;<span class="k">button</span>&gt;próximo →&lt;/<span class="k">button</span>&gt;\n  &lt;/<span class="k">div</span>&gt;\n&lt;/<span class="k">nav</span>&gt;'),
))

# ----- RADIO BUTTON ---------------------------------------------------------
write("pages/components/radio-button.html", component_page(
    page_id="radio-button",
    name="radio-button",
    intro="Seleção mutuamente exclusiva: só uma opção do grupo pode estar ativa. Pra múltipla seleção, use checkbox.",
    demo_html=demo('<fieldset style="border: none"><legend class="form-label" style="margin-bottom: var(--spacing-04)">tema preferido</legend><label class="radio-row"><input type="radio" name="theme" value="light" checked> light</label><label class="radio-row"><input type="radio" name="theme" value="dark"> dark</label><label class="radio-row"><input type="radio" name="theme" value="auto"> auto (sistema)</label></fieldset>'),
    states=demo('<div class="stack"><label class="radio-row"><input type="radio" name="s"> default</label><label class="radio-row"><input type="radio" name="s" checked> checked</label><label class="radio-row"><input type="radio" name="s" disabled> disabled</label><label class="radio-row"><input type="radio" name="s" checked disabled> checked + disabled</label></div>'),
    modifiers=api_table([
        {"prop":'type="radio"',"type":"attr","desc":"required"},
        {"prop":"name","type":"attr","desc":"agrupa radios mutuamente exclusivos"},
        {"prop":"checked","type":"attr","desc":"estado inicial"},
        {"prop":"disabled","type":"attr","desc":"desabilita"},
    ]),
    usage=do_dont(
        ["2-7 opções mutuamente exclusivas","Decisão importante onde todas as opções são visíveis"],
        ["Só 1 opção possível — não usa","8+ opções — usa dropdown","Múltipla seleção — usa checkbox"],
    ),
    a11y=checklist([
        "&lt;fieldset&gt; + &lt;legend&gt; pra agrupar radios relacionados",
        "Todos com mesmo name agrupam exclusivamente",
        "↑ / ↓ navegam dentro do grupo (comportamento nativo)",
        "Label associado por for/id OU envolvendo o input",
    ]),
    code_html=code('&lt;<span class="k">fieldset</span>&gt;\n  &lt;<span class="k">legend</span>&gt;tema&lt;/<span class="k">legend</span>&gt;\n  &lt;<span class="k">label</span> <span class="v">class</span>=<span class="s">"radio-row"</span>&gt;\n    &lt;<span class="k">input</span> <span class="v">type</span>=<span class="s">"radio"</span> <span class="v">name</span>=<span class="s">"theme"</span> <span class="v">value</span>=<span class="s">"light"</span>&gt; light\n  &lt;/<span class="k">label</span>&gt;\n  &lt;<span class="k">label</span> <span class="v">class</span>=<span class="s">"radio-row"</span>&gt;\n    &lt;<span class="k">input</span> <span class="v">type</span>=<span class="s">"radio"</span> <span class="v">name</span>=<span class="s">"theme"</span> <span class="v">value</span>=<span class="s">"dark"</span>&gt; dark\n  &lt;/<span class="k">label</span>&gt;\n&lt;/<span class="k">fieldset</span>&gt;'),
    related_html=related([{"href":"checkbox.html","title":"Checkbox","desc":"Pra seleção múltipla independente."}]),
))

# ----- SEARCH ---------------------------------------------------------------
write("pages/components/search.html", component_page(
    page_id="search",
    name="search",
    intro="Input dedicado pra busca textual. Visualmente distinto de text-input regular pra reforçar a função.",
    demo_html=demo('<div class="search" style="max-width: 480px"><input type="search" placeholder="// buscar componentes..."></div>'),
    sizes='<p class="t-secondary">Altura padrão 40px. Variantes futuras: small (32px) e large (48px).</p>',
    states=demo('<div class="stack" style="max-width: 480px"><div class="search"><input type="search" placeholder="// vazio"></div><div class="search"><input type="search" value="button"></div><div class="search"><input type="search" placeholder="// disabled" disabled></div></div>'),
    behaviors=checklist([
        "X aparece quando há valor (futuro — depende do browser)",
        "Enter dispara o submit do form",
        "Escape limpa o valor",
        'Navegação por teclado: "/" foca o input (atalho global)',
    ]),
    usage=do_dont(
        ["Busca global no app/site","Filtragem de lista longa","Ações que envolvem keyword/query"],
        ["Filtros estruturados — usa dropdowns/checkboxes","Input genérico — usa text-input"],
    ),
    a11y=checklist([
        'type="search" semântico',
        "aria-label='buscar' ou label associado",
        "Foco visível",
        'role="search" no container quando relevante',
    ]),
    code_html=code('&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"search"</span>&gt;\n  &lt;<span class="k">input</span> <span class="v">type</span>=<span class="s">"search"</span> <span class="v">placeholder</span>=<span class="s">"// buscar..."</span> <span class="v">aria-label</span>=<span class="s">"buscar"</span>&gt;\n&lt;/<span class="k">div</span>&gt;'),
    related_html=related([{"href":"text-input.html","title":"Text input","desc":"Pra entrada genérica."},{"href":"dropdown.html","title":"Dropdown","desc":"Pra filtros estruturados."}]),
))

# ----- TABS -----------------------------------------------------------------
write("pages/components/tabs.html", component_page(
    page_id="tabs",
    name="tabs",
    intro="Navegação horizontal entre seções relacionadas. ARIA tablist com navegação completa por teclado.",
    demo_html=demo('<div role="tablist" class="tabs"><button role="tab" aria-controls="t1" class="tab active">overview</button><button role="tab" aria-controls="t2" class="tab">specs</button><button role="tab" aria-controls="t3" class="tab">downloads</button></div><div role="tabpanel" id="t1" class="tab-panel"><p>conteúdo do overview.</p></div><div role="tabpanel" id="t2" class="tab-panel" hidden><p>conteúdo de specs.</p></div><div role="tabpanel" id="t3" class="tab-panel" hidden><p>conteúdo de downloads.</p></div>'),
    behaviors=checklist([
        "Click no tab ativa o panel correspondente",
        "← / → movem foco entre tabs",
        "Home / End vão pro primeiro / último tab",
        "Enter / Space ativam o tab focado",
        "Auto-init pelo components.js em qualquer [role='tablist']",
    ]),
    modifiers=api_table([
        {"prop":'role="tablist"',"type":"attr","desc":"container"},
        {"prop":'role="tab"',"type":"attr","desc":"botão tab"},
        {"prop":'role="tabpanel"',"type":"attr","desc":"painel de conteúdo"},
        {"prop":"aria-controls","type":"attr","desc":"id do panel correspondente"},
        {"prop":".active","type":"class","desc":"tab ativo"},
        {"prop":"hidden","type":"attr no panel","desc":"escondido (não-ativo)"},
    ]),
    usage=do_dont(
        ["Conteúdo relacionado dividido em poucas seções (2-6)","Quando comparação rápida entre seções é útil","Configurações agrupadas por categoria"],
        ["Conteúdo sequencial — usa wizard","Mais de 7 tabs — usa sidebar ou accordion","Tabs aninhadas — fluxo confuso"],
    ),
    a11y=checklist([
        'role="tablist", role="tab", role="tabpanel"',
        'aria-selected reflete estado',
        'aria-controls aponta pro id do panel',
        "Tab navigation pula tabs não-ativos (tabindex -1)",
        "Setas implementadas (✓ no components.js)",
    ]),
    code_html=code('&lt;<span class="k">div</span> <span class="v">role</span>=<span class="s">"tablist"</span> <span class="v">class</span>=<span class="s">"tabs"</span>&gt;\n  &lt;<span class="k">button</span> <span class="v">role</span>=<span class="s">"tab"</span> <span class="v">aria-controls</span>=<span class="s">"p1"</span> <span class="v">class</span>=<span class="s">"tab active"</span>&gt;um&lt;/<span class="k">button</span>&gt;\n  &lt;<span class="k">button</span> <span class="v">role</span>=<span class="s">"tab"</span> <span class="v">aria-controls</span>=<span class="s">"p2"</span> <span class="v">class</span>=<span class="s">"tab"</span>&gt;dois&lt;/<span class="k">button</span>&gt;\n&lt;/<span class="k">div</span>&gt;\n&lt;<span class="k">div</span> <span class="v">role</span>=<span class="s">"tabpanel"</span> <span class="v">id</span>=<span class="s">"p1"</span> <span class="v">class</span>=<span class="s">"tab-panel"</span>&gt;conteúdo um&lt;/<span class="k">div</span>&gt;\n&lt;<span class="k">div</span> <span class="v">role</span>=<span class="s">"tabpanel"</span> <span class="v">id</span>=<span class="s">"p2"</span> <span class="v">class</span>=<span class="s">"tab-panel"</span> <span class="v">hidden</span>&gt;conteúdo dois&lt;/<span class="k">div</span>&gt;'),
))

# ----- TAG ------------------------------------------------------------------
write("pages/components/tag.html", component_page(
    page_id="tag",
    name="tag",
    intro="Pequenos rótulos pra metadata, status, categorias. Cor coordenada com tokens semânticos. Suporta dismissible.",
    demo_html=demo('<div class="row"><span class="tag">default</span><span class="tag tag--code">code</span><span class="tag tag--blue">blue</span><span class="tag tag--pink">pink</span><span class="tag tag--script">script</span><span class="tag tag--purple">purple</span><span class="tag tag--red">red</span><span class="tag tag--outline">outline</span></div>'),
    variants='<div class="stack-06"><div><h3 class="t-h02 mb-04">Por cor</h3>' + demo('<div class="row"><span class="tag tag--code">code</span><span class="tag tag--blue">blue</span><span class="tag tag--pink">pink</span><span class="tag tag--script">script</span><span class="tag tag--purple">purple</span><span class="tag tag--red">red</span></div>') +
        '</div><div><h3 class="t-h02 mb-04">Outline</h3>' + demo('<span class="tag tag--outline">outline</span>') +
        '</div><div><h3 class="t-h02 mb-04">Dismissible</h3>' + demo('<span class="tag tag--code tag--dismissible">react <button aria-label="remover">×</button></span>') +
        '</div></div>',
    sizes=demo('<div class="row"><span class="tag tag--sm">small</span><span class="tag">default</span></div>') +
        '<p class="t-helper mt-04">small: 20px · default: 24px</p>',
    modifiers=api_table([
        {"prop":".tag","type":"class","desc":"tag base"},
        {"prop":".tag--{cor}","type":"class","desc":"code, blue, pink, script, purple, red, outline"},
        {"prop":".tag--sm","type":"class","desc":"variante 20px"},
        {"prop":".tag--dismissible","type":"class","desc":"adiciona botão remover"},
    ]),
    usage=do_dont(
        ["Status (stable, beta, new, draft)","Categorias e filtros aplicados","Metadata como tag de post","Múltiplas seleções visuais"],
        ["Ação primária — usa button","Mais de 7 tags juntas — agrupa ou pagina","Tags sem significado claro (decorativas)"],
    ),
    a11y=checklist([
        "Cor não é único portador de significado",
        "Ícones decorativos com aria-hidden",
        "Botão dismiss com aria-label='remover tag'",
        "Status badge com role='status' se reflete estado dinâmico",
    ]),
    code_html=code('&lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"tag tag--code"</span>&gt;novo&lt;/<span class="k">span</span>&gt;\n&lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"tag tag--purple"</span>&gt;ia&lt;/<span class="k">span</span>&gt;\n\n<span class="c">&lt;!-- dismissible --&gt;</span>\n&lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"tag tag--outline tag--dismissible"</span>&gt;\n  filtro&lt;<span class="k">button</span> <span class="v">aria-label</span>=<span class="s">"remover"</span>&gt;×&lt;/<span class="k">button</span>&gt;\n&lt;/<span class="k">span</span>&gt;'),
))

# ----- TEXT INPUT -----------------------------------------------------------
write("pages/components/text-input.html", component_page(
    page_id="text-input",
    name="text-input",
    intro="Campo de texto single-line com label, helper e estados de validação. Variante textarea pra multi-line.",
    demo_html=demo('<div style="max-width: 480px"><div class="form-group"><label class="form-label" for="ti">label</label><input class="input" id="ti" placeholder="// digite aqui"><div class="form-helper">texto de ajuda</div></div></div>'),
    variants='<div class="stack-06" style="max-width: 480px"><div><h3 class="t-h02 mb-04">Text</h3>' + demo('<input class="input" placeholder="single line">') +
        '</div><div><h3 class="t-h02 mb-04">Textarea</h3>' + demo('<textarea class="textarea" placeholder="multi-line"></textarea>') +
        '</div><div><h3 class="t-h02 mb-04">Select</h3>' + demo('<select class="select"><option>opção 1</option><option>opção 2</option></select>') + '</div></div>',
    states='<div class="stack" style="max-width: 480px">' +
        demo('<div class="form-group"><label class="form-label" for="x1">default</label><input class="input" id="x1"></div>') +
        demo('<div class="form-group"><label class="form-label" for="x2">com valor</label><input class="input" id="x2" value="texto"></div>') +
        demo('<div class="form-group"><label class="form-label" for="x3">disabled</label><input class="input" id="x3" value="readonly" disabled></div>') +
        demo('<div class="form-group"><label class="form-label" for="x4">erro</label><input class="input invalid" id="x4" value="inválido"><div class="form-error">corrige isso</div></div>') +
        '</div>',
    modifiers=api_table([
        {"prop":".input","type":"class","desc":"text/email/password/number"},
        {"prop":".textarea","type":"class","desc":"multi-line"},
        {"prop":".select","type":"class","desc":"native select estilizado"},
        {"prop":".invalid","type":"class","desc":"estado de erro"},
        {"prop":"disabled","type":"attr","desc":"desabilita"},
        {"prop":"required","type":"attr","desc":"obrigatório"},
    ]),
    usage=do_dont(
        ["Sempre com &lt;label&gt; associado","Placeholder como exemplo, não como label","Helper text dá contexto, erro corrige"],
        ["Placeholder substituindo label","Validar a cada keystroke — espera blur","Input sem label — quebra a11y"],
    ),
    a11y=checklist([
        "Label associado por for/id",
        "Helper antes do erro (não substituído)",
        "Erro associado por aria-describedby",
        "Required com required attribute",
        "Foco visível 2px",
    ]),
    code_html=code('&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"form-group"</span>&gt;\n  &lt;<span class="k">label</span> <span class="v">class</span>=<span class="s">"form-label"</span> <span class="v">for</span>=<span class="s">"email"</span>&gt;email&lt;/<span class="k">label</span>&gt;\n  &lt;<span class="k">input</span> <span class="v">class</span>=<span class="s">"input"</span> <span class="v">type</span>=<span class="s">"email"</span> <span class="v">id</span>=<span class="s">"email"</span> <span class="v">required</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"form-helper"</span>&gt;usaremos só pra contato&lt;/<span class="k">div</span>&gt;\n&lt;/<span class="k">div</span>&gt;'),
    related_html=related([{"href":"form.html","title":"Form","desc":"Composição completa."},{"href":"search.html","title":"Search","desc":"Variante pra busca."}]),
))

# ----- TILE -----------------------------------------------------------------
write("pages/components/tile.html", component_page(
    page_id="tile",
    name="tile",
    intro="Container retangular pra agrupar conteúdo relacionado. Variantes clicável (navega) e selecionável (seleção múltipla).",
    demo_html=demo('<div class="grid-3"><div class="tile"><h4>tile padrão</h4><p>card simples com fundo layer-01.</p></div><a class="tile tile--clickable" href="#"><h4>clicável</h4><p>hover muda borda e mostra barra verde.</p></a><div class="tile tile--selected"><h4>selecionado</h4><p>borda verde + fundo selected.</p></div></div>'),
    variants='<div class="stack-06"><div><h3 class="t-h02 mb-04">Default</h3>' + demo('<div class="tile" style="max-width: 320px"><h4>título</h4><p>tile estático sem interação.</p></div>') +
        '</div><div><h3 class="t-h02 mb-04">Clickable</h3>' + demo('<a class="tile tile--clickable" href="#" style="max-width: 320px"><h4>navegável</h4><p>vira link com hover.</p></a>') +
        '</div><div><h3 class="t-h02 mb-04">Selected</h3>' + demo('<div class="tile tile--selected" style="max-width: 320px"><h4>opção escolhida</h4><p>usado em seleção visual de cards.</p></div>') +
        '</div><div><h3 class="t-h02 mb-04">Bordered</h3>' + demo('<div class="tile tile--bordered" style="max-width: 320px"><h4>com borda</h4><p>destaca o tile do fundo.</p></div>') + '</div></div>',
    states=demo('<div class="row"><div class="tile" style="max-width: 200px"><h4>default</h4><p>estático.</p></div><a class="tile tile--clickable" style="max-width: 200px;background: var(--layer-hover-01); border-color: var(--border-subtle-01)" href="#"><h4>hover</h4><p>borda subtle.</p></a><div class="tile tile--selected" style="max-width: 200px"><h4>selected</h4><p>com barra verde.</p></div></div>'),
    modifiers=api_table([
        {"prop":".tile","type":"class","desc":"tile base"},
        {"prop":".tile--clickable","type":"class","desc":"hover + cursor pointer"},
        {"prop":".tile--selected","type":"class","desc":"estado escolhido"},
        {"prop":".tile--bordered","type":"class","desc":"borda visível por padrão"},
    ]),
    usage=do_dont(
        ["Cards em grid (resource cards)","Opções selecionáveis (planos, temas)","Agrupador de conteúdo relacionado"],
        ["Substituto de button — sem aria-label, sem comportamento","Tile aninhado em tile — fluxo confuso","Sem hierarquia visual interna — apenas título já basta"],
    ),
    a11y=checklist([
        "Tile clicável usa &lt;a&gt; ou &lt;button&gt; (não div com onClick)",
        "Foco visível",
        "Conteúdo semântico interno (h4, p, etc.)",
        "Estado selected anunciado (aria-pressed ou aria-current)",
    ]),
    code_html=code('<span class="c">&lt;!-- default --&gt;</span>\n&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"tile"</span>&gt;\n  &lt;<span class="k">h4</span>&gt;título&lt;/<span class="k">h4</span>&gt;\n  &lt;<span class="k">p</span>&gt;descrição&lt;/<span class="k">p</span>&gt;\n&lt;/<span class="k">div</span>&gt;\n\n<span class="c">&lt;!-- clickable --&gt;</span>\n&lt;<span class="k">a</span> <span class="v">class</span>=<span class="s">"tile tile--clickable"</span> <span class="v">href</span>=<span class="s">"/page"</span>&gt;\n  &lt;<span class="k">h4</span>&gt;navega pra página&lt;/<span class="k">h4</span>&gt;\n&lt;/<span class="k">a</span>&gt;'),
))

# ----- TOOLTIP --------------------------------------------------------------
write("pages/components/tooltip.html", component_page(
    page_id="tooltip",
    name="tooltip",
    intro="Mensagem contextual ao hover/focus. CSS-only via atributo data-tooltip — sem JS necessário pra casos simples.",
    demo_html=demo('<div class="row" style="gap: var(--spacing-08)"><button class="btn btn--secondary" data-tooltip="dica simples">hover aqui</button><button class="btn btn--secondary" data-tooltip="atalho: ctrl+s">salvar</button><button class="btn btn--ghost" data-tooltip="remover este item">×</button></div>'),
    behaviors=checklist([
        "Aparece em hover OU focus (acessibilidade por teclado)",
        "Delay zero (sem espera frustrante)",
        "Posição default: acima do elemento",
        "z-index: var(--z-tooltip) garante topo",
        "CSS-only — funciona sem JS",
    ]),
    modifiers=api_table([
        {"prop":"data-tooltip","type":"attr","desc":"texto do tooltip"},
    ]),
    usage=do_dont(
        ["Atalhos de teclado","Esclarecer ícone-only buttons","Definição de termos técnicos","Status indicators"],
        ["Texto longo — usa popover ou modal","Informação crítica que precisa ser vista","Tooltip aninhado","Mobile (não tem hover) — usa long-press ou inline"],
    ),
    a11y=checklist([
        "Funciona via focus do teclado",
        "aria-describedby idealmente (limitação do CSS-only puro)",
        "Não impede interação — só decora",
        "Pra a11y completo, usar versão JS com aria-describedby setado",
    ]),
    code_html=code('<span class="c">&lt;!-- CSS-only --&gt;</span>\n&lt;<span class="k">button</span> <span class="v">class</span>=<span class="s">"btn btn--secondary"</span> <span class="v">data-tooltip</span>=<span class="s">"atalho: ctrl+s"</span>&gt;\n  salvar\n&lt;/<span class="k">button</span>&gt;'),
))

# ----- UI SHELL -------------------------------------------------------------
write("pages/components/ui-shell.html", component_page(
    page_id="ui-shell",
    name="ui-shell",
    intro="O esqueleto da aplicação: header fixo + sidebar colapsável + main + footer. Injetado por shell.js em qualquer página com &lt;main class='main'&gt;.",
    demo_html=demo('<div style="background: var(--ch-dos); color: var(--ch-css); padding: var(--spacing-04); display: flex; align-items: center; gap: var(--spacing-04); margin-bottom: var(--spacing-04)"><div class="h-mini" style="width: 16px; height: 16px"><span class="on"></span><span></span><span class="on"></span><span></span><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span class="on"></span></div><span class="t-label-02">casa hacker / ds</span><span style="margin-left: auto; color: var(--ch-inspect); font: var(--label-01)">GITHUB ↗</span></div><div style="display: grid; grid-template-columns: 200px 1fr; min-height: 200px; border: 1px solid var(--border-subtle-00)"><div style="padding: var(--spacing-04); background: var(--layer-01); border-right: 1px solid var(--border-subtle-00)"><div class="t-label-01" style="color: var(--text-helper); margin-bottom: var(--spacing-03)">// SECTION</div><div style="padding: var(--spacing-02) 0; border-left: 2px solid var(--ch-code); padding-left: var(--spacing-03); background: var(--background-selected)">item ativo</div><div style="padding: var(--spacing-02) 0; padding-left: var(--spacing-03)">item</div></div><div style="padding: var(--spacing-05)"><h4>main content</h4><p class="t-secondary">conteúdo da página</p></div></div>'),
    variants='<p class="t-secondary">Composição única: 1 header + 1 sidebar + 1 main + 1 footer. Variantes futuras (sem sidebar, sem footer) podem ser adicionadas.</p>',
    behaviors=checklist([
        "Header fixo (sticky top: 0)",
        "Sidebar colapsável por seção, estado persistido em localStorage",
        "Mobile: sidebar vira drawer com backdrop",
        "Atalho '/' foca a busca da sidebar",
        "Esc fecha sidebar mobile",
        "Active section auto-expande na sidebar",
    ]),
    modifiers=api_table([
        {"prop":".shell-header","type":"class","desc":"header dos · sticky"},
        {"prop":".sidebar","type":"class","desc":"nav lateral · colapsa por seção"},
        {"prop":".main","type":"class","desc":"conteúdo principal · max-width 1280px"},
        {"prop":".shell-footer","type":"class","desc":"rodapé"},
        {"prop":'meta[name="ch-page"]',"type":"meta","desc":"id da página atual"},
        {"prop":'meta[name="ch-base"]',"type":"meta","desc":"path relativo ao root"},
    ]),
    usage=do_dont(
        ["Páginas internas do produto","Sites de documentação","Apps com nav fixa","Páginas com 5+ seções"],
        ["Landing pages — usa layout próprio","Email templates","Single-purpose pages (login isolado)"],
    ),
    a11y=checklist([
        "Skip-link 'pular pra conteúdo' visível no foco",
        '&lt;nav aria-label="navegação primária"&gt;',
        'aria-current="page" no link ativo',
        "Sidebar com toggle aria-expanded",
        "Mobile: focus trap quando drawer aberto",
    ]),
    code_html=code('<span class="c">&lt;!-- toda página tem essa estrutura --&gt;</span>\n&lt;<span class="k">html</span>&gt;\n&lt;<span class="k">head</span>&gt;\n  &lt;<span class="k">meta</span> <span class="v">name</span>=<span class="s">"ch-page"</span> <span class="v">content</span>=<span class="s">"my-page"</span>&gt;\n  &lt;<span class="k">meta</span> <span class="v">name</span>=<span class="s">"ch-base"</span> <span class="v">content</span>=<span class="s">"../../"</span>&gt;\n  &lt;<span class="k">link</span> <span class="v">rel</span>=<span class="s">"stylesheet"</span> <span class="v">href</span>=<span class="s">"../../styles.css"</span>&gt;\n&lt;/<span class="k">head</span>&gt;\n&lt;<span class="k">body</span>&gt;\n  &lt;<span class="k">main</span> <span class="v">class</span>=<span class="s">"main"</span>&gt;\n    &lt;!-- conteúdo --&gt;\n  &lt;/<span class="k">main</span>&gt;\n  &lt;<span class="k">script</span> <span class="v">src</span>=<span class="s">"../../shell.js"</span>&gt;&lt;/<span class="k">script</span>&gt;\n&lt;/<span class="k">body</span>&gt;'),
))

print("done · components batch B")
