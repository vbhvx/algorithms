"""
Empirical benchmark for As Far from Land as Possible Multi-Source BFS
"""
import time
from algorithms.practice.graphs_and_traversals.as_far_from_land import solve_as_far_from_land

def benchmark_as_far_from_land():
    start = time.perf_counter()
    for _ in range(100):
        solve_as_far_from_land([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_as_far_from_land()
    print(f"As Far from Land as Possible Multi-Source BFS 100 iterations took {t*1000:.3f}ms")
