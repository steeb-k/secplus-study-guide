# Domain 5 — Security Program Management and Oversight (20%)

> **Note:** AI-generated content, not yet vetted for accuracy. See the README for details.

Objectives 5.1–5.6. Governance, risk, third parties, compliance, audits, awareness. Heavy on vocabulary and "which term fits this scenario" questions.

---

## 5.1 Summarize elements of effective security governance

### Guidelines, policies, standards, procedures

| Document | Nature | Answers | Mandatory? | Example |
|---|---|---|---|---|
| **Policy** | High-level management statement of intent and direction | *Why / what* | Yes | "All data must be encrypted at rest" |
| **Standard** | Specific, measurable requirement that supports a policy | *What exactly* (specs) | Yes | "AES-256 for data at rest" |
| **Procedure** | Step-by-step instructions to perform a task | *How* | Yes | Steps to onboard a new user |
| **Guideline** | Recommended best practice, advisory | *Suggestion* | **No** | "Use a password manager" |

> **Exam tip:** Order of abstraction: policy (broadest) > standard > procedure (most detailed). Guideline = optional/recommendation; everything else is mandatory. "Step-by-step" = procedure. "Minimum technical requirement" = standard.

### Policies (named in the objectives)

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

### Standards

| Standard | What it specifies |
|---|---|
| **Password** | Length, complexity, history, age, lockout, MFA requirement, no reuse. |
| **Access control** | Model (RBAC/ABAC/MAC/DAC), least privilege, separation of duties, review cadence, provisioning rules. |
| **Physical security** | Badges, access control vestibules (mantraps), cameras, visitor logs, locks, guard coverage. |
| **Encryption** | Approved algorithms, key lengths, protocols (TLS 1.2+), key management and rotation. |

### Procedures

| Procedure | Notes |
|---|---|
| **Change management** | Request > impact/risk analysis > approval (CAB) > test > schedule (maintenance window, backout plan ready) > implement > verify or back out > document/post-review. |
| **Onboarding** | Accounts provisioned by role, AUP signed, training, equipment issued, background check complete. |
| **Offboarding** | Disable accounts immediately, retrieve assets/badges, revoke access and tokens, exit interview, reassign data. |
| **Playbooks** | Prescribed step-by-step response for a specific scenario (ransomware, phishing). Often automated via SOAR. Distinct from a runbook (routine operational tasks). |

### External considerations

