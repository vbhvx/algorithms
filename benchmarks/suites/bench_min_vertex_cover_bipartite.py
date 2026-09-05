"""
Empirical benchmark for Konig Theorem Minimum Vertex Cover Bipartite
"""
import time
from algorithms.practice.network_flow_matching.min_vertex_cover_bipartite import solve_min_vertex_cover_bipartite

def benchmark_min_vertex_cover_bipartite():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_vertex_cover_bipartite([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_vertex_cover_bipartite()
    print(f"Konig Theorem Minimum Vertex Cover Bipartite 100 iterations took {t*1000:.3f}ms")
