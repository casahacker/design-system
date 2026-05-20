"""Hackerclubes · página dedicada (flagship program).

Refaz pages/submarcas/hackerclubes.html com:
- Identidade aprofundada (tom de voz, mascote, taglines)
- 8 slide deck templates (capa, divider, content, quote, chart, closing)
- 12+ posts redes sociais (Instagram square, Stories, LinkedIn)
- Material educacional (apostila, diploma, atividade, crachá)
- Aplicações escolares (uniforme, pin, caderno, adesivo)
- Comunicação institucional (apresentação, newsletter, email)
- Anatomia avançada (grid logo, variações cor, don'ts)
- Recursos pra implementação

Sobrescreve hackerclubes.html · gen_brand.py mantém todas as outras submarcas.
"""
from common import page, sec, demo, do_dont, code, checklist, table, write

SIG = "#B3D9FE"           # Sec Blue · signature do Hackerclubes
SIG_FG = "#0E3A6B"        # foreground sobre Sec Blue
SIG_DARK = "#0F62FE"      # azul mais saturado pra acentos
DOS = "#3C433C"
CODE = "#32FA96"
CSS = "#F8FCF8"
JAVA = "#91938C"
INSPECT = "#D7DCD7"
PINK = "#FF9ECF"
PURPLE = "#AA78E6"
YELLOW = "#E8D048"


# ---------- reusable SVG components ----------------------------------------
def h_pixel(x=0, y=0, size=10, color=CODE):
    """H pixelado 3×3 grid · cada pixel = `size`."""
    s = size
    cells = [(0,0),(2,0),(0,1),(1,1),(2,1),(0,2),(2,2)]
    rects = ''.join(f'<rect x="{x+c*s}" y="{y+r*s}" width="{s}" height="{s}"/>' for c, r in cells)
    return f'<g fill="{color}">{rects}</g>'

def graf_bg(num, opacity=0.12, mix="multiply"):
    """Imagem de fundo de grafismo com opacity baixa."""
    return (
        f'<image href="../../assets/grafismos/PATTERNS_Artboard {num}.svg" '
        f'x="0" y="0" width="100%" height="100%" opacity="{opacity}" '
        f'style="mix-blend-mode:{mix}"/>'
    )


# ---------- INSTAGRAM POSTS (1080×1080 → viewBox 1080) ---------------------
def post_anuncio_evento():
    """Anúncio de evento · tagline canônica do manifesto."""
    return f'''<svg viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" aria-label="post anúncio de evento">
<rect width="1080" height="1080" fill="{SIG}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 19.svg" x="0" y="0" width="1080" height="1080" opacity="0.18"/>
<text x="80" y="120" font-family="IBM Plex Mono" font-size="36" fill="{DOS}" letter-spacing="3">// HACKERCLUBES</text>
<text x="80" y="380" font-family="Roboto Flex" font-size="120" font-weight="300" fill="{DOS}" letter-spacing="-4">o futuro</text>
<text x="80" y="500" font-family="Roboto Flex" font-size="120" font-weight="300" fill="{DOS}" letter-spacing="-4">não é uma</text>
<text x="80" y="620" font-family="Roboto Flex" font-size="120" font-weight="700" fill="{DOS}" letter-spacing="-4">coisa distante</text>
<rect x="80" y="680" width="180" height="6" fill="{DOS}"/>
<text x="80" y="750" font-family="IBM Plex Mono" font-size="32" fill="{DOS}">// inscrições abertas no seu clube</text>
<g transform="translate(720, 800)">{h_pixel(0, 0, 32, CODE)}</g>
<text x="80" y="990" font-family="IBM Plex Mono" font-size="28" fill="{DOS}">casahacker.org/clubes</text>
</svg>'''


def post_citacao():
    """Post citação · frase canônica do manifesto."""
    return f'''<svg viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="post citação manifesto">
<rect width="1080" height="1080" fill="{DOS}"/>
<g fill="{SIG}" opacity="0.10">
  <rect x="120" y="120" width="40" height="40"/>
  <rect x="200" y="200" width="40" height="40"/>
  <rect x="900" y="800" width="40" height="40"/>
  <rect x="820" y="880" width="40" height="40"/>
</g>
<text x="120" y="280" font-family="Roboto Flex" font-size="280" font-weight="700" fill="{SIG}" opacity="0.4">"</text>
<text x="120" y="500" font-family="Roboto Flex" font-size="56" font-weight="400" fill="{CSS}" letter-spacing="-1">
  <tspan x="120" dy="0">tecnologia como direito</tspan>
  <tspan x="120" dy="72">e como linguagem de poder,</tspan>
  <tspan x="120" dy="72">não como privilégio</tspan>
  <tspan x="120" dy="72">de poucos.</tspan>
</text>
<rect x="120" y="820" width="80" height="3" fill="{CODE}"/>
<text x="120" y="870" font-family="IBM Plex Mono" font-size="24" fill="{CODE}">// manifesto casa hacker</text>
<g transform="translate(120, 950)">{h_pixel(0, 0, 18, SIG)}</g>
<text x="200" y="985" font-family="IBM Plex Mono" font-size="24" fill="{INSPECT}">@hackerclubes</text>
</svg>'''


def post_carrossel_capa():
    """Carrossel slide 1 · capa convidando."""
    return f'''<svg viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="post carrossel capa">
<rect width="1080" height="1080" fill="{CSS}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 22.svg" x="0" y="0" width="1080" height="1080" opacity="0.10"/>
<rect x="0" y="0" width="1080" height="100" fill="{SIG}"/>
<text x="80" y="65" font-family="IBM Plex Mono" font-size="32" fill="{DOS}" letter-spacing="2">// CARROSSEL · 1 de 5</text>
<text x="80" y="380" font-family="Roboto Flex" font-size="120" font-weight="300" fill="{DOS}" letter-spacing="-4">o que é</text>
<text x="80" y="500" font-family="Roboto Flex" font-size="120" font-weight="700" fill="{SIG_DARK}" letter-spacing="-4">hackerclube?</text>
<text x="80" y="610" font-family="IBM Plex Mono" font-size="32" fill="{JAVA}">// pra começar a conversa</text>
<rect x="80" y="680" width="900" height="1" fill="{INSPECT}"/>
<g transform="translate(80, 880)">{h_pixel(0, 0, 24, SIG_DARK)}</g>
<text x="80" y="1020" font-family="IBM Plex Mono" font-size="28" fill="{DOS}">arrasta pro lado →</text>
</svg>'''


def post_carrossel_conteudo():
    """Carrossel slide 2 · conteúdo."""
    return f'''<svg viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="post carrossel conteúdo">
<rect width="1080" height="1080" fill="{CSS}"/>
<rect x="0" y="0" width="1080" height="100" fill="{SIG}"/>
<text x="80" y="65" font-family="IBM Plex Mono" font-size="32" fill="{DOS}" letter-spacing="2">// CARROSSEL · 2 de 5</text>
<text x="80" y="220" font-family="Roboto Flex" font-size="80" font-weight="500" fill="{DOS}" letter-spacing="-2">é um espaço</text>
<text x="80" y="310" font-family="Roboto Flex" font-size="80" font-weight="500" fill="{DOS}" letter-spacing="-2">na escola</text>
<rect x="80" y="370" width="160" height="6" fill="{SIG_DARK}"/>
<g font-family="IBM Plex Mono" font-size="34" fill="{DOS}">
  <text x="80" y="490">→ encontros semanais</text>
  <text x="80" y="555">→ um orientador parceiro</text>
  <text x="80" y="620">→ projetos práticos</text>
  <text x="80" y="685">→ comunidade entre clubes</text>
</g>
<g transform="translate(720, 800)" opacity="0.6">{h_pixel(0, 0, 28, SIG_DARK)}</g>
<text x="80" y="1020" font-family="IBM Plex Mono" font-size="28" fill="{DOS}">arrasta pro lado →</text>
</svg>'''


