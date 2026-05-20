"""Submarcas (6) + Impressos (4) + Contributing (4) + Help (2)."""
from common import page, sec, demo, do_dont, code, checklist, table, related, write, anatomy, api_table, grid
import os

ROOT = "C:/Users/geraldo_casahacker/Downloads/design-system"

# Helper to grab a representative SVG from a submarca folder
def first_svg(folder):
    p = os.path.join(ROOT, "assets/submarcas", folder)
    if not os.path.isdir(p):
        return None
    for f in sorted(os.listdir(p)):
        if f.endswith(".svg"):
            return f"../../assets/submarcas/{folder}/{f}"
    return None

# ----- SUBMARCAS ------------------------------------------------------------
SUBMARCAS = [
    ("hackerclubes",    "Hackerclubes",    "Programa de clubes de tecnologia em escolas. Identidade própria com o H modular adaptado.",  "var(--ch-sub-hackerclubes)",   "Tecnologia + educação básica"),
    ("inclusao-tech",   "Inclusão Tech",   "Inclusão digital em comunidades vulneráveis. Cores acolhedoras e mensagem clara.",          "var(--ch-sub-inclusao-tech)",  "Inclusão · acessibilidade · diversidade"),
    ("minas-em-tech",   "Minas em Tech",   "Mulheres na tecnologia. Identidade que celebra protagonismo feminino na área tech.",        "var(--ch-sub-minas-em-tech)",  "Mulheres na tecnologia"),
    ("mao-na-massa",    "Mão na Massa",    "Programa de hands-on: oficinas práticas, makers, fabricação. Energia DIY.",                  "var(--ch-sub-mao-na-massa)",   "Faça-você-mesmo · oficinas"),
    ("perifa-impacto",  "Perifa Impacto",  "Tecnologia + impacto social na periferia. Roxo como cor-signature. Mesma cor da IA.",        "var(--ch-sub-perifa-impacto)", "Periferia · impacto social · IA"),
]

# Submarcas index
cards_html = "".join(
    f'<a class="resource-card" href="{slug}.html"><div class="meta">submarca</div><h4>{title}</h4><p>{desc}</p><span class="cta">explorar</span></a>'
    for slug, title, desc, _, _ in SUBMARCAS
)
write("pages/submarcas/index.html", page(
    "sub-index", "Submarcas",
    '<a href="../../index.html">home</a><span class="sep">/</span>submarcas',
    "5 submarcas da Casa Hacker. Cada uma tem identidade própria (cor, tom, aplicação) mas herda o sistema visual base.",
    "".join([
        sec("family", "família de marcas", "01 · 5 submarcas", f'<div class="resource-cards">{cards_html}</div>'),
        sec("philosophy", "filosofia", "02",
            '<p class="t-body-02 t-secondary prose">Submarcas estendem o sistema sem fragmentá-lo. Cada uma adiciona tokens próprios (cor signature, tipografia opcional) preservando a estrutura, spacing e princípios.</p>'),
    ]),
    tags=[{"cls":"tag--code","label":"5 submarcas"}],
    toc=[{"id":"family","label":"Família"},{"id":"philosophy","label":"Filosofia"}],
))

