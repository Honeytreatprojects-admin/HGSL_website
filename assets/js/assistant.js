/* ==========================================================================
   HGSL Assistant
   Ships as a self-contained intent router so the site works with zero backend.
   To switch to a live model, set ASSISTANT.endpoint below to your own server
   route. Never put an API key in this file — proxy the call server-side.
   ========================================================================== */
window.ASSISTANT = { endpoint: null };

(function () {
  'use strict';
  var $ = function (s, c) { return (c || document).querySelector(s); };

  var KB = [
    { id: 'greet', k: ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening'],
      a: 'Hello. I can answer questions about HGSL\u2019s five divisions, our technology products, projects, careers, or how to reach the right team. What are you looking for?' },
    { id: 'divisions', k: ['division', 'divisions', 'business unit', 'what do you do', 'services', 'sectors'],
      a: 'HGSL operates five divisions:<br><br><strong>EQL</strong> \u2014 Equipment Leasing<br><strong>RED</strong> \u2014 Real Estate Development<br><strong>CNG</strong> \u2014 Compressed Natural Gas Distribution<br><strong>MIN</strong> \u2014 Mining Operations<br><strong>SDI</strong> \u2014 Software Development & Digital Innovation<br><br>Each has its own page under <a href="divisions.html">Divisions</a>.' },
    { id: 'equipment', k: ['equipment', 'lease', 'leasing', 'excavator', 'machinery', 'plant hire', 'rental', 'cat', 'mantrac'],
      a: 'Our Equipment Leasing division supplies excavators, loaders, concrete pumps, dozers and support plant on daily, monthly and project-term contracts, with maintenance and operator cover included. See <a href="equipment-leasing.html">Equipment Leasing</a> or request availability from the <a href="contact.html">contact page</a>.' },
    { id: 'realestate', k: ['real estate', 'property', 'housing', 'land', 'apartment', 'residential', 'commercial'],
      a: 'Real Estate Development covers residential, commercial and industrial assets \u2014 site acquisition through design, delivery and asset management. Details on the <a href="real-estate.html">Real Estate</a> page.' },
    { id: 'cng', k: ['cng', 'gas', 'energy', 'fuel', 'conversion', 'compressed natural'],
      a: 'Our CNG division builds refuelling infrastructure, distributes compressed natural gas to industrial and transport customers, and runs vehicle conversion programmes. It typically cuts fuel spend against diesel while lowering emissions. See <a href="cng.html">CNG Distribution</a>.' },
    { id: 'mining', k: ['mining', 'mineral', 'quarry', 'granite', 'aggregate', 'extraction', 'solid mineral'],
      a: 'Mining Operations handles licensed extraction and processing of industrial minerals and aggregates, with community development and rehabilitation built into each site plan. See <a href="mining.html">Mining Operations</a>.' },
    { id: 'software', k: ['software', 'tech', 'technology', 'digital', 'app', 'development', 'sdi', 'engineering team', 'product'],
      a: 'Software Development & Digital Innovation is a full division, not a support function. We build enterprise platforms for the group and commercial products for market \u2014 currently <strong>QwikCare</strong> (healthcare) and <strong>SurDrive</strong> (mobility). See <a href="technology.html">Technology & Innovation</a>.' },
    { id: 'qwikcare', k: ['qwikcare', 'healthcare', 'health', 'patient', 'clinic', 'hospital'],
      a: '<strong>QwikCare</strong> is our healthcare technology platform \u2014 it connects patients with providers, handles records and appointments, and supports care delivery at scale. Live at <a href="https://qwikcare.org" target="_blank" rel="noopener">qwikcare.org</a>.' },
    { id: 'surdrive', k: ['surdrive', 'mobility', 'transport', 'ride', 'driver', 'fleet', 'logistics'],
      a: '<strong>SurDrive</strong> is our mobility and transportation platform, covering fleet operations, driver management and trip infrastructure. Live at <a href="https://surdrive.org" target="_blank" rel="noopener">surdrive.org</a>.' },
    { id: 'contact', k: ['contact', 'email', 'phone', 'call', 'reach', 'address', 'office', 'located', 'where'],
      a: 'Head office: 9A Bankole Street, Magodo Phase 1, Lagos, Nigeria.<br>Email: <a href="mailto:contact@honeytreatglobal.com">contact@honeytreatglobal.com</a><br><br>The <a href="contact.html">contact page</a> routes enquiries to the right division.' },
    { id: 'careers', k: ['career', 'job', 'jobs', 'hiring', 'vacancy', 'apply', 'work with', 'internship', 'graduate'],
      a: 'We hire across engineering, operations, energy, real estate and software. Open roles and the graduate pathway are on the <a href="careers.html">Careers</a> page.' },
    { id: 'partner', k: ['partner', 'partnership', 'supplier', 'vendor', 'collaborate', 'joint venture', 'jv'],
      a: 'For partnerships, supply agreements or joint ventures, use the <a href="contact.html">contact form</a> and select \u201cPartnership enquiry\u201d \u2014 it goes to Group Business Development.' },
    { id: 'esg', k: ['esg', 'sustainability', 'environment', 'emission', 'carbon', 'community', 'social', 'green'],
      a: 'Our ESG work runs on three tracks: cleaner energy adoption through CNG, responsible extraction and land rehabilitation in mining, and local employment and skills development. Full detail on the <a href="sustainability.html">Sustainability</a> page.' },
    { id: 'investors', k: ['investor', 'investment', 'shareholder', 'financial', 'annual report', 'governance', 'board'],
      a: 'Investor materials, governance framework and board structure are under <a href="investors.html">Investor Information</a> and <a href="governance.html">Corporate Governance</a>.' },
    { id: 'projects', k: ['project', 'projects', 'portfolio', 'case study', 'track record', 'reference'],
      a: 'Delivered and active work across all five divisions is on the <a href="projects.html">Projects</a> page, filterable by division.' },
    { id: 'about', k: ['about', 'who are you', 'history', 'company', 'story', 'founded', 'leadership', 'ceo', 'md'],
      a: 'HGSL is a diversified Nigerian industrial and technology group operating in equipment leasing, real estate, CNG, mining and software. See <a href="about.html">About Us</a> and <a href="leadership.html">Leadership</a>.' },
    { id: 'quote', k: ['quote', 'price', 'pricing', 'cost', 'rate', 'how much', 'proposal'],
      a: 'Pricing depends on scope, duration and location, so we quote per enquiry. Send the details through the <a href="contact.html">contact form</a> and the division lead will respond with a costed proposal.' }
  ];

  var FALLBACK = 'I don\u2019t have that one on hand. Try asking about a specific division \u2014 equipment leasing, real estate, CNG, mining or software \u2014 or reach the team directly through the <a href="contact.html">contact page</a>.';

  function score(text, entry) {
    var s = 0;
    entry.k.forEach(function (k) { if (text.indexOf(k) > -1) s += k.split(' ').length * 2; });
    return s;
  }
  function route(text) {
    var q = text.toLowerCase().replace(/[^a-z0-9\s]/g, ' ');
    var best = null, bestScore = 0;
    KB.forEach(function (e) { var s = score(q, e); if (s > bestScore) { bestScore = s; best = e; } });
    return bestScore > 0 ? best.a : FALLBACK;
  }

  var panel = $('.chat'), log = $('.chat__log'), input = $('.chat__f input');
  var opener = $('.chat-open'), closer = $('.chat__x'), form = $('.chat__f');
  if (!panel) return;

  function bubble(html, who) {
    var d = document.createElement('div');
    d.className = 'msg msg--' + who;
    d.innerHTML = html;
    log.appendChild(d);
    log.scrollTop = log.scrollHeight;
    return d;
  }
  function thinking() {
    var d = document.createElement('div');
    d.className = 'msg msg--b typing';
    d.innerHTML = '<span></span><span></span><span></span>';
    log.appendChild(d);
    log.scrollTop = log.scrollHeight;
    return d;
  }

  function answer(text) {
    var t = thinking();
    var done = function (html) { t.remove(); bubble(html, 'b'); };
    if (window.ASSISTANT.endpoint) {
      // Live mode: POST to your own server route, which holds the model key.
      fetch(window.ASSISTANT.endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, page: location.pathname })
      }).then(function (r) { return r.json(); })
        .then(function (d) { done(d.reply || FALLBACK); })
        .catch(function () { done(route(text)); });
    } else {
      setTimeout(function () { done(route(text)); }, 520);
    }
  }

  function open() {
    panel.classList.add('open');
    opener.style.display = 'none';
    panel.setAttribute('aria-hidden', 'false');
    if (!log.children.length) {
      bubble('Welcome to Honeytreat Global Services. I can help with our divisions, technology products, projects and enquiries \u2014 ask away, or pick a starting point below.', 'b');
    }
    setTimeout(function () { input.focus(); }, 320);
  }
  function close() {
    panel.classList.remove('open');
    opener.style.display = '';
    panel.setAttribute('aria-hidden', 'true');
    opener.focus();
  }

  opener.addEventListener('click', open);
  closer.addEventListener('click', close);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && panel.classList.contains('open')) close(); });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var v = input.value.trim();
    if (!v) return;
    bubble(v.replace(/</g, '&lt;'), 'u');
    input.value = '';
    answer(v);
  });

  document.querySelectorAll('.chips button').forEach(function (c) {
    c.addEventListener('click', function () {
      bubble(c.textContent, 'u');
      answer(c.textContent);
    });
  });
})();
