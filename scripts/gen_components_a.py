"""Components batch A: index + button, breadcrumb, checkbox, code-snippet, data-table,
dropdown, form, link, loading, modal."""
from common import page, sec, demo, do_dont, code, checklist, table, related, write, anatomy, component_page, api_table, grid

# ----- COMPONENTS INDEX -----------------------------------------------------
COMPONENTS = [
    ("accordion",    "divulgação progressiva, single ou multi-mode"),
    ("breadcrumb",   "rastro de navegação hierárquica"),
    ("button",       "ações primárias, secundárias e ghost"),
    ("checkbox",     "seleção múltipla independente"),
    ("code-snippet", "código formatado com copy-to-clipboard"),
    ("data-table",   "tabelas tabulares densas"),
    ("dropdown",     "select customizado com ARIA listbox"),
    ("file-uploader","upload com drag-and-drop"),
    ("form",         "composição de inputs com validação"),
    ("inline-notification", "banner persistente in-page"),
    ("link",         "navegação inline e standalone"),
    ("loading",      "spinner, skeleton, progress"),
    ("modal",        "dialogs sobrepostos com focus trap"),
    ("notification", "feedback inline e toast"),
    ("number-input", "input numérico com stepper +/-"),
    ("pagination",   "navegação entre páginas de resultado"),
    ("radio-button", "seleção mutuamente exclusiva"),
    ("search",       "input dedicado pra busca"),
    ("slider",       "valor contínuo dentro de um range"),
    ("tabs",         "navegação horizontal entre seções"),
    ("tag",          "metadados, status, categorias"),
    ("text-input",   "campo de texto single-line"),
    ("tile",         "container clicável com hover"),
    ("toggle",       "switch on/off com efeito imediato"),
    ("tooltip",      "informação contextual ao hover"),
    ("ui-shell",     "header + sidebar (este site)"),
]

cards_html = "".join(
    f'<a class="resource-card" href="{name}.html"><div class="meta">componente</div><h4>{name}</h4><p>{desc}</p><span class="cta">explorar</span></a>'
    for name, desc in COMPONENTS
)

write("pages/components/index.html", page(
    "comp-index", "Components",
    '<a href="../../index.html">home</a><span class="sep">/</span>components',
    "22 componentes que compõem a UI do CHDS. Todos com tokens semânticos, acessibilidade AA, light + dark theme.",
    sec("library", "biblioteca", "01 · 22 componentes", f'<div class="resource-cards">{cards_html}</div>'),
    tags=[{"cls":"tag--code","label":"22 itens"},{"cls":"tag--blue","label":"stable"}],
    toc=[{"id":"library","label":"Biblioteca"}],
))

