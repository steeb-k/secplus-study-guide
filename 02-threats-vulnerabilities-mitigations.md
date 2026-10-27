# Domain 2 — Threats, Vulnerabilities, and Mitigations (22%)

> **Note:** AI-generated content, not yet vetted for accuracy. See the README for details.

Objectives 2.1–2.5. Heaviest conceptual domain after Domain 4; most questions are scenario → classify the actor, vector, vulnerability, attack or indicator, then pick the mitigation.

---

## 2.1 Compare and contrast common threat actors and motivations

### Threat actors

| Actor | Resources / funding | Sophistication | Internal / external | Typical motivation |
|---|---|---|---|---|
| **Nation-state** | Very high (government) | Very high; custom tools, zero-days, long dwell time (APT) | External | Espionage, political/military advantage, disruption of critical infrastructure, war |
| **Unskilled attacker** (script kiddie) | Low | Low; uses prebuilt tools/scripts | External | Disruption, curiosity, notoriety, "fun" |
| **Hacktivist** | Low–medium | Low–medium; DDoS, defacement, doxing, leaks | External | Philosophical/political belief, protest, revenge, disruption |
| **Insider threat** | Variable; already has access | Variable; knows where the data is | Internal | Revenge, financial gain, espionage (recruited), or negligence (unintentional) |
| **Organized crime** | High (business model) | High; ransomware-as-a-service, fraud rings | External | Financial gain (extortion, theft, fraud) |
| **Shadow IT** | Employee/department budget | Low (not an attacker but a risk source) | Internal | Convenience, speed, bypassing slow IT process; creates unmanaged assets and data leakage |

> **Exam tip:** "Long-term, stealthy, well-funded, targeted" = **nation-state / APT**. "Hired by competitors / sold data for profit" = **insider (financial)** or **organized crime**. "Deployed unapproved SaaS / personal cloud storage / unmanaged server" = **shadow IT**. "Downloaded a tool and ran it without understanding it" = **unskilled attacker**.

### Attributes of actors

- **Internal vs external** — insiders bypass perimeter controls; mitigate with least privilege, DLP, UEBA, separation of duties, job rotation.
- **Resources/funding** — determines ability to buy zero-days, run infrastructure, sustain campaigns.
- **Level of sophistication/capability** — from copy-paste tools to custom malware and supply-chain compromise.

### Motivations

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

## 2.2 Explain common threat vectors and attack surfaces

**Attack surface** = all points where an attacker could try to enter or extract data. **Threat vector** = the path/method used. Reduce the surface by closing ports, removing unused services/software, and removing unsupported systems.

### Message-based

| Vector | Definition / exam keyword |
|---|---|
| **Email** | Phishing, malicious attachments, BEC; mitigated by SPF/DKIM/DMARC, filtering, sandboxing |
| **Short Message Service (SMS)** | **Smishing**; links or "reply to confirm" texts |
| **Instant messaging (IM)** | Malicious links/files via chat platforms; impersonation of coworkers |

### Image-based
- Malicious content hidden in images (embedded payloads, steganography, malformed image files exploiting a parser; QR codes that redirect to malicious sites = **quishing**).

### File-based
- Malicious documents/PDFs/archives/executables; macros in Office files; files that exploit viewer vulnerabilities. Mitigate: disable macros, sandbox/detonate attachments, application allow listing.

### Voice call
- **Vishing**; caller-ID spoofing, fake help desk or bank calls; deepfake voice impersonation of executives.

### Removable device
- USB drives dropped in parking lots (baiting), malicious USB cables/devices (HID emulation, e.g. "rubber ducky"), autorun malware. Mitigate: disable USB mass storage/autorun, port blocking, DLP, endpoint control.

### Vulnerable software
- **Client-based** — software installed and run on each endpoint; a flaw in that installed client is exploitable on every device that has it, and every copy must be patched (often a slow, uneven rollout).
- **Agentless** — nothing installed on the endpoint; the code runs centrally or is delivered on demand (web app, browser-delivered code). The vulnerability lives in one place: an attacker who compromises it hits every user at once, but a single server-side fix covers everyone.

