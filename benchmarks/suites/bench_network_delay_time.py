"""
Empirical benchmark for Network Delay Time Dijkstra Broadcast
"""
import time
from algorithms.practice.shortest_paths.network_delay_time import solve_network_delay_time

def benchmark_network_delay_time():
    start = time.perf_counter()
    for _ in range(100):
        solve_network_delay_time([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_network_delay_time()
    print(f"Network Delay Time Dijkstra Broadcast 100 iterations took {t*1000:.3f}ms")