def post_curiosidade():
    """Post curiosidade · número em destaque."""
    return f'''<svg viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="post curiosidade número">
<rect width="1080" height="1080" fill="{SIG_DARK}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 29.svg" x="0" y="0" width="1080" height="1080" opacity="0.15"/>
<text x="80" y="160" font-family="IBM Plex Mono" font-size="32" fill="{CSS}" opacity="0.8" letter-spacing="2">// VOCÊ SABIA?</text>
<text x="80" y="600" font-family="Roboto Flex" font-size="480" font-weight="700" fill="{CSS}" letter-spacing="-20">87%</text>
<rect x="80" y="650" width="120" height="6" fill="{CODE}"/>
<text x="80" y="780" font-family="Roboto Flex" font-size="56" font-weight="300" fill="{CSS}" letter-spacing="-1">
  <tspan x="80" dy="0">dos clubes em escolas</tspan>
  <tspan x="80" dy="68">públicas continuam</tspan>
  <tspan x="80" dy="68">após o 1º ano</tspan>
</text>
<text x="80" y="1020" font-family="IBM Plex Mono" font-size="24" fill="{INSPECT}">// dados: relatório hackerclubes 2025</text>
</svg>'''


def post_lancamento():
    """Hero post launch · destaque máximo."""
    return f'''<svg viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="post lançamento clube">
<rect width="1080" height="1080" fill="{CODE}"/>
<g fill="{DOS}" opacity="0.08">
  <rect x="40" y="40" width="60" height="60"/>
  <rect x="160" y="40" width="60" height="60"/>
  <rect x="40" y="160" width="60" height="60"/>
  <rect x="160" y="160" width="60" height="60"/>
  <rect x="860" y="860" width="60" height="60"/>
  <rect x="980" y="860" width="60" height="60"/>
  <rect x="860" y="980" width="60" height="60"/>
</g>
<text x="80" y="180" font-family="IBM Plex Mono" font-size="40" fill="{DOS}" letter-spacing="3">// LANÇAMENTO</text>
<text x="80" y="450" font-family="Roboto Flex" font-size="200" font-weight="700" fill="{DOS}" letter-spacing="-8">novo</text>
<text x="80" y="650" font-family="Roboto Flex" font-size="200" font-weight="300" fill="{DOS}" letter-spacing="-8">clube</text>
<text x="80" y="800" font-family="Roboto Flex" font-size="80" font-weight="500" fill="{DOS}" letter-spacing="-2">em sp</text>
<rect x="80" y="850" width="200" height="6" fill="{DOS}"/>
<text x="80" y="930" font-family="IBM Plex Mono" font-size="40" fill="{DOS}">e.e. parque belém</text>
<g transform="translate(820, 920)">{h_pixel(0, 0, 40, DOS)}</g>
</svg>'''


def post_bastidores():
    """Post bastidores · território + autoria."""
    return f'''<svg viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="post bastidores">
<rect width="1080" height="1080" fill="{DOS}"/>
<rect x="80" y="80" width="920" height="540" fill="{INSPECT}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 31.svg" x="80" y="80" width="920" height="540" opacity="0.25"/>
<g transform="translate(440, 280)">{h_pixel(0, 0, 50, SIG_DARK)}</g>
<text x="540" y="490" font-family="IBM Plex Mono" font-size="22" fill="{JAVA}" text-anchor="middle">// foto da turma</text>
<text x="80" y="700" font-family="IBM Plex Mono" font-size="32" fill="{SIG}" letter-spacing="2">// PROJETO DO TERRITÓRIO</text>
<text x="80" y="800" font-family="Roboto Flex" font-size="58" font-weight="400" fill="{CSS}" letter-spacing="-1">
  <tspan x="80" dy="0">solução nasceu na rua,</tspan>
  <tspan x="80" dy="72">voltou pra rua em forma</tspan>
  <tspan x="80" dy="72">de fortalecimento.</tspan>
</text>
<text x="80" y="1040" font-family="IBM Plex Mono" font-size="22" fill="{SIG}">// clube · novembro 2025</text>
</svg>'''


# ---------- INSTAGRAM STORIES (1080×1920) ----------------------------------
def story_save_date():
    """Story save the date · tagline canônica."""
    return f'''<svg viewBox="0 0 540 960" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="story save the date">
<rect width="540" height="960" fill="{SIG}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 33.svg" x="0" y="0" width="540" height="960" opacity="0.20"/>
<text x="40" y="100" font-family="IBM Plex Mono" font-size="20" fill="{DOS}" letter-spacing="2">// ENCONTRO</text>
<text x="40" y="320" font-family="Roboto Flex" font-size="78" font-weight="300" fill="{DOS}" letter-spacing="-2">vamos</text>
<text x="40" y="410" font-family="Roboto Flex" font-size="78" font-weight="300" fill="{DOS}" letter-spacing="-2">programar</text>
<text x="40" y="500" font-family="Roboto Flex" font-size="78" font-weight="700" fill="{SIG_DARK}" letter-spacing="-2">outros</text>
<text x="40" y="590" font-family="Roboto Flex" font-size="78" font-weight="700" fill="{SIG_DARK}" letter-spacing="-2">futuros</text>
<rect x="40" y="630" width="120" height="4" fill="{DOS}"/>
<text x="40" y="700" font-family="IBM Plex Mono" font-size="20" fill="{DOS}">
  <tspan x="40" dy="0">// 15-17 setembro</tspan>
  <tspan x="40" dy="30">// casa hacker · sp</tspan>
</text>
<g transform="translate(40, 800)">{h_pixel(0, 0, 18, DOS)}</g>
<text x="40" y="900" font-family="IBM Plex Mono" font-size="18" fill="{DOS}">arrasta pra cima ↑</text>
</svg>'''


def story_countdown():
    """Story countdown."""
    return f'''<svg viewBox="0 0 540 960" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="story countdown">
<rect width="540" height="960" fill="{DOS}"/>
<g fill="{SIG_DARK}" opacity="0.12">
  <rect x="40" y="40" width="50" height="50"/>
  <rect x="100" y="40" width="50" height="50"/>
  <rect x="450" y="870" width="50" height="50"/>
</g>
<text x="270" y="200" font-family="IBM Plex Mono" font-size="20" fill="{CSS}" text-anchor="middle" letter-spacing="2">// FALTAM</text>
<text x="270" y="500" font-family="Roboto Flex" font-size="280" font-weight="700" fill="{CSS}" text-anchor="middle" letter-spacing="-12">07</text>
<text x="270" y="580" font-family="IBM Plex Mono" font-size="32" fill="{CODE}" text-anchor="middle">DIAS</text>
<rect x="220" y="640" width="100" height="3" fill="{CODE}"/>
<text x="270" y="720" font-family="Roboto Flex" font-size="32" fill="{CSS}" text-anchor="middle">
  <tspan x="270" dy="0">pra novo encontro</tspan>
  <tspan x="270" dy="40">do clube vila prudente</tspan>
</text>
<g transform="translate(240, 850)">{h_pixel(0, 0, 16, CODE)}</g>
</svg>'''


