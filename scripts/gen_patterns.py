"""Patterns (10) + Data Visualization (4)."""
from common import page, sec, demo, do_dont, code, checklist, table, related, write, anatomy, api_table, grid

PATTERNS = [
    ("bit-system",       "BIT modular",       "DNA visual da marca: como o BIT primitivo gera símbolos, padrões e identidades"),
    ("colored-symbol",   "Colored symbol",    "Variantes coloridas do H — uso e regras"),
    ("grafismos",        "Grafismos",         "Biblioteca de 67+ padrões geométricos prontos"),
    ("forms-pattern",    "Forms",             "Composição de formulários com validação, agrupamento e ações"),
    ("dialogs",          "Dialogs",           "Quando usar modal vs alert vs toast"),
    ("empty-states",     "Empty states",      "Telas vazias informativas e acionáveis"),
    ("login",            "Login",             "Padrão de autenticação"),
    ("global-header",    "Global header",     "Header padrão de produtos Casa Hacker"),
    ("status-indicators","Status indicators", "Comunicando estados de sistema (online, sync, erro)"),
]

# Patterns index
cards_html = "".join(
    f'<a class="resource-card" href="{slug}.html"><div class="meta">pattern</div><h4>{title}</h4><p>{desc}</p><span class="cta">explorar</span></a>'
    for slug, title, desc in PATTERNS
)
write("pages/patterns/index.html", page(
    "pat-overview", "Patterns",
    '<a href="../../index.html">home</a><span class="sep">/</span>patterns',
    "Patterns combinam componentes pra resolver problemas recorrentes: formulários, autenticação, navegação, estados, sinalizações.",
    sec("library", "biblioteca de patterns", f"01 · {len(PATTERNS)} padrões", f'<div class="resource-cards">{cards_html}</div>'),
    tags=[{"cls":"tag--code","label":f"{len(PATTERNS)} patterns"}],
    toc=[{"id":"library","label":"Biblioteca"}],
))

# BIT system
write("pages/patterns/bit-system.html", page(
    "bit-system", "BIT modular",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">patterns</a><span class="sep">/</span>bit modular',
    "O BIT — um cubo de 8px — é a unidade fundamental. Combinações de BITs geram o H da marca, ícones, padrões geométricos e identidades de submarcas. Sistema modular reproduzível em digital e impresso.",
    "".join([
        sec("primitive", "primitiva: o bit", "01",
            '<p class="t-body-02 t-secondary mb-05" style="max-width:720px">Um quadrado de 8×8px (ou 1×1 unidade modular). Todas as composições visuais descendem dele.</p>' +
            demo('<div style="display: flex; gap: var(--spacing-06); align-items: flex-end;"><div style="width: 8px; height: 8px; background: var(--ch-code)"></div><div style="width: 16px; height: 16px; background: var(--ch-code)"></div><div style="width: 32px; height: 32px; background: var(--ch-code)"></div><div style="width: 64px; height: 64px; background: var(--ch-code)"></div></div><p class="t-helper mt-04">1 BIT · 2 BITs · 4 BITs · 8 BITs</p>')),
        sec("h-symbol", "o h da casa hacker", "02",
            '<p class="t-body-02 t-secondary mb-05" style="max-width:720px">Grid 3×3 de BITs forma o H. Padrão: 5 quadrados ativos formando a letra.</p>' +
            demo('<div class="row" style="gap: var(--spacing-08)"><div class="h-symbol h-symbol--dark" style="width:96px;height:96px"><span class="on"></span><span></span><span class="on"></span><span></span><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span class="on"></span></div><div class="h-symbol" style="width:96px;height:96px"><span class="on"></span><span></span><span class="on"></span><span></span><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span class="on"></span></div></div>')),
        sec("patterns", "padrões geométricos", "03",
            '<p class="t-body-02 t-secondary mb-05" style="max-width:720px">Tessellations geradas a partir de combinações modulares de BITs. 67+ variações na <a class="link" href="grafismos.html">biblioteca de grafismos</a>.</p>' +
            demo('<div style="background: repeating-linear-gradient(45deg, var(--ch-code) 0 16px, transparent 16px 32px, var(--ch-purple) 32px 48px, transparent 48px 64px); height: 200px; border: 1px solid var(--border-subtle-00)"></div>')),
        sec("submarcas", "identidade das submarcas", "04",
            '<p class="t-body-02 t-secondary" style="max-width:720px">Cada submarca tem uma variação do H: cor, posicionamento, padrão. Veja em <a class="link" href="../submarcas/index.html">submarcas</a>.</p>'),
        sec("usage", "diretrizes", "05",
            do_dont(
                ["Múltiplos de 8 em tudo (spacing, sizing, ícones, grid)","Padrões alinhados ao grid invisível de BITs","Compor identidade nova respeitando o BIT base"],
                ["Valores quebrados que não são múltiplos do BIT","Padrões que ignoram o grid (vira ruído)","Símbolo H com proporção diferente de 3×3"],
            )),
    ]),
    toc=[{"id":"primitive","label":"Primitiva: o BIT"},{"id":"h-symbol","label":"O H da Casa Hacker"},{"id":"patterns","label":"Padrões geométricos"},{"id":"submarcas","label":"Identidade das submarcas"},{"id":"usage","label":"Diretrizes"}],
))

