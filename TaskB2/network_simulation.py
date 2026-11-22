"""Deterministic queue/load model for the online-learning network case.
This is an analytical demonstration, not a measured Packet Tracer/NS-3 result.
"""
CASES = [
    ("baseline", 100, 20, 10, 2, False),
    ("lower bandwidth", 20, 50, 10, 2, False),
    ("more users", 20, 50, 50, 2, False),
    ("background download", 20, 50, 50, 2, True),
    ("voice priority", 20, 50, 50, 2, True),
]

def run(name, mbps, rtt_ms, users, voice_mbps, background):
    file_mbps = min(4.0 * users, mbps * 0.9) if background else 0.0
    voice_total = voice_mbps * min(users, 10) / 10
    offered = file_mbps + voice_total
    utilisation = min(1.0, offered / mbps)
    # Simple illustrative queue penalty rises sharply above 80% utilisation.
    queue_ms = max(0.0, utilisation - 0.8) * 100
    voice_delay = rtt_ms / 2 + 5 + queue_ms
    voice_loss = max(0.0, (offered / mbps - 1.0) * 100)
    file_throughput = max(0.0, min(file_mbps, mbps - voice_total))
    if name == "voice priority":
        voice_delay = rtt_ms / 2 + 5
        file_throughput = max(0.0, min(file_mbps, mbps - voice_total))
        voice_loss = 0.0 if voice_total < mbps else 100.0
    return utilisation*100, voice_delay, voice_loss, file_throughput

if __name__ == "__main__":
    for case in CASES:
        name, bw, rtt, users, voice, bg = case
        util, delay, loss, file_rate = run(*case)
        print(f"{name:22} util={util:5.1f}% voice_delay={delay:6.1f} ms "
              f"voice_loss={loss:5.1f}% file_rate={file_rate:5.1f} Mbps")
    print("Model outputs are illustrative; replace with simulator measurements in your report.")