def story_quiz():
    """Story quiz interativo."""
    return f'''<svg viewBox="0 0 540 960" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="story quiz">
<rect width="540" height="960" fill="{SIG_DARK}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 28.svg" x="0" y="0" width="540" height="960" opacity="0.15"/>
<text x="40" y="100" font-family="IBM Plex Mono" font-size="20" fill="{CSS}" letter-spacing="2">// QUIZ</text>
<text x="40" y="280" font-family="Roboto Flex" font-size="56" font-weight="400" fill="{CSS}" letter-spacing="-1">
  <tspan x="40" dy="0">qual linguagem</tspan>
  <tspan x="40" dy="64">aprender primeiro?</tspan>
</text>
<rect x="40" y="430" width="460" height="80" fill="{CSS}" rx="4"/>
<text x="270" y="480" font-family="IBM Plex Mono" font-size="24" fill="{DOS}" text-anchor="middle">A · python</text>
<rect x="40" y="530" width="460" height="80" fill="{CSS}" rx="4" opacity="0.4"/>
<text x="270" y="580" font-family="IBM Plex Mono" font-size="24" fill="{DOS}" text-anchor="middle">B · javascript</text>
<rect x="40" y="630" width="460" height="80" fill="{CSS}" rx="4" opacity="0.4"/>
<text x="270" y="680" font-family="IBM Plex Mono" font-size="24" fill="{DOS}" text-anchor="middle">C · scratch</text>
<text x="40" y="780" font-family="IBM Plex Mono" font-size="18" fill="{CODE}">// vota nos stories</text>
<g transform="translate(40, 850)">{h_pixel(0, 0, 16, CODE)}</g>
</svg>'''


# ---------- LINKEDIN POST (1200×627) ---------------------------------------
def linkedin_institutional():
    """Banner LinkedIn institucional · tagline canônica."""
    return f'''<svg viewBox="0 0 1200 627" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="linkedin banner institucional">
<rect width="1200" height="627" fill="{DOS}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 19.svg" x="0" y="0" width="1200" height="627" opacity="0.10"/>
<g transform="translate(80, 100)">{h_pixel(0, 0, 36, SIG)}</g>
<text x="80" y="260" font-family="Roboto Flex" font-size="52" font-weight="300" fill="{CSS}" letter-spacing="-2">vamos programar</text>
<text x="80" y="330" font-family="Roboto Flex" font-size="52" font-weight="700" fill="{SIG}" letter-spacing="-2">outros futuros</text>
<rect x="80" y="380" width="120" height="4" fill="{CODE}"/>
<text x="80" y="440" font-family="IBM Plex Mono" font-size="22" fill="{INSPECT}">
  <tspan x="80" dy="0">// 142 hackerclubes ativos</tspan>
  <tspan x="80" dy="30">// 4.800+ jovens · 18 cidades</tspan>
  <tspan x="80" dy="30">// a partir de onde tudo já acontece</tspan>
</text>
<text x="80" y="600" font-family="IBM Plex Mono" font-size="20" fill="{SIG}">casahacker.org/clubes</text>
</svg>'''


# ---------- WHATSAPP STICKERS (512×512) ------------------------------------
def whatsapp_sticker(label, bg, fg, accent=None):
    """Sticker WhatsApp 512×512."""
    accent = accent or fg
    return f'''<svg viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="sticker {label}">
<rect x="20" y="20" width="200" height="200" rx="20" fill="{bg}" stroke="{fg}" stroke-width="4"/>
<text x="120" y="135" font-family="Roboto Flex" font-size="40" font-weight="700" fill="{fg}" text-anchor="middle" letter-spacing="-1">{label}</text>
<g transform="translate(105, 165)">{h_pixel(0, 0, 10, accent)}</g>
</svg>'''


# ---------- SLIDE DECKS (1920×1080 → viewBox compressed) -------------------
def slide_capa():
    return f'''<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="slide capa">
<rect width="1920" height="1080" fill="{DOS}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 19.svg" x="0" y="0" width="1920" height="1080" opacity="0.10"/>
<g transform="translate(120, 120)">{h_pixel(0, 0, 32, SIG)}</g>
<text x="120" y="500" font-family="Roboto Flex" font-size="120" font-weight="300" fill="{CSS}" letter-spacing="-4">apresentação</text>
<text x="120" y="640" font-family="Roboto Flex" font-size="120" font-weight="700" fill="{SIG}" letter-spacing="-4">hackerclubes</text>
<rect x="120" y="720" width="240" height="6" fill="{CODE}"/>
<text x="120" y="820" font-family="IBM Plex Mono" font-size="28" fill="{INSPECT}">// programa de clubes de tecnologia em escolas</text>
<text x="120" y="980" font-family="IBM Plex Mono" font-size="20" fill="{JAVA}">casa hacker · 2026</text>
</svg>'''


def slide_divider():
    return f'''<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="slide divider">
<rect width="1920" height="1080" fill="{SIG}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 22.svg" x="0" y="0" width="1920" height="1080" opacity="0.12"/>
<text x="120" y="200" font-family="IBM Plex Mono" font-size="32" fill="{DOS}" letter-spacing="3">// SEÇÃO 02</text>
<text x="120" y="600" font-family="Roboto Flex" font-size="180" font-weight="700" fill="{DOS}" letter-spacing="-6">o que</text>
<text x="120" y="780" font-family="Roboto Flex" font-size="180" font-weight="300" fill="{DOS}" letter-spacing="-6">já fizemos</text>
<g transform="translate(120, 920)">{h_pixel(0, 0, 32, DOS)}</g>
</svg>'''


def slide_content():
    return f'''<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="slide content + image">
<rect width="1920" height="1080" fill="{CSS}"/>
<text x="120" y="120" font-family="IBM Plex Mono" font-size="24" fill="{JAVA}" letter-spacing="2">// COMO FUNCIONA</text>
<text x="120" y="220" font-family="Roboto Flex" font-size="80" font-weight="500" fill="{DOS}" letter-spacing="-2">3 pilares</text>
<rect x="120" y="270" width="120" height="4" fill="{SIG_DARK}"/>
<g font-family="Roboto Flex" font-size="34" fill="{DOS}">
  <text x="120" y="380" font-weight="700" fill="{SIG_DARK}">01 · orientação</text>
  <text x="120" y="430" font-size="24" fill="{JAVA}">um professor capacitado guia o clube</text>

  <text x="120" y="540" font-weight="700" fill="{SIG_DARK}">02 · projeto</text>
  <text x="120" y="590" font-size="24" fill="{JAVA}">grupo cria projeto resolvendo problema real</text>

  <text x="120" y="700" font-weight="700" fill="{SIG_DARK}">03 · comunidade</text>
  <text x="120" y="750" font-size="24" fill="{JAVA}">conectado com 140+ clubes em rede nacional</text>
</g>
<!-- imagem direita -->
<rect x="1120" y="120" width="680" height="800" fill="{INSPECT}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 28.svg" x="1120" y="120" width="680" height="800" opacity="0.40"/>
<g transform="translate(1410, 480)">{h_pixel(0, 0, 28, SIG_DARK)}</g>
<text x="1460" y="540" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}" text-anchor="middle">// foto turma</text>
<text x="120" y="1010" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}">03 / 18</text>
</svg>'''


