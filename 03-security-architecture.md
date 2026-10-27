# Domain 3 — Security Architecture (18%)

> **Note:** AI-generated content, not yet vetted for accuracy. See the README for details.

Objectives 3.1–3.4. Reader assumed to know the basics; this is the exam-framed version.

---

## 3.1 Compare and contrast security implications of different architecture models

### Architecture and infrastructure concepts

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

### Cloud responsibility matrix

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

### Considerations table (by model)

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

### The considerations list (how the exam words them)

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

## 3.2 Given a scenario, apply security principles to secure enterprise infrastructure

### Infrastructure considerations

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

### Network appliances

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

### Port security

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

### Firewall types

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

### Secure communication/access

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

### Selection of effective controls

Match the control to the scenario: need to block in real time → IPS/NGFW; web-app attacks → WAF; secure admin access → jump server + MFA; unknown or unpatchable device → segment/VLAN + ACL; rogue device → 802.1X/NAC; remote workers → VPN/ZTNA/SASE; encrypt data crossing untrusted networks → TLS/IPSec; filter egress/web use → forward proxy. Prefer defense in depth, least privilege, and zero trust (verify explicitly; microsegmentation). Controls must address the stated risk at acceptable cost, and fit failure-mode requirements (availability vs security).

---

## 3.3 Compare and contrast concepts and strategies to protect data

### Data types

| Type | Definition |
|---|---|
| **Regulated** | Governed by law/standard: PII, PHI (HIPAA), financial/cardholder (PCI DSS), GDPR personal data. Breach brings fines/notification. |
| **Trade secret** | Proprietary info giving competitive edge (formulas, algorithms); protected by NDAs, access control. |
| **Intellectual property** | Patents, copyrights, trademarks. |
| **Legal information** | Contracts, case files, privileged communications. |
| **Financial information** | Account data, statements, payment info. |
| **Human-readable** | Plain text people can read directly. |
| **Non-human-readable** | Binary, encoded, database, machine formats; still sensitive. |

### Classifications

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

### States of data

| State | Definition | Primary protections |
|---|---|---|
| **At rest** | Stored on disk, DB, backup, USB | Full-disk/volume (BitLocker, LUKS), file/DB encryption (TDE), access controls, HSM/TPM for keys |
| **In transit / in motion** | Moving across a network | TLS, IPSec, SSH, VPN, WPA3, S/MIME |
| **In use** | Being processed in memory/CPU | Secure enclaves, confidential computing, memory protection, screen locks, DLP; hardest to protect |

> **Exam tip:** Data in use = RAM/CPU; encryption is hardest. Keyword "enclave / confidential computing / TEE" = in use.

### Data sovereignty and geolocation

- **Data sovereignty:** data is subject to the laws of the country where it is stored/collected (GDPR, residency laws). Cloud region choice and backups matter.
- **Geolocation:** physical or logical location of data/users/devices. Used for policy (geofencing, conditional access), and compliance. IP-based location can be spoofed (VPN).

### Methods to secure data

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

### Scenario → method

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

## 3.4 Explain the importance of resilience and recovery in security architecture

### High availability

| Concept | Definition |
|---|---|
| **High availability** | Systems remain operational with minimal downtime; no single point of failure. |
| **Load balancing** | Spreads requests across multiple **active** nodes for performance and availability; nodes typically independent and stateless. |
| **Clustering** | Multiple nodes act as one system sharing state/storage; **failover** to a standby on node failure. Active/active or active/passive. |

> **Exam tip:** Load balancing = distribute work (performance + availability). Clustering = redundancy via failover (availability). "Servers appear as a single system" = cluster.

### Site considerations

| Site | Description | Cost | Recovery time |
|---|---|---|---|
| **Hot** | Fully equipped, live data replication, mirror of production | Highest | Minutes to hours (near zero) |
| **Warm** | Hardware/connectivity in place, data restored from recent backup | Medium | Hours to days |
| **Cold** | Space, power, and connectivity only; bring equipment and data | Lowest | Days to weeks |
| **Mobile site** | Trailer/portable datacenter | Variable | Depends |

Also: **hot/cold aisles** are datacenter cooling, not DR sites. **Reciprocal agreement** = mutual-use with a partner (cheap, unreliable).

> **Exam tip:** Lowest RTO = hot. Cheapest = cold. "Balanced cost and recovery" = warm.

### Resilience concepts

| Concept | Definition |
|---|---|
| **Geographic dispersion** | Spreading sites/data far apart so a regional disaster cannot take out all (but latency, sovereignty). |
| **Platform diversity** | Different OSes, vendors, hardware, and technologies so one vulnerability or failure doesn't hit everything. Related: technology diversity, vendor diversity, crypto diversity, control diversity. |
| **Multi-cloud systems** | Using several cloud providers to avoid lock-in/outage dependence; adds complexity and inconsistent security tooling. |
| **Continuity of operations planning (COOP)** | Plan to keep essential functions running during/after disruption (alternate site, succession, communications, essential records). Often government-framed. |
| **Capacity planning** | Ensuring resources meet demand across **people** (staff/skills for incident and recovery), **technology** (hardware, bandwidth, licenses, cloud scale) and **infrastructure** (facilities, power, cooling, space). |

### Testing

| Test | Definition |
|---|---|
| **Tabletop exercise** | Discussion-based walkthrough of a scenario; no systems touched; cheapest. |
| **Failover test** | Actually switch production to the secondary/redundant system to prove it works. |
| **Simulation** | Scenario-driven exercise that mimics an incident with realistic injects (drill/live-fire like phishing sim or DR drill) without full production impact. |
| **Parallel processing** | Run the recovery/backup system alongside production, processing the same data; production unaffected; compare results. |
| **Walkthrough / checklist** | Review plans for accuracy. |
| **Full interruption** | Shut down production and run on DR; riskiest. |

> **Exam tip:** Tabletop = talk only. Failover = production moves. Parallel = both run at once. Simulation = realistic scenario drill.

### Backups

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

### Power

| Item | Definition |
|---|---|
| **UPS** | Battery bridging short outages (minutes); conditions power (surge, sag); allows graceful shutdown. Online (double-conversion) vs line-interactive vs standby. |
| **Generator** | Fuel-powered long-term backup; startup delay so UPS bridges the gap; fuel supply and testing needed. |
| **Dual power supplies / redundant feeds / PDUs** | Remove power single points of failure. |
| **Managed PDU** | Remote monitoring/control of outlets. |

> **Exam tip:** UPS = short-term, immediate. Generator = long-term, delayed start. They are used together.

---

## Most-tested distinctions

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
