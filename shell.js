/* =============================================================================
   CASA HACKER DS · Shell injection (v1.0)
   ─────────────────────────────────────────────────────────────────────────────
   - Injeta header, sidebar, footer
   - Nav config com seções colapsáveis (estado persistido em localStorage)
   - Theme toggle com prefers-color-scheme inicial
   - Auto-TOC com scrollspy quando há section[id] na página
   - Skip-link de a11y
   - Atalhos de teclado: "/" foca busca · "g h" home
   - Meta description / OG default
   ============================================================================= */
(function () {
  'use strict';

  const $ = (sel, root) => (root || document).querySelector(sel);
  const $$ = (sel, root) => Array.from((root || document).querySelectorAll(sel));

  const pageId = $('meta[name="ch-page"]')?.content || '';
  const base = $('meta[name="ch-base"]')?.content || './';

  /* --------------------------------------------------------------------- */
  /*  NAV CONFIG                                                            */
  /* --------------------------------------------------------------------- */
  const navConfig = [
    { id: 'about', section: 'sobre o sistema', items: [
      { id: 'home',         label: 'visão geral',         href: 'index.html' },
      { id: 'about',        label: 'sobre o sistema',     href: 'pages/about/index.html' },
      { id: 'principles',   label: 'princípios',          href: 'pages/about/principles.html' },
      { id: 'who-uses',     label: 'quem usa',            href: 'pages/about/who-uses.html' },
      { id: 'ecosystem',    label: 'ecossistema',         href: 'pages/about/ecosystem.html' },
    ]},
    { id: 'guidelines', section: 'guidelines', items: [
      { id: 'g-overview',   label: 'overview',            href: 'pages/guidelines/index.html' },
      { id: 'g-a11y',       label: 'accessibility',       href: 'pages/guidelines/accessibility.html' },
      { id: 'g-content',    label: 'content & voice',     href: 'pages/guidelines/content.html' },
      { id: 'g-ai',         label: 'casa hacker for ai',  href: 'pages/guidelines/ai.html' },
    ]},
    { id: 'foundation', section: 'foundations', items: [
      { id: 'color',        label: 'color',               href: 'pages/elements/color.html' },
      { id: 'typography',   label: 'typography',          href: 'pages/elements/typography.html' },
      { id: 'spacing',      label: 'spacing · bit',       href: 'pages/elements/spacing.html' },
      { id: 'grid',         label: '2x grid',             href: 'pages/elements/grid.html' },
      { id: 'iconography',  label: 'iconography',         href: 'pages/elements/iconography.html' },
      { id: 'motion',       label: 'motion',              href: 'pages/elements/motion.html' },
      { id: 'themes',       label: 'themes',              href: 'pages/elements/themes.html' },
    ]},
    { id: 'components', section: 'components', items: [
      { id: 'comp-index',   label: 'overview',            href: 'pages/components/index.html' },
      { id: 'accordion',    label: 'accordion',           href: 'pages/components/accordion.html' },
      { id: 'breadcrumb',   label: 'breadcrumb',          href: 'pages/components/breadcrumb.html' },
      { id: 'button',       label: 'button',              href: 'pages/components/button.html' },
      { id: 'checkbox',     label: 'checkbox',            href: 'pages/components/checkbox.html' },
      { id: 'code-snippet', label: 'code snippet',        href: 'pages/components/code-snippet.html' },
      { id: 'data-table',   label: 'data table',          href: 'pages/components/data-table.html' },
      { id: 'dropdown',     label: 'dropdown',            href: 'pages/components/dropdown.html' },
      { id: 'form',         label: 'form',                href: 'pages/components/form.html' },
      { id: 'link',         label: 'link',                href: 'pages/components/link.html' },
      { id: 'loading',      label: 'loading',             href: 'pages/components/loading.html' },
      { id: 'modal',        label: 'modal',               href: 'pages/components/modal.html' },
      { id: 'notification', label: 'notification',        href: 'pages/components/notification.html' },
      { id: 'pagination',   label: 'pagination',          href: 'pages/components/pagination.html' },
      { id: 'radio-button', label: 'radio button',        href: 'pages/components/radio-button.html' },
      { id: 'search',       label: 'search',              href: 'pages/components/search.html' },
      { id: 'tabs',         label: 'tabs',                href: 'pages/components/tabs.html' },
      { id: 'tag',          label: 'tag',                 href: 'pages/components/tag.html' },
      { id: 'text-input',   label: 'text input',          href: 'pages/components/text-input.html' },
      { id: 'tile',         label: 'tile',                href: 'pages/components/tile.html' },
      { id: 'tooltip',      label: 'tooltip',             href: 'pages/components/tooltip.html' },
      { id: 'ui-shell',     label: 'ui shell',            href: 'pages/components/ui-shell.html' },
    ]},
    { id: 'patterns', section: 'patterns', items: [
      { id: 'pat-overview', label: 'overview',            href: 'pages/patterns/index.html' },
      { id: 'bit-system',   label: 'bit modular',         href: 'pages/patterns/bit-system.html' },
      { id: 'colored-symbol', label: 'colored symbol',    href: 'pages/patterns/colored-symbol.html' },
      { id: 'grafismos',    label: 'grafismos',           href: 'pages/patterns/grafismos.html' },
      { id: 'forms-pat',    label: 'forms',               href: 'pages/patterns/forms-pattern.html' },
      { id: 'dialogs',      label: 'dialogs',             href: 'pages/patterns/dialogs.html' },
      { id: 'empty-states', label: 'empty states',        href: 'pages/patterns/empty-states.html' },
      { id: 'login',        label: 'login',               href: 'pages/patterns/login.html' },
      { id: 'global-header',label: 'global header',       href: 'pages/patterns/global-header.html' },
      { id: 'status',       label: 'status indicators',   href: 'pages/patterns/status-indicators.html' },
    ]},
    { id: 'dataviz', section: 'data visualization', items: [
      { id: 'dv-overview',     label: 'overview',          href: 'pages/dataviz/index.html' },
      { id: 'dv-anatomy',      label: 'chart anatomy',     href: 'pages/dataviz/anatomy.html' },
      { id: 'dv-types',        label: 'chart types',       href: 'pages/dataviz/types.html' },
      { id: 'dv-colors',       label: 'color palettes',    href: 'pages/dataviz/colors.html' },
      { id: 'dv-labels',       label: 'labels & axes',     href: 'pages/dataviz/labels.html' },
      { id: 'dv-interaction',  label: 'interaction',       href: 'pages/dataviz/interaction.html' },
      { id: 'dv-accessibility',label: 'accessibility',     href: 'pages/dataviz/accessibility.html' },
      { id: 'dv-examples',     label: 'examples',          href: 'pages/dataviz/examples.html' },
    ]},
    { id: 'submarcas', section: 'submarcas', items: [
      { id: 'sub-index',       label: 'visão geral',      href: 'pages/submarcas/index.html' },
      { id: 'hackerclubes',    label: 'hacker/clubes',    href: 'pages/submarcas/hackerclubes.html' },
      { id: 'inclusao-tech',   label: 'inclusão/tech',    href: 'pages/submarcas/inclusao-tech.html' },
      { id: 'minas-em-tech',   label: 'minas/em tech',    href: 'pages/submarcas/minas-em-tech.html' },
      { id: 'mao-na-massa',    label: 'mão/na massa',     href: 'pages/submarcas/mao-na-massa.html' },
      { id: 'perifa-impacto',  label: 'perifa/impacto',   href: 'pages/submarcas/perifa-impacto.html' },
    ]},
    { id: 'impressos', section: 'impressos', items: [
      { id: 'imp-index',    label: 'overview',            href: 'pages/impressos/index.html' },
      { id: 'papelaria',    label: 'papelaria',           href: 'pages/impressos/papelaria.html' },
      { id: 'eventos',      label: 'eventos',             href: 'pages/impressos/eventos.html' },
      { id: 'loja',         label: 'loja & merch',        href: 'pages/impressos/loja.html' },
    ]},
    { id: 'contributing', section: 'contributing', items: [
      { id: 'contrib-start',label: 'get started',         href: 'pages/contributing/index.html' },
      { id: 'checklist',    label: 'component checklist', href: 'pages/contributing/checklist.html' },
      { id: 'pdlc',         label: 'lifecycle',           href: 'pages/contributing/pdlc.html' },
      { id: 'docs-guide',   label: 'documentation',       href: 'pages/contributing/documentation.html' },
    ]},
    { id: 'help', section: 'help', items: [
      { id: 'help-contact', label: 'contato',             href: 'pages/help/index.html' },
      { id: 'help-faq',     label: 'faq',                 href: 'pages/help/faq.html' },
    ]},
  ];

  /* --------------------------------------------------------------------- */
  /*  THEME · prefers-color-scheme as default                               */
  /* --------------------------------------------------------------------- */
  (function applyInitialTheme() {
    try {
      const saved = localStorage.getItem('chds-theme');
      if (saved === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
      else if (saved === 'light') document.documentElement.removeAttribute('data-theme');
      else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-theme', 'dark');
      }
    } catch (e) {}
  })();

  /* --------------------------------------------------------------------- */
  /*  HEAD · meta tags padrão (apenas se não definidos na página)           */
  /* --------------------------------------------------------------------- */
  (function ensureMetas() {
    const head = document.head;
    const ensureMeta = (name, content) => {
      if (head.querySelector(`meta[name="${name}"]`)) return;
      const m = document.createElement('meta');
      m.name = name; m.content = content;
      head.appendChild(m);
    };
    const ensureProp = (prop, content) => {
      if (head.querySelector(`meta[property="${prop}"]`)) return;
      const m = document.createElement('meta');
      m.setAttribute('property', prop); m.content = content;
      head.appendChild(m);
    };
    const title = document.title || 'Casa Hacker DS';
    ensureMeta('description', 'Casa Hacker Design System — forked from IBM Carbon e reskinned com a identidade Casa Hacker.');
    ensureMeta('theme-color', '#3C433C');
    ensureProp('og:title', title);
    ensureProp('og:type', 'website');
    ensureProp('og:description', 'Casa Hacker Design System — sistema de design completo: tokens, componentes, padrões, submarcas e impressos.');
    if (!head.querySelector('link[rel="icon"]')) {
      const link = document.createElement('link');
      link.rel = 'icon';
      link.type = 'image/svg+xml';
      link.href = base + 'favicon.svg';
      head.appendChild(link);
    }
    if (!head.querySelector('link[rel="manifest"]')) {
      const m = document.createElement('link');
      m.rel = 'manifest';
      m.href = base + 'manifest.webmanifest';
      head.appendChild(m);
    }
  })();

  /* --------------------------------------------------------------------- */
  /*  SERVICE WORKER · offline + caching                                    */
  /* --------------------------------------------------------------------- */
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register(base + 'sw.js', { scope: base })
        .catch(err => console.warn('[chds] sw registration failed:', err));
    });
  }

  /* --------------------------------------------------------------------- */
  /*  ACCESSIBILITY BAR · obrigatória em produtos Casa Hacker               */
  /*  Carrega via CDN (https://github.com/casahacker/barra-acessibilidade)  */
  /* --------------------------------------------------------------------- */
  (function loadA11yBar() {
    if (document.querySelector('#chds-a11y-bar-css')) return;
    const ver = 'v0.1.0';
    const cssBase = `https://cdn.jsdelivr.net/gh/casahacker/barra-acessibilidade@${ver}/packages/standalone/dist`;
    const css = document.createElement('link');
    css.id = 'chds-a11y-bar-css';
    css.rel = 'stylesheet';
    css.href = `${cssBase}/bar.css`;
    document.head.appendChild(css);
    const js = document.createElement('script');
    js.src = `${cssBase}/bar.iife.js`;
    js.defer = true;
    js.setAttribute('data-auto', 'true');
    document.head.appendChild(js);
  })();

  /* --------------------------------------------------------------------- */
  /*  HEADER + SKIP LINK                                                    */
  /* --------------------------------------------------------------------- */
  const H_SYMBOL = `<span class="on"></span><span></span><span class="on"></span>
                    <span></span><span class="on"></span><span class="on"></span>
                    <span class="on"></span><span></span><span class="on"></span>`;

  document.body.insertAdjacentHTML('afterbegin', `
    <a class="skip-link" href="#main-content">pular para conteúdo</a>
    <header class="shell-header" role="banner">
      <button class="menu-toggle" id="menuToggle" aria-label="abrir menu" aria-controls="sidebar" aria-expanded="false">☰</button>
      <a href="${base}index.html" class="shell-brand" aria-label="Casa Hacker Design System — home">
        <div class="h-mini" aria-hidden="true">${H_SYMBOL}</div>
        <span class="shell-brand-name">casa hacker<span class="ds">/ ds v1.0</span></span>
      </a>
      <nav class="shell-actions" aria-label="links secundários">
        <a href="${base}index.html" class="shell-link optional-mobile">home</a>
        <a href="${base}pages/about/index.html" class="shell-link optional-mobile">sobre</a>
        <button class="shell-theme-toggle" id="themeToggle" type="button" aria-label="alternar tema claro/escuro" aria-pressed="false">
          <svg class="theme-icon theme-icon--sun" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><circle cx="8" cy="8" r="3"/><g stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><line x1="8" y1="1" x2="8" y2="3"/><line x1="8" y1="13" x2="8" y2="15"/><line x1="1" y1="8" x2="3" y2="8"/><line x1="13" y1="8" x2="15" y2="8"/><line x1="3" y1="3" x2="4.5" y2="4.5"/><line x1="11.5" y1="11.5" x2="13" y2="13"/><line x1="13" y1="3" x2="11.5" y2="4.5"/><line x1="4.5" y1="11.5" x2="3" y2="13"/></g></svg>
          <svg class="theme-icon theme-icon--moon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M14 9.5A6 6 0 0 1 6.5 2a6 6 0 1 0 7.5 7.5z"/></svg>
        </button>
        <a href="https://github.com/casahacker/design-system" target="_blank" rel="noopener noreferrer" class="shell-link">github ↗</a>
      </nav>
    </header>
  `);

  /* --------------------------------------------------------------------- */
  /*  SIDEBAR with collapsible sections                                     */
  /* --------------------------------------------------------------------- */
  const collapsedState = (() => {
    try { return JSON.parse(localStorage.getItem('chds-nav-collapsed') || '{}'); }
    catch (e) { return {}; }
  })();

  // Determine which section contains the active page; force-expand it
  let activeSectionId = null;
  for (const sec of navConfig) {
    if (sec.items.some(i => i.id === pageId)) { activeSectionId = sec.id; break; }
  }

  // Collapse all non-active sections by default on first visit
  for (const sec of navConfig) {
    if (!(sec.id in collapsedState)) {
      collapsedState[sec.id] = sec.id !== activeSectionId;
    }
  }
  collapsedState[activeSectionId] = false;

  const sidebarHTML = `
    <aside class="sidebar" id="sidebar" role="navigation" aria-label="navegação primária">
      <div class="sidebar-search-wrap">
        <input type="search" class="sidebar-search" placeholder="// buscar..." id="sidebarSearch" aria-label="buscar na navegação">
        <span class="sidebar-search-kbd" aria-hidden="true">/</span>
      </div>
      ${navConfig.map(s => `
        <div class="nav-section ${collapsedState[s.id] ? 'collapsed' : ''}" data-section-id="${s.id}">
          <button class="nav-section-toggle" aria-expanded="${!collapsedState[s.id]}" aria-controls="nav-items-${s.id}">
            <span>${s.section}</span>
            <span class="chevron" aria-hidden="true">▼</span>
          </button>
          <div class="nav-section-items" id="nav-items-${s.id}">
            ${s.items.map(item => `
              <a href="${base}${item.href}" data-id="${item.id}" class="${item.id === pageId ? 'active' : ''}" ${item.id === pageId ? 'aria-current="page"' : ''}>
                <span>${item.label}</span>
              </a>
            `).join('')}
          </div>
        </div>
      `).join('')}
    </aside>
    <div class="sidebar-backdrop" id="sidebarBackdrop"></div>
  `;

  const main = $('main.main') || $('.main');
  if (main) {
    main.id = main.id || 'main-content';
    main.setAttribute('role', 'main');
    main.setAttribute('tabindex', '-1');
    const wrapper = document.createElement('div');
    wrapper.className = 'shell-container';
    main.parentNode.insertBefore(wrapper, main);
    wrapper.insertAdjacentHTML('afterbegin', sidebarHTML);
    wrapper.appendChild(main);
    main.insertAdjacentHTML('beforeend', `
      <footer class="shell-footer" role="contentinfo">
        <span class="left">casa hacker design system · v1.0 · forked from ibm carbon</span>
        <span class="right">
          <a href="${base}pages/help/index.html">help</a> ·
          <a href="${base}pages/contributing/index.html">contribuir</a> ·
          made with ◆ in br
        </span>
      </footer>
    `);
  }

  /* --------------------------------------------------------------------- */
  /*  THEME TOGGLE (in header)                                              */
  /* --------------------------------------------------------------------- */
  const themeBtn = document.getElementById('themeToggle');
  const reflectTheme = () => {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    themeBtn?.setAttribute('aria-pressed', String(isDark));
  };
  reflectTheme();
  themeBtn?.addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme');
    if (cur === 'dark') {
      document.documentElement.removeAttribute('data-theme');
      try { localStorage.setItem('chds-theme', 'light'); } catch (e) {}
    } else {
      document.documentElement.setAttribute('data-theme', 'dark');
      try { localStorage.setItem('chds-theme', 'dark'); } catch (e) {}
    }
    reflectTheme();
  });

  /* --------------------------------------------------------------------- */
  /*  PREV / NEXT navigation in footer                                      */
  /* --------------------------------------------------------------------- */
  (function injectPrevNext() {
    if (!main) return;
    const flat = [];
    navConfig.forEach(s => s.items.forEach(i => flat.push(i)));
    const idx = flat.findIndex(i => i.id === pageId);
    if (idx < 0) return;
    const prev = flat[idx - 1];
    const next = flat[idx + 1];
    if (!prev && !next) return;
    const html = `
      <nav class="page-nav" aria-label="navegação entre páginas">
        ${prev ? `<a class="page-nav-link page-nav-prev" href="${base}${prev.href}">
          <span class="page-nav-label">← anterior</span>
          <span class="page-nav-title">${prev.label}</span>
        </a>` : '<span></span>'}
        ${next ? `<a class="page-nav-link page-nav-next" href="${base}${next.href}">
          <span class="page-nav-label">próximo →</span>
          <span class="page-nav-title">${next.label}</span>
        </a>` : '<span></span>'}
      </nav>`;
    const footer = main.querySelector('.shell-footer');
    if (footer) footer.insertAdjacentHTML('beforebegin', html);
    else main.insertAdjacentHTML('beforeend', html);
  })();

  /* --------------------------------------------------------------------- */
  /*  BACK TO TOP button (visible on scroll > 600)                          */
  /* --------------------------------------------------------------------- */
  (function backToTop() {
    const btn = document.createElement('button');
    btn.className = 'back-to-top';
    btn.type = 'button';
    btn.setAttribute('aria-label', 'voltar ao topo');
    btn.innerHTML = '↑';
    document.body.appendChild(btn);
    const onScroll = () => btn.classList.toggle('visible', window.scrollY > 600);
    window.addEventListener('scroll', onScroll, { passive: true });
    btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    onScroll();
  })();

  /* --------------------------------------------------------------------- */
  /*  Sidebar — section collapse                                            */
  /* --------------------------------------------------------------------- */
  $$('.nav-section-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const sec = btn.closest('.nav-section');
      const id = sec.dataset.sectionId;
      const willCollapse = !sec.classList.contains('collapsed');
      sec.classList.toggle('collapsed', willCollapse);
      btn.setAttribute('aria-expanded', String(!willCollapse));
      collapsedState[id] = willCollapse;
      try { localStorage.setItem('chds-nav-collapsed', JSON.stringify(collapsedState)); } catch (e) {}
    });
  });

  /* --------------------------------------------------------------------- */
  /*  Mobile menu                                                           */
  /* --------------------------------------------------------------------- */
  const menuToggle = $('#menuToggle');
  const sidebar = $('#sidebar');
  const backdrop = $('#sidebarBackdrop');
  const closeMenu = () => {
    sidebar?.classList.remove('open');
    backdrop?.classList.remove('open');
    menuToggle?.setAttribute('aria-expanded', 'false');
  };
  menuToggle?.addEventListener('click', () => {
    const willOpen = !sidebar.classList.contains('open');
    sidebar.classList.toggle('open', willOpen);
    backdrop.classList.toggle('open', willOpen);
    menuToggle.setAttribute('aria-expanded', String(willOpen));
  });
  backdrop?.addEventListener('click', closeMenu);
  $$('.sidebar a').forEach(a => a.addEventListener('click', closeMenu));

  /* --------------------------------------------------------------------- */
  /*  Sidebar search · filter + hide empty sections                         */
  /* --------------------------------------------------------------------- */
  const search = $('#sidebarSearch');
  if (search) {
    search.addEventListener('input', e => {
      const q = e.target.value.toLowerCase().trim();
      $$('.nav-section').forEach(s => {
        let anyMatch = false;
        $$('a', s).forEach(a => {
          const match = !q || a.textContent.toLowerCase().includes(q);
          a.style.display = match ? '' : 'none';
          if (match) anyMatch = true;
        });
        s.style.display = anyMatch ? '' : 'none';
        if (q) s.classList.remove('collapsed');
      });
    });
  }

  /* --------------------------------------------------------------------- */
  /*  Keyboard shortcuts: "/" focus search, "Esc" close menu                */
  /* --------------------------------------------------------------------- */
  document.addEventListener('keydown', e => {
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
      e.preventDefault();
      search?.focus();
    }
    if (e.key === 'Escape') {
      if (sidebar?.classList.contains('open')) closeMenu();
    }
  });

  /* --------------------------------------------------------------------- */
  /*  Auto-TOC · if container .toc[data-auto] exists                        */
  /* --------------------------------------------------------------------- */
  const autoTOC = $('.toc[data-auto]');
  if (autoTOC) {
    const ol = autoTOC.querySelector('ol') || (() => {
      const o = document.createElement('ol');
      autoTOC.appendChild(o);
      return o;
    })();
    ol.innerHTML = '';
    $$('section.section[id]').forEach(s => {
      const h = $('h2', s);
      if (!h) return;
      const li = document.createElement('li');
      li.innerHTML = `<a href="#${s.id}">${h.textContent.trim()}</a>`;
      ol.appendChild(li);
    });
  }

  /* --------------------------------------------------------------------- */
  /*  TOC scrollspy · marca o link da seção atual                           */
  /* --------------------------------------------------------------------- */
  (function tocSpy() {
    const tocLinks = $$('.toc a[href^="#"]');
    if (!tocLinks.length) return;
    const sections = tocLinks
      .map(a => document.getElementById(a.getAttribute('href').slice(1)))
      .filter(Boolean);
    if (!sections.length || !('IntersectionObserver' in window)) return;

    const linkByID = new Map(tocLinks.map(a => [a.getAttribute('href').slice(1), a]));
    let lastActive = null;
    const setActive = (id) => {
      if (lastActive === id) return;
      tocLinks.forEach(a => a.classList.remove('toc-active'));
      const link = linkByID.get(id);
      if (link) link.classList.add('toc-active');
      lastActive = id;
    };

    const io = new IntersectionObserver((entries) => {
      // Pega a seção mais visível
      const visible = entries
        .filter(e => e.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio);
      if (visible.length) setActive(visible[0].target.id);
    }, {
      rootMargin: '-100px 0px -60% 0px',
      threshold: [0, 0.5, 1],
    });

    sections.forEach(s => io.observe(s));
  })();

  /* --------------------------------------------------------------------- */
  /*  Smooth in-page scroll (offset-aware)                                  */
  /* --------------------------------------------------------------------- */
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const id = a.getAttribute('href').slice(1);
    if (!id) return;
    const target = document.getElementById(id);
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
  });

  /* --------------------------------------------------------------------- */
  /*  Code snippet — copy button                                            */
  /* --------------------------------------------------------------------- */
  $$('.code-snippet').forEach(snippet => {
    if (snippet.querySelector('.code-copy')) return;
    const btn = document.createElement('button');
    btn.className = 'code-copy';
    btn.type = 'button';
    btn.textContent = 'copy';
    btn.setAttribute('aria-label', 'copiar código');
    btn.addEventListener('click', async () => {
      const text = snippet.textContent.replace(/copy$/i, '').trim();
      try {
        await navigator.clipboard.writeText(text);
        btn.textContent = 'copied!';
        btn.classList.add('is-copied');
        setTimeout(() => { btn.textContent = 'copy'; btn.classList.remove('is-copied'); }, 1500);
      } catch (err) {
        btn.textContent = 'erro';
        setTimeout(() => { btn.textContent = 'copy'; }, 1500);
      }
    });
    snippet.appendChild(btn);
  });

  /* --------------------------------------------------------------------- */
  /*  Scroll active section in nav into view                                */
  /* --------------------------------------------------------------------- */
  const activeLink = $('.nav-section a.active');
  if (activeLink) {
    setTimeout(() => {
      activeLink.scrollIntoView({ block: 'center', behavior: 'auto' });
    }, 50);
  }
})();
