"""
Empirical benchmark for Min Cost Max Flow SPFA Augmenting Paths
"""
import time
from algorithms.practice.network_flow_matching.min_cost_max_flow_spfa import solve_min_cost_max_flow_spfa

def benchmark_min_cost_max_flow_spfa():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_cost_max_flow_spfa([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_cost_max_flow_spfa()
    print(f"Min Cost Max Flow SPFA Augmenting Paths 100 iterations took {t*1000:.3f}ms")
