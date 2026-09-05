"""
Empirical benchmark for Maximum Independent Set in Bipartite Graph
"""
import time
from algorithms.practice.network_flow_matching.max_independent_set_bip import solve_max_independent_set_bip

def benchmark_max_independent_set_bip():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_independent_set_bip([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_independent_set_bip()
    print(f"Maximum Independent Set in Bipartite Graph 100 iterations took {t*1000:.3f}ms")