# ----- BUTTON ----------------------------------------------------------------
write("pages/components/button.html", component_page(
    page_id="button",
    name="button",
    intro="Botões comunicam ações que os usuários podem tomar. 5 variantes pra diferentes níveis de hierarquia, 4 tamanhos.",
    demo_html=demo('<div class="row"><button class="btn btn--primary">primary</button><button class="btn btn--secondary">secondary</button><button class="btn btn--tertiary">tertiary</button><button class="btn btn--ghost">ghost</button><button class="btn btn--danger">danger</button></div>'),
    variants='<div class="stack-06">' + ''.join(
        f'<div><h3 class="t-h02 mb-04">{label}</h3><p class="t-comment mb-04">{desc}</p>' +
        demo(f'<button class="btn btn--{cls}">{label}</button>') + '</div>'
        for label, cls, desc in [
            ("Primary","primary","Ação mais importante de uma página. Use no máximo uma por contexto."),
            ("Secondary","secondary","Ação alternativa de mesmo peso. Usada junto ao primary."),
            ("Tertiary","tertiary","Ação de baixa ênfase. Outlined, sem fundo."),
            ("Ghost","ghost","Mínimo destaque visual. Sem fundo nem borda."),
            ("Danger","danger","Ação destrutiva — deletar, remover, cancelar permanente."),
        ]
    ) + '</div>',
    sizes='<div class="row" style="gap: var(--spacing-05); align-items: center;">' +
          '<button class="btn btn--primary btn--sm">small</button>' +
          '<button class="btn btn--primary">default</button>' +
          '<button class="btn btn--primary btn--lg">large</button>' +
          '<button class="btn btn--primary btn--xl">extra large</button></div>' +
          '<p class="t-helper mt-04">small: 32px · default: 48px · large: 64px · xl: 80px</p>',
    states=demo('<div class="row"><button class="btn btn--primary">default</button><button class="btn btn--primary" style="background:var(--btn-primary-bg-hover)">hover</button><button class="btn btn--primary" style="box-shadow:inset 0 0 0 2px var(--focus)">focus</button><button class="btn btn--primary" disabled>disabled</button></div>'),
    anatomy_html=anatomy(
        '<svg width="380" height="160" viewBox="0 0 380 160"><rect x="80" y="60" width="220" height="48" fill="var(--ch-code)"/><text x="100" y="92" font-family="IBM Plex Mono" font-size="14" font-weight="500" fill="var(--text-primary)">label</text><text x="275" y="92" font-family="IBM Plex Mono" font-size="14" fill="var(--text-primary)">→</text><circle cx="50" cy="84" r="9" fill="var(--layer-01)" stroke="var(--text-tertiary)"/><text x="46" y="88" font-family="IBM Plex Mono" font-size="11" font-weight="600">1</text><circle cx="190" cy="40" r="9" fill="var(--layer-01)" stroke="var(--text-tertiary)"/><text x="186" y="44" font-family="IBM Plex Mono" font-size="11" font-weight="600">2</text><circle cx="295" cy="125" r="9" fill="var(--layer-01)" stroke="var(--text-tertiary)"/><text x="291" y="129" font-family="IBM Plex Mono" font-size="11" font-weight="600">3</text></svg>',
        ["Container — fundo da variante (primary, secondary, etc.)","Label — verbo no infinitivo, caixa baixa","Glifo — seta indicando ação direcional (opcional)"]
    ),
    modifiers=api_table([
        {"prop":".btn--primary","type":"class","desc":"variante primária — destaque verde"},
        {"prop":".btn--secondary","type":"class","desc":"variante secundária — dos"},
        {"prop":".btn--tertiary","type":"class","desc":"variante outlined"},
        {"prop":".btn--ghost","type":"class","desc":"sem fundo nem borda"},
        {"prop":".btn--danger","type":"class","desc":"ação destrutiva"},
        {"prop":".btn--sm","type":"class","desc":"altura 32px"},
        {"prop":".btn--lg","type":"class","desc":"altura 64px · 2 linhas opcional"},
        {"prop":".btn--xl","type":"class","desc":"altura 80px · expressivo"},
        {"prop":".btn--icon","type":"class","desc":"botão só com ícone"},
        {"prop":"disabled","type":"attr","desc":"desabilita interação"},
    ]),
    usage=do_dont(
        ["Um primary por contexto","Verbo no infinitivo: salvar, enviar, publicar","Danger só pra ação destrutiva irreversível","Ghost pra ações secundárias dentro de cards"],
        ['"clique aqui" como label — usa o verbo da ação','Múltiplos primary numa mesma seção',"Danger pra cancelar formulário (use ghost)","Botão pra navegação — usa link standalone"],
    ),
    a11y=checklist([
        "Elemento &lt;button&gt; nativo, não div",
        'type="button" explícito (default é submit)',
        "Foco visível com outline 2px",
        "Disabled: aria-disabled true OU disabled attribute",
        "Botão só com ícone tem aria-label",
    ]),
    code_html=code('<span class="c">&lt;!-- variantes --&gt;</span>\n&lt;<span class="k">button</span> <span class="v">type</span>=<span class="s">"button"</span> <span class="v">class</span>=<span class="s">"btn btn--primary"</span>&gt;salvar&lt;/<span class="k">button</span>&gt;\n&lt;<span class="k">button</span> <span class="v">type</span>=<span class="s">"button"</span> <span class="v">class</span>=<span class="s">"btn btn--secondary"</span>&gt;cancelar&lt;/<span class="k">button</span>&gt;\n&lt;<span class="k">button</span> <span class="v">type</span>=<span class="s">"button"</span> <span class="v">class</span>=<span class="s">"btn btn--danger"</span>&gt;deletar&lt;/<span class="k">button</span>&gt;\n\n<span class="c">&lt;!-- tamanho --&gt;</span>\n&lt;<span class="k">button</span> <span class="v">class</span>=<span class="s">"btn btn--primary btn--sm"</span>&gt;small&lt;/<span class="k">button</span>&gt;\n\n<span class="c">&lt;!-- icon-only --&gt;</span>\n&lt;<span class="k">button</span> <span class="v">class</span>=<span class="s">"btn btn--ghost btn--icon"</span> <span class="v">aria-label</span>=<span class="s">"fechar"</span>&gt;×&lt;/<span class="k">button</span>&gt;'),
    related_html=related([
        {"href":"link.html","title":"Link","desc":"Pra navegação — não use button pra ir pra outra página."},
        {"href":"tag.html","title":"Tag","desc":"Pra metadados — não use button pra exibir status."},
    ]),
))

