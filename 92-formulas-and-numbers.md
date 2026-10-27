# Formulas and Numbers

> **Note:** AI-generated content, not yet vetted for accuracy. See the README for details.

## Quantitative risk

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

**Inherent risk** = before controls; **residual risk** = what remains after controls and must be accepted by the risk owner. Accept includes exemption and exception.

Qualitative: likelihood x impact on a heat map/risk matrix. **Risk = threat x vulnerability x impact** (conceptual).

## RTO, RPO, MTTR, MTBF

| Term | Meaning |
|---|---|
| **RTO** | Recovery time objective: target time to restore a service after disruption; must fit within MTD (MTD = RTO + WRT) |
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

## Availability and downtime

| Availability | Downtime / year | Per month (approx.) | Per week |
|---|---|---|---|
| 99% ("two nines") | 3.65 days | 7.3 hours | 1.68 hours |
| 99.9% ("three nines") | 8.76 hours | 43.8 minutes | 10.1 minutes |
| 99.99% ("four nines") | 52.6 minutes | 4.38 minutes | 1.01 minutes |
| 99.999% ("five nines") | 5.26 minutes | 26.3 seconds | 6.05 seconds |

## Backup restore counts

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

## Key lengths and algorithms

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

## CVSS (v3.x / v4.0)

| Rating | Score |
|---|---|
| None | 0.0 |
| Low | 0.1 - 3.9 |
| Medium | 4.0 - 6.9 |
| High | 7.0 - 8.9 |
| Critical | 9.0 - 10.0 |

Base metrics (v3.x): attack vector, attack complexity, privileges required, user interaction, scope, C/I/A impact. v4.0 drops Scope, adds Attack Requirements, and splits impact into vulnerable-system and subsequent-system C/I/A. Severity bands are the same in both. Temporal (v3; "Threat" in v4) and environmental metrics adjust. **EPSS** estimates exploit likelihood. **CVE** = identifier; **CWE** = weakness type; **NVD** = database.

## Password and MFA numbers

| Item | Common value |
|---|---|
| NIST SP 800-63B password guidance | Length over complexity; minimum 8 characters (800-63B-4 recommends at least 15), allow 64+; no forced periodic rotation; block breached/common passwords; no hints or KBA |
| Account lockout | Threshold 3-10 failed attempts; lockout duration or admin reset; ties to throttling |
| Password history | Commonly 5-24 remembered |
| Min/max age | Min age stops rapid cycling through history |
| Entropy | More length is better than more complexity |
| MFA factors | Something you **know**, **have**, **are**, **somewhere you are** (SY0-701's four; older material adds 'something you do') |
| OTP | HOTP (counter-based), TOTP (time-based, usually 30 s window) |
| Biometric errors | FAR (false accept; security risk), FRR (false reject; usability), **CER/EER** = point where FAR = FRR (lower is better) |
| SMS OTP | Weakest MFA delivery (SIM swap, interception) |
| Kerberos clock skew | 5 minutes default |
| Session timeouts | Idle timeout + absolute timeout |

## Incident response phases (SY0-701 exam order)

**Preparation -> Detection -> Analysis -> Containment -> Eradication -> Recovery -> Lessons learned**

(SY0-701 objective 4.8 lists these seven separately.) NIST SP 800-61r2 grouped these into four phases (preparation; detection & analysis; containment, eradication & recovery; post-incident activity). r2 was superseded in 2025 by r3, which maps IR onto the CSF 2.0 functions. Answer exam questions with the seven-step order above.

## Order of volatility (most to least volatile)

1. CPU registers and cache
2. RAM: memory contents, routing table, ARP cache, process table, kernel statistics
3. Temporary file systems / swap
4. Disk (storage)
5. Remote logging and monitoring data
6. Physical configuration, network topology
7. Archival media / backups

Forensics: legal hold, chain of custody, hash (write blocker) before analysis, work on copies, document everything. **Collect memory first.**

## Data classification ladders

| Level (high to low) | Government (US) | Commercial (one common example scheme) |
|---|---|---|
| 1 | Top Secret | Restricted |
| 2 | Secret | Confidential |
| 3 | Confidential | Sensitive / Private / Internal |
| 4 | Unclassified (CUI for controlled unclassified data; replaces FOUO) | Public |

SY0-701 data classification terms: **sensitive, confidential, public, restricted, private, critical** (no fixed order across organisations; see Domain 3 for the exam-framed label definitions). Other terms: PII, PHI, financial, trade secret, intellectual property, regulated; owner (accountable), custodian (day-to-day), steward, controller (decides purposes), processor (handles on behalf of controller), DPO.

## Compliance frameworks and laws

| Name | Covers |
|---|---|
| **PCI DSS** | Payment card data; merchants and processors; 12 requirements; contractual standard, not law |
| **HIPAA** | US healthcare; PHI; Privacy, Security, and Breach Notification Rules |
| **GDPR** | EU/EEA personal data; consent, rights (access, erasure, portability), breach notification within **72 hours**, fines up to EUR 20M or 4% of global annual turnover, whichever is higher |
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
| **SOC 2** | System and Organization Controls (AICPA; formerly Service Organization Controls), trust services criteria; Type I = design at a point in time, Type II = operating effectiveness over a period |
| **CSA CCM / STAR** | Cloud security controls and assurance |
| **MITRE ATT&CK** | Adversary tactics/techniques knowledge base (not a compliance framework) |
| **Diamond Model / Cyber Kill Chain** | Intrusion analysis models |
