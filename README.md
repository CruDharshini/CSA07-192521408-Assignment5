# CSA07 – Computer Networks | Assignment 5 (CO5)
**Student:** Dharshini | **Register No.:** 192521408  
**Department:** Information Technology | **Faculty:** Dr. Sivachandar K  
**Academic Year:** 2026–2027 | **Total:** 50 marks

**Topic:** Measuring Network Performance and Securing Applications

## Repository map
| Folder | Task |
|---|---|
| TaskA1 | Delay, bandwidth-delay product and measurement targets |
| TaskA2 | SMTP, POP3/IMAP, FTP/SFTP, SNMP, DNS and HTTP |
| TaskA3 | P2P distribution, VoIP and overlays |
| TaskA4 | TLS, firewall analysis and completed Python code |
| TaskA5 | SYN flood sizing and defensive plan |
| TaskB1 | Real-network measurement commands and completed trace-analysis code |
| TaskB2 | Repeatable network-condition simulator |
| TaskB3 | Safe stress-condition model, tc netem and firewall test guidance |
| TaskB4 | Scale-up prediction and engineering recommendation |
| Report | Consolidated written answers |

## Software
- Python 3 (standard library only)
- Wireshark, ping, traceroute, iperf3
- Linux `tc netem` and `iptables`/UFW where available
- Cisco Packet Tracer or NS-3 for network simulation

Record the exact OS, Python, Wireshark, iperf3 and simulator versions used on your own laptop. They are intentionally left as fields to fill after checking the installed versions.

## Run the supplied Python programs
```bash
python TaskA4/firewall_filter.py
python TaskB1/trace_metrics.py
python TaskB2/network_simulation.py
python TaskB3/stress_model.py
python TaskB4/scale_prediction.py
```
On Windows, use `py` if `python` is not recognised.

## Important evidence note
The analytical scripts and command templates are supplied. B1 measurements must be collected on the student's actual network at three times of day; B2 should be built/run in Packet Tracer or NS-3; B3 tests must remain inside an isolated lab or simulator. No real-network measurements, Wireshark captures, screenshots or .pkt files are claimed as completed here. Add the actual outputs to each task's `evidence/` directory after running them.

## Ethical testing
Do not run denial-of-service or flooding tests against public websites, campus networks or any third-party system. Use only a private isolated lab or a local simulator, with explicit permission.