# Colored symbol
write("pages/patterns/colored-symbol.html", page(
    "colored-symbol", "Colored symbol",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">patterns</a><span class="sep">/</span>colored symbol',
    "Variante colorida do H pra contextos celebrativos: eventos, campanhas, marcos. Cada quadrado recebe uma cor da paleta brand.",
    "".join([
        sec("examples", "exemplos", "01",
            demo('<div class="row" style="gap: var(--spacing-07)"><div style="display:grid;grid-template-columns:repeat(3,32px);grid-template-rows:repeat(3,32px)"><div style="background:#32FA96"></div><div></div><div style="background:#FF9ECF"></div><div></div><div style="background:#AA78E6"></div><div style="background:#D79B2E"></div><div style="background:#B3D9FE"></div><div></div><div style="background:#3C433C"></div></div></div>')),
        sec("when", "quando usar", "02",
            do_dont(
                ["Campanhas de aniversário","Identidade de eventos pontuais","Material promocional/celebrativo"],
                ["Material institucional formal","UI funcional","Substituto do H monocromático em uso diário"],
            )),
        sec("library", "biblioteca", "03",
            '<p class="t-body-02 t-secondary" style="max-width:720px">Variações em <code class="code-inline">assets/colored-symbols/</code>. Use sempre as cores tokenizadas da paleta brand.</p>'),
    ]),
    toc=[{"id":"examples","label":"Exemplos"},{"id":"when","label":"Quando usar"},{"id":"library","label":"Biblioteca"}],
))

# Grafismos
write("pages/patterns/grafismos.html", page(
    "grafismos", "Grafismos",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">patterns</a><span class="sep">/</span>grafismos',
    "Biblioteca de 67+ padrões geométricos derivados do BIT. Tessellations isométricas, padrões pixel, ornamentos modulares.",
    "".join([
        sec("library", "biblioteca", "01 · 67+",
            '<p class="t-body-02 t-secondary mb-05" style="max-width:720px">Padrões prontos em <code class="code-inline">assets/grafismos/</code> em formato SVG. Reescaláveis sem perda.</p>' +
            demo('<div class="grid-4"><div style="background: var(--ch-dos); aspect-ratio: 1; background-image: repeating-linear-gradient(45deg, var(--ch-code) 0 8px, transparent 8px 16px)"></div><div style="background: var(--ch-css); aspect-ratio: 1; background-image: radial-gradient(circle at center, var(--ch-code) 2px, transparent 2px); background-size: 16px 16px"></div><div style="background: var(--ch-purple); aspect-ratio: 1; background-image: repeating-conic-gradient(var(--ch-css) 0% 25%, transparent 0% 50%); background-size: 16px 16px"></div><div style="background: var(--ch-sec-b); aspect-ratio: 1; background-image: linear-gradient(135deg, var(--ch-dos) 25%, transparent 25%), linear-gradient(225deg, var(--ch-dos) 25%, transparent 25%); background-size: 16px 16px"></div></div>')),
        sec("categories", "categorias", "02",
            table(["categoria","quantidade","uso típico"], [
                ["Isométrico","18","fundos de hero, banners"],
                ["Pixel art","23","backgrounds de eventos, redes sociais"],
                ["Ornamento modular","16","divisores, frames"],
                ["Tessellation","10","fundos institucionais"],
            ])),
        sec("download", "download", "03",
            '<p class="t-body-02 t-secondary" style="max-width:720px">Acesse <code class="code-inline">assets/grafismos/</code> no repositório. Cada SVG é otimizado e versionável.</p>'),
        sec("when", "quando usar", "04",
            do_dont(
                ["Fundos de hero, banner, eventos","Redes sociais e materiais promocionais","Frames decorativos em prints"],
                ["Conteúdo crítico — distrai","Mais de um padrão na mesma tela","Sobre fotos densas — vira ruído"],
            )),
    ]),
    toc=[{"id":"library","label":"Biblioteca"},{"id":"categories","label":"Categorias"},{"id":"download","label":"Download"},{"id":"when","label":"Quando usar"}],
))

