"""
Empirical benchmark for Bipartite Edge Coloring Vizing Degree
"""
import time
from algorithms.practice.network_flow_matching.bipartite_edge_coloring import solve_bipartite_edge_coloring

def benchmark_bipartite_edge_coloring():
    start = time.perf_counter()
    for _ in range(100):
        solve_bipartite_edge_coloring([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_bipartite_edge_coloring()
    print(f"Bipartite Edge Coloring Vizing Degree 100 iterations took {t*1000:.3f}ms")