| Factor | Examples / key point |
|---|---|
| **Regulatory** | Government-mandated; penalties for noncompliance (HIPAA, SOX, GLBA, FISMA). PCI DSS is *not* a regulation: it is a contractual/industry standard (see Industry). |
| **Legal** | Laws, contractual obligations, liability, e-discovery, breach notification. |
| **Industry** | Sector standards and frameworks (PCI DSS, ISO 27001, NIST CSF, CIS). |
| **Geographic: local / regional / national / global** | Local ordinances; regional (US state laws such as CCPA/CPRA, EU member-state law); national (HIPAA, GLBA, SOX, COPPA); global (GDPR's extraterritorial reach, cross-border data-transfer rules, international agreements). **Data sovereignty** applies: data is subject to the laws of the country where it is collected or stored. |

### Monitoring and revision

- Review policies on a **schedule** and after **triggers**: new laws, incidents, audit findings, business changes, new technology.
- Monitor compliance with metrics/audits; track exceptions; version-control documents; communicate and re-acknowledge changes.

### Types of governance structures

| Structure | Role |
|---|---|
| **Boards** | Ultimate accountability; set direction and risk oversight. |
| **Committees** | Specialized oversight (risk committee, audit committee, change advisory board, security steering). |
| **Government entities** | Regulators/legislatures whose rules the organization must follow (local, state, national). |
| **Centralized** | One central body makes decisions; consistent, efficient, slower to adapt locally. |
| **Decentralized** | Business units decide locally; flexible and fast, inconsistent and harder to audit. |

### Roles and responsibilities for systems and data

| Role | Responsibility |
|---|---|
| **Owner** | Senior business person accountable for the data; sets classification and access rules. |
| **Controller** | Determines **why and how** personal data is processed (GDPR). |
| **Processor** | Processes personal data **on behalf of** the controller (e.g. cloud payroll vendor). |
| **Custodian / steward** | Day-to-day handling: implements controls, backups, access, quality. Custodian = technical protection; steward = quality/meaning/proper use of the data. |

> **Exam tip:** Owner = accountable and decides. Custodian = does the technical work. Controller decides purposes; processor follows instructions. The data owner classifies; the custodian applies the protections.

---

## 5.2 Explain elements of the risk management process

### Risk identification

Find assets, threats, vulnerabilities, and existing controls. Sources: asset inventory, vulnerability scans, threat intel, audits, incidents, interviews.

### Risk assessment

| Type | When |
|---|---|
| **Ad hoc** | Triggered by an event (new threat, incident, urgent project). |
| **Recurring** | On a schedule (annual, quarterly), often compliance-driven. |
| **One-time** | A single assessment for a specific project, acquisition, or system. |
| **Continuous** | Ongoing, automated monitoring; real-time risk posture. |

### Risk analysis

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

> **Exam tip:** Never spend more per year on a control than the ALE reduction it delivers (ALE before − ALE after). "Once every 5 years" means ARO = 0.2. "Twice a year" means ARO = 2.

### Risk register

Living document listing identified risks with: description, owner, likelihood, impact, score, mitigation plan, status, residual risk.

| Element | Meaning |
|---|---|
| **Key risk indicators (KRIs)** | Metrics that signal rising risk exposure (e.g. unpatched critical vulns count, failed logins). Leading indicators. |
| **Risk owner** | Person accountable for managing a specific risk. |
| **Risk threshold** | Level at which a risk requires action/escalation; trigger point for KRIs. |

### Risk tolerance vs risk appetite

| Term | Definition |
|---|---|
| **Risk appetite** | Amount/type of risk the organization is *willing to pursue* to meet objectives (strategic, broad). |
| **Risk tolerance** | Acceptable *deviation* around the appetite for a specific risk (operational, measurable limit). |

Appetite postures:
- **Expansionary**: willing to take on more risk for growth/returns.
- **Conservative**: minimize risk; prefers stability.
- **Neutral**: balanced; takes risk when reward justifies it.

> **Exam tip:** Appetite = how much risk we want to take (strategy). Tolerance = how far from that we can stray (limit). A startup chasing market share = expansionary; a bank or hospital = conservative.

### Risk management strategies

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

### Risk reporting

Communicate risk posture to stakeholders: executive dashboards, heat maps, risk register extracts, KRI trends, status of mitigation. Tailor detail to the audience (board = summary, ops = detail).

### Business impact analysis (BIA)

Identifies critical functions and quantifies the effect of their loss; drives recovery priorities.

| Term | Definition |
|---|---|
| **RTO** (recovery time objective) | Maximum acceptable time to restore a service after disruption. |
| **RPO** (recovery point objective) | Maximum acceptable data loss, measured in time since last good backup. |
| **MTTR** (mean time to repair; CompTIA's acronym list says recover) | Average time to repair a failed component and restore service. |
| **MTBF** (mean time between failures) | Average operating time between failures; reliability. |
| **MTD / MAO** | Maximum tolerable downtime; the absolute limit before the business suffers unacceptable harm. RTO must be < MTD. |
| **WRT** | Work recovery time: time after systems are restored to verify data and resume normal operations. MTD = RTO + WRT, so RTO must be shorter than MTD |

**Worked example.** Order system: RPO 1 hour, RTO 4 hours. The business can lose at most 1 hour of orders, so backups/replication must occur at least hourly. Service must be back within 4 hours of the outage. A nightly backup fails the RPO. Availability from MTBF/MTTR: MTBF 1,000 h, MTTR 10 h gives availability = 1000 / (1000 + 10) = about 99.0%.

> **Exam tip:** RTO = "how long can we be down"; RPO = "how much data can we lose" (look at backup frequency). MTBF = reliability (bigger is better); MTTR = repairability (smaller is better).

---

## 5.3 Explain the processes associated with third-party risk assessment and management

### Vendor assessment

| Method | Description |
|---|---|
| **Penetration testing** | Authorized testing of the vendor's systems (or of your integration with them), only with permission and defined scope. |
| **Right-to-audit clause** | Contract clause letting the customer (or its auditor) inspect the vendor's controls, records, and facilities. |
| **Evidence of internal audits** | Vendor shares its own audit reports and remediation evidence. |
| **Independent assessments** | Third-party audits/attestations (SOC 2 Type II, ISO 27001 certification) - more credible than self-reporting. |
| **Supply chain analysis** | Evaluate the vendor's own suppliers and dependencies (fourth parties); software provenance, SBOM, hardware origin. |

### Vendor selection

- **Due diligence**: investigate the vendor *before* contracting (financial health, security posture, references, certifications, breach history).
- **Conflict of interest**: relationship that could bias selection (family ties, financial stake, gifts). Disclose and recuse.

### Agreement types

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

### Vendor monitoring

Continuous, not one-time: review SLA metrics, audit reports, security ratings, incident notifications, financial health, and re-assess on contract renewal or after changes. Separate 5.3 items, covered next: questionnaires (assessment and periodic re-assessment) and rules of engagement (scope and limits for any testing of the vendor).

### Questionnaires

Standardized security questionnaires (SIG, CAIQ, custom) the vendor completes about its controls; first-pass screening; self-reported so verify with evidence.

### Rules of engagement

Defines what is allowed in testing/assessment of the vendor: scope, targets, timing, methods, excluded systems, contacts, and escalation. Prevents unintended damage and legal exposure.

### Vendor risk terms

| Term | Meaning |
|---|---|
| **Third party** | Vendor/supplier directly contracted. |
| **Fourth party** | The vendor's own suppliers. |
| **Offboarding** | End of the relationship: revoke access, retrieve/destroy data, confirm per contract. |

---

## 5.4 Summarize elements of effective security compliance

### Compliance reporting

| Type | Audience / purpose |
|---|---|
| **Internal** | Management, board, audit committee: status of controls, exceptions, remediation. |
| **External** | Regulators, auditors, customers, partners: required filings, attestations, certifications. |

### Consequences of non-compliance

| Consequence | Notes |
|---|---|
| **Fines** | Monetary penalties (GDPR up to EUR 20M or 4% of global annual turnover, whichever is higher). |
| **Sanctions** | Regulatory restrictions or formal penalties; can include trade restrictions. |
| **Reputational damage** | Loss of customer trust, negative press. |
| **Loss of license** | Cannot operate in regulated sector. |
| **Contractual impacts** | Lost contracts, terminated partnerships, penalties (e.g. loss of ability to process cards under PCI DSS). |

### Compliance monitoring

| Element | Definition |
|---|---|
| **Due diligence** | Investigating/understanding risk *before* acting (research, vetting). |
| **Due care** | Acting responsibly on an ongoing basis; doing what a reasonable person would to protect assets (applying controls, patching). |
| **Attestation** | Formal statement (by management or auditor) that controls are in place and operating. |
| **Acknowledgement** | Individual confirms they read and understood a policy (AUP signing). |
| **Internal vs external** | Internal monitoring by compliance team/internal audit; external by regulators and independent auditors. |
| **Automation** | Continuous control monitoring, policy-as-code, automated evidence collection, and dashboards reduce manual effort and drift. |

> **Exam tip:** Due *diligence* = before/investigate. Due *care* = after/ongoing maintenance. Failing to apply due care is negligence.

### Privacy

| Concept | Key point |
|---|---|
| **Legal implications - local/regional** | State/provincial laws (CCPA/CPRA, other US state laws). |
| **National** | Country-level (HIPAA, GLBA, COPPA, PIPEDA). |
| **Global** | GDPR applies to organizations established in the EU and to any organization elsewhere that offers goods or services to, or monitors, people in the EU (exam shorthand: 'EU residents' data'). Cross-border transfer rules; data sovereignty. |
| **Data subject** | The individual the personal data is about; holds rights (access, correction, deletion, portability, objection). |
| **Controller vs processor** | Controller decides purpose/means; processor processes on controller's behalf. Controller remains accountable. |
| **Ownership** | Data owner is accountable for the data; the data subject retains privacy rights regardless. |
| **Data inventory and retention** | Know what personal data you hold, where, why, and for how long; delete when retention ends. Data minimization. |
| **Right to be forgotten** | Data subject may request erasure (GDPR Art. 17) when data is no longer needed or consent withdrawn; limited by legal retention duties. |

> **Exam tip:** "EU residents' data" = GDPR. "Health data, US" = HIPAA. "Children under 13" = COPPA. "California consumers" = CCPA. "Erasure request" = right to be forgotten.

---

## 5.5 Explain types and purposes of audits and assessments

### Attestation

An independent party's (or management's) formal opinion that a control or statement is accurate and effective (e.g. SOC 2 report, signed compliance statement).

### Internal

| Type | Purpose |
|---|---|
| **Compliance** | Verify adherence to laws, regulations, policies, contracts. |
| **Audit committee** | Board-level body overseeing financial reporting, internal audit, and controls; independent of management. |
| **Self-assessments** | Teams evaluate their own controls (checklists, questionnaires); cheap and frequent but least objective. |

### External

| Type | Purpose |
|---|---|
| **Regulatory** | Required by law/regulators; findings may carry penalties. |
| **Examinations** | Formal regulator review (bank examiners). |
| **Assessment** | Evaluation against a framework or standard (maturity, gap analysis). |
| **Independent third-party audit** | Unbiased outside auditor for certification or customer assurance (SOC 2, ISO 27001, PCI QSA). |

> **Exam tip:** Independence and objectivity increase self-assessment < internal audit < external independent audit. "Provides assurance to customers" = independent third-party audit/attestation.

### Penetration testing

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
| **Passive** | No direct interaction with the target's systems; very hard to detect | OSINT, WHOIS, social media, DNS records, Shodan |
| **Active** | Direct interaction with target systems; detectable | Port scans, banner grabbing, ping sweeps |

> **Exam tip:** Written permission and rules of engagement come before any penetration test. "No prior knowledge" = unknown environment/black box. "Red + blue working together" = integrated/purple. Passive recon avoids touching the target's systems (uses public/third-party sources).

---

## 5.6 Given a scenario, implement security awareness practices

### Phishing

- **Campaigns**: simulated phishing emails sent to staff to measure susceptibility (click rate, credential-submission rate, report rate); followed by targeted training.
- **Recognition**: suspicious sender/domain, urgency, mismatched URLs, unexpected attachments, requests for credentials or payment, generic greeting, grammar errors.
- **Response**: do not click or reply; report using the report-phishing button or to the security team; if clicked, disconnect and report immediately; change credentials.
- **Handling reports (security team):** acknowledge the reporter, triage (headers, URLs, attachments, sandbox), search and purge the message from all mailboxes, block sender/domain/URL/hash, identify who clicked or entered credentials (reset, revoke sessions), escalate to IR if compromise is confirmed, feed results into awareness metrics.

### Anomalous behavior recognition

| Category | Meaning | Example |
|---|---|---|
| **Risky** | Behavior that increases exposure | Using unsanctioned apps (shadow IT), reusing passwords, plugging in unknown USB |
| **Unexpected** | Out-of-pattern activity | Login at 3 a.m. from another country, large data download |
| **Unintentional** | Mistakes without malicious intent | Misdirected email, misconfigured sharing, lost device |

### User guidance and training topics

| Topic | What users are taught |
|---|---|
| **Policy/handbooks** | Know and acknowledge the AUP, data handling/classification rules, and where to find policies. |
| **Situational awareness** | Notice surroundings: shoulder surfing, tailgating/piggybacking, strangers in secure areas, clean desk, screen locks. |
| **Insider threat** | Recognize and report warning signs (unusual access, data hoarding, policy circumvention) through a confidential channel. |
| **Password management** | Long unique passphrases, password manager, MFA, never share or reuse credentials. |
| **Removable media and cables** | Do not plug in found USB drives or unknown cables (a malicious cable or drive can pose as a keyboard and inject keystrokes); avoid public USB charging ports ('juice jacking' = data theft or malware through a compromised charging port) and use your own charger or a data blocker. Use only approved, encrypted media. |
| **Social engineering** | Recognize pretexting, phishing/vishing/smishing, impersonation, urgency and authority tactics; verify out of band. |
| **Operational security (OPSEC)** | Avoid leaking sensitive details (projects, travel, org charts) in conversation or on social media that attackers can use for reconnaissance. |
| **Hybrid/remote work environments** | Secure home Wi-Fi, use VPN, avoid public Wi-Fi without VPN, lock screens, keep family off work devices, physical privacy for calls. |

### Reporting and monitoring

| Phase | Meaning |
|---|---|
| **Initial** | Baseline measurement: pre-training results, first campaign, first assessment. |
| **Recurring** | Repeated measurement over time (quarterly campaigns, annual training) to show trends. |

Metrics: completion rates, phishing click/report rates, incident counts, time to report.

### Development and execution

- **Development**: build a program tailored to roles (executives, developers, admins, general users); content updated for current threats; gamification, posters, newsletters, videos.
- **Execution**: new-hire training at onboarding, annual refreshers, role-based training, simulated attacks, LMS tracking, management support, and consequences for repeated failures.

> **Exam tip:** Awareness = everyone, general; training = role-specific skills; education = deeper knowledge. A user who clicks a simulated phish should get immediate feedback and targeted remedial training, not punishment.

---

## Most-tested distinctions

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
