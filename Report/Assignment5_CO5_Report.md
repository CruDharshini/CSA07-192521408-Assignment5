# SIMATS ENGINEERING
## Department of Information Technology
## CSA07 – Computer Networks
# Assignment 5 – CO5
### Measuring Network Performance and Securing Applications

**Student Name:** Dharshini  
**Register Number:** 192521408  
**Department:** Information Technology  
**Faculty:** Dr. Sivachandar K  
**Academic Year:** 2026–2027  
**Total Marks:** 50  
**GitHub:** https://github.com/CruDharshini/CSA07-192521408-Assignment5

---

# Part A – Design

## A1 – Where Does the Delay Come From? (7 marks)

A 1,500-byte packet contains 12,000 bits. At 100 Mbps, transmission delay is 12,000/100,000,000 = 0.12 ms. Assuming fibre propagation speed 2×10^8 m/s, 2,000 km gives 10 ms propagation delay. Three routers add 3×0.5 = 1.5 ms queuing and 3×0.1 = 0.3 ms processing. Total = 0.12+10+1.5+0.3 = **11.92 ms**. Propagation is the largest component. At 1 Gbps, transmission becomes 0.012 ms and total becomes 11.812 ms, an improvement of only 0.108 ms. Therefore, upgrading bandwidth alone does not significantly reduce this path delay.

For a 1 Gbps link and 80 ms RTT, BDP = 1,000,000,000×0.08 = 80,000,000 bits = 10 MB. A 64 KiB TCP window contains 524,288 bits and limits throughput to 524,288/0.08 = **6.55 Mbps**. A larger TCP receive window/window scaling is needed to utilise the link.

Targets: interactive video <150 ms delay, <30 ms jitter and <1% loss; voice <150 ms, <30 ms jitter and <1% loss; recorded video prioritises throughput and reliable delivery; email tolerates seconds; downloads use available bandwidth. Ping measures RTT/loss, traceroute path, iperf3 throughput, Wireshark packet-level behaviour, SNMP utilisation and Packet Tracer/NS-3 controlled scenarios. Active measurement injects probes; passive measurement observes real traffic. Passive monitoring can show existing traffic volume and observed packet behaviour but may miss idle-path performance and one-way delay without synchronised clocks.

## A2 – Follow the Application Protocols (5 marks)

SMTP sends EHLO, MAIL FROM, RCPT TO, DATA, message body, a dot terminator and QUIT. Typical replies are 220 greeting, 250 command accepted, 354 start mail input and 221 closing. POP3 configured to delete after download can remove mail after the first device downloads it. IMAP keeps messages on the server and synchronises folders/read state across phone, laptop and lab PC.

Active FTP asks the server to initiate a data connection back to the client, which is commonly blocked by NAT/firewalls. Passive FTP lets the client initiate both connections. SFTP over SSH and HTTPS over TLS encrypt authentication and content. SNMP GET reads interface counters from an agent; a TRAP asynchronously notifies the manager of an event such as linkDown. SNMPv3 is preferred. Browser Developer Tools timings to inspect include DNS lookup, connection, TLS, TTFB/waiting and content download.

For a 50-message mailbox with 2 KB per message preview, message content is approximately 100 KB before protocol overhead. Webmail additionally downloads page resources, while IMAP can fetch headers first and retrieve bodies/attachments on demand. Both can be encrypted; central webmail can simplify endpoint control.

## A3 – Peer-to-Peer, VoIP and Overlays (5 marks)

A 4 GB package is 32 Gbits. Client–server sends 20 copies, totalling 640 Gbits. At a 100 Mbps server upload, minimum distribution time is 6,400 seconds (106.7 minutes). For ideal P2P, the distribution lower bound is max(F/u_server, N×F/(u_server+sum peer upload), F/min download). Values are 320 s, 1,280 s and 640 s, so the ideal bound is **1,280 s (21.3 minutes)**. This assumes all centres upload at 20 Mbps and piece exchange is efficient; NAT restrictions, peer availability and overhead can reduce the benefit.

G.711 uses 64 kbps and 20 ms packets: 50 packets/s. Payload is 160 bytes; with 40 bytes IP/UDP/RTP headers, packet size is 200 bytes. Rate is 200×8×50 = **80 kbps per direction**, so a 2 Mbps link theoretically supports 25 calls per direction before additional overhead and reserve. SIP establishes/manages sessions; RTP carries media. A CDN caches content near users to reduce origin load and long-haul delay; a VPN creates an encrypted logical network over the internet.

A 1 Gbps CDN edge serving a centre whose download is 50 Mbps is limited by the centre link: 32 Gbits/50 Mbps = 640 s per package. All 20 regions can download concurrently from their respective edges, so the slowest centre completes in 640 s, assuming each edge already has the package. CDN costs include edge capacity and content synchronisation, but improves availability and reduces origin load. P2P reduces central upload demand but relies on participating peers.

## A4 – Find the Hole in the Firewall (4 marks)

