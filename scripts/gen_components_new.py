"""Gera as 5 páginas de componentes novos da issue #4:
Toggle, Slider, Number input, File uploader, Inline notification."""
from common import sec, demo, do_dont, code, checklist, table, related, write, anatomy, component_page, api_table

# ----- TOGGLE (SWITCH) ------------------------------------------------------
write("pages/components/toggle.html", component_page(
    page_id="toggle",
    name="toggle",
    intro="Switch on/off pra preferências binárias. Diferente de checkbox: toggle aplica mudança imediatamente, checkbox espera submit.",
    demo_html=demo('<div class="stack"><label class="toggle"><input type="checkbox" checked><span class="toggle-track"></span><span>notificações</span></label><label class="toggle"><input type="checkbox"><span class="toggle-track"></span><span>modo escuro automático</span></label><label class="toggle"><input type="checkbox" disabled><span class="toggle-track"></span><span>desabilitado</span></label></div>'),
    variants='<div class="stack-06"><div><h3 class="t-h02 mb-04">Default (medium)</h3>' + demo('<label class="toggle"><input type="checkbox" checked><span class="toggle-track"></span><span>label</span></label>') + '</div><div><h3 class="t-h02 mb-04">Small</h3>' + demo('<label class="toggle toggle--sm"><input type="checkbox" checked><span class="toggle-track"></span><span>label menor</span></label>') + '</div></div>',
    sizes='<p class="t-secondary">Default: track 40×24, knob 18px. Small: 32×18, knob 14px.</p>',
    states=demo('<div class="stack"><label class="toggle"><input type="checkbox"><span class="toggle-track"></span><span>off</span></label><label class="toggle"><input type="checkbox" checked><span class="toggle-track"></span><span>on</span></label><label class="toggle"><input type="checkbox" disabled><span class="toggle-track"></span><span>off + disabled</span></label><label class="toggle"><input type="checkbox" checked disabled><span class="toggle-track"></span><span>on + disabled</span></label></div>'),
    modifiers=api_table([
        {"prop":".toggle","type":"class","desc":"container"},
        {"prop":".toggle-track","type":"class","desc":"trilho visual"},
        {"prop":".toggle--sm","type":"class","desc":"variante 32×18"},
        {"prop":'type="checkbox"',"type":"input","desc":"semântica nativa"},
        {"prop":"checked","type":"attr","desc":"estado inicial on"},
        {"prop":"disabled","type":"attr","desc":"desabilita"},
    ]),
    usage=do_dont(
        ["Preferências binárias com efeito imediato (notificações on/off)","Settings de configuração","Opção isolada (1 toggle por linha)"],
        ["Form com múltiplos campos esperando submit — usa checkbox","Escolha entre 2+ opções — usa radio","Ação destrutiva — usa button confirmação"],
    ),
    a11y=checklist([
        'role="switch" implícito via input[type="checkbox"]',
        "aria-checked reflete estado",
        "Funciona via Tab + Space",
        "Foco visível com outline 2px",
        "Label clicável (toda a área .toggle)",
    ]),
    code_html=code('&lt;<span class="k">label</span> <span class="v">class</span>=<span class="s">"toggle"</span>&gt;\n  &lt;<span class="k">input</span> <span class="v">type</span>=<span class="s">"checkbox"</span> <span class="v">checked</span>&gt;\n  &lt;<span class="k">span</span> <span class="v">class</span>=<span class="s">"toggle-track"</span>&gt;&lt;/<span class="k">span</span>&gt;\n  &lt;<span class="k">span</span>&gt;notificações&lt;/<span class="k">span</span>&gt;\n&lt;/<span class="k">label</span>&gt;'),
    related_html=related([
        {"href":"checkbox.html","title":"Checkbox","desc":"Pra seleção em forms (espera submit)."},
        {"href":"radio-button.html","title":"Radio","desc":"Pra escolha entre múltiplas opções."},
    ]),
))

