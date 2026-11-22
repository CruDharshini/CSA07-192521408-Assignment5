"""Scale-up planning calculator. Enter measured values from B1/B2 before final use."""
def predict(current_users, current_peak_mbps, link_mbps, current_rtt_ms, regional_rtt_ms):
    doubled_load = current_peak_mbps * 2
    current_util = current_peak_mbps / link_mbps * 100
    doubled_util = doubled_load / link_mbps * 100
    approx_one_way_saving = max(0.0, (current_rtt_ms - regional_rtt_ms) / 2)
    print(f"Current users: {current_users}; doubled users: {2*current_users}")
    print(f"Current utilisation: {current_util:.1f}%")
    print(f"Predicted utilisation at doubled load: {doubled_util:.1f}%")
    print(f"Current measured RTT: {current_rtt_ms:.1f} ms")
    print(f"Regional measured RTT: {regional_rtt_ms:.1f} ms")
    print(f"Approximate one-way delay saving: {approx_one_way_saving:.1f} ms")
    if doubled_util > 80:
        print("Recommendation: upgrade capacity and apply QoS before doubling load.")
    else:
        print("Capacity headroom appears more comfortable; validate with peak-hour testing.")

if __name__ == "__main__":
    # Replace these placeholders with actual B1/B2 measurements.
    predict(current_users=1000, current_peak_mbps=300, link_mbps=1000,
            current_rtt_ms=220, regional_rtt_ms=60)
    print("Example only: substitute your measured values before submission.")
