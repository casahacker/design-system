"""Impressos (4 pages) · papelaria · eventos · loja & merch + index.

Mockups SVG inline com proporções reais (referência Printi BR).
Cada item tem: visual de aplicação · specs técnicos · bleed/sangria · CMYK.
"""
from common import page, sec, demo, do_dont, code, checklist, table, write

# ---------- mockup helpers --------------------------------------------------
def mockup(svg, label, sub=""):
    """Wrapper para mockup SVG · label uppercase + descrição opcional."""
    return (
        f'<div class="mockup">'
        f'<div class="mockup-stage">{svg}</div>'
        f'<div class="mockup-meta"><span class="mockup-label">{label}</span>'
        + (f'<span class="mockup-sub">{sub}</span>' if sub else '')
        + f'</div></div>'
    )


# ---------- SVG templates (proporções reais) -------------------------------
def card_business():
    """Cartão de visita 90×50mm (padrão BR via Printi)."""
    return '''<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="cartão de visita frente e verso">
<!-- frente · Dos -->
<g>
  <rect width="360" height="200" rx="2" fill="#3C433C"/>
  <!-- H pixelado -->
  <g transform="translate(28, 32)" fill="#32FA96">
    <rect width="9" height="9"/>
    <rect x="18" width="9" height="9"/>
    <rect y="18" width="9" height="9"/>
    <rect x="9" y="18" width="9" height="9"/>
    <rect x="18" y="18" width="9" height="9"/>
    <rect width="9" height="9" y="36"/>
    <rect x="18" y="36" width="9" height="9"/>
  </g>
  <text x="28" y="120" font-family="IBM Plex Mono, monospace" font-size="9" fill="#91938C" letter-spacing="0.5">// produto</text>
  <text x="28" y="138" font-family="Roboto Flex, sans-serif" font-size="14" font-weight="500" fill="#F8FCF8">geraldo barros</text>
  <text x="28" y="155" font-family="IBM Plex Mono, monospace" font-size="10" fill="#D7DCD7">tech lead · casa hacker</text>
  <text x="28" y="178" font-family="IBM Plex Mono, monospace" font-size="9" fill="#32FA96">geraldo@casahacker.org</text>
</g>
</svg>'''


def letterhead():
    """Papel timbrado A4 (210×297mm)."""
    return '''<svg viewBox="0 0 210 297" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="papel timbrado A4">
<rect width="210" height="297" fill="#F8FCF8"/>
<!-- barra superior Code -->
<rect x="0" y="0" width="210" height="6" fill="#32FA96"/>
<!-- H pequeno -->
<g transform="translate(15, 18)" fill="#3C433C">
  <rect width="3" height="3"/>
  <rect x="6" width="3" height="3"/>
  <rect y="6" width="3" height="3"/>
  <rect x="3" y="6" width="3" height="3"/>
  <rect x="6" y="6" width="3" height="3"/>
  <rect y="12" width="3" height="3"/>
  <rect x="6" y="12" width="3" height="3"/>
</g>
<text x="28" y="28" font-family="IBM Plex Mono, monospace" font-size="6" fill="#3C433C" letter-spacing="0.3">casa hacker</text>
<!-- corpo simulado -->
<g fill="#91938C" opacity="0.5">
  <rect x="25" y="55" width="160" height="2"/>
  <rect x="25" y="62" width="140" height="2"/>
  <rect x="25" y="69" width="155" height="2"/>
  <rect x="25" y="80" width="135" height="2"/>
  <rect x="25" y="87" width="160" height="2"/>
  <rect x="25" y="94" width="120" height="2"/>
  <rect x="25" y="105" width="155" height="2"/>
  <rect x="25" y="112" width="140" height="2"/>
</g>
<!-- rodapé -->
<rect x="25" y="280" width="160" height="0.5" fill="#3C433C"/>
<text x="25" y="288" font-family="IBM Plex Mono, monospace" font-size="3.5" fill="#91938C">casahacker.org · rua das hackers, 42 · são paulo</text>
</svg>'''


def envelope():
    """Envelope C5 (229×162mm)."""
    return '''<svg viewBox="0 0 229 162" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="envelope C5">
<rect width="229" height="162" fill="#F0F5F0" stroke="#D7DCD7"/>
<!-- aba traseira (linha) -->
<line x1="0" y1="0" x2="114.5" y2="60" stroke="#D7DCD7" stroke-width="0.5"/>
<line x1="229" y1="0" x2="114.5" y2="60" stroke="#D7DCD7" stroke-width="0.5"/>
<!-- logo canto -->
<g transform="translate(14, 14)" fill="#3C433C">
  <rect width="4" height="4"/>
  <rect x="8" width="4" height="4"/>
  <rect y="8" width="4" height="4"/>
  <rect x="4" y="8" width="4" height="4"/>
  <rect x="8" y="8" width="4" height="4"/>
  <rect y="16" width="4" height="4"/>
  <rect x="8" y="16" width="4" height="4"/>
</g>
<text x="26" y="22" font-family="IBM Plex Mono, monospace" font-size="6" fill="#3C433C">casa hacker</text>
<text x="14" y="40" font-family="IBM Plex Mono, monospace" font-size="4.5" fill="#91938C">rua das hackers, 42 · sp</text>
<!-- linhas destinatário -->
<g fill="#91938C" opacity="0.6">
  <rect x="100" y="100" width="100" height="2"/>
  <rect x="100" y="108" width="120" height="2"/>
  <rect x="100" y="116" width="80" height="2"/>
</g>
</svg>'''