# ----- BREADCRUMB ------------------------------------------------------------
write("pages/components/breadcrumb.html", component_page(
    page_id="breadcrumb",
    name="breadcrumb",
    intro="Mostra a posição da página atual numa hierarquia. Permite navegar pra qualquer nível superior. Usado em sites com 3+ níveis de profundidade.",
    demo_html=demo('<nav class="breadcrumb" aria-label="breadcrumb"><a href="#">home</a><span class="sep">/</span><a href="#">components</a><span class="sep">/</span><span aria-current="page">breadcrumb</span></nav>'),
    states='<div class="stack">' +
        demo('<nav class="breadcrumb"><a href="#">home</a><span class="sep">/</span><a href="#">components</a><span class="sep">/</span><span aria-current="page">página atual</span></nav>') +
        demo('<nav class="breadcrumb"><a href="#">a</a><span class="sep">/</span><a href="#">b</a><span class="sep">/</span><a href="#">c</a><span class="sep">/</span><a href="#">d</a><span class="sep">/</span><span aria-current="page">muito longo</span></nav>') + '</div>',
    anatomy_html=anatomy(
        '<svg width="500" height="60" viewBox="0 0 500 60"><text x="40" y="36" font-family="IBM Plex Mono" font-size="12" fill="var(--text-tertiary)" letter-spacing="1">HOME</text><text x="100" y="36" font-family="IBM Plex Mono" font-size="14" fill="var(--ch-code)">/</text><text x="120" y="36" font-family="IBM Plex Mono" font-size="12" fill="var(--text-tertiary)" letter-spacing="1">COMPONENTS</text><text x="225" y="36" font-family="IBM Plex Mono" font-size="14" fill="var(--ch-code)">/</text><text x="245" y="36" font-family="IBM Plex Mono" font-size="12" fill="var(--text-primary)" font-weight="500" letter-spacing="1">BREADCRUMB</text><circle cx="105" cy="32" r="9" fill="var(--layer-01)" stroke="var(--text-tertiary)"/><text x="101" y="36" font-family="IBM Plex Mono" font-size="11" font-weight="600">1</text><circle cx="270" cy="20" r="9" fill="var(--layer-01)" stroke="var(--text-tertiary)"/><text x="266" y="24" font-family="IBM Plex Mono" font-size="11" font-weight="600">2</text></svg>',
        ["Separador — barra verde pra ritmar a hierarquia","Item atual — sem link, marcado com aria-current"]
    ),
    modifiers=api_table([
        {"prop":".breadcrumb","type":"class","desc":"container nav"},
        {"prop":".sep","type":"class","desc":"separador entre itens"},
        {"prop":"aria-current","type":'"page"',"desc":"item ativo (não clicável)"},
    ]),
    usage=do_dont(
        ["Sites com 3+ níveis de profundidade","Hierarquia navegável pra cima","Topo da página, abaixo do header"],
        ["Sites flat com 1-2 níveis — desnecessário","Em vez de back button","Misturar com tabs no mesmo nível"],
    ),
    a11y=checklist([
        "Elemento &lt;nav aria-label=\"breadcrumb\"&gt;",
        'aria-current="page" no item ativo',
        "Separador é decoração — pode ser aria-hidden",
        "Foco visível em cada link",
    ]),
    code_html=code('&lt;<span class="k">nav</span> <span class="v">class</span>=<span class="s">"breadcrumb"</span> <span class="v">aria-label</span>=<span class="s">"breadcrumb"</span>&gt;\n  &lt;<span class="k">a</span> <span class="v">href</span>=<span class="s">"/"</span>&gt;home&lt;/<span class="k">a</span>&gt;\n  &lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"sep"</span>&gt;/&lt;/<span class="k">span</span>&gt;\n  &lt;<span class="k">a</span> <span class="v">href</span>=<span class="s">"/components"</span>&gt;components&lt;/<span class="k">a</span>&gt;\n  &lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"sep"</span>&gt;/&lt;/<span class="k">span</span>&gt;\n  &lt;<span class="k">span</span> <span class="v">aria-current</span>=<span class="s">"page"</span>&gt;breadcrumb&lt;/<span class="k">span</span>&gt;\n&lt;/<span class="k">nav</span>&gt;'),
))

# ----- CHECKBOX --------------------------------------------------------------
write("pages/components/checkbox.html", component_page(
    page_id="checkbox",
    name="checkbox",
    intro="Permite selecionar múltiplas opções independentes. Para opções mutuamente exclusivas, use radio button.",
    demo_html=demo('<div class="stack"><label class="checkbox-row"><input type="checkbox" checked> opção marcada</label><label class="checkbox-row"><input type="checkbox"> opção desmarcada</label><label class="checkbox-row"><input type="checkbox" disabled> opção desabilitada</label></div>'),
    states=demo('<div class="stack"><label class="checkbox-row"><input type="checkbox"> default</label><label class="checkbox-row"><input type="checkbox" checked> checked</label><label class="checkbox-row"><input type="checkbox" disabled> disabled</label><label class="checkbox-row"><input type="checkbox" checked disabled> checked + disabled</label></div>'),
    modifiers=api_table([
        {"prop":'type="checkbox"',"type":"attr","desc":"required"},
        {"prop":"checked","type":"attr","desc":"estado inicial"},
        {"prop":"disabled","type":"attr","desc":"desabilita"},
        {"prop":"required","type":"attr","desc":"obrigatório em form"},
        {"prop":"indeterminate","type":"prop JS","desc":"estado parcial (pai de checkboxes mistos)"},
    ]),
    usage=do_dont(
        ["Múltipla seleção independente","Opção on/off isolada","Concordo com termos (1 checkbox)"],
        ["Escolha mutuamente exclusiva — usa radio","Mais de 7 opções juntas — usa multi-select","Quando só uma alternativa faz sentido"],
    ),
    a11y=checklist([
        "Sempre dentro de &lt;label&gt; ou com label associado por for/id",
        "accent-color: var(--ch-code) pra usar a cor brand",
        "Foco visível",
        "Estado checked anunciado por SR",
    ]),
    code_html=code('&lt;<span class="k">label</span> <span class="v">class</span>=<span class="s">"checkbox-row"</span>&gt;\n  &lt;<span class="k">input</span> <span class="v">type</span>=<span class="s">"checkbox"</span>&gt; concordo com os termos\n&lt;/<span class="k">label</span>&gt;'),
    related_html=related([{"href":"radio-button.html","title":"Radio button","desc":"Pra escolha mutuamente exclusiva."},{"href":"form.html","title":"Form","desc":"Composição com outros campos."}]),
))