def slide_chart():
    return f'''<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="slide chart">
<rect width="1920" height="1080" fill="{CSS}"/>
<text x="120" y="120" font-family="IBM Plex Mono" font-size="24" fill="{JAVA}" letter-spacing="2">// MÉTRICAS</text>
<text x="120" y="220" font-family="Roboto Flex" font-size="64" font-weight="500" fill="{DOS}" letter-spacing="-1">crescimento de clubes</text>
<rect x="120" y="270" width="80" height="4" fill="{SIG_DARK}"/>
<text x="120" y="320" font-family="IBM Plex Mono" font-size="22" fill="{JAVA}">// 2020 - 2026</text>

<!-- chart bars -->
<g>
  <rect x="240" y="640" width="100" height="160" fill="{SIG}"/>
  <text x="290" y="630" font-family="IBM Plex Mono" font-size="22" fill="{DOS}" text-anchor="middle">8</text>
  <text x="290" y="830" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}" text-anchor="middle">2020</text>

  <rect x="400" y="580" width="100" height="220" fill="{SIG}"/>
  <text x="450" y="570" font-family="IBM Plex Mono" font-size="22" fill="{DOS}" text-anchor="middle">22</text>
  <text x="450" y="830" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}" text-anchor="middle">2021</text>

  <rect x="560" y="500" width="100" height="300" fill="{SIG_DARK}"/>
  <text x="610" y="490" font-family="IBM Plex Mono" font-size="22" fill="{DOS}" text-anchor="middle">48</text>
  <text x="610" y="830" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}" text-anchor="middle">2022</text>

  <rect x="720" y="420" width="100" height="380" fill="{SIG_DARK}"/>
  <text x="770" y="410" font-family="IBM Plex Mono" font-size="22" fill="{DOS}" text-anchor="middle">76</text>
  <text x="770" y="830" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}" text-anchor="middle">2023</text>

  <rect x="880" y="340" width="100" height="460" fill="{CODE}"/>
  <text x="930" y="330" font-family="IBM Plex Mono" font-size="22" fill="{DOS}" text-anchor="middle">98</text>
  <text x="930" y="830" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}" text-anchor="middle">2024</text>

  <rect x="1040" y="240" width="100" height="560" fill="{CODE}"/>
  <text x="1090" y="230" font-family="IBM Plex Mono" font-size="22" fill="{DOS}" text-anchor="middle">122</text>
  <text x="1090" y="830" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}" text-anchor="middle">2025</text>

  <rect x="1200" y="180" width="100" height="620" fill="{CODE}"/>
  <text x="1250" y="170" font-family="IBM Plex Mono" font-size="22" fill="{DOS}" text-anchor="middle">142</text>
  <text x="1250" y="830" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}" text-anchor="middle">2026</text>
</g>
<!-- callout -->
<rect x="1420" y="350" width="380" height="240" fill="{DOS}"/>
<text x="1440" y="410" font-family="IBM Plex Mono" font-size="22" fill="{CODE}" letter-spacing="2">// DESTAQUE</text>
<text x="1440" y="500" font-family="Roboto Flex" font-size="60" font-weight="700" fill="{CSS}">+1675%</text>
<text x="1440" y="550" font-family="IBM Plex Mono" font-size="20" fill="{INSPECT}">crescimento em 6 anos</text>
<text x="120" y="1010" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}">10 / 18</text>
</svg>'''


def slide_quote():
    """Slide quote · frase canônica do manifesto sobre periferia."""
    return f'''<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="slide quote manifesto">
<rect width="1920" height="1080" fill="{SIG}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 31.svg" x="0" y="0" width="1920" height="1080" opacity="0.10"/>
<text x="120" y="280" font-family="Roboto Flex" font-size="220" font-weight="700" fill="{SIG_DARK}" opacity="0.5">"</text>
<text x="120" y="540" font-family="Roboto Flex" font-size="56" font-weight="400" fill="{DOS}" letter-spacing="-1">
  <tspan x="120" dy="0">as periferias não são</tspan>
  <tspan x="120" dy="76">um lugar de espera,</tspan>
  <tspan x="120" dy="76">são um lugar de começo:</tspan>
  <tspan x="120" dy="76">de ideias, de tecnologias,</tspan>
  <tspan x="120" dy="76">de inovação.</tspan>
</text>
<rect x="120" y="960" width="80" height="4" fill="{DOS}"/>
<text x="120" y="1015" font-family="IBM Plex Mono" font-size="22" fill="{DOS}">// manifesto casa hacker</text>
</svg>'''


def slide_closing():
    """Slide closing · convite final do manifesto."""
    return f'''<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="slide closing">
<rect width="1920" height="1080" fill="{DOS}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 33.svg" x="0" y="0" width="1920" height="1080" opacity="0.08"/>
<text x="120" y="280" font-family="Roboto Flex" font-size="100" font-weight="300" fill="{CSS}" letter-spacing="-3">quem quiser</text>
<text x="120" y="380" font-family="Roboto Flex" font-size="100" font-weight="300" fill="{CSS}" letter-spacing="-3">caminhar junto</text>
<text x="120" y="510" font-family="Roboto Flex" font-size="120" font-weight="700" fill="{CODE}" letter-spacing="-4">é bem-vindo</text>
<rect x="120" y="560" width="160" height="6" fill="{SIG}"/>
<g font-family="IBM Plex Mono" font-size="28" fill="{INSPECT}">
  <text x="120" y="680">// hackerclubes@casahacker.org</text>
  <text x="120" y="730">// casahacker.org/clubes</text>
  <text x="120" y="780">// @hackerclubes nas redes</text>
</g>
<g transform="translate(120, 880)">{h_pixel(0, 0, 28, SIG)}</g>
<text x="180" y="918" font-family="IBM Plex Mono" font-size="22" fill="{SIG}">obrigado.</text>
<text x="120" y="1010" font-family="IBM Plex Mono" font-size="18" fill="{JAVA}">18 / 18</text>
</svg>'''


# ---------- MATERIAL EDUCACIONAL --------------------------------------------
def diploma():
    return f'''<svg viewBox="0 0 1500 1050" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="diploma de participação">
<rect width="1500" height="1050" fill="{CSS}"/>
<rect x="40" y="40" width="1420" height="970" fill="none" stroke="{SIG_DARK}" stroke-width="3"/>
<rect x="60" y="60" width="1380" height="930" fill="none" stroke="{SIG}" stroke-width="1"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 19.svg" x="80" y="80" width="1340" height="890" opacity="0.05"/>
<g transform="translate(700, 120)">{h_pixel(0, 0, 26, SIG_DARK)}</g>
<text x="750" y="170" font-family="IBM Plex Mono" font-size="24" fill="{DOS}" text-anchor="middle" letter-spacing="3">// CERTIFICADO</text>
<text x="750" y="320" font-family="Roboto Flex" font-size="64" font-weight="300" fill="{DOS}" text-anchor="middle" letter-spacing="-1">a casa hacker certifica que</text>
<text x="750" y="500" font-family="Roboto Flex" font-size="80" font-weight="700" fill="{SIG_DARK}" text-anchor="middle" letter-spacing="-2">maria souza silva</text>
<rect x="500" y="540" width="500" height="2" fill="{DOS}"/>
<text x="750" y="620" font-family="Roboto Flex" font-size="32" fill="{DOS}" text-anchor="middle">
  <tspan x="750" dy="0">participou do hackerclube ibirapuera</tspan>
  <tspan x="750" dy="44">no ano letivo de 2026 · 60 horas</tspan>
</text>
<g transform="translate(280, 850)">
  <line x1="0" y1="0" x2="280" y2="0" stroke="{DOS}"/>
  <text x="140" y="30" font-family="IBM Plex Mono" font-size="18" fill="{DOS}" text-anchor="middle">orientador(a)</text>
</g>
<g transform="translate(940, 850)">
  <line x1="0" y1="0" x2="280" y2="0" stroke="{DOS}"/>
  <text x="140" y="30" font-family="IBM Plex Mono" font-size="18" fill="{DOS}" text-anchor="middle">coordenação casa hacker</text>
</g>
</svg>'''


