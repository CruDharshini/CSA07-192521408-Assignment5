# A4 – Find the Hole in the Firewall (4 marks)

## A4.1 TLS
A certificate binds a public key to a domain identity, signed by a trusted CA; hostname, validity and trust chain must be checked. The TLS handshake negotiates protocol version, cipher suite, key agreement and session keys, and authenticates the server (and optionally the client). On café Wi-Fi an observer can generally see IP addresses, ports, timing, traffic volume and often DNS/SNI metadata depending on encryption features, but cannot read or alter authenticated HTTPS application content without defeating TLS or compromising an endpoint/certificate.

## A4.2 Firewall rules
Rules are evaluated top-to-bottom, first match wins. In the question's original list, rule 2 “allow TCP any → 22” shadows rule 3 “deny TCP any → 22” and rule 4 “allow TCP 10.1.0.0/16 → 22”. Rule 4 can never match because all TCP/22 traffic was already allowed by rule 2. The security hole is public SSH access. Correct order:
1. allow TCP 10.1.0.0/16 → 22
2. deny TCP any → 22
3. allow TCP any → 443
4. allow UDP any → 53 (only if this host is intended to provide DNS; restrict to required clients)
5. deny all any → any

Stateless filtering checks each packet independently and does not remember connection state. Stateful firewall tracks sessions and permits valid return traffic. Application proxy terminates and inspects application-layer requests (e.g. HTTP methods/URLs/content), offering deeper filtering at additional latency and processing cost.

The completed first-match program is in `firewall_filter.py`. Its included rules implement the corrected SSH order. The requested swap experiment is documented in its output/comments.