# ----- CODE SNIPPET ----------------------------------------------------------
write("pages/components/code-snippet.html", component_page(
    page_id="code-snippet",
    name="code-snippet",
    intro="Bloco de código com syntax highlighting básico e botão de copy automático. Otimizado pra trechos curtos a médios.",
    demo_html=demo('<div class="code-snippet"><span class="c">// exemplo</span>\n<span class="k">const</span> ds = <span class="s">"casa hacker"</span>;\n<span class="k">function</span> hack() { <span class="k">return</span> ds; }</div>'),
    variants='<div class="stack-06"><div><h3 class="t-h02 mb-04">Multi-linha (default)</h3>' + demo('<div class="code-snippet"><span class="k">const</span> x = <span class="v">42</span>;</div>') + '</div><div><h3 class="t-h02 mb-04">Inline</h3>' + demo('<p>Usa o <code class="code-inline">var(--ch-code)</code> pra destaque verde.</p>') + '</div></div>',
    modifiers=api_table([
        {"prop":".code-snippet","type":"class","desc":"bloco multi-linha"},
        {"prop":".code-inline","type":"class","desc":"código inline em texto corrido"},
        {"prop":"span.k","type":"class","desc":"keyword (verde)"},
        {"prop":"span.s","type":"class","desc":"string (pink)"},
        {"prop":"span.c","type":"class","desc":"comment (italic, java)"},
        {"prop":"span.v","type":"class","desc":"value (blue)"},
        {"prop":"span.n","type":"class","desc":"number (script orange)"},
    ]),
    behaviors=checklist([
        "Botão 'copy' aparece automaticamente (injetado pelo shell.js)",
        "Click copia o texto puro (sem tags HTML)",
        "Feedback visual 'copied!' por 1.5s",
        "Funciona via Clipboard API (HTTPS ou localhost)",
    ]),
    usage=do_dont(
        ["Trechos de código de exemplo","Comandos de terminal","URLs ou paths","Configurações em formato chave-valor"],
        ["Logs longos — usa um viewer dedicado","Conteúdo crítico que precisa ser editável","Substituir explicação textual"],
    ),
    a11y=checklist([
        "Botão copy tem aria-label",
        "Foco visível no botão",
        "Texto copiado tem feedback visível E anunciável",
        "Conteúdo pre-formatado preservado com white-space: pre",
    ]),
    code_html=code('&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"code-snippet"</span>&gt;\n  &lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"c"</span>&gt;// comentário&lt;/<span class="k">span</span>&gt;\n  &lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"k"</span>&gt;const&lt;/<span class="k">span</span>&gt; x = &lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"s"</span>&gt;"hello"&lt;/<span class="k">span</span>&gt;;\n&lt;/<span class="k">div</span>&gt;\n\n<span class="c">&lt;!-- inline --&gt;</span>\n&lt;<span class="k">p</span>&gt;Usa &lt;<span class="k">code</span> <span class="v">class</span>=<span class="s">"code-inline"</span>&gt;var(--ch-code)&lt;/<span class="k">code</span>&gt;.&lt;/<span class="k">p</span>&gt;'),
))

# ----- DATA TABLE -----------------------------------------------------------
write("pages/components/data-table.html", component_page(
    page_id="data-table",
    name="data-table",
    intro="Tabelas pra exibir dados estruturados. Suporta variantes default, zebra (alternada) e compact (densa).",
    demo_html=demo('<table class="data-table"><thead><tr><th>nome</th><th>função</th><th>status</th></tr></thead><tbody><tr><td>Code</td><td>destaque · CTA</td><td><span class="tag tag--code">stable</span></td></tr><tr><td>Dos</td><td>fundo escuro</td><td><span class="tag tag--code">stable</span></td></tr><tr><td>Purple</td><td>perifa · ia</td><td><span class="tag tag--purple">new</span></td></tr></tbody></table>'),
    variants='<div class="stack-06"><div><h3 class="t-h02 mb-04">Default</h3>' + demo('<table class="data-table"><thead><tr><th>col 1</th><th>col 2</th></tr></thead><tbody><tr><td>linha 1</td><td>valor</td></tr><tr><td>linha 2</td><td>valor</td></tr></tbody></table>') +
        '</div><div><h3 class="t-h02 mb-04">Zebra</h3>' + demo('<table class="data-table data-table--zebra"><thead><tr><th>col 1</th><th>col 2</th></tr></thead><tbody><tr><td>linha 1</td><td>valor</td></tr><tr><td>linha 2</td><td>valor</td></tr><tr><td>linha 3</td><td>valor</td></tr></tbody></table>') +
        '</div><div><h3 class="t-h02 mb-04">Compact</h3>' + demo('<table class="data-table data-table--compact"><thead><tr><th>col 1</th><th>col 2</th></tr></thead><tbody><tr><td>row a</td><td>v</td></tr><tr><td>row b</td><td>v</td></tr></tbody></table>') + '</div></div>',
    sizes='<p class="t-secondary">Compact reduz padding pra 8px e usa font-size 14px. Default tem padding 16px e font-size 16px.</p>',
    modifiers=api_table([
        {"prop":".data-table","type":"class","desc":"tabela base"},
        {"prop":".data-table--compact","type":"class","desc":"variante densa"},
        {"prop":".data-table--zebra","type":"class","desc":"linhas alternadas"},
    ]),
    usage=do_dont(
        ["Dados tabulares com colunas relacionadas","Comparação entre linhas","Listagens com 5+ campos"],
        ["Layout — usa CSS grid/flex","Listas simples (1-2 colunas) — usa &lt;ul&gt;","Dashboards com cards — usa tile grid"],
    ),
    a11y=checklist([
        "&lt;table&gt; semântico, não divs",
        "&lt;th scope=\"col\"&gt; em headers",
        "&lt;caption&gt; descrevendo a tabela (visível ou .sr-only)",
        "Responsivo: scroll horizontal em mobile ou transformação em cards",
    ]),
    code_html=code('&lt;<span class="k">table</span> <span class="v">class</span>=<span class="s">"data-table"</span>&gt;\n  &lt;<span class="k">caption</span>&gt;tokens de cor&lt;/<span class="k">caption</span>&gt;\n  &lt;<span class="k">thead</span>&gt;\n    &lt;<span class="k">tr</span>&gt;&lt;<span class="k">th</span> <span class="v">scope</span>=<span class="s">"col"</span>&gt;nome&lt;/<span class="k">th</span>&gt;&lt;<span class="k">th</span> <span class="v">scope</span>=<span class="s">"col"</span>&gt;valor&lt;/<span class="k">th</span>&gt;&lt;/<span class="k">tr</span>&gt;\n  &lt;/<span class="k">thead</span>&gt;\n  &lt;<span class="k">tbody</span>&gt;\n    &lt;<span class="k">tr</span>&gt;&lt;<span class="k">td</span>&gt;Code&lt;/<span class="k">td</span>&gt;&lt;<span class="k">td</span>&gt;#32FA96&lt;/<span class="k">td</span>&gt;&lt;/<span class="k">tr</span>&gt;\n  &lt;/<span class="k">tbody</span>&gt;\n&lt;/<span class="k">table</span>&gt;'),
))

