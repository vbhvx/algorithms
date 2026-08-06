"""
Empirical benchmark for Is Graph Bipartite 2-Coloring BFS
"""
import time
from algorithms.practice.graphs_and_traversals.is_graph_bipartite import solve_is_graph_bipartite

def benchmark_is_graph_bipartite():
    start = time.perf_counter()
    for _ in range(100):
        solve_is_graph_bipartite([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_is_graph_bipartite()
    print(f"Is Graph Bipartite 2-Coloring BFS 100 iterations took {t*1000:.3f}ms")