def apostila_capa():
    return f'''<svg viewBox="0 0 420 594" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="apostila capa A4">
<rect width="420" height="594" fill="{SIG_DARK}"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 22.svg" x="0" y="0" width="420" height="594" opacity="0.18"/>
<g transform="translate(40, 60)">{h_pixel(0, 0, 16, CODE)}</g>
<text x="40" y="220" font-family="IBM Plex Mono" font-size="14" fill="{INSPECT}" letter-spacing="2">// APOSTILA · MÓDULO 01</text>
<text x="40" y="320" font-family="Roboto Flex" font-size="56" font-weight="300" fill="{CSS}" letter-spacing="-2">o que é</text>
<text x="40" y="380" font-family="Roboto Flex" font-size="56" font-weight="700" fill="{CSS}" letter-spacing="-2">programação?</text>
<rect x="40" y="420" width="60" height="3" fill="{CODE}"/>
<text x="40" y="460" font-family="IBM Plex Mono" font-size="14" fill="{INSPECT}">// 40 páginas · projetos práticos · gratuito</text>
<text x="40" y="555" font-family="IBM Plex Mono" font-size="11" fill="{SIG}">casahacker.org/clubes/apostilas</text>
</svg>'''


def crachá_clube():
    """Crachá específico do membro de clube."""
    return f'''<svg viewBox="0 0 200 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="crachá hackerclube">
<rect x="20" y="20" width="160" height="14" fill="{SIG_DARK}"/>
<line x1="100" y1="34" x2="100" y2="42" stroke="{DOS}" stroke-width="2"/>
<rect x="10" y="42" width="180" height="226" rx="3" fill="{CSS}" stroke="{DOS}" stroke-width="0.5"/>
<rect x="10" y="42" width="180" height="48" fill="{SIG}"/>
<text x="20" y="68" font-family="IBM Plex Mono" font-size="11" fill="{DOS}" letter-spacing="0.5">// HACKERCLUBE</text>
<text x="20" y="82" font-family="IBM Plex Mono" font-size="8" fill="{DOS}">ibirapuera · sp</text>
<text x="20" y="125" font-family="Roboto Flex" font-size="20" font-weight="500" fill="{DOS}">julia rocha</text>
<text x="20" y="145" font-family="IBM Plex Mono" font-size="8" fill="{JAVA}">8ª série · 13 anos</text>
<rect x="20" y="155" width="160" height="0.5" fill="{INSPECT}"/>
<text x="20" y="175" font-family="IBM Plex Mono" font-size="7" fill="{JAVA}">// papel</text>
<text x="20" y="187" font-family="IBM Plex Mono" font-size="9" fill="{DOS}">desenvolvedora · clube alpha</text>
<text x="20" y="205" font-family="IBM Plex Mono" font-size="7" fill="{JAVA}">// orientador</text>
<text x="20" y="217" font-family="IBM Plex Mono" font-size="9" fill="{DOS}">prof. carlos silva</text>
<g transform="translate(20, 230)">
  <rect width="40" height="40" fill="{DOS}"/>
  <g fill="{CSS}"><rect x="4" y="4" width="4" height="4"/><rect x="14" y="4" width="4" height="4"/><rect x="24" y="4" width="4" height="4"/><rect x="32" y="4" width="4" height="4"/><rect x="14" y="14" width="4" height="4"/><rect x="24" y="14" width="4" height="4"/></g>
</g>
<text x="70" y="248" font-family="IBM Plex Mono" font-size="7" fill="{JAVA}">// id</text>
<text x="70" y="260" font-family="IBM Plex Mono" font-size="9" fill="{DOS}">HC-IBI-2026-0142</text>
</svg>'''


# ---------- APPLIES ESPECÍFICAS --------------------------------------------
def t_shirt_clube():
    """T-shirt uniforme de clube."""
    return f'''<svg viewBox="0 0 240 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="t-shirt hackerclube">
<path d="M50 50 L25 60 L15 100 L40 110 L40 270 L200 270 L200 110 L225 100 L215 60 L190 50 L155 35 L135 60 Q120 75 105 60 L85 35 Z" fill="{SIG_DARK}" stroke="#0F4FCE" stroke-width="0.5"/>
<path d="M105 50 Q120 70 135 50" fill="none" stroke="#0F4FCE" stroke-width="0.8"/>
<g transform="translate(100, 110)">{h_pixel(0, 0, 9, CODE)}</g>
<text x="120" y="165" font-family="IBM Plex Mono" font-size="6" fill="{CSS}" text-anchor="middle" letter-spacing="0.3">// HACKERCLUBES</text>
<text x="120" y="220" font-family="Roboto Flex" font-size="9" font-weight="700" fill="{CSS}" text-anchor="middle">clube alpha · ibirapuera</text>
<text x="120" y="240" font-family="IBM Plex Mono" font-size="6" fill="{INSPECT}" text-anchor="middle">2026</text>
</svg>'''


def pin_botton():
    """Pin/botton 38mm clube."""
    return f'''<svg viewBox="0 0 180 180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="botton/pin hackerclube">
<circle cx="90" cy="90" r="80" fill="{SIG}" stroke="{SIG_DARK}" stroke-width="2"/>
<circle cx="90" cy="90" r="80" fill="none" stroke="{DOS}" stroke-width="0.5" stroke-dasharray="2 2" opacity="0.3"/>
<text x="90" y="50" font-family="IBM Plex Mono" font-size="9" fill="{DOS}" text-anchor="middle" letter-spacing="0.8">// MEMBRO</text>
<g transform="translate(72, 65)">{h_pixel(0, 0, 12, DOS)}</g>
<text x="90" y="135" font-family="IBM Plex Mono" font-size="9" font-weight="600" fill="{DOS}" text-anchor="middle">hackerclubes</text>
<text x="90" y="148" font-family="IBM Plex Mono" font-size="7" fill="{DOS}" text-anchor="middle" opacity="0.7">2026</text>
</svg>'''


def caderno_aluno():
    """Caderno A5 do aluno do clube."""
    return f'''<svg viewBox="0 0 148 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="caderno aluno A5">
<rect width="148" height="210" fill="{SIG_DARK}" rx="1"/>
<image href="../../assets/grafismos/PATTERNS_Artboard 28.svg" x="0" y="0" width="148" height="210" opacity="0.08"/>
<!-- espiral -->
<g fill="{CODE}">
  <rect x="0" y="20" width="6" height="2"/>
  <rect x="0" y="36" width="6" height="2"/>
  <rect x="0" y="52" width="6" height="2"/>
  <rect x="0" y="68" width="6" height="2"/>
  <rect x="0" y="84" width="6" height="2"/>
  <rect x="0" y="100" width="6" height="2"/>
  <rect x="0" y="116" width="6" height="2"/>
  <rect x="0" y="132" width="6" height="2"/>
  <rect x="0" y="148" width="6" height="2"/>
  <rect x="0" y="164" width="6" height="2"/>
  <rect x="0" y="180" width="6" height="2"/>
</g>
<text x="74" y="50" font-family="IBM Plex Mono" font-size="6" fill="{INSPECT}" text-anchor="middle">// MEU CADERNO</text>
<g transform="translate(60, 70)">{h_pixel(0, 0, 9, CODE)}</g>
<text x="74" y="138" font-family="Roboto Flex" font-size="14" font-weight="300" fill="{CSS}" text-anchor="middle">hackerclubes</text>
<rect x="34" y="148" width="80" height="0.5" fill="{CODE}"/>
<text x="74" y="170" font-family="IBM Plex Mono" font-size="6" fill="{INSPECT}" text-anchor="middle">// nome:</text>
<line x1="34" y1="180" x2="114" y2="180" stroke="{INSPECT}" stroke-width="0.3"/>
<text x="74" y="195" font-family="IBM Plex Mono" font-size="6" fill="{INSPECT}" text-anchor="middle">// clube · escola · ano</text>
</svg>'''