# ----- DROPDOWN -------------------------------------------------------------
write("pages/components/dropdown.html", component_page(
    page_id="dropdown",
    name="dropdown",
    intro="Select customizado com ARIA listbox. Suporta navegação por teclado (setas, Enter, Esc), clique e visualização de selecionado.",
    demo_html=demo('<div class="dropdown" style="max-width: 280px;"><button class="dropdown-trigger" type="button">selecione um tema <span class="chevron">▼</span></button><div class="dropdown-menu"><div class="dropdown-item selected" data-value="light">light</div><div class="dropdown-item" data-value="dark">dark</div><div class="dropdown-item" data-value="auto">auto</div></div></div>'),
    behaviors=checklist([
        "Click no trigger abre/fecha o menu",
        "↓ / ↑ navegam as opções",
        "Enter / Space seleciona a opção focada",
        "Esc fecha sem selecionar",
        "Click fora fecha",
        "Disparou evento custom chds:change com {value, label}",
    ]),
    modifiers=api_table([
        {"prop":".dropdown","type":"class","desc":"container"},
        {"prop":".dropdown-trigger","type":"class","desc":"botão clicável"},
        {"prop":".dropdown-menu","type":"class","desc":"lista de opções"},
        {"prop":".dropdown-item","type":"class","desc":"opção"},
        {"prop":".selected","type":"class","desc":"item selecionado"},
        {"prop":"data-value","type":"attr","desc":"valor enviado no evento"},
    ]),
    usage=do_dont(
        ["5-15 opções","Necessidade de busca/filtro futuro","Opções com labels longos"],
        ["1-4 opções — usa radio button","20+ opções — usa search/combobox","Opções mutuamente complementares — usa checkbox"],
    ),
    a11y=checklist([
        'role="listbox" no menu',
        'role="option" nas opções',
        'aria-haspopup="listbox" e aria-expanded no trigger',
        "Foco mantido visível na opção atual",
        "Funciona via teclado totalmente",
    ]),
    code_html=code('&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"dropdown"</span>&gt;\n  &lt;<span class="k">button</span> <span class="v">class</span>=<span class="s">"dropdown-trigger"</span> <span class="v">type</span>=<span class="s">"button"</span>&gt;\n    label &lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"chevron"</span>&gt;▼&lt;/<span class="k">span</span>&gt;\n  &lt;/<span class="k">button</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"dropdown-menu"</span>&gt;\n    &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"dropdown-item"</span> <span class="v">data-value</span>=<span class="s">"1"</span>&gt;opção 1&lt;/<span class="k">div</span>&gt;\n    &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"dropdown-item"</span> <span class="v">data-value</span>=<span class="s">"2"</span>&gt;opção 2&lt;/<span class="k">div</span>&gt;\n  &lt;/<span class="k">div</span>&gt;\n&lt;/<span class="k">div</span>&gt;'),
))

