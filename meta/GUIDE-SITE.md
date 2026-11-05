# Guide site spec — HTML study guide at steeb-k.github.io/sec-plus-test/guide/

## Principles
1. **Markdown stays canonical.** The repo's `00…92-*.md` files are the only source. A build script converts them into one data
   file in the site; nothing is hand-edited on the HTML side. A sync test fails when the built data is stale.
2. **Same look as the practice site.** Reuse `../css/style.css` tokens, IBM Plex from `../fonts/ibm-plex/`, the frosted header,
   the "Sec+ | 701" pill. No CDN, no fetch, works from file://. Dark default.
3. **No runtime markdown parsing.** HTML is generated at build time by python-markdown (tables, fenced_code, toc, attr_list,
   sane_lists). The page only renders pre-built HTML.

## Files
Guide repo (`/home/steeb/security+-study/`):
```
meta/build-site.py      python3; reads 00..92 md → writes ../steeb-k.github.io/sec-plus-test/guide/data/guide.js (path overridable by --out)
```
Site (`/home/steeb/steeb-k.github.io/sec-plus-test/`):
```
guide/index.html        page shell: header (pill, "Practice" link back to ../, Contents toggle on phone), sidebar, content, tooltip host
guide/guide.css         layout + content typography on top of ../css/style.css (loaded first)
guide/guide-core.js     PURE helpers (no DOM): slugify, buildSearchIndex, search, tokenizeForTips (text → segments with acronym/objective hits),
                        readinessByObjective(attempts) — ends with `if (typeof module !== 'undefined') module.exports = GuideCore;`
guide/guide.js          app: routing, sidebar, scrollspy, search UI, tooltip UI, readiness marks, prev/next, copy-link anchors
guide/data/guide.js     GENERATED: window.SEC_GUIDE = { sourceCommit, sourceHash, builtAt, files:[…], sections:[…], acronymAnchors:{KEY:"id"} }
tests/guide-core.test.js node unit tests for guide-core.js
tests/guide-sync.sh     fails if guide/data/guide.js sourceHash ≠ sha256 of the md files in $GUIDE_SRC (default ../../security+-study); skips with a note if the dir is absent
```
`index.html` script order: ../fonts/ibm-plex/plex.css + ../css/style.css + guide.css; ../data/objectives.js, ../data/acronyms.js, data/guide.js, guide-core.js, guide.js.

## Generated data shape (`guide/data/guide.js`)
```js
window.SEC_GUIDE = {
  sourceCommit: "abc1234",          // git rev-parse --short HEAD of the guide repo (or "uncommitted")
  sourceHash: "<sha256 of the concatenated md sources in filename order>",
  builtAt: "2026-10-27T06:01:45-07:00", // HEAD commit date of the guide repo (git log -1 --format=%cI), not the wall clock: rebuilds are byte-identical
  files: [
    { id: "00", slug: "exam-overview", title: "Exam Overview", src: "00-exam-overview.md",
      html: "<h1 id=\"...\">…</h1>…",               // full file HTML, headings carry ids (see below), per-file disclaimer line removed
      toc: [ { level: 2, id: "obj-1-1", text: "1.1 Compare and contrast …" }, { level: 3, id: "…", text: "…" } ] },
    …  // order: 00, 01, 02, 03, 04, 05, 90, 91, 92
  ],
  sections: [ { file: "exam-overview", id: "obj-1-1", title: "1.1 …", path: "Domain 1 › 1.1 …", text: "plain text of that section (until next heading of same or higher level)" }, … ],
  acronymAnchors: { "AAA": "acr-aaa", … }          // row ids inserted into the 91 acronym tables
};
```
Heading ids: stable and readable. Objective headings matching `^## (\d)\.(\d+) ` get `obj-<d>-<n>` (e.g. `obj-4-8`) so the quiz can deep-link;
every other heading gets a slug of its text, de-duplicated per file with `-2`, `-3`. In 91, give every table row `<tr id="acr-<key lowercased, non-alnum→'-'>">`.
Strip the per-file "> **Note:** AI-generated…" line from each file (the page shows one banner instead). Keep everything else.

