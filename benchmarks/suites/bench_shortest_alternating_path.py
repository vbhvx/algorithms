"""
Empirical benchmark for Shortest Path with Alternating Colors Dual BFS
"""
import time
from algorithms.practice.shortest_paths.shortest_alternating_path import solve_shortest_alternating_path

def benchmark_shortest_alternating_path():
    start = time.perf_counter()
    for _ in range(100):
        solve_shortest_alternating_path([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_shortest_alternating_path()
    print(f"Shortest Path with Alternating Colors Dual BFS 100 iterations took {t*1000:.3f}ms")
