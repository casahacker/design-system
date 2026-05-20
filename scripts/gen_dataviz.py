"""Data Visualization — rebuild completo (8 páginas).

Inclui SVGs inline reais (bar, line, area, pie, scatter, heatmap, etc.)
construídos por helpers Python — light + dark theme-aware via tokens CSS.
"""
from common import page, sec, demo, do_dont, code, checklist, table, related, write, anatomy, api_table, grid

# Paleta categórica (apontando pros tokens --dv-cat-N)
CAT = ['var(--dv-cat-1)','var(--dv-cat-2)','var(--dv-cat-3)','var(--dv-cat-4)',
       'var(--dv-cat-5)','var(--dv-cat-6)','var(--dv-cat-7)','var(--dv-cat-8)']

# ============================================================================
# SVG CHART HELPERS
# ============================================================================
def svg_open(w=520, h=240, label=''):
    """SVG container chart-aware."""
    return f'<svg class="chart-svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">'

def svg_close():
    return '</svg>'

def axis_x(x0, y, x1, ticks):
    """Eixo X horizontal com ticks."""
    out = f'<line class="axis-line" x1="{x0}" y1="{y}" x2="{x1}" y2="{y}"/>'
    n = len(ticks)
    if n > 1:
        step = (x1 - x0) / (n - 1) if n > 1 else 0
        for i, label in enumerate(ticks):
            x = x0 + step * i
            out += f'<text x="{x}" y="{y+14}" text-anchor="middle">{label}</text>'
    return out

def axis_y(x, y0, y1, ticks, max_val):
    """Eixo Y com gridlines."""
    out = ''
    for tick in ticks:
        y = y0 - (tick / max_val) * (y0 - y1)
        out += f'<line class="grid-line" x1="{x}" y1="{y}" x2="{x+460}" y2="{y}"/>'
        out += f'<text x="{x-6}" y="{y+3}" text-anchor="end">{tick}</text>'
    return out

# ---- BAR CHART ----
def bar_chart(data, labels, colors=None, w=520, h=240, label='gráfico de barras'):
    """data: [valores]. labels: [strings]. colors: opcional, list of CSS colors."""
    colors = colors or [CAT[0]] * len(data)
    pad_l, pad_r, pad_t, pad_b = 40, 16, 16, 32
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b
    max_val = max(data) * 1.1
    bar_w = plot_w / len(data) * 0.7
    gap = plot_w / len(data) * 0.3
    out = svg_open(w, h, label)
    # Y axis
    yticks = [0, round(max_val * 0.25), round(max_val * 0.5), round(max_val * 0.75), round(max_val)]
    for t in yticks:
        y = pad_t + plot_h - (t / max_val) * plot_h
        out += f'<line class="grid-line" x1="{pad_l}" y1="{y}" x2="{w-pad_r}" y2="{y}"/>'
        out += f'<text x="{pad_l-6}" y="{y+3}" text-anchor="end">{int(t)}</text>'
    out += f'<line class="axis-line" x1="{pad_l}" y1="{pad_t+plot_h}" x2="{w-pad_r}" y2="{pad_t+plot_h}"/>'
    # Bars
    for i, val in enumerate(data):
        bar_h = (val / max_val) * plot_h
        x = pad_l + (plot_w / len(data)) * i + gap / 2
        y = pad_t + plot_h - bar_h
        out += f'<g class="bar-group">'
        out += f'<rect class="bar" x="{x}" y="{y}" width="{bar_w}" height="{bar_h}" fill="{colors[i % len(colors)]}"/>'
        out += f'<g class="tip" transform="translate({x + bar_w/2},{y-8})"><rect x="-22" y="-18" width="44" height="18" rx="1"/><text x="0" y="-5" text-anchor="middle">{val}</text></g>'
        out += '</g>'
        out += f'<text x="{x+bar_w/2}" y="{pad_t+plot_h+14}" text-anchor="middle">{labels[i]}</text>'
    out += svg_close()
    return out

# ---- LINE CHART ----
def line_chart(series, x_labels, colors=None, w=520, h=240, label='gráfico de linha'):
    """series: list of lists. x_labels: comum entre séries."""
    colors = colors or CAT
    pad_l, pad_r, pad_t, pad_b = 40, 16, 16, 32
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b
    max_val = max(max(s) for s in series) * 1.1
    n = len(x_labels)
    step_x = plot_w / (n - 1) if n > 1 else plot_w
    out = svg_open(w, h, label)
    # Gridlines + Y axis
    yticks = [0, round(max_val * 0.25), round(max_val * 0.5), round(max_val * 0.75), round(max_val)]
    for t in yticks:
        y = pad_t + plot_h - (t / max_val) * plot_h
        out += f'<line class="grid-line" x1="{pad_l}" y1="{y}" x2="{w-pad_r}" y2="{y}"/>'
        out += f'<text x="{pad_l-6}" y="{y+3}" text-anchor="end">{int(t)}</text>'
    out += f'<line class="axis-line" x1="{pad_l}" y1="{pad_t+plot_h}" x2="{w-pad_r}" y2="{pad_t+plot_h}"/>'
    # X labels
    for i, lbl in enumerate(x_labels):
        x = pad_l + step_x * i
        out += f'<text x="{x}" y="{pad_t+plot_h+14}" text-anchor="middle">{lbl}</text>'
    # Lines + points
    for si, s in enumerate(series):
        pts = [(pad_l + step_x * i, pad_t + plot_h - (v / max_val) * plot_h) for i, v in enumerate(s)]
        path = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        c = colors[si % len(colors)]
        out += f'<polyline class="line" points="{path}" stroke="{c}"/>'
        for x, y in pts:
            out += f'<circle class="point" cx="{x}" cy="{y}" r="3" fill="{c}"/>'
    out += svg_close()
    return out

# ---- AREA CHART ----
def area_chart(data, x_labels, color=None, w=520, h=240, label='gráfico de área'):
    color = color or CAT[0]
    pad_l, pad_r, pad_t, pad_b = 40, 16, 16, 32
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b
    max_val = max(data) * 1.1
    n = len(data)
    step_x = plot_w / (n - 1) if n > 1 else plot_w
    out = svg_open(w, h, label)
    yticks = [0, round(max_val * 0.5), round(max_val)]
    for t in yticks:
        y = pad_t + plot_h - (t / max_val) * plot_h
        out += f'<line class="grid-line" x1="{pad_l}" y1="{y}" x2="{w-pad_r}" y2="{y}"/>'
        out += f'<text x="{pad_l-6}" y="{y+3}" text-anchor="end">{int(t)}</text>'
    out += f'<line class="axis-line" x1="{pad_l}" y1="{pad_t+plot_h}" x2="{w-pad_r}" y2="{pad_t+plot_h}"/>'
    for i, lbl in enumerate(x_labels):
        x = pad_l + step_x * i
        out += f'<text x="{x}" y="{pad_t+plot_h+14}" text-anchor="middle">{lbl}</text>'
    pts = [(pad_l + step_x * i, pad_t + plot_h - (v / max_val) * plot_h) for i, v in enumerate(data)]
    poly = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    area_poly = f'{pad_l},{pad_t+plot_h} ' + poly + f' {pad_l+plot_w},{pad_t+plot_h}'
    out += f'<polygon class="area" points="{area_poly}" fill="{color}"/>'
    out += f'<polyline class="line" points="{poly}" stroke="{color}"/>'
    out += svg_close()
    return out

# ---- PIE/DONUT ----
def pie_chart(data, labels, colors=None, donut=False, w=200, h=200, label='gráfico de pizza'):
    import math
    colors = colors or CAT
    total = sum(data)
    cx, cy = w / 2, h / 2
    r = min(w, h) * 0.45
    ir = r * 0.6 if donut else 0
    out = svg_open(w, h, label)
    angle_start = -math.pi / 2
    for i, v in enumerate(data):
        angle = (v / total) * 2 * math.pi
        angle_end = angle_start + angle
        x1 = cx + r * math.cos(angle_start); y1 = cy + r * math.sin(angle_start)
        x2 = cx + r * math.cos(angle_end);   y2 = cy + r * math.sin(angle_end)
        large = 1 if angle > math.pi else 0
        if donut:
            xi1 = cx + ir * math.cos(angle_start); yi1 = cy + ir * math.sin(angle_start)
            xi2 = cx + ir * math.cos(angle_end);   yi2 = cy + ir * math.sin(angle_end)
            d = f'M {x1:.2f} {y1:.2f} A {r} {r} 0 {large} 1 {x2:.2f} {y2:.2f} L {xi2:.2f} {yi2:.2f} A {ir} {ir} 0 {large} 0 {xi1:.2f} {yi1:.2f} Z'
        else:
            d = f'M {cx} {cy} L {x1:.2f} {y1:.2f} A {r} {r} 0 {large} 1 {x2:.2f} {y2:.2f} Z'
        out += f'<path class="bar" d="{d}" fill="{colors[i % len(colors)]}"/>'
        angle_start = angle_end
    out += svg_close()
    return out

