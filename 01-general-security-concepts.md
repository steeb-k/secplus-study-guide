# Domain 1 — General Security Concepts (12%)

> **Note:** AI-generated content, not yet vetted for accuracy. See the README for details.

Objectives 1.1–1.4. Smallest domain by weight, but the vocabulary (control types, CIA, zero trust, crypto) is reused in every other domain.

---

## 1.1 Compare and contrast various types of security controls

Two independent axes: **category** (who/what implements it) and **type** (what it does / when it acts). Every control has one of each.

### Categories (how it is implemented)

| Category | Definition (exam framing) | Examples |
|---|---|---|
| Technical | Implemented in systems with technology; also called "logical" controls | Firewall, IDS/IPS, ACLs, encryption, EDR, antivirus, MFA |
| Managerial | Administrative; governs risk through policy and oversight at the planning level | Risk assessments, security policies, pen-test programs, vulnerability-management program, SDLC requirements |
| Operational | Carried out day to day by people (processes), not by a technology alone | Security awareness training, guard duty, change-control procedures, incident-response procedure execution, backups run by staff |
| Physical | Controls that act on the physical world | Fences, locks, bollards, badges, cameras, guards, mantraps |

> **Exam tip:** "Managerial" = plan/policy/assess/oversee. "Operational" = people executing a procedure. If a question says a *policy or risk assessment*, it is managerial; if it says *training or staff carrying out a procedure*, it is operational. A lock is physical even though it is "preventive". Guards are ambiguous: listed under physical security in 1.2, but treated as operational when the stem stresses the person performing a procedure (patrols, checking IDs). Pick the category the stem emphasises.

### Types (what it does)

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

### Category × type example matrix

| | Preventive | Deterrent | Detective | Corrective | Compensating | Directive |
|---|---|---|---|---|---|---|
| **Technical** | Firewall rule, ACL, encryption, MFA, IPS (block mode) | Login warning banner / splash screen | IDS, SIEM alerts, log monitoring, FIM | Restore from backup, EDR isolates host, patch deployment | Network segmentation for unpatchable system, WAF in front of vulnerable app | File-storage or acceptable-use notice pushed to systems telling users where/how to store data |
| **Managerial** | Risk assessment gating deployment, separation-of-duties design | Sanctions/disciplinary policy | Audits, pen tests, vulnerability scan reviews | Incident-response plan lessons learned, corrective action plan | Added management review when SoD is impossible | Security policy, standards, AUP |
| **Operational** | Awareness training, job rotation, onboarding/offboarding procedures | Publicised consequences, security reminders | Guard reviewing logs, user-activity reviews | Incident handling by IR team, backup restoration procedure | Manual review of transactions when automation unavailable | Procedures, SOPs, playbooks |
| **Physical** | Locks, fences, bollards, vestibule, badge reader | "Cameras in use" signs, visible guards, lighting | CCTV, motion/infrared sensors, alarms | Fire suppression, switching to alternate site | Guard stationed at a door whose reader is broken | "Authorized personnel only" signage, visitor-escort rules |

> **Exam tip:** Most matrix cells are judgment calls; the exam asks you to pick the *best* category and type. Anchor on the verb: stops = preventive, warns = deterrent, notices = detective, fixes = corrective, substitutes = compensating, mandates = directive.

---

## 1.2 Summarize fundamental security concepts

### Confidentiality, Integrity, Availability (CIA triad)

| Property | Meaning | Controls | Attack against it |
|---|---|---|---|
| Confidentiality | Only authorized parties can read data | Encryption, access control, data classification | Eavesdropping, data breach |
| Integrity | Data/systems are not altered without authorization; changes detectable | Hashing, digital signatures, FIM, version control | Tampering, MITM modification |
| Availability | Authorized users can access when needed | Redundancy, backups, load balancing, UPS | DoS/DDoS, ransomware |

Related terms: **Non-repudiation** = a party cannot credibly deny having performed an action or sent a message. Achieved with **digital signatures** (plus audit logs and timestamps). Hashing gives integrity only; HMAC gives integrity + authenticity but not non-repudiation (shared key).

