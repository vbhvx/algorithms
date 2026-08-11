"""
Empirical benchmark for Shortest Path to Get All Keys Bitmask BFS
"""
import time
from algorithms.practice.graphs_and_traversals.shortest_path_all_keys import solve_shortest_path_all_keys

def benchmark_shortest_path_all_keys():
    start = time.perf_counter()
    for _ in range(100):
        solve_shortest_path_all_keys([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_shortest_path_all_keys()
    print(f"Shortest Path to Get All Keys Bitmask BFS 100 iterations took {t*1000:.3f}ms")
