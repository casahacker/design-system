/* =============================================================================
   CASA HACKER DS · Interactive components (v1.0)
   ─────────────────────────────────────────────────────────────────────────────
   Componentes JS vanilla:
   - Accordion       (single | multi)
   - Tabs            (com setas, Home/End)
   - Modal           (focus trap, Esc, click backdrop)
   - Dropdown        (Listbox ARIA, setas, Esc)
   - Notification    (dismiss, auto-timeout)
   - Toast           (notify global)

   API:
   Inicializa automaticamente em DOMContentLoaded. Também expõe `window.CHDS`
   com métodos imperativos.
   ============================================================================= */
(function () {
  'use strict';

  const $ = (sel, root) => (root || document).querySelector(sel);
  const $$ = (sel, root) => Array.from((root || document).querySelectorAll(sel));

  const focusableSelector = 'a[href], button:not([disabled]), textarea, input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])';

  /* --------------------------------------------------------------------- */
  /*  ACCORDION                                                             */
  /* --------------------------------------------------------------------- */
  function initAccordion(root) {
    const mode = root.dataset.mode || 'single';   // single | multi
    const headers = $$('.accordion-header', root);
    headers.forEach(btn => {
      const item = btn.closest('.accordion-item');
      btn.setAttribute('aria-expanded', item.classList.contains('open') ? 'true' : 'false');
      btn.addEventListener('click', () => {
        const open = item.classList.contains('open');
        if (mode === 'single' && !open) {
          $$('.accordion-item.open', root).forEach(other => {
            other.classList.remove('open');
            $('.accordion-header', other)?.setAttribute('aria-expanded', 'false');
          });
        }
        item.classList.toggle('open', !open);
        btn.setAttribute('aria-expanded', String(!open));
      });
    });
  }

  /* --------------------------------------------------------------------- */
  /*  TABS                                                                   */
  /* --------------------------------------------------------------------- */
  function initTabs(root) {
    const tabs = $$('[role="tab"]', root);
    const panels = $$('[role="tabpanel"]', root.parentNode);
    if (!tabs.length) return;

    const activate = (idx, focus = true) => {
      tabs.forEach((t, i) => {
        const sel = i === idx;
        t.classList.toggle('active', sel);
        t.setAttribute('aria-selected', String(sel));
        t.setAttribute('tabindex', sel ? '0' : '-1');
      });
      panels.forEach((p, i) => {
        const id = tabs[i]?.getAttribute('aria-controls');
        if (!id) return;
        const target = document.getElementById(id);
        if (!target) return;
        target.hidden = i !== idx;
      });
      if (focus) tabs[idx].focus();
    };

    tabs.forEach((tab, i) => {
      tab.addEventListener('click', () => activate(i));
      tab.addEventListener('keydown', e => {
        if (e.key === 'ArrowRight') { e.preventDefault(); activate((i + 1) % tabs.length); }
        if (e.key === 'ArrowLeft')  { e.preventDefault(); activate((i - 1 + tabs.length) % tabs.length); }
        if (e.key === 'Home')       { e.preventDefault(); activate(0); }
        if (e.key === 'End')        { e.preventDefault(); activate(tabs.length - 1); }
      });
    });
    // Initial active
    const initial = tabs.findIndex(t => t.classList.contains('active'));
    activate(initial >= 0 ? initial : 0, false);
  }

  /* --------------------------------------------------------------------- */
  /*  MODAL                                                                  */
  /* --------------------------------------------------------------------- */
  let savedFocus = null;
  function openModal(modalEl) {
    if (!modalEl) return;
    savedFocus = document.activeElement;
    modalEl.classList.add('open');
    modalEl.setAttribute('aria-hidden', 'false');
    const focusable = $$(focusableSelector, modalEl);
    (focusable[0] || modalEl).focus();
    document.body.style.overflow = 'hidden';
  }
  function closeModal(modalEl) {
    if (!modalEl) return;
    modalEl.classList.remove('open');
    modalEl.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    savedFocus?.focus();
  }
  function initModal(modalEl) {
    modalEl.setAttribute('aria-hidden', modalEl.classList.contains('open') ? 'false' : 'true');
    modalEl.setAttribute('role', 'dialog');
    modalEl.setAttribute('aria-modal', 'true');
    // Backdrop click
    modalEl.addEventListener('click', e => {
      if (e.target === modalEl) closeModal(modalEl);
    });
    // Close buttons
    $$('[data-modal-close]', modalEl).forEach(b => b.addEventListener('click', () => closeModal(modalEl)));
    // Focus trap & Esc
    modalEl.addEventListener('keydown', e => {
      if (e.key === 'Escape') { closeModal(modalEl); return; }
      if (e.key !== 'Tab') return;
      const focusable = $$(focusableSelector, modalEl);
      if (focusable.length === 0) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault(); last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault(); first.focus();
      }
    });
  }
  // Click triggers
  document.addEventListener('click', e => {
    const trigger = e.target.closest('[data-modal-open]');
    if (trigger) {
      const id = trigger.getAttribute('data-modal-open');
      openModal(document.getElementById(id));
    }
  });

  /* --------------------------------------------------------------------- */
  /*  DROPDOWN                                                               */
  /* --------------------------------------------------------------------- */
  function initDropdown(root) {
    const trigger = $('.dropdown-trigger', root);
    const menu = $('.dropdown-menu', root);
    if (!trigger || !menu) return;

    const items = $$('.dropdown-item', menu);
    let focusedIdx = -1;

    trigger.setAttribute('aria-haspopup', 'listbox');
    trigger.setAttribute('aria-expanded', 'false');
    menu.setAttribute('role', 'listbox');
    items.forEach((it, i) => {
      it.setAttribute('role', 'option');
      it.setAttribute('tabindex', '-1');
      it.addEventListener('click', () => select(i));
      it.addEventListener('mouseover', () => setFocus(i));
    });

    function open() {
      root.classList.add('open');
      trigger.setAttribute('aria-expanded', 'true');
      const selected = items.findIndex(i => i.classList.contains('selected'));
      setFocus(selected >= 0 ? selected : 0);
    }
    function close() {
      root.classList.remove('open');
      trigger.setAttribute('aria-expanded', 'false');
    }
    function toggle() { root.classList.contains('open') ? close() : open(); }
    function setFocus(i) {
      items.forEach(it => it.classList.remove('focused'));
      focusedIdx = (i + items.length) % items.length;
      items[focusedIdx]?.classList.add('focused');
    }
    function select(i) {
      items.forEach(it => it.classList.remove('selected'));
      items[i]?.classList.add('selected');
      const label = items[i]?.textContent.trim();
      const labelEl = trigger.querySelector('.label') || trigger;
      if (labelEl.querySelector('.label')) labelEl.querySelector('.label').textContent = label;
      else {
        const chev = trigger.querySelector('.chevron');
        trigger.textContent = label;
        if (chev) trigger.appendChild(chev);
      }
      close();
      trigger.dispatchEvent(new CustomEvent('chds:change', { detail: { value: items[i]?.dataset.value, label } }));
    }

    trigger.addEventListener('click', toggle);
    trigger.addEventListener('keydown', e => {
      if (e.key === 'ArrowDown') { e.preventDefault(); root.classList.contains('open') ? setFocus(focusedIdx + 1) : open(); }
      if (e.key === 'ArrowUp')   { e.preventDefault(); if (root.classList.contains('open')) setFocus(focusedIdx - 1); }
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); root.classList.contains('open') ? select(focusedIdx) : open(); }
      if (e.key === 'Escape') close();
    });
    document.addEventListener('click', e => {
      if (!root.contains(e.target)) close();
    });
  }

  /* --------------------------------------------------------------------- */
  /*  NOTIFICATION DISMISS                                                   */
  /* --------------------------------------------------------------------- */
  function initNotification(root) {
    const close = $('.notification-close', root);
    if (!close) return;
    close.setAttribute('aria-label', 'fechar notificação');
    close.addEventListener('click', () => {
      root.classList.add('is-dismissing');
      setTimeout(() => root.remove(), 200);
    });
  }

  /* --------------------------------------------------------------------- */
  /*  TOAST (programmatic)                                                   */
  /* --------------------------------------------------------------------- */
  function ensureToastStack() {
    let stack = $('#chdsToastStack');
    if (!stack) {
      stack = document.createElement('div');
      stack.id = 'chdsToastStack';
      stack.className = 'toast-stack';
      stack.setAttribute('aria-live', 'polite');
      stack.setAttribute('aria-atomic', 'false');
      document.body.appendChild(stack);
    }
    return stack;
  }
  function toast({ title, message, kind = 'info', timeout = 4500 } = {}) {
    const stack = ensureToastStack();
    const n = document.createElement('div');
    n.className = `notification notification--${kind}`;
    n.setAttribute('role', 'status');
    const icons = { success: '✓', error: '⚠', warning: '⚠', info: 'i' };
    n.innerHTML = `
      <div class="notification-icon" aria-hidden="true">${icons[kind] || 'i'}</div>
      <div class="notification-body">
        ${title ? `<strong>${title}</strong>` : ''}
        ${message ? `<p>${message}</p>` : ''}
      </div>
      <button class="notification-close" aria-label="fechar">×</button>
    `;
    stack.appendChild(n);
    initNotification(n);
    if (timeout) setTimeout(() => {
      n.classList.add('is-dismissing');
      setTimeout(() => n.remove(), 200);
    }, timeout);
    return n;
  }

  /* --------------------------------------------------------------------- */
  /*  NUMBER INPUT — stepper buttons                                         */
  /* --------------------------------------------------------------------- */
  function initNumberInput(root) {
    const input = $('input[type="number"]', root);
    const dec = $('[data-action="dec"]', root);
    const inc = $('[data-action="inc"]', root);
    if (!input) return;
    const step = parseFloat(input.step) || 1;
    const min = input.min !== '' ? parseFloat(input.min) : -Infinity;
    const max = input.max !== '' ? parseFloat(input.max) : Infinity;
    const update = (delta) => {
      const cur = parseFloat(input.value) || 0;
      const next = Math.min(max, Math.max(min, cur + delta));
      input.value = next;
      input.dispatchEvent(new Event('input', { bubbles: true }));
      input.dispatchEvent(new Event('change', { bubbles: true }));
      if (dec) dec.disabled = next <= min;
      if (inc) inc.disabled = next >= max;
    };
    dec?.addEventListener('click', () => update(-step));
    inc?.addEventListener('click', () => update(step));
  }

  /* --------------------------------------------------------------------- */
  /*  FILE UPLOADER — drag & drop + click                                    */
  /* --------------------------------------------------------------------- */
  function initFileUploader(root) {
    const input = $('input[type="file"]', root);
    const list = root.parentElement?.querySelector('.file-list');
    if (!input) return;

    const fmt = (b) => {
      if (b < 1024) return b + ' B';
      if (b < 1024*1024) return (b/1024).toFixed(1) + ' KB';
      return (b/(1024*1024)).toFixed(1) + ' MB';
    };
    const render = (files) => {
      if (!list) return;
      list.innerHTML = '';
      Array.from(files).forEach((f, i) => {
        const li = document.createElement('li');
        li.className = 'file-list-item';
        li.innerHTML = `<span class="file-name">${f.name}</span><span class="file-size">${fmt(f.size)}</span><button type="button" class="file-remove" aria-label="remover">×</button>`;
        li.querySelector('.file-remove').addEventListener('click', () => li.remove());
        list.appendChild(li);
      });
    };

    root.addEventListener('click', (e) => {
      if (e.target.tagName !== 'INPUT' && e.target.tagName !== 'BUTTON') input.click();
    });
    input.addEventListener('change', () => render(input.files));

    ['dragenter','dragover'].forEach(evt => root.addEventListener(evt, (e) => {
      e.preventDefault(); root.classList.add('is-dragover');
    }));
    ['dragleave','drop'].forEach(evt => root.addEventListener(evt, (e) => {
      e.preventDefault(); root.classList.remove('is-dragover');
    }));
    root.addEventListener('drop', (e) => {
      const files = e.dataTransfer.files;
      input.files = files;
      render(files);
    });
  }

  /* --------------------------------------------------------------------- */
  /*  SLIDER — sync value label                                              */
  /* --------------------------------------------------------------------- */
  function initSlider(root) {
    const input = $('input[type="range"]', root);
    const out = $('.slider-value', root.parentElement);
    if (!input || !out) return;
    const sync = () => out.textContent = input.value;
    input.addEventListener('input', sync);
    sync();
  }

  /* --------------------------------------------------------------------- */
  /*  DATA TABLE — sortable headers                                          */
  /* --------------------------------------------------------------------- */
  function initSortableTable(table) {
    const headers = $$('th[data-sort]', table);
    if (!headers.length) return;
    headers.forEach((th, colIdx) => {
      th.setAttribute('tabindex', '0');
      th.setAttribute('role', 'button');
      const sortBy = () => {
        const cur = th.dataset.sort || 'none';
        const dir = cur === 'asc' ? 'desc' : 'asc';
        headers.forEach(h => h.dataset.sort = 'none');
        th.dataset.sort = dir;
        const tbody = $('tbody', table);
        const rows = $$('tr', tbody);
        rows.sort((a, b) => {
          const ta = a.children[colIdx]?.textContent.trim() || '';
          const tb = b.children[colIdx]?.textContent.trim() || '';
          const na = parseFloat(ta);
          const nb = parseFloat(tb);
          let cmp;
          if (!isNaN(na) && !isNaN(nb)) cmp = na - nb;
          else cmp = ta.localeCompare(tb, 'pt-BR');
          return dir === 'asc' ? cmp : -cmp;
        });
        rows.forEach(r => tbody.appendChild(r));
      };
      th.addEventListener('click', sortBy);
      th.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sortBy(); }
      });
    });
  }

  /* --------------------------------------------------------------------- */
  /*  PLAYGROUND — props playground genérico                                 */
  /*  HTML pattern:                                                          */
  /*    <div class="playground" data-template="...">                         */
  /*      <div class="playground-preview" data-target></div>                 */
  /*      <div class="playground-controls">                                  */
  /*        <select data-prop="variant"><option value="primary">...</option> */
  /*      </div>                                                             */
  /*      <pre class="playground-code"></pre>                                */
  /*    </div>                                                               */
  /* --------------------------------------------------------------------- */
  function initPlayground(root) {
    const tpl = root.dataset.template;
    const preview = $('[data-target]', root);
    const codeEl = $('.playground-code', root);
    if (!tpl || !preview) return;

    const controls = $$('[data-prop]', root);

    function render() {
      const props = {};
      controls.forEach(c => {
        const k = c.dataset.prop;
        if (c.type === 'checkbox') props[k] = c.checked;
        else props[k] = c.value;
      });
      // Substitui {{prop}} no template
      let html = tpl;
      for (const [k, v] of Object.entries(props)) {
        const re = new RegExp(`\\{\\{${k}\\}\\}`, 'g');
        html = html.replace(re, v === true ? '' : (v === false ? 'data-_off' : v));
      }
      // Remove placeholders not substituídos
      html = html.replace(/\{\{[^}]+\}\}/g, '');
      // Remove atributos data-_off
      html = html.replace(/\sdata-_off/g, '');
      preview.innerHTML = html;
      if (codeEl) codeEl.textContent = html.trim();
    }

    controls.forEach(c => c.addEventListener('input', render));
    render();
  }

  /* --------------------------------------------------------------------- */
  /*  AUTO-INIT                                                              */
  /* --------------------------------------------------------------------- */
  function initAll() {
    $$('.accordion').forEach(initAccordion);
    $$('[role="tablist"]').forEach(initTabs);
    $$('.modal-backdrop').forEach(initModal);
    $$('.dropdown').forEach(initDropdown);
    $$('.notification').forEach(initNotification);
    $$('.number-input').forEach(initNumberInput);
    $$('.file-uploader').forEach(initFileUploader);
    $$('.slider').forEach(initSlider);
    $$('table.data-table').forEach(initSortableTable);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  /* --------------------------------------------------------------------- */
  /*  PUBLIC API                                                             */
  /* --------------------------------------------------------------------- */
  window.CHDS = window.CHDS || {};
  Object.assign(window.CHDS, {
    openModal,
    closeModal,
    toast,
    initAccordion,
    initTabs,
    initModal,
    initDropdown,
    initNotification,
  });
})();
