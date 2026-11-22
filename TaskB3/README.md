# B3 – Performance Under Stress and Attack (8 marks)

## B3.1 Delay/loss matrix
Use an isolated Linux lab host or NS-3. Linux examples (apply only to your own test interface):
```bash
sudo tc qdisc add dev <lab-interface> root netem delay 50ms
sudo tc qdisc change dev <lab-interface> root netem delay 150ms
sudo tc qdisc change dev <lab-interface> root netem delay 300ms
sudo tc qdisc change dev <lab-interface> root netem delay 50ms loss 1%
sudo tc qdisc change dev <lab-interface> root netem delay 50ms loss 5%
sudo tc qdisc change dev <lab-interface> root netem delay 50ms loss 10%
sudo tc qdisc del dev <lab-interface> root
```
Repeat iperf3 TCP and a controlled voice/RTP test at each setting. Restore qdisc after every test. Keep a table of TCP throughput, voice delay/jitter/loss.

## B3.2 TCP window
A1.2 gives BDP ≈10 MB for 1 Gbps and 80 ms RTT. A 64 KiB window limits throughput to about 6.55 Mbps. Compare iperf3 with a small socket window and a sufficiently large window on a controlled long-delay link; document actual negotiated window and measured rate.

## B3.3 Firewall and flood protection
Apply the corrected SSH allowlist/deny rules from A4 to a private lab VM. Verify trusted SSH succeeds, untrusted SSH fails, HTTPS remains accessible and default-denied services remain blocked. For rate limiting, use a controlled low-rate request generator against a local test server only; compare response time and accepted request count with and without the limit. Never use public targets or high-volume flood tools.

## B3.4 QoS trade-off
Strict priority (DiffServ EF) can keep voice delay low but may starve downloads if voice is unbounded. Weighted fair queuing reserves fair shares and protects other traffic but may add some voice delay under congestion. Prefer bounded strict priority for voice plus WFQ/CBWFQ for remaining classes; police voice to its engineered rate.

The included stress model is a safe analytical illustration, not a network attack or measured result.