# ----- SLIDER --------------------------------------------------------------
write("pages/components/slider.html", component_page(
    page_id="slider",
    name="slider",
    intro="Seleção de valor contínuo dentro de um range. Útil pra volume, brilho, opacidade, valores numéricos visuais.",
    demo_html=demo('<div class="slider-row max-w-xs"><div class="slider"><input type="range" min="0" max="100" value="60"></div><div class="slider-value">60</div></div>'),
    variants='<div class="stack-06"><div><h3 class="t-h02 mb-04">Slider simples</h3>' + demo('<div class="max-w-xs"><label class="form-label">brilho</label><div class="slider-row"><div class="slider"><input type="range" min="0" max="100" value="40"></div><div class="slider-value">40</div></div></div>') + '</div><div><h3 class="t-h02 mb-04">Sem display de valor</h3>' + demo('<div class="slider max-w-xs"><input type="range" min="0" max="10" value="3"></div>') + '</div></div>',
    states=demo('<div class="stack max-w-xs">' +
        '<div class="slider"><input type="range" min="0" max="100" value="0"></div>' +
        '<div class="slider"><input type="range" min="0" max="100" value="50"></div>' +
        '<div class="slider"><input type="range" min="0" max="100" value="100"></div>' +
        '<div class="slider"><input type="range" min="0" max="100" value="50" disabled></div>' +
        '</div>'),
    behaviors=checklist([
        "← / → ajustam 1 step",
        "↑ / ↓ ajustam 1 step",
        "Home / End vão pro min / max",
        "PageUp / PageDown ajustam ~10 steps",
        "JS auto-sincroniza .slider-value se presente",
    ]),
    modifiers=api_table([
        {"prop":".slider","type":"class","desc":"wrapper do input"},
        {"prop":".slider-row","type":"class","desc":"grid 1fr 80px (slider + valor)"},
        {"prop":".slider-value","type":"class","desc":"display do valor atual"},
        {"prop":"min","type":"attr","desc":"valor mínimo"},
        {"prop":"max","type":"attr","desc":"valor máximo"},
        {"prop":"step","type":"attr","desc":"incremento"},
        {"prop":"value","type":"attr","desc":"valor inicial"},
    ]),
    usage=do_dont(
        ["Valores contínuos (brilho, volume)","Quando precisão exata não é crítica","Quando visualização do range ajuda (zoom, escala)"],
        ["Valores discretos pequenos (1-5) — usa radio","Quando precisão é crítica — usa number input","Múltiplos sliders empilhados sem labels"],
    ),
    a11y=checklist([
        'role="slider" implícito via input[type="range"]',
        "aria-valuemin/max/now implícitos",
        "Funciona 100% via teclado (setas + Home/End/PageUp/Down)",
        "Foco visível com box-shadow no thumb",
        "Sempre acompanhar de label associado",
    ]),
    code_html=code('&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"slider-row"</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"slider"</span>&gt;\n    &lt;<span class="k">input</span> <span class="v">type</span>=<span class="s">"range"</span> <span class="v">min</span>=<span class="s">"0"</span> <span class="v">max</span>=<span class="s">"100"</span> <span class="v">value</span>=<span class="s">"60"</span>&gt;\n  &lt;/<span class="k">div</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"slider-value"</span>&gt;60&lt;/<span class="k">div</span>&gt;\n&lt;/<span class="k">div</span>&gt;'),
))

