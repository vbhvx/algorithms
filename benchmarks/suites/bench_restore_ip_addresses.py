"""
Empirical benchmark for Restore IP Addresses Valid 4-Octet Split
"""
import time
from algorithms.practice.backtracking.restore_ip_addresses import solve_restore_ip_addresses

def benchmark_restore_ip_addresses():
    start = time.perf_counter()
    for _ in range(100):
        solve_restore_ip_addresses([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_restore_ip_addresses()
    print(f"Restore IP Addresses Valid 4-Octet Split 100 iterations took {t*1000:.3f}ms")