def folder():
    """Folder A4 dobrado (capa)."""
    return '''<svg viewBox="0 0 210 297" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="folder A4 capa">
<rect width="210" height="297" fill="#3C433C"/>
<!-- grafismo de fundo -->
<g opacity="0.08" fill="#32FA96">
  <rect x="0" y="0" width="20" height="20"/>
  <rect x="40" y="40" width="20" height="20"/>
  <rect x="80" y="80" width="20" height="20"/>
  <rect x="120" y="120" width="20" height="20"/>
  <rect x="160" y="160" width="20" height="20"/>
  <rect x="0" y="40" width="20" height="20"/>
  <rect x="40" y="80" width="20" height="20"/>
  <rect x="80" y="120" width="20" height="20"/>
</g>
<!-- H grande -->
<g transform="translate(60, 80)" fill="#32FA96">
  <rect width="30" height="30"/>
  <rect x="60" width="30" height="30"/>
  <rect y="60" width="30" height="30"/>
  <rect x="30" y="60" width="30" height="30"/>
  <rect x="60" y="60" width="30" height="30"/>
  <rect y="120" width="30" height="30"/>
  <rect x="60" y="120" width="30" height="30"/>
</g>
<text x="20" y="250" font-family="Roboto Flex, sans-serif" font-size="20" font-weight="300" fill="#F8FCF8" letter-spacing="-0.5">casa hacker</text>
<text x="20" y="265" font-family="IBM Plex Mono, monospace" font-size="6" fill="#32FA96">// relatório 2026</text>
</svg>'''


def badge_event():
    """Crachá de evento 90×130mm."""
    return '''<svg viewBox="0 0 180 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="crachá de evento">
<!-- cordão -->
<rect x="78" y="0" width="24" height="14" fill="#32FA96"/>
<line x1="90" y1="14" x2="90" y2="22" stroke="#3C433C" stroke-width="2"/>
<!-- card -->
<rect x="10" y="22" width="160" height="220" rx="3" fill="#F8FCF8" stroke="#3C433C" stroke-width="0.5"/>
<!-- header verde -->
<rect x="10" y="22" width="160" height="40" fill="#32FA96"/>
<text x="20" y="48" font-family="IBM Plex Mono, monospace" font-size="11" fill="#3C433C" letter-spacing="0.5">// participante</text>
<!-- nome -->
<text x="20" y="105" font-family="Roboto Flex, sans-serif" font-size="22" font-weight="500" fill="#3C433C">maria souza</text>
<text x="20" y="125" font-family="IBM Plex Mono, monospace" font-size="9" fill="#91938C">desenvolvedora · perifa impacto</text>
<!-- QR placeholder -->
<rect x="20" y="155" width="50" height="50" fill="#3C433C"/>
<g fill="#F8FCF8">
  <rect x="24" y="159" width="6" height="6"/>
  <rect x="34" y="159" width="6" height="6"/>
  <rect x="44" y="159" width="6" height="6"/>
  <rect x="60" y="159" width="6" height="6"/>
  <rect x="24" y="169" width="6" height="6"/>
  <rect x="54" y="179" width="6" height="6"/>
  <rect x="34" y="189" width="6" height="6"/>
  <rect x="44" y="189" width="6" height="6"/>
  <rect x="60" y="199" width="6" height="6"/>
</g>
<text x="80" y="170" font-family="IBM Plex Mono, monospace" font-size="6" fill="#91938C">// linkedin</text>
<text x="80" y="180" font-family="IBM Plex Mono, monospace" font-size="6" fill="#3C433C">@msouza</text>
<text x="80" y="195" font-family="IBM Plex Mono, monospace" font-size="6" fill="#91938C">// trilha</text>
<text x="80" y="205" font-family="IBM Plex Mono, monospace" font-size="6" fill="#3C433C">backend / api</text>
<!-- footer -->
<rect x="10" y="220" width="160" height="22" fill="#3C433C"/>
<text x="20" y="234" font-family="IBM Plex Mono, monospace" font-size="7" fill="#32FA96">hackathon · 15-17 set 2026</text>
</svg>'''


def banner_rollup():
    """Banner roll-up 850×2000mm."""
    return '''<svg viewBox="0 0 100 235" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="banner roll-up">
<rect width="100" height="235" fill="#3C433C"/>
<!-- grafismo lateral -->
<g opacity="0.12" fill="#32FA96">
  <rect x="5" y="5" width="6" height="6"/>
  <rect x="5" y="17" width="6" height="6"/>
  <rect x="5" y="29" width="6" height="6"/>
  <rect x="5" y="41" width="6" height="6"/>
  <rect x="5" y="53" width="6" height="6"/>
</g>
<!-- H -->
<g transform="translate(30, 30)" fill="#32FA96">
  <rect width="10" height="10"/>
  <rect x="20" width="10" height="10"/>
  <rect y="20" width="10" height="10"/>
  <rect x="10" y="20" width="10" height="10"/>
  <rect x="20" y="20" width="10" height="10"/>
  <rect y="40" width="10" height="10"/>
  <rect x="20" y="40" width="10" height="10"/>
</g>
<text x="22" y="110" font-family="Roboto Flex, sans-serif" font-size="14" font-weight="300" fill="#F8FCF8" letter-spacing="-0.3">hack a</text>
<text x="22" y="124" font-family="Roboto Flex, sans-serif" font-size="14" font-weight="700" fill="#32FA96">casa</text>
<text x="22" y="145" font-family="IBM Plex Mono, monospace" font-size="6" fill="#D7DCD7">// hackathon brasileiro de tecnologia comunitária</text>
<text x="22" y="155" font-family="IBM Plex Mono, monospace" font-size="6" fill="#D7DCD7">// edição 2026</text>
<!-- info -->
<rect x="22" y="170" width="56" height="1" fill="#32FA96"/>
<text x="22" y="183" font-family="IBM Plex Mono, monospace" font-size="6" fill="#32FA96">15-17 setembro</text>
<text x="22" y="193" font-family="IBM Plex Mono, monospace" font-size="6" fill="#F8FCF8">casa hacker · sp</text>
<text x="22" y="220" font-family="IBM Plex Mono, monospace" font-size="5" fill="#91938C">casahacker.org/hackathon</text>
<!-- base bar -->
<rect x="0" y="230" width="100" height="5" fill="#32FA96"/>
</svg>'''


