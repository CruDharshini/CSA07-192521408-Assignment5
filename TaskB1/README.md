# B1 – Measure a Real Network (7 marks)

## B1.1 RTT, jitter, loss and path
Run the commands at morning, afternoon and evening for three destinations (choose stable public endpoints or institution-approved servers):
```bash
ping -c 20 1.1.1.1
traceroute 1.1.1.1
ping -c 20 8.8.8.8
traceroute 8.8.8.8
ping -c 20 <third-approved-server>
traceroute <third-approved-server>
```
Windows equivalents: `ping -n 20 host` and `tracert host`. Save raw terminal output with date/time. RTT jitter can be approximated as mean absolute difference between consecutive RTT samples. Loss = lost probes / sent probes ×100%. Compare minimum RTT with propagation estimate 2×distance/signal speed; public routing distance and queueing mean geographic straight-line distance is only an approximation.

## B1.2 TCP/UDP throughput
On the receiving machine:
```bash
iperf3 -s
```
On sender, run on wired and wireless separately:
```bash
iperf3 -c <server-ip> -t 30
iperf3 -c <server-ip> -u -b 10M -t 30
iperf3 -c <server-ip> -R -t 30
```
Use a rate appropriate to the lab link; do not overload a shared network. Save complete output.

## B1.3 Wireshark
Capture an authorised voice/video call or a controlled RTP test. Use Telephony → RTP → RTP Streams → Analyze. Record packet count, sequence gaps/loss, inter-arrival jitter and bitrate. For the supplied sample trace, `trace_metrics.py` computes the expected metrics; it is a teaching trace, not a capture from your network.

## B1.4 Compare
Use A1.3 targets as the baseline. State which target is met, which fails, and a likely bottleneck. Evidence folder contains a blank table template; fill it with real observations.