### Unsupported systems and applications
- End-of-life/end-of-support OS or software receives **no security patches**; permanent known vulnerabilities. Mitigate: replace/upgrade, or isolate (segmentation), restrict access, compensating controls, virtual patching with IPS/WAF.

### Unsecure networks

| Type | Risk |
|---|---|
| **Wireless** | Rogue AP, evil twin, weak encryption (WEP/WPA), open guest networks, eavesdropping |
| **Wired** | Unprotected jacks in public areas; rogue devices; mitigate with 802.1X NAC, port security |
| **Bluetooth** | Bluejacking (unsolicited messages), bluesnarfing (data theft), pairing weaknesses |

### Open service ports
- Each listening port is attack surface. Unneeded open ports = misconfiguration; discover with port scanners (Nmap), close with host firewall/hardening, disable unused services.

### Default credentials
- Vendor-default usernames/passwords on routers, cameras, IoT, databases, admin consoles. Mitigate: change on deployment, unique credentials, enforce at provisioning.

### Supply chain
- Compromise through a trusted third party; each has an attack position:
  - **Managed service provider (MSP)** — a compromised MSP gives access to all its customers.
  - **Vendor** — compromised product/update (e.g. trojanized software update); hardware tampering.
  - **Supplier** — counterfeit or tampered components/parts.
- Mitigate: vendor assessment, SBOM, code signing, update verification, contractual security requirements, hardware provenance checks.

### Human vectors / social engineering
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
| **Elicitation** (eliciting information) | Extracting information through ordinary conversation |
| **Identity fraud / theft** | Using stolen identity data to open accounts or impersonate |

> **Exam tip:** Spear phishing (any specific person) vs whaling (executives) vs BEC (financial request via business email). Phishing = link click; **pharming** = redirected without clicking. **Typosquatting** = misspelled domain; **brand impersonation** = looks like the brand. **Watering hole** = target's usual site is compromised. Tailgating vs piggybacking: tailgating is unauthorised follow-through; **mantrap/access control vestibule** is the control.

**Principles of social engineering (why it works):** authority, intimidation, consensus/social proof, scarcity, familiarity/liking, trust, urgency.

---

## 2.3 Explain various types of vulnerabilities

### Application
| Vulnerability | Definition / keyword |
|---|---|
| **Memory injection** | Malicious code written into a legitimate running process's memory (DLL injection, process hollowing) so it runs with that process's rights and evades file-based AV; typical of fileless malware. Mitigate: EDR, DEP/ASLR, least privilege |
| **Buffer overflow** | Input exceeds buffer size and overwrites adjacent memory; crashes or code execution; mitigate with bounds checking, ASLR, DEP |
| **Race condition** | Outcome depends on timing of events; **TOC/TOU** (time-of-check to time-of-use) is the classic form. TOC = the moment a resource or permission is checked; TOU = the moment it is used; the attacker changes the resource in between (swap a checked file for a symlink, double-spend a balance before it updates). Mitigate with atomic operations and locking |
| **Malicious update** | Update channel delivers tampered code; mitigate with code signing and hash verification |

### Operating system (OS)-based
- Unpatched OS flaws, insecure defaults, unnecessary services, privilege escalation bugs, legacy/unsupported OS versions.

### Web-based
| Vulnerability | Definition / keyword |
|---|---|
| **SQL injection (SQLi)** | Untrusted input altered a database query; fix with parameterized queries/prepared statements and input validation |
| **Cross-site scripting (XSS)** | Script injected into a page and executed in other users' browsers (reflected, stored, DOM-based); fix with output encoding, input sanitization, CSP |
| **CSRF/XSRF** (related) | Forces an authenticated user's browser to send an unwanted request; fix with anti-CSRF tokens, SameSite cookies |

### Hardware
| Vulnerability | Definition |
|---|---|
| **Firmware** | Outdated/malicious/unsigned firmware (BIOS/UEFI, device); mitigate with signed updates, secure boot |
| **End-of-life (EOL) / end-of-service-life (EOSL)** | EOL: vendor stops selling and winds down support; EOSL/EOS: no more security patches at all. Exam framing: an EOL/unsupported system is unpatchable, so replace, upgrade, or isolate it |
| **Legacy** | Old but possibly still supported; poor security design, hard to patch |