def tshirt():
    """T-shirt com logo no peito."""
    return '''<svg viewBox="0 0 220 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="t-shirt frente">
<!-- shape -->
<path d="M40 40 L20 50 L10 90 L30 100 L30 230 L190 230 L190 100 L210 90 L200 50 L180 40 L150 30 L130 50 Q110 65 90 50 L70 30 Z" fill="#3C433C" stroke="#1F231F" stroke-width="0.5"/>
<!-- gola -->
<path d="M90 40 Q110 60 130 40" fill="none" stroke="#1F231F" stroke-width="0.8"/>
<!-- H no peito -->
<g transform="translate(90, 95)" fill="#32FA96">
  <rect width="9" height="9"/>
  <rect x="18" width="9" height="9"/>
  <rect y="18" width="9" height="9"/>
  <rect x="9" y="18" width="9" height="9"/>
  <rect x="18" y="18" width="9" height="9"/>
  <rect y="36" width="9" height="9"/>
  <rect x="18" y="36" width="9" height="9"/>
</g>
<text x="110" y="160" font-family="IBM Plex Mono, monospace" font-size="6" fill="#D7DCD7" text-anchor="middle">// casa hacker</text>
</svg>'''


def mug():
    """Caneca cerâmica branca."""
    return '''<svg viewBox="0 0 220 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="caneca">
<!-- alça -->
<path d="M160 60 Q200 60 200 95 Q200 130 160 130" fill="none" stroke="#3C433C" stroke-width="6"/>
<!-- corpo -->
<rect x="40" y="40" width="130" height="120" rx="4" fill="#F8FCF8" stroke="#3C433C" stroke-width="1.5"/>
<!-- base -->
<ellipse cx="105" cy="160" rx="65" ry="5" fill="#3C433C" opacity="0.3"/>
<!-- H -->
<g transform="translate(70, 75)" fill="#32FA96">
  <rect width="8" height="8"/>
  <rect x="16" width="8" height="8"/>
  <rect y="16" width="8" height="8"/>
  <rect x="8" y="16" width="8" height="8"/>
  <rect x="16" y="16" width="8" height="8"/>
  <rect y="32" width="8" height="8"/>
  <rect x="16" y="32" width="8" height="8"/>
</g>
<text x="105" y="135" font-family="IBM Plex Mono, monospace" font-size="8" fill="#3C433C" text-anchor="middle">// hack</text>
</svg>'''


def sticker():
    """Sticker redondo 75mm."""
    return '''<svg viewBox="0 0 180 180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="sticker redondo">
<circle cx="90" cy="90" r="85" fill="#32FA96"/>
<circle cx="90" cy="90" r="85" fill="none" stroke="#3C433C" stroke-width="1" stroke-dasharray="2 2" opacity="0.3"/>
<g transform="translate(67, 55)" fill="#3C433C">
  <rect width="14" height="14"/>
  <rect x="28" width="14" height="14"/>
  <rect y="28" width="14" height="14"/>
  <rect x="14" y="28" width="14" height="14"/>
  <rect x="28" y="28" width="14" height="14"/>
  <rect y="56" width="14" height="14"/>
  <rect x="28" y="56" width="14" height="14"/>
</g>
<text x="90" y="145" font-family="IBM Plex Mono, monospace" font-size="9" fill="#3C433C" text-anchor="middle" font-weight="600">casa hacker</text>
</svg>'''


def tote_bag():
    """Tote bag / saco de algodão."""
    return '''<svg viewBox="0 0 200 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="tote bag">
<!-- alças -->
<path d="M50 30 Q70 0 90 0 L110 0 Q130 0 150 30" fill="none" stroke="#3C433C" stroke-width="3"/>
<!-- corpo do saco -->
<rect x="20" y="30" width="160" height="200" fill="#D7DCD7" stroke="#91938C" stroke-width="0.5"/>
<!-- H estampado -->
<g transform="translate(75, 95)" fill="#3C433C">
  <rect width="12" height="12"/>
  <rect x="24" width="12" height="12"/>
  <rect y="24" width="12" height="12"/>
  <rect x="12" y="24" width="12" height="12"/>
  <rect x="24" y="24" width="12" height="12"/>
  <rect y="48" width="12" height="12"/>
  <rect x="24" y="48" width="12" height="12"/>
</g>
<text x="100" y="175" font-family="IBM Plex Mono, monospace" font-size="9" fill="#3C433C" text-anchor="middle">casa hacker</text>
<text x="100" y="190" font-family="IBM Plex Mono, monospace" font-size="6" fill="#91938C" text-anchor="middle">// tecnologia + comunidade</text>
</svg>'''


def notebook():
    """Caderno A5 capa."""
    return '''<svg viewBox="0 0 148 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="caderno A5">
<rect width="148" height="210" fill="#3C433C" rx="1"/>
<!-- espiral -->
<g fill="#32FA96">
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
<!-- H grande centralizado -->
<g transform="translate(48, 70)" fill="#32FA96">
  <rect width="16" height="16"/>
  <rect x="32" width="16" height="16"/>
  <rect y="32" width="16" height="16"/>
  <rect x="16" y="32" width="16" height="16"/>
  <rect x="32" y="32" width="16" height="16"/>
  <rect y="64" width="16" height="16"/>
  <rect x="32" y="64" width="16" height="16"/>
</g>
<text x="74" y="180" font-family="IBM Plex Mono, monospace" font-size="7" fill="#D7DCD7" text-anchor="middle">// pensamento livre</text>
<text x="74" y="195" font-family="Roboto Flex, sans-serif" font-size="9" fill="#F8FCF8" text-anchor="middle">casa hacker</text>
</svg>'''


