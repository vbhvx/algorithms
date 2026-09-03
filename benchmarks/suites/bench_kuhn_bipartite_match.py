"""
Empirical benchmark for Kuhn Hungarian Algorithm Maximum Bipartite
"""
import time
from algorithms.practice.network_flow_matching.kuhn_bipartite_match import solve_kuhn_bipartite_match

def benchmark_kuhn_bipartite_match():
    start = time.perf_counter()
    for _ in range(100):
        solve_kuhn_bipartite_match([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kuhn_bipartite_match()
    print(f"Kuhn Hungarian Algorithm Maximum Bipartite 100 iterations took {t*1000:.3f}ms")