A TLS certificate authenticates the server domain through a trusted certificate chain. The handshake negotiates cryptographic parameters and session keys. A café Wi-Fi observer may see metadata such as IP addresses, timing and volume, but cannot normally read or alter authenticated HTTPS content.

Firewall rules use first-match order. In the question, allowing TCP/22 from any source before denying TCP/22 makes the deny rule unreachable and exposes SSH publicly; the later trusted-source allow rule is also shadowed. Correct order is allow TCP/22 from 10.1.0.0/16, deny other TCP/22, allow TCP/443, allow UDP/53 only if DNS is required, then deny all. A stateless filter evaluates each packet; a stateful firewall tracks sessions; an application proxy inspects application-layer requests and can block malicious HTTP patterns at added processing delay.

## A5 – How Easy Is It to Take the Site Down? (4 marks)

A 1,024-entry half-open queue with a 60-second timeout fills at 1,024/60 = **17.07 half-open SYNs per second** in the idealised steady state. SYN cookies avoid allocating full connection state until the client returns a valid ACK. DNS amplification is difficult to block at the victim because many distributed resolvers send spoofed-source responses and the incoming link may saturate.

Use SYN cookies and connection rate limits for SYN floods; upstream scrubbing, anti-spoofing and DNS response-rate limiting for DNS amplification; CDN/WAF, caching and application rate limits for HTTP floods. Four independent identical queues provide 4,096 entries, or 68.27 SYN/s at a 60-second hold time, but this only quadruples a finite queue and does not protect the shared link. Capacity alone is not a complete DDoS defence.

---

# Part B – Implementation and Experimental Investigation

## B1 – Measure a Real Network (7 marks)

Run ping and traceroute to three approved servers at morning, afternoon and evening. Record RTT minimum/average/maximum, jitter and loss. Run iperf3 TCP and UDP tests between two authorised machines over wired and wireless connections. Capture an authorised voice/video stream or controlled RTP test in Wireshark and analyse packet sequence, loss, delay, jitter and bitrate. Compare all results with A1.3 targets.

The supplied trace program analyses the assignment's example data: 20% packet loss, 42.9 ms average one-way delay, 6.6 ms jitter and 345.9 kbps throughput. This is a provided sample trace, not a measurement from the student's network. Actual B1 results must be entered in TaskB1/evidence/measurement_table.csv.

## B2 – Simulate Under Varying Conditions (5 marks)

Build a regional-centre-to-company-server model in Packet Tracer or NS-3. Vary bandwidth, delay and users; add background file transfer and repeat with voice priority. Record throughput, delay and loss for each case. The Python script in TaskB2 provides a simple repeatable analytical model to plan comparisons, but its output is not claimed as Packet Tracer/NS-3 measurement. NS-3 offers packet-level timing/queue detail; Packet Tracer is easier for visual device configuration.

## B3 – Performance Under Stress and Attack (8 marks)

In an isolated lab, apply 50/150/300 ms delay and 1/5/10% loss using tc netem or simulator settings. Measure TCP throughput and voice quality at each point. Compare small and large TCP windows against the 10 MB BDP calculated in A1.2. Apply corrected firewall rules and verify allowed HTTPS/DNS and trusted SSH while blocking untrusted SSH. Compare local test-server response under a conservative rate limit. Never attack a public site or shared network.

Strict priority can protect voice delay but may starve downloads if unbounded. Weighted fair queuing protects other classes but can add delay under congestion. A bounded EF voice queue plus fair scheduling for remaining traffic is a balanced choice.

## B4 – Final Engineering Decision (5 marks)

For twice the users, estimate offered load as twice the measured peak demand. If current utilisation is already above 50%, doubling traffic may exceed link capacity and cause queueing/loss. For overseas classes, compare measured RTT to India and a regional edge; approximate one-way improvement as half the RTT difference. Verify that HTTPS, DNS and approved services still work at doubled load while untrusted SSH and abusive request rates remain blocked.

Recommended changes are CDN/edge caching for recorded lectures and course packages, regional media servers/relays for overseas live classes, QoS for voice/video, WAN capacity based on peak measurements, and stateful firewall/WAF/SYN-cookie/upstream scrubbing protection. Regional servers reduce delay but add synchronisation and operational cost; justify them using measured RTT improvement.

---

## Conclusion

Network quality must be evaluated using delay, jitter, loss, throughput and utilisation rather than connectivity alone. The calculations identify propagation and TCP-window limits; protocol analysis supports secure mail/file transfer; P2P/CDN reduce content distribution bottlenecks; firewall ordering closes public SSH exposure; and layered DDoS controls are more effective than buying capacity alone. Final engineering choices must be checked against the student's own real-network and simulator measurements.

## Evidence still to add after local execution

- OS and tool versions
- Three-time-of-day ping/traceroute and iperf3 outputs
- Wireshark capture and RTP analysis
- Packet Tracer/NS-3 project and run results
- tc netem measurements and safe local firewall/rate-limit test outputs
- Screenshots and interpretation tables

Do not describe sample calculations or supplied trace data as personal measurements.