def water_bottle():
    """Garrafa térmica 500ml."""
    return '''<svg viewBox="0 0 80 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="garrafa térmica">
<!-- tampa -->
<rect x="25" y="0" width="30" height="20" rx="2" fill="#3C433C"/>
<!-- pescoço -->
<rect x="30" y="20" width="20" height="10" fill="#3C433C"/>
<!-- corpo (inox) -->
<rect x="20" y="30" width="40" height="170" rx="6" fill="#D7DCD7" stroke="#91938C" stroke-width="0.5"/>
<!-- rótulo verde wrap -->
<rect x="20" y="80" width="40" height="60" fill="#32FA96"/>
<!-- H no rótulo -->
<g transform="translate(34, 92)" fill="#3C433C">
  <rect width="3" height="3"/>
  <rect x="6" width="3" height="3"/>
  <rect y="6" width="3" height="3"/>
  <rect x="3" y="6" width="3" height="3"/>
  <rect x="6" y="6" width="3" height="3"/>
  <rect y="12" width="3" height="3"/>
  <rect x="6" y="12" width="3" height="3"/>
</g>
<text x="40" y="118" font-family="IBM Plex Mono, monospace" font-size="4" fill="#3C433C" text-anchor="middle">casa hacker</text>
<text x="40" y="130" font-family="IBM Plex Mono, monospace" font-size="3" fill="#3C433C" text-anchor="middle">500ml</text>
</svg>'''


def signage():
    """Sinalização A3 vertical (totem/placa)."""
    return '''<svg viewBox="0 0 297 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="sinalização A3">
<rect width="297" height="420" fill="#F8FCF8"/>
<!-- barra Code superior -->
<rect x="0" y="0" width="297" height="8" fill="#32FA96"/>
<!-- ícone seta grande -->
<g transform="translate(74, 50)" fill="#3C433C">
  <path d="M0 75 L150 75 L150 50 L200 100 L150 150 L150 125 L0 125 Z"/>
</g>
<text x="148" y="240" font-family="Roboto Flex, sans-serif" font-size="32" font-weight="500" fill="#3C433C" text-anchor="middle">palco a</text>
<text x="148" y="270" font-family="IBM Plex Mono, monospace" font-size="12" fill="#91938C" text-anchor="middle">// 50m à direita</text>
<!-- rodapé -->
<rect x="0" y="402" width="297" height="18" fill="#3C433C"/>
<text x="148" y="415" font-family="IBM Plex Mono, monospace" font-size="6" fill="#32FA96" text-anchor="middle">// hackathon casa hacker · setembro 2026</text>
</svg>'''


def invite():
    """Convite 100×150mm."""
    return '''<svg viewBox="0 0 200 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="convite save the date">
<rect width="200" height="300" fill="#32FA96"/>
<text x="20" y="50" font-family="IBM Plex Mono, monospace" font-size="9" fill="#3C433C" letter-spacing="0.5">// save the date</text>
<text x="20" y="120" font-family="Roboto Flex, sans-serif" font-size="36" font-weight="300" fill="#3C433C" letter-spacing="-1.5">hack a</text>
<text x="20" y="158" font-family="Roboto Flex, sans-serif" font-size="36" font-weight="700" fill="#3C433C" letter-spacing="-1.5">casa</text>
<line x1="20" y1="195" x2="80" y2="195" stroke="#3C433C" stroke-width="1.5"/>
<text x="20" y="225" font-family="IBM Plex Mono, monospace" font-size="10" fill="#3C433C">15.set.2026 · 14h</text>
<text x="20" y="240" font-family="IBM Plex Mono, monospace" font-size="10" fill="#3C433C">casa hacker · sp</text>
<text x="20" y="282" font-family="IBM Plex Mono, monospace" font-size="7" fill="#3C433C" opacity="0.7">casahacker.org/hackathon</text>
<!-- H decorativo -->
<g transform="translate(150, 235)" fill="#3C433C" opacity="0.18">
  <rect width="10" height="10"/>
  <rect x="20" width="10" height="10"/>
  <rect y="20" width="10" height="10"/>
  <rect x="10" y="20" width="10" height="10"/>
  <rect x="20" y="20" width="10" height="10"/>
  <rect y="40" width="10" height="10"/>
  <rect x="20" y="40" width="10" height="10"/>
</g>
</svg>'''