# Individual submarca pages
for slug, title, desc, color, foco in SUBMARCAS:
    logo_path = first_svg(slug)
    logo_html = f'<img src="{logo_path}" alt="logo {title}" style="max-width: 280px; max-height: 120px; margin: 0 auto;">' if logo_path else f'<div class="t-h04 text-helper">{title}</div>'
    write(f"pages/submarcas/{slug}.html", page(
        slug, title,
        f'<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">submarcas</a><span class="sep">/</span>{slug}',
        desc,
        "".join([
            sec("logo", "logo", "01",
                f'<div class="logo-stage" style="background: var(--logo-stage-bg); padding: var(--spacing-09); border: 1px solid var(--logo-stage-border); text-align: center;">{logo_html}</div>'),
            sec("color", "cor signature", "02",
                f'<div class="grid-3"><div class="tile" style="background:{color}; color: var(--ch-css)"><h4 style="color: var(--ch-css)">{title.lower()}</h4><p style="color: var(--ch-css)">{color}</p></div><div class="tile tile--bordered"><h4>foco</h4><p>{foco}</p></div><div class="tile tile--bordered"><h4>aplicação</h4><p>Materiais digitais e impressos relacionados ao programa.</p></div></div>'),
            sec("usage", "regras de uso", "03",
                do_dont(
                    ["Logo sobre fundo claro ou Dos","Cor signature pra destaques e ações","Manter clear space mínimo (1× altura do H)","Tipografia Roboto Flex + Plex Mono (padrão CHDS)"],
                    [f"Substituir cor signature ({color}) por outra","Distorcer ou rotacionar logo","Usar logo abaixo do tamanho mínimo (24px)","Aplicar efeitos (sombra, gradiente, etc.) no logo"],
                )),
            sec("assets", "assets", "04",
                f'<p class="t-body-02 t-secondary prose">Arquivos disponíveis em <code class="code-inline">assets/submarcas/{slug}/</code>. Versões SVG vetorial pra todos os usos.</p>'),
        ]),
        tags=[{"cls":"tag--code","label":"stable"}],
        toc=[{"id":"logo","label":"Logo"},{"id":"color","label":"Cor signature"},{"id":"usage","label":"Regras de uso"},{"id":"assets","label":"Assets"}],
    ))

# ----- IMPRESSOS -----------------------------------------------------------
IMPRESSOS = [
    ("papelaria", "Papelaria", "Cartões de visita, papel timbrado, envelopes, pastas e folders."),
    ("eventos",   "Eventos",   "Sinalização, crachás, banners, painéis de palco, programações impressas."),
    ("loja",      "Loja & merch", "T-shirts, canecas, adesivos, mochilas, brindes promocionais."),
]

imp_cards = "".join(
    f'<a class="resource-card" href="{slug}.html"><div class="meta">impressos</div><h4>{title}</h4><p>{desc}</p><span class="cta">explorar</span></a>'
    for slug, title, desc in IMPRESSOS
)
write("pages/impressos/index.html", page(
    "imp-index", "Impressos",
    '<a href="../../index.html">home</a><span class="sep">/</span>impressos',
    "Diretrizes pra materiais físicos: papelaria, sinalização de eventos, merchandise. Tokens digitais traduzidos pro impresso.",
    "".join([
        sec("library", "biblioteca", "01", f'<div class="resource-cards">{imp_cards}</div>'),
        sec("rules", "regras gerais", "02",
            checklist([
                "Cores em CMYK pra impressão offset (manter perfil de cor brand)",
                "BIT vale também em impresso — múltiplos de 8mm pra margens e gutters",
                "Logo mínimo 12mm de altura em qualquer material",
                "Tipografia: Plex Mono pra labels, Roboto Flex pra body",
                "Clear space do logo: pelo menos 1× altura do H",
            ])),
    ]),
    toc=[{"id":"library","label":"Biblioteca"},{"id":"rules","label":"Regras gerais"}],
))

# Papelaria
write("pages/impressos/papelaria.html", page(
    "papelaria", "Papelaria",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">impressos</a><span class="sep">/</span>papelaria',
    "Cartões de visita, papel timbrado, envelopes, folders. Identidade institucional formal.",
    "".join([
        sec("items", "itens", "01",
            grid([
                {"title":"cartão de visita","desc":"90×55mm · plex mono + roboto flex · fundo Dos ou CSS"},
                {"title":"papel timbrado","desc":"A4 · logo + barra Code superior · margens 25mm"},
                {"title":"envelope","desc":"C5/C6 · logo no canto superior esquerdo"},
                {"title":"folder/pasta","desc":"A4 dobrado · capa com H e nome do programa"},
            ])),
        sec("specs", "specs técnicos", "02",
            table(["item","tamanho","papel","acabamento"], [
                ["cartão","90×55mm","triplex 300g","laminação fosca"],
                ["timbrado","210×297mm (A4)","sulfite 90g","sem acabamento"],
                ["envelope","229×162mm (C5)","sulfite 90g","sem acabamento"],
                ["folder","420×297mm (A3 dobrado)","couché 150g","verniz UV no logo"],
            ])),
        sec("colors", "cores impressas (CMYK)", "03",
            table(["nome","cmyk","pantone"], [
                ["Code Green","C70 M0 Y65 K0","802C"],
                ["Dos","C68 M55 Y65 K59","Black 7C"],
                ["Console","C5 M0 Y5 K3","—"],
            ])),
    ]),
    toc=[{"id":"items","label":"Itens"},{"id":"specs","label":"Specs técnicos"},{"id":"colors","label":"Cores impressas (CMYK)"}],
))

