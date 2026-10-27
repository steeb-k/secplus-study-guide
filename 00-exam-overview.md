# 00 - Exam Overview

> **Note:** AI-generated content, not yet vetted for accuracy. See the README for details.

## Exam facts

| Item | Value |
|---|---|
| Exam code | SY0-701 |
| Questions | Up to 90 (MCQ + performance-based) |
| Time | 90 minutes |
| Question types | Multiple choice (single and multiple response), performance-based (PBQ) |
| Scoring | Scaled 100-900 |
| Passing score | 750 |
| Recommended experience | 2+ years in IT admin with security focus (Network+ helpful) |
| Retake | No wait before the 2nd attempt; 14 days before the 3rd and later (verify current CompTIA policy); each attempt needs a new voucher |

## Domains and weights

| # | Domain | Weight |
|---|---|---|
| 1 | General Security Concepts | 12% |
| 2 | Threats, Vulnerabilities, and Mitigations | 22% |
| 3 | Security Architecture | 18% |
| 4 | Security Operations | 28% |
| 5 | Security Program Management and Oversight | 20% |

Domain 4 plus Domain 2 is half the exam. Domain 1 is smallest but its content (controls, crypto, AAA, Zero Trust) underlies everything else.

## Performance-based questions (PBQs)

- Simulations: firewall rule tables, matching/ordering, log analysis, configuring a device, drag-and-drop labelling, network diagram placement.
- Typically **a handful (about 3-6) at the start** of the exam; they take far longer than MCQs.
- **Skip and return.** Flag the PBQs, answer all MCQs first, then come back with the remaining time. Early MCQs build momentum and bank points.
- **Partial credit** is possible: fill in everything you can; never leave a PBQ blank.
- Scoring is weighted; PBQs are not known to be worth more than MCQs per se, but they cost more time.
- Common PBQ themes: firewall/ACL rules (first match wins, implicit deny at bottom), matching attacks to descriptions, ordering incident response or forensic steps, choosing controls for scenarios, selecting a secure protocol/port, reading logs for IoCs, PKI/certificate tasks, wireless configuration (WPA3/EAP).

## Question-style patterns

| Stem keyword | How to read it |
|---|---|
| **BEST** | Several answers work; pick the most complete or most appropriate for the scenario |
| **MOST** | Degree question; pick the strongest/most effective/most likely |
| **FIRST** | Order question; pick the earliest step in the process (e.g. IR order: preparation -> detection -> analysis -> containment -> eradication -> recovery -> lessons learned) |
| **LEAST** | Inverted; find the weakest, least secure, or the odd one out |
| **NEXT** | What follows the step already described |
| **MOST cost-effective / secure** | Weigh constraints stated in the stem |

- **"Which of the following" with two plausible answers:** reread the stem and find the specific keyword (e.g. "non-repudiation" -> digital signature, not hashing; "prevent" vs "detect"; "preventive" vs "deterrent"; "real-time" vs "scheduled"; "legacy" or "embedded"). The right answer matches that keyword; the other is generally true but not specific.
- Scenario stems often hide the answer in one clue: "contractor", "unmanaged BYOD", "no change to the application code", "minimal downtime", "regulated data".
- Multiple-response questions say "Select TWO/THREE". Both/all must be right.
- Watch for qualifiers: "without impacting availability", "least privilege", "cost", "ease of use".

## Time management

- 90 min for up to 90 items = about 1 minute each, but PBQs eat 5-10 each.
- Plan: flag PBQs (about 30 seconds), MCQs at 45-60 seconds each, a target of finishing MCQs with 25-30 minutes left, then PBQs, then review flagged items.
- Never spend more than 90 seconds on any MCQ on the first pass; mark and move on.
- No penalty for guessing: answer every question.
- Check at the 30-minute and 60-minute marks: you should be about one-third and two-thirds done with MCQs.

## Elimination tactics

1. Eliminate answers that are the wrong category (technical control offered where a managerial one is asked, etc.).
2. Eliminate absolutes ("always", "never", "all") unless they are the definition.
3. Eliminate answers that are overkill or violate a stated constraint (cost, downtime, no code changes).
4. Between two survivors, find the stem keyword that favours one.
5. Prefer the answer that is least privilege, defense in depth, or addresses the root cause rather than the symptom.
6. In incident questions, containment before eradication before recovery; do not jump to forensics or blame first.
7. Policy/process answers beat purely technical ones for governance-flavoured stems; vice versa for hands-on stems.

## Score report

- Pass/fail shown on screen at the end of the exam; the official report follows by email/portal.
- Overall scaled score (100-900).
- **Per-domain performance feedback** (objective-level strengths and weaknesses), not scaled scores per domain.
- A failed report lists weaker areas; use them to plan the retake.
- Scoring is not a simple percentage; the 750 line is roughly 80% by most estimates. The companion site uses `100 + round(pct * 800)` as a rough estimate only.

## Logistics

| Topic | Details |
|---|---|
| Scheduling | Buy a voucher from CompTIA (or a reseller), schedule through Pearson VUE |
| Options | In-person at a Pearson VUE test centre, or **online proctored** at home |
| ID | Valid, unexpired government-issued photo ID with signature; name must match registration exactly (some countries require a second ID; check current policy) |
| Test centre | Arrive about 15 minutes early; lockers for belongings; whiteboard or notepad provided; palm/ID checks |
| Online | Quiet, clear room and desk; webcam, mic, stable connection; system test beforehand; photos of ID and room; no breaks that leave camera view (check current rules); no notes, second monitors, or phones in reach |
| Online risks | Connectivity or proctor interruptions; choose a test centre if your home setup is unreliable |
| Rescheduling | Reschedule or cancel well ahead (typically 24+ hours) to avoid forfeiting the fee |
| Discounts | Student/academic pricing, retake and bundle offers |
| Renewal | Valid 3 years; renew via CE credits (50 CEUs) or higher-level certification |

## Study schedules

### 4-week plan (about 1-2 hours per weekday, longer weekends)

| Week | Focus | Tasks |
|---|---|---|
| 1 | Domains 1 and 2 | Read 01 and 02; module quizzes until 3 consecutive at least 83%; start acronym list |
| 2 | Domains 3 and 4 | Read 03 and 04; module quizzes; memorize ports (90) |
| 3 | Domain 5 and review | Read 05; module quiz; missed-question drill; read 92 (formulas) |
| 4 | Practice exams | Full timed finals; drill misses after each; reread weak domains; light review day before |

### 2-week plan (about 3-4 hours per day)

| Days | Focus | Tasks |
|---|---|---|
| 1-2 | Overview + Domain 1 | Read 00, 01; quiz; skim 90 ports |
| 3-4 | Domain 2 | Read 02; quiz; drill misses |
| 5-6 | Domain 3 | Read 03; quiz |
| 7-9 | Domain 4 (heaviest) | Read 04; quiz in two sessions; drill misses |
| 10 | Domain 5 | Read 05; quiz |
| 11 | Reference review | 90, 91, 92; full missed-question drill |
| 12-13 | Final exams | Two timed finals; drill misses; review weak domains |
| 14 | Light review | Ports, formulas, rest; sleep |
