/* PLÍNIO MARCOS — site estático. Sem dependências. */
(function(){
  "use strict";

  /* ---------- menu hambúrguer (mobile) ---------- */
  var burger = document.querySelector('.burger');
  var navMobile = document.querySelector('.nav-mobile');
  if (burger && navMobile){
    var toggle = function(open){
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      navMobile.classList.toggle('open', open);
      document.body.classList.toggle('menu-open', open);
    };
    burger.addEventListener('click', function(){
      toggle(!navMobile.classList.contains('open'));
    });
    navMobile.addEventListener('click', function(e){
      if (e.target.tagName === 'A') toggle(false);
    });
    document.addEventListener('keydown', function(e){
      if (e.key === 'Escape') toggle(false);
    });
  }

  /* ---------- dropdown "A obra" (desktop): clique/toque abre ---------- */
  var dropToggle = document.querySelector('.nav-drop-toggle');
  var drop = document.querySelector('.nav-drop');
  if (dropToggle && drop){
    var closeDrop = function(){ drop.classList.remove('open'); dropToggle.setAttribute('aria-expanded','false'); };
    dropToggle.addEventListener('click', function(e){
      e.preventDefault(); e.stopPropagation();
      var open = !drop.classList.contains('open');
      drop.classList.toggle('open', open);
      dropToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('click', function(e){
      if (!e.target.closest('.has-drop')) closeDrop();
    });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape') closeDrop(); });
    drop.addEventListener('click', function(e){ if (e.target.tagName === 'A') closeDrop(); });
  }

  /* ---------- barra que gruda / fica sólida ao rolar ---------- */
  var topbar = document.querySelector('.topbar');
  if (topbar && !topbar.classList.contains('force-solid')){
    var onScroll = function(){
      topbar.classList.toggle('solid', window.scrollY > 40);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, {passive:true});
  }

  /* ---------- rolagem suave para âncoras internas ---------- */
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) return;
    var id = a.getAttribute('href');
    if (id.length < 2) return;
    var el = document.querySelector(id);
    if (!el) return;
    e.preventDefault();
    el.scrollIntoView({behavior:'smooth', block:'start'});
    history.replaceState(null,'',id);
  });

  /* ---------- índice da biografia: capítulo ativo ---------- */
  var bioLinks = document.querySelectorAll('.bio-index a');
  if (bioLinks.length && 'IntersectionObserver' in window){
    var map = {};
    bioLinks.forEach(function(a){ map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if (en.isIntersecting){
          bioLinks.forEach(function(a){ a.classList.remove('active'); });
          var link = map[en.target.id];
          if (link){
            link.classList.add('active');
            link.scrollIntoView({block:'nearest', inline:'center'});
          }
        }
      });
    }, {rootMargin:'-45% 0px -50% 0px', threshold:0});
    document.querySelectorAll('.chapter[id]').forEach(function(c){ io.observe(c); });
  }

  /* ---------- lightbox do álbum ---------- */
  var gallery = document.querySelector('.album-grid');
  var lb = document.querySelector('.lightbox');
  if (gallery && lb){
    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('figcaption');
    var items = Array.prototype.slice.call(gallery.querySelectorAll('button'));
    var idx = 0;

    var show = function(i){
      idx = (i + items.length) % items.length;
      var btn = items[idx];
      var full = btn.getAttribute('data-full');
      var cap  = btn.getAttribute('data-caption') || '';
      lbImg.src = full;
      lbImg.alt = cap;
      lbCap.textContent = cap;
      lbCap.style.display = cap ? 'block' : 'none';
    };
    var open = function(i){ show(i); lb.classList.add('open'); document.body.classList.add('menu-open'); };
    var close = function(){ lb.classList.remove('open'); document.body.classList.remove('menu-open'); lbImg.src=''; };

    items.forEach(function(btn,i){ btn.addEventListener('click', function(){ open(i); }); });
    lb.querySelector('.lightbox__close').addEventListener('click', close);
    lb.querySelector('.lightbox__next').addEventListener('click', function(){ show(idx+1); });
    lb.querySelector('.lightbox__prev').addEventListener('click', function(){ show(idx-1); });
    lb.addEventListener('click', function(e){ if (e.target === lb) close(); });
    document.addEventListener('keydown', function(e){
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowRight') show(idx+1);
      if (e.key === 'ArrowLeft') show(idx-1);
    });
  }
})();