> **Exam tip:** "Prove who sent it / sender cannot deny" -> non-repudiation -> digital signature. "Ensure data wasn't modified" -> integrity -> hash. "Keep data secret" -> encryption -> confidentiality.

### Authentication, Authorization, Accounting (AAA)

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

### Gap analysis

Comparing the **current state** to a **desired state/standard/framework** (e.g., NIST CSF, ISO 27001, CIS Controls) to identify what is missing, then planning remediation. Output: list of gaps with remediation plan. Often precedes an audit or certification.

> **Exam tip:** "Compare current controls to a framework/target" -> gap analysis. Not a vulnerability scan (finds technical flaws) and not a risk assessment (assesses likelihood/impact).

### Zero trust

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

### Physical security

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

### Deception and disruption technology

| Technology | Definition |
|---|---|
| Honeypot | Decoy system that looks like a real target to attract and study attackers |
| Honeynet | Network of honeypots simulating an entire environment |
| Honeyfile | Decoy file (e.g., "passwords.xlsx") that alerts when opened or copied |
| Honeytoken | Fake data/credential/record (fake API key, DB row, account) planted to detect misuse or theft; any use is suspicious |

Purpose: early detection, intelligence on TTPs, and distraction/delay. Any interaction with a decoy is by definition suspicious, so false positives are low.

> **Exam tip:** Honeytoken = fake *data/credential*; honeyfile = fake *file*; honeypot = fake *host/service*; honeynet = fake *network*. Tarpit and sinkhole are related disruption techniques but are not in the list here.

---

## 1.3 Explain the importance of change management processes and the impact to security

Change management ensures modifications are requested, assessed, approved, tested, implemented, and documented so security is not degraded. It underpins availability and integrity.

### Business processes impacting security operations

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

### Technical implications

| Item | Concern |
|---|---|
| Allow lists / deny lists | Updating application or IP lists; wrong entries block legit use or permit malware |
| Restricted activities | Some changes need extra authorisation (privileged operations) |
| Downtime | Planned outages affect availability; coordinate with stakeholders |
| Service restart | Brief interruption; sessions dropped; may be needed to apply config |
| Application restart | Same as above, scoped to the application; state lost |
| Legacy applications | Fragile; changes may break; may need compensating controls |
| Dependencies | Components that rely on each other; changing one can break another |

### Documentation

- **Updating diagrams:** network/architecture diagrams must reflect the change.
- **Updating policies/procedures:** keep them in line with new reality.
- Records of approvals, test results, and change logs support audits and rollback.

### Version control

Tracks changes to code, configs, and documents over time (e.g., Git): who changed what and when, ability to revert, branch/merge, and prevent unauthorised/uncontrolled changes. Supports integrity, accountability, and rollback (backout).

> **Exam tip:** Undocumented/unauthorised changes ("shadow changes", config drift) are a security risk; the fix is formal change control plus version control and configuration baselines.

---

## 1.4 Explain the importance of using appropriate cryptographic solutions

### Public key infrastructure (PKI)

System of CAs, certificates, keys, and policies that binds public keys to identities.

| Component | Role |
|---|---|
| Public key | Shared openly; encrypts data or verifies signatures |
| Private key | Kept secret; decrypts or signs |
| Key escrow | Third party holds a copy of keys for recovery (e.g., lost keys, legal access) |
| Key management | Lifecycle: generate, distribute, store, rotate, revoke, destroy |

### Encryption: levels

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

### Encryption: symmetric vs asymmetric

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

### Common algorithms

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

### Key length

Longer keys increase brute-force cost. Rules of thumb: AES-128 is acceptable, AES-256 for high security; RSA 2048 minimum; ECC 256. Symmetric keys are much shorter than asymmetric for the same strength. **Key exchange** (DH/RSA) and **perfect forward secrecy** (ephemeral keys) protect past sessions if a long-term key is compromised.

### Tools

