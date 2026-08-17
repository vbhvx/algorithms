"""
Empirical benchmark for Shortest Path Visiting All Nodes Bitmask BFS
"""
import time
from algorithms.practice.shortest_paths.shortest_path_all_nodes import solve_shortest_path_all_nodes

def benchmark_shortest_path_all_nodes():
    start = time.perf_counter()
    for _ in range(100):
        solve_shortest_path_all_nodes([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_shortest_path_all_nodes()
    print(f"Shortest Path Visiting All Nodes Bitmask BFS 100 iterations took {t*1000:.3f}ms")