# Eventos
write("pages/impressos/eventos.html", page(
    "eventos", "Eventos",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">impressos</a><span class="sep">/</span>eventos',
    "Materiais pra hackathons, oficinas, palestras: crachás, banners, sinalização, painéis de palco.",
    "".join([
        sec("items", "itens", "01",
            grid([
                {"title":"crachá","desc":"100×140mm · nome grande + função + foto opcional + qr"},
                {"title":"banner roll-up","desc":"850×2000mm · hero visual + 1 mensagem-chave"},
                {"title":"painel de palco","desc":"3×3m · padrão grafismo + logo programa + edição/ano"},
                {"title":"sinalização","desc":"setas e wayfinding em A3 com ícones BIT"},
                {"title":"programação","desc":"A5 dobrado · grid de horários + descrição de sessões"},
                {"title":"adesivo","desc":"50×50mm · H ou colored symbol · papel adesivo branco"},
            ])),
        sec("crachas", "regras de crachá", "02",
            checklist([
                "Nome em ≥36pt — legível a 2m",
                "Função em 14pt abaixo",
                "Cor da fita por papel (participante = verde, staff = dos, palestrante = roxo)",
                "QR code opcional pra check-in / linkedin",
                "Verso com programação resumida",
            ])),
        sec("banners", "banners e painéis", "03",
            do_dont(
                ["1 mensagem-chave por banner","Hierarquia forte (título grande, suporte menor)","H ou logo do programa visível","Grafismo de fundo discreto"],
                ["Encher de texto — banner não é folder","Múltiplos call-to-actions","Cores não-brand","Fontes diferentes das do sistema"],
            )),
    ]),
    toc=[{"id":"items","label":"Itens"},{"id":"crachas","label":"Regras de crachá"},{"id":"banners","label":"Banners e painéis"}],
))

# Loja
write("pages/impressos/loja.html", page(
    "loja", "Loja & merch",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">impressos</a><span class="sep">/</span>loja & merch',
    "Brindes e merchandising: t-shirts, canecas, adesivos, mochilas, garrafas. Identidade lúdica mantendo coerência.",
    "".join([
        sec("items", "produtos", "01",
            grid([
                {"title":"t-shirt","desc":"H grande no peito ou costas · slogan opcional · 100% algodão"},
                {"title":"caneca","desc":"H + slogan na superfície · cerâmica branca ou preta"},
                {"title":"adesivo","desc":"Kit com H + colored symbols + grafismos"},
                {"title":"mochila/saco","desc":"H estampado · lona ou nylon"},
                {"title":"garrafa","desc":"Rótulo com H · 500ml · inox ou plástico"},
                {"title":"caderno","desc":"A5 · capa Dos · página de abertura com manifesto"},
            ])),
        sec("rules", "regras de aplicação", "02",
            checklist([
                "H sempre alinhado ao grid · sem rotação livre",
                "Cores brand (Code, Dos, Console, Purple) — nada de cores aleatórias",
                "Logo mínimo 30mm de altura em produto físico",
                "Composições novas seguem padrões de grafismo existentes",
                "Sem efeitos de impressão que distorçam a identidade",
            ])),
        sec("submarcas", "merch das submarcas", "03",
            '<p class="t-body-02 t-secondary prose">Cada submarca pode ter merch próprio mantendo sua cor signature. Exemplo: t-shirt Perifa Impacto em roxo, t-shirt Minas em Tech em roxo claro, etc.</p>'),
    ]),
    toc=[{"id":"items","label":"Produtos"},{"id":"rules","label":"Regras de aplicação"},{"id":"submarcas","label":"Merch das submarcas"}],
))