def program():
    """Programação A5 dobrado."""
    return '''<svg viewBox="0 0 296 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="programação A5 dobrada">
<rect width="296" height="210" fill="#F8FCF8"/>
<line x1="148" y1="0" x2="148" y2="210" stroke="#D7DCD7" stroke-dasharray="3 3"/>
<!-- página esquerda · capa -->
<rect x="0" y="0" width="148" height="210" fill="#3C433C"/>
<g transform="translate(60, 50)" fill="#32FA96">
  <rect width="10" height="10"/><rect x="20" width="10" height="10"/>
  <rect y="20" width="10" height="10"/><rect x="10" y="20" width="10" height="10"/><rect x="20" y="20" width="10" height="10"/>
  <rect y="40" width="10" height="10"/><rect x="20" y="40" width="10" height="10"/>
</g>
<text x="74" y="125" font-family="Roboto Flex, sans-serif" font-size="13" font-weight="300" fill="#F8FCF8" text-anchor="middle">programação</text>
<text x="74" y="142" font-family="IBM Plex Mono, monospace" font-size="6" fill="#32FA96" text-anchor="middle">// hackathon casa hacker 2026</text>
<!-- página direita · grid -->
<text x="158" y="20" font-family="IBM Plex Mono, monospace" font-size="6" fill="#91938C">// sexta · 15.set</text>
<g font-family="IBM Plex Mono, monospace" font-size="6" fill="#3C433C">
  <text x="158" y="38">09h00</text><text x="184" y="38">abertura · auditório</text>
  <text x="158" y="50">10h30</text><text x="184" y="50">workshop python · sala 1</text>
  <text x="158" y="62">14h00</text><text x="184" y="62">team formation · café</text>
  <text x="158" y="74">16h00</text><text x="184" y="74">hack começa · todo lugar</text>
  <text x="158" y="86">20h00</text><text x="184" y="86">jantar · cozinha</text>
</g>
<text x="158" y="106" font-family="IBM Plex Mono, monospace" font-size="6" fill="#91938C">// sábado · 16.set</text>
<g font-family="IBM Plex Mono, monospace" font-size="6" fill="#3C433C">
  <text x="158" y="124">09h00</text><text x="184" y="124">café + mentoria livre</text>
  <text x="158" y="136">13h00</text><text x="184" y="136">almoço comunitário</text>
  <text x="158" y="148">19h00</text><text x="184" y="148">show de hardware · palco</text>
</g>
<text x="158" y="168" font-family="IBM Plex Mono, monospace" font-size="6" fill="#91938C">// domingo · 17.set</text>
<g font-family="IBM Plex Mono, monospace" font-size="6" fill="#3C433C">
  <text x="158" y="186">12h00</text><text x="184" y="186">pitches · auditório</text>
  <text x="158" y="198">17h00</text><text x="184" y="198">premiação + encerramento</text>
</g>
</svg>'''


def bleed_diagram():
    """Diagrama de bleed/sangria/área segura."""
    return '''<svg viewBox="0 0 360 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="diagrama de sangria, corte e área segura">
<!-- sangria (vermelho) -->
<rect x="10" y="10" width="340" height="220" fill="#FFB3B3" stroke="#DA1E28" stroke-width="0.5" stroke-dasharray="3 2"/>
<!-- corte (preto) -->
<rect x="20" y="20" width="320" height="200" fill="#F8FCF8" stroke="#3C433C" stroke-width="0.8"/>
<!-- área segura (verde) -->
<rect x="40" y="40" width="280" height="160" fill="none" stroke="#32FA96" stroke-width="0.8" stroke-dasharray="2 2"/>
<!-- conteúdo simulado -->
<text x="60" y="80" font-family="Roboto Flex, sans-serif" font-size="14" font-weight="500" fill="#3C433C">conteúdo importante</text>
<text x="60" y="100" font-family="IBM Plex Mono, monospace" font-size="9" fill="#91938C">fica dentro da área segura</text>
<!-- labels -->
<text x="180" y="20" font-family="IBM Plex Mono, monospace" font-size="9" fill="#DA1E28" text-anchor="middle">sangria · 3mm · vermelho</text>
<text x="350" y="30" font-family="IBM Plex Mono, monospace" font-size="8" fill="#3C433C" text-anchor="end">corte · linha preta</text>
<text x="50" y="220" font-family="IBM Plex Mono, monospace" font-size="8" fill="#32FA96">área segura · 5mm interno</text>
<!-- linhas-guia -->
<line x1="0" y1="120" x2="6" y2="120" stroke="#3C433C" stroke-width="0.5"/>
<line x1="354" y1="120" x2="360" y2="120" stroke="#3C433C" stroke-width="0.5"/>
<line x1="180" y1="0" x2="180" y2="6" stroke="#3C433C" stroke-width="0.5"/>
<line x1="180" y1="234" x2="180" y2="240" stroke="#3C433C" stroke-width="0.5"/>
</svg>'''


# ---------- INDEX -----------------------------------------------------------
IMPRESSOS = [
    ("papelaria", "Papelaria",
     "Identidade institucional: cartões, papel timbrado, envelopes, folders. Materiais formais de identidade corporativa.",
     "documento"),
    ("eventos", "Eventos",
     "Hackathons, oficinas, palestras: crachás, banners, sinalização, convites, programação impressa.",
     "calendar"),
    ("loja", "Loja & merch",
     "Brindes e merchandising: t-shirts, canecas, totebags, adesivos, garrafas, cadernos.",
     "star"),
]

cards = "".join(
    f'<a class="resource-card" href="{slug}.html">'
    f'<div class="meta">impressos</div>'
    f'<h4>{title}</h4><p>{desc}</p>'
    f'<span class="cta">explorar</span></a>'
    for slug, title, desc, _ in IMPRESSOS
)

