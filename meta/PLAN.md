# Security+ SY0-701 Study Kit — Build Plan

Owner: steeb. Planned by a lead agent, implemented by writer agents, debugged/QA'd by reviewer agents.

## Decisions (confirmed with user)
- Exam: **CompTIA Security+ SY0-701** (90 questions max, 90 minutes, scaled 100–900, pass 750).
- Study guide: **Markdown, one file per domain**, in `/home/steeb/security+-study/`.
- Quiz site: static, **`/home/steeb/steeb-k.github.io/sec-plus-test/`**, served at `https://steeb-k.github.io/sec-plus-test/`.
- Bank size: **~100 MCQ per domain (500 total) + ~20 simplified PBQs**.
- PBQs: simplified (match / order / config-table), no drag-and-drop.
- Features: practice mode (instant feedback) + exam mode, flag & review, missed-question drill, score history dashboard.
- Scoring: percent + estimated scaled score (linear: `100 + round(pct * 800)`), pass line 750 (≈ 81.25%). Per-domain breakdown.
- Persistence: localStorage, with JSON export/import. In-flight exam state saved on every answer so the user can walk away.
- Deploy: commit and push to `steeb-k/steeb-k.github.io`.

## Deliverable 1 — Study guide (`/home/steeb/security+-study/`)
```
README.md                                  index, how to use, exam logistics, link to quiz site
00-exam-overview.md                        format, domains & weights, scoring, PBQ strategy, test-day tactics
01-general-security-concepts.md            Domain 1 (12%) objectives 1.1–1.4
02-threats-vulnerabilities-mitigations.md  Domain 2 (22%) objectives 2.1–2.5
03-security-architecture.md                Domain 3 (18%) objectives 3.1–3.4
04-security-operations.md                  Domain 4 (28%) objectives 4.1–4.9
05-program-management-oversight.md         Domain 5 (20%) objectives 5.1–5.6
90-ports-protocols.md                      ports/protocols cheat sheet (secure vs insecure pairs)
91-acronyms.md                             SY0-701 acronym list with one-line definitions
92-formulas-and-numbers.md                 SLE/ALE/ARO, RTO/RPO/MTTR/MTBF, key lengths, CVSS ranges, etc.
```
Style: meat-and-potatoes. Reader already knows most of the material. Every file follows the official
objective numbering exactly (e.g. `## 1.2 Summarize fundamental security concepts`) and every sub-bullet in the
objectives gets at least a one-line definition **framed the way the exam tests it**. Use tables for
compare/contrast sets (control categories × types, symmetric vs asymmetric, hot/warm/cold, SLA/MOU/MOA/MSA/SOW/NDA/BPA,
MAC/DAC/RBAC/ABAC/rule-based, SAML/OAuth/OIDC/LDAP, IDS vs IPS, etc.). Add `> **Exam tip:**` callouts for
commonly-confused pairs and "keyword → answer" patterns. End each domain with "Most-tested distinctions" (10–20 bullets).
No fluff, no history lessons, no motivational text.

## Deliverable 2 — Quiz site (`/home/steeb/steeb-k.github.io/sec-plus-test/`)
```
index.html            single page app shell; loads css + data + js via plain <script> tags (no build, no modules, no fetch)
css/style.css         dark-mode-aware, responsive, keyboard friendly
js/storage.js         localStorage wrapper, schema versioning, export/import JSON
js/engine.js          pure logic: question selection, shuffling, scoring, scaled score, PBQ grading, final-exam composition
js/pbq.js             PBQ renderers + answer capture for types: match, order, config
js/ui.js              rendering helpers, screens, review grid, results, dashboard
js/app.js             router (hash-based), session lifecycle, timer, resume-on-load, wiring
data/objectives.js    domain names, weights, objective titles  (WRITTEN BY LEAD — do not change shape)
data/domain1.js … domain5.js   MCQ banks; each file does `window.SEC_BANK.push(...questions)`
data/pbq.js           PBQ bank; `window.SEC_PBQ.push(...)`
tests/validate-bank.js   node script: schema + sanity validation of all banks (WRITTEN BY LEAD)
tests/engine.test.js     node script: unit tests for engine.js (selection counts, weights, scoring, PBQ grading)
tests/smoke.sh           headless chromium smoke test (page loads with zero console errors, banks loaded, counts right)
```
Everything must work from `file://` AND from GitHub Pages: therefore **no fetch(), no ES modules, no CDN dependencies**.
`engine.js` must be loadable in Node for tests: end it with
`if (typeof module !== 'undefined') module.exports = Engine;` and never touch `window`/`document` inside it.

### Question schema
See `QUESTION-SCHEMA.md` (authoritative). Validator: `node tests/validate-bank.js`.

### App behaviour spec
**Screens (hash routes):** `#/` home · `#/module/:d` module quiz setup · `#/final` final setup · `#/drill` missed drill ·
`#/quiz` active session · `#/results/:attemptId` results · `#/history` dashboard · `#/settings` export/import/reset.

