# sec-plus-test visual design spec (v2 — dark pastel, IBM Plex)

Goal: replace the generic "AI default" look (saturated blue primary, pure-white cards, Inter/system sans) with a calm,
dark-pastel design. Dark is the designed default; light remains available and uses the same hues on warm paper.
No gradients, no glassmorphism, no emoji, no drop-shadow stacks, no saturated #2563eb-style blues anywhere.

## Fonts — self-hosted IBM Plex, zero CDN
- Files live at the repo root so other projects can share them: `/home/steeb/steeb-k.github.io/fonts/ibm-plex/`
  - `IBMPlexSans-Regular.woff2`, `IBMPlexSans-Italic.woff2`, `IBMPlexSans-Medium.woff2`, `IBMPlexSans-SemiBold.woff2`
  - `IBMPlexMono-Regular.woff2`, `IBMPlexMono-Medium.woff2`
  - `plex.css` with the `@font-face` rules (`font-display: swap`, latin + latin-ext only), `OFL.txt` (license).
- `sec-plus-test/index.html` links `../fonts/ibm-plex/plex.css`; `sec-plus-test/tests/dev.html` links `../../fonts/ibm-plex/plex.css`.
  Add `<link rel="preload" as="font" type="font/woff2" crossorigin>` for Sans-Regular and Sans-SemiBold.
- Stacks: `--font-sans: "IBM Plex Sans", system-ui, sans-serif;` `--font-mono: "IBM Plex Mono", ui-monospace, monospace;`
- Hard rule: grep the whole sec-plus-test folder and plex.css for `http://` / `https://` — the only allowed external URL is the
  GitHub "Source" link on the home page. No `@import`, no `fonts.googleapis`, no `cdn`.

## Palette (v3 — chosen from tests/palette-sampler.html: graphite / black / bright / sky / vivid)
Dark (default)
```
--bg-0:#080808  --bg-1:#141414  --bg-2:#1f1f1f  --bg-3:#2b2b2b
--line:#292929  --line-strong:#3d3d3d
--ink:#f0f0f0   --ink-2:#bdbdbd  --ink-3:#999999
--accent:#9cc3e6  --accent-hi:#b7d6f0  --accent-ink:#080808  --accent-tint:rgba(156,195,230,.14)
--ok:#8fe0a6  --bad:#f29aa1  --warn:#f2d383  (tints at .14)   --info = accent
```
Light (neutral paper, same structure)
```
--bg-0:#f3f3f3  --bg-1:#fbfbfb  --bg-2:#eeeeee  --bg-3:#e3e3e3
--line:#dedede  --line-strong:#c8c8c8
--ink:#161616   --ink-2:#505050  --ink-3:#666666
--accent:#2f6f9f  --accent-hi:#265d86  --accent-ink:#ffffff  --accent-tint:rgba(47,111,159,.10)
--ok:#2b7a45  --bad:#a8404b  --warn:#7d5f0a  (tints .10–.12)
```
Rationale: fully neutral greys (no hue cast), near-black depth and brighter ink for separation; pastels only on accent/status.
To revisit, open `sec-plus-test/tests/palette-sampler.html` and report the code shown in the top-right.