write("pages/impressos/index.html", page(
    "imp-index", "Impressos",
    '<a href="../../index.html">home</a><span class="sep">/</span>impressos',
    "Diretrizes pra materiais físicos: papelaria, eventos, merchandise. Tokens digitais traduzidos pro impresso, com mockups SVG de cada peça + specs técnicos prontos pra gráfica.",
    "".join([
        sec("library", "biblioteca", "01 · 3 categorias",
            f'<div class="resource-cards">{cards}</div>'),
        sec("bleed", "anatomia · sangria e corte", "02 · referência",
            '<p class="t-body-02 t-secondary mb-05 prose">Todo material impresso tem 3 camadas. Conteúdo fica na área segura · sangria evita corte mostrar bordas brancas · gráficas geralmente pedem 3mm de sangria.</p>'
            + demo(f'<div style="max-width: 480px; margin: 0 auto">{bleed_diagram()}</div>')
            + checklist([
                "Sangria · 3mm além da linha de corte (vermelho)",
                "Linha de corte · borda final do produto (preto)",
                "Área segura · 5mm para dentro do corte (verde)",
                "Conteúdo crítico sempre dentro da área segura",
                "Cor de fundo sempre estende até a sangria",
            ])),
        sec("colors-cmyk", "cores impressas · cmyk + pantone", "03",
            '<p class="t-body-02 t-secondary mb-05 prose">Conversão RGB→CMYK perde saturação · sempre validar prova de cor antes de tiragem grande. Use Pantone pra cores brand críticas em quantidade.</p>'
            + table(["nome","hex (rgb)","cmyk","pantone","gamut"], [
                ["Code Green",   "#32FA96", "C70 M0 Y65 K0",      "802 C",   "✓ aceitável (-15% saturação)"],
                ["Dos",          "#3C433C", "C68 M55 Y65 K59",    "Black 7 C","✓ ideal"],
                ["CSS",          "#F8FCF8", "C5 M0 Y5 K3",        "—",       "✓ ideal"],
                ["Sec Pink",     "#FF9ECF", "C0 M52 Y0 K0",       "230 C",   "⚠ aproximado"],
                ["Sec Blue",     "#B3D9FE", "C32 M10 Y0 K0",      "284 C",   "✓ ideal"],
                ["Purple",       "#AA78E6", "C40 M55 Y0 K0",      "265 C",   "⚠ aproximado"],
                ["Yellow",       "#E8D048", "C8 M15 Y75 K0",      "108 C",   "✓ ideal"],
                ["Script",       "#D79B2E", "C12 M40 Y90 K0",     "138 C",   "✓ ideal"],
            ])),
        sec("brief", "brief pra gráfica · checklist", "04",
            '<p class="t-body-02 t-secondary mb-05 prose">Antes de enviar pra Printi ou qualquer gráfica · checa estes itens pra evitar retrabalho.</p>'
            + checklist([
                "Arquivo em PDF/X-1a:2001 (compatibilidade universal)",
                "Sangria de 3mm em todas as bordas",
                "Linhas-guia (crop marks) ativadas",
                "Todas as fontes convertidas em curvas (outlines)",
                "Cores em CMYK (não RGB) · Pantone só se contratado",
                "Resolução: imagens em 300 dpi mínimo",
                "Preto chapado: C0 M0 Y0 K100 (texto) · C40 M30 Y30 K100 (áreas grandes)",
                "Verniz UV/relevo · em camada separada nomeada 'spot_uv'",
            ])),
        sec("finishes", "acabamentos · catálogo", "05",
            '<p class="t-body-02 t-secondary mb-05 prose">Acabamentos comuns disponíveis na maioria das gráficas brasileiras (Printi, Gráfica Digital, etc).</p>'
            + table(["acabamento","custo","melhor pra","obs"], [
                ["Laminação fosca",     "+",   "Cartão de visita",       "Textura premium, leve, anti-impressão digital"],
                ["Laminação brilho",    "+",   "Folders, capas",         "Mais vibrante, mas mostra digitais"],
                ["Verniz UV total",     "++",  "Capas, convites",        "Brilho intenso, proteção total"],
                ["Verniz UV localizado","+++", "Logo em destaque",       "Brilho só onde aplicado · efeito 'spot'"],
                ["Hot stamping",        "++++","Convites premium",       "Lâmina metálica · só prata/dourado em pequena tiragem"],
                ["Relevo seco/baixo",   "+++", "Logo gravado",           "Sente ao tato · sem cor"],
                ["Corte especial",      "+++", "Tags, etiquetas",        "Faca específica · custo de matriz"],
                ["Furação/serrilha",    "+",   "Talões, tickets",        "Destacável"],
            ])),
        sec("typography", "tipografia em impressos", "06",
            '<p class="t-body-02 t-secondary mb-05 prose">Regras diferem do digital. Letras pequenas + papel barato = ilegível.</p>'
            + table(["uso","tamanho mínimo","fonte","notas"], [
                ["Corpo de texto",  "9pt",  "Roboto Flex 400", "abaixo de 8pt fica difícil"],
                ["Footer / fine print", "7pt",  "Roboto Flex 400", "limite absoluto · só em A4+"],
                ["Cartão de visita",  "8pt",  "IBM Plex Mono",   "tracking +5"],
                ["Título crachá",   "24pt", "Roboto Flex 500", "ler a 2m de distância"],
                ["Banner roll-up",  "120pt", "Roboto Flex 300", "fica grande no real"],
                ["Sinalização A3",  "60pt", "Roboto Flex 500", "ler a 5m de distância"],
            ])),
    ]),
    tags=[{"cls":"tag--code","label":"stable"}, {"cls":"tag--outline","label":"printi-ready"}],
    toc=[
        {"id":"library","label":"Biblioteca"},
        {"id":"bleed","label":"Sangria"},
        {"id":"colors-cmyk","label":"CMYK"},
        {"id":"brief","label":"Brief gráfica"},
        {"id":"finishes","label":"Acabamentos"},
        {"id":"typography","label":"Tipografia"},
    ],
))