# ----- NUMBER INPUT -------------------------------------------------------
write("pages/components/number-input.html", component_page(
    page_id="number-input",
    name="number-input",
    intro="Input numérico com botões + e − pra ajuste fino. Usado quando precisão exata é necessária ou quando o usuário precisa visualizar o valor.",
    demo_html=demo('<div class="number-input"><button type="button" data-action="dec" aria-label="diminuir">−</button><input type="number" value="1" min="0" max="99" step="1"><button type="button" data-action="inc" aria-label="aumentar">+</button></div>'),
    variants='<div class="stack-06">' +
        '<div><h3 class="t-h02 mb-04">Inteiro</h3>' + demo('<div class="number-input"><button type="button" data-action="dec">−</button><input type="number" value="5" min="0" max="100" step="1"><button type="button" data-action="inc">+</button></div>') + '</div>' +
        '<div><h3 class="t-h02 mb-04">Decimal</h3>' + demo('<div class="number-input"><button type="button" data-action="dec">−</button><input type="number" value="0.5" min="0" max="1" step="0.1"><button type="button" data-action="inc">+</button></div>') + '</div>' +
        '<div><h3 class="t-h02 mb-04">Com label</h3>' + demo('<div class="form-group max-w-card"><label class="form-label" for="qty">quantidade</label><div class="number-input"><button type="button" data-action="dec">−</button><input type="number" id="qty" value="1" min="1" max="10"><button type="button" data-action="inc">+</button></div><div class="form-helper">máx 10 por pedido</div></div>') + '</div>' +
        '</div>',
    states=demo('<div class="row"><div class="number-input"><button type="button" data-action="dec" disabled>−</button><input type="number" value="0" min="0" max="10"><button type="button" data-action="inc">+</button></div><div class="number-input"><button type="button" data-action="dec">−</button><input type="number" value="10" min="0" max="10"><button type="button" data-action="inc" disabled>+</button></div></div>'),
    behaviors=checklist([
        "Botões − / + ajustam por step",
        "Digitação direta sempre permitida",
        "Setas ↑/↓ no input nativo funcionam",
        "Botões boundary desabilitam quando min/max atingido",
        "JS auto-init pelo components.js",
    ]),
    modifiers=api_table([
        {"prop":".number-input","type":"class","desc":"container"},
        {"prop":'data-action="dec"',"type":"attr","desc":"botão diminuir"},
        {"prop":'data-action="inc"',"type":"attr","desc":"botão aumentar"},
        {"prop":"min","type":"attr","desc":"valor mínimo"},
        {"prop":"max","type":"attr","desc":"valor máximo"},
        {"prop":"step","type":"attr","desc":"incremento"},
    ]),
    usage=do_dont(
        ["Quantidades (carrinho, estoque)","Configurações numéricas com range fixo","Quando step é pequeno (precisão por digitação)"],
        ["Valores visuais (volume, brilho) — usa slider","Range muito amplo (0-99999) — usa input + select de unidade","Valores não-numéricos"],
    ),
    a11y=checklist([
        "Botões com aria-label descritivo",
        "Input nativo &lt;input type='number'&gt;",
        "Foco visível em todos os 3 elementos",
        "Disabled refletido visualmente E semanticamente",
    ]),
    code_html=code('&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"number-input"</span>&gt;\n  &lt;<span class="k">button</span> <span class="v">type</span>=<span class="s">"button"</span> <span class="v">data-action</span>=<span class="s">"dec"</span> <span class="v">aria-label</span>=<span class="s">"diminuir"</span>&gt;−&lt;/<span class="k">button</span>&gt;\n  &lt;<span class="k">input</span> <span class="v">type</span>=<span class="s">"number"</span> <span class="v">value</span>=<span class="s">"1"</span> <span class="v">min</span>=<span class="s">"0"</span> <span class="v">max</span>=<span class="s">"99"</span>&gt;\n  &lt;<span class="k">button</span> <span class="v">type</span>=<span class="s">"button"</span> <span class="v">data-action</span>=<span class="s">"inc"</span> <span class="v">aria-label</span>=<span class="s">"aumentar"</span>&gt;+&lt;/<span class="k">button</span>&gt;\n&lt;/<span class="k">div</span>&gt;'),
    related_html=related([{"href":"slider.html","title":"Slider","desc":"Pra valores contínuos visuais."}]),
))