# ---- SCATTER ----
def scatter_chart(points, w=520, h=240, label='gráfico de dispersão'):
    """points: [(x, y, optional_size)]."""
    pad_l, pad_r, pad_t, pad_b = 40, 16, 16, 32
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b
    xs = [p[0] for p in points]; ys = [p[1] for p in points]
    xmax = max(xs) * 1.1; ymax = max(ys) * 1.1
    out = svg_open(w, h, label)
    yticks = [0, round(ymax * 0.5), round(ymax)]
    for t in yticks:
        y = pad_t + plot_h - (t / ymax) * plot_h
        out += f'<line class="grid-line" x1="{pad_l}" y1="{y}" x2="{w-pad_r}" y2="{y}"/>'
        out += f'<text x="{pad_l-6}" y="{y+3}" text-anchor="end">{int(t)}</text>'
    out += f'<line class="axis-line" x1="{pad_l}" y1="{pad_t+plot_h}" x2="{w-pad_r}" y2="{pad_t+plot_h}"/>'
    for p in points:
        size = p[2] if len(p) > 2 else 4
        x = pad_l + (p[0] / xmax) * plot_w
        y = pad_t + plot_h - (p[1] / ymax) * plot_h
        out += f'<circle class="point" cx="{x:.1f}" cy="{y:.1f}" r="{size}" fill="{CAT[0]}" opacity="0.7"/>'
    out += svg_close()
    return out

# ---- HEATMAP ----
def heatmap(rows, cols, values, w=520, h=240, label='heatmap'):
    """values: matrix [row][col] of 0-1 normalized."""
    pad_l, pad_r, pad_t, pad_b = 100, 16, 16, 32
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b
    cell_w = plot_w / len(cols)
    cell_h = plot_h / len(rows)
    out = svg_open(w, h, label)
    for ri, row in enumerate(rows):
        out += f'<text x="{pad_l-6}" y="{pad_t + cell_h*ri + cell_h/2 + 3}" text-anchor="end">{row}</text>'
        for ci, val in enumerate(values[ri]):
            opacity = 0.1 + val * 0.9
            x = pad_l + cell_w * ci
            y = pad_t + cell_h * ri
            out += f'<rect x="{x}" y="{y}" width="{cell_w-1}" height="{cell_h-1}" fill="var(--ch-code)" opacity="{opacity:.2f}"/>'
    for ci, col in enumerate(cols):
        out += f'<text x="{pad_l + cell_w*ci + cell_w/2}" y="{pad_t+plot_h+14}" text-anchor="middle">{col}</text>'
    out += svg_close()
    return out

def legend(items):
    """items: [(label, color, 'dot'|'line')]."""
    out = '<div class="chart-legend">'
    for lbl, c, kind in items:
        if kind == 'line':
            out += f'<span class="chart-legend-item"><span class="line" style="background:{c}"></span>{lbl}</span>'
        else:
            out += f'<span class="chart-legend-item"><span class="dot" style="background:{c}"></span>{lbl}</span>'
    out += '</div>'
    return out

def chart_card(title, subtitle, svg, source='', legend_html=''):
    src = f'<p class="chart-source">{source}</p>' if source else ''
    leg = legend_html if legend_html else ''
    return f'<div class="chart"><div class="chart-title">{title}</div><div class="chart-subtitle">{subtitle}</div>{svg}{leg}{src}</div>'

# ============================================================================
# PAGE 1 · OVERVIEW
# ============================================================================
write("pages/dataviz/index.html", page(
    "dv-overview", "Data Visualization",
    '<a href="../../index.html">home</a><span class="sep">/</span>data visualization',
    "Sistema de visualização de dados Casa Hacker. Charts respondem perguntas — escolha errada de chart gera mais confusão que clareza. Tipos canônicos, paletas brand-aligned, padrões de interação e regras de acessibilidade.",
    "".join([
        sec("why", "por que data viz", "01 · contexto",
            '<p class="t-body-02 t-secondary mb-05 prose">A Casa Hacker mede impacto: alunos matriculados, hackerclubes ativos, oficinas realizadas, parcerias firmadas. Dados sem visualização são planilhas — visualizações sem método são desinformação. Este sistema dá vocabulário visual consistente em produto, relatório e impressos.</p>'),
        sec("principles", "4 princípios", "02",
            '<div class="grid-2">' +
            '<div class="tile tile--bordered"><h4>verdadeiro</h4><p>O chart conta a verdade dos dados. Eixo Y começa no zero quando faz sentido. Sem distorções intencionais ou acidentais.</p></div>' +
            '<div class="tile tile--bordered"><h4>simples</h4><p>1 mensagem por chart. Tira tudo o que não ajuda a entender. Chart-junk (grades pesadas, sombras, gradientes decorativos) sai.</p></div>' +
            '<div class="tile tile--bordered"><h4>acessível</h4><p>Cor + texto + ícone. Tabular fallback. Daltonismo-safe. Funciona com leitor de tela.</p></div>' +
            '<div class="tile tile--bordered"><h4>insightful</h4><p>Não basta ser bonito — precisa revelar padrão, comparar, contar uma história que números crus não contam.</p></div>' +
            '</div>'),
        sec("picker", "que chart usar?", "03 · matriz de decisão",
            '<p class="t-body-02 t-secondary mb-05 prose">Comece pela pergunta. Cada pergunta tem 1-2 charts ideais.</p>' +
            table(["pergunta","chart ideal"], [
                ["Comparar valores entre categorias","Bar"],
                ["Mostrar mudança ao longo do tempo","Line"],
                ["Mostrar composição (% do todo)","Pie/Donut (≤5 fatias) ou Stacked bar"],
                ["Mostrar distribuição de valores","Histogram"],
                ["Correlação entre duas variáveis","Scatter"],
                ["Densidade de valores em 2D","Heatmap"],
                ["Hierarquia + proporção","Treemap"],
                ["Evolução de partes ao longo do tempo","Stacked area"],
                ["Métrica única destacada","Big number / KPI tile"],
                ["Tendência inline em pouco espaço","Sparkline"],
            ])),
        sec("showcase", "preview", "04",
            '<p class="t-body-02 t-secondary mb-05 prose">Cada uma das 8 páginas desta seção entra em detalhe.</p>' +
            '<div class="resource-cards">' +
            '<a class="resource-card" href="anatomy.html"><div class="meta">structure</div><h4>chart anatomy</h4><p>Partes universais de qualquer chart.</p><span class="cta">explorar</span></a>' +
            '<a class="resource-card" href="types.html"><div class="meta">gallery</div><h4>chart types</h4><p>12 tipos com SVG, código e quando usar.</p><span class="cta">explorar</span></a>' +
            '<a class="resource-card" href="colors.html"><div class="meta">paleta</div><h4>color palettes</h4><p>Categórica · sequencial · divergente · status.</p><span class="cta">explorar</span></a>' +
            '<a class="resource-card" href="labels.html"><div class="meta">type</div><h4>labels & axes</h4><p>Annotations, formatting numérico, eixos.</p><span class="cta">explorar</span></a>' +
            '<a class="resource-card" href="interaction.html"><div class="meta">behaviors</div><h4>interaction</h4><p>Hover, tooltip, legend toggle, drill-down.</p><span class="cta">explorar</span></a>' +
            '<a class="resource-card" href="accessibility.html"><div class="meta">a11y</div><h4>accessibility</h4><p>Alt text, fallback tabular, color-blind safe.</p><span class="cta">explorar</span></a>' +
            '<a class="resource-card" href="examples.html"><div class="meta">in-context</div><h4>examples</h4><p>Dashboards compostos, casos Casa Hacker reais.</p><span class="cta">explorar</span></a>' +
            '</div>'),
    ]),
    tags=[{"cls":"tag--script","label":"beta"}, {"cls":"tag--code","label":"8 páginas"}],
    toc=[{"id":"why","label":"Por que data viz"},{"id":"principles","label":"4 princípios"},{"id":"picker","label":"Que chart usar?"},{"id":"showcase","label":"Preview"}],
))

