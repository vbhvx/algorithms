"""
Empirical benchmark for Path with Minimum Effort Binary Search Dijkstra
"""
import time
from algorithms.practice.shortest_paths.path_minimum_effort import solve_path_minimum_effort

def benchmark_path_minimum_effort():
    start = time.perf_counter()
    for _ in range(100):
        solve_path_minimum_effort([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_path_minimum_effort()
    print(f"Path with Minimum Effort Binary Search Dijkstra 100 iterations took {t*1000:.3f}ms")