# ----- CONTRIBUTING --------------------------------------------------------
write("pages/contributing/index.html", page(
    "contrib-start", "Contributing",
    '<a href="../../index.html">home</a><span class="sep">/</span>contributing',
    "Como propor melhorias, novos componentes ou patterns no CHDS. Lifecycle, checklist e documentação.",
    "".join([
        sec("how", "como contribuir", "01",
            '<ol class="checklist">' +
            '<li>Fork do <a class="link" href="https://github.com/casahacker/design-system" target="_blank" rel="noopener">repo no github</a></li>' +
            '<li>Cria branch a partir de main: <code class="code-inline">git checkout -b feat/meu-componente</code></li>' +
            '<li>Faz a mudança seguindo o <a class="link" href="checklist.html">component checklist</a></li>' +
            '<li>Abre PR descrevendo o que mudou e por quê</li>' +
            '<li>Aguarda review (em geral 3-5 dias úteis)</li>' +
            '</ol>'),
        sec("areas", "áreas que aceitam contribuição", "02",
            grid([
                {"title":"componentes novos","desc":"Submeta proposta antes via issue. Precisa passar pelo PDLC."},
                {"title":"melhorias de a11y","desc":"Sempre bem-vindas. Cite o critério WCAG no PR."},
                {"title":"correções de bug","desc":"Pode ir direto pra PR. Inclua reproduction."},
                {"title":"docs","desc":"Typos, exemplos, traduções, melhorias de conteúdo."},
                {"title":"performance","desc":"Otimizações de CSS/JS desde que mantenham legibilidade."},
                {"title":"submarcas/impressos","desc":"Novos templates, exemplos de uso, especificações."},
            ])),
        sec("docs", "documentação relacionada", "03",
            '<div class="resource-cards">' +
            '<a class="resource-card" href="checklist.html"><div class="meta">checklist</div><h4>component checklist</h4><p>O que um componente novo precisa cobrir.</p><span class="cta">ver</span></a>' +
            '<a class="resource-card" href="pdlc.html"><div class="meta">lifecycle</div><h4>pdlc</h4><p>Product Design Lifecycle: como um componente vira parte do sistema.</p><span class="cta">ver</span></a>' +
            '<a class="resource-card" href="documentation.html"><div class="meta">docs</div><h4>documentation guide</h4><p>Como documentar pra que faça sentido pros próximos.</p><span class="cta">ver</span></a>' +
            '</div>'),
    ]),
    toc=[{"id":"how","label":"Como contribuir"},{"id":"areas","label":"Áreas"},{"id":"docs","label":"Docs relacionadas"}],
))

write("pages/contributing/checklist.html", page(
    "checklist", "Component checklist",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">contributing</a><span class="sep">/</span>component checklist',
    "Lista do que precisa estar pronto antes de um componente entrar no sistema. Use como guia ao propor PR.",
    "".join([
        sec("a11y", "acessibilidade", "01",
            checklist([
                "Operável só com teclado",
                "Estado focado é evidente visualmente (outline 2px)",
                "Contraste 4.5:1 em texto / 3:1 em bordas",
                "ARIA aplicado conforme APG do tipo de componente",
                "Funciona em leitor de tela (testar com NVDA ou VoiceOver)",
                "prefers-reduced-motion respeitado se há animação",
                "Áreas de toque ≥ 44×44px",
            ])),
        sec("design", "design", "02",
            checklist([
                "Usa tokens semânticos, não cores cruas",
                "Spacing em múltiplos do BIT",
                "Funciona em ambos os temas (light e dark)",
                "Estados cobertos: default, hover, focus, active, disabled",
                "Responsivo (mobile <600 / tablet <1024 / desktop)",
            ])),
        sec("docs", "documentação", "03",
            checklist([
                "Página com TOC + 10 seções (overview, variants, sizes, states, anatomy, behaviors, modifiers, usage, a11y, code)",
                "Demo interativa funcional",
                "Anatomy SVG anotada",
                "Exemplos de uso claros (do/don't)",
                "Código copiável (HTML/CSS/JS)",
                "Listado em components/index.html",
                "Adicionado ao navConfig do shell.js",
            ])),
        sec("code", "código", "04",
            checklist([
                "CSS no styles.css (não inline)",
                "JS interativo no components.js (não inline)",
                "BEM-like naming (.component, .component__elem, .component--modifier)",
                "Sem dependências externas (manter zero-build)",
                "Funciona em browsers modernos (Chrome, Firefox, Safari, Edge)",
            ])),
    ]),
    toc=[{"id":"a11y","label":"Acessibilidade"},{"id":"design","label":"Design"},{"id":"docs","label":"Documentação"},{"id":"code","label":"Código"}],
))