# ============================================================================
# PAGE 2 · ANATOMY
# ============================================================================
anatomy_svg = '''<svg viewBox="0 0 640 380" class="chart-svg" role="img" aria-label="anatomia anotada de um chart">
  <!-- title area -->
  <text x="60" y="36" font-size="14" font-weight="600" fill="var(--text-primary)">vendas mensais 2026</text>
  <text x="60" y="52" font-size="10" fill="var(--text-helper)">// faturamento por mês · em R$ mil</text>

  <!-- y axis ticks + gridlines -->
  <line class="grid-line" x1="100" y1="90"  x2="600" y2="90"/>
  <line class="grid-line" x1="100" y1="150" x2="600" y2="150"/>
  <line class="grid-line" x1="100" y1="210" x2="600" y2="210"/>
  <line class="grid-line" x1="100" y1="270" x2="600" y2="270"/>
  <line class="axis-line" x1="100" y1="330" x2="600" y2="330"/>
  <text x="94" y="93"  text-anchor="end">100</text>
  <text x="94" y="153" text-anchor="end">75</text>
  <text x="94" y="213" text-anchor="end">50</text>
  <text x="94" y="273" text-anchor="end">25</text>
  <text x="94" y="333" text-anchor="end">0</text>

  <!-- axis title Y -->
  <text x="40" y="200" transform="rotate(-90,40,200)" text-anchor="middle" font-size="9" fill="var(--text-helper)">FATURAMENTO (R$ mil)</text>

  <!-- bars -->
  <rect class="bar" x="115" y="180" width="32" height="150" fill="var(--dv-cat-1)"/>
  <rect class="bar" x="170" y="200" width="32" height="130" fill="var(--dv-cat-1)"/>
  <rect class="bar" x="225" y="140" width="32" height="190" fill="var(--dv-cat-1)"/>
  <rect class="bar" x="280" y="170" width="32" height="160" fill="var(--dv-cat-1)"/>
  <rect class="bar" x="335" y="110" width="32" height="220" fill="var(--dv-cat-1)"/>
  <rect class="bar" x="390" y="130" width="32" height="200" fill="var(--dv-cat-1)"/>
  <rect class="bar" x="445" y="150" width="32" height="180" fill="var(--dv-cat-1)"/>
  <rect class="bar" x="500" y="100" width="32" height="230" fill="var(--dv-cat-1)"/>
  <rect class="bar" x="555" y="80"  width="32" height="250" fill="var(--dv-cat-1)"/>

  <!-- x labels -->
  <text x="131" y="346" text-anchor="middle">jan</text>
  <text x="186" y="346" text-anchor="middle">fev</text>
  <text x="241" y="346" text-anchor="middle">mar</text>
  <text x="296" y="346" text-anchor="middle">abr</text>
  <text x="351" y="346" text-anchor="middle">mai</text>
  <text x="406" y="346" text-anchor="middle">jun</text>
  <text x="461" y="346" text-anchor="middle">jul</text>
  <text x="516" y="346" text-anchor="middle">ago</text>
  <text x="571" y="346" text-anchor="middle">set</text>

  <!-- axis title X -->
  <text x="350" y="375" text-anchor="middle" font-size="9" fill="var(--text-helper)">MÊS</text>

  <!-- annotation -->
  <line x1="571" y1="60" x2="571" y2="80" stroke="#DA1E28" stroke-width="1"/>
  <text x="568" y="56" text-anchor="end" font-size="9" fill="#DA1E28" font-weight="600">recorde</text>

  <!-- numbered markers -->
  <g font-family="IBM Plex Mono" font-weight="600" font-size="11">
    <circle cx="60" cy="36" r="9" fill="#FFF" stroke="#91938C"/><text x="56" y="40" fill="#3C433C">1</text>
    <circle cx="60" cy="52" r="9" fill="#FFF" stroke="#91938C"/><text x="56" y="56" fill="#3C433C">2</text>
    <circle cx="40" cy="200" r="9" fill="#FFF" stroke="#91938C"/><text x="36" y="204" fill="#3C433C">3</text>
    <circle cx="94" cy="93" r="9" fill="#FFF" stroke="#91938C"/><text x="90" y="97" fill="#3C433C">4</text>
    <circle cx="100" cy="150" r="9" fill="#FFF" stroke="#91938C"/><text x="96" y="154" fill="#3C433C">5</text>
    <circle cx="295" cy="210" r="9" fill="#FFF" stroke="#91938C"/><text x="291" y="214" fill="#3C433C">6</text>
    <circle cx="350" cy="375" r="9" fill="#FFF" stroke="#91938C"/><text x="346" y="379" fill="#3C433C">7</text>
    <circle cx="571" cy="56" r="9" fill="#FFF" stroke="#91938C"/><text x="567" y="60" fill="#3C433C">8</text>
  </g>
</svg>'''

write("pages/dataviz/anatomy.html", page(
    "dv-anatomy", "Chart anatomy",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">data visualization</a><span class="sep">/</span>anatomy',
    "Partes universais de qualquer chart. Todo gráfico bem construído tem essas peças nos mesmos lugares — vira linguagem comum entre quem lê.",
    "".join([
        sec("annotated", "anatomia anotada", "01",
            f'<div class="anatomy">{anatomy_svg}<ol class="anatomy-legend">'
            '<li>Título · resposta direta à pergunta que o chart responde · heading-02</li>'
            '<li>Subtítulo · unidade, período, fonte breve · label-01 mono</li>'
            '<li>Título do eixo Y · unidade ou variável · uppercase 9pt (rotacionado)</li>'
            '<li>Ticks Y · valores numéricos · mono 10pt right-aligned</li>'
            '<li>Gridlines · subtle (dashed) · apenas horizontais em bar/line</li>'
            '<li>Plot area · onde os dados moram · padding interno generoso (16-24px)</li>'
            '<li>Eixo X · labels de categoria ou tempo · mono 10pt center-aligned</li>'
            '<li>Annotation · destaque pontual (recorde, anomalia, meta) · cor de support quando crítico</li>'
            '</ol></div>'),
        sec("title", "título e subtítulo", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">Título responde a pergunta. Subtítulo dá contexto.</p>' +
            do_dont(
                ['"vendas mensais 2026" — claro, datado','"// faturamento em R$ mil" — unidade explícita','Subtítulo opcional quando título já basta'],
                ['"gráfico de barras" — descreve forma, não conteúdo','Título sem unidade ("vendas") — força ler eixos pra entender','Título genérico ("dados", "performance")'],
            )),
        sec("axes", "eixos", "03",
            '<div class="grid-2">' +
            '<div class="tile tile--bordered"><h4>eixo y</h4><p>Comece em zero pra bar/area (truncar distorce). Line pode truncar se a variação for sutil — sempre indique.</p></div>' +
            '<div class="tile tile--bordered"><h4>eixo x</h4><p>Tempo da esquerda pra direita. Categorias ordenadas por valor decrescente quando comparação.</p></div>' +
            '</div>'),
        sec("gridlines", "gridlines", "04",
            '<p class="t-body-02 t-secondary prose">Só horizontais em bar/line. Tracejadas, cor <code class="code-inline">--dv-gridline</code> (subtle). Verticais só em scatter ou quando ajuda a leitura. Nunca grades duplas (X+Y juntos) — vira tabela.</p>'),
        sec("legend", "legenda", "05",
            '<p class="t-body-02 t-secondary mb-05 prose">Necessária quando há 2+ séries. Pode ficar abaixo do chart ou inline com direct labels.</p>' +
            do_dont(
                ['Legenda inline em line com poucas séries (≤3)','Legenda abaixo em pies/bars empilhadas','Cor + texto sempre (nunca só cor)'],
                ['Legenda longa em chart pequeno (vira maior que o chart)','Cor crua sem label adjacente','Legenda no topo (rouba foco do título)'],
            )),
        sec("tooltip", "tooltip", "06",
            '<p class="t-body-02 t-secondary mb-05 prose">Aparece on-hover (ou tap mobile). Mostra valor exato + label + comparação opcional.</p>' +
            chart_card("hover sobre uma barra", "experimenta passar o mouse",
                       bar_chart([45, 32, 60, 38, 72, 55, 80], ['seg','ter','qua','qui','sex','sáb','dom'], label='exemplos de hover'),
                       "demonstração · valores fictícios")),
        sec("source", "fonte", "07",
            '<p class="t-body-02 t-secondary prose">Sempre cite a fonte dos dados. Texto pequeno (code-01) abaixo do chart. Quando interno, datar a query: <code class="code-inline">// extração: 2026-05-19</code>.</p>'),
        sec("spacing", "spacing", "08 · BIT-aligned",
            checklist([
                "Padding interno do chart: spacing-06 (24px)",
                "Distância título → plot: spacing-04 (12px)",
                "Distância plot → eixo X labels: spacing-03 (8px)",
                "Distância chart → fonte: spacing-04",
                "Spacing entre charts num dashboard: spacing-05 (16px)",
            ])),
    ]),
    toc=[{"id":"annotated","label":"Anatomia anotada"},{"id":"title","label":"Título"},{"id":"axes","label":"Eixos"},{"id":"gridlines","label":"Gridlines"},{"id":"legend","label":"Legenda"},{"id":"tooltip","label":"Tooltip"},{"id":"source","label":"Fonte"},{"id":"spacing","label":"Spacing"}],
))