def adesivo_carteira():
    """Adesivo de carteira / notebook 80×30mm."""
    return f'''<svg viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="adesivo notebook">
<rect x="2" y="2" width="196" height="76" rx="3" fill="{DOS}" stroke="{INSPECT}" stroke-width="0.5" stroke-dasharray="2 2" opacity="0.9"/>
<g transform="translate(15, 22)">{h_pixel(0, 0, 12, CODE)}</g>
<text x="62" y="36" font-family="Roboto Flex" font-size="14" font-weight="500" fill="{CSS}">hackerclube</text>
<text x="62" y="56" font-family="IBM Plex Mono" font-size="9" fill="{SIG}">// curioso desde sempre</text>
</svg>'''


# ---------- LOGO USAGE ----------------------------------------------------
def logo_grid_demo():
    """Grid de clear-space + tamanho mínimo."""
    return f'''<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="grid de uso do logo">
<rect width="720" height="360" fill="{CSS}"/>
<!-- esquerda: clear space -->
<g transform="translate(40, 40)">
  <rect x="0" y="0" width="280" height="280" fill="none" stroke="{INSPECT}" stroke-dasharray="2 2"/>
  <rect x="60" y="60" width="160" height="160" fill="none" stroke="{SIG_DARK}" stroke-dasharray="3 3"/>
  <g transform="translate(100, 100)">{h_pixel(0, 0, 27, DOS)}</g>
  <text x="140" y="320" font-family="IBM Plex Mono" font-size="11" fill="{JAVA}" text-anchor="middle">clear space · 1× altura do H</text>
</g>
<!-- direita: tamanhos -->
<g transform="translate(380, 60)">
  <text x="0" y="-10" font-family="IBM Plex Mono" font-size="11" fill="{JAVA}">// tamanhos canônicos</text>
  <g transform="translate(0, 20)">{h_pixel(0, 0, 4, DOS)}</g>
  <text x="50" y="50" font-family="IBM Plex Mono" font-size="11" fill="{DOS}">12px · min digital</text>
  <g transform="translate(0, 80)">{h_pixel(0, 0, 8, DOS)}</g>
  <text x="50" y="120" font-family="IBM Plex Mono" font-size="11" fill="{DOS}">24px · uso comum</text>
  <g transform="translate(0, 160)">{h_pixel(0, 0, 14, DOS)}</g>
  <text x="80" y="220" font-family="IBM Plex Mono" font-size="11" fill="{DOS}">42px · destaque</text>
</g>
</svg>'''


