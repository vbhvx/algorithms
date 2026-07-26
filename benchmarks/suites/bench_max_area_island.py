"""
Empirical benchmark for Max Area of Island DFS Component Size
"""
import time
from algorithms.practice.graphs_and_traversals.max_area_island import solve_max_area_island

def benchmark_max_area_island():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_area_island([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_area_island()
    print(f"Max Area of Island DFS Component Size 100 iterations took {t*1000:.3f}ms")