# ============================================================================
# PAGE 3 · TYPES (12 tipos com SVG real)
# ============================================================================
def type_block(name, when, when_not, svg, code_hint=''):
    body = f'<div class="grid-2"><div>{svg}</div><div class="stack-05">'
    body += f'<div class="tile tile--bordered"><h4>quando usar</h4><ul class="bare">{"".join(f"<li>{w}</li>" for w in when)}</ul></div>'
    body += f'<div class="tile tile--bordered"><h4>quando NÃO usar</h4><ul class="bare">{"".join(f"<li>{w}</li>" for w in when_not)}</ul></div>'
    if code_hint:
        body += f'<p class="t-helper">{code_hint}</p>'
    body += '</div></div>'
    return body

types_body = ''

# bar simples
types_body += sec("bar", "bar chart (simples)", "01",
    type_block("bar",
        ["comparar valores entre categorias", "ranking (ordenado decrescente)", "5-30 categorias"],
        ["séries temporais contínuas — usa line", "mais de 30 itens — usa horizontal scrollable", "porcentagens de um todo — usa stacked bar"],
        chart_card("hackerclubes ativos por região", "número de clubes em maio/2026",
                   bar_chart([42, 28, 35, 18, 22], ['sudeste','nordeste','sul','norte','centro'], label='bar chart'),
                   "demonstração · dados fictícios")))

# bar grouped
types_body += sec("bar-grouped", "bar chart (agrupado)", "02",
    type_block("grouped bar",
        ["comparar 2-3 subcategorias por categoria principal", "comparação ano sobre ano"],
        ["mais de 3 subcategorias — vira mosaico", "categorias com escalas muito diferentes"],
        chart_card("alunos por programa · 2025 vs 2026", "evolução por programa",
                   # Custom grouped bar
                   f'''<svg class="chart-svg" viewBox="0 0 520 240" role="img" aria-label="bar agrupado">
  <line class="grid-line" x1="40" y1="50" x2="504" y2="50"/>
  <line class="grid-line" x1="40" y1="110" x2="504" y2="110"/>
  <line class="grid-line" x1="40" y1="170" x2="504" y2="170"/>
  <line class="axis-line" x1="40" y1="200" x2="504" y2="200"/>
  <text x="34" y="53" text-anchor="end">600</text>
  <text x="34" y="113" text-anchor="end">400</text>
  <text x="34" y="173" text-anchor="end">200</text>
  <text x="34" y="203" text-anchor="end">0</text>
  ''' + ''.join(
    f'<rect x="{60+i*100}" y="{200-h1}" width="34" height="{h1}" fill="{CAT[0]}"/>'
    f'<rect x="{96+i*100}" y="{200-h2}" width="34" height="{h2}" fill="{CAT[1]}"/>'
    f'<text x="{95+i*100}" y="220" text-anchor="middle">{lbl}</text>'
    for i, (lbl, h1, h2) in enumerate([
      ('hackerclubes',80,120), ('inclusão',60,95), ('minas',45,70), ('mão massa',55,80)])
  ) +
  '</svg>',
                   "demonstração",
                   legend([('2025', CAT[0], 'dot'), ('2026', CAT[1], 'dot')]))))

# stacked bar
types_body += sec("bar-stacked", "bar chart (empilhado)", "03",
    type_block("stacked bar",
        ["composição (parte do todo) por categoria", "comparar tamanho total + subcategorias"],
        ["se quer comparar valores absolutos das subcategorias entre si — usa grouped", "muitas subcategorias — fica ilegível"],
        chart_card("composição de horas por atividade", "por programa",
                   f'''<svg class="chart-svg" viewBox="0 0 520 240" role="img" aria-label="bar empilhado">
  <line class="axis-line" x1="40" y1="200" x2="504" y2="200"/>
  ''' + ''.join(
    f'<g><rect x="{60+i*100}" y="{200-h1-h2-h3}" width="60" height="{h3}" fill="{CAT[2]}"/>'
    f'<rect x="{60+i*100}" y="{200-h1-h2}" width="60" height="{h2}" fill="{CAT[1]}"/>'
    f'<rect x="{60+i*100}" y="{200-h1}" width="60" height="{h1}" fill="{CAT[0]}"/>'
    f'<text x="{90+i*100}" y="220" text-anchor="middle">{lbl}</text></g>'
    for i, (lbl, h1, h2, h3) in enumerate([
      ('jan',60,40,30), ('fev',55,50,35), ('mar',70,45,40), ('abr',80,60,45)])
  ) +
  '</svg>',
                   "demonstração",
                   legend([('oficinas', CAT[0], 'dot'), ('mentoria', CAT[1], 'dot'), ('eventos', CAT[2], 'dot')]))))

# line
types_body += sec("line", "line chart", "04",
    type_block("line",
        ["evolução ao longo do tempo", "comparar tendências entre 2-5 séries", "dados contínuos com muitos pontos"],
        ["categorias discretas (não-temporais) — usa bar", "1 ponto único — usa big number", "mais de 5 séries — escolhe 2-3 destaque + faded rest"],
        chart_card("alunos matriculados · evolução 2026", "crescimento mensal",
                   line_chart([[120, 180, 220, 280, 320, 380, 450, 510, 580]],
                              ['jan','fev','mar','abr','mai','jun','jul','ago','set'], label='line'),
                   "demonstração",
                   legend([('alunos', CAT[0], 'line')]))))

# multi-line
types_body += sec("line-multi", "line chart (multi-série)", "05",
    type_block("multi-line",
        ["comparar evolução de 2-5 grupos paralelos", "ver convergência ou divergência ao longo do tempo"],
        ["mais de 5 séries — usa small multiples (grid de mini-charts)"],
        chart_card("alunos por região · 2026", "crescimento comparativo",
                   line_chart([[80, 120, 150, 180, 220, 260, 310, 350, 400],
                               [50, 70, 90, 120, 160, 200, 240, 290, 340],
                               [30, 50, 70, 90, 120, 150, 180, 220, 250]],
                              ['jan','fev','mar','abr','mai','jun','jul','ago','set'], label='multi-line'),
                   "demonstração",
                   legend([('sudeste', CAT[0], 'line'), ('nordeste', CAT[1], 'line'), ('sul', CAT[2], 'line')]))))

# area
types_body += sec("area", "area chart", "06",
    type_block("area",
        ["mostrar volume/magnitude ao longo do tempo", "1 série apenas (mais que isso usa stacked area)"],
        ["várias séries não-stacked — área ofusca o que tá embaixo"],
        chart_card("oficinas realizadas · 2026", "acumulado mensal",
                   area_chart([15, 22, 28, 35, 42, 50, 60, 68, 75],
                              ['jan','fev','mar','abr','mai','jun','jul','ago','set'], label='area'),
                   "demonstração")))

# pie
types_body += sec("pie", "pie / donut", "07",
    type_block("pie",
        ["composição (parte do todo)", "máximo 5 fatias", "donut quando quer destacar uma métrica no centro"],
        ["6+ fatias — usa bar ou treemap", "valores muito próximos (difícil comparar ângulos)", "tendência temporal"],
        '<div class="row" style="gap: var(--spacing-06)">'
        + chart_card("composição de programa", "5 fatias",
                     pie_chart([45, 25, 15, 10, 5], ['hackerclubes','inclusão','minas','mão massa','perifa'], w=220, h=220, label='pie'),
                     "demonstração",
                     legend([(l, CAT[i], 'dot') for i, l in enumerate(['hackerclubes','inclusão','minas','mão massa','perifa'])]))
        + chart_card("donut com KPI central", "65% — engajamento",
                     pie_chart([65, 35], ['ativo', 'inativo'], donut=True, w=220, h=220, label='donut'),
                     "demonstração")
        + '</div>'))

# scatter
types_body += sec("scatter", "scatter plot", "08",
    type_block("scatter",
        ["correlação entre 2 variáveis numéricas", "identificar clusters ou outliers", "tamanho do ponto pode codificar 3ª variável (bubble)"],
        ["dados categóricos","menos de 15-20 pontos — vira anedótico"],
        chart_card("horas de oficina × alunos formados", "correlação",
                   scatter_chart([(20,40),(35,55),(15,25),(50,75),(40,60),(28,42),(45,65),(60,85),
                                  (25,38),(38,58),(48,72),(55,80),(30,45),(42,62),(52,75)],
                                 label='scatter'),
                   "demonstração")))