# Forms pattern
write("pages/patterns/forms-pattern.html", page(
    "forms-pat", "Forms",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">patterns</a><span class="sep">/</span>forms',
    "Composição de formulários longos: agrupamento por seção, validação, ações no rodapé. Single column como padrão.",
    "".join([
        sec("structure", "estrutura", "01",
            '<p class="t-body-02 t-secondary mb-05" style="max-width:720px">1 coluna · labels acima · seções com título quando >5 campos · ações no rodapé alinhadas à esquerda.</p>' +
            demo('<form style="max-width: 480px"><div class="t-label-01 mb-04" style="color: var(--text-helper)">// dados pessoais</div><div class="form-group"><label class="form-label" for="fn">nome <span class="req">*</span></label><input class="input" id="fn" required></div><div class="form-group"><label class="form-label" for="fe">email <span class="req">*</span></label><input class="input" type="email" id="fe" required></div><div class="t-label-01 mb-04 mt-06" style="color: var(--text-helper)">// preferências</div><div class="form-group"><label class="checkbox-row"><input type="checkbox"> receber newsletter</label></div><div class="row" style="margin-top: var(--spacing-06)"><button type="submit" class="btn btn--primary">cadastrar</button><button type="button" class="btn btn--ghost">cancelar</button></div></form>')),
        sec("validation", "validação", "02",
            checklist([
                "Validar no blur do campo (não a cada keystroke)",
                "Mostrar erro abaixo do campo",
                "Manter helper text — não substituir por erro",
                "Resumo de erros no topo só pra forms longos",
                "Foco no primeiro campo com erro ao submeter",
            ])),
        sec("actions", "ações", "03",
            '<p class="t-body-02 t-secondary" style="max-width:720px">Primary à esquerda (ação principal), ghost à direita (cancelar). Em flows multi-step, usar "voltar" (ghost) à esquerda e "próximo" (primary) à direita.</p>'),
        sec("when", "quando usar", "04",
            do_dont(
                ["Single column como default","Agrupamento em seções com título quando >5 campos","Helper text antecipando dúvidas"],
                ["Two-column em forms longos — quebra fluxo de leitura","Validar a cada keystroke — irritante","Esconder requirements até o erro"],
            )),
    ]),
    toc=[{"id":"structure","label":"Estrutura"},{"id":"validation","label":"Validação"},{"id":"actions","label":"Ações"},{"id":"when","label":"Quando usar"}],
))

# Dialogs
write("pages/patterns/dialogs.html", page(
    "dialogs", "Dialogs",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">patterns</a><span class="sep">/</span>dialogs',
    "Quando usar modal, alert, toast — escolha do componente certo conforme urgência e nível de interrupção.",
    "".join([
        sec("comparison", "comparação", "01",
            table(["tipo","interrompe?","duração","usa quando"], [
                ["Modal","sim","até usuário fechar","confirmação, form focado, conteúdo crítico"],
                ["Notification inline","não","persistente até dispensar","feedback de ação, info contextual"],
                ["Toast","não","timed (4-6s)","feedback rápido pós-ação (salvo, copiado)"],
                ["Alert nativo","sim","até usuário fechar","emergência (não usar — quebra UX)"],
            ])),
        sec("modal-usage", "modal — quando", "02",
            do_dont(
                ["Confirmação destrutiva (deletar conta)","Formulário curto fora do contexto","Conteúdo crítico que precisa decisão"],
                ["Notificação simples — usa toast","Conteúdo longo — usa página","Pré-requisito de fluxo — usa wizard"],
            )),
        sec("toast-usage", "toast — quando", "03",
            do_dont(
                ['Feedback rápido pós-ação ("salvo")','Notificação não-bloqueante','Confirmação leve'],
                ['Erro crítico — usa modal','Conteúdo persistente — usa notification inline','Empilhar muitos toasts simultaneamente'],
            )),
    ]),
    toc=[{"id":"comparison","label":"Comparação"},{"id":"modal-usage","label":"Modal — quando"},{"id":"toast-usage","label":"Toast — quando"}],
))

