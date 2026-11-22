# A5 – How Easy Is It to Take the Site Down? (4 marks)

## A5.1 SYN queue sizing
The server can hold 1,024 half-open connections, each retained for 60 seconds. A steady arrival rate of 1,024/60 = **17.07 half-open attempts per second** fills the queue in the idealised case. Real systems have SYN backlog policies, retransmissions and timeouts, so measure the actual host rather than treating this as a universal threshold.

SYN cookies avoid allocating full connection state when the SYN arrives. The server encodes state in its SYN-ACK sequence number and allocates the connection after a valid ACK returns. This reduces resource exhaustion from spoofed half-open connections, though it does not stop bandwidth saturation or all application-layer attacks.

DNS amplification uses spoofed source addresses and open recursive resolvers to send large responses to a victim. It is difficult for the victim to block because traffic arrives from many legitimate-looking DNS servers and can saturate the inbound link before the firewall can process it. Upstream filtering, response-rate limiting at resolvers, anti-spoofing and scrubbing are needed.

## A5.2 Protection plan
| Attack | Main protection | Supporting protection |
|---|---|---|
| SYN flood | SYN cookies, SYN backlog tuning | Connection rate limits, upstream DDoS protection |
| DNS amplification | Upstream scrubbing and provider filtering | DNS response-rate limiting, BCP38 anti-spoofing |
| HTTP request flood | CDN/WAF and application rate limiting | Caching, bot detection, autoscaling |

Four identical independent servers would raise the theoretical half-open queue capacity to 4×1,024 = 4,096; at a 60 s hold time, idealised fill rate is **68.27 SYN/s**. This is only four times the queue capacity, not a robust defence: distributed attacks can exceed it, and a shared network link can saturate first. Capacity expansion complements but does not replace SYN cookies and upstream DDoS mitigation.

## Safety
Never generate a flood against a public website or shared network. Use a local simulator or isolated lab with explicit permission.
