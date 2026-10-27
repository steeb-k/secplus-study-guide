# Domain 4 — Security Operations (28%)

> **Note:** AI-generated content, not yet vetted for accuracy. See the README for details.

Largest domain. Expect many scenario and PBQ items (firewall rules, log analysis, IAM, IR ordering).

---

## 4.1 Given a scenario, apply common security techniques to computing resources

### Secure baselines
- **Establish** the approved secure configuration (CIS Benchmark, vendor guide, DISA STIG), **deploy** it (golden image, GPO, MDM, config management), **maintain** it (re-baseline after approved changes, detect drift).
- Baseline = "what good looks like"; deviation from it = configuration drift = finding.

### Hardening targets

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

### Wireless devices
- **Installation considerations** (the exam's sub-bullets are site surveys and heat maps): AP placement (coverage vs. leakage), channel planning (2.4 GHz: 1/6/11 non-overlapping; 5 GHz has more channels), antenna type/power, PoE, wired backhaul.
- **Site survey:** physically measures RF coverage, interference and dead zones; done before and after deployment.
- **Heat map:** visual overlay of signal strength on a floor plan, output of a site survey. Keyword: "visualize coverage/dead spots" -> heat map.
- Rogue AP detection and WIPS belong here too.

### Mobile solutions
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
| **Cellular** | Carrier network, encrypted to the tower but **outside corporate control/monitoring**; a phone on cellular bypasses corporate firewall/DLP. Risks: rogue base stations (IMSI catchers/stingrays); SIM swapping (attacker social-engineers the carrier to port the number, hijacking SMS codes). Use VPN/ZTNA and MDM. |
| **Wi-Fi** | Untrusted public hotspots, evil twin/rogue AP, on-path attacks. Use WPA3/802.1X on corporate Wi-Fi, always-on VPN elsewhere, disable auto-join. |
| **Bluetooth** | Short-range PAN. Attacks: bluejacking (unsolicited messages), bluesnarfing (data theft), bluebugging (device control). Disable discoverable mode, require pairing PIN, turn off when unused. |
| Others | NFC (centimetres, contactless pay, relay risk), USB/tethering/hotspot (bridges networks, bypasses controls), infrared, point-to-point/ad hoc. Disable unused radios via MDM. |

- Mobile security features: biometrics, lock screen/PIN, remote wipe, full-device encryption, containerization/app sandboxing, geofencing, geotagging controls, content management.

### Wireless security settings
- **WPA3:** Personal uses **SAE** (Simultaneous Authentication of Equals, "Dragonfly") instead of WPA2-PSK, so a captured handshake cannot be brute-forced offline; per-session keys give forward secrecy; **PMF** (protected management frames) mandatory, stopping deauth attacks; Enterprise offers a 192-bit (CNSA, GCMP-256) mode. **OWE** (Opportunistic Wireless Encryption, "Enhanced Open") encrypts open/guest networks without a password.
- **WPA2:** AES-CCMP. **WPA:** TKIP (deprecated). **WEP:** RC4, broken.
- **AAA / RADIUS:** 802.1X port-based access control. Supplicant (client) -> authenticator (AP/switch) -> authentication server (RADIUS). RADIUS = UDP 1812/1813, encrypts only password; TACACS+ = TCP 49, encrypts entire payload, separates AAA, Cisco-origin (device admin). Diameter is RADIUS successor.
- **Cryptographic protocols:** WPA2 = AES-**CCMP**; WPA3 = AES-CCMP (Personal) or **GCMP-256** (Enterprise 192-bit). TKIP and WEP/RC4 are the wrong answers. TLS is used inside EAP methods. Exam framing: questions usually pair **WPA2 → CCMP** and **WPA3 → GCMP**; if GCMP is offered for WPA3, take it.
- **Authentication protocols (EAP family):**

| Method | Server cert | Client cert | Tunnel | Notes |
|---|---|---|---|---|
| EAP-TLS | Yes | **Yes** (mutual) | TLS | Strongest; requires PKI on every client |
| PEAP | Yes | No | TLS tunnel protects inner (MS-CHAPv2) | Microsoft/Cisco/RSA; username+password inside tunnel |
| EAP-TTLS | Yes | No (optional) | TLS tunnel | Like PEAP; supports more inner methods (PAP, CHAP) |
| EAP-FAST | Optional (PAC normally replaces it) | No | Protected Access Credential tunnel | Cisco; replaced LEAP; no client cert, PAC instead |
| LEAP | - | - | None | Cisco legacy, crackable, avoid |

> **Exam tip:** "Certificates on both client and server" = EAP-TLS. "Cisco, no certificates, PAC" = EAP-FAST. "Tunnel + password only client" = PEAP/EAP-TTLS.

- **WPS** (PIN-based) is brute-forceable: disable. **Captive portal** = guest web auth. **Open network + OWE** for guests.

### Application security
- **Input validation:** whitelist/allow-list expected type, length, format, range on the server side; stops injection and overflows. Client-side validation alone is not security.
- **Secure cookies:** `Secure` (HTTPS only), `HttpOnly` (not readable by JavaScript; stops XSS cookie theft), `SameSite` (mitigates CSRF).
- **Static code analysis (SAST):** analyzes source/binaries without running; finds flaws early. **Dynamic analysis (DAST)/fuzzing:** tests the running app with malformed input.
- **Code signing:** digital signature on code proves publisher identity and integrity (not that it is bug-free).
- Also: secure coding practices, manual code review, dependency/package scanning.

### Sandboxing
Run untrusted code/files/apps in an isolated environment with restricted access to host (malware detonation, browser tabs, mobile apps, containers). Contains damage; used for analysis.

### Monitoring
Continuous collection of logs and telemetry from hardened resources (SIEM, EDR, FIM, config-compliance scans) so baseline drift, attacks and policy violations are detected quickly. Hardening without monitoring cannot show that a baseline is still in place (see 4.4).

---

## 4.2 Explain the security implications of proper hardware, software, and data asset management

- **Acquisition/procurement process:** vetted vendors, security requirements in contracts, supply chain risk review, approved purchase channels, ownership documented at purchase.
- **Assignment/accounting:**
  - **Ownership:** every asset has a named owner accountable for it.
  - **Classification:** asset labeled by sensitivity/criticality; drives handling and protection.
- **Monitoring/asset tracking:**
  - **Inventory:** authoritative list of hardware, software, data (CMDB). You cannot protect what you do not know exists; unknown assets = shadow IT.
  - **Enumeration:** discovering and listing assets (network scans, agents, NAC).
  - Also tag/barcode/RFID, lifecycle tracking, license tracking.
- **Disposal/decommissioning:**
  - **Sanitization:** make data unrecoverable, normally so the media can be reused (overwrite, cryptographic erase, ATA/NVMe secure erase for SSDs). Standard: NIST SP 800-88 (clear, purge, destroy).
  - **Destruction:** physically destroy media (shred, pulverize, incinerate, disintegrate). Required for highest sensitivity or non-sanitizable media. **Degaussing** (strong magnetic field) erases magnetic media; it also wipes an HDD's servo tracks, so the drive is unusable afterwards (tape survives). Useless on SSDs/flash.
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

## 4.3 Explain various activities associated with vulnerability management

### Identification methods
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

### Analysis
- **Confirmation:** validate findings before acting. **False positive:** scanner reports a vuln that does not exist. **False negative:** scanner misses a real vuln (worse, because nobody fixes it). True positive = real and reported. Reduce false positives with credentialed scans and updated plugins; confirm by manual check or a second tool.
- **Prioritization and severity:** **CVSS** scores severity (not risk).

| CVSS v3.x score | Severity |
|---|---|
| 0.0 | None |
| 0.1 – 3.9 | Low |
| 4.0 – 6.9 | Medium |
| 7.0 – 8.9 | High |
| 9.0 – 10.0 | Critical |

- **CVE:** standardized identifier for a publicly known vuln (CVE-YYYY-NNNN, four or more digits, e.g. CVE-2021-44228). NVD enriches with CVSS. **CWE** = weakness type. CVSS = how severe; CVE = what/which.
- **Vulnerability classification:** by type/category (e.g., misconfiguration, zero-day, injection, outdated software).
- **Exposure factor:** % of asset value lost if exploited (feeds SLE).
- **Environmental variables:** your specifics: internet-facing or not, compensating controls, data on system.
- **Industry/organizational impact:** regulated data, business criticality, reputational effect.
- **Risk tolerance/appetite:** how much residual risk leadership accepts; drives remediation priority and acceptance.
- Prioritize by: severity x exploitability (known exploit in the wild, EPSS) x asset criticality x exposure.

### Vulnerability response and remediation
- **Patching:** primary fix; test in staging, schedule, deploy, verify.
- **Insurance:** risk transfer for residual risk (does not remove vuln).
- **Segmentation:** isolate vulnerable system when it cannot be patched.
- **Compensating controls:** alternative control reducing risk when primary fix unavailable (WAF, IPS virtual patch, extra monitoring).
- **Exceptions and exemptions:** both are documented, approved forms of risk acceptance. An exception is a time-boxed deviation with compensating controls; an exemption releases a system from the requirement (see 5.2).

### Validation of remediation
- **Rescanning:** confirm vuln gone. **Audit:** verify process/config. **Verification:** manual confirmation that the fix works and nothing broke.

### Reporting
Communicates findings: severity, affected assets, trends, remediation status, SLAs to technical staff and management. Tailored per audience (exec vs. engineers).

> **Exam tip:** Scanner says vulnerable but admin proves not = false positive. Scan "identifies", pen test "exploits". CVSS score 9.8 = Critical. "Cannot patch legacy system" -> segmentation / compensating control / documented exception.

---

## 4.4 Explain security alerting and monitoring concepts and tools

### Monitoring computing resources
- **Systems:** hosts, servers, endpoints: CPU, memory, disk, processes, logons, service and patch state (agents, EDR, OS logs).
- **Applications:** application logs, errors, authentication events, API calls, transactions, response time.
- **Infrastructure:** network devices, firewalls, hypervisors, cloud control plane, power/HVAC (SNMP, NetFlow, firewall and cloud audit logs).

### Activities
- **Log aggregation:** centralize logs from many sources into one place (SIEM) for correlation.
- **Alerting:** notification when events match rules/thresholds.
- **Scanning:** periodic vuln/compliance/discovery scanning.
- **Reporting:** dashboards and periodic summaries for ops and compliance.
- **Archiving:** retain logs long-term (compliance, forensics), integrity-protected, per retention policy.
- **Alert response and remediation/validation:**
  - **Quarantine:** isolate the host/file/user from the network.
  - **Alert tuning:** adjust thresholds/rules to cut false positives (alert fatigue) while not creating false negatives.

### Tools
- **SCAP (Security Content Automation Protocol):** NIST specification (SP 800-126) that bundles open standards (XCCDF checklists, OVAL checks, CPE/CCE naming, CVE identifiers, CVSS scores) so scanners can check configuration compliance and vulnerabilities automatically. **Benchmarks:** CIS/STIG configuration checklists used with SCAP.
- **Agents vs. agentless:** agent = software on endpoint, works off-network, richer data, deployment overhead. Agentless = remote scan/WMI/API, no install, less depth, needs network access/creds.
- **SIEM:** aggregates, normalizes, correlates logs, alerts, dashboards, retention. (SOAR then automates the response.)
- **Antivirus/anti-malware:** signature/heuristic/behavior detection on endpoint.
- **DLP:** detect/block sensitive data leaving (email, USB, cloud, print).
- **SNMP traps:** unsolicited alerts from managed devices to the NMS (UDP 162; polling uses 161). SNMPv3 adds auth+encryption.
- **NetFlow:** flow metadata (src/dst IP, ports, bytes, time), not payloads. Detects exfiltration, anomalies, top talkers. (sFlow, IPFIX similar.)
- **Vulnerability scanners:** Nessus, OpenVAS, Qualys.

> **Exam tip:** "Who talked to whom and how much, without content" -> NetFlow. "Device pushes alert to monitoring server" -> SNMP trap. "Correlate logs from many systems" -> SIEM. Too many false alarms -> tuning.

---

## 4.5 Given a scenario, modify enterprise capabilities to enhance security

### Firewall
- **Rules / access lists:** ordered, top-down, first match wins, **implicit deny** at the end. Elements: source, destination, port, protocol, action (allow/deny). Put specific rules before general; deny-all last.
- **Ports/protocols:** match by service port; block unneeded ones.
- **Screened subnet (DMZ):** network segment between untrusted outside and internal, hosting public-facing servers; two firewalls or three-legged firewall.
- Types: stateless (packet filter), stateful (tracks sessions), NGFW (app-aware, IPS, TLS inspection), WAF (HTTP/S layer 7, protects web apps from SQLi/XSS).

Example ACL reading:
```
1 permit tcp any host 10.0.1.10 eq 443       # allow HTTPS to web server
2 permit tcp 10.0.2.0/24 10.0.1.0/24 eq 22   # allow SSH from admin net to server net
3 deny ip any any                            # implicit/explicit deny
```

### IDS/IPS

| | IDS | IPS |
|---|---|---|
| Placement | Out of band (SPAN/TAP) | Inline |
| Action | Detect, alert | Detect and block |
| Failure effect | None on traffic | Fail-closed = outage (traffic blocked); fail-open = traffic flows uninspected |

- **Trends:** reviewing IDS/IPS alert data over time (top signatures, sources, targets, volume changes) to spot campaigns, tune rules and adjust defenses; most products show trend dashboards. Exam framing: "what is changing" vs a single alert.
- **Detection methods:** signature-based (known patterns; needs updates; misses zero-days), anomaly/behavior-based (baseline deviations; catches novel; more false positives), heuristic.
- **Signatures:** pattern definitions for known attacks; must be updated continuously (vendor feeds), tuned to the environment, and custom signatures can be written (Snort/Suricata rules). Out-of-date signatures = false negatives.
- Network (NIDS/NIPS) vs. host (HIDS/HIPS).

### Web filter

| Item | Exam-framed definition |
|---|---|
| **Agent-based** | Filtering software on each endpoint; policy follows the device **off-network** (remote/roaming users) without backhauling traffic. Must be deployed and kept updated on every device. |
| **Centralized proxy** | All web traffic passes a forward proxy/secure web gateway on the network (or in the cloud); one place to enforce, cache and log. Only covers traffic that goes through it. |
| **URL scanning** | Inspects requested URLs (and often page content) against threat lists and policy before allowing the request. |
| **Content categorization** | URLs/sites grouped into categories (gambling, social media, malware, adult); policy allows/blocks per category instead of per site. |
| **Block rules** | Explicit allow/deny entries by URL, domain, category, file type or keyword; override categorization. |
| **Reputation** | Sites scored (trustworthy, suspicious, malicious; newly registered domains score low) from threat intel; block below a threshold. |

> **Exam tip:** "Filtering must work when laptops are at home without VPN" -> agent-based. "Single point to inspect all outbound web traffic" -> centralized proxy. "Block all gambling sites" -> content categorization.

### Operating system security
- **Group Policy (Windows AD):** central enforcement of security settings (password policy, lockout, software restriction, AppLocker, firewall) on OUs/domains.
- **SELinux:** Security-Enhanced Linux, kernel-level **mandatory access control (MAC)** using security labels/contexts on subjects and objects; even root is constrained by policy. Modes: enforcing, permissive (log only), disabled. AppArmor is a path-based alternative.

> **Exam tip:** Windows domain-wide settings -> Group Policy (GPO). Linux least privilege via mandatory labels -> SELinux.

### Implementation of secure protocols
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
| DNS | UDP/TCP 53 | DNSSEC (integrity only) / DoH / DoT | 53 / TCP 443 / TCP 853 |
| TFTP | UDP 69 | SFTP/SCP | 22 |
| RDP | TCP/UDP 3389 | via VPN/RD Gateway | |
| Syslog | UDP 514 | Syslog over TLS | 6514 |
| NTP | UDP 123 | NTS | UDP 123 (NTS-KE on TCP 4460) |
| SQL/others | | TLS-wrapped | |

Others to know: DHCP 67/68, Kerberos 88, SMB 445, RADIUS 1812/1813, TACACS+ 49, IPsec IKE UDP 500 (NAT-T 4500), NetBIOS 137-139.

> **Exam tip:** Secure version = same service wrapped in TLS/SSH. Port questions: "encrypted email retrieval" 993/995; "secure remote shell" 22; "directory over TLS" 636.

### DNS filtering
Block resolution of malicious/unwanted domains at the resolver (threat-intel categories, newly registered domains). Works for any device using the resolver; stops C2 callbacks and phishing before connection. Complements DNSSEC (which provides authenticity of records, not filtering).

### Email security
- **SPF (Sender Policy Framework):** DNS TXT record listing the servers authorized to send for a domain. Checks sending IP.
- **DKIM (DomainKeys Identified Mail):** sending server signs message headers/body with a private key; receivers verify via the public key in DNS. Proves integrity and domain origin.
- **DMARC:** DNS policy built on SPF and DKIM; requires alignment with the From domain; tells receivers what to do on failure (none / quarantine / reject) and sends reports back to the domain owner.
- **Gateway (email security gateway):** inline filter (spam, phishing, malware attachments, URL rewriting, DLP, sandboxing) before mail reaches the mailbox.

Fit together: SPF = "which IPs may send", DKIM = "message is signed and unaltered", DMARC = "policy + reporting: a message passes if SPF or DKIM passes and aligns with the From domain; the policy (none / quarantine / reject) applies only when neither does".

> **Exam tip:** Spoofed sender domain -> SPF/DKIM/DMARC. "Policy: reject unauthenticated mail and receive reports" -> DMARC. "Digital signature on message headers" -> DKIM.

### File integrity monitoring (FIM)
Baselines hashes of critical OS files, binaries, registry keys and configs, then alerts on unauthorized change (detects tampering, rootkits, web defacement, config drift). Examples: Tripwire, OSSEC/Wazuh, EDR/AV-suite FIM modules. (Windows SFC only verifies and repairs system files on demand; it is not FIM.) Required by PCI DSS. Keyword: "detect changes to system files".

### DLP
Classifies and inspects data in use (endpoint), in motion (network/email) and at rest (storage); blocks, quarantines, encrypts, or alerts. Keyword: "prevent SSNs/credit cards from leaving".

### Network access control (NAC)
Checks device identity and posture (patch level, AV, config) before granting access (802.1X); non-compliant devices sent to a quarantine/remediation VLAN or denied. Posture agents: **persistent** (permanently installed), **dissolvable** (downloaded, runs once, removes itself), or **agentless** (checks via AD/remote query). Keyword: "check health of device before it joins the network" -> NAC.

### Endpoint detection and response (EDR) / XDR
- **EDR:** continuous endpoint telemetry, behavioral detection, investigation, isolation and rollback/remediation.
- **XDR:** extends across endpoint, network, cloud, email, identity into one correlated detection and response platform.
- **MDR** = outsourced EDR/XDR service.

### User behavior analytics (UBA/UEBA)
Uses machine learning to baseline normal user (and, in UEBA, entity: hosts, apps, service accounts) behavior and flags anomalies (impossible travel, unusual hours, abnormal data volumes, first-time access to a sensitive share); finds compromised accounts and insider threats that signatures miss. Often a SIEM/XDR feature.

---

## 4.6 Given a scenario, implement and maintain identity and access management

### Provisioning / deprovisioning user accounts
Create accounts with correct least-privilege rights on hire/role change; **deprovision** (disable, then remove) immediately on termination. Orphaned and dormant accounts are findings. Automate via HR-driven workflows.

### Permission assignments and implications
Grant by role/group, review regularly (access recertification), watch for privilege creep (accumulated rights after transfers) and separation of duties violations.

### Identity proofing
Verify a person is who they claim before issuing credentials (documents, in-person, knowledge checks); precedes account creation. NIST 800-63 IALs.

### Federation
Trust between separate organizations/IdPs so users authenticate once at home IdP and access partner resources (SAML/OIDC).

### Single sign-on (SSO)
One authentication grants access to multiple systems.

| Protocol | Purpose | Format / notes |
|---|---|---|
| LDAP | Directory access/query (AD); authentication binds | TCP 389, LDAPS 636 |
| OAuth 2.0 | **Authorization** (delegated access via tokens; "allow app to access my photos") | Access tokens, JSON/REST |
| SAML | **Authentication + authorization** federation for web SSO, enterprise | XML assertions; IdP <-> SP |
| OpenID Connect (OIDC) | **Authentication** layer on top of OAuth 2.0 ("Sign in with Google") | JWT ID token |
| Kerberos | Ticket-based SSO in AD | UDP/TCP 88, timestamps (clock skew) |

> **Exam tip:** XML + enterprise federation -> SAML. "Authorize third-party app without sharing password" -> OAuth. "Social login/authentication" -> OIDC. OAuth is authorization, not authentication.

### Interoperability
Standards-based integration so IAM systems work across vendors, platforms and cloud (SAML, SCIM for provisioning, OIDC).

### Attestation
Periodic confirmation by managers/owners that users' access remains appropriate (access reviews); also hardware/software attestation proving a system state (e.g., TPM measured boot).

### Access controls

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

### Multifactor authentication (MFA)
- **Implementations:**
  - **Biometrics:** fingerprint, face, iris, retina, voice, vein. Errors: FAR (false acceptance, a security failure), FRR (false rejection, a usability problem); CER/EER = where they cross, lower is better.
  - **Hard authentication token:** physical device generating OTPs (key fob showing a TOTP/HOTP code) or smart card.
  - **Soft authentication token:** OTP generated by an authenticator app (software version of the key fob). Codes **delivered** out of band by SMS/email/push are a separate category; SMS is weakest (SIM swap, interception).
  - **Security keys:** USB/NFC/Bluetooth hardware keys (FIDO2/WebAuthn, U2F) doing public-key challenge/response; phishing-resistant.
  - TOTP = time-based (30-second codes); HOTP = counter/event-based (valid until used).
- **Factors (SY0-701 lists four):** something you **know** (password, PIN, pattern), something you **have** (token, smart card, phone), something you **are** (biometric), **somewhere you are** (location: GPS, IP geolocation). Older material adds something you **do** (gait, typing rhythm, signature); treat it as a behavioral attribute if it appears. Two passwords or password + security question is not MFA (same factor).

> **Exam tip:** Smart card + PIN = have + know (MFA). PIN + password = single factor. Push fatigue/MFA bombing = attack against push MFA; number matching mitigates.

### Password concepts
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

### Privileged access management (PAM)
- **Just-in-time (JIT) permissions:** elevate only when needed, expire automatically (no standing privilege).
- **Password vaulting:** privileged credentials stored in vault, checked out, rotated, session recorded.
- **Ephemeral credentials:** short-lived, auto-generated credentials (temporary accounts/tokens) created for one session or task and destroyed afterwards, so nothing persistent can be stolen.
- Also: session monitoring, approval workflows, break-glass accounts.

---

## 4.7 Explain the importance of automation and orchestration related to secure operations

**Automation** = a task runs without human action. **Orchestration** = coordinating many automated tasks/tools across systems into a workflow (SOAR playbooks).

### Use cases of automation and scripting

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

### Benefits

| Benefit | Meaning |
|---|---|
| **Efficiency/time saving** | Repetitive tasks done in seconds, not hours. |
| **Enforcing baselines** | Every system configured the same way; drift auto-corrected. |
| **Standard infrastructure configurations** | Templates produce identical, known-good builds. |
| **Scaling in a secure manner** | Growth without proportional staff or loss of control. |
| **Employee retention** | Less tedious work reduces burnout and turnover. |
| **Reaction time** | Machine-speed response (isolate host, block IP) shortens attacker dwell time. |
| **Workforce multiplier** | Each analyst covers more; small team does the work of a larger one. |

### Other considerations

| Consideration | Meaning |
|---|---|
| **Complexity** | Automation adds moving parts that must be designed, understood and debugged. |
| **Cost** | Tools, licenses, integration and development time. |
| **Single point of failure** | If the automation platform fails or is compromised, every dependent process fails with it. |
| **Technical debt** | Quick scripts that are never maintained or documented become fragile liabilities. |
| **Ongoing supportability** | Someone must maintain scripts as systems, APIs and staff change. |

> **Exam tip:** Benefits list answers "why automate". Risk list: bad automation can propagate errors at machine speed; compromised automation account = broad blast radius. Keep humans in the loop for high-impact actions.

---

## 4.8 Explain appropriate incident response activities

### Process (SY0-701 order)
1. **Preparation:** IR plan, policy, team/roles, contact lists, tooling, playbooks, training, communication plan, jump bag.
2. **Detection:** identify potential incident via alerts, users, threat intel (IoCs).
3. **Analysis:** validate (true vs. false positive), scope, classify severity, determine impact, prioritize.
4. **Containment:** limit spread (isolate, segment, disable accounts); short-term vs. long-term; choose containment actions that preserve evidence (isolate rather than power off; image before rebuilding).
5. **Eradication:** remove root cause (malware, persistence, attacker accounts, vulnerability).
6. **Recovery:** restore from clean backups, rebuild, validate, return to production, heightened monitoring.
7. **Lessons learned:** post-incident review, improve plan, controls and documentation.

> **Exam tip:** Order matters on the exam. Containment before eradication before recovery. "Isolate the infected host" = containment. "Reimage / remove malware" = eradication. "Restore services" = recovery. "After-action meeting" = lessons learned. Do not power off a compromised system (loses volatile evidence); isolate it.

### Training
IR team members get role-specific training (tools, playbooks, evidence handling, communication); all staff get awareness training on recognizing and **reporting** incidents; managers/executives learn decision and notification responsibilities. Refresh regularly and after plan changes.

### Testing
- **Tabletop exercise:** discussion-based walk-through of a scenario around a table; no systems touched; cheapest.
- **Simulation:** hands-on realistic exercise (e.g., simulated phishing, red/purple team, live drill) exercising actual tooling and procedures.
- Also: walkthrough, parallel/failover testing for continuity.

### Root cause analysis (RCA)
Find the underlying cause (not just symptom) so recurrence is prevented (5 Whys, fishbone). Happens during/after the incident, feeds lessons learned.

### Threat hunting
Proactive, hypothesis-driven search for threats already inside that evaded detection; uses threat intel, IoCs, TTPs, and anomalies. Assumes breach. Contrast: detection is reactive to alerts.

### Digital forensics
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

## 4.9 Given a scenario, use data sources to support an investigation

### Log data

| Log source | Question it answers |
|---|---|
| Firewall logs | What traffic was allowed/blocked? Which IPs/ports did a host contact? |
| Application logs | What did the app do? Errors, user actions, failed transactions |
| Endpoint logs | What happened on this host? Process starts, logons, changes |
| OS-specific security logs (Windows Security, Linux auth.log) | Who logged on/failed, privilege use, account changes |
| IPS/IDS logs | Which signature fired? What attack was detected/blocked? |
| Network logs (router, switch, flow) | What path/volume/protocols moved across the network? |
| Metadata (file, email headers, web, mobile) | Who created/sent/modified, when, from where, device/geo |

### Data sources
- **Vulnerability scans:** what weaknesses existed on the affected system?
- **Automated reports:** summarized, scheduled results from tools.
- **Dashboards:** real-time visual status and trends.
- **Packet captures (pcap):** full content of traffic; what exactly was sent? (Wireshark, tcpdump); most detail, large storage.

> **Exam tip:** "Which user account logged in and when" -> authentication/OS security log. "Which hosts talked to the C2 IP" -> firewall/NetFlow/DNS logs. "Exact payload" -> packet capture. "Who sent the email and from which server" -> email header metadata. "What attack signature matched" -> IPS log. Sort out sequence with synchronized time (NTP).

---

## Most-tested distinctions

- **Site survey vs. heat map:** survey is the activity; heat map is its visual signal-strength output.
- **BYOD / COPE / CYOD / COBO:** employee-owned / company-owned + personal use / pick from a list / business only.
- **EAP-TLS vs. PEAP vs. EAP-FAST:** client+server certs / server cert only + inner password / PAC, no certs.
- **RADIUS vs. TACACS+:** UDP 1812/1813, password-only encryption vs. TCP 49, full encryption, separate AAA.
- **WPA3-SAE (exam: GCMP):** replaces PSK handshake, resists offline guessing; OWE encrypts open networks.
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
