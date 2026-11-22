# B2 – Simulate Under Varying Conditions (5 marks)

Create a simple Packet Tracer or NS-3 model with one company server, internet/WAN link and one regional centre. Add one voice flow and one large file-download flow. Run at least these cases:
1. 100 Mbps, 20 ms link delay, 10 users
2. 20 Mbps, 50 ms delay, 10 users
3. 20 Mbps, 50 ms delay, 50 users
4. Case 3 plus background download
5. Case 4 with voice priority queue / QoS

Record configured bandwidth, delay, number of users, voice delay/jitter/loss and file throughput. The included Python model is a repeatable analytical approximation to compare offered load and queueing; it is not a substitute for a Packet Tracer/NS-3 run. For cross-simulator analysis, NS-3 can model packet-level queues and timing in detail; Packet Tracer is easier for device configuration and visual topology but provides less granular performance data.