write("pages/contributing/pdlc.html", page(
    "pdlc", "Lifecycle (PDLC)",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">contributing</a><span class="sep">/</span>lifecycle',
    "Product Design Lifecycle: as 5 etapas que um componente percorre, do conceito ao sistema.",
    "".join([
        sec("stages", "5 etapas", "01",
            table(["etapa","status","critério pra avançar"], [
                ["1. proposal","ideia","issue aprovada por maintainer"],
                ["2. exploration","draft","protótipo aprovado por design"],
                ["3. development","beta","código + docs + a11y completos"],
                ["4. release","stable","review de maintainer + a11y audit"],
                ["5. maintenance","stable","bugs corrigidos, evolução versionada"],
            ])),
        sec("status-badges", "status badges", "02",
            demo('<div class="row" style="gap: var(--spacing-04)"><span class="status-badge status-badge--draft">draft</span><span class="status-badge status-badge--beta">beta</span><span class="status-badge status-badge--stable">stable</span><span class="status-badge status-badge--new">new</span></div>')),
        sec("deprecation", "deprecation", "03",
            '<p class="t-body-02 t-secondary prose">Componentes deprecated mantêm 1 versão major suportada. Avisos no console e no docs. Substituição recomendada clara na página do componente.</p>'),
    ]),
    toc=[{"id":"stages","label":"5 etapas"},{"id":"status-badges","label":"Status badges"},{"id":"deprecation","label":"Deprecation"}],
))

write("pages/contributing/documentation.html", page(
    "docs-guide", "Documentation",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">contributing</a><span class="sep">/</span>documentation',
    "Como documentar componentes e patterns pra que façam sentido pros próximos. Princípios de boa documentação.",
    "".join([
        sec("structure", "estrutura padrão", "01",
            '<p class="t-body-02 t-secondary mb-05 prose">Toda página de componente segue a estrutura abaixo. Use o gerador Python ou copie de uma página existente como base.</p>' +
            checklist([
                "Page header: breadcrumb + title + intro + tags",
                "TOC com links pra cada seção",
                "Overview com demo principal",
                "Variants (cores, estilos)",
                "Sizes (quando aplicável)",
                "States (default, hover, focus, disabled, etc.)",
                "Anatomy SVG anotada",
                "Behaviors (interações específicas)",
                "Modifiers / API (tabela)",
                "Usage (do/don't grid)",
                "Accessibility (WCAG + ARIA)",
                "Code (HTML/CSS/JS copiável)",
                "Related (links pra componentes correlatos)",
            ])),
        sec("voice", "tom", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">Direto, em pt-br caixa baixa. Frases curtas. Comandos no infinitivo. Exemplos comparados (faz/não faz) em vez de prescrições vagas.</p>' +
            '<p class="t-body-02 t-secondary mb-05 prose">Veja <a class="link" href="../guidelines/content.html">content & voice</a> pra detalhes.</p>'),
        sec("code-examples", "code examples", "03",
            checklist([
                "Mínimo viável — só o necessário pra entender",
                "Sintaxe HTML semântica",
                "Comentários em pt-br explicando o porquê",
                "Botão copy automático (já vem via shell.js)",
                "Mostrar variantes em snippets separados",
            ])),
    ]),
    toc=[{"id":"structure","label":"Estrutura padrão"},{"id":"voice","label":"Tom"},{"id":"code-examples","label":"Code examples"}],
))

