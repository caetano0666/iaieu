/* Acervo Plínio Marcos — comportamento compartilhado
   Nav Headroom (esconde ao rolar pra baixo), menu mobile, scroll-reveal. */
(function () {
  'use strict';

  /* ---- menu mobile ---- */
  var nav = document.querySelector('.nav');
  var toggle = document.querySelector('.navtoggle');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('menu-open');
      var open = nav.classList.contains('menu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    // fecha ao clicar num link
    nav.querySelectorAll('.menu a').forEach(function (a) {
      a.addEventListener('click', function () { nav.classList.remove('menu-open'); });
    });
  }

  /* ---- Headroom: esconde a nav ao descer, mostra ao subir ---- */
  var lastY = window.pageYOffset;
  var ticking = false;
  function onScroll() {
    var y = window.pageYOffset;
    if (nav && !nav.classList.contains('menu-open')) {
      if (y > lastY && y > 160) nav.classList.add('nav--hide');
      else nav.classList.remove('nav--hide');
    }
    lastY = y;
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { window.requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });

  /* ---- scroll-reveal (respeita prefers-reduced-motion) ---- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var items = document.querySelectorAll('[data-reveal]');
  if (reduce || !('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          var el = e.target;
          var delay = parseFloat(el.getAttribute('data-delay') || '0');
          el.style.transitionDelay = delay + 'ms';
          el.classList.add('in');
          io.unobserve(el);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  }

  /* ---- ano corrente no rodapé ---- */
  var yr = document.querySelector('[data-year]');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- form de contato (demonstração, sem back-end) ---- */
  var form = document.querySelector('[data-contact]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = form.querySelector('[data-ok]');
      if (ok) { ok.hidden = false; }
      form.reset();
    });
  }
})();

/* ---- Lightbox: qualquer <img class="lb" data-full data-cap>, agrupado por [data-gallery] ---- */
(function () {
  'use strict';
  var triggers = Array.prototype.slice.call(document.querySelectorAll('img.lb'));
  if (!triggers.length) return;

  var box = document.createElement('div');
  box.className = 'lightbox';
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.innerHTML =
    '<button class="lb-btn lb-close" aria-label="Fechar">✕</button>' +
    '<button class="lb-btn lb-prev" aria-label="Anterior">‹</button>' +
    '<button class="lb-btn lb-next" aria-label="Próxima">›</button>' +
    '<img alt="">' +
    '<p class="lb-cap"></p><p class="lb-count"></p>';
  document.body.appendChild(box);

  var imgEl = box.querySelector('img');
  var capEl = box.querySelector('.lb-cap');
  var countEl = box.querySelector('.lb-count');
  var group = [];
  var idx = 0;

  function groupOf(el) {
    var scope = el.closest('[data-gallery]') || document;
    return Array.prototype.slice.call(scope.querySelectorAll('img.lb'));
  }
  function show(i) {
    if (i < 0) i = group.length - 1;
    if (i >= group.length) i = 0;
    idx = i;
    var t = group[idx];
    imgEl.src = t.getAttribute('data-full') || t.src;
    imgEl.alt = t.alt || '';
    capEl.textContent = t.getAttribute('data-cap') || t.alt || '';
    countEl.textContent = group.length > 1 ? (idx + 1) + ' / ' + group.length : '';
  }
  function open(el) {
    group = groupOf(el);
    show(group.indexOf(el));
    box.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function close() {
    box.classList.remove('open');
    document.body.style.overflow = '';
    imgEl.src = '';
  }

  triggers.forEach(function (t) {
    t.addEventListener('click', function () { open(t); });
  });
  box.querySelector('.lb-close').addEventListener('click', close);
  box.querySelector('.lb-prev').addEventListener('click', function () { show(idx - 1); });
  box.querySelector('.lb-next').addEventListener('click', function () { show(idx + 1); });
  box.addEventListener('click', function (e) { if (e.target === box) close(); });
  document.addEventListener('keydown', function (e) {
    if (!box.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(idx - 1);
    else if (e.key === 'ArrowRight') show(idx + 1);
  });
})();
