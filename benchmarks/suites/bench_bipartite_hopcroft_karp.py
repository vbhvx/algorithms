"""
Empirical benchmark for Hopcroft-Karp Maximum Bipartite Matching
"""
import time
from algorithms.practice.network_flow_matching.bipartite_hopcroft_karp import solve_bipartite_hopcroft_karp

def benchmark_bipartite_hopcroft_karp():
    start = time.perf_counter()
    for _ in range(100):
        solve_bipartite_hopcroft_karp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_bipartite_hopcroft_karp()
    print(f"Hopcroft-Karp Maximum Bipartite Matching 100 iterations took {t*1000:.3f}ms")