# histogram
types_body += sec("histogram", "histogram", "09",
    type_block("histogram",
        ["distribuição de uma variável contínua","ver concentração e cauda"],
        ["dados categóricos — usa bar","poucos valores — fica trivial"],
        chart_card("distribuição de idades · alunos", "frequência por faixa etária",
                   bar_chart([12, 35, 60, 85, 72, 40, 18, 8], ['12-14','15-17','18-20','21-25','26-30','31-40','41-50','50+'], label='histogram'),
                   "demonstração")))

# heatmap
types_body += sec("heatmap", "heatmap", "10",
    type_block("heatmap",
        ["densidade de valores em 2 dimensões","ver padrões em matrizes (ex: atividade por hora × dia)","calendar heatmap"],
        ["categorias sem ordem natural","poucas células — usa tabela"],
        chart_card("atividade no portal · hora × dia da semana", "intensidade de acessos",
                   heatmap(['seg','ter','qua','qui','sex','sáb','dom'],
                           ['00','03','06','09','12','15','18','21'],
                           [[0.1,0.05,0.1,0.4,0.6,0.7,0.8,0.5],
                            [0.1,0.05,0.1,0.5,0.7,0.8,0.9,0.6],
                            [0.1,0.05,0.1,0.5,0.7,0.8,0.9,0.6],
                            [0.1,0.05,0.1,0.5,0.7,0.8,0.9,0.6],
                            [0.15,0.1,0.15,0.45,0.6,0.65,0.7,0.4],
                            [0.3,0.2,0.15,0.25,0.4,0.5,0.6,0.45],
                            [0.4,0.3,0.2,0.3,0.45,0.55,0.65,0.5]], label='heatmap'),
                   "demonstração")))

# treemap-stub (drawn manually)
types_body += sec("treemap", "treemap", "11",
    type_block("treemap",
        ["hierarquia + proporção","quando quer mostrar muitos níveis de uma estrutura","alocação de recursos por categoria"],
        ["dados não-hierárquicos — usa bar","poucas categorias — usa pie"],
        chart_card("orçamento por programa", "alocação 2026",
                   f'''<svg class="chart-svg" viewBox="0 0 520 240" role="img" aria-label="treemap">
  <rect x="0" y="0" width="260" height="240" fill="{CAT[0]}" stroke="white" stroke-width="2"/>
  <text x="130" y="125" text-anchor="middle" font-size="13" fill="#3C433C" font-weight="600">hackerclubes</text>
  <text x="130" y="142" text-anchor="middle" font-size="11" fill="#3C433C">45%</text>
  <rect x="260" y="0" width="170" height="140" fill="{CAT[1]}" stroke="white" stroke-width="2"/>
  <text x="345" y="65" text-anchor="middle" font-size="12" fill="#FFF" font-weight="600">inclusão tech</text>
  <text x="345" y="82" text-anchor="middle" font-size="10" fill="#FFF">25%</text>
  <rect x="430" y="0" width="90" height="140" fill="{CAT[2]}" stroke="white" stroke-width="2"/>
  <text x="475" y="65" text-anchor="middle" font-size="11" fill="#3C433C">minas</text>
  <text x="475" y="82" text-anchor="middle" font-size="10" fill="#3C433C">15%</text>
  <rect x="260" y="140" width="170" height="100" fill="{CAT[3]}" stroke="white" stroke-width="2"/>
  <text x="345" y="185" text-anchor="middle" font-size="11" fill="#3C433C">mão na massa</text>
  <text x="345" y="200" text-anchor="middle" font-size="10" fill="#3C433C">10%</text>
  <rect x="430" y="140" width="90" height="100" fill="{CAT[4]}" stroke="white" stroke-width="2"/>
  <text x="475" y="185" text-anchor="middle" font-size="10" fill="#3C433C">perifa</text>
  <text x="475" y="200" text-anchor="middle" font-size="10" fill="#3C433C">5%</text>
</svg>''',
                   "demonstração")))

# KPI big number
types_body += sec("kpi", "big number / KPI tile", "12",
    type_block("KPI tile",
        ["destacar uma métrica única","comparação rápida (delta vs período anterior)","topo de dashboard"],
        ["se precisar de contexto histórico — adiciona sparkline","métricas não-quantitativas"],
        '<div class="grid-3">'
        + '<div class="chart-kpi"><div class="label">alunos · mai/2026</div><div class="value">2.847</div><div class="delta up">↑ 18% vs abr</div></div>'
        + '<div class="chart-kpi"><div class="label">hackerclubes ativos</div><div class="value">145</div><div class="delta up">↑ 6 novos</div></div>'
        + '<div class="chart-kpi"><div class="label">churn mensal</div><div class="value">3,2%</div><div class="delta down">↓ -0,5pp</div></div>'
        + '</div>'))

# sparkline
types_body += sec("sparkline", "sparkline", "13",
    type_block("sparkline",
        ["tendência inline em pouco espaço","ao lado de KPI ou em linha de tabela","mostrar shape sem precisão"],
        ["se precisar de valores exatos — usa line tradicional"],
        '<div class="chart-kpi"><div class="label">acessos · últimos 30 dias</div><div class="value" style="display:flex;align-items:center;gap:var(--spacing-04)">14.523 <svg viewBox="0 0 120 32" width="120" height="32"><polyline fill="none" stroke="var(--ch-code)" stroke-width="2" points="2,28 12,24 22,26 32,20 42,22 52,18 62,20 72,14 82,16 92,10 102,12 112,8"/></svg></div><div class="delta up">↑ 22%</div></div>'))

write("pages/dataviz/types.html", page(
    "dv-types", "Chart types",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">data visualization</a><span class="sep">/</span>chart types',
    "13 tipos de chart cobrem 95% dos casos. Cada tipo tem uma pergunta canônica que responde — escolha errada de tipo gera mais confusão que clareza.",
    types_body,
    tags=[{"cls":"tag--code","label":"13 tipos"}],
    toc=[
        {"id":"bar","label":"Bar (simples)"},
        {"id":"bar-grouped","label":"Bar (agrupado)"},
        {"id":"bar-stacked","label":"Bar (empilhado)"},
        {"id":"line","label":"Line"},
        {"id":"line-multi","label":"Line (multi)"},
        {"id":"area","label":"Area"},
        {"id":"pie","label":"Pie / Donut"},
        {"id":"scatter","label":"Scatter"},
        {"id":"histogram","label":"Histogram"},
        {"id":"heatmap","label":"Heatmap"},
        {"id":"treemap","label":"Treemap"},
        {"id":"kpi","label":"Big number / KPI"},
        {"id":"sparkline","label":"Sparkline"},
    ],
))

# ============================================================================
# PAGE 4 · COLORS
# ============================================================================
def palette_swatches(items, on_dark=False):
    cls = ' on-dark' if on_dark else ''
    cells = ''.join(f'<div class="swatch{cls}" style="background:{c};">{n}</div>' for c, n in items)
    return f'<div class="chart-palette-row">{cells}</div>'

