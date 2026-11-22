# A1 – Where Does the Delay Come From? (7 marks)

## A1.1 Delay breakdown
Packet size = 1,500 bytes = 12,000 bits. Link rate = 100 Mbps.
Transmission delay = 12,000 / 100,000,000 = 0.00012 s = **0.12 ms**.

Assume propagation speed in fibre = 2×10^8 m/s. Distance = 2,000 km = 2,000,000 m.
Propagation delay = 2,000,000 / (2×10^8) = **10 ms**.

Three routers each add 0.5 ms queuing and 0.1 ms processing:
- Queuing = 3×0.5 = **1.5 ms**
- Processing = 3×0.1 = **0.3 ms**

Total one-way delay = 0.12 + 10 + 1.5 + 0.3 = **11.92 ms** (assuming the 100 Mbps transmission occurs once and the stated distance is the total path distance; router forwarding transmission details are not separately added).

At 1 Gbps, transmission becomes 0.012 ms and total = **11.812 ms**. Improvement is only 0.108 ms (about 0.91%). Propagation and router queuing dominate, so upgrading bandwidth alone gives little latency improvement.

## A1.2 Bandwidth-delay product
BDP = 1 Gbps × 0.080 s = 80,000,000 bits = 10,000,000 bytes ≈ **10 MB** (decimal). A 64 KiB window holds 65,536 bytes = 524,288 bits. Maximum throughput = 524,288 / 0.08 = 6,553,600 bps ≈ **6.55 Mbps**, far below 1 Gbps. TCP window scaling or a larger receive window is required to fill the path.

## A1.3 Application targets (engineering targets, not universal guarantees)
| Application | One-way delay target | Jitter | Loss | Throughput target | Measurement |
|---|---:|---:|---:|---:|---|
| Live interactive video | <150 ms | <30 ms | <1% | 1–4 Mbps/stream | iperf3, ping, RTP/Wireshark |
| Voice | <150 ms | <20–30 ms | <1% | ~80 kbps/direction G.711 with headers | RTP analysis, ping |
| Recorded video | Buffering hides delay | Not critical | <1% after recovery | 3–8 Mbps/stream | iperf3, HTTP waterfall |
| E-mail | Seconds acceptable | Not critical | Reliable delivery | Low | Wireshark, SMTP logs |
| Large downloads | Not interactive | Not critical | TCP recovers | As high as available | iperf3, SNMP |

Active measurement injects probes/test traffic (ping, traceroute, iperf3); passive measurement observes existing traffic and counters (Wireshark, SNMP). Passive data can show actual throughput, packet loss/retransmissions visible in captures, flow delay if timestamps are reliable, and interface utilisation. It may miss unobserved paths, idle-time performance, one-way delay without clock synchronisation, and problems before users generate traffic. Active tests can detect degradation before a user complains but add test load.

## Evidence
Record actual ping/traceroute/iperf3 values under TaskB1. Do not replace them with the theoretical examples above.