# ----- FORM ------------------------------------------------------------------
write("pages/components/form.html", component_page(
    page_id="form",
    name="form",
    intro="Composição de inputs com label, helper, validação e ações. Layout vertical default, com agrupamento por seção lógica.",
    demo_html=demo('<form class="max-w-xs"><div class="form-group"><label class="form-label" for="dn">nome <span class="req">*</span></label><input class="input" id="dn" required placeholder="seu nome"><div class="form-helper">como deve aparecer no perfil</div></div><div class="form-group"><label class="form-label" for="de">email</label><input class="input" type="email" id="de" placeholder="voce@email.com"></div><div class="form-group"><label class="form-label" for="dm">mensagem</label><textarea class="textarea" id="dm" placeholder="conte mais"></textarea></div><div class="row"><button type="submit" class="btn btn--primary">enviar</button><button type="button" class="btn btn--ghost">cancelar</button></div></form>'),
    variants='<div class="stack-06"><div><h3 class="t-h02 mb-04">Single column (default)</h3><p class="t-secondary">Forms longos · mais legível, melhor em mobile.</p></div><div><h3 class="t-h02 mb-04">Inline</h3><p class="t-secondary">Forms curtos (login, busca) · economiza espaço vertical.</p>' + demo('<form class="row"><input class="input" placeholder="seu email" style="max-width:240px"><button class="btn btn--primary">inscrever</button></form>') + '</div></div>',
    states='<div class="stack">' +
        demo('<div class="form-group"><label class="form-label" for="ss">default</label><input class="input" id="ss" placeholder="digite seu email"></div>') +
        demo('<div class="form-group"><label class="form-label" for="sv">success · validado</label><input class="input valid" id="sv" value="geraldo@casahacker.org" aria-describedby="sv-success"><div class="form-success" id="sv-success" role="status">email válido</div></div>') +
        demo('<div class="form-group"><label class="form-label" for="sw">warning</label><input class="input warning" id="sw" value="senha123"><div class="form-warning">senha fraca · considere mais caracteres</div></div>') +
        demo('<div class="form-group"><label class="form-label" for="se">erro</label><input class="input invalid" id="se" value="email@inv" aria-invalid="true" aria-describedby="se-err"><div class="form-error" id="se-err" role="alert">formato de email inválido</div></div>') +
        demo('<div class="form-group"><label class="form-label" for="sd">disabled</label><input class="input" id="sd" value="readonly" disabled aria-describedby="sd-hint"><div class="form-disabled-hint" id="sd-hint">campo desabilitado · faça login pra editar</div></div>') +
    '</div>',
    modifiers=api_table([
        {"prop":".form-group","type":"class","desc":"agrupador label+input+helper"},
        {"prop":".form-label","type":"class","desc":"label uppercase mono"},
        {"prop":".form-label .req","type":"class","desc":"asterisco obrigatório"},
        {"prop":".form-helper","type":"class","desc":"texto auxiliar abaixo"},
        {"prop":".form-error","type":"class","desc":"mensagem de erro"},
        {"prop":".invalid","type":"class no input","desc":"estado de erro visual"},
    ]),
    usage=do_dont(
        ["Single column como default","Labels acima dos inputs (não ao lado)","Botão primary à esquerda, ghost à direita","Helper antes do erro, não substituído"],
        ["Placeholder substituindo label","Mais de 6-8 campos sem agrupar","Validar antes do submit (só se for crítico)","Asterisco vermelho sem indicação textual"],
    ),
    a11y=checklist([
        "Todo input tem &lt;label for=\"id\"&gt;",
        "Required tem required attribute, não só asterisco",
        "Erros associados por aria-describedby",
        "Foco visível em todos os controles",
        "Submit funciona via Enter no input",
    ]),
    code_html=code('&lt;<span class="k">form</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"form-group"</span>&gt;\n    &lt;<span class="k">label</span> <span class="v">class</span>=<span class="s">"form-label"</span> <span class="v">for</span>=<span class="s">"name"</span>&gt;nome &lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"req"</span>&gt;*&lt;/<span class="k">span</span>&gt;&lt;/<span class="k">label</span>&gt;\n    &lt;<span class="k">input</span> <span class="v">class</span>=<span class="s">"input"</span> <span class="v">id</span>=<span class="s">"name"</span> <span class="v">required</span>&gt;\n    &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"form-helper"</span>&gt;ajuda&lt;/<span class="k">div</span>&gt;\n  &lt;/<span class="k">div</span>&gt;\n  &lt;<span class="k">button</span> <span class="v">type</span>=<span class="s">"submit"</span> <span class="v">class</span>=<span class="s">"btn btn--primary"</span>&gt;enviar&lt;/<span class="k">button</span>&gt;\n&lt;/<span class="k">form</span>&gt;'),
))

