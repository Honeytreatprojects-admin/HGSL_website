/* HGSL — site behaviour. No dependencies. */
(function () {
  'use strict';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Nav: solid on scroll ------------------------------------------- */
  var nav = $('.nav');
  var bar = $('.progress');
  function onScroll() {
    var y = window.scrollY;
    if (nav) nav.classList.toggle('solid', y > 24 || document.body.dataset.navSolid === 'true');
    if (bar) {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = 'scaleX(' + (h > 0 ? y / h : 0) + ')';
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---- Mega menu ------------------------------------------------------ */
  var mega = $('.mega');
  var megaBtn = $('[data-mega]');
  function closeMega() {
    if (!mega) return;
    mega.classList.remove('open');
    megaBtn.setAttribute('aria-expanded', 'false');
  }
  if (mega && megaBtn) {
    megaBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = mega.classList.toggle('open');
      megaBtn.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', function (e) {
      if (!mega.contains(e.target) && e.target !== megaBtn) closeMega();
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMega(); });
  }

  /* ---- Mobile drawer -------------------------------------------------- */
  var burger = $('.burger');
  var drawer = $('.drawer');
  if (burger && drawer) {
    burger.addEventListener('click', function () {
      var open = drawer.classList.toggle('open');
      burger.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
      if (open) nav.classList.add('solid');
    });
    $$('a', drawer).forEach(function (a) {
      a.addEventListener('click', function () {
        drawer.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  /* ---- Scroll reveal -------------------------------------------------- */
  var rv = $$('.rv');
  if (!('IntersectionObserver' in window) || calm) {
    rv.forEach(function (el) { el.classList.add('in'); });
  } else {
    var ro = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); ro.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
    rv.forEach(function (el) { ro.observe(el); });
  }

  /* ---- Animated counters ---------------------------------------------- */
  /* Only runs on a data-count that parses to a real number. A data-count
     holding a label string is skipped, so it can never render as NaN. */
  function countUp(el) {
    var target = parseFloat(el.dataset.count);
    if (isNaN(target)) return;
    var dec = (el.dataset.dec | 0);
    if (calm) { el.textContent = target.toFixed(dec); return; }
    var dur = 1500, t0 = null;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (target * eased).toFixed(dec);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var nums = $$('[data-count]').filter(function (el) {
    return !isNaN(parseFloat(el.dataset.count));
  });
  if (nums.length) {
    if (!('IntersectionObserver' in window)) { nums.forEach(countUp); }
    else {
      var no = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { countUp(e.target); no.unobserve(e.target); } });
      }, { threshold: 0.5 });
      nums.forEach(function (n) { no.observe(n); });
    }
  }

  /* ---- ESG bars ------------------------------------------------------- */
  var bars = $$('.bar__f');
  if (bars.length && 'IntersectionObserver' in window) {
    var bo = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { e.target.style.width = e.target.dataset.pct + '%'; bo.unobserve(e.target); }
      });
    }, { threshold: 0.4 });
    bars.forEach(function (b) { bo.observe(b); });
  } else {
    bars.forEach(function (b) { b.style.width = b.dataset.pct + '%'; });
  }

  /* ---- Hero division switcher ---------------------------------------- */
  var rails = $$('.rail__b');
  var fields = $$('.hero__slide');
  var titleEl = $('[data-hero-title]');
  var leadEl = $('[data-hero-lead]');
  var timer = null, idx = 0;

  function setDivision(i, manual) {
    idx = i;
    rails.forEach(function (b, n) { b.classList.toggle('on', n === i); b.setAttribute('aria-pressed', String(n === i)); });
    fields.forEach(function (f, n) { f.classList.toggle('is-on', n === i); });
    var b = rails[i];
    if (titleEl && b) {
      titleEl.innerHTML = b.dataset.title;
      if (!calm) { titleEl.animate([{ opacity: 0, transform: 'translateY(12px)' }, { opacity: 1, transform: 'none' }], { duration: 620, easing: 'cubic-bezier(.22,1,.36,1)' }); }
    }
    if (leadEl && b) leadEl.textContent = b.dataset.lead;
    if (manual && timer) { clearInterval(timer); timer = null; }
  }
  if (rails.length) {
    rails.forEach(function (b, i) {
      b.addEventListener('click', function () { setDivision(i, true); });
      b.addEventListener('mouseenter', function () { setDivision(i, true); });
      b.addEventListener('focus', function () { setDivision(i, true); });
    });
    setDivision(0);
    if (!calm) timer = setInterval(function () { setDivision((idx + 1) % rails.length); }, 6000);
  }

  /* ---- Accordions ----------------------------------------------------- */
  $$('.acc__b').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var panel = btn.nextElementSibling;
      var open = btn.getAttribute('aria-expanded') === 'true';
      // close siblings in the same accordion
      var group = btn.closest('.acc');
      if (group) {
        $$('.acc__b', group).forEach(function (o) {
          if (o !== btn) { o.setAttribute('aria-expanded', 'false'); o.nextElementSibling.style.height = '0px'; }
        });
      }
      btn.setAttribute('aria-expanded', String(!open));
      panel.style.height = open ? '0px' : panel.firstElementChild.offsetHeight + 'px';
    });
  });

  /* ---- Project filters ------------------------------------------------ */
  var fbtns = $$('.filters button');
  if (fbtns.length) {
    fbtns.forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.dataset.filter;
        fbtns.forEach(function (o) { o.setAttribute('aria-pressed', String(o === b)); });
        $$('.pj__i').forEach(function (card) {
          var show = f === 'all' || card.dataset.div === f;
          card.hidden = !show;
        });
      });
    });
  }

  /* ---- Sub-nav scroll spy -------------------------------------------- */
  var spy = $$('.subnav a[href^="#"]');
  if (spy.length && 'IntersectionObserver' in window) {
    var targets = spy.map(function (a) { return $(a.getAttribute('href')); }).filter(Boolean);
    var so = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) {
          spy.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id); });
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    targets.forEach(function (t) { so.observe(t); });
  }

  /* ---- Contact / careers form (demo handler) -------------------------- */
  $$('[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = $('.form__ok', form);
      if (ok) { ok.classList.add('on'); ok.setAttribute('role', 'status'); }
      form.reset();
    });
  });

  /* ---- Year stamp ----------------------------------------------------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
