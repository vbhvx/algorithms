"""
Empirical benchmark for Dinic Algorithm on Unit Networks Unit Capacities
"""
import time
from algorithms.practice.network_flow_matching.dinic_unit_networks import solve_dinic_unit_networks

def benchmark_dinic_unit_networks():
    start = time.perf_counter()
    for _ in range(100):
        solve_dinic_unit_networks([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_dinic_unit_networks()
    print(f"Dinic Algorithm on Unit Networks Unit Capacities 100 iterations took {t*1000:.3f}ms")