**Home:** five domain cards (name, weight, questions in bank, last score, readiness badge), Final Exam card, Missed Drill card
(count of currently-missed questions), History link, link to study guide repo.

**Module quiz setup:** domain fixed; choose count (10 / 25 / 50 / all); choose mode (Practice = instant feedback with
explanation after each answer; Exam = feedback only at the end); optional "include PBQs for this domain" toggle (default on,
adds up to 2). Start.

**Final exam:** always Exam mode. Composition: 5 PBQs first (spread across domains, no two from the same objective if
avoidable), then 85 MCQs distributed by weight: D1 10, D2 19, D3 15, D4 24, D5 17 (=85). Timer 90:00 counting down,
shown top-right; **Pause** button; the timer only runs while the page is visible and not paused (store accumulated
elapsed ms + a `runningSince` timestamp; on `visibilitychange`→hidden or pause, fold elapsed and clear `runningSince`).
When the timer hits 0: auto-submit. A "strict timer" toggle in settings makes the clock keep running while away (default off).

**Selection (variety):** per question track `seen` count in storage. Module/final draws prefer least-seen questions:
sort by seen asc with random tie-break, take N, then shuffle order. Option order shuffled per presentation
(seeded by attemptId+questionId so it is stable on reload). Never present the same question twice in one session.

**Session UI:** question counter `Q 12 / 25`, domain + objective tag (hidden in Final exam mode? No — show the objective
tag only in Practice mode; exam mode hides it to match the real test), stem, options as large click targets (radio for
single, checkbox for multi with "Choose N" hint), Flag button, Prev/Next, "Review" button opening the review grid
(numbers coloured: answered / unanswered / flagged), Submit with confirmation listing unanswered count.
Keyboard: 1–6 select option, F flag, ←/→ navigate, Enter next/submit.
**Every answer change persists immediately** to `sec.session` in localStorage. On load, if a session exists, home shows a
"Resume in-progress <type>" banner; the session screen restores position, answers, flags, timer.

**Practice mode:** after locking an answer (click "Check"), show correct/incorrect, highlight correct option(s), show
explanation and objective ref. Then Next.

**Results:** percent, estimated scaled score with pass/fail vs 750, per-domain table (count, correct, %), per-objective
weak spots (bottom 5 objectives by %), time used, full review list: every question with your answer, correct answer,
explanation, filter buttons All / Missed / Flagged. Buttons: Retry missed from this attempt, Back to home.

**Missed drill:** all questions whose most recent result was wrong (or wrong ≥ correct lifetime), filterable by domain,
Practice mode. Getting one right removes it from the missed set.

**History dashboard:** table of attempts (date, type, domain, score %, scaled, pass?, duration) newest first; per-domain
summary row: attempts, best, last 3 average, readiness badge (green if last 3 module attempts all ≥ 83%, yellow if last ≥ 83%,
red otherwise); final exam summary (attempts, best scaled, passes). Simple CSS bar charts — no chart libraries.

**Settings:** export all data as JSON file download; import JSON (merge or replace); reset everything (confirm);
strict-timer toggle; theme (auto/light/dark).

**Scoring:**
- MCQ single: 1 if chosen index == answer.
- MCQ multi: 1 if chosen set == answer set exactly; else 0 (matches CompTIA — no partial credit on MCQ).
- PBQ: partial credit = correct cells / total cells, counts as 1 question-equivalent (so the final is out of 90).
- pct = points / total; scaled = 100 + round(pct * 800); pass = scaled >= 750.

### Storage keys (all JSON, prefix `secplus.`)
`secplus.version` (int) · `secplus.session` (active session or null) · `secplus.attempts` (array) ·
`secplus.qstats` ({qid: {seen, correct, wrong, lastCorrect:boolean, lastAt}}) · `secplus.settings`.

## Deliverable 3 — Tests
- `node tests/validate-bank.js` must exit 0 (schema, counts, unique ids, single answers have exactly 1, multi have 2–3 and
  stem says "Choose TWO"/"Choose THREE", explanation ≥ 60 chars, 4–6 options, objective ids valid, no duplicate stems,
  ≥ 95 MCQ per domain, ≥ 18 PBQs, every objective in objectives.js has ≥ 3 questions).
- `node tests/engine.test.js` must exit 0.
- `tests/smoke.sh` launches `chromium --headless` against `file://…/index.html`, asserts no console errors and bank counts.

## Orchestration
**Wave 1 (writers, parallel):** app builder (whole site with a 6-question sample bank it then deletes), 5 MCQ bank writers
(one per domain), 1 PBQ writer.
**Wave 2 (writers, parallel):** 5 domain guide writers, 1 writer for README/00/90/91/92.
**Wave 3 (reviewers, parallel):** app debugger (runs all tests, headless smoke, code review, fixes), 5 bank QA reviewers
(accuracy, ambiguity, duplicates, distractor quality, exam realism — fix in place), 2 guide QA reviewers (accuracy and
objective coverage).
**Wave 4 (lead):** final validation, git commit + push, summary to user.