# ----- FILE UPLOADER ------------------------------------------------------
write("pages/components/file-uploader.html", component_page(
    page_id="file-uploader",
    name="file-uploader",
    intro="Upload de arquivos com drag-and-drop ou click. Lista de arquivos selecionados com remoção individual.",
    demo_html=demo('<div class="file-uploader" tabindex="0"><div class="uploader-icon">↑</div><div class="uploader-text">arraste arquivos ou <strong>clica pra escolher</strong></div><div class="uploader-hint">máx 10MB · png, jpg, pdf</div><input type="file" multiple></div><ul class="file-list"></ul>'),
    variants='<div class="stack-06">' +
        '<div><h3 class="t-h02 mb-04">Multi-file</h3>' + demo('<div class="file-uploader" tabindex="0"><div class="uploader-icon">↑</div><div class="uploader-text">arraste vários arquivos</div><div class="uploader-hint">aceita múltiplos</div><input type="file" multiple></div><ul class="file-list"></ul>') + '</div>' +
        '<div><h3 class="t-h02 mb-04">Single file</h3>' + demo('<div class="file-uploader max-w-xs" tabindex="0"><div class="uploader-icon">↑</div><div class="uploader-text">enviar foto de perfil</div><div class="uploader-hint">jpg ou png · até 5MB</div><input type="file" accept="image/*"></div><ul class="file-list"></ul>') + '</div>' +
        '</div>',
    behaviors=checklist([
        "Click na zona abre o file picker",
        "Drag-and-drop de arquivo(s) sobre a zona destaca borda",
        "Drop registra os arquivos",
        "Lista mostra nome, tamanho formatado (KB/MB) e botão remover",
        "Remover é só visual — em produção precisa interagir com upload state",
    ]),
    modifiers=api_table([
        {"prop":".file-uploader","type":"class","desc":"zona drop"},
        {"prop":".file-list","type":"class","desc":"lista de arquivos selecionados"},
        {"prop":".is-dragover","type":"class","desc":"estado durante drag (auto)"},
        {"prop":"accept","type":"attr","desc":"filtro de tipos (image/*, .pdf)"},
        {"prop":"multiple","type":"attr","desc":"permite múltiplos"},
    ]),
    usage=do_dont(
        ["Upload de avatar, documentos, attachments","Quando preview rápido ajuda (lista do que foi escolhido)","Quando drag-and-drop melhora UX (anexar email)"],
        ["Sem indicação de progress quando upload demora — adiciona .progress","Sem validação de tipo/tamanho","Sem feedback de erro quando falha"],
    ),
    a11y=checklist([
        "Zona com tabindex='0' pra ser focável",
        "Input file sempre presente (mesmo escondido) — fallback total",
        'role="button" implícito quando interativo',
        "Lista de arquivos anunciada por SR (region com aria-live)",
        "Botão remover com aria-label",
    ]),
    code_html=code('&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"file-uploader"</span> <span class="v">tabindex</span>=<span class="s">"0"</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"uploader-icon"</span>&gt;↑&lt;/<span class="k">div</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"uploader-text"</span>&gt;arraste ou &lt;<span class="k">strong</span>&gt;escolha&lt;/<span class="k">strong</span>&gt;&lt;/<span class="k">div</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"uploader-hint"</span>&gt;máx 10MB · png, jpg&lt;/<span class="k">div</span>&gt;\n  &lt;<span class="k">input</span> <span class="v">type</span>=<span class="s">"file"</span> <span class="v">multiple</span>&gt;\n&lt;/<span class="k">div</span>&gt;\n&lt;<span class="k">ul</span> <span class="v">class</span>=<span class="s">"file-list"</span>&gt;&lt;/<span class="k">ul</span>&gt;'),
))

