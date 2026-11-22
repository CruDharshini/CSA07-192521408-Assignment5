# B4 – Final Engineering Decision (5 marks)

## B4.1 Predict doubled users and overseas students
Use B1 measured RTTs and B2/B3 measured load response. For a first-order capacity estimate, if current peak active users = U and measured aggregate demand = R Mbps, doubling users without added capacity approximately doubles offered load to 2R. If current utilisation is already above 50%, the link may become congested. Queueing delay and loss can rise sharply near saturation; do not assume they merely double.

Overseas live classes add propagation delay. Estimate one-way propagation as path distance / 2×10^8 m/s for fibre and add measured routing/queuing delay. A regional media server/CDN can reduce RTT by serving from a closer edge; record current India RTT and regional-edge RTT, then improvement = (RTT_India − RTT_edge)/2 for an approximate one-way reduction.

## B4.2 Security check
At doubled load, verify normal HTTPS/DNS/approved mail traffic still passes, untrusted SSH remains denied, guest/user rate limits do not block legitimate bursts, and monitoring alerts are generated. Record before/after accepted request rate and latency. Do not run external attack tests.

## B4.3 Recommendation
Prioritise: (1) CDN/edge caching for recorded lectures and course packages; (2) regional media relays/servers for live classes in other continents; (3) QoS with bounded EF voice/video classes; (4) adequate WAN capacity based on measured peak and headroom; (5) stateful firewall, WAF, SYN cookies, upstream DDoS scrubbing and rate limits. Keep origin servers protected and replicate content securely. A regional server improves live delay but adds synchronisation, deployment and operational cost. Choose it if measured RTT reduction materially improves interactive sessions.
