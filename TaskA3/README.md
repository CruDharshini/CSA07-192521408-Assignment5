# A3 – Peer-to-Peer, VoIP and Overlays (5 marks)

## A3.1 Distribute a 4 GB package to 20 centres
Use decimal GB and Mbps: 4 GB = 32 Gbits.
**Client–server:** server must upload 20 copies = 640 Gbits. At 100 Mbps, lower bound = 640,000 Mbits / 100 Mbps = **6,400 s = 106.7 min**. Each centre's 50 Mbps download would take 640 s for one copy, so the server aggregate upload is the bottleneck.

**Peer-to-peer:** idealised fluid lower bound is max(F/u_server, N×F/(u_server + sum peer uploads), F/d_min). Here:
- F/u_server = 32,000 Mbits / 100 Mbps = 320 s
- N×F/(100 + 20×20 Mbps) = 640,000 / 500 = 1,280 s
- F/d_min = 32,000 / 50 = 640 s
Therefore **1,280 s = 21.3 min** is the ideal lower bound. This assumes every centre can upload 20 Mbps while downloading, all peers can exchange pieces efficiently, and no protocol/overhead/seed delay. P2P reduces the origin bottleneck. It may not win if clients are behind restrictive NATs, upload is unavailable/expensive, peers arrive late, or content integrity/security is not controlled.

## A3.2 G.711 voice
G.711 payload rate = 64 kbps. Packet interval = 20 ms, so 1/0.02 = **50 packets/s**. Payload per packet = 64,000×0.02/8 = 160 bytes. IP/UDP/RTP headers = 40 bytes. Total = 200 bytes × 8 × 50 = **80,000 bps = 80 kbps per direction** (ignoring link-layer, encryption, tunnelling and silence suppression). A 2 Mbps link can carry floor(2,000/80) = **25 calls per direction** theoretically; reserve capacity and allow for overhead/QoS, so practical capacity is lower. SIP establishes, modifies and terminates sessions; RTP carries real-time audio/video media.

## A3.3 Overlays and CDN
A CDN is an application overlay of distributed edge caches/servers on top of the internet; it reduces long-haul delay and origin-server load for recorded lectures and package downloads. A VPN is an encrypted logical tunnel overlay between users/sites; it protects traffic over untrusted networks but does not automatically reduce latency. CDN helps content distribution and global performance; VPN helps secure centre-to-company communication.