write("pages/dataviz/colors.html", page(
    "dv-colors", "Color palettes",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">data visualization</a><span class="sep">/</span>color palettes',
    "4 paletas dedicadas a dataviz: categórica (séries sem ordem), sequencial (intensidade ordenada), divergente (extremos + neutro), status (estados de sistema). Tokens prefixados <code class='code-inline'>--dv-*</code>.",
    "".join([
        sec("categorical", "categórica · 8 cores", "01",
            '<p class="t-body-02 t-secondary mb-05 prose">Pra séries qualitativas (categorias sem ordem natural). Cores ordenadas por contraste mútuo — use sempre da 1 pra cima.</p>'
            + palette_swatches([
                ('#32FA96','01'),('#AA78E6','02'),('#D79B2E','03'),('#B3D9FE','04'),
                ('#FF9ECF','05'),('#3C433C','06'),('#5CFFAA','07'),('#D3BAF5','08'),
            ])
            + table(['token','hex','nome brand','quando usar'], [
                ['--dv-cat-1','#32FA96','Code','série principal · destaque'],
                ['--dv-cat-2','#AA78E6','Purple','série secundária'],
                ['--dv-cat-3','#D79B2E','Script','terceira'],
                ['--dv-cat-4','#B3D9FE','Sec Blue','quarta'],
                ['--dv-cat-5','#FF9ECF','Sec Pink','quinta'],
                ['--dv-cat-6','#3C433C','Dos','sexta (escura — usa em fundo claro)'],
                ['--dv-cat-7','#5CFFAA','Code Light','sétima'],
                ['--dv-cat-8','#D3BAF5','Purple Light','oitava'],
            ])
            + sec("", "", "", chart_card("aplicação — multi-line categórica",
                "as 4 primeiras cores em uso real",
                line_chart([
                    [120, 180, 220, 280, 320, 380, 450, 510],
                    [80, 110, 140, 175, 210, 245, 290, 340],
                    [40, 60, 85, 105, 130, 155, 185, 215],
                    [20, 30, 45, 60, 80, 105, 130, 160],
                ], ['jan','fev','mar','abr','mai','jun','jul','ago'], label='multi-line 4 séries'),
                "demonstração",
                legend([('hackerclubes',CAT[0],'line'),('inclusão',CAT[1],'line'),('minas',CAT[2],'line'),('mão massa',CAT[3],'line')])))),
        sec("sequential", "sequencial · 7 steps · verde", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">Pra dados ordenados (intensidade, frequência). Gradiente do mais claro ao mais escuro, sem cor neutra no meio.</p>'
            + palette_swatches([
                ('#E1FFDE','01'),('#C2F5DA','02'),('#9BE5BF','03'),('#5CFFAA','04'),
                ('#32FA96','05'),('#24C775','06'),('#0F5A33','07'),
            ])
            + '<p class="t-helper mt-04">Tokens <code class="code-inline">--dv-seq-1</code> a <code class="code-inline">--dv-seq-7</code></p>'),
        sec("divergent", "divergente · 7 steps · vermelho→neutro→verde", "03",
            '<p class="t-body-02 t-secondary mb-05 prose">Pra dados com ponto neutro e dois extremos opostos (ex: variação positiva/negativa, satisfação 1-5).</p>'
            + palette_swatches([
                ('#DA1E28','01'),('#FF8389','02'),('#FFCCE3','03'),('#F0F5F0','04'),
                ('#C2F5DA','05'),('#5CFFAA','06'),('#24C775','07'),
            ])
            + '<p class="t-helper mt-04">Tokens <code class="code-inline">--dv-div-1</code> a <code class="code-inline">--dv-div-7</code> · meio (04) é o neutro</p>'),
        sec("status", "status · 4 cores", "04",
            '<p class="t-body-02 t-secondary mb-05 prose">Estados de sistema. Use sempre acompanhados de ícone ou texto.</p>'
            + '<div class="row" style="gap: 1px;">'
            + '<div style="flex:1;height:64px;background:#24C775;display:flex;align-items:center;justify-content:center;color:#FFF;font:var(--code-02)">success</div>'
            + '<div style="flex:1;height:64px;background:#D79B2E;display:flex;align-items:center;justify-content:center;color:#FFF;font:var(--code-02)">warning</div>'
            + '<div style="flex:1;height:64px;background:#DA1E28;display:flex;align-items:center;justify-content:center;color:#FFF;font:var(--code-02)">error</div>'
            + '<div style="flex:1;height:64px;background:#0F62FE;display:flex;align-items:center;justify-content:center;color:#FFF;font:var(--code-02)">info</div>'
            + '</div>'
            + '<p class="t-helper mt-04">Tokens <code class="code-inline">--support-success / warning / error / info</code></p>'),
        sec("rules", "regras", "05",
            do_dont(
                ["Categórica em ordem (1→8) — não pula","Sequencial pra valores ordenados, não-categóricos","Divergente quando há ponto neutro claro","Sempre cor + label/legenda"],
                ["Cor sozinha pra transmitir significado","Misturar categórica com sequencial no mesmo chart","Mais de 8 séries (use small multiples)","Cor crua (#XXXXXX) — usa o token"],
            )),
        sec("code", "código", "06",
            code('<span class="c">/* uso direto via token */</span>\n<span class="k">.bar-1</span> { fill: <span class="k">var</span>(--dv-cat-1); }\n<span class="k">.bar-2</span> { fill: <span class="k">var</span>(--dv-cat-2); }\n\n<span class="c">/* heatmap sequencial */</span>\n<span class="k">.cell-low</span>  { background: <span class="k">var</span>(--dv-seq-1); }\n<span class="k">.cell-mid</span>  { background: <span class="k">var</span>(--dv-seq-4); }\n<span class="k">.cell-high</span> { background: <span class="k">var</span>(--dv-seq-7); }')),
    ]),
    toc=[{"id":"categorical","label":"Categórica"},{"id":"sequential","label":"Sequencial"},{"id":"divergent","label":"Divergente"},{"id":"status","label":"Status"},{"id":"rules","label":"Regras"},{"id":"code","label":"Código"}],
))

# ============================================================================
# PAGE 5 · LABELS & AXES
# ============================================================================
write("pages/dataviz/labels.html", page(
    "dv-labels", "Labels & axes",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">data visualization</a><span class="sep">/</span>labels & axes',
    "Annotations, eixos, formatting numérico, direct labels vs legenda. As decisões textuais que separam um chart claro de um confuso.",
    "".join([
        sec("direct-vs-legend", "direct labels vs legenda", "01",
            '<p class="t-body-02 t-secondary mb-05 prose">Quando há poucas séries (≤3) e ponta da linha não colide, direct labels eliminam ida-e-volta do olho.</p>'
            + '<div class="grid-2">'
            + chart_card("✓ direct labels", "leitura direta sem legenda",
                line_chart([[120, 180, 220, 280, 320, 380, 450]],
                           ['jan','fev','mar','abr','mai','jun','jul'], label='direct'),
                "", "<p class='t-helper'>Adicione &lt;text&gt; no fim de cada linha</p>")
            + chart_card("✓ legenda", "3+ séries · cores próximas",
                line_chart([[120, 180, 220, 280, 320, 380, 450],
                            [80, 110, 140, 175, 210, 245, 290],
                            [40, 60, 85, 105, 130, 155, 185]],
                           ['jan','fev','mar','abr','mai','jun','jul'], label='legend'),
                "",
                legend([('a',CAT[0],'line'),('b',CAT[1],'line'),('c',CAT[2],'line')]))
            + '</div>'),
        sec("axes", "eixos", "02",
            checklist([
                "Eixo Y começa em zero pra bar e area (truncar distorce)",
                "Eixo Y pode truncar em line se variação for sutil — sempre indique",
                "Eixo X tempo: da esquerda pra direita, mais antigo → mais recente",
                "Eixo X categorias: ordenadas por valor (decrescente)",
                "Título do eixo só quando ambíguo (omita 'tempo' óbvio em time series)",
                "Unidades sempre presentes (R$ mil, %, count)",
            ])),
        sec("numbers", "formatting numérico", "03",
            table(['contexto','formato','exemplo'], [
                ['valores grandes','separador de milhar','1.547 · 23.487 · 1.250.000'],
                ['decimais','vírgula','3,2% · 1,5x · R$ 4,99'],
                ['abreviações','K/M/B em axes apertados','1,5K · 230M'],
                ['moeda','R$ + número','R$ 1.250,00'],
                ['porcentagem','sufixo %','18,5%'],
                ['data','dd/mm ou dd/mm/aaaa','15/05 · 15/05/2026'],
                ['delta','+ ou ↑ / - ou ↓','+18% · ↓3,2pp · -R$ 50'],
            ])),
        sec("annotations", "annotations", "04",
            '<p class="t-body-02 t-secondary mb-05 prose">Quando há marco crítico (recorde, meta atingida, anomalia), anote diretamente no chart.</p>'
            + chart_card("com annotation", "destaca o marco",
                f'''<svg class="chart-svg" viewBox="0 0 520 240" role="img" aria-label="line com annotation">
  <line class="grid-line" x1="40" y1="50" x2="504" y2="50"/>
  <line class="grid-line" x1="40" y1="110" x2="504" y2="110"/>
  <line class="grid-line" x1="40" y1="170" x2="504" y2="170"/>
  <line class="axis-line" x1="40" y1="200" x2="504" y2="200"/>
  <text x="34" y="53" text-anchor="end">600</text>
  <text x="34" y="113" text-anchor="end">400</text>
  <text x="34" y="173" text-anchor="end">200</text>
  <line x1="40" y1="100" x2="504" y2="100" stroke="#DA1E28" stroke-dasharray="4 2" stroke-width="1.5"/>
  <text x="500" y="93" text-anchor="end" fill="#DA1E28" font-size="9" font-weight="600">META · 400</text>
  <polyline class="line" stroke="{CAT[0]}" points="60,180 124,160 188,140 252,110 316,80 380,70 444,55"/>
  <circle class="point" cx="316" cy="80" r="5" fill="{CAT[0]}"/>
  <text x="320" y="74" font-size="9" fill="#3C433C" font-weight="600">+ meta batida</text>
</svg>''',
                "demonstração")),
        sec("rules", "regras", "05",
            do_dont(
                ["Annotations apontam direto pro ponto (linha de chamada ≤8px)","Texto curto (3-5 palavras)","Cor de support quando crítico (--support-error pra meta perdida)","Use 1 annotation por chart"],
                ["Annotations longas (texto fica acima)","Múltiplas linhas de referência (vira teia)","Cor que conflita com a paleta categórica"],
            )),
    ]),
    toc=[{"id":"direct-vs-legend","label":"Direct labels vs legenda"},{"id":"axes","label":"Eixos"},{"id":"numbers","label":"Formatting numérico"},{"id":"annotations","label":"Annotations"},{"id":"rules","label":"Regras"}],
))

