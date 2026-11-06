# Guide site spec — HTML study guide at steeb-k.github.io/sec-plus-test/guide/

## Principles
1. **Markdown stays canonical.** The repo's `00…92-*.md` files are the only source. `meta/build-site.py` converts them into one
   data file in the site; nothing is hand-edited on the HTML side. A sync test fails when the built data is stale.
2. **Same look as the practice site.** The guide reuses `../css/style.css` tokens, IBM Plex from `../fonts/ibm-plex/`, the frosted
   header and the "Security+ | SY0-701" pill. No CDN, no fetch, works from file://. Dark default.
3. **No runtime markdown parsing.** HTML is generated at build time by python-markdown (tables, fenced_code, toc, attr_list,
   sane_lists). The page only renders pre-built HTML.

## Files
Guide repo (`/home/steeb/security+-study/`):
```
meta/build-site.py      python3; reads 00..92 md → writes ../steeb-k.github.io/sec-plus-test/guide/data/guide.js (path overridable by --out)
```
Site (`/home/steeb/steeb-k.github.io/sec-plus-test/`):
```
guide/index.html        page shell: shared header, floating phone contents button, <template id="g-howto">, sidebar, content, tooltip host
guide/guide.css         layout + content typography on top of ../css/style.css (loaded first)
guide/guide-core.js     PURE helpers (no DOM): slugify, buildSearchIndex, search, tokenizeForTips, readinessByObjective, weakSpots,
                        hlKey, groupHighlights, highlightsMarkdown, mdText — ends with `if (typeof module !== 'undefined') module.exports = GuideCore;`
guide/guide.js          app: routing, sidebar, scrollspy, search UI, tooltip UI, readiness marks, highlights, prev/next, copy-link anchors
guide/data/guide.js     GENERATED: window.SEC_GUIDE = { sourceCommit, sourceHash, builtAt, files, sections, acronymAnchors, acronymMeta }
js/header.js            shared by every page: steps the pill's wording down only as far as it must to fit (see DESIGN.md "Header wordmark")
tests/guide-core.test.js node unit tests for guide-core.js
tests/guide-sync.sh     fails if guide/data/guide.js sourceHash ≠ sha256 of the md files in $GUIDE_SRC (default ../../security+-study); skips with a note if the dir is absent
tests/guide-ui.test.js  headless-Chromium checks for the guide and the shared header (skips if Chromium is absent)
```
`guide/index.html` load order: ../fonts/ibm-plex/plex.css, ../css/style.css, guide.css; then ../js/header.js right after the header;
at the end ../data/objectives.js, ../data/acronyms.js, data/guide.js, guide-core.js, guide.js.

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
  acronymAnchors: { "AAA": "acr-aaa", … },         // row ids inserted into the 91 acronym tables
  acronymMeta: { "AAA": { expansion, meaning, anchor }, … } // every row of 91-acronyms.md (Acronym | Expansion | Meaning); "IMAP (IMAP4)" registers both spellings
};
```
Heading ids are stable and readable. Objective headings matching `^## (\d)\.(\d+) ` get `obj-<d>-<n>` (e.g. `obj-4-8`) so the quiz can
deep-link; every other heading gets a slug of its text, de-duplicated per file with `-2`, `-3`. In 91, every table row gets
`<tr id="acr-<key lowercased, non-alnum→'-'>">`. The per-file "> **Note:** AI-generated…" line is stripped from each file (the caveat
lives on the How-to page, in the README and in the markdown). Everything else is kept.

File slugs: exam-overview, domain-1-general-security-concepts, domain-2-threats-vulnerabilities-mitigations, domain-3-security-architecture,
domain-4-security-operations, domain-5-program-management-oversight, ports-protocols, acronyms, formulas-numbers. The quiz pages hold the
same slugs in one place (`js/ui.js`).

## Layout
- Tokens `--page-w` (1240px), `--side-w` (280px) and `--col-w` (820px) in `css/style.css` drive both the shared header grid and
  `.g-layout` (sidebar column + content column). The header itself is specified in DESIGN.md "Site header".
- **Sidebar (desktop):** sticky, its own scroll box. It starts at the top of the viewport (sticky `top: 0`, negative top margin of the
  header height `--g-hdr`, matching top padding and `scroll-padding-top`), so its rows slide beneath the translucent header exactly as
  the main column does. `sideView()` in guide.js treats the header's bottom edge as the visible top when it auto-scrolls the current
  entry into view. The sidebar is an independent pane: navigating in the content never moves it except to keep the current entry visible.
