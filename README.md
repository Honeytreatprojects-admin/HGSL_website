# HGSL Corporate Website

Static, dependency-free build for Honeytreat Global Services Limited. Open `index.html`
directly, or serve the folder (`python3 -m http.server`) — no build step needed to view it.

## What's here

| Page | Purpose |
|---|---|
| `index.html` | Executive overview: division switcher hero, group grid, stats, technology ecosystem, projects, ESG, partners, insights |
| `divisions.html` | Division index |
| `equipment-leasing.html` `real-estate.html` `cng.html` `mining.html` `technology.html` | The five division pages. Each carries overview, spec table, services, applications, projects, gallery, FAQ, cross-links |
| `about.html` `leadership.html` `governance.html` | Corporate section |
| `projects.html` `sustainability.html` `insights.html` `careers.html` `investors.html` `contact.html` | Remaining architecture |
| `404.html` `sitemap.xml` `robots.txt` | Housekeeping |

`technology.html` is both the SDI division page and the Technology & Innovation page — it
carries the QwikCare and SurDrive product showcase rather than duplicating it on a separate URL.

## Regenerating

Content is not hand-edited in the HTML. It lives in `../build.py`:

```
DIVISIONS   five division dicts — code, copy, spec rows, services, apps, projects, gallery, FAQs, stats
PRODUCTS    QwikCare / SurDrive
STATS_HOME  homepage counters
ESG         sustainability tracks and percentages
LEADERS     executive team
INSIGHTS    article stubs
```

Edit, then `python3 build.py`. Adding a sixth division to `DIVISIONS` propagates it to the
nav, mega menu, homepage grid, divisions index, projects filter, footer and sitemap, and
generates its page — that's the scalability requirement, handled structurally.

## Design system

Tokens are at the top of `assets/css/hgsl.css`.

- **Palette** — `#14101C` plum-ink, `#6C2BD9` brand violet, `#A78BFA` lift, `#F0A400` honey-amber, `#F7F5F9` paper. Each division also carries a two-colour field (`--fa` / `--fb`).
- **Type** — Archivo (variable width, set expanded) for display, IBM Plex Sans for body, IBM Plex Mono for labels and data.
- **Asset plate** — `.plate`, `.code`, `.spec` and the `EQL / RED / CNG / MIN / SDI` codes are one device, borrowed from the spec plate on leased equipment. Keep it consistent when adding sections.

## Adding real photography and video

Every image area is a `.field` — layered gradients plus a grid overlay standing in for
photography. To use a real photo, set `--img` on the element:

```html
<div class="field" style="--fa:#F0A400;--fb:#7A4A00">
  <div class="field__img" style="--img:url('assets/img/eql-01.jpg')"></div>
  <div class="field__scrim"></div>
</div>
```

Drop files in `assets/img/` (see the README there for suggested names). The `.field__img`
layer sits at 34% opacity in luminosity blend so photos inherit the division colour — raise
the opacity in CSS if you want the photograph to dominate.

**Hero video:** add a muted, looping, `playsinline` `<video>` as the first child of any
`.hero__f` or `.shero` field, above `.field__scrim`. Keep it under ~2 MB, poster it, and
gate it behind `prefers-reduced-motion` before launch.

## Before launch

- [ ] **Wire the forms.** Contact and careers forms are marked `data-demo-form` and do not transmit. Point them at your mail handler or CRM, then remove the `.form__note` disclaimer.
- [ ] **Wire the assistant (optional).** `assets/js/assistant.js` ships as a self-contained intent router — it works offline with no key. For a live model, set `window.ASSISTANT.endpoint` to *your own server route* and have that route hold the key. Never put an API key in this file.
- [ ] **Replace placeholder leadership names** in `LEADERS` with the real team and photos.
- [ ] **Verify the stats.** Homepage and division counters carry indicative figures — confirm each against operational data before publishing, since they read as claims.
- [ ] **Confirm contact details** (`ADDR` / `MAIL` / `TEL` in `build.py`) and the social links in the footer, which currently point to `#`.
- [ ] **Add favicons and an OG share image**, then reference the OG image in `head()`.
- [ ] **Self-host the fonts** if Lagos-side latency on Google Fonts is a concern.

## Accessibility and performance notes

Skip link, visible focus rings, keyboard-operable menus and accordions, `aria-expanded` on
every disclosure, `prefers-reduced-motion` honoured throughout (the hero stops auto-advancing,
counters snap to final value, reveals are pre-shown). No JS framework, no images by default,
so first paint is fast — the main budget risk is whatever photography and video you add.
