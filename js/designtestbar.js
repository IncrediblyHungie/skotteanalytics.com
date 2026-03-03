/* === DESIGN TEST BAR ===
   Accent color, hero typography, credentials bar, service cards.
   Toggle: click "Design" button at bottom-right of page.
   Remove this file + script tag when design is finalized.     */

(function () {
  'use strict';

  var ROOT = document.documentElement;

  /* ─── ACCENT COLORS ──────────────────────────────────────── */
  var ACCENTS = [
    { name: 'Green',  accent: '#06d6a0', dim: '#05b888', glow: 'rgba(6,214,160,0.15)'   },
    { name: 'Blue',   accent: '#3b82f6', dim: '#2563eb', glow: 'rgba(59,130,246,0.15)'  },
    { name: 'Amber',  accent: '#f59e0b', dim: '#d97706', glow: 'rgba(245,158,11,0.15)'  },
    { name: 'Coral',  accent: '#f97316', dim: '#ea580c', glow: 'rgba(249,115,22,0.15)'  },
  ];

  /* ─── HERO TITLE SIZE ─────────────────────────────────────── */
  var HERO_SIZES = [
    { name: 'Tight',   size: 'clamp(1.875rem, 4vw, 3rem)',   weight: '700', tracking: '-0.02em' },
    { name: 'Current', size: 'clamp(2.25rem, 5vw, 3.75rem)', weight: '800', tracking: '-0.03em' },
    { name: 'Bold XL', size: 'clamp(2.5rem, 6vw, 4.5rem)',   weight: '800', tracking: '-0.04em' },
  ];

  /* ─── HERO BADGE STYLE ────────────────────────────────────── */
  var BADGE_STYLES = [
    { name: 'Pill (current)', bg: 'rgba(6,214,160,0.1)',  border: '1px solid rgba(6,214,160,0.3)', color: 'var(--color-accent)', radius: '999px', pad: '' },
    { name: 'Solid',          bg: 'var(--color-accent)',  border: 'none',                           color: '#0b0f1a',             radius: '999px', pad: '' },
    { name: 'Plain label',    bg: 'transparent',           border: 'none',                           color: 'var(--color-text-muted)', radius: '0', pad: '4px 0' },
  ];

  /* ─── CREDENTIALS BAR LAYOUT ──────────────────────────────── */
  var CREDS_DATA = [
    { label: 'UEI',             value: 'KM4REVCBKA78', accent: false },
    { label: 'CAGE Code',       value: '17NY6',         accent: false },
    { label: 'SAM.gov Status',  value: 'Active',        accent: true  },
    { label: 'Micro-Purchase',  value: 'Under $10K',    accent: false },
  ];

  var CREDS_LAYOUTS = [
    { name: 'Grid (current)', id: 'grid'     },
    { name: 'Pills',          id: 'pills'    },
    { name: 'Table',          id: 'table'    },
    { name: 'Ticker strip',   id: 'ticker'   },
    { name: 'Cards',          id: 'cards'    },
    { name: 'Active-first',   id: 'active'   },
    { name: 'Mono terminal',  id: 'terminal' },
  ];

  /* ─── SERVICE CARD STYLE ──────────────────────────────────── */
  var CARD_STYLES = [
    { name: 'Current',    id: 'default'   },
    { name: 'Outlined',   id: 'outlined'  },
    { name: 'Accent bar', id: 'accentbar' },
    { name: 'Elevated',   id: 'elevated'  },
  ];

  /* ─── STATE ───────────────────────────────────────────────── */
  var state = {
    accentIdx:   parseInt(localStorage.getItem('dtb-accent')   || '0', 10),
    heroSizeIdx: parseInt(localStorage.getItem('dtb-herosize') || '1', 10),
    badgeIdx:    parseInt(localStorage.getItem('dtb-badge')    || '0', 10),
    credsIdx:    parseInt(localStorage.getItem('dtb-creds')    || '0', 10),
    cardIdx:     parseInt(localStorage.getItem('dtb-card')     || '0', 10),
  };

  /* ─── APPLY FUNCTIONS ─────────────────────────────────────── */
  function applyAccent() {
    var a = ACCENTS[state.accentIdx];
    ROOT.style.setProperty('--color-accent',      a.accent);
    ROOT.style.setProperty('--color-accent-dim',  a.dim);
    ROOT.style.setProperty('--color-accent-glow', a.glow);
    localStorage.setItem('dtb-accent', state.accentIdx);
  }

  function applyHeroSize() {
    var h = HERO_SIZES[state.heroSizeIdx];
    var title = document.querySelector('.hero__title');
    if (title) {
      title.style.fontSize      = h.size;
      title.style.fontWeight    = h.weight;
      title.style.letterSpacing = h.tracking;
    }
    localStorage.setItem('dtb-herosize', state.heroSizeIdx);
  }

  function applyBadge() {
    var b = BADGE_STYLES[state.badgeIdx];
    var badge = document.querySelector('.hero__badge');
    if (badge) {
      badge.style.background   = b.bg;
      badge.style.border       = b.border;
      badge.style.color        = b.color;
      badge.style.borderRadius = b.radius;
      if (b.pad) badge.style.padding = b.pad;
    }
    localStorage.setItem('dtb-badge', state.badgeIdx);
  }

  function applyCredsLayout() {
    var grid = document.querySelector('.metrics__grid');
    if (!grid) return;
    var layout = CREDS_LAYOUTS[state.credsIdx].id;

    if (layout === 'grid') {
      grid.style.cssText = 'padding-block: var(--space-10);';
      grid.innerHTML = CREDS_DATA.map(function (c) {
        var valStyle = 'font-size:var(--text-xl);' + (c.accent ? 'color:#22c55e;' : '');
        return '<div class="metric">' +
          '<div class="metric__value" style="' + valStyle + '">' + c.value + '</div>' +
          '<div class="metric__label">' + c.label + '</div>' +
          '</div>';
      }).join('');
    }

    if (layout === 'pills') {
      grid.style.cssText = 'padding-block:var(--space-8);display:flex;flex-wrap:wrap;justify-content:center;gap:var(--space-3);';
      grid.innerHTML = CREDS_DATA.map(function (c) {
        var extra = c.accent ? 'color:#22c55e;border-color:rgba(34,197,94,0.4);' : '';
        return '<div style="display:inline-flex;align-items:center;gap:8px;padding:8px 20px;' +
          'border:1px solid var(--color-border);border-radius:999px;' + extra + '">' +
          '<span style="font-size:var(--text-xs);text-transform:uppercase;letter-spacing:0.08em;color:var(--color-text-muted);">' + c.label + '</span>' +
          '<span style="font-family:monospace;font-weight:700;font-size:var(--text-sm);color:' + (c.accent ? '#22c55e' : 'var(--color-text)') + ';">' + c.value + '</span>' +
          '</div>';
      }).join('');
    }

    if (layout === 'table') {
      grid.style.cssText = 'padding-block:var(--space-8);display:flex;justify-content:center;';
      grid.innerHTML = '<table style="border-collapse:collapse;font-size:var(--text-sm);min-width:320px;">' +
        CREDS_DATA.map(function (c) {
          var valStyle = c.accent
            ? 'color:#22c55e;font-weight:700;'
            : 'color:var(--color-text);font-family:monospace;font-weight:600;';
          return '<tr style="border-bottom:1px solid var(--color-border);">' +
            '<td style="padding:10px 32px 10px 0;color:var(--color-text-muted);white-space:nowrap;">' + c.label + '</td>' +
            '<td style="padding:10px 0;' + valStyle + '">' + c.value + '</td>' +
            '</tr>';
        }).join('') +
        '</table>';
    }

    if (layout === 'ticker') {
      grid.style.cssText = 'padding-block:var(--space-6);display:flex;justify-content:center;';
      grid.innerHTML =
        '<div style="display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:0;font-size:var(--text-sm);font-family:monospace;">' +
        CREDS_DATA.map(function (c, i) {
          var valColor = c.accent ? '#22c55e' : 'var(--color-text)';
          var sep = i < CREDS_DATA.length - 1
            ? '<span style="color:var(--color-border-hover);padding:0 16px;">|</span>'
            : '';
          return '<span style="display:inline-flex;align-items:center;gap:6px;">' +
            '<span style="color:var(--color-text-muted);text-transform:uppercase;letter-spacing:0.08em;font-size:var(--text-xs);">' + c.label + '</span>' +
            '<span style="color:' + valColor + ';font-weight:700;">' + c.value + '</span>' +
            '</span>' + sep;
        }).join('') +
        '</div>';
    }

    if (layout === 'cards') {
      grid.style.cssText = 'padding-block:var(--space-8);display:grid;grid-template-columns:repeat(4,1fr);gap:var(--space-4);max-width:800px;margin-inline:auto;';
      grid.innerHTML = CREDS_DATA.map(function (c) {
        var valColor = c.accent ? '#22c55e' : 'var(--color-text)';
        return '<div style="background:var(--color-bg);border:1px solid var(--color-border);border-radius:var(--radius-lg);padding:var(--space-5) var(--space-4);text-align:center;">' +
          '<div style="font-size:var(--text-xs);text-transform:uppercase;letter-spacing:0.1em;color:var(--color-text-muted);margin-bottom:var(--space-2);">' + c.label + '</div>' +
          '<div style="font-family:monospace;font-size:var(--text-lg);font-weight:700;color:' + valColor + ';">' + c.value + '</div>' +
          '</div>';
      }).join('');
    }

    if (layout === 'active') {
      grid.style.cssText = 'padding-block:var(--space-10);display:flex;flex-direction:column;align-items:center;gap:var(--space-6);';
      grid.innerHTML =
        '<div style="display:inline-flex;align-items:center;gap:var(--space-3);background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.35);border-radius:var(--radius-lg);padding:var(--space-4) var(--space-8);">' +
          '<div style="width:10px;height:10px;border-radius:50%;background:#22c55e;box-shadow:0 0 10px rgba(34,197,94,0.6);flex-shrink:0;"></div>' +
          '<div style="font-size:var(--text-2xl);font-weight:800;color:#22c55e;letter-spacing:-0.01em;">SAM.gov Active</div>' +
        '</div>' +
        '<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:var(--space-6);">' +
        CREDS_DATA.filter(function (c) { return !c.accent; }).map(function (c) {
          return '<div style="text-align:center;">' +
            '<div style="font-size:var(--text-xs);text-transform:uppercase;letter-spacing:0.1em;color:var(--color-text-muted);margin-bottom:var(--space-1);">' + c.label + '</div>' +
            '<div style="font-family:monospace;font-size:var(--text-base);font-weight:700;color:var(--color-text);">' + c.value + '</div>' +
          '</div>';
        }).join('') +
        '</div>';
    }

    if (layout === 'terminal') {
      grid.style.cssText = 'padding-block:var(--space-8);display:flex;justify-content:center;';
      grid.innerHTML =
        '<div style="background:#080c14;border:1px solid var(--color-border);border-radius:var(--radius-md);padding:var(--space-5) var(--space-8);font-family:monospace;font-size:var(--text-sm);min-width:340px;">' +
          '<div style="color:#3a4a5e;font-size:var(--text-xs);margin-bottom:var(--space-4);letter-spacing:0.08em;"># vendor credentials</div>' +
          CREDS_DATA.map(function (c) {
            var valColor = c.accent ? '#22c55e' : '#e2e8f0';
            return '<div style="display:flex;gap:var(--space-4);margin-bottom:var(--space-2);">' +
              '<span style="color:#5a6a82;min-width:160px;">' + c.label.toLowerCase().replace(/ /g, '_') + '</span>' +
              '<span style="color:' + valColor + ';font-weight:700;">' + c.value + '</span>' +
            '</div>';
          }).join('') +
        '</div>';
    }

    localStorage.setItem('dtb-creds', state.credsIdx);
  }

  function applyCardStyle() {
    var cards = document.querySelectorAll('#services .card');
    var style = CARD_STYLES[state.cardIdx].id;
    for (var i = 0; i < cards.length; i++) {
      var c = cards[i];
      c.style.cssText = '';
      if (style === 'outlined') {
        c.style.background = 'transparent';
        c.style.border     = '1.5px solid var(--color-border-hover)';
      }
      if (style === 'accentbar') {
        c.style.borderTop    = '3px solid var(--color-accent)';
        c.style.borderLeft   = 'none';
        c.style.borderRight  = 'none';
        c.style.borderBottom = 'none';
        c.style.borderRadius = '0 0 var(--radius-lg) var(--radius-lg)';
        c.style.paddingTop   = 'var(--space-6)';
      }
      if (style === 'elevated') {
        c.style.boxShadow = '0 8px 40px rgba(0,0,0,0.45)';
        c.style.border    = '1px solid var(--color-border-hover)';
      }
    }
    localStorage.setItem('dtb-card', state.cardIdx);
  }

  function applyAll() {
    applyAccent();
    applyHeroSize();
    applyBadge();
    applyCredsLayout();
    applyCardStyle();
  }

  /* ─── BAR UI ──────────────────────────────────────────────── */
  var bar, toggleBtn, isOpen = false;

  function updateActive(type) {
    if (!bar) return;
    var pills = bar.querySelectorAll('[data-dtb-' + type + ']');
    for (var i = 0; i < pills.length; i++) {
      var idx = parseInt(pills[i].getAttribute('data-dtb-' + type), 10);
      pills[i].classList.toggle('dtb-active', idx === state[type + 'Idx']);
    }
  }

  function buildSection(label, items, stateKey, applyFn) {
    var sec = document.createElement('div');
    sec.className = 'dtb-section';
    sec.innerHTML =
      '<div class="dtb-head">' +
        '<span class="dtb-label">' + label + '</span>' +
        '<span class="dtb-divider"></span>' +
      '</div>';
    var row = document.createElement('div');
    row.className = 'dtb-row';
    for (var i = 0; i < items.length; i++) {
      (function (idx) {
        var btn = document.createElement('button');
        btn.className = 'dtb-pill';
        btn.setAttribute('data-dtb-' + stateKey, idx);
        btn.textContent = items[idx].name;
        btn.addEventListener('click', function () {
          state[stateKey + 'Idx'] = idx;
          updateActive(stateKey);
          applyFn();
        });
        row.appendChild(btn);
      })(i);
    }
    sec.appendChild(row);
    return sec;
  }

  function createBar() {
    bar = document.createElement('div');
    bar.id = 'dtb-bar';

    var css = document.createElement('style');
    css.textContent =
      '#dtb-bar{position:fixed;bottom:0;left:0;right:0;z-index:9999;' +
        'background:rgba(11,15,26,0.97);backdrop-filter:blur(20px);' +
        'border-top:1px solid rgba(255,255,255,0.08);' +
        'transform:translateY(100%);opacity:0;transition:transform .3s ease,opacity .3s ease;' +
        'padding:16px 5%;max-height:60vh;overflow-y:auto;}' +
      '#dtb-bar.dtb-open{transform:translateY(0);opacity:1;}' +
      '.dtb-section{margin-bottom:12px;}' +
      '.dtb-head{display:flex;align-items:center;gap:10px;margin-bottom:8px;}' +
      '.dtb-label{font-family:monospace;font-size:11px;color:#5a6a82;text-transform:uppercase;letter-spacing:0.12em;flex-shrink:0;}' +
      '.dtb-divider{flex:1;height:1px;background:rgba(255,255,255,0.06);}' +
      '.dtb-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}' +
      '.dtb-pill{padding:5px 12px;font-size:11px;font-family:monospace;' +
        'border:1px solid rgba(255,255,255,0.12);border-radius:999px;cursor:pointer;' +
        'background:transparent;color:#8896ab;white-space:nowrap;transition:all .15s;}' +
      '.dtb-pill:hover{border-color:rgba(6,214,160,0.4);color:#e2e8f0;}' +
      '.dtb-pill.dtb-active{background:#06d6a0;border-color:#06d6a0;color:#0b0f1a;font-weight:700;}' +
      '.dtb-note{font-family:monospace;font-size:10px;color:#3a4a5e;margin-top:10px;}' +
      '#dtb-toggle{position:fixed;bottom:20px;right:20px;z-index:10000;padding:9px 18px;' +
        'font-family:monospace;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.12em;' +
        'color:#0b0f1a;background:#06d6a0;border:none;border-radius:999px;cursor:pointer;' +
        'box-shadow:0 4px 20px rgba(6,214,160,0.35);transition:all .2s;}' +
      '#dtb-toggle:hover{transform:scale(1.05);box-shadow:0 6px 28px rgba(6,214,160,0.5);}' +
      '#dtb-toggle.dtb-btn-open{background:#1e2a42;color:#8896ab;box-shadow:0 4px 12px rgba(0,0,0,0.4);}';

    bar.appendChild(css);
    bar.appendChild(buildSection('Accent Color',    ACCENTS,       'accent',   applyAccent));
    bar.appendChild(buildSection('Hero Size',        HERO_SIZES,    'heroSize', applyHeroSize));
    bar.appendChild(buildSection('Hero Badge',       BADGE_STYLES,  'badge',    applyBadge));
    bar.appendChild(buildSection('Credentials Bar',  CREDS_LAYOUTS, 'creds',    applyCredsLayout));
    bar.appendChild(buildSection('Service Cards',    CARD_STYLES,   'card',     applyCardStyle));

    var note = document.createElement('div');
    note.className = 'dtb-note';
    note.textContent = 'Changes apply live. State persists in localStorage. Remove designtestbar.js when done.';
    bar.appendChild(note);

    document.body.appendChild(bar);

    updateActive('accent');
    updateActive('heroSize');
    updateActive('badge');
    updateActive('creds');
    updateActive('card');
  }

  function toggle() {
    if (!bar) createBar();
    isOpen = !isOpen;
    bar.classList.toggle('dtb-open', isOpen);
    toggleBtn.classList.toggle('dtb-btn-open', isOpen);
    toggleBtn.textContent = isOpen ? 'Close' : 'Design';
  }

  document.addEventListener('DOMContentLoaded', function () {
    toggleBtn = document.createElement('button');
    toggleBtn.id = 'dtb-toggle';
    toggleBtn.textContent = 'Design';
    toggleBtn.addEventListener('click', toggle);
    document.body.appendChild(toggleBtn);
    applyAll();
  });

})();