# ---------- PAPELARIA ------------------------------------------------------
write("pages/impressos/papelaria.html", page(
    "papelaria", "Papelaria",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">impressos</a><span class="sep">/</span>papelaria',
    "Cartões de visita, papel timbrado, envelopes, folders. Identidade institucional formal · specs prontos pra Printi.",
    "".join([
        sec("mockups", "mockups", "01 · referência visual",
            '<div class="mockup-grid">'
            + mockup(card_business(), "cartão de visita", "90×50mm · frente")
            + mockup(letterhead(), "papel timbrado", "A4 · 210×297mm")
            + mockup(envelope(), "envelope C5", "229×162mm")
            + mockup(folder(), "folder/capa", "A4 dobrado")
            + mockup(notebook(), "caderno A5", "148×210mm · capa")
            + '</div>'),
        sec("specs", "specs técnicos · referência Printi", "02",
            table(["item","tamanho","papel","gramatura","acabamento","prazo médio"], [
                ["cartão de visita","90×50mm",     "Couché ou Triplex","300g",        "laminação fosca","3-5 dias úteis"],
                ["cartão premium",  "90×50mm",     "Couché",            "350g",        "verniz UV localizado no logo","5-7 dias úteis"],
                ["papel timbrado",  "210×297mm",   "Sulfite",           "90g",         "sem acabamento","2-4 dias úteis"],
                ["envelope C5",     "229×162mm",   "Sulfite",           "90g",         "fecho gomado","3-5 dias úteis"],
                ["envelope C6",     "162×114mm",   "Sulfite",           "90g",         "fecho gomado","3-5 dias úteis"],
                ["folder/pasta",    "420×297mm",   "Couché brilho",     "240g",        "verniz UV na capa","5-8 dias úteis"],
                ["caderno A5",      "148×210mm",   "Capa: Couché 300g · miolo: offset 75g","—","wire-o ou costurado","7-10 dias úteis"],
            ])),
        sec("rules", "regras de aplicação", "03",
            do_dont(
                ["H sempre no canto superior esquerdo (cartão) ou centralizado (capa)",
                 "Cor signature CSS (claro) ou Dos (escuro) como fundo · nunca cores secundárias",
                 "Tracking +5 em Plex Mono pra textos pequenos (cartão)",
                 "Margem mínima de 5mm da linha de corte (área segura)",
                 "Endereço completo no rodapé do timbrado"],
                ["Múltiplas cores de fundo no mesmo material",
                 "Fontes diferentes de Roboto Flex + Plex Mono",
                 "Logo abaixo de 8mm de altura (não fica legível)",
                 "Textos críticos dentro da margem de sangria",
                 "Elementos coloridos contra o limite do papel"],
            )),
        sec("anatomy", "anatomia do cartão de visita", "04",
            '<p class="t-body-02 t-secondary mb-05 prose">5 elementos canônicos. Hierarquia clara · informação técnica em mono · nome em Roboto.</p>'
            + demo(f'<div style="max-width: 360px; margin: 0 auto; background: var(--layer-02); padding: var(--spacing-04)">{card_business()}</div>')
            + checklist([
                "Logo H verde (Code) · canto superior esquerdo · 18×18px no SVG = ~9mm impresso",
                "Eyebrow '// produto' · Plex Mono 9pt · cor Java",
                "Nome · Roboto Flex 14pt 500 · cor CSS",
                "Cargo + organização · Plex Mono 10pt · cor Inspect",
                "Email · Plex Mono 9pt · cor Code (destaque)",
            ])),
    ]),
    tags=[{"cls":"tag--code","label":"stable"}],
    toc=[
        {"id":"mockups","label":"Mockups"},
        {"id":"specs","label":"Specs técnicos"},
        {"id":"rules","label":"Regras"},
        {"id":"anatomy","label":"Anatomia cartão"},
    ],
))


# ---------- EVENTOS --------------------------------------------------------
write("pages/impressos/eventos.html", page(
    "eventos", "Eventos",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">impressos</a><span class="sep">/</span>eventos',
    "Hackathons, oficinas, palestras. Crachás identificáveis, banners legíveis, sinalização clara.",
    "".join([
        sec("mockups", "mockups", "01 · referência visual",
            '<div class="mockup-grid">'
            + mockup(badge_event(), "crachá", "90×130mm · cordão verde")
            + mockup(banner_rollup(), "banner roll-up", "850×2000mm")
            + mockup(signage(), "sinalização A3", "297×420mm · setas")
            + mockup(invite(), "save the date", "100×150mm")
            + mockup(program(), "programação A5", "148×210mm dobrado")
            + '</div>'),
        sec("specs", "specs técnicos · referência Printi", "02",
            table(["item","tamanho","papel/material","acabamento","custo médio (50un)"], [
                ["crachá",         "90×130mm",   "PVC ou couché 250g + cordão", "envelopinho transparente", "R$ 4-8 / un"],
                ["banner roll-up", "850×2000mm", "Lona front 440g",              "estrutura retrátil",       "R$ 280-450 / un"],
                ["sinalização A3", "297×420mm",  "Foamboard 5mm ou PVC 3mm",     "impressão UV direta",      "R$ 35-65 / un"],
                ["programação A5", "148×210mm",  "Couché 150g brilho",           "dobra ao meio",            "R$ 1-2 / un"],
                ["convite/STD",    "100×150mm",  "Couché 300g fosco",            "verniz UV opcional",       "R$ 1.5-3 / un"],
                ["adesivo",        "50×50mm",    "Vinil branco fosco",           "corte na faca",            "R$ 0.5-1 / un"],
                ["painel palco",   "3000×3000mm","Lona front 440g",              "ilhós nos cantos",         "R$ 850-1400 / un"],
            ])),
        sec("badges", "regras de crachá", "03",
            '<p class="t-body-02 t-secondary mb-05 prose">Crachá precisa identificar a pessoa a 2m de distância · cor da fita codifica a função.</p>'
            + demo(f'<div style="max-width: 200px; margin: 0 auto">{badge_event()}</div>')
            + table(["função","cor da fita","cor do header","exemplo"], [
                ["Participante","verde (Code)","verde (Code) sobre CSS","maioria"],
                ["Staff",       "dos (escuro)","dos sobre CSS",         "organização"],
                ["Palestrante", "roxo (Purple)","roxo sobre CSS",       "speakers, mentores"],
                ["Patrocinador","amarelo (Yellow)","amarelo sobre Dos", "parceiros, sponsors"],
                ["Imprensa",    "azul (Sec Blue)","azul sobre CSS",     "jornalistas"],
            ])),
        sec("banners", "banners e painéis", "04",
            do_dont(
                ["1 mensagem-chave central + 1-2 metadados (data, local, url)",
                 "Hierarquia tipográfica clara · título 4× maior que body",
                 "H ou logo do programa visível em pelo menos 1 lugar",
                 "Grafismo de fundo com opacity 0.1-0.15 · não compete com texto",
                 "Texto sempre dentro da área segura (5mm)",
                 "Cor dominante consistente com a identidade do evento"],
                ["Encher de texto · banner não é folder",
                 "Múltiplos call-to-actions (1 url no máximo)",
                 "Cores não-brand · seguir paleta Casa Hacker",
                 "Fontes diferentes das oficiais (Roboto Flex, Plex Mono)",
                 "Elementos críticos perto das bordas (corte os pega)",
                 "QR code muito pequeno · mínimo 30×30mm pra ler"],
            )),
    ]),
    tags=[{"cls":"tag--code","label":"stable"}],
    toc=[
        {"id":"mockups","label":"Mockups"},
        {"id":"specs","label":"Specs técnicos"},
        {"id":"badges","label":"Crachás"},
        {"id":"banners","label":"Banners"},
    ],
))


