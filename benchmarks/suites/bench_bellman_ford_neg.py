"""
Empirical benchmark for Bellman Ford Shortest Path Negative Cycles
"""
import time
from algorithms.practice.shortest_paths.bellman_ford_neg import solve_bellman_ford_neg

def benchmark_bellman_ford_neg():
    start = time.perf_counter()
    for _ in range(100):
        solve_bellman_ford_neg([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_bellman_ford_neg()
    print(f"Bellman Ford Shortest Path Negative Cycles 100 iterations took {t*1000:.3f}ms")
