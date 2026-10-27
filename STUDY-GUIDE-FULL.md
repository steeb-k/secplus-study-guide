# CompTIA Security+ SY0-701 — Complete Study Guide

> **⚠ AI-generated, not yet vetted.** This guide was written by AI from its knowledge of the CompTIA SY0-701 objectives and has **not yet been reviewed by a human for accuracy**. Cross-check anything surprising against the official objectives before relying on it.

## Contents

- [Exam Overview](#exam-overview)
- [Domain 1 — General Security Concepts (12%)](#domain-1--general-security-concepts-12)
- [Domain 2 — Threats, Vulnerabilities, and Mitigations (22%)](#domain-2--threats-vulnerabilities-and-mitigations-22)
- [Domain 3 — Security Architecture (18%)](#domain-3--security-architecture-18)
- [Domain 4 — Security Operations (28%)](#domain-4--security-operations-28)
- [Domain 5 — Security Program Management and Oversight (20%)](#domain-5--security-program-management-and-oversight-20)
- [Ports and Protocols](#ports-and-protocols)
- [Acronyms](#acronyms)
- [Formulas and Numbers](#formulas-and-numbers)

---

## Exam Overview

### Exam facts

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

### Domains and weights

| # | Domain | Weight |
|---|---|---|
| 1 | General Security Concepts | 12% |
| 2 | Threats, Vulnerabilities, and Mitigations | 22% |
| 3 | Security Architecture | 18% |
| 4 | Security Operations | 28% |
| 5 | Security Program Management and Oversight | 20% |

Domain 4 plus Domain 2 is half the exam. Domain 1 is smallest but its content (controls, crypto, AAA, Zero Trust) underlies everything else.

### Performance-based questions (PBQs)

- Simulations: firewall rule tables, matching/ordering, log analysis, configuring a device, drag-and-drop labelling, network diagram placement.
- Typically **a handful (about 3-6) at the start** of the exam; they take far longer than MCQs.
- **Skip and return.** Flag the PBQs, answer all MCQs first, then come back with the remaining time. Early MCQs build momentum and bank points.
- **Partial credit** is possible: fill in everything you can; never leave a PBQ blank.
- Scoring is weighted; PBQs are not known to be worth more than MCQs per se, but they cost more time.
- Common PBQ themes: firewall/ACL rules (first match wins, implicit deny at bottom), matching attacks to descriptions, ordering incident response or forensic steps, choosing controls for scenarios, selecting a secure protocol/port, reading logs for IoCs, PKI/certificate tasks, wireless configuration (WPA3/EAP).

### Question-style patterns

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

### Time management

- 90 min for up to 90 items = about 1 minute each, but PBQs eat 5-10 each.
- Plan: flag PBQs (about 30 seconds), MCQs at 45-60 seconds each, a target of finishing MCQs with 25-30 minutes left, then PBQs, then review flagged items.
- Never spend more than 90 seconds on any MCQ on the first pass; mark and move on.
- No penalty for guessing: answer every question.
- Check at the 30-minute and 60-minute marks: you should be about one-third and two-thirds done with MCQs.

### Elimination tactics

1. Eliminate answers that are the wrong category (technical control offered where a managerial one is asked, etc.).
2. Eliminate absolutes ("always", "never", "all") unless they are the definition.
3. Eliminate answers that are overkill or violate a stated constraint (cost, downtime, no code changes).
4. Between two survivors, find the stem keyword that favours one.
5. Prefer the answer that is least privilege, defense in depth, or addresses the root cause rather than the symptom.
6. In incident questions, containment before eradication before recovery; do not jump to forensics or blame first.
7. Policy/process answers beat purely technical ones for governance-flavoured stems; vice versa for hands-on stems.

### Score report

- Pass/fail shown on screen at the end of the exam; the official report follows by email/portal.
- Overall scaled score (100-900).
- **Per-domain performance feedback** (objective-level strengths and weaknesses), not scaled scores per domain.
- A failed report lists weaker areas; use them to plan the retake.
- Scoring is not a simple percentage; the 750 line is roughly 80% by most estimates. The companion site uses `100 + round(pct * 800)` as a rough estimate only.

### Logistics

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

### Study schedules

#### 4-week plan (about 1-2 hours per weekday, longer weekends)

| Week | Focus | Tasks |
|---|---|---|
| 1 | Domains 1 and 2 | Read 01 and 02; module quizzes until 3 consecutive at least 83%; start acronym list |
| 2 | Domains 3 and 4 | Read 03 and 04; module quizzes; memorize ports (90) |
| 3 | Domain 5 and review | Read 05; module quiz; missed-question drill; read 92 (formulas) |
| 4 | Practice exams | Full timed finals; drill misses after each; reread weak domains; light review day before |

#### 2-week plan (about 3-4 hours per day)

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

---

## Domain 1 — General Security Concepts (12%)

Objectives 1.1–1.4. Smallest domain by weight, but the vocabulary (control types, CIA, zero trust, crypto) is reused in every other domain.

---

### 1.1 Compare and contrast various types of security controls

Two independent axes: **category** (who/what implements it) and **type** (what it does / when it acts). Every control has one of each.

#### Categories (how it is implemented)

| Category | Definition (exam framing) | Examples |
|---|---|---|
| Technical | Implemented in systems with technology; also called "logical" controls | Firewall, IDS/IPS, ACLs, encryption, EDR, antivirus, MFA |
| Managerial | Administrative; governs risk through policy and oversight at the planning level | Risk assessments, security policies, pen-test programs, vulnerability-management program, SDLC requirements |
| Operational | Carried out day to day by people (processes), not by a technology alone | Security awareness training, guard duty, change-control procedures, incident-response procedure execution, backups run by staff |
| Physical | Controls that act on the physical world | Fences, locks, bollards, badges, cameras, guards, mantraps |

> **Exam tip:** "Managerial" = plan/policy/assess/oversee. "Operational" = people executing a procedure. If a question says a *policy or risk assessment*, it is managerial; if it says *training or staff carrying out a procedure*, it is operational. A lock is physical even though it is "preventive". Guards are ambiguous: listed under physical security in 1.2, but treated as operational when the stem stresses the person performing a procedure (patrols, checking IDs). Pick the category the stem emphasises.

#### Types (what it does)

| Type | Definition (exam framing) | Timing |
|---|---|---|
| Preventive | Stops the event from occurring | Before |
| Deterrent | Discourages an attacker from attempting; does not physically stop | Before |
| Detective | Identifies and alerts that an event occurred or is occurring | During/after |
| Corrective | Limits damage and restores the system after an event | After |
| Compensating | Alternative control used when the primary control is impractical or fails; gives equivalent protection | Substitute |
| Directive | Directs/mandates behaviour; establishes what must or must not be done | Before |

> **Exam tip:** Deterrent vs preventive: a "Beware of dog" or "Cameras in use" sign deters; a locked door prevents. Directive vs deterrent: a policy/AUP/procedure *tells people what to do* (directive); a warning banner/signage *discourages* (deterrent). Compensating keywords: "cannot patch / legacy system / cannot implement X, so they did Y instead" (e.g., network segmentation for an unpatchable device).

> **Exam tip:** Corrective vs detective: restoring from backup, patching after the fact, killing a malicious process, EDR isolating an infected host = corrective. An IPS blocking traffic inline is preventive. Log review, IDS alert, motion sensor, SIEM alert = detective.

#### Category × type example matrix

| | Preventive | Deterrent | Detective | Corrective | Compensating | Directive |
|---|---|---|---|---|---|---|
| **Technical** | Firewall rule, ACL, encryption, MFA, IPS (block mode) | Login warning banner / splash screen | IDS, SIEM alerts, log monitoring, FIM | Restore from backup, EDR isolates host, patch deployment | Network segmentation for unpatchable system, WAF in front of vulnerable app | File-storage or acceptable-use notice pushed to systems telling users where/how to store data |
| **Managerial** | Risk assessment gating deployment, separation-of-duties design | Sanctions/disciplinary policy | Audits, pen tests, vulnerability scan reviews | Incident-response plan lessons learned, corrective action plan | Added management review when SoD is impossible | Security policy, standards, AUP |
| **Operational** | Awareness training, job rotation, onboarding/offboarding procedures | Publicised consequences, security reminders | Guard reviewing logs, user-activity reviews | Incident handling by IR team, backup restoration procedure | Manual review of transactions when automation unavailable | Procedures, SOPs, playbooks |
| **Physical** | Locks, fences, bollards, vestibule, badge reader | "Cameras in use" signs, visible guards, lighting | CCTV, motion/infrared sensors, alarms | Fire suppression, switching to alternate site | Guard stationed at a door whose reader is broken | "Authorized personnel only" signage, visitor-escort rules |

> **Exam tip:** Most matrix cells are judgment calls; the exam asks you to pick the *best* category and type. Anchor on the verb: stops = preventive, warns = deterrent, notices = detective, fixes = corrective, substitutes = compensating, mandates = directive.

---

### 1.2 Summarize fundamental security concepts

#### Confidentiality, Integrity, Availability (CIA triad)

| Property | Meaning | Controls | Attack against it |
|---|---|---|---|
| Confidentiality | Only authorized parties can read data | Encryption, access control, data classification | Eavesdropping, data breach |
| Integrity | Data/systems are not altered without authorization; changes detectable | Hashing, digital signatures, FIM, version control | Tampering, MITM modification |
| Availability | Authorized users can access when needed | Redundancy, backups, load balancing, UPS | DoS/DDoS, ransomware |

Related terms: **Non-repudiation** = a party cannot credibly deny having performed an action or sent a message. Achieved with **digital signatures** (plus audit logs and timestamps). Hashing gives integrity only; HMAC gives integrity + authenticity but not non-repudiation (shared key).

> **Exam tip:** "Prove who sent it / sender cannot deny" -> non-repudiation -> digital signature. "Ensure data wasn't modified" -> integrity -> hash. "Keep data secret" -> encryption -> confidentiality.

#### Authentication, Authorization, Accounting (AAA)

- **Authentication:** proving identity (something you know / have / are / somewhere you are / something you do).
- **Authorization:** what the authenticated identity is permitted to do.
- **Accounting:** recording what was done (logging, auditing, billing); supports non-repudiation and forensics.
- Protocol pairing: **RADIUS** (UDP, encrypts password only, combines authN/authZ), **TACACS+** (TCP/49, encrypts entire payload, separates AAA), **Diameter** (RADIUS successor).

**Authenticating people**: passwords, MFA, biometrics, smart cards, SSO/federation.

**Authenticating systems**: machine/device certificates (mutual TLS, 802.1X EAP-TLS), API keys, service accounts, SSH keys, TPM-backed attestation, MAC address filtering (weak, spoofable). Systems typically use certificates or keys because there is no human to type a secret.

**Authorization models**

| Model | Who decides | Basis | Keyword |
|---|---|---|---|
| DAC | Resource owner | Owner sets ACL entries | "Owner decides", file permissions |
| MAC | System/policy | Labels (classification) vs clearance | "Labels", "clearance", government/military |
| RBAC | Admin | Role/job function | "Job function", "role" |
| ABAC | Policy engine | Attributes (user, resource, environment) | "Attributes", time/location/device conditions |
| Rule-based | System rules | Rules applied to all (e.g., firewall ACL, time-of-day) | "Rules" regardless of identity |

> **Exam tip:** Rule-based and Role-based are both abbreviated RBAC in some text; the exam spells them out. Least privilege is the guiding principle behind all authorization models.

#### Gap analysis

Comparing the **current state** to a **desired state/standard/framework** (e.g., NIST CSF, ISO 27001, CIS Controls) to identify what is missing, then planning remediation. Output: list of gaps with remediation plan. Often precedes an audit or certification.

> **Exam tip:** "Compare current controls to a framework/target" -> gap analysis. Not a vulnerability scan (finds technical flaws) and not a risk assessment (assesses likelihood/impact).

#### Zero trust

Principle: **never trust, always verify**; no implicit trust based on network location. Assume breach; verify explicitly every request; least privilege; microsegmentation.

**Control plane** (decides)

| Component | Role |
|---|---|
| Adaptive identity | Authentication that adapts to context/risk (device posture, location, behaviour) |
| Threat scope reduction | Limit the blast radius: microsegmentation, least privilege, narrow access |
| Policy-driven access control | Access decisions made from defined policy, not network location |
| Policy Administrator (PA) | Establishes/shuts down the session path; instructs the PEP (issues tokens/credentials) |
| Policy Engine (PE) | Evaluates policy + signals and grants, denies, or revokes access (the "brain"; PE + PA = Policy Decision Point) |

**Data plane** (carries traffic and enforces)

| Component | Role |
|---|---|
| Subject/System | The user/device requesting access |
| Implicit trust zones | Areas where traffic is trusted once past the gate; zero trust aims to shrink/eliminate these |
| Policy Enforcement Point (PEP) | Gatekeeper that allows/blocks the connection per the PA/PE decision (e.g., gateway, agent, proxy) |

Flow: Subject -> PEP -> (asks PA -> asks PE) -> decision returned -> PEP opens or denies path to resource.

> **Exam tip:** PE decides, PA configures/tells, PEP enforces. Control plane = decision-making; data plane = traffic path. "Implicit trust zone" is what sits *behind* the PEP.

#### Physical security

| Control | Definition / what it does | Type |
|---|---|---|
| Bollards | Posts that stop vehicles from ramming/approaching a building | Preventive |
| Access control vestibule | Two-door enclosure (formerly mantrap); one door must close before the next opens; prevents tailgating | Preventive |
| Fencing | Perimeter barrier; height/anti-climb determines deterrence vs prevention | Preventive/deterrent |
| Video surveillance (CCTV) | Records and monitors; detective, also deterrent; supports investigations | Detective/deterrent |
| Security guard | Human verification, response, deterrence; adaptive judgment | Preventive/detective/deterrent |
| Access badge | Credential for readers (proximity/smart card); gives audit trail | Preventive |
| Lighting | Deters intruders, improves camera/guard effectiveness | Deterrent |
| Sensors | Detect presence/motion (below) | Detective |

**Sensors**

| Sensor | Detects by |
|---|---|
| Infrared | Heat (PIR passive-infrared) or interrupted IR beam; body-heat movement |
| Pressure | Weight on a mat/floor/object (e.g., pressure on a display case or door mat) |
| Microwave | Emits microwaves and detects reflected change (Doppler) from movement; covers larger area, can pass through thin walls |
| Ultrasonic | Emits ultrasonic sound and detects reflected change from movement; indoor, affected by airflow |

> **Exam tip:** Vestibule/mantrap = tailgating/piggybacking defence. Bollards = vehicle. Lighting = deterrent. Badge reader alone does not stop tailgating; guard or vestibule does.

#### Deception and disruption technology

| Technology | Definition |
|---|---|
| Honeypot | Decoy system that looks like a real target to attract and study attackers |
| Honeynet | Network of honeypots simulating an entire environment |
| Honeyfile | Decoy file (e.g., "passwords.xlsx") that alerts when opened or copied |
| Honeytoken | Fake data/credential/record (fake API key, DB row, account) planted to detect misuse or theft; any use is suspicious |

Purpose: early detection, intelligence on TTPs, and distraction/delay. Any interaction with a decoy is by definition suspicious, so false positives are low.

> **Exam tip:** Honeytoken = fake *data/credential*; honeyfile = fake *file*; honeypot = fake *host/service*; honeynet = fake *network*. Tarpit and sinkhole are related disruption techniques but are not in the list here.

---

### 1.3 Explain the importance of change management processes and the impact to security

Change management ensures modifications are requested, assessed, approved, tested, implemented, and documented so security is not degraded. It underpins availability and integrity.

#### Business processes impacting security operations

| Element | Definition (exam framing) |
|---|---|
| Approval process | Formal sign-off from appropriate authority (CAB/change owner) before implementation |
| Ownership | A named individual accountable for the asset/change |
| Stakeholders | Parties affected or with an interest; must be informed/consulted |
| Impact analysis | Assess what the change affects (systems, security, users, dependencies) and the risk |
| Test results | Evidence the change works and is safe, tested in non-production first |
| Backout plan | Steps to revert to the prior state if the change fails |
| Maintenance window | Scheduled time for changes to minimise business disruption |
| Standard operating procedure (SOP) | Documented, repeatable steps for routine tasks/changes |

> **Exam tip:** Typical sequence: request -> impact analysis -> approval -> test -> schedule in maintenance window (with backout plan) -> implement -> document. "Revert if something goes wrong" -> backout plan. Pre-approved low-risk routine changes are "standard changes".

#### Technical implications

| Item | Concern |
|---|---|
| Allow lists / deny lists | Updating application or IP lists; wrong entries block legit use or permit malware |
| Restricted activities | Some changes need extra authorisation (privileged operations) |
| Downtime | Planned outages affect availability; coordinate with stakeholders |
| Service restart | Brief interruption; sessions dropped; may be needed to apply config |
| Application restart | Same as above, scoped to the application; state lost |
| Legacy applications | Fragile; changes may break; may need compensating controls |
| Dependencies | Components that rely on each other; changing one can break another |

#### Documentation

- **Updating diagrams:** network/architecture diagrams must reflect the change.
- **Updating policies/procedures:** keep them in line with new reality.
- Records of approvals, test results, and change logs support audits and rollback.

#### Version control

Tracks changes to code, configs, and documents over time (e.g., Git): who changed what and when, ability to revert, branch/merge, and prevent unauthorised/uncontrolled changes. Supports integrity, accountability, and rollback (backout).

> **Exam tip:** Undocumented/unauthorised changes ("shadow changes", config drift) are a security risk; the fix is formal change control plus version control and configuration baselines.

---

### 1.4 Explain the importance of using appropriate cryptographic solutions

#### Public key infrastructure (PKI)

System of CAs, certificates, keys, and policies that binds public keys to identities.

| Component | Role |
|---|---|
| Public key | Shared openly; encrypts data or verifies signatures |
| Private key | Kept secret; decrypts or signs |
| Key escrow | Third party holds a copy of keys for recovery (e.g., lost keys, legal access) |
| Key management | Lifecycle: generate, distribute, store, rotate, revoke, destroy |

#### Encryption: levels

| Level | Protects | Examples |
|---|---|---|
| Full-disk | Entire drive at rest | BitLocker, FileVault, LUKS |
| Partition | One partition/volume | Encrypted volume |
| File | Individual files | EFS, GPG-encrypted file |
| Volume | Logical volume | VeraCrypt volume |
| Database | Whole DB or columns | TDE (transparent data encryption), column-level/cell-level |
| Record | Individual rows/records | Per-record keys in a DB |
| Transport/communication | Data in transit | TLS, IPsec, SSH, VPN |

States of data: **at rest**, **in transit**, **in use** (memory/processing; secure enclave, homomorphic encryption).

> **Exam tip:** TDE protects database files at rest (theft of storage), not data from an authorised DB user. Column/cell-level encryption protects specific sensitive fields even from DBAs.

#### Encryption: symmetric vs asymmetric

| | Symmetric | Asymmetric |
|---|---|---|
| Keys | One shared secret key | Key pair (public + private) |
| Speed | Fast | Slow (~1000x) |
| Best for | Bulk data encryption | Key exchange, digital signatures, identity |
| Key distribution | Hard (must share securely) | Easy (public key is public) |
| Scalability | n(n-1)/2 keys for n parties | 2n keys (one pair each) |
| Provides | Confidentiality | Confidentiality, authentication, non-repudiation (signatures) |
| Examples | AES, 3DES, ChaCha20 | RSA, ECC, DH (key agreement) |

**Key exchange:** how two parties get a shared symmetric key over an untrusted network. Either encrypt it with the recipient's public key (RSA key transport) or derive it with Diffie-Hellman/ECDH (key agreement; the key is never sent). Out-of-band = delivered separately (courier, in person); in-band = over the same network.

#### Common algorithms

| Algorithm | Type | Key/output size | Typical use |
|---|---|---|---|
| AES | Symmetric block | 128/192/256-bit | Standard bulk encryption (disk, TLS, VPN, Wi-Fi WPA2/3) |
| 3DES | Symmetric block | 168-bit (effective 112) | Legacy; deprecated; replaced by AES |
| ChaCha20 | Symmetric stream | 256-bit | Mobile TLS where AES hardware is absent |
| RSA | Asymmetric | 2048+ (4096 for high) | Key exchange/encryption, digital signatures, certificates |
| ECC | Asymmetric | 256-bit ~ RSA 3072 | Same as RSA with smaller keys; mobile/IoT |
| DH / ECDHE | Asymmetric key agreement | 2048+ / 256+ | Establish a shared secret; ephemeral gives forward secrecy |
| DSA / ECDSA | Asymmetric signature | varies | Digital signatures only |
| SHA-2 (SHA-256/512) | Hash | 256/512-bit digest | Integrity, signatures, certificates |
| SHA-3 | Hash | 224-512-bit digest | SHA-2 alternative (Keccak) |
| MD5 | Hash | 128-bit digest | Broken (collisions); only non-security checksums |
| SHA-1 | Hash | 160-bit digest | Deprecated; collisions |
| HMAC | Keyed hash (MAC) | depends on hash | Message integrity + authenticity with a shared key |
| PBKDF2 / bcrypt / scrypt | Key stretching / password hash | configurable work factor | Storing password hashes; deriving keys |

> **Exam tip:** Stream vs block: stream (RC4, ChaCha) encrypts bit/byte at a time; block (AES, 3DES) encrypts fixed blocks with a mode (GCM, CBC, CTR). GCM gives authenticated encryption. ECB is insecure (patterns leak).

#### Key length

Longer keys increase brute-force cost. Rules of thumb: AES-128 is acceptable, AES-256 for high security; RSA 2048 minimum; ECC 256. Symmetric keys are much shorter than asymmetric for the same strength. **Key exchange** (DH/RSA) and **perfect forward secrecy** (ephemeral keys) protect past sessions if a long-term key is compromised.

#### Tools

| Tool | Definition (exam framing) |
|---|---|
| TPM (Trusted Platform Module) | Chip on the motherboard that stores keys, measures boot integrity, and enables full-disk encryption (BitLocker), attestation; tied to that device |
| HSM (Hardware Security Module) | Dedicated tamper-resistant appliance/card for generating, storing, and using keys; high-performance crypto; used by CAs and payment systems; FIPS 140 |
| KMS (Key Management System/Service) | Centralised service for creating, storing, rotating, and controlling keys, often cloud-based (and may be backed by HSMs) |
| Secure enclave | Isolated, protected processor area (CPU/SoC) that protects sensitive operations and data even if the OS is compromised (e.g., Apple Secure Enclave, Intel SGX) |

> **Exam tip:** TPM = one device, motherboard, disk encryption/boot. HSM = enterprise key storage, removable/network appliance. KMS = management service. Secure enclave = protects data *in use* / isolated execution.

#### Obfuscation

| Technique | Definition | Reversible? |
|---|---|---|
| Steganography | Hiding data inside another file (image, audio, video) so its existence is concealed; security by obscurity | Yes (extract) |
| Tokenization | Replace sensitive value with a random token; the real value is stored in a secure vault; used for PCI (card numbers) | Yes, via vault lookup only |
| Data masking | Replace/hide parts of data (e.g., ****-1234) for display or non-production use | Usually not |

> **Exam tip:** Steganography hides *that* a message exists; encryption hides *what* it says. Tokenization = token has no mathematical relationship to the original (unlike encryption). Masking = test/dev data, display.

#### Hashing

One-way function producing a fixed-length digest; same input = same output; tiny change = very different output (avalanche); collision-resistant. Provides **integrity**, not confidentiality. Uses: file integrity, password storage, digital signatures, forensic evidence verification.

#### Salting

Random per-user value added to a password before hashing so identical passwords yield different hashes; defeats **rainbow tables** and precomputed attacks. Salt is stored with the hash (not secret). **Pepper** is a secret value stored separately.

#### Key stretching

Making brute force expensive by repeating the hash many times (work factor/iterations): **PBKDF2, bcrypt, scrypt** (and Argon2). Slows an attacker much more than a legitimate single login.

> **Exam tip:** Salt = defeats rainbow tables/precomputation. Key stretching = slows brute force/dictionary attacks. Both are used together for password storage.

#### Digital signatures

Hash the message, then encrypt the hash with the **sender's private key**; receiver verifies with the sender's **public key**. Provides **integrity, authentication, non-repudiation**. Does not provide confidentiality.

> **Exam tip:** Encrypt for confidentiality: use the *recipient's public key*. Sign for authenticity: use the *sender's private key*. Never the reverse for these goals.

#### Blockchain / open public ledger

Distributed, append-only ledger of blocks linked by hashes; each block contains the previous block's hash, so altering one breaks the chain. Consensus across many nodes; transparent and tamper-evident; used for cryptocurrency, provenance, audit trails. Provides integrity and non-repudiation in a decentralised way.

**Open public ledger:** the shared blockchain record itself; anyone can view and verify every transaction, no central authority owns it (transparency + tamper evidence, not confidentiality).

#### Certificates

| Term | Definition (exam framing) |
|---|---|
| Certificate authority (CA) | Trusted entity that issues and signs certificates; may be public or private (internal) |
| Intermediate CA | Signed by root; issues end-entity certs so the root can stay offline |
| Registration authority (RA) | Verifies identity before CA issues certificate |
| CRL (Certificate Revocation List) | CA-published list of revoked certificate serial numbers; downloaded periodically; can be stale |
| OCSP | Real-time query of a certificate's revocation status (responder); **OCSP stapling** has the server attach a signed response to the TLS handshake |
| Self-signed certificate | Signed by its own private key; no third-party trust; used for testing/internal; browsers warn |
| Third-party (public) certificate | Issued by a publicly trusted CA; trusted by default in browsers/OS |
| Root of trust | The trust anchor (root CA, or hardware like a TPM) from which all other trust derives |
| Certificate signing request (CSR) | Request sent to a CA containing public key and subject info (CN/SAN), signed by the requester's private key; private key never leaves the requester |
| Wildcard certificate | Covers all first-level subdomains of a domain (*.example.com covers www/mail.example.com, not a.b.example.com); one compromised key affects every host using it |
| SAN (Subject Alternative Name) | Lists multiple specific names covered by a cert |

Certificate fields: subject, issuer, validity dates, public key, serial number, signature algorithm, SAN. Common formats: PEM (Base64, text), DER (binary), PFX/P12 (cert + private key bundle), CER/CRT.

> **Exam tip:** Revoked-cert checking: CRL = list, periodic; OCSP = real-time query. "Cert from internal CA not trusted by browser" -> missing root in trust store. "*.example.com does not cover a.b.example.com". Chain of trust: end-entity -> intermediate -> root.

#### Worked example: TLS handshake (asymmetric then symmetric)

1. **Client Hello:** client sends supported TLS versions, cipher suites, and a random value.
2. **Server Hello + certificate:** server picks a cipher suite and sends its certificate (public key, signed by a CA) and random value.
3. **Client validates the certificate:** checks the chain to a trusted root, validity dates, name match (CN/SAN), and revocation (CRL/OCSP). This authenticates the server.
4. **Key exchange (asymmetric):** with ECDHE, client and server each create ephemeral key pairs and exchange public values; both compute the same **shared secret**. The server signs its ephemeral value with its certificate's private key to prove identity. (In older RSA key exchange, the client encrypts a pre-master secret with the server's public key.)
5. **Derive session keys:** both sides derive identical **symmetric session keys** (e.g., AES-GCM) from the shared secret and random values.
6. **Finished:** each side sends a MAC-verified Finished message; bulk application data is then encrypted with the **symmetric** session key.

Why: asymmetric crypto solves key distribution and authentication but is slow; symmetric crypto is fast for bulk data. ECDHE (ephemeral) gives **forward secrecy**: stealing the server's private key later does not decrypt recorded sessions. TLS 1.3 removes static RSA key exchange and weak ciphers.

---

### Most-tested distinctions

- Category (technical/managerial/operational/physical) vs type (preventive/deterrent/detective/corrective/compensating/directive) are separate axes; every control has one of each.
- Deterrent discourages (signs, banners, visible cameras); preventive blocks (locks, firewall rules); directive mandates (policy, procedure).
- Detective notices (IDS, logs, CCTV); corrective fixes after (restore, patch, isolate); compensating substitutes for a control that cannot be used.
- Managerial = policy, risk assessment, oversight; operational = people executing procedures (training, guards).
- Confidentiality -> encryption; integrity -> hashing/signatures; availability -> redundancy; non-repudiation -> digital signature.
- Authentication = who you are; authorization = what you may do; accounting = what you did. TACACS+ (TCP, full encryption, separate AAA) vs RADIUS (UDP, password only).
- DAC owner decides; MAC labels/clearance; RBAC roles; ABAC attributes/context; rule-based applies fixed rules to everyone.
- Gap analysis compares current state to a target framework; it is not a vulnerability scan or risk assessment.
- Zero trust: Policy Engine decides, Policy Administrator establishes the session, Policy Enforcement Point enforces; control plane decides, data plane carries traffic.
- Access control vestibule defeats tailgating; bollards stop vehicles; lighting deters; infrared = heat, pressure = weight, microwave/ultrasonic = reflected-wave motion.
- Honeypot = host; honeynet = network; honeyfile = file; honeytoken = fake data/credential.
- Change management: impact analysis, approval, testing, maintenance window, backout plan, then documentation (diagrams, policies); version control gives history and rollback.
- Symmetric = one key, fast, bulk; asymmetric = key pair, slow, key exchange/signatures. TLS uses asymmetric to authenticate and agree on keys, then symmetric for data; ephemeral exchange (DHE/ECDHE) gives perfect forward secrecy.
- Encrypt with recipient's public key; sign with sender's private key.
- TPM = per-device chip; HSM = dedicated key appliance; KMS = management service; secure enclave = isolated execution (data in use).
- Encryption is reversible with a key; hashing is one-way; tokenization uses a vault; masking hides display data; steganography hides existence.
- Salt defeats rainbow tables; key stretching (PBKDF2, bcrypt) slows brute force; HMAC needs a shared key.
- MD5 and SHA-1 are broken/deprecated; SHA-256/SHA-3 are current; 3DES is deprecated; AES is the standard; RSA 2048+ minimum.
- CRL = periodic list of revoked certs; OCSP = real-time status; stapling attaches the response to the handshake.
- CSR holds the public key and subject details, never the private key; wildcard covers one subdomain level; self-signed is not publicly trusted.

---

## Domain 2 — Threats, Vulnerabilities, and Mitigations (22%)

Objectives 2.1–2.5. Heaviest conceptual domain after Domain 4; most questions are scenario → classify the actor, vector, vulnerability, attack or indicator, then pick the mitigation.

---

### 2.1 Compare and contrast common threat actors and motivations

#### Threat actors

| Actor | Resources / funding | Sophistication | Internal / external | Typical motivation |
|---|---|---|---|---|
| **Nation-state** | Very high (government) | Very high; custom tools, zero-days, long dwell time (APT) | External | Espionage, political/military advantage, disruption of critical infrastructure, war |
| **Unskilled attacker** (script kiddie) | Low | Low; uses prebuilt tools/scripts | External | Disruption, curiosity, notoriety, "fun" |
| **Hacktivist** | Low–medium | Low–medium; DDoS, defacement, doxing, leaks | External | Philosophical/political belief, protest, revenge, disruption |
| **Insider threat** | Variable; already has access | Variable; knows where the data is | Internal | Revenge, financial gain, espionage (recruited), or negligence (unintentional) |
| **Organized crime** | High (business model) | High; ransomware-as-a-service, fraud rings | External | Financial gain (extortion, theft, fraud) |
| **Shadow IT** | Employee/department budget | Low (not an attacker but a risk source) | Internal | Convenience, speed, bypassing slow IT process; creates unmanaged assets and data leakage |

> **Exam tip:** "Long-term, stealthy, well-funded, targeted" = **nation-state / APT**. "Hired by competitors / sold data for profit" = **insider (financial)** or **organized crime**. "Deployed unapproved SaaS / personal cloud storage / unmanaged server" = **shadow IT**. "Downloaded a tool and ran it without understanding it" = **unskilled attacker**.

#### Attributes of actors

- **Internal vs external** — insiders bypass perimeter controls; mitigate with least privilege, DLP, UEBA, separation of duties, job rotation.
- **Resources/funding** — determines ability to buy zero-days, run infrastructure, sustain campaigns.
- **Level of sophistication/capability** — from copy-paste tools to custom malware and supply-chain compromise.

#### Motivations

| Motivation | Typical actor(s) / example |
|---|---|
| **Data exfiltration** | Organized crime, nation-state, insider; theft of PII/IP |
| **Espionage** | Nation-state, corporate insider/competitor |
| **Service disruption** | Hacktivist, nation-state, unskilled; DDoS, wipers |
| **Blackmail** | Organized crime, insider; threaten to leak data |
| **Financial gain** | Organized crime, insider; ransomware, fraud, cryptojacking |
| **Philosophical/political beliefs** | Hacktivist, nation-state |
| **Ethical** | Authorized penetration testers / bug-bounty researchers (white hat) |
| **Revenge** | Disgruntled insider, hacktivist |
| **Disruption/chaos** | Unskilled attackers, hacktivists |
| **War** | Nation-state; attacks on military/critical infrastructure, cyberwarfare |

> **Exam tip:** Hat colours: **white/authorized** = ethical pen tester; **black/unauthorized** = malicious; **gray/semi-authorized** = finds flaws without permission, may disclose them (no malicious intent, still unauthorized). **Blue team** defends, **red team** attacks, **purple team** combines both.

---

### 2.2 Explain common threat vectors and attack surfaces

**Attack surface** = all points where an attacker could try to enter or extract data. **Threat vector** = the path/method used. Reduce the surface by closing ports, removing unused services/software, and removing unsupported systems.

#### Message-based

| Vector | Definition / exam keyword |
|---|---|
| **Email** | Phishing, malicious attachments, BEC; mitigated by SPF/DKIM/DMARC, filtering, sandboxing |
| **Short Message Service (SMS)** | **Smishing**; links or "reply to confirm" texts |
| **Instant messaging (IM)** | Malicious links/files via chat platforms; impersonation of coworkers |

#### Image-based
- Malicious content hidden in images (embedded payloads, steganography, malformed image files exploiting a parser; QR codes that redirect to malicious sites = **quishing**).

#### File-based
- Malicious documents/PDFs/archives/executables; macros in Office files; files that exploit viewer vulnerabilities. Mitigate: disable macros, sandbox/detonate attachments, application allow listing.

#### Voice call
- **Vishing**; caller-ID spoofing, fake help desk or bank calls; deepfake voice impersonation of executives.

#### Removable device
- USB drives dropped in parking lots (baiting), malicious USB cables/devices (HID emulation, e.g. "rubber ducky"), autorun malware. Mitigate: disable USB mass storage/autorun, port blocking, DLP, endpoint control.

#### Vulnerable software
- **Client-based** — software installed and run on each endpoint; a flaw in that installed client is exploitable on every device that has it, and every copy must be patched (often a slow, uneven rollout).
- **Agentless** — nothing installed on the endpoint; the code runs centrally or is delivered on demand (web app, browser-delivered code). The vulnerability lives in one place: an attacker who compromises it hits every user at once, but a single server-side fix covers everyone.

#### Unsupported systems and applications
- End-of-life/end-of-support OS or software receives **no security patches**; permanent known vulnerabilities. Mitigate: replace/upgrade, or isolate (segmentation), restrict access, compensating controls, virtual patching with IPS/WAF.

#### Unsecure networks

| Type | Risk |
|---|---|
| **Wireless** | Rogue AP, evil twin, weak encryption (WEP/WPA), open guest networks, eavesdropping |
| **Wired** | Unprotected jacks in public areas; rogue devices; mitigate with 802.1X NAC, port security |
| **Bluetooth** | Bluejacking (unsolicited messages), bluesnarfing (data theft), pairing weaknesses |

#### Open service ports
- Each listening port is attack surface. Unneeded open ports = misconfiguration; discover with port scanners (Nmap), close with host firewall/hardening, disable unused services.

#### Default credentials
- Vendor-default usernames/passwords on routers, cameras, IoT, databases, admin consoles. Mitigate: change on deployment, unique credentials, enforce at provisioning.

#### Supply chain
- Compromise through a trusted third party; each has an attack position:
  - **Managed service provider (MSP)** — a compromised MSP gives access to all its customers.
  - **Vendor** — compromised product/update (e.g. trojanized software update); hardware tampering.
  - **Supplier** — counterfeit or tampered components/parts.
- Mitigate: vendor assessment, SBOM, code signing, update verification, contractual security requirements, hardware provenance checks.

#### Human vectors / social engineering
Exploits trust and psychology, not technology. Mitigated primarily by **security awareness training**, procedures (callback verification), and simulation exercises.

| Technique | Distinguishing keyword |
|---|---|
| **Phishing** | Mass, generic email lures; link/attachment/credential request |
| **Spear phishing** | Targeted at a specific person/group with personalised details |
| **Whaling** | Targets senior executives (C-suite) |
| **Vishing** | Voice/phone call |
| **Smishing** | SMS/text message |
| **Misinformation / disinformation** | False information, spread unintentionally (mis-) or deliberately (dis-) to influence |
| **Impersonation** | Pretending to be someone trusted (help desk, auditor, vendor, executive) |
| **Business email compromise (BEC)** | Spoofed/compromised executive or vendor email requesting wire transfer or invoice change |
| **Pretexting** | Invented scenario/backstory to extract information or access |
| **Watering hole** | Compromise a website the target group frequents; wait for them to visit |
| **Brand impersonation** | Fake emails/sites that mimic a known brand |
| **Typosquatting** | Look-alike misspelled domain (gooogle.com); "URL hijacking" |
| **Pharming** | Redirects legitimate domain traffic to a fake site (DNS poisoning/hosts file); no click on a bad link needed |
| **Baiting** | Free/tempting item (infected USB, free download) |
| **Tailgating / piggybacking** | Following an authorised person through a secure door; tailgating = without their knowledge/consent, piggybacking = they knowingly let you in (e.g. holding the door) |
| **Shoulder surfing** | Observing screens/keypads (physical/visual) |
| **Dumpster diving** | Retrieving information from discarded materials |
| **Quid pro quo** | Offering a service/benefit in exchange for information or access |
| **Eliciting** | Extracting information through ordinary conversation |
| **Identity fraud / theft** | Using stolen identity data to open accounts or impersonate |

> **Exam tip:** Spear phishing (any specific person) vs whaling (executives) vs BEC (financial request via business email). Phishing = link click; **pharming** = redirected without clicking. **Typosquatting** = misspelled domain; **brand impersonation** = looks like the brand. **Watering hole** = target's usual site is compromised. Tailgating vs piggybacking: tailgating is unauthorised follow-through; **mantrap/access control vestibule** is the control.

**Principles of social engineering (why it works):** authority, intimidation, consensus/social proof, scarcity, familiarity/liking, trust, urgency.

---

### 2.3 Explain various types of vulnerabilities

#### Application
| Vulnerability | Definition / keyword |
|---|---|
| **Memory injection** | Malicious code injected into a running process's memory |
| **Buffer overflow** | Input exceeds buffer size and overwrites adjacent memory; crashes or code execution; mitigate with bounds checking, ASLR, DEP |
| **Race condition** | Outcome depends on timing of events; **TOC/TOU** (time-of-check to time-of-use) is the classic form |
| **Malicious update** | Update channel delivers tampered code; mitigate with code signing and hash verification |

#### Operating system (OS)-based
- Unpatched OS flaws, insecure defaults, unnecessary services, privilege escalation bugs, legacy/unsupported OS versions.

#### Web-based
| Vulnerability | Definition / keyword |
|---|---|
| **SQL injection (SQLi)** | Untrusted input altered a database query; fix with parameterized queries/prepared statements and input validation |
| **Cross-site scripting (XSS)** | Script injected into a page and executed in other users' browsers (reflected, stored, DOM-based); fix with output encoding, input sanitization, CSP |
| **CSRF/XSRF** (related) | Forces an authenticated user's browser to send an unwanted request; fix with anti-CSRF tokens, SameSite cookies |

#### Hardware
| Vulnerability | Definition |
|---|---|
| **Firmware** | Outdated/malicious/unsigned firmware (BIOS/UEFI, device); mitigate with signed updates, secure boot |
| **End-of-life** | Vendor no longer provides updates |
| **Legacy** | Old but possibly still supported; poor security design, hard to patch |

#### Virtualization
| Vulnerability | Definition |
|---|---|
| **VM escape** | Guest breaks out to the hypervisor or other VMs |
| **Resource reuse** | Memory/storage allocated to a new VM still contains data from a previous tenant; mitigate by scrubbing |
| **VM sprawl** (related) | Unmanaged, forgotten VMs that go unpatched |

#### Cloud-specific
- Misconfigured storage buckets/permissions, insecure APIs, excessive IAM permissions, weak tenant isolation, shared-responsibility misunderstandings, exposed keys in code repos.

#### Supply chain
| Component | Meaning |
|---|---|
| **Service provider** | Third party with network/data access compromised |
| **Hardware provider** | Tampered or counterfeit devices, firmware backdoors |
| **Software provider** | Compromised libraries/updates/build systems (also open-source dependency risk) |

#### Cryptographic
- Weak/deprecated algorithms (DES, MD5, SHA-1, RC4), short keys, poor random number generation, hard-coded or exposed keys, improper certificate validation, no encryption of data in transit/at rest, expired certs.

#### Misconfiguration
- Open permissions, default settings/credentials, unnecessary services, verbose error messages, excessive ports. The most common real-world vulnerability type.

#### Mobile device
| Vulnerability | Definition |
|---|---|
| **Side loading** | Installing apps from outside the official store, bypassing vetting |
| **Jailbreaking** (iOS) / **Rooting** (Android) | Removes manufacturer restrictions; defeats the security model; MDM should detect and block/quarantine |

#### Zero-day
- A vulnerability unknown to the vendor (no patch exists). Patching can't help; use layered defenses: segmentation, IPS/behavioural detection, EDR, least privilege, virtual patching, threat intelligence.

> **Exam tip:** "No patch available / vendor unaware" = **zero-day**. "Guest to host" = **VM escape**. "Leftover data on new VM" = **resource reuse**. "Check then use gap" = **race condition/TOCTOU**. "Database query manipulated" = SQLi; "script runs in victim's browser" = XSS. "Rooted/jailbroken" = defeats mobile controls; "unofficial app source" = **side loading**.

---

### 2.4 Given a scenario, analyze indicators of malicious activity

#### Malware attacks

| Type | Distinguishing indicator |
|---|---|
| **Ransomware** | Files encrypted, ransom note, demand for payment (crypto); often with data-theft extortion |
| **Trojan** | Looks legitimate/useful but carries a malicious payload; does not self-replicate |
| **Worm** | Self-replicates across the network without user action; sudden network congestion |
| **Spyware** | Secretly gathers user activity/information |
| **Bloatware** | Preinstalled unwanted software; consumes resources, expands attack surface |
| **Virus** | Needs a host file and user execution to spread |
| **Keylogger** | Records keystrokes (hardware or software); stolen credentials |
| **Logic bomb** | Dormant code triggered by a condition (date, event, account removal); typically insider |
| **Rootkit** | Hides its presence at kernel/OS/firmware level, gives persistent privileged access; evades normal AV |
| **Backdoor** (related) | Hidden access path bypassing authentication |
| **Botnet / RAT** (related) | Compromised hosts under C2 control; DDoS, spam |
| **Fileless** (related) | Runs in memory using legitimate tools (PowerShell, WMI); no file on disk; detect with EDR/behavioural analysis |
| **Cryptojacking** (related) | Hijacked CPU/GPU used to mine crypto; high resource use |

> **Exam tip:** Worm vs virus: worm spreads **on its own**; virus needs a **host and user action**. Trojan = disguised, no self-replication. Logic bomb = **condition-triggered**. Rootkit = **concealment + persistence**. Fileless = **memory-only / living-off-the-land**.

#### Physical attacks
| Attack | Definition |
|---|---|
| **Brute force (physical)** | Forcing entry — breaking locks, doors, barriers |
| **RFID cloning** | Copying a badge/credential to a new card; mitigate with encrypted/higher-security credentials, MFA |
| **Environmental** | Attacks on power, HVAC, fire suppression, water; disrupts availability |

#### Network attacks
| Attack | Definition / keyword |
|---|---|
| **DDoS — amplified** | Small spoofed request yields large response sent to victim (DNS, NTP amplification) |
| **DDoS — reflected** | Spoofed source IP makes third-party servers send responses to the victim |
| **DNS attacks** | DNS poisoning/spoofing, DNS hijacking, domain hijacking, tunnelling; users redirected to fake sites |
| **Wireless** | Rogue AP, **evil twin** (lookalike SSID), deauthentication, WPS/weak-key attacks |
| **On-path** (formerly MITM) | Attacker intercepts/alters traffic between two parties; ARP poisoning, rogue AP; mitigate with TLS, DAI |
| **Credential replay** | Captured valid credentials/tokens/hashes reused (pass-the-hash, session replay); mitigate with nonces, timestamps, short-lived tokens, Kerberos protections |
| **Malicious code** | Malware delivered or executed over the network |

#### Application attacks
| Attack | Definition / keyword |
|---|---|
| **Injection** | Untrusted input interpreted as commands (SQL, command, LDAP, XML) |
| **Buffer overflow** | Memory overwrite via oversized input |
| **Replay** | Valid data transmission captured and re-sent |
| **Privilege escalation** | Gaining higher rights (vertical) or another user's rights (horizontal) |
| **Forgery** | CSRF (forged request from authenticated browser), SSRF (server tricked into making internal requests) |
| **Directory traversal** | `../` sequences to reach files outside the web root; mitigate with input validation, least privilege |

#### Cryptographic attacks
| Attack | Definition |
|---|---|
| **Downgrade** | Forces use of weaker protocol/cipher (e.g. TLS → SSL); disable legacy protocols |
| **Collision** | Two different inputs yield the same hash; breaks integrity (MD5, SHA-1) |
| **Birthday** | Probability-based method to find hash collisions faster than brute force |

#### Password attacks
| Attack | Keyword |
|---|---|
| **Spraying** | One/few common passwords against **many accounts** (avoids lockout); many accounts with few attempts each |
| **Brute force** | Try all possible combinations against one account/hash; online or offline |
| **Dictionary** | Wordlist of likely passwords |
| **Rainbow table** (related) | Precomputed hash lookups; defeated by **salting** |
| **Credential stuffing** (related) | Reused breached username/password pairs tried on other sites |

> **Exam tip:** Spraying = many accounts, few passwords, evades lockout. Brute force = one target, all combos, triggers lockout. Credential stuffing = breach data. Salting defeats rainbow tables; key stretching (bcrypt, PBKDF2) slows brute force. Online attacks are limited by lockout; offline attacks against stolen hashes are not.

#### Indicators

| Indicator | What it suggests |
|---|---|
| **Account lockout** | Brute-force/password attack on that account (or user error) |
| **Concurrent session usage** | Same credential in use from two places: credential theft/sharing |
| **Blocked content** | Security tools blocking malicious URLs/files: attempted exploit, malware delivery, or exfiltration to blocked sites |
| **Impossible travel** | Logins from geographically distant locations within an impossible time: compromised credentials |
| **Resource consumption** | Unexplained CPU/memory/disk/bandwidth spikes: malware, cryptojacking, botnet, exfiltration |
| **Resource inaccessibility** | Services/files unavailable: DoS, ransomware, destructive attack |
| **Out-of-cycle logging** | Activity or log entries at unusual times: unauthorised access, scheduled malicious tasks |
| **Published/documented** | Attack details appear in public sources (breach notices, paste sites, dark web, vendor advisories): data already leaked or technique known |
| **Missing logs** | Log gaps, cleared or disabled logging: attacker covering tracks (anti-forensics) |

#### Symptom → most likely attack

| Symptom | Most likely |
|---|---|
| One account locked out after a burst of failed logins | Brute force (online) |
| Many accounts each with one or two failed logins from the same source, few lockouts | Password spraying |
| Files renamed with new extension; ransom note | Ransomware |
| Fast network spread with no user action | Worm |
| Legit-looking free program causes backdoor | Trojan |
| Fires on a date or when employee's account is disabled | Logic bomb |
| AV clean but hidden processes/files and persistent admin access | Rootkit |
| Malicious activity with no files on disk; PowerShell/WMI abuse | Fileless malware |
| Sustained high CPU, slow machines, mining pool traffic | Cryptojacking |
| Login in London, then Tokyo 20 minutes later | Impossible travel → credential compromise |
| Website returns wrong IP / redirect to fake bank | DNS poisoning / pharming |
| Cert warnings, traffic via unknown device | On-path attack (ARP poisoning / rogue AP) |
| Same SSID twice, one stronger | Evil twin |
| Flood of traffic from many sources | DDoS (botnet) |
| Tiny DNS/NTP queries produce huge responses to victim | Amplification (reflected DDoS) |
| Request contains `' OR 1=1 --` | SQL injection |
| `<script>` in input field, executed on another user's page | XSS |
| `../../etc/passwd` in URL | Directory traversal |
| Valid old session/token accepted again | Replay |
| Connection negotiated to weaker cipher | Downgrade |
| Insider copying files to USB at night | Data exfiltration; out-of-cycle activity |
| Logs end/gap during incident window | Missing logs: attacker clearing tracks |

---

### 2.5 Explain the purpose of mitigation techniques used to secure the enterprise

#### Segmentation
- Divide the network into zones (VLANs, subnets, firewalls, microsegmentation) to contain breaches and limit lateral movement; reduces attack surface and scopes compliance (e.g. PCI).

#### Access control
| Item | Definition |
|---|---|
| **Access control list (ACL)** | Ordered rules permitting/denying traffic or object access (router/firewall rules, file permissions); implicit deny at the end |
| **Permissions** | Rights granted on resources (read/write/execute); assigned per least privilege |

#### Application allow list
- Only approved applications may run (default deny). Stronger than a block list (deny list), which only stops known-bad. Also blocks unknown malware and shadow IT.

#### Isolation
- Separate a compromised/risky system from the network (quarantine VLAN, air gap, disconnecting an infected host); used in incident containment and for legacy/unsupported systems.

#### Patching
- Apply vendor fixes for known vulnerabilities; follow test → deploy → verify; prioritise by severity and exposure (CVSS). Counters known-vulnerability exploitation, not zero-days.

#### Encryption
- Protect confidentiality of data at rest, in transit, and in use (disk, file, TLS, VPN); makes stolen data unusable.

#### Monitoring
- Continuous logging, SIEM correlation, IDS/IPS, EDR, NetFlow; enables detection of the indicators in 2.4.

#### Least privilege
- Give users, processes, and services the minimum access required; limits privilege escalation, insider damage and malware impact. Pair with PAM, just-in-time access, and separation of duties.

#### Configuration enforcement
- Maintain systems at an approved baseline: group policy, MDM, configuration management, compliance checks (e.g. NAC posture assessment), auto-remediation of drift. Compare to the secure baseline.

#### Decommissioning
- Securely retire assets: sanitise/destroy media (wipe, degauss, shred), remove from inventory/DNS/AD, revoke credentials and certificates, update asset records. Prevents data leakage and orphaned (zombie) systems.

#### Hardening techniques
| Technique | What it does |
|---|---|
| **Encryption** | Protect data/communications |
| **Installation of endpoint protection** | AV/anti-malware, EDR, XDR, host-based firewall, HIDS/HIPS |
| **Host-based firewall** | Filters traffic to/from a single host |
| **Host-based intrusion prevention system (HIPS)** | Detects and blocks malicious behaviour on the host |
| **Disabling ports/protocols** | Closes unneeded listeners and insecure protocols (Telnet, FTP, SMBv1) |
| **Default password changes** | Replace vendor defaults |
| **Removal of unnecessary software** | Fewer services/apps = smaller attack surface (also removes bloatware) |

> **Exam tip:** Allow list = "only approved run" (default deny); deny/block list = "known bad blocked". Segmentation **contains**; isolation **removes** access entirely for one asset. Patching does nothing for a **zero-day** or unsupported system, so isolate/segment/virtually patch. Hardening = reduce attack surface; configuration enforcement = keep it that way (prevent drift).

#### Attack → best mitigation

| Attack / weakness | Best mitigation |
|---|---|
| Phishing / social engineering | Awareness training, email filtering (SPF/DKIM/DMARC), MFA, simulations |
| Ransomware | Offline/immutable backups, patching, EDR, least privilege, segmentation, email filtering |
| Worm | Patching, segmentation, host firewall, disabling unused services |
| Zero-day | Defense in depth: segmentation, IPS/EDR behavioural detection, least privilege, application allow list |
| Unsupported/legacy system | Replace; otherwise isolate/segment, restrict access, virtual patching |
| SQL injection | Parameterized queries, input validation, WAF, least-privilege DB account |
| XSS | Output encoding, input sanitization, Content Security Policy |
| CSRF | Anti-CSRF tokens, SameSite cookies, re-authentication |
| Buffer overflow | Bounds checking, ASLR/DEP, secure coding, patching |
| Directory traversal | Input validation/canonicalisation, chroot/least privilege |
| Password spraying / brute force | MFA, lockout/throttling, password policy, banned password list, monitoring |
| Credential stuffing | MFA, unique passwords, breached-password checks |
| Rainbow table / offline cracking | Salting, key stretching (bcrypt, PBKDF2, Argon2), long passphrases |
| On-path / eavesdropping | TLS, VPN, DAI, port security, 802.1X |
| DNS poisoning | DNSSEC, secure resolvers, patching DNS |
| DDoS | Rate limiting, DDoS protection/CDN, scrubbing services, anycast, over-provisioning |
| Replay | Nonces, timestamps, session tokens, TLS, Kerberos |
| Downgrade | Disable legacy protocols/ciphers, enforce minimum TLS version |
| Collision / weak hash | Use SHA-256+ |
| Evil twin / rogue AP | WPA3-Enterprise/802.1X, wireless IPS, certificate validation |
| Insider threat | Least privilege, separation of duties, job rotation, DLP, monitoring/UEBA, offboarding |
| Removable media | Disable USB storage, DLP, endpoint control, awareness |
| Tailgating | Access control vestibule, badges, guards, awareness |
| Supply chain | Vendor vetting, SBOM, code signing, contracts, monitoring updates |
| VM escape / resource reuse | Patch hypervisor, isolate sensitive VMs, scrub memory/storage |
| Default credentials | Change at deployment, hardening baselines |
| Rooted/jailbroken, side-loaded apps | MDM compliance enforcement, app allow list, restrict stores |
| Rootkit / fileless | EDR, secure boot/integrity checks, application allow list, restrict scripting |
| Log tampering | Centralised/immutable logging (SIEM), restricted log access, hashing |
| Data leakage via shadow IT | CASB, DLP, policy, approved alternatives |

---

### Most-tested distinctions

- **Nation-state** (APT: well-funded, stealthy, espionage/war) vs **organized crime** (financial) vs **hacktivist** (belief/protest) vs **insider** (internal, access plus knowledge) vs **unskilled** (uses others' tools) vs **shadow IT** (unapproved tech from within).
- Internal vs external, resources/funding and sophistication are the three actor attributes; match motivation to actor.
- Phishing (mass) / spear phishing (targeted) / whaling (executives) / vishing (voice) / smishing (SMS) / BEC (financial request via business email).
- Typosquatting (misspelled domain) vs pharming (DNS redirect) vs watering hole (compromised site target frequents) vs brand impersonation.
- Pretexting (invented story) vs impersonation (pretending to be someone) vs elicitation (conversation) vs baiting (tempting item).
- Tailgating (without the person's knowledge/consent) vs piggybacking (authorised person knowingly lets you in); mitigated by access control vestibule.
- Client-based vs agentless software vectors; unsupported systems cannot be patched, so isolate or replace.
- Zero-day = no patch exists; patching can't fix it, so defense in depth.
- SQL injection (database) vs XSS (victim's browser) vs CSRF (forged authenticated request) vs directory traversal (`../`) vs buffer overflow (memory).
- VM escape (guest → host) vs resource reuse (leftover data between VMs) vs VM sprawl (unmanaged VMs).
- Side loading (unofficial app source) vs jailbreaking/rooting (removing OS restrictions).
- Worm (self-spreading) vs virus (needs host and user) vs trojan (disguised) vs logic bomb (conditional trigger) vs rootkit (hides, persists) vs fileless (memory only).
- Password spraying (many accounts, few passwords, avoids lockout) vs brute force (one target, all combos) vs dictionary vs credential stuffing (breach data) vs rainbow table (precomputed, defeated by salt).
- Amplified (response bigger than request) vs reflected (spoofed source bounces traffic to victim) DDoS.
- On-path (intercept/alter) vs replay (resend captured valid data) vs credential replay (reuse hashes/tokens).
- Downgrade (force weaker protocol) vs collision (same hash, two inputs) vs birthday (probabilistic collision search).
- Indicators: impossible travel and concurrent sessions = credential compromise; account lockout = guessing; missing logs = cover-up; resource consumption = malware/cryptojacking; resource inaccessibility = DoS/ransomware; out-of-cycle logging = unauthorised activity.
- Allow list (default deny) vs block list (known bad); segmentation (contain) vs isolation (cut off); hardening (reduce surface) vs configuration enforcement (prevent drift).
- Decommissioning = sanitise data, remove from inventory, revoke credentials; patching = known flaws only.

---

## Domain 3 — Security Architecture (18%)

Objectives 3.1–3.4. Reader assumed to know the basics; this is the exam-framed version.

---

### 3.1 Compare and contrast security implications of different architecture models

#### Architecture and infrastructure concepts

| Concept | Exam-framed definition |
|---|---|
| **Cloud** | On-demand, metered, shared-pool compute. Public (multi-tenant provider), private (single org), community (shared by orgs with common needs), hybrid (mix). Security hinges on the **shared responsibility model**. |
| **Responsibility matrix** | Contract/model dividing who secures what. The customer is *always* responsible for its data, identities/accounts, and access config. |
| **Hybrid** | On-prem plus cloud (or private plus public) connected together. Adds integration/connectivity risk, inconsistent policy, and larger attack surface. |
| **Third-party vendors** | Supply-chain/vendor risk. Controls: due diligence, SLAs, right-to-audit, SOC 2 reports, least-privilege vendor access, monitoring. You transfer *work*, not *accountability*. |
| **Infrastructure as code (IaC)** | Infrastructure defined in version-controlled templates (Terraform, CloudFormation, Ansible). Gives consistency, repeatability, auditability, drift detection, no configuration drift/snowflake servers. Risk: a flawed or secret-laden template is deployed everywhere. Scan templates. |
| **Serverless** | Function-as-a-Service (Lambda, Azure Functions). Provider manages OS/runtime; customer secures function code, permissions, and data. No servers to patch; short-lived, event-driven; hard to monitor/forensically capture. |
| **Microservices** | Application decomposed into small, independently deployable services communicating via APIs. Pros: isolation, independent scaling/patching. Cons: large API attack surface, service-to-service authentication, east-west traffic. |
| **Network infrastructure** | See below: physical isolation, air-gap, logical segmentation, SDN. |
| **Physical isolation** | Separate hardware and cabling, no shared medium. |
| **Air-gapped** | No network connection at all to other networks/internet. Data moves by removable media (a malware path: Stuxnet). Used for classified systems, ICS, backups. |
| **Logical segmentation** | Separation via VLANs, subnets, ACLs, firewalls, microsegmentation on shared hardware. Limits lateral movement. VLAN hopping is the attack. |
| **Software-defined networking (SDN)** | Control plane separated from data plane; centralized controller programs the network via APIs. Application / control / data (infrastructure) planes. Enables dynamic policy and microsegmentation; the controller is a high-value target. |
| **On-premises** | Org owns and operates everything. Full control and customization; org bears all cost, patching, physical security, capacity. |
| **Centralized** | Single point of administration/processing. Easier to secure and audit and enforce policy; single point of failure and a juicy target. |
| **Decentralized** | Distributed control/processing (e.g., blockchain, peer-to-peer, branch autonomy). No single point of failure; harder to govern, inconsistent policy, harder to patch and monitor. |
| **Containerization** | OS-level virtualization; containers share the host kernel (Docker, Kubernetes). Lightweight and fast, but weaker isolation than VMs; kernel vulnerability or container escape affects all. Secure images, registries, and orchestrator (K8s) config. |
| **Virtualization** | Hypervisor runs multiple VMs, each with its own OS. Type 1 (bare-metal: ESXi, Hyper-V, KVM) vs Type 2 (hosted: VirtualBox, Workstation). Risks: **VM escape**, **VM sprawl**, hypervisor compromise, snapshots storing secrets/memory. |
| **IoT** | Smart devices (cameras, sensors, thermostats). Weak/default credentials, no patching, limited compute, long lifespans. Mitigate: segment on own VLAN, change defaults, disable unused services. |
| **ICS** | Industrial control systems: control physical processes (plants, grids, HVAC). |
| **SCADA** | Supervisory Control and Data Acquisition: ICS variant for geographically distributed sites (pipelines, utilities); HMI + PLCs/RTUs. Legacy protocols (Modbus, DNP3), availability and safety prioritized over confidentiality; segment/air-gap, strict change control. |
| **RTOS** | Real-time operating system: deterministic, guaranteed response times. Used in ICS, medical, automotive. Constraints: rarely patched, limited resources, no room for security agents. |
| **Embedded systems** | Purpose-built hardware+firmware (printers, medical devices, PLCs, smart TVs, SoC). Hard to patch, long lifecycle, often default credentials, firmware vulnerabilities. |
| **High availability (HA)** | Design for minimal downtime: redundancy, failover, load balancing, clustering, no single point of failure. Measured as uptime ("nines"). (Detail in 3.4.) |

> **Exam tip:** Air gap vs logical segmentation: air gap = no connection whatsoever; VLAN/firewall = still connected. "Highest isolation / classified / ICS safety" = air gap.

> **Exam tip:** Containers share a **kernel**; VMs each have their own OS. "Lightweight, fast to deploy, shares host OS" = container. "VM escape" = virtualization, not containers (those are "container escape").

> **Exam tip:** Serverless/FaaS: "no patching the OS, pay per execution, event-driven." Microservices: "independent services, APIs, scale each separately."

> **Exam tip:** ICS/SCADA/RTOS/embedded/IoT keyword set → "cannot be patched easily, compensating controls: segmentation, air-gap, monitoring, virtual patching (IPS), allow-lists."

#### Cloud responsibility matrix

| Layer | On-prem | IaaS | PaaS | SaaS |
|---|---|---|---|---|
| Data, accounts/identities, access config | Customer | **Customer** | **Customer** | **Customer** |
| Application | Customer | Customer | Customer | Provider |
| Runtime / middleware | Customer | Customer | Provider | Provider |
| Operating system | Customer | Customer | Provider | Provider |
| Virtualization / hypervisor | Customer | Provider | Provider | Provider |
| Servers, storage, network hardware | Customer | Provider | Provider | Provider |
| Physical facility / datacenter | Customer | Provider | Provider | Provider |

- **IaaS** (EC2, Azure VMs): customer gets VMs/storage/networks; patches the guest OS.
- **PaaS** (App Engine, Azure App Service, RDS): customer deploys code/data; provider handles OS and runtime.
- **SaaS** (M365, Salesforce, Gmail): customer manages users, data, and config only.
- **FaaS/serverless** sits at PaaS-and-above: customer owns code and permissions only.

> **Exam tip:** "Who patches the guest OS?" IaaS = customer; PaaS/SaaS = provider. "Who is always responsible for data?" Customer. Provider is *always* responsible for the physical facility (except private cloud/on-prem).

#### Considerations table (by model)

| Model | Strengths | Weaknesses |
|---|---|---|
| **On-premises** | Full control; no third-party dependency; data location certain; predictable latency | High capex; org does all patching/power/cooling/physical; slow to scale; own DR needed |
| **Public cloud** | Elastic scalability; low upfront cost (opex); fast deployment; provider resilience; risk partly transferred | Shared responsibility confusion; multi-tenancy; vendor lock-in; data sovereignty; misconfiguration (open buckets) |
| **Private cloud** | Control and isolation; custom compliance | Costly; org capacity-limited; org patches |
| **Hybrid** | Burst to cloud; keep sensitive data on-prem; flexible DR | Complexity; connectivity/integration risk; inconsistent policies |
| **Containers / microservices** | Fast deployment; scalable; portable; small patchable units | Shared kernel; image supply chain; orchestration complexity |
| **Serverless** | No server patching; auto-scale; pay-per-use | Limited visibility; vendor lock-in; function-permission sprawl; cold-start latency |
| **IaC** | Repeatable, fast, auditable, low drift; ease of recovery (redeploy) | Template flaws replicated at scale; secrets in repos |
| **Virtualization** | Consolidation (cost); snapshots/ease of recovery; rapid provisioning | VM escape; sprawl; hypervisor is single point of failure |
| **SDN** | Central policy; automation; fast reconfiguration; microsegmentation | Controller is single point of failure/target; complexity |
| **Centralized** | Easy governance, patching, monitoring | Single point of failure/compromise |
| **Decentralized** | Resilience; no single point of failure | Governance, inconsistency, hard to patch and audit |
| **ICS/SCADA/RTOS/embedded/IoT** | Purpose-built; deterministic; low power/cost | Often **cannot be patched**; legacy protocols; long life; limited compute |
| **Air-gapped** | Strongest isolation | Inconvenient; removable-media path; manual updates; hard to patch |

#### The considerations list (how the exam words them)

| Consideration | What it means in a scenario |
|---|---|
| **Availability** | Uptime requirement; drives redundancy/HA. |
| **Resilience** | Ability to withstand and recover from failure/attack. |
| **Cost** | Capex (on-prem) vs opex (cloud); HA and hot sites cost more. |
| **Responsiveness** | Latency/performance; edge, CDN, on-prem for real-time (RTOS). |
| **Scalability** | Handle growth. *Horizontal* (add nodes, elasticity) vs *vertical* (bigger node). Cloud wins. |
| **Ease of deployment** | IaC, containers, SaaS are fast; on-prem/embedded are slow. |
| **Risk transference** | Shifting financial/operational risk to provider/insurer via contract (cloud SLA, cyber insurance). Accountability stays with you. |
| **Ease of recovery** | Snapshots, IaC redeploy, VM images, cloud backup beat bare-metal rebuild. |
| **Patch availability** | Does the vendor still ship patches? (End-of-life = no.) |
| **Inability to patch** | Embedded/ICS/IoT/legacy: use segmentation, compensating controls, virtual patching, replace. |
| **Power** | Consumption and continuity: UPS/generator; IoT/embedded battery constraints. |
| **Compute** | Processing capacity; constrained devices cannot run agents or strong crypto. |

> **Exam tip:** "Cannot be patched" or "legacy" → segment/isolate + compensating controls. "Transfer risk" → insurance or cloud/SLA (never fully eliminates responsibility).

---

### 3.2 Given a scenario, apply security principles to secure enterprise infrastructure

#### Infrastructure considerations

| Concept | Exam-framed definition |
|---|---|
| **Device placement** | Where a control sits determines what it sees/blocks: firewall at the perimeter and between zones; IDS/IPS inline or on a tap; WAF in front of web apps; proxies at the edge; jump server in the DMZ/management zone; honeypots in DMZ/internal. |
| **Security zones** | Trust-based network areas: **untrusted** (internet), **DMZ/screened subnet** (public-facing servers), **trusted/internal**, **management**, **guest**, **extranet**. Traffic crossing zones is filtered by a firewall. |
| **Attack surface** | Sum of exposed entry points (ports, services, APIs, users, devices). Reduce by disabling services, closing ports, segmentation, patching, least privilege. |
| **Connectivity** | How devices attach: wired, wireless, cellular, VPN, third-party links. Every link is a path; secure with encryption, NAC, and filtering. |
| **Failure modes** | What a device does when it fails (below). |
| **Fail-open** | On failure, traffic/access **passes**; favors availability and safety (fire doors unlock). |
| **Fail-closed** | On failure, traffic/access is **blocked**; favors security/confidentiality (firewall denies all, door locks). |
| **Fail-safe vs fail-secure** | Safe = protect people (unlock). Secure = protect assets (lock). |
| **Active** | Takes action (IPS, firewall blocking). |
| **Passive** | Observes and alerts only (IDS, tap). |
| **Inline** | Traffic physically passes through the device; can block; can be a point of failure/latency. |
| **Tap/monitor (SPAN)** | Device receives a copy via TAP or switch SPAN/mirror port; cannot block; no impact on traffic. |

> **Exam tip:** Fail-open = availability/safety priority; fail-closed = security priority. An inline IPS that fails open lets attacks through; one that fails closed causes an outage.

> **Exam tip:** Inline + active = IPS. Tap/SPAN + passive = IDS. "Cannot affect production traffic" = passive/tap.

#### Network appliances

| Appliance | Definition / how it is tested |
|---|---|
| **Jump server** | Hardened, monitored host in a DMZ/management zone used as the single admin path to systems in a more secure segment. Logged; MFA. Keyword: "secure administrative access to isolated devices." |
| **Forward proxy** | Sits in front of **clients**; filters outbound web traffic, caches, enforces acceptable use, hides client IPs. |
| **Reverse proxy** | Sits in front of **servers**; terminates TLS, hides origin servers, load balances, can host WAF. Keyword: "protect the web server / inbound." |
| **Transparent proxy** | Intercepts without client config. |
| **IDS** | Detects and alerts; passive, out of band. |
| **IPS** | Detects and blocks; active, inline. |
| **Load balancer** | Distributes traffic across servers (round-robin, least connections, weighted); health checks; session persistence (affinity); can be L4 or L7; provides availability and scalability. Active/active or active/passive. |
| **Sensors** | Collect data (network/host) and feed IDS/SIEM/NDR: network sensors, taps, agents. |
| **Collectors** | Aggregate sensor data for analysis (SIEM ingestion). |

IDS/IPS detection methods: **signature** (known patterns), **anomaly/behavior** (baseline deviation; more false positives, catches unknown), **heuristic**, **policy**.

| IDS | IPS |
|---|---|
| Passive, tap/SPAN | Active, inline |
| Alerts | Blocks/drops/resets |
| Failure does not affect traffic | Failure can break traffic (fail-open/closed decision) |
| False positive = noise | False positive = blocked legit traffic |

#### Port security

- **Port security (MAC filtering/sticky MAC):** limit MACs per switch port; violation action shutdown/restrict. Mitigates MAC flooding and rogue devices.
- **BPDU guard / root guard / loop prevention (STP):** stop rogue switches altering topology.
- **DHCP snooping / dynamic ARP inspection:** block rogue DHCP and ARP spoofing.
- **802.1X:** port-based network access control (NAC). Three roles: **supplicant** (client), **authenticator** (switch/AP/WLC), **authentication server** (RADIUS). Port stays blocked (only EAPoL) until authentication succeeds.

| EAP variant | Key facts |
|---|---|
| **EAP-TLS** | Mutual certificate auth (client and server certs). Strongest; needs PKI on every client. |
| **PEAP** | Server cert only builds a TLS tunnel; client authenticates inside with MSCHAPv2/password. Most common. |
| **EAP-TTLS** | Like PEAP; tunnel then almost any inner method (PAP, CHAP, MSCHAPv2); client cert optional. |
| **EAP-FAST** | Cisco; uses PAC (protected access credential) instead of certificates. Replaces LEAP. |
| **EAP-MD5** | One-way, weak, no mutual auth. Avoid. |
| **LEAP** | Legacy Cisco, crackable. Avoid. |

> **Exam tip:** "Mutual authentication with certificates on both sides" = EAP-TLS. "Only server cert / password inside tunnel" = PEAP or EAP-TTLS. "No certificates / PAC" = EAP-FAST.

> **Exam tip:** 802.1X = port-based NAC with RADIUS. Don't confuse with 802.11 (Wi-Fi) or 802.1Q (VLAN trunking).

#### Firewall types

| Type | Layer | What it does |
|---|---|---|
| **Packet filter / stateless** | L3–4 | Rule per packet (IP, port, protocol); no session memory. |
| **Stateful** | L3–4 | Tracks connection state; allows return traffic automatically. |
| **Layer 4 firewall** | Transport | Decisions on IP/port/protocol only; cannot see content. |
| **Layer 7 / application firewall** | Application | Inspects payload/application protocol (HTTP, SQL, DNS); identifies apps and content. |
| **NGFW** | L7 | Stateful plus app awareness, user identity, integrated IPS, TLS inspection, threat intelligence. |
| **UTM** | Multi | All-in-one appliance: firewall, IPS, AV, content/URL filter, VPN, anti-spam. Single point of failure; aimed at SMB. |
| **WAF** | L7 (HTTP/S) | Protects web apps from SQLi, XSS, CSRF, etc.; reverse-proxy placement; virtual patching for web apps. |
| **Host-based firewall** | Endpoint | Per-device policy; protects when off-network. |

Rule hygiene: ACLs processed top-down, first match wins; **implicit deny** at the end; put specific rules before general ones; least-privilege (deny by default); document and review rules.

> **Exam tip:** SQL injection/XSS against a web app → **WAF**. Block by application/user, deep inspection → **NGFW**. Many security functions in one box → **UTM**. Only IP/port → L4 (or stateless packet filter).

#### Secure communication/access

| Technology | Definition |
|---|---|
| **VPN site-to-site** | Gateway-to-gateway tunnel (always-on) connecting two networks; users unaware. Typically IPSec. |
| **VPN remote access** | Individual client to gateway; user-initiated, with client or clientless (browser/SSL VPN). |
| **Split tunnel** | Only corporate traffic via VPN; internet direct. Less load, more risk. |
| **Full tunnel** | All traffic via VPN; full inspection. |
| **TLS (SSL VPN)** | Transport-layer encryption; port 443; works through firewalls/NAT; client or browser-based. Application-level access. |
| **IPSec** | Network layer (L3) suite; encrypts any IP traffic; IKE (UDP 500, NAT-T UDP 4500) negotiates SAs. |
| **AH (Authentication Header)** | Integrity + authentication (+anti-replay); **no encryption**; protocol 51; breaks under NAT. |
| **ESP (Encapsulating Security Payload)** | Confidentiality + integrity + authentication; protocol 50; works with NAT-T. Normally used. |
| **Transport mode** | Encrypts payload only; original IP header kept; host-to-host. |
| **Tunnel mode** | Encrypts entire original packet and adds a new IP header; gateway-to-gateway (site-to-site VPN). |
| **SD-WAN** | Software-defined overlay managing multiple WAN links (MPLS, broadband, LTE); application-aware routing, centralized policy, encryption, zero-touch branch provisioning. |
| **SASE** | Secure Access Service Edge: cloud-delivered convergence of **SD-WAN plus network security** (SWG, CASB, ZTNA, FWaaS) at the edge close to the user. Keyword: "branch/remote workforce, cloud-delivered security, single vendor." |

> **Exam tip:** AH = no encryption. ESP = encryption. Tunnel mode = new header, gateway-to-gateway. Transport mode = host-to-host, original header. TLS VPN = port 443, easy through firewalls.

> **Exam tip:** SD-WAN = connectivity/WAN optimization. SASE = SD-WAN **plus** cloud security services.

#### Selection of effective controls

Match the control to the scenario: need to block in real time → IPS/NGFW; web-app attacks → WAF; secure admin access → jump server + MFA; unknown or unpatchable device → segment/VLAN + ACL; rogue device → 802.1X/NAC; remote workers → VPN/ZTNA/SASE; encrypt data crossing untrusted networks → TLS/IPSec; filter egress/web use → forward proxy. Prefer defense in depth, least privilege, and zero trust (verify explicitly; microsegmentation). Controls must address the stated risk at acceptable cost, and fit failure-mode requirements (availability vs security).

---

### 3.3 Compare and contrast concepts and strategies to protect data

#### Data types

| Type | Definition |
|---|---|
| **Regulated** | Governed by law/standard: PII, PHI (HIPAA), financial/cardholder (PCI DSS), GDPR personal data. Breach brings fines/notification. |
| **Trade secret** | Proprietary info giving competitive edge (formulas, algorithms); protected by NDAs, access control. |
| **Intellectual property** | Patents, copyrights, trademarks. |
| **Legal information** | Contracts, case files, privileged communications. |
| **Financial information** | Account data, statements, payment info. |
| **Human-readable** | Plain text people can read directly. |
| **Non-human-readable** | Binary, encoded, database, machine formats; still sensitive. |

#### Classifications

| Label | Exam-framed meaning |
|---|---|
| **Public** | Approved for release; no harm if disclosed (marketing, published prices). |
| **Private** | Internal or personal information not for public release (employee records, internal memos); often contains PII. |
| **Sensitive** | Would cause harm if disclosed; access limited (PII, financial details). Also used loosely as an umbrella for "anything non-public". |
| **Confidential** | Highly sensitive business data (trade secrets, source code, contracts); serious damage if disclosed; need to know. |
| **Restricted** | Most tightly controlled; strict need to know, often bound by law or contract; severe damage if disclosed. |
| **Critical** | Data the business cannot operate without; the emphasis is **availability** (backup/recovery priority). |

Government scheme for comparison (highest to lowest): Top Secret > Secret > Confidential > Unclassified (with CUI for controlled-but-unclassified data).

> **Exam tip:** CompTIA does not fix a single commercial hierarchy; questions describe the data and you pick the label. "Must stay available or operations stop" = critical. "Most restricted access" = restricted/confidential. Government order is fixed: Top Secret is highest.

Classification drives handling, labeling, retention, access, and encryption. Data **owner** classifies; **custodian** implements controls; **steward** quality/policy; **controller** decides purpose and means (GDPR); **processor** processes on behalf of the controller.

#### States of data

| State | Definition | Primary protections |
|---|---|---|
| **At rest** | Stored on disk, DB, backup, USB | Full-disk/volume (BitLocker, LUKS), file/DB encryption (TDE), access controls, HSM/TPM for keys |
| **In transit / in motion** | Moving across a network | TLS, IPSec, SSH, VPN, WPA3, S/MIME |
| **In use** | Being processed in memory/CPU | Secure enclaves, confidential computing, memory protection, screen locks, DLP; hardest to protect |

> **Exam tip:** Data in use = RAM/CPU; encryption is hardest. Keyword "enclave / confidential computing / TEE" = in use.

#### Data sovereignty and geolocation

- **Data sovereignty:** data is subject to the laws of the country where it is stored/collected (GDPR, residency laws). Cloud region choice and backups matter.
- **Geolocation:** physical or logical location of data/users/devices. Used for policy (geofencing, conditional access), and compliance. IP-based location can be spoofed (VPN).

#### Methods to secure data

| Method | Definition (as tested) |
|---|---|
| **Geographic restrictions (geofencing)** | Allow/deny access or storage based on location; supports sovereignty. |
| **Encryption** | Reversible ciphertext protection with a key (AES, RSA). Full-disk, volume, partition, file, database, record/field. |
| **Hashing** | One-way digest for **integrity** and password storage; not reversible. |
| **Masking** | Hides part of the value with substitute characters (`XXX-XX-1234`); display-level. Static (permanent copy) or dynamic (on the fly). Original may still exist. |
| **Tokenization** | Replaces data with a random **token**; mapping held in a secure vault; token has no mathematical relation to original. Reduces PCI scope. |
| **Obfuscation** | Making data/code hard to understand (scrambling, shuffling, substitution, steganography). Not strong security alone. |
| **Segmentation** | Isolating data/systems (network, database, tenant) to limit exposure and lateral movement. |
| **Permission restrictions** | Access controls (ACLs, RBAC, least privilege, need to know, file/share permissions). |
| **Anonymization / pseudonymization** | Anonymization irreversibly removes identity; pseudonymization replaces identifiers with a reversible alias (re-identification possible with extra info). |
| **DLP** | Detects/blocks exfiltration by content inspection (endpoint, network, cloud). |
| **Data minimization / retention** | Collect and keep only what is needed; destroy when expired. |

#### Scenario → method

| Scenario | Method |
|---|---|
| Laptop is lost or stolen | Full-disk encryption |
| Protect data on a database column but reversible by authorized app | Field-level / database encryption |
| Credit card number stored for recurring billing; reduce PCI scope | **Tokenization** |
| Support agents may see only last four digits of SSN | **Masking** |
| Verify file was not altered; store passwords | **Hashing** (salted) |
| Developers need realistic test data without real PII | Static masking / anonymization |
| Data must stay in the EU | Geographic restriction / region lock (sovereignty) |
| Limit who can open a file | Permission restrictions (least privilege) |
| Isolate regulated data from the rest of the network | Segmentation |
| Prevent employees emailing out customer records | DLP |
| Customer records must be unrecoverable by anyone | Anonymization |
| Data crossing the internet | TLS / IPSec VPN |
| Data being processed in memory | Secure enclave / confidential computing |

> **Exam tip:** Masking vs tokenization: masking hides part of a value for **display**; tokenization **replaces** the value with a surrogate, original in a vault. Tokenization is not mathematically reversible; encryption is.

> **Exam tip:** Hashing = integrity, not confidentiality. Encryption = confidentiality, reversible with key. Pseudonymization is reversible; anonymization is not.

---

### 3.4 Explain the importance of resilience and recovery in security architecture

#### High availability

| Concept | Definition |
|---|---|
| **High availability** | Systems remain operational with minimal downtime; no single point of failure. |
| **Load balancing** | Spreads requests across multiple **active** nodes for performance and availability; nodes typically independent and stateless. |
| **Clustering** | Multiple nodes act as one system sharing state/storage; **failover** to a standby on node failure. Active/active or active/passive. |

> **Exam tip:** Load balancing = distribute work (performance + availability). Clustering = redundancy via failover (availability). "Servers appear as a single system" = cluster.

#### Site considerations

| Site | Description | Cost | Recovery time |
|---|---|---|---|
| **Hot** | Fully equipped, live data replication, mirror of production | Highest | Minutes to hours (near zero) |
| **Warm** | Hardware/connectivity in place, data restored from recent backup | Medium | Hours to days |
| **Cold** | Space, power, and connectivity only; bring equipment and data | Lowest | Days to weeks |
| **Mobile site** | Trailer/portable datacenter | Variable | Depends |

Also: **hot/cold aisles** are datacenter cooling, not DR sites. **Reciprocal agreement** = mutual-use with a partner (cheap, unreliable).

> **Exam tip:** Lowest RTO = hot. Cheapest = cold. "Balanced cost and recovery" = warm.

#### Resilience concepts

| Concept | Definition |
|---|---|
| **Geographic dispersion** | Spreading sites/data far apart so a regional disaster cannot take out all (but latency, sovereignty). |
| **Platform diversity** | Different OSes, vendors, hardware, and technologies so one vulnerability or failure doesn't hit everything. Related: technology diversity, vendor diversity, crypto diversity, control diversity. |
| **Multi-cloud systems** | Using several cloud providers to avoid lock-in/outage dependence; adds complexity and inconsistent security tooling. |
| **Continuity of operations planning (COOP)** | Plan to keep essential functions running during/after disruption (alternate site, succession, communications, essential records). Often government-framed. |
| **Capacity planning** | Ensuring resources meet demand across **people** (staff/skills for incident and recovery), **technology** (hardware, bandwidth, licenses, cloud scale) and **infrastructure** (facilities, power, cooling, space). |

#### Testing

| Test | Definition |
|---|---|
| **Tabletop exercise** | Discussion-based walkthrough of a scenario; no systems touched; cheapest. |
| **Failover test** | Actually switch production to the secondary/redundant system to prove it works. |
| **Simulation** | Scenario-driven exercise that mimics an incident with realistic injects (drill/live-fire like phishing sim or DR drill) without full production impact. |
| **Parallel processing** | Run the recovery/backup system alongside production, processing the same data; production unaffected; compare results. |
| **Walkthrough / checklist** | Review plans for accuracy. |
| **Full interruption** | Shut down production and run on DR; riskiest. |

> **Exam tip:** Tabletop = talk only. Failover = production moves. Parallel = both run at once. Simulation = realistic scenario drill.

#### Backups

| Concept | Definition |
|---|---|
| **Onsite** | Fast restore; vulnerable to the same disaster as the source. |
| **Offsite** | Different location or cloud; survives site disaster; slower restore; transport risk. |
| **3-2-1 rule** | 3 copies, 2 media types, 1 offsite (plus immutable/offline copy against ransomware). |
| **Frequency** | Set by RPO; more frequent = less data loss, more resource use. |
| **Encryption** | Encrypt backups at rest and in transit; protect keys separately. |
| **Snapshots** | Point-in-time state of a VM/volume; fast; not a true backup if on same storage. |
| **Recovery** | Restore process; test restores regularly; verify integrity. |
| **Replication** | Continuous/near-real-time copy to another system or site (synchronous: no data loss, latency; asynchronous: slight lag). Replicates corruption/ransomware too. |
| **Journaling** | Logs changes before/as committed so data can be replayed/rolled back to a consistent state (file systems, databases); allows recovery after crash. |

| Backup type | Backs up | Backup speed | Restore needs | Archive bit |
|---|---|---|---|---|
| **Full** | Everything | Slowest, most storage | Latest full only (fastest restore) | Cleared |
| **Incremental** | Changes since **last backup of any type** | Fastest, least storage | Last full + **every** incremental (slowest restore) | Cleared |
| **Differential** | Changes since **last full** | Moderate (grows daily) | Last full + **latest** differential | Not cleared |

> **Exam tip:** Fastest backup, slowest restore = incremental. Fastest restore = full. Compromise = differential (restore needs only two sets).

#### Power

| Item | Definition |
|---|---|
| **UPS** | Battery bridging short outages (minutes); conditions power (surge, sag); allows graceful shutdown. Online (double-conversion) vs line-interactive vs standby. |
| **Generator** | Fuel-powered long-term backup; startup delay so UPS bridges the gap; fuel supply and testing needed. |
| **Dual power supplies / redundant feeds / PDUs** | Remove power single points of failure. |
| **Managed PDU** | Remote monitoring/control of outlets. |

> **Exam tip:** UPS = short-term, immediate. Generator = long-term, delayed start. They are used together.

---

### Most-tested distinctions

- **Shared responsibility:** customer always owns data, identities, and access config; IaaS customer patches the OS, PaaS/SaaS provider does.
- **Container vs VM:** containers share the host kernel (lighter, weaker isolation); VMs have separate OS (VM escape risk).
- **Air gap vs logical segmentation:** no connection at all vs VLAN/firewall separation. ICS/SCADA/RTOS/embedded/IoT can't patch easily: segment, air-gap, virtual patch.
- **Risk transference** moves financial impact, not accountability.
- **Fail-open (availability/safety) vs fail-closed (security)**; inline IPS failure choice.
- **IDS (passive, tap, alert) vs IPS (active, inline, block).**
- **Forward proxy (clients/outbound) vs reverse proxy (servers/inbound).**
- **802.1X EAP:** EAP-TLS mutual certs; PEAP/TTLS server cert and tunnel; EAP-FAST uses PAC.
- **WAF (web app attacks) vs NGFW (L7 app/user aware) vs UTM (all-in-one) vs L4 (IP/port only).**
- **IPSec:** AH = integrity only; ESP = encryption; tunnel mode = gateway-to-gateway with new header; transport = host-to-host.
- **SD-WAN vs SASE:** SASE = SD-WAN plus cloud-delivered security (SWG, CASB, ZTNA).
- **Masking (display hiding) vs tokenization (vault surrogate) vs encryption (reversible with key) vs hashing (one-way).**
- **Data states:** at rest, in transit, in use (hardest; enclaves).
- **Data sovereignty:** law of the country where data resides; solve with region restrictions.
- **Hot/warm/cold:** cost down, recovery time up; hot = near zero downtime.
- **Load balancing (distribute) vs clustering (single logical system, failover).**
- **Tabletop (discussion) vs failover (real switch) vs parallel (both run) vs simulation.**
- **Incremental (fast backup, slow restore) vs differential (growing, two-set restore) vs full.** Replication copies corruption too; backups/snapshots give point-in-time recovery.
- **UPS (short, instant) vs generator (long, delayed).**

---

## Domain 4 — Security Operations (28%)

Largest domain. Expect many scenario and PBQ items (firewall rules, log analysis, IAM, IR ordering).

---

### 4.1 Given a scenario, apply common security techniques to computing resources

#### Secure baselines
- **Establish** the approved secure configuration (CIS Benchmark, vendor guide, DISA STIG), **deploy** it (golden image, GPO, MDM, config management), **maintain** it (re-baseline after approved changes, detect drift).
- Baseline = "what good looks like"; deviation from it = configuration drift = finding.

#### Hardening targets

| Target | Typical hardening actions |
|---|---|
| Mobile devices | MDM, screen lock, encryption, remote wipe, disable sideloading |
| Workstations | Remove bloatware, disable unused services, patch, host firewall, EDR, disk encryption |
| Switches | Disable unused ports (assign to an unused VLAN), port security/802.1X, change defaults, SSH not Telnet, SNMPv3, patch firmware |
| Routers | Change defaults, SSH/HTTPS management only, ACLs on management interfaces, disable unused services, secure routing updates, patch firmware |
| Cloud infrastructure | Least-privilege IAM, no public storage buckets, CSPM, security groups, logging on |
| Servers | Role-only services, remove defaults, patch, restrict admin access, host firewall |
| ICS / SCADA | Segmentation/air gap, no direct internet, strict change control, passive monitoring |
| Embedded systems | Limited patchability: isolate, change default creds, disable unused interfaces, apply vendor firmware when available |
| RTOS | Deterministic and resource-constrained (no room for agents): segment, restrict network access, vendor-supplied updates only |
| IoT devices | Change default creds, isolate on own VLAN, disable UPnP, update firmware |

Core hardening list: remove/disable unnecessary software, accounts and services; close unused ports; change default credentials; patch; host firewall; encrypt disks.

#### Wireless devices
- **Installation considerations** (the exam's sub-bullets are site surveys and heat maps): AP placement (coverage vs. leakage), channel planning (2.4 GHz: 1/6/11 non-overlapping; 5 GHz has more channels), antenna type/power, PoE, wired backhaul.
- **Site survey:** physically measures RF coverage, interference and dead zones; done before and after deployment.
- **Heat map:** visual overlay of signal strength on a floor plan, output of a site survey. Keyword: "visualize coverage/dead spots" -> heat map.
- Rogue AP detection and WIPS belong here too.

#### Mobile solutions
- **MDM (Mobile Device Management):** enforces policy on devices: enrollment, app allow/deny lists, remote wipe, geofencing, containerization, encryption, passcode, patch/OS enforcement. **MAM** manages apps only; **UEM** unifies MDM+endpoint management.

| Model | Device owner | Who chooses device | Personal use | Exam keyword |
|---|---|---|---|---|
| BYOD (bring your own device) | Employee | Employee | Yes | Lowest cost; hardest to control; needs containerization/MDM |
| COPE (corporate-owned, personally enabled) | Company | Company | Yes | Company control + personal use allowed |
| CYOD (choose your own device) | Company | Employee picks from approved list | Usually yes | Approved menu of devices |
| COBO (corporate-owned, business only) | Company | Company | No | Strictest (not in the 4.1 list, but appears as a distractor) |

> **Exam tip:** "Employees pick from a list the company offers" = CYOD. "Company-owned but personal use allowed" = COPE. "Own phone" = BYOD.

- **Connection methods** (the exam lists cellular, Wi-Fi, Bluetooth):

| Method | Security implication |
|---|---|
| **Cellular** | Carrier network, encrypted to the tower but **outside corporate control/monitoring**; a phone on cellular bypasses corporate firewall/DLP. Risks: rogue base stations (IMSI catchers, SIM swap). Use VPN/ZTNA and MDM. |
| **Wi-Fi** | Untrusted public hotspots, evil twin/rogue AP, on-path attacks. Use WPA3/802.1X on corporate Wi-Fi, always-on VPN elsewhere, disable auto-join. |
| **Bluetooth** | Short-range PAN. Attacks: bluejacking (unsolicited messages), bluesnarfing (data theft), bluebugging (device control). Disable discoverable mode, require pairing PIN, turn off when unused. |
| Others | NFC (centimetres, contactless pay, relay risk), USB/tethering/hotspot (bridges networks, bypasses controls), infrared, point-to-point/ad hoc. Disable unused radios via MDM. |

- Mobile security features: biometrics, lock screen/PIN, remote wipe, full-device encryption, containerization/app sandboxing, geofencing, geotagging controls, content management.

#### Wireless security settings
- **WPA3:** Personal uses **SAE** (Simultaneous Authentication of Equals, "Dragonfly") instead of WPA2-PSK, so a captured handshake cannot be brute-forced offline; per-session keys give forward secrecy; **PMF** (protected management frames) mandatory, stopping deauth attacks; Enterprise offers a 192-bit (CNSA, GCMP-256) mode. **OWE** (Opportunistic Wireless Encryption, "Enhanced Open") encrypts open/guest networks without a password.
- **WPA2:** AES-CCMP. **WPA:** TKIP (deprecated). **WEP:** RC4, broken.
- **AAA / RADIUS:** 802.1X port-based access control. Supplicant (client) -> authenticator (AP/switch) -> authentication server (RADIUS). RADIUS = UDP 1812/1813, encrypts only password; TACACS+ = TCP 49, encrypts entire payload, separates AAA, Cisco-origin (device admin). Diameter is RADIUS successor.
- **Cryptographic protocols:** WPA2 = AES-**CCMP**; WPA3 = AES-CCMP (Personal) or **GCMP-256** (Enterprise 192-bit). TKIP and WEP/RC4 are the wrong answers. TLS is used inside EAP methods.
- **Authentication protocols (EAP family):**

| Method | Server cert | Client cert | Tunnel | Notes |
|---|---|---|---|---|
| EAP-TLS | Yes | **Yes** (mutual) | TLS | Strongest; requires PKI on every client |
| PEAP | Yes | No | TLS tunnel protects inner (MS-CHAPv2) | Microsoft/Cisco/RSA; username+password inside tunnel |
| EAP-TTLS | Yes | No (optional) | TLS tunnel | Like PEAP; supports more inner methods (PAP, CHAP) |
| EAP-FAST | No (uses PAC) | No | Protected Access Credential tunnel | Cisco; replaced LEAP; no certs needed |
| LEAP | - | - | None | Cisco legacy, crackable, avoid |

> **Exam tip:** "Certificates on both client and server" = EAP-TLS. "Cisco, no certificates, PAC" = EAP-FAST. "Tunnel + password only client" = PEAP/EAP-TTLS.

- **WPS** (PIN-based) is brute-forceable: disable. **Captive portal** = guest web auth. **Open network + OWE** for guests.

#### Application security
- **Input validation:** whitelist/allow-list expected type, length, format, range on the server side; stops injection and overflows. Client-side validation alone is not security.
- **Secure cookies:** `Secure` (HTTPS only), `HttpOnly` (not readable by JavaScript; stops XSS cookie theft), `SameSite` (mitigates CSRF).
- **Static code analysis (SAST):** analyzes source/binaries without running; finds flaws early. **Dynamic analysis (DAST)/fuzzing:** tests the running app with malformed input.
- **Code signing:** digital signature on code proves publisher identity and integrity (not that it is bug-free).
- Also: secure coding practices, manual code review, dependency/package scanning.

#### Sandboxing
Run untrusted code/files/apps in an isolated environment with restricted access to host (malware detonation, browser tabs, mobile apps, containers). Contains damage; used for analysis.

#### Monitoring
Continuous collection of logs and telemetry from hardened resources (SIEM, EDR, FIM, config-compliance scans) so baseline drift, attacks and policy violations are detected quickly. Hardening without monitoring cannot show that a baseline is still in place (see 4.4).

---

### 4.2 Explain the security implications of proper hardware, software, and data asset management

- **Acquisition/procurement process:** vetted vendors, security requirements in contracts, supply chain risk review, approved purchase channels, ownership documented at purchase.
- **Assignment/accounting:**
  - **Ownership:** every asset has a named owner accountable for it.
  - **Classification:** asset labeled by sensitivity/criticality; drives handling and protection.
- **Monitoring/asset tracking:**
  - **Inventory:** authoritative list of hardware, software, data (CMDB). You cannot protect what you do not know exists; unknown assets = shadow IT.
  - **Enumeration:** discovering and listing assets (network scans, agents, NAC).
  - Also tag/barcode/RFID, lifecycle tracking, license tracking.
- **Disposal/decommissioning:**
  - **Sanitization:** make data unrecoverable while device may be reused (overwrite, crypto erase, secure erase for SSDs, degauss for magnetic media). Standard: NIST SP 800-88 (clear, purge, destroy).
  - **Destruction:** physically destroy media (shred, pulverize, incinerate, disintegrate). Required for highest sensitivity or non-sanitizable media. Degaussing does not work on SSDs.
  - **Certification:** documented proof (certificate of destruction/sanitization), often from a third-party vendor, for audit/compliance.
  - **Data retention:** keep data only as long as legal/business need requires, then dispose per policy; retain disposal records. Over-retention = liability; premature deletion = compliance violation (and legal hold overrides schedules).

| Method | Media reusable? | Notes |
|---|---|---|
| Overwrite / wipe | Yes | Multiple passes mostly legacy; weak for SSD wear-leveling |
| Crypto erase | Yes | Destroy key of encrypted drive |
| Degauss | HDD no longer usable | Magnetic only |
| Shred / pulverize / incinerate | No | Physical destruction |
| Deleting / formatting | Data recoverable | Not sanitization |

> **Exam tip:** "Prove to auditors the drives were destroyed" -> certification. "Reuse the drive but remove data" -> sanitization. "SSD" -> not degauss; use crypto erase or physical destruction.

---

### 4.3 Explain various activities associated with vulnerability management

#### Identification methods
- **Vulnerability scan:** automated discovery of known weaknesses; credentialed (authenticated, deeper, fewer false positives) vs. non-credentialed; intrusive vs. non-intrusive; agent-based vs. network.
- **Application security:** **static analysis (SAST)** reviews code at rest; **dynamic analysis (DAST)** tests running app; **package monitoring** (software composition analysis) watches third-party libraries/dependencies for known vulns (supply chain).
- **Threat feed:** curated data on emerging threats/IoCs.
  - **OSINT:** public sources (free).
  - **Proprietary/third-party:** paid commercial feeds.
  - **Information-sharing organization:** ISACs, CISA AIS, sector-specific sharing.
  - **Dark web:** monitoring criminal forums/markets for leaked credentials and chatter.
- **Penetration testing:** authorized active exploitation to prove exploitability; goes beyond scanning (exploits and chains).
- **Responsible disclosure program:** defined channel for researchers to report vulns privately. **Bug bounty:** pays rewards for valid findings.
- **System/process audit:** formal review of configuration and process against policy/standard.

#### Analysis
- **Confirmation:** validate findings before acting. **False positive:** scanner reports a vuln that does not exist. **False negative:** scanner misses a real vuln (worse, because nobody fixes it). True positive = real and reported. Reduce false positives with credentialed scans and updated plugins; confirm by manual check or a second tool.
- **Prioritization and severity:** **CVSS** scores severity (not risk).

| CVSS v3.x score | Severity |
|---|---|
| 0.0 | None |
| 0.1 – 3.9 | Low |
| 4.0 – 6.9 | Medium |
| 7.0 – 8.9 | High |
| 9.0 – 10.0 | Critical |

- **CVE:** standardized identifier for a publicly known vuln (CVE-YYYY-NNNN). NVD enriches with CVSS. **CWE** = weakness type. CVSS = how severe; CVE = what/which.
- **Vulnerability classification:** by type/category (e.g., misconfiguration, zero-day, injection, outdated software).
- **Exposure factor:** % of asset value lost if exploited (feeds SLE).
- **Environmental variables:** your specifics: internet-facing or not, compensating controls, data on system.
- **Industry/organizational impact:** regulated data, business criticality, reputational effect.
- **Risk tolerance/appetite:** how much residual risk leadership accepts; drives remediation priority and acceptance.
- Prioritize by: severity x exploitability (known exploit in the wild, EPSS) x asset criticality x exposure.

#### Vulnerability response and remediation
- **Patching:** primary fix; test in staging, schedule, deploy, verify.
- **Insurance:** risk transfer for residual risk (does not remove vuln).
- **Segmentation:** isolate vulnerable system when it cannot be patched.
- **Compensating controls:** alternative control reducing risk when primary fix unavailable (WAF, IPS virtual patch, extra monitoring).
- **Exceptions and exemptions:** formally documented, time-limited, risk-accepted, approved by owner/management.

#### Validation of remediation
- **Rescanning:** confirm vuln gone. **Audit:** verify process/config. **Verification:** manual confirmation that the fix works and nothing broke.

#### Reporting
Communicates findings: severity, affected assets, trends, remediation status, SLAs to technical staff and management. Tailored per audience (exec vs. engineers).

> **Exam tip:** Scanner says vulnerable but admin proves not = false positive. Scan "identifies", pen test "exploits". CVSS score 9.8 = Critical. "Cannot patch legacy system" -> segmentation / compensating control / documented exception.

---

### 4.4 Explain security alerting and monitoring concepts and tools

#### Monitoring computing resources
- **Systems, applications, infrastructure** all generate telemetry to monitor.

#### Activities
- **Log aggregation:** centralize logs from many sources into one place (SIEM) for correlation.
- **Alerting:** notification when events match rules/thresholds.
- **Scanning:** periodic vuln/compliance/discovery scanning.
- **Reporting:** dashboards and periodic summaries for ops and compliance.
- **Archiving:** retain logs long-term (compliance, forensics), integrity-protected, per retention policy.
- **Alert response and remediation/validation:**
  - **Quarantine:** isolate the host/file/user from the network.
  - **Alert tuning:** adjust thresholds/rules to cut false positives (alert fatigue) while not creating false negatives.

#### Tools
- **SCAP (Security Content Automation Protocol):** NIST standards (e.g., OVAL, XCCDF, CVE, CVSS) for automated compliance and vuln checking. **Benchmarks:** CIS/STIG configuration checklists used with SCAP.
- **Agents vs. agentless:** agent = software on endpoint, works off-network, richer data, deployment overhead. Agentless = remote scan/WMI/API, no install, less depth, needs network access/creds.
- **SIEM:** aggregates, normalizes, correlates logs, alerts, dashboards, retention. (SOAR then automates the response.)
- **Antivirus/anti-malware:** signature/heuristic/behavior detection on endpoint.
- **DLP:** detect/block sensitive data leaving (email, USB, cloud, print).
- **SNMP traps:** unsolicited alerts from managed devices to the NMS (UDP 162; polling uses 161). SNMPv3 adds auth+encryption.
- **NetFlow:** flow metadata (src/dst IP, ports, bytes, time), not payloads. Detects exfiltration, anomalies, top talkers. (sFlow, IPFIX similar.)
- **Vulnerability scanners:** Nessus, OpenVAS, Qualys.

> **Exam tip:** "Who talked to whom and how much, without content" -> NetFlow. "Device pushes alert to monitoring server" -> SNMP trap. "Correlate logs from many systems" -> SIEM. Too many false alarms -> tuning.

---

### 4.5 Given a scenario, modify enterprise capabilities to enhance security

#### Firewall
- **Rules / access lists:** ordered, top-down, first match wins, **implicit deny** at the end. Elements: source, destination, port, protocol, action (allow/deny). Put specific rules before general; deny-all last.
- **Ports/protocols:** match by service port; block unneeded ones.
- **Screened subnet (DMZ):** network segment between untrusted outside and internal, hosting public-facing servers; two firewalls or three-legged firewall.
- Types: stateless (packet filter), stateful (tracks sessions), NGFW (app-aware, IPS, TLS inspection), WAF (HTTP/S layer 7, protects web apps from SQLi/XSS).

Example ACL reading:
```
1 permit tcp any host 10.0.1.10 eq 443   # allow HTTPS to web server
2 permit tcp 10.0.2.0/24 any eq 22       # allow SSH from admin net
3 deny ip any any                        # implicit/explicit deny
```

#### IDS/IPS

| | IDS | IPS |
|---|---|---|
| Placement | Out of band (SPAN/TAP) | Inline |
| Action | Detect, alert | Detect and block |
| Failure effect | None on traffic | Fail-open or fail-closed can disrupt traffic |

- **Trends:** reviewing IDS/IPS alert data over time (top signatures, sources, targets, volume changes) to spot campaigns, tune rules and adjust defenses; most products show trend dashboards. Exam framing: "what is changing" vs a single alert.
- **Detection methods:** signature-based (known patterns; needs updates; misses zero-days), anomaly/behavior-based (baseline deviations; catches novel; more false positives), heuristic.
- **Signatures:** pattern definitions for known attacks; must be updated continuously (vendor feeds), tuned to the environment, and custom signatures can be written (Snort/Suricata rules). Out-of-date signatures = false negatives.
- Network (NIDS/NIPS) vs. host (HIDS/HIPS).

#### Web filter

| Item | Exam-framed definition |
|---|---|
| **Agent-based** | Filtering software on each endpoint; policy follows the device **off-network** (remote/roaming users) without backhauling traffic. Must be deployed and kept updated on every device. |
| **Centralized proxy** | All web traffic passes a forward proxy/secure web gateway on the network (or in the cloud); one place to enforce, cache and log. Only covers traffic that goes through it. |
| **URL scanning** | Inspects requested URLs (and often page content) against threat lists and policy before allowing the request. |
| **Content categorization** | URLs/sites grouped into categories (gambling, social media, malware, adult); policy allows/blocks per category instead of per site. |
| **Block rules** | Explicit allow/deny entries by URL, domain, category, file type or keyword; override categorization. |
| **Reputation** | Sites scored (trustworthy, suspicious, malicious; newly registered domains score low) from threat intel; block below a threshold. |

> **Exam tip:** "Filtering must work when laptops are at home without VPN" -> agent-based. "Single point to inspect all outbound web traffic" -> centralized proxy. "Block all gambling sites" -> content categorization.

#### Operating system security
- **Group Policy (Windows AD):** central enforcement of security settings (password policy, lockout, software restriction, AppLocker, firewall) on OUs/domains.
- **SELinux:** Security-Enhanced Linux, kernel-level **mandatory access control (MAC)** using security labels/contexts on subjects and objects; even root is constrained by policy. Modes: enforcing, permissive (log only), disabled. AppArmor is a path-based alternative.

> **Exam tip:** Windows domain-wide settings -> Group Policy (GPO). Linux least privilege via mandatory labels -> SELinux.

#### Implementation of secure protocols
- **Protocol selection:** choose the encrypted/authenticated protocol for the job (SSH not Telnet, SFTP/FTPS not FTP, LDAPS not LDAP, SNMPv3 not v1/v2c, HTTPS not HTTP) and disable the insecure one.
- **Port selection:** use the secure protocol's standard port and open only that port on firewalls; close the legacy port. Moving a service to a non-standard port is obscurity, not security.
- **Transport method:** how the data is protected in transit: TCP vs UDP as the service requires, and the encryption wrapper (TLS for an application, SSH tunnel, IPSec/VPN for everything between sites). Choose an encrypted transport whenever data crosses an untrusted network.

| Insecure | Port | Secure replacement | Port |
|---|---|---|---|
| Telnet | TCP 23 | SSH | TCP 22 |
| HTTP | TCP 80 | HTTPS (TLS) | TCP 443 |
| FTP | TCP 20/21 | SFTP (SSH) | TCP 22 |
| FTP | TCP 20/21 | FTPS (FTP over TLS; explicit on 21, implicit 989/990) | 21 / 990 |
| SMTP | TCP 25 | SMTP over TLS (SMTPS/submission) | 465 / 587 |
| POP3 | TCP 110 | POP3S | 995 |
| IMAP | TCP 143 | IMAPS | 993 |
| LDAP | TCP 389 | LDAPS | 636 |
| SNMP v1/v2 | UDP 161/162 | SNMPv3 | 161/162 |
| DNS | 53 | DNSSEC (integrity) / DoH 443 / DoT 853 | |
| TFTP | UDP 69 | SFTP/SCP | 22 |
| RDP | TCP 3389 | via VPN/RD Gateway | |
| Syslog | UDP 514 | Syslog over TLS | 6514 |
| NTP | UDP 123 | NTS | |
| SQL/others | | TLS-wrapped | |

Others to know: DHCP 67/68, Kerberos 88, SMB 445, RADIUS 1812/1813, TACACS+ 49, IPsec IKE UDP 500 (NAT-T 4500), NetBIOS 137-139.

> **Exam tip:** Secure version = same service wrapped in TLS/SSH. Port questions: "encrypted email retrieval" 993/995; "secure remote shell" 22; "directory over TLS" 636.

#### DNS filtering
Block resolution of malicious/unwanted domains at the resolver (threat-intel categories, newly registered domains). Works for any device using the resolver; stops C2 callbacks and phishing before connection. Complements DNSSEC (which provides authenticity of records, not filtering).

#### Email security
- **SPF (Sender Policy Framework):** DNS TXT record listing the servers authorized to send for a domain. Checks sending IP.
- **DKIM (DomainKeys Identified Mail):** sending server signs message headers/body with a private key; receivers verify via the public key in DNS. Proves integrity and domain origin.
- **DMARC:** DNS policy built on SPF and DKIM; requires alignment with the From domain; tells receivers what to do on failure (none / quarantine / reject) and sends reports back to the domain owner.
- **Gateway (email security gateway):** inline filter (spam, phishing, malware attachments, URL rewriting, DLP, sandboxing) before mail reaches the mailbox.

Fit together: SPF = "which IPs may send", DKIM = "message is signed and unaltered", DMARC = "policy + reporting when either fails to align".

> **Exam tip:** Spoofed sender domain -> SPF/DKIM/DMARC. "Policy: reject unauthenticated mail and receive reports" -> DMARC. "Digital signature on message headers" -> DKIM.

#### File integrity monitoring (FIM)
Baselines hashes of critical OS files, binaries, registry keys and configs, then alerts on unauthorized change (detects tampering, rootkits, web defacement, config drift). Examples: Tripwire, OSSEC/Wazuh, Windows SFC. Required by PCI DSS. Keyword: "detect changes to system files".

#### DLP
Classifies and inspects data in use (endpoint), in motion (network/email) and at rest (storage); blocks, quarantines, encrypts, or alerts. Keyword: "prevent SSNs/credit cards from leaving".

#### Network access control (NAC)
Checks device identity and posture (patch level, AV, config) before granting access (802.1X); non-compliant devices sent to a quarantine/remediation VLAN or denied. Posture agents: **persistent** (permanently installed), **dissolvable** (downloaded, runs once, removes itself), or **agentless** (checks via AD/remote query). Keyword: "check health of device before it joins the network" -> NAC.

#### Endpoint detection and response (EDR) / XDR
- **EDR:** continuous endpoint telemetry, behavioral detection, investigation, isolation and rollback/remediation.
- **XDR:** extends across endpoint, network, cloud, email, identity into one correlated detection and response platform.
- **MDR** = outsourced EDR/XDR service.

#### User behavior analytics (UBA/UEBA)
Uses machine learning to baseline normal user (and, in UEBA, entity: hosts, apps, service accounts) behavior and flags anomalies (impossible travel, unusual hours, abnormal data volumes, first-time access to a sensitive share); finds compromised accounts and insider threats that signatures miss. Often a SIEM/XDR feature.

---

### 4.6 Given a scenario, implement and maintain identity and access management

#### Provisioning / deprovisioning user accounts
Create accounts with correct least-privilege rights on hire/role change; **deprovision** (disable, then remove) immediately on termination. Orphaned and dormant accounts are findings. Automate via HR-driven workflows.

#### Permission assignments and implications
Grant by role/group, review regularly (access recertification), watch for privilege creep (accumulated rights after transfers) and separation of duties violations.

#### Identity proofing
Verify a person is who they claim before issuing credentials (documents, in-person, knowledge checks); precedes account creation. NIST 800-63 IALs.

#### Federation
Trust between separate organizations/IdPs so users authenticate once at home IdP and access partner resources (SAML/OIDC).

#### Single sign-on (SSO)
One authentication grants access to multiple systems.

| Protocol | Purpose | Format / notes |
|---|---|---|
| LDAP | Directory access/query (AD); authentication binds | TCP 389, LDAPS 636 |
| OAuth 2.0 | **Authorization** (delegated access via tokens; "allow app to access my photos") | Access tokens, JSON/REST |
| SAML | **Authentication + authorization** federation for web SSO, enterprise | XML assertions; IdP <-> SP |
| OpenID Connect (OIDC) | **Authentication** layer on top of OAuth 2.0 ("Sign in with Google") | JWT ID token |
| Kerberos | Ticket-based SSO in AD | UDP/TCP 88, timestamps (clock skew) |

> **Exam tip:** XML + enterprise federation -> SAML. "Authorize third-party app without sharing password" -> OAuth. "Social login/authentication" -> OIDC. OAuth is authorization, not authentication.

#### Interoperability
Standards-based integration so IAM systems work across vendors, platforms and cloud (SAML, SCIM for provisioning, OIDC).

#### Attestation
Periodic confirmation by managers/owners that users' access remains appropriate (access reviews); also hardware/software attestation proving a system state (e.g., TPM measured boot).

#### Access controls

| Model | Who decides | Basis | Keyword |
|---|---|---|---|
| MAC | System/policy (central authority) | Labels/clearance (Top Secret etc.) | Government/military, SELinux |
| DAC | Resource owner | ACLs set by owner | Owner grants access; file shares, most flexible/least secure |
| RBAC | Admin | Job role | "Role", job function; most common enterprise |
| Rule-based | System | Rules applied to all (firewall ACL, time rules) | Rules, not roles |
| ABAC | Policy engine | Attributes of user, resource, environment | Context-aware, dynamic, location/device/time |
| Time-of-day restrictions | System | Time | Login only business hours |
| Least privilege | | Minimum rights necessary | Always the default principle |

Note: RBAC = Role-based; rule-based is a different thing though abbreviations conflict.

#### Multifactor authentication (MFA)
- **Implementations:**
  - **Biometrics:** fingerprint, face, iris, retina, voice, vein. Errors: FAR (false acceptance, a security failure), FRR (false rejection, a usability problem); CER/EER = where they cross, lower is better.
  - **Hard authentication token:** physical device generating OTPs (key fob showing a TOTP/HOTP code) or smart card.
  - **Soft authentication token:** OTP generated by an app (Google/Microsoft Authenticator) or delivered by SMS/email/push. SMS is weakest (SIM swap, interception).
  - **Security keys:** USB/NFC/Bluetooth hardware keys (FIDO2/WebAuthn, U2F) doing public-key challenge/response; phishing-resistant.
  - TOTP = time-based (30-second codes); HOTP = counter/event-based (valid until used).
- **Factors (SY0-701 lists four):** something you **know** (password, PIN, pattern), something you **have** (token, smart card, phone), something you **are** (biometric), **somewhere you are** (location: GPS, IP geolocation). Older material adds something you **do** (gait, typing rhythm, signature); treat it as a behavioral attribute if it appears. Two passwords or password + security question is not MFA (same factor).

> **Exam tip:** Smart card + PIN = have + know (MFA). PIN + password = single factor. Push fatigue/MFA bombing = attack against push MFA; number matching mitigates.

#### Password concepts
- **Best practices (exam list):**
  - **Length:** the most important property; longer beats complex (passphrases).
  - **Complexity:** mixing upper/lower/digits/symbols to enlarge the keyspace.
  - **Reuse:** prohibit reuse across systems and of recent passwords (password **history**).
  - **Expiration:** maximum age; forces a change after N days.
  - **Age:** minimum age; stops a user changing the password repeatedly to cycle back to an old one through the history list.
  - Also: lockout after failed attempts, check against breached-password lists.

- **Password managers:** generate/store unique strong passwords; single master secret; reduces reuse.
- **Passwordless:** FIDO2/WebAuthn passkeys, certificates, biometrics bound to device, magic links; phishing-resistant.

> **Exam tip:** Current NIST SP 800-63B favors length, breached-password screening, and **no** forced periodic expiration or composition rules unless compromise is suspected. CompTIA questions may still offer complexity and expiration as "best practice" answers; pick the one that matches the question's wording. "User keeps resetting to reuse the old password" -> minimum password age.

#### Privileged access management (PAM)
- **Just-in-time (JIT) permissions:** elevate only when needed, expire automatically (no standing privilege).
- **Password vaulting:** privileged credentials stored in vault, checked out, rotated, session recorded.
- **Ephemeral credentials:** short-lived, auto-generated credentials (temporary accounts/tokens) created for one session or task and destroyed afterwards, so nothing persistent can be stolen.
- Also: session monitoring, approval workflows, break-glass accounts.

---

### 4.7 Explain the importance of automation and orchestration related to secure operations

**Automation** = a task runs without human action. **Orchestration** = coordinating many automated tasks/tools across systems into a workflow (SOAR playbooks).

#### Use cases of automation and scripting

| Use case | What is automated |
|---|---|
| **User provisioning** | Create/modify/disable accounts and group membership from HR events (joiner/mover/leaver); removes delay and orphaned accounts. |
| **Resource provisioning** | Spin up/tear down VMs, cloud resources and networks from templates (IaC); consistent and auditable. |
| **Guard rails** | Automated policy checks that block or auto-fix non-compliant actions (e.g., refuse a public storage bucket, require encryption). |
| **Security groups** | Automatically add/remove users or hosts from security/firewall groups based on role, tag or posture. |
| **Ticket creation** | Alerts or events open tickets automatically with context attached. |
| **Escalation** | Route an incident to the next tier or on-call staff automatically when severity/time thresholds are met. |
| **Enabling/disabling services and access** | Turn services, ports or accounts on/off by script (e.g., disable an account on detection of compromise). |
| **Continuous integration and testing** | Code changes automatically built and tested (unit, SAST/DAST, dependency scans) before merge/deploy. |
| **Integrations and APIs** | Tools exchange data and trigger actions through APIs (SIEM -> SOAR -> firewall/EDR). |

#### Benefits

| Benefit | Meaning |
|---|---|
| **Efficiency/time saving** | Repetitive tasks done in seconds, not hours. |
| **Enforcing baselines** | Every system configured the same way; drift auto-corrected. |
| **Standard infrastructure configurations** | Templates produce identical, known-good builds. |
| **Scaling in a secure manner** | Growth without proportional staff or loss of control. |
| **Employee retention** | Less tedious work reduces burnout and turnover. |
| **Reaction time** | Machine-speed response (isolate host, block IP) shortens attacker dwell time. |
| **Workforce multiplier** | Each analyst covers more; small team does the work of a larger one. |

#### Other considerations

| Consideration | Meaning |
|---|---|
| **Complexity** | Automation adds moving parts that must be designed, understood and debugged. |
| **Cost** | Tools, licenses, integration and development time. |
| **Single point of failure** | If the automation platform fails or is compromised, every dependent process fails with it. |
| **Technical debt** | Quick scripts that are never maintained or documented become fragile liabilities. |
| **Ongoing supportability** | Someone must maintain scripts as systems, APIs and staff change. |

> **Exam tip:** Benefits list answers "why automate". Risk list: bad automation can propagate errors at machine speed; compromised automation account = broad blast radius. Keep humans in the loop for high-impact actions.

---

### 4.8 Explain appropriate incident response activities

#### Process (SY0-701 order)
1. **Preparation:** IR plan, policy, team/roles, contact lists, tooling, playbooks, training, communication plan, jump bag.
2. **Detection:** identify potential incident via alerts, users, threat intel (IoCs).
3. **Analysis:** validate (true vs. false positive), scope, classify severity, determine impact, prioritize.
4. **Containment:** limit spread (isolate, segment, disable accounts); short-term vs. long-term; preserve evidence first.
5. **Eradication:** remove root cause (malware, persistence, attacker accounts, vulnerability).
6. **Recovery:** restore from clean backups, rebuild, validate, return to production, heightened monitoring.
7. **Lessons learned:** post-incident review, improve plan, controls and documentation.

> **Exam tip:** Order matters on the exam. Containment before eradication before recovery. "Isolate the infected host" = containment. "Reimage / remove malware" = eradication. "Restore services" = recovery. "After-action meeting" = lessons learned. Do not power off a compromised system (loses volatile evidence); isolate it.

#### Training
IR team members get role-specific training (tools, playbooks, evidence handling, communication); all staff get awareness training on recognizing and **reporting** incidents; managers/executives learn decision and notification responsibilities. Refresh regularly and after plan changes.

#### Testing
- **Tabletop exercise:** discussion-based walk-through of a scenario around a table; no systems touched; cheapest.
- **Simulation:** hands-on realistic exercise (e.g., simulated phishing, red/purple team, live drill) exercising actual tooling and procedures.
- Also: walkthrough, parallel/failover testing for continuity.

#### Root cause analysis (RCA)
Find the underlying cause (not just symptom) so recurrence is prevented (5 Whys, fishbone). Happens during/after the incident, feeds lessons learned.

#### Threat hunting
Proactive, hypothesis-driven search for threats already inside that evaded detection; uses threat intel, IoCs, TTPs, and anomalies. Assumes breach. Contrast: detection is reactive to alerts.

#### Digital forensics
- **Legal hold:** legal requirement to preserve potentially relevant data when litigation is anticipated; suspends deletion/retention schedules.
- **Chain of custody:** documented, unbroken record of who handled evidence, when, and where, from collection to court; proves integrity and admissibility. Use hashes (SHA-256) to prove no alteration.
- **Acquisition:** collect forensically sound copy (bit-for-bit image with a write blocker); work on copy, never original.
  - **Order of volatility** (most to least volatile):
    1. CPU registers/cache
    2. RAM (memory, routing/ARP tables, processes)
    3. Temporary files / swap / page file
    4. Disk
    5. Remote logging and monitoring data
    6. Physical configuration / network topology
    7. Archival media/backups
- **Reporting:** documents findings, methods, evidence, and conclusions; factual and reproducible; for management/legal.
- **Preservation:** protect evidence integrity (write blockers, secure storage, hashing, tamper-evident bags, limited access).
- **E-discovery:** identifying, collecting, and producing electronically stored information for legal proceedings.
- Also: timestamps/time offset, provenance, snapshots, forensic imaging of VMs, interviews.

> **Exam tip:** "First thing to collect" -> most volatile (memory). "Prove evidence was not altered" -> hash + chain of custody. "Litigation expected, stop deleting emails" -> legal hold.

---

### 4.9 Given a scenario, use data sources to support an investigation

#### Log data

| Log source | Question it answers |
|---|---|
| Firewall logs | What traffic was allowed/blocked? Which IPs/ports did a host contact? |
| Application logs | What did the app do? Errors, user actions, failed transactions |
| Endpoint logs | What happened on this host? Process starts, logons, changes |
| OS-specific security logs (Windows Security, Linux auth.log) | Who logged on/failed, privilege use, account changes |
| IPS/IDS logs | Which signature fired? What attack was detected/blocked? |
| Network logs (router, switch, flow) | What path/volume/protocols moved across the network? |
| Metadata (file, email headers, web, mobile) | Who created/sent/modified, when, from where, device/geo |

#### Data sources
- **Vulnerability scans:** what weaknesses existed on the affected system?
- **Automated reports:** summarized, scheduled results from tools.
- **Dashboards:** real-time visual status and trends.
- **Packet captures (pcap):** full content of traffic; what exactly was sent? (Wireshark, tcpdump); most detail, large storage.

> **Exam tip:** "Which user account logged in and when" -> authentication/OS security log. "Which hosts talked to the C2 IP" -> firewall/NetFlow/DNS logs. "Exact payload" -> packet capture. "Who sent the email and from which server" -> email header metadata. "What attack signature matched" -> IPS log. Sort out sequence with synchronized time (NTP).

---

### Most-tested distinctions

- **Site survey vs. heat map:** survey is the activity; heat map is its visual signal-strength output.
- **BYOD / COPE / CYOD / COBO:** employee-owned / company-owned + personal use / pick from a list / business only.
- **EAP-TLS vs. PEAP vs. EAP-FAST:** client+server certs / server cert only + inner password / PAC, no certs.
- **RADIUS vs. TACACS+:** UDP 1812/1813, password-only encryption vs. TCP 49, full encryption, separate AAA.
- **WPA3-SAE:** replaces PSK handshake, resists offline guessing; OWE encrypts open networks.
- **Sanitization vs. destruction vs. certification:** reuse-safe wipe / physical, unrecoverable / paper proof.
- **False positive vs. false negative:** reported but not real / real but missed. **Scan vs. pen test:** identify vs. exploit.
- **CVE vs. CVSS vs. CWE:** identifier / severity score (9.0-10.0 critical, 7.0-8.9 high, 4.0-6.9 medium, 0.1-3.9 low) / weakness class.
- **Unpatchable systems:** segmentation, compensating control, documented exception, insurance (transfer) — not "ignore".
- **SIEM vs. SOAR vs. SNMP trap vs. NetFlow:** correlate logs / automate response / device-pushed alert / flow metadata.
- **IDS vs. IPS:** passive detect (out-of-band) vs. inline block.
- **SPF vs. DKIM vs. DMARC:** authorized sender IPs / signed message / policy + alignment + reporting.
- **SAML vs. OAuth vs. OIDC vs. LDAP:** XML federation SSO / authorization delegation / authentication on OAuth / directory queries.
- **MAC vs. DAC vs. RBAC vs. rule-based vs. ABAC:** labels / owner / job role / fixed rules / attributes and context.
- **MFA requires different factors:** password + PIN is still one factor; 701 factors are know / have / are / somewhere you are.
- **JIT vs. vaulting vs. ephemeral credentials:** time-limited elevation / stored and rotated secrets / short-lived one-use credentials.
- **Automation vs. orchestration:** one task vs. coordinated workflow across tools.
- **IR order:** preparation -> detection -> analysis -> containment -> eradication -> recovery -> lessons learned. **Tabletop** (discussion) vs. **simulation** (hands-on drill).
- **Chain of custody vs. legal hold vs. e-discovery:** evidence handling record / preserve data for litigation / produce ESI to court.
- **Order of volatility:** registers/cache -> RAM -> swap/temp -> disk -> remote logs -> config -> archive media.

---

## Domain 5 — Security Program Management and Oversight (20%)

Objectives 5.1–5.6. Governance, risk, third parties, compliance, audits, awareness. Heavy on vocabulary and "which term fits this scenario" questions.

---

### 5.1 Summarize elements of effective security governance

#### Guidelines, policies, standards, procedures

| Document | Nature | Answers | Mandatory? | Example |
|---|---|---|---|---|
| **Policy** | High-level management statement of intent and direction | *Why / what* | Yes | "All data must be encrypted at rest" |
| **Standard** | Specific, measurable requirement that supports a policy | *What exactly* (specs) | Yes | "AES-256 for data at rest" |
| **Procedure** | Step-by-step instructions to perform a task | *How* | Yes | Steps to onboard a new user |
| **Guideline** | Recommended best practice, advisory | *Suggestion* | **No** | "Use a password manager" |

> **Exam tip:** Order of abstraction: policy (broadest) > standard > procedure (most detailed). Guideline = optional/recommendation; everything else is mandatory. "Step-by-step" = procedure. "Minimum technical requirement" = standard.

#### Policies (named in the objectives)

| Policy | Purpose |
|---|---|
| **Acceptable use policy (AUP)** | What users may/may not do with company systems, data, and networks; email, web, personal use, social media. Signed at onboarding. |
| **Information security policies** | Overarching program policy: roles, responsibilities, data classification, management commitment. Parent of the others. |
| **Business continuity (BCP)** | Keep critical business functions running during/after disruption. Broader than IT. |
| **Disaster recovery (DRP)** | Restore IT systems/data after a disaster. Subset of BC; technology-focused. |
| **Incident response (IR)** | Roles, phases, escalation, and communication for security incidents. |
| **Software development lifecycle (SDLC)** | Security requirements across design, coding, test, deploy, maintain; code review, SAST/DAST gates. |
| **Change management** | Formal approval, testing, scheduling, and rollback for changes to production. |

> **Exam tip:** BCP = business keeps operating; DRP = technology gets restored. AUP is what the *user* agrees to; it is not the same as an information security policy.

#### Standards

| Standard | What it specifies |
|---|---|
| **Password** | Length, complexity, history, age, lockout, MFA requirement, no reuse. |
| **Access control** | Model (RBAC/ABAC/MAC/DAC), least privilege, separation of duties, review cadence, provisioning rules. |
| **Physical security** | Badges, mantraps, cameras, visitor logs, locks, guard coverage. |
| **Encryption** | Approved algorithms, key lengths, protocols (TLS 1.2+), key management and rotation. |

#### Procedures

| Procedure | Notes |
|---|---|
| **Change management** | Request > impact/risk analysis > approval (CAB) > test > schedule > implement > backout plan > document/post-review. |
| **Onboarding** | Accounts provisioned by role, AUP signed, training, equipment issued, background check complete. |
| **Offboarding** | Disable accounts immediately, retrieve assets/badges, revoke access and tokens, exit interview, reassign data. |
| **Playbooks** | Prescribed step-by-step response for a specific scenario (ransomware, phishing). Often automated via SOAR. Distinct from a runbook (routine operational tasks). |

#### External considerations

| Factor | Examples / key point |
|---|---|
| **Regulatory** | Government-mandated; penalties for noncompliance (HIPAA, SOX, GLBA, FISMA, PCI DSS is contractual/industry). |
| **Legal** | Laws, contractual obligations, liability, e-discovery, breach notification. |
| **Industry** | Sector standards and frameworks (PCI DSS, ISO 27001, NIST CSF, CIS). |
| **Geographic: local / regional / national / global** | Local ordinances, state laws (CCPA), national (HIPAA), regional (GDPR - EU), global (ISO). **Data sovereignty** applies: data is subject to the laws of the country where it is stored. |

#### Monitoring and revision

- Review policies on a **schedule** and after **triggers**: new laws, incidents, audit findings, business changes, new technology.
- Monitor compliance with metrics/audits; track exceptions; version-control documents; communicate and re-acknowledge changes.

#### Types of governance structures

| Structure | Role |
|---|---|
| **Boards** | Ultimate accountability; set direction and risk oversight. |
| **Committees** | Specialized oversight (risk committee, audit committee, change advisory board, security steering). |
| **Government entities** | Regulators/legislatures whose rules the organization must follow (local, state, national). |
| **Centralized** | One central body makes decisions; consistent, efficient, slower to adapt locally. |
| **Decentralized** | Business units decide locally; flexible and fast, inconsistent and harder to audit. |

#### Roles and responsibilities for systems and data

| Role | Responsibility |
|---|---|
| **Owner** | Senior business person accountable for the data; sets classification and access rules. |
| **Controller** | Determines **why and how** personal data is processed (GDPR). |
| **Processor** | Processes personal data **on behalf of** the controller (e.g. cloud payroll vendor). |
| **Custodian / steward** | Day-to-day handling: implements controls, backups, access, quality. Custodian = technical protection; steward = quality/meaning/proper use of the data. |

> **Exam tip:** Owner = accountable and decides. Custodian = does the technical work. Controller decides purposes; processor follows instructions. The data owner classifies; the custodian applies the protections.

---

### 5.2 Explain elements of the risk management process

#### Risk identification

Find assets, threats, vulnerabilities, and existing controls. Sources: asset inventory, vulnerability scans, threat intel, audits, incidents, interviews.

#### Risk assessment

| Type | When |
|---|---|
| **Ad hoc** | Triggered by an event (new threat, incident, urgent project). |
| **Recurring** | On a schedule (annual, quarterly), often compliance-driven. |
| **One-time** | A single assessment for a specific project, acquisition, or system. |
| **Continuous** | Ongoing, automated monitoring; real-time risk posture. |

#### Risk analysis

| | Qualitative | Quantitative |
|---|---|---|
| Output | Ratings: high/medium/low, heat map, risk matrix | Dollar values and probabilities |
| Basis | Judgment, experience, Delphi technique | Asset value, historical data |
| Pros | Fast, cheap, no hard data needed | Objective, supports cost-benefit |
| Cons | Subjective | Needs good data; time-consuming |

**Terms**

| Term | Definition |
|---|---|
| **Likelihood** | Chance the threat exploits the vulnerability, usually expressed qualitatively (rare, possible, likely). |
| **Probability** | Likelihood expressed numerically (e.g., 0.25 or 25% per year); used in quantitative analysis. |
| **Impact** | Consequence if it happens (financial, operational, reputation, safety). |
| **Exposure factor (EF)** | Percentage of asset value lost in one incident. |
| **SLE** | Single loss expectancy = AV x EF. |
| **ARO** | Annualized rate of occurrence = expected incidents per year. |
| **ALE** | Annualized loss expectancy = SLE x ARO. |
| **Inherent risk** | Risk before controls. |
| **Residual risk** | Risk remaining after controls. |
| **Control risk** | Risk that a control fails to prevent/detect. |
| **Risk posture** | Overall risk state of the organization. |

**Worked example.** Server worth $200,000; a flood would destroy 40% (EF = 0.4); floods occur once every 10 years (ARO = 0.1).
- SLE = 200,000 x 0.4 = **$80,000**
- ALE = 80,000 x 0.1 = **$8,000/year**
- A flood-protection control costing $5,000/year that eliminates the risk is justified (saves $3,000/year). One costing $12,000/year is not.
- If the control cuts ARO from 0.1 to 0.02: new ALE = $1,600; savings = $6,400; subtract annual control cost to get net benefit.

> **Exam tip:** Never spend more on a control than the ALE it prevents. "Once every 5 years" means ARO = 0.2. "Twice a year" means ARO = 2.

#### Risk register

Living document listing identified risks with: description, owner, likelihood, impact, score, mitigation plan, status, residual risk.

| Element | Meaning |
|---|---|
| **Key risk indicators (KRIs)** | Metrics that signal rising risk exposure (e.g. unpatched critical vulns count, failed logins). Leading indicators. |
| **Risk owner** | Person accountable for managing a specific risk. |
| **Risk threshold** | Level at which a risk requires action/escalation; trigger point for KRIs. |

#### Risk tolerance vs risk appetite

| Term | Definition |
|---|---|
| **Risk appetite** | Amount/type of risk the organization is *willing to pursue* to meet objectives (strategic, broad). |
| **Risk tolerance** | Acceptable *deviation* around the appetite for a specific risk (operational, measurable limit). |

Appetite postures:
- **Expansionary**: willing to take on more risk for growth/returns.
- **Conservative**: minimize risk; prefers stability.
- **Neutral**: balanced; takes risk when reward justifies it.

> **Exam tip:** Appetite = how much risk we want to take (strategy). Tolerance = how far from that we can stray (limit). A startup chasing market share = expansionary; a bank or hospital = conservative.

#### Risk management strategies

| Strategy | What it means | Example |
|---|---|---|
| **Transfer** | Shift financial impact to a third party | Cyber insurance, outsourcing, contract indemnity |
| **Accept** | Acknowledge and live with the risk | Cost of control exceeds loss |
| - **Exemption** | Formal, documented waiver from a policy/requirement (usually longer term, approved) | Legacy system exempted from patch policy |
| - **Exception** | Approved temporary deviation with compensating controls and an expiry | One-off deviation for a project |
| **Avoid** | Stop the activity that creates the risk | Discontinue a product, don't enter a market |
| **Mitigate** | Reduce likelihood or impact with controls | Patch, segment, MFA |

Remaining risk after mitigation is **residual risk**; it must be accepted by the risk owner.

> **Exam tip:** Exemption vs exception is loosely defined; the exam framing is exemption = released from the requirement altogether, exception = a specific, time-boxed deviation with compensating controls. Both are forms of **acceptance** and need documented approval.

> **Exam tip:** "Buy insurance" = transfer (the risk is not eliminated, only the cost moves). "Stop doing it" = avoid. "Documented approval to not follow policy" = exception/exemption under accept. Risk can never be *ignored* or *rejected*.

#### Risk reporting

Communicate risk posture to stakeholders: executive dashboards, heat maps, risk register extracts, KRI trends, status of mitigation. Tailor detail to the audience (board = summary, ops = detail).

#### Business impact analysis (BIA)

Identifies critical functions and quantifies the effect of their loss; drives recovery priorities.

| Term | Definition |
|---|---|
| **RTO** (recovery time objective) | Maximum acceptable time to restore a service after disruption. |
| **RPO** (recovery point objective) | Maximum acceptable data loss, measured in time since last good backup. |
| **MTTR** (mean time to repair/recover) | Average time to repair a failed component and restore service. |
| **MTBF** (mean time between failures) | Average operating time between failures; reliability. |
| **MTD / MAO** | Maximum tolerable downtime; the absolute limit before the business suffers unacceptable harm. RTO must be < MTD. |

**Worked example.** Order system: RPO 1 hour, RTO 4 hours. The business can lose at most 1 hour of orders, so backups/replication must occur at least hourly. Service must be back within 4 hours of the outage. A nightly backup fails the RPO. Availability from MTBF/MTTR: MTBF 1,000 h, MTTR 10 h gives availability = 1000 / (1000 + 10) = about 99.0%.

> **Exam tip:** RTO = "how long can we be down"; RPO = "how much data can we lose" (look at backup frequency). MTBF = reliability (bigger is better); MTTR = repairability (smaller is better).

---

### 5.3 Explain the processes associated with third-party risk assessment and management

#### Vendor assessment

| Method | Description |
|---|---|
| **Penetration testing** | Authorized testing of the vendor's systems (or of your integration with them), only with permission and defined scope. |
| **Right-to-audit clause** | Contract clause letting the customer (or its auditor) inspect the vendor's controls, records, and facilities. |
| **Evidence of internal audits** | Vendor shares its own audit reports and remediation evidence. |
| **Independent assessments** | Third-party audits/attestations (SOC 2 Type II, ISO 27001 certification) - more credible than self-reporting. |
| **Supply chain analysis** | Evaluate the vendor's own suppliers and dependencies (fourth parties); software provenance, SBOM, hardware origin. |

#### Vendor selection

- **Due diligence**: investigate the vendor *before* contracting (financial health, security posture, references, certifications, breach history).
- **Conflict of interest**: relationship that could bias selection (family ties, financial stake, gifts). Disclose and recuse.

#### Agreement types

| Agreement | What it is | Use when |
|---|---|---|
| **SLA** (service-level agreement) | Measurable service levels (uptime, response time) with penalties/credits | Defining and enforcing performance of a service |
| **MOA** (memorandum of agreement) | Binding agreement on what each party will do; more formal than MOU | Parties commit to specific obligations without full contract |
| **MOU** (memorandum of understanding) | Non-binding statement of intent and shared goals | Early/informal cooperation; shows intent, not legal commitment |
| **MSA** (master service agreement) | Umbrella contract with general terms for repeat business | Ongoing relationship with multiple projects; avoids renegotiating terms |
| **WO / SOW** (work order / statement of work) | Defines specific project: scope, deliverables, timeline, cost | Each individual engagement under an MSA |
| **NDA** (non-disclosure agreement) | Legally binds parties to keep information confidential | Sharing sensitive information before/during relationship |
| **BPA** (business partners agreement) | Defines partnership terms: profit/loss share, responsibilities, decision-making, exit | Two or more businesses operating jointly |

> **Exam tip:** MOU = non-binding intent; MOA = binding commitment (CompTIA framing: MOA is more formal and defines each party's responsibilities; in the real world whether an MOA is legally enforceable depends on its wording). SLA = performance metrics. MSA = the framework; SOW/WO = the specific job under it. NDA = confidentiality. BPA = business partnership.

#### Vendor monitoring

Continuous, not one-time: review SLA metrics, audit reports, security ratings, incident notifications, financial health, and re-assess on contract renewal or after changes. Includes **questionnaires** and **rules of engagement**.

#### Questionnaires

Standardized security questionnaires (SIG, CAIQ, custom) the vendor completes about its controls; first-pass screening; self-reported so verify with evidence.

#### Rules of engagement

Defines what is allowed in testing/assessment of the vendor: scope, targets, timing, methods, excluded systems, contacts, and escalation. Prevents unintended damage and legal exposure.

#### Vendor risk terms

| Term | Meaning |
|---|---|
| **Third party** | Vendor/supplier directly contracted. |
| **Fourth party** | The vendor's own suppliers. |
| **Offboarding** | End of the relationship: revoke access, retrieve/destroy data, confirm per contract. |

---

### 5.4 Summarize elements of effective security compliance

#### Compliance reporting

| Type | Audience / purpose |
|---|---|
| **Internal** | Management, board, audit committee: status of controls, exceptions, remediation. |
| **External** | Regulators, auditors, customers, partners: required filings, attestations, certifications. |

#### Consequences of non-compliance

| Consequence | Notes |
|---|---|
| **Fines** | Monetary penalties (GDPR up to 4% of global annual turnover or EUR 20M). |
| **Sanctions** | Regulatory restrictions or formal penalties; can include trade restrictions. |
| **Reputational damage** | Loss of customer trust, negative press. |
| **Loss of license** | Cannot operate in regulated sector. |
| **Contractual impacts** | Lost contracts, terminated partnerships, penalties (e.g. loss of ability to process cards under PCI DSS). |

#### Compliance monitoring

| Element | Definition |
|---|---|
| **Due diligence** | Investigating/understanding risk *before* acting (research, vetting). |
| **Due care** | Acting responsibly on an ongoing basis; doing what a reasonable person would to protect assets (applying controls, patching). |
| **Attestation** | Formal statement (by management or auditor) that controls are in place and operating. |
| **Acknowledgement** | Individual confirms they read and understood a policy (AUP signing). |
| **Internal vs external** | Internal monitoring by compliance team/IA; external by regulators and independent auditors. |
| **Automation** | Continuous control monitoring, policy-as-code, automated evidence collection, and dashboards reduce manual effort and drift. |

> **Exam tip:** Due *diligence* = before/investigate. Due *care* = after/ongoing maintenance. Failing to apply due care is negligence.

#### Privacy

| Concept | Key point |
|---|---|
| **Legal implications - local/regional** | State/provincial laws (CCPA/CPRA, other US state laws). |
| **National** | Country-level (HIPAA, GLBA, COPPA, PIPEDA). |
| **Global** | GDPR applies to any organization handling EU residents' data regardless of location. Cross-border transfer rules; data sovereignty. |
| **Data subject** | The individual the personal data is about; holds rights (access, correction, deletion, portability, objection). |
| **Controller vs processor** | Controller decides purpose/means; processor processes on controller's behalf. Controller remains accountable. |
| **Ownership** | Data owner is accountable for the data; the data subject retains privacy rights regardless. |
| **Data inventory and retention** | Know what personal data you hold, where, why, and for how long; delete when retention ends. Data minimization. |
| **Right to be forgotten** | Data subject may request erasure (GDPR Art. 17) when data is no longer needed or consent withdrawn; limited by legal retention duties. |

> **Exam tip:** "EU residents' data" = GDPR. "Health data, US" = HIPAA. "Children under 13" = COPPA. "California consumers" = CCPA. "Erasure request" = right to be forgotten.

---

### 5.5 Explain types and purposes of audits and assessments

#### Attestation

An independent party's (or management's) formal opinion that a control or statement is accurate and effective (e.g. SOC 2 report, signed compliance statement).

#### Internal

| Type | Purpose |
|---|---|
| **Compliance** | Verify adherence to laws, regulations, policies, contracts. |
| **Audit committee** | Board-level body overseeing financial reporting, internal audit, and controls; independent of management. |
| **Self-assessments** | Teams evaluate their own controls (checklists, questionnaires); cheap and frequent but least objective. |

#### External

| Type | Purpose |
|---|---|
| **Regulatory** | Required by law/regulators; findings may carry penalties. |
| **Examinations** | Formal regulator review (bank examiners). |
| **Assessment** | Evaluation against a framework or standard (maturity, gap analysis). |
| **Independent third-party audit** | Unbiased outside auditor for certification or customer assurance (SOC 2, ISO 27001, PCI QSA). |

> **Exam tip:** Independence and objectivity increase self-assessment < internal audit < external independent audit. "Provides assurance to customers" = independent third-party audit/attestation.

#### Penetration testing

| Type | Meaning |
|---|---|
| **Physical** | Attempt to breach buildings, locks, badges, tailgating, dumpster diving. |
| **Offensive** | Red team: simulates attacker to breach defenses. |
| **Defensive** | Blue team: detection and response to attack. |
| **Integrated** | Red and blue (purple team) collaborate in real time to improve detection and controls. |

**Environment knowledge**

| Test | Tester knowledge | Simulates |
|---|---|---|
| **Known environment** (white box) | Full information: source, diagrams, credentials | Insider / most thorough |
| **Partially known** (gray box) | Some information: limited credentials, network info | Compromised user / partial insider |
| **Unknown environment** (black box) | None | External attacker |

**Reconnaissance**

| Type | Definition | Examples |
|---|---|---|
| **Passive** | No direct interaction with target; leaves no trace | OSINT, WHOIS, social media, DNS records, Shodan |
| **Active** | Direct interaction with target systems; detectable | Port scans, banner grabbing, ping sweeps |

> **Exam tip:** Written permission and rules of engagement come before any penetration test. "No prior knowledge" = unknown environment/black box. "Red + blue working together" = integrated/purple. Passive recon never touches the target's systems.

---

### 5.6 Given a scenario, implement security awareness practices

#### Phishing

- **Campaigns**: simulated phishing emails sent to staff to measure susceptibility (click rate, credential-submission rate, report rate); followed by targeted training.
- **Recognition**: suspicious sender/domain, urgency, mismatched URLs, unexpected attachments, requests for credentials or payment, generic greeting, grammar errors.
- **Response**: do not click or reply; report using the report-phishing button or to the security team; if clicked, disconnect and report immediately; change credentials.

#### Anomalous behavior recognition

| Category | Meaning | Example |
|---|---|---|
| **Risky** | Behavior that increases exposure | Using unsanctioned apps (shadow IT), reusing passwords, plugging in unknown USB |
| **Unexpected** | Out-of-pattern activity | Login at 3 a.m. from another country, large data download |
| **Unintentional** | Mistakes without malicious intent | Misdirected email, misconfigured sharing, lost device |

#### User guidance and training topics

| Topic | What users are taught |
|---|---|
| **Policy/handbooks** | Know and acknowledge the AUP, data handling/classification rules, and where to find policies. |
| **Situational awareness** | Notice surroundings: shoulder surfing, tailgating/piggybacking, strangers in secure areas, clean desk, screen locks. |
| **Insider threat** | Recognize and report warning signs (unusual access, data hoarding, policy circumvention) through a confidential channel. |
| **Password management** | Long unique passphrases, password manager, MFA, never share or reuse credentials. |
| **Removable media and cables** | Do not plug in found USB drives or unknown charging cables (malicious cables/"juice jacking" can deliver keystroke-injection payloads); use only approved, encrypted media. |
| **Social engineering** | Recognize pretexting, phishing/vishing/smishing, impersonation, urgency and authority tactics; verify out of band. |
| **Operational security (OPSEC)** | Avoid leaking sensitive details (projects, travel, org charts) in conversation or on social media that attackers can use for reconnaissance. |
| **Hybrid/remote work environments** | Secure home Wi-Fi, use VPN, avoid public Wi-Fi without VPN, lock screens, keep family off work devices, physical privacy for calls. |

#### Reporting and monitoring

| Phase | Meaning |
|---|---|
| **Initial** | Baseline measurement: pre-training results, first campaign, first assessment. |
| **Recurring** | Repeated measurement over time (quarterly campaigns, annual training) to show trends. |

Metrics: completion rates, phishing click/report rates, incident counts, time to report.

#### Development and execution

- **Development**: build a program tailored to roles (executives, developers, admins, general users); content updated for current threats; gamification, posters, newsletters, videos.
- **Execution**: new-hire training at onboarding, annual refreshers, role-based training, simulated attacks, LMS tracking, management support, and consequences for repeated failures.

> **Exam tip:** Awareness = everyone, general; training = role-specific skills; education = deeper knowledge. A user who clicks a simulated phish should get immediate feedback and targeted remedial training, not punishment.

---

### Most-tested distinctions

- **Policy vs standard vs procedure vs guideline**: policy = management intent; standard = measurable requirement; procedure = step-by-step; guideline = optional advice.
- **BCP vs DRP**: BCP keeps the business running; DRP restores IT.
- **Owner vs custodian vs steward**: owner is accountable and classifies; custodian implements protections; steward ensures data quality and proper use.
- **Controller vs processor**: controller decides purpose and means; processor acts on its behalf.
- **Qualitative vs quantitative**: ratings and heat maps vs dollar figures (SLE, ALE).
- **SLE = AV x EF; ALE = SLE x ARO**. Control cost must not exceed ALE reduction.
- **Inherent vs residual risk**: before controls vs after controls.
- **Risk appetite vs tolerance**: strategic willingness vs acceptable deviation. Expansionary, conservative, neutral.
- **Transfer vs avoid vs mitigate vs accept**: insurance; stop the activity; apply controls; live with it (with exception/exemption).
- **RTO vs RPO**: time to restore vs data-loss window. **MTBF** = reliability; **MTTR** = repair time.
- **MOU vs MOA**: non-binding intent vs binding commitment. **MSA vs SOW**: umbrella vs specific project.
- **SLA vs NDA vs BPA**: performance; confidentiality; business partnership.
- **Due diligence vs due care**: before/investigate vs ongoing/maintain.
- **Attestation vs acknowledgement**: formal statement about controls vs a user confirming they read a policy.
- **Self-assessment vs internal audit vs external audit**: increasing independence; external third-party gives customer assurance.
- **Known vs partially known vs unknown environment**: white vs gray vs black box.
- **Offensive vs defensive vs integrated testing**: red; blue; purple.
- **Passive vs active recon**: OSINT with no target contact vs scanning that touches the target.
- **Right-to-audit clause**: contractual permission to inspect a vendor. **Rules of engagement**: bounds for a test.
- **Risky vs unexpected vs unintentional behavior**: increases exposure; out of pattern; accidental.

---

## Ports and Protocols

> **Exam tip:** The exam tests "replace the insecure protocol with its secure equivalent" and "which port is this". Know the pairs cold.

### Main table

| Service | Insecure protocol / port | Secure replacement / port | Notes |
|---|---|---|---|
| File transfer | FTP TCP 20 (data), 21 (control) | **FTPS** TCP 989/990 (implicit: data/control) or 21 + AUTH TLS (explicit); **SFTP** TCP 22 | SFTP = SSH File Transfer, not FTP over SSL. FTPS = FTP + TLS. Both encrypt credentials |
| Simple file transfer | TFTP UDP 69 | None (use SFTP) | No authentication, used for PXE/network device configs |
| Remote shell | Telnet TCP 23 | **SSH** TCP 22 | SSH also does SCP, SFTP, port forwarding/tunneling |
| Web | HTTP TCP 80 | **HTTPS** TCP 443 (TLS) | HTTP/3 uses QUIC over UDP 443 |
| Mail relay (server to server) | SMTP TCP 25 | SMTPS TCP 465 (implicit TLS); STARTTLS on 25 | Port 25 is server-to-server |
| Mail submission (client to server) | SMTP 25 | **Submission TCP 587** (STARTTLS) | Authenticated client submission |
| Mail retrieval | POP3 TCP 110 | **POP3S** TCP 995 | Downloads mail, usually deletes from server |
| Mail retrieval | IMAP TCP 143 | **IMAPS** TCP 993 | Keeps mail on server, syncs folders |
| Name resolution | DNS UDP/TCP 53 | **DNSSEC** (still 53; adds signatures, integrity not confidentiality); **DoT** TCP 853; **DoH** TCP 443 | Zone transfers use TCP 53. DoT/DoH encrypt queries |
| Network management | SNMPv1/v2c UDP 161 (queries), 162 (traps) | **SNMPv3** UDP 161/162 | v3 adds auth + encryption. v1/v2c use cleartext community strings |
| Directory | LDAP TCP/UDP 389 | **LDAPS** TCP 636 (also StartTLS on 389) | Global Catalog: 3268 / 3269 (TLS) |
| Time | NTP UDP 123 | **NTS** (Network Time Security, NTP over TLS-based key exchange, TCP 4460 for NTS-KE) | NTP is amplification-attack prone |
| Remote desktop | RDP TCP/UDP 3389 | Same port; use NLA, TLS, gateway/VPN | Never expose directly to the internet |
| File sharing | SMB TCP 445 (legacy NetBIOS 139) | SMB 3.x with encryption (same port) | SMBv1 deprecated (EternalBlue) |
| NetBIOS | UDP 137 (name), UDP 138 (datagram), TCP 139 (session) | Replace with SMB over 445 | Legacy Windows name/file services |
| Authentication | Kerberos TCP/UDP 88 | n/a | Ticket-based, time-sensitive (5 min skew), AD default |
| AAA (network access) | RADIUS UDP **1812** (auth), **1813** (accounting); legacy 1645/1646 | RADIUS over TLS (RadSec) TCP 2083 | Only encrypts the password field. UDP |
| AAA (device admin) | **TACACS+** TCP 49 | n/a | Cisco, encrypts the entire payload, separates authN/authZ/accounting |
| Logging | Syslog UDP 514 | **Syslog over TLS** TCP **6514** | Syslog UDP is unreliable and unencrypted |
| VPN (IPSec) | IKE/ISAKMP UDP **500**; NAT-T UDP **4500** | ESP (protocol 50), AH (protocol 51) | Not TCP/UDP ports for ESP/AH |
| VPN (SSL/TLS) | OpenVPN UDP/TCP **1194** | n/a | TLS-based VPN; L2TP UDP 1701; PPTP TCP 1723 (deprecated) |
| DHCP | UDP 67 (server), 68 (client) | DHCP snooping on switches | Rogue DHCP risk |
| VoIP signalling | SIP UDP/TCP 5060 | **SIP TLS** 5061 (SIPS); SRTP for media | SRTP secures the media |
| SQL Server | TCP 1433 | Same, with TLS | |
| MySQL / MariaDB | TCP 3306 | Same, with TLS | |
| PostgreSQL | TCP 5432 | Same, with TLS | |
| Oracle | TCP 1521 | Same (Oracle Net with encryption) | |

### Quick memorization list (by number)

20/21 FTP, 22 SSH/SCP/SFTP, 23 Telnet, 25 SMTP, 49 TACACS+, 53 DNS, 67/68 DHCP, 69 TFTP, 80 HTTP, 88 Kerberos, 110 POP3, 123 NTP, 137-139 NetBIOS, 143 IMAP, 161/162 SNMP, 389 LDAP, 443 HTTPS, 445 SMB, 465 SMTPS, 500 IKE, 514 syslog, 587 SMTP submission, 636 LDAPS, 853 DoT, 989/990 FTPS, 993 IMAPS, 995 POP3S, 1194 OpenVPN, 1433 SQL Server, 1521 Oracle, 1645/1646 legacy RADIUS, 1812/1813 RADIUS, 3306 MySQL, 3389 RDP, 4500 IPSec NAT-T, 5060/5061 SIP, 5432 PostgreSQL, 6514 syslog TLS.

> **Exam tip:** Port ranges: well-known 0-1023, registered 1024-49151, dynamic/ephemeral 49152-65535. TCP = connection-oriented/reliable; UDP = connectionless (DNS queries, DHCP, TFTP, SNMP, syslog, NTP, RADIUS, IKE).

### TLS versions

| Version | Status | Notes |
|---|---|---|
| SSL 2.0 / 3.0 | Deprecated, broken | POODLE (SSL 3.0), downgrade attacks |
| TLS 1.0 / 1.1 | Deprecated | BEAST, weak ciphers; disable |
| **TLS 1.2** | Acceptable | Needs strong cipher suites (AEAD, ECDHE) |
| **TLS 1.3** | Preferred | Faster handshake, removes legacy ciphers, forward secrecy mandatory, encrypts more of the handshake |

- Certificates (X.509) bind identity to public key; the session key is symmetric, agreed via (EC)DHE.
- **Perfect forward secrecy (PFS):** ephemeral keys per session; compromise of the long-term private key does not expose past sessions.
- **HSTS** forces HTTPS; **certificate pinning** limits trusted CAs; **STARTTLS** upgrades a plaintext connection to TLS in place.

### IPSec

| Concept | Meaning |
|---|---|
| **AH** (Authentication Header, protocol 51) | Integrity + authentication + anti-replay. **No encryption.** Breaks with NAT |
| **ESP** (Encapsulating Security Payload, protocol 50) | Encryption + integrity + authentication. The common choice |
| **Transport mode** | Only the payload is protected; original IP header kept. Host-to-host |
| **Tunnel mode** | Entire original packet encapsulated with a new IP header. Site-to-site and remote access VPNs (gateway-to-gateway) |
| **IKE** (UDP 500) | Negotiates Security Associations (SAs); Phase 1 builds the ISAKMP SA, Phase 2 builds the IPSec SAs |
| **NAT-T** (UDP 4500) | Encapsulates ESP in UDP to cross NAT |

> **Exam tip:** "Needs confidentiality" -> ESP. "Integrity only" -> AH. "Site-to-site" -> tunnel mode. "Host-to-host, payload only" -> transport mode.

### Wireless security

| Standard | Encryption / auth | Status |
|---|---|---|
| **WEP** | RC4, 24-bit IV | Broken; never use |
| **WPA** | TKIP (RC4-based) | Deprecated |
| **WPA2** | **AES-CCMP**; PSK or Enterprise (802.1X) | Still common; vulnerable to offline PSK cracking via captured 4-way handshake, KRACK |
| **WPA3** | AES (CCMP-128 in Personal; GCMP-256 in Enterprise 192-bit mode); **SAE** replaces PSK | Current; resists offline dictionary attacks, forward secrecy, mandatory PMF |

| Concept | Meaning |
|---|---|
| **PSK / Personal** | Shared passphrase for all users; no per-user identity |
| **Enterprise (802.1X)** | Per-user/device auth via RADIUS + EAP; supplicant (client), authenticator (AP/switch), authentication server (RADIUS) |
| **SAE** | Simultaneous Authentication of Equals; Dragonfly handshake used in WPA3-Personal |
| **WPS** | Push-button/PIN setup; PIN is brute-forceable; disable |
| **Open + OWE** | Opportunistic Wireless Encryption (Enhanced Open) gives encryption for open networks |
| **Evil twin / rogue AP** | Impersonating or unauthorized AP; mitigate with 802.1X and WIDS |
| **Captive portal** | Web-based guest authentication |

### EAP methods (802.1X)

| Method | Client cert? | Server cert? | Notes |
|---|---|---|---|
| **EAP-TLS** | Yes | Yes | Mutual certificate auth; strongest; needs PKI |
| **PEAP** | No | Yes | TLS tunnel then inner auth (MSCHAPv2); username/password |
| **EAP-TTLS** | No | Yes | Tunnelled TLS; supports more inner methods |
| **EAP-FAST** | No (PAC) | Optional | Cisco; uses Protected Access Credential |
| **EAP-MD5** | No | No | Weak; no mutual auth |
| **LEAP** | No | No | Cisco legacy; broken |

### Email authentication

| Mechanism | What it does | How |
|---|---|---|
| **SPF** | Lists which mail servers may send for a domain | DNS TXT record; checks the envelope sender (Return-Path) against sending IP |
| **DKIM** | Message integrity and domain authenticity | Sender signs headers/body with a private key; public key in DNS TXT; signature in header |
| **DMARC** | Policy + reporting that ties SPF/DKIM to the visible From domain | DNS TXT at `_dmarc`; policy `none` / `quarantine` / `reject`; aggregate (rua) and forensic (ruf) reports |
| **S/MIME / PGP** | End-to-end message signing and encryption | Certificates (S/MIME) or web of trust (PGP) |

> **Exam tip:** WPA2 -> CCMP; WPA3 -> exam materials usually say GCMP. If a question pairs WPA3 with GCMP, accept it; WPA3-Personal actually still uses CCMP-128.

> **Exam tip:** SPF = which servers, DKIM = signed and unmodified, DMARC = what to do on failure and report back. All three combat spoofing/phishing; none encrypt message content.

---

## Acronyms

SY0-701 acronym list: acronym, expansion, one-line meaning. Where an acronym has two meanings, both are noted.

Jump: [A](#a) [B](#b) [C](#c) [D](#d) [E](#e) [F](#f) [G](#g) [H](#h) [I](#i) [J](#j) [K](#k) [L](#l) [M](#m) [N](#n) [O](#o) [P](#p) [Q](#q) [R](#r) [S](#s) [T](#t) [U](#u) [V](#v) [W](#w) [X](#x) [Z](#z)

### A

| Acronym | Expansion | Meaning |
|---|---|---|
| AAA | Authentication, Authorization, and Accounting | Framework for verifying identity, granting access, and logging activity |
| ACL | Access Control List | Rules permitting or denying access to resources or traffic |
| AES | Advanced Encryption Standard | Symmetric block cipher, 128/192/256-bit keys |
| AES-256 | Advanced Encryption Standard 256-bit | AES with a 256-bit key |
| AH | Authentication Header | IPSec protocol for integrity/authentication without encryption |
| AI | Artificial Intelligence | Machine-based systems that simulate intelligent behaviour |
| AIS | Automated Indicator Sharing | CISA service for exchanging threat indicators |
| ALE | Annualized Loss Expectancy | SLE x ARO |
| AP | Access Point | Device that connects wireless clients to a network |
| API | Application Programming Interface | Defined way for software components to communicate |
| APT | Advanced Persistent Threat | Well-resourced, long-term, stealthy attacker |
| ARO | Annualized Rate of Occurrence | Expected number of incidents per year |
| ARP | Address Resolution Protocol | Maps IP addresses to MAC addresses |
| ASLR | Address Space Layout Randomization | Randomizes memory addresses to hinder exploits |
| ATT&CK | Adversarial Tactics, Techniques, and Common Knowledge | MITRE knowledge base of attacker behaviour |
| AUP | Acceptable Use Policy | Defines permitted use of organization resources |
| AV | Antivirus (also Asset Value) | Software that detects and removes malware; in risk math, AV = asset value (SLE = AV x EF) |

### B

| Acronym | Expansion | Meaning |
|---|---|---|
| BASH | Bourne Again Shell | Common Unix/Linux command shell |
| BCP | Business Continuity Planning | Keeping critical functions running during disruption |
| BGP | Border Gateway Protocol | Inter-domain internet routing protocol |
| BIA | Business Impact Analysis | Identifies critical functions and the impact of their loss |
| BIOS | Basic Input/Output System | Legacy firmware that initializes hardware at boot |
| BPA | Business Partners Agreement | Agreement defining partner roles, profit and responsibilities |
| BPDU | Bridge Protocol Data Unit | Spanning Tree message between switches |
| BSSID | Basic Service Set Identifier | MAC address of a wireless access point |
| BYOD | Bring Your Own Device | Personal devices used for work |

### C

| Acronym | Expansion | Meaning |
|---|---|---|
| C2 | Command and Control | Attacker infrastructure that directs compromised hosts |
| CA | Certificate Authority | Issues and signs digital certificates |
| CAC | Common Access Card | US DoD smart card for physical and logical access |
| CAPTCHA | Completely Automated Public Turing Test to Tell Computers and Humans Apart | Challenge to block bots |
| CAR | Corrective Action Report | Documents remediation of a finding |
| CASB | Cloud Access Security Broker | Enforces security policy between users and cloud services |
| CBC | Cipher Block Chaining | Block cipher mode chaining each block to the previous one |
| CBT | Computer-Based Training | Security awareness delivered by computer |
| CCMP | Counter Mode/CBC-MAC Protocol | AES-based WPA2 encryption protocol |
| CCPA | California Consumer Privacy Act | California state privacy law for consumer data |
| CCTV | Closed-Circuit Television | Video surveillance |
| CER | Crossover Error Rate | Point where biometric FAR equals FRR; lower is better (also EER) |
| CERT | Computer Emergency Response Team | Group that handles security incidents |
| CFB | Cipher Feedback | Block cipher mode acting as a stream cipher |
| CHAP | Challenge-Handshake Authentication Protocol | Challenge/response authentication, periodically re-challenges |
| CIA | Confidentiality, Integrity, Availability | Core security triad |
| CI/CD | Continuous Integration / Continuous Delivery (Deployment) | Automated build, test, and release pipeline |
| CIO | Chief Information Officer | Executive responsible for IT strategy |
| CIRT | Computer Incident Response Team | Team that responds to security incidents |
| CIS | Center for Internet Security | Publishes CIS Benchmarks and CIS Controls |
| CISA | Cybersecurity and Infrastructure Security Agency | US agency for cyber defense and info sharing (AIS) |
| CISO | Chief Information Security Officer | Executive accountable for the security program |
| CMDB | Configuration Management Database | Authoritative inventory of assets and their configurations |
| CMS | Content Management System | Platform for managing web content |
| CN | Common Name | Certificate field naming the subject, e.g. FQDN |
| COOP | Continuity of Operations Planning | Maintaining essential functions during crises |
| COPE | Corporate-Owned, Personally Enabled | Company device that permits personal use |
| CP | Contingency Planning | Plans for responding to disruptive events |
| CPE | Common Platform Enumeration | Standard naming of products/platforms (SCAP component) |
| CRC | Cyclic Redundancy Check | Error-detection checksum |
| CRL | Certificate Revocation List | List of revoked certificates published by a CA |
| CSA | Cloud Security Alliance | Cloud security standards body |
| CSIRT | Computer Security Incident Response Team | Team handling security incidents |
| CSO | Chief Security Officer | Executive responsible for physical and cyber security |
| CSP | Cloud Service Provider | Vendor offering cloud services |
| CSPM | Cloud Security Posture Management | Continuously checks cloud configurations for misconfiguration |
| CSR | Certificate Signing Request | Request to a CA for a certificate |
| CSRF | Cross-Site Request Forgery | Tricks an authenticated user's browser into sending unwanted requests |
| CSU | Channel Service Unit | WAN line termination device |
| CTM | Counter Mode | Block cipher mode producing a keystream from a counter (usually written CTR) |
| CTO | Chief Technology Officer | Executive responsible for technology direction |
| CVE | Common Vulnerabilities and Exposures | Identifier list for publicly known vulnerabilities |
| CVSS | Common Vulnerability Scoring System | 0-10 severity scoring |
| CWE | Common Weakness Enumeration | Catalog of software weakness types (e.g. CWE-79 XSS) |
| CYOD | Choose Your Own Device | Employee selects from approved device list |

### D

| Acronym | Expansion | Meaning |
|---|---|---|
| DAC | Discretionary Access Control | Owner decides who has access |
| DAST | Dynamic Application Security Testing | Tests a running application from outside |
| DBA | Database Administrator | Manages databases |
| DDoS | Distributed Denial of Service | DoS from many sources |
| DEP | Data Execution Prevention | Blocks code execution from data memory |
| DER | Distinguished Encoding Rules | Binary encoding for certificates |
| DES | Data Encryption Standard | Obsolete 56-bit symmetric cipher |
| DHCP | Dynamic Host Configuration Protocol | Automatically assigns IP configuration |
| DHE | Diffie-Hellman Ephemeral | Ephemeral key exchange giving forward secrecy |
| DKIM | DomainKeys Identified Mail | Digitally signs email to verify sender domain and integrity |
| DLL | Dynamic Link Library | Shared Windows code library |
| DLP | Data Loss Prevention | Detects and blocks sensitive data exfiltration |
| DMARC | Domain-based Message Authentication, Reporting, and Conformance | Policy/reporting layer over SPF and DKIM |
| DMZ | Demilitarized Zone | Screened subnet hosting public-facing services |
| DNAT | Destination Network Address Translation | Rewrites destination address, e.g. port forwarding |
| DNS | Domain Name System | Resolves names to IP addresses |
| DNSSEC | Domain Name System Security Extensions | Signs DNS records for integrity |
| DoH | DNS over HTTPS | Encrypted DNS over TCP 443 |
| DoS | Denial of Service | Attack that makes a service unavailable |
| DoT | DNS over TLS | Encrypted DNS over TCP 853 |
| DPO | Data Protection Officer | Oversees data protection compliance (GDPR) |
| DR | Disaster Recovery | Restoring IT after a disaster |
| DRP | Disaster Recovery Plan | Documented recovery procedures |
| DSA | Digital Signature Algorithm | Signature algorithm standard |
| DSL | Digital Subscriber Line | Broadband over telephone lines |

### E

| Acronym | Expansion | Meaning |
|---|---|---|
| EAP | Extensible Authentication Protocol | Framework for authentication methods |
| ECB | Electronic Code Book | Insecure block mode; identical blocks give identical ciphertext |
| ECC | Elliptic Curve Cryptography | Asymmetric crypto with small keys |
| ECDHE | Elliptic Curve Diffie-Hellman Ephemeral | Ephemeral ECC key exchange with PFS |
| ECDSA | Elliptic Curve Digital Signature Algorithm | ECC-based digital signatures |
| EDR | Endpoint Detection and Response | Endpoint monitoring, detection and response |
| EF | Exposure Factor | Percentage of asset value lost in one incident |
| EFS | Encrypting File System | Windows NTFS file-level encryption |
| EGP | Exterior Gateway Protocol | Routing between autonomous systems |
| EIP | Extended Instruction Pointer | CPU register for next instruction; buffer overflow target |
| EOL | End of Life | Vendor stops selling (and eventually supporting) a product; plan replacement |
| EOS | End of Service (Life) | Vendor no longer supports or patches (EOSL); unpatchable from this point |
| ERP | Enterprise Resource Planning | Integrated business management software |
| ESN | Electronic Serial Number | Unique mobile device identifier |
| ESP | Encapsulating Security Payload | IPSec protocol providing encryption and integrity |
| ESSID | Extended Service Set Identifier | Wireless network name |
| ETL | Extract, Transform, Load | Data pipeline process |

### F

| Acronym | Expansion | Meaning |
|---|---|---|
| FACL | File System Access Control List | ACL on files and folders |
| FAR | False Acceptance Rate | Impostors wrongly accepted by biometrics (security failure) |
| FDE | Full Disk Encryption | Encrypts entire storage volume |
| FIDO | Fast IDentity Online | Standards (FIDO2/WebAuthn, U2F) for phishing-resistant passwordless auth |
| FIM | File Integrity Monitoring | Detects unauthorized file changes |
| FISMA | Federal Information Security Modernization Act | US law requiring federal agency security programs |
| FPGA | Field Programmable Gate Array | Reconfigurable hardware chip |
| FRR | False Rejection Rate | Valid users wrongly rejected by biometrics |
| FTP | File Transfer Protocol | Cleartext file transfer, TCP 20/21 |
| FTPS | File Transfer Protocol Secure | FTP over TLS |
| FWaaS | Firewall as a Service | Cloud-delivered firewall, a SASE component |

### G

| Acronym | Expansion | Meaning |
|---|---|---|
| GCM | Galois/Counter Mode | Authenticated encryption mode for block ciphers |
| GDPR | General Data Protection Regulation | EU data protection law |
| GLBA | Gramm-Leach-Bliley Act | US law protecting financial institution customer data |
| GPG | GNU Privacy Guard | Open source PGP implementation |
| GPO | Group Policy Object | Windows centralized configuration policy |
| GPS | Global Positioning System | Satellite location system |
| GPU | Graphics Processing Unit | Processor used for graphics and parallel cracking |
| GRC | Governance, Risk, and Compliance | Integrated management of governance, risk and compliance |
| GRE | Generic Routing Encapsulation | Unencrypted tunneling protocol, often wrapped in IPSec |
| GUI | Graphical User Interface | Visual interface |

### H

| Acronym | Expansion | Meaning |
|---|---|---|
| HA | High Availability | Design that minimizes downtime |
| HDD | Hard Disk Drive | Magnetic storage |
| HIDS | Host-based Intrusion Detection System | Monitors a single host for intrusions |
| HIPAA | Health Insurance Portability and Accountability Act | US law protecting health information |
| HIPS | Host-based Intrusion Prevention System | Blocks intrusions on a host |
| HMAC | Hash-based Message Authentication Code | Keyed hash for integrity and authenticity |
| HMI | Human-Machine Interface | Operator console for ICS/SCADA |
| HOTP | HMAC-based One-Time Password | Counter-based OTP |
| HSM | Hardware Security Module | Tamper-resistant device for key storage and crypto ops |
| HTML | Hypertext Markup Language | Web page markup language |
| HTTP | Hypertext Transfer Protocol | Cleartext web protocol, TCP 80 |
| HTTPS | Hypertext Transfer Protocol Secure | HTTP over TLS, TCP 443 |
| HVAC | Heating, Ventilation, Air Conditioning | Environmental controls |

### I

| Acronym | Expansion | Meaning |
|---|---|---|
| IaaS | Infrastructure as a Service | Cloud VMs, storage, network; customer manages OS up |
| IaC | Infrastructure as Code | Managing infrastructure via code/config files |
| IAM | Identity and Access Management | Processes and tools for identities and permissions |
| ICMP | Internet Control Message Protocol | Diagnostics and error messages (ping) |
| ICS | Industrial Control Systems | Systems controlling industrial processes |
| IDEA | International Data Encryption Algorithm | Symmetric block cipher, 128-bit key |
| IDF | Intermediate Distribution Frame | Wiring closet connecting to the main distribution frame |
| IdP | Identity Provider | Authenticates users and issues assertions/tokens |
| IDS | Intrusion Detection System | Detects and alerts on suspicious activity |
| IEEE | Institute of Electrical and Electronics Engineers | Standards body, e.g. 802.1X |
| IKE | Internet Key Exchange | Negotiates IPSec security associations |
| IM | Instant Messaging | Real-time text communication |
| IMAP4 | Internet Message Access Protocol v4 | Mail retrieval keeping mail on server, TCP 143 |
| IoC | Indicators of Compromise | Evidence that a system has been breached |
| IoT | Internet of Things | Network-connected embedded devices |
| IP | Internet Protocol | Layer 3 addressing and routing |
| IPS | Intrusion Prevention System | Inline system that blocks detected attacks |
| IPSec | Internet Protocol Security | Suite securing IP traffic |
| IR | Incident Response | Process for handling security incidents |
| IRC | Internet Relay Chat | Chat protocol, historic botnet C2 |
| IRP | Incident Response Plan | Documented incident handling procedures |
| ISA | Interconnection Security Agreement | Agreement securing connection between two organizations' systems |
| ISAC | Information Sharing and Analysis Center | Sector-specific threat-intelligence sharing organization |
| ISFW | Internal Segmentation Firewall | Firewall between internal network segments |
| ISO | International Organization for Standardization | Standards body (e.g. 27001) |
| ISP | Internet Service Provider | Provides internet access |
| ISSO | Information Systems Security Officer | Manages security of an information system |
| ITCP | IT Contingency Plan | Plan for IT service recovery |
| IV | Initialization Vector | Random value that prevents repeated ciphertext |

### J

| Acronym | Expansion | Meaning |
|---|---|---|
| JIT | Just-in-Time | Temporary privilege granted only when needed (PAM) |
| JSON | JavaScript Object Notation | Lightweight data format used by REST APIs and OAuth/OIDC |
| JWT | JSON Web Token | Signed token format used for OIDC ID tokens and OAuth |

### K

| Acronym | Expansion | Meaning |
|---|---|---|
| KDC | Key Distribution Center | Kerberos component issuing tickets |
| KEK | Key Encryption Key | Key that encrypts other keys |
| Kerberos | (not an acronym) | Ticket-based network authentication protocol, port 88 |
| KRI | Key Risk Indicator | Metric signalling rising risk exposure |

### L

| Acronym | Expansion | Meaning |
|---|---|---|
| L2TP | Layer 2 Tunneling Protocol | VPN tunnel protocol, usually with IPSec |
| LAN | Local Area Network | Network in a limited area |
| LDAP | Lightweight Directory Access Protocol | Directory query protocol, TCP 389 |
| LEAP | Lightweight Extensible Authentication Protocol | Cisco legacy EAP, insecure |

### M

| Acronym | Expansion | Meaning |
|---|---|---|
| MaaS | Monitoring as a Service | Outsourced monitoring |
| MAC | Mandatory Access Control | Labels/clearances enforced by system (also Media Access Control, Message Authentication Code) |
| MAM | Mobile Application Management | Controls apps on mobile devices |
| MAN | Metropolitan Area Network | City-scale network |
| MAO | Maximum Acceptable Outage | Longest outage the business can survive (same idea as MTD) |
| MBR | Master Boot Record | First sector of a disk with boot code |
| MD5 | Message Digest 5 | 128-bit hash, deprecated |
| MDF | Main Distribution Frame | Central wiring point for a facility |
| MDM | Mobile Device Management | Manages and secures mobile devices |
| MDR | Managed Detection and Response | Outsourced EDR/XDR monitoring and response service |
| MFA | Multifactor Authentication | Two or more factor types |
| MFD | Multifunction Device | Printer/scanner/copier combo |
| MFP | Multifunction Printer | Printer with scan/copy/fax |
| ML | Machine Learning | Algorithms that learn from data |
| MMS | Multimedia Message Service | Mobile messaging with media |
| MOA | Memorandum of Agreement | Formal agreement defining each party's responsibilities (binding commitment in exam framing) |
| MOU | Memorandum of Understanding | Non-binding statement of intent |
| MPLS | Multiprotocol Label Switching | WAN technology using labels |
| MSA | Master Service Agreement | Umbrella contract terms |
| MSCHAP | Microsoft Challenge-Handshake Authentication Protocol | Microsoft CHAP variant, weak |
| MSP | Managed Service Provider | Outsourced IT management |
| MSSP | Managed Security Service Provider | Outsourced security monitoring/management |
| MTBF | Mean Time Between Failures | Average operational time between failures |
| MTD | Maximum Tolerable Downtime | Absolute limit on downtime; RTO must not exceed it |
| MTTF | Mean Time to Failure | Average time until a non-repairable failure |
| MTTR | Mean Time to Repair / Recover | Average time to restore a failed component or service (CompTIA list: "Recover") |
| MTU | Maximum Transmission Unit | Largest packet size on a link |

### N

| Acronym | Expansion | Meaning |
|---|---|---|
| NAC | Network Access Control | Enforces device posture and identity before network access |
| NAS | Network Attached Storage | File-level network storage |
| NAT | Network Address Translation | Maps private to public addresses |
| NAT-T | NAT Traversal | Encapsulates IPSec ESP in UDP 4500 to pass through NAT |
| NDA | Non-Disclosure Agreement | Confidentiality contract |
| NDR | Network Detection and Response | Behavioral analysis of network traffic with response actions |
| NFC | Near-Field Communication | Very short-range wireless |
| NFV | Network Function Virtualization | Virtualizes network appliances |
| NGFW | Next-Generation Firewall | Application-aware firewall with IPS and inspection |
| NG-SWG | Next-Generation Secure Web Gateway | Cloud web filtering with advanced inspection |
| NIC | Network Interface Card | Network adapter |
| NIDS | Network-based Intrusion Detection System | Monitors network traffic for intrusions |
| NIPS | Network-based Intrusion Prevention System | Inline network attack blocker |
| NIST | National Institute of Standards and Technology | US standards agency, publishes SP 800 series |
| NOC | Network Operations Center | Monitors network health |
| NTFS | New Technology File System | Windows file system with permissions |
| NTLM | New Technology LAN Manager | Windows challenge/response authentication, legacy |
| NTP | Network Time Protocol | Time synchronization, UDP 123 |
| NVD | National Vulnerability Database | NIST database enriching CVEs with CVSS scores |

### O

| Acronym | Expansion | Meaning |
|---|---|---|
| OAUTH | Open Authorization | Delegated authorization framework |
| OCSP | Online Certificate Status Protocol | Real-time certificate revocation check |
| OID | Object Identifier | Unique identifier for objects in certs/MIBs |
| OIDC | OpenID Connect | Authentication layer on top of OAuth 2.0 (ID token as JWT) |
| OS | Operating System | Core system software |
| OSI | Open Systems Interconnection | Seven-layer network model |
| OSINT | Open-source Intelligence | Intelligence from public sources |
| OSPF | Open Shortest Path First | Link-state routing protocol |
| OT | Operational Technology | Hardware/software controlling physical processes |
| OTA | Over the Air | Wireless updates or delivery |
| OTG | On-The-Go | USB device role capability |
| OTP | One-Time Password | Password valid for a single use or short window (HOTP/TOTP) |
| OVAL | Open Vulnerability and Assessment Language | Standard for expressing vulnerability checks |
| OWASP | Open Web Application Security Project | Community publishing web app security guidance |
| OWE | Opportunistic Wireless Encryption | Encrypts open Wi-Fi without a password (Wi-Fi Enhanced Open) |

### P

| Acronym | Expansion | Meaning |
|---|---|---|
| P12 | PKCS #12 | Certificate and private key container format |
| P2P | Peer to Peer | Direct communication between peers |
| PaaS | Platform as a Service | Cloud platform for deploying apps; provider manages OS |
| PAC | Proxy Auto Configuration (also Protected Access Credential) | Script telling browsers which proxy to use; in EAP-FAST, the credential that replaces certificates |
| PAM | Privileged Access Management | Controls and monitors privileged accounts (also Pluggable Authentication Modules) |
| PAP | Password Authentication Protocol | Cleartext authentication protocol |
| PAT | Port Address Translation | NAT using ports to share one public IP |
| PBKDF2 | Password-Based Key Derivation Function 2 | Slow salted hashing for passwords |
| PBX | Private Branch Exchange | Private phone system |
| PCAP | Packet Capture | Saved network traffic file |
| PCI DSS | Payment Card Industry Data Security Standard | Card data protection standard |
| PDP | Policy Decision Point | Zero trust component that decides to grant access (policy engine + administrator) |
| PDU | Power Distribution Unit | Distributes power to racks |
| PE | Portable Executable | Windows executable file format |
| PEAP | Protected Extensible Authentication Protocol | EAP in a TLS tunnel |
| PED | Personal Electronic Device | Portable electronics |
| PEM | Privacy Enhanced Mail | Base64 text encoding for certificates/keys |
| PEP | Policy Enforcement Point | Zero trust component that enforces the PDP decision on the data path |
| PFS | Perfect Forward Secrecy | Past sessions stay safe if long-term keys are compromised |
| PGP | Pretty Good Privacy | Email/file encryption using web of trust |
| PHI | Personal Health Information | Health data protected by HIPAA (usually "Protected Health Information" outside CompTIA) |
| PII | Personally Identifiable Information | Data that identifies an individual |
| PIN | Personal Identification Number | Numeric secret; something you know |
| PIV | Personal Identity Verification | US federal smart card credential |
| PKCS | Public Key Cryptography Standards | Family of crypto format standards |
| PKI | Public Key Infrastructure | CAs, certificates and policies for public-key trust |
| PLC | Programmable Logic Controller | Industrial controller running physical processes |
| PMF | Protected Management Frames | 802.11w; mandatory in WPA3, prevents deauthentication attacks |
| PoC | Proof of Concept | Demonstration that something works or is exploitable |
| POP | Post Office Protocol | Mail retrieval, TCP 110 |
| POTS | Plain Old Telephone Service | Analog phone network |
| PPP | Point-to-Point Protocol | Layer 2 link protocol |
| PPTP | Point-to-Point Tunneling Protocol | Deprecated VPN protocol |
| PSK | Pre-Shared Key | Shared secret for authentication |
| PTZ | Pan-Tilt-Zoom | Camera with movement controls |
| PUP | Potentially Unwanted Program | Unwanted bundled software |

### Q

| Acronym | Expansion | Meaning |
|---|---|---|
| QA | Quality Assurance | Verifying quality of software/process |
| QoS | Quality of Service | Traffic prioritization |

### R

| Acronym | Expansion | Meaning |
|---|---|---|
| RA | Registration Authority | Verifies identity before CA issues certificate |
| RAD | Rapid Application Development | Iterative development approach |
| RADIUS | Remote Authentication Dial-in User Service | Centralized AAA over UDP 1812/1813 |
| RAID | Redundant Array of Inexpensive (Independent) Disks | Disk redundancy/performance schemes |
| RAM | Random Access Memory | Volatile memory |
| RAS | Remote Access Server | Provides remote network access |
| RAT | Remote Access Trojan | Malware giving attacker remote control |
| RBAC | Role-based Access Control (also Rule-based Access Control) | Permissions assigned to roles (or rules) |
| RC4 | Rivest Cipher version 4 | Stream cipher, broken (WEP) |
| RCA | Root Cause Analysis | Finding the underlying cause of an incident to prevent recurrence |
| RCE | Remote Code Execution | Attacker runs arbitrary code on a remote system |
| RCS | Rich Communication Services | Modern SMS replacement |
| RDP | Remote Desktop Protocol | Windows remote desktop, TCP 3389 |
| RFC | Request for Comments | Internet standards document |
| RFID | Radio Frequency Identification | Wireless tag identification |
| RIPEMD | RACE Integrity Primitives Evaluation Message Digest | Hash function family |
| ROI | Return on Investment | Benefit relative to cost |
| RPO | Recovery Point Objective | Maximum tolerable data loss in time |
| RSA | Rivest, Shamir, Adleman | Asymmetric algorithm for encryption and signatures |
| RTBH | Remotely Triggered Black Hole | Drops attack traffic at the network edge |
| RTO | Recovery Time Objective | Maximum tolerable downtime to restore |
| RTOS | Real-time Operating System | OS with deterministic timing |
| RTP | Real-time Transport Protocol | Carries audio/video |
| RTU | Remote Terminal Unit | Field device in SCADA reporting to a master station |

### S

| Acronym | Expansion | Meaning |
|---|---|---|
| SaaS | Software as a Service | Provider-hosted application |
| SAE | Simultaneous Authentication of Equals | WPA3 password-based key exchange |
| SAML | Security Assertions Markup Language | XML federated SSO standard (formal name: Security Assertion Markup Language) |
| SAN | Storage Area Network (also Subject Alternative Name) | Block-level storage network; certificate field for extra names |
| SASE | Secure Access Service Edge | Cloud-delivered networking plus security |
| SAST | Static Application Security Testing | Analyzes source/binary code without running it |
| SBOM | Software Bill of Materials | Inventory of components and dependencies in software |
| SCA | Software Composition Analysis | Scans third-party/open-source dependencies for known vulnerabilities |
| SCADA | Supervisory Control and Data Acquisition | Industrial control monitoring system |
| SCAP | Security Content Automation Protocol | Standards for automated compliance/vulnerability checks |
| SCEP | Simple Certificate Enrollment Protocol | Automated certificate enrollment |
| SCIM | System for Cross-domain Identity Management | Standard for automated user provisioning across systems |
| SDK | Software Development Kit | Tools for building software |
| SDLC | Software Development Life Cycle | Stages of software development |
| SDLM | Software Development Life-cycle Methodology | Approach to the SDLC |
| SDN | Software-defined Networking | Separates control plane from data plane |
| SD-WAN | Software-defined Wide Area Network | Centrally managed WAN overlay |
| SED | Self-Encrypting Drive | Drive with built-in hardware encryption |
| SEH | Structured Exception Handling | Windows exception mechanism |
| SELinux | Security-Enhanced Linux | Linux kernel mandatory access control using security labels |
| SFTP | SSH File Transfer Protocol | File transfer over SSH, TCP 22 |
| SHA | Secure Hashing Algorithm | Family of cryptographic hashes |
| SHTTP | Secure Hypertext Transfer Protocol | Obsolete message-level HTTP security |
| SIEM | Security Information and Event Management | Aggregates and correlates logs |
| SIM | Subscriber Identity Module | Mobile network identity card |
| SIP | Session Initiation Protocol | VoIP signalling |
| SLA | Service-level Agreement | Contracted service performance levels |
| SLE | Single Loss Expectancy | AV x EF |
| SLO | Service Level Objective | Specific measurable target within an SLA |
| SMB | Server Message Block | Windows file sharing, TCP 445 |
| S/MIME | Secure/Multipurpose Internet Mail Extensions | Certificate-based email encryption and signing |
| SMS | Short Message Service | Text messaging |
| SMTP | Simple Mail Transfer Protocol | Mail transfer, TCP 25 |
| SMTPS | Simple Mail Transfer Protocol Secure | SMTP over TLS |
| SNMP | Simple Network Management Protocol | Network device management |
| SOAP | Simple Object Access Protocol | XML web services messaging |
| SOAR | Security Orchestration, Automation, and Response | Automates playbook-driven response |
| SOC | Security Operations Center | Team/facility monitoring security |
| SoC | System on Chip | Entire system on one chip |
| SOW | Statement of Work | Defines specific project deliverables |
| SOX | Sarbanes-Oxley Act | US law on financial reporting integrity and internal controls |
| SPAN | Switched Port Analyzer | Switch port mirroring that copies traffic to a monitor port |
| SPF | Sender Policy Framework | DNS record listing authorized mail senders |
| SPIM | Spam over Instant Messaging | Unsolicited instant messages |
| SQL | Structured Query Language | Database query language |
| SQLi | SQL Injection | Injecting SQL via input |
| SRTP | Secure Real-time Transport Protocol | Encrypted RTP |
| SSD | Solid State Drive | Flash storage |
| SSH | Secure Shell | Encrypted remote administration, TCP 22 |
| SSID | Service Set Identifier | Wireless network name |
| SSL | Secure Sockets Layer | Deprecated predecessor of TLS |
| SSO | Single Sign-on | One login for multiple systems |
| SSRF | Server-Side Request Forgery | Tricks a server into making requests to internal resources |
| STIG | Security Technical Implementation Guide | DISA hardening configuration standards |
| STIX | Structured Threat Information eXpression | Standard format for threat intel |
| SWG | Secure Web Gateway | Filters web traffic and enforces policy |

### T

| Acronym | Expansion | Meaning |
|---|---|---|
| TACACS+ | Terminal Access Controller Access Control System Plus | Cisco AAA over TCP 49 |
| TAXII | Trusted Automated eXchange of Indicator Information | Transport protocol for sharing STIX |
| TCP/IP | Transmission Control Protocol/Internet Protocol | Core internet protocol suite |
| TEE | Trusted Execution Environment | Isolated processor area protecting data in use (secure enclave) |
| TGT | Ticket Granting Ticket | Kerberos ticket used to request service tickets |
| TKIP | Temporal Key Integrity Protocol | WPA RC4-based encryption, deprecated |
| TLS | Transport Layer Security | Encrypts data in transit |
| TOCTOU | Time-of-Check to Time-of-Use | Race condition between checking and using a resource |
| TOTP | Time-based One-Time Password | OTP derived from time |
| TPM | Trusted Platform Module | Hardware chip for keys, measured boot, attestation |
| TSIG | Transaction Signature | Authenticates DNS updates |
| TTP | Tactics, Techniques, and Procedures | Attacker behaviour patterns |

### U

| Acronym | Expansion | Meaning |
|---|---|---|
| UAT | User Acceptance Testing | Users validate software meets needs |
| UBA | User Behavior Analytics | Baselines user behavior and flags anomalies |
| UDP | User Datagram Protocol | Connectionless transport |
| UEBA | User and Entity Behavior Analytics | UBA extended to hosts, apps and service accounts |
| UEFI | Unified Extensible Firmware Interface | Modern firmware with Secure Boot |
| UEM | Unified Endpoint Management | Manages all endpoint types centrally |
| UPS | Uninterruptible Power Supply | Battery backup |
| URI | Uniform Resource Identifier | Identifies a resource |
| URL | Universal Resource Locator | Web address (formal name: Uniform Resource Locator; CompTIA list uses "Universal") |
| USB | Universal Serial Bus | Peripheral connection standard |
| USB OTG | USB On-The-Go | Lets devices act as USB hosts |
| UTM | Unified Threat Management | All-in-one security appliance |
| UTP | Unshielded Twisted Pair | Common network cabling |

### V

| Acronym | Expansion | Meaning |
|---|---|---|
| VBA | Visual Basic for Applications | Office macro language, malware vector |
| VDE | Virtual Desktop Environment | Hosted desktop |
| VDI | Virtual Desktop Infrastructure | Centrally hosted virtual desktops |
| VLAN | Virtual Local Area Network | Logical network segmentation |
| VLSM | Variable Length Subnet Masking | Subnets of differing sizes |
| VM | Virtual Machine | Software-emulated computer |
| VoIP | Voice over IP | Phone over IP networks |
| VPC | Virtual Private Cloud | Isolated network in a public cloud |
| VPN | Virtual Private Network | Encrypted tunnel over untrusted network |
| VTC | Video Teleconferencing | Video meetings |

### W

| Acronym | Expansion | Meaning |
|---|---|---|
| WAF | Web Application Firewall | Filters HTTP traffic to protect web apps |
| WAP | Wireless Access Point | Wireless network access device |
| WEP | Wired Equivalent Privacy | Broken Wi-Fi encryption using RC4 |
| WIDS | Wireless Intrusion Detection System | Detects wireless threats such as rogue APs |
| WIPS | Wireless Intrusion Prevention System | Blocks wireless threats |
| WO | Work Order | Authorizes a specific piece of work, often under an MSA (paired with SOW) |
| WORM | Write Once Read Many | Immutable storage (also self-replicating malware) |
| WPA | Wi-Fi Protected Access | Wi-Fi security standard (WPA2/WPA3 successors) |
| WPA2 | Wi-Fi Protected Access 2 | Wi-Fi security using AES-CCMP; PSK or 802.1X |
| WPA3 | Wi-Fi Protected Access 3 | Wi-Fi security using SAE, PMF, and 192-bit enterprise mode |
| WPS | Wi-Fi Protected Setup | Easy pairing; PIN is weak |
| WTLS | Wireless TLS | TLS for WAP devices |

### X

| Acronym | Expansion | Meaning |
|---|---|---|
| XCCDF | Extensible Configuration Checklist Description Format | SCAP language for security checklists/benchmarks |
| XDR | Extended Detection and Response | EDR extended across endpoints, network, cloud |
| XML | Extensible Markup Language | Structured data format |
| XOR | Exclusive Or | Bitwise operation used in ciphers |
| XSRF | Cross-site Request Forgery | Alternate abbreviation for CSRF |
| XSS | Cross-site Scripting | Injecting scripts into pages viewed by others |

### Z

| Acronym | Expansion | Meaning |
|---|---|---|
| ZTA | Zero Trust Architecture | Never trust, always verify |
| ZTNA | Zero Trust Network Access | Per-application, identity- and context-verified access replacing VPN |

---

## Formulas and Numbers

### Quantitative risk

| Term | Formula / meaning |
|---|---|
| **AV** | Asset value |
| **EF** | Exposure factor: % of the asset lost in one event |
| **SLE** | Single loss expectancy = **AV x EF** |
| **ARO** | Annualized rate of occurrence: events per year |
| **ALE** | Annualized loss expectancy = **SLE x ARO** |

Control is worth it when: **ALE before - ALE after > annual cost of control**. (Also: net benefit = ALE reduction - control cost.)

**Example 1.** Server worth $200,000, a flood destroys 25% of it, expected once every 5 years.
SLE = 200,000 x 0.25 = $50,000. ARO = 1/5 = 0.2. ALE = 50,000 x 0.2 = **$10,000**.

**Example 2.** Laptop fleet worth $80,000; theft takes 10% per event; 3 events per year.
SLE = $8,000. ALE = 8,000 x 3 = **$24,000**.

**Example 3 (is the control worth it?).** Ransomware: AV = $500,000, EF = 40%, ARO = 0.5.
SLE = $200,000; ALE = **$100,000**. An EDR plus immutable backup program costs $60,000/year and cuts the ARO to 0.1 (ALE = $20,000).
Reduction = 100,000 - 20,000 = $80,000 > $60,000 cost, so net benefit $20,000/year: **worth it**.
Compare: a $90,000/year control reducing ALE by $80,000 is **not** justified.

| Risk response | Meaning |
|---|---|
| Accept | Tolerate (within appetite/threshold) |
| Avoid | Stop the activity |
| Mitigate | Apply controls to reduce likelihood/impact |
| Transfer | Insurance, contract, outsourcing |
| Residual risk | Remaining after controls. Inherent risk is before controls |

Qualitative: likelihood x impact on a heat map/risk matrix. **Risk = threat x vulnerability x impact** (conceptual).

### RTO, RPO, MTTR, MTBF

| Term | Meaning |
|---|---|
| **RTO** | Recovery time objective: max acceptable downtime; how fast to restore |
| **RPO** | Recovery point objective: max acceptable data loss measured in time; drives backup frequency |
| **MTTR** | Mean time to repair/restore (average) |
| **MTBF** | Mean time between failures (reliability) |
| **MTTF** | Mean time to failure (non-repairable items) |
| **WRT** | Work recovery time: after systems restored, time to verify data and resume operations |
| **MTD** | Maximum tolerable downtime = RTO + WRT |

```
 last good      DISASTER       systems         business
 backup/copy    strikes        restored        fully normal
     |<---- RPO ---->|<------ RTO ------>|<--- WRT --->|
 ----+---------------+-------------------+-------------+------> time
      (data lost)
                     |<-------------- MTD ------------>|

 MTBF:  up------------X(fail)<-MTTR->up------------X(fail)
        |<-- MTBF --->|              |<-- MTBF --->|
        (MTBF = average operating time between failures; MTTR = average repair time)
```

- Smaller RPO means more frequent backups/replication. Smaller RTO means hot site, failover, clustering.
- Availability = MTBF / (MTBF + MTTR).

### Availability and downtime

| Availability | Downtime / year | Per month (approx.) | Per week |
|---|---|---|---|
| 99% ("two nines") | 3.65 days | 7.3 hours | 1.68 hours |
| 99.9% ("three nines") | 8.76 hours | 43.8 minutes | 10.1 minutes |
| 99.99% ("four nines") | 52.6 minutes | 4.38 minutes | 1.01 minutes |
| 99.999% ("five nines") | 5.26 minutes | 26.3 seconds | 6.05 seconds |

### Backup restore counts

| Type | Backs up | Archive bit | Restore needs | Backup speed | Restore speed |
|---|---|---|---|---|---|
| **Full** | Everything | Cleared | Latest full only | Slowest | Fastest |
| **Incremental** | Changes since last backup (any type) | Cleared | Last full + **all** incrementals since | Fastest | Slowest |
| **Differential** | Changes since last **full** | Not cleared | Last full + **latest** differential | Medium (grows) | Medium |
| **Snapshot** | Point-in-time image | n/a | The snapshot | Fast | Fast |

Example: Full on Sunday, backups Mon-Fri, failure on Friday before the Friday backup (data through Thursday).
- Incremental: restore Sun full + Mon + Tue + Wed + Thu = **5 sets**.
- Differential: restore Sun full + Thu differential = **2 sets**.

Rules: **3-2-1** = 3 copies, 2 media types, 1 offsite (modern: 3-2-1-1-0 adds 1 offline/immutable, 0 errors). Rotation: GFS (grandfather-father-son: monthly, weekly, daily).

### Key lengths and algorithms

| Algorithm | Type | Size | Status |
|---|---|---|---|
| **AES** | Symmetric block | 128 / 192 / 256-bit key; 128-bit block | Standard; 10/12/14 rounds |
| 3DES | Symmetric | 168-bit (112 effective) | Deprecated |
| DES | Symmetric | 56-bit | Broken |
| ChaCha20 | Symmetric stream | 256-bit | Good on mobile; with Poly1305 |
| **RSA** | Asymmetric | 2048 minimum; 3072; 4096 | 2048 acceptable now; larger for long-term |
| **ECC** | Asymmetric | **256-bit ~ RSA 3072**; 384 ~ RSA 7680 | Smaller keys, less compute; good for mobile/IoT |
| DH / ECDH | Key exchange | 2048+ / 256+ | Ephemeral (DHE/ECDHE) gives PFS |
| **SHA-256** | Hash | 256-bit digest | SHA-2 family; standard |
| SHA-384 / SHA-512 | Hash | 384 / 512-bit | SHA-2 |
| SHA-3 | Hash | 224-512 | Keccak; different design |
| **MD5** | Hash | 128-bit | **Deprecated** (collisions) |
| **SHA-1** | Hash | 160-bit | **Deprecated** (collisions) |
| HMAC | Keyed hash | depends | Integrity + authenticity with shared secret |
| bcrypt / scrypt / PBKDF2 / Argon2 | Password hashing / KDF | n/a | Salted, slow by design; stretching |

Symmetric: fast, same key, key distribution problem, confidentiality. Asymmetric: slow, key pair, supports non-repudiation, key exchange, signatures. Hybrid used in practice (TLS). Quantum: Shor breaks RSA/ECC; Grover halves symmetric strength (AES-256 stays adequate); post-quantum algorithms (e.g. CRYSTALS-Kyber/ML-KEM) are the response.

### CVSS (v3.x / v4.0)

| Rating | Score |
|---|---|
| None | 0.0 |
| Low | 0.1 - 3.9 |
| Medium | 4.0 - 6.9 |
| High | 7.0 - 8.9 |
| Critical | 9.0 - 10.0 |

Base metrics: attack vector, complexity, privileges required, user interaction, scope, C/I/A impact. Temporal (v3; "Threat" in v4) and environmental metrics adjust. **EPSS** estimates exploit likelihood. **CVE** = identifier; **CWE** = weakness type; **NVD** = database.

### Password and MFA numbers

| Item | Common value |
|---|---|
| NIST SP 800-63B password guidance | Length over complexity; min 8 (15 for single-factor-only), allow 64+; no forced periodic rotation; block breached/common passwords; no hints/KBA |
| Account lockout | Threshold 3-10 failed attempts; lockout duration or admin reset; ties to throttling |
| Password history | Commonly 5-24 remembered |
| Min/max age | Min age stops rapid cycling through history |
| Entropy | More length is better than more complexity |
| MFA factors | Something you **know**, **have**, **are**, **somewhere you are**, **something you do** |
| OTP | HOTP (counter-based), TOTP (time-based, usually 30 s window) |
| Biometric errors | FAR (false accept; security risk), FRR (false reject; usability), **CER/EER** = point where FAR = FRR (lower is better) |
| SMS OTP | Weakest MFA delivery (SIM swap, interception) |
| Kerberos clock skew | 5 minutes default |
| Session timeouts | Idle timeout + absolute timeout |

### Incident response phases (NIST SP 800-61 / exam order)

**Preparation -> Detection -> Analysis -> Containment -> Eradication -> Recovery -> Lessons learned**

(SY0-701 objective 4.8 lists these seven separately. NIST SP 800-61r2 groups them into four phases: preparation; detection and analysis; containment, eradication and recovery; post-incident activity. Answer exam questions with the seven-step order.)

### Order of volatility (most to least volatile)

1. CPU registers and cache
2. Routing table, ARP cache, process table, kernel statistics
3. RAM (memory contents)
4. Temporary file systems / swap
5. Disk (storage)
6. Remote logging and monitoring data
7. Physical configuration, network topology
8. Archival media / backups

Forensics: legal hold, chain of custody, hash (write blocker) before analysis, work on copies, document everything. **Collect memory first.**

### Data classification ladders

| Level (high to low) | Government (US) | Commercial |
|---|---|---|
| 1 | Top Secret | Confidential / Restricted / Proprietary |
| 2 | Secret | Private / Sensitive |
| 3 | Confidential | Internal / Company-confidential |
| 4 | Unclassified (CUI, FOUO) | Public |

SY0-701 data classification terms: **sensitive, confidential, public, restricted, private, critical** (no fixed order across organisations). Other terms: PII, PHI, financial, trade secret, intellectual property, regulated; owner (accountable), custodian (day-to-day), steward, controller (decides purposes), processor (handles on behalf of controller), DPO.

### Compliance frameworks and laws

| Name | Covers |
|---|---|
| **PCI DSS** | Payment card data; merchants and processors; 12 requirements; contractual standard, not law |
| **HIPAA** | US healthcare; PHI; Privacy, Security, and Breach Notification Rules |
| **GDPR** | EU/EEA personal data; consent, rights (access, erasure, portability), breach notification within **72 hours**, fines up to 4% global turnover or EUR 20M |
| **SOX** | US public companies; financial reporting integrity; internal controls and audit (IT controls over financial systems) |
| **GLBA** | US financial institutions; protection of customers' nonpublic personal information |
| **FISMA** | US federal agencies and contractors; information security program (uses NIST SP 800-53) |
| **FERPA** | US student education records |
| **CCPA/CPRA** | California consumer privacy |
| **NIST CSF** | Voluntary framework: Identify, Protect, Detect, Respond, Recover (+ Govern in CSF 2.0) |
| **NIST RMF (SP 800-37)** | Risk management framework for federal systems: prepare, categorize, select, implement, assess, authorize, monitor |
| **NIST SP 800-53** | Security and privacy control catalogue |
| **ISO/IEC 27001** | International ISMS standard (certifiable); **27002** control guidance; **27701** privacy; **27017/27018** cloud |
| **CIS Controls / Benchmarks** | Prioritized safeguards; configuration hardening benchmarks per OS/app |
| **SOC 2** | Service organization controls (trust services criteria); Type I = point-in-time design, Type II = operating effectiveness over a period |
| **CSA CCM / STAR** | Cloud security controls and assurance |
| **MITRE ATT&CK** | Adversary tactics/techniques knowledge base (not a compliance framework) |
| **Diamond Model / Cyber Kill Chain** | Intrusion analysis models |

---
