# sec-plus-test visual design spec — dark pastel, IBM Plex

A calm, dark-pastel design. Dark is the designed default; light uses the same hues on neutral paper. No gradients, no
glassmorphism (the frosted header is the one blur), no emoji, no drop-shadow stacks, no saturated blues.

## Fonts — self-hosted IBM Plex, zero CDN
- Files live at the repo root so other projects can share them: `/home/steeb/steeb-k.github.io/fonts/ibm-plex/`
  - `IBMPlexSans-Regular.woff2`, `IBMPlexSans-Italic.woff2`, `IBMPlexSans-Medium.woff2`, `IBMPlexSans-SemiBold.woff2`
  - `IBMPlexMono-Regular.woff2`, `IBMPlexMono-Medium.woff2`
  - `plex.css` with the `@font-face` rules (`font-display: swap`, latin + latin-ext only), `OFL.txt` (license).
- `sec-plus-test/index.html` links `../fonts/ibm-plex/plex.css`; `guide/index.html` and `tests/dev.html` link `../../fonts/ibm-plex/plex.css`.
  Each page preloads Sans-Regular and Sans-SemiBold (`<link rel="preload" as="font" type="font/woff2" crossorigin>`, skipped on file://).
- Stacks: `--font-sans: "IBM Plex Sans", system-ui, sans-serif;` `--font-mono: "IBM Plex Mono", ui-monospace, monospace;`
- Hard rule: no `http://` / `https://` in link, script or preload tags, no `@import`, no `fonts.googleapis`, no `cdn`. The only external
  URLs are the GitHub links (header, home "Source", guide footer). `tests/smoke.sh` enforces this.

## Palette (chosen from tests/palette-sampler.html: graphite / black / bright / sky / vivid)
Dark (default)
```
--bg-0:#080808  --bg-1:#141414  --bg-2:#1f1f1f  --bg-3:#2b2b2b   --hdr-bg: rgba(20,20,20,.45)
--line:#292929  --line-strong:#3d3d3d
--ink:#f0f0f0   --ink-2:#bdbdbd  --ink-3:#999999
--accent:#9cc3e6  --accent-hi:#b7d6f0  --accent-ink:#080808  --accent-tint:rgba(156,195,230,.14)
--ok:#8fe0a6  --bad:#f29aa1  --warn:#f2d383  (tints at .14)   --info = accent   --shadow: none
```
Light (neutral paper, same structure; `[data-theme="light"]` or `prefers-color-scheme: light` without a stored theme)
```
--bg-0:#f3f3f3  --bg-1:#fbfbfb  --bg-2:#eeeeee  --bg-3:#e3e3e3   --hdr-bg: rgba(251,251,251,.5)
--line:#dedede  --line-strong:#c8c8c8
--ink:#161616   --ink-2:#505050  --ink-3:#666666
--accent:#2f6f9f  --accent-hi:#265d86  --accent-ink:#ffffff  --accent-tint:rgba(47,111,159,.10)
--ok:#2b7a45  --bad:#a8404b  --warn:#7d5f0a  (tints .10–.12)   --shadow: 0 1px 2px rgba(30,30,40,.06)
```
Print always uses a white-paper light palette (`@media print`), whatever the screen theme, and hides the header and actions.
Rationale: fully neutral grays (no hue cast), near-black depth and brighter ink for separation; pastels only on accent/status.
To revisit, open `sec-plus-test/tests/palette-sampler.html` and report the code shown in the top-right.
The guide adds highlight tokens `--hl`, `--hl-ink`, `--hl-tint` in guide.css (see GUIDE-SITE.md "Highlights").

## Type scale
Base 16px / line-height 1.55, body color `--ink`. h1 26px/600 letter-spacing -0.01em (22px under 560px); h2 20px/600; h3 16px/600;
small/meta 13.5px `--ink-2`; uppercase labels 11.5px/500, letter-spacing .07em, `--ink-3`.
Mono (`--font-mono`): timer, question counter, keyboard number chips, acronym keys, scores in tables, the pill's exam code.

## Shape, surface, spacing
Radii: `--r-card` 10px, `--r-btn` 8px (buttons, inputs, selects, fieldsets), `--r-chip` 6px (chips, grid cells). Borders 1px `--line`;
hover `--line-strong`. Cards and panels = `--bg-1` on page `--bg-0`; inputs/options = `--bg-2`.
Spacing scale `--s1…--s7` = 4/8/12/16/24/32/48px.
Layout tokens: `--page-w` 1240px (header grid and guide layout), `--side-w` 280px (sidebar column), `--col-w` 820px (reading column on
every page: `main` on practice pages, the content column of the guide). Gutters 24px; 16px below 900px.
Focus: `:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px }` everywhere; outlines are never removed.
Motion: `.opt, .btn, .card, .cell` transition border/background .12s only under `prefers-reduced-motion: no-preference`.

## Site header (shared by the practice page, the guide and tests/dev.html)
Markup on every page: `header.site-header > div.hwrap > a.brand + div.hnav > nav`, followed directly by `<script src="js/header.js">`
(`../js/header.js` from guide/ and tests/). The header is sticky (z-index 5), `--bg-1` with a 1px bottom `--line`; where
backdrop-filter is supported it is `--hdr-bg` with `blur(14px) saturate(1.15)` so content slides beneath it.
- `.hwrap` is a `--page-w` grid of `--side-w` + content column; the pill sits 16px into the first column; the nav is right-aligned
  inside a `--col-w` box centered in the content column. The practice page has no sidebar but uses the same grid, so pill and links
  sit at identical pixel positions on every page (guide-ui.test.js checks 1280, 1000 and 390). Below 900px the wrapper is a flex row
  with 16px gutters and the nav gap tightens to `--s3`.
- Nav links: Guide, Practice (same tab; `aria-current="page"` marks the section you are in, underlined in `--accent`), GitHub (study-guide
  repo, new tab, inline external-link icon). Links are `--ink-2` → `--ink` on hover, weight 500. History and Settings live on the
  practice home page only.
- The pill links to `#/` on both pages: the practice home on the practice page, the Exam Overview on the guide. It never switches sections.

### Header wordmark
- The brand is a single two-segment pill reading **"Security+ | SY0-701"**. The pages' `<title>` strings stay short: "Sec+ 701",
  "Sec+ 701 Guide", "<section> · Sec+ 701 Guide".
- Markup: `<a class="brand" href="#/" aria-label="Security+ SY0-701 home"><span class="brand-pill"><span class="brand-l"><span class="brand-full">Security+</span><span class="brand-abbr">Sec+</span></span><span class="brand-r"><span class="brand-full">SY0-701</span><span class="brand-abbr">701</span></span></span></a>`.
- Fit: the pill shows "Security+ | SY0-701" whenever it fits. "Fits" means the nav neither runs into the pill nor past the header's
  right edge. When it does not, `js/header.js` steps the header's `data-brand` down only as far as needed: `short` → "Sec+ | SY0-701",
  then `tiny` → "Sec+ | 701" (narrow phones). CSS toggles the `.brand-full` / `.brand-abbr` spans inside each segment; `.brand-pill`
  and the nav are `white-space: nowrap` so nothing ever wraps to a second line. Measured on load, on resize and on
  `document.fonts.ready`; both pages load the same script, so their pills always agree.
- `.brand-pill`: inline-flex, border-radius 999px, a 1.5px outline in `--ink` drawn as a spread box-shadow (Chromium snaps border widths
  to whole pixels), background `--ink`, 1.5px margin, overflow hidden so the segments clip to the pill shape, font-weight 600, 14px,
  line-height 1, letter-spacing .01em. In light theme the same tokens give a dark/paper inversion with the same structure. Under
  `forced-colors` the shadow becomes a 1px CanvasText border.
- `.brand-l` ("Security+" / "Sec+"): background `--ink`, text `--bg-0`, padding 5px 10px 5px 12px.
- `.brand-r` ("SY0-701" / "701"): background `--bg-0`, text `--ink`, padding 5px 12px 5px 10px, font-family `--font-mono`.
- The outline runs around the whole pill; there is no inner divider beyond the color change. No hover color change; the whole link gets
  the standard focus ring. The practice home's h1 "Security+ SY0-701 practice" is visually hidden (`.sr`) and kept for screen readers.

## Favicon
`icons/favicon.svg` (plus `favicon.ico` 16/32/48, `favicon-32.png`, `apple-touch-icon.png`), regenerated by
`python3 icons/make-favicon.py [outline] [divider-x] [S-height] [plus-height]` in the site folder (defaults 32 300 250 150)
followed by rsvg-convert / magick. Shape: a 512px squircle (rx 133) in `#f0f0f0` with an inset black (`#080808`) segment on
the right (clipped to the inner rounded rect), "S" in Plex Sans SemiBold on the white side, "+" in white on the black side.
Same idea as the header pill: the white outline and the "S" segment are a single shape. Glyph outlines come from the self-hosted font.

## Components (practice page)
- Buttons: primary = `--accent` bg, `--accent-ink` text, hover `--accent-hi`; secondary = transparent, 1px `--line-strong`, `--ink`;
  danger = transparent with `--bad` border/text; disabled 45% opacity. Min height 40px, 44px on touch widths.
- Domain cards: title 600, meta line `--ink-2`, readiness badge = pastel chip (`--ok-tint`/`--ok`, `--warn-tint`/`--warn`,
  `--bad-tint`/`--bad`, neutral `--bg-3`/`--ink-2`). Final Exam card gets a 3px top rule in `--accent` (not a full border).
- Home footer nav: History, Settings, Source (GitHub, new tab) as secondary buttons. A "Resume in-progress …" banner (`.banner`,
  accent tint and border) appears above the cards while a session exists.
- Question card: stem 17px; options are full-width rows on `--bg-2`, 1px `--line`; hover `--line-strong`; keyboard chip (mono,
  `--bg-3`, `--ink-2`) left; selected = `--accent` border + `--accent-tint` bg; correct = `--ok` border + `--ok-tint`; incorrect =
  `--bad` border + `--bad-tint`; correct/incorrect marks are inline SVG in the matching color at the right.
- Feedback panel: left 3px rule in `--ok` or `--bad`, bg = matching tint, "Correct"/"Incorrect" 600 in the hue, explanation `--ink`,
  objective line `--ink-2` linking into the guide, acronym block: uppercase label, keys in mono 600 `--ink`, expansions `--ink-2`.
- Review grid: 36px cells, mono numbers; answered = `--accent-tint` bg + `--accent` border; unanswered = dashed `--line-strong`;
  flagged = `--warn` border + small corner triangle in `--warn`; current = 2px `--accent` ring. Legend chips reuse the same styles.
- Timer: mono 18px; `.low` (`--warn`) under 10 minutes, `.crit` (`--bad`) under 2 minutes; the class is applied on route render and
  every 500ms tick. Pause button secondary; while paused the question is hidden behind a "Paused" panel.
- Results: big score in mono 40px/500; pass pill `--ok-tint`/`--ok`, fail pill `--bad-tint`/`--bad`; per-domain table: thin rules,
  right-aligned mono numbers, a 6px bar in `--accent` on a `--bg-3` track (bars hidden under 560px); weakest objectives table the same.
- History: table rows with `--line` separators, readiness chips, bars as above, no chart library. Tables sit in `.table-wrap`
  (horizontal scroll inside the card when needed).
- Settings: grouped panels, checkboxes/radios use `accent-color: var(--accent)`.
- PBQ: match selects and config dropdowns styled as inputs (`--bg-2`, 1px `--line`, `--r-btn`). Config PBQs are stacked rows
  (`.pbq-rows`) whose fields wrap, so every dropdown is visible at any width. Ordering PBQs are a numbered list of rows (`.pbq-order li`,
  `--bg-2`, 1px `--line`, 54px min height, the position number in a `--bg-3` chip) with Up/Down secondary buttons that wrap under the
  text on phones.
- Theme: default setting `dark` (settings offer auto / light / dark); `body` has an explicit background in both themes. The guide reads
  the same `secplus.settings` theme before first paint.
- Scrolling: moving to the previous/next question (or jumping from the review grid) scrolls the window back to the top smoothly
  (`behavior: 'smooth'`, instant under `prefers-reduced-motion: reduce`). Opening a different page (`paint()` on a route change) starts
  at the top instantly, since the content under the reader is new.

### Ordering PBQs: swap animation
Pressing Up or Down re-renders the question, but `animateSwap()` in app.js measures the rows' tops before the re-render and afterwards
plays the difference on the two rows that changed places (Web Animations API, 240ms, `cubic-bezier(.2,.7,.2,1)`, translateY only), so
the two items visibly slide past each other. The moved row carries `.swapped` for 450ms: accent border (`border-color .3s` transition
under `prefers-reduced-motion: no-preference`) and `z-index: 1` so it passes over the other row. With reduced motion the slide is skipped
and only the tint shows. Focus follows the moved row's button (`po<pos>u` / `po<pos>d`).
