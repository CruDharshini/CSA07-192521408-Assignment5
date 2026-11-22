"""Metrics from the assignment's example packet trace."""
TRACE = [
    (1, 0, 42, 1200), (2, 20, 61, 1200), (3, 40, 85, 1200),
    (4, 60, None, 1200), (5, 80, 119, 1200), (6, 100, 146, 1200),
    (7, 120, 158, 1200), (8, 140, 190, 1200), (9, 160, None, 1200),
    (10, 180, 222, 1200),
]

def metrics(trace):
    total = len(trace)
    got = [(seq, tx, rx, size) for seq, tx, rx, size in trace if rx is not None]
    delays = [rx - tx for _, tx, rx, _ in got]
    loss = (total - len(got)) / total * 100 if total else 0.0
    avg_delay = sum(delays) / len(delays) if delays else 0.0
    jitter = (sum(abs(delays[i] - delays[i-1]) for i in range(1, len(delays))) /
              (len(delays)-1)) if len(delays) > 1 else 0.0
    elapsed_ms = got[-1][2] - trace[0][1] if got else 0.0
    received_bits = sum(size * 8 for _, _, _, size in got)
    throughput = received_bits / elapsed_ms if elapsed_ms > 0 else 0.0  # kbps: bit/ms
    return loss, avg_delay, jitter, throughput

if __name__ == "__main__":
    loss, delay, jitter, throughput = metrics(TRACE)
    print(f"packet loss {loss:.1f} %")
    print(f"average delay {delay:.1f} ms, jitter {jitter:.1f} ms")
    print(f"throughput {throughput:.1f} kbps")
    print("VoIP quality:", "acceptable" if delay < 150 and jitter < 30 and loss < 1 else "poor")
    clean = [row for row in TRACE if row[2] is not None]
    loss2, d2, j2, t2 = metrics(clean)
    print(f"Without the two lost packets: loss {loss2:.1f}%, delay {d2:.1f} ms, jitter {j2:.1f} ms, throughput {t2:.1f} kbps")