# ----- LINK ------------------------------------------------------------------
write("pages/components/link.html", component_page(
    page_id="link",
    name="link",
    intro="Navegação inline em texto, ou standalone como CTA secundário. Sempre sublinhado pra acessibilidade.",
    demo_html=demo('<div class="stack">' +
        '<p>Inline: leia mais sobre <a class="link" href="#">tokens de cor</a> e <a class="link" href="#">tipografia</a>.</p>' +
        '<a class="link link--standalone" href="#">ver documentação completa</a>' +
        '</div>'),
    variants='<div class="stack-06"><div><h3 class="t-h02 mb-04">Inline</h3><p class="t-comment mb-04">Dentro de texto corrido.</p>' + demo('<p>Texto com <a class="link" href="#">link inline</a> no meio.</p>') +
        '</div><div><h3 class="t-h02 mb-04">Standalone</h3><p class="t-comment mb-04">CTA secundário, com seta.</p>' + demo('<a class="link link--standalone" href="#">próximo passo</a>') + '</div></div>',
    states='<div class="row" style="gap: var(--spacing-06)"><a class="link" href="#">default</a><a class="link" href="#" style="color: var(--link-primary-hover)">hover</a><a class="link" href="#" style="outline: 2px solid var(--focus); outline-offset: 2px;">focus</a><a class="link" href="#" style="color: var(--text-disabled); pointer-events: none">disabled</a></div>',
    modifiers=api_table([
        {"prop":".link","type":"class","desc":"link inline (sublinhado verde)"},
        {"prop":".link--standalone","type":"class","desc":"CTA com seta, sem sublinhado"},
    ]),
    usage=do_dont(
        ["Navegação pra outra página/rota","Referências externas (abre em nova aba com rel=noopener)","Inline em texto corrido","Standalone como 'continuar', 'ver mais'"],
        ['Ação (use button)','"clique aqui" — usa o texto descritivo','Sem sublinhado inline','Link sobre ícone sem aria-label'],
    ),
    a11y=checklist([
        "Sempre &lt;a href=\"...\"&gt;, não JS-only div",
        "Texto descritivo (\"ler artigo\", não \"clique\")",
        "target=\"_blank\" sempre com rel=\"noopener noreferrer\"",
        "Foco visível 2px solid focus",
        "External link sinalizado (↗) quando relevante",
    ]),
    code_html=code('<span class="c">&lt;!-- inline --&gt;</span>\n&lt;<span class="k">p</span>&gt;Leia mais sobre &lt;<span class="k">a</span> <span class="v">class</span>=<span class="s">"link"</span> <span class="v">href</span>=<span class="s">"/color"</span>&gt;cor&lt;/<span class="k">a</span>&gt;.&lt;/<span class="k">p</span>&gt;\n\n<span class="c">&lt;!-- standalone --&gt;</span>\n&lt;<span class="k">a</span> <span class="v">class</span>=<span class="s">"link link--standalone"</span> <span class="v">href</span>=<span class="s">"/next"</span>&gt;próximo passo&lt;/<span class="k">a</span>&gt;\n\n<span class="c">&lt;!-- externo --&gt;</span>\n&lt;<span class="k">a</span> <span class="v">class</span>=<span class="s">"link"</span> <span class="v">href</span>=<span class="s">"https://x.com"</span> <span class="v">target</span>=<span class="s">"_blank"</span> <span class="v">rel</span>=<span class="s">"noopener"</span>&gt;site externo ↗&lt;/<span class="k">a</span>&gt;'),
    related_html=related([{"href":"button.html","title":"Button","desc":"Pra disparar ações, não navegação."}]),
))

# ----- LOADING --------------------------------------------------------------
write("pages/components/loading.html", component_page(
    page_id="loading",
    name="loading",
    intro="Indicadores de estado de carregamento: spinner pra ações curtas, skeleton pra blocos de conteúdo, progress pra operações com tempo conhecido.",
    demo_html=demo('<div class="row" style="gap: var(--spacing-08); align-items: center"><span class="spinner"></span><span class="spinner spinner--sm"></span><span class="spinner spinner--lg"></span></div>'),
    variants='<div class="stack-06">' +
        '<div><h3 class="t-h02 mb-04">Spinner</h3><p class="t-comment mb-04">Operação rápida sem tempo conhecido.</p>' + demo('<span class="spinner"></span>') + '</div>' +
        '<div><h3 class="t-h02 mb-04">Skeleton</h3><p class="t-comment mb-04">Placeholder enquanto conteúdo carrega.</p>' + demo('<div style="max-width: 360px"><div class="skeleton" style="height: 20px; margin-bottom: 8px"></div><div class="skeleton" style="height: 14px; width: 80%; margin-bottom: 8px"></div><div class="skeleton" style="height: 14px; width: 60%"></div></div>') + '</div>' +
        '<div><h3 class="t-h02 mb-04">Progress determinado</h3><p class="t-comment mb-04">Quando o tempo é conhecido.</p>' + demo('<div class="progress"><div class="progress-bar" style="width: 60%"></div></div>') + '</div>' +
        '<div><h3 class="t-h02 mb-04">Progress indeterminado</h3>' + demo('<div class="progress progress--indeterminate"><div class="progress-bar"></div></div>') + '</div></div>',
    sizes=demo('<div class="row" style="gap: var(--spacing-06); align-items: center"><span class="spinner spinner--sm"></span><span class="spinner"></span><span class="spinner spinner--lg"></span></div>'),
    modifiers=api_table([
        {"prop":".spinner","type":"class","desc":"círculo girando 32px"},
        {"prop":".spinner--sm","type":"class","desc":"16px"},
        {"prop":".spinner--lg","type":"class","desc":"64px"},
        {"prop":".skeleton","type":"class","desc":"placeholder shimmer"},
        {"prop":".progress","type":"class","desc":"barra de progresso"},
        {"prop":".progress--indeterminate","type":"class","desc":"sem porcentagem"},
    ]),
    usage=do_dont(
        ["Spinner pra <2s sem tempo conhecido","Skeleton pra carregamento de página/lista","Progress pra upload/download com tempo","Skeleton mantém layout estável (sem CLS)"],
        ["Spinner pra >5s sem feedback adicional","Progress fake (porcentagem aleatória)","Skeleton com forma muito diferente do conteúdo real"],
    ),
    a11y=checklist([
        'aria-busy="true" no container que está carregando',
        'role="status" e aria-live="polite" pra anunciar mudanças',
        'aria-label="carregando" no spinner',
        "Respeitar prefers-reduced-motion (spin reduzido)",
    ]),
    code_html=code('<span class="c">&lt;!-- spinner --&gt;</span>\n&lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"spinner"</span> <span class="v">role</span>=<span class="s">"status"</span> <span class="v">aria-label</span>=<span class="s">"carregando"</span>&gt;&lt;/<span class="k">span</span>&gt;\n\n<span class="c">&lt;!-- skeleton --&gt;</span>\n&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"skeleton"</span> <span class="v">style</span>=<span class="s">"height: 20px"</span>&gt;&lt;/<span class="k">div</span>&gt;\n\n<span class="c">&lt;!-- progress --&gt;</span>\n&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"progress"</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"progress-bar"</span> <span class="v">style</span>=<span class="s">"width: 60%"</span>&gt;&lt;/<span class="k">div</span>&gt;\n&lt;/<span class="k">div</span>&gt;'),
))