# ----- INLINE NOTIFICATION ------------------------------------------------
write("pages/components/inline-notification.html", component_page(
    page_id="inline-notif",
    name="inline-notification",
    intro="Banner persistente in-page pra info importante mas não-bloqueante. Diferente do toast (timed): inline fica até o usuário interagir ou dispensar.",
    demo_html=demo('<div class="stack">' +
        '<div class="notification notification--inline notification--info"><div class="notification-icon">i</div><div class="notification-body"><strong>nova versão disponível</strong><p>v1.1 chegou com toggle, slider e file uploader.</p></div><button class="notification-close" aria-label="dispensar">×</button></div>' +
        '<div class="notification notification--inline notification--warning"><div class="notification-icon">⚠</div><div class="notification-body"><strong>cuidado</strong><p>essa ação vai afetar 247 registros.</p></div></div>' +
        '<div class="notification notification--inline notification--success"><div class="notification-icon">✓</div><div class="notification-body"><strong>dados sincronizados</strong><p>tudo certo, última atualização há 2 minutos.</p></div></div>' +
        '</div>'),
    variants='<p class="t-secondary mb-04">Mesmas 4 cores do notification base (success/error/warning/info), mas com fundo --layer-02 e sem shadow.</p>' +
        demo('<div class="stack">' +
        '<div class="notification notification--inline notification--success"><div class="notification-icon">✓</div><div class="notification-body"><strong>success</strong><p>operação concluída.</p></div></div>' +
        '<div class="notification notification--inline notification--error"><div class="notification-icon">⚠</div><div class="notification-body"><strong>error</strong><p>algo deu errado.</p></div></div>' +
        '<div class="notification notification--inline notification--warning"><div class="notification-icon">⚠</div><div class="notification-body"><strong>warning</strong><p>atenção a isso.</p></div></div>' +
        '<div class="notification notification--inline notification--info"><div class="notification-icon">i</div><div class="notification-body"><strong>info</strong><p>fyi.</p></div></div>' +
        '</div>'),
    modifiers=api_table([
        {"prop":".notification--inline","type":"class","desc":"variante banner (vs toast/notification regular)"},
        {"prop":".notification--success","type":"class","desc":"verde"},
        {"prop":".notification--error","type":"class","desc":"vermelho"},
        {"prop":".notification--warning","type":"class","desc":"amarelo"},
        {"prop":".notification--info","type":"class","desc":"neutro"},
        {"prop":".notification-close","type":"class","desc":"botão dispensar (opcional)"},
    ]),
    usage=do_dont(
        ["Info persistente que precisa ser vista (banner de update)","Aviso contextual no topo de uma seção","Confirmação que fica até o usuário ler"],
        ["Feedback rápido pós-ação — usa toast","Erro crítico bloqueante — usa modal","Notificação genérica do app — usa notification regular"],
    ),
    a11y=checklist([
        'role="status" pra info/success',
        'role="alert" pra erro crítico',
        "Botão close com aria-label",
        "Não auto-dismiss (diferente do toast)",
        'aria-live="polite" se aparecer dinamicamente',
    ]),
    code_html=code('&lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"notification notification--inline notification--info"</span> <span class="v">role</span>=<span class="s">"status"</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"notification-icon"</span>&gt;i&lt;/<span class="k">div</span>&gt;\n  &lt;<span class="k">div</span> <span class="v">class</span>=<span class="s">"notification-body"</span>&gt;\n    &lt;<span class="k">strong</span>&gt;título&lt;/<span class="k">strong</span>&gt;\n    &lt;<span class="k">p</span>&gt;mensagem.&lt;/<span class="k">p</span>&gt;\n  &lt;/<span class="k">div</span>&gt;\n  &lt;<span class="k">button</span> <span class="v">class</span>=<span class="s">"notification-close"</span>&gt;×&lt;/<span class="k">button</span>&gt;\n&lt;/<span class="k">div</span>&gt;'),
    related_html=related([{"href":"notification.html","title":"Notification (toast)","desc":"Pra feedback rápido pós-ação."}]),
))

print('done · 5 componentes novos')
