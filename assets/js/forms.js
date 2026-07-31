/* HGSL — live forms (Formspree) + careers apply modal. No dependencies. */
(function () {
  'use strict';

  var ENDPOINT = 'https://formspree.io/f/xjgndzjr';
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---- 1. Formspree submit ------------------------------------------- */
  function wireForm(form) {
    var ok  = $('.form__ok', form);
    var err = $('.form__err', form);
    var btn = $('[type=submit]', form);
    var btnHTML = btn ? btn.innerHTML : '';

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.dataset.busy === '1') return;

      form.dataset.busy = '1';
      if (ok)  ok.classList.remove('on');
      if (err) err.classList.remove('on');
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }

      fetch(ENDPOINT, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      })
      .then(function (r) {
        if (r.ok) return {};
        return r.json().then(function (d) { throw d; }, function () { throw {}; });
      })
      .then(function () {
        if (ok) { ok.classList.add('on'); ok.setAttribute('role', 'status'); }
        form.reset();
      })
      .catch(function (d) {
        var msg = 'Sorry — that did not send. Please email contact@honeytreatglobal.com or call +234 807 158 4064.';
        if (d && d.errors && d.errors.length) {
          msg = d.errors.map(function (x) { return x.message; }).join(', ');
        }
        if (err) { err.textContent = msg; err.classList.add('on'); err.setAttribute('role', 'alert'); }
      })
      .then(function () {
        form.dataset.busy = '0';
        if (btn) { btn.disabled = false; btn.innerHTML = btnHTML; }
      });
    });
  }
  $$('form[data-form]').forEach(wireForm);

  /* ---- 2. Careers apply modal ---------------------------------------- */
  var modal = $('#apply');
  if (!modal) return;

  var roleEl = $('[data-apply-role]', modal);
  var divEl  = $('[data-apply-div]', modal);
  var field  = $('[data-apply-field]', modal);
  var lastFocus = null;

  function openModal(role, div) {
    if (roleEl) roleEl.textContent = role;
    if (divEl)  divEl.textContent  = div;
    if (field) {
      var v = role + (div ? ' — ' + div : '');
      field.setAttribute('value', v);   /* attribute, so form.reset() keeps it */
      field.value = v;
    }
    var ok = $('.form__ok', modal), er = $('.form__err', modal);
    if (ok) ok.classList.remove('on');
    if (er) er.classList.remove('on');

    lastFocus = document.activeElement;
    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    var first = $('input:not([type=hidden]):not(.sr)', modal);
    if (first) setTimeout(function () { first.focus(); }, 60);
  }

  function closeModal() {
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  $$('[data-jobs] a.card').forEach(function (card) {
    card.addEventListener('click', function (e) {
      e.preventDefault();
      var h = $('h3', card), p = $('.plate', card);
      openModal(h ? h.textContent.trim() : 'Open role', p ? p.textContent.trim() : '');
    });
  });

  $$('[data-close]', modal).forEach(function (el) { el.addEventListener('click', closeModal); });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modal.classList.contains('open')) closeModal();
  });

  /* keep tab focus inside the dialog */
  modal.addEventListener('keydown', function (e) {
    if (e.key !== 'Tab') return;
    var f = $$('a[href],button:not([disabled]),input:not([type=hidden]),select,textarea', modal)
      .filter(function (el) { return el.offsetParent !== null; });
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });
})();