# Empty states
write("pages/patterns/empty-states.html", page(
    "empty-states", "Empty states",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">patterns</a><span class="sep">/</span>empty states',
    "Telas sem conteúdo viram oportunidades: explicar contexto, sugerir próxima ação, evitar frustração do usuário.",
    "".join([
        sec("anatomy", "anatomia", "01",
            demo('<div style="text-align: center; padding: var(--spacing-09);"><div style="width: 64px; height: 64px; margin: 0 auto var(--spacing-05); background: var(--layer-02); display: flex; align-items: center; justify-content: center; font: 28px var(--font-mono); color: var(--text-helper)">∅</div><h3 class="t-h03 mb-04">nenhum item por aqui</h3><p class="t-secondary mb-06" style="max-width: 380px; margin-left: auto; margin-right: auto;">você ainda não criou nenhum projeto. comece criando o primeiro.</p><button class="btn btn--primary">criar projeto</button></div>')),
        sec("when", "tipos", "02",
            table(["tipo","exemplo"], [
                ["Sem dados (first run)","\"você ainda não tem projetos\""],
                ["Sem resultado de filtro","\"nenhum resultado pra 'xyz'\""],
                ["Erro de carregamento","\"não rolou carregar — tenta de novo\""],
                ["Sem permissão","\"você não tem acesso a essa área\""],
            ])),
        sec("ingredients", "ingredientes", "03",
            checklist([
                "Ícone ou ilustração leve (BIT-aligned)",
                "Título curto explicativo",
                "Descrição com 1 linha de contexto",
                "Botão primary com ação clara",
                "Botão ghost opcional pra ação secundária",
            ])),
    ]),
    toc=[{"id":"anatomy","label":"Anatomia"},{"id":"when","label":"Tipos"},{"id":"ingredients","label":"Ingredientes"}],
))

# Login
write("pages/patterns/login.html", page(
    "login", "Login",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">patterns</a><span class="sep">/</span>login',
    "Padrão de autenticação: formulário minimalista, social login opcional, links pra cadastro e recuperação.",
    "".join([
        sec("standard", "padrão", "01",
            demo('<div style="max-width: 380px; margin: 0 auto; padding: var(--spacing-07); background: var(--layer-01); border: 1px solid var(--border-subtle-00)"><div class="h-symbol h-symbol--dark" style="width: 32px; height: 32px; margin-bottom: var(--spacing-05)"><span class="on"></span><span></span><span class="on"></span><span></span><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span class="on"></span></div><h3 class="t-h03 mb-06">entrar na casa hacker</h3><div class="form-group"><label class="form-label" for="le">email</label><input class="input" type="email" id="le"></div><div class="form-group"><label class="form-label" for="lp">senha</label><input class="input" type="password" id="lp"><div class="form-helper"><a class="link" href="#">esqueci a senha</a></div></div><button class="btn btn--primary" style="width: 100%; justify-content: center;">entrar</button><p class="t-helper mt-06" style="text-align: center">primeira vez? <a class="link" href="#">cria sua conta</a></p></div>')),
        sec("variants", "variantes", "02",
            checklist([
                "Email + senha (default)",
                "Magic link (sem senha)",
                "Social login (GitHub, Google)",
                "SSO empresarial",
            ])),
        sec("rules", "regras", "03",
            do_dont(
                ["Centralizar visualmente","Mostrar 'esqueci a senha' próximo do campo","Link claro pra cadastro","Botão primary largura total"],
                ["Pedir 5+ campos no login","Captcha sem necessidade real","Esconder requisitos de senha","Auto-submit sem confirmação"],
            )),
    ]),
    toc=[{"id":"standard","label":"Padrão"},{"id":"variants","label":"Variantes"},{"id":"rules","label":"Regras"}],
))

# Global header — mantida manualmente (versão expandida com barra de acessibilidade
# obrigatória). NÃO regenerar aqui — ver pages/patterns/global-header.html direto.

# Status indicators
write("pages/patterns/status-indicators.html", page(
    "status", "Status indicators",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">patterns</a><span class="sep">/</span>status indicators',
    "Sinalizações de estado de sistema: online/offline, sync, processando, erro. Padrões consistentes pra ambientes técnicos.",
    "".join([
        sec("library", "biblioteca", "01",
            demo('<div class="row" style="gap: var(--spacing-06)"><span class="status-badge status-badge--stable">stable</span><span class="status-badge status-badge--beta">beta</span><span class="status-badge status-badge--new">new</span><span class="status-badge status-badge--draft">draft</span></div>')),
        sec("system-states", "estados de sistema", "02",
            table(["estado","indicação","cor"], [
                ["Online","ponto verde + texto","--ch-code"],
                ["Offline","ponto cinza + texto","--ch-java"],
                ["Sincronizando","spinner pequeno","--ch-code"],
                ["Erro","triângulo + texto","--support-error"],
                ["Aviso","triângulo + texto","--support-warning"],
            ])),
        sec("rules", "regras", "03",
            do_dont(
                ["Cor + ícone + texto (nunca só cor)","Estado anunciado por SR (role='status')","Atualização em tempo real com aria-live"],
                ["Só cor pra transmitir significado","Mudar de estado sem feedback visual","Pontos coloridos sem label adjacente"],
            )),
    ]),
    toc=[{"id":"library","label":"Biblioteca"},{"id":"system-states","label":"Estados de sistema"},{"id":"rules","label":"Regras"}],
))

# Data Viz movido pra scripts/gen_dataviz.py (rebuild completo, 8 páginas)

print("done · patterns")
