# Ports and Protocols

> **Note:** AI-generated content, not yet vetted for accuracy. See the README for details.

> **Exam tip:** The exam tests "replace the insecure protocol with its secure equivalent" and "which port is this". Know the pairs cold.

## Main table

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

## Quick memorization list (by number)

20/21 FTP, 22 SSH/SCP/SFTP, 23 Telnet, 25 SMTP, 49 TACACS+, 53 DNS, 67/68 DHCP, 69 TFTP, 80 HTTP, 88 Kerberos, 110 POP3, 123 NTP, 137-139 NetBIOS, 143 IMAP, 161/162 SNMP, 389 LDAP, 443 HTTPS, 445 SMB, 465 SMTPS, 500 IKE, 514 syslog, 587 SMTP submission, 636 LDAPS, 853 DoT, 989/990 FTPS, 993 IMAPS, 995 POP3S, 1194 OpenVPN, 1433 SQL Server, 1521 Oracle, 1645/1646 legacy RADIUS, 1812/1813 RADIUS, 3306 MySQL, 3389 RDP, 4500 IPSec NAT-T, 5060/5061 SIP, 5432 PostgreSQL, 6514 syslog TLS.

> **Exam tip:** Port ranges: well-known 0-1023, registered 1024-49151, dynamic/ephemeral 49152-65535. TCP = connection-oriented/reliable; UDP = connectionless (DNS queries, DHCP, TFTP, SNMP, syslog, NTP, RADIUS, IKE).

## TLS versions

| Version | Status | Notes |
|---|---|---|
| SSL 2.0 / 3.0 | Deprecated, broken | POODLE (SSL 3.0), downgrade attacks |
| TLS 1.0 / 1.1 | Deprecated | BEAST, weak ciphers; disable |
| **TLS 1.2** | Acceptable | Needs strong cipher suites (AEAD, ECDHE) |
| **TLS 1.3** | Preferred | Faster handshake, removes legacy ciphers, forward secrecy mandatory, encrypts more of the handshake |

- Certificates (X.509) bind identity to public key; the session key is symmetric, agreed via (EC)DHE.
- **Perfect forward secrecy (PFS):** ephemeral keys per session; compromise of the long-term private key does not expose past sessions.
- **HSTS** forces HTTPS; **certificate pinning** limits trusted CAs; **STARTTLS** upgrades a plaintext connection to TLS in place.

## IPSec

| Concept | Meaning |
|---|---|
| **AH** (Authentication Header, protocol 51) | Integrity + authentication + anti-replay. **No encryption.** Breaks with NAT |
| **ESP** (Encapsulating Security Payload, protocol 50) | Encryption + integrity + authentication. The common choice |
| **Transport mode** | Only the payload is protected; original IP header kept. Host-to-host |
| **Tunnel mode** | Entire original packet encapsulated with a new IP header. Site-to-site and remote access VPNs (gateway-to-gateway) |
| **IKE** (UDP 500) | Negotiates Security Associations (SAs); Phase 1 builds the ISAKMP SA, Phase 2 builds the IPSec SAs |
| **NAT-T** (UDP 4500) | Encapsulates ESP in UDP to cross NAT |

> **Exam tip:** "Needs confidentiality" -> ESP. "Integrity only" -> AH. "Site-to-site" -> tunnel mode. "Host-to-host, payload only" -> transport mode.

## Wireless security

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

## EAP methods (802.1X)

| Method | Client cert? | Server cert? | Notes |
|---|---|---|---|
| **EAP-TLS** | Yes | Yes | Mutual certificate auth; strongest; needs PKI |
| **PEAP** | No | Yes | TLS tunnel then inner auth (MSCHAPv2); username/password |
| **EAP-TTLS** | No | Yes | Tunnelled TLS; supports more inner methods |
| **EAP-FAST** | No (PAC) | Optional | Cisco; uses Protected Access Credential |
| **EAP-MD5** | No | No | Weak; no mutual auth |
| **LEAP** | No | No | Cisco legacy; broken |

## Email authentication

| Mechanism | What it does | How |
|---|---|---|
| **SPF** | Lists which mail servers may send for a domain | DNS TXT record; checks the envelope sender (Return-Path) against sending IP |
| **DKIM** | Message integrity and domain authenticity | Sender signs headers/body with a private key; public key in DNS TXT; signature in header |
| **DMARC** | Policy + reporting that ties SPF/DKIM to the visible From domain | DNS TXT at `_dmarc`; policy `none` / `quarantine` / `reject`; aggregate (rua) and forensic (ruf) reports |
| **S/MIME / PGP** | End-to-end message signing and encryption | Certificates (S/MIME) or web of trust (PGP) |

> **Exam tip:** WPA2 -> CCMP; WPA3 -> exam materials usually say GCMP. If a question pairs WPA3 with GCMP, accept it; WPA3-Personal actually still uses CCMP-128.

> **Exam tip:** SPF = which servers, DKIM = signed and unmodified, DMARC = what to do on failure and report back. All three combat spoofing/phishing; none encrypt message content.