| Tool | Definition (exam framing) |
|---|---|
| TPM (Trusted Platform Module) | Chip on the motherboard that stores keys, measures boot integrity, and enables full-disk encryption (BitLocker), attestation; tied to that device |
| HSM (Hardware Security Module) | Dedicated tamper-resistant appliance/card for generating, storing, and using keys; high-performance crypto; used by CAs and payment systems; FIPS 140 |
| KMS (Key Management System/Service) | Centralised service for creating, storing, rotating, and controlling keys, often cloud-based (and may be backed by HSMs) |
| Secure enclave | Isolated, protected processor area (CPU/SoC) that protects sensitive operations and data even if the OS is compromised (e.g., Apple Secure Enclave, Intel SGX) |

> **Exam tip:** TPM = one device, motherboard, disk encryption/boot. HSM = enterprise key storage, removable/network appliance. KMS = management service. Secure enclave = protects data *in use* / isolated execution.

### Obfuscation

| Technique | Definition | Reversible? |
|---|---|---|
| Steganography | Hiding data inside another file (image, audio, video) so its existence is concealed; security by obscurity | Yes (extract) |
| Tokenization | Replace sensitive value with a random token; the real value is stored in a secure vault; used for PCI (card numbers) | Yes, via vault lookup only |
| Data masking | Replace/hide parts of data (e.g., ****-1234) for display or non-production use | Usually not |

> **Exam tip:** Steganography hides *that* a message exists; encryption hides *what* it says. Tokenization = token has no mathematical relationship to the original (unlike encryption). Masking = test/dev data, display.

### Hashing

One-way function producing a fixed-length digest; same input = same output; tiny change = very different output (avalanche); collision-resistant. Provides **integrity**, not confidentiality. Uses: file integrity, password storage, digital signatures, forensic evidence verification.

### Salting

Random per-user value added to a password before hashing so identical passwords yield different hashes; defeats **rainbow tables** and precomputed attacks. Salt is stored with the hash (not secret). **Pepper** is a secret value stored separately.

### Key stretching

Making brute force expensive by repeating the hash many times (work factor/iterations): **PBKDF2, bcrypt, scrypt** (and Argon2). Slows an attacker much more than a legitimate single login.

> **Exam tip:** Salt = defeats rainbow tables/precomputation. Key stretching = slows brute force/dictionary attacks. Both are used together for password storage.

### Digital signatures

Hash the message, then encrypt the hash with the **sender's private key**; receiver verifies with the sender's **public key**. Provides **integrity, authentication, non-repudiation**. Does not provide confidentiality.

> **Exam tip:** Encrypt for confidentiality: use the *recipient's public key*. Sign for authenticity: use the *sender's private key*. Never the reverse for these goals.

### Blockchain / open public ledger

Distributed, append-only ledger of blocks linked by hashes; each block contains the previous block's hash, so altering one breaks the chain. Consensus across many nodes; transparent and tamper-evident; used for cryptocurrency, provenance, audit trails. Provides integrity and non-repudiation in a decentralised way.

**Open public ledger:** the shared blockchain record itself; anyone can view and verify every transaction, no central authority owns it (transparency + tamper evidence, not confidentiality).

### Certificates

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

### Worked example: TLS handshake (asymmetric then symmetric)

1. **Client Hello:** client sends supported TLS versions, cipher suites, and a random value.
2. **Server Hello + certificate:** server picks a cipher suite and sends its certificate (public key, signed by a CA) and random value.
3. **Client validates the certificate:** checks the chain to a trusted root, validity dates, name match (CN/SAN), and revocation (CRL/OCSP). This authenticates the server.
4. **Key exchange (asymmetric):** with ECDHE, client and server each create ephemeral key pairs and exchange public values; both compute the same **shared secret**. The server signs its ephemeral value with its certificate's private key to prove identity. (In older RSA key exchange, the client encrypts a pre-master secret with the server's public key.)
5. **Derive session keys:** both sides derive identical **symmetric session keys** (e.g., AES-GCM) from the shared secret and random values.
6. **Finished:** each side sends a MAC-verified Finished message; bulk application data is then encrypted with the **symmetric** session key.

Why: asymmetric crypto solves key distribution and authentication but is slow; symmetric crypto is fast for bulk data. ECDHE (ephemeral) gives **forward secrecy**: stealing the server's private key later does not decrypt recorded sessions. TLS 1.3 removes static RSA key exchange and weak ciphers.

---

## Most-tested distinctions

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