## Page behaviour
- **Routes:** `#/` → Exam Overview. `#/<file-slug>` → that file. `#/<file-slug>/<heading-id>` → file + scroll to heading (offset for sticky header).
  `#/highlights` → Highlighted page. `#/how-to` → "How to use this guide" (static page from `<template id="g-howto">` in index.html, not
  markdown; no AI banner, no highlight buttons). Unknown → Exam Overview. Document title = "<section title> · Sec+ 701 Guide".
- **Sidebar (280px, sticky, own scrollbar):** search box at top (placeholder "Search guide… ( / )"), then two page links ("How to use
  this guide", "Highlighted (n)"), then the tree: each file as a top-level
  entry; the current file expanded to show its H2s (and H3s under the active H2); other files collapsed. Scrollspy highlights the
  H2/H3 in view. Below the tree: "Weak spots" block (see Readiness). Phone (<900px): sidebar is an off-canvas drawer opened by a
  "Contents" button in the header; closes on navigation or Escape.
- **Content column:** max-width 820px; the file's HTML; headings get a hover "#" copy-link anchor; prev/next file links at the bottom;
  footer line "Built from steeb-k/secplus-study-guide @ <sourceCommit> · <builtAt date> · Edit this file on GitHub" (link to the md).
  One AI-generated banner at the top of the content (same text as the README disclaimer, short).
- **Tooltips:** after rendering, walk text nodes (skip `pre`, `code`, `a`, `abbr`, `h1`, the acronyms file's own table key column) and wrap:
  - acronyms present in `window.SEC_ACRONYMS` (longest key first; boundaries = start/end or non-alphanumeric; case-sensitive; allow a
    trailing lowercase "s" or "v<digits>"): `<abbr class="tip" tabindex="0" data-tip="<expansion>" data-acr="KEY">KEY</abbr>`.
    Do NOT wrap when the same text node already contains the expansion right next to it in parentheses like "Certificate Authority (CA)"? → still wrap; cheap and consistent.
  - objective references: text matching `/\b(?:objective|objectives|see|per)\s+(\d)\.(\d+)\b/i` → wrap the `d.n` part as
    `<a class="xref" href="#/<file-slug-of-domain d>/obj-d-n">d.n</a>`; also bare `(d.n)` inside parentheses. Never match version-like text
    (TLS 1.3, CVSS 3.1, 800-63B-4): the patterns above avoid it.
  - Tooltip UI: one floating `div.tooltip` reused; show on mouseenter/focus of `.tip`, hide on mouseleave/blur/Escape/scroll; on touch,
    tap toggles. Positioned below the word, flipped above near the viewport bottom, clamped to the viewport horizontally, 8px gap, small
    caret. Content: `<b>KEY</b> expansion` + a "Acronyms list ↗" link to `#/acronyms/<acr-id>` when an anchor exists. Dotted underline on `.tip`
    (`text-decoration: underline dotted; text-decoration-thickness: 1px; text-underline-offset: 3px; cursor: help`), colour `--ink-2`→`--ink` on hover.
- **Search:** index built from `sections` (title + text) and from the acronym glossary. Typing (debounced 80ms) shows a results panel
  under the box: first an "Acronyms" group (key or expansion match, up to 5), then "Sections" (up to 20) ranked by title match > count
  of query tokens in text > shorter section; each result shows the breadcrumb path and a snippet with the first match highlighted
  (`<mark>`). ↑/↓ moves, Enter opens. Opening a result navigates and, if the query matched body text, briefly highlights the first
  match in the content (scroll to it). The query and the results STAY in the sidebar after opening one (the opened item is the
  selected one) so the reader can work through them; a row above the results shows "N results" and a "Back to outline" button.
  Back to outline, Escape, or emptying the box restore the chapter tree. "/" focuses the box when not in an input.
- **Readiness marks:** read `localStorage['secplus.attempts']` (same origin as the quiz). For each objective, take the last 5 attempts that
  include it and compute points/count → pct. In the sidebar, show a 7px dot before each objective H2: `--ok` ≥ 83%, `--warn` ≥ 70%,
  `--bad` < 70%, none without data; dot `title` = "72% over N questions". "Weak spots" block lists the bottom 5 objectives with data as
  links. If localStorage is unavailable, show nothing (try/catch).
- **Keyboard:** `/` search, Escape closes drawer/results/tooltips, `[` / `]` previous/next file.
- **Boot status:** set `document.documentElement.dataset.ready="1"` and write `#boot-status` text "files=9 sections=N acronyms=M errors=0"
  (errors counter via window.onerror like the quiz page) so `tests/smoke.sh guide/index.html` can assert it.

## Quiz-site integration (small)
- Header nav on the quiz pages gains a "Guide" link (`guide/index.html`), before History. Home card button "Study guide" → `guide/index.html` (keep "Source" → GitHub).
  Always name `index.html`: a bare `guide/` (or the guide's "Practice" → `../`) opens a directory listing from file://.
- Practice-mode feedback panel and results review: the "Objective d.n: …" line becomes a link to
  `guide/index.html#/<domain-file-slug>/obj-d-n` (target `_blank`, rel noopener). Exam mode unchanged (no objective shown).
- Domain file slugs: exam-overview, domain-1-general-security-concepts, domain-2-threats-vulnerabilities-mitigations,
  domain-3-security-architecture, domain-4-security-operations, domain-5-program-management-oversight, ports-protocols, acronyms, formulas-numbers.
  Export the slug map from the build into `window.SEC_GUIDE.files[].slug`; the quiz pages hard-code the same slugs in one place (`js/ui.js` const).

## Tests (all must pass)
- `node tests/guide-core.test.js`: slugify; heading-id rules (obj ids, de-dup); tokenizeForTips (boundary cases from the quiz acronym tests:
  "MAC address" lowercase no-match, "CAs" plural, "SNMPv3", "TACACS+", "CI/CD", skip inside code); objective-ref regex (matches "objective 4.8",
  "see 5.2", "(1.4)"; rejects "TLS 1.3", "CVSS 3.1", "800-63B-4"); search ranking (title match first; AND semantics; snippet contains <mark>);
  readinessByObjective (last-5 window, pct, no data → absent).
- `bash tests/guide-sync.sh` → OK when guide/data/guide.js matches the md sources.
- `node tests/guide-ui.test.js` → headless-Chromium checks (deep-link offset, sidebar indent, tooltip in viewport, touch toggle,
  readiness with junk data, quiz → guide link, no requests outside the site). Skips if Chromium is absent.
- `bash tests/smoke.sh guide/index.html` → extend smoke.sh so a non-index page passes its own boot-status check and the no-external-URL
  check; the index/dev asset-sync check stays index-only.
- Headless screenshots (desktop dark/light, phone dark): overview, domain 4 with sidebar expanded, a tooltip open, search results open,
  acronyms page, phone drawer open. No horizontal overflow at 390px. Tooltip never off-screen.

## Build + sync workflow (document in the guide repo README)
```
python3 meta/build-full.py     # STUDY-GUIDE-FULL.md
python3 meta/build-site.py     # ../steeb-k.github.io/sec-plus-test/guide/data/guide.js
cd ../steeb-k.github.io/sec-plus-test && bash tests/guide-sync.sh && bash tests/smoke.sh guide/index.html
```
Optional later: a GitHub Action in the guide repo that runs build-site.py and pushes guide.js to the Pages repo with a deploy key.

## Addendum 2 (2026-11-04): tooltip meanings, paragraph highlights, Highlighted page

### Tooltip meanings
- `build-site.py` exports `acronymMeta: { KEY: { expansion, meaning, anchor } }` parsed from every row of 91-acronyms.md
  (columns: Acronym | Expansion | Meaning). Keys like "IMAP (IMAP4)" register both spellings. `acronymAnchors` stays for compatibility.
- Tooltip body: line 1 `<b>KEY</b> expansion`; line 2 the meaning in `--ink-2` (13px); line 3 the "Acronyms list ↗" link. Fallback to
  `window.SEC_ACRONYMS[KEY]` (expansion only) when no 91 row exists. Keep max-width 320px; let the meaning wrap.

### Paragraph highlights
- Highlightable blocks inside `.g-doc`: `p`, `li`, `blockquote`, `tr` (table rows), excluding the AI banner and the footer. Each block
  gets a stable key at render: `file + ':' + sectionId + ':' + hash(normalized text)` (hash = Engine-style string hash or FNV; the text
  is the block's textContent lower-cased, whitespace-collapsed, first 240 chars). Store in `data-hl` on the element.
- Gutter control: a `button.hl-btn` absolutely positioned in the left gutter of each block (left: -30px; 22px square; icon = inline SVG
  highlighter/marker, no emoji; `aria-label="Highlight this paragraph"` / "Remove highlight"; `aria-pressed`). Visible on block hover and
  on focus; on `(hover: none)` devices always visible at 45% opacity. Clicking toggles. For `tr`, position the button relative to the
  row's first cell (use `position: relative` on the cell).
- Highlighted style: `background: var(--hl-tint)`; `box-shadow: inset 3px 0 0 var(--hl)` (left bar); for `tr`, apply to its cells.
  Tokens: dark `--hl: #f2d383; --hl-tint: rgba(242,211,131,.16)`; light `--hl: #9c7a1f; --hl-tint: rgba(156,122,31,.14)`.
- Storage: `localStorage['secplus.highlights']` = `{ [key]: { file, section, heading, text, at } }` where `text` is the first 300 chars
  of the block's textContent (for the Highlighted page and for orphans), `at` = ISO time. Guard every read/write with try/catch.
- Section marks: any H2/H3 whose section contains ≥1 highlight gets a small mark after its text (`span.hl-mark`, the same marker icon at
  14px in `--hl`, `title="N highlighted"`); the sidebar entry for that section and for its chapter shows a count badge `N` in `--hl` on
  `--hl-tint`. Update marks live on toggle.
- Highlighted page: route `#/highlights`. Sidebar: an entry "Highlighted (N)" directly under the search box (always present; N may be 0).
  Content: grouped by chapter (file order) → section (document order), each item shows the saved text (clamped to ~6 lines), a "View in
  context" link (`#/<file>/<sectionId>?hl=<key>`: navigates, scrolls the block into view below the header, flashes it 1.5s, marks the
  section in the sidebar even when the block is too near the chapter end to reach the top; Back returns to the Highlighted page), and a
  remove button.
  Items whose block no longer exists in the current build (text changed) are listed in a final "No longer found" group with their saved
  text, a remove button, and "View in context" (to the section, no flash) while their section still exists. "Highlighted (N)" counts
  valid items plus orphans (exactly what the page lists). Toolbar: "Export as Markdown" (downloads `secplus-highlights.md`: `# Highlights`, `## <chapter>`, `### <section>`,
  `> text` blocks) and "Clear all" (inline confirm; an unanswered confirm is reset when the page is left). Empty state explains how to
  highlight. Export text is plain text made Markdown-safe: backslash, backtick, `*`, `<`, `[`, `]`, word-boundary `_`, entity-like `&` and a leading `#`, `>`,
  `-`, `+` or `1.` are backslash-escaped, so "<script>" or "****-1234" render literally and the file never contains raw HTML.
- Keyboard: when a block's button has focus, Space/Enter toggles. Escape closes nothing new.
- Tests: guide-core gets pure helpers `hlKey(file, sectionId, text)`, `groupHighlights(store, data)` (chapter → section grouping, orphans
  detection), `highlightsMarkdown(groups)` and `mdText(text)`, with unit tests. guide-ui test: toggle a paragraph, reload, still highlighted;
  sidebar badge count; Highlighted page lists it and "View in context" lands within 8–24px below the header; remove clears everything;
  corrupt storage is ignored; plus the regressions listed below.

### Behaviour settled during verification (2026-11-04)
- Block text for keys: a list item's own text is its child nodes concatenated with no separator (nested lists excluded). Joining with
  spaces made the rendered page (text split around tooltip `<abbr>`s) disagree with the detached parse used for orphan detection, so
  every highlighted list item containing an acronym showed under "No longer found", and keys would have shifted whenever the glossary
  changed. Identical blocks in one section get `key~2`, `key~3` in document order.
- Saved `text`: first 300 chars, ending in "…" when cut (the key still hashes the full normalized text).
- Storage: the store is a prototype-less object; `__proto__` keys are dropped on load; `?hl=` lookups use own properties only (a crafted
  `?hl=__proto__` used to throw). A refused write (quota, storage disabled) keeps the change for the visit and the live region says
  "not saved". A `storage` event from another tab also redraws an open Highlighted page.
- Table rows: the first cell of every highlightable row, and the first header cell, get 32px left padding on all devices; the button
  sits in that padding and never covers the key text. A row's View-in-context flash is a cell background (accent tint), not per-cell
  outlines; the acronym-list arrival flash also shows on a highlighted row.
- Hover: a nested list item reveals only its own button (`:has()`), not its parent's too.
- Contrast on the tint: links inside a highlighted block and on the Highlighted page use `--accent-hi` (light: `--accent` was 4.17:1);
  light `--hl-ink` is `#6b5108` (badges on the active/hovered sidebar row were 4.11:1). Measured minimums after the change: dark 5.15
  (muted tooltip-word ink on a doubly tinted nested item), light 5.15 (badge on the active row).

## Addendum 3 (2026-11-04): sidebar under the frosted header; favicon as the pill

- The desktop sidebar's scroll box starts at the top of the viewport (sticky `top: 0`, negative top margin of the header
  height, matching top padding and `scroll-padding-top`), so its rows slide beneath the translucent header exactly as the
  main column does. `sideView()` in guide.js treats the header's bottom edge as the visible top when it auto-scrolls the
  current heading into view. The phone drawer still opens flush under the header, above the backdrop.
- Phone contents button: no longer in the header (the pill sits flush left). It is a 48px round, frosted button fixed at
  the bottom-left of the viewport (16px in, safe-area aware), outside the header element because the header's
  backdrop-filter would act as the containing block for a fixed child. z-index 45, above the drawer (40) and backdrop
  (30). Closed it shows a hamburger (aria-label "Contents"); while the drawer is open it shows a back arrow (aria-label
  "Back to the page") so the same button reads as "open the contents" and "go back". Icons are inline SVG swapped by
  `aria-expanded` in CSS. Content and drawer get 88px bottom padding so their last rows clear the button.
- Favicon (`icons/favicon.svg` + ico/png, generator `icons/make-favicon.py`): the header pill as a squircle. White
  rounded square (outline and the "S" segment are one shape, as in the pill), black inner segment on the right carrying a
  white "+", S side wider than the + side. Glyph outlines come from the self-hosted Plex Sans SemiBold.

## Addendum 4 (2026-11-04): persistent search results; How-to page

- Search results no longer clear when a result is opened (see Search above). `#g-res-top` holds the count and the "Back to outline"
  button; `backToOutline()` is the single path used by the button, Escape, and the input's own Escape.
- "How to use this guide": `#/how-to`, linked first in the sidebar (above Highlighted) with a question-mark icon in the accent colour.
  Content lives in `<template id="g-howto">` in guide/index.html, written conversationally, and is NOT built from the markdown repo:
  edit it there when features change. Styled by `.g-howto` (h1/h2/p/li/kbd). `page` in guide.js is 'highlights' | 'howto' | null.

## Addendum 5 (2026-11-05): shared header

The guide's header grid (`.g-hwrap`/`.g-hnav`) moved to `css/style.css` as `.hwrap`/`.hnav` and is used by every page; see
DESIGN.md "Site header". The guide's "Practice" link opens in the same tab (one site); the pill goes to `../index.html`; the
phone contents button is unchanged (outside the header). Tokens `--page-w`, `--side-w`, `--col-w` drive both the header and
`.g-layout`.

## Addendum 6 (2026-11-05): no chapter banner; last section remembered

- The AI-generated banner above each chapter is gone (the How-to page's caveat, the README and the markdown notes stay).
- `localStorage['secplus.guide.last']` holds the last section in view (`#/<slug>/<heading-id>`, written by the scrollspy when it
  changes) or `#/highlights` / `#/how-to`. Opening the guide with no hash (the shared header's Guide link) restores it via
  `history.replaceState` before the first route render; an explicit `#/` still opens the overview. Deep links are unaffected.
- The practice home's "Security+ SY0-701 practice" heading is visually hidden (`.sr`), kept for screen readers.