# ---------- LOJA -----------------------------------------------------------
write("pages/impressos/loja.html", page(
    "loja", "Loja & merch",
    '<a href="../../index.html">home</a><span class="sep">/</span><a href="index.html">impressos</a><span class="sep">/</span>loja & merch',
    "Brindes e merchandising: t-shirts, canecas, totebags, adesivos, garrafas, cadernos. Identidade lúdica mantendo coerência.",
    "".join([
        sec("mockups", "produtos", "01 · referência visual",
            '<div class="mockup-grid">'
            + mockup(tshirt(), "t-shirt", "estampa 200×280mm peito")
            + mockup(mug(), "caneca", "200×80mm wrap · 325ml")
            + mockup(tote_bag(), "tote bag", "380×420mm · algodão")
            + mockup(sticker(), "sticker redondo", "75mm vinil")
            + mockup(water_bottle(), "garrafa térmica", "500ml inox")
            + mockup(notebook(), "caderno A5", "148×210mm capa")
            + '</div>'),
        sec("specs", "specs técnicos · referência Printi/Yampi", "02",
            table(["produto","material","área impressa","técnica","tiragem mínima"], [
                ["t-shirt",         "algodão 100% · 180g",      "300×400mm (A3)",      "serigrafia ou DTF",   "20un"],
                ["caneca cerâmica", "branca · 325ml",           "200×80mm (wrap)",     "sublimação",          "10un"],
                ["caneca dos",      "preta · 325ml",            "200×80mm (wrap)",     "laser engraving",     "20un"],
                ["tote bag",        "algodão cru · 100% bege",  "200×250mm centro",    "serigrafia ou DTF",   "30un"],
                ["sticker round",   "vinil branco fosco",       "75mm Ø",              "impressão digital + corte", "100un"],
                ["sticker quad.",   "vinil branco fosco",       "50×50mm",             "impressão digital + corte", "100un"],
                ["garrafa térmica", "inox 500ml",               "200×80mm (rótulo)",   "vinil ou laser",      "10un"],
                ["caderno wire-o",  "capa couché 300g · A5",    "148×210mm capa",      "impressão offset",    "30un"],
                ["caderno couro",   "capa couro sintético · A5","branco/preto · gravado", "laser engraving",    "10un"],
            ])),
        sec("rules", "regras de aplicação", "03",
            checklist([
                "H sempre alinhado ao grid · sem rotação livre",
                "Apenas paleta brand (Code, Dos, Console, Purple, Pink, Yellow) — nada de cores aleatórias",
                "Logo mínimo 30mm de altura em produto físico",
                "Composições novas seguem padrões de grafismo existentes (assets/grafismos/)",
                "Sem efeitos de impressão que distorçam a identidade (drop shadow, gradientes)",
                "Em produtos pequenos (sticker), preferir versão mono do logo",
                "Versão clara do logo (Code sobre Dos) em produtos escuros",
                "Versão escura (Dos sobre claro) em produtos brancos/CSS",
            ])),
        sec("submarcas", "merch das submarcas", "04",
            '<p class="t-body-02 t-secondary mb-05 prose">Cada submarca pode ter merch próprio mantendo sua cor signature. Padrão visual herda do CHDS · varia só a cor + grafismo de fundo.</p>'
            + table(["submarca","cor signature","exemplo de aplicação"], [
                ["Hackerclubes",    "Sec Blue",     "T-shirt azul-claro · sticker com H verde"],
                ["Inclusão Tech",   "Sec Green Light","Tote bag verde claríssimo · caderno com manifesto"],
                ["Internet Segura", "Yellow",       "Caneca amarela · sticker do escudo + slogan"],
                ["Minas em Tech",   "Pink",         "Camiseta pink · caderno feminino · botton"],
                ["Mão na Massa",    "Script Orange","T-shirt cinza com print laranja · adesivo industrial"],
                ["PerifaImpacto",   "Purple",       "T-shirt roxa · sticker com símbolo · garrafa preta"],
            ])),
        sec("checklist", "checklist antes de mandar pra produção", "05",
            checklist([
                "Arquivo em PDF/X-1a com sangria de 3mm",
                "Todas as fontes em curvas (outline)",
                "CMYK validado (não RGB)",
                "Cor crítica em Pantone (se quantidade >50un)",
                "Resolução 300dpi pra raster · vetor pra logo sempre",
                "Cor branca em camada separada (pra serigrafia)",
                "Mockup aprovado pelo cliente",
                "Confirmação do tamanho final (cm × cm)",
                "Quantidade · prazo · forma de entrega definidos",
            ])),
    ]),
    tags=[{"cls":"tag--code","label":"stable"}],
    toc=[
        {"id":"mockups","label":"Mockups"},
        {"id":"specs","label":"Specs técnicos"},
        {"id":"rules","label":"Regras"},
        {"id":"submarcas","label":"Submarcas merch"},
        {"id":"checklist","label":"Checklist produção"},
    ],
))

print("done · impressos (4 pages)")
