"""
Empirical benchmark for Dinic Max Flow Level Graph Blocking Flow
"""
import time
from algorithms.practice.network_flow_matching.dinic_algorithm_flow import solve_dinic_algorithm_flow

def benchmark_dinic_algorithm_flow():
    start = time.perf_counter()
    for _ in range(100):
        solve_dinic_algorithm_flow([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_dinic_algorithm_flow()
    print(f"Dinic Max Flow Level Graph Blocking Flow 100 iterations took {t*1000:.3f}ms")