# ----- HELP -----------------------------------------------------------------
write("pages/help/index.html", page(
    "help-contact", "Help · Contato",
    '<a href="../../index.html">home</a><span class="sep">/</span>help',
    "Canais oficiais pra tirar dúvida, reportar bug ou propor melhoria no CHDS.",
    "".join([
        sec("channels", "canais", "01",
            grid([
                {"title":"github issues","desc":"Bug reports, feature requests, dúvidas técnicas. <a class='link' href='https://github.com/casahacker/design-system/issues' target='_blank' rel='noopener'>abrir issue ↗</a>"},
                {"title":"github discussions","desc":"Conversas mais longas sobre direção do sistema, casos de uso, comparações."},
                {"title":"docs","desc":"A maior parte das perguntas já está respondida aqui — veja a <a class='link' href='faq.html'>FAQ</a>."},
            ])),
        sec("response", "tempo de resposta", "02",
            '<p class="t-body-02 t-secondary prose">Equipe é pequena, voluntária e atende em horário comercial. Issues técnicas: 3-5 dias úteis. PRs: 5-7 dias úteis. Pra urgências, marca como "urgent" no título.</p>'),
    ]),
    toc=[{"id":"channels","label":"Canais"},{"id":"response","label":"Tempo de resposta"}],
))

write("pages/help/faq.html", page(
    "help-faq", "FAQ",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">help</a><span class="sep">/</span>faq',
    "Perguntas frequentes sobre o Casa Hacker Design System.",
    "".join([
        sec("usage", "uso", "01",
            '<div class="accordion" data-mode="single">' +
            '<div class="accordion-item open"><button class="accordion-header" type="button">posso usar o CHDS num projeto comercial? <span class="chevron">›</span></button><div class="accordion-body">Sim. Código é MIT, conteúdo de marca é CC BY-SA. Use à vontade, com atribuição.</div></div>' +
            '<div class="accordion-item"><button class="accordion-header" type="button">preciso de framework (react, vue) pra usar? <span class="chevron">›</span></button><div class="accordion-body">Não. É HTML/CSS/JS vanilla. Funciona em qualquer stack — basta importar styles.css e (opcionalmente) shell.js + components.js.</div></div>' +
            '<div class="accordion-item"><button class="accordion-header" type="button">como mudar a cor primária pra outra? <span class="chevron">›</span></button><div class="accordion-body">Sobrescreva <code class="code-inline">--ch-code</code> no :root e nas variantes dark. Os tokens semânticos que apontam pra ela atualizam em cadeia.</div></div>' +
            '</div>'),
        sec("contributing", "contribuição", "02",
            '<div class="accordion" data-mode="single">' +
            '<div class="accordion-item"><button class="accordion-header" type="button">como propor um componente novo? <span class="chevron">›</span></button><div class="accordion-body">Abre uma issue descrevendo o problema (não a solução) primeiro. Após validação, segue o <a class="link" href="../contributing/pdlc.html">PDLC</a>.</div></div>' +
            '<div class="accordion-item"><button class="accordion-header" type="button">posso traduzir o sistema pra outra língua? <span class="chevron">›</span></button><div class="accordion-body">No momento priorizamos pt-br. Traduções comunitárias em fork são bem-vindas. PR pra inglês pode ser aceito no futuro como segunda língua oficial.</div></div>' +
            '</div>'),
        sec("tech", "técnico", "03",
            '<div class="accordion" data-mode="single">' +
            '<div class="accordion-item"><button class="accordion-header" type="button">por que zero-build? <span class="chevron">›</span></button><div class="accordion-body">Pra reduzir barreira de entrada (qualquer pessoa edita HTML/CSS sem npm install), facilitar deploy em qualquer estático, e evitar dependência de toolchain JS.</div></div>' +
            '<div class="accordion-item"><button class="accordion-header" type="button">qual o suporte de browsers? <span class="chevron">›</span></button><div class="accordion-body">Browsers evergreen: Chrome, Firefox, Safari, Edge — últimas 2 versões. CSS custom properties são essenciais — IE11 não é suportado.</div></div>' +
            '<div class="accordion-item"><button class="accordion-header" type="button">posso usar só os tokens sem os componentes? <span class="chevron">›</span></button><div class="accordion-body">Sim — basta importar a parte de :root do styles.css e usar via var().</div></div>' +
            '</div>'),
    ]),
    toc=[{"id":"usage","label":"Uso"},{"id":"contributing","label":"Contribuição"},{"id":"tech","label":"Técnico"}],
))

print("done · brand + contributing + help")