### Virtualization
| Vulnerability | Definition |
|---|---|
| **VM escape** | Guest breaks out to the hypervisor or other VMs |
| **Resource reuse** | Memory/storage allocated to a new VM still contains data from a previous tenant; mitigate by scrubbing |
| **VM sprawl** (related) | Unmanaged, forgotten VMs that go unpatched |

### Cloud-specific
- Misconfigured storage buckets/permissions, insecure APIs, excessive IAM permissions, weak tenant isolation, shared-responsibility misunderstandings, exposed keys in code repos.

### Supply chain
| Component | Meaning |
|---|---|
| **Service provider** | Third party with network/data access compromised |
| **Hardware provider** | Tampered or counterfeit devices, firmware backdoors |
| **Software provider** | Compromised libraries/updates/build systems (also open-source dependency risk) |

### Cryptographic
- Weak/deprecated algorithms (DES, MD5, SHA-1, RC4), short keys, poor random number generation, hard-coded or exposed keys, improper certificate validation, no encryption of data in transit/at rest, expired certs.

### Misconfiguration
- Open permissions, default settings/credentials, unnecessary services, verbose error messages, excessive ports. The most common real-world vulnerability type.

### Mobile device
| Vulnerability | Definition |
|---|---|
| **Side loading** | Installing apps from outside the official store, bypassing vetting |
| **Jailbreaking** (iOS) / **Rooting** (Android) | Removes manufacturer restrictions; defeats the security model; MDM should detect and block/quarantine |

### Zero-day
- A vulnerability unknown to the vendor (no patch exists). Patching can't help; use layered defenses: segmentation, IPS/behavioural detection, EDR, least privilege, virtual patching, threat intelligence.

> **Exam tip:** "No patch available / vendor unaware" = **zero-day**. "Guest to host" = **VM escape**. "Leftover data on new VM" = **resource reuse**. "Check then use gap" = **race condition/TOCTOU**. "Database query manipulated" = SQLi; "script runs in victim's browser" = XSS. "Rooted/jailbroken" = defeats mobile controls; "unofficial app source" = **side loading**.

---

## 2.4 Given a scenario, analyze indicators of malicious activity

### Malware attacks

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
| **Botnet** (related) | Many compromised hosts (bots) under C2 control; DDoS, spam, credential stuffing |
| **RAT** (related) | Remote access trojan: a trojan that gives the attacker covert interactive control of one host (files, webcam, keystrokes) |
| **Fileless** (related) | Runs in memory using legitimate tools (PowerShell, WMI); no file on disk; detect with EDR/behavioural analysis |
| **Cryptojacking** (related) | Hijacked CPU/GPU used to mine crypto; high resource use |

> **Exam tip:** Worm vs virus: worm spreads **on its own**; virus needs a **host and user action**. Trojan = disguised, no self-replication. Logic bomb = **condition-triggered**. Rootkit = **concealment + persistence**. Fileless = **memory-only / living-off-the-land**.

### Physical attacks
| Attack | Definition |
|---|---|
| **Brute force (physical)** | Forcing entry — breaking locks, doors, barriers |
| **RFID cloning** | Copying a badge/credential to a new card; mitigate with encrypted/higher-security credentials, MFA |
| **Environmental** | Attacks on power, HVAC, fire suppression, water; disrupts availability |

### Network attacks
| Attack | Definition / keyword |
|---|---|
| **DDoS — amplified** | Small spoofed request yields large response sent to victim (DNS, NTP amplification) |
| **DDoS — reflected** | Spoofed source IP makes third-party servers send responses to the victim |
| **DNS attacks** | DNS poisoning/spoofing, DNS hijacking, domain hijacking, tunnelling; users redirected to fake sites |
| **Wireless** | Rogue AP, **evil twin** (lookalike SSID), deauthentication, WPS/weak-key attacks |
| **On-path** (formerly MITM) | Attacker intercepts/alters traffic between two parties; ARP poisoning, rogue AP; mitigate with TLS, DAI |
| **Credential replay** | Captured valid credentials/tokens/hashes reused (pass-the-hash, session replay); mitigate with nonces, timestamps, short-lived tokens, Kerberos protections |
| **Malicious code** | Malware delivered or executed over the network |

