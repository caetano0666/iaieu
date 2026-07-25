/* IAieu · comportamento compartilhado das 7 páginas
   nav Headroom · menu mobile · reveal no scroll · modal de imagem (data-modal) */
(function(){
  /* ---- nav headroom + stuck ---- */
  var nav=document.getElementById('nav'),last=0;
  if(nav){
    window.addEventListener('scroll',function(){
      var y=window.pageYOffset;
      nav.classList.toggle('stuck',y>8);
      if(y>last&&y>160)nav.classList.add('hidden');else nav.classList.remove('hidden');
      last=y;
    },{passive:true});
  }
  /* ---- menu mobile ---- */
  var t=document.getElementById('navToggle'),l=document.getElementById('navLinks');
  if(t&&l){
    t.addEventListener('click',function(){var o=l.classList.toggle('open');t.setAttribute('aria-expanded',o);});
    l.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){l.classList.remove('open');t.setAttribute('aria-expanded',false);});});
  }
  /* ---- scroll reveal ---- */
  var els=document.querySelectorAll('[data-reveal]');
  if(!('IntersectionObserver'in window)){els.forEach(function(e){e.classList.add('in');});}
  else{
    var io=new IntersectionObserver(function(en){
      en.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});
    },{threshold:.12,rootMargin:'0px 0px -8% 0px'});
    els.forEach(function(e){io.observe(e);});
  }
  /* ---- modal de imagem genérico (recomendações LinkedIn) ---- */
  var ov=document.getElementById('ov');
  if(ov){
    var img=document.getElementById('ovImg'),close=document.getElementById('ovClose');
    document.querySelectorAll('[data-modal]').forEach(function(btn){
      btn.addEventListener('click',function(){img.src='assets/img/'+btn.getAttribute('data-modal');ov.classList.add('open');document.body.style.overflow='hidden';});
    });
    var hide=function(){ov.classList.remove('open');document.body.style.overflow='';};
    close.addEventListener('click',hide);
    ov.addEventListener('click',function(e){if(e.target===ov)hide();});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')hide();});
  }
})();