## Type scale
Base 16px / line-height 1.55, body colour `--ink`. h1 26px/600 letter-spacing -0.01em; h2 20px/600; h3 16px/600;
small/meta 13.5px `--ink-2`; uppercase labels 11.5px/500, letter-spacing .07em, `--ink-3`.
Mono (`--font-mono`): timer, question counter, keyboard number chips, acronym keys, scores in tables, code/log snippets in stems
(render stems' `code`-like lines in mono if the app marks them; otherwise leave).

## Shape and surface
Radii: cards 10px, buttons/inputs 8px, chips 6px, grid cells 6px. Borders 1px `--line`; hover `--line-strong`.
Shadows: none in dark; light may use `0 1px 2px rgba(30,30,40,.06)`. Cards = `--bg-1` on page `--bg-0`. Inputs/options = `--bg-2`.
Spacing scale 4/8/12/16/24/32/48. Content column max 920px, 16px side gutters at phone width.

## Components
- Header: `--bg-1`, 1px bottom `--line`, title in 600, nav links `--ink-2` → `--ink` on hover, current route underlined with `--accent`.
- Buttons: primary = `--accent` bg, `--accent-ink` text, hover `--accent-hi`; secondary = transparent, 1px `--line-strong`, `--ink`;
  danger = transparent with `--bad` border/text; disabled 45% opacity. Min height 40px, 44px on touch widths.
- Focus: `outline: 2px solid var(--accent); outline-offset: 2px` everywhere; never remove outlines.
- Domain cards: title 600, meta line `--ink-2`, readiness badge = pastel chip (`--ok-tint`/`--ok` text, `--warn-tint`/`--warn`,
  `--bad-tint`/`--bad`, neutral `--bg-3`/`--ink-2`). Final Exam card gets a 3px top rule in `--accent` (not a full border).
- Question card: stem 17px; options are full-width rows on `--bg-2`, 1px `--line`; hover `--line-strong`; keyboard chip (mono,
  `--bg-3`, `--ink-2`) left; selected = `--accent` border + `--accent-tint` bg; correct = `--ok` border + `--ok-tint`; incorrect =
  `--bad` border + `--bad-tint`; ✓/✗ glyphs in the matching colour at the right (use text glyphs or inline SVG, no emoji).
- Feedback panel: left 3px rule in `--ok` or `--bad`, bg = matching tint, "Correct"/"Incorrect" 600 in the hue, explanation `--ink`,
  objective line `--ink-2`, acronym block: label uppercase style, keys in mono 600 `--ink`, expansions `--ink-2`, separators `--ink-3`.
- Review grid: 36px cells, mono numbers; answered = `--accent-tint` bg + `--accent` border; unanswered = dashed `--line-strong`;
  flagged = `--warn` border + small corner triangle in `--warn`; current = 2px `--accent` ring. Legend chips reuse the same styles.
- Timer: mono 18px; turns `--warn` under 10 min, `--bad` under 2 min. Pause button secondary.
- Results: big score in mono 40px/500; pass pill `--ok-tint`/`--ok`, fail pill `--bad-tint`/`--bad`; per-domain table: thin rules,
  right-aligned mono numbers, a 6px bar in `--accent` on a `--bg-3` track; weakest objectives table same.
- History: table rows `--line` separators, readiness chips, bars as above, no chart library.
- Settings: grouped panels, custom-styled checkboxes/radios using `accent-color: var(--accent)`.
- PBQ: match selects and config table cells styled as inputs (`--bg-2`, 1px `--line`, 8px radius); order list rows with Up/Down
  secondary buttons; table scrolls horizontally inside its card at phone width.
- Default theme setting = `dark` (settings still offer auto / light / dark). Give `body` an explicit background in both themes.

## Header wordmark (user request, revised)
- The brand is a single two-segment pill reading **"Sec+ | 701"** (no "Prep"). The app's `<title>` is "Sec+ 701".
- Markup: `<a class="brand" href="#/" aria-label="Sec+ 701 home"><span class="brand-pill"><span class="brand-l">Sec+</span><span class="brand-r">701</span></span></a>`.
- `.brand-pill`: inline-flex, border-radius 999px, 1.5px solid outline in "white" (`--ink`, i.e. off-white #e6e4dd in dark;
  in light theme also use `--ink` so the pill is a dark/paper inversion with the same structure), overflow hidden so the
  segments clip to the pill shape, font-weight 600, 14px, line-height 1, letter-spacing .01em.
- `.brand-l` ("Sec+"): background `--ink` (white segment), text colour `--bg-0` (page background), padding 5px 10px 5px 12px.
- `.brand-r` ("701"): background `--bg-0` (dark segment), text colour `--ink`, padding 5px 12px 5px 10px, font-family `--font-mono`.
- The outline runs around the whole pill; there is no inner divider line beyond the colour change (the "|" in the request is the
  segment boundary, not a literal character).
- No hover colour change; the whole link gets the standard focus ring. Replace every remaining "Security+ Practice"/"Sec+ Prep"
  string; the home h1 reads "Security+ SY0-701 practice" in normal heading style under the header.
