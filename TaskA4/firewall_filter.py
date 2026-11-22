"""First-match stateless firewall demonstration. Corrected SSH ordering."""
RULES = [
    ("allow", "tcp", 443, None),
    ("allow", "tcp", 22, "10.1."),
    ("deny", "tcp", 22, None),
    ("allow", "udp", 53, None),
]
DEFAULT = "deny"

def decide(proto, port, src):
    for action, rule_proto, dport, prefix in RULES:
        if (rule_proto == proto
                and (dport is None or dport == port)
                and (prefix is None or src.startswith(prefix))):
            return action
    return DEFAULT

packets = [
    ("tcp", 443, "49.37.2.8"),
    ("tcp", 22, "10.1.4.20"),
    ("tcp", 22, "49.37.2.8"),
    ("udp", 53, "10.1.4.20"),
    ("tcp", 80, "49.37.2.8"),
    ("icmp", None, "49.37.2.8"),
]

if __name__ == "__main__":
    for packet in packets:
        print(f"{packet[0]:<5} {str(packet[1]):<5} from {packet[2]:<10} -> {decide(*packet)}")
    print("\nSwap experiment: move the deny TCP/22 rule above the trusted 10.1. rule.")
    print("Then the trusted SSH packet is denied too, because first match wins.")