### Application attacks
| Attack | Definition / keyword |
|---|---|
| **Injection** | Untrusted input interpreted as commands (SQL, command, LDAP, XML) |
| **Buffer overflow** | Memory overwrite via oversized input |
| **Replay** | Valid data transmission captured and re-sent |
| **Privilege escalation** | Gaining higher rights (vertical) or another user's rights (horizontal) |
| **Forgery** | CSRF (forged request from authenticated browser), SSRF (server tricked into making internal requests) |
| **Directory traversal** | `../` sequences to reach files outside the web root; mitigate with input validation, least privilege |

### Cryptographic attacks
| Attack | Definition |
|---|---|
| **Downgrade** | Forces use of weaker protocol/cipher (e.g. TLS → SSL); disable legacy protocols |
| **Collision** | Two different inputs yield the same hash; breaks integrity (MD5, SHA-1) |
| **Birthday** | Probability-based method to find hash collisions faster than brute force |

### Password attacks
| Attack | Keyword |
|---|---|
| **Spraying** | One/few common passwords against **many accounts** (avoids lockout); many accounts with few attempts each |
| **Brute force** | Try all possible combinations against one account/hash; online or offline |
| **Dictionary** | Wordlist of likely passwords |
| **Rainbow table** (related) | Precomputed hash lookups; defeated by **salting** |
| **Credential stuffing** (related) | Reused breached username/password pairs tried on other sites |

> **Exam tip:** Spraying = many accounts, few passwords, evades lockout. Brute force = one target, all combos, triggers lockout. Credential stuffing = breach data. Salting defeats rainbow tables; key stretching (bcrypt, PBKDF2) slows brute force. Online attacks are limited by lockout; offline attacks against stolen hashes are not.

### Indicators

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

### Symptom → most likely attack

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

## 2.5 Explain the purpose of mitigation techniques used to secure the enterprise

### Segmentation
- Divide the network into zones (VLANs, subnets, firewalls, microsegmentation) to contain breaches and limit lateral movement; reduces attack surface and scopes compliance (e.g. PCI).

### Access control
| Item | Definition |
|---|---|
| **Access control list (ACL)** | Ordered rules permitting/denying traffic or object access (router/firewall rules, file permissions); implicit deny at the end |
| **Permissions** | Rights granted on resources (read/write/execute); assigned per least privilege |

### Application allow list
- Only approved applications may run (default deny). Stronger than a block list (deny list), which only stops known-bad. Also blocks unknown malware and shadow IT.

### Isolation
- Separate a compromised/risky system from the network (quarantine VLAN, air gap, disconnecting an infected host); used in incident containment and for legacy/unsupported systems.

### Patching
- Apply vendor fixes for known vulnerabilities; follow test → deploy → verify; prioritise by severity and exposure (CVSS). Counters known-vulnerability exploitation, not zero-days.

### Encryption
- Protect confidentiality of data at rest, in transit, and in use (disk, file, TLS, VPN); makes stolen data unusable.

### Monitoring
- Continuous logging, SIEM correlation, IDS/IPS, EDR, NetFlow; enables detection of the indicators in 2.4.

### Least privilege
- Give users, processes, and services the minimum access required; limits privilege escalation, insider damage and malware impact. Pair with PAM, just-in-time access, and separation of duties.

### Configuration enforcement
- Maintain systems at an approved baseline: group policy, MDM, configuration management, compliance checks (e.g. NAC posture assessment), auto-remediation of drift. Compare to the secure baseline.

### Decommissioning
- Securely retire assets: sanitise/destroy media (wipe, degauss, shred), remove from inventory/DNS/AD, revoke credentials and certificates, update asset records. Prevents data leakage and orphaned (zombie) systems.

### Hardening techniques
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

### Attack → best mitigation

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

## Most-tested distinctions

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
