"""
Empirical benchmark for Graph Valid Tree Cycle & Connectivity
"""
import time
from algorithms.practice.graphs_and_traversals.graph_valid_tree import solve_graph_valid_tree

def benchmark_graph_valid_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_graph_valid_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_graph_valid_tree()
    print(f"Graph Valid Tree Cycle & Connectivity 100 iterations took {t*1000:.3f}ms")