# ----- MODAL ----------------------------------------------------------------
write("pages/components/modal.html", component_page(
    page_id="modal",
    name="modal",
    intro="Diálogo sobreposto que captura foco do usuário. Use pra confirmações, formulários focados, conteúdo crítico. Esc fecha, focus trap interno.",
    demo_html=demo('<button class="btn btn--primary" data-modal-open="demoModal">abrir modal</button><div class="modal-backdrop" id="demoModal"><div class="modal"><div class="modal-header"><h3>confirmar ação</h3><button class="modal-close" data-modal-close aria-label="fechar">×</button></div><div class="modal-body"><p>Esta ação não pode ser desfeita. Deseja continuar?</p></div><div class="modal-footer"><button class="btn btn--ghost" data-modal-close>cancelar</button><button class="btn btn--danger" data-modal-close>confirmar</button></div></div></div>'),
    variants='<p class="t-secondary">Tamanhos por largura: 480px (compact), 640px (default), 800px (wide), 1024px (full). Use o tamanho mínimo que comporta o conteúdo.</p>',
    sizes='<p class="t-secondary">A largura máxima padrão é 640px. Pra customizar, sobrescreva <code class="code-inline">max-width</code> no .modal.</p>',
    behaviors=checklist([
        "Click em [data-modal-open=\"id\"] abre o modal id",
        "Click em [data-modal-close] fecha",
        "Click no backdrop (fora do modal) fecha",
        "Esc fecha",
        "Foco vai pro primeiro foco-able ao abrir",
        "Tab cycla apenas dentro do modal (focus trap)",
        "Foco volta pro elemento que abriu ao fechar",
        "body com overflow:hidden enquanto aberto",
    ]),
    modifiers=api_table([
        {"prop":".modal-backdrop","type":"class","desc":"overlay escuro"},
        {"prop":".modal","type":"class","desc":"container principal"},
        {"prop":".modal-header","type":"class","desc":"título + close"},
        {"prop":".modal-body","type":"class","desc":"conteúdo scrollable"},
        {"prop":".modal-footer","type":"class","desc":"ações no rodapé"},
        {"prop":"data-modal-open","type":"attr","desc":"ID do modal a abrir"},
        {"prop":"data-modal-close","type":"attr","desc":"fecha o modal pai"},
    ]),
    usage=do_dont(
        ["Confirmação de ação destrutiva","Formulário curto e focado","Conteúdo crítico que precisa de atenção"],
        ["Conteúdo longo — usa página inteira","Notificação não-bloqueante — usa toast","Modal dentro de modal — fluxo confuso"],
    ),
    a11y=checklist([
        'role="dialog" + aria-modal="true"',
        'aria-labelledby aponta pro h3 do header',
        "Focus trap implementado",
        "Esc fecha sempre",
        "Foco retorna ao elemento de origem",
        'aria-label="fechar" no botão close',
    ]),
    code_html=code('<span class="c">&lt;!-- trigger --&gt;</span>\n&lt;<span class="k">button</span> <span class="v">class</span>=<span class="s">"btn btn--primary"</span> <span class="v">data-modal-open</span>=<span class="s">"myModal"</span>&gt;abrir&lt;/<span class="k">button</span>&gt;\n\n<span class="c">&lt;!-- modal --&gt;</span>\n&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"modal-backdrop"</span> <span class="v">id</span>=<span class="s">"myModal"</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"modal"</span>&gt;\n    &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"modal-header"</span>&gt;\n      &lt;<span class="k">h3</span>&gt;título&lt;/<span class="k">h3</span>&gt;\n      &lt;<span class="k">button</span> <span class="v">class</span>=<span class="s">"modal-close"</span> <span class="v">data-modal-close</span>&gt;×&lt;/<span class="k">button</span>&gt;\n    &lt;/<span class="k">div</span>&gt;\n    &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"modal-body"</span>&gt;conteúdo&lt;/<span class="k">div</span>&gt;\n    &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"modal-footer"</span>&gt;\n      &lt;<span class="k">button</span> <span class="v">class</span>=<span class="s">"btn btn--ghost"</span> <span class="v">data-modal-close</span>&gt;cancelar&lt;/<span class="k">button</span>&gt;\n      &lt;<span class="k">button</span> <span class="v">class</span>=<span class="s">"btn btn--primary"</span>&gt;ok&lt;/<span class="k">button</span>&gt;\n    &lt;/<span class="k">div</span>&gt;\n  &lt;/<span class="k">div</span>&gt;\n&lt;/<span class="k">div</span>&gt;'),
    related_html=related([{"href":"notification.html","title":"Notification","desc":"Pra feedback não-bloqueante."},{"href":"../patterns/dialogs.html","title":"Dialogs pattern","desc":"Padrões de uso de dialogs."}]),
))

print("done · components batch A")
