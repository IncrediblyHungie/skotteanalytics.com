/* === PHOTO TEST BAR — Hero & About photo style previewer ===
   Toggle: Click the "Photo" button at bottom-right of page
   Remove this file + script tag when design is finalized       */

(function () {
  'use strict';

  var SHAPES = [
    { name: 'Circle',       borderRadius: '50%',  aspectRatio: 1 },
    { name: 'Rounded rect', borderRadius: '16px', aspectRatio: 1.3 },
    { name: 'Squircle',     borderRadius: '24px', aspectRatio: 1 },
    { name: 'Sharp rect',   borderRadius: '4px',  aspectRatio: 1.3 },
    { name: 'Square',       borderRadius: '8px',  aspectRatio: 1 },
  ];

  var FILTERS = [
    { name: 'Color',     filter: 'none' },
    { name: 'Grayscale', filter: 'grayscale(100%)' },
    { name: 'Green tint', filter: 'grayscale(100%) sepia(40%) hue-rotate(100deg) saturate(200%) brightness(0.9)' },
    { name: 'Faded',     filter: 'grayscale(60%) brightness(0.85)' },
  ];

  var BORDERS = [
    { name: 'None',       border: 'none',                                         boxShadow: 'none' },
    { name: 'Subtle',     border: '1px solid rgba(255,255,255,0.12)',              boxShadow: 'none' },
    { name: 'Accent',     border: '2px solid rgba(6, 214, 160, 0.5)',             boxShadow: 'none' },
    { name: 'Glow',       border: '2px solid rgba(6, 214, 160, 0.4)',             boxShadow: '0 0 32px rgba(6,214,160,0.2)' },
    { name: 'White glow', border: '2px solid rgba(255,255,255,0.25)',             boxShadow: '0 0 32px rgba(255,255,255,0.08)' },
  ];

  var SIZES = [
    { name: 'S',   px: 160 },
    { name: 'M',   px: 220 },
    { name: 'L',   px: 280 },
    { name: 'XL',  px: 360 },
  ];

  /* State */
  var state = {
    shapeIdx:  parseInt(localStorage.getItem('ptb-shape')  || '0', 10),
    filterIdx: parseInt(localStorage.getItem('ptb-filter') || '0', 10),
    borderIdx: parseInt(localStorage.getItem('ptb-border') || '2', 10),
    sizeIdx:   parseInt(localStorage.getItem('ptb-size')   || '2', 10),
  };

  function getHeroImg() { return document.querySelector('.hero__photo-wrap img'); }
  function getAboutImg() { return document.querySelector('.about-teaser img'); }

  function applyToImg(img, shape, filter, border, size) {
    if (!img) return;
    var h = Math.round(size.px * shape.aspectRatio);
    img.style.width        = size.px + 'px';
    img.style.height       = h + 'px';
    img.style.borderRadius = shape.borderRadius;
    img.style.filter       = filter.filter;
    img.style.border       = border.border;
    img.style.boxShadow    = border.boxShadow;
    img.style.objectFit    = 'cover';
    img.style.objectPosition = 'center top';
    img.style.display      = 'block';
  }

  function applyAll() {
    var shape  = SHAPES[state.shapeIdx];
    var filter = FILTERS[state.filterIdx];
    var border = BORDERS[state.borderIdx];
    var size   = SIZES[state.sizeIdx];
    applyToImg(getHeroImg(),  shape, filter, border, size);
    applyToImg(getAboutImg(), shape, filter, border, { px: Math.round(size.px * 0.75) });
    localStorage.setItem('ptb-shape',  state.shapeIdx);
    localStorage.setItem('ptb-filter', state.filterIdx);
    localStorage.setItem('ptb-border', state.borderIdx);
    localStorage.setItem('ptb-size',   state.sizeIdx);
  }

  function updateActive(type) {
    if (!bar) return;
    var pills = bar.querySelectorAll('[data-ptb-' + type + ']');
    for (var i = 0; i < pills.length; i++) {
      var idx = parseInt(pills[i].getAttribute('data-ptb-' + type), 10);
      pills[i].classList.toggle('ptb-active', idx === state[type + 'Idx']);
    }
  }

  var bar, toggleBtn, isOpen = false;

  function createBar() {
    bar = document.createElement('div');
    bar.id = 'ptb-bar';
    bar.innerHTML =
      '<style>' +
        '#ptb-bar{position:fixed;bottom:0;left:0;right:0;z-index:9999;' +
          'background:rgba(11,15,26,0.97);backdrop-filter:blur(20px);' +
          'border-top:1px solid rgba(255,255,255,0.08);' +
          'transform:translateY(100%);opacity:0;transition:transform .3s ease,opacity .3s ease;' +
          'padding:16px 5%;max-height:60vh;overflow-y:auto;}' +
        '#ptb-bar.ptb-open{transform:translateY(0);opacity:1;}' +
        '.ptb-section{margin-bottom:12px;}' +
        '.ptb-head{display:flex;align-items:center;gap:10px;margin-bottom:8px;}' +
        '.ptb-label{font-family:monospace;font-size:11px;color:#5a6a82;text-transform:uppercase;letter-spacing:0.12em;flex-shrink:0;}' +
        '.ptb-divider{flex:1;height:1px;background:rgba(255,255,255,0.06);}' +
        '.ptb-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}' +
        '.ptb-pill{padding:5px 12px;font-size:11px;font-family:monospace;border:1px solid rgba(255,255,255,0.12);' +
          'border-radius:999px;cursor:pointer;background:transparent;color:#8896ab;white-space:nowrap;transition:all .15s;}' +
        '.ptb-pill:hover{border-color:rgba(6,214,160,0.4);color:#e2e8f0;}' +
        '.ptb-pill.ptb-active{background:#06d6a0;border-color:#06d6a0;color:#0b0f1a;font-weight:700;}' +
        '.ptb-note{font-family:monospace;font-size:10px;color:#3a4a5e;margin-top:10px;}' +
        '#ptb-toggle{position:fixed;bottom:20px;right:20px;z-index:10000;padding:9px 18px;' +
          'font-family:monospace;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.12em;' +
          'color:#0b0f1a;background:#06d6a0;border:none;border-radius:999px;cursor:pointer;' +
          'box-shadow:0 4px 20px rgba(6,214,160,0.35);transition:all .2s;}' +
        '#ptb-toggle:hover{transform:scale(1.05);box-shadow:0 6px 28px rgba(6,214,160,0.5);}' +
        '#ptb-toggle.ptb-btn-open{background:#1e2a42;color:#8896ab;box-shadow:0 4px 12px rgba(0,0,0,0.4);}' +
      '</style>' +
      '<div id="ptb-shapes-section" class="ptb-section"></div>' +
      '<div id="ptb-filters-section" class="ptb-section"></div>' +
      '<div id="ptb-borders-section" class="ptb-section"></div>' +
      '<div id="ptb-sizes-section" class="ptb-section"></div>' +
      '<div class="ptb-note">Changes apply live to hero + about section photos. Persists in localStorage. Remove phototestbar.js when done.</div>';

    function buildSection(id, label, items, stateKey) {
      var sec = bar.querySelector('#ptb-' + id + '-section');
      sec.innerHTML = '<div class="ptb-head"><span class="ptb-label">' + label + '</span><span class="ptb-divider"></span></div>';
      var row = document.createElement('div');
      row.className = 'ptb-row';
      for (var i = 0; i < items.length; i++) {
        var btn = document.createElement('button');
        btn.className = 'ptb-pill';
        btn.setAttribute('data-ptb-' + stateKey, i);
        btn.textContent = items[i].name;
        btn.addEventListener('click', (function(idx, key) {
          return function() {
            state[key + 'Idx'] = idx;
            updateActive(key);
            applyAll();
          };
        })(i, stateKey));
        row.appendChild(btn);
      }
      sec.appendChild(row);
    }

    buildSection('shapes',  'Shape',     SHAPES,  'shape');
    buildSection('filters', 'Treatment', FILTERS, 'filter');
    buildSection('borders', 'Border',    BORDERS, 'border');
    buildSection('sizes',   'Size',      SIZES,   'size');

    document.body.appendChild(bar);

    /* set active states */
    updateActive('shape');
    updateActive('filter');
    updateActive('border');
    updateActive('size');
  }

  function toggle() {
    if (!bar) createBar();
    isOpen = !isOpen;
    bar.classList.toggle('ptb-open', isOpen);
    toggleBtn.classList.toggle('ptb-btn-open', isOpen);
    toggleBtn.textContent = isOpen ? 'Close' : 'Photo';
  }

  document.addEventListener('DOMContentLoaded', function () {
    toggleBtn = document.createElement('button');
    toggleBtn.id = 'ptb-toggle';
    toggleBtn.textContent = 'Photo';
    toggleBtn.addEventListener('click', toggle);
    document.body.appendChild(toggleBtn);

    /* restore persisted state on load */
    applyAll();
  });

})();
