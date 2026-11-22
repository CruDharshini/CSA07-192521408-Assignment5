"""Safe numerical illustration of delay/loss and application impact.
No packets are generated; use this to plan isolated-lab tests.
"""
import math

SETTINGS = [(50, 0), (150, 0), (300, 0), (50, 1), (50, 5), (50, 10)]
BASE_RTT_MS = 40
BASE_TCP_MBPS = 100
BASE_VOICE_JITTER_MS = 5

if __name__ == "__main__":
    for delay_ms, loss_pct in SETTINGS:
        rtt = BASE_RTT_MS + 2 * delay_ms
        # Illustrative Reno-like throughput trend; not a prediction for every TCP stack.
        loss_fraction = max(loss_pct / 100, 0.0001)
        tcp = min(BASE_TCP_MBPS, 1.22 * 1460 * 8 / (rtt / 1000 * math.sqrt(loss_fraction)) / 1e6)
        voice_loss = loss_pct
        voice_jitter = BASE_VOICE_JITTER_MS + delay_ms * 0.05
        print(f"added_delay={delay_ms:3}ms loss={loss_pct:2}% "
              f"estimated_RTT={rtt:3}ms illustrative_TCP={tcp:6.2f}Mbps "
              f"voice_jitter_est={voice_jitter:5.1f}ms voice_loss={voice_loss:2}%")
    print("Illustrative formula only. Replace estimates with iperf3 and RTP measurements.")