# ---------- GERA A PÁGINA --------------------------------------------------
write("pages/submarcas/hackerclubes.html", page(
    "hackerclubes", "Hackerclubes",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">submarcas</a><span class="sep">/</span>hackerclubes',
    "Programa principal da Casa Hacker · clubes de tecnologia em escolas. Identidade visual completa: posts, stories, slides, material educacional, aplicações escolares e kit institucional.",
    "".join([
        # Hero · 01
        sec("hero", "identidade · hackerclubes", "01 · flagship program",
            '<div class="row mb-05"><span class="submarca-chip" data-submarca="hackerclubes">hackerclubes</span><span class="t-helper">tecnologia + educação básica</span><span class="tag tag--blue">flagship</span></div>'
            '<div class="logo-stage" style="position:relative;background:var(--logo-stage-bg);padding:var(--spacing-09);border:1px solid var(--logo-stage-border);text-align:center;overflow:hidden;">'
            '<div aria-hidden="true" style="position:absolute;inset:0;background-image:url(\'../../assets/grafismos/PATTERNS_Artboard 19.svg\');background-size:160px;background-repeat:repeat;opacity:0.10;mix-blend-mode:multiply;pointer-events:none"></div>'
            '<img src="../../assets/submarcas/hackerclubes/HACKERCLUBES_Artboard 103.svg" alt="logo Hackerclubes" loading="lazy" style="max-width:320px;max-height:120px;margin:0 auto;position:relative;z-index:1;">'
            '</div>'
            f'<div class="grid-3 mt-06"><div class="tile tile--bordered"><h4>142</h4><p>clubes ativos · 18 cidades brasileiras</p></div>'
            f'<div class="tile tile--bordered"><h4>4.800+</h4><p>jovens impactados desde 2020</p></div>'
            f'<div class="tile tile--bordered"><h4>87%</h4><p>taxa de continuidade após o 1º ano</p></div></div>'),

        # Tagline + tom de voz · 02 (frases do manifesto)
        sec("voice", "tagline + tom de voz", "02 · público amplo",
            '<p class="t-body-02 t-secondary mb-05 prose">Público: jovens, orientadores, comunidades. Tom direto, brasileiro, sem condescendência. Frases-fonte vêm do <a class="link" href="../about/manifesto.html">manifesto oficial</a> · não inventar paráfrases.</p>'
            '<div class="grid-2 mb-05">'
            '<div class="tile" style="background:var(--ch-sub-hackerclubes);color:var(--ch-sub-hackerclubes-fg);padding:var(--spacing-07)">'
            '<div class="t-label-01" style="color:inherit;opacity:0.7">// TAGLINE PRINCIPAL · DO MANIFESTO</div>'
            '<h3 style="font:300 32px/1.2 var(--font-sans);color:inherit;margin-top:var(--spacing-04);letter-spacing:-0.02em">o futuro não é uma coisa <strong>distante</strong></h3>'
            '</div>'
            '<div class="tile tile--bordered">'
            '<div class="t-label-01">// TAGLINES ALTERNATIVAS · DO MANIFESTO</div>'
            '<p class="mt-03" style="font:var(--code-02);color:var(--text-primary);line-height:1.85">→ vamos programar outros futuros<br>→ a partir de onde tudo já acontece<br>→ periferia: lugar de começo<br>→ tecnologia como direito</p>'
            '</div>'
            '</div>'
            + '<p class="t-body-02 t-secondary mb-05 prose"><strong>Princípio:</strong> tratar tecnologia como direito e linguagem de poder, não como privilégio. Conteúdo deve refletir essa postura.</p>'
            + do_dont(
                ['Frases exatas do manifesto · texto canônico',
                 'Verbos de ação · "programa", "inventa", "ocupa"',
                 'Caixa baixa nas labels · estilo CHDS',
                 'Linguagem que vem do território · "quebrada", "rua"',
                 'Referenciar autonomia, território, direito'],
                ['Tom paternalista · "querido jovem"',
                 'Infantilização · "pequenos hackers"',
                 'Inventar taglines · usar as do manifesto',
                 'Promessas individualistas · "vire programador"',
                 'Termos elitistas · "engenheiro de software"']
            )),

        # Logo usage · 03
        sec("logo-usage", "uso do logo", "03 · clear space + tamanhos",
            demo(logo_grid_demo()) +
            checklist([
                "Clear space mínimo: 1× a altura do H ao redor do logo",
                "Tamanho mínimo digital: 12px de altura",
                "Tamanho mínimo impresso: 8mm de altura (uso comum em cartões)",
                "Em fundos escuros, usar versão Code (verde)",
                "Em fundos claros, usar versão Dos (escuro)",
                "Nunca rotacionar, distorcer ou aplicar efeitos no logo",
            ])),

        # Posts redes sociais · 04
        sec("instagram-square", "posts instagram · feed 1080×1080", "04 · 6 templates",
            '<p class="t-body-02 t-secondary mb-05 prose">Templates de feed Instagram com proporção quadrada (1080×1080). Cada um tem propósito diferente · use o adequado ao tipo de conteúdo.</p>'
            '<div class="mockup-grid">'
            + f'<div class="mockup"><div class="mockup-stage">{post_anuncio_evento()}</div><div class="mockup-meta"><span class="mockup-label">anúncio de evento</span><span class="mockup-sub">inscrição aberta · CTA claro</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{post_citacao()}</div><div class="mockup-meta"><span class="mockup-label">citação de aluno</span><span class="mockup-sub">depoimento · destaque humano</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{post_carrossel_capa()}</div><div class="mockup-meta"><span class="mockup-label">carrossel · capa</span><span class="mockup-sub">1 de 5 · pergunta abre</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{post_carrossel_conteudo()}</div><div class="mockup-meta"><span class="mockup-label">carrossel · conteúdo</span><span class="mockup-sub">bullets + grafismo</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{post_curiosidade()}</div><div class="mockup-meta"><span class="mockup-label">curiosidade · dado</span><span class="mockup-sub">número grande · contexto</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{post_lancamento()}</div><div class="mockup-meta"><span class="mockup-label">lançamento</span><span class="mockup-sub">novo clube · cor Code</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{post_bastidores()}</div><div class="mockup-meta"><span class="mockup-label">bastidores</span><span class="mockup-sub">foto + texto · cor Dos</span></div></div>'
            + '</div>'),

        # Stories · 05
        sec("instagram-story", "stories · vertical 1080×1920", "05 · 3 templates",
            '<p class="t-body-02 t-secondary mb-05 prose">Stories verticais · pensados pra interação rápida e mobile-first. Use stickers nativos do Instagram (votação, perguntas, countdown) sobre os templates.</p>'
            '<div class="mockup-grid">'
            + f'<div class="mockup"><div class="mockup-stage">{story_save_date()}</div><div class="mockup-meta"><span class="mockup-label">save the date</span><span class="mockup-sub">tagline gigante</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{story_countdown()}</div><div class="mockup-meta"><span class="mockup-label">countdown</span><span class="mockup-sub">número grande · contagem</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{story_quiz()}</div><div class="mockup-meta"><span class="mockup-label">quiz interativo</span><span class="mockup-sub">3 opções · A/B/C</span></div></div>'
            + '</div>'),

        # LinkedIn · 06
        sec("linkedin", "linkedin · institucional", "06 · 1200×627",
            '<p class="t-body-02 t-secondary mb-05 prose">LinkedIn pede tom mais institucional · números + impacto. Banner usado em página de empresa.</p>'
            + demo(f'<div style="max-width:720px;margin:0 auto">{linkedin_institutional()}</div>')),

        # WhatsApp stickers · 07
        sec("whatsapp", "whatsapp stickers", "07 · 4 stickers prontos",
            '<p class="t-body-02 t-secondary mb-05 prose">Pack de 4 stickers exportáveis em 512×512 PNG transparente. Cada um expressa uma reação típica da comunidade do clube.</p>'
            '<div class="mockup-grid">'
            + f'<div class="mockup"><div class="mockup-stage">{whatsapp_sticker("hackeei", SIG, DOS)}</div><div class="mockup-meta"><span class="mockup-label">hackeei!</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{whatsapp_sticker("não rodou", DOS, CSS, CODE)}</div><div class="mockup-meta"><span class="mockup-label">não rodou</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{whatsapp_sticker("tmj", CODE, DOS)}</div><div class="mockup-meta"><span class="mockup-label">tmj</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{whatsapp_sticker("git push", DOS, CODE)}</div><div class="mockup-meta"><span class="mockup-label">git push 🚀</span></div></div>'
            + '</div>'),

        # Slide decks · 08
        sec("slides", "slide deck · apresentações 16:9", "08 · 6 templates",
            '<p class="t-body-02 t-secondary mb-05 prose">Templates pra Google Slides / Keynote / PowerPoint · proporção 16:9 (1920×1080). Use pra apresentar o programa a escolas, parceiros, instâncias governamentais.</p>'
            '<div class="mockup-grid">'
            + f'<div class="mockup"><div class="mockup-stage">{slide_capa()}</div><div class="mockup-meta"><span class="mockup-label">capa · slide 01</span><span class="mockup-sub">grafismo + título</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{slide_divider()}</div><div class="mockup-meta"><span class="mockup-label">divider · seção</span><span class="mockup-sub">cor Sec Blue</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{slide_content()}</div><div class="mockup-meta"><span class="mockup-label">conteúdo + imagem</span><span class="mockup-sub">2 colunas · 60/40</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{slide_chart()}</div><div class="mockup-meta"><span class="mockup-label">gráfico</span><span class="mockup-sub">métricas + callout</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{slide_quote()}</div><div class="mockup-meta"><span class="mockup-label">citação</span><span class="mockup-sub">aspas grandes</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{slide_closing()}</div><div class="mockup-meta"><span class="mockup-label">encerramento</span><span class="mockup-sub">contato + obrigado</span></div></div>'
            + '</div>'),

        # Material educacional · 09
        sec("educational", "material educacional", "09",
            '<p class="t-body-02 t-secondary mb-05 prose">Apostilas, certificados e crachás específicos do programa · entregues fisicamente ou em PDF aos alunos e orientadores.</p>'
            '<div class="mockup-grid">'
            + f'<div class="mockup"><div class="mockup-stage">{apostila_capa()}</div><div class="mockup-meta"><span class="mockup-label">apostila A4 capa</span><span class="mockup-sub">módulo 01 · 40 páginas</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{diploma()}</div><div class="mockup-meta"><span class="mockup-label">certificado A4 paisagem</span><span class="mockup-sub">60h · 2 assinaturas</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{crachá_clube()}</div><div class="mockup-meta"><span class="mockup-label">crachá do clube</span><span class="mockup-sub">id único · QR opcional</span></div></div>'
            + '</div>'),

        # Aplicações escolares · 10
        sec("school-applications", "aplicações escolares · merch do clube", "10",
            '<p class="t-body-02 t-secondary mb-05 prose">Identidade visual do clube em produtos do dia-a-dia escolar. Cada clube pode personalizar o nome (ex: "clube alpha", "clube ibirapuera") mantendo a identidade Hackerclubes.</p>'
            '<div class="mockup-grid">'
            + f'<div class="mockup"><div class="mockup-stage">{t_shirt_clube()}</div><div class="mockup-meta"><span class="mockup-label">camiseta de uniforme</span><span class="mockup-sub">Sec Blue · H verde · nome clube</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{pin_botton()}</div><div class="mockup-meta"><span class="mockup-label">botton 38mm</span><span class="mockup-sub">membro do clube · 2026</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{caderno_aluno()}</div><div class="mockup-meta"><span class="mockup-label">caderno A5 aluno</span><span class="mockup-sub">capa Sec Blue · espiral Code</span></div></div>'
            + f'<div class="mockup"><div class="mockup-stage">{adesivo_carteira()}</div><div class="mockup-meta"><span class="mockup-label">adesivo notebook</span><span class="mockup-sub">80×30mm · vinil fosco</span></div></div>'
            + '</div>'),

        # Paleta · 11
        sec("palette", "paleta hackerclubes", "11 · auditado",
            '<p class="t-body-02 t-secondary mb-05 prose">Hackerclubes usa toda a paleta CH com <strong>Sec Blue</strong> como cor signature de identificação. Combina com Code Green nos destaques de ação.</p>'
            '<div class="token-grid">'
            f'<div class="token-tile"><div class="token-swatch light" style="background:{SIG}"><span class="hex">#B3D9FE</span></div><div class="token-info"><span class="name">Sec Blue</span><span class="role">signature · azul tech educacional</span></div></div>'
            f'<div class="token-tile"><div class="token-swatch" style="background:{SIG_DARK}"><span class="hex">#0F62FE</span></div><div class="token-info"><span class="name">Blue Active</span><span class="role">acento · CTAs</span></div></div>'
            f'<div class="token-tile"><div class="token-swatch" style="background:{CODE}"><span class="hex">#32FA96</span></div><div class="token-info"><span class="name">Code</span><span class="role">destaque · ações</span></div></div>'
            f'<div class="token-tile"><div class="token-swatch" style="background:{DOS}"><span class="hex">#3C433C</span></div><div class="token-info"><span class="name">Dos</span><span class="role">texto · fundo escuro</span></div></div>'
            f'<div class="token-tile"><div class="token-swatch light" style="background:{CSS}"><span class="hex">#F8FCF8</span></div><div class="token-info"><span class="name">CSS</span><span class="role">fundo claro</span></div></div>'
            f'<div class="token-tile"><div class="token-swatch light" style="background:{PINK}"><span class="hex">#FF9ECF</span></div><div class="token-info"><span class="name">Sec Pink</span><span class="role">variação eventual</span></div></div>'
            f'<div class="token-tile"><div class="token-swatch light" style="background:#E1FFDE"><span class="hex">#E1FFDE</span></div><div class="token-info"><span class="name">Sec Green Light</span><span class="role">variação eventual</span></div></div>'
            '</div>'),

        # Grafismos signature · 12
        sec("grafismos", "grafismos signature", "12 · 6 favoritos",
            '<p class="t-body-02 t-secondary mb-05 prose">6 grafismos da biblioteca CH (67 total) selecionados pelo encaixe visual com a identidade Hackerclubes. Use como backgrounds em posts, slides, materiais impressos.</p>'
            '<div class="grid-3" style="gap:var(--spacing-04)">'
            + ''.join(
                f'<div style="background:{bg};padding:var(--spacing-05);border:1px solid var(--border-subtle-00)">'
                f'<div style="aspect-ratio:1;background-image:url(\'../../assets/grafismos/PATTERNS_Artboard {num}.svg\');background-size:contain;background-repeat:no-repeat;background-position:center;background-color:{fg};opacity:1;margin-bottom:var(--spacing-03)"></div>'
                f'<div style="font:var(--label-01);text-transform:uppercase;letter-spacing:0.08em;color:var(--text-primary)">artboard {num}</div>'
                f'<div style="font:var(--code-01);color:var(--text-helper);margin-top:var(--spacing-02)">{label}</div>'
                f'</div>'
                for num, label, bg, fg in [
                    (19, "modular educacional · backgrounds", "var(--layer-02)", "transparent"),
                    (22, "DIY mosaico · capas", "var(--layer-02)", "transparent"),
                    (28, "acolhedor · materiais soft", "var(--layer-02)", "transparent"),
                    (29, "isométrico 3d · destaque", "var(--layer-02)", "transparent"),
                    (31, "fluido · backgrounds amplos", "var(--layer-02)", "transparent"),
                    (33, "estruturado · convites", "var(--layer-02)", "transparent"),
                ]
            )
            + '</div>'
            + '<p class="t-helper mt-04">Biblioteca completa em <a class="link" href="../patterns/grafismos.html">/patterns/grafismos</a> · 67 padrões disponíveis</p>'),

        # Como montar um clube · 13
        sec("howto", "como montar um clube", "13 · passo-a-passo",
            '<p class="t-body-02 t-secondary mb-05 prose">Guia rápido pra criar um Hackerclube na sua escola. O processo completo está no manual do orientador (PDF · disponível mediante cadastro).</p>'
            + '<div class="grid-2">'
            '<div class="tile tile--bordered">'
            '<h4>01 · proposta</h4>'
            '<p>Direção e coordenação alinham objetivo + horário. Não precisa de laboratório especial · começa com o que tem.</p>'
            '</div>'
            '<div class="tile tile--bordered">'
            '<h4>02 · orientador</h4>'
            '<p>Um professor (qualquer área) topa orientar. Casa Hacker oferece capacitação online de 20h gratuita.</p>'
            '</div>'
            '<div class="tile tile--bordered">'
            '<h4>03 · turma</h4>'
            '<p>5-20 alunos por turma · inscrição aberta na escola. Sem pré-requisito técnico.</p>'
            '</div>'
            '<div class="tile tile--bordered">'
            '<h4>04 · projeto</h4>'
            '<p>1 projeto por semestre resolvendo problema da comunidade. Pode ser app, site, instalação, mídia.</p>'
            '</div>'
            '<div class="tile tile--bordered">'
            '<h4>05 · encontro</h4>'
            '<p>Conexão com outros clubes via discord nacional · participação no hackathon anual.</p>'
            '</div>'
            '<div class="tile tile--bordered">'
            '<h4>06 · suporte contínuo</h4>'
            '<p>Casa Hacker apoia com material, mentoria e contato com profissionais da indústria.</p>'
            '</div>'
            '</div>'
            + '<div class="callout callout--info mt-06" data-icon="→"><div><strong>Interessado em criar um clube?</strong>Cadastre a escola em <code class="code-inline">casahacker.org/clubes/criar</code> · resposta em até 48h úteis.</div></div>'),

        # Assets · 14
        sec("assets", "assets · download", "14 · tudo aqui",
            '<p class="t-body-02 t-secondary mb-05 prose">Arquivos vetoriais e templates editáveis disponíveis.</p>'
            + table(["recurso", "formato", "local"], [
                ["Logos vetoriais (24 variantes)", "SVG", "assets/submarcas/hackerclubes/"],
                ["Grafismos da biblioteca", "SVG", "assets/grafismos/PATTERNS_Artboard {19,22,28,29,31,33}.svg"],
                ["Templates de slide deck", "PPTX/Keynote", "[em construção]"],
                ["Templates de post Instagram", "PSD/Figma", "[em construção]"],
                ["Apostila pedagógica", "PDF", "casahacker.org/clubes/apostilas"],
                ["Manual do orientador", "PDF · 80 páginas", "casahacker.org/clubes/manual"],
                ["Identidade visual aplicada", "Esta página", "/pages/submarcas/hackerclubes.html"],
            ])),
    ]),
    tags=[
        {"cls":"tag--code","label":"flagship"},
        {"cls":"tag--blue","label":"Sec Blue signature"},
        {"cls":"tag--outline","label":"educação básica"},
    ],
    toc=[
        {"id":"hero","label":"Identidade"},
        {"id":"voice","label":"Tagline + voz"},
        {"id":"logo-usage","label":"Uso do logo"},
        {"id":"instagram-square","label":"Posts feed"},
        {"id":"instagram-story","label":"Stories"},
        {"id":"linkedin","label":"LinkedIn"},
        {"id":"whatsapp","label":"WhatsApp"},
        {"id":"slides","label":"Slide deck"},
        {"id":"educational","label":"Material educacional"},
        {"id":"school-applications","label":"Aplicações escolares"},
        {"id":"palette","label":"Paleta"},
        {"id":"grafismos","label":"Grafismos"},
        {"id":"howto","label":"Como montar"},
        {"id":"assets","label":"Assets"},
    ],
))

print("done · hackerclubes (flagship page)")