# ============================================================================
# PAGE 6 · INTERACTION
# ============================================================================
write("pages/dataviz/interaction.html", page(
    "dv-interaction", "Interaction",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">data visualization</a><span class="sep">/</span>interaction',
    "Padrões de interação em charts: hover/tooltip, legend toggle, drill-down, brush selection, time range. Toda interação deve ter equivalente acessível via teclado.",
    "".join([
        sec("hover", "hover & tooltip", "01",
            '<p class="t-body-02 t-secondary mb-05 prose">Tooltip aparece on-hover (desktop) ou tap (mobile). Conteúdo: label + valor exato + comparação opcional. Passa o mouse no chart abaixo.</p>'
            + chart_card("demo · hover sobre barras", "tooltip aparece on-hover",
                bar_chart([45, 32, 60, 38, 72, 55, 80], ['seg','ter','qua','qui','sex','sáb','dom'], label='hover'),
                "demonstração interativa")),
        sec("legend-toggle", "legend toggle", "02",
            '<p class="t-body-02 t-secondary prose">Clique na legenda esconde/mostra a série. Visual: opacidade 0.3 quando "off". Implementação JS opcional — em SVG nativo, usar <code class="code-inline">display: none</code> ou <code class="code-inline">opacity</code>.</p>'),
        sec("drill-down", "drill-down", "03",
            '<p class="t-body-02 t-secondary prose">Click numa barra/fatia abre detalhamento. Usar quando há hierarquia (mês → semana → dia). Sinalize com cursor pointer + tooltip "clica pra detalhar".</p>'),
        sec("brush", "brush selection (range)", "04",
            '<p class="t-body-02 t-secondary prose">Em line charts longos, brush no eixo X permite zoom em sub-range. Mostra o range selecionado destacado, resto fica fade. Equivalente teclado: input de date range acima.</p>'),
        sec("time-range", "time range selector", "05",
            '<p class="t-body-02 t-secondary mb-05 prose">Quando dashboard tem múltiplos charts com mesmo eixo temporal, controle único no topo.</p>'
            + demo('<div class="row"><button class="btn btn--ghost btn--sm">7d</button><button class="btn btn--ghost btn--sm">30d</button><button class="btn btn--primary btn--sm">90d</button><button class="btn btn--ghost btn--sm">1a</button><button class="btn btn--ghost btn--sm">tudo</button><span class="t-helper">· customizado: <input class="input" type="date" style="width:140px;display:inline-block;height:32px"></span></div>')),
        sec("filter", "filter chips", "06",
            demo('<div class="row"><span class="t-label-01 text-helper">filtros ativos:</span><span class="tag tag--code">programa: hackerclubes ×</span><span class="tag tag--purple">região: sudeste ×</span><span class="tag tag--outline">+ adicionar</span></div>')),
        sec("empty", "empty state em chart", "07",
            '<p class="t-body-02 t-secondary mb-05 prose">Quando não há dados pra mostrar (filtro vazio, primeira vez, erro), substitua o chart por um estado vazio com call-to-action.</p>'
            + demo('<div style="background:var(--layer-01);border:1px solid var(--border-subtle-00);padding:var(--spacing-09);text-align:center"><div style="width:48px;height:48px;margin:0 auto var(--spacing-04);background:var(--layer-02);display:flex;align-items:center;justify-content:center;font:var(--code-02);color:var(--text-helper)">∅</div><h4 class="t-h03 mb-03">sem dados pra esse período</h4><p class="t-secondary mb-05">tenta um intervalo maior ou ajusta os filtros.</p><button class="btn btn--ghost btn--sm">resetar filtros</button></div>')),
        sec("a11y", "alternativas via teclado", "08",
            checklist([
                "Hover → equivalente: focus via Tab no ponto/barra",
                "Drill-down → Enter no elemento focado",
                "Brush → input de data range (input type='date')",
                "Legend toggle → checkbox associado",
                "Time range → button group nativo",
            ])),
    ]),
    toc=[{"id":"hover","label":"Hover & tooltip"},{"id":"legend-toggle","label":"Legend toggle"},{"id":"drill-down","label":"Drill-down"},{"id":"brush","label":"Brush selection"},{"id":"time-range","label":"Time range"},{"id":"filter","label":"Filter chips"},{"id":"empty","label":"Empty state"},{"id":"a11y","label":"Alternativas via teclado"}],
))

# ============================================================================
# PAGE 7 · ACCESSIBILITY (chart-specific a11y)
# ============================================================================
write("pages/dataviz/accessibility.html", page(
    "dv-accessibility", "Chart accessibility",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">data visualization</a><span class="sep">/</span>accessibility',
    "Charts precisam funcionar pra quem não enxerga cor, não vê tela, ou navega via teclado. Padrões WCAG 2.1 AA aplicados a dataviz.",
    tags=[{"cls":"tag--blue","label":"wcag aa"}],
    sections="".join([
        sec("alt-text", "texto alternativo", "01 · 1.1.1",
            '<p class="t-body-02 t-secondary mb-05 prose">Todo chart é uma <code class="code-inline">&lt;svg role="img" aria-label="descrição"&gt;</code>. O aria-label conta a história, não a forma.</p>'
            + do_dont(
                ['"vendas de jan a dez · alta consistente · setembro recorde com 580"','"alunos por região · sudeste lidera com 320 · norte menor 18"','Resumo informativo (não enumera valores)'],
                ['"gráfico de barras com 9 colunas"','"chart"','"figura ilustrativa"','Enumerar todos os valores (vira tabela falada)'],
            )),
        sec("table-fallback", "tabular fallback", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">Pra leitores de tela e usuários que preferem dados crus, ofereça versão tabela. Pode ficar oculta visualmente (sr-only) ou em &lt;details&gt;.</p>'
            + demo('<details><summary class="t-label-02" style="cursor:pointer">▸ ver dados em tabela</summary><table class="data-table data-table--compact mt-04"><thead><tr><th>mês</th><th>vendas</th></tr></thead><tbody><tr><td>jan</td><td>45</td></tr><tr><td>fev</td><td>32</td></tr><tr><td>mar</td><td>60</td></tr><tr><td>abr</td><td>38</td></tr></tbody></table></details>')),
        sec("color-blind", "color-blind safe", "03 · 1.4.1",
            '<p class="t-body-02 t-secondary mb-05 prose">Nossa paleta categórica foi testada em deuteranopia (verde-vermelho, ~5% da população masculina) e protanopia. Mesmo assim, sempre acompanhe cor com pattern, ícone ou label.</p>'
            + table(['daltonismo','prevalência','o que vira'], [
                ['deuteranopia','5% (homens)','verde/vermelho indistinguíveis'],
                ['protanopia','1%','vermelho parece marrom'],
                ['tritanopia','<1%','azul/amarelo confusos'],
                ['monocromacia','muito raro','tudo em tons de cinza'],
            ])),
        sec("patterns", "patterns como alternativa", "04",
            '<p class="t-body-02 t-secondary mb-05 prose">Em bar/area stacked, use hachura (pattern fill SVG) pra distinguir além da cor.</p>'
            + chart_card("bar com hachura", "hachura distingue além da cor",
                f'''<svg class="chart-svg" viewBox="0 0 520 240" role="img" aria-label="bar com hachura">
  <defs>
    <pattern id="hatch1" patternUnits="userSpaceOnUse" width="6" height="6"><line x1="0" y1="0" x2="0" y2="6" stroke="white" stroke-width="1.5"/></pattern>
    <pattern id="hatch2" patternUnits="userSpaceOnUse" width="6" height="6"><line x1="0" y1="0" x2="6" y2="6" stroke="white" stroke-width="1.5"/></pattern>
  </defs>
  <line class="axis-line" x1="40" y1="200" x2="504" y2="200"/>
  ''' + ''.join(
    f'<g><rect x="{60+i*120}" y="{200-h1-h2}" width="80" height="{h2}" fill="{CAT[1]}"/>'
    f'<rect x="{60+i*120}" y="{200-h1-h2}" width="80" height="{h2}" fill="url(#hatch2)"/>'
    f'<rect x="{60+i*120}" y="{200-h1}" width="80" height="{h1}" fill="{CAT[0]}"/>'
    f'<rect x="{60+i*120}" y="{200-h1}" width="80" height="{h1}" fill="url(#hatch1)" opacity="0.3"/>'
    f'<text x="{100+i*120}" y="220" text-anchor="middle">{lbl}</text></g>'
    for i, (lbl, h1, h2) in enumerate([('q1',60,40),('q2',80,55),('q3',95,70),('q4',110,85)])
  ) + '</svg>',
                "")),
        sec("contrast", "contraste", "05 · 1.4.3 / 1.4.11",
            checklist([
                "Texto em chart: 4.5:1 contra fundo",
                "Elementos gráficos (bars, lines, dots): 3:1 contra fundo",
                "Axis labels: legíveis em ambos os temas",
                "Tooltip: contraste alto sempre (--dv-tooltip-bg vs fg)",
            ])),
        sec("keyboard", "keyboard navigation", "06 · 2.1.1",
            '<p class="t-body-02 t-secondary prose">Quando chart é interativo: cada ponto/barra é focável via Tab. Setas navegam entre pontos da mesma série. Enter ativa drill-down. Esc sai do modo "explorando chart".</p>'),
        sec("motion", "motion", "07 · 2.3.3",
            '<p class="t-body-02 t-secondary prose">Animações de entrada (barras crescendo, linhas desenhando) ≤ 700ms. Respeitar <code class="code-inline">prefers-reduced-motion</code> — desativa animação, mostra estado final.</p>'),
        sec("checklist", "checklist por chart", "08",
            checklist([
                'role="img" + aria-label descritivo no SVG',
                "Tabular fallback disponível (visible ou sr-only)",
                "Cor não é único portador de significado",
                "Contraste de texto e elementos verificado",
                "Funciona em high-contrast mode (testar via barra de acessibilidade)",
                "Animação respeita prefers-reduced-motion",
                "Quando interativo: 100% via teclado",
                "Quando dinâmico (atualização real-time): aria-live em região fora do svg",
            ])),
    ]),
    toc=[{"id":"alt-text","label":"Texto alternativo"},{"id":"table-fallback","label":"Tabular fallback"},{"id":"color-blind","label":"Color-blind safe"},{"id":"patterns","label":"Patterns"},{"id":"contrast","label":"Contraste"},{"id":"keyboard","label":"Keyboard"},{"id":"motion","label":"Motion"},{"id":"checklist","label":"Checklist"}],
))

