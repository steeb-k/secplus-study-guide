# Question bank schema (authoritative)

All bank files are plain browser scripts (no modules, no JSON files). They are loaded by `index.html` **after**
`data/objectives.js` and **before** the app scripts.

## MCQ files: `data/domain1.js` … `data/domain5.js`
```js
// data/domain3.js
window.SEC_BANK = window.SEC_BANK || [];
window.SEC_BANK.push(
  {
    id: "d3-001",                 // "d<domain>-<3 digit>", unique across all files, sequential within file
    domain: 3,                    // 1..5
    objective: "3.2",             // must exist in window.SEC_OBJECTIVES[domain].objectives
    type: "single",               // "single" | "multi"
    question: "A security engineer needs to inspect HTTPS traffic for SQL injection attempts before it reaches a public web server. Which of the following should be deployed?",
    options: [                    // 4 options normally; 5–6 allowed for multi. Plain strings, no "A." prefixes.
      "Layer 4 firewall",
      "WAF",
      "Jump server",
      "Load balancer"
    ],
    answer: [1],                  // array of 0-based indexes into options. single → exactly 1; multi → 2 or 3
    explanation: "A web application firewall operates at layer 7 and understands HTTP(S) semantics, so it can detect injection payloads. A layer 4 firewall only sees ports/addresses; a jump server is for administrative access; a load balancer distributes traffic.",
    difficulty: 2,                // 1 easy recall, 2 scenario, 3 hard/trick
    tags: ["WAF", "firewall types"] // 1–4 short keywords, used for drill filtering and QA
  },
  // ...
);
```
Rules for writers:
- **Style = real exam.** Mostly scenario stems ("A company…", "Which of the following BEST…", "…MOST likely…", "FIRST", "LEAST").
  Capitalise the qualifier word (BEST/MOST/FIRST/LEAST/NOT) exactly as CompTIA does. Target mix per domain: ~25% difficulty 1,
  ~55% difficulty 2, ~20% difficulty 3. ~15% of questions `multi` ("Choose TWO." / "Choose THREE." must appear at the end of
  the stem, exactly in that form).
- Distractors must be plausible items from the same objective family (not obviously wrong, never jokes). No "All of the above",
  no "None of the above", no "Both A and B".
- Each objective sub-bullet family in the official SY0-701 list should be hit. Spread questions across every objective in the
  domain roughly proportional to the size of the objective's bullet list; **minimum 3 per objective**, and for the big domain 4
  objectives aim for 8–14 each.
- Explanation: 1–3 sentences, states why the right answer is right AND briefly why the key distractors are wrong. ≥ 60 chars.
- One unambiguous correct answer (or set). If a question could be argued two ways, rewrite it.
- No duplicated stems or near-duplicates within a domain. Vary the scenario industry (hospital, bank, SaaS, manufacturing, school, government, MSP).
- Option order inside the file does not matter (the app shuffles), but keep `answer` indexes correct.
- Escape double quotes inside strings or use single-quoted JS strings. No trailing-comma problems; the file must parse.

## PBQ file: `data/pbq.js`
```js
window.SEC_PBQ = window.SEC_PBQ || [];
window.SEC_PBQ.push(
  // type "match": each left item gets one choice from a shared list of right-hand options (dropdown). Right options may be
  // reused across left items unless `unique: true`. Score = correct left items / total left items.
  {
    id: "pbq-001", domain: 2, objective: "2.2", type: "match",
    title: "Identify the social engineering technique",
    instructions: "For each scenario, select the attack type that BEST describes it.",
    left: [
      "An email claiming to be from the CFO asks accounting to wire funds to a new vendor today.",
      "A caller claiming to be from the help desk asks a user to read back their MFA code.",
      "A fake site at examp1e.com harvests credentials from users who mistype the URL.",
      "A legitimate industry news site frequented by the target's staff is compromised to serve malware."
    ],
    right: ["Business email compromise", "Vishing", "Typosquatting", "Watering hole", "Smishing", "Pretexting"],
    answer: [0, 1, 2, 3],              // index into `right` for each `left` item
    unique: true,
    explanation: "BEC impersonates executives to redirect payments; vishing is voice phishing; typosquatting relies on look-alike domains; a watering hole compromises a site the targets already trust."
  },
  // type "order": arrange items into the correct sequence. UI gives Up/Down buttons (or number selects). Score = items in the
  // correct position / total.
  {
    id: "pbq-002", domain: 4, objective: "4.8", type: "order",
    title: "Incident response process",
    instructions: "Place the incident response phases in the correct order.",
    items: ["Containment", "Preparation", "Lessons learned", "Detection", "Recovery", "Eradication", "Analysis"],
    answer: [1, 3, 6, 0, 5, 4, 2],      // indexes of `items` in correct order
    explanation: "SY0-701 order: preparation, detection, analysis, containment, eradication, recovery, lessons learned."
  },
  // type "config": a table where each row has one or more cells to fill from per-column dropdowns. Score = correct cells / total cells.
  // Typical uses: firewall rule set, ACL ordering, port/protocol selection, selecting control type/category, log triage.
  {
    id: "pbq-003", domain: 4, objective: "4.5", type: "config",
    title: "Firewall rule set",
    instructions: "Complete the rules so that only HTTPS and SSH from the admin subnet reach the web server, and everything else is blocked. Rules are processed top-down.",
    columns: [
      { key: "action",   label: "Action",   choices: ["Allow", "Deny"] },
      { key: "source",   label: "Source",   choices: ["Any", "10.0.50.0/24", "10.0.10.5"] },
      { key: "dest",     label: "Destination", choices: ["Any", "10.0.10.5"] },
      { key: "port",     label: "Port",     choices: ["22", "80", "443", "Any"] }
    ],
    rows: [
      { label: "Rule 1", fixed: { },                       answer: { action: "Allow", source: "Any",          dest: "10.0.10.5", port: "443" } },
      { label: "Rule 2", fixed: { },                       answer: { action: "Allow", source: "10.0.50.0/24", dest: "10.0.10.5", port: "22" } },
      { label: "Rule 3", fixed: { source: "Any", dest: "Any", port: "Any" }, answer: { action: "Deny" } }
    ],
    // `fixed` cells are shown read-only and not scored; `answer` lists only the scorable cells for that row.
    explanation: "Specific allows go first; the implicit/explicit deny-all goes last. SSH must be limited to the admin subnet."
  }
);
```
PBQ writer rules: ~20 PBQs total, at least 3 per domain, mix of the three types (≥ 5 of each). Keep each solvable in 2–4
minutes. Every PBQ has an `explanation`. For `config`, every row's `answer` keys must be a subset of column keys and every
answer value must be in that column's `choices`. For `order`, `answer` must be a permutation of all item indexes. For `match`,
`answer.length === left.length` and each value indexes `right`.

## `data/objectives.js` (already written; shape is fixed)
```js
window.SEC_OBJECTIVES = {
  1: { name: "General Security Concepts", weight: 0.12, objectives: { "1.1": "Compare and contrast various types of security controls", ... } },
  ...
};
window.SEC_EXAM = { totalQuestions: 90, pbqCount: 5, mcqPerDomain: {1:10, 2:19, 3:15, 4:24, 5:17}, minutes: 90, passScaled: 750 };
```
