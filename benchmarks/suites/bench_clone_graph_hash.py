"""
Empirical benchmark for Clone Graph Undirected Hash Map Traversal
"""
import time
from algorithms.practice.graphs_and_traversals.clone_graph_hash import solve_clone_graph_hash

def benchmark_clone_graph_hash():
    start = time.perf_counter()
    for _ in range(100):
        solve_clone_graph_hash([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_clone_graph_hash()
    print(f"Clone Graph Undirected Hash Map Traversal 100 iterations took {t*1000:.3f}ms")