# ============================================================================
# PAGE 8 · EXAMPLES (dashboards compostos)
# ============================================================================
write("pages/dataviz/examples.html", page(
    "dv-examples", "Examples",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">data visualization</a><span class="sep">/</span>examples',
    "Composições reais de dashboards Casa Hacker. Como vários charts trabalham juntos pra contar uma história única.",
    "".join([
        sec("dashboard-1", "dashboard · impacto hackerclubes", "01",
            '<p class="t-body-02 t-secondary mb-05 prose">Composição típica de relatório mensal de programa. Layout 3 KPIs + 2 charts.</p>'
            + '<div class="grid-3 mb-05">'
            + '<div class="chart-kpi"><div class="label">alunos · mai/2026</div><div class="value">2.847</div><div class="delta up">↑ 18% vs abr</div></div>'
            + '<div class="chart-kpi"><div class="label">clubes ativos</div><div class="value">145</div><div class="delta up">↑ 6 novos</div></div>'
            + '<div class="chart-kpi"><div class="label">churn mensal</div><div class="value">3,2%</div><div class="delta down">↓ -0,5pp</div></div>'
            + '</div>'
            + '<div class="chart-grid">'
            + chart_card("evolução de alunos · 2026", "crescimento mensal",
                line_chart([[120, 180, 220, 280, 320, 380, 450, 510, 580]],
                           ['jan','fev','mar','abr','mai','jun','jul','ago','set'], label='alunos'),
                "demonstração",
                legend([('alunos', CAT[0], 'line')]))
            + chart_card("clubes por região", "distribuição geográfica",
                bar_chart([42, 28, 35, 18, 22], ['SE','NE','S','N','CO'], label='regiao'),
                "demonstração")
            + '</div>'),
        sec("dashboard-2", "relatório · perifa impacto", "02",
            '<p class="t-body-02 t-secondary mb-05 prose">Foco em métricas de impacto social. Comparação ano sobre ano + composição.</p>'
            + '<div class="chart-grid">'
            + chart_card("oficinas realizadas · 2024-2026", "evolução acumulada",
                area_chart([15, 22, 28, 35, 42, 50, 60, 68, 75],
                           ['jan','fev','mar','abr','mai','jun','jul','ago','set'], color=CAT[1], label='oficinas'),
                "demonstração")
            + chart_card("composição de programa", "alocação 2026",
                pie_chart([45, 25, 15, 10, 5], ['hack','incl','minas','massa','perifa'],
                          donut=True, w=240, h=240, label='programa'),
                "demonstração",
                legend([(l, CAT[i], 'dot') for i, l in enumerate(['hackerclubes','inclusão','minas','mão massa','perifa'])]))
            + '</div>'),
        sec("dashboard-3", "atividade · portal hacker clubes", "03",
            '<p class="t-body-02 t-secondary mb-05 prose">Heatmap de atividade horária + KPIs com sparklines.</p>'
            + '<div class="grid-3 mb-05">'
            + '<div class="chart-kpi"><div class="label">acessos · últimos 30d</div><div class="value" style="display:flex;align-items:center;gap:var(--spacing-03);flex-wrap:wrap">14.523<svg viewBox="0 0 120 32" width="100" height="28"><polyline fill="none" stroke="var(--ch-code)" stroke-width="2" points="2,28 12,24 22,26 32,20 42,22 52,18 62,20 72,14 82,16 92,10 102,12 112,8"/></svg></div><div class="delta up">↑ 22%</div></div>'
            + '<div class="chart-kpi"><div class="label">sessões médias</div><div class="value" style="display:flex;align-items:center;gap:var(--spacing-03);flex-wrap:wrap">8min 32s<svg viewBox="0 0 120 32" width="100" height="28"><polyline fill="none" stroke="var(--ch-purple)" stroke-width="2" points="2,16 12,18 22,14 32,12 42,16 52,10 62,12 72,8 82,10 92,6 102,8 112,4"/></svg></div><div class="delta up">↑ 12%</div></div>'
            + '<div class="chart-kpi"><div class="label">conversão de cadastro</div><div class="value">38,5%</div><div class="delta down">↓ -1,2pp</div></div>'
            + '</div>'
            + chart_card("atividade · hora × dia da semana", "intensidade de acessos",
                heatmap(['seg','ter','qua','qui','sex','sáb','dom'],
                        ['00','03','06','09','12','15','18','21'],
                        [[0.1,0.05,0.1,0.4,0.6,0.7,0.8,0.5],
                         [0.1,0.05,0.1,0.5,0.7,0.8,0.9,0.6],
                         [0.1,0.05,0.1,0.5,0.7,0.8,0.9,0.6],
                         [0.1,0.05,0.1,0.5,0.7,0.8,0.9,0.6],
                         [0.15,0.1,0.15,0.45,0.6,0.65,0.7,0.4],
                         [0.3,0.2,0.15,0.25,0.4,0.5,0.6,0.45],
                         [0.4,0.3,0.2,0.3,0.45,0.55,0.65,0.5]], label='heatmap atividade'),
                "demonstração · 30d acumulados")),
        sec("layout-tips", "tips de layout", "04",
            checklist([
                "KPIs sempre no topo (info crítica primeiro)",
                "Charts complementares lado-a-lado (2-coluna)",
                "Heatmap/treemap ocupando largura total quando denso",
                "Spacing entre charts: spacing-05 (16px)",
                "Em mobile, charts viram 1-coluna (já configurado em .chart-grid)",
                "Use mesma paleta categórica em todo o dashboard pra consistência",
                "Sincronize cores entre charts (hackerclubes = sempre cat-1)",
            ])),
    ]),
    toc=[{"id":"dashboard-1","label":"Impacto hackerclubes"},{"id":"dashboard-2","label":"Perifa Impacto"},{"id":"dashboard-3","label":"Portal hacker clubes"},{"id":"layout-tips","label":"Tips de layout"}],
))

print('done · all 8 dataviz pages')