- **Phone (<900px):** the sidebar is an off-canvas drawer (z-index 40) over a backdrop (30), opening flush under the header; it closes
  on navigation or Escape. The contents button is a 48px round frosted button fixed at the bottom-left of the viewport (16px in,
  safe-area aware, z-index 45), outside the header element because the header's backdrop-filter would act as the containing block for
  a fixed child. Closed it shows a hamburger (aria-label "Contents"); while the drawer is open it shows a back arrow (aria-label "Back to
  the page"). Icons are inline SVG swapped by `aria-expanded` in CSS. Content and drawer get 88px bottom padding so their last rows
  clear the button.
- **Content column:** `--col-w`; the file's HTML; headings get a hover "#" copy-link anchor; prev/next file links at the bottom; footer
  line "Built from steeb-k/secplus-study-guide @ <sourceCommit> · <builtAt date> · Edit this file on GitHub" (link to the md). No banner
  above chapters.

## Page behavior
- **Routes:** `#/` → Exam Overview. `#/<file-slug>` → that file. `#/<file-slug>/<heading-id>` → file + scroll to heading (offset for the
  sticky header via `scroll-margin-top`). `#/<file>/<sectionId>?hl=<key>` → View in context for a highlight (below). `#/highlights` → Highlighted page.
  `#/how-to` → "How to use this guide" (static page from `<template id="g-howto">` in guide/index.html, written conversationally, NOT
  built from the markdown repo: edit it there when features change; styled by `.g-howto`). Unknown → Exam Overview. Document title =
  "<section title> · Sec+ 701 Guide". `page` in guide.js is 'highlights' | 'howto' | null.
- **Scrolling:** every programmatic scroll glides (`behavior: 'smooth'`): section links within the chapter being read, the hash-anchor
  copy links, search hits (`highlightHit`), the sidebar's auto-scroll to the current entry (`revealCur()`) and to the selected search
  result. `motion()` in guide.js returns `'instant'` instead for the first render, for a change of chapter or page (new content under
  the reader) and under `prefers-reduced-motion: reduce`. Because a smooth scroll arrives later, `spyHold` for View in context stores
  the start and the resting position (`restY()`, the element's top minus its `scroll-margin-top`, clamped to the page's scroll range):
  the scrollspy keeps the target section marked while the window is between the two and after it arrives, and releases the hold once
  the reader scrolls away.
- **Last section remembered:** `localStorage['secplus.guide.last']` holds the last section in view (`#/<slug>/<heading-id>`, written by
  the scrollspy when it changes) or `#/highlights` / `#/how-to`. Opening the guide with no hash (the header's Guide link) restores it via
  `history.replaceState` before the first route render; an explicit `#/` still opens the overview. Deep links are unaffected.
- **Sidebar contents, top to bottom:** search box (placeholder "Search guide… ( / )"); the links "How to use this guide" (question-mark
  icon in the accent color) and "Highlighted (N)" (always present; N may be 0); the tree: each file as a top-level entry, the current
  file expanded to show its H2s (and H3s under the active H2), other files collapsed; scrollspy marks the H2/H3 in view (`a.cur`) and
  the active H2 (`li.active`); below the tree the "Weak spots" block (see Readiness).
- **Tooltips:** after rendering, text nodes are walked (skipping `pre`, `code`, `a`, `abbr`, `h1`, and the acronyms file's own key column) and wrapped:
  - acronyms present in `window.SEC_ACRONYMS` (longest key first; boundaries = start/end or non-alphanumeric; case-sensitive; a trailing
    lowercase "s" or "v<digits>" is allowed): `<abbr class="tip" tabindex="0" data-tip="<expansion>" data-acr="KEY">KEY</abbr>`. The
    acronym is wrapped even when its expansion sits next to it in parentheses.
  - objective references: text matching `/\b(?:objective|objectives|see|per)\s+(\d)\.(\d+)\b/i`, and bare `(d.n)` inside parentheses,
    get the `d.n` part wrapped as `<a class="xref" href="#/<file-slug-of-domain d>/obj-d-n">d.n</a>`. Version-like text (TLS 1.3,
    CVSS 3.1, 800-63B-4) never matches.
  - Tooltip UI: one floating `div.tooltip` reused; shown on mouseenter/focus of `.tip`, hidden on mouseleave/blur/Escape/scroll; on
    touch, tap toggles. Positioned below the word, flipped above near the viewport bottom, clamped horizontally, 8px gap, small caret,
    max-width 320px. Body: line 1 `<b>KEY</b> expansion`; line 2 the meaning from `acronymMeta` in `--ink-2` (13px), when the 91 table
    has the row; line 3 an "Acronyms list ↗" link to `#/acronyms/<acr-id>` when an anchor exists. Without a 91 row the expansion comes
    from `window.SEC_ACRONYMS`. `.tip` style: `text-decoration: underline dotted; text-decoration-thickness: 1px; text-underline-offset: 3px;
    cursor: help`, color `--ink-2` → `--ink` on hover. Enter on a focused `.tip` opens its acronym row.
- **Search:** index built from `sections` (title + text) and from the acronym glossary. Typing (debounced 80ms) replaces the tree with a
  results panel: first an "Acronyms" group (key or expansion match, up to 5), then "Sections" (up to 20) ranked by title match > count
  of query tokens in text > shorter section; each result shows the breadcrumb path and a snippet with the first match in `<mark>`.
  ↑/↓ moves, Enter opens. Opening a result navigates and, if the query matched body text, briefly highlights the first match in the
  content. The query and the results STAY in the sidebar after opening one (the opened item is the selected one), and the results list
  keeps its scroll position: `revealCur()` in guide.js (the sidebar's auto-scroll to the current outline entry) does nothing while
  `#g-tree` is hidden. A row above the results (`#g-res-top`) shows "N results" and a "Back to outline" button; `backToOutline()` is the
  single path used by that button, Escape, and emptying the box, and `clearResults()` calls `revealCur()` so the outline comes back
  scrolled to the current entry. "/" focuses the box when not in an input.
- **Readiness marks:** read `localStorage['secplus.attempts']` (same origin as the quiz). For each objective, take the last 5 attempts
  that include it and compute points/count → pct. A 7px dot before each objective H2 in the sidebar: `--ok` ≥ 83%, `--warn` ≥ 70%,
  `--bad` < 70%, none without data; dot `title` = "72% over N questions". "Weak spots" lists the bottom 5 objectives with data as links.
  Junk entries in storage are skipped; if localStorage is unavailable nothing is shown.
- **Keyboard:** `/` search, Escape closes drawer/results/tooltips, `[` / `]` previous/next file.
- **Boot status:** `document.documentElement.dataset.ready="1"` and `#boot-status` text "files=9 sections=N acronyms=M errors=0"
  (errors counted via window.onerror like the quiz page) so `tests/smoke.sh guide/index.html` can assert it.

## Highlights
- Highlightable blocks inside `.g-doc`: `p`, `li`, `blockquote`, `tr` (table rows), excluding the footer. Each block gets a stable key
  at render: `file + ':' + sectionId + ':' + hash(normalized text)`, stored in `data-hl`. The normalized text is the block's own text
  (a list item's child nodes concatenated with no separator, nested lists excluded), lower-cased, whitespace-collapsed, first 240 chars.
  Identical blocks in one section get `key~2`, `key~3` in document order.
- Gutter control: `button.hl-btn` in the left gutter of each block (left: -30px; 22px square; inline SVG marker icon; `aria-label`
  "Highlight this paragraph" / "Remove highlight"; `aria-pressed`). Visible on block hover (a nested list item reveals only its own
  button, via `:has()`) and on focus; on `(hover: none)` devices always visible at 45% opacity. Space/Enter toggle when it has focus.
  For table rows the first cell of every highlightable row, and the first header cell, get 32px left padding and the button sits there.
- Highlighted style: `background: var(--hl-tint)`; `box-shadow: inset 3px 0 0 var(--hl)` (left bar); for `tr`, applied to its cells.
  Tokens (guide.css): dark `--hl: #f2d383; --hl-ink: #f2d383; --hl-tint: rgba(242,211,131,.16)`; light `--hl: #9c7a1f; --hl-ink: #6b5108;
  --hl-tint: rgba(156,122,31,.14)`. Links inside a highlighted block and on the Highlighted page use `--accent-hi` so they keep ≥ 4.5:1
  on the tint; `--hl-ink` is the badge color.
- Storage: `localStorage['secplus.highlights']` = `{ [key]: { file, section, heading, text, at } }`; `text` is the first 300 chars of the
  block's text, ending in "…" when cut; `at` is an ISO time. The store is a prototype-less object, `__proto__` keys are dropped on load,
  and `?hl=` lookups use own properties only. Every read/write is guarded: a refused write (quota, storage disabled) keeps the change for
  the visit and the live region says "not saved". A `storage` event from another tab redraws an open Highlighted page.
- Section marks: any H2/H3 whose section contains ≥ 1 highlight gets `span.hl-mark` after its text (the marker icon at 14px in `--hl`,
  `title="N highlighted"`); the sidebar entry for that section and for its chapter shows a count badge. Marks update live on toggle.
- Highlighted page (`#/highlights`): grouped by chapter (file order) → section (document order). Each item shows the saved text
  (clamped to ~6 lines), a "View in context" link (`#/<file>/<sectionId>?hl=<key>`: navigates, scrolls the block into view below the
  header, flashes it 1.5s as a cell/block background in the accent tint, and keeps the section marked in the sidebar even when the
  block is too near the chapter end to reach the top; Back returns to the Highlighted page) and a remove button. Items whose block no
  longer exists in the current build are listed in a final "No longer found" group with their saved text, a remove button, and "View
  in context" to the section (no flash) while the section still exists. "Highlighted (N)" counts valid items plus orphans. Toolbar:
  "Export as Markdown" (downloads `secplus-highlights.md`: `# Highlights`, `## <chapter>`, `### <section>`, `> text` blocks) and "Clear
  all" (inline confirm; an unanswered confirm is reset when the page is left). Empty state explains how to highlight.
- Export text is Markdown-safe: backslash, backtick, `*`, `<`, `[`, `]`, word-boundary `_`, entity-like `&` and a leading `#`, `>`,
  `-`, `+` or `1.` are backslash-escaped, so "<script>" or "****-1234" render literally and the file never contains raw HTML.

## Quiz-site integration
- The shared header's "Guide" link opens `guide/index.html` (always named: a bare `guide/` opens a directory listing from file://).
- Practice-mode feedback panel and results review: the "Objective d.n: …" line is a link to `guide/index.html#/<domain-file-slug>/obj-d-n`
  (target `_blank`, rel noopener). Exam mode shows no objective.

## Tests (all must pass)
- `node tests/guide-core.test.js`: slugify; heading-id rules (obj ids, de-dup); tokenizeForTips boundary cases ("MAC address" lowercase
  no-match, "CAs" plural, "SNMPv3", "TACACS+", "CI/CD", skip inside code); objective-ref regex (matches "objective 4.8", "see 5.2",
  "(1.4)"; rejects "TLS 1.3", "CVSS 3.1", "800-63B-4"); search ranking (title match first; AND semantics; snippet contains <mark>);
  readinessByObjective (last-5 window, pct, no data → absent); hlKey, groupHighlights (grouping, orphans), highlightsMarkdown, mdText.
- `bash tests/guide-sync.sh` → OK when guide/data/guide.js matches the md sources.
- `node tests/guide-ui.test.js` → headless Chromium: deep-link offset, sidebar indent and under-header scrolling, shared header positions
  on guide and practice pages (1280/1000/390), pill wording and links, last-section memory, search persistence and scroll position,
  tooltips in viewport and on touch, readiness with junk data, highlights (toggle, reload, badges, Highlighted page, View in context,
  export escaping, quota errors, crafted `?hl=`), light-theme contrast, phone drawer and contents button, ordering-PBQ swap animation,
  no requests outside the site.
- `bash tests/smoke.sh guide/index.html` → boot-status, Exam Overview rendered, tooltips present, no external URLs, zero console errors.

## Build + sync workflow
```
python3 meta/build-full.py     # STUDY-GUIDE-FULL.md
python3 meta/build-site.py     # ../steeb-k.github.io/sec-plus-test/guide/data/guide.js
cd ../steeb-k.github.io/sec-plus-test && bash tests/guide-sync.sh && bash tests/smoke.sh guide/index.html
```
Run this after ANY markdown edit, then commit both repos.